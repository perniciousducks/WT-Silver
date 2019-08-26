

screen with_tonks_animated():
    tag tonks_chibi
    add "genie_toast_goblet" at Position(xpos=435, ypos=200)
    add "snape_toast_goblet" at Position(xpos=618, ypos=200) # TODO: Add correct Chibi images.

    zorder 3

screen tonks_chibi_large(xx=nxpos, yy=nypos):
    tag tonks_chibi
    add "characters/tonks/chibis/nt_walk_large.png" xpos xx ypos yy zoom (1.0/scaleratio)
    zorder 3



### Tonks Chibi ###
label ton_chibi(action = "", xpos=ton_chibi_xpos, ypos=ton_chibi_ypos, flip=False, animation=False):
    $ ton_chibi_status = ""
    $ update_chibi_image("tonks")

    if xpos != ton_chibi_xpos:
        if xpos == "mid":
            $ ton_chibi_xpos = 560
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
        add ton_chibi_shoes    xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_top      xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_bottom   xpos ton_chibi_xpos ypos ton_chibi_ypos xzoom ton_chibi_flip zoom (1.0/scaleratio)
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
        add ton_chibi_shoes        xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_top          xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_bottom       xzoom ton_chibi_flip zoom (1.0/scaleratio)
        if "quid" in ton_chibi_shoes:
            add ton_chibi_shoes        xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_robe         xzoom ton_chibi_flip zoom (1.0/scaleratio)
        add ton_chibi_gloves       xzoom ton_chibi_flip zoom (1.0/scaleratio)
    if ton_cloth_pile:
        add "characters/chibis/cloth_pile_r.png" xpos ton_pile_xpos ypos ton_pile_ypos



init python:
    # Temporal function
    # TODO: Create a chibi class instead.
    def update_chibi_image(name):
        if name == "cho":
            imagepath = "characters/cho/chibis/"
            animation = "_"+cho_chibi_animation if cho_chibi_animation else ""
            status = "_"+cho_chibi_status if cho_chibi_status else ""
            global cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk
            cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk, cho_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_cho blink", "ch_cho walk", "ch_cho walk_shoes"

            if cho_chibi_animation == "fly":
                cho_chibi_stand = "ch_cho fly_idle"
                cho_chibi_walk = "ch_cho fly"

            if cho_class.get_worn("top"):
                if cho_class.get_cloth("top").id == "top_sweater_1":
                    cho_chibi_top = imagepath+"cc_sweater"+animation+status+".png" if animation else imagepath+"cc_sweater.png"
                else:
                    cho_chibi_top = imagepath+"cc_top"+animation+status+".png" if animation else imagepath+"cc_top.png"

            if cho_class.get_worn("bottom"):
                if cho_class.get_cloth("bottom").id in ("pants_long_2", "pants_short_4"):
                    if not status == "_move":
                        cho_chibi_bottom = imagepath+"cc_trousers"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_bottom = imagepath+"cc_trousers"+animation+status+".png"
                        else:
                            if status == "_move":
                                cho_chibi_bottom = "ch_cho trousers"
                            else:
                                cho_chibi_bottom = imagepath+"cc_trousers.png"
                else:
                    cho_chibi_bottom = imagepath+"cc_skirt"+animation+status+".png" if animation else imagepath+"cc_skirt.png"

            if cho_class.get_worn("gloves"):
                if cho_class.get_cloth("gloves").id == "quidditch":
                    cho_chibi_gloves = imagepath+"cc_gloves"+animation+status+".png" if animation else imagepath+"cc_gloves.png"

            if cho_class.get_worn("robe"):
                if cho_class.get_cloth("robe").id == "robe_quidditch_1":
                    cho_chibi_robe = imagepath+"cc_quid_robe"+animation+status+".png" if animation else imagepath+"cc_quid_robe.png"
                    if not animation:
                        cho_chibi_fix = imagepath+"cc_quid_robe_fix.png"
                else:
                    cho_chibi_robe = imagepath+"cc_robe"+animation+status+".png" if animation else imagepath+"cc_robe.png"

            if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"):
                if cho_class.get_worn("gloves") and cho_class.get_cloth("gloves").id == "quidditch":
                    if not animation and status == "_move":
                        cho_chibi_shoes = "ch_cho walk_quid_shoes"
                    else:
                        cho_chibi_shoes = imagepath+"cc_quid_shoes"+animation+status+".png"
                else:
                    if not status == "_move":
                        cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
            else:
                cho_chibi_shoes = "blank"
        elif name == "tonks":
            imagepath = "characters/tonks/chibis/"
            animation = "_"+ton_chibi_animation if ton_chibi_animation else ""
            status = "_"+ton_chibi_status if ton_chibi_status else ""
            global ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk
            ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk, ton_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_ton blink", "ch_ton walk", "ch_ton walk_shoes"

            if tonks_class.get_worn("top"):
                ton_chibi_top = imagepath+"nt_top"+animation+status+".png" if animation else imagepath+"nt_top.png"

            if tonks_class.get_worn("bottom"):
                ton_chibi_bottom = imagepath+"nt_trousers"+animation+status+".png" if animation else imagepath+"nt_trousers.png"

            if tonks_class.get_worn("gloves"):
                ton_chibi_gloves = imagepath+"nt_gloves"+animation+status+".png" if animation else imagepath+"nt_gloves.png"

            if tonks_class.get_worn("robe"):
                ton_chibi_robe = imagepath+"nt_robe"+animation+status+".png" if animation else imagepath+"nt_robe.png"

            if tonks_class.get_worn("bottom") or tonks_class.get_worn("stockings"):
                if not status == "_move":
                    ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
                else:
                    if animation:
                        ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
            else:
                ton_chibi_shoes = "blank"
        return
