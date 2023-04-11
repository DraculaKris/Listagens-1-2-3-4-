idaluno = input("Digite o número de identificação do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
media = float(input("Digite a média dos exercícios: "))

ma = (nota1 + nota2*2 + nota3*3 + media) / 7

if ma >= 9:
    conceito = "A"
    situacao = "APROVADO"
elif ma >= 7.5:
    conceito = "B"
    situacao = "APROVADO"
elif ma >= 6:
    conceito = "C"
    situacao = "APROVADO"
elif ma >= 4:
    conceito = "D"
    situacao = "REPROVADO"
else:
    conceito = "E"
    situacao = "REPROVADO"

print(f"O aluno {idaluno} foi {situacao} com conceito {conceito} (MA={ma:.2f})")
