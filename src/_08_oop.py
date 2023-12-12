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

class CuentaBancaria:
    def __init__(self, holder, initial_balance=0 ):
        # Private attributes
        self._balance = initial_balance
        self._holder = holder
        
    def deposit(self, amount):
        # Method to deposit money
        self._balance += amount
        print(f"Deposited {amount} units. Current balance: {self._balance} units.")
        
    def withdraw(self, amount):
        # Method to withdraw money
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self._balance} units.")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")
            
    def check_balance(self):
        # Method to view the current balance
        print(f"Current balance for account holder {self._holder}: {self._balance} units.")

# Example usage:
# Create an instance of the BankAccount class
account = CuentaBancaria(holder="John Doe", initial_balance=1000)

# Call methods to perform transactions
account.deposit(500)
account.withdraw(200)
account.check_balance()


# Ejercicio 4: Polimorfismo
# Crea una clase base Forma con un método area. Luego, crea dos clases derivadas, 
# Circulo y Cuadrado, que implementen el método area.


# Create a base class Shape with an area method. Then, create two derived classes,
# Circle and Square, that implement the area method.

class Forma:
    def area(self):
        # This method will be implemented by the derived classes
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # Implementation of the area method for Circulo
        return 3.14 * self.radio**2

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Implementation of the area method for Cuadrado
        return self.lado**2