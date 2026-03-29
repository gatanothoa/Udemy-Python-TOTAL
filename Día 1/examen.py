"""Examen de práctica - Día 1 (print, input, strings y escapes)."""


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
        print("Excelente. Dominas muy bien los fundamentos del Día 1.")
    elif porcentaje >= 70:
        print("Buen trabajo. Ya tienes una base sólida.")
    elif porcentaje >= 50:
        print("Vas bien, pero conviene repasar algunos conceptos clave.")
    else:
        print("Necesitas repasar Día 1 antes de avanzar al siguiente tema.")

    print("=" * 50)


def mini_reto():
    print("\nMini reto final (sin calificación automática)")
    print("Escribe un programa que haga esto:")
    print("1) Pida tu comida favorita con input().")
    print("2) Pida un color con input().")
    print('3) Imprima: "Tu plato especial es: <comida> <color>"')
    print("\nTip: usa concatenación con + y un espacio entre ambos datos.")


def main():
    print("=" * 50)
    print("EXAMEN DE PRÁCTICA - DÍA 1")
    print("Temas: print, input, strings, concatenación y escapes")
    print("=" * 50)

    nombre = input("\nEscribe tu nombre: ").strip()
    if not nombre:
        nombre = "Estudiante"

    print(f"\nHola, {nombre}. Comenzamos el examen.")

    puntaje = 0

    puntaje += preguntar_opcion(
        1,
        '¿Qué hace print("Hola")?',
        [
            ("a", "Pide un dato al usuario"),
            ("b", "Muestra texto en consola"),
            ("c", "Guarda datos en una variable"),
        ],
        "b",
    )

    puntaje += preguntar_opcion(
        2,
        '¿Cuál es el resultado de print("153" + "100")?',
        [
            ("a", "253"),
            ("b", "153 + 100"),
            ("c", "153100"),
        ],
        "c",
    )

    puntaje += preguntar_opcion(
        3,
        "¿Cuál es el resultado de print(153 + 100)?",
        [
            ("a", "153100"),
            ("b", "253"),
            ("c", "153 + 100"),
        ],
        "b",
    )

    puntaje += preguntar_opcion(
        4,
        "¿Qué secuencia de escape hace un salto de línea?",
        [("a", "\\n"), ("b", "\\t"), ("c", "\\\\")],
        "a",
    )

    puntaje += preguntar_opcion(
        5,
        "¿Qué secuencia de escape inserta una tabulación?",
        [("a", "\\n"), ("b", "\\t"), ("c", '\\"')],
        "b",
    )

    puntaje += preguntar_opcion(
        6,
        "¿Qué devuelve input() por defecto?",
        [
            ("a", "int"),
            ("b", "float"),
            ("c", "str"),
        ],
        "c",
    )

    puntaje += preguntar_texto(
        7,
        "Completa: input() siempre devuelve tipo...",
        {"str", "string"},
    )

    puntaje += preguntar_texto(
        8,
        "¿Qué operador se usa para concatenar strings en Python?",
        {"+", "mas", "signo +", "operador +"},
    )

    puntaje += preguntar_opcion(
        9,
        "¿Cuál imprime una barra invertida literal?",
        [
            ("a", 'print("\\\\")'),
            ("b", 'print("\\")'),
            ("c", 'print("/")'),
        ],
        "a",
    )

    puntaje += preguntar_opcion(
        10,
        '¿Qué línea imprime exactamente: Mi nombre es "Ana" ?',
        [
            ("a", 'print("Mi nombre es "Ana"")'),
            ("b", "print('Mi nombre es \"Ana\"')"),
            ("c", "print(\"Mi nombre es 'Ana'\")"),
        ],
        "b",
    )

    puntaje += preguntar_texto(
        11,
        'Si haces input() y escribes 25, el valor almacenado es 25 o "25"?',
        {'"25"', "25 como texto", "texto", "string"},
    )

    puntaje += preguntar_opcion(
        12,
        "En el mini proyecto del día, ¿qué se combina para crear el nombre final?",
        [
            ("a", "Ciudad + comida + edad"),
            ("b", "Personaje + animal + color"),
            ("c", "Mes + número + país"),
        ],
        "b",
    )

    mostrar_resultado(puntaje, 12)
    mini_reto()


if __name__ == "__main__":
    main()
