

### HERMIONE CHIBI SCREENS ###



screen her_wand_slow():  # Hermione rubs wand slowly
    add "rub_wand_slow_ani"

screen hermione_02_w(): #Hermione stands still wearing a robe.
    tag hermione
    add "images/animation/h_Wand_01s.png" at Position(xpos=her_chibi_xpos+140, ypos=her_chibi_ypos)
screen hermione_02_wSlow(): #Hermione rubs wand between her legs slowly.
    tag hermione
    add "rub_wand_slow_ani" at Position(xpos=her_chibi_xpos+140, ypos=her_chibi_ypos)
screen hermione_02_wFast(): #Hermione rubs wand between her legs quickly.
    tag hermione
    add "rub_wand_fast_ani" at Position(xpos=her_chibi_xpos+140, ypos=her_chibi_ypos)
screen hermione_02_wf1(): #Hermione finishes rubbing the wand - eyes closed.
    tag hermione
    add "images/animation/h_Wand_01f.png" at Position(xpos=her_chibi_xpos+140, ypos=her_chibi_ypos)
screen hermione_02_wf2(): #Hermione finishes rubbing the wand - eyes opened.
    tag hermione
    add "images/animation/h_Wand_02s.png" at Position(xpos=her_chibi_xpos+140, ypos=her_chibi_ypos)



### HERMIONE CHIBI ACTIONS ###

#Lift top.
screen hermione_chibi_lift_top():
    tag hermione_chibi
    add "characters/hermione/chibis/lift_top/tits_00.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder

#Lift skirt.
screen hermione_chibi_lift_skirt():
    tag hermione_chibi
    if hermione_wear_panties:
        if hg_pf_show_panties_OBJ.points <= 1:
            add "characters/hermione/chibis/lift_skirt/panties_00.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
        else:
            add "characters/hermione/chibis/lift_skirt/panties_01.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    else:
        add "characters/hermione/chibis/lift_skirt/panties_02.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder

#Drink potion.
screen ch_potion():
    tag hermione_chibi
    add "ch_hem potion" at Position(xpos=her_chibi_xpos-30, ypos=her_chibi_ypos)
    zorder her_chibi_zorder



### HERMIONE CHIBI FAVOUR SCREENS (with Genie or Snape,...) ###

### GROPING ###
screen groping_01(): #Facing Genie.
    tag favor
    add "groping_01" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)

screen groping_02(): #Facing Genie.
    tag favor
    add "groping_02" at Position(xpos=-60, ypos=10)
    add "groping_02_blinking" at Position(xpos=-60, ypos=10)

screen no_groping_01(): #Facing Genie.
    tag favor
    add "images/animation/grope_05.png" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)

screen no_groping_02(): #Facing Genie.
    tag favor
    add "images/animation/grope_b_05.png" at Position(xpos=-60, ypos=10)
    add "groping_02_blinking" at Position(xpos=-60, ypos=10)


### MOLESTING TITS FULLY CLOTHED ###
screen groping_03(): #Facing Genie.
    tag favor
    add "groping_03_ani" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)

### MOLESTING NAKED TITS ###
screen groping_naked_tits():
    tag favor
    add "groping_naked_tits_ani" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    zorder 1 #Otherwise chair is on top.

### JERKING OFF ###
screen jerking_off_01():
    tag favor
    add "jerking_off_ani" at Position(xpos=-60, ypos=10)
    if not no_blinking: #When True - blinking animation is not displayed.
        add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    zorder 1 #Otherwise chair is on top.

### SPERM ###
screen jerking_off_cum():
    add "jerking_off_cum_ani" at Position(xpos=-60, ypos=10)
    #add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 2 #Otherwise there is a bug with blinking.

### ADMIRING TITS ###
screen genie_and_tits_01(): #Genie sitting, looking ar naked tits. Hermione stands right in front of him. (Behind the desk even).
    tag favor
    add "images/rooms/main_room/admire_tits_00.png" at Position(xpos=-60, ypos=10)



### HERMIONE DANCING ###
screen hermione_chibi_dance():
    tag hermione_chibi
    if hermione_wear_top:
        if h_top == "top_1" or h_top == "top_6":
            add "clothed_dance_ani" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
        else:
            if hermione_wear_bottom:
                add "no_vest_dance_ani" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
            else:
                add "no_skirt_dance_ani" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)

    else:
        if hermione_wear_bottom:
            add "no_shirt_dance_ani" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
        else: #Nude
            add "no_shirt_no_skirt_dance_ani" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder


### SIT NAKED ###
screen hermione_chibi_sit_naked_A():
    tag hermione_chibi
    add "characters/hermione/chibis/sitting/sit_naked_blink.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder
screen hermione_chibi_sit_naked_B():
    tag hermione_chibi
    add "characters/hermione/chibis/sitting/sit_naked.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder
screen hermione_chibi_stand_no_shirt():
    tag hermione_chibi
    add "characters/hermione/chibis/dance/03_no_shirt_03.png" at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)
    zorder her_chibi_zorder

### UNIVERSAL SCREEN ###
screen h_c_u():
    tag hermione_chibi
    add h_c_u_pic at Position(xpos=her_chibi_xpos, ypos=her_chibi_ypos)








### Hermione stand & Hermione walk screens ###

screen hermione_stand():
    tag hermione_chibi

    add her_chibi_stand    xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip #zoom (1.0/scaleratio)
    #add her_chibi_shoes    xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip zoom (1.0/scaleratio)
    #add her_chibi_top      xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip zoom (1.0/scaleratio)
    #add her_chibi_bottom   xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip zoom (1.0/scaleratio)
    #add her_chibi_robe     xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip zoom (1.0/scaleratio)

    zorder her_chibi_zorder


screen hermione_walk():
    tag hermione_chibi

    add her_chibi_walk         at her_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom her_chibi_flip #zoom (1.0/scaleratio)
    #add her_chibi_walk_shoes   at her_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom her_chibi_flip zoom (1.0/scaleratio)

    #add her_chibi_top          at her_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom her_chibi_flip zoom (1.0/scaleratio)
    #add her_chibi_bottom       at her_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom her_chibi_flip zoom (1.0/scaleratio)
    #add her_chibi_robe         at her_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2) xzoom her_chibi_flip zoom (1.0/scaleratio)

    zorder her_chibi_zorder


label update_chibi_uniform:

    #Naked
    if not hermione_wear_top and not hermione_wear_bottom and not hermione_wear_robe:
        $ her_chibi_stand    = "ch_hem blink_n"
        $ her_chibi_walk     = "ch_hem walk_n"

    #Robe
    elif hermione_wear_robe and hermione_wear_top:
        $ her_chibi_stand    = "ch_hem blink_robe"
        $ her_chibi_walk     = "ch_hem walk_robe"

    elif hermione_wear_robe and not hermione_wear_top:
        $ her_chibi_stand    = "ch_hem blink_robe_n"
        $ her_chibi_walk     = "ch_hem walk_robe_n"

    # Uniform
    else:
        $ her_chibi_stand    = "ch_hem blink_a"
        $ her_chibi_walk     = "ch_hem walk_a"

    return




### HERMIONE MAIN CHIBI ###

label her_chibi(action = "", xpos=her_chibi_xpos, ypos=her_chibi_ypos, pic = "", flip=False):
    hide screen hermione_stand
    hide screen hermione_walk

    hide screen h_c_u
    hide screen hermione_chibi_dance

    hide screen hermione_chibi_lift_top
    hide screen hermione_chibi_lift_skirt

    hide screen ch_potion
    hide screen ch_hotdog

    if xpos != her_chibi_xpos:
        if xpos == "mid":
            $ her_chibi_xpos = 540
        elif xpos == "desk":
            $ her_chibi_xpos = 440
        elif xpos == "on_desk":
            $ her_chibi_xpos = 350
        elif xpos == "door":
            $ her_chibi_xpos = 750
        else:
            $ her_chibi_xpos = int(xpos)

    if ypos != her_chibi_ypos:
        if ypos == "base" or ypos == "default":
            $ her_chibi_ypos = 250
        elif ypos == "on_desk":
            $ her_chibi_ypos = 180
        else:
            $ her_chibi_ypos = int(ypos)


    #Hermione Chibi Actions.
    if action == "lift_top":
        show screen hermione_chibi_lift_top

    elif action == "lift_skirt":
        show screen hermione_chibi_lift_skirt

    #Hermione Chibi Dance. #Strips automatically when removing clothes.
    elif action == "dance":
        show screen hermione_chibi_dance

    #Stnad top less
    elif action == "top_naked":
        show screen hermione_chibi_stand_no_shirt

    #Sit Naked
    elif action == "sit_naked":
        show screen hermione_chibi_sit_naked_A
    elif action == "sit_naked_wide_eyes" or action == "sit_naked_scared" or action == "sit_naked_shocked":
        show screen hermione_chibi_sit_naked_B

    #Drink POTION
    elif action == "drink_potion":
        show screen ch_potion

    #Special Images. These need custom xpos/ypos positions!
    elif action == "image":

        #Add specific xpos and ypos number when calling.

        if pic != "":
            $ h_c_u_pic = "characters/hermione/chibis/"+str(pic)+".png"

        show screen h_c_u



    elif action == "hide":
        pass

    elif action == "leave":
        call play_sound("door")
        hide screen hermione_main
        hide screen bld1
        hide screen blktone
        with d3
        pause.5

    else:
        if flip:
            $ her_chibi_flip = -1
            show screen hermione_stand
        else:
            $ her_chibi_flip = 1
            show screen hermione_stand

    return


### Hermione Chibi Walk ###

# xpos + ypos = position the chibi walks to.
# action = "enter", sets the starting position of the chibi at the entrance (door).
# action = "leave", automatically hide the chibi with a door sound and pause.
# speed = time it will take for the chibi to move A to B in seconds. Lower value = faster walk.
# loiter = flag that shows the standing chibi after the walk, default is True
# redux_pause = value to decrease the time to pause before hideing the animation early

label her_walk(xpos=walk_xpos, ypos=walk_ypos, speed=her_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    hide screen hermione_stand
    hide screen hermione_walk

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ her_chibi_xpos = 750
        $ her_chibi_ypos = 250
    if action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False
    if action == "run":
        $ her_chibi_walk = "ch_hem run_a"

    # Start position.
    $ walk_xpos = her_chibi_xpos
    $ walk_ypos = her_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 540
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ["base","default"]:
        $ walk_ypos2 = 250
    else:
        $ walk_ypos2 = int(ypos)

    $ her_speed = speed #Speed of walking animation. (lower = faster)


    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ her_chibi_flip = 1
        show screen hermione_walk
        $ tmp = her_speed - redux_pause
        $ renpy.pause(tmp)
        $ her_chibi_xpos = walk_xpos2
        $ her_chibi_ypos = walk_ypos2
        hide screen hermione_walk
        if loiter:
            show screen hermione_stand

    # Walk left to right (flipped)
    else:
        $ her_chibi_flip = -1
        show screen hermione_walk
        $ tmp = her_speed - redux_pause
        $ renpy.pause(tmp)
        $ her_chibi_xpos = walk_xpos2
        $ her_chibi_ypos = walk_ypos2
        hide screen hermione_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.5
        if loiter:
            show screen hermione_stand

    return




# label to be called to remove hermiones chibi from the screen
#
# @param dissolveTime how long to use the desolve transition for i.e.(2=d2, 3=d3)
label her_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen hermione_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen hermione_stand
    return



label set_h_animation(ani=u_h_animation, xpos = u_h_ani_xpos, ypos = u_h_ani_ypos):
    if ani != u_h_animation:
        $ u_h_animation = ani
    if ani == "sex_ani":
        $ u_h_ani_xpos = -210
        $ u_h_ani_ypos = 10
    if ani == "blowjob_ani":
        $ u_h_animation_paused = "hand_ani"
        $ u_h_ani_xpos = -150
        $ u_h_ani_ypos = 10
    return

label play_h_animation:
    hide screen u_h_ani_scr_pause
    if u_h_animation == "sex_ani":
        hide screen genie
        show screen chair_left
    if ani == "blowjob_ani":
        hide screen genie
        show screen chair_left
    #if:

    show screen u_h_ani_scr
    return

label pause_u_animation:
    hide screen u_h_ani_scr
    show screen u_h_ani_scr_pause
    with d2
    return

label end_h_animation:
    if u_h_animation == "sex_ani":
        show screen genie
        hide screen chair_left
        hide screen u_h_ani_scr
    #if:
    return


screen u_h_ani_scr():
    add u_h_animation at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)

screen u_h_ani_scr_pause():
    add u_h_animation_paused at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
