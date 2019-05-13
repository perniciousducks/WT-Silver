

### LUNA CHIBI ###

label lun_chibi(action = "", xpos=luna_chibi_xpos, ypos=luna_chibi_ypos, flip=False):
    hide screen luna_blink
    hide screen luna_blink_f

    if xpos != luna_chibi_xpos:
        if xpos == "mid":
            $ luna_chibi_xpos_name = "mid"
            $ luna_chibi_xpos = 580
        elif xpos in ["wardrobe","center","base","default"]: #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ luna_chibi_xpos_name = "mid"
            $ luna_chibi_xpos = 540
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
        pause.5

    else:
        if flip or luna_flip != 1: #Same variable that the main sprite is using. #1 == Default
            show screen luna_blink_f
        else:
            show screen luna_blink
        with d3

    return



### LUNA CHIBI WALK ###

label lun_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = her_speed, action = "", loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3

    hide screen luna_walk
    hide screen luna_walk_f

    hide screen luna_blink
    hide screen luna_blink_f

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
    $ luna_speed = speed #Speed of walking animation. (lower = faster)

    #Luna walks
    if walk_xpos >= walk_xpos2: #right to left
        #if action == "fly":
            #show screen luna_fly
        #if action == "run":
        #    show screen luna_run
        #else:
        show screen luna_walk
        $ tmp = luna_speed - redux_pause
        $ renpy.pause(tmp)
        $ luna_chibi_xpos = walk_xpos2
        #hide screen luna_fly
        #hide screen luna_run
        hide screen luna_walk
        if loiter:
            show screen luna_blink

    else: #left to right (flipped)
        #if action == "fly":
            #show screen luna_fly_f
        #if action == "run":
        #    show screen luna_run_f
        #else:
        show screen luna_walk_f
        $ tmp = luna_speed - redux_pause
        $ renpy.pause(tmp)
        $ luna_chibi_xpos = walk_xpos2
        #hide screen luna_fly_f
        #hide screen luna_run_f
        hide screen luna_walk_f
        if pos2 == "leave":
            call play_sound("door") #Sound of a door opening.
            with d3
            pause.5
        if loiter:
            show screen luna_blink_f

    return

label luna_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen luna_stand
        hide screen luna_stand_f
        hide screen luna_blink
        hide screen luna_blink_f
        with Dissolve((dissolveTime/10))
    else:
        hide screen luna_stand
        hide screen luna_stand_f
        hide screen luna_blink
        hide screen luna_blink_f
    return



### LUNA CHIBI SCREENS ###

screen luna_chibi():
    tag luna_chibi
    add luna_chibi_stand xpos luna_chibi_xpos ypos luna_chibi_ypos xzoom luna_flip zoom (1.0/scaleratio)
    zorder luna_chibi_zorder
screen luna_blink():
    tag luna_chibi
    add luna_chibi_blink xpos luna_chibi_xpos ypos luna_chibi_ypos zoom (1.0/scaleratio)
    zorder luna_chibi_zorder
screen luna_blink_f():
    tag luna_chibi
    add luna_chibi_blink_f xpos luna_chibi_xpos ypos luna_chibi_ypos zoom (1.0/scaleratio)
    zorder luna_chibi_zorder
screen luna_walk():
    tag luna_chibi
    add luna_chibi_walk at custom_walk_02(walk_xpos, walk_xpos2) zoom (1.0/scaleratio)
    zorder luna_chibi_zorder
screen luna_walk_f():
    tag luna_chibi
    add luna_chibi_walk_f at custom_walk_02(walk_xpos, walk_xpos2) zoom (1.0/scaleratio)
    zorder luna_chibi_zorder


label update_luna_chibi_uniform:

    if luna_wear_top and luna_wear_bottom:
        $ luna_chibi_stand    = "characters/luna/chibis/luna_stand.png"
        $ luna_chibi_blink    = "ch_lun blink_a"
        $ luna_chibi_blink_f  = "ch_lun blink_a_flip"
        $ luna_chibi_walk     = "ch_lun walk_a"
        $ luna_chibi_walk_f   = "ch_lun walk_a_flip"
    elif luna_wear_bottom and not luna_wear_top:
        $ luna_chibi_stand    = "characters/luna/chibis/luna_stand_topless.png"
        $ luna_chibi_blink    = "characters/luna/chibis/luna_stand_topless.png"
        $ luna_chibi_blink_f  = "characters/luna/chibis/luna_stand_topless_flip.png"
        # Add clothing layers individually to the nude body so they can be turned on or off individually (top, skirt, and stockings).
    elif not luna_wear_top and not luna_wear_bottom:
        $ luna_chibi_stand    = "characters/luna/chibis/walk/l_walk_n_01.png"
        $ luna_chibi_blink    = "ch_lun blink_n"
        $ luna_chibi_blink_f  = "ch_lun blink_n_flip"
        $ luna_chibi_walk     = "ch_lun walk_n"
        $ luna_chibi_walk_f   = "ch_lun walk_n_flip"
    elif luna_wear_robe:
        $ luna_chibi_stand    = "characters/luna/chibis/walk/l_walk_robe_01.png"
        $ luna_chibi_blink    = "ch_lun blink_robe"
        $ luna_chibi_blink_f  = "ch_lun blink_robe_flip"
        $ luna_chibi_walk     = "ch_lun walk_robe"
        $ luna_chibi_walk_f   = "ch_lun walk_robe_flip"
    else:
        pass

    return
