class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        print(f"El rectangulo tiene como base {self.base} y altura {self.altura}")
              
figura = Rectangulo(15,20)
figura.calcular()

class FiguraGeometrica:
    def calcular_area(self):
        pass  # The method will be implemented in the subclasses

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado


triangulo = Triangulo(base=5, altura=8)
print(f"Área del triángulo: {triangulo.calcular_area()}")

cuadrado = Cuadrado(lado=4)
print(f"Área del cuadrado: {cuadrado.calcular_area()}")


class CuentaBancaria:
    def __init__(self, saldo_inicial=0.0):
        self.__saldo = saldo_inicial  

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.__saldo}")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.__saldo}")

# Example usage:
cuenta = CuentaBancaria(saldo_inicial=1000.0)
cuenta.consultar_saldo()  

cuenta.depositar(500.0)  
cuenta.retirar(200.0)   

cuenta.consultar_saldo()  # Output: Saldo actual: $1300.0


