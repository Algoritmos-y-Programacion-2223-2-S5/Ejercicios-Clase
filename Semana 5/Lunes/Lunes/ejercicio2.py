
def operation(function, test_list):
    return [x for x in test_list if function(x)]

def main():
    lista = [1,2,3,4,5]
    print(operation(lambda x: x%2==0,lista))

main()