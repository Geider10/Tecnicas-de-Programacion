#Bucles
# Listas y matrices
# lista = [1, 2, 3, 4]
# print(lista[2])'

# ¿Qué hace lista.append(5) si lista = [1, 2, 3, 4]?

# Agrega el número 5 al final de la lista

#Tuplas y diccionarios

#formulario 3

# ¿Qué imprimirá el siguiente código?

# x = 5
# for i in range(3):# 0, 1, 2
#     if x % 2 == 0:
#         x += i#
#     else:
#         x -= i# 5,4, 6
# print(x) #4 


# for i in range(3):# 0, 1, 2
#     # print("i")
#     for j in range(i, 3):# 0, 1, 2
#         print(i, j)# 00 

## 00, 01, 02
## 11, 12
## 22



# x = 12
# if x > 2:
#     x += 3# 15
# if x > 10:
#     x -= 1# 14
# else:#ACA NO ENTRA!
#     x = 0
# print(x)#  14


# x = 10 
# if x > 5: 
#     print('Mayor')#aca se termina
# elif x > 8: 
#     print('Mayor que 8')
# else: 
#     print('Menor')


# for i in range(3):
#     for j in range(2):
#         print(i, j)


x = 0 
while x <= 4: # 0, 1, 2,3
    x += 1 # 1, 2, 3, 4, 5
print(x)# 4, 5


result = 0
for i in range(1, 5):
	for j in range(i):
	    result += j
#result: 0, 1, 2, 4, 5, 7, 10

#for i: 1, 2, 3, 4

#for j: 
# 1 vuelta: 0
# 2 vuelta: 0, 1
# 3 vuelta: 0, 1, 2
# 4 veluta: 0, 1, 2, 3