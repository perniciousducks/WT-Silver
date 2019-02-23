label t_wardrobe(return_label, char_label):
    $ char_active = get_character_object(active_girl)
    $ char_nickname = char_active.char
    $ hide_transitions = True
    
    # Styling
    if daytime:
        $ btn_hover = "#e3ba7140"
    else:
        $ btn_hover = "#7d75aa40"
        
    default bg_color_wardrobe = "#7d756e"
    
    $ items_shown = 20
    $ current_page = 0
    $ current_category = ""
    $ current_item = None
    $ wardrobe_categories_sorted = ["head", "tops", "bottoms", "legs", "potions", "underwear", "outfits", "gifts"]
    $ wardrobe_categories = char_active.clothing_dictlist
    
    python:
        list_keys = char_active.clothing.keys()
        character_clothing = []
        for i in xrange(0, len(list_keys)):
            value = char_active.clothing[list_keys[i]][1]
            character_clothing.append([list_keys[i], value])
        character_clothing = sorted(character_clothing, key=lambda x: x[1], reverse=True)
    
    if wardrobe_music_active:
        call play_music("my_immortal")
    
    label t_wardrobe_after_init:
    
    show screen t_wardrobe_menu(550, 50)
    
    if current_category != "":
        show screen t_wardrobe_menuitem(20, 50)
    
    $ _return = ui.interact()
    
    hide screen t_wardrobe_menu
    hide screen t_wardrobe_menuitem
    
    if _return[0] == "equip":
        $ renpy.play('sounds/equip.ogg')
        $ current_item = _return[1]
        $ char_active.equip(current_item)
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        show screen t_wardrobe_menu(550, 50)
        $ char_active.cache_override = True
        $ current_item.set_color(active_layer)
        $ char_active.cache_override = False
        $ active_layer = None
        $ char_active.cached = False
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        show screen t_wardrobe_menu(550, 50)
        $ char_active.cache_override = True
        $ current_item.set_color(active_layer)
        $ char_active.cache_override = False
        $ active_layer = None
    elif _return == "bg_color":
        show screen t_wardrobe_menu(550, 50)
        $ bg_color_wardrobe = color_picker(get_rgb_tuple(bg_color_wardrobe), False, "Wardrobe Background Color", pos_xy=[20, 130])
        $ bg_color_wardrobe = get_hex_string(bg_color_wardrobe[0]/255.0, bg_color_wardrobe[1]/255.0, bg_color_wardrobe[2]/255.0, bg_color_wardrobe[3]/255.0)
    elif _return == "item_reset":
        $ current_item.reset_color()
        $ char_active.cached = False
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return[0] == "category":
        if current_category == _return[1]:
            $ renpy.play('sounds/door2.mp3')
            $ current_category = ""
            $ char_active.wear("all")
        else:
            if _return[1] == "underwear":
                $ char_active.strip("top")
                $ char_active.strip("bottom")
            else:
                $ char_active.wear("top")
                $ char_active.wear("bottom")
            $ renpy.play('sounds/scroll.mp3')
            $ current_category = _return[1]
            $ category_items = wardrobe_categories[current_category]
            # Default subcategory
            $ current_subcategory = list(category_items)[0]
            $ menu_items = category_items[current_subcategory]
            $ menu_items_length = len(menu_items)
            # Default selected item
            $ current_item = None
    elif _return[0] == "subcategory":
        $ renpy.play('sounds/scroll.mp3')
        $ current_subcategory = _return[1]
        $ menu_items = category_items[current_subcategory]
        $ menu_items_length = len(menu_items)
        # Default selected item
        $ current_item = None
    elif _return == "erozone":
        call expression char_label pass (text="", face="horny")
    elif _return == "music":
        if wardrobe_music_active:
            $ wardrobe_music_active = False
            call music_block
            call expression char_label pass (text="", face="annoyed")
        else:
            $ wardrobe_music_active = True
            call play_music("my_immortal")
            call expression char_label pass (text="", face="happy")
    elif _return == "Close":
        $ renpy.play('sounds/door2.mp3')
        $ hide_transitions = False
        $ char_active.wear("all")
        if wardrobe_music_active:
            call music_block
        python:
            renpy.jump(return_label)
    jump t_wardrobe_after_init
        
screen t_wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 4

    python:
        if current_item and color_preview and not active_layer == None:
            current_item.color[active_layer] = color_preview
    
    use top_bar_close_button
    
    frame:
        xpos xx
        ypos yy
        xsize 540
        ysize 548
        style "empty"
        
        frame xsize 340 ysize 548 xpos 100 style "empty" background bg_color_wardrobe
        
        add "interface/wardrobe/test/"+str(interface_color)+"/icons_"+char_active.char+"_"+current_category+".png" xpos 13 ypos 80 zoom 0.5

        add "interface/panels/"+interface_color+"/wardrobe_panel.png"
            
        for i in xrange(0, len(wardrobe_categories_sorted)):
            $ cat_row = (i // 4) % 2
            $ cat_col = i % 4
            if current_category == wardrobe_categories_sorted[i]:
                button xpos 14+425*(cat_row) ypos 80+110*(cat_col) xsize 90 ysize 98 style "empty" hover_background btn_hover action Return(["category", wardrobe_categories_sorted[i]])
            else:
                button xpos 61+377*(cat_row) ypos 80+110*(cat_col) xsize 44 ysize 98 style "empty" hover_background btn_hover action Return(["category", wardrobe_categories_sorted[i]])

        vbox:
            xpos 120
            ypos 60
            spacing 5
            textbutton "{size=12}Music{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(wardrobe_music_active)+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("music")
            textbutton "{size=12}BG Color{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_true.png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("bg_color")
            vbox:
                ypos 60
                for i in xrange (0, len(character_clothing)):
                    $ curr_item = character_clothing[i][0]
                    textbutton "{size=12}[curr_item]{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(char_active.get_worn(curr_item))+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Function(char_active.toggle_wear, curr_item)
            
        #Erogenous zones
        vbox:
            xalign 0.5
            ypos 260
            spacing 72
            button xsize 120 ysize 60 style "empty" action Return("erozone")
            button xsize 120 ysize 50 style "empty" action Return("erozone")
                
        add "interface/general/"+str(interface_color)+"/button_wide.png" xpos 200 ypos -4
        text char_nickname xalign 0.5 ypos 4 size 16
        
screen t_wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Buttons
    if menu_items_length > items_shown:
        # Up Button
        imagebutton:
            xpos xx+480
            ypos yy+190
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            if not current_page <= 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")

        # Down Button
        imagebutton:
            xpos xx+480
            ypos yy+245
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            if current_page < math.ceil((menu_items_length-1)/items_shown):
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        xpos xx
        ypos yy
        xsize 467
        ysize 548
        style "empty"
        background bg_color_wardrobe
   
        add "interface/panels/"+interface_color+"/icon_panel_1.png"
        
        if current_item:
            hbox:
                xpos 300
                ypos 40
                spacing 4
                
                for i in xrange(0, current_item.layers-1):
                    button xsize 24 ysize 24 background current_item.get_color_hex(i) action Return(["item_color", i])
                textbutton "R" xsize 24 ysize 24 background "#d3d3d3" action Return("item_reset")
            
        # Add subcategory list
        for i in xrange (0, len(list(category_items))):
            add "interface/wardrobe/test/icons/"+char_active.char+"/"+current_category+"_"+list(category_items)[i]+".png" ypos 88 xpos 10+(90*i) zoom 0.2
            button xsize 86 ysize 86 ypos 88 xpos 10+(90*i) style "empty" hover_background btn_hover action Return(["subcategory", list(category_items)[i]])
            
        text "[current_category]: [current_subcategory]" xpos 24 ypos 44 size 16
        
        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 5) % 4
                $ col = i % 5
                add menu_items[i].get_icon() xpos 40+90*(col) ypos 75+90*(row) xalign 0.5 zoom 0.2
                button xsize 90 ysize 90 style "empty" hover_background btn_hover xpos 10+90*(col) ypos 176+90*(row) action Return(["equip", menu_items[i]])
                if menu_items[i] == char_active.get_equipped(current_category, current_subcategory, i):
                    text "{color=#FFFFFF}Worn{/color}"xpos 26+90*(col) ypos 240+90*(row)