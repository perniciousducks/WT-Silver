

label summon_luna:

    call play_sound("door")

    call lun_chibi("stand","mid","base")

    if lun_dom >= lun_sub:
        if lun_dom >= 4:
            call lun_main("[lun_genie_name]...","normal","suspicious","angry","R",xpos="base",ypos="base")
        else:
            call lun_main("[lun_genie_name]...","upset","mad","mad","R",xpos="base",ypos="base")
    else:
        call lun_main("[lun_genie_name]...","normal","base","sad","mid",xpos="base",ypos="base")

    label luna_requests:

    $ menu_x = 0.1
    $ menu_y = 0.5

    $ hide_transitions = False
    $ luna_busy = True

    menu:
        "-Chit Chat-":
            call luna_chitchat
            jump luna_requests

        "-favours-":
            if gold <= 0 and not lun_reverted:
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

            $ hide_transitions = True
            call lun_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        "-Gifts-":
            $ current_category = None
            label luna_gift_menu:
                python:

                    category_list = [] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
                    category_list.append("item_lollipop")
                    category_list.append("item_mag_adult")
                    category_list.append("item_butterbeer")
                    category_list.append("item_plush_owl")
                    category_list.append("box_brown_3")

                    if current_category == None:
                        current_category = category_list[0]
                        category_choice = category_list[0]

                    item_list = []
                    if current_category == "item_lollipop":
                        item_list.extend(candy_gift_list)
                    if current_category == "item_mag_adult":
                        item_list.extend(mag_gift_list)
                    if current_category == "item_butterbeer":
                        item_list.extend(drink_gift_list)
                    if current_category == "item_plush_owl":
                        item_list.extend(toy_gift_list)
                    if current_category == "box_brown_3":
                        item_list.extend(toy_gift_list)

                    #item_list = list(filter(lambda x: x.unlocked==False, item_list))
                show screen icon_menu(item_list, category_list, "Gifts & Quest Items", xpos=257, ypos=50)

                $ _return = ui.interact()

                hide screen icon_menu
                if category_choice != current_category:
                    $ current_category = _return

                elif isinstance(_return, item_class):
                    call give_lun_gift(_return)
                    if lun_mood == 0:
                        jump luna_gift_menu
                    else:
                        jump luna_requests

                elif _return == "Close":
                    $ current_page = 0
                    $ category_choice = None
                    hide screen icon_menu
                    with d3

                    jump luna_requests

                elif _return == "inc":
                    $ current_page += 1
                elif _return == "dec":
                    $ current_page += -1

                jump luna_gift_menu

        "-Never mind-":

            #ADD Luna says goodbye.

            call play_sound("door")

            $ luna_busy = True

            jump main_room



label luna_favour_menu:
    menu:
        "-Talk to me-" if not lun_reverted:
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
