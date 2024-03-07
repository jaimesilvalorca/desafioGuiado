from src.juego import start_game

def main():
    nombre_personaje = input("Por favor indique nombre de su personaje: ")
    start_game(nombre_personaje)

if __name__ == "__main__":
    main()
