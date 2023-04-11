palavra = input("Digite uma palavra: ")
nova_palavra = ""

for caractere in palavra:
    novo_valor_ascii = ord(caractere) + 1
    novo_caractere = chr(novo_valor_ascii)
    nova_palavra += novo_caractere

print("A nova palavra é:", nova_palavra)
