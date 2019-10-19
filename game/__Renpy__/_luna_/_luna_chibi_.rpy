

### LUNA CHIBI ###

label lun_chibi(action = "", xpos=luna_chibi_xpos, ypos=luna_chibi_ypos, flip=False):
    hide screen luna_blink

    if xpos != luna_chibi_xpos:
        if xpos == "mid":
            $ luna_chibi_xpos_name = "mid"
            $ luna_chibi_xpos = 580
        elif xpos == "desk":
            $ luna_chibi_xpos_name = "desk"
            $ luna_chibi_xpos = 440
        elif xpos == "on_desk":
            $ luna_chibi_xpos_name = "desk"
            $ luna_chibi_xpos = 350
        elif xpos == "door":
            $ luna_chibi_xpos_name = "door"
            $ luna_chibi_xpos = 750
        else:
            $ luna_chibi_xpos = int(xpos)

    if ypos != luna_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ luna_chibi_ypos = 250
        elif ypos == "on_desk":
            $ luna_chibi_ypos = 180
        else:
            $ luna_chibi_ypos = int(ypos)


    if action == "hide":
        pass

    elif action == "leave":
        call play_sound("door")
        hide screen luna_main
        hide screen bld1
        hide screen blktone
        with d3
        pause .5
    else:
        if flip or luna_flip != 1: #Same variable that the main sprite is using. #1 == Default
            $ luna_flip = -1
        else:
            $ luna_flip = 1
        show screen luna_blink

    return



### LUNA CHIBI WALK ###
default lun_speed = 2.0
label lun_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = lun_speed, action = "", loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3

    hide screen luna_walk
    hide screen luna_blink

    if pos1 == "mid":
        $ walk_xpos = 580 #540
    elif pos1 == "desk":
        $ walk_xpos = 440
    elif pos1 == "door":
        $ walk_xpos = 750
    else:
        $ walk_xpos = int(pos1)

    if pos2 == "mid":
        $ luna_chibi_xpos_name = "mid"
        $ walk_xpos2 = 580 #540
    elif pos2 == "desk":
        $ luna_chibi_xpos_name = "desk"
        $ walk_xpos2 = 440
    elif pos2 == "door":
        $ luna_chibi_xpos_name = "door"
        $ walk_xpos2 = 750
    elif pos2 == "leave":
        $ luna_chibi_xpos_name = "door"
        $ walk_xpos2 = 750
        $ loiter = False
    else:
        $ luna_chibi_xpos_name = "mid"
        $ walk_xpos2 = int(pos2)

    $ luna_chibi_ypos = 250
    $ lun_speed = speed # Speed of walking animation. (lower = faster)

    # Luna walks
    if walk_xpos >= walk_xpos2:
        $ luna_flip = 1
    else:
        $ luna_flip = -1
    show screen luna_walk
    $ tmp = lun_speed - redux_pause
    $ renpy.pause(tmp)
    $ luna_chibi_xpos = walk_xpos2
    hide screen luna_walk
    if pos2 == "leave":
        call play_sound("door")
        with d3
        pause.5
    if loiter:
        show screen luna_blink

    return

### LUNA CHIBI SCREENS ###

transform luna_chibi_transform:
    xpos luna_chibi_xpos ypos luna_chibi_ypos xzoom luna_flip zoom (1.0/scaleratio)

screen luna_blink():
    tag luna_chibi
    zorder luna_chibi_zorder
    if luna_wear_top and luna_wear_bottom:
        add "ch_lun blink_a" at luna_chibi_transform
    elif luna_wear_bottom and not luna_wear_top:
        add "characters/luna/chibis/luna_stand_topless.png" at luna_chibi_transform
    elif not luna_wear_top and not luna_wear_bottom:
        add "ch_lun blink_n" at luna_chibi_transform
    elif luna_wear_robe:        
        add "ch_lun blink_robe" at luna_chibi_transform

screen luna_walk():
    tag luna_chibi
    zorder luna_chibi_zorder
    if luna_wear_top and luna_wear_bottom:
        add "ch_lun walk_a" at luna_chibi_transform, custom_walk_02(walk_xpos, walk_xpos2)
    elif luna_wear_bottom and not luna_wear_top:
        pass # No topless walking chibi available
    elif not luna_wear_top and not luna_wear_bottom:
        add "ch_lun walk_n" at luna_chibi_transform, custom_walk_02(walk_xpos, walk_xpos2)
    elif luna_wear_robe:
        add "ch_lun walk_robe" at luna_chibi_transform, custom_walk_02(walk_xpos, walk_xpos2)

default luna_chibi = chibi("luna", ["base"], update_luna_chibi)

init python:
    def update_luna_chibi(chibi):
        if chibi.action == "walk":
            if luna_wear_top and luna_wear_bottom:
                chibi["base"] = "ch_lun walk_a"
            elif luna_wear_bottom and not luna_wear_top:
                pass #TODO Add topless walking chibi for Luna
            elif not luna_wear_top and not luna_wear_bottom:
                chibi["base"] = "ch_lun walk_n"
            elif luna_wear_robe:
                chibi["base"] = "ch_lun walk_robe"
        else:
            if luna_wear_top and luna_wear_bottom:
                chibi["base"] = "ch_lun blink_a"
            elif luna_wear_bottom and not luna_wear_top:
                chibi["base"] = "luna_stand_topless.png"
            elif not luna_wear_top and not luna_wear_bottom:
                chibi["base"] = "ch_lun blink_n"
            elif luna_wear_robe:        
                chibi["base"] = "ch_lun blink_robe"
