idade = int(input("Digite a idade do trabalhador: "))
tempodeservico = int(input("Digite o tempo de serviço do trabalhador em anos: "))

if idade >= 65:
    print("O trabalhador pode se aposentar!")
elif tempodeservico >= 30:
    print("O trabalhador pode se aposentar!")
elif idade >= 60 and tempodeservico >= 25:
    print("O trabalhador pode se aposentar!")
else:
    print("O trabalhador não pode se aposentar por enquanto!")
