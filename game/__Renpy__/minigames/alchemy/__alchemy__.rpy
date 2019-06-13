screen alchemy_screen(ingredient):
    zorder 3
    textbutton ingredient_pos[0].name xalign 0.05 yalign 0.33 action Return(0)
    textbutton ingredient_pos[1].name xalign 0.15 yalign 0.33 action Return(1)
    textbutton ingredient_pos[2].name xalign 0.25 yalign 0.33 action Return(2)
    textbutton ingredient_pos[3].name xalign 0.35 yalign 0.33 action Return(3)
    
    textbutton "ingr" xalign 0.10 yalign 0.10 action Return("ingredient")
    textbutton "garbage" xalign 0.66 yalign 0.33 action Return("garbage")
    
    textbutton "book" xalign 0.10 yalign 0.80 action Return("book")
    
    
    textbutton "brew" xalign 0.5 yalign 0.33 action Return("brew")
    textbutton "cut_board" xalign 0.33 yalign 0.66 action Return("cut_board")
    
    use top_bar_close_button
 
screen display_ingredient(ingredient, align):
    tag ingredient_screen
    zorder 4
    add ingredient.jar xalign align[0] yalign align[1] zoom 0.2
    
screen move_ingredient(ingredient, align, move_align):
    tag ingredient_screen
    zorder 4
    add ingredient.jar zoom 0.2 at move_image(align, move_align)
    
init python: 
    water = ingredient("water")
    stuff = ingredient("stuff")
    
    ingredient_pos = [water, stuff, water, stuff]
    
    water_stuff = recipe([water,stuff])
    stuff_water = recipe([stuff,water])
    
    all_ingredients = [water, stuff]
    all_recipe = [water_stuff, stuff_water]
    
    def start_alchemy():
        recipe_state = 0
        selected_ingredient = None
        holding_ingredient = None
        recipe_done = False
        valid_recipe = []
        for i in range(0, len(all_recipe)):
            valid_recipe.append(all_recipe[i])
        
        while not recipe_done:
            renpy.hide_screen("ingredient_screen")
            if not holding_ingredient == None:
                holding_ingredient.show_screen()
            renpy.show_screen("alchemy_screen", holding_ingredient)
            
            _return = ui.interact()
            
            if isinstance(_return, int):
                selected_ingredient = _return
                holding_ingredient = ingredient_pos[_return].clone()
                
            elif not selected_ingredient == None:
                if _return == "brew":
                    new_valid = []
                    for recipes in valid_recipe:
                        if recipes.validate(holding_ingredient, recipe_state):
                            new_valid.append(recipes)
                    
                    valid_recipe = new_valid
                    print(valid_recipe)
                    if len(valid_recipe) == 1:
                        print("check if you won:")
                    elif len(valid_recipe) == 0:
                        print("youlost")
                        
                elif _return == "cut_board":
                    holding_ingredient = holding_ingredient.update_state(_return) 
                    
                elif _return == "ingredient":
                    renpy.show_screen("list_menu", all_ingredients, "Ingredients")
                    _return = ui.interact()
                    ingredient_pos[selected_ingredient] = _return
                    selected_ingredient = None
                    holding_ingredient = None
                    renpy.hide_screen("list_menu")
                    
                elif _return == "garbage":
                    selected_ingredient = None
                    holding_ingredient = None
                
    