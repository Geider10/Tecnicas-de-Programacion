#Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
print("\nExercise 1")
for i in range(0,11):
    if i%2 == 1:
        print(i)


#Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
print("\nExercise 2")
i = 1
while i <= 10:
    print(i)
    i += 2

#Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
#salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. Usa el esqueleto de abajo:
print("\nExercise 3")
for ch in "pablo.melissari@bue.edu.ar":
    if ch == "@":
        break
    print(ch, end="")

print("\n")
emailFace = "mirko_de20@hotmail.com"
for i in emailFace:
    if i == "_":
        break #sale del bucle for
    print(i,end="");#se va renderizar cada item hasta que se ejecute el break

#Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, 
#reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:
print("\nExercise 4")
for i in "02120098237030":
    if i == "0":
        print("x",end="")
        continue #ejecuta la siguiente linea
    print(i,end="")

#Pregunta 5: ¿Cuál es la salida del siguiente código?
print("\nExercise 5")
n = 3

while n > 0:
    print(n + 1)#se renderiza: 4,3,2
    n -= 1# valor de n: 2,1,0
else:
    print(n)#se renderiza esto por ultimo: 0

#Pregunta 6: ¿Cuál es la salida del siguiente código?
print("\nExercise 6")
n = range(4)#0,1,2,3

for num in n:
    print(num - 1)#-1, 0, 1, 2  : se ejecuta esto
else:
    print(num)#3

#Pregunta 7: ¿Cuál es la salida del siguiente código?
#range(inico,fin - 1,salto)
print("\nExercise 7")
for i in range(0, 10, 3):
    print(i)#0, 3, 6, 9

