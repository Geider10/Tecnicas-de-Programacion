#paso 1: Crea una lista vacía llamada beatles
beatles = []

#paso 2: Utiliza el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
for i in ["John Lennon", "Paul McCartney", "George Harrison"]:
    beatles.append(i);

#paso 3: Utiliza el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
artistas=["Stu Sutcliffe","Pete Best"]
for i in artistas:
    permiso = input("Quiere ingresar mas artistas (S/N): ")
    while permiso.lower() != "s":#se ejecuta el while cuando se cumple la condicion osea es TRUE
        permiso = input("ingresar mas artistas (S/N): ")
    beatles.append(i)

#paso 4: Utiliza la instrucción del para eliminars a Stu Sutcliffe y Pete Best de la lista;
def deleteMember(pos):
    del beatles[-1]
deleteMember(-1)
deleteMember(-1)
print(beatles)

#paso 5: Utiliza el método insert() para agregar a Ringo Starr al principio de la lista.
def addMember (pos,name):
    beatles.insert(pos,name);

addMember(0,"Ringo Star");
addMember(-1,"Profesor");
print(beatles);