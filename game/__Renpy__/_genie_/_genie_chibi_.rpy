
#TODO Convert Genie chibi screens into chibi class actions if position and such depend on it
screen genie(): # Sitting behind desk
    tag genie_chibi
    zorder desk_zorder
    if room_menu_active:
        use genie_desk
    else:
        add "genie_sit_behind_desk" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5

screen rummaging():
    tag genie_chibi
    zorder 1
    add "genie_rum_ani" xpos 160 ypos 110

screen feeding():
    tag genie_chibi
    zorder 1
    add "grab_high" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5    

screen petting():
    tag genie_chibi
    zorder 1
    add "petting" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5

screen paperwork():
    tag genie_chibi
    zorder desk_zorder
    add "genie_paperwork" xpos 84+140 ypos 205

screen genie_rummage():
    tag genie_chibi
    zorder genie_chibi.zorder
    add "genie_rum_ani" pos genie_chibi.pos xzoom (-1 if genie_chibi.flip else 1)

#TODO Make actions for Genie reading chibis and use existing screens for the furniture
screen reading_near_fire():
    tag genie_chibi
    zorder 3
    add "images/rooms/main_room/chair_left_with_shadow.png" xpos 180+140 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "images/rooms/main_room/desk_with_shadow.png" xpos 220+140 ypos 330 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "reading_near_fire" xpos 290+140 ypos 205

screen reading():
    tag genie_chibi
    zorder 3
    add "images/rooms/main_room/chair_left_with_shadow.png" xpos 180+140 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "images/rooms/main_room/desk_with_shadow.png" xpos 220+140 ypos 330 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "reading" xpos 290+140 ypos 205

screen done_reading():
    tag genie_chibi
    zorder 3
    add "images/rooms/main_room/chair_left_with_shadow.png" xpos 180+140 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "images/rooms/main_room/desk_with_shadow.png" xpos 220+140 ypos 330 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "characters/genie/chibis/reading/07.png" xpos 290+140 ypos 205 xzoom -1 zoom 0.5

screen done_reading_near_fire():
    tag genie_chibi
    zorder 3
    add "images/rooms/main_room/chair_left_with_shadow.png" xpos 180+140 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "images/rooms/main_room/desk_with_shadow.png" xpos 220+140 ypos 330 xanchor 0.5 yanchor 0.5 zoom 0.5
    add "characters/genie/chibis/reading/07.png" xpos 290+140 ypos 205 zoom 0.5

# Jerking off behind desk

screen genie_jerking_off(): #Genie sitting behind his desk and jerking off...
    tag genie_chibi
    zorder desk_zorder
    add "genie_jerk_off_behind_desk" xpos 218 ypos 205

screen genie_jerking_sperm(): #Genie's behind desk cum animation, CUM ONLY!
    tag genie_cum
    zorder desk_zorder
    add "genie_cum_behind_desk_layer" xpos 218 ypos 205

screen genie_jerking_sperm_02(): #Genie's behind desk cum still image, CUM ONLY!
    tag genie_cum
    zorder desk_zorder
    add "characters/genie/chibis/masturbating/desk_sperm_11.png" xpos 218 ypos 205

screen genie_dick_out_desk(): #Genie sitting behind his desk and jerking off...
    tag genie_chibi
    zorder desk_zorder
    add "genie_dick_out_desk" xpos 218 ypos 205

# Jerking off standing

screen genie_jerking_off_standing(action):
    tag genie_chibi
    zorder genie_chibi.zorder
    if action == "cumming":
        add "genie_cum_standing" xpos genie_chibi.pos[0]-270 ypos genie_chibi.pos[1]-185
    elif action == "cumming_done":
        add "genie_cum_standing_done" xpos genie_chibi.pos[0]-270 ypos genie_chibi.pos[1]-185
    else:
        add "genie_jerk_off_standing" xpos genie_chibi.pos[0]-270 ypos genie_chibi.pos[1]-185

screen genie_jerking_off_standing_cum():
    tag genie_cum
    zorder genie_chibi.zorder
    add "genie_cum_standing_layer" xpos genie_chibi.pos[0]-270  ypos genie_chibi.pos[1]-185

screen jerking_off_cum(): # Used when Hermione is standing between Genie and desk
    tag genie_cum
    zorder genie_chibi.zorder
    add "genie_cum_standing_close_layer" xpos -60 ypos 10
    #add "grope_front_blinking" xpos -200 ypos 10

screen genie_stands_holds_dick():
    tag genie_chibi
    zorder genie_chibi.zorder
    add "characters/genie/chibis/masturbating/01.png" xpos genie_chibi.pos[0]-270 ypos genie_chibi.pos[1]-185 zoom 0.5

screen genie_stand_shocked:
    tag genie_chibi
    zorder genie_chibi.zorder
    add "genie_stand_shocked" pos genie_chibi.pos


label gen_chibi(action=None, xpos=None, ypos=None, flip=False, pic=None):
    hide screen favor # screen tag

    #TODO Merge cum screens into chibi animations
    hide screen genie_cum # screen tag

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

    elif action == "rummage":
        $ genie_chibi.hide()
        show screen genie_rummage

    elif action in ("jerking_off","cumming","cumming_done"):
        $ genie_chibi.hide()
        show screen genie_jerking_off_standing(action)

    elif action == "hold_dick":
        $ genie_chibi.hide()
        show screen genie_stands_holds_dick

    elif action == "dick_out_desk":
        $ genie_chibi.hide()
        show screen genie_dick_out_desk

    elif action == "sit_behind_desk":
        $ genie_chibi.hide()
        hide screen chair_left
        hide screen desk
        show screen genie

    elif action in ["jerk_off_behind_desk", "cum_behind_desk", "cum_on_desk"]:
        $ genie_chibi.hide()
        $ masturbating = True # Set event flag
        if action == "cum_behind_desk":
            show screen genie_jerking_off
            show screen genie_jerking_sperm
        elif action == "cum_on_desk":
            hide screen desk
            show screen genie
            show screen genie_jerking_sperm_02
        else:
            show screen genie_jerking_off
    
    elif action == "stand_shocked":
        $ genie_chibi.hide()
        show screen genie_stand_shocked

    elif action in ("standing_alt",):
        $ genie_chibi.do(action)
    else: # stand
        $ genie_chibi.do(None)

    return

label gen_walk(xpos=None, ypos=None, speed=None, action=None, loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    #TODO Convert speed

    if action == "enter":
        call play_sound("door")
        call gen_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ genie_chibi.move(xpos, ypos)
    elif action == "leave":
        $ genie_chibi.show()
        $ genie_chibi.move("door", "base")
        call play_sound("door")
        $ genie_chibi.hide()
        with d3
        pause .5
    else:
        $ genie_chibi.show()
        $ genie_chibi.move(xpos, ypos)

    return

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
        if chibi.action == "walk":
            chibi["base"] = "genie_walk_ani"
        elif chibi.action == "standing_alt":
            chibi["base"] = "genie_stand_alternative"
        else:
            chibi["base"] = "genie_stand_ani"
