

label summon_cho:

    call play_sound("door")

    call cho_chibi("stand","mid","base")
    call ctc
    call cho_random_clothing

    label cho_requests:

    $ menu_x = 0.1
    $ menu_y = 0.5

    $ hide_transitions = False
    $ cho_busy = True

    menu:
        #"-Talk-":
        "-Training-": #For Quidditch events.
            jump cho_training_menu
        "-Personal Favours-":
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

        #"-Public Favours-":
        #    "To be done."
        #    jump summon_cho

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

        "-Gifts-" if not gave_cho_gift:
            $ current_category = None

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

            call play_sound("door")

            $ cho_busy = True

            jump main_room



label cho_training_menu:
    menu:
        "-Change outfit-":
            jump cho_wardrobe_test
            #jump cho_quidditch_outfit
        #"-Discuss tactics-":
        #    jump cho_tactics
        "-Go back-":
            jump cho_requests
