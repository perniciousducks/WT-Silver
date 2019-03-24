

# Susan Gift Menu

label susan_gift_menu:

    python:

        category_list = [] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
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
            call give_sus_gift(_return)
        else:
            ">You don't own this item."
            jump susan_gift_menu

        if sus_mood != 0:
            jump susan_gift_menu
        else:
            jump susan_requests

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump susan_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump susan_gift_menu



# Susan Gift Responses

label give_sus_gift(gift_item):
    hide screen susan_main
    with d5
    call sus_main(xpos="mid",ypos="base",trans="d5")

    if gift_item == lollipop_ITEM:
        call give_gift(">You give the lollipop to Susan...",gift_item)
        #Add text

    if gift_item == chocolate_ITEM:
        call give_gift(">You give the chocolate to Susan...",gift_item)
        #Add text

    if gift_item == plush_owl_ITEM:
        call give_gift(">You give the plush owl to Susan...",gift_item)
        #Add text

    if gift_item == butterbeer_ITEM:
        call give_gift(">You give the butterbeer to Susan...",gift_item)
        #Add text

    if gift_item == science_mag_ITEM:
        call give_gift(">You give the educational magazine to Susan...",gift_item)
        #Add text

    if gift_item == girls_mag_ITEM:
        call give_gift(">You give the girls magazine to Susan...",gift_item)
        #Add text

    if gift_item == adult_mag_ITEM:
        call give_gift(">You give the adult magazine to Susan...",gift_item)
        #Add text

    if gift_item == porn_mag_ITEM:
        call give_gift(">You give the porn magazine to Susan...",gift_item)
        #Add text

    if gift_item == krum_poster_ITEM:
        call give_gift(">You give the poster to Susan...",gift_item)
        #Add text

    if gift_item == sexy_lingerie_ITEM:
        call give_gift(">You give the lingerie to Susan...",gift_item)
        #Add text

    if gift_item == pink_condoms_ITEM:
        call give_gift(">You give the condoms to Susan...",gift_item)
        #Add text

    if gift_item == vibrator_ITEM:
        call give_gift(">You give the vibrator to Susan...",gift_item)
        #Add text

    if gift_item == anal_lube_ITEM:
        call give_gift(">You give the anal lube to Susan...",gift_item)
        #Add text

    if gift_item == ballgag_and_cuffs_ITEM:
        call give_gift(">You give the handcuffs to Susan...",gift_item)
        #Add text

    if gift_item == anal_plugs_ITEM:
        call give_gift(">You give the anal plugs to Susan...",gift_item)
        #Add text

    if gift_item == testral_strapon_ITEM:
        call give_gift(">You give the strap-on to Susan...",gift_item)
        #Add text

    if gift_item == broom_2000_ITEM:
        call give_gift(">You give the broom to Susan...",gift_item)
        #Add text

    if gift_item == sexdoll_ITEM:
        call give_gift(">You give the doll to Susan...",gift_item)
        #Add text


    hide screen susan_main
    with d5
    call sus_main(xpos="base",ypos="base",trans="d5")

    return
