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
    paragrama = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z"}
    solo_letras = set()  # Define un set vacio para guardar solo letras
    for l in cad:
        # cada letra se reprecentar con un numero lo que es el ordinal de las letras, cada una tiene un numero
        # y como esta de forma creciente se puede comparar cunts cuantos carateres hay y colocamos de la "a" a
        # la "z" y le agregamos la "ñ" ya que esta se encuentra en otro lugar
        if ord("a") <= ord(l) <= ord("z") or l == "ñ":  #
            solo_letras.add(l)  # Arma un set que contiene las letras -- elimina cualquier otro simbolo
    return len(paragrama) == len(solo_letras)  # Compara las longitudes, si ambas son iguales es que esta contenido


print(es_panagrama("Un jugoso zumo de piña y kiwi bien frio es exquisito y no lleva alcohol.".lower()))


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
