valormulta = float(input("Digite o valor da multa mensal: "))
faturamentomensal = float(input("Digite o valor do faturamento mensal: "))
num_fitas_mes = float(input("Digite o número de fitas alugadas por mês: "))

faturamentoanual = faturamentomensal * 12
multasanuais = valormulta * 12
totalfitas = num_fitas_mes * 12

print("Faturamento anual: R${:.2f}".format(faturamentoanual))
print("Valor das multas anuais: R${:.2f}".format(multasanuais))
print("Total de fitas ao final de 1 ano: {:.2f}".format(totalfitas))
