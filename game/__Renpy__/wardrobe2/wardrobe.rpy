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
    $ current_subcategory = ""
    $ current_item = None
    $ wardrobe_categories_sorted = ["head", "tops", "bottoms", "legs", "misc", "underwear", "outfits", "studio"]
    $ wardrobe_categories = char_active.clothing_dictlist
    
    python:
        list_keys = char_active.clothing.keys()
        character_clothing = []
        for i in xrange(0, len(list_keys)):
            value = char_active.clothing[list_keys[i]][1]
            character_clothing.append([list_keys[i], value])
        character_clothing = sorted(character_clothing, key=lambda x: x[1], reverse=True)
        character_clothing.pop(12)
    
    if wardrobe_music_active:
        call play_music("my_immortal")
    
    label t_wardrobe_after_init:
    
    show screen t_wardrobe_menu(550, 50)
    
    if current_category:
        if current_category == "outfits":
            show screen t_wardrobe_outfit_menuitem(20, 50)
        else:
            show screen t_wardrobe_menuitem(20, 50)
    
    $ _return = ui.interact()
    
    hide screen t_wardrobe_menu
    hide screen t_wardrobe_menuitem
    hide screen t_wardrobe_outfit_menuitem
    
    $ ui_hint = ""
    
    if _return[0] == "equip":
        $ renpy.play('sounds/equip.ogg')
        $ current_item = _return[1]
        $ char_active.equip(current_item)
    elif _return == "addoutfit":
        $ cho_outfit_custom.clone()
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "deloutfit":
        $ char_active.outfits.pop(_return[1])
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "export":
        $ _return[1].outfit_export()
    elif _return == "import":
        $ cho_outfit_custom.outfit_import()
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        show screen t_wardrobe_menu(550, 50)
        $ char_active.cache_override = True
        $ current_item.set_color(active_layer)
        $ char_active.cache_override = False
        $ active_layer = None
        $ char_active.cached = False
    elif _return == "item_reset":
        $ current_item.reset_color()
        $ char_active.cached = False
    elif _return == "bg_color":
        show screen t_wardrobe_menu(550, 50)
        $ bg_color_wardrobe = color_picker(get_rgb_tuple(bg_color_wardrobe), False, "Wardrobe Background Color", pos_xy=[20, 130])
        $ bg_color_wardrobe = get_hex_string(bg_color_wardrobe[0]/255.0, bg_color_wardrobe[1]/255.0, bg_color_wardrobe[2]/255.0, bg_color_wardrobe[3]/255.0)
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return[0] == "category":
        $ current_page = 0
        if current_category == _return[1]:
            $ renpy.play('sounds/door2.mp3')
            $ current_category = ""
            $ current_subcategory = ""
            $ char_active.wear("all")
        else:
            $ renpy.play('sounds/scroll.mp3')
            $ current_category = _return[1]
            # Outfits
            if current_category == "outfits":
                $ category_items = ["Load", "Save", "Delete"]
                $ current_subcategory = category_items[0]
                $ current_item = None
                $ char_active.wear("all")
                $ menu_items = char_active.outfits
                $ menu_items_length = len(menu_items)
            elif current_category == "studio":
                call expression 'studio' pass (studio_return=return_label, studio_char=char_label)
            else:
                if current_category == "underwear":
                    $ char_active.strip("top")
                    $ char_active.strip("bottom")
                    $ char_active.strip("robe")
                else:
                    $ char_active.wear("top")
                    $ char_active.wear("bottom")
                    $ char_active.wear("robe")
                $ category_items = wardrobe_categories.get(current_category)
                # Default subcategory
                if category_items:
                    $ current_subcategory = list(category_items)[0]
                    $ menu_items = category_items[current_subcategory]
                else:
                    $ category_items = []
                    $ current_subcategory = "No items available"
                    $ menu_items = []
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
    elif _return[0] == "subcategory":
        if current_subcategory != _return[1]:
            $ renpy.play('sounds/scroll.mp3')
            $ current_subcategory = _return[1]
            if current_category != "outfits":
                $ current_page = 0
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
        
        for i in xrange(0, len(wardrobe_categories_sorted)):
            $ cat_row = (i // 4) % 2
            $ cat_col = i % 4
            if current_category == wardrobe_categories_sorted[i]:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/test/"+char_active.char+"_"+wardrobe_categories_sorted[i]+".png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                button xpos 14+411*cat_row ypos 80+110*cat_col xsize 90 ysize 96 style "empty" hover_background btn_hover action Return(["category", wardrobe_categories_sorted[i]])
            else:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/test/"+char_active.char+"_"+wardrobe_categories_sorted[i]+".png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                button xpos 61+377*cat_row ypos 80+110*cat_col xsize 44 ysize 96 style "empty" hover_background btn_hover action Return(["category", wardrobe_categories_sorted[i]]) hovered SetVariable("ui_hint", wardrobe_categories_sorted[i]) unhovered SetVariable("ui_hint", "")
        
        frame xsize 340 ysize 548 xpos 100 style "empty" background bg_color_wardrobe
        
        #add "interface/wardrobe/test/"+str(interface_color)+"/icons_"+char_active.char+"_"+current_category+".png" xpos 13 ypos 80 zoom 0.5

        add "interface/panels/"+interface_color+"/wardrobe_panel.png"

        hbox:
            xpos 120
            ypos 60
            spacing 158
            vbox:
                spacing 2
                for i in xrange (0, len(character_clothing)):
                    $ curr_item = character_clothing[i][0]
                    textbutton "{size=12}[curr_item]{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(char_active.get_worn(curr_item))+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Function(char_active.toggle_wear, curr_item)
            vbox:
                ypos 416
                textbutton "{size=12}Music{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_"+str(wardrobe_music_active)+".png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("music")
                textbutton "{size=12}BG Color{/size}" style "empty" background "interface/wardrobe/"+str(interface_color)+"/check_true.png" text_yanchor 0.5 text_ypos 14 text_xpos 24 ysize 24 xsize 68 action Return("bg_color")
                
        # Tooltip
        if persistent.ui_hint:
            text "[ui_hint]" xalign 0.5 ypos 33
            
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
        
        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                xpos 270
                spacing 5
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown)+1)) ypos 44 size 16
        
        if current_item:
            hbox:
                xpos 300
                ypos 40
                spacing 4
                
                for i in xrange(0, current_item.layers):
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
                $ image_zoom = get_zoom(menu_items[i].get_icon(), 80, 80)
                add menu_items[i].get_icon() xpos 58+90*col ypos 225+90*row xanchor 0.5 yanchor 0.5 zoom image_zoom
                button xsize 90 ysize 90 style "empty" hover_background btn_hover xpos 10+90*(col) ypos 176+90*(row) action Return(["equip", menu_items[i]])
                if menu_items[i].id == char_active.get_equipped(current_category, current_subcategory, i):
                    text "{color=#FFFFFF}Worn{/color}"xpos 26+90*col ypos 240+90*row
                    
        # Add empty items
        for i in xrange(menu_items_length, items_shown):
            $ row = (i // 5) % 4
            $ col = i % 5
            button xsize 88 ysize 88 style "empty" background "#00000033" xpos 10+90*(col) ypos 180+90*(row)
                    
screen t_wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    if menu_items_length > 9:
        # Up Button
        if not current_page <= 0:
            imagebutton:
                xpos xx+480
                ypos yy+190
                idle "interface/general/"+interface_color+"/button_arrow_up.png"
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")
        if current_page < math.ceil((menu_items_length)/10):
            # Down Button
            imagebutton:
                xpos xx+480
                ypos yy+245
                idle "interface/general/"+interface_color+"/button_arrow_down.png"
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        xpos xx
        ypos yy
        xsize 467
        ysize 548
        style "empty"
        background bg_color_wardrobe
   
        add "interface/panels/"+interface_color+"/icon_panel_2.png"
            
        text "[current_category]: [current_subcategory]" xpos 24 ypos 44 size 16
        
        textbutton "Import" xsize 100 ysize 50 action Return("import")
        
        # Page counter
        if menu_items_length > 9:
            hbox:
                xanchor 1.0
                xpos 270
                spacing 5
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/10))+1) ypos 44 size 16
        
        # Add subcategory list
        for i in xrange (0, len(category_items)):
            add "interface/wardrobe/test/icons/"+current_category+"_"+category_items[i]+".png" ypos 88 xpos 10+(90*i) zoom 0.2
            button xsize 86 ysize 86 ypos 88 xpos 10+(90*i) style "empty" hover_background btn_hover action Return(["subcategory", category_items[i]])
        
        # Add items
        for i in xrange(current_page*10, (current_page*10)+10):
            if i < menu_items_length:
                $ row = (i // 5) % 2
                $ col = i % 5
                add menu_items[i].get_image() xpos 40+90*col ypos 117+180*row xalign 0.5 zoom 0.2
                if current_subcategory == "Delete":
                    button xsize 90 ysize 180 style "empty" hover_background "#cc330040" xpos 10+90*col ypos 176+180*row action Return(["deloutfit", i])
                    #textbutton "{color=#B33A3A}{size=50}-{/size}{/color}" style "empty" hover_background "#cc330040" xsize 90 ysize 180 xpos 10+90*col ypos 176+180*row text_xalign 0.5 text_yalign 0.5 action Return(["deloutfit", i]) text_outlines [ (4, "#000", 0, 0) ]
                elif current_subcategory == "Load":
                    button xsize 90 ysize 180 style "empty" hover_background btn_hover xpos 10+90*col ypos 176+180*row action Return(["equip", menu_items[i]])
                    textbutton "E" xsize 50 ysize 50 style "empty" hover_background btn_hover xpos 10+90*col ypos 176+180*row text_align 0.5 action Return(["export", menu_items[i]])
                    
        # Add empty items
        for i in xrange(menu_items_length, (current_page*10)+10):
            $ row = (i // 5) % 2
            $ col = i % 5
            if current_subcategory == "Save":
                textbutton "{color=#FFFFFF}{size=50}+{/size}{/color}" style "empty" background "#00000033" hover_background btn_hover xsize 88 ysize 178 xpos 10+90*col ypos 180+180*row text_xalign 0.5 text_yalign 0.5 action Return("addoutfit")
            else:
                button style "empty" background "#00000033" xsize 88 ysize 178 xpos 10+90*col ypos 180+180*row