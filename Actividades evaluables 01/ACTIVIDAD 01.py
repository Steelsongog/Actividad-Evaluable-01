
############################################################

#● Actividad 1

#  Clonar una lista.
# ¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”?

original_list = [1, 2, 3, 4, 5]

#Utilizamos lo siguiente para clonar listas en Python.
import copy

# Shallow copy
shallow_copy = copy.copy(original_list)

# Deep copy
deep_copy = copy.deepcopy(original_list)

# Diferencia:
# Shallow copy crea una nueva lista, pero los objetos internos de la nueva lista son referencias a los objetos en la lista original. Cambios en los objetos internos afectarán ambas listas.
# Deep copy crea una nueva lista y objetos internos completamente independientes, evitando así que los cambios afecten a la lista original.



# ● Agregar un elemento a una lista.

my_list = [1, 2, 3]
my_list.append(4)  # Agrega al final
my_list.insert(1, 5)  # Inserta en la posición 1 (desplaza los elementos existentes)

# ● Quitar un elemento a una lista.

my_list = [1, 2, 3, 4]
my_list.remove(3)  # Elimina el valor 3
removed_element = my_list.pop(1)  # Elimina y devuelve el elemento en la posición 1

# ● Crear una lista nueva con los 4 últimos elementos de una lista.

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = original_list[-4:]  # Obtiene los últimos 4 elementos

# ● Convertir las palabras de una cadena (separadas por espacio) a una lista.

sentence = "Lorem ipsum arr"
word_list = sentence.split()  # Dividir la cadena por espacios en blanco

# ● Comentarios con una línea.

# Este es un comentario de una línea

# ● Comentarios multilínea.

"""
Este es un comentario
multilínea en Python.
Puede abarcar varias líneas
y se usa para descripciones extensas.
"""












