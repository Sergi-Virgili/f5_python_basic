import math
# Ejercicios de POO en Python

# Ejercicio 1: Clase Libro
# Crea una clase `Libro` que tenga dos atributos: `titulo` y `autor`.
# Además, debe tener un método `mostrar_informacion` que imprima "Título: [titulo], Autor: [autor]".

class Libro:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        
    def show_information(self):
        print(f"Title: {self.title}, Author: {self.author}")
    pass

my_book = Libro(title="Divae SHams" , author="Rumi")

my_book.show_information()

# Ejercicio 2: Herencia
# Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
# Luego crea una clase `Coche` que herede de `Vehiculo` y añade un atributo `cilindrada`.


# --------------------------------------------------
# YOU CODE HERE
# ---------------------------------------------------


# Ejercicio 3: Encapsulación
# Crea una clase CuentaBancaria que tenga dos atributos privados:
# _saldo y _titular. Implementa métodos para depositar y retirar dinero, 
# además de un método para ver el saldo actual.


# --------------------------------------------------
# YOU CODE HERE
# ---------------------------------------------------


# Ejercicio 4: Polimorfismo
# Crea una clase base Forma con un método area. Luego, crea dos clases derivadas, 
# Circulo y Cuadrado, que implementen el método area.


# --------------------------------------------------
# YOU CODE HERE
# ---------------------------------------------------