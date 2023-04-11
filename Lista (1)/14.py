palavra = input("Digite uma palavra: ")
vogais = 'aeiou'
num_vogais = 0

for letra in palavra:
    if letra.lower() in vogais:
        num_vogais += 1

substituir = input("Digite um caractere para substituir as vogais: ")

nova_palavra = ""
for letra in palavra:
    if letra.lower() in vogais:
        nova_palavra += substituir
    else:
        nova_palavra += letra

print("A palavra", palavra, "possui", num_vogais, "vogais.")
print("Nova palavra:", nova_palavra)