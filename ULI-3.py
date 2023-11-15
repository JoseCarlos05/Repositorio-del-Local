lista1 = input('Introduce tres números separados por espacios: ')
lista2 = input('Introduce tres números separados por espacios: ')
lista = lista1 + ' ' + lista2 + ' '
lista_f = lista * 3
lista_f = lista_f.split()
elem = 0
suma = 0
for num in lista_f:
    elem += 1
    suma += int(num)
media = suma/elem
print('La lista final es:', lista_f)
print(f'Se han introducido un total de {elem} números')
print('La media de todos ellos es:', media)