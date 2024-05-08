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

# number = int(input("ingrese un numero"))
# for i in range(number,0, -1):
#     print(i,end=",")

#ejercicio11 pida una cantidad a invertir y el interes anual y los años devuelve cuanto gano con la inversion
# capital = int(input("ingrese su capital"))
# intereses = float(input("ingrese los intereses en decimales"))
# años = int(input("ingrese los años invertidos"))

# print(int(capital*intereses*años))

#ejercicio 11 Tabla multiplicar
# number = int(input("que tabla necesita"))
# for i in range(10+1):
#     print(f"{number} x {i} = {number*i}")

#ejercicio12 invertir palabra caracter x caracter
# palabra =input("palabra")
# palabra =palabra[::-1]
# for i in range(0,len(palabra)):
#     print(palabra[i])

# ejercicio funcion factorial
# def factorial(num):
#     return 1 if num == 0 else num*(factorial(num -1))
# num = int(input("ingrese numero"))
# print(factorial(num))
# ---------------ejercicios listas -----------------------------

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
# numbers = [1,2,3,4,5,6,7,8,9,10]

# print(reverse(numbers))
    
# """
# Escribir un programa que tenga un menú interactivo que se repite hasta que el usuario diga salir, 
# las opciones del menú son:

# -Verificar si un número es primo
# -Verificar si un número es par o impar
# -Obtener la media de una serie de números
# -Verificar si una palabra contiene la letra x o z

# Cada proceso de las opciones del menú deben implementarse en una función.
# """

# #Verificar si un número es primo
# def primo (num):
#     contador = 2
#     resultado = True     
#     while (contador <= num/2 and resultado):         
#         resultado = num % contador != 0
#         contador+= 1
#     return resultado
# #Verificar si un número es par o impar
# def par (num):
#     return num%2==0
# #Obtener la media de una serie de números
# def media(lista):
#     suma=0
#     for numero in lista:
#         suma+=numero
#     return suma/len(lista)

# def generar_lista():
#     cantidad = (int(input("Ingrese cuantos valores desea ingresar: ")))
#     lista =[]
#     for i in range(cantidad):
#         lista.append(int(input("Ingrese el valor: ")))
#     return lista
# #Verificar si una palabra contiene la letra x o z
# def palabra ():
#     palabra = (input("ingrese una palabra: "))
    
#     return palabra.count ("x") != 0 or palabra.count ("z") != 0
    
# continuar="si"
# menu = ("primo","par","media","palabra")

# while continuar=="si":
#     operacion=str(input("ingresa el proceso que deseas realizar (primo) (par) (media) (palabra)"))
#     if operacion== "primo" in menu:
#         print(primo(int(input("Ingrese el número: "))))
#     elif operacion=="primo" in menu:
#         print(par(int(input("Ingrese el número: "))))
#     elif operacion=="media" in menu:
#         print(media(generar_lista()))
#     elif operacion=="palabra" in menu:
#         print(palabra())
#     else:   
#        print("ingreso una operacion no valida")
#     continuar=str(input("Deseas repetir el proceso? Ingresa (no) para cerrar el ciclo y (si) para repetir el proceso "))

# # conjuntos
# opciones = {"1","2","3","4","5","6","7","8","9","10"}

# for i in range(len(opciones)):
#     print(i)
#     if i == 9 :
#         print(f"jugador{opciones} gano ")
#     else:
#         print(f"jugador{opciones.pop()} eliminado")

# asignatura = [{"nombre" : "skills","profesor":"Juan", "salon":"sputnik"},{"nombre" : "SER","profesor":"Angie", "salon":"auditorio"},{"nombre" : "Ingles","profesor":"Orbin", "salon":"kepler"}]
# print(asignatura[1]["nombre"])

#Crea un menú que se repita hasta que el usuario ingrese la
# opción de salida (a tu elección) y utilice una función para cada
# opción válida. Las funcionalidades son:

# Empresas = {

# "Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

# "Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

# "Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

# "Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

# "Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

# }

# #Mostrar cuántas empresas tienen más de 10 empleados en 
# #Recursos Humanos
# def contador_empresas():
    
#     for i in Empresas:
#         #print(i)
#         for j in Empresas.get(i):
#             if j['departamento'] == "Recursos Humanos" and j['empleados'] > 15:
#                 return i
# #print(Empresas['Empresa 1'][0].get('empleados'))

# #Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo)
# def promedio_emple():
#     empleados_rh =[]
#     contabilidad = []
#     ventas = []
#     operaciones = []
#     for i in Empresas:
#         for j in Empresas.get(i):
#             if j['departamento'] == 'Recursos Humanos':
#                 empleados_rh.append(j['empleados'])
#             elif j['departamento'] == 'Contabilidad':
#                 contabilidad.append(j['empleados'])
#             elif j['departamento'] == 'Ventas':
#                 ventas.append(j['empleados'])
#             elif j['departamento'] == 'Operaciones':
#                 operaciones.append(j['empleados'])
#     #print(sum(empleados_rh))

# promedio_emple()
# #print(contador_empresas())


