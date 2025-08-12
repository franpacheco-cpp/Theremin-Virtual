class Theremin:
    #diccionario privado
    __notas = {
        "DO3": 130, "DO#3": 138, "RE3": 146, "RE#3": 155, "MI3": 164,
        "FA3": 174, "FA#3": 185, "SOL3": 196, "SOL#3": 207,
        "LA3": 220, "LA#3": 233, "SI3": 246, "DO4": 261
    }
    #init
    def __init__(self, frecuencia, amplitud, estado, MIDI=False, notaActual=""):
        self.__frecuencia = frecuencia
        self.__amplitud = amplitud
        self.__estado = estado
        self.__MIDI = MIDI
        self.__notaActual = notaActual

    #getters
    def get_frecuencia(self):
        return self.__frecuencia

    def get_amplitud(self):
        return self.__amplitud

    def get_estado(self):
        return self.__estado

    def get_MIDI(self):
        return self.__MIDI

    def get_notaActual(self):
        return self.__notaActual

    #setters
    def set_frecuencia(self, frecuencia):
        self.__frecuencia = frecuencia

    def set_amplitud(self, amplitud):
        #limita amplitud entre 0 y 1
        if amplitud < 0:
            amplitud = 0
        elif amplitud > 1:
            amplitud = 1
        self.__amplitud = amplitud

    def set_estado(self, estado):
        self.__estado = estado

    def set_MIDI(self, MIDI):
        self.__MIDI = MIDI

    def set_notaActual(self, notaActual):
        self.__notaActual = notaActual

    #métodos
    def cambiarFrecuencia(self, deltaFrecuencia):
        nueva_freq = self.get_frecuencia() + deltaFrecuencia
        if nueva_freq < 20:  #límite inferior audible aprox
            nueva_freq = 20
        self.set_frecuencia(nueva_freq)

    def cambiarAmplitud(self, deltaAmplitud):
        nueva_amp = self.get_amplitud() + deltaAmplitud
        self.set_amplitud(nueva_amp)

    def conectar(self):
        self.set_estado(not self.get_estado())

    def conectarMIDI(self):
        self.set_MIDI(not self.get_MIDI())

    def __encontrarNota(self):
        #busca la nota más cercana a la frecuencia actual
        freq = self.get_frecuencia()
        notas = self.__notas
        nota_cercana = min(notas.items(), key=lambda x: abs(x[1] - freq))
        self.set_notaActual(nota_cercana[0])

    def emitir(self):
        if self.get_estado() and self.get_frecuencia() > 0 and self.get_amplitud() > 0:
            self.__encontrarNota()
            return f"Emitiendo nota {self.get_notaActual()} a {self.get_frecuencia():.2f} Hz con amplitud {self.get_amplitud():.2f}"
        else:
            return "No se puede emitir: Theremin apagado o parámetros inválidos."

    #método mágico
    def __str__(self):
        if self.get_estado():
            if self.get_MIDI():
                return f'Theremin encendido con frecuencia {str(self.get_frecuencia())}hz y amplitud de {str(self.get_amplitud())}. Dispositivo MIDI conectado.'
            else:
                return f'Theremin encendido con frecuencia {str(self.get_frecuencia())}hz y amplitud de {str(self.get_amplitud())}.'
        else:
            return f'Theremin apagado'
