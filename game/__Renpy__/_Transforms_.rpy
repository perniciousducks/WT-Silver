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

transform ton_walk_trans(x, x2, y, y2):
    xpos x
    ypos y
    linear ton_speed xpos x2 ypos y2 # linear

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

transform moveFade:
    subpixel True

    on show, appear, start:
        alpha 0.0
        xoffset 200
        easein_back 1.0 alpha 1.0 xoffset absolute(0)

    on hide:
        alpha 1.0
        xoffset 0
        easeout_back 1.0 alpha 0.0 xoffset absolute(200)

transform basicfade:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.5 alpha 0.0

transform fadeInOut:
    alpha 0.0
    linear 0.15 alpha 1.0
    on hide:
        linear 0.15 alpha 0.0

transform fadeOutOnly:
    on hide:
        linear 0.15 alpha 0.0

transform blink:
    on show:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat

transform pulse:
    on show:
        xzoom 1.0
        yzoom 1.0
        linear 0.8 xzoom 1.2 yzoom 1.2
        linear 0.8 xzoom 1.0 yzoom 1.0
        repeat

transform moveto(start_x=0, start_y=0, target_x, target_y, duration=1.0):
    on show:
        xpos start_x
        ypos start_y
        linear duration xpos target_x ypos target_y
