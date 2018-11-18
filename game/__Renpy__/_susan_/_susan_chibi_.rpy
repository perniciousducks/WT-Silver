

### SUSAN CHIBI ###

label sus_chibi(action = "", xpos=susan_chibi_xpos, ypos=susan_chibi_ypos, flip=False):
    hide screen susan_stand

    if xpos != susan_chibi_xpos:
        if xpos == "mid":
            $ susan_chibi_xpos_name = "mid"
            $ susan_chibi_xpos = 560
        elif xpos in ["wardrobe","center","base","default"]: #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ susan_chibi_xpos_name = "mid"
            $ susan_chibi_xpos = 530
        elif xpos == "desk":
            $ susan_chibi_xpos_name = "desk"
            $ susan_chibi_xpos = 440
        elif xpos == "on_desk":
            $ susan_chibi_xpos_name = "desk"
            $ susan_chibi_xpos = 350
        elif xpos == "door":
            $ susan_chibi_xpos_name = "door"
            $ susan_chibi_xpos = 750
        else:
            $ susan_chibi_xpos = int(xpos)

    if ypos != susan_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ susan_chibi_ypos = 250
        elif ypos == "on_desk":
            $ susan_chibi_ypos = 180
        else:
            $ susan_chibi_ypos = int(ypos)


    if action == "hide":
        pass

    elif action == "leave":
        call play_sound("door")
        hide screen susan_main
        hide screen bld1
        hide screen blktone
        with d3
        pause.5

    else:
        if flip or susan_flip != 1: #Same variable that the main sprite is using. #1 == Default
            $ susan_chibi_flip = 1
            show screen susan_stand
        else:
            $ susan_chibi_flip = -1
            show screen susan_stand
        with d3

    return



### SUSAN CHIBI WALK ###

label sus_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = susan_speed, action = "", loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3

    hide screen susan_walk

    hide screen susan_stand

    if pos1 == "mid":
        $ walk_xpos = 580 #540
    elif pos1 == "desk":
        $ walk_xpos = 440
    elif pos1 == "door":
        $ walk_xpos = 750
    else:
        $ walk_xpos = int(pos1)

    if pos2 == "mid":
        $ susan_chibi_xpos_name = "mid"
        $ walk_xpos2 = 580 #540
    elif pos2 == "desk":
        $ susan_chibi_xpos_name = "desk"
        $ walk_xpos2 = 440
    elif pos2 == "door":
        $ susan_chibi_xpos_name = "door"
        $ walk_xpos2 = 750
    elif pos2 == "leave":
        $ susan_chibi_xpos_name = "door"
        $ walk_xpos2 = 750
        $ loiter = False
    else:
        $ susan_chibi_xpos_name = "mid"
        $ walk_xpos2 = int(pos2)

    $ susan_chibi_ypos = 250
    $ susan_speed = speed #Speed of walking animation. (lower = faster)

    #Susan walks
    if walk_xpos >= walk_xpos2: #right to left
        $ susan_chibi_flip = 1
        show screen susan_walk
        $ tmp = susan_speed - redux_pause
        pause tmp
        $ susan_chibi_xpos = walk_xpos2
        hide screen susan_walk
        if loiter:
            show screen susan_stand

    else: #left to right (flipped)
        $ susan_chibi_flip = -1
        show screen susan_walk
        $ tmp = susan_speed - redux_pause
        pause tmp
        $ susan_chibi_xpos = walk_xpos2
        hide screen susan_walk
        if pos2 == "leave":
            call play_sound("door") #Sound of a door opening.
            with d3
            pause.5
        if loiter:
            show screen susan_stand

    return

label susan_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen susan_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen susan_stand
    return



### SUSAN CHIBI SCREENS ###

screen susan_stand:
    tag susan_chibi

    add susan_chibi_stand    xpos susan_chibi_xpos ypos susan_chibi_ypos xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_shoes    xpos susan_chibi_xpos ypos susan_chibi_ypos xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_top      xpos susan_chibi_xpos ypos susan_chibi_ypos xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_bottom   xpos susan_chibi_xpos ypos susan_chibi_ypos xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_robe     xpos susan_chibi_xpos ypos susan_chibi_ypos xzoom susan_chibi_flip zoom (1.0/scaleratio)

    zorder susan_chibi_zorder

screen susan_walk:
    tag susan_chibi

    add susan_chibi_walk         at susan_walk(walk_xpos, walk_xpos2) xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_walk_shoes   at susan_walk(walk_xpos, walk_xpos2) xzoom susan_chibi_flip zoom (1.0/scaleratio)

    add susan_chibi_top          at susan_walk(walk_xpos, walk_xpos2) xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_bottom       at susan_walk(walk_xpos, walk_xpos2) xzoom susan_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_robe         at susan_walk(walk_xpos, walk_xpos2) xzoom susan_chibi_flip zoom (1.0/scaleratio)

    zorder susan_chibi_zorder


label update_susan_chibi_uniform:

    #Clothing
    if susan_wear_top:
        $ susan_chibi_top       = "characters/susan/chibis/sb_cloth_shirt_h.png"
    else:
        $ susan_chibi_top       = "characters/susan/chibis/blank.png"

    if susan_wear_bottom:
        $ susan_chibi_bottom    = "characters/susan/chibis/sb_cloth_skirt.png"
    else:
        $ susan_chibi_bottom    = "characters/susan/chibis/blank.png"

    if susan_wear_robe:
        $ susan_chibi_robe      = "characters/susan/chibis/sb_cloth_robe_h.png"
    else:
        $ susan_chibi_robe      = "characters/susan/chibis/blank.png"

    $ susan_chibi_stand         = "ch_sus blink"

    #Main Chibi
    if susan_wear_bottom or susan_wear_stockings: #With Shoes.
        $ susan_chibi_shoes         = "characters/susan/chibis/sb_walk_01_shoes.png"
        $ susan_chibi_walk_shoes    = "ch_sus walk_shoes"
    else:
        $ susan_chibi_shoes         = "characters/susan/chibis/blank.png"
        $ susan_chibi_walk_shoes    = "characters/susan/chibis/blank.png"


    return
