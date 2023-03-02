import random

class Race:
    def __init__(self,number,horse_list):
        self.number = number
        self.horses = horse_list

    def start_race(self):
        print("Esta por comenzar la carrera", self.number)
        print("PARTIDAAAAAAAAAAAAAAAAAAAAAA SALIERON LOS CABALLOS")
        for horse in self.horses: 
            print(horse.name)


    def finish_race(self):
        print("The winner is:",random.choice(self.horses).name)

