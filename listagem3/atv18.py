n = int(input("Digite um número inteiro: "))

divisores = []
for i in range(2, n):
    if n % i == 0:
        divisores.append(i)

if len(divisores) == 0:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
    print(f"Ele é divisível pelos números {divisores}.")
