

label summon_cho:
    pause.5
    call play_sound("knocking")    
    pause 1
    call play_sound("door")
    call cho_chibi("stand","mid","base")
    call ctc
    call cho_random_clothing
    
    $ active_girl = "cho"
    $ cho_busy = True
    
    label cho_requests:
    call cho_main(xpos="base",ypos="base")
    
    $ menu_x = 0.25
    $ menu_y = 0.5

    $ hide_transitions = False

    menu:
        #"-Talk-":


        # Quidditch
        "-Training-" if not lock_cho_training:
            jump cho_training_menu

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

        "-Start Hufflepuff Match-" if (huffl_matches_won == 2 and main_matches_won == 0):
            $ lock_cho_training = True # Temporarily, Until next events get added.
            $ main_matches_won = 1
            $ main_match_1_stage = "start"
            $ days_without_an_event = 0 # Event starts on the next day.
            jump start_hufflepuff_match


        # Favours
        "{color=#858585}-Personal Favours-{/color}" if not cho_training_unlocked:
            m "I need to help her with her Quidditch training, before I can ask for something like this."
            jump cho_requests

        "-Personal Favours-" if cho_training_unlocked:
            if cho_mood <= 0:
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


        # Wardrobe
        "{color=#858585}-Hidden-{/color}" if not cho_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump cho_requests
        "-Wardrobe-" if cho_wardrobe_unlocked:
            call cho_main(xpos="wardrobe",ypos="base", face="neutral")
            call expression 't_wardrobe' pass (return_label="cho_requests", char_label="cho_main")
        "-Gifts-" if not gave_cho_gift:
            $ current_category = None
            $ current_page = 0
            label cho_gift_menu:

            python:

                category_list = []
                category_list.append("ui_gifts")
                #category_list.append("ui_quest_items")

                if current_category == None:
                    current_category = category_list[0]
                    category_choice = category_list[0]

                item_list = []
                if current_category == "ui_gifts":
                    menu_title = "Gift Items"
                    item_list.extend(candy_gift_list)
                    item_list.extend(mag_gift_list)
                    item_list.extend(drink_gift_list)
                    item_list.extend(toy_gift_list)
                if current_category == "ui_quest_items":
                    menu_title = "Quest Items"
                    item_list.extend(toy_gift_list)

                #item_list = list(filter(lambda x: x.unlocked==False, item_list))
            show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

            $ _return = ui.interact()

            hide screen bottom_menu
            if category_choice != current_category:
                $ current_category = _return

            elif isinstance(_return, item_class):
                if _return.number > 0:
                    call give_cho_gift(_return)
                else:
                    ">You don't own this item."
                    jump cho_gift_menu

                if cho_mood != 0:
                    jump cho_gift_menu
                else:
                    jump cho_requests

            elif _return == "Close":
                $ current_page = 0
                $ category_choice = None
                hide screen bottom_menu
                with d3

                jump cho_requests

            elif _return == "inc":
                $ current_page += 1
            elif _return == "dec":
                $ current_page += -1

            jump cho_gift_menu
        "{color=#858585}-Gifts-{/color}" if gave_cho_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump cho_requests

        "-Dismiss Her-":
            call cho_main("Good bye, [cho_genie_name].","smile","base","base","R")

            jump end_cho_event

label favor_not_ready:
    call nar("You can't do this favour just yet.")
    return

label not_available:
    call nar("This feature is currently not availabel in v[config.version], and will be added in a later patch.")
    return