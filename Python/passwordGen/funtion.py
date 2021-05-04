import random as rn


def complexity(Choice):
    if Choice == "Strong":
        return Strong()
    elif Choice == "Medium":
        return Medium()
    else:
        return Low()

def Strong():
    temporally = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
    a = ""
    for i in range (16):
        a = a+ rn.choice(temporally)
    return a

def Medium():
    temporally = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
    a = ""
    for i in range (8):
        a = a+ rn.choice(temporally)
    return a

def Low():
    temporally = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
    a = ""
    for i in range(6):
        a = a+ rn.choice(temporally)
    return a
