#Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 1")
x = 5
y = 10
z = 8

print(x > y) #false x < y
print(y > z) #true y es mayor a z

#Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 2")
x, y, z = 5, 10, 8
print(x > z) # flase x < z ===
print((y - 5) == x) # true

#Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 3")
x, y, z, = 5, 10, 8
x, y, z, = z, y, x # x & z intercambian los valores.
print(x,y,z)
print(x > z) # true
print((y - 5) == x) # flase: y = 5 & x = 8

#Pregunta 4: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 4")
X = 10

if x == 10: #se cumple esta condicion
    print(x == 10) #se ejecuta este bloque de codigo
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

#Pregunta 5: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 5")
x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")#se ejecuta esto
if int(x) == 1:
    print("five")#se ejecuta esto
else:
    print("six")

#Pregunta 6: ¿Cuál es el resultado del siguiente fragmento de código?
print("\nExercise 6")

x = 1
y = 1.0
z = "1"

if x == y:#1 int && 1.0 float = son iguales
    print("one")
if y == int(z):
    print("two")#true
elif x == y:
    print("three")
else:
    print("four")