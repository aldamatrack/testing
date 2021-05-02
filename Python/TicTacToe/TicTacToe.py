
a = ["-","-","-"]
b = ["-","-","-"]
c = ["-","-","-"]
g = [a,b,c]

def cuadro(h):
    a = h[0]
    b = h[1]
    c = h[2]
    for i in range(3):
        if i == 0:
            print ("   1   2   3 \n" )
            print ("1  {a}   {b}   {c} \n" .format(a = a[0], b= a[1], c=a[2]))
        elif i == 1:
            print ("2  {d}   {e}   {f} \n" .format(d = b[0], e= b[1], f=b[2]))
        else:
            print ("3  {g}   {h}   {i} \n" .format(g = c[0], h= c[1], i=c[2]))

def update(Player, X, Y, g):

    a = g[0]
    b = g[1]
    c = g[2]
    x = int(X)
    y = int(Y)

#Opciones para jugador 1
    if  Player == 1 and x == 1 and y == 1:
        print("testing")
        a[0] = "X"
    elif Player == 1 and x ==2 and y==1:
        a[1] = "X"
    elif Player == 1 and x ==3 and y==1:
        a[2] = "X"
    if Player == 1 and x ==1 and y==2:
        b[0] = "X"
    elif Player == 1 and x ==2 and y==2:
        b[1] = "X"
    elif Player == 1 and x ==3 and y==2:
        b[2] = "X"
    if Player == 1 and x ==1 and y==3:
        c[0] = "X"
    elif Player == 1 and x ==2 and y==3:
        c[1] = "X"
    elif Player == 1 and x ==3 and y==3:
        c[2] = "X"
#Opciones para jugador 2
    if Player == 2 and x ==1 and y==1:
        a[0] = "O"
    elif Player == 2 and x ==2 and y==1:
        a[1] = "O"
    elif Player == 2 and x ==3 and y==1:
        a[2] = "O"
    if Player == 2 and x ==1 and y==2:
        b[0] = "O"
    elif Player == 2 and x ==2 and y==2:
        b[1] = "O"
    elif Player == 2 and x ==3 and y==2:
        b[2] = "O"
    if Player == 2 and x ==1 and y==3:
        c[0] = "O"
    elif Player == 2 and x ==2 and y==3:
        c[1] = "O"
    elif Player == 2 and x ==3 and y==3:
        c[2] = "O"

    h=[a,b,c]
    #print(h)
    return h
