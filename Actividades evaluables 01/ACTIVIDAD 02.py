############################################################

#  ACTIVIDAD 02

#  En Python 3 los tipos simples se pasan por valor y los compuestos por referencia.
# Crea un ejemplo con 3 funciones que:
# ● Reciba 2 números y devuelva la suma.

def suma_numeros(a, b):
    resultado = a + b
    return resultado

# ● Reciba una lista y modifique esa misma lista (referencia) doblando los valores de todos los elementos. No debe devolver nada.

def doblar_valores_en_sitio(lista):
    for i in range(len(lista)):
        lista[i] *= 2

# ● Reciba una lista y devuelva una copia de la lista misma lista (referencia) doblando los valores de todos los elementos. La lista original no debe modificarse.

def doblar_valores_copia(lista):
    lista_copia = lista.copy()  # Creamos una copia para no modificar la lista original
    for i in range(len(lista_copia)):
        lista_copia[i] *= 2
    return lista_copia