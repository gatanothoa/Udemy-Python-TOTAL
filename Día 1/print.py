print("Hola Mundo")
print("153 + 100 ")
print("Hola" + " " + "Mundo")
print("153" + "100")
print("Mi nombre es 'Emmanuel'")
print('Mi nombre es "Emmanuel"')
print("Mi nombre es\nEmmanuel")
print("Mi nombre es\tEmmanuel")
print("Esta es una barra invertida \\")

# ============================================================================
# RESUMEN DEL APRENDIZAJE - DÍA 1
# ============================================================================
#
# En esta lección exploramos la función print() de Python y aprendimos:
#
# 1. FUNCIÓN PRINT() BÁSICA
#    - Mostrar texto en la consola
#    - print("Hola Mundo") → salida: Hola Mundo
#
# 2. DIFERENCIA ENTRE TEXTO Y OPERACIONES MATEMÁTICAS
#    - print("153 + 100") → muestra el texto literal
#    - Para calcular: print(153 + 100) → muestra: 253
#
# 3. CONCATENACIÓN DE STRINGS
#    - Usar el operador (+) para unir textos
#    - print("Hola" + " " + "Mundo") → Hola Mundo
#    - IMPORTANTE: Los números como strings se concatenan, no se suman
#    - print("153" + "100") → 153100 (no 253)
#
# 4. CARACTERES DE ESCAPE (Secuencias especiales)
#    - \" = Comillas dobles dentro de un string
#    - \' = Comillas simples dentro de un string
#    - \n = Salto de línea (nueva fila)
#    - \t = Tabulación (espacios de indentación)
#    - \\ = Barra invertida literal
#
# 5. CONCEPTO IMPORTANTE
#    Python interpreta los caracteres de escape y los convierte en su
#    acción correspondiente. Si necesitas la barra invertida como texto,
#    debes usar \\ (escaparla)
