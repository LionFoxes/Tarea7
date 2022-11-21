"""
Catalina G
entrega 3 proyectos
06 / 11 / 2022
"""
# UP y DOWN significa a que dirección van si es UP entonces recorren la lista en valores positivos,
# Pero si es DOWN entonces ello recorren valores en negativo, la dirección
# Cuando esta SECOND, THIRD, FOURTH, FIFTH, SIXTH, SEVENTH, or OCTAVE, son las posiciones que se mueve la nota
# en la nota, los pasos


def problema_449(key, nota, direccion, pasos):  # key es la llave que tomamos para verificar el valor
    ans = ""  # nos guarda el valor final
    r = ""  # nos guarda la nota de los resultados
    n = list(nota)
    escala = ["C", "B#", "C#", "Db", "D", "D#", "Eb", "E", "Fb", "F", "E#", "F#", "Gb", "G", "G#", "Ab", "A", "A#",
              "Bb", "B", "Cb"]
    while key != " ":
        for i in range(len(escala)):
            keys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
            for j in range(len(keys)):
                paso = {"SECOND": escala[2], "THIRD": escala[3], "FOURTH": escala[4], "FIFTH": escala[5],
                        "SIXTH": escala[6], "SEVENTH": escala[7], "OCTAVE": escala[8]}
                for k in paso:
                    if keys[i] == "C":
                        if direccion == "UP":
                            if pasos == paso[k]:
                                if n == "#":
                                    ans = "Key of ", key, nota, ":", direccion, pasos, ">", r
                                elif n == "d":
                                    ans = "Key of ", key, nota, ":", direccion, pasos, ">", r
                                else:
                                    ans = "Key of ", key, nota, ":", direccion, pasos, ">", r

    return ans


print(problema_449("C", "F", "UP", "SECOND"))
