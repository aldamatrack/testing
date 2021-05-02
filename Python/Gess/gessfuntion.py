from random import *
def gest(str, randomNumber):
    a = int(str)
    if a < randomNumber:

        return "more"
    elif a == randomNumber:

        return "success"
    else:

        return "less"

def wannaKeep(arg):
    if arg == "exit" or arg == "no":
        print("Too bad :c")
        return False

    else:
        return True


def provide():
    random = randrange(1,10,1)
    return random
