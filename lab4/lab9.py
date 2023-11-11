class IceCream():
    def __init__(self, packaged:bool, mainingridient:str):
        self.packeged = packaged
        self.mainingridient = mainingridient
        
class Popsicle(IceCream):
    def __init__(self, packaged: bool, mainingridient: str,rate:float):
        self.rate = rate
        super().__init__(packaged, mainingridient)
    
product = Popsicle(True,"Ice Juice",6.7)       
print(product.__dict__)

# najpierw jest wykonywana inicjalizacja w inicjalizacja w klasie dziedziczącej(self.rate) a potem po wykonywaniu super()
# z klasy  nadrzędnej (self.packeged oraz self.mainingridient)