string = input("Digite a string: ")
count = 0

for char in string:
    if char == '1':
        count += 1

print("O número de ocorrências do caractere '1' na string é:", count)