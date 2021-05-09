import json

with open("prueba.json","r") as pj:

    a = json.load(pj)



    for i in a["telefonos"].keys():
        print(i)
