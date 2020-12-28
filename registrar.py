from otros import organizar_paciente
from otros import organizar_lecturas
from paciente import Paciente
from sensor import Sensor

def registrar():
    f = open('paciente.csv','r')
    paciente = f.readlines()       
    f.close()
    flag = 0
    documento = input("\nDocumento del paciente: ") 
    for i in range (0,len(paciente)):
        datos = organizar_paciente(i,paciente)
        if documento == datos.documento:
            flag=1
            datos.datos()
            if datos.frecuencia == "s" or datos.frecuencia == "S":
                f=0
                while f==0:
                    fr = int(input("Frecuencia cardiaca (0 - 120 bpm): "))
                    if (fr>=0 and fr<=120):
                        f=1
                    else:
                        print("Valor no valido")
            else: fr = "---"
            if datos.temperatura == "s" or datos.temperatura == "S":
                f=0
                while f==0:
                    t = float(input("Temperatura (0 - 50 C): "))
                    if (t>=0 and t<=50):
                        f=1
                    else:
                        print("Valor no valido")
            else: t = "----"
            if datos.oximetro == "s" or datos.oximetro == "S":
                f = 0
                while f==0:
                    o = float(input("Oximetro (0 - 99 %): "))
                    if (o>=0 and o<=99):
                        f=1
                    else:
                        print("Valor no valido") 
            else: o = "---"        
            p = Sensor(documento,fr,t,o)
            p.guardar_lecturas()
    if (flag==0): print("El documento no esta registrado") 