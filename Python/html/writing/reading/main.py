
def number_of_names(testoname):
    with open(testoname, "r") as file:
        list = file.read().split()
        counter= [0,0,0]
        for i in list:
            if i == "Lea":
                counter[0] +=1
            elif i == "Darth":
                counter[1] +=1
            elif i == "Luke":
                counter[2] +=1

        return counter


a = number_of_names("names.txt")
print("In total there is {Lea} times the Lea name, {Darth} times the Darth name,and {Luke} times the Luke name,".format(Lea = a[0], Darth=a[1], Luke=a[2]))
