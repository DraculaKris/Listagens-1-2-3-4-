while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre zero e dez.")
    else:
        break
        
print("Nota válida: ", nota)