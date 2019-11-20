label sna_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ snape_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ snape_chibi.hide()
        return
    elif action == "leave":
        hide screen snape_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ snape_chibi.hide()
        with d3
        pause .5
        return
    #TODO Add Snape chibi wand actions
    # elif action in ("wand",):
    #     $ snape_chibi.do(action)
    elif action in ("jerking_off", "cumming", "cumming_done"):
        $ snape_chibi.hide() # Not handled by chibi class
        show screen snape_jerking_off(action)
    elif action == "hold_dick":
        $ snape_chibi.hide() # Not handled by chibi class
        show screen snape_stands_holds_dick
    elif action == "stand_shocked":
        $ snape_chibi.hide()
        show screen snape_stand_shocked
    elif action == "reset":
        $ snape_chibi.do(None)
    else: # stand
        $ snape_chibi.do(None)

    return

label sna_walk(xpos=None, ypos=None, speed=1.0, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call sna_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ snape_chibi.move(xpos, ypos, speed)
    elif action == "leave":
        $ snape_chibi.show()
        $ snape_chibi.move("door", "base", speed)
        call play_sound("door")
        $ snape_chibi.hide()
        with d3
        pause .5
    else:
        $ snape_chibi.show()
        $ snape_chibi.move(xpos, ypos, speed)

    return

#TODO Convert Snape chibi screens into chibi class actions if position and such depend on it
# Screens
screen with_snape(ani=False):
    tag hanging_with_snape
    zorder 3
    if ani:
        if daytime:
            add "ch_gen toast_goblet_daytime" xpos 435 ypos 200 # Different shadow.
        else:
            add "ch_gen toast_goblet" xpos 435 ypos 200
        add "snape_toast_goblet" xpos 618 ypos 200 zoom 0.5

    else:
        if daytime:
            add "characters/genie/chibis/drinking/01_day.png" xpos 435 ypos 200 zoom 0.5 # Different shadow.
        else:
            add "characters/genie/chibis/drinking/01.png" xpos 435 ypos 200 zoom 0.5
        add "characters/snape/chibis/drinking/01.png" xpos 618 ypos 200 zoom 0.5

screen snape_jerking_off(action="jerking_off"):
    tag snape_chibi
    zorder snape_chibi.zorder
    if action == "cumming":
        add "snape_jerking_off_cum" pos snape_chibi.pos
    elif action == "cumming_done":
        add "snape_jerking_off_cum_done" pos snape_chibi.pos
    else:
        add "snape_jerking_off" pos snape_chibi.pos

screen snape_stands_holds_dick():
    tag snape_chibi
    zorder snape_chibi.zorder
    add "characters/snape/chibis/masturbating/01.png" pos snape_chibi.pos zoom 0.5 yoffset -60

screen snape_stand_shocked:
    tag snape_chibi
    zorder snape_chibi.zorder
    add "snape_stand_shocked" pos snape_chibi.pos

# Chibi definition
default snape_chibi = chibi("snape", ["base"], update_snape_chibi, places=snape_places)

define snape_places = {
    "base": (None, 190),
    "mid": (500, None),
    "desk_close": (425, 245)
}

init python:
    def update_snape_chibi(chibi):
        if chibi.action == "walk":
            chibi["base"] = "snape_walk"
        else:
            chibi["base"] = "snape_stand"
