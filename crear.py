from paciente import Paciente

def crear():
    nombre = input("\nNombre: ")
    documento = input("Documento de identificacion: ")
    sangre = input("Tipo de sangre: ")
    patologia = input("Patologia: ")
    print ("\nSensores conectados (s/n)")
    a=b=c=0
    while a==0 or b==0 or c==0 :
        frecuencia = input("Sensor de frecuencia: ")
        temperatura = input("Sensor de temperatura: ")
        oximetro = input("Sensor oximetro: ")
        if frecuencia == "s" or frecuencia == "n" or frecuencia == "S" or frecuencia == "N":
            a = 1
        else: print("Sensor de frecuencia no valido")
        if temperatura == "s" or temperatura == "n" or temperatura == "S" or temperatura == "N":
            b = 1
        else: print("Sensor de temperatura no valido")
        if temperatura == "s" or temperatura == "n" or temperatura == "S" or temperatura == "N":
            c = 1
        else: print("Sensor oximetro no valido")
    paciente = Paciente(nombre,documento,sangre,patologia,frecuencia,temperatura,oximetro)
    paciente.guardar()