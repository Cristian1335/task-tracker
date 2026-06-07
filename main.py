import json 
import datetime
import sys
def Presentacion():
    print("Bienvenido al Task Tracker")
    print("Comandos disponibles:")
    print("1. 'agregar' <nombre> [descripcion] [estado]")
    print("2. 'eliminar' <id> de la tarea a eliminar")
    print("3. 'actualizar' <id> de tarea <descripcion> <estado>")
    print("4. 'listar' para ver todas las tareas o filtrar segun estado")

class Task:
    def __init__(self, id,name, description, status="to do", createdAt=None, updatedAt=None):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.createdAt = createdAt if createdAt else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = updatedAt if updatedAt else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.name} -- Descripcion: {self.description}\nEstado: {self.status}\nCreada el: {self.createdAt} \nActualizada el: {self.updatedAt}\n"
    
    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

class TaskManager:
    def __init__(self):
        self.tasks = [] #lista de tareas
        self.LoadTasks() #cargo las tareas al iniciar el programa
    
    def AddTask(self, name, description=None, status="to do", createdAt=None, updatedAt=None):
        if len(self.tasks) == 0:
            id = 1
        else:
            id = self.tasks[-1].id + 1 #sumo +1 al ultimo id de la lista
        newTask = Task(id, name, description, status, createdAt, updatedAt)
        self.tasks.append(newTask)
        self.SaveTasks() #guardo las tareas cada vez que agrego una nueva
        #print(f"Tarea {name} agregada") -- comentado, lo usaba para verificar que funcionaba.
    def GetTasks(self):
        for task in self.tasks:
            print(task)

    def LoadTasks(self):
        try:
            with open("tasks.json", "r") as archivo:
                tareas_guardadas = json.load(archivo)
                for item in tareas_guardadas:
                    tarea = Task(id=item["id"], name=item["name"], description=item["description"], status=item["status"], createdAt=item["createdAt"], updatedAt=item["updatedAt"])
                    self.tasks.append(tarea)
        except FileNotFoundError:
            pass #si no existe el archivo, no hace nada ya que la lista de tareas está vacía

    def UpdateTask(self, id, description, status): 
        for task in self.tasks:
            if task.id == id:
                task.description = description
                task.status = status
                task.updatedAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.SaveTasks() #guardo las tareas cada vez que actualizo una tarea
                #print(f"Tarea {task.name} actualizada") -- comentado, lo usaba para verificar que funcionaba.
                return
        #se ejecuta en caso de no encontrarla en el for
        print(f"No se encontró la tarea con id {id}")
    
    def DeleteTask(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                self.SaveTasks() #guardo las tareas cada vez que elimino una tarea
                #print(f"Tarea {task.name} eliminada") -- comentado, lo usaba para verificar que funcionaba.
                return
        print(f"No se encontró la tarea con id {id}")

    def SaveTasks(self):
        lista_a_guardar = [] #Creo una lista vacía para guardar las tareas convertidas a diccionario
        for task in self.tasks:
            tarea = task.convertir_a_diccionario() #recorro cada tarea y la convierto en diccionario
            lista_a_guardar.append(tarea)
        with open("tasks.json","w") as archivo:
            json.dump(lista_a_guardar, archivo, indent=4) #guardo la lista en un json
            #print("Tareas guardadas correctamente") -- comentado, lo usaba para verificar que funcionaba.

    def ListTasksByStatus(self, status):
        for task in self.tasks:
            if task.status == status:
                print(task)
def main(): 
    manager = TaskManager()
    
    if len(sys.argv) < 2:
        Presentacion()
        return
    else: 
        command = sys.argv[1] 
        match command: 
            case "agregar":
                if len(sys.argv) < 3:
                    print("Faltan argumentos para agregar una tarea. Uso: agregar <nombre> [descripcion] [estado]")
                    return
                name = sys.argv[2]
                description = sys.argv[3] if len(sys.argv) > 3 else None
                status = sys.argv[4] if len(sys.argv) > 4 else "to do"
                manager.AddTask(name, description, status)
                print("Tarea agregada")
            case "eliminar":
                if len(sys.argv) < 3:
                    print("Faltan argumentos para eliminar una tarea. Uso: eliminar <id>")
                    return
                try:
                    id = int(sys.argv[2])
                    manager.DeleteTask(id)
                    print("Tarea eliminada")
                except ValueError:
                    print("El ID debe ser un número entero.")
            case "actualizar":
                if len(sys.argv) < 5:
                    print("Faltan argumentos para actualizar una tarea. Uso: actualizar <id> <descripcion> <estado>")
                    return
                try: 
                    id = int(sys.argv[2])
                    description = sys.argv[3]
                    status = sys.argv[4]
                    manager.UpdateTask(id, description, status)
                    print("Tarea actualizada")
                except ValueError:
                    print("El ID debe ser un número entero.")
            case "listar":
                opcion = input("¿Desea listar todas las tareas [1] o por estado [2]?")
                match opcion:
                    case "1":
                        manager.GetTasks()
                    case "2":
                        estado = input("Ingrese el estado por el que desea filtrar las tareas (to do, in progress, done): ")
                        manager.ListTasksByStatus(estado)
                    case _:
                        print("Opción no válida.")
        
if __name__ == "__main__":
    main()                



