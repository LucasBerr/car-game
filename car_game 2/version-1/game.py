
class Carro:
    # método construtor
    def __init__(self, color, plate, yearOfFabrication, maxVelocity):
        self.color = color
        self.plate = plate
        self.yearOfFabrication = yearOfFabrication
        self.velocity = 0
        self.maxVelocity = maxVelocity
        self.marcha = 0
        self.isOn = False
        self.packaging = False

    def __str__(self):
        return f"""Car:
            color:{self.color}
            plate: {self.plate}
            year of fabrication: {self.yearOfFabrication}
            on: {self.isOn}
            velocity: {self.velocity}
            packaging: {self.packaging}
            """

    def ligar(self):
        self.isOn = True
        print("VVVrrrmmmmm")

    def desligar(self):
        self.isOn = False
        print("BBbrlll")

    def OnPackaging(self):
        self.packaging = True
        print("vvuu")

    def OffPackaging(self):
        self.packaging = False
        print("vuoon")

    def carGear(self, carGearNumber):
        if self.packaging == True:
            self.marcha = carGearNumber
            print("Tchack")

    def acellerate(self, time):
        if self.packaging == True:
            if self.velocity + 10 * time > self.maxVelocity:
                print("HHHAAAAAAA")
                self.velocity = 200
            else:
                self.velocity += 10 * time
                print("VRRRRRRRRR")
        else:
            print("HHHHKKKKRRRRRRR")

    def deacellerate(self, time):
        if self.packaging == True:
            if self.velocity - 10 * time < 0:
                print("RRRRRIIIIII")
                self.velocity = 0
            else:
                self.velocity -= 10 * time
                print("FIIiiiii")
        else:
            print("HHHHKKKKRRRRRRR")


class Car_on_game:
    def __init__(self):
        self.notMoving = """
            _______      
           //  ||\ \     
     _____//___||_\ \___ 
     )  _          _    \\
     |_/ \________/ \___|
_______\_/________\_/_______________________
    """
        self.forward = """
            _______  ----
           //  ||\ \    -----
     _____//___||_\ \___   -----
     )  _          _    \\    -----
     |_/ \________/ \___|  -----
_______\_/________\_/_______________________
    """
        self.backward = """
     -----  _______      
   -----   //  ||\ \     
---  _____//___||_\ \___ 
--   )  _          _    \\
--   |_/ \________/ \___|
_______\_/________\_/_______________________
    """
        self.stop = """
     xxx    _______     xxx     
xxxx       //  ||\ \     xxxx
xx   _____//___||_\ \___   xx
xx   )  _          _    \\  xx
xx   |_/ \________/ \___|  xx
_______\_/________\_/_______________________
    """

    def still(self):
        return self.notMoving

    def moving_backwards(self):
        return self.backward

    def move_forward(self):
        return self.forward

    def stopping(self):
        return self.stop

    def turningOn(self):
        return self.notMoving

    def turningOff(self):
        return self.notMoving

class Game:
    def __init__(self):
        self.on = True
        self.options = """
        1 = ligar carro
        2 = desligar carro
        3 = apertar embreagem
        4 = mudar de marcha
        w = Acelerar
        p = Parar
        s = Ré
        o = off
        """

    def is_on(self):
        return self.on

    def show_options(self, car:Car_on_game):
        print(self.options)
        selecao = input("Digite a opcao desejada: ")
        while selecao not in ["1", "2", "3", "w", "p", "s", "o"]:
            selecao = input("Digite a opcao desejada: ")

        match selecao:
            case "1":
                print(car.turningOn())
            case "2":
                print(car.turningOff())
            case "3":
                print("Apertando embreagem")
            case "w":
                print(car.move_forward())

            case "p":
                print(car.stopping())

            case "s":
                print(car.moving_backwards())

            case "o":
                self.on = False





if __name__ == "__main__":
    carrinho = Car_on_game()
    the_game = Game()
    while the_game.is_on() == True:
        the_game.show_options(car=carrinho)