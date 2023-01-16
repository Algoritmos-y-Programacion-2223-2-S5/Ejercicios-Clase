print("***** WELCOME TO PIZZERIA BELLA NAPOLI *****")
pizza_type = input("Please select a pizza \n1-Vegetarian\n2-Non Vegetarian\n->")
ingredient = ""
if pizza_type == "1":
    ingredient_option = input("Please select an ingredient \n1-Pimiento \n2-Tofu \n->")
    if ingredient_option == "1":
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print("The pizza is vegetarian and has Tomate, Mozzarella and",ingredient)
elif pizza_type == "2":
    ingredient_option = input("Please select an ingredient \n1-Peperoni \n2-Jamon \n3-Salmon \n->")
    if ingredient_option == "1":
        ingredient = "Peperoni"
    elif ingredient_option == "2":
        ingredient = "Jamon"
    else:
        ingredient = "Salmon"
    print("The pizza is non vegetarian and has Tomate, Mozzarella and",ingredient)
    