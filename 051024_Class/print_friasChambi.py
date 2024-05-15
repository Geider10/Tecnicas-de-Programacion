#1. Inventario de Productos:

products = ("manzana", "naranja", "frutillaa", "limon", "morron")
price = {"manzana": 1000, "naranja": 1200, "frutilla":1500, "limon":1800, "morron":2000}

# for ele in products:
#     if ele in price:
#         print("Producto: ",ele + " precio: ",price[ele]);

# 2. Agenda Telefónica:
names = "Pedro", "Juan", "Franco"
number_phone = {"Pedro": 11111, "Juan":22222, "Franco":33333}
# name = input("Ingresa tu nombre para buscar tu telefono: ");

# if name in names:
#     print("Nombre: ", name, " el telefono es: ", number_phone[name]);
# else:
#     print("Nombre: ", name, " no esta registrado");
     

# 3. Calculadora de IMC:
weight_height = (68, 75, 80, 85, 90,165, 175, 180, 185, 190);
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10= weight_height;#desempaquetar
imc = (
    a1 / ((a6/100)**2) ,
    a2 / ((a7/100)**2),
    a3 / ((a8/100)**2),
    a4 / ((a9/100)**2),
    a5 / ((a10/100)**2),
    )
# print(imc);#nueva tupla con el imc calculado

names = {"Pedro": "", "Juan": "", "Franco":"", "Luca": "", "Leo": ""};
for key in names.keys():
    for value in imc:
        names[key] = value
    # print(key, "--->",names[key]);#le asigno un IMC distinto a cada valor del diccionario.
   
# 4. Alumno y calificaciones
names = ("Pedro", "Juan" , "Franco", "Luca", "Leo");
notas = {"Matematica": 8,"Fisica": 10, "Quimica":6}
cont = 0
promedio = 0
total = 0
for name in names:
    for nota in notas.keys():
        cont+=1
        total += notas[nota]
    promedio = total / cont
    # print("Nombres: ",name, " promedio: ",promedio)
    cont = 0
    total= 0
    promedio = 0

# 5. Iventario de Ropa
tallas = ("S","M","L","XL")
quantity = {"S":5,"M":10,"L":15,"XL":20}
# search = input("Ingrese la talla: ")
# for talla in tallas:
#     if search == talla:
#         print("Talla: ",talla, " cantidad: ",quantity[talla]);
#     else:
#         print("No existe dicha talla");
#         break;

# 6. Menú de Restaurante:
platos = "Ravioles", "Pastas", "Empanadas", "Asado", "Pastel de papas"
pricing = { "Ravioles": 3000, "Pastas":4000,"Empanadas":5000,"Asado":6000, "Pastel de papas":7000}
# print("Menu:\n 1:Ravioles\n 2:Pastas\n 3:Empanadas\n 4:Asado\n 5:Pastel de papas")
# option = input("Escribí el plato para ver el precio: ");
# for pric in platos:
#     if option == pric:
#         print("Plato: ", pric, " precio es: ", pricing[pric])


# 7. Biblioteca de Libros:
books = "1984", "El principito", "El nombre del viento", "La sobra del viento", "Cien años de soledad"
autores = {
    "1984": "George Orwell",
    "El principito": "Antoine de Saint-Exupéry",
    "El nombre del viento": "Patrick Rothfuss" ,
    "La sobra del viento":"Carlos Ruiz Zafón",
    "Cien años de soledad": "Gabriel García Márquez"
}
# print("Menu:\n 1:1984\n 2:El principito\n 3:El nombre del viento\n 4:La sobra del viento\n 5:Cien años de soledad")
# option = input("Escribí el libro para ver a su autor: ");
# for book in books:
#     if option == book:
#         print("Libro: ", book, " autor es: ", autores[book])

# 8. Agenda de Citas:
from datetime import datetime
dates = ( "10/04/2024", "11/04/2024", "18/04/2024", "22/04/2024", "30/04/2024");
citas = { "10/04/2024": "Pedro" , "11/04/2024" : "Juan", "18/04/2024": "Franco", "22/04/2024" : "Luca", "30/04/2024": "Leo"};
# option = input("Ingresa la fecha (dd/mm/aaaa): ")
# for date in dates:
#     if option in date:
#         print("fecha ", date, " la cita es: ", citas[date]);

# 9. Tienda de Electrónica:

# Crea un programa que almacene en una tupla los nombres de 5 productos electrónicos y en un diccionario las características de cada uno (marca, modelo, precio). Permite al usuario buscar un producto por nombre y mostrar sus características.
products = ("telefono", "audis", "cargador", "heladera", "aire", "aire acondicionado")
feuturs = {"Marca": "Samsung","Modelos": "z01", "Precio": 2100.60}
option = input("Busca un producto: ")
for product in products:
    if(option == product):
        print("El producto es: ", product) 
        for key, value in feuturs.items():
            print(key, " ---> ", value)
            
            
            
# 10. Gestión de Alumnos:

# Crea un programa que almacene en una tupla los nombres de 5 alumnos y en un diccionario la información de cada uno (dirección, teléfono, fecha de nacimiento). Permite al usuario buscar un alumno por nombre y mostrar su información completa.




