

### INIT ###

init -2:

    python:

        import math
        import threading

        def notNull(object):
            if object == None or object == "":
                return False
            else:
                return True

    $ daytime = False
    $ interface_color = "gray"
    $ use_cgs = False
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

    transform custom_walk_02(x,x2): # Used for Luna screens
        xpos x
        ypos 250
        linear her_speed xpos x2 # linear



    transform gen_walk_trans(x, x2, y, y2):
        xpos x
        ypos y
        linear gen_speed xpos x2 ypos y2 # linear

    transform sna_walk_trans(x, x2, y, y2):
        xpos x
        ypos y
        linear sna_speed xpos x2 ypos y2 # linear

    transform her_walk_trans(x, x2, y, y2):
        xpos x
        ypos y
        linear her_speed xpos x2 ypos y2 # linear

    transform sus_walk_trans(x, x2, y, y2):
        xpos x
        ypos y
        linear sus_speed xpos x2 ypos y2 # linear

    transform cho_walk_trans(x, x2, y, y2):
        xpos x
        ypos y
        linear cho_speed xpos x2 ypos y2 # linear
        
    transform chibi_fly_idle:
        subpixel True
        
        on show, appear, start:
            yoffset absolute(0)
            ease_back 2.5 yoffset absolute(-10)
            ease_back 2.5 yoffset absolute(10)
            ease_back 2.0 yoffset absolute(0)
            repeat
        
    transform chibi_fly(x, x2, y, y2, speed):
        subpixel True
        
        on show, appear, start:
            parallel:
                xpos x
                ypos y
                ease_quad speed xpos x2 ypos y2

            parallel:
                yoffset absolute(0)
                linear speed/3.0 yoffset absolute(-10)
                linear speed/3.0 yoffset absolute(10)
                linear speed/3.0 yoffset absolute(0)
                repeat
