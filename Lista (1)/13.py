string = input("Digite uma palavra ou frase: ")

nova_string = ""

for letra in string:
    if letra.lower() not in "aeiou":
        nova_string += letra

print("A nova string sem vogais é:", nova_string)