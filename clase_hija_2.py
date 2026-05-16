# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

from clase_base import ServicioBancario

class Prestamo(ServicioBancario):
    def __init__(self, codigo, titular, anio_apertura, monto, anios_plazo):
        super().__init__(codigo, titular, anio_apertura)
        self.__monto = monto
        self.__anios_plazo = anios_plazo

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        if valor <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__monto = valor

    @property
    def anios_plazo(self):
        return self.__anios_plazo

    @anios_plazo.setter
    def anios_plazo(self, valor):
        if valor <= 0:
            raise ValueError("El plazo debe ser mayor a cero")
        self.__anios_plazo = valor

    def calcular_costos(self):
        seguro_desgravamen = self.__monto * 0.01
        return seguro_desgravamen

    def __str__(self):
        return f"Prestamo: {self.titular} - Monto: {self.__monto} - Plazo: {self.__anios_plazo} anios"

if __name__ == "__main__":
    prestamo_prueba = Prestamo("P001", "Luiz Perez", 2026, 5000.0, 5)
    print(prestamo_prueba)
    print(prestamo_prueba.calcular_costos())