

dictionary = {"allan":25, "karoly":24,"yes":10, "Carmen":60, "johanna":41 }

listnames = ""

for i in dictionary.keys():
    listnames += i + " "
print("Welcome we knoe the names of:"+ listnames)
a = input("which one would you like to know?: ")

print ("the age would be: ", dictionary.get(a))

#
#for i, j in dictionary.items():
#    print(i , j)
