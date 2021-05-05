import random as rn

def NumberCreation(Dif):
    a = []

    if Dif == "hard":
        a= str(rn.randint(000000,999999))
        return a

    elif Dif == "medium":
        a= str(rn.randint(0000,9999))
        return a

    elif Dif == "easy":
        a= str(rn.randint(00,99))
        return a

def CoworBull(Computer, User):
    solution=[0,0]
    for i in range(len(Computer)):

        if Computer[i] == User[i] :
            solution[0]+=1
        else:
            for j in range(len(User)):
                if Computer[i] == User[j]:
                    solution[1]+=1

    return solution
