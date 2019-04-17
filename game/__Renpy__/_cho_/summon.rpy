

label summon_cho:
    call play_sound("door")
    call cho_chibi("stand","mid","base")

    call cho_random_clothing

    $ active_girl = "cho"
    $ cho_busy = True

    label cho_requests:
    call cho_main(xpos="base",ypos="base")

    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-" if cho_training_unlocked:
            if not cho_chatted:
                if cho_mood <= 3:
                    $ cho_chatted = True
                    #call cho_chit_chat
                    jump cho_talk
                else:
                    cho "I have nothing to say to you, [cho_genie_name]..."
                    jump cho_requests
            else:
                jump cho_talk


        # Quidditch Training
        "-Training-" if not lock_cho_training:
            if cho_mood != 0:
                m "Ready to get back to training?"
                if cho_mood >= 5:
                    cho "No.{w} And I don't want to hear of it right now, Sir."
                else:
                    cho "I don't think I'm ready yet, Sir."
                m "Fair enough..."
                call nar(">Cho is still mad at you.")
                jump cho_requests
            jump cho_training_menu


        # Practice Matches
        "-Practice Match-" if daytime and huffl_matches_won < 2 and cho_mood == 0 and not lock_cho_practice:
            jump start_training_match

        "{color=#858585}-Practice Match-{/color}" if (not daytime or cho_mood != 0 or lock_cho_practice) and not cho_content_complete:
            if not daytime:
                call nar(">You can only do that during the day.")
            elif cho_mood != 0:
                cho "I'm sorry, [cho_genie_name]. But I don't feel like playing today."
            else:
                call nar(">You can't do that right now.")
            jump cho_requests


        # Main Matches
        "-Start Hufflepuff Match-" if (huffl_matches_won == 2 and main_matches_won == 0):
            $ lock_cho_training = True # Temporarily, Until next events get added.
            $ main_matches_won = 1
            $ main_match_1_stage = "start"
            $ days_without_an_event = 0 # Event starts on the next day.
            jump start_hufflepuff_match


        # Favours
        "-Personal Favours-" if cho_favors_unlocked:
            if cho_mood <= 0:
                jump cho_favor_menu
            else:
                call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like it today...","upset","base","sad","mid")
                jump cho_requests

        "{color=#858585}-Personal Favours-{/color}" if not cho_favors_unlocked:
            m "I need to help her with her Quidditch training, before I can ask for something like this."
            jump cho_requests


        # Requests
        "-Public Requests-" if daytime and cho_requests_unlocked:
            if cho_mood <= 0:
                jump cho_requests_menu
            else:
                call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like it today...","upset","base","sad","mid")
                jump cho_requests

        "{color=#858585}-Public Requests-{/color}" if not daytime and cho_requests_unlocked:
            call nar(">Public requests are available during the daytime only.")
            jump cho_requests

        "{color=#858585}-Hidden-{/color}" if not cho_requests_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump cho_requests


        # Wardrobe
        "-Wardrobe-" if cho_wardrobe_unlocked:
            call cho_main(xpos="wardrobe",ypos="base", face="neutral")
            call expression 't_wardrobe' pass (return_label="cho_requests", char_label="cho_main")

        "{color=#858585}-Hidden-{/color}" if not cho_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump cho_requests


        # Gifts
        "-Gifts-" if not gave_cho_gift:
            $ current_category = None
            $ current_page = 0
            jump cho_gift_menu

        "{color=#858585}-Gifts-{/color}" if gave_cho_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump cho_requests


        # Dismiss
        "-Dismiss Her-":
            call cho_main("Good bye, [cho_genie_name].","smile","base","base","R")

            jump end_cho_event



# Cho Favor Menu
label cho_favor_menu:
    call update_cho_heart_color
    python:
        menu_choices = []
        for i in cc_favor_list:
            if i in [cc_pf_blowjob_OBJ, cc_pf_sex_OBJ]: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            elif i.tier > main_matches_won:
                menu_choices.append(("{color=#858585}-Not ready-{/color}","vague"))
            else:
                menu_choices.append((i.getMenuText(),i.start_label))
        menu_choices.append(("-Never mind-", "nvm"))
        result = custom_menu(menu_choices)
    if result == "nvm":
        jump cho_requests
    elif result == "vague":
        call favor_not_ready
        jump cho_requests
    elif result == "na":
        call not_available
        jump cho_requests
    else:
        $ renpy.jump(result)


# Cho Requests Menu
label cho_requests_menu:
    python:
        menu_choices = []
        for i in cc_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            elif i.tier > main_matches_won:
                menu_choices.append(("{color=#858585}-Not ready-{/color}","vague"))
            else:
                menu_choices.append((i.getMenuText(),i.start_label))
        menu_choices.append(("-Never mind-", "nvm"))
        result = custom_menu(menu_choices)
    if result == "nvm":
        jump cho_requests
    elif result == "vague":
        call favor_not_ready
        jump cho_requests
    elif result == "na":
        call not_available
        jump cho_requests
    else:
        $ renpy.jump(result)

label update_cho_heart_color:
    if main_matches_won == 0:
        $ heart_color = "yellow"
    elif main_matches_won == 1:
        $ heart_color = "green"
    elif main_matches_won == 2:
        $ heart_color = "red"
    else:
        $ heart_color = "blue"

    $ cc_pf_talking_OBJ.heart_color = heart_color
    $ cc_pf_groping_OBJ.heart_color = heart_color

    return

label favor_not_ready:
    call nar("You can't do this favour just yet.")
    return

label not_available:
    call nar("This feature is currently not availabel in v[config.version], and will be added in a later patch.")
    return


# Cho Talk
label cho_talk:
    menu:
        #"-Working-":

        "-Quidditch Commentator-" if quidditch_commentator == "talk_with_cho":
            $ lock_cho_practice = False
            $ quidditch_commentator = "hermione"
            jump quidditch_commentator_event_3

        # Naming
        "\"Address me only as\"":
            menu:
                "\"Coach\"":
                    $ cho_genie_name = "Coach"
                "\"Sergeant\"":
                    $ cho_genie_name = "Sergeant"
                "\"Captain\"":
                    $ cho_genie_name = "Captain"
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ cho_genie_name = "Sir"
                    $ cho_genie_name = temp_name
                    cho "Do I really have to?"

                "\"Never mind\"":
                    pass

            jump cho_talk

        "\"From now on I will refer to you as\"":
            menu:
                "\"Miss Chang\"":
                    $ temp_name = "Miss Chang"
                    jump cho_requests
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ temp_name = "Miss Chang"
                    $ cho_name = temp_name
                    jump cho_requests
                "\"Never mind\"":
                    pass

            jump cho_talk

        "\"Never mind\"":
            jump cho_requests
