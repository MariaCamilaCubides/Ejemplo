from paciente import Paciente
from sensor import Sensor

def estadisticas(lista,sensor,unidad):
    print("\nValor maximo de",sensor,": ",max(lista),unidad)
    print("Valor minimo de",sensor,": ",min(lista),unidad)
    print("Valor promedio de",sensor,": ",(sum(lista)/len(lista)),unidad)
    
def organizar_paciente(numero,paciente):
    p1 = paciente[numero]
    a = paciente[numero].find(";")
    b = paciente[numero].find(";",a+1)
    c = paciente[numero].find(";",b+1)
    d = paciente[numero].find(";",c+1)
    e = paciente[numero].find(";",d+1)
    f = paciente[numero].find(";",e+1)
    g = paciente[numero].find("\n")
    datos = Paciente(p1[0:a],p1[a+1:b],p1[b+1:c],p1[c+1:d],p1[d+1:e],p1[e+1:f],p1[f+1:g])
    return datos

def organizar_lecturas(numero,paciente):
    p1 = paciente[numero]
    a = paciente[numero].find(";")
    b = paciente[numero].find(";",a+1)
    c = paciente[numero].find(";",b+1)
    d = paciente[numero].find(";",c+1)
    e = paciente[numero].find(";",d+1)
    f = paciente[numero].find("\n")
    sensores = Sensor(p1[0:a],p1[c+1:d],p1[d+1:e],p1[e+1:f])
    return sensores
