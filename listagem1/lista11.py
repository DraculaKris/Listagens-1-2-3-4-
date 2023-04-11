import math

cateto1 = float(input("Digite o valor do cateto 1 : "))
cateto2 = float(input("Digite o valor do cateto 2 : "))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f"Hipotenusa: {hipotenusa:.1f}")
