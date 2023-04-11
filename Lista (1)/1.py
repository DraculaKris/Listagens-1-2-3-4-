palavra = input("Digite uma palavra de até 10 caracteres: ")
vogais = "aeiouAEIOU" # Definindo as vogais

num_vogais = 0
for letra in palavra:
    if letra in vogais:
        num_vogais += 1

print("A palavra", palavra, "possui", num_vogais, "vogais.")