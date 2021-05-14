'''
Programa que muestra un triangulo
'''
print("-----")
print("Triangulo")
print("Ingresa un numero")
n1 = int(input())
for i in range(n1+1):
    print("*"*i)

'''
Programa que muestra si un numero es primo
'''
print("---")
print("Programa que te indica si un numero es primo o no")
print("Si no te muestra nada, significa que el numero es primo")
n2 = int(input())
if n2 > 1:
    for x in range(2,n2):
        if n2%x == 0:
            print(" no es primo")
            break


'''
Programa que hace una cuenta regresiva
'''
print("----")
print("Programa que hace una cuenta regresiva")
print("Ingresa un numero:")
n4 = int(input())
for y in range(n4+1):
    print(n4-y)
    
