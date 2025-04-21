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
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
