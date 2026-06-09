from mascota import Mascota

def main():
    print("--- Creando Objetos (POO) ---\n")
    
    mascota1 = Mascota("Firulais", "Perro", 3)
    
    mascota2 = Mascota("Michi", "Gato", 2)
    
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

if __name__ == "__main__":
    main()