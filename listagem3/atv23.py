turmas = int(input("Informe a quantidade de turmas: "))

talunos = 0

for i in range(turmas):
    print("Turma {}:".format(i+1))
    n_alunos = int(input("Informe a quantidade de alunos (até 40): "))
    if n_alunos <= 40:
        talunos += n_alunos
    else:
        print("Quantidade inválida de alunos, tente novamente")
        continue

if turmas > 0:
    media_alunos = talunos / turmas
else:
    mediaalunos = 0

print("O número médio de alunos por turma é: {:.2f}".format(mediaalunos))

