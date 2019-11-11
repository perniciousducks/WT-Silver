

### Snape Chibi ###

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
    elif action == "stand_shocked":
        pass #TODO Add action stand_shocked to Snape chibi
    elif action in ("jerking_off", "cumming", "cumming_done"):
        $ snape_chibi.hide() # Not handled by chibi class
        show screen snape_jerking_off(action)
    elif action == "hold_dick":
        $ snape_chibi.hide() # Not handled by chibi class
        show screen snape_stands_holds_dick
    elif action == "reset":
        $ snape_chibi.do(None)
    else: # stand
        $ snape_chibi.do(None)

    return

label sna_walk(xpos=None, ypos=None, speed=None, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    #TODO Convert speed

    if action == "enter":
        call play_sound("door")
        call sna_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ snape_chibi.move(xpos, ypos)
    elif action == "leave":
        $ snape_chibi.show()
        $ snape_chibi.move("door", "base")
        call play_sound("door")
        $ snape_chibi.hide()
        with d3
        pause .5
    else:
        $ snape_chibi.show()
        $ snape_chibi.move(xpos, ypos)

    return

# Screens
screen with_snape(ani=False):
    tag hanging_with_snape
    zorder 3
    if ani:
        if daytime:
            add "genie_toast_goblet_daytime" xpos 435 ypos 200 # Different shadow.
        else:
            add "genie_toast_goblet" xpos 435 ypos 200
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

# Chibi definition
default snape_chibi = chibi("snape", ["base"], update_snape_chibi)

init python:
    def update_snape_chibi(chibi):
        if chibi.action == "walk":
            chibi["base"] = "snape_walk"
        else:
            chibi["base"] = "snape_stand"
