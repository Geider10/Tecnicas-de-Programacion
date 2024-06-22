#Importar las fuciones 
from funciones import *
import os 

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
    if os.path.exists(archivo):
        while (True):
            menu()
            option = inputInt("Elegí una opción del menú: ")

            if(option == 1):
                postProduct()
            elif(option == 2):
                getProducts()            
            elif(option == 3):
                searchValuesProduct()
            elif(option == 4):
                patchProduct()
            elif(option == 5):
                deleteProduct()
            elif(option == 6):
                saveProducts()
            elif(option == 7):
                break
    else: 
        print("No existe el archivo")

#punto de inicio de la app
def _main():
    controllerUser()

_main()