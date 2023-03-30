#2. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.

nombre=input("ingrese nombre:")
# Opcion 1
print("hola " +  (nombre))
#opcion 2
print(f"hola: {nombre}")
#opcion 3
print("hola: {}".format(nombre))
#opcion 4
print("hola" ,nombre)

