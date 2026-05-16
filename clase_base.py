# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

class ServicioBancario:
    def __init__(self, codigo, titular, anio_apertura):
        self.__codigo = codigo
        self.__titular = titular
        self.__anio_apertura = anio_apertura

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def anio_apertura(self):
        return self.__anio_apertura

    @anio_apertura.setter
    def anio_apertura(self, valor):
        self.__anio_apertura = valor

    def calcular_costos(self):
        pass

    def __str__(self):
        return f"{self.__codigo} - {self.__titular} - {self.__anio_apertura}"

if __name__ == "__main__":
    servicio_prueba = ServicioBancario("S001", "Luis Perez", 2024)
    print(servicio_prueba)