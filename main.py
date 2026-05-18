# Integrantes:
# -- Gordillo Diana
# -- Vidal Jostin
# -- Plaza Edison
# -- Chalen Camila

from clase_hija_1 import CuentaAhorro
from clase_hija_2 import Prestamo
from clase_extra_1 import Cliente
from clase_extra_2 import Sucursal


def generar_reporte(servicios: list):
    """Calcula de manera polimórfica los costos mensuales individuales y consolidados

    de los servicios provistos.
    """
    total_costos = 0
    for servicio in servicios:
        print(servicio)
        costo = servicio.calcular_costos()
        print(f"Costo asociado: {costo}")
        total_costos += costo
    print(f"Total de costos de todos los servicios: {total_costos}")


def main():
    """Flujo principal que actúa como el punto neurálgico de orquestación y

    ejecución de los modelos de objetos bancarios.
    """
    sucursal = Sucursal("Centro", "Guayaquil", 2010)
    cliente1 = Cliente("09487654321", "Luiz Perez", 2004)

    cuenta1 = CuentaAhorro("C001", cliente1.nombre, 2026, 1500.0, 0.03)
    prestamo1 = Prestamo("P001", cliente1.nombre, 2026, 5000.0, 5)
    cuenta2 = CuentaAhorro("C002", "Carlos Martinez", 2025, 3000.0, 0.04)

    print(sucursal)
    print(cliente1)
    print("-" * 30)

    lista_servicios = [cuenta1, prestamo1, cuenta2]

    generar_reporte(lista_servicios)


if __name__ == "__main__":
    main()
