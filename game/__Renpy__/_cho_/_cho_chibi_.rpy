### cho CHIBI ###
label cho_chibi(action = "", xpos=cho_chibi_xpos, ypos=cho_chibi_ypos, flip=False, animation=False):
    hide screen cho_stand

    if xpos != cho_chibi_xpos:
        if xpos == "mid":
            $ cho_chibi_xpos = 560
        elif xpos in ["wardrobe","center","base","default"]: #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ cho_chibi_xpos = 530
        elif xpos == "desk":
            $ cho_chibi_xpos = 440
        elif xpos == "on_desk":
            $ cho_chibi_xpos = 350
        elif xpos == "door":
            $ cho_chibi_xpos = 750
        else:
            $ cho_chibi_xpos = int(xpos)

    if ypos != cho_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ cho_chibi_ypos = 250
        elif ypos == "on_desk":
            $ cho_chibi_ypos = 180
        else:
            $ cho_chibi_ypos = int(ypos)


    if action == "hide":
        pass

    elif action == "leave":
        call play_sound("door")
        hide screen cho_main
        hide screen bld1
        hide screen blktone
        with d3
        pause.5

    else:
        if flip or cho_flip != 1: #Same variable that the main sprite is using. #1 == Default
            $ cho_chibi_flip = -1
            show screen cho_stand
        else:
            $ cho_chibi_flip = 1
            show screen cho_stand
            
    if animation != False:
        $ cho_chibi_animation = animation

    return

### cho CHIBI WALK ###
label cho_walk(xpos=walk_xpos, ypos=walk_ypos, speed=cho_speed, action="", loiter=True, redux_pause=0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3

    hide screen cho_walk
    hide screen cho_stand

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ cho_chibi_xpos = 750
        $ cho_chibi_ypos = 250
    if action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = cho_chibi_xpos
    $ walk_ypos = cho_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 580 #540
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ["base","default"]:
        $ walk_ypos2 = 250
    else:
        $ walk_ypos2 = int(ypos)

    $ cho_speed = speed #Speed of walking animation. (lower = faster)

    #cho walks
    if walk_xpos >= walk_xpos2: #right to left
        $ cho_chibi_flip = 1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        pause tmp
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if loiter:
            show screen cho_stand

    else: #left to right (flipped)
        $ cho_chibi_flip = -1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        pause tmp
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if action == "leave":
            call play_sound("door") #Sound of a door opening.
            with d3
            pause.5
        if loiter:
            show screen cho_stand

    return

label cho_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen cho_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen cho_stand
    return

### CHO CHIBI SCREENS ###
screen cho_stand:
    tag cho_chibi

    add cho_chibi_stand    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_shoes    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_top      xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_bottom   xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_robe     xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)

    zorder cho_chibi_zorder

screen cho_walk:
    tag cho_chibi

    add cho_chibi_walk         at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_walk_shoes   at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom cho_chibi_flip zoom (1.0/scaleratio)

    add cho_chibi_top          at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_bottom       at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom cho_chibi_flip zoom (1.0/scaleratio)
    add cho_chibi_robe         at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom cho_chibi_flip zoom (1.0/scaleratio)

    zorder cho_chibi_zorder



label flying_cho_chibi(flying=True):

    if flying == True:
        $ cho_chibi_stand  = "ch_hem fly_a" # Temporarily
        $ cho_chibi_walk   = "characters/hermione/chibis/broom/shime14.png" # Temporarily

        $ cho_chibi_top       = "characters/cho/chibis/blank.png"
        $ cho_chibi_bottom    = "characters/cho/chibis/blank.png"
        $ cho_chibi_robe      = "characters/cho/chibis/blank.png"

        $ cho_chibi_shoes         = "characters/cho/chibis/blank.png"
        $ cho_chibi_walk_shoes    = "characters/cho/chibis/blank.png"

    elif flying == False:
        call update_cho_chibi_uniform

    return

label update_cho_chibi_uniform:
    #Clothing
    if cho_class.get_worn("top"):
        $ cho_chibi_top       = "characters/cho/chibis/cc_cloth_shirt_r.png"
    else:
        $ cho_chibi_top       = "characters/cho/chibis/blank.png"

    if cho_class.get_worn("bottom"):
        $ cho_chibi_bottom    = "characters/cho/chibis/cc_cloth_skirt.png"
    else:
        $ cho_chibi_bottom    = "characters/cho/chibis/blank.png"

    if cho_class.get_worn("robe"):
        $ cho_chibi_robe      = "characters/cho/chibis/cc_cloth_robe_r.png"
    else:
        $ cho_chibi_robe      = "characters/cho/chibis/blank.png"

    $ cho_chibi_stand         = "ch_cho blink"

    #Main Chibi
    if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"): #With Shoes.
        $ cho_chibi_shoes         = "characters/cho/chibis/cc_walk_01_shoes.png"
        $ cho_chibi_walk_shoes    = "ch_cho walk_shoes"
    else:
        $ cho_chibi_shoes         = "characters/cho/chibis/blank.png"
        $ cho_chibi_walk_shoes    = "characters/cho/chibis/blank.png"

    return
