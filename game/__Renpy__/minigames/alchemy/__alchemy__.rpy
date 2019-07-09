screen alchemy_screen(ingredient):
    zorder 3
    $ alchemy_zoom = 0.25
    add "interface/alchemy/Desk.png" zoom 0.25
    add "interface/alchemy/Firepit_glow.png" zoom 0.25
    
    for i in range(0,4):
        imagebutton:
            xpos 30 +(ingredient_pos[i].ranx*i)
            ypos 120 + ingredient_pos[i].rany + (-30*(i%2))
            focus_mask True
            idle scale_multi(ingredient_pos[i].jar, alchemy_zoom)
            hover im.MatrixColor(scale_multi(ingredient_pos[i].jar, alchemy_zoom),im.matrix.brightness(0.12))
            action Return(i)
    
    imagebutton:
        focus_mask True
        idle scale_multi("interface/alchemy/Book.png", alchemy_zoom)
        hover im.MatrixColor(scale_multi("interface/alchemy/Book.png", alchemy_zoom),im.matrix.brightness(0.12))
        action Return("book")
        
    imagebutton:
        focus_mask True
        idle scale_multi("interface/alchemy/Bellows.png", alchemy_zoom)
        hover im.MatrixColor(scale_multi("interface/alchemy/Bellows.png", alchemy_zoom),im.matrix.brightness(0.12))
        action Return("bellow")
        
    imagebutton:
        focus_mask True
        idle scale_multi("interface/alchemy/Pestle_and_Mortar.png", alchemy_zoom)
        hover im.MatrixColor(scale_multi("interface/alchemy/Pestle_and_Mortar.png", alchemy_zoom),im.matrix.brightness(0.12))
        action Return("mortar")
        
    imagebutton:
        focus_mask True
        idle scale_multi("interface/alchemy/Chopping_Board.png", alchemy_zoom)
        hover im.MatrixColor(scale_multi("interface/alchemy/Chopping_Board.png", alchemy_zoom),im.matrix.brightness(0.12))
        action Return("cut_board")
    
    add Solid((31,43,51)) zoom 0.1 xpos 675 ypos 200 rotate 90
    add im.MatrixColor(im.Scale("interface/alchemy/one_pixel.png", 40, 50,  bilinear=False), im.matrix.tint(0.1, 0.5, 0.15)) xpos 720 ypos 250
    
    imagebutton:
        focus_mask True
        idle scale_multi("interface/alchemy/Cauldron.png", alchemy_zoom)
        hover im.MatrixColor(scale_multi("interface/alchemy/Cauldron.png", alchemy_zoom),im.matrix.brightness(0.12))
        action Return("brew")
    
    
    imagebutton:
        xpos 59
        ypos 15
        idle "interface/topbar/buttons/" +interface_color+ "/ui_delete.png"
        hover im.MatrixColor("interface/topbar/buttons/" +interface_color+ "/ui_delete.png",im.matrix.brightness(0.12))
        action Return("garbage")
        
    imagebutton:
        xpos 15
        ypos 15
        idle "interface/topbar/buttons/" +interface_color+ "/ui_inv.png"
        hover im.MatrixColor("interface/topbar/buttons/" +interface_color+ "/ui_inv.png",im.matrix.brightness(0.12))
        action Return("ingredient")

    use top_bar_close_button
 
screen display_ingredient(ingredient, align):
    tag ingredient_screen
    zorder 4
    add ingredient.jar xalign align[0] yalign align[1] zoom 0.2 rotate 315
    
screen move_ingredient(ingredient, align, move_align):
    tag ingredient_screen
    zorder 4
    add ingredient.jar zoom 0.2 rotate 315 at move_image(align, move_align)
    
init python: 
    water = ingredient("water")
    stuff = ingredient("stuff")
    
    ingredient_pos = [water.clone(), stuff.clone(), water.clone(), stuff.clone()]
    
    recipe_book = book_readable_class("Snakes recipes for dymmies", [])
    
    water_stuff = recipe([water,stuff], "Water Brew", "A potion based on water and stuff very simple to make just put water and then stuff into the coldron.")
    stuff_water = recipe([stuff,water], "Stuff Brew", "Something something dark side")
    
    
    
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
                    ingredient_pos[selected_ingredient] = _return.clone()
                    selected_ingredient = None
                    holding_ingredient = None
                    renpy.hide_screen("list_menu")
                    
                elif _return == "garbage":
                    selected_ingredient = None
                    holding_ingredient = None
                    
            elif _return == "book":
                renpy.call("book_handle", recipe_book)
                 
            elif _return == "Close":
                renpy.hide_screen("alchemy_screen")
                renpy.jump("return_office")
                print("works")
                
    