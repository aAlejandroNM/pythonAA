#ejercicio 1
#password = "password"

#input_pssw = input("ingrese la contraseña: ")
#if (input_pssw == password):
#    print("la contraseña coincide")
#else:
#    print("no coincide")

#ejercicio2
#number1 = int(input("ingrese el primer numero: "))

#number2 = int(input("ingrese el primer segundo: "))

#if(number1 / number2 ==0):
#    print("error")
#else:
# #   print(number1 / number2)

#ejercicio3
#number = int(input("ingrese un numero: "))
#if (number % 2 ==1):
#    print("es inpar")
#else:
#    print("el numero es par")

#ejercicio4
#age =int(input("ingrese su edad: "))
#ingresos =int(input("ingrese sus ingresos"))

#if (ingresos > 1000 and age >= 18):
#    print("usted tiene que tributar")
#else:
#    print("no tiene que tributar")

# #ejecicio5
# name = input("ingrese su primer nombre: ")
# gender = input("escriba su genero: -masculino -femenino: ")

# first_letter = name[0]
# print(first_letter)

# letters_groupA  = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
# letter_isin = False

# indice = 0
# while(True):
#     if(letters_groupA[indice] == first_letter):
#         letter_isin = True
#         break
#     else:
#         letter_isin = False
#         break

#     indice +=1

# if((letter_isin == True and gender == "femenino") or (letter_isin == False and gender == "masculino")):
#     print("pertence al grupo A")
# else:
#     print("pertenece al grupo B")

# #ejercicio6
# # age = int(input("ingrese su edad: "))
# # if(age < 4):
# #     print("la entrada es gratis")
# # elif(age >= 4 and age <= 18):
# #     print("la entrada es de 5€ ")
# # elif(age > 18):
# #     print("la entrada es de 10€ ")
# # else:
# #     print("error")

#ejercicio7
# palabra = input("ingrese la palabra a repetir")
# for i in range(10):
#     print(palabra)
#ejercicio8:Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# age = int(input("ingrese su edad "))
# for i in range(1,age+1,1):
#     print(i)

#ejercicio9 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# number = int(input("ingrese un numero entero"))
# for i in range(1,number+1,2):
#  print(i)
# print(number%2)
#ejercicio10 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

#metodos listas
#metodo pop eliminar por su indice
# dulces = ["barrilete ", "mani","chicle"]
# dulces.pop(1)

#metodo clear se utiliza para borrar todos los elementos de la lista
# dulces.clear()
# metodo count recibe valor cuantas veces esta el elemento
# dulces.count("chicle")

# metodo sort ordenar de forma asendente reverse invierte 
#dulces.sort() #ordeno alfabeticamente

# operador in 
# comparar si el elemento exactamente esta en lalista valores

# operador is es para validar si tienen la misma referencia 

# operador any para ver si almenos hay 1 elemento en la lista como el operador or operador all es como un and

# range() es un iterable genera una lista de numeros interables.

# metodo copy() copiar listas valores
# dulces = [1 , 2 ,3]
# dulces2 = dulces.copy()

# metodo append agregar valores al final de la lista
# dulces.append[5]

#metodo extend() agregar valores de otra lista 
# lista.extent(otralista)

#metodo insert


#metodo len() cantidad de cosas 
# lista =["perro", "gato ", "juan", "pedro"]
# contador = 0
# while contador <= len(lista)-1:
#     print(lista[contador],contador)
#     contador += 1

#ejercicio con append Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
# Química, Historia y Lengua) en una lista y la muestre por pantalla.
# materias = []
# cantidad_materias = int(input('cuantas materias va ingresar'))
# for i in range(cantidad_materias):
#     asignatura = input("ingrese la materia") 
#     materias.append(asignatura)
#     print(materias)

#ejercicio Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre 
#por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
# materias = ['fisica', 'matematicas']
# len(materias)
# mensaje_final = ''
# for i in range(0,len(materias)):
#     mensaje = (f'{materias[i]}')
#     mensaje_final = mensaje_final + mensaje    
# print(f'yo estudio: {mensaje_final}')

#ejercicio Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
#lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
#donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
# todas_materias = ['matematicas', 'fisica','quimica','historia']
# notas = []
# for i in range(0,len(todas_materias)):
#     print("cuanto ha sacado en: ", todas_materias[i])
    
#     nota = float(int(input()))
#     notas.append(nota)

# for i in range(0,len(todas_materias)):
#     print(f"En {todas_materias[i]} saco {notas[i]}")

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numbers = [1,2,3,4,5,6,7,8,9,10]

print(reverse(numbers))
    
    