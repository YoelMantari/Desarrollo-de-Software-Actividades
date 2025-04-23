class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("No se puede comer una cantidad negativa de pepinos.")
        if pepinos > 1000:
            raise ValueError("No se puede comer más de 1000 pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        suficiente_tiempo = self.tiempo_esperado >= 1.5
        suficientes_pepinos = self.pepinos_comidos > 10
        return suficiente_tiempo and suficientes_pepinos
    
    def obtener_pepinos_comidos(self):
        return self.pepinos_comidos