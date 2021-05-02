

def game(a,b):

    if ((a == "piedra" and b == "tijera") or (a == "papel" and b == "piedra")
    or (a == "tijera" and b == "papel")):
        print ("Player one win")
    elif a == b:
        print("draw")
    else:
        print("Player two win")
