from functools import reduce
import array as arr

# Diccionario inicial de biodiversidad
biodiversidad = {
    "Águila Real": ("animal", 5, "montañas"),
    "Roble": ("planta", 20, "bosques"),
    "Jaguar": ("animal", 2, "selva"),
    "Orquídea": ("planta", 50, "bosques"),
    "Tiburón Blanco": ("animal", 3, "océano"),
    "Delfín": ("animal", 10, "océano"),
    "Girasol": ("planta", 15, "bosques"),
}

print(biodiversidad)

# Actualizar la cantidad de una especie en el inventario.
def actualizar_cantidad(especie, nueva_cantidad):
    global biodiversidad
    biodiversidad[especie] = (biodiversidad[especie][0], nueva_cantidad, biodiversidad[especie][2])

# Cambiar el hábitat de una especie.
def cambiar_habitat(especie, nuevo_habitat):
    global biodiversidad
    biodiversidad[especie] = (biodiversidad[especie][0], biodiversidad[especie][1], nuevo_habitat)

# Listar especies por tipo ("animal" o "planta") utilizando programación funcional.
def listar_por_tipo(tipo):
    return list(filter(lambda especie: biodiversidad[especie][0] == tipo, biodiversidad))

# Calcular el total de individuos observados utilizando programación funcional.
def total_individuos():
    return reduce(lambda total, especie: total + biodiversidad[especie][1], biodiversidad, 0)

# Crear un arreglo con las cantidades observadas de todas las especies utilizando programación funcional.
cantidades = arr.array('i', list(map(lambda especie: biodiversidad[especie][1], biodiversidad)))

# Calcular y mostrar la cantidad promedio de individuos observados.
promedio = reduce(lambda acc, x: acc + x, cantidades) / len(cantidades)
print(f'Promedio: {promedio}')

 