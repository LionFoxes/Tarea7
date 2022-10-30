"""
Catalina G.
tarea 6
"""
# Punto 1 #


def problema_11581(matri):
    count = -1
    while True:
        for i in range(len(matri)):
            c = 0
            for y in range(len(matri[i])):
                d = matri[i+1][c]
                a = matri[i][c + 1]
                e = matri[i][c]
                b = matri[i][c] + matri[i][c+1] + matri[i+1][c]
                if b // 2 == 0:
                    matri[i][c] = 1
                    c += 1
                    count += 1
                else:
                    matri[i][c] = 0
                    c += 1
        return count




print(problema_11581([[1,1,1], [1,0,0], [0,0,1]]))

# Punto 2 #


#def matrix(casos, taMatix, Matix, ):

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

# punto 5 #


def obtener_inversa(d):
    dic = {}
    for i in d:
        gllave = d[i]
        for j in gllave:
            a = j
            if j not in dic:
                dic[a] = [i]
            else:
                dic[a].append(i)
    return dic


#print(obtener_inversa({ 2 : [3, 7, 4, 1], 4 : [5, 1, 7], 6 : [], 11 : [2, 4, 8, 10, 1] }))


# Punto 6 #


def crear_matriz_dispersa(m):
    disp = {}
    for i in range(len(m)):
        for j in m[i]:
            y = m[j]
    return disp

"""
print(crear_matriz_dispersa([[1, 0, 0, 0, 0, 4, 0, 5],
[0, 0, 0, 0, 0, 0, 4, 7],
[2, 2, 0, 0, 9, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 8, 1, 0, 7, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[3, 0, 0, 0, 0, 6, 0, 2],
[4, 4, 7, 0, 0, 0, 0, 0],
[0, 9, 0, 8, 0, 7, 0, 6]]))
"""

# Punto 7 #



def organizar_palabras(cad):
    dic = {}
    c = cad.split()
    for i in range(len(c)):
        if c[i][0] not in dic:
            dic[c[i][0]] =[c[i]]
        else:
            dic[c[i][0]].append(c[i])
    return dic


#print(organizar_palabras("mi corazón encantado vibra por el polvo de esperanza y magia del universo que ambicionan todos poseer"))


