from gessfuntion import *

start = True
randomNumber = provide()
counter = 1
while start:
    try:
        userChoice = input("Try to gest, give me a number: ")
        if userChoice == "exit":
            start = wannaKeep(userChoice)
        else:
            temp = gest(userChoice, randomNumber)
            if temp == "more" :
                counter = counter + 1
                print("Come on a little bit more")
            elif temp == "less":
                counter = counter + 1
                print("Come on a little bit less")
            else:

                print ("You GOT IT! It took you: {} tries to get the answer".format(counter))
                Final= input("Wanna keep playin?: yes or no: ")
                start = wannaKeep(Final)
                if Final == "yes":
                    randomNumber = provide()
                    counter = 0

    except ValueError:
        print ("Invalid entry, please provide a right entry ")
