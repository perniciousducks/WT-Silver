label ton_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ tonks_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ tonks_chibi.hide()
        return
    elif action == "leave":
        hide screen tonks_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ tonks_chibi.hide()
        with d3
        pause .5
        return
    elif action == "slack_jaw":
        pass #TODO Add slack_jaw action to Tonks chibi
    elif action == "reset":
        $ tonks_chibi.do(None)
    else: # stand
        $ tonks_chibi.do(None)

    return

label ton_walk(xpos=None, ypos=None, speed=1.0, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call ton_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ tonks_chibi.move(xpos, ypos, speed)
    elif action == "leave":
        $ tonks_chibi.show()
        $ tonks_chibi.move("door", "base", speed)
        call play_sound("door")
        $ tonks_chibi.hide()
        with d3
        pause .5
    else:
        $ tonks_chibi.show()
        $ tonks_chibi.move(xpos, ypos, speed)

    return

# Screens
screen ton_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag ton_cloth_pile
    zorder tonks_chibi.zorder
    add "characters/chibis/cloth_pile_r.png" pos position zoom 0.5

screen with_tonks_animated():
    tag ton_chibi
    zorder tonks_chibi.zorder
    
    if daytime:
        add "ch_gen toast_goblet_daytime" xpos 435 ypos 200
    else:
        add "ch_gen toast_goblet" xpos 435 ypos 200

    add "ch_ton sit" xpos 610 ypos 175
    
    if tonks_class.get_worn("bottom"):
        add "ch_ton sit_trousers" xpos 610 ypos 175
    if tonks_class.get_worn("bottom") or tonks_class.get_worn("stockings"):
        add "ch_ton sit_shoes" xpos 610 ypos 175
    if tonks_class.get_worn("top"):
        add "ch_ton sit_top" xpos 610 ypos 175


# Chibi definition
default tonks_chibi = chibi("tonks", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_tonks_chibi)

init python:
    def update_tonks_chibi(chibi):
        # Tonks special: drinking (not part of chibi definition)
        if chibi.action == "walk":
            chibi["base"] = "ch_ton walk"
        else:
            chibi["base"] = "ch_ton blink"
                    
        if tonks_class.get_worn("top"):
            chibi["top"] = "nt_top.png"

        if tonks_class.get_worn("bottom"):
            if tonks_class.get_cloth("bottom").subcat == "trousers":
                if chibi.action == "walk":
                    chibi["bottom"] = "ch_ton trousers"
                else:
                    chibi["bottom"] = "nt_trousers.png"
            else:
                chibi["bottom"] = "nt_skirt.png"

        if tonks_class.get_worn("gloves"):
            chibi["gloves"] = "nt_gloves.png"

        if tonks_class.get_worn("robe"):
            chibi["robe"] = "nt_robe.png"

        if tonks_class.get_worn("bottom") or tonks_class.get_worn("stockings"):
            if chibi.action == "walk":
                chibi["shoes"] = "ch_ton walk_shoes"
            else:
                chibi["shoes"] = "nt_shoes.png"
