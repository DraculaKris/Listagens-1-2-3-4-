votosbranco = 0
votosnulo = 0
votoskiko = 0
votoschaves = 0
votoschiquinha = 0

while True:
    print("VOTE 1 para votar em Branco")
    print("VOTE 2 para votar Nulo")
    print("VOTE 3 para votar Kiko")
    print("VOTE 4 para votar Chaves")
    print("VOTE 5 para votar Chiquinha")
    print("VOTE 666 para encerrar a votação")
    
    voto = int(input("Digite o número do seu voto: "))
    
    if voto == 666:
        break
    elif voto == 1:
        votosbranco += 1
    elif voto == 2:
        votosnulo += 1
    elif voto == 3:
        votoskiko += 1
    elif voto == 4:
        votoschaves += 1
    elif voto == 5:
        votoschiquinha += 1
    else:
        print("Voto inválido. Tente novamente.")
    
print("RESULTADO FINAL")
print(f"Votos em Branco: {votosbranco}")
print(f"Votos Nulos: {votosnulo}")
print(f"Votos em Kiko: {votoskiko}")
print(f"Votos em Chaves: {votoschaves}")
print(f"Votos em Chiquinha: {votoschiquinha}")
