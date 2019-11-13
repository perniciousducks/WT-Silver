
# Label used to set up chibi scenes with Hermione and Genie in it
label hg_chibi_transition(action="stand", xpos="mid", ypos="base", flip=False, trans=None):
    if trans != None:
        call hide_characters
    show screen blkfade

    $ menu_y = 0.75 # Menu moved down.
    call her_chibi("hide")
    call gen_chibi("hide")

    if action in ["lift_top", "lift_skirt"]:
        $ menu_y = 0.5
        call her_chibi(action, xpos, ypos, flip)
        call gen_chibi("sit_behind_desk")

    elif action in ["admire_breasts"]:
        show screen genie_and_tits_01

    elif action in ["stand_behind_desk"]:
        if flip:
            show screen no_groping_02 # Towards Door.
        else:
            show screen no_groping_01 # Towards Cupboard.

    elif action in ["admire_ass","admire_ass_jerk_off","admire_ass_cum"]:
        if action == "admire_ass": # Bend over desk, with clothes on.
            show screen hermione_chibi_ass(ani=action)
        else:
            show screen chair_left
            if flip:
                $ masturbating = True
                if action == "admire_ass_jerk_off":
                    call gen_chibi("jerking_off","behind_desk","base")
                if action == "admire_ass_cum":
                    call gen_chibi("cumming","behind_desk","base")
            show screen no_groping_02

    elif action in ["grope_breasts"]:
        show screen chair_left

        if hermione_use_action and hermione_action in ["lift_top"]:
            show screen groping_naked_tits
        else:
            show screen groping_03

    elif action in ["grope_ass"]:
        if flip:
            show screen groping_02 # Towards Door.
        else:
            show screen groping_01 # Towards Cupboard.
    
    elif action in ("grope_on_podium_horny", "grope_on_podium_close", "grope_on_podium_cumming", "grope_on_podium_idle", "grope_on_podium_cumming"):
        show screen grope_on_podium(action)
        
    elif action in ["jerk_off"]:
        show screen chair_left
        show screen jerking_off_01

    ### Handjob ###
    elif action in ["hj","hj_pause","hj_kiss","hj_cumming_in","hj_cumming_in_pause","hj_cumming_on","hj_cumming_on_pause"]:
        show screen chair_left
        show screen desk
        show screen hermione_chibi_hj(ani=action, xpos=230, ypos=0)

    ### Titjob ###
    elif action in ["tj","tj_pause","tj_idle","tj_bj_pause","tj_cumming_in","tj_cumming_in_pause","tj_cumming_on","tj_cumming_on_pause"]:
        show screen chair_left
        show screen desk
        show screen hermione_chibi_tj(ani=action, xpos=450, ypos=200)

    ### Blowjob ###
    elif action in ["bj","bj_pause","bj_cumming_in","bj_cumming_out","bj_cumming_out_blink"]:
        show screen chair_left
        show screen hermione_chibi_bj(ani=action)
        if action in ["bj_cumming_out","bj_cumming_out_blink"]:
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_07.png"

    ### Sex ###
    elif action in ["sex","sex_slow","sex_fast","sex_pause","sex_cumming_out","sex_cumming_out_blink","sex_creampie","sex_creampie_blink"]:
        show screen chair_left
        show screen hermione_chibi_sex(ani=action)
        if action in ["sex_cumming_out","sex_cumming_out_blink","sex_creampie","sex_creampie_blink"]:
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"

    else:
        $ menu_y = 0.5
        call reset_hermione
        call her_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    hide screen bld1
    hide screen blkfade

    if trans != None:
        call transition(trans)

    return

### HERMIONE CHIBI FAVOUR SCREENS (with Genie or Snape,...) ###

### GROPING ###
screen groping_01(): # Grope Ass fully clothed (front)
    tag favor
    if hermione_wear_top == False and hermione_wear_bottom == False:
        add "characters/hermione/chibis/fingering/02.png" xpos -60 ypos 10 zoom 0.5
        add "fingering_blinking" at Position(xpos=-60, ypos=10)
    else:
        add "grope_ass_front" at Position(xpos=-60, ypos=10)
        add "grope_front_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

screen groping_02(): # Grope Ass fully clothed (back)
    tag favor
    add "grope_ass_back" at Position(xpos=-60, ypos=10)
    add "grope_back_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

screen no_groping_01(): # Hermione stands with you behind desk - Flip = True (facing door)
    tag favor
    add "characters/hermione/chibis/grope_ass/front_05.png" xpos -60 ypos 10 zoom 0.5
    add "grope_front_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

screen no_groping_02(): # Hermione stands with you behind desk - Flip = False
    tag favor
    if hermione_wear_top == False and hermione_wear_bottom == False:
        if masturbating:
            add "characters/hermione/chibis/fingering/back_n_solo.png" xpos -60 ypos 10 zoom 0.5
        else:
            add "characters/hermione/chibis/fingering/back_n_idle.png" xpos -60 ypos 10 zoom 0.5
        add "fingering_blinking" at Position(xpos=-60, ypos=10)
    else:
        add "characters/hermione/chibis/grope_ass/back_b_05.png" xpos -60 ypos 10 zoom 0.5
        add "grope_back_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

screen grope_on_podium(action):
    tag favor
    if action in ("grope_on_podium_horny", "grope_on_podium_close", "grope_on_podium_cumming", "grope_on_podium_idle", "grope_on_podium_cumming"):
        add action pos (328, 100)

### MOLESTING TITS FULLY CLOTHED ###
screen groping_03(): # Grope breasts fully clothed
    tag favor
    add "groping_tits" at Position(xpos=-60, ypos=10)
    add "grope_front_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

### MOLESTING NAKED TITS ###
screen groping_naked_tits():
    tag favor
    add "groping_naked_tits_ani" at Position(xpos=-60, ypos=10)
    add "grope_front_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

### JERKING OFF ###
screen jerking_off_01():
    tag favor
    add "jerking_off_ani" at Position(xpos=-60, ypos=10)
    if not no_blinking: #When True - blinking animation is not displayed.
        add "grope_front_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder

### ADMIRING TITS ###
screen genie_and_tits_01(): #Genie sitting, looking ar naked tits. Hermione stands right in front of him. (Behind the desk even).
    tag favor
    add "images/rooms/main_room/admire_tits_00.png" xpos -60 ypos 10 zoom 0.5
    zorder desk_zorder



### Admire Ass ###
screen hermione_chibi_ass(ani=None):
    tag favor
    if ani in ["admire_ass"]:
        if hermione_wear_top and hermione_wear_bottom:
            add "characters/hermione/chibis/fingering/01.png" xpos -60 ypos 10 zoom 0.5
        else: # Nude
            add "characters/hermione/chibis/fingering/02.png" xpos -60 ypos 10 zoom 0.5
        add "fingering_blinking" at Position(xpos=-60, ypos=10)
    zorder desk_zorder



### Handjob ###
screen hermione_chibi_hj(ani=None, xpos=230, ypos=0):
    tag favor
    zorder desk_zorder
    $ chibi_xpos = xpos
    $ chibi_ypos = ypos

    if ani in ["hj"]:
        add "handjob_ani" xpos chibi_xpos ypos chibi_ypos
    elif ani in ["hj_pause"]:
        add "characters/hermione/chibis/handjob/01.png" xpos chibi_xpos ypos chibi_ypos zoom 0.5
    elif ani in ["hj_kiss"]:
        add "kiss_ani" xpos chibi_xpos ypos chibi_ypos

    elif ani in ["hj_cumming_on"]:
        add "on_shirt_cum_ani" xpos chibi_xpos ypos chibi_ypos
    elif ani in ["hj_cumming_on_pause"]:
        add "characters/hermione/chibis/handjob/sperm_on_21.png" xpos chibi_xpos ypos chibi_ypos zoom 0.5
    elif ani in ["hj_cumming_in"]:
        add "undershirt_cum_ani" xpos chibi_xpos ypos chibi_ypos
    elif ani in ["hj_cumming_in_pause"]:
        add "characters/hermione/chibis/handjob/sperm_under_12.png" xpos chibi_xpos ypos chibi_ypos zoom 0.5



### Titjob ###
screen hermione_chibi_tj(ani=None, xpos=450, ypos=200):
    tag favor
    zorder desk_zorder
    $ chibi_xpos = xpos
    $ chibi_ypos = ypos

    if ani in ["tj"]:
        add "titjob_ani" xpos chibi_xpos ypos chibi_ypos
    elif ani in ["tj_pause"]:
        add "characters/hermione/chibis/titjob/tj_sex_01.png" xpos chibi_xpos ypos chibi_ypos zoom 0.5

    # Number offset so Hermione's Chibi doesn't move.
    elif ani in ["tj_idle"]:
        add "characters/hermione/chibis/titjob/tj_cum_chest_01.png" xpos chibi_xpos-15 ypos chibi_ypos+16 zoom 0.5
    elif ani in ["tj_cumming_on"]:
        add "titjob_chest_ani" xpos chibi_xpos-15 ypos chibi_ypos+16
    elif ani in ["tj_cumming_on_pause"]:
        add "characters/hermione/chibis/titjob/tj_cum_chest_25.png" xpos chibi_xpos-15 ypos chibi_ypos+16 zoom 0.5

    elif ani in ["tj_bj_pause"]:
        add "characters/hermione/chibis/titjob/tj_cum_mouth_01.png" xpos chibi_xpos+27 ypos chibi_ypos+16 zoom 0.5
    elif ani in ["tj_cumming_in"]:
        add "titjob_mouth_ani" xpos chibi_xpos+27 ypos chibi_ypos+16
    elif ani in ["tj_cumming_in_pause"]:
        add "characters/hermione/chibis/titjob/tj_cum_mouth_09.png" xpos chibi_xpos+27 ypos chibi_ypos+16 zoom 0.5



### Blowjob ###
screen hermione_chibi_bj(ani=None): # x-10 y10
    tag favor
    zorder desk_zorder
    if ani in ["bj"]:
        add "blowjob_ani" at Position(xpos=-10, ypos=10)
    elif ani in ["bj_pause"]:
        add "hand_ani" at Position(xpos=-10, ypos=10)

    elif ani in ["bj_cumming_in"]:
        add "cum_in_mouth_ani" at Position(xpos=-10, ypos=10)
    elif ani in ["bj_cumming_out"]:
        add "cum_on_face_ani" at Position(xpos=-10, ypos=10)
    elif ani in ["bj_cumming_out_blink"]:
        add "cum_on_face_blink_ani" at Position(xpos=-10, ypos=10)

    else:
        add "blowjob_ani" at Position(xpos=-10, ypos=10)

### Sex ###
screen hermione_chibi_sex(ani=None): #x-70 y10
    tag favor
    if ani == "sex_slow":
        add "sex_slow_ani" at Position(xpos=-70, ypos=10)
    elif ani == "sex_fast":
        add "sex_fast_ani" at Position(xpos=-70, ypos=10)
    elif ani == "sex_pause":
        add "pause_sex" at Position(xpos=-70, ypos=10)

    elif ani in ["sex_cumming_out","sex_cumming_out_blink"]:
        if ani == "sex_cumming_out":
            add "sex_cum_out_ani" at Position(xpos=-70, ypos=10)
        else:
            add "sex_cum_out_blink_ani" at Position(xpos=-70, ypos=10)

    elif ani in ["sex_creampie"]:
        add "sex_cum_in_ani" at Position(xpos=-70, ypos=10)
    elif ani in ["sex_creampie_blink"]:
        add "sex_cum_in_blink_ani" xpos -70 ypos 10 zoom 0.5

    else:
        add "sex_ani" at Position(xpos=-70, ypos=10)

    zorder desk_zorder

screen ch_hotdog():
    tag favor
    add "ch_hem hotdog" xpos -70 ypos 10 zoom 0.5
    zorder 0

screen genie_and_hermione(): #Genie sitting, Hermione stands right in front of him (behind the desk even).
    tag favor
    add "images/rooms/main_room/genie_and_hermione_01.png" xpos -84 ypos 10 zoom 0.5

screen groping_05():
    tag favor
    add "groping_05" at Position(xpos = -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen groping_05b():
    tag favor
    add "groping_05b" at Position(xpos = -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_05():
    tag favor
    add "characters/hermione/chibis/grope_ass/back_d_05.png" xpos -84 ypos 10 zoom 0.5
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_05_desk():
    tag favor
    add "characters/hermione/chibis/fingering/02.png" xpos -84 ypos 10 zoom 0.5

screen no_groping_06(): #Facing Genie.
    tag favor
    add "characters/hermione/chibis/grope_ass/front_e_05.png" xpos -84 ypos 10 zoom 0.5
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen groping_06():
    tag favor
    add "groping_06" at Position(xpos = -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen groping_06b():
    tag favor
    add "groping_06b" at Position(xpos = -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_laying_01():
    tag favor
    add "characters/hermione/chibis/fingering/01.png" xpos -84 ypos 10 zoom 0.5

screen no_groping_laying_02():
    tag favor
    add "characters/hermione/chibis/fingering/b_01.png" xpos -84 ypos 10 zoom 0.5

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "fingering_naked_slow" at Position(xpos = -84, ypos = 10)
    else:
        add "fingering_naked" at Position(xpos = -84, ypos = 10)
    add "fingering_blinking" at Position(xpos = -84, ypos = 10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "sex_naked_slow" at Position(xpos = -84, ypos = 10)
    elif speed == "normal":
        add "sex_naked" at Position(xpos = -84, ypos = 10)
    elif speed == "fast":
        add "sex_naked_fast" at Position(xpos = -84, ypos = 10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "sex_cum_out_naked" at Position(xpos = -84, ypos = 10)
