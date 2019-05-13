

### SUSAN CHIBI ###

label sus_chibi(action = "", xpos=sus_chibi_xpos, ypos=sus_chibi_ypos, flip=False):
    hide screen susan_stand

    if xpos != sus_chibi_xpos:
        if xpos == "mid":
            $ sus_chibi_xpos = 560
        elif xpos in ["wardrobe","center","base","default"]: #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ sus_chibi_xpos = 530
        elif xpos == "desk":
            $ sus_chibi_xpos = 440
        elif xpos == "on_desk":
            $ sus_chibi_xpos = 350
        elif xpos == "door":
            $ sus_chibi_xpos = 750
        else:
            $ sus_chibi_xpos = int(xpos)

    if ypos != sus_chibi_ypos:
        if ypos in ["base","default"]:
            $ sus_chibi_ypos = 250
        elif ypos == "on_desk":
            $ sus_chibi_ypos = 180
        else:
            $ sus_chibi_ypos = int(ypos)


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
        if flip:
            $ sus_chibi_flip = -1
            show screen susan_stand
        else:
            $ sus_chibi_flip = 1
            show screen susan_stand

    return



### SUSAN CHIBI WALK ###

label sus_walk(xpos=walk_xpos, ypos=walk_ypos, speed=sus_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    hide screen susan_walk
    hide screen susan_stand

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ sus_chibi_xpos = 750
        $ sus_chibi_ypos = 250
    if action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = sus_chibi_xpos
    $ walk_ypos = sus_chibi_ypos

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

    $ sus_speed = speed #Speed of walking animation. (lower = faster)


    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ sus_chibi_flip = 1
        show screen susan_walk
        $ tmp = sus_speed - redux_pause
        $ renpy.pause(tmp)
        $ sus_chibi_xpos = walk_xpos2
        $ sus_chibi_ypos = walk_ypos2
        hide screen susan_walk
        if loiter:
            show screen susan_stand

    # Walk left to right
    else:
        $ sus_chibi_flip = -1
        show screen susan_walk
        $ tmp = sus_speed - redux_pause
        $ renpy.pause(tmp)
        $ sus_chibi_xpos = walk_xpos2
        $ sus_chibi_ypos = walk_ypos2
        hide screen susan_walk
        if action == "leave":
            call play_sound("door")
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

screen susan_stand():
    tag susan_chibi

    add susan_chibi_stand    xpos sus_chibi_xpos ypos sus_chibi_ypos xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_shoes    xpos sus_chibi_xpos ypos sus_chibi_ypos xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_top      xpos sus_chibi_xpos ypos sus_chibi_ypos xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_bottom   xpos sus_chibi_xpos ypos sus_chibi_ypos xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_robe     xpos sus_chibi_xpos ypos sus_chibi_ypos xzoom sus_chibi_flip zoom (1.0/scaleratio)

    zorder sus_chibi_zorder

screen susan_walk():
    tag susan_chibi

    add susan_chibi_walk         at sus_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_walk_shoes   at sus_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sus_chibi_flip zoom (1.0/scaleratio)

    add susan_chibi_top          at sus_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_bottom       at sus_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sus_chibi_flip zoom (1.0/scaleratio)
    add susan_chibi_robe         at sus_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sus_chibi_flip zoom (1.0/scaleratio)

    zorder sus_chibi_zorder


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
