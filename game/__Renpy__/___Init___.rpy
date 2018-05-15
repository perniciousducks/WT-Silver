

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
        


    transform cloud_move: #http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 50 # linear
        pause 7
        repeat


    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 130
        choice:
            ypos 150
        choice:
            ypos 150
        linear 30.0 xpos 50 # linear
        pause 2
        repeat

    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 170
        linear 70.0 xpos 50 # linear
        pause 2
        repeat

    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        ypos 160
        linear 50.0 xpos 50 # linear
        pause 2
        repeat
