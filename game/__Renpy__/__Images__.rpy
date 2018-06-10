init:
    image ch_hem 01 = "characters/hermione/chibis/walk/h_walk_a_01.png"

    image check_07 = "interface/check_07.png"
    image check_08 = "interface/check_08.png"
    
    image heart_00 = "interface/heart_00.png"
    image heart_01 = "interface/heart_01.png"
    image heart_02 = "interface/heart_02.png"
    image heart_03 = "interface/heart_03.png"
    image heart_04 = "interface/heart_04.png"
    
    image textheart = "interface/textheart.png"
    
### UNIVERSAL ANIMATION ###
label __init_variables:
    
    if not hasattr(renpy.store,'u_ani_pause_img'):
        $ u_ani_pause_img = ""
        $ u_ani_play_img = ""
        $ u_ani_xpos = 1
        $ u_ani_ypos = 1
        
    return
    
label set_u_ani(play = u_ani_play_img, pause = u_ani_pause_img, xpos = u_ani_xpos, ypos = u_ani_ypos):
    if play != u_ani_play_img:
        $ u_ani_play_img = play
    if pause != u_ani_pause_img:
        $ u_ani_pause_img = pause
    if xpos != u_ani_xpos:
        $ u_ani_xpos = xpos
    if ypos != u_ani_ypos:
        $ u_ani_ypos = ypos
    return
    
label u_play_ani:
    hide screen u_ani_pause
    show screen u_ani_play
    with d3
    return
label u_pause_ani:
    hide screen u_ani_play
    show screen u_ani_pause
    with d3
    return
    
label u_end_ani:
    hide screen u_ani_play
    hide screen u_ani_pause
    with d3
    return
    
screen u_ani_pause: 
    tag u_animation
    add u_ani_pause_img at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)

screen u_ani_play: 
    tag u_animation
    add u_ani_play_img at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
