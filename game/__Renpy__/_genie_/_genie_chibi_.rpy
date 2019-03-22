

### GENIE CHIBI ###


###  GENIE CHIBI UNIVERSAL SCREEN ###
screen g_c_u:
    tag genie
    add g_c_u_pic at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
    zorder 3


###  GENIE'S CUM UNIVERSAL SCREEN ###
screen g_c_c_u:
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos) #xpos=-45,ypos=5
    zorder 4



### SUSAN CHIBI SCREENS ###

screen genie_stand:
    tag genie_chibi

    add genie_chibi_stand xpos genie_chibi_xpos ypos genie_chibi_ypos xzoom genie_chibi_flip #zoom (1.0/scaleratio)

    zorder genie_chibi_zorder

screen genie_walk:
    tag genie_chibi

    add genie_chibi_walk at genie_walk(walk_xpos, walk_xpos2) xzoom genie_chibi_flip #zoom (1.0/scaleratio)

    zorder genie_chibi_zorder

label update_gen_chibi:
    $ genie_chibi_stand = "characters/genie/chibis/walk_01.png"
    $ genie_chibi_walk = "genie_walk_ani"

    return



screen genie: #Sitting behind desk.
    tag genie_chibi
    add "images/rooms/main_room/11_genie_00.png" at Position(xpos=370, ypos=336, xanchor="center", yanchor="center")
    zorder 1


screen rum_screen: #Rummaging through the cumpboard.
    tag genie_chibi
    add "images/rooms/_objects_/cupboard/cupboard_open.png" at Position(xpos=cupboard_OBJ.xpos, ypos=cupboard_OBJ.ypos, xanchor="center", yanchor="center")
    add "images/rooms/_objects_/cupboard/cupboard_open" +str(cupboard_deco)+ ".png" at Position(xpos=cupboard_OBJ.xpos, ypos=cupboard_OBJ.ypos, xanchor="center", yanchor="center") #Pinup Girl
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=332, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=371, ypos=331, xanchor="center", yanchor="center")
    add "genie_rum_ani" xpos 160 ypos 110
    zorder 1

screen feeding: #FEEDING THE PHOENIX.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=320, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    add "grab_high" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 #xpos 410 ypos 75
    zorder 1

screen petting: #PETTING THE PHOENIX.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=320, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    add "petting" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 #xpos 390 ypos 65
    zorder 1

screen sad_phoenix: #SAD SMILEY THAT SHOWS WHEN YOU PET THE BIRD.
    tag genie_chibi
    add "sad_01" xpos 423+140 ypos 130
    zorder 1


screen paperwork: #GENIE DOING PAPERWORK BEHIND HIS DESK.
    tag genie_chibi
    add "paperwork_02" xpos 84+140 ypos 205


screen reading_near_fire: #GENIE READING A BOOK BY THE FIRE.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "reading_near_fire" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen reading: #GENIE READING A BOOK.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "reading" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading: #DONE READING THE BOOK.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add im.Flip("images/animation/reading_07.png", horizontal=True) xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading_near_fire: #DONE READING THE BOOK BY THE FIRE.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "images/animation/reading_07.png" xpos 290+140 ypos 205

    zorder 4 #Because otherwise the bird food would be on top.

### JERKING OFF BEHIND DESK ###

screen genie_jerking_off: #Genie sitting behind his desk and jerking off...
    tag genie_chibi
    add "genie_jerking_off" xpos 218 ypos 205
    zorder 2

screen genie_jerking_sperm: #Genie's behind desk cum animation, CUM ONLY!
    add "genie_jerking_sperm_ani" xpos 218 ypos 205
    zorder 2

screen genie_jerking_sperm_02: #Genie's behind desk cum still image, CUM ONLY!
    add "images/animation/jerking_sperm_11.png" xpos 218 ypos 205
    zorder 2


### JERKING OFF STANDING ###

screen genie_jerking_off_standing:
    tag genie_chibi
    add "jerking_off_02_ani" at Position(xpos=genie_chibi_xpos-270, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_jerking_off_standing_cum:
    add "genie_cum_03" at Position(xpos=genie_chibi_xpos-270, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_stands_holds_dick:
    tag genie_chibi
    add "images/animation/06_jerking_01.png" at Position(xpos=genie_chibi_xpos-270, ypos=genie_chibi_ypos-185)
    zorder 2


### HANDJOB, Genie and Hermione ###

screen genie_handjob:
    tag genie_chibi
    add "handjob_ani" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_handjob_pause:
    tag genie_chibi
    add "images/animation/12_handjob_01.png" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_handjob_kiss:
    tag genie_chibi
    add "kiss_ani" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_on_shirt:
    add "on_shirt_cum_ani" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_on_shirt_pause:
    add "images/animation/15_cum_21.png" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_under_shirt:
    add "undershirt_cum_ani" at Position(xpos=genie_chibi_xpos-230, ypos=genie_chibi_ypos-185)
    zorder 2


### TITJOB HERMIONE ###
screen genie_titjob:
    tag genie_chibi
    add "titjob_ani" at Position(xpos=genie_chibi_xpos-30, ypos=genie_chibi_ypos)

screen genie_titjob_pause:
    tag genie_chibi
    add "characters/hermione/chibis/titjob/tj_cum_chest_01.png" at Position(xpos=genie_chibi_xpos-30, ypos=genie_chibi_ypos)

screen genie_titjob_cum_on_tits:
    tag genie_chibi
    add "titjob_chest_ani" at Position(xpos=genie_chibi_xpos-30, ypos=genie_chibi_ypos+10)

screen genie_titjob_cum_in_mouth:
    tag genie_chibi
    add "titjob_mouth_ani" at Position(xpos=genie_chibi_xpos-30, ypos=genie_chibi_ypos+10)


screen genie_groping:
    tag genie_chibi
    add "groping_ass_ani" at Position(xpos=genie_chibi_xpos-285, ypos=genie_chibi_ypos-185)




label gen_chibi(action = "", xpos=genie_chibi_xpos, ypos=genie_chibi_ypos, pic = "", flip=False):
    hide screen genie_stand

    hide screen g_c_u
    hide screen genie

    $ masturbating = False
    hide screen genie_jerking_off                #Jerking off sitting behind desk.
    hide screen genie_jerking_sperm_02           #Sperm on desk and floor.
    hide screen genie_jerking_sperm
    hide screen genie_jerking_off_standing
    hide screen genie_jerking_off_standing_cum

    hide screen genie_handjob
    hide screen genie_handjob_pause
    hide screen genie_handjob_kiss
    hide screen genie_handjob_cum_on_shirt
    hide screen genie_handjob_cum_on_shirt_pause
    hide screen genie_handjob_cum_under_shirt

    hide screen genie_titjob
    hide screen genie_titjob_pause
    hide screen genie_titjob_cum_in_mouth
    hide screen genie_titjob_cum_on_tits

    hide screen groping_01
    hide screen groping_02
    hide screen no_groping_01
    hide screen no_groping_02
    hide screen groping_03
    hide screen groping_naked_tits

    hide screen genie_groping
    hide screen blktone
    hide screen bld1

    if xpos != genie_chibi_xpos:
        if xpos == "mid":
            $ genie_chibi_xpos = 500
        elif xpos == "desk":
            $ genie_chibi_xpos = 420
        elif xpos == "on_girl": #Girl has to stand at mid.
            $ genie_chibi_xpos = 470
        elif xpos == "door":
            $ genie_chibi_xpos = 750
        elif xpos == "left":
            $ genie_chibi_xpos = 100
        elif xpos == "behind_desk":
            $ genie_chibi_xpos = 230
        else:
            $ genie_chibi_xpos = int(xpos)

    if ypos != genie_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ genie_chibi_ypos = 190
        elif ypos == "behind_desk":
            $ genie_chibi_ypos = 200
        else:
            $ genie_chibi_ypos = int(ypos)


    #Genie Chibi Actions.

    #Special Images. These need custom xpos/ypos positions!
    if action == "image":

        #Add specific xpos and ypos number when calling.

        if pic != "":
            $ s_c_u_pic = "characters/genie/chibis/"+str(pic)+".png"

        show screen g_c_u

    #Jerking off solo.
    elif action in ["jerking","jerking_off","cumming","hold_dick"]:

        if action == "cumming":
            show screen genie_jerking_off_standing
            show screen genie_jerking_off_standing_cum
        elif action == "hold_dick":
            show screen genie_stands_holds_dick
        else:
            show screen genie_jerking_off_standing

    #Sit behinde desk
    elif action in ["sit","sitting","sit_behind_desk"]:
        hide screen chair_left
        hide screen desk
        show screen genie

    #Jerking off behind desk.
    elif action in ["jerking_behind_desk","jerking_off_behind_desk","cumming_behind_desk","cum_on_desk","came_on_desk"]:

        $ masturbating = True

        if action == "cumming_behind_desk":
            show screen genie_jerking_off
            show screen genie_jerking_sperm
        elif action in ["cum_on_desk","came_on_desk"]:
            hide screen desk
            show screen genie
            show screen genie_jerking_sperm_02
        else:
            show screen genie_jerking_off

    #Handjob with Hermione.
    elif action in ["handjob","handjob_pause","handjob_kiss","cumming_under_shirt","cumming_on_shirt","cumming_on_shirt_pause"]:

        if action == "handjob":
            show screen genie_handjob
        if action == "handjob_pause":
            show screen genie_handjob_pause
        if action == "handjob_kiss":
            show screen genie_handjob_kiss
        if action == "cumming_on_shirt":
            show screen genie_handjob_cum_on_shirt
        if action == "cumming_on_shirt_pause":
            show screen genie_handjob_cum_on_shirt_pause
        if action == "cumming_under_shirt":
            show screen genie_handjob_cum_under_shirt

    #Titjob
    elif action in ["titjob","titjob_pause","titjob_cum_in_mouth","titjob_cum_on_tits"]:

        if action == "titjob":
            show screen genie_titjob
        if action == "titjob_pause":
            show screen genie_titjob_pause
        if action == "titjob_cum_in_mouth":
            show screen genie_titjob_cum_in_mouth
        if action == "titjob_cum_on_tits":
            show screen genie_titjob_cum_on_tits

        if xpos == "behind_desk": #No xpos change.
            hide screen desk
            show screen desk

    elif action == "groping":
        show screen genie_groping

    elif action == "hide":
        pass

    elif action == "leave":
        call play_sound("door")
        with d3
        pause.5

    else:
        if flip or genie_flip != 1: #Same variable that the main sprite is using. #1 == Default
            $ genie_chibi_flip = -1
            show screen genie_stand
        else:
            $ genie_chibi_flip = 1
            show screen genie_stand

    return


label gen_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = genie_speed, loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    with d3

    hide screen genie_walk

    hide screen genie_stand

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
    elif pos2 == "left":
        $ walk_xpos2 = 100
    elif pos2 == "door":
        $ walk_xpos2 = 750
    elif pos2 == "leave":
        $ walk_xpos2 = 750
        $ loiter = False
    else:
        $ walk_xpos2 = int(pos2)

    $ genie_chibi_ypos = 190
    $ genie_speed = speed #Speed of walking animation. (lower = faster)

    if walk_xpos > walk_xpos2: #right to left (genie_walk)
        $ genie_chibi_flip = -1 #ToDo - Flip Genie's images so this can be the same as every other chibi ( 1 )
        show screen genie_walk
        $ tmp = genie_speed - redux_pause
        pause tmp
        $ genie_chibi_xpos = walk_xpos2
        hide screen genie_walk
        if loiter:
            show screen genie_stand
    else: #left to right (genie_walk)
        $ genie_chibi_flip = 1 #ToDo - Flip Genie's images so this can be the same as every other chibi ( -1 )
        show screen genie_walk
        $ tmp = genie_speed - redux_pause
        pause tmp
        $ genie_chibi_xpos = walk_xpos2
        hide screen genie_walk
        if pos2 == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen genie_stand

    return
