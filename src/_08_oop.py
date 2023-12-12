import math
# Ejercicios de POO en Python

# Ejercicio 1: Clase Libro
# Crea una clase `Libro` que tenga dos atributos: `titulo` y `autor`.
# Además, debe tener un método `mostrar_informacion` que imprima "Título: [titulo], Autor: [autor]".

class Libro:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        
    def mostrar_informacion(self):
        print(f"Title: {self.title}, Author: {self.author}")
    pass

my_book = Libro(title="Divae SHams" , author="Rumi")
my_book.mostrar_informacion()

# Ejercicio 2: Herencia
# Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
# Luego crea una clase `Coche` que herede de `Vehiculo` y añade un atributo `cilindrada`.

class Vehiculo:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        pass

class Coche(Vehiculo):
    def __init__(self, brand, model, cylander_capacity):
        super().__init__(brand, model)
        self.cylander_capacity = cylander_capacity
        

# Ejercicio 3: Encapsulación
# Crea una clase CuentaBancaria que tenga dos atributos privados:
# _saldo y _titular. Implementa métodos para depositar y retirar dinero, 
# además de un método para ver el saldo actual.

# Create a class BankAccount that has two private attributes:
# _balance and _holder. Implement methods to deposit and withdraw money,
# as well as a method to view the current balance.

# --------------------------------------------------
# YOU CODE HERE
# ---------------------------------------------------


# Ejercicio 4: Polimorfismo
# Crea una clase base Forma con un método area. Luego, crea dos clases derivadas, 
# Circulo y Cuadrado, que implementen el método area.


# --------------------------------------------------
# YOU CODE HERE
# ---------------------------------------------------