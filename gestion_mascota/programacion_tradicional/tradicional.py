def registrar_mascota():
    """Solicita los datos de la mascota por teclado y los devuelve en un diccionario."""
    print("--- Registro de Mascota (Enfoque Tradicional) ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
            
    return {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }

def mostrar_mascota(mascota):
    """Recibe el diccionario de la mascota y muestra su información organizada."""
    print("\n=================================")
    print("      INFORMACIÓN DE LA MASCOTA  ")
    print("=================================")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print("=================================\n")

if __name__ == "__main__":
    nueva_mascota = registrar_mascota()
    mostrar_mascota(nueva_mascota)
