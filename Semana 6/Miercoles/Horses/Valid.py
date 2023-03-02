class Valid:
    def __init__(self,number,race_list):
        self.number = number
        self.races = race_list

    def start_valid(self):
        print("Estamos iniciando la valida", self.number)
        for race in self.races:
            race.start_race()
            race.finish_race()
