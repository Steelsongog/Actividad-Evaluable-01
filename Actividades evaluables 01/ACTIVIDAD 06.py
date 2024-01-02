############################################################

# ACTIVIDAD 06
# Crea un listado en el que cada elemento de esa lista sea una lista con dos valores: tamaño y peso.
# Utilizandohttps://docs.python.org/3/howto/sorting.htmly las “key functions”, hacer que esta lista
# se ordene por mayor altura y en caso de igualdad, por menor peso.
# Explica en comentarios que es realmente la “key function”.


# Lista de listas con tamaño y peso
lista_datos = [
    [180, 75],
    [160, 60],
    [175, 70],
    [180, 65],
    [160, 55]
]

# Explicación de la "key function":
# La "key function" se utiliza como argumento en la función sorted() o en otros métodos de ordenación en Python. 
# La función sorted() toma un iterable y opcionalmente una "key function",
# y devuelve una nueva lista ordenada según el criterio definido por la "key function".
# permitiendo que el usuario defina un criterio de ordenación personalizado. 


# Definición de la "key function"
def custom_key(item):
    # La "key function" devuelve una tupla (-tamaño, peso)
    # El tamaño se invierte negativamente para ordenar por mayor altura.
    # En caso de igualdad en altura, se ordena por menor peso.
    return -item[0], item[1]

# Utilizamos la función custom_key en la función sorted.
# sorted(iterable, key=key_function)
lista_ordenada = sorted(lista_datos, key=custom_key)

# Imprimir la lista original y la lista ordenada
print("Lista original:")
for dato in lista_datos:
    print(dato)

print("\nLista ordenada por mayor altura y menor peso:")
for dato in lista_ordenada:
    print(dato)