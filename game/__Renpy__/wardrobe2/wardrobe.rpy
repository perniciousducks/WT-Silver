label t_wardrobe(return_label):
    $ char_active = get_character_object(active_girl)
    $ char_nickname = char_active.char
    $ hide_transitions = True
    
    # Styling
    if daytime:
        $ btn_hover = "#e3ba7140"
    else:
        $ btn_hover = "#7d75aa40"
    
    $ items_shown = 20
    $ current_page = 0
    $ current_category = ""
    $ current_item = None
    $ wardrobe_categories = ["head", "misc", "tops", "underwear", "bottoms", "outfits", "other","gifts"]
    
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
        $ active_layer = None
        $ char_active.cache_override = False
    elif _return == "item_reset":
        $ current_item.reset_color()
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return == "category":
        $ renpy.play('sounds/scroll.mp3')
        $ current_item = None
        if current_category:
            $ menu_items = char_active.get_clothing_list(current_category)
            $ menu_items_length = len(menu_items)
    elif _return == "Close":
        $ renpy.play('sounds/door2.mp3')
        $ hide_transitions = False
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
        
        add "interface/wardrobe/test/"+str(interface_color)+"/icons_"+char_active.char+"_"+current_category+".png" xpos 13 ypos 80 zoom 0.5

        add "interface/panels/"+interface_color+"/wardrobe_panel.png"
        
        grid 2 4:
            ypos 78
            xpos 10
            xspacing 330
            yspacing 10
            for i in xrange (0, len(wardrobe_categories)):
                button xsize 98 ysize 100 style "empty" hover_background btn_hover action [ToggleVariable("current_category", wardrobe_categories[i], ""), Return("category")]
                
        hbox:
            xpos 120
            ypos 60
            spacing 12
            imagebutton idle "interface/wardrobe/"+str(interface_color)+"/check_true.png"
            imagebutton idle "interface/wardrobe/"+str(interface_color)+"/check_true.png"
            imagebutton idle "interface/wardrobe/"+str(interface_color)+"/check_true.png"
            
        add "interface/general/"+str(interface_color)+"/button_wide.png" xpos 200 ypos -4
        text char_nickname xalign 0.5 ypos 4 size 16
        
screen t_wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Buttons
    if menu_items_length > items_shown:
        # Up Button
        imagebutton:
            xpos ui_xpos +480
            ypos ui_ypos +190
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            if not current_page <= 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")

        # Down Button
        imagebutton:
            xpos ui_xpos +480
            ypos ui_ypos +190 +55
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

        add "interface/panels/"+interface_color+"/icon_panel_1.png"
        
        text current_category xalign 0.22 ypos 44 size 16
        
        if current_item:
            hbox:
                xpos 300
                ypos 40
                spacing 4
                
                for i in xrange(0, current_item.layers-1):
                    button xsize 24 ysize 24 background current_item.get_color_hex(i) action Return(["item_color", i])

                textbutton "R" xsize 24 ysize 24 background "#d3d3d3" action Return("item_reset")
            
        # Add category list    
        for i in xrange (0, 5):
            button xpos 10+(90*i) ypos 86 xsize 88 ysize 90 style "empty" background "#7d75aa80"
        
        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 5) % 4
                $ col = i % 5
                add menu_items[i].get_icon() xpos 40+90*(col) ypos 75+90*(row) xalign 0.5 zoom 0.2
                button xsize 90 ysize 90 style "empty" hover_background btn_hover xpos 10+90*(col) ypos 176+90*(row) action Return(["equip", menu_items[i]])
                if menu_items[i] == char_active.get_equipped(current_category, i):
                    text "{color=#FFFFFF}Worn{/color}"xpos 26+90*(col) ypos 240+90*(row)