"""
Catalina G.
Tarea 7

Fecha: 13 / 11 / 2022
"""

# Punto 1


def obtener_elementos(lis):
    ans = None
    a = set()
    b = set()
    for i in range(len(lis)):
        for j in lis[i]:
            if j in a:
                b.add(j)
            else:
                a.add(j)

    ans = list(b)
    return ans

# print(obtener_elementos([[2, 1, 8, 4], [1, 5, 3], [2, 6, 7], [8, 9]]))

# punto 2


def es_panagrama(cad):
    ans = False
    panagrama = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"}
    a = cad.split(" ")
    b = list(a)
    while b in panagrama:
        ans = True
    return ans
print(es_panagrama("Un jugoso zumo de piña y kiwi bien frio es exquisito y no lleva alcohol."))


# punto 5

def problem_13037(ntest, cantidadchoco, chocolatesLeju, chocolatesRony, chocolatesSujon):
    ans = ""
    Leju = [chocolatesLeju]
    Rony = [chocolatesRony]
    Sujon = [chocolatesSujon]
    while ntest != 0:
        for i in range(cantidadchoco):
            b = Leju[0] + Rony[0]
            if Leju[0] + Rony[0] + Sujon[0] == cantidadchoco:
                ans = 0
        ntest += -1

    return ans
# print(problem_13037(3, 2, 2, 8, 2, 2))
