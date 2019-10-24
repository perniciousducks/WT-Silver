label cho_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ cho_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ cho_chibi.hide()
        return
    elif action == "leave":
        hide screen cho_chang
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ cho_chibi.hide()
        with d3
        pause .5
        return
    elif action == "fly":
        $ cho_chibi.do(action)
    elif action == "reset":
        $ cho_chibi.do(None)
    else: # stand
        $ cho_chibi.do(None)

    $ cho_chibi.show()
    return

label cho_walk(xpos=None, ypos=None, speed=None, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    #TODO Convert speed

    if action == "enter":
        call play_sound("door")
        call cho_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ cho_chibi.move(xpos, ypos)
    elif action == "leave":
        $ cho_chibi.show()
        $ cho_chibi.move("door", "base", time_speed=speed)
        call play_sound("door")
        $ cho_chibi.hide()
        with d3
        pause .5
    else:
        $ cho_chibi.show()
        $ cho_chibi.move(xpos, ypos, time_speed=speed)

    return

# Screens
screen cho_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag cho_cloth_pile
    zorder cho_chibi.zorder
    add "characters/chibis/cloth_pile_r.png" pos position zoom 0.5

# Chibi definition
default cho_chibi = chibi("cho", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_cho_chibi)

init python:
    def update_cho_chibi(chibi):
        # Cho special: fly (fly_idle!), fly_move
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
                    chibi["shoes"] = "ch_cho walk_quid_shoes"
                else:
                    chibi["shoes"] = "cc_quid_shoes.png"
            else:
                if chibi.action == "walk":
                    chibi["shoes"] = "ch_cho walk_shoes"
                else:
                    chibi["shoes"] = "cc_shoes.png"
