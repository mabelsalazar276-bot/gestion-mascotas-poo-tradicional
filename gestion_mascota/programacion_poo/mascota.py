class Mascota:
    """Clase que representa la abstracción de una mascota."""

    def __init__(self, nombre, especie, edad):
        """Método constructor para inicializar los atributos."""
        self.nombre = nombre       # Atributo
        self.especie = especie     # Atributo
        self.edad = edad           # Atributo

    def mostrar_informacion(self):
        """Método para imprimir los datos de la mascota."""
        print(f"Mascota: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """Método para simular el sonido de la mascota."""
        especie_baja = self.especie.lower()
        if "perro" in especie_baja:
            sonido = "¡Guau Guau!"
        elif "gato" in especie_baja:
            sonido = "¡Miau Miau!"
        else:
            sonido = "un sonido nativo de su especie"
        print(f"{self.nombre} hace: {sonido}")
