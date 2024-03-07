from .models.personaje import Personaje
import random

def start_game(pj_nick):
    print("¡Bienvenido a Gran Fantasía!")
    player = Personaje(pj_nick)
    print(player)

    orco = Personaje("Orco")
    print(f"¡Oh no!, ¡Ha aparecido un {orco.get_name()}!")

    chance_to_win = player.chance_of_win(orco)
    print(f"Con tu nivel actual, tienes {chance_to_win}% de probabilidades de ganarle al {orco.get_name()}.")

    option = input("¿Qué deseas hacer? (1. Atacar, 2. Huir): ")

    while option == "1":
        result = atack(player, orco)
        print(result)
        option = input("¿Qué deseas hacer? (1. Atacar, 2. Huir): ")

    if option == "2":
        print("¡Has huido! El orco ha quedado atrás.")

def atack(player, orco):
    chance_to_win = player.chance_of_win(orco)
    result = random.uniform(0, 1)
    if result <= chance_to_win:
        player.win()
        return "¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!\n" + player.get_status() + orco.get_status()
    else:
        player.lose()
        return "¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n" + player.get_status() + orco.get_status()
