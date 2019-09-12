

### Tonks Chibi ###

label ton_chibi(action = "", xpos=ton_chibi_xpos, ypos=ton_chibi_ypos, flip=False, animation=False):
    $ ton_chibi_status = ""
    $ update_chibi_image("tonks")

    if xpos != ton_chibi_xpos:
        if xpos == "mid":
            $ ton_chibi_xpos = 540 # 560
        elif xpos in ("wardrobe","center","base","default"): #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ ton_chibi_xpos = 530
        elif xpos == "desk":
            $ ton_chibi_xpos = 440
        elif xpos == "on_desk":
            $ ton_chibi_xpos = 350
        elif xpos == "door":
            $ ton_chibi_xpos = 750
        else:
            $ ton_chibi_xpos = int(xpos)

    if ypos != ton_chibi_ypos:
        if ypos in ("base","default"):
            $ ton_chibi_ypos = 250
        elif ypos == "on_desk":
            $ ton_chibi_ypos = 180
        else:
            $ ton_chibi_ypos = int(ypos)

    # Action command.
    if action == "hide":
        hide screen ton_stand
    elif action == "leave":
        call play_sound("door")
        hide screen ton_main
        hide screen bld1
        hide screen blktone
        hide screen ton_stand
        with d3
        pause.5

    else:
        if action == "reset":
            $ ton_chibi_animation = None
            $ update_chibi_image("tonks")

        if flip: #Same variable that the main sprite is using. #1 == Default
            $ ton_chibi_flip = -1
            show screen ton_stand
        else:
            $ ton_chibi_flip = 1
            show screen ton_stand

    if animation != False:
        $ ton_chibi_animation = animation

    return



### Tonks Chibi Walk ###

label ton_walk(xpos=walk_xpos, ypos=walk_ypos, speed=ton_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    $ ton_chibi_status = "move"
    $ update_chibi_image("tonks")

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ ton_chibi_xpos = 750
        $ ton_chibi_ypos = 250
        $ ton_chibi_flip = 1
    elif action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = ton_chibi_xpos
    $ walk_ypos = ton_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 540 # 560
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ("base","default"):
        $ walk_ypos2 = 250
    else:
        $ walk_ypos2 = int(ypos)

    $ ton_speed = speed #Speed of walking animation. (lower = faster)

    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ ton_chibi_flip = 1
        show screen ton_walk
        $ tmp = ton_speed - redux_pause
        $ renpy.pause(tmp)
        $ ton_chibi_xpos = walk_xpos2
        $ ton_chibi_ypos = walk_ypos2
        hide screen ton_walk
        if loiter:
            $ ton_chibi_status = ""
            $ update_chibi_image("tonks")
            show screen ton_stand

    # Walk left to right
    else:
        $ ton_chibi_flip = -1
        show screen ton_walk
        $ tmp = ton_speed - redux_pause
        $ renpy.pause(tmp)
        $ ton_chibi_xpos = walk_xpos2
        $ ton_chibi_ypos = walk_ypos2
        hide screen ton_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.3
            $ ton_chibi_flip = 1
        else:
            if loiter:
                $ update_chibi_image("tonks")
                $ ton_chibi_status = ""
                show screen ton_stand

    return


label ton_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen ton_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen ton_stand
    return



### TONKS CHIBI SCREENS ###

screen ton_stand():
    tag ton_chibi
    zorder ton_chibi_zorder

    frame:
        style "empty"
        if ton_chibi_animation == "fly":
            at chibi_fly_idle
        add ton_chibi_fix      xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_stand    xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_bottom   xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_shoes    xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_top      xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_robe     xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_gloves     xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        if ton_cloth_pile:
            add "characters/chibis/cloth_pile_r.png" xpos ton_pile_xpos ypos ton_pile_ypos

screen ton_walk():
    tag ton_chibi
    zorder ton_chibi_zorder

    frame:
        style "empty"
        if ton_chibi_animation == "fly":
            at chibi_fly(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2, speed=ton_speed)
        else:
            at ton_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2)
        add ton_chibi_fix          xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_walk         xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_bottom       xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_shoes        xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_top          xzoom ton_chibi_flip zoom (1.0/scaleratio)
        if "quid" in ton_chibi_shoes:
            add ton_chibi_shoes        xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_robe         xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_gloves       xzoom ton_chibi_flip zoom (1.0/scaleratio)
    if ton_cloth_pile:
        add "characters/chibis/cloth_pile_r.png" xpos ton_pile_xpos ypos ton_pile_ypos

screen with_tonks_animated():
    tag tonks_chibi
    if daytime:
        add "genie_toast_goblet_daytime" at Position(xpos=435, ypos=200)
    else:
        add "genie_toast_goblet" at Position(xpos=435, ypos=200)
    add "snape_toast_goblet" at Position(xpos=618, ypos=200) # TODO: Add correct Chibi images.

    zorder 3