liminferior = int(input("Digite o limite inferior: "))
limsuperior = int(input("Digite o limite superior: "))
incremento = int(input("Digite o incremento: "))

for num in range(liminferior, limsuperior+1, incremento):
    print(num)
