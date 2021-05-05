from funtion import *

print("Lets play Cows or bulls :D ")
loop= True
while loop:
    diff= input("please choose the dificulty:\n\n hard, medium or easy: ")
    Computer = NumberCreation(diff)
    loop2=True
    counter = 0
    while loop2:
        counter +=1
        if diff == "hard" :
            user = input("Try to gess the number 6 digit number: ")
        elif diff == "medium" :
            user = input("Try to gess the number 4 digit number: ")
        elif diff == "easy" :
            user = input("Try to gess the number 2 digit number: ")
        a = CoworBull(Computer, user)
        if a[0] != len(user):
            print("With that choise you have {cow} cows and {bull} bulls".format(cow = a[0], bull = a[1]))
            print ("Is not over yet try again")
        else:
            print("Congratulation, you choose {u} and the answer was {c}, you tried {t} times to get the answer, you win".format(u=user, c=Computer, t = counter))
            print("Game over!!")
            loop2= False
            loop = False
