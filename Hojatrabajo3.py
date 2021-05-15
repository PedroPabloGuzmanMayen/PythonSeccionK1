'''
Programa de la contrasena
'''
print("------")
print("Choose your password")
password = input()
print("Confirm your password")
password2 = input()

if password == password2:
    print("Your password is correct")

if password != password2:
    print("Your password is incorrect")

'''
Programa que te indica si eres del grupo A o B"
'''
print("------")
print("Ingresa tu nombre")
nombre = str(input())
print("Ingresa tu sexo (H o M")
genero = str(input())

#. Grupo A:

if genero == "M":
    if nombre.lower() < "m":
        print("Eres del grupo A")
    else: 
        print("Eres del grupo B")

if genero == "H":
    if nombre.lower() > "n":
        print("Eres del grupo A")
    else:
        print("Eres del grupo B")


