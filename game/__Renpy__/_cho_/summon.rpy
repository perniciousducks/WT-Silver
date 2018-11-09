

label cho_menu:

    call play_sound("door")

    #ADD Cho chibi here.
    call cho_random_clothing

    label cho_requests:

    $ menu_x = 0.1
    $ menu_y = 0.5

    $ hide_transitions = False
    $ cho_busy = True

    menu:
        #"-Talk-":
        #"-Training-": #For Quidditch events.
        "-Personal Favours-":
            if cho_mad <= 0:
                label cho_favor_menu:
                menu:
                    "-Admire her body-":
                        jump cho_favor_1
                    #"-Play with her butt-": #I don't think these event have the right posig yet or are missing CGs? They also cause crashes.
                    #    jump cho_favor_2
                    #"-Make her suck my cock-":
                        jump cho_favor_3
                    #"{color=#858585}-A vague idea-{/color}" if imagination <= 3:
                    #    call vague_idea
                    #    jump cho_favor_menu
                    "-Nevermind-":
                        jump cho_requests
            else:
                call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like it today...","upset","base","sad","mid")
                jump cho_requests

        #"-Public Favours-":
        #    "To be done."
        #    jump cho_menu

        "{color=#858585}-Hidden-{/color}" if not cho_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump cho_requests
        "-Wardrobe-" if cho_wardrobe_unlocked:
            $ active_girl = "cho"

            call load_cho_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ hide_transitions = True
            call cho_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        "-Dismiss Her-":
            call cho_main("Good bye, [cho_genie_name].","smile","base","base","R")

            call play_sound("door")

            $ cho_busy = True

            jump main_room
