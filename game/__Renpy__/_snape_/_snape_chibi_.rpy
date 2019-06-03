

screen snape_jerking_off():
    tag snape_chibi
    add "jerking_off_03_ani" at Position(xpos=sna_chibi_xpos-500, ypos=sna_chibi_ypos-240)
    zorder 3

screen snape_jerking_off_cum():
    add "snape_cum_01" at Position(xpos=sna_chibi_xpos-500, ypos=sna_chibi_ypos-240)
    zorder 3

screen snape_stands_holds_dick():
    tag snape_chibi
    add "characters/snape/chibis/masturbating/01.png" at Position(xpos=sna_chibi_xpos-500, ypos=sna_chibi_ypos-240)
    zorder 3


###  SNAPE CHIBI UNIVERSAL SCREEN ###
screen s_c_u():
    tag snape_chibi
    add s_c_u_pic at Position(xpos=sna_chibi_xpos, ypos=sna_chibi_ypos) # (xpos=360, ypos=210)
    zorder 3

###  SNAPE'S CUM UNIVERSAL SCREEN ###
screen s_c_c_u():
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos+140, ypos=snape_cum_chibi_ypos)
    zorder 3



### SNAPE CHIBI SCREENS ###

screen snape_stand():
    tag snape_chibi

    add sna_chibi_stand xpos sna_chibi_xpos ypos sna_chibi_ypos xzoom sna_chibi_flip #zoom (1.0/scaleratio)

    zorder sna_chibi_zorder

screen snape_walk():
    tag snape_chibi

    add sna_chibi_walk         at sna_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom sna_chibi_flip #zoom (1.0/scaleratio)

    zorder sna_chibi_zorder


label update_sna_chibi:
    $ sna_chibi_stand = "characters/snape/chibis/snape_stand.png"
    $ sna_chibi_walk = "snape_walk"
    return



label sna_chibi(action = "", xpos=sna_chibi_xpos, ypos=sna_chibi_ypos, pic = "", flip=False):
    hide screen snape_stand

    hide screen s_c_u
    hide screen snape_jerking_off
    hide screen snape_jerking_off_cum

    $ sna_chibi_xpos = 500
    $ sna_chibi_ypos = 190

    if xpos != sna_chibi_xpos:
        if xpos == "mid":
            $ sna_chibi_xpos = 500
        elif xpos == "desk":
            $ sna_chibi_xpos = 440
        elif xpos == "desk_close":
            $ sna_chibi_xpos = 420
        elif xpos == "door":
            $ sna_chibi_xpos = 750
        else:
            $ sna_chibi_xpos = int(xpos)

    if ypos != sna_chibi_ypos:
        if ypos in ["base","default"]:
            $ sna_chibi_ypos = 190
        else:
            $ sna_chibi_ypos = int(ypos)

    #Snape Chibi Actions.

    #Special Images. These need custom xpos/ypos positions!
    if action == "image":

        if xpos == "desk":
            $ sna_chibi_xpos = 440
        elif xpos == "mid":
            $ sna_chibi_xpos = 500
        elif xpos == "door":
            $ sna_chibi_xpos = 750
        else:
            $ sna_chibi_xpos = 500

        if ypos == "base":
            $ sna_chibi_ypos = 190
        else:
            $ sna_chibi_ypos = 190

        if pic != "":
            $ s_c_u_pic = "characters/snape/chibis/"+str(pic)+".png"

        show screen s_c_u

    elif action == "jerking" or action == "jerking_off" or action == "cumming":
        show screen snape_jerking_off

        if action == "cumming":
            show screen snape_jerking_off_cum

    elif action == "hold_dick" or action == "stand_hold_dick":
        show screen snape_stands_holds_dick

    elif action == "hide":
        pass

    elif action == "leave":
        hide screen sna_main
        hide screen bld1
        hide screen blktone
        with d3
        pause.5

    else:
        if flip:
            $ sna_chibi_flip = -1
            show screen snape_stand
        else:
            $ sna_chibi_flip = 1
            show screen snape_stand

    return


### Snape Chibi Walk ###

# xpos + ypos = position the chibi walks to.
# action = "enter", sets the starting position of the chibi at the entrance (door).
# action = "leave", automatically hide the chibi with a door sound and pause.
# speed = time it will take for the chibi to move A to B in seconds. Lower value = faster walk.
# loiter = flag that shows the standing chibi after the walk, default is True
# redux_pause = value to decrease the time to pause before hideing the animation early

label sna_walk(xpos=walk_xpos, ypos=walk_ypos, speed=sna_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    hide screen snape_walk
    hide screen snape_stand

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ sna_chibi_xpos = 750
        $ sna_chibi_ypos = 190
    if action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = sna_chibi_xpos
    $ walk_ypos = sna_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 500
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "left":
        $ walk_xpos2 = 100
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ["base","default"]:
        $ walk_ypos2 = 190
    else:
        $ walk_ypos2 = int(ypos)

    $ sna_speed = speed #Speed of walking animation. (lower = faster)


    # Walk right to left
    if walk_xpos > walk_xpos2:
        $ sna_chibi_flip = 1
        show screen snape_walk
        $ tmp = sna_speed - redux_pause
        $ renpy.pause(tmp)
        $ sna_chibi_xpos = walk_xpos2
        $ sna_chibi_ypos = walk_ypos2
        hide screen snape_walk
        if loiter:
            show screen snape_stand

    # Walk left to right
    else:
        $ sna_chibi_flip = -1
        show screen snape_walk
        $ tmp = sna_speed - redux_pause
        $ renpy.pause(tmp)
        $ sna_chibi_xpos = walk_xpos2
        $ sna_chibi_ypos = walk_ypos2
        hide screen snape_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen snape_stand

    return
