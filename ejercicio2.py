table = int(input("Please enter what table you want:"))

for number in range(1,11,1):
    print(f"{table} x {number} =",number*table)
    #print(table,number,sep=" x ",end=" ")
    #print("=",number*table)
