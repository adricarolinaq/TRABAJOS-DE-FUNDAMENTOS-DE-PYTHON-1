print("NOMBRE:ADRIANA QUICHIBO")
# EJERCICIOS
#1.
#Crear un programa que permita decidir a una persona cruzar la calle o no según:
#- Si semáforo esta en verde cruzar la calle
#- Si semáforo esta en rojo o amarillo no cruzar
#La persona debe poder ingresar el estado del semáforo por teclado

semaforo=input("INGRESE EL COLOR DEL SEMAFORO: ")
if semaforo=="verde":
    print("USTED PUEDE CRUZAR")
elif  semaforo =="amarillo":
    print("USTED TIENE QUE ESPERAR")
elif semaforo =="rojo":
    print ("NO CRUZAR")
else:
    print("NO ES EL COLOR CORRECTO")

#2.
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad=int(input("Introduzca su edad: "))
if edad >= 17:
    print ("mayor de edad")
else:
    print ("menor de edad")
#3.
#Escribir un programa que almacene la cadena de caracteres <b>contraseña</b> en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por 
# el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contra= "pablo123"
x= input ("ingrese la contraseña")
if x.lower()== contra:
    print("CONTTRASEÑA CORRECTA")
else:
    print("CONTRASEÑA INCORRECTA")

#4. 
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


numero= int(input("Introduce un número entero: "))
if numero%2== 0:
    print("El número  es par")
else:
    print("El número es impar")

#5.
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Realizar un programa que pueda decir el % de impuestos que una persona deba pagar según su sueldo

salario=float(input("INGRESE SU SUELDO: "))
impuesto=0
if salario < 10000:
    impuesto=0.05
elif salario >=10000 and impuesto < 20000:
    impuesto=0.15
elif salario >= 20000 and salario < 35000:
    impuesto=0.20
elif salario >= 35000 and salario < 60000:
    impuesto=0.30
elif salario >= 60000:
    impuesto=0.45
else:
    print ("EL SALARIO INGRESADO ES INCORRECTO")
total= salario*impuesto
print("El valor del impuesto ha pagar es ",total)
print("El salario ha resivir es ",salario - total)
#6. 
#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

valor_1=int(input("valor 1 = "))
valor_2=int(input("valor 2 = "))
valor_3= valor_1 + valor_2
valor_4= valor_1 - valor_2
valor_5= valor_1*valor_2

print("Presione 1 para sumar")
print("Presione 2 para restar")
print("Presione 3 para multiplicar")

opción= input("Que opción desea:")
if opción=="1":
    print("La suma de los valores es", valor_3)
elif opción=="2":
    print("La resta de los valores es", valor_4 )
elif opción=="3":
    print("La multiplicación es", valor_5)
else:
    print("No es correcta la opcion")


#7.
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#- Ingredientes vegetarianos: Pimiento y tofu.
#- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla 
#si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print('\n\tPizzería Napolitana\n\n\tMenú de Pizzas\n1.Pizzas vegetarianas\n2.Pizzas no vegetarianas')
opción=int(input('Ingrese una opción del menú: '))
if opción==1:
    print('\tUsted eligio el tipo de pizzas vegetarianas\nLos ingredientes disponibles son:\n1.Pimiento\n2.tofu\n Solo puede elegir un ingrediente!!!')
    ingredientev=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientev==1:
        print('Su pizza consta de Pimiento,mozzarella y tomate!!')
    elif ingredientev==2:
        print('Su pizza consta de Tofu,mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')
elif opción==2:
    print('\tUsted eligio el tipo de pizzas no vegetarianas\nLos ingredientes disponibles son:\n1.Peperoni\n2.Jamón\nSalmon\nSolo puede elegir un ingrediente!!!')
    ingredientesn=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientesn==1:
        print('Su pizza consta de Peperoni,mozzarella y tomate!!')
    elif ingredientesn==2:
        print('Su pizza consta de Jamón,mozzarella y tomate!!')
    elif ingredientesn==3:
        print('Su pizza consta de Salmon,mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')

#8.
#Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
letra= input("ingrese una letra")
if len(letra) !=1:
    print("no se puede procesar el dato. Debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("es vocal")
else:
    print("no es vocal")
    

#8.1
numero= input("Ingrese el numero: ")
print(numero)
if len(numero) != 1:
    print("No se puede procesar el dato. Debe ingresar un solo numero.")
elif numero in "123456789":
    print("Es numero")
else:
    print("No es numero")



#9. Calificación de un examen. Ingrese la puntuación de un examen.
#Si es >= 90 La calificación es A, si es >= 80 La calificación es B,
#si es >= 70 La calificación es C,
#si >= 60 La calificación es D,
#sino La calificación es F,


print("Detalles: calificacion d un examen")
calificacion= int (input( "ingrese la calificacion del examen "))
print(calificacion )
if calificacion>=90:
    print("la calificacin es A")
elif calificacion>=80:
    print("La calificacion es B")
elif calificacion>=70:
    print("La calificacion es C")
elif calificacion>=60:
    print("La calificacion es D")
else :
    print("La calificacion es F")
#9.1


print("Detalles: calificacion de un examen")
calificacion= float (input( "ingrese la calificacion del examen "))
print(calificacion )
if calificacion>=9.5 and calificacion<=10 :
    print("la calificacion es EXCELENTE")
elif calificacion>=8.5 and calificacion<=9.5:
    print("La calificacion es MUY BUENO")
elif calificacion>=7 and calificacion<=8.5:
    print("La calificacion es BUENO")
elif calificacion>=4 and calificacion<=7:
    print("La calificacion es REGULAR")
elif calificacion>=0 and calificacion<=4:
    print("La calificacion es DEFICIENTE")
else :
    print("La calificacion no se encuentra detro del rango")


#10. Determinar si un año es bisiesto.
#Es divisible entre 4, pero no es divisible entre 100.
#Es divisible entre 400.
#Por ejemplo, los años 2000 y 2020 son bisiestos porque son divisibles entre 400, mientras 
#que el año 1900 no es bisiesto porque es divisible entre 100 pero no entre 400.


año = 1980 #el año que queremos comprobar

if año % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")


#11. Determinar el mayor de tres números:

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el terser numero: "))

if a>b and a >c :
    print ("el numero ",a ," es mayor al segundo y terser numero")
elif b>a and b >c :
    print ("el numero ",b ," es mayor al primer y terser numero")
elif c>b and c >a :
    print ("el numero ",c ," es mayor al primer y segundo numero")
else :
    print ("Ninguno es mayor ")

#12. Programa para determinar si un número es positivo, negativo o cero:

numero= int(input("ingresar un numero:"))
if numero==0:
   print("el numero es 0")
elif numero<0:
   print("el numero es negativo")
elif numero>0:
   print("el numero es positivo") 


#Ejercicio 13
#Crear un programa para determinar si un número es múltiplo de 3:
dato=int(input('Digite el número a verfificar si es múltiplo de 3: '))
if(dato%3==0):
    print('El número {} es múltiplo de 3'.format(dato))
else:
    print(f'El número: {dato} no es multiplo de 3')
#14. Programa para determinar si un número es divisible por 4 y 6:

numero= int (input("igresar un valor: "))
if numero % 4==0:
    print("El numero es divisible para 4")
numero= int (input("igresar un valor: "))    
if numero % 6==0:
    print("El numero es visible para 6")
#15. Programa para imprimir el día de la semana correspondiente a un número del 1 al 7:


dia=int(input("Ingrese un un numero del 1 al 7: "))
if dia==1:
    print("Corresponde al dia Lunes")
elif dia==2:
    print("Corresponde al dia Martes")
elif dia==3:
    print("Corresponde al dia Miercoles")
elif dia==4:
    print("Corresponde al dia Jueves")
elif dia==5:
    print("Corresponde al dia Viernes")
elif dia==6:
    print("Corresponde al dia Sabado")
elif dia==7:
    print("Corresponde al dia Domingo")
else:
    print("El valor ingresado no corresponde a ningun dia de la semana")
#16. Programa para imprimir el nombre del mes correspondiente a un número del 1 al 12:

mes=int(input("Ingrese un numero del 1 al 12 para saber el mes del año :"))

if mes==1:
    print("Corresponde al mes de ENERO.")
elif mes==2:
    print("Corresponde al mes de FEBREO.")
elif mes==3:
    print("Corresponde al mes de Marzo.")
elif mes ==4:
    print("Corresponde al mes de Abril.")
elif mes==5:
    print("Corresponde al mes de MAYO.")
elif mes==6:
    print("Corresponde al mes de JUNIO.")
elif mes==7:
    print("Corresponde al mes de JULIO.")
elif mes==8:
    print("Corresponde al mes de AGOSTO.")
elif mes==9:
    print("Corresponde al mes de SEPTIEMBRE.")
elif mes==10:
    print("Corresponde al mes de OCTUBRE.")
elif mes==11:
    print("Corresponde al mes de Noviembre.")
elif mes==12:
    print("Corresponde al mes de DICIEMBRE.")
else:
    print("No correponde a ningun mes ")

#17. Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
#- 0-2: Muy deficiente
#- 3-4: Insuficiente
#- 5-6: Suficiente
#- 7: Bien
#- 8-9: Notable
#- 10: Sobresaliente


nota=float(input("Ingrese la nota: "))
if nota >= 0 and nota <= 2:
    print(f"La nota de {nota} es muy deficiente")
elif nota >= 3 and nota <= 4:
    print(f"La nota de {nota} es insuficiente")
elif nota >= 5 and nota <= 6:
    print(f"La nota de {nota} es suficiente")
elif nota == 7:
    print(f"La nota de {nota} esta bien")
elif nota >= 8 and nota <= 9:
    print(f"La nota de {nota} es notable")
elif nota == 10:
    print(f"La nota de {nota} es sobresaliente")
else:
    print(f"La nota de {nota} no existe")
#18. Escribir un programa que pida al usuario una frase y determine si es un palíndromo. Ignorar espacios en blanco y mayúsculas/minúsculas al determinar si la frase es un palíndromo o no.
#-Un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo, "ana", "radar" y "aibohphobia" son palíndromos.

palabra = input("Ingrese la palabra a comprobar: ")

if str(palabra) == str(palabra)[::-1] : # Primero calculamos el valor inverso de la palabra original con [::-1] como índice de lista.
    print(f"La palabra ingresada {palabra},si es un Palindromo")
else:
    print(f"La palabra ingresada {palabra},no es Palindromo")


#19. Escribir un programa que pida al usuario su nombre y edad, y muestre por pantalla un mensaje con dichos datos en la siguiente forma: "Hola, {nombre}, tienes {edad} años".

nombre=input("igresar su nombre: ")
edad=int(input("ingresar su edad "))
if edad>=18:
    print(nombre, "es mayor de edad")
elif edad<18:
    print(nombre, "es menor de edad")

#20. Escribir un programa que pregunte al usuario una cantidad de días y muestre por pantalla cuantas horas, minutos y segundos hay en dicha cantidad de días.


cant_dias= int(input("INGRESE LOS DIAS DESEADOS"))