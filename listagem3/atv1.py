
limsuperior = int(input("Digite o limite superior do intervalo desejado: "))
incremento = float(input("Digite o incremento desejado: "))

limiteinferior = 10

print("Fahrenheit  Celsius")

for fahrenheit in range(limiteinferior, limsuperior+1, incremento):
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}F\t\t{celsius:.2f}C")   