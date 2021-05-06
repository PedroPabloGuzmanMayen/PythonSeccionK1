print("Escribe tu peso en kg")
peso = float(input())
print("Escribe tu altura en metros")
altura = float(input())

imc = peso / (altura**2)
print("Su masa corporal es de: %.2f" %imc)