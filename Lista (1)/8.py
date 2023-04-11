nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa (M ou F): ")
idade = int(input("Digite a idade da pessoa: "))

if sexo == "F" and idade < 25:
    print(nome + " ACEITA")
else:
    print("NÃO ACEITA")