import math

def print_result(function, number):
    for x in range(number+1):
        print(function(x))

def main():
    while True:
        number = int(input("Please enter a number to validate:"))
        option = int(input("Please enter a option to continue \n1-Sin\n2-Cos\n3-Tan\n4-Exp\n5-Logn\n6-Exit\n-->"))
        if option == 1:
            print_result(math.sin,number)
        elif option == 2:
            print_result(math.cos,number)
        elif option == 3:
            print_result(math.tan,number)
        elif option == 4:
            print_result(math.exp,number)
        elif option == 5:
            print_result(math.log,number)
        elif option == 6:
            break
        else:
            print("Invalid option please try again")

main()