n = int(input("Digite um número inteiro: "))
divisoestotais = 0
for num in range(1, n+1):
    divisores = []
    for i in range(2, num):
        divisoestotais += 1
        if num % i == 0:
            divisores.append(i)
    if len(divisores) == 0:
        print(num, "é um número primo.")
print("Número total de divisões realizadas:", divisoestotais)
