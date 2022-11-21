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
    cadena = set(cad.lower())
    c = set()
    ans = False
    for letras in cadena:
        if ord("a") <= ord(letras) <= ord("z") or letras == "ñ":
            c.add(letras)
            if 27 == len(c):
                ans = True
            else:
                ans = False
    return ans


# print(es_panagrama("abc  def g hi j k l m n O p q R s t u v w x y z ñ"))
# Punto 3
cursos = {"Introducción a la Programación": [["Pepito Perez", "892324", 4.0],
                                             ["Rivaldo Rodriguez", "434335", 4.3],
                                             ["Novita Caicedo", "442565", 3.4],
                                             ["Manuela Beltran", "2323232", 4.1]],
          "Matemáticas": [["Pepito Perez", "892324", 4.0],
                           ["Ruperto Gutierrez", "111335", 4.3],
                           ["Lupita Gallego", "789232", 4.8],
                           ["Novita Caicedo", "442565", 3.4]],
          "Humanidades": [["Eric Cartman", "343422", 2.0],
                          ["Stan Marsh", "22999", 3.3],
                          ["Novita Caicedo", "442565", 3.4]]}

""" a """


def obtener_estudiantes(curso):
    ans = []
    for i in curso.values():
        for j in i:
            estudiantes = j[0]
            if estudiantes not in ans:
                ans.append(estudiantes)
    return ans


# print(obtener_estudiantes(cursos))

""" b """


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


# punto 4
profCursos = {"Maestro Roshi": ["Introducción a la Programación", "Matemáticas"],
              "Maestro Kaiosama": ["Introducción a la Programación", "Estructuras de Datos", "Árboles y Grafos"],
              "Bills": ["Física Cuántica", "Análisis y Diseño de Algoritmos", "Diseño e Implementación de Algoritmos"]}

""" a """


def profesores_para_curso(diccionario_profesor_curso, materia):
    ans = []
    curso = diccionario_profesor_curso.values()
    profesores = diccionario_profesor_curso.keys()
    for materias in curso:
        for profe in profesores:
            for mater in materias:
                if materia == mater and profe not in ans:
                    ans.append(profe)

    return ans


# print(profesores_para_curso(profCursos, "Introducción a la Programación"))

""" b """


def estudiantes_con_profesor(cursos, diccionario_profesor_curso, profesor):
    ans = []
    for i in cursos.values():
        for j in i:
            estudiantes = j[0]
            for y in diccionario_profesor_curso[profesor]:
                for mate in cursos:
                    if y == mate and estudiantes not in ans:
                        ans.append(estudiantes)
    return ans


print(estudiantes_con_profesor(cursos, profCursos, "Maestro Roshi"))


# punto 5


def problem_13037(i, b1, b2, b3):
    print(f"Case #{i + 1}:")
    print(len(b1 - b2 - b3), len(b2.intersection(b3) - b1))
    print(len(b2 - b1 - b3), len(b1.intersection(b3) - b2))
    print(len(b3 - b2 - b1), len(b2.intersection(b1) - b3))


def grab_input():
    n = input()
    for i in range(int(n)):
        sizes = input().split(" ")
        b1 = set()
        b2 = set()
        b3 = set()
        flag = 1
        for j in range(3):
            chocolates = input().split(" ")
            for chocolate in chocolates:
                if flag == 1:
                    b1.add(int(chocolate))
                elif flag == 2:
                    b2.add(int(chocolate))
                elif flag == 3:
                    b3.add(int(chocolate))
            flag += 1
        problem_13037(i, b1, b2, b3)