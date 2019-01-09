

label summon_cho:

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

                    category_list = [] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
                    category_list.append("item_lollipop")
                    category_list.append("item_mag_porn")
                    category_list.append("item_butterbeer")
                    category_list.append("item_broom")
                    #category_list.append("box_brown_1")

                    if current_category == None:
                        current_category = category_list[0]
                        category_choice = category_list[0]

                    item_list = []
                    if current_category == "item_lollipop":
                        item_list.extend(candy_gift_list)
                    if current_category == "item_mag_porn":
                        item_list.extend(mag_gift_list)
                    if current_category == "item_butterbeer":
                        item_list.extend(drink_gift_list)
                    if current_category == "item_broom":
                        item_list.extend(toy_gift_list)
                    if current_category == "box_brown_1":
                        item_list.extend(toy_gift_list)

                    #item_list = list(filter(lambda x: x.unlocked==False, item_list))
                show screen icon_menu(item_list, category_list, "Gifts & Quest Items", xpos=257, ypos=50)

                $ _return = ui.interact()

                hide screen icon_menu
                if category_choice != current_category:
                    $ current_category = _return

                elif isinstance(_return, item_class):
                    call give_cho_gift(_return)
                    if cho_mood != 0:
                        jump cho_gift_menu
                    else:
                        jump cho_requests

                elif _return == "Close":
                    $ current_page = 0
                    $ category_choice = None
                    hide screen icon_menu
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
