

#Cho Chibi

#Stand
image ch_cho blink:
    "characters/cho/chibis/cc_walk_01.png"
    pause 2
    "characters/cho/chibis/cc_stand_blink.png"
    pause.08
    "characters/cho/chibis/cc_walk_01.png"
    pause 5
    "characters/cho/chibis/cc_stand_blink.png"
    pause.08
    "characters/cho/chibis/cc_walk_01.png"
    pause.08
    "characters/cho/chibis/cc_stand_blink.png"
    pause.08
    "characters/cho/chibis/cc_walk_01.png"
    pause 3

    repeat

 #Walk
image ch_cho walk: #No shoes.
    "characters/cho/chibis/cc_walk_01.png"
    pause.08
    "characters/cho/chibis/cc_walk_02.png"
    pause.08
    "characters/cho/chibis/cc_walk_03.png"
    pause.08
    "characters/cho/chibis/cc_walk_02.png"
    pause.08
    "characters/cho/chibis/cc_walk_01.png"
    pause.08
    "characters/cho/chibis/cc_walk_04.png"
    pause.08
    "characters/cho/chibis/cc_walk_05.png"
    pause.08
    "characters/cho/chibis/cc_walk_04.png"
    pause.08

    repeat

image ch_cho walk_shoes: #With Shoes.
    "characters/cho/chibis/cc_walk_01_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_03_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_01_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_05_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_shoes.png"
    pause.08

    repeat

### FLYING ANIMATIONS ###
transform chibi_fly_idle:
    subpixel True
    
    on show, appear, start:
        yoffset absolute(0)
        ease_back 2.5 yoffset absolute(-10)
        ease_back 2.5 yoffset absolute(10)
        ease_back 2.0 yoffset absolute(0)
        repeat
        
transform chibi_fly(x, x2, y, y2):
    subpixel True
    
    on show, appear, start:
        parallel:
            xpos x
            ypos y
            ease_quad cho_speed xpos x2 ypos y2

        parallel:
            yoffset absolute(0)
            linear cho_speed/3.0 yoffset absolute(-10)
            linear cho_speed/3.0 yoffset absolute(10)
            linear cho_speed/3.0 yoffset absolute(0)
            repeat
        
image ch_cho fly:
    "characters/cho/chibis/cc_fly.png"
    
image ch_cho fly_idle:
    contains chibi_fly_idle
    "characters/cho/chibis/cc_fly_idle.png" 