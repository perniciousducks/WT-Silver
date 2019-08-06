

label open_inventory_menu:
    jump inventory_menu
    #$ current_category = None

    #label inventory_menu:
    #call update_quest_items

    # python:

        # category_list = []
        # category_list.append("ui_gifts")  #Gifts
        # category_list.append("ui_quest_items") #Quest_items

        # if current_category == None:
            # menu_title = "Gift Items"
            # current_category = category_list[0]
            # category_choice = category_list[0]

        # item_list = []
        # if current_category == "ui_gifts":
            # menu_title = "Gift Items"
            # item_list.extend(candy_gift_list)
            # item_list.extend(mag_gift_list)
            # item_list.extend(drink_gift_list)
            # item_list.extend(toy_gift_list)
        # if current_category == "ui_quest_items":
            # menu_title = "Quest Items"
            # item_list.extend(gen_quest_items_list)

        # #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    # show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    # $ _return = ui.interact()

    # hide screen bottom_menu
    # if category_choice != current_category:
        # $ current_category = _return

    # elif isinstance(_return, item_class):
        # if _return in gen_quest_items_list:
            # $ quest_item = _return
            # jump use_your_quest_item
        # else:
            # call item_description(_return)
            # jump inventory_menu

    # elif _return == "Close":
        # $ current_page = 0
        # $ category_choice = None
        # hide screen bottom_menu
        # with d3

        # jump day_main_menu

    # elif _return == "inc":
        # $ current_page += 1
    # elif _return == "dec":
        # $ current_page += -1

    # jump inventory_menu

label use_your_quest_item: #(quest_item)

    if quest_item == sealed_scroll_ITEM:
        if sealed_scroll_ITEM.unlocked and tentacle_owned == False:
            m "It's missing the key ingredient."

    if quest_item == puzzle_box_ITEM:
        if unlocked_7th == False:
            jump start_slide_puzzle

    jump day_main_menu
