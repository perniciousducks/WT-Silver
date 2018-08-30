

label cho_menu:
    call play_sound("door")
    call cho_main("Hello, [cho_genie_name].","smile","base","base","mid",xpos="base",ypos="base")

    $ cho_busy = True

    label cho_requests:

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

        "-Dismiss Her-":
            call cho_main("Good bye, [cho_genie_name].","smile","base","base","R")

            call play_sound("door")

            $ cho_busy = True

            jump main_room
