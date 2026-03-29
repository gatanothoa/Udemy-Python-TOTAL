num1 = 1  # Esto es un entero (int)
num2 = 30.2  # Esto es un numero con decimales (float)

num1 = num1 + num2  # Suma num1 y num2, el resultado es un float

print(num1, type(num1))  # Imprime el valor y el tipo de num1
print(num2, type(num2))  # Imprime el valor y el tipo de num2

edad = int(input("Ingresa tu edad: "))  # Convierte la entrada del usuario a un entero

edad = int(edad)  # Convierte la variable edad a un entero (int)

nueva_edad = edad + 5  # Suma 5 a la edad

print("Tu edad dentro de 5 años será:", nueva_edad)  # Imprime la nueva edad

# Descripcion breve:
# Las conversiones en Python cambian un dato de un tipo a otro
# (por ejemplo, de texto a numero) para poder operar con el correctamente.

# Ejemplos de conversion:
print(int("25"), type(int("25")))      # str -> int
print(float("19.8"), type(float("19.8")))  # str -> float
print(str(2026), type(str(2026)))        # int -> str