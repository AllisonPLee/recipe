def recipe_box():
    ingredients = ["Flour Tortilla Chips: 4 cups", "Ground Cinnamon: 1 tbsp", "Granulated Sugar: 1 tbsp", "Grated Semi-sweet Chocolate: 1 cup", "Grated White Chocolate: 1 cup", "Creme Frianche: 1 cup", "Warm Berry Salsa: 1 cup"]
    instructions = ["Step 1: Preheat oven to 350 degrees F", "Step 2: Mix chips with cinnamon and sugar", "Step 3: Mound nachos on large plate", "Step 4: Top with chocolate", "Step 5: Bake until chocolate melts (8-10 min)", "Step 6: Serve with Creme Friache & Warm Berry Salsa", "Step 7: Enjoy!"]

    creme_ingredients = ["Sour Cream: 1 cup", "Heavy Cream: 1/2 cup", "Confectioners' Sugar: 1/4 cup", "Orange-flavored Liqueur: 2 tbsp"]
    creme_instructions = ["Step 1: Mix everything", "Step 2: Refridgerate for 20-30 min"]

    salsa_ingredients = ["Granulated Sugar: 1/2 cup", "Liqueur: 1 tbsp", "Butter (room temperature): 1 tbsp", "White Wine Vinegar: 1 tbsp", "Blueberries: 1/4 cup", "Rasberries: 1/4 cup", "[Optional] hot sauce, chile-garlic sauce, diced peppers or chile seeds"]
    salsa_instructions = ["Step 1: Boil 1/2 cup of water (high heat)", "Step 2: Reduce heat, add sugar and liqueur", "Step 3: Cook until sugar brown (6-8 min)", "Step 4: Remove from heat, add vinegar and butter", "Step 5: Refridgerate until chilled (10 min)", "Step 6: Add berries & mix", "Step 7: Finish with a splash of spice if desired", "Step 8: Serve warm and enjoy!"]

    print("Main Ingredients")
    for ingredient in ingredients:
        print(ingredient)
    print(" ")

    print("Main Instructions")
    for step in instructions:
        print(step)
    print(" ")

    further_instructions = input("Would you like the recipe for the Creme Friache and/or Warm Berry Salsa? ")
    if further_instructions == "Yes" or further_instructions == "yes":
        print("Creme Friache Ingredients")
        for ingredient in creme_ingredients:
            print(ingredient)
        print(" ")

        print("Creme Friche Instructions")
        for step in creme_instructions:
            print(step)
        print(" ")

        print("Warm Berry Salsa Ingredients")
        for ingredient in salsa_ingredients:
            print(ingredient)
        print(" ")
        
        print("Warm Berry Salsa Instructions")
        for step in salsa_instructions:
            print(step)
    elif further_instructions == "No" or further_instructions == "no":
        print("Enjoy!")
    else:
        print("Sorry, that is not a command.")


recipe_box()
