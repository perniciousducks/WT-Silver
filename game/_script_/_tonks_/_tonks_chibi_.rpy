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
    elif action == "reset":
        $ tonks_chibi.do(None)
        return

    $ tonks_chibi.do(action)

    return

label ton_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call ton_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ tonks_chibi.move(xpos, ypos, speed, reduce)
    elif action == "leave":
        $ tonks_chibi.show()
        $ tonks_chibi.move("door", "base", speed, reduce)
        call play_sound("door")
        $ tonks_chibi.hide()
        with d3
        pause .5
    elif path:
        $ tonks_chibi.show()
        $ tonks_chibi.path_move(path, speed)
    else:
        $ tonks_chibi.show()
        $ tonks_chibi.move(xpos, ypos, speed, reduce)

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
    
    if tonks.is_worn("bottom"):
        add "ch_ton sit_trousers" xpos 610 ypos 175
    if tonks.is_worn("bottom") or tonks.is_worn("stockings"):
        add "ch_ton sit_shoes" xpos 610 ypos 175
    if tonks.is_worn("top"):
        add "ch_ton sit_top" xpos 610 ypos 175


# Chibi definition
default tonks_chibi = Chibi("tonks", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_tonks_chibi)

init python:
    def update_tonks_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_ton {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Determine clothing state
        
        if tonks.is_worn("top"):
            chibi["top"] = "nt_top.png"

        if tonks.is_worn("bottom"):
            if tonks.get_equipped("bottom").categories[1] == "trousers":
                if chibi.action == "walk":
                    chibi["bottom"] = "ch_ton walk trousers"
                else:
                    chibi["bottom"] = "nt_trousers.png"
            else:
                chibi["bottom"] = "nt_skirt.png"

        if tonks.is_worn("gloves"):
            chibi["gloves"] = "nt_gloves.png"

        if tonks.is_worn("robe"):
            chibi["robe"] = "nt_robe.png"

        if tonks.is_worn("bottom") or tonks.is_worn("stockings"):
            if chibi.action == "walk":
                chibi["shoes"] = "ch_ton walk shoes"
            else:
                chibi["shoes"] = "nt_shoes.png"
