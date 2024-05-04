#Exercise 03
def setNumber(number):
    return float(number)

def setOperation(nameOperation,a, b):
    if(nameOperation == "suma"):
        return "La" , nameOperation , "es: " , setNumber(a) + setNumber(b)
    elif(nameOperation == "resta"):
        return "La" , nameOperation , "es: " , setNumber(a) - setNumber(b)
    elif(nameOperation == "multiplicacion"):
        return "La" , nameOperation , "es: " , setNumber(a) * setNumber(b)
    elif(nameOperation == "division"):
        return "La" , nameOperation , "es: " , setNumber(a) / setNumber(b)

    
print(setOperation("suma",2,2))
print(setOperation("resta",8,2))
print(setOperation("multiplicacion",3,3))
print(setOperation("division",10,5))
