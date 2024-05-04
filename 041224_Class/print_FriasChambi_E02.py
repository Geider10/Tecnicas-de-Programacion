#Ejercicio 01
# Mi***primer***programa...Python

print("Mi","primer" ,"programa" ,sep="***" ,end="...")
print("Python")

#Ejercicio 02
# minimizar el número de invocaciones de la función print() insertando \n en las cadenas;
# hacer que la flecha sea el doble de grande (pero mantener las proporciones)
# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)
# elimina cualquiera de las comillas y observe detenidamente la respuesta de Python; presta atención a dónde Python ve un error - ¿es este el lugar donde realmente existe el error?
# haz lo mismo con algunos de los paréntesis;
# cambia cualquiera de las palabras print por otra cosa, que difiera solo en mayúsculas y minúsculas (por ejemplo, Print) - qué sucede ahora?
# reemplaza algunas de las comillas con apóstrofes; observa lo que sucede con cuidado.
# El código es el siguiente:

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

arrow = "    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"
twoArrow = "".join([arrow,arrow])
newArrow = arrow.replace(" ", "  ")
print(newArrow)
print(newArrow.replace("*"," *"))

variabe1 = "10.5"
variabe2 = "true"
variabe3 = False
variabe4  = 12.0
print((type(variabe1)))