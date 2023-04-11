n = int(input("Digite um número inteiro: "))

primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
