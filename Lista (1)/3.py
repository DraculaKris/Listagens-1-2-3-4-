vetA = list("COMPUTACAO")

vetB = input("Digite uma palavra de 10 letras: ")

vetB = vetB.upper()

for i in range(len(vetA)):
    if vetA[i] == vetB[i]:
        print(f"A letra '{vetB[i]}' está na posição {i} de vetB.")

vetA = "COMPUTACAO"
vetB = input("Digite uma palavra de 10 letras: ")

print("As letras em comum nas mesmas posições são:")
for i in range(len(vetA)):
    if vetA[i].lower() == vetB[i].lower():
        print(i, end=" ")
print()

print("A palavra digitada foi:", vetB)

string = input("Digite uma string: ")
comprimento = len(string)
print("O comprimento da string é:", comprimento)