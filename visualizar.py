from otros import organizar_paciente
from otros import organizar_lecturas
from otros import estadisticas
from paciente import Paciente
from sensor import Sensor

def visualizar():
    flag = 0
    s_f = []
    s_t = []
    s_o = []
    f = open('paciente.csv','r')
    paciente = f.readlines()       
    f.close()
    f = open('lecturas.csv','r')
    lecturas = f.readlines()       
    f.close()
    documento = input("\nDocumento del paciente: ")
    for i in range (0,len(paciente)):
        datos = organizar_paciente(i,paciente) 
        try: 
            if documento == datos.documento:
                datos.datos()
                flag = 1
                print("   Fecha  ","|","Hora ","|","FR ","|"," T  ","|"," O ")
                for j in range (0,len(lecturas)):
                    sensores = organizar_lecturas(j,lecturas)
                    if documento == sensores.documento:
                        if int(sensores.fr) >= 100:
                            sensores.parametros1()
                        if int(sensores.fr) < 100:
                            sensores.parametros()
                        if sensores.fr != "---":
                            s_f.append(int(sensores.fr))
                        if sensores.t != "----":
                            s_t.append(float(sensores.t))
                        if sensores.o != "---":
                            s_o.append(float(sensores.o))
                if datos.frecuencia == "s" or datos.frecuencia == "S":
                    estadisticas(s_f,"frecuencia cardiaca","bpm")
                if datos.temperatura == "s" or datos.temperatura == "S":
                    estadisticas(s_t,"temperatura","C")  
                if datos.oximetro == "s" or datos.oximetro == "S":
                    estadisticas(s_o,"oximetria","%")  
        except:
            print("\nEl paciente no tiene lecturas registradas")
    if (flag==0): print("El documento no esta registrado")