############################################################

# ACTIVIDAD 05
# Pon un ejemplo de cómo pasar varios parámetros desde consola a un programa Python 3.
# Pon un ejemplo de cómo realizar “sobrecarga de funciones” (funciones que pueden recibir varios
# números de parámetros), incluyendo el caso de que el número de parámetros no sea definido.

import sys

# Obtener los argumentos de la línea de comandos
# El primer argumento (sys.argv[0]) es el nombre del script
script_name = sys.argv[0]
arguments = sys.argv[1:]

print(f"Nombre del script: {script_name}")
print(f"Argumentos proporcionados: {arguments}")

# Ejemplo para introducir por consola:  python3 mi_script.py arg1 arg2 arg3


# Python no admite la sobrecarga de funciones de la misma manera que algunos otros lenguajes,
# podemos utilizar argumentos opcionales y valores predeterminados para lograr algo similar:

def suma(*args):
        resultado = sum(args)
        return resultado

# Ejemplos de uso
resultado1 = suma(1, 2, 3)
print(f"Resultado 1: {resultado1}")

resultado2 = suma(1, 2, 3, 4, 5, 6, 7)
print(f"Resultado 2: {resultado2}")