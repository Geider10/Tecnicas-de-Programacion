# 1.- Como creamos una lista vacía?
list_empty = [];

# 2.- Como agregamos elementos a una lista?
newNumber = int(input("Enter a number: "))
list_empty.append(newNumber);
print("Get list: ", list_empty)

# 3.- Como podemos utilizar el bucle for para agregar más elementos?
for i in range(3):
    newNumber = int(input("Enter a number: "))
    list_empty.append(newNumber)
    i+=1
print("Get list: ", list_empty)

# 4.- Como podemos eliminar un elemento de la lista
lenList = (len(list_empty) - 1)
print("Elimina un elemento del arrray del (0 -", lenList," )")
newNumber = int(input("Enter a number: "))
del list_empty[newNumber]
print("Get list: ", list_empty)

# 5.- Como podemos agregar un elemento al principio de la lista?
newNumber = int(input("Enter a number: "))
list_empty.insert(0,newNumber)
print("Get list: ", list_empty)

# 6.- Ahora imprimí por consola la longitud de la lista.
print("La longitud de la lista es ",len(list_empty));