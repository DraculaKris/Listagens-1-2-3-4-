ncds = int(input("Informe a quantidade de CDs: "))

totalcds = 0
totalvalor = 0

for i in range(ncds):
    print("CD {}:".format(i+1))
    valor_cd = float(input("Informe o valor investido: "))
    totalcds += 1
    totalvalor += valor_cd

if totalcds > 0:
    media_valor = totalvalor / totalcds
else:
    media_valor = 0

print("O valor total investido em {} CDs é: R$ {:.2f}".format(totalcds, totalvalor))
print("O valor médio gasto em cada CD é: R$ {:.2f}".format(media_valor))
