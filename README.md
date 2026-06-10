Task Tracker CLI
Aplicación de línea de comandos para gestión de tareas personales, con persistencia de datos en archivo JSON.
Proyecto basado en el challenge de roadmap.sh.

Funcionalidades

Agregar tareas con nombre, descripción y estado
Actualizar descripción y estado de una tarea existente
Eliminar tareas por ID
Listar todas las tareas o filtrar por estado (to do, in progress, done)
Persistencia automática en tasks.json


Tecnologías

Python 3
Módulos estándar: json, datetime, sys


Uso
bash# Agregar una tarea
python main.py agregar "Nombre" "Descripción" "to do"

# Eliminar una tarea
python main.py eliminar <id>

# Actualizar una tarea
python main.py actualizar <id> "Nueva descripción" "in progress"

# Listar tareas
python main.py listar

Si se ejecuta sin argumentos, se muestra el menú de ayuda.


Estructura del proyecto
task-tracker/
├── main.py       # Lógica principal: clases Task y TaskManager
├── tasks.json    # Almacenamiento de tareas (se genera automáticamente)
└── .gitignore

Decisiones de diseño

POO: se utilizaron las clases Task y TaskManager para separar responsabilidades y evitar acoplamiento.
Patrones de diseño: se aplicaron principios básicos para mejorar la estructura y reducir redundancia:
    - Principio de Responsabilidad Única (SRP): cada clase tiene una responsabilidad definida — Task representa y serializa una tarea, TaskManager gestiona la colección y la persistencia.
Generación de IDs: se toma el último ID registrado y se incrementa en 1, garantizando unicidad incluso tras eliminaciones.
Manejo de errores: se contemplaron casos como archivo inexistente, ID no encontrado e inputs inválidos.

