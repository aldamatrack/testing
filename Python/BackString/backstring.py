def wordmatching(list):

    a = list.rsplit()
    b = ""
    for i in range(len(a)):
        b = b + a[len(a)-i-1] + " "

    return b
