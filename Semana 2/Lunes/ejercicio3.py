num1 = input("Please enter a number to validate: ")

if num1.isnumeric():
    num1 = int(num1)
    if num1%2==0:
        print("The number",num1,"is even")
    else:
        print("The number",num1,"is odd")

else: 
    print("ERROR")