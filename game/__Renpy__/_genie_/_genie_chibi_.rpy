

### GENIE CHIBI ###


###  GENIE CHIBI UNIVERSAL SCREEN ###
screen g_c_u: 
    tag genie
    add g_c_u_pic at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
 

###  GENIE'S CUM UNIVERSAL SCREEN ###
screen g_c_c_u: 
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos) #xpos=-45,ypos=5


screen genie_walk: #Default Genie walk animation. 
    tag genie_chibi
    add "genie_walk_ani" at genie_walk(walk_xpos, walk_xpos2) #Check __Init__.rpy for ypos

screen genie_walk_f: #Default Genie walk animation. 
    tag genie_chibi
    add "genie_walk_ani_f" at genie_walk(walk_xpos, walk_xpos2) #Check __Init__.rpy for ypos

screen genie_stands:
    tag genie_chibi
    add "characters/genie/chibis/standing.png" at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
    
screen genie_stands_f: #Genie stands. Facing left.
    tag genie_chibi
    add im.Flip("characters/genie/chibis/standing.png", horizontal=True) at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)

screen genie: #Sitting behind desk.
    tag genie_chibi
    add "images/main_room/11_genie_00.png" at Position(xpos=370, ypos=336, xanchor="center", yanchor="center")
    zorder 1


screen rum_screen: #Rummaging through the cumpboard.
    tag genie_chibi
    add "images/main_room/cupboard_open.png" at Position(xpos=120+140, ypos=280, xanchor="center", yanchor="center")
    add "images/main_room/chair_left.png" at Position(xpos=192+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+141, ypos=331, xanchor="center", yanchor="center") 
    add "rum" xpos 20+140 ypos 110
    zorder 1
    
screen feeding: #FEEDING THE PHOENIX.
    tag genie_chibi
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
    add "feeding" xpos 270+140 ypos 75
    zorder 1
    
screen petting: #PETTING THE PHOENIX.
    tag genie_chibi
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
    add "petting" xpos 250+140 ypos 65
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
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
    add "reading_near_fire" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen reading: #GENIE READING A BOOK.
    tag genie_chibi
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
    add "reading" xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading: #DONE READING THE BOOK.
    tag genie_chibi
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
    add im.Flip("images/animation/reading_07.png", horizontal=True) xpos 290+140 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.
    
screen done_reading_near_fire: #DONE READING THE BOOK BY THE FIRE.
    tag genie_chibi
    add "images/main_room/chair_left.png" at Position(xpos=180+140, ypos=300, xanchor="center", yanchor="center")
    add "images/main_room/09_table.png" at Position(xpos=220+140, ypos=330, xanchor="center", yanchor="center") 
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




label gen_chibi(action = "", xpos=str(genie_chibi_xpos), ypos=str(genie_chibi_ypos), pic = "", flip=False):
    hide screen genie_stands
    hide screen genie_stands_f

    hide screen g_c_u

    $ secretly_jerking_off = False
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

    hide screen genie_groping

    if xpos != genie_chibi_xpos:
        if xpos == "mid":
            $ genie_chibi_xpos = 500
        elif xpos == "desk":
            $ genie_chibi_xpos = 420
        elif xpos == "door":
            $ genie_chibi_xpos = 750
        elif xpos == "behind_desk":
            $ genie_chibi_xpos = 230
        elif xpos.isdigit():
            $ genie_chibi_xpos = int(xpos)

    if ypos != genie_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ genie_chibi_ypos = 190
        elif ypos.isdigit():
            $ genie_chibi_ypos = int(ypos)


    #Genie Chibi Actions.
            
    #Special Images. These need custom xpos/ypos positions!
    if action == "image":

        #Add specific xpos and ypos number when calling.

        if pic != "":
            $ s_c_u_pic = "characters/genie/chibis/"+str(pic)+".png"

        show screen g_c_u

    #Jerking off solo.
    elif action == "jerking" or action == "jerking_off" or action == "cumming" or action == "hold_dick":

        if xpos == "behind_desk":
            $ genie_chibi_xpos = 230
        if xpos == "on_girl":
            $ genie_chibi_xpos = 470

        if ypos == "behind_desk":
            $ genie_chibi_ypos = +10

        if action == "cumming":
            show screen genie_jerking_off_standing
            show screen genie_jerking_off_standing_cum

        elif action == "hold_dick":
            show screen genie_stands_holds_dick

        else:
            show screen genie_jerking_off_standing

    #Jerking off behind desk.
    elif action == "jerking_behind_desk" or action == "jerking_off_behind_desk" or action == "cumming_behind_desk" or action == "cum_on_desk":

        $ secretly_jerking_off = True

        if action == "cumming_behind_desk":
            show screen genie_jerking_off
            show screen genie_jerking_sperm
        elif action == "cum_on_desk":
            hide screen desk
            show screen genie
            show screen genie_jerking_sperm_02
        else:
            show screen genie_jerking_off

    #Handjob with Hermione.
    elif action == "handjob" or action == "handjob_pause" or action == "handjob_kiss" or action == "cumming_under_shirt" or action == "cumming_on_shirt" or action == "cumming_on_shirt_pause":

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
    elif action == "titjob" or action == "titjob_pause" or action == "titjob_cum_in_mouth" or action == "titjob_cum_on_tits":

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
            show screen genie_stands_f
        else:
            show screen genie_stands

    return


label gen_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = genie_speed, loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    with d3
    
    hide screen genie_walk
    hide screen genie_walk_f

    hide screen genie_stands
    hide screen genie_stands_f

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

    $ genie_chibi_ypos = 190
    $ genie_speed = speed #Speed of walking animation. (lower = faster)

    if walk_xpos > walk_xpos2: #right to left (genie_walk)
        show screen genie_walk_f #Genie's chibis are mirrored for whatever reason!
        $ tmp = genie_speed - redux_pause
        pause tmp
        $ genie_chibi_xpos = walk_xpos2
        hide screen genie_walk_f
        if loiter:
            show screen genie_stands_f
    else: #left to right (genie_walk_f)
        show screen genie_walk #Genie's chibis are mirrored for whatever reason! #Don't use flip here or he moonwalks!
        $ tmp = genie_speed - redux_pause
        pause tmp
        $ genie_chibi_xpos = walk_xpos2
        hide screen genie_walk
        if pos2 == "leave":
            call play_sound("door") 
            with d3
            pause.5
        if loiter:
            show screen genie_stands

    return
    



