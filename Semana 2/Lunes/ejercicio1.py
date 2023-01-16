num1 = input("Please enter number 1: ")
num2 = input("Please enter number 2: ")

if num1.isnumeric():
    num1 = int(num1)
    if num2.isnumeric():
        num2 = int(num2)
        if num2 == 0:
            print("ERROR!! The divisor is 0")
        else:
            print("The result is:", num1/num2)
    else: 
        print("Error num2 no puede ser letras")

else:
    print("Error num1 no puede ser letras")