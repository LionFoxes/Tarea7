"""
Catalina G.
Tarea 6

Fecha: 30 / 10 / 2022
"""


# Punto 1 #

"""
En este programa hay varias cosas que no se han visto o en clase o que se han mencionado que no estan permitidas. 
En una función la instrucción return debe estar en la última línea y no debe estar dentro de ningún 
condicional ni nigún ciclo. Por cuestiones de estilo tampoco debería usarse los ciclos while como:

while True:

El programa podría cambiarse para que utilizando banderas el ciclo pare cuando necesites que pare. 
Realmente debo recomendarte que nunca uses while True:. Los doncionales en las asignaciones no han sido vistos en clase.
Tampoco se ha visto en clase definiciones dentro de definiciones ni la instrucción enumerate.

Esta solución está muy alejada de las cosas que se han visto en clase.
"""


def copiar_matriz(matri):
    ans = []
    for i in range(len(matri)):
        ans.append([])
        for j in range(len(matri)):
            ans[i].append(matri[i][j])
    return ans


def problema_11581(matri):
    count = -1
    orig = copiar_matriz(matri)
    siguiente = copiar_matriz(matri)
    while True:
        suma = 0
        for i in range(len(matri)):
            for j in range(len(matri[i])):
                suma += orig[i][j]

        if suma == 0:
            return count

        for i in range(len(matri)):
            for j in range(len(matri[i])):
                izquierda = orig[i - 1][j] if i != 0 else 0
                derecha = orig[i + 1][j] if i != len(matri[i]) - 1 else 0
                arriba = orig[i][j - 1] if j != 0 else 0
                abajo = orig[i][j + 1] if j != len(matri) - 1 else 0
                siguiente[i][j] = (izquierda + derecha + arriba + abajo) % 2
        orig = copiar_matriz(siguiente)
        count += 1


def leer_input():
    def leer_fila():
        s = input()
        s = list(s[:len(s)])
        for i, n in enumerate(s):
            s[i] = int(n)
        return s

    count = int(input())

    for i in range(count):
        matri = [leer_fila(), leer_fila(), leer_fila()]
        print(problema_11581(matri))


#leer_input()


# Punto 2 #
matri = [[1, 5, 7],
         [4, 2, 9],
         [6, 8, 3]]

"""
No es necesario definir varias veces una misma función. Las operaciones row y col deberían recibir los valores 
para a y b y no se reciben dichos valores por lo que no se sabe cuáles son 
las filas o columnas que se deben intercambiar.
"""

def copiar_m(m):
    ans = []
    for i in range(len(m)):
        ans.append([])
        for j in range(len(m)):
            ans[i].append(m[i][j])
    return ans


def row_a_b(m):
    ogri = copiar_matriz(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j == 0:
                m[j] = ogri[j + 1]
            else:
                m[j] = ogri[j - 1]
                return m


def col_a_b(m):
    ogri = copiar_matriz(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            abajo = ogri[i + 1][j]
            if i == 0:
                m[i][j+1] = abajo
            else:
                arriba = ogri[i - 3][j - 2]
    return m


def cambiar_col(m):
    for j in range(len(m[0])):
        for col1 in range(m):
            for col2 in range(m):
                m[col1][j], m[col2][j] = m[col2][j], m[col1][j]

#print(cambiar_col(matri))


def inc (m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] += 1
            if m[i][j] == 10:
                m[i][j] = 0
    return m


def dec (m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] -= 1
            if m[i][j] == -1:
                m[i][j] = 9
    return m


def transpose(m):
    n = 3
    start = 0
    for j in range(n):
        for i in range(start, n):
            m[i][start], m[start][i] = m[start][i], m[i][start]
        start += 1


transpose(matri)

# Punto 3 #

"""
La operación de multiplicación de cadenas no está permitida. 
No es necesario transformar la cadena cade a lista ya que las cadenas también se pueden recorrer. 
Este ejercicio funciona por casualidad ya que se hace algo que no es correcto pero que igual funciona. 
No debería recorrerse el diccionario y preguntar si cada letra está en alguna de las claves del diccionario; 
sería suficiente con verificar que cada letra sea una clave en el diccionario pero para esto no es necesario recorrer 
el diccionario.
"""

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

"""
Se comete un error similar al del ejercicio anterior. Se recorre sin necesidad el diccionario. Además, 
el condicional que está más interno que compara x con fr[-1] produciría resultados incorrectos si la palabra que está 
al final aparece varias veces en la frase.
"""

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


# print(obtener_inversa({ 2 : [3, 7, 4, 1], 4 : [5, 1, 7], 6 : [], 11 : [2, 4, 8, 10, 1] }))


# Punto 6 #
"""a"""

"""
Dado que se necesita el número de la columna debería recorrerse cada fila de la matriz con el for que utiliza range 
y no con el for que recorre cada elemento ya que eso hace necesario que se utilice la variable adicional y.
"""

def crear_matriz_dispersa(m):
    disp = {}
    count = 0
    for i in range(len(m)):
        y = -1
        for j in m[i]:
            y += 1
            if j != 0:
                if count not in disp:
                    disp[count] = [(y, j)]
                else:
                    disp[count].append([y, j])

        count += 1
    return disp

""" b """

"""
Se hace más trabajo del necesario ya que se recorren todas las claves de la matriz dispersa y esto no es necesario.
"""


def obtener_valor(disp, i, j):
    ans = 0
    count = 0
    for k in disp:
        for l in range(len(disp[k])):
            count += 1
            if l == i:
                for a in range(len(disp[i][l])):
                    a += 1
                    if a == j:
                        ans = count
    return ans
"""
print(obtener_valor({0 : [(0, 1), (5, 4), (7, 5)],
1 : [(6, 4), (7, 7)],
2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
4 : [(2, 8), (3, 1), (5, 7)],
6 : [(0, 3), (5, 6), (7, 2)],
7 : [(0, 4), (1, 4), (2, 7)],
8 : [(1, 9), (3, 8), (5, 7), (7, 6)]}, 1, 2))




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
            dic[c[i][0]] = [c[i]]
        else:
            dic[c[i][0]].append(c[i])
    return dic

# print(organizar_palabras("mi corazón encantado vibra por el polvo de esperanza y magia del universo que ambicionan todos poseer"))
