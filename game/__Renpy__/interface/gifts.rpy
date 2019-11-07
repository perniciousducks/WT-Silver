label gift_menu:
    python:
        category_list = ["ui_gifts", "ui_quest_items"] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
        current_category = category_list[0]
        category_choice = category_list[0]
        current_page = 0

    label .after_init:

    python:
        item_list = []
        if current_category == "ui_gifts":
            menu_title = "Gift Items"
            item_list.extend(candy_gift_list)
            item_list.extend(mag_gift_list)
            item_list.extend(drink_gift_list)
            item_list.extend(toy_gift_list)

        if current_category == "ui_quest_items":
            menu_title = "Quest Items"
            #item_list.extend(toy_gift_list)

            #TODO Manage (quest) items for all girls (avoid using globals() magic, maybe have one global inventory object)
            if active_girl == "hermione":
                item_list.extend(her_quest_items_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    $ _return = ui.interact()

    hide screen bottom_menu
    
    if category_choice != current_category:
        $ current_category = _return
    elif isinstance(_return, item_class):
        if current_category == "ui_quest_items":
            # Give quest item
            $ quest_item = _return
            call expression 'give_'+active_girl[:3]+'_quest_item'
        elif _return.number > 0:
            # Give gift
            call expression 'give_'+active_girl[:3]+'_gift' pass (gift_item=_return)
            if globals()[active_girl[:3]+"_mood"] <= 0:
                return
        else:
            ">You don't own this item."
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page -= 1
    elif _return == "Close":
        hide screen bottom_menu
        with d3
        return

    jump .after_init
    
label give_gift(text = "", gift = ""):
    hide screen hermione_main
    with d3
    $ the_gift = "interface/icons/"+str(gift.image)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift.number -= 1

    return
