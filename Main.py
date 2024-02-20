from Funciones import *
print("Bienvenida al menú del libro de recetas.")
opcion = menu()
while opcion != 6:
    if opcion == 1:
        opcion1(recetas)
    elif opcion == 2:
        opcion2(recetas)
    elif opcion == 3:
        opcion3(recetas)
    elif opcion == 4:
        opcion4(recetas)
    elif opcion == 5:
        opcion5(recetas)
    else:
        erroropcion()
    opcion = menu()
print()
print("Saliendo del programa. Muchas Gracias")
print()
