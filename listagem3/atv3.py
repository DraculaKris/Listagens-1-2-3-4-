notaa = -1
while notaa < 0 or notaa > 10:
    nota = float(input("Digite a nota (entre 0 e 10): "))
    if notaa < 0 or notaa > 10:
        print("Valor inválido! Digite uma nota entre 0 e 10.")

print(f"A nota digitada foi {notaa}.")
