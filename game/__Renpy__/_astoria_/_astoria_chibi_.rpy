label ast_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ astoria_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ astoria_chibi.hide()
        return
    elif action == "leave":
        hide screen astoria_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ astoria_chibi.hide()
        with d3
        pause .5
        return
    elif action in ("wand", "wand_casting", "wand_imperio"):
        $ astoria_chibi.do(action)
    elif action == "reset":
        $ astoria_chibi.do(None)
    else: # stand
        $ astoria_chibi.do(None)

    $ astoria_chibi.show()
    return

label ast_walk(xpos=None, ypos=None, speed=None, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    #TODO Convert speed

    if action == "enter":
        call play_sound("door")
        call ast_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ astoria_chibi.move(xpos, ypos)
    elif action == "leave":
        $ astoria_chibi.show()
        $ astoria_chibi.move("door", "base")
        call play_sound("door")
        $ astoria_chibi.hide()
        with d3
        pause .5
    else:
        $ astoria_chibi.show()
        $ astoria_chibi.move(xpos, ypos)

    return

# Screens
screen ast_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag ast_cloth_pile
    zorder astoria_chibi.zorder
    add "characters/chibis/cloth_pile_r.png" pos position zoom 0.5

# Chibi definition
default astoria_chibi = chibi("astoria", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_astoria_chibi)

init python:
    def update_astoria_chibi(chibi):
        # Astoria actions: wand, wand_casting, wand_imperio
        if chibi.action == "wand":
            chibi["base"] = "ch_ast wand_stand"
        elif chibi.action == "wand_casting":
            chibi["base"] = "ch_ast wand_casting"
        elif chibi.action == "wand_imperio":
            chibi["base"] = "ch_ast wand_imperio"
        elif chibi.action == "walk":
            chibi["base"] = "ch_ast walk"
        else:
            chibi["base"] = "ch_ast blink"

        if astoria_class.get_worn("top"):
            chibi["top"] = "ag_top.png"

        if astoria_class.get_worn("bottom") or astoria_class.get_worn("top") and astoria_class.get_cloth("top").id == astoria_cloth_topann.id:
            chibi["bottom"] = "ag_skirt.png"

        if astoria_class.get_worn("robe") and not chibi.special:
            chibi["robe"] = "ag_robe.png"

        if astoria_class.get_worn("bottom") or astoria_class.get_worn("stockings"):
            if chibi.action == "wand_imperio":
                chibi["shoes"] = "ch_ast imperio_shoes"
            elif chibi.action == "walk":
                chibi["shoes"] = "ch_ast walk_shoes"
            else:
                chibi["shoes"] = "ag_shoes.png"
