init:
    transform move_image(align, new_align):
        xalign align[0]
        yalign align[1]

        linear 2.0 xalign new_align[0] yalign new_align[1]


init -1 python:
    class ingredient(item_class):
        jar = "interface/icons/item_potion.png"
        imagepath = "interface/icons/item_lollipop.png"
        name = ""
        current_state = "hand"
        cut_ingredient = None
        number = 4
        def __init__(self, ingredient):
            self.name = ingredient
            
        def update_state(self, new_state):
            if new_state == "cut_board":
                if self.current_state == new_state:
                    return self.cut_ingredient
                self.current_state = new_state
                return self
            
        def __eq__(self, other):
            ##Overrides the default == implementation##
            if isinstance(other, ingredient):
                return self.ingredient == other.ingredient
            return False
            
        def show_screen(self):
            renpy.hide_screen("display_ingredient")
            if self.current_state == "hand":
                renpy.show_screen("display_ingredient", self, (0.5,0.5))
            elif self.current_state == "cut_board":
                renpy.show_screen("move_ingredient", self, (0.5,0.5), (0.33,0.66))
                renpy.pause(2)
                renpy.hide_screen("move_ingredient")
                renpy.show_screen("display_ingredient", self, (0.33,0.66))
        
        def clone(self):
            return ingredient(self.name)
        
    class recipe:
        recipe_steps =[]
        finish_label =""
        
        
        def __init__(self, recipe):
            self.recipe_steps = recipe
        
        def validate(self, action, current_state):
            if self.recipe_steps[current_state] == action:
                return True
            return False
              
        
            
        
        
    def lerp_color(color1, color2, time):
        return Color((float(color1[0]+(color2[0]-color1[0])*time),int(color1[1]+(color2[1]-color1[1])*time),int(color1[2]+(color2[2]-color1[2])*time)))
    
    