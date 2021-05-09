import json


def data(bd):
    a = json.load(bd)
    contador = 0
    b = ["enero","febrero","marzo", "abril","mayo", "junio", "julio", "agosto", "septiembre","octubre","noviembre", "diciembre"]
    c = [0,0,0,0,0,0,0,0,0,0,0,0]
    d = {}
    e={}
    for j in b:
        for i in a.values():
            if j in i and j=="enero":
                    c[0] += 1
            elif j in i and j=="febrero":
                c[1] += 1
            elif j in i and j=="marzo":
                c[2] += 1
            elif j in i and j=="abril":
                    c[3] += 1
            elif j in i and j=="mayo" :
                    c[4] += 1
            elif j in i and j=="junio":
                c[5] += 1
            elif j in i and j=="julio":
                c[6] += 1
            elif j in i and j=="agosto":
                c[7] += 1
            elif j in i and j=="septiembre":
                c[8] += 1
            elif j in i and j=="octubre":
                c[9] += 1
            elif j in i and j=="noviembre":
                c[10] += 1
            elif j in i and j=="diciembre":
                c[11] += 1
    for v in b:
        d[v] = c[contador]
        contador +=1
    e["lista"] = c
    e["meses"] = d
    return e
