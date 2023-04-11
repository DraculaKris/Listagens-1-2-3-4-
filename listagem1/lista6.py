salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts = float(input("Digite a quantidade de quilowatts gasta pela residência: "))

vquilowatt = salario_minimo / 700
vpago = quilowatts * vquilowatt
vpago_desconto = vpago * 0.9

print(f"Valor do quilowatt: R${vquilowatt:.2f}")
print(f"Valor a ser pago: R${vpago:.2f}")
print(f"Valor a ser pago com desconto: R${vpago_desconto:.2f}")
