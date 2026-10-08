# Alonso Lopez García NC = 0087
print("TIPOS DE FUNCIONES EN PYTHON")
print(" ")
print("Funciones Incorporadas (Built-in Functions)")
print(" ")
print("Ejemplo 1")
nombre = "Alonso"
print(nombre)

print(" ")
print("Ejemplo 2")
texto = "Python"
print(len(texto))

print(" ")
print("Ejemplo 3")
numero = 25
print(numero)

print(" ")
print("Ejemplo 4")
numeros = [10, 25, 5, 30]
print(max(numeros))

print(" ")
print("Ejemplo 5")
numeros = [10, 25, 5, 30]
print(min(numeros))

print(" ")
print("+-+-+-+-+-+-+-+-+-+-+-+")
print(" ")

print("Funciones Definidas por el Usuario")
print(" ")

print("Ejemplo 1")
def saludar():
    print("Hola, bienvenido")

saludar()

print(" ")
print("Ejemplo 2")
def sumar(a, b):
    print(a + b)

sumar(5, 3)

print(" ")
print("Ejemplo 3")
def mostrar_nombre(nombre):
    print("Mi nombre es", nombre)

mostrar_nombre("Alonso")

print(" ")
print("Ejemplo 4")
def calcular_area(base, altura):
    area = base * altura
    print("Área:", area)

calcular_area(10, 5)

print(" ")
print("Ejemplo 5")
def verificar_edad(edad):
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

verificar_edad(16)

print(" ")
print("Alonso López García NC = 0087")