"""Examen de practica - Dia 2 (variables, tipos, operadores, conversiones y formato)."""


def normalizar(texto):
    return texto.strip().lower()


def preguntar_opcion(numero, enunciado, opciones, correcta):
    print(f"\nPregunta {numero}")
    print(enunciado)
    for clave, texto in opciones:
        print(f"  {clave}) {texto}")

    respuesta = normalizar(input("Tu respuesta: "))
    if respuesta == correcta:
        print("Correcto")
        return 1

    print(f"Incorrecto. Respuesta correcta: {correcta}")
    return 0


def preguntar_texto(numero, enunciado, respuestas_validas):
    print(f"\nPregunta {numero}")
    print(enunciado)
    respuesta = normalizar(input("Tu respuesta: "))

    if respuesta in respuestas_validas:
        print("Correcto")
        return 1

    ejemplo = ", ".join(sorted(respuestas_validas))
    print(f"Incorrecto. Respuesta esperada (ejemplo): {ejemplo}")
    return 0


def mostrar_resultado(puntaje, total):
    porcentaje = (puntaje / total) * 100
    print("\n" + "=" * 50)
    print(f"Resultado final: {puntaje}/{total} ({porcentaje:.1f}%)")

    if porcentaje >= 90:
        print("Excelente. Dominas muy bien los fundamentos del Dia 2.")
    elif porcentaje >= 70:
        print("Buen trabajo. Ya tienes una base solida.")
    elif porcentaje >= 50:
        print("Vas bien, pero conviene repasar algunos conceptos clave.")
    else:
        print("Necesitas repasar Dia 2 antes de avanzar al siguiente tema.")

    print("=" * 50)


def mini_reto():
    print("\nMini reto final (sin calificacion automatica)")
    print("Crea un programa que haga esto:")
    print("1) Pida nombre y apellido.")
    print("2) Pida el total vendido y convierta el dato a float.")
    print("3) Calcule comision del 13%.")
    print("4) Muestre un mensaje final usando f-strings.")


def main():
    print("=" * 50)
    print("EXAMEN DE PRACTICA - DIA 2")
    print("Temas: variables, tipos, operadores, conversiones, round y f-strings")
    print("=" * 50)

    nombre = input("\nEscribe tu nombre: ").strip()
    if not nombre:
        nombre = "Estudiante"

    print(f"\nHola, {nombre}. Comenzamos el examen.")

    puntaje = 0

    puntaje += preguntar_opcion(
        1,
        "Que tipo de dato es 3.14 en Python?",
        [("a", "int"), ("b", "float"), ("c", "str")],
        "b",
    )

    puntaje += preguntar_opcion(
        2,
        "Que operador se usa para potencia?",
        [("a", "**"), ("b", "//"), ("c", "%")],
        "a",
    )

    puntaje += preguntar_opcion(
        3,
        "Que operador devuelve solo la parte entera de una division?",
        [("a", "/"), ("b", "//"), ("c", "%")],
        "b",
    )

    puntaje += preguntar_opcion(
        4,
        "Cual es el resultado de 7 % 2?",
        [("a", "0"), ("b", "1"), ("c", "3")],
        "b",
    )

    puntaje += preguntar_opcion(
        5,
        "Que conversion necesitas para sumar 5 a un dato de input()?",
        [("a", "str()"), ("b", "float()"), ("c", "int()")],
        "c",
    )

    puntaje += preguntar_opcion(
        6,
        "Que funcion redondea numeros en Python?",
        [("a", "format()"), ("b", "round()"), ("c", "type()")],
        "b",
    )

    puntaje += preguntar_opcion(
        7,
        "Que resultado da round(10/3, 2)?",
        [("a", "3.33"), ("b", "3"), ("c", "3.333")],
        "a",
    )

    puntaje += preguntar_opcion(
        8,
        "Cual es la forma mas moderna de interpolar variables en texto?",
        [("a", "Concatenacion con +"), ("b", "format()"), ("c", "f-strings")],
        "c",
    )

    puntaje += preguntar_texto(
        9,
        "Completa: input() devuelve por defecto tipo...",
        {"str", "string"},
    )

    puntaje += preguntar_texto(
        10,
        "Si tienes texto '25' y quieres numero entero, que funcion usas?",
        {"int", "int()"},
    )

    puntaje += preguntar_texto(
        11,
        "Escribe el operador de modulo en Python.",
        {"%", "modulo", "operador %"},
    )

    puntaje += preguntar_opcion(
        12,
        "En el proyecto del Dia 2, cuanto es la comision de ventas?",
        [("a", "10%"), ("b", "13%"), ("c", "15%")],
        "b",
    )

    mostrar_resultado(puntaje, 12)
    mini_reto()


if __name__ == "__main__":
    main()
