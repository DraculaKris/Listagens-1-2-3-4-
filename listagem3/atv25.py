limitsup = float(input("Informe o limite superior do intervalo (em Fahrenheit): "))
incremento = float(input("Informe o incremento (em  Fahrenheit): "))

limiteinf = 10.0

print("Fahrenheit\tCelsius")

for f in range(int(limiteinf), int(limitsup)+1, int(incremento)):
    c = (f - 32) * 5/9
    print("{:.1f}\t\t{:.1f}".format(f, c))
