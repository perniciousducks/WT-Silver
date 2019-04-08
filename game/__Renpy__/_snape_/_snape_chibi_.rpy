

###  SNAPE CHIBI UNIVERSAL SCREEN ###
screen s_c_u:
    tag snape_chibi
    add s_c_u_pic at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos) # (xpos=360, ypos=210)
    zorder 3

###  SNAPE'S CUM UNIVERSAL SCREEN ###
screen s_c_c_u:
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos+140, ypos=snape_cum_chibi_ypos)
    zorder 3



### SNAPE CHIBI SCREENS ###

screen snape_stand:
    tag snape_chibi

    add snape_chibi_stand xpos snape_chibi_xpos ypos snape_chibi_ypos xzoom snape_chibi_flip #zoom (1.0/scaleratio)

    zorder snape_chibi_zorder


screen snape_walk:
    tag snape_chibi

    add snape_chibi_walk at snape_walk(walk_xpos, walk_xpos2) xzoom snape_chibi_flip #zoom (1.0/scaleratio)

    zorder snape_chibi_zorder


label update_sna_chibi:
    $ snape_chibi_stand = "characters/snape/chibis/snape_stand.png"
    $ snape_chibi_walk = "snape_walk"
    return



screen snape_jerking_off:
    tag snape_chibi
    add "jerking_off_03_ani" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240)
    zorder 3

screen snape_jerking_off_cum:
    add "snape_cum_01" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240)
    zorder 3

screen snape_stands_holds_dick:
    tag snape_chibi
    add "images/animation/10_jerking_01.png" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240)
    zorder 3




label sna_chibi(action = "", xpos=str(snape_chibi_xpos), ypos=str(snape_chibi_ypos), pic = "", flip=False):
    hide screen snape_stand

    hide screen s_c_u
    hide screen snape_jerking_off
    hide screen snape_jerking_off_cum

    $ snape_chibi_xpos = 500
    $ snape_chibi_ypos = 250

    if xpos != snape_chibi_xpos:
        if xpos == "mid":
            $ snape_chibi_xpos = 500
        elif xpos == "desk":
            $ snape_chibi_xpos = 440
        elif xpos == "desk_close":
            $ snape_chibi_xpos = 420
        elif xpos == "door":
            $ snape_chibi_xpos = 750
        elif xpos.isdigit():
            $ snape_chibi_xpos = int(xpos)

    if ypos != snape_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ snape_chibi_ypos = 210
        elif ypos.isdigit():
            $ snape_chibi_ypos = int(ypos)

    #Snape Chibi Actions.

    #Special Images. These need custom xpos/ypos positions!
    if action == "image":

        if xpos == "desk":
            $ snape_chibi_xpos = 440
        elif xpos == "mid":
            $ snape_chibi_xpos = 500
        elif xpos == "door":
            $ snape_chibi_xpos = 750
        else:
            $ snape_chibi_xpos = 500

        if ypos == "base":
            $ snape_chibi_ypos = 210
        else:
            $ snape_chibi_ypos = 210

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
        if flip or snape_flip != 1: #Same variable that the main sprite is using. #1 == Default
            $ snape_chibi_flip = -1
            show screen snape_stand
        else:
            $ snape_chibi_flip = 1
            show screen snape_stand

    return


label sna_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = snape_speed, action = "", loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3

    hide screen snape_walk

    hide screen snape_stand

    if pos1 == "mid":
        $ walk_xpos = 500
    elif pos1 == "desk":
        $ walk_xpos = 440
    elif pos1 == "door":
        $ walk_xpos = 750
    else:
        $ walk_xpos = int(pos1)

    if pos2 == "mid":
        $ walk_xpos2 = 500
    elif pos2 == "desk":
        $ walk_xpos2 = 440
    elif pos2 == "door":
        $ walk_xpos2 = 750
    elif pos2 == "leave":
        $ walk_xpos2 = 750
        $ loiter = False
    else:
        $ walk_xpos2 = int(pos2)

    $ snape_chibi_ypos = 210 #Works for walking chibi, doesn't for standing (needs 210 for standing?!)
    $ snape_speed = speed #Speed of walking animation. (lower = faster)

    if walk_xpos > walk_xpos2: #right to left (snape_walk)
        $ snape_chibi_flip = 1
        show screen snape_walk
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = walk_xpos2
        hide screen snape_walk
        if loiter:
            show screen snape_stand
    else: #left to right (snape_walk)
        $ snape_chibi_flip = -1
        show screen snape_walk
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = walk_xpos2
        hide screen snape_walk
        if pos2 == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen snape_stand

    return
