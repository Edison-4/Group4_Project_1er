# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

class Sucursal:
    def __init__(self, nombre, ciudad, anio_inauguracion):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__anio_inauguracion = anio_inauguracion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre de la sucursal no puede estar vacío")
        self.__nombre = valor

    @property
    def ciudad(self):
        return self.__ciudad

    @ciudad.setter
    def ciudad(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La ciudad no puede estar vacía")
        self.__ciudad = valor

    @property
    def anio_inauguracion(self):
        return self.__anio_inauguracion

    @anio_inauguracion.setter
    def anio_inauguracion(self, valor):
        if valor <= 0:
            raise ValueError("El año de inauguración debe ser mayor a cero")
        self.__anio_inauguracion = valor

    def __str__(self):
        return f"Sucursal {self.__nombre} ubicada en {self.__ciudad}"

if __name__ == "__main__":
    sucursal_prueba = Sucursal("Centro", "Guayaquil", 2010)
    print(sucursal_prueba)