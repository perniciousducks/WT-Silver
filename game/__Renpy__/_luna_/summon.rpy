

label summon_luna:

    call play_sound("door")

    call lun_chibi("stand","mid","base")

    if luna_reverted:
        call lun_main("Hello, [lun_genie_name]!","normal","wink","base","mid",xpos="base",ypos="base")
    elif lun_dom >= lun_sub:
        if lun_dom >= 4:
            call lun_main("[lun_genie_name]...","normal","suspicious","angry","R",xpos="base",ypos="base")
        else:
            call lun_main("[lun_genie_name]...","upset","mad","mad","R",xpos="base",ypos="base")
    else:
        call lun_main("[lun_genie_name]...","normal","base","sad","mid",xpos="base",ypos="base")

    label luna_requests:

    $ hide_transitions = False
    $ luna_busy = True
    $ gave_luna_gift = True #Remove when adding gift texts!

    menu:

        # Talk
        #"-Chit Chat-":
        #    call luna_chitchat
        #    jump luna_requests


        # Personal Favors
        "-favours-":
            if gold <= 0 and not luna_reverted:
                m "I don't have any gold..."
                jump luna_requests
            jump luna_favour_menu


        # Wardrobe
        "-Wardrobe-": # if luna_wardrobe_unlocked:
            $ active_girl = "luna"
            $ ll_quirky_muggle_ITEM.unlocked = True #Temporary unlock. Will be a random clothing event eventually.

            call load_luna_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            call lun_chibi("stand","wardrobe","base")

            $ hide_transitions = True
            call lun_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        #"{color=#858585}-Hidden-{/color}" if not luna_wardrobe_unlocked:
        #    call nar(">You haven't unlocked this feature yet.")
        #    jump luna_requests


        # Gifts
        "-Gifts-" if not gave_luna_gift:
            $ current_category = None
            jump luna_gift_menu

        "{color=#858585}-Gifts-{/color}" if gave_luna_gift:
            "Not yet added. WIP!"
            #m "I already gave her a gift today. Don't want to spoil her too much..."
            jump luna_requests


        # Dismiss
        "-Never mind-":

            if luna_reverted:
                call lun_main("Oh... alright then... Bye, [lun_genie_name]!","normal","wink","sad","down",xpos="base",ypos="base")

            call play_sound("door")

            $ luna_busy = True

            jump main_room



label luna_favour_menu:
    menu:
        "-Talk to me-" if not luna_reverted:
            jump luna_favour_1
        "-Sit on my lap-" if lun_corruption >= 3 and not luna_reverted:
            jump luna_favour_2
        "-Strip for me-" if lun_corruption >= 5 and not luna_reverted:
            jump luna_favour_3
        "-Touch me-" if lun_corruption >= 9 and not luna_reverted:
            if lun_corruption == 9:
                jump luna_reversion_event
            jump luna_favour_4
        "-Touch me with Hermione-" if lun_corruption >= 11 and not luna_reverted:
            jump luna_favour_5
        "-Suck it-" if lun_corruption >= 14 and not luna_reverted:
            jump luna_favour_6
        "-Sex-" if lun_corruption >= 17 and not luna_reverted:
            jump luna_favour_7

        #Luna reverted.
        #"-Talk about Wrackspurts-": #Luna would describe the affects Wrackspurts (cum) had on her, their smell, taste,...
        #"-Wrackspurt infection-": #Luna will help you with your wrackspurts problem, by giving you a handjob.
        "-Sucking out Wrackspurts-" if lun_corruption >= 3 and luna_reverted:
            jump luna_blowjob_under_desk #Repeat of event.

        "-Never mind-":
            jump luna_requests
