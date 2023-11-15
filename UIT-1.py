positiv = 0
negativ = 0
nulos = 0
for i in range(1, 26):
    Num = int(input('Teclea el dato número {}: '.format(i)))
    if Num < 0:
        negativ = negativ + 1
    elif Num > 0:
        positiv = positiv + 1
    else:
        nulos = nulos + 1
print('Números positivos introducidos', positiv)
print('Números negativos introducidos', negativ)
print('Números nulos introducidos', nulos)