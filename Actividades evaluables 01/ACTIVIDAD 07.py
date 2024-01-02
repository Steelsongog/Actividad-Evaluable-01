############################################################

# ACTIVIDAD 07
# Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”.
# Crea un método imprimir, y además dos métodos que quieras.
# En segundo lugar, haz que el programa pida un número “n” por teclado y se creen “n” instancias de
# la clase, donde cada instancia:
# ● Cada "matricula" tendrá un número consecutivo desde 1 hasta "n".
# ● El “color” será para cada instancia un color aleatorio obtenido de este listado [“red”, “white”,
# “black”, “pink”, “blue”)
# Por último, el programa deberá imprimir los valores de las 10 primeras instancias. En caso de que
# "n" sea menor que 10, sólo imprimirá "n" instancias.
    
import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def metodo_1(self):
        print(f"El tamaño de instancias[] es: {len(instancias)}")

    def metodo_2(self):
        count_pink = sum(1 for car in instancias if car.color == "pink")
        print(f"Hay {count_pink} coches con color 'pink' en instancias[]")

# Solicitar un número "n" por teclado
        
n = int(input("Ingrese un número 'n': "))

# Crear "n" instancias de la clase Car
colores_disponibles = ["red", "white", "black", "pink", "blue"]
instancias = []

for i in range(1, n + 1):
    matricula = i
    color = random.choice(colores_disponibles)
    car = Car(matricula, color)
    instancias.append(car)

# Imprimir los valores de las 10 primeras instancias
print("\nValores de las primeras 10 instancias:")
for i in range (len(instancias)):
    instancias[i].imprimir()
    if i == 9:
        break


# Llamar al método metodo_1
instancias[0].metodo_1()

# Llamar al método metodo_2
instancias[0].metodo_2()
