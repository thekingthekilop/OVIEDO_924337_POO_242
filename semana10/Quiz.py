class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

    def __repr__(self):
        return f"Coche(marca='{self.marca}', modelo='{self.modelo}', año={self.año})"

mi_coche = Coche("Toyota", "Corolla", 2022)

print(str(mi_coche))
print(repr(mi_coche)) 



class CuentaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de {monto} realizado con éxito.")
        
        else:
            print("El monto a depositar debe ser positivo.")



    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro de {monto} realizado con éxito.")
            
        else:
            print("Fondos insuficientes o monto inválido.")
            
    def mostrar_saldo(self):
        return f"El saldo actual es: {self.__saldo}"

cuenta = CuentaBancaria("Carlos")
cuenta.depositar(1000)
cuenta.retirar(500)

print(cuenta.mostrar_saldo())
