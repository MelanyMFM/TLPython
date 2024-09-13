#Crear un diccionario con especies, donde cada clave sea el nombre de la especie 
#y el valor una tupla con el tipo de especie, la cantidad observada y el hábitat principal. 
#Imprimir el diccionario.

biodiversidad = {
    "Águila Real": ("animal", 5, "montañas"),
    "Roble": ("planta", 20, "bosques"),
    "Jaguar": ("animal", 2, "selva"),
    "Orquídea": ("planta", 50, "bosques"),
    "Tiburón Blanco": ("animal", 3, "océano"),
    "Delfin": ("animal", 10, "océano"),
    "Girasol": ("planta", 15, "bosques"),
}

print(biodiversidad)
#Actualizar la cantidad de una especie en el inventario.
def actualizar_cantidad(especie, nueva_cantidad):
    global biodiversidad
    biodiversidad[especie] = (biodiversidad[especie][0], nueva_cantidad, biodiversidad[especie][2])

#Cambiar el hábitat de una especie.
def cambiar_habitat(especie, nuevo_habitat):
    global biodiversidad
    biodiversidad[especie] = (biodiversidad[especie][0], biodiversity[especie][1], nuevo_habitat)

#Listar especies por tipo ("animal" o "planta").
def listar_por_tipo(tipo):
    global biodiversidad
    especies_filtradas = [i for i in biodiversidad if biodiversidad[i][0] == tipo]
    return especies_filtradas

#Calcular el total de individuos observados.
def total_individuos():
    global biodiversidad
    total = sum([biodiversidad[i][1] for i in biodiversidad])
    return total

#Usa la biblioteca array para crear un arreglo con las cantidades observadas de todas las especies.
import array as arr
cantidades = arr.array('i', [biodiversidad[i][1] for i in biodiversidad])

#Calcula y muestra la cantidad promedio de individuos observados utilizando este arreglo.
promedio = sum(cantidades) / len(cantidades)
print(f'Promedio: {promedio}')