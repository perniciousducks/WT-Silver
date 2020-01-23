label her_chibi(action=None, xpos=None, ypos=None, flip=False, pic=None):
    hide screen favor # screen tag

    $ hermione_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ hermione_chibi.hide()
        return
    elif action == "leave":
        hide screen hermione_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ hermione_chibi.hide()
        with d3
        pause .5
        return

    elif action == "reset":
        $ hermione_chibi.do(None)
        return

    $ hermione_chibi.do(action)
    
    return

label her_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call her_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ hermione_chibi.move(xpos, ypos, speed, reduce)
    elif action == "leave":
        $ hermione_chibi.show()
        $ hermione_chibi.move("door", "base", speed, reduce)
        call play_sound("door")
        $ hermione_chibi.hide()
        with d3
        pause .5
    elif action == "run":
        $ hermione_chibi.show()
        $ hermione_chibi.move(xpos, ypos, speed, reduce, action)
    elif path:
        $ hermione_chibi.show()
        $ hermione_chibi.path_move(path, speed)
    else:
        $ hermione_chibi.show()
        $ hermione_chibi.move(xpos, ypos, speed, reduce)

    return

# Chibi definition
default hermione_chibi = Chibi("hermione", ["base"], update_hermione_chibi)

#TODO Hermione's chibis need clothing layers and then update logic must be reworked to set clothing state (using chibi class best practice, see Cho chibi for example)

init python:
    def update_hermione_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_hem {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Certain actions require more complex image selection, which is handled below

        if chibi.action == "walk":
            # Determine clothing state
            if not hermione.is_worn("top") and not hermione.is_worn("bottom") and not hermione.is_worn("robe"):
                chibi["base"] = "ch_hem walk_n"
            elif hermione.is_worn("robe"):
                if hermione.is_worn("top"):
                    chibi["base"] = "ch_hem walk_robe"
                else:
                    chibi["base"] = "ch_hem walk_robe_n"
            else:
                 chibi["base"] = "ch_hem walk"

        elif not chibi.action or chibi.action == "stand":
            # Determine clothing state
            if not hermione.is_worn("top") and not hermione.is_worn("bottom") and not hermione.is_worn("robe"):
                chibi["base"] = "ch_hem blink_n"
            elif hermione.is_worn("robe"):
                if hermione.is_worn("top"):
                    chibi["base"] = "ch_hem blink_robe"
                else:
                    chibi["base"] = "ch_hem blink_robe_n"
            else:
                 chibi["base"] = "ch_hem blink"

        elif chibi.action == "dance":
            # Determine clothing state
            if hermione.is_worn("top"):
                if hermione.get_equipped("top").id in ("top_1", "top_6"):
                    chibi["base"] =  "clothed_dance_ani"
                elif hermione.is_worn("bottom"):
                    chibi["base"] = "no_vest_dance_ani"
                else:
                    chibi["base"] = "no_skirt_dance_ani"
            else:
                if hermione.is_worn("bottom"):
                    chibi["base"] = "no_shirt_dance_ani"
                else:
                    chibi["base"] = "no_shirt_no_skirt_dance_ani"
        
        elif chibi.action == "dance_pause":
            # Determine clothing state
            if hermione.is_worn("panties"):
                chibi["base"] = "no_shirt_no_skirt_dance_pause"
            else:
                chibi["base"] = "no_panties_dance_pause"

        elif chibi.action == "top_naked":
            chibi["base"] = "dance/03_no_shirt_03.png" #TODO Should be 'stand' action without top clothes (needs layers first)
        
        elif chibi.action == "lift_skirt":
            if hermione.is_worn("panties"):
                #TODO Figure out a better way to determine the expression (so it can be reused in a different event)
                if hg_pf_admire_panties.counter <= 1:
                    # Reluctant expression
                    chibi["base"] = "~/lift_skirt/panties_00.png"
                else:
                    # Happy expression
                    chibi["base"] = "~/lift_skirt/panties_01.png"
            else:
                chibi["base"] = "~/lift_skirt/panties_02.png"
