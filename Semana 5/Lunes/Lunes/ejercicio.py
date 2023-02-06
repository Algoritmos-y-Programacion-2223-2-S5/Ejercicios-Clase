def operation(function, test_list):
    return [function(x) for x in test_list]

def main():
    lista = [1,2,3,4,5]
    print(operation(lambda x: x**2,lista))

main()