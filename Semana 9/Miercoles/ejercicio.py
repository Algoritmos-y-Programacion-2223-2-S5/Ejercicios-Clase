def main():
    base = input("Please enter the base:")
    exponential = input("Please enter the exponential:")

    variable = calculate(int(base), int(exponential))
    print(variable)

def calculate(base,exponential):
    if exponential == 1:
        return base
    return base * calculate(base,exponential-1)

# base = 2 
# exp = 5

# 2 * calculate(2,4) - 2 * 2 * 2 * 2
# 2 * calculate(2,3) - 2 * 2 * 2
# 2 * calculate(2,2) - 2 * 2
# 2 * calculate(2,1) - 2
# return 2

main()