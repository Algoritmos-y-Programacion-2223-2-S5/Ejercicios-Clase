from Horse import Horse
from Race import Race
from Valid import Valid

def create_horses():
    return [
        Horse("Rayo Veloz"),
        Horse("Rucio Moro"),
        Horse("Caballo Viejo"),
        Horse("Palo de agua"),
        Horse("Perro loco"),
        Horse("McQueen")
    ]

def create_race(number):
    return Race(number,create_horses())

def create_valid(valid_number,race_quantity):
    race_list = []
    for number in range(1,race_quantity+1):
        race_list.append(create_race(number))
    return Valid(valid_number,race_list)

def main():
    print("**** WELCOME TO KENTUCKY DERBY ****")
    race_quantity = int(input("How many races do you want in each valid: "))
    valid5 = create_valid(5,race_quantity)
    valid6 = create_valid(6,race_quantity)
    valid5.start_valid()
    valid6.start_valid()


main()