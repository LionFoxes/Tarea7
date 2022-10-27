"""
Catalina G.
tarea 6
"""

# Punto 3 #


def bombear_cadena(cade, dic):
    ans = ""
    acum = ""
    c = list(cade)
    for x in c:
        for y in dic:
            if x in y:
                ans = y * dic[y]
                acum += ans
    return acum


# print(bombear_cadena("mmmnnpmnppqtr", {"r" : 10, "f" : 4, "c" : 2, "g" : 5}))


# Punto 4#


def traducir(d, frase):
    fr = frase.split(" ")
    ans = ""
    for x in fr:
        for j in d:
            if x in j:
                if x != fr[-1]:
                    ans += d[j]
                    ans += " "
                else:
                    ans += d[j]
    return ans


d = {"ojo": "eye", "otro": "another", "con": "with", "amigo": "friend", "eso": "that", "manito": "little hand"}

# print(traducir(d, "ojo con eso manito"))



