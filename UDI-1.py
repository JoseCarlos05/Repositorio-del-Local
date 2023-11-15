carta = {'Plátano':'1.35', 'Manzana':'0.8', 'Pera':'0.85', 'Naranja':'0.7'}
fruta = input('Introduce la fruta deseada: ')
if fruta in carta.keys():
    cant = float(input('Indique los kilos que desea: '))
    precio = cant * float(carta[fruta])
    print(f'{cant} kilos de {fruta} valen {precio}€')
else:
    print('Lo sentimos no nos queda', fruta)