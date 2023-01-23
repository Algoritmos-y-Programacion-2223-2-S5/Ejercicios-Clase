print("Welcomeee")
height = int(input("Please enter the height:"))
for i in range(1,height * 2,2):
    if i > 1:
        print(i, end=" ")
    else:
        print(i)
    for j in range(i-2,0,-2):
        if j > 1:
            print(j,end=" ")
        else: 
            print(j)


