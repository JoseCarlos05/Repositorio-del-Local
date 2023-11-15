tab = [0] *10
suma = 0
i = 0
while i < 10:
   tab[i] = int(input('Teclea número de tabla {}: '.format(i)))
   i = i + 1
i = 0
while i < 10:
   suma = suma + tab[i]
   i = i + 1
print('Suma resultante: ', suma)
print(tab)