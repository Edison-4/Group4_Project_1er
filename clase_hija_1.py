# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

from clase_base import ServicioBancario

class CuentaAhorro(ServicioBancario):
    def __init__(self, codigo, titular, anio_apertura, saldo, tasa_interes):
        super().__init__(codigo, titular, anio_apertura)
        self.__saldo = saldo
        self.__tasa_interes = tasa_interes

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def tasa_interes(self):
        return self.__tasa_interes

    @tasa_interes.setter
    def tasa_interes(self, valor):
        self.__tasa_interes = valor

    def calcular_costos(self):
        mantenimiento = 5.0
        return mantenimiento

    def __str__(self):
        return f"Cuenta Ahorro: {self.titular} - Saldo: {self.__saldo}"

if __name__ == "__main__":
    cuenta_prueba = CuentaAhorro("C001", "Carlos Martinez", 2026, 1500.0, 0.03)
    print(cuenta_prueba)
    print(cuenta_prueba.calcular_costos())