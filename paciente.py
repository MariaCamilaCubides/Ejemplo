class Paciente():
    __file = "paciente.csv"
    def __init__(self,nombre,documento,sangre,patologia,frecuencia,temperatura,oximetro):
        self.nombre = nombre
        self.documento = documento
        self.sangre = sangre
        self.patologia = patologia
        self.frecuencia = frecuencia
        self.temperatura = temperatura
        self.oximetro = oximetro

        
    def datos(self):
        print("\nInformacion del paciente".center(45))
        print("\nNombre: ",self.nombre)
        print("Documento del paciente: ",self.documento)
        print("Tipo de sangre: ",self.sangre)
        print("Patologia: ",self.patologia)
        print("Sensores conectados:")
        if self.frecuencia=="s" or self.frecuencia=="S":
            print("***Sensor de frecuencia")
        if self.temperatura=="s" or self.temperatura=="S":
            print("***Sensor de temperatura")
        if self.oximetro=="s" or self.oximetro=="S":
            print("***Sensor oximetro")
        print("\n")
        
    def guardar (self):
        try:
            f = open(self.__file,"a")
            paciente = self.nombre+";"+self.documento+";"+ self.sangre+";"+ self.patologia+";"+self.frecuencia+";"+self.temperatura+";"+self.oximetro+"\n"
            f.write(paciente)
            f.close()
        except:
            print("Error en el archivo")