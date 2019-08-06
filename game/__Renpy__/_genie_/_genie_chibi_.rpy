

### GENIE CHIBI ###


###  GENIE CHIBI UNIVERSAL SCREEN ###
screen g_c_u():
    tag genie
    add g_c_u_pic xpos gen_chibi_xpos ypos gen_chibi_ypos xzoom gen_chibi_flip
    zorder 3


###  GENIE'S CUM UNIVERSAL SCREEN ###
screen g_c_c_u():
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos) #xpos=-65,ypos=5
    zorder 4


screen genie(): #Sitting behind desk.
    tag genie_chibi
    add "images/rooms/main_room/11_genie_00.png" at Position(xpos=370, ypos=336, xanchor="center", yanchor="center")
    zorder 1


screen rum_screen(): #Rummaging through the cumpboard.
    tag genie_chibi
    add "images/rooms/_objects_/cupboard/cupboard_open.png" at Position(xpos=cupboard_OBJ.xpos, ypos=cupboard_OBJ.ypos, xanchor="center", yanchor="center")
    add "images/rooms/_objects_/cupboard/cupboard_open" +str(cupboard_deco)+ ".png" at Position(xpos=cupboard_OBJ.xpos, ypos=cupboard_OBJ.ypos, xanchor="center", yanchor="center") #Pinup Girl
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=332, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=371, ypos=331, xanchor="center", yanchor="center")
    add "genie_rum_ani" xpos 160 ypos 110
    zorder 1

screen feeding(): #FEEDING THE PHOENIX.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=320, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    add "grab_high" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 #xpos 410 ypos 75
    zorder 1

screen petting(): #PETTING THE PHOENIX.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=320, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    add "petting" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5 #xpos 390 ypos 65
    zorder 1

screen sad_phoenix(): #SAD SMILEY THAT SHOWS WHEN YOU PET THE BIRD.
    tag genie_chibi
    add "sad_01" xpos 423+140 ypos 130
    zorder 1


screen paperwork(): #GENIE DOING PAPERWORK BEHIND HIS DESK.
    tag genie_chibi
    add "paperwork_02" xpos 84+140 ypos 205


screen reading_near_fire(): #GENIE READING A BOOK BY THE FIRE.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "reading_near_fire" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen reading(): #GENIE READING A BOOK.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "reading" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading(): #DONE READING THE BOOK.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add im.Flip("characters/genie/chibis/reading/07.png", horizontal=True) xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading_near_fire(): #DONE READING THE BOOK BY THE FIRE.
    tag genie_chibi
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center")
    add "characters/genie/chibis/reading/07.png" xpos 290+140 ypos 205

    zorder 4 #Because otherwise the bird food would be on top.

### JERKING OFF BEHIND DESK ###

screen genie_jerking_off(): #Genie sitting behind his desk and jerking off...
    tag genie_chibi
    add "genie_jerking_off" xpos 218 ypos 205
    zorder 2

screen genie_jerking_sperm(): #Genie's behind desk cum animation, CUM ONLY!
    add "genie_jerking_sperm_ani" xpos 218 ypos 205
    zorder 2

screen genie_jerking_sperm_02(): #Genie's behind desk cum still image, CUM ONLY!
    add "characters/genie/chibis/masturbating/desk_sperm_11.png" xpos 218 ypos 205
    zorder 2


### JERKING OFF STANDING ###

screen genie_jerking_off_standing():
    tag genie_chibi
    add "jerking_off_02_ani" at Position(xpos=gen_chibi_xpos-270, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_jerking_off_standing_cum():
    add "genie_cum_03" at Position(xpos=gen_chibi_xpos-290, ypos=gen_chibi_ypos-190) #x270, y185 #290
    zorder 4

screen genie_stands_holds_dick():
    tag genie_chibi
    add "characters/genie/chibis/masturbating/01.png" at Position(xpos=gen_chibi_xpos-270, ypos=gen_chibi_ypos-185)
    zorder 2


### HANDJOB, Genie and Hermione ###

screen genie_handjob():
    tag genie_chibi
    add "handjob_ani" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_handjob_pause():
    tag genie_chibi
    add "characters/hermione/chibis/handjob/01.png" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_handjob_kiss():
    tag genie_chibi
    add "kiss_ani" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_on_shirt():
    add "on_shirt_cum_ani" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_on_shirt_pause():
    add "characters/hermione/chibis/handjob/sperm_on_21.png" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2

screen genie_handjob_cum_under_shirt():
    add "undershirt_cum_ani" at Position(xpos=gen_chibi_xpos-230, ypos=gen_chibi_ypos-185)
    zorder 2


### TITJOB HERMIONE ###
screen genie_titjob():
    tag genie_chibi
    add "titjob_ani" at Position(xpos=gen_chibi_xpos-30, ypos=gen_chibi_ypos)

screen genie_titjob_pause():
    tag genie_chibi
    add "characters/hermione/chibis/titjob/tj_cum_chest_01.png" at Position(xpos=gen_chibi_xpos-30, ypos=gen_chibi_ypos)

screen genie_titjob_cum_on_tits():
    tag genie_chibi
    add "titjob_chest_ani" at Position(xpos=gen_chibi_xpos-30, ypos=gen_chibi_ypos+10)

screen genie_titjob_cum_in_mouth():
    tag genie_chibi
    add "titjob_mouth_ani" at Position(xpos=gen_chibi_xpos-30, ypos=gen_chibi_ypos+10)


screen genie_groping():
    tag genie_chibi
    add "groping_ass_ani" at Position(xpos=gen_chibi_xpos-285, ypos=gen_chibi_ypos-185)



### SUSAN CHIBI SCREENS ###

screen genie_stand():
    tag genie_chibi

    add gen_chibi_stand xpos gen_chibi_xpos ypos gen_chibi_ypos xzoom gen_chibi_flip #zoom (1.0/scaleratio)

    zorder gen_chibi_zorder

screen genie_walk():
    tag genie_chibi
    add gen_chibi_walk         at gen_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom gen_chibi_flip #zoom (1.0/scaleratio)

    zorder gen_chibi_zorder

label update_gen_chibi:
    $ gen_chibi_stand = "characters/genie/chibis/walk_01.png"
    $ gen_chibi_walk = "genie_walk_ani"

    return



label gen_chibi(action = "", xpos=gen_chibi_xpos, ypos=gen_chibi_ypos, pic = "", flip=False):
    hide screen genie_stand

    hide screen g_c_u
    hide screen genie

    hide screen jerking_off_01                   #Hermione topless. Genie jerking off.
    hide screen genie_jerking_off                #Jerking off sitting behind desk.
    hide screen genie_jerking_sperm_02           #Sperm on desk and floor.
    hide screen genie_jerking_sperm
    hide screen genie_jerking_off_standing
    hide screen genie_jerking_off_standing_cum

    # Favors
    hide screen hermione_chibi_ass
    hide screen hermione_chibi_hj
    hide screen hermione_chibi_bj
    hide screen hermione_chibi_sex

    hide screen genie_titjob
    hide screen genie_titjob_pause
    hide screen genie_titjob_cum_in_mouth
    hide screen genie_titjob_cum_on_tits

    hide screen groping_01    # Grope Ass fully clothed - Flip = True (facing door)
    hide screen groping_02    # Grope Ass fully clothed - Flip = False
    hide screen no_groping_01 # Hermione stands with you behind desk - Flip = True (facing door)
    hide screen no_groping_02 # Hermione stands with you behind desk - Flip = False

    hide screen groping_03         # Grope breasts fully clothed
    hide screen genie_and_tits_01
    hide screen groping_naked_tits
    hide screen genie_groping

    hide screen rum_screen

    hide screen blktone
    hide screen bld1

    if xpos != gen_chibi_xpos:
        if xpos == "mid":
            $ gen_chibi_xpos = 500
        elif xpos == "desk":
            $ gen_chibi_xpos = 420
        elif xpos == "on_girl": #Girl has to stand at mid.
            $ gen_chibi_xpos = 470
        elif xpos == "door":
            $ gen_chibi_xpos = 750
        elif xpos == "left":
            $ gen_chibi_xpos = 100
        elif xpos == "behind_desk":
            $ gen_chibi_xpos = 210
        elif xpos == "cupboard":
            $ gen_chibi_xpos = 260
        else:
            $ gen_chibi_xpos = int(xpos)

    if ypos != gen_chibi_ypos:
        if ypos in ["base","default"]:
            $ gen_chibi_ypos = 190
        elif ypos == "behind_desk":
            $ gen_chibi_ypos = 190
        else:
            $ gen_chibi_ypos = int(ypos)


    #Genie Chibi Actions.

    #Special Images. These need custom xpos/ypos positions!
    if action in ["image","animation"]:
        if flip:
            $ gen_chibi_flip = -1
        else:
            $ gen_chibi_flip = 1

        if pic != "":

            #Add specific xpos and ypos number when calling.
            if action == "animation":
                $ g_c_u_pic = pic
            else:
                $ g_c_u_pic = "characters/genie/chibis/"+str(pic)+".png"

        show screen g_c_u

    #Jerking off solo.
    elif action in ["jerk_off","jerking","jerking_off","cumming","hold_dick"]:

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
        if flip:
            $ gen_chibi_flip = -1
            show screen genie_stand
        else:
            $ gen_chibi_flip = 1
            show screen genie_stand

    return


### Genie Chibi Walk ###

# xpos + ypos = position the chibi walks to.
# action = "enter", sets the starting position of the chibi at the entrance (door).
# action = "leave", automatically hide the chibi with a door sound and pause.
# speed = time it will take for the chibi to move A to B in seconds. Lower value = faster walk.
# loiter = flag that shows the standing chibi after the walk, default is True
# redux_pause = value to decrease the time to pause before hideing the animation early

label gen_walk(xpos=walk_xpos, ypos=walk_ypos, speed=gen_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    hide screen genie_walk
    hide screen genie_stand

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ gen_chibi_xpos = 750
        $ gen_chibi_ypos = 250
    if action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = gen_chibi_xpos
    $ walk_ypos = gen_chibi_ypos

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

    $ gen_speed = speed #Speed of walking animation. (lower = faster)


    # Walk right to left
    if walk_xpos > walk_xpos2:
        $ gen_chibi_flip = -1 #ToDo - Flip Genie's images so this can be the same as every other chibi ( 1 )
        show screen genie_walk
        $ tmp = gen_speed - redux_pause
        $ renpy.pause(tmp)
        $ gen_chibi_xpos = walk_xpos2
        $ gen_chibi_ypos = walk_ypos2
        hide screen genie_walk
        if loiter:
            show screen genie_stand

    # Walk left to right
    else:
        $ gen_chibi_flip = 1 #ToDo - Flip Genie's images so this can be the same as every other chibi ( -1 )
        show screen genie_walk
        $ tmp = gen_speed - redux_pause
        $ renpy.pause(tmp)
        $ gen_chibi_xpos = walk_xpos2
        $ gen_chibi_ypos = walk_ypos2
        hide screen genie_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen genie_stand

    return
