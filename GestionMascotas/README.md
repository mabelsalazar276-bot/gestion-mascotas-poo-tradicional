# Sistema de Gestión de Mascotas

Este repositorio contiene la solución a la tarea de gestión de mascotas implementada bajo dos metodologías de desarrollo de software: **Programación Tradicional (Estructurada)** y **Programación Orientada a Objetos (POO)**.

## Datos del Estudiante
* **Nombre Completo:** Mabela del Cisne Salazar Ren
* **Asignatura:** Programacion Orientada a Objetos
* **Lenguaje utilizado:** Python 3

---

## Descripción de los Programas

### 1. Programación Tradicional (`programacion_tradicional/`)
Solución estructurada basada puramente en variables locales y funciones jerárquicas. Solicita los datos de la mascota (`Nombre`, `Especie`, `Edad`) a través del teclado, procesa la información y la imprime en consola de forma organizada sin recurrir a estructuras complejas de clases.

### 2. Programación Orientada a Objetos (`programacion_poo/`)
Solución modular dividida en dos archivos principales:
* `mascota.py`: Modela la plantilla conceptual (**Clase**) de la mascota utilizando principios de abstracción, encapsulando sus características (**Atributos**) y comportamientos (**Métodos**).
* `main.py`: Punto de entrada del programa donde se instancian y manipulan múltiples **Objetos** de la clase `Mascota`.

---

## Reflexión: Diferencias entre Programación Tradicional y POO

1. **Organización del Código:** En la programación tradicional, los datos y las funciones que los manipulan están completamente separados. En cambio, en la POO, los datos (atributos) y los comportamientos (métodos) coexisten de forma unificada dentro de un objeto, facilitando el orden lógico.
2. **Escalabilidad:** Si el sistema de gestión de mascotas necesitara crecer (por ejemplo, agregar citas médicas o vacunas), la solución estructurada tradicional se volvería compleja de mantener debido al flujo de variables. Con la POO, expandir funciones es natural mediante la adición de nuevos métodos o el uso de la herencia.
3. **Reutilización:** La POO destaca por permitir crear infinitas instancias independientes (mascotas) a partir de un solo molde conceptual (Clase), mientras que el enfoque tradicional requiere estructurar colecciones manuales de variables para no sobreescribir la información.
