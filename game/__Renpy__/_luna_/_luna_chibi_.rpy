label lun_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ luna_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ luna_chibi.hide()
        return
    elif action == "leave":
        hide screen luna_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ luna_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ luna_chibi.do(None)
        return
    
    $ luna_chibi.do(action)

    return

label lun_walk(xpos=None, ypos=None, speed=1.0, action=None, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call lun_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ luna_chibi.move(xpos, ypos, speed)
    elif action == "leave":
        $ luna_chibi.show()
        $ luna_chibi.move("door", "base", speed)
        call play_sound("door")
        $ luna_chibi.hide()
        with d3
        pause .5
    else:
        $ luna_chibi.show()
        $ luna_chibi.move(xpos, ypos, speed)

    return

# Chibi definition
default luna_chibi = chibi("luna", ["base"], update_luna_chibi)

init python:
    def update_luna_chibi(chibi):
        if chibi.action == "walk":
            if luna_wear_top and luna_wear_bottom:
                chibi["base"] = "ch_lun walk_a"
            # elif luna_wear_bottom and not luna_wear_top:
            #     pass #TODO Add topless walking chibi for Luna
            elif not luna_wear_top and not luna_wear_bottom:
                chibi["base"] = "ch_lun walk_n"
            elif luna_wear_robe:
                chibi["base"] = "ch_lun walk_robe"
        elif not chibi.action or chibi.action == "stand":
            if luna_wear_top and luna_wear_bottom:
                chibi["base"] = "ch_lun blink_a"
            elif luna_wear_bottom and not luna_wear_top:
                chibi["base"] = "luna_stand_topless.png"
            elif not luna_wear_top and not luna_wear_bottom:
                chibi["base"] = "ch_lun blink_n"
            elif luna_wear_robe:        
                chibi["base"] = "ch_lun blink_robe"
        else:
            # Assume chibi action has a matching image definition
            chibi_image = "ch_lun {}".format(chibi.action or "stand")
            chibi["base"] = chibi_image
