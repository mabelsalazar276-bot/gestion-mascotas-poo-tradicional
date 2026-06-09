from mascota import Mascota

if __name__ == "__main__":
    print("--- Gestión de Mascotas (Enfoque POO) ---\n")
    
    mascota1 = Mascota("Max", "Perro", 3)
    mascota2 = Mascota("Luna", "Gato", 2)
    
    print("[Mascota 1]")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    print("-" * 40)
    
    print("[Mascota 2]")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
