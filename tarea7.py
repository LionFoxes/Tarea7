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



# Punto 3
cursos = {"Introducción a la Programación": [["Pepito Perez", "892324", 4.0],
["Rivaldo Rodriguez", "434335", 4.3],
["Novita Caicedo", "442565", 3.4],
["Manuela Beltran", "2323232", 4.1]], "Matemáticas": [["Pepito Perez", "892324", 4.0],
["Ruperto Gutierrez", "111335", 4.3],
["Lupita Gallego", "789232", 4.8],
["Novita Caicedo", "442565", 3.4]], "Humanidades": [["Eric Cartman", "343422", 2.0],
["Stan Marsh", "22999", 3.3],
["Novita Caicedo", "442565", 3.4]]}


def obtener_estudiantes(curso):
    ans = []
    for i in curso.values():
        for j in i:
            estudiantes = j[0]
            if estudiantes not in ans:
                ans.append(estudiantes)
    return ans


# print(obtener_estudiantes(cursos))


def estudiantes_en_comun(cursos, materia1, materia2):
    ans = []
    curso1 = cursos[materia1]
    curso2 = cursos[materia2]
    for i in curso1:
        estudiantes_curso1 = (i[0], i[1])
        for j in curso2:
            estudiantes_curso2 = (j[0], j[1])
            if estudiantes_curso1 == estudiantes_curso2:
                ans.append(estudiantes_curso1)
    return ans



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
