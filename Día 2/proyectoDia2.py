nombre = input("¡Hola! 🖐 \nPor favor dime tú nombre: ")
apellido = input("Ahora por favor dime tus apellidos: ")
nombreCompleto = nombre + " " + apellido
venta = float(input("Ahora por favor dime ¿Cuánto has vendido? 💰💲 : ")
)
comision = venta * 13 / 100

print(f"Muy bien: '{nombreCompleto}'\nHas vendido ${venta} Pesos\nTu comisión por las ventas es de ${comision}\n¡Felicidades! {nombre}! 🥳🥳😇😇 ")