

label summon_cho:
    call play_sound("door")
    call cho_chibi("stand","mid","base")
    with d3

    $ active_girl = "cho"
    $ cho_busy = True
    call cho_random_clothing

    label cho_requests:

    call cho_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Main Matches
        "Start Hufflepuff Match" if (huffl_matches_won == 2 and cho_tier == 1):
            $ lock_cho_training = True # Temporarily, Until next events get added.
            $ cho_tier = 2
            $ main_match_1_stage = "start"
            $ cc_event_pause  += 1  # Event starts on the next day.
            $ cc_summon_pause += 1 # Can't be summoned until next event.
            jump start_hufflepuff_match


        # Talk
        "-Talk-" if cho_training_unlocked:
            if not cho_chatted:
                if cho_mood <= 3:
                    $ cho_chatted = True
                    #call cho_chit_chat
                    jump cho_talk
                else:
                    call cho_main("I have nothing to say to you, [cho_genie_name]...",face="annoyed")
                    jump cho_requests
            else:
                jump cho_talk


        # Quidditch Training
        "-Training-" if not lock_cho_training:
            if cho_mood != 0:
                m "Ready to get back to training?"
                if cho_mood >= 5:
                    call cho_main("No.{w} And I don't want to hear of it right now, Sir.",face="angry")
                else:
                    call cho_main("I'm sorry, [cho_genie_name]. But I don't feel like training today.","soft","base","sad","down")
                call nar(">Cho is still upset with you.")
                jump cho_requests
            jump cho_training_menu


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
            if cho_mood != 0:
                call cho_main("Good bye, [cho_genie_name].",face="annoyed")
            else:
                call cho_main("Good bye, [cho_genie_name].",face="happy")

            jump end_cho_event



# Cho Favor Menu
label cho_favor_menu:
    call update_cho_favors
    python:
        menu_choices = []
        for i in cc_favor_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            elif i.start_tier > cho_tier:
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

label update_cho_favors:
    python:
        for i in cc_favor_list:
            if i.tier != cho_tier and i.max_tiers >= cho_tier:
                i.tier = cho_tier

    return

# Cho Requests Menu
label cho_requests_menu:
    call update_cho_requests
    python:
        menu_choices = []
        for i in cc_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            elif i.start_tier > cho_tier:
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

label update_cho_requests:
    # Set event tier to current Cho tier if they are different
    python:
        for i in cc_requests_list:
            if i.tier != cho_tier and i.max_tiers >= cho_tier:
                i.tier = cho_tier

    return


label favor_not_ready:
    call nar("You can't do this favour just yet.")
    return

label not_available:
    $ ver = config.version[:4]+"."+config.version[4:6] if len(config.version) >=5 else config.version
    call nar("This feature is currently not available in v[ver], and will be added in a later patch.")
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
                "\"Professor\"":
                    $ cho_genie_name = "Professor"
                "\"Coach\"":
                    $ cho_genie_name = "Coach"
                "\"Old Man\"":
                    $ cho_genie_name = "Old Man"
                "\"Daddy\"":
                    $ cho_genie_name = "Daddy"
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ cho_genie_name = "Sir"
                    $ cho_genie_name = temp_name
                    call cho_main("If I really have to...",face="annoyed")
                    jump cho_talk
                "\"Never mind\"":
                    jump cho_talk

            call cho_main("Of course, [cho_genie_name]...",face="neutral")
            jump cho_talk

        "\"From now on I will refer to you as\"":
            menu:
                "\"Miss Chang\"":
                    $ cho_name = "Miss Chang"
                "\"Princess\"":
                    $ cho_name = "Princess"
                "\"Boy\"":
                    $ cho_name = "Boy"
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ temp_name = "Miss Chang"
                    $ cho_name = temp_name
                    call cho_main("If you say so, [cho_genie_name].",face="neutral")
                    jump cho_talk
                "\"Never mind\"":
                    jump cho_talk

            call cho_main("Very well,...",face="neutral")
            jump cho_talk

        "\"Never mind\"":
            jump cho_requests
