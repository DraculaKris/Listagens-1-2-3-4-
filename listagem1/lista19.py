conta = input("Digite o número da conta corrente 3 dígitos: ")
containvertida = conta[::-1] 
soma = int(conta) + int(containvertida)  
multsoma = [int(digito) * (i + 1) for i, digito in enumerate(str(soma))] 
dverificador = str(sum(multsoma))[-1] 

print("Dígito verificador: ", dverificador)
