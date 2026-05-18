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
```

## Evidencias de Ejecucion

### clase_base.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071000" src="https://github.com/user-attachments/assets/0e6fd250-e871-4803-95b8-9d4d5add07d6" />

### clase_hija_1.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071020" src="https://github.com/user-attachments/assets/c781cc31-92ea-4b3c-ac7c-e6d7a5e62866" />

### clase_hija_2.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071102" src="https://github.com/user-attachments/assets/dacdc4b4-6078-4d42-90a2-46568bc95c12" />

### clase_extra_1.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071142" src="https://github.com/user-attachments/assets/1aa7fd88-4ecf-42b0-bb54-a60a25cf5387" />

### clase_extra_2.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071239" src="https://github.com/user-attachments/assets/e8d43c65-d0a3-4024-888e-4249863a1f29" />

### main.py

<img width="1920" height="1080" alt="Captura de pantalla 2026-05-16 071342" src="https://github.com/user-attachments/assets/73131691-cb98-4507-b440-0242c589c9a0" />
