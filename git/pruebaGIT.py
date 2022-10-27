class personas():
    def __init__(self, nombre, peso, altura, pais_de_origen) -> None:
        self.name = nombre
        self.weight = peso
        self.height = altura
        self.nationality = pais_de_origen
    
    def bmi(self):
        bmi = self.weight / (self.height ** 2)
        print(bmi)
        


Felipe = personas('Felipe', 70, 1.79, "Colombia")   
print(Felipe.nationality)
print(Felipe.height)
print(Felipe.name)
print(Felipe.bmi())

    