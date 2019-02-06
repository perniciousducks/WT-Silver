












label cho_wardrobe_test: # WIP

    # Reset
    $ category_choice = None
    #$ category_choice = None
    $ current_group = "1"
    $ char_name = cho_name
    $ bg_color = "gray" # Temporarily
    $ hide_transitions = True

    label cho_wardrobe_test_menu:

    call update_cho_wardrobe_items(current_category, current_group) # Updates 'item_list'
    call cho_main(xpos="wardrobe",ypos="base")

    label wardrobe_test_menu:

    python:

        # Right Wardrobe Panel
        current_category = category_choice
        wardrobe_categories = ["head","tops","bottoms","other","misc","underwear","outfits","gifts"]

        # Left Wardrobe Panel
        if current_group == "1":
            current_group = group_list[0]
            group_choice = group_list[0]

        if current_category == "head":
            menu_title = "Hair & Head Items"
        if current_category == "tops":
            menu_title = "Tops"
        # Add more

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))

    show screen wardorobe_menu(char_name, current_category, xpos=550, ypos=50)

    #if current_category != None:
    #    show screen wardorobe_item_menu(item_list, current_category, current_group, menu_title, xpos=nxpos, ypos=nypos)

    $ _return = ui.interact()

    hide screen wardorobe_menu
    hide screen wardorobe_item_menu

    if isinstance(_return, item_class):
        call equip_cho_item(_return)

    elif _return == "Close":
        $ current_page = 0
        $ hide_transitions = False
        call cho_main(xpos="base",ypos="base")

        jump cho_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump cho_wardrobe_test_menu


# Right Wardrobe Menu # Not working yet
screen wardorobe_menu(character, category, xpos, ypos):
    $ ui_xpos = xpos
    $ ui_ypos = ypos
    zorder 4

    # Close Button
    use top_bar_close_button

    # Main Window
    add "interface/wardrobe/bg/" +str(bg_color)+ "_right.png" xpos ui_xpos+100 ypos ui_ypos
    if category == None:
        add "interface/wardrobe/test/" +str(interface_color)+ "/icons_" +str(character)+ ".png" xpos ui_xpos+13 ypos ui_ypos+80 zoom 0.5
    else:
        add "interface/wardrobe/test/" +str(interface_color)+ "/icons_" +str(character)+ "_" +str(category)+ ".png" xpos ui_xpos+13 ypos ui_ypos+80 zoom 0.5

    imagemap:
        xpos ui_xpos
        ypos ui_ypos
        xsize 540 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/store/"+interface_color+"/wardrobe_panel.png"
        hover "interface/store/"+interface_color+"/wardrobe_panel_hover.png"

        for i in range(0,4): # Left side.
            if category == wardrobe_categories[i]:
                hotspot (15 , 82 +(110*i) , 85 , 93) clicked SetVariable("category_choice",None), Return()
            else:
                hotspot (15+48 , 82 +(110*i) , 37 , 93) clicked SetVariable("category_choice",wardrobe_categories[i]), Return()

        for i in range(4,8): # Right side.
            if category == wardrobe_categories[i]:
                hotspot (15 +425 , 82 +(110*(i-4)) , 84 , 93) clicked SetVariable("category_choice",None), Return()
            else:
                hotspot (15 +425 , 82 +(110*(i-4)) , 40 , 93) clicked SetVariable("category_choice",wardrobe_categories[i]), Return()



        # Character Name
        add "interface/general/"+str(interface_color)+"/button_wide.png" xpos 200 ypos -4
        hbox:
            xpos 200
            ypos -4
            xsize 140
            ysize 34
            text character xalign 0.5 yalign 0.5 size 16 bold 0.2

        #Categories
        #for i in range(0,len(categories)): #Max 5 items!
        #    hotspot (12+(90*i), 87, 83, 85) clicked SetVariable("category_choice",categories[i]), Return(categories[i])
        #    add "interface/icons/" +str(categories[i])+ ".png" xpos 0+(90*i) ypos 70 zoom 0.35

        #Items
        #for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
        #    if i < len(menu_items):
        #        $ row = i // 5
        #        $ col = i % 5
        #        if menu_items[i].number > 0 or menu_items[i].unlocked == True:
        #            hotspot ( (12+(90*col)), (87+92+(92*row)-(current_page*items_shown)), 83, 85) clicked Return(menu_items[i])
        #        text str(menu_items[i].number) xpos 75+(90*col) ypos 150+92+(92*row)
        #        use icon_menu_item(menu_items[i], 5+90*(col-(current_page*items_shown)), 175+90*(row-(current_page*items_shown)))


# Left Wardrobe Menu # Not working yet
screen wardorobe_item_menu(menu_items, categories, character, title, xpos, ypos):
    $ items_shown = 20
    $ ui_xpos = xpos
    $ ui_ypos = ypos
    zorder 5

    #Up Button
    imagebutton:
        xpos ui_xpos +480
        ypos ui_ypos +175
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button
    imagebutton:
        xpos ui_xpos +480
        ypos ui_ypos +175 +52
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Main Window
    imagemap:
        xpos ui_xpos
        ypos ui_ypos
        xsize 467 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/store/"+interface_color+"/icons_panel.png"
        hover "interface/store/"+interface_color+"/icons_panel_hover.png"

        #Header
        hbox:
            xpos 11
            ypos 30
            xsize 265
            ysize 45
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        #Categories
        for i in range(0,len(categories)): #Max 5 items!
            hotspot (12+(90*i), 87, 83, 85) clicked SetVariable("category_choice",categories[i]), Return(categories[i])
            add "interface/icons/" +str(categories[i])+ ".png" xpos 0+(90*i) ypos 70 zoom 0.35

        #Items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                $ row = i // 5
                $ col = i % 5
                if menu_items[i].number > 0 or menu_items[i].unlocked == True:
                    hotspot ( (12+(90*col)), (87+92+(92*row)-(current_page*items_shown)), 83, 85) clicked Return(menu_items[i])
                text str(menu_items[i].number) xpos 75+(90*col) ypos 150+92+(92*row)
                use icon_menu_item(menu_items[i], 5+90*(col-(current_page*items_shown)), 175+90*(row-(current_page*items_shown)))



label update_cho_wardrobe_items(category, group):
python:

    item_list = []
    group_list = ["1"]
    toggle_list = []
    use_wr_color = False

    if category == "head":
        group_list = ["1","2","3"]
        if group == "1":
            item_list.append("ponytail_blue")

    if category == "tops":
        group_list = ["1","3"]
        item_xpos_offset = 0
        item_ypos_offset = 0
        item_scaling = 0.5

        if group == "1":
            item_list.append("uniform_r")
        if group == "3":
            use_wr_color = True
            item_list.append("uniform_r")

    if category == "bottoms":
        if group == "1":
            use_wr_color = True
            item_list.append("skirt_1")



return
