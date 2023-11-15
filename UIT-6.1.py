salir = False
opcion = 0
while not salir:
  print("Menú")
  print("1) Opción 1")
  print("2) Opción 2")
  print("3) Opción 3")
  print("4) Salir")
  opcion = int(input("Opcion: "))
  if opcion == 1:
    print("Opción 1")
  elif opcion == 2:
    print("Opción 2")
  elif opcion == 3:
    print("Opción 3")
  elif opcion == 4:
    salir = True
  else:
    print("Introduce un número entre 1 y 4")
print("Fin")