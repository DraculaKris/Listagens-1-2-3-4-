quantidade_cds = int(input("Informe a quantidade de CDs na coleção: "))
total_investido = 0

for i in range(quantidade_cds):
    preco_cd = float(input(f"Informe o preço do CD {i+1}: "))
    total_investido += preco_cd

valor_medio = total_investido / quantidade_cds

print(f"Valor total investido na coleção: R${total_investido:.2f}")
print(f"Valor médio gasto em cada CD: R${valor_medio:.2f}")
