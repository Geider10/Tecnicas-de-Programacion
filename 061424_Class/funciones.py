import io #permite modificar la condificacion de texto de los archivos que se leean.
import json #tiene metodos para guadar y cargar diccionarios como json

# especificar el nombre del archivo, tiene que estar en el directorio raiz 
archivo = 'emptyFile.txt'
dataSet = {}

def loadProducts():
    try:
        with io.open(archivo, "r",encoding="utf-8") as file:
            contenido = file.read()
            return contenido
    except: print("No existe el archivo")


def saveProducts():
    #se sobrescribe el nuevo inventario en el mismo archivo
    with open(archivo, "w") as file:
        file.write(json.dumps(dataSet)) 
    inputKey()

try:
    dataSet = json.loads(loadProducts())
except:
    print("Error")

def inputString(mensaje = "Ingresa: "):
    data = input(mensaje).lower()
    return data

#bucle infinito hasta poner un dato correcto
def inputInt(mensaje = "Ingresa: "):
    while (True):
        try:
            data = int(input(mensaje))
            return data
        except ValueError:
            print("Error, se espera un número [1 - 7].")

def inputKey():
    input("\nPresione enter...\n")

#crea un producto 
def postProduct():
    keyProduct = inputString("Ingresa el nombre: ")
    precioProduct = inputInt("Ingresa el precio: ")
    cantidadProduct = inputInt("Ingresa la cantidad: ")
    dataSet[keyProduct] = {"precio" : precioProduct, "cantidad" : cantidadProduct}
    inputKey()

#muestra los productos o un msj que no los hay
def getProducts():
    cont = 0
    for key,value in dataSet.items():
        cont = cont + 1
        print(cont, key, value, "\n")

    if(cont == 0): print("No tiene productos")#solo se ejecuta cuando no tiene elementos el diccionario
    inputKey()

#buscar un producto por su clave
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
    inputKey()

#edita los valores del producto
def patchProduct():
    product = searchKeyProduct()
    if(product != None):
        precioProduct = inputInt("Ingresa el precio: ")
        cantidadProduct = inputInt("Ingresa la cantidad: ")
        dataSet[product] = {"precio" : precioProduct, "cantidad": cantidadProduct}
    inputKey()

#elimina un producto por su clave
def deleteProduct():
    product = searchKeyProduct()
    if(product != None):
        del dataSet[product]
    inputKey()
    
 