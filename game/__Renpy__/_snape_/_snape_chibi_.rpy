
  
###  SNAPE CHIBI UNIVERSAL SCREEN ###
screen s_c_u: 
    tag snape_chibi
    add s_c_u_pic at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos) # (xpos=360, ypos=210) 
    zorder 3

###  SNAPE'S CUM UNIVERSAL SCREEN ###
screen s_c_c_u: 
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos+140, ypos=snape_cum_chibi_ypos)


### SNAPE CHIBI
screen snape_01: #Snape stands still near the door.
    tag snape_chibi
    add "characters/snape/chibis/snape_stand.png" at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos-40)
    
screen snape_01_f: #Snape stands still near the door. (Mirrored).
    tag snape_chibi
    add im.Flip("characters/snape/chibis/snape_stand.png", horizontal=True) at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos-40)
  
screen snape_walk: #Default Snape walk animation. 
    tag snape_chibi
    add "snape_walk" at custom_walk(walk_xpos, walk_xpos2)
    zorder 4

screen snape_walk_f: #Default Snape walk animation. (Mirrored).
    tag snape_chibi
    add "snape_walk_f" at custom_walk(walk_xpos, walk_xpos2)
    zorder 4

screen snape_jerking_off:
    tag snape_chibi
    add "jerking_off_03_ani" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240) 

screen snape_jerking_off_cum:
    add "snape_cum_01" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240) 

screen snape_stands_holds_dick:
    tag snape_chibi
    add "images/animation/10_jerking_01.png" at Position(xpos=snape_chibi_xpos-500, ypos=snape_chibi_ypos-240)




label sna_chibi(action = "", xpos=snape_chibi_xpos, ypos=snape_chibi_ypos, pic = "", flip=False):
    hide screen snape_01
    hide screen snape_01_f

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

    if ypos != snape_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ snape_chibi_ypos = 250
        if ypos == "on_desk":
            $ snape_chibi_ypos = 250


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
            $ snape_chibi_ypos = 250
        else:
            $ snape_chibi_ypos = 250

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
            show screen snape_01_f
        else:
            show screen snape_01

    return


label sna_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = snape_speed, loiter = True,redux_pause = 0):
    hide screen sna_main
    hide screen bld1
    hide screen blktone
    with d3
    
    hide screen snape_walk
    hide screen snape_walk_f

    hide screen snape_01
    hide screen snape_01_f

    if pos1 == "mid":
        $ walk_xpos = 500
    elif pos1 == "desk":
        $ walk_xpos = 440
    elif pos1 == "door":
        $ walk_xpos = 750
    else:
        $ walk_xpos = pos1

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
        $ walk_xpos2 = pos2

    $ snape_chibi_ypos = 250 #Works for walking chibi, doesn't for standing (needs 210 for standing?!)
    $ snape_speed = speed #Speed of walking animation. (lower = faster)

    if walk_xpos > walk_xpos2: #right to left (snape_walk)
        show screen snape_walk
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = walk_xpos2
        hide screen snape_walk
        if loiter:
            show screen snape_01
    else: #left to right (snape_walk_f)
        show screen snape_walk_f
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = walk_xpos2
        hide screen snape_walk_f
        if pos2 == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen snape_01_f

    return
    
