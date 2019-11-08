label her_chibi(action=None, xpos=None, ypos=None, flip=False, pic=None):
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

    elif action == "lift_top":
        $ hermione_chibi.hide()
        show screen hermione_chibi_lift_top

    elif action == "lift_skirt":
        $ hermione_chibi.hide()
        show screen hermione_chibi_lift_skirt

    elif action == "dance":
        $ hermione_chibi.hide()
        show screen hermione_chibi_dance

    elif action == "top_naked":
        $ hermione_chibi.hide()
        show screen hermione_chibi_stand_no_shirt

    elif action == "sit":
        $ hermione_chibi.hide()
        show screen hermione_chibi_sit_naked_A #TODO Add clothing layers for this chibi

    elif action == "sit_naked":
        $ hermione_chibi.hide()
        show screen hermione_chibi_sit_naked_A

    elif action == "sit_naked_wide_eyes" or action == "sit_naked_scared" or action == "sit_naked_shocked":
        $ hermione_chibi.hide()
        show screen hermione_chibi_sit_naked_B

    elif action == "drink_potion":
        $ hermione_chibi.hide()
        show screen ch_potion

    elif action == "lying":
        $ hermione_chibi.hide()
        show screen hermione_lying

    elif action == "kneel_pant":
        $ hermione_chibi.hide()
        show screen hermione_kneel_pant

    elif action == "image" and pic:
        $ hermione_chibi.hide()
        # Add specific xpos and ypos number when calling.
        $ h_c_u_pic = "characters/hermione/chibis/"+str(pic)+".png"
        show screen h_c_u

    elif action == "reset":
        $ hermione_chibi.do(None)
    else: # stand
        $ hermione_chibi.do(None)
    
    return

label her_walk(xpos=None, ypos=None, speed=None, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    #TODO Convert speed

    if action == "enter":
        call play_sound("door")
        call her_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ hermione_chibi.move(xpos, ypos)
    elif action == "leave":
        $ hermione_chibi.show()
        $ hermione_chibi.move("door", "base")
        call play_sound("door")
        $ hermione_chibi.hide()
        with d3
        pause .5
    else:
        $ hermione_chibi.show()
        $ hermione_chibi.move(xpos, ypos)

    return

# Screens
screen hermione_chibi_lift_top():
    tag hermione_chibi
    add "characters/hermione/chibis/lift_top/tits_00.png" pos hermione_chibi.pos zoom 0.5
    zorder her_chibi_zorder

screen hermione_chibi_lift_skirt():
    tag hermione_chibi
    zorder her_chibi_zorder
    if hermione_wear_panties:
        #TODO Move this into the actual event, use it to set clothing state before showing chibi
        if hg_pf_admire_panties.counter <= 1:
            add "characters/hermione/chibis/lift_skirt/panties_00.png" pos hermione_chibi.pos zoom 0.5
        else:
            add "characters/hermione/chibis/lift_skirt/panties_01.png" pos hermione_chibi.pos zoom 0.5
    else:
        add "characters/hermione/chibis/lift_skirt/panties_02.png" pos hermione_chibi.pos zoom 0.5

screen ch_potion():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "ch_hem potion" pos hermione_chibi.pos xoffset -30 zoom 0.5

screen hermione_chibi_dance():
    tag hermione_chibi
    zorder her_chibi_zorder
    if hermione_wear_top:
        if h_top == "top_1" or h_top == "top_6":
            add "clothed_dance_ani" pos hermione_chibi.pos zoom 0.5
        else:
            if hermione_wear_bottom:
                add "no_vest_dance_ani" pos hermione_chibi.pos zoom 0.5
            else:
                add "no_skirt_dance_ani" pos hermione_chibi.pos zoom 0.5
    else:
        if hermione_wear_bottom:
            add "no_shirt_dance_ani" pos hermione_chibi.pos zoom 0.5
        else: #Nude
            add "no_shirt_no_skirt_dance_ani" pos hermione_chibi.pos zoom 0.5

screen hermione_chibi_sit_naked_A():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "characters/hermione/chibis/sitting/sit_naked_blink.png" pos hermione_chibi.pos zoom 0.5 # 0.4

screen hermione_chibi_sit_naked_B():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "characters/hermione/chibis/sitting/sit_naked.png" pos hermione_chibi.pos zoom 0.5 # 0.4
    
screen hermione_chibi_stand_no_shirt():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "characters/hermione/chibis/dance/03_no_shirt_03.png" pos hermione_chibi.pos zoom 0.5

screen hermione_lying():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "characters/hermione/chibis/lying/shime21.png" pos hermione_chibi.pos

screen hermione_kneel_pant():
    tag hermione_chibi
    zorder her_chibi_zorder
    add "ch_hem kneel_pant" pos hermione_chibi.pos zoom 0.5

#TODO Remove universal screen (h_c_u)
screen h_c_u():
    tag hermione_chibi
    zorder her_chibi_zorder
    if "/chibis/" in h_c_u_pic:
        add h_c_u_pic pos hermione_chibi.pos zoom 0.5
    else:
        add h_c_u_pic pos hermione_chibi.pos

# Chibi definition
default hermione_chibi = chibi("hermione", ["base"], update_hermione_chibi)

init python:
    def update_hermione_chibi(chibi):
        if chibi.action == "walk":
            # Determine clothing state
            if not hermione_class.get_worn("top") and not hermione_class.get_worn("bottom") and not hermione_class.get_worn("robe"):
                chibi["base"] = "ch_hem walk_n"
            elif hermione_class.get_worn("robe"):
                if hermione_class.get_worn("top"):
                    chibi["base"] = "ch_hem walk_robe"
                else:
                    chibi["base"] = "ch_hem walk_robe_n"
            else:
                 chibi["base"] = "ch_hem walk_n"

        elif chibi.action == "run":
            chibi["base"] = "ch_hem run"

        else:
            # Determine clothing state
            if not hermione_class.get_worn("top") and not hermione_class.get_worn("bottom") and not hermione_class.get_worn("robe"):
                chibi["base"] = "ch_hem blink_n"
            elif hermione_class.get_worn("robe"):
                if hermione_class.get_worn("top"):
                    chibi["base"] = "ch_hem blink_robe"
                else:
                    chibi["base"] = "ch_hem blink_robe_n"
            else:
                 chibi["base"] = "ch_hem blink_n"
