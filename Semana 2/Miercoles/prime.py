number = int(input("Please enter a number"))
aux = number -1
isPrime = True

if number <= 1:
    isPrime = False 
else:
    while aux > 1:
        if number%aux == 0:
            isPrime = False

        aux-=1

if isPrime:
    print("The number",number,"is prime")
else:
    print("The number",number,"is not prime")
