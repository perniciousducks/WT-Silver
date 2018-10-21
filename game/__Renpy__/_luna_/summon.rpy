

label summon_luna:
    call luna_reset
    $ renpy.play('sounds/door.mp3')
    call lun_chibi("stand","mid","base")

    if luna_dom >= luna_sub:
        if luna_dom >= 4:
            call lun_main("[l_genie_name]...","normal","suspicious","angry","R",xpos="base",ypos="base")
        else:
            call lun_main("[l_genie_name]...","upset","mad","mad","R",xpos="base",ypos="base")
    else:
        call lun_main("[l_genie_name]...","normal","base","sad","mid",xpos="base",ypos="base")

    label luna_requests:
    menu:
        "-Chit Chat-":
            call luna_chitchat
            jump luna_requests

        "-favours-":
            if gold <= 0 and not luna_reverted:
                m "I don't have any gold..."
                jump luna_requests
            jump luna_favour_menu

        #"{color=#858585}-Hidden-{/color}" if not luna_wardrobe_unlocked:
        #    call nar(">You haven't unlocked this feature yet.")
        #    jump luna_requests
        "-Wardrobe-": # if luna_wardrobe_unlocked:
            $ active_girl = "luna"

            call load_luna_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            call lun_chibi("stand","wardrobe","base")

            $ wardrobe_active = True
            call lun_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        "-Never mind-":

            #ADD Luna says goodbye.

            call play_sound("door")

            $ luna_busy = True

            jump main_room



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

        #Luna reverted.
        #"-Talk about Wrackspurts-": #Luna would describe the affects Wrackspurts (cum) had on her, their smell, taste,...
        #"-Wrackspurt infection-": #Luna will help you with your wrackspurts problem, by giving you a handjob.
        "-Sucking out Wrackspurts-" if luna_corruption >= 3 and luna_reverted:
            jump luna_blowjob_under_desk #Repeat of event.

        "-Never mind-":
            jump luna_requests
