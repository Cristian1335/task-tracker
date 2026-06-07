# task-tracker en CLI 

Task tracker aplicando persistencia de datos en un archivo JSON. El programa debe permitir al usuario agregar, actualizar, eliminar y listar tareas, así como marcar tareas como "en progreso" o "hecho". Cada tarea debe tener un nombre, una descripción, un estado (pendiente, en progreso o hecho) y una fecha de creación y actualización. Además utilizo mmanejo de errores, principios de POO para estructurar mejor las tareas y aplico patrones de diseño para mejorar las clases aplicadas y evitar acoplamiento y redundancia.
La generacion de id se hace mediante la deteccion del ultimo id registrado en la lista de tareas, al cual se le incrementa 1 unidad para generar el nuevo id, Esto garantiza que no se repitan id y que el sistema de identificación de tareas sea robusto y confiable, incluso después de eliminar tareas. 

Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks   
List all tasks that are done     
List all tasks that are not done 
List all tasks that are in progress 