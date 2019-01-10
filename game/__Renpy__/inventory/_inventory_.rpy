

label open_inventory_menu:
    call update_quest_items
    $ current_category = None
    label inventory_menu:
        python:

            category_list = [] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
            category_list.append("item_chocolate")  #Gifts
            #category_list.append("item_potion")    #Potions
            #category_list.append("cards") #Cards
            #category_list.append("gold")  #Gold
            category_list.append("box_blue_1") #Quest_items

            if current_category == None:
                current_category = category_list[0]
                category_choice = category_list[0]

            item_list = []
            if current_category == "item_chocolate":
                item_list.extend(candy_gift_list)
                item_list.extend(mag_gift_list)
                item_list.extend(drink_gift_list)
                item_list.extend(toy_gift_list)
            if current_category == "item_potion":
                item_list.extend(candy_gift_list) #Add a list with potion items. New potion items need to be created first! Replace the old ones.
            if current_category == "gold":
                item_list.extend(candy_gift_list) #ADD right list.
            if current_category == "cards":
                item_list.extend(candy_gift_list) #ADD right list.
            if current_category == "box_blue_1":
                item_list.extend(gen_quest_items_list)

            #item_list = list(filter(lambda x: x.unlocked==False, item_list))
        show screen icon_menu(item_list, category_list, "Inventory", xpos=492, ypos=50)

        $ _return = ui.interact()

        hide screen icon_menu
        if category_choice != current_category:
            $ current_category = _return

        elif isinstance(_return, item_class):
            if _return in gen_quest_items_list:
                $ quest_item = _return
                jump use_your_quest_item
            else:
                call item_description(_return)
                jump inventory_menu

        elif _return == "Close":
            $ current_page = 0
            $ category_choice = None
            hide screen icon_menu
            with d3

            jump day_main_menu

        elif _return == "inc":
            $ current_page += 1
        elif _return == "dec":
            $ current_page += -1

        jump inventory_menu

label use_your_quest_item: #(quest_item)

    if quest_item == sealed_scroll_ITEM:
        if sealed_scroll_ITEM.unlocked and tentacle_owned == False:
            m "It's missing the key ingredient."

    if quest_item == puzzle_box_ITEM:
        if sealed_scroll_ITEM.unlocked and unlocked_7th == False:
            jump start_slide_puzzle

    jump day_main_menu
