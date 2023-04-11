frase = "Esta é uma frase de exemplo."
contador = 0

for caractere in frase:
    if caractere.isspace():
        contador += 1

print("A frase tem", contador, "caracteres em branco.")
