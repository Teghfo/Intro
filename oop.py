class Peguet405:
    count = 0   # class atribute
    
    def __init__(self, type, color = "white", ring= "mamuli", airbag = False) -> None:
        self.type = type
        self.color = color
        self.ring = ring
        self.sandali = None
        self.airbag = airbag

    def print_color(self):
        print(self.color)

    def pomp_benzin(self):
        print("benzin mikeshe")


    def start(self):
        self.pomp_benzin()


p1 = Peguet405("takSuz")
p1.print_color()

p2 = Peguet405("Gazi", color="black")
p2.print_color()





