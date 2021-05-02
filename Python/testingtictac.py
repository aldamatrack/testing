import funtions
from TicTacToe import *
a = ["-","-","-"]
b = ["-","-","-"]
c = ["-","-","-"]
g = [a,b,c]

Play = input("Do you want to play?: yes or no ")
if Play == "yes":
    cuadro(g)
    a = True
    while a:
        for i in range(9):
            if i%2 == 0:
                player1=input("Player1 one is your turn please choose where to move: 11, 12, 13...")
                j=update(1,player1[1],player1[0],g)
                #print(player1[0] , player1[1])
                cuadro(j)
            else:
                player2=input("Player2 one is your turn please choose where to move: 11, 12, 13...")
                k = update(2,player2[1],player2[0],g)
                #print(player2[0] , player2[1])
                cuadro(k)
        Stillgaming = input("Wanna keep playing? yes or no: ")
        if Stillgaming == "yes":
            cuadro(g)
        else:
            a = False
            print("Thanks for playing :)")
if Play == "no":
    print("Too bad :c see yo soon")
