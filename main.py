#Task tracker aplicando el principio de responsabilidad única (SRP) y POO

class Task:
    def __init__(self, name, description, status, createdAt, updatedAt):
        self.name = name
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    def __str__(self):
        return f"Nombre: {self.name} Descripcion: {self.description}\nEstado: {self.status}\nCreada el: {self.createdAt} \nActualizada el: {self.updatedAt}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def AddTask(self, name, description, status, createdAt, updatedAt):
        newTask = Task(name, description, status, createdAt, updatedAt)
        self.tasks.append(newTask)
        print(f"Tarea {name} agregada")

    def GetTasks(self):
        for task in self.tasks:
            print(task)

    def UpdateTask(self, name, description, status, updatedAt): 
        for task in self.tasks:
            if task.name == name:
                task.description = description
                task.status = status
                task.updatedAt = updatedAt
                print(f"Tarea {name} actualizada")
            else:
                print(f"No se encontró la tarea {name}")
    
    def DeleteTask(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Tarea {name} eliminada")
            else: 
                print(f"No se encontró la tarea {name}")

manager = TaskManager()
manager.AddTask("Tarea 1", "Descripción de la tarea 1", "Pendiente", "2024-06-01", "2024-06-01")
manager.AddTask("Tarea 2", "Descripción de la tarea 2", "En progreso", "2024-06-02", "2024-06-02")
manager.GetTasks()

