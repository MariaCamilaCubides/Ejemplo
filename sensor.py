import datetime

class Sensor():
    __file1 = "lecturas.csv"
    def __init__(self,documento,fr,t,o): 
        self.documento = documento
        self.fr = fr
        self.t = t
        self.o = o
        self.hora = datetime.datetime.now().strftime("%H:%M")
        self.fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        
    def parametros(self):
        print(self.fecha,"|",self.hora,"| ",self.fr,"|",self.t,"|",self.o)
    
    def parametros1(self):
        print(self.fecha,"|",self.hora,"|",self.fr,"|",self.t,"|",self.o)

    def guardar_lecturas(self):
        try:
            f = open(self.__file1,"a")
            paciente = self.documento+";"+self.fecha+";"+ self.hora+";"+ str(self.fr)+";"+str(self.t)+";"+str(self.o)+"\n"
            f.write(paciente)
            f.close()
        except:
            print("Error en el archivo")