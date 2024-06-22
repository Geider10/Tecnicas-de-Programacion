# Agregar nuevos productos al inventario. ✅
# Listar todos los productos en el inventario. ✅
# Buscar un producto por su nombre. ✅
# Actualizar la cantidad de un producto en el inventario. ✅
# Guardar el inventario en un archivo de texto al finalizar. ✅

# funciones que realicen cada una de las tareas ✅
# una funcion que llame las funciones segun la eleccion del usuario ✅
# cargar el inventario en un archivo al iniciar ✅
# usar libreria OS ✅

# EXTRAS:
# eliminar producto por su key ✅
# usar modulos para importar o exportar archivos❌
# organizar las funciones en carpetas❌

import os
import io #permite modificar la condificacion de texto de los archivos que se leean.
import json #tiene metodos para guadar y cargar diccionarios como json

archivo = 'file.txt'
def loadProducts():
    if os.path.exists(archivo) : 
        with io.open(archivo, "r",encoding="utf-8") as file:
            contenido = file.read()
            return contenido
    else:
        print("No Existe dicho archivo")
        
def saveProducts():
    #se sobrescribe el inventario en el mismo archivo
    with open(archivo, "w") as file:
        file.write(json.dumps(dataSet))

dataSet = json.loads(loadProducts())

def inputString(mensaje = "Ingresa: "):
    data = input(mensaje).lower()
    return data

def inputInt(mensaje = "Ingresa: "):
    while (True):
        try:
            data = int(input(mensaje))
            return data
        except ValueError:
            print("Error, se espera un número [1 - 7].")
        
def postProduct():
    keyProduct = inputString("Ingresa el nombre: ")
    precioProduct = inputInt("Ingresa el precio: ")
    cantidadProduct = inputInt("Ingresa la cantidad: ")
    dataSet[keyProduct] = {"precio" : precioProduct, "cantidad" : cantidadProduct}

def getProducts():
    cont = 1
    for key,value in dataSet.items():
        print(cont, key, value, "\n")
        cont = cont + 1

def searchKeyProduct():
    product = inputString("Ingresa el nombre: ")
    for key in dataSet.keys():
        if key == product:
            return product
    
    print("No existe dicho producto")
        
def searchValuesProduct():
    product = searchKeyProduct()
    if(product != None):
        values = dataSet.get(product)
        print(values)

def patchProduct():
    product = searchKeyProduct()
    if(product != None):
        # solo edita los valores del producto
        precioProduct = inputInt("Ingresa el precio: ")
        cantidadProduct = inputInt("Ingresa la cantidad: ")
        dataSet[product] = {"precio" : precioProduct, "cantidad": cantidadProduct}

def deleteProduct():
    product = searchKeyProduct()
    if(product != None):
        del dataSet[product]
 
def menu():
    print("Bienvenido a OfiNet, tu tienda de computación.\n")
    print("1) --- Agregar un producto --- ")
    print("2) --- Listar todos los productos --- ")
    print("3) --- Buscar un producto por su nombre --- ")
    print("4) --- Actualizar los datos de un producto --- ")
    print("5) --- Eliminar un producto --- ")
    print("6) --- Guardar el inventario en un archivo --- ")
    print("7) --- Salir ---\n")

def controllerUser():
    while (True):
        menu()
        option = inputInt("Elegí una opción del menu: ")

        if(option == 1):
            postProduct()
            var = input()
        elif(option == 2):
            getProducts()
            var = input()
        elif(option == 3):
            searchValuesProduct()
            var = input()
        elif(option == 4):
            patchProduct()
            var = input()
        elif(option == 5):
            deleteProduct()
            var = input()
        elif(option == 6):
            saveProducts()
            var = input()
        elif(option == 7):
            break

#punto de inicio de la app
def _main():
    loadProducts()
    controllerUser()

_main()

