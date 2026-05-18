# Group4_Project
# Sistema de Gestión de Servicios Bancarios

**Integrantes:**
* Gordillo Diana
* Vidal Jostin
* Plaza Edison
* Chalen Camila

## Descripción del Proyecto
Este proyecto es una aplicación desarrollada en Python que simula la gestión básica de un sistema bancario utilizando los pilares de la **Programación Orientada a Objetos (POO)**. 

El sistema implementa:
* **Encapsulamiento:** Uso de atributos privados (ej. `__codigo`, `__saldo`) protegidos mediante decoradores `@property` (getters y setters) con validaciones de datos.
* **Herencia:** Creación de una clase padre (`ServicioBancario`) de la cual heredan clases hijas (`CuentaAhorro` y `Prestamo`) para reutilizar atributos y métodos comunes.
* **Polimorfismo:** Sobrescritura del método `calcular_costos()` en las clases hijas para aplicar lógicas de negocio distintas (mantenimiento fijo vs. porcentaje de seguro de desgravamen) dependiendo del tipo de servicio.
* **Clases Adicionales:** Modelado de entidades relacionadas como `Cliente` y `Sucursal` para complementar el ecosistema del banco.

---

## Diagrama de Clases

A continuación se presenta el diagrama estructural de las clases desarrolladas.

```mermaid
classDiagram
    class ServicioBancario {
        -String __codigo
        -String __titular
        -int __anio_apertura
        +codigo() String
        +titular() String
        +anio_apertura() int
        +calcular_costos() float
        +__str__() String
    }
    
    class CuentaAhorro {
        -float __saldo
        -float __tasa_interes
        +saldo() float
        +tasa_interes() float
        +calcular_costos() float
        +__str__() String
    }
    
    class Prestamo {
        -float __monto
        -int __anios_plazo
        +monto() float
        +anios_plazo() int
        +calcular_costos() float
        +__str__() String
    }
    
    class Cliente {
        -String __identificacion
        -String __nombre
        -int __anio_nacimiento
        +identificacion() String
        +nombre() String
        +anio_nacimiento() int
        +__str__() String
    }
    
    class Sucursal {
        -String __nombre
        -String __ciudad
        -int __anio_inauguracion
        +nombre() String
        +ciudad() String
        +anio_inauguracion() int
        +__str__() String
    }

    ServicioBancario <|-- CuentaAhorro : Hereda de
    ServicioBancario <|-- Prestamo : Hereda de
