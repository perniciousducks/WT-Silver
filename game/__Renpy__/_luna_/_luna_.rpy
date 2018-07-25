#LUNA PLOT
#Turned into a bitchy Slytherin by the sorting hat. Willing to do anything for money/fame/status. Incredibly vain

#Don't forget to incorporate the quibbler

#LUNA MECHANICS




label luna_day_flags:
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
    $ luna_busy = False
return

label luna_night_flags:
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_busy = False
return


label luna_door:
    call luna_reset 
    $ renpy.play('sounds/door.mp3')
    $ luna_chibi("stand")
    if luna_dom >= luna_sub:
        if luna_dom >= 4:
            call luna_main("[l_genie_name]...", "doubtful", "right", "angry", "upset") 
        else:
            call luna_main("[l_genie_name]...", "mad", "right", "mad", "angry") 
    else:
        call luna_main("[l_genie_name]...", "default", "default", "sad", "upset") 

label luna_door_menu:
    menu:
        "-Chit Chat-":
            call luna_chitchat 
            jump luna_door_menu
        "-favours-":
            if gold <= 100:
                m "Hmmm, I probably need a bit more gold if I want to ask for any favours..."
                jump luna_door_menu
            jump luna_favour_menu
        "-Never mind-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Talk to me-" if not luna_reverted:
            jump luna_favour_1
        "-Sit on my lap-" if luna_corruption >= 3 and not luna_reverted:
            jump luna_favour_2
        "-Strip for me-" if luna_corruption >= 5 and not luna_reverted:
            jump luna_favour_3
        "-Touch me-" if luna_corruption >= 9 and not luna_reverted:
            if luna_corruption == 9:
                jump luna_reversion_event
            jump luna_favour_4
        "-Touch me with Hermione-" if luna_corruption >= 11 and not luna_reverted:
            jump luna_favour_5
        "-Suck it-" if luna_corruption >= 14 and not luna_reverted:
            jump luna_favour_6
        "-Sex-" if luna_corruption >= 17 and not luna_reverted:
            jump luna_favour_7
        "-Never mind-":
            jump luna_door_menu

label luna_summon:
    $ changeLuna(8, 2, 3, 3)
return

label luna_away:
    call luna_reset 
    $ luna_busy = True
    $ renpy.play('sounds/door2.mp3')
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    show screen genie
    hide screen luna
    hide screen luna_chibi
    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with d3
    jump day_main_menu

label luna_reset:
    $ luna_flip = 1
    $ luna_l_arm = 1
    $ luna_r_arm = 1
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_chibi_image = "characters/luna/chibis/luna_stand.png" 
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250
    $ luna_tears = 0
    $ luna_wear_skirt = True
    $ luna_wear_top = True
    $ luna_wear_cum = False 
    $ luna_wear_cum_under = False 
    return

label luna_no_money:
    call luna_main("You expect me to do it for free?", "mad", "right", "mad", "angry") 
    call luna_main("Hmph!", "mad", "right", "mad", "angry") 
    jump luna_away

###CHIBIS###------------------------------------------------------




###PLOT###--------------------------------------------------------
#After the sex favour, Luna will either return to normal if you choose the sub route or she will become a slytherin dom if you go the dom route
#All the private favours will then have a 4th level unlocked, tailored to either the sub or dom option
