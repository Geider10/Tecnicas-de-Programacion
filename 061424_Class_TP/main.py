#1
# Agregar nuevos productos al inventario.✅
# Listar todos los productos en el inventario. ✅
# Buscar un producto por su nombre.
# Actualizar la cantidad de un producto en el inventario.
# Guardar el inventario en un archivo de texto al finalizar.

#2 
# funciones que realicen cada una de las tareas
# una funcion que llame las funciones segun la eleccion del usuario
listProduct = {
    "microfono" : { "precio" : 40000, "cantidad" : 4},
    "mouse" : { "precio" : 10000, "cantidad" : 10},
    "camara" : { "precio" : 80000, "cantidad" : 6}
}
def inputInt(mensaje):
    while (True):
        try:
            value = int(input(mensaje))
            return value
        except ValueError:
            print("Error, se espera un entero.")
        
def postProduct():
    keyProduct = input("Ingresa el nombre: ")
    precioProduct = inputInt("Ingresa el precio: ")
    cantidadProduct = inputInt("Ingresa la cantidad: ")
    listProduct[keyProduct] = {"precio" : precioProduct, "cantidad" : cantidadProduct}

def getProducts():
    cont = 1
    for key,value in listProduct.items():
        print(cont, key, value, "\n")
        cont = cont + 1

def searchProduct():
    product = input("Ingresa el nombre: ")
    for product in listProduct:
        print(product)

    # print("No existe dicho producto")
def controllUser(option):
    if(option == 1):
        print("--- Agrega un nuevo producto ---")
        postProduct()
    elif(option == 2):
        print("--- Los productos ---")
        getProducts()
    elif(option == 3):
        print("--- Buscar producto ---")
        searchProduct()
    elif(option == 4):
        print("4) Actualizar la cantidad de productos")

def menu():
    print("Bienvenido a OfiNet, tu tienda de computación.")
    print("1) Agregar un producto: ")
    print("2) Listar todos los productos: ")
    print("3) Buscar un producto por su nombre: ")
    print("4) Actualizar la cantidad de productos: ")
    print("5) Guardar el inventario en un archivo .txt: ")

    option = inputInt("Elegí una opción: ")
    controllUser(option)

def _main():#punto de inicio de la app
    menu()
_main()

# for key,value in listProduct.items():
#     print("key: ", key, " value: ", value)
