number = int(input("Please enter a number"))
aux = number -1
acum_value = 0

while aux > 0:
    if number%aux == 0:
        acum_value += aux
    aux-=1

if acum_value > number:
    print("The number",number,"is abundant")
else:
    print("The number",number,"is not abundant")
