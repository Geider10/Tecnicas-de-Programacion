# Declara una lista que contenga por elementos los nombres de alumnos de un curso (mínimo 5)
alumns = ["Franco", "Juan", "Pedro", "Luka", "Agustin"]

# Usa sort() para ordenar a los alumnos
alumns.sort(reverse=False)

# Imprime el nombre del primer alumno
print(alumns[0])

# Inscribe un nuevo alumno en el curso(lo cuál puede alterar el orden)
newAlumn = ""
def addAlumn ():
    newAlumn = input("ingrese un nuevo alumno: ")
    alumns.append(newAlumn)

addAlumn()
print("Nuevo alumno: ",newAlumn," se agrega a la lista ordenada: ",alumns)