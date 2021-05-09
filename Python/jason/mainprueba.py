import json
personal_dic = {"name": "ALLAN", "Novia:":"karoly", "programas": ["FMA", "SAO", "ATO"], "telefonos": {"casa": 22504425, "celular": 87186740, "trabajo": 8976}}

with open("prueba.json", "w") as p:
    json.dump(personal_dic, p)
