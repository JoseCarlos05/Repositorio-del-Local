menu = True
trabajo_l = {}
desempleo_l = {}
trabajo = set(trabajo_l)
desempleo = set(desempleo_l)
while menu == True:
    print()
    print('1. Añade DNI a la Seguridad Social\n2. Elimina DNI de la Seguridad Social\n3. Muestra el número de DNIs que cobran prestación\n4. Muestra los DNIs que aparecen en ambos conjuntos')
    print()
    select = int(input('Seleccione una opción: '))
    print()
    if select == 1:
        dni = input('Introduce el DNI de usuario: ')
        trabajo.add(dni)
    elif select == 2:
        dni = input('Introduce el DNI de usuario a eliminar: ')
        trabajo.discard(dni)
        desempleo.add(dni)
    elif select == 3:
        print('Hay', int(len(desempleo)), 'DNIs que cobran prestaciones.')
    elif select == 4:
        print('Usuarios con empleo:', trabajo)
        print('Usuarios cobrando prestaciones por desempleo:', desempleo)
    else:
        print('Introduzca un número válido')
        print()