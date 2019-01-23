

### INIT ###

init -2:

    python:

        import math

        def notNull(object):
            if object == None or object == "":
                return False
            else:
                return True



    $ config.autoreload = False

    transform fade_in(x, y, speed):
        alpha 0
        xpos x
        ypos y
        linear speed alpha 1
        
    define flash = Fade(0.1, 0.0, 0.5, color="#fff")    
        
    transform move_in(x, speed):
        xpos x
        linear speed xpos 0
        pause speed

    transform universal_chibi_walk(x,x2,speed,y): #Universal transform for all chibis
        xpos x
        ypos y
        linear speed xpos x2 # linear

    transform custom_walk(x,x2):
        xpos x
        ypos 210
        linear speed xpos x2 # linear



    transform genie_walk(x,x2):
        xpos x
        ypos 190
        linear genie_speed xpos x2 # linear

    transform snape_walk(x,x2):
        xpos x
        ypos 210
        linear snape_speed xpos x2 # linear

    transform custom_walk_02(x,x2):
        xpos x
        ypos 250
        linear hermione_speed xpos x2 # linear

    transform susan_walk(x,x2):
        xpos x
        ypos 250
        linear susan_speed xpos x2 # linear
