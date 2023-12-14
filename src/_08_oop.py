import math
# Ejercicios de POO en Python

# Ejercicio 1: Clase Libro
# Crea una clase `Libro` que tenga dos atributos: `titulo` y `autor`.
# Además, debe tener un método `mostrar_informacion` que imprima "Título: [titulo], Autor: [autor]".

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    


# Ejercicio 2: Herencia
# Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
# Luego crea una clase `Coche` que herede de `Vehiculo` y añade un atributo `cilindrada`.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Derived class for Car
class Coche(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        # Call the constructor of the base class (Vehiculo)
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
       
        

# Ejercicio 3: Encapsulación
# Crea una clase CuentaBancaria que tenga dos atributos privados:
# _saldo y _titular. Implementa métodos para depositar y retirar dinero, 
# además de un método para ver el saldo actual.

# Create a class BankAccount that has two private attributes:
# _balance and _holder. Implement methods to deposit and withdraw money,
# as well as a method to view the current balance.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            return True
        else:
            return False

    def retirar(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            return True
        else:
            return False

    def ver_saldo(self):
        return self._saldo

    
# Example usage:
# Create an instance of the BankAccount class
account = CuentaBancaria(titular="John Doe", saldo_inicial=1000)
assert account.depositar(500) == True  # Check deposit

# Call methods to perform transactions
account.depositar(500)
account.retirar(200)
account.ver_saldo()


# Ejercicio 4: Polimorfismo
# Crea una clase base Forma con un método area. Luego, crea dos clases derivadas, 
# Circulo y Cuadrado, que implementen el método area.

# Create a base class Shape with an area method. Then, create two derived classes,
# Circle and Square, that implement the area method.

class Forma:
    def area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2
    
    def make_resizable(self):
        def resize(new_size):
            self.radio = new_size
        
        self.resize = resize

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2 
    