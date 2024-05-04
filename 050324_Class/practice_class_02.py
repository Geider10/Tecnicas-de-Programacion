# Vamos con otro ejercicio
# Supongamos que tienen una lista que contiene las calificaciones de un grupo de estudiantes en un examen.
# Cada calificación es un número entero entre 0 y 100, donde 0 representa la calificación más baja y 100 la más alta. Tu tarea es escribir un programa que realice las siguientes acciones:

# Crea una lista llamada calificaciones que contenga las siguientes calificaciones: 85, 92, 78, 90, 89, 95, 87, 80, 82, 100.
notas = [85, 92, 78, 90, 89, 95, 87, 80, 82, 100]

# Calcula y muestra el promedio de las calificaciones.
suma = 0
for i in notas:
    suma += i
promedio = suma / len(notas)
print("The avarage is: ", promedio);

# Encuentra y muestra la calificación más alta en la lista.
notaMax = max(notas);
print(notaMax)

# Encuentra y muestra la calificación más baja en la lista.
notaMax = min(notas);
print(notaMax)

# Ordena la lista de calificaciones de forma ascendente y muestre la lista ordenada.
notas.sort(reverse=True);
print(notas);
