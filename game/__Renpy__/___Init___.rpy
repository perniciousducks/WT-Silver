

### INIT ###

init -2:

    $ l_blush = False # Turns on blushing in the l_head screen. (Lola).
    $ l_things = False # Turns on cheerful emotion symbol in l_screen. (Lola).
    $ l_question = False # Turns on question mark emotion symbol in l_screen. (Lola).
    $ l_drop = False # Turns on drop emotion symbol in l_screen. (Lola).
    $ l_hearts = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_exclamation = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_tears = False # Turns on tears in l_screen. (Lola).

    $ config.autoreload = False
    
    transform universal_chibi_walk(x,x2,speed,y): #Universal transform for all chibis
        xpos x
        ypos y
        linear speed xpos x2 # linear
    
    transform custom_walk_02(x,x2): #Same custom walk but for Hermione.
        xpos x
        ypos 250
        linear hermione_speed xpos x2 # linear

    transform custom_walk(x,x2): # http://www.renpy.org/wiki/atl 
        xpos x
        ypos 210
        linear snape_speed xpos x2 # linear
        
    transform genie_walk(x,x2): #http://www.renpy.org/wiki/atl 
        xpos x
        ypos 190
        linear snape_speed xpos x2 # linear