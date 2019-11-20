
# Genie chibi actions:
# stand, stand_alt, stand_shocked
# rummage, petting, grab_mid, grab_high
# sit_behind_desk
# jerk_off_behind_desk, cum_behind_desk, cum_behind_desk_done
# dick_out
# hold_dick, jerk_off, cum, cum_done, cum_close, cum_close_done
# read, read_done, read_near_fire, read_near_fire_done

#TODO Genie chibi images and calls (at least for stand and walk) have to be flipped consistently with other chibis

label gen_chibi(action=None, xpos=None, ypos=None, flip=False, pic=None):
    hide screen favor # screen tag

    #TODO Check if needed. These hide screen calls are not in other chibi labels
    hide screen blktone
    hide screen bld1

    # Rarely used position
    if xpos == "on_girl": # Girl has to stand at mid
        $ xpos = 470

    $ genie_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ genie_chibi.hide()
        return
    elif action == "leave":
        hide screen genie_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ genie_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ genie_chibi.do(None)
        return

    # Special setup for certain actions

    elif action == "sit_behind_desk":
        $ genie_chibi.hide()
        hide screen chair_left
        hide screen desk
        show screen genie_sit_behind_desk
        return

    elif action in ("jerk_off_behind_desk", "cum_behind_desk", "cum_behind_desk_done"):
        hide screen chair_left
        hide screen desk
        $ masturbating = True #TODO Set this flag in events for clarity (only when needed)
        $ genie_chibi.position(218, 205, False)

    elif action in ("read", "read_done", "read_near_fire", "read_near_fire_done"):
        show screen chair_left
        show screen desk
        $ genie_chibi.position(430, 205, False)
    
    elif action == "paperwork":
        hide screen chair_left
        hide screen desk
        $ genie_chibi.position(224, 205, False)

    $ genie_chibi.do(action)

    return

label gen_walk(xpos=None, ypos=None, speed=1.0, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call gen_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ genie_chibi.move(xpos, ypos, speed)
    elif action == "leave":
        $ genie_chibi.show()
        $ genie_chibi.move("door", "base", speed)
        call play_sound("door")
        $ genie_chibi.hide()
        with d3
        pause .5
    else:
        $ genie_chibi.show()
        $ genie_chibi.move(xpos, ypos, speed)
        $ genie_chibi.do()

    return

# Screen with interactive option
screen genie_sit_behind_desk:
    tag genie_chibi
    zorder desk_zorder
    if room_menu_active:
        use genie_desk_interactive
    else:
        add "ch_gen sit_behind_desk" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5

# Chibi definition
default genie_chibi = chibi("genie", ["base"], update_genie_chibi, places=genie_places)

define genie_places = {
    "base": (None, 190),
    "behind_desk": (210, 190),
    "mid": (500, None),
    "left": (100, None),
    "fireplace": (550, 160),
    "cupboard": (260, None),
}

init python:
    def update_genie_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_gen {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image
