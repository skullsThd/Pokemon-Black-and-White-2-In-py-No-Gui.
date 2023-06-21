import time
import random
import numpy as np
from pygame import mixer

mixer.init()
mixer.music.load("musica/OS.mp3")

class Pokemon:
    def __init__(self, nome, tipo, mosse, stats, livello):
        self.nome = nome
        self.tipo = tipo
        self.mosse = mosse
        self.attacco = stats['ATTACCO']
        self.difesa = stats['DIFESA']
        self.livello = livello
        self.barre = livello * 10  # Aumenta la quantità di barre in base al livello
        self.salute = ""

classifica_clicked = False

def mostra_classifica():
    global classifica_clicked
    classifica_clicked = True
    print("\n--- CLASSIFICA ---")
    # Mostra la classifica dei giocatori

def prossima_battaglia():
    print("\nVuoi andare alla prossima battaglia?")
    scelta = input("[S]ì / [N]o: ")
    return scelta.upper() == "S"

def conferma_battaglia():
    print("Sei sicuro di voler iniziare la prossima battaglia?")
    scelta = input("[S]ì / [N]o: ")
    return scelta.upper() == "S"

def play_victory_music():
    mixer.music.load("musica/VICTORY.mp3")
    mixer.music.play()

def match(pokemon1, pokemon2):
    print(f"\n{pokemon1.nome}\tVS\t{pokemon2.nome}")
    print(f"Tipo: {pokemon1.tipo}\tVS\tTipo: {pokemon2.tipo}")
    print(f"Level: {pokemon1.livello}\tVS\tLevel: {pokemon2.livello}")

    while pokemon1.barre > 0 and pokemon2.barre > 0:
        print(f"{pokemon1.nome}\t\tPS\t{pokemon1.salute}")
        print(f"{pokemon2.nome}\t\tPS\t{pokemon2.salute}")

        print("\nScegli una mossa:\n")
        for i, mossa in enumerate(pokemon1.mosse):
            print(f"[{i + 1}]{mossa}\n")
        index = int(input("[?]: "))
        print(f"\n{pokemon1.nome} usa {pokemon1.mosse[index - 1]}!\n")

        # Determina il danno
        brutto_colpo = random.randint(0, 12)
        if brutto_colpo == 1:
            pokemon1.attacco += 4
            pokemon2.barre -= pokemon1.attacco
            pokemon2.salute = ""
            pokemon1.attacco -= 4
            print("\nBrutto colpo!\n\n")
        else:
            pokemon2.barre -= pokemon1.attacco
            pokemon2.salute = ""

            for j in range(int(pokemon2.barre + 0.1 * pokemon2.difesa)):
                pokemon2.salute += "="

        print(f"{pokemon1.nome}\t\tPS\t{pokemon1.salute}")
        print(f"{pokemon2.nome}\t\tPS\t{pokemon2.salute}")

        # Controlla se l'avversario è esausto
        if pokemon2.barre <= 0:
            print(f"\nIl {pokemon2.nome} nemico è esausto!")
            break

        soldi = np.random.choice([100, 200])
        print(f"\nL'avversario ha pagato ${soldi}.")

        # Visualizza l'attacco dell'avversario
        avversario_attacco = random.choice(pokemon2.mosse)
        print(f"Il {pokemon2.nome} nemico usa {avversario_attacco}!\n")

        # Verifica se il danno ha causato troppo danno al Pokémon
        if pokemon1.barre < 0.2 * pokemon1.livello:
            print(f"Il tuo {pokemon1.nome} è in pericolo di essere sostituito!")
            print("Vuoi cambiare Pokémon?\n")
            risposta = input("[S]ì / [N]o: ")
            if risposta.upper() == 'S':
                print("\nCambio del Pokémon in corso...\n")
                time.sleep(2)
                print("Vai, Pokémon successivo!\n")
                return False
            else:
                print(f"Il tuo Pokémon {pokemon1.nome} continua a combattere!\n")

        pokemon1.barre -= pokemon2.attacco
        pokemon1.salute = ""

        for _ in range(int(pokemon1.barre + 0.1 * pokemon1.difesa)):
            pokemon1.salute += "="

        print(f"{pokemon1.nome}\t\tPS\t{pokemon1.salute}")
        print(f"{pokemon2.nome}\t\tPS\t{pokemon2.salute}")

        # Controlla se il tuo Pokémon è esausto
        if pokemon1.barre <= 0:
            print(f"\nIl tuo {pokemon1.nome} è esausto!")
            break

    if pokemon1.barre > 0:
        print(f"\nIl tuo {pokemon1.nome} ha vinto la battaglia!")
        play_victory_music()
        return prossima_battaglia()
    else:
        print(f"\nIl {pokemon2.nome} nemico ha vinto la battaglia!")
        return False


pokemon1 = Pokemon("Pikachu", "Elettrico", ["Tuonopugno", "Tuonoshock", "Fulmine", "Codaferrea"], {"ATTACCO": 50, "DIFESA": 30}, 10)
pokemon2 = Pokemon("Charizard", "Fuoco", ["Lanciafiamme", "Artigliofuria", "Dragospiro", "Soffio Caldo"], {"ATTACCO": 70, "DIFESA": 50}, 10)

while True:
    if not classifica_clicked:
        print("--- MENU ---")
        print("1. Mostra Classifica")
        print("2. Inizia una Nuova Battaglia")
        print("3. Esci")
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            mostra_classifica()
        elif scelta == "2":
            if conferma_battaglia():
                if match(pokemon1, pokemon2):
                    break
            else:
                print("Battaglia annullata.")
        elif scelta == "3":
            break
        else:
            print("Scelta non valida. Riprova.")

    else:
        print("\n--- CLASSIFICA ---")
        # Mostra la classifica dei giocatori
        print("Classifica:")
        print("1. Giocatore 1")
        print("2. Giocatore 2")
        print("3. Giocatore 3")
        print("4. Torna al Menu")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "4":
            classifica_clicked = False
        else:
            print("Opzione non valida. Riprova.")
