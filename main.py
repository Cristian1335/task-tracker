import json 
import datetime

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
    
    def AddTask(self, name, description, status="to do", createdAt=None, updatedAt=None):
        if len(self.tasks) == 0:
            id = 1
        else:
            id = self.tasks[-1].id + 1 #sumo +1 al ultimo id de la lista
        newTask = Task(id, name, description, status, createdAt, updatedAt)
        self.tasks.append(newTask)
        self.SaveTasks() #guardo las tareas cada vez que agrego una nueva
        print(f"Tarea {name} agregada")

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
                print(f"Tarea {task.name} actualizada")
                return
        #se ejecuta en caso de no encontrarla en el for
        print(f"No se encontró la tarea con id {id}")
    
    def DeleteTask(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                self.SaveTasks() #guardo las tareas cada vez que elimino una tarea
                print(f"Tarea {task.name} eliminada")
                return
        print(f"No se encontró la tarea con id {id}")

    def SaveTasks(self):
        lista_a_guardar = [] #Creo una lista vacía para guardar las tareas convertidas a diccionario
        for task in self.tasks:
            tarea = task.convertir_a_diccionario() #recorro cada tarea y la convierto en diccionario
            lista_a_guardar.append(tarea)
        with open("tasks.json","w") as archivo:
            json.dump(lista_a_guardar, archivo, indent=4) #guardo la lista en un json
            print("Tareas guardadas correctamente")

    def ListTasksByStatus(self, status):
        for task in self.tasks:
            if task.status == status:
                print(task)

manager = TaskManager()
#manager.AddTask("Tarea 1", "Descripción de la tarea 1", "Pendiente")
#manager.AddTask("Tarea 2", "Descripción de la tarea 2", "En progreso", "2024-06-02", "2024-06-02")
manager.GetTasks()
#manager.DeleteTask(5)

