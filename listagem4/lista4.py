n = int(input("Digite o valor de N: "))
soma = 0
i = 0
cont = 0

while cont < n:
    if i % 2 == 0:
        soma += i
        cont += 1
    i += 1

print(f"A soma dos {n} primeiros números pares é {soma}.")
