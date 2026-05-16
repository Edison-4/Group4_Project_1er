# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

class Cliente:
    def __init__(self, identificacion, nombre, anio_nacimiento):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__anio_nacimiento = anio_nacimiento

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La identificación no puede estar vacía")
        self.__identificacion = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = valor

    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento

    @anio_nacimiento.setter
    def anio_nacimiento(self, valor):
        if valor <= 0:
            raise ValueError("El año de nacimiento debe ser mayor a cero")
        self.__anio_nacimiento = valor

    def __str__(self):
        return f"Cliente: {self.__nombre} - ID: {self.__identificacion}"

if __name__ == "__main__":
    cliente_prueba = Cliente("0987654321", "Luis Perez", 2004)
    print(cliente_prueba)