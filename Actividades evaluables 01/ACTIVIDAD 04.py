############################################################

# ACTIVIDAD 04
# Explica con ejemplos cómo funcionan los operadores “is”, “not”, “in” en Python 3.

# El operador "is" se utiliza para verificar si dos objetos son el mismo objeto en memoria. 
# Compara las identidades de los objetos en lugar de sus valores.

a = 25
b = 25
c = a

print(a is b)  # True, a y b apuntan al mismo objeto
print(a is c)  # True, a y c apuntan al mismo objeto

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1


# El operador "not" se utiliza para negar una condición. Cambia el valor de verdad de una expresión lógica.

x = True
y = not x

print(y)  # False, ya que not True es False

# El operador "in" se utiliza para verificar si un valor está presente en una secuencia (como una lista, tupla, cadena, etc.).

coche = ['puerta', 'retrovisor', 'rueda']

print('puerta' in coche)  # True, 'puerta' está en la lista
print('llanta' in coche)  # False, 'llanta' no está en la lista