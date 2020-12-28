def menu ():
    print ("\nSistema medico de registro".center(38))
    print ("\n1)Crear paciente")
    print ("2)Registrar lecturas")
    print ("3)Visualizar paciente")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        crear.crear()
        menu()
    elif opcion == 2: 
        registrar.registrar()
        menu()
    elif opcion == 3:
        visualizar.visualizar()
        menu()
    else:
        print ("Opcion no valida")
        menu()

import datetime
import crear
import registrar
import visualizar
menu()