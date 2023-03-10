def main():
    lista = ["A","B","C","D","E","F","G","H","I","J"]
    letter = input("Please enter a letter to search: ")
        

    variable = search_in_list(lista, letter,0)
    print(variable)

def search_in_list(lista,letter,index):
    if letter == lista[index]:
        return letter
    elif index == len(lista)-1:
        if letter == lista[index]:
            return letter
        else:
            return None
    
    return search_in_list(lista,letter,index+1)
        


main()