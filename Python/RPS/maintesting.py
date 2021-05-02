from RPS import *

a= True
while a:
    Player1choice= input("Elige jugador 1: piedra, papel or tijera: ")
    Player2choice= input("Elige jugador 2: piedra, papel or tijera: ")
    game(Player1choice, Player2choice)
    Retry= input("Juegas otra?: yes or no: ")
    if Retry == "yes":
        pass
    else:
        print("Thanks for playing c: ")
        a= False
