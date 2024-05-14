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
print(imc);#nueva tupla con el imc calculado

names = {"Pedro": "", "Juan": "", "Franco":"", "Luca": "", "Leo": ""};
for key in names.keys():
    for value in imc:
        names[key] = value
    print(key, "--->",names[key]);#le asigno un IMC distinto a cada valor del diccionario.
   
   




