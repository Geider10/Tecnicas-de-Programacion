# Agregar nuevos productos al inventario. ✅
# Listar todos los productos en el inventario. ✅
# Buscar un producto por su nombre. ✅
# Actualizar la cantidad de un producto en el inventario. ✅
# Guardar el inventario en un archivo de texto al finalizar. ❌

# funciones que realicen cada una de las tareas ✅
# una funcion que llame las funciones segun la eleccion del usuario ✅
# cargar el inventario en un archivo al iniciar ❌

# EXTRAS:
# eliminar producto por su key ✅
# usar modulos para importar o exportar archivos❌
# organizar las funciones en carpetas❌

listProduct = {
    "microfono" : { "precio" : 40000, "cantidad" : 4},
    "mouse" : { "precio" : 10000, "cantidad" : 10},
    "camara" : { "precio" : 80000, "cantidad" : 6}
}
def inputString(mensaje = "Ingresa: "):
    data = input(mensaje).lower()
    return data

def inputInt(mensaje = "Ingresa: "):
    while (True):
        try:
            data = int(input(mensaje))
            return data
        except ValueError:
            print("Error, se espera un entero.")
        
def postProduct():
    keyProduct = inputString("Ingresa el nombre: ")
    precioProduct = inputInt("Ingresa el precio: ")
    cantidadProduct = inputInt("Ingresa la cantidad: ")
    listProduct[keyProduct] = {"precio" : precioProduct, "cantidad" : cantidadProduct}

def getProducts():
    cont = 1
    for key,value in listProduct.items():
        print(cont, key, value, "\n")
        cont = cont + 1

def searchKeyProduct():
    product = inputString("Ingresa el nombre: ")
    for key in listProduct.keys():
        if key == product:
            return product
        
    print("No se encontro dicho producto")

def searchValuesProduct(name):
    return listProduct.get(name)

def patchProduct():
    product = searchKeyProduct()
    if(product != None):
        # postProduct(), este puede crear un producto o editar sus valores
        #pero esto solo edita sus valores
        precioProduct = inputInt("Ingresa el precio: ")
        cantidadProduct = inputInt("Ingresa la cantidad: ")
        listProduct[product] = {"precio" : precioProduct, "cantidad": cantidadProduct}

def loadProducts():
    print("hola")
def saveProducts():
    print("hola")

def deleteProduct():
    product = searchKeyProduct()
    del listProduct[product]
    print(listProduct)
 
def controllUser(option):
    if(option == 1):
        postProduct()
    elif(option == 2):
        getProducts()
    elif(option == 3):
        product = searchKeyProduct()
        values = searchValuesProduct(product)
        print(product, "--->", values)
    elif(option == 4):
        patchProduct()
    elif(option == 5):
        deleteProduct()
    elif(option == 6):
        print("aguante boca")



def menu():
    print("Bienvenido a OfiNet, tu tienda de computación.")
    print("1) --- Agregar un producto --- ")
    print("2) --- Listar todos los productos --- ")
    print("3) --- Buscar un producto por su nombre --- ")
    print("4) --- Actualizar los datos de un producto --- ")
    print("5) --- Eliminar un producto --- ")
    print("6) --- Guardar el inventario en un archivo --- ")

    option = inputInt("Elegí una opción: ")
    controllUser(option)

#punto de inicio de la app
def _main():
    menu()
_main()

