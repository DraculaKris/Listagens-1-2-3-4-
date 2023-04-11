salbruto = float(input("Informe o salário bruto do funcionário: "))
proventos = float(input("Informe os adventos do funcionário: "))

if salbruto <= 5000:
    desconto = salbruto * 0.05
else:
    desconto = salbruto * 0.1

salario_liquido = salbruto + proventos - desconto

print("O salário líquido do funcionário é R$%.2f" % salario_liquido)

