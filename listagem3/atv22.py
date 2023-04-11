n = int(input("Informe o número total de eleitores: "))

votcandidato1 = 0
votcandidato2 = 0
votcandidato3 = 0

for i in range(n):
    print("Eleitor {}:".format(i+1))
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do candidato escolhido: "))
    if voto == 1:
        votcandidato1 += 1
    elif voto == 2:
        votcandidato2 += 1
    elif voto == 3:
        votcandidato3 += 1
    else:
        print("Voto inválido, tente novamente")
        continue

print("Resultado da eleição:")
print("Candidato 1 - {} votos".format(votcandidato1))
print("Candidato 2 - {} votos".format(votcandidato2))
print("Candidato 3 - {} votos".format(votcandidato3))

