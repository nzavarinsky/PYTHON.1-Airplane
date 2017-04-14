class Airplane:
    name=None
    type=None
    speed=None
    weight=None
    numOfSeats=None

    def __init__(self, name,type,speed,weight, numOfSeats):
        self.nameOfPlain = name
        self.typeOfPlain = type
        self.speedOfPlain = speed
        self.weightOfPlain = weight
        self.seatsInPlain = numOfSeats

    def resetValues(self, name,type,speed,weight, numOfSeats):
        self.resetName = name
        self.resetType = type
        self.resetSpeed = speed
        self.resetWeight = weight
        self.resetSeats = numOfSeats

    def toString(self):
        plane = Airplane("Ruslan", "Passengers plain", 230, 15000, 10)
        print("Variables before reseting :")
        print("Name : ", plane.nameOfPlain, "\nType : ", plane.typeOfPlain)
        print("Max speed is : ", plane.speedOfPlain, "km/h")
        print("Number of Passengers: ", plane.seatsInPlain, "\nWeight : ", plane.weightOfPlain, "kg")
        print(plane.nameOfPlain, plane.typeOfPlain, plane.speedOfPlain, plane.weightOfPlain, plane.seatsInPlain, "\n")
        plane.resetValues("Mig-125 ", "Military plain ", 400, 7000, 2)
        print("Variables after reseting : ")
        print("Name : ", plane.resetName, "\nType : ", plane.resetType)
        print("Max speed is : ", plane.resetSpeed, "km/h")
        print("Number of Passengers: ", plane.resetSeats,"\nWeight : ", plane.resetWeight, "kg")











