

### Cho Chibi ###

label cho_chibi(action = "", xpos=cho_chibi_xpos, ypos=cho_chibi_ypos, flip=False, animation=False):
    $ cho_chibi_status = ""
    $ update_chibi_image("cho")

    if xpos != cho_chibi_xpos:
        if xpos == "mid":
            $ cho_chibi_xpos = 560
        elif xpos == "desk":
            $ cho_chibi_xpos = 440
        elif xpos == "on_desk":
            $ cho_chibi_xpos = 350
        elif xpos == "door":
            $ cho_chibi_xpos = 750
        else:
            $ cho_chibi_xpos = int(xpos)

    if ypos != cho_chibi_ypos:
        if ypos in ("base","default"):
            $ cho_chibi_ypos = 250
        elif ypos == "on_desk":
            $ cho_chibi_ypos = 180
        else:
            $ cho_chibi_ypos = int(ypos)

    # Action command.
    if action == "hide":
        hide screen cho_stand
    elif action == "leave":
        call play_sound("door")
        hide screen cho_main
        hide screen bld1
        hide screen blktone
        hide screen cho_stand
        with d3
        pause .5
    else:
        if action == "fly":
            $ cho_chibi_animation = "fly"
            $ update_chibi_image("cho")
        elif action == "reset":
            $ cho_chibi_animation = None
            $ update_chibi_image("cho")

        if flip: #Same variable that the main sprite is using. #1 == Default
            $ cho_chibi_flip = -1
            show screen cho_stand
        else:
            $ cho_chibi_flip = 1
            show screen cho_stand

    if animation != False:
        $ cho_chibi_animation = animation

    return



### Cho Chibi Walk ###
default cho_speed = 2.0
label cho_walk(xpos=walk_xpos, ypos=walk_ypos, speed=cho_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    $ cho_chibi_status = "move"
    $ update_chibi_image("cho")

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ cho_chibi_xpos = 750
        $ cho_chibi_ypos = 250
        $ cho_chibi_flip = 1
    elif action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = cho_chibi_xpos
    $ walk_ypos = cho_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 560
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

    $ cho_speed = speed #Speed of walking animation. (lower = faster)

    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ cho_chibi_flip = 1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        $ renpy.pause(tmp)
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if loiter:
            $ cho_chibi_status = ""
            $ update_chibi_image("cho")
            show screen cho_stand

    # Walk left to right
    else:
        $ cho_chibi_flip = -1
        show screen cho_walk
        $ tmp = cho_speed - redux_pause
        $ renpy.pause(tmp)
        $ cho_chibi_xpos = walk_xpos2
        $ cho_chibi_ypos = walk_ypos2
        hide screen cho_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.3
            $ cho_chibi_flip = 1
        else:
            if loiter:
                $ cho_chibi_status = ""
                $ update_chibi_image("cho")
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
screen cho_stand():
    tag cho_chibi
    zorder cho_chibi_zorder

    frame:
        style "empty"
        if cho_chibi_animation == "fly":
            at chibi_fly_idle
        add cho_chibi_fix      xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_stand    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_shoes    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_top      xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_bottom   xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        if "quid" in cho_chibi_shoes:
            add cho_chibi_shoes    xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_robe     xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_gloves     xpos cho_chibi_xpos ypos cho_chibi_ypos xzoom cho_chibi_flip zoom (1.0/scaleratio)
        #TODO Put cloth pile on separate screen
        if cho_cloth_pile:
            add "characters/chibis/cloth_pile_r.png" xpos cho_pile_xpos ypos cho_pile_ypos zoom 0.5

screen cho_walk():
    tag cho_chibi
    zorder cho_chibi_zorder

    frame:
        style "empty"
        if cho_chibi_animation == "fly":
            at chibi_fly(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2, speed=cho_speed)
        else:
            at cho_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2)
        add cho_chibi_fix          xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_walk         xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_shoes        xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_top          xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_bottom       xzoom cho_chibi_flip zoom (1.0/scaleratio)
        if "quid" in cho_chibi_shoes:
            add cho_chibi_shoes        xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_robe         xzoom cho_chibi_flip zoom (1.0/scaleratio)
        add cho_chibi_gloves       xzoom cho_chibi_flip zoom (1.0/scaleratio)
    #TODO Put cloth pile on separate screen
    if cho_cloth_pile:
        add "characters/chibis/cloth_pile_r.png" xpos cho_pile_xpos ypos cho_pile_ypos zoom 0.5


default cho_chibi = chibi("cho", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves", "quid_shoes"], update_cho_chibi)

init python:
    # Cho special: fly (fly_idle!), fly_move
    def update_cho_chibi(chibi):
        # Temporary way of assigning chibi.special
        if cho_chibi_animation:
            chibi.special = cho_chibi_animation
            if cho_chibi_status:
                chibi.special += "_" + cho_chibi_status

        if chibi.special == "fly":
            chibi["base"] = "ch_cho fly_idle"
        elif chibi.special == "fly_move":
            chibi["base"] = "ch_cho fly"
        elif chibi.action == "walk":
            chibi["base"] = "ch_cho walk"
        else:
            chibi["base"] = "ch_cho blink"

        if cho_class.get_worn("top"):
            if cho_class.get_cloth("top").id == "top_sweater_1":
                chibi["top"] = "cc_sweater.png"
            else:
                chibi["top"] = "cc_top.png"

        if cho_class.get_worn("bottom"):
            if cho_class.get_cloth("bottom").id in ("pants_long_2", "pants_short_4"):
                if chibi.action == "walk":
                    chibi["bottom"] = "ch_cho trousers"
                else:
                    chibi["bottom"] = "cc_trousers.png"
            else:
                chibi["bottom"] = "cc_skirt.png"

        if cho_class.get_worn("gloves"):
            if cho_class.get_cloth("gloves").id == "quidditch":
                chibi["gloves"] = "cc_gloves.png"

        if cho_class.get_worn("robe"):
            if cho_class.get_cloth("robe").id == "robe_quidditch_1":
                chibi["robe"] = "cc_quid_robe.png"
                if not chibi.special:
                    chibi["fix"] = "cc_quid_robe_fix.png"
            else:
                chibi["robe"] = "cc_robe.png"

        if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"):
            if cho_class.get_worn("gloves") and cho_class.get_cloth("gloves").id == "quidditch":
                if chibi.action == "walk":
                    chibi["quid_shoes"] = "ch_cho walk_quid_shoes"
                else:
                    chibi["quid_shoes"] = "cc_quid_shoes.png"
            else:
                if chibi.action == "walk":
                    chibi["shoes"] = "ch_cho walk_shoes"
                else:
                    chibi["shoes"] = "cc_shoes.png"
