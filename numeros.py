#1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

#- Si los dos números son iguales
#- Si los dos números son diferentes
#- Si el primero es mayor que el segundo
#- Si el segundo es mayor o igual que el primero

a1=str(input("Ingrese dato:"))
a2=str(input("Ingrese datos:"))
a3 = a1 == a2

print("los numeros " +  str(a1)  + "y" + "son iguales" +  str(a3))
a4= a1 != a2
print("los numero" + str(a1) + "y" + str(a2) + "son diferentes" + str(a4))
a5 = a1 >a2
print("los numero" + str(a1) + "es mayr que" + str(a2) + "R:" + str(a5))
a6 = a1< a2
print("el numero:" + str(a2) + "es mayor que:" + str(a1) + "R:" + str(a6))

#opcion2
print(f"los numeros {a1}y {a2} son iguales: {a3}")
print(f"los numeros {a1} y {a2} sondiferentes: {a4}")
print(f"el numero: {a1} es mayor que: {a2} {a2} R: {a5}")
print(f"el numero: {a2} es mayor que: {a2} R: {a6}")

#opcion3
print("los numeros {} y {} son iguales: {}".format(a1,a2,a3))
print("los numeros {} y {} son diferentes {}".format(a1,a2,a4))
print("el numero: {} es maor que: {} R: {}".format(a1,a2,a5))
print("el numero: {} es mayor que: {} R: {}".format(a2,a1,a6))


#opcion4
print("los numeros",a1,"y",a2,"son iguales:",a3)
print("los numeros",a1,"y",a2,"son diferentes:",a4)
print("el numero",a1,"es mayor que",a2,"R:",a5)
print("el numero",a2,"es mayor que",a1,"R:",a6)
