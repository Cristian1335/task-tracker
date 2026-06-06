#Archivo creado para practicar la conversion de python a json, y viceversa, con el modulo json
import json

#diccionario de ejemplo
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
#creo un archivo "persona" en formato json
with open("persona.json","w") as arch:
    #.dump() convierte un objeto de python a json, y lo escribe en el archivo que le pase como segundo argumento
    json.dump(persona,arch,indent=4) #el indent es para que el json se vea mas bonito, con saltos de linea y espacios
    print("Archivo json creado")

#Ahora voy a leer el archivo json y convertirlo a un diccionario de python
with open("persona.json","r") as arch:
    #.load() convierte un json a un objeto de python, en este caso un diccionario
    datos_recuperados = json.load(arch) 

print("Datos recuperados del json:")
print(datos_recuperados)
