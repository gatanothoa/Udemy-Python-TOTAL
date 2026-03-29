"""Ejemplos básicos de tipos de datos en Python."""

# 1) Tipos numéricos
entero = 10
flotante = 3.14
complejo = 2 + 3j

print("ENTERO:", entero, type(entero))
print("FLOTANTE:", flotante, type(flotante))
print("COMPLEJO:", complejo, type(complejo))


# 2) Texto
cadena = "Hola, Python"
print("\nCADENA:", cadena, type(cadena))


# 3) Booleano
booleano = True
print("\nBOOLEANO:", booleano, type(booleano))


# 4) Secuencias
lista = [1, 2, 3, "cuatro"]
tupla = (1, 2, 3)
rango = range(5)

print("\nLISTA:", lista, type(lista))
print("TUPLA:", tupla, type(tupla))
print("RANGO:", list(rango), type(rango))


# 5) Conjuntos
conjunto = {1, 2, 3, 3}
conjunto_inmutable = frozenset([1, 2, 3])

print("\nCONJUNTO:", conjunto, type(conjunto))
print("FROZENSET:", conjunto_inmutable, type(conjunto_inmutable))


# 6) Diccionario
diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "activo": True,
}
print("\nDICCIONARIO:", diccionario, type(diccionario))


# 7) NoneType
nulo = None
print("\nNONE:", nulo, type(nulo))
