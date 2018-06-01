

### HERMIONE CHIBI SCREENS ###
    

### UNIVERSAL SCREEN ###
screen h_c_u: 
    tag hermione_chibi
    add h_c_u_pic at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)




screen hermione_blank_main:
    tag hermione_main
    zorder hermione_SC.zorder
screen hermione_blank_head:
    tag hermione_head
    zorder 8
screen hermione_blank_chibi:
    tag hermione_chibi
    zorder hermione_SC.chibi.zorder
    
    
screen hermione_walk:
    tag hermione_chibi
    add hermione_chibi_walk at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_SC.chibi.zorder
screen hermione_walk_f:  #Hermione walking animation. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_walk_f at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_SC.chibi.zorder

screen hermione_blink:   #Hermione stands still and blinks.
    tag hermione_chibi
    add hermione_chibi_blink at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
screen hermione_blink_f: #Hermione stands still and blinks facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_blink_f at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder

screen hermione_stand:   #Hermione stands still
    tag hermione_chibi
    add hermione_chibi_stand at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
screen hermione_stand_f: #Hermione stands still facing right. (Leaving tower).
    tag hermione_chibi
    add im.Flip(hermione_chibi_stand, horizontal=True) at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder

screen hermione_stand_nude: #Hermione stands naked
    tag hermione_chibi
    add hermione_chibi_stand_nude at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
screen hermione_stand_f_nude: #Hermione stands still facing right. (Leaving tower).
    tag hermione_chibi
    add im.Flip(hermione_chibi_stand_nude, horizontal=True) at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder

screen hermione_01: #Hermione stands still.
    tag hermione_chibi
    add hermione_chibi_stand at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_chibi_zorder
screen hermione_01_f: #Hermione stands still. (MIRRORED)
    tag hermione_chibi
    add im.Flip(hermione_chibi_stand, horizontal=True) at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_chibi_zorder

screen hermione_02: #Hermione stands still and blinks.
    tag hermione_chibi
    add hermione_chibi_blink at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_chibi_zorder

screen hermione_walk_01:
    tag hermione_chibi
    add hermione_chibi_walk at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
screen hermione_walk_01_f: #Hermione walking animation. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_walk_f at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
    
screen hermione_run: #Hermione running. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_run at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
screen hermione_run_f: #Hermione running. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_run_f at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
    
screen hermione_fly: #Hermione running. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_fly at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
screen hermione_fly_f: #Hermione running. facing right. (Leaving tower).
    tag hermione_chibi
    add hermione_chibi_fly_f at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder

screen hermione_chibi_robe: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione_chibi
    if not wear_shirts:
        add "ch_hem walk_robe_n" at custom_walk_02(walk_xpos, walk_xpos2)
    else:
        add "ch_hem walk_robe" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
screen hermione_chibi_robe_f: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione_chibi
    if not wear_shirts:
        add "ch_hem walk_robe_n_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    else:
        add "ch_hem walk_robe_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder hermione_chibi_zorder
    
screen hermione_02_b: #Hermione stands still wearing a robe. #Not in use.
    tag hermione_chibi
    add "characters/hermione/chibis/walk/h_walk_robe_01.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
  


screen her_wand_slow:  # Hermione rubs wand slowly
    add "rub_wand_slow_ani" 

screen hermione_02_w: #Hermione stands still wearing a robe.
    tag hermione
    add "images/animation/h_Wand_01s.png" at Position(xpos=hermione_SC.chibi.xpos+140, ypos=hermione_SC.chibi.ypos)
screen hermione_02_wSlow: #Hermione rubs wand between her legs slowly.
    tag hermione
    add "rub_wand_slow_ani" at Position(xpos=hermione_SC.chibi.xpos+140, ypos=hermione_SC.chibi.ypos)
screen hermione_02_wFast: #Hermione rubs wand between her legs quickly.
    tag hermione
    add "rub_wand_fast_ani" at Position(xpos=hermione_SC.chibi.xpos+140, ypos=hermione_SC.chibi.ypos)
screen hermione_02_wf1: #Hermione finishes rubbing the wand - eyes closed.
    tag hermione
    add "images/animation/h_Wand_01f.png" at Position(xpos=hermione_SC.chibi.xpos+140, ypos=hermione_SC.chibi.ypos)
screen hermione_02_wf2: #Hermione finishes rubbing the wand - eyes opened. 
    tag hermione
    add "images/animation/h_Wand_02s.png" at Position(xpos=hermione_SC.chibi.xpos+140, ypos=hermione_SC.chibi.ypos)



### HERMIONE CHIBI ACTIONS ###

#Lift top.
screen hermione_chibi_lift_top:
    tag hermione_chibi
    add "characters/hermione/chibis/lift_top/tits_00.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
    
#Lift skirt.
screen hermione_chibi_lift_skirt:
    tag hermione_chibi
    if hermione_wear_panties:
        if hg_pf_NicePanties_OBJ.points <= 1:
            add "characters/hermione/chibis/lift_skirt/panties_00.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
        else:
            add "characters/hermione/chibis/lift_skirt/panties_01.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    else:
        add "characters/hermione/chibis/lift_skirt/panties_02.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
    
#Drink potion.
screen ch_potion:
    tag hermione_chibi
    add "ch_hem potion" at Position(xpos=hermione_SC.chibi.xpos-30, ypos=hermione_SC.chibi.ypos)
    zorder hermione_SC.chibi.zorder
 


### HERMIONE CHIBI FAVOUR SCREENS (with Genie or Snape,...) ###

### GROPING ###
screen groping_01: #Facing Genie.
    tag favor
    add "groping_01" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    
screen groping_02: #Facing Genie.
    tag favor
    add "groping_02" at Position(xpos=-60, ypos=10)
    add "groping_02_blinking" at Position(xpos=-60, ypos=10)
    
screen no_groping_01: #Facing Genie.
    tag favor
    add "images/animation/grope_05.png" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    
screen no_groping_02: #Facing Genie.
    tag favor
    add "images/animation/grope_b_05.png" at Position(xpos=-60, ypos=10)
    add "groping_02_blinking" at Position(xpos=-60, ypos=10)
    

### MOLESTING TITS FULLY CLOTHED ###
screen groping_03: #Facing Genie.
    tag favor
    add "groping_03_ani" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    
### MOLESTING NAKED TITS ###
screen groping_naked_tits: 
    tag favor
    add "groping_naked_tits_ani" at Position(xpos=-60, ypos=10)
    add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    zorder 1 #Otherwise chair is on top.
    
### JERKING OFF ###
screen jerking_off_01: 
    tag favor
    add "jerking_off_ani" at Position(xpos=-60, ypos=10)
    if not no_blinking: #When True - blinking animation is not displayed. 
        add "groping_01_blinking" at Position(xpos=-60, ypos=10)
    zorder 1 #Otherwise chair is on top.

### SPERM ###
screen jerking_off_cum: 
    add "jerking_off_cum_ani" at Position(xpos=-60, ypos=10)
    #add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 2 #Otherwise there is a bug with blinking.

### ADMIRING TITS ###
screen genie_and_tits_01: #Genie sitting, looking ar naked tits. Hermione stands right in front of him. (Behind the desk even).
    tag favor
    add "images/main_room/admire_tits_00.png" at Position(xpos=-60, ypos=10)



### HERMIONE DANCING ###
screen hermione_chibi_dance:
    tag hermione_chibi
    if hermione_wear_top:
        if h_top == "uni_top_1" or h_top == "uni_top_6":
            add "clothed_dance_ani" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
        else:
            if hermione_wear_bottom:
                add "no_vest_dance_ani" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
            else:
                add "no_skirt_dance_ani" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)

    else:
        if hermione_wear_bottom:
            add "no_shirt_dance_ani" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
        else: #Nude
            add "no_shirt_no_skirt_dance_ani" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
            

screen clothed_dance: #Hermione stands still.
    tag hermione_chibi
    add "clothed_dance_ani" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)
screen clothed_dance_pause: #Hermione stands still.
    tag hermione_chibi
    add "ch_hem blink_a" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)

### NO VEST ###
screen no_vest_dance: #Hermione stands still.
    tag hermione_chibi
    add "no_vest_dance_ani" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)
    
### NO SHIRT ###
screen no_shirt_dance: #Hermione stands still.
    tag hermione_chibi
    add "no_shirt_dance_ani" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)

### NO BOTTOM/SKIRT ###
screen no_skirt_dance: #Hermione stands still.
    tag hermione_chibi
    add "no_skirt_dance_ani" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)
   
### NAKED DANCE ###
screen no_shirt_no_skirt_dance: #Hermione stands still.
    tag hermione_chibi
    add "no_shirt_no_skirt_dance_ani" at Position(xpos=her_chibi_dance_xpos, ypos=her_chibi_dance_ypos)
    
### SIT NAKED ###
screen hermione_chibi_sit_naked_A:
    tag hermione_chibi
    add "characters/hermione/chibis/sitting/sit_naked_blink.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    
screen hermione_chibi_sit_naked_B:
    tag hermione_chibi
    add "characters/hermione/chibis/sitting/sit_naked.png" at Position(xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos)
    



label update_chibi_uniform:

    #Naked
    if not hermione_wear_top and not hermione_wear_bottom and not hermione_wear_robe:
        $ hermione_chibi_blink    = "ch_hem blink_n"
        $ hermione_chibi_blink_f  = "ch_hem blink_n_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_n_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_n"
        $ hermione_chibi_walk_f   = "ch_hem walk_n_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"
        
    #Robe
    elif hermione_wear_robe and hermione_wear_top:
        $ hermione_chibi_blink    = "ch_hem blink_robe_blink"
        $ hermione_chibi_blink_f  = "ch_hem blink_robe_blink_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_robe_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_robe"
        $ hermione_chibi_walk_f   = "ch_hem walk_robe_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_robe and not hermione_wear_top:
        $ hermione_chibi_blink    = "ch_hem blink_robe_n"
        $ hermione_chibi_blink_f  = "ch_hem blink_robe_n_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_robe_n_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_robe_n"
        $ hermione_chibi_walk_f   = "ch_hem walk_robe_n_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    #Uniform
    elif hermione_wear_top and h_top == "uni_top_1":# shirt_00
        $ hermione_chibi_blink    = "ch_hem blink_a"
        $ hermione_chibi_blink_f  = "ch_hem blink_a_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_a_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_a"
        $ hermione_chibi_walk_f   = "ch_hem walk_a_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_top and h_top == "uni_top_2":# shirt_01
        $ hermione_chibi_blink    = "ch_hem blink_d"
        $ hermione_chibi_blink_f  = "ch_hem blink_d_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_d_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_d"
        $ hermione_chibi_walk_f   = "ch_hem walk_d_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_top and h_top == "uni_top_3":# shirt_02
        $ hermione_chibi_blink    = "ch_hem blink_e"
        $ hermione_chibi_blink_f  = "ch_hem blink_e_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_e_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_e"
        $ hermione_chibi_walk_f   = "ch_hem walk_e_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_top and h_top == "uni_top_4":# shirt_03
        $ hermione_chibi_blink    = "ch_hem blink_f"
        $ hermione_chibi_blink_f  = "ch_hem blink_f_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_f_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_f"
        $ hermione_chibi_walk_f   = "ch_hem walk_f_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_top and h_top == "uni_top_5":# shirt_04
        $ hermione_chibi_blink    = "ch_hem blink_g"
        $ hermione_chibi_blink_f  = "ch_hem blink_g_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_g_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_g"
        $ hermione_chibi_walk_f   = "ch_hem walk_g_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    elif hermione_wear_top and h_top == "uni_top_6":# shirt_05
        $ hermione_chibi_blink    = "ch_hem blink_h"
        $ hermione_chibi_blink_f  = "ch_hem blink_h_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_h_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_h"
        $ hermione_chibi_walk_f   = "ch_hem walk_h_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"
        
    else:# shirt_00
        $ hermione_chibi_blink    = "ch_hem blink_a"
        $ hermione_chibi_blink_f  = "ch_hem blink_a_flip"
        $ hermione_chibi_stand    = "characters/hermione/chibis/walk/h_walk_a_01.png"
        $ hermione_chibi_walk     = "ch_hem walk_a"
        $ hermione_chibi_walk_f   = "ch_hem walk_a_flip"
        $ hermione_chibi_run      = "ch_hem run_a"
        $ hermione_chibi_run_f    = "ch_hem run_a_flip"

    return




### HERMIONE MAIN CHIBI ###

label her_chibi(action = "", xpos=hermione_SC.chibi.xpos, ypos=hermione_SC.chibi.ypos, pic = "", flip=False):
    hide screen hermione_blink
    hide screen hermione_blink_f

    hide screen h_c_u
    hide screen hermione_chibi_dance

    hide screen hermione_chibi_lift_top
    hide screen hermione_chibi_lift_skirt 

    hide screen ch_potion  
    hide screen ch_hotdog
    
    $ hermione_SC.chibi.xpos = 540
    $ hermione_SC.chibi.ypos = 250

    if xpos != hermione_SC.chibi.xpos:
        if xpos == "mid":
            $ hermione_xpos_name = "mid"
            $ hermione_SC.chibi.xpos = 540
        elif xpos == "desk":
            $ hermione_xpos_name = "desk"
            $ hermione_SC.chibi.xpos = 440
        elif xpos == "on_desk":
            $ hermione_xpos_name = "desk"
            $ hermione_SC.chibi.xpos = 350
        elif xpos == "door":
            $ hermione_xpos_name = "door"
            $ hermione_SC.chibi.xpos = 750
        else:
            $ hermione_SC.chibi.xpos = xpos

    if ypos != hermione_SC.chibi.ypos:
        if ypos == "base" or ypos == "default":
            $ hermione_ypos_name = "base"
            $ hermione_SC.chibi.ypos = 250
        elif ypos == "on_desk":
            $ hermione_ypos_name = "base"
            $ hermione_SC.chibi.ypos = 180
        else:
            $ hermione_SC.chibi.ypos = ypos


    #Hermione Chibi Actions.
    if action == "lift_top":
        show screen hermione_chibi_lift_top

    elif action == "lift_skirt":
        show screen hermione_chibi_lift_skirt

    #Hermione Chibi Dance. #Strips automatically when removing clothes.
    elif action == "dance":
        show screen hermione_chibi_dance

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
            show screen hermione_blink_f
        else:
            show screen hermione_blink
        with d3


    return




### HERMIONE WALKING CHIBI ###


# label to be called to display the hermione chibi walking in a given direction
#
# @param pos1 starting position for the chibi, defaults to the value of walk_xpos
# @param pos2 ending position for the chibi, defaults to the value of walk_xpos2
# @param speed the the time it will take the chibi to move from pos1 to pos2 in seconds, defaults to the value of hermione_speed
# @param loiter boolean flag to detetermine weather to show the chibi when the animation ends, defaults to False
# @param redux_pause value to decrease the time to pause before hideing the animation early 




label her_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = hermione_speed, action = "", loiter = True, redux_pause = 0):
    hide screen bld1
    hide screen blktone
    call hide_characters
    with d3
    
    hide screen hermione_walk
    hide screen hermione_walk_f
    hide screen hermione_run
    hide screen hermione_run_f
    #hide screen hermione_fly #Screen and animation not yet added.
    #hide screen hermione_fly_f

    hide screen hermione_blink
    hide screen hermione_blink_f

    if pos1 == "mid":
        $ walk_xpos = 540
    elif pos1 == "desk":
        $ walk_xpos = 440
    elif pos1 == "door":
        $ walk_xpos = 750
    else:
        $ walk_xpos = pos1

    if pos2 == "mid":
        $ hermione_xpos_name = "mid"
        $ walk_xpos2 = 540
    elif pos2 == "desk":
        $ hermione_xpos_name = "desk"
        $ walk_xpos2 = 440
    elif pos2 == "door":
        $ hermione_xpos_name = "door"
        $ walk_xpos2 = 750
    elif pos2 == "leave":
        $ hermione_xpos_name = "door"
        $ walk_xpos2 = 750
        $ loiter = False
    else:
        $ hermione_xpos_name = "mid"
        $ walk_xpos2 = pos2

    $ hermione_SC.chibi.ypos = 250
    $ hermione_speed = speed #Speed of walking animation. (lower = faster)

    #Hermione walks
    if walk_xpos >= walk_xpos2: #right to left
        #if action == "fly":
            #show screen hermione_fly
        if action == "run":
            show screen hermione_run
        else:
            show screen hermione_walk
        $ tmp = speed - redux_pause
        pause tmp
        $ hermione_SC.chibi.xpos = walk_xpos2
        #hide screen hermione_fly
        hide screen hermione_run
        hide screen hermione_walk
        if loiter:
            show screen hermione_blink

    else: #left to right (flipped)
        #if action == "fly":
            #show screen hermione_fly_f
        if action == "run":
            show screen hermione_run_f
        else:
            show screen hermione_walk_f
        $ tmp = speed - redux_pause
        pause tmp
        $ hermione_SC.chibi.xpos = walk_xpos2
        #hide screen hermione_fly_f
        hide screen hermione_run_f
        hide screen hermione_walk_f
        if pos2 == "leave":
            call play_sound("door") #Sound of a door opening.
            with d3
            pause.5
        if loiter:
            show screen hermione_blink_f
        
    return
    




# label to be called to remove hermiones chibi from the screen
#
# @param dissolveTime how long to use the desolve transition for i.e.(2=d2, 3=d3)
label her_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen hermione_stand
        hide screen hermione_stand_f
        hide screen hermione_blink
        hide screen hermione_blink_f
        with Dissolve((dissolveTime/10))
    else:
        hide screen hermione_stand
        hide screen hermione_stand_f
        hide screen hermione_blink
        hide screen hermione_blink_f
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
    
    show screen u_h_animation
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
        hide screen u_h_animation
    #if:
    return
    
    
screen u_h_ani_scr:
    add u_h_animation at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
screen u_h_ani_scr_pause:
    add u_h_animation_paused at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
