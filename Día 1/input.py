print(
    "Tu nombre es: "
    + input("Dime tu nombre:")
    + " y tu edad es: "
    + input("Dime tu edad:")
)

# ============================================================================
# RESUMEN DEL APRENDIZAJE - DÍA 1 (CONTINUACIÓN)
# ============================================================================
#
# En esta lección aprendimos a interactuar con el usuario usando input()
#
# 1. FUNCIÓN input()
#    - Pausa la ejecución y espera entrada del usuario
#    - Muestra un mensaje prompt para pedir el dato
#    - Devuelve SIEMPRE un string (texto), nunca un número
#    - Sintaxis: variable = input("Tu pregunta aquí:")
#
# 2. CÓMO FUNCIONA ESTE CÓDIGO
#    - input("Dime tu nombre:") → pide al usuario su nombre
#    - El resultado se concatena (+) con otros strings
#    - input("Dime tu edad:") → pide al usuario su edad
#    - Todo se imprime en una sola línea con print()
#
# 3. IMPORTANTE: TIPO DE DATO
#    - input() SIEMPRE devuelve string
#    - Si escribes 25, input devuelve "25" (texto, no número)
#    - Para operaciones matemáticas necesitarías convertir: int(input(...))
#
# 4. FLUJO DE EJECUCIÓN
#    1. Se ejecuta print()
#    2. Primera pausa en input() → espera respuesta del usuario
#    3. Se concatena el nombre
#    4. Segunda pausa en input() → espera edad
#    5. Se concatena la edad
#    6. Se imprime el resultado final
#
# EJEMPLO DE EJECUCIÓN
# Terminal:
#    Tu nombre es: Emmanuel
#    Tu nombre es: Emmanuel y tu edad es: 25
