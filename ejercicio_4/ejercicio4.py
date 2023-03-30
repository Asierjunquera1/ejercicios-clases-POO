class Logger:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.numero_registros = 0
        self.archivo = open(self.nombre_archivo, 'w')
        self.archivo.write('--Inicio del registro--\n')
        self.archivo.close()

    def log(self, mensaje):
        self.numero_registros += 1
        self.archivo = open(self.nombre_archivo, 'a')
        self.archivo.write(mensaje + '\n')
        self.archivo.close()

    def __del__(self):
        self.archivo = open(self.nombre_archivo, 'a')
        self.archivo.write('--Fin del registro: {} registros--\n'.format(self.numero_registros))
        self.archivo.close()

class Test:
    def __init__(self):
        self.logger = Logger('registro.txt')

    def llamada(self, mensaje):
        self.logger.log(mensaje)
