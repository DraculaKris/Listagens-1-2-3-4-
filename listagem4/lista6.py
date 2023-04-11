def celsiusfahrenheit(celsius):
    return celsius * 9/5 + 32

def convertable(lowelimit, uppelimit, decrement):
    print(f'Celsius\t Fahrenheit')
    celsius = uppelimit
    while celsius >= lowelimit:
        fahrenheit = celsiusfahrenheit(celsius)
        print(f'{celsius:.1f}C\t {fahrenheit:.1f}F')
        celsius -= decrement

lowelimit = float(input("Digite o limite inferior do intervalo em graus Celsius: "))
uppelimit = float(input("Digite o limite superior do intervalo em graus Celsius: "))
decrement = float(input("Digite o decremento a ser utilizado: "))

convertable(lowelimit, uppelimit, decrement)
