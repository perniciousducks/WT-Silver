default wardrobe_background_day = "#e8c97e"
default wardrobe_background_night = "#7d756e"

default wardrobe_toggles = False
default wardrobe_music = False

label t_wardrobe(char_label):
    python:
        char_active = get_character_object(active_girl)
        char_nickname = char_active.char
        char_scale = 1.0/globals()[active_girl+"_scaleratio"]
        hide_transitions = True

        wardrobe_background = wardrobe_background_day if interface_color == "gold" else wardrobe_background_night
        
        items_shown = 20
        current_page = 0
        current_category = ""
        current_subcategory = ""
        current_item = None
        wardrobe_categories_sorted = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
        wardrobe_categories = char_active.clothing_dictlist
        export_in_progress = False
        item_to_export = None
        wardrobe_outfit_schedule = ("Day", "Night", "Cloudy", "Rainy", "Snowy", "School")

        character_toggles = [(k, v[1]) for k, v in char_active.clothing.iteritems() if k != "hair" and not any(i.isdigit() for i in k)]
        character_toggles.extend([("tattoo", 10), ("piercing", 10), ("makeup", 11), ("accessory", 20)])
        character_toggles.sort(key=lambda x: x[1], reverse=True)
        
        renpy.hide_screen(active_girl+"_main")
    
    if wardrobe_music:
        call play_music("wardrobe")
    
    label .after_init:
    
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
    
    if _return == "tabswitch":
        show screen t_wardrobe_menu(550, 50)
        $ renpy.call(active_girl+"_wardrobe_check", _return)
        if _return in (None, True):
            $ current_page = 0
            $ current_category = ""
            $ current_subcategory = ""
            $ current_item = None
            $ renpy.play('sounds/click3.mp3')
            if "head" in wardrobe_categories_sorted:
                $ wardrobe_categories_sorted = ("face", "torso", "hips", "legs", "makeup", "breasts", "pelvis", "misc")
                $ char_active.strip("top")
                $ char_active.strip("bottom")
                $ char_active.strip("robe")
                $ char_active.strip("bra")
                $ char_active.strip("panties")
            else:
                $ wardrobe_categories_sorted = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
                $ char_active.wear("top")
                $ char_active.wear("bottom")
                $ char_active.wear("robe")
                $ char_active.wear("bra")
                $ char_active.wear("panties")
    elif _return == "studio":
        $ renpy.play('sounds/click3.mp3')
        call studio(char_label)
    elif _return[0] == "equip":
        show screen t_wardrobe_menu(550, 50)
        if _return[1].type in char_active.incompatible_wardrobe:
            $ renpy.play('sounds/fail.mp3')
        else:
            $ renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])
        $ char_active.reset_compatibility()
    elif _return == "addoutfit":
        $ char_active.create_outfit("Custom", "A custom outfit")
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "deloutfit":
        $ char_active.outfits.pop(_return[1])
        $ char_active.update_outfits_schedule(all=True)
        $ menu_items = char_active.outfits
        $ menu_items_length = len(menu_items)
    elif _return[0] == "tagoutfit":
        $ _item = char_active.outfits[_return[1]]
        $ _item.schedule[_return[2]] = not _item.schedule[_return[2]]
        if _return[2] > 1 and (not _item.schedule[0] and not _item.schedule[1]):
            $ _item.schedule[0] = True
            $ _item.schedule[1] = True
        $ char_active.update_outfits_schedule(_item)
    elif _return[0] == "export":
        menu:
            "Export to PNG file" if not renpy.variant('android'):
                $ export_in_progress = True
                $ globals()[active_girl+"_outfit_last"].save()
                $ char_active.equip(_return[1])
                $ item_to_export = _return[1]
                call studio(char_label)
            "Export to clipboard":
                $ _return[1].outfit_export(False)
            "Back":
                pass
        $ achievement.unlock("export")
    elif _return == "import":
        menu:
            "Import from PNG file" if not renpy.variant('android'):
                $ txt_filename = "exported"
                $ txt_filename = renpy.input("Filename", txt_filename, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#& ", length=64)
                $ globals()[active_girl+"_outfit_custom"].outfit_import(True, txt_filename)
            "Import from clipboard":
                $ globals()[active_girl+"_outfit_custom"].outfit_import(False)
            "Back":
                pass
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
        $ active_layer = None
        show screen t_wardrobe_menu(550, 50)
        $ wardrobe_background = color_picker(get_rgb_list(wardrobe_background), False, "Wardrobe Background Color", pos_xy=[20, 130])
        $ wardrobe_background = get_hex_string(wardrobe_background[0]/255.0, wardrobe_background[1]/255.0, wardrobe_background[2]/255.0, wardrobe_background[3]/255.0)
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
            if "head" in wardrobe_categories_sorted:
                $ char_active.wear("all")
        else:
            $ renpy.call(active_girl+"_wardrobe_check", "category", _return)
            $ renpy.play('sounds/scroll.mp3')
            $ current_category = _return[1]
            # Outfits
            if current_category == "outfits":
                $ category_items = ["Load", "Save", "Delete", "Export&Import", "Schedule"]
                $ current_subcategory = category_items[0]
                $ current_item = None
                $ char_active.wear("all")
                $ menu_items = char_active.outfits
                $ menu_items_length = len(menu_items)
            else:
                if current_category in ("bras", "panties"):
                    $ char_active.strip("top")
                    $ char_active.strip("bottom")
                    $ char_active.strip("robe")
                else:
                    if 'head' in wardrobe_categories_sorted:
                        $ char_active.wear("top")
                        $ char_active.wear("bottom")
                        $ char_active.wear("robe")
                $ category_items = wardrobe_categories.get(current_category)
                # Default subcategory
                if category_items:
                    $ current_subcategory = category_items.keys()[0]
                    $ menu_items = category_items.get(current_subcategory)
                else:
                    $ category_items = []
                    $ current_subcategory = "No items available"
                    $ menu_items = []
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if item.id == char_active.get_equipped(current_category, current_subcategory):
                            current_item = item
                            break
    elif _return[0] == "subcategory":
        if current_subcategory != _return[1]:
            $ renpy.play('sounds/scroll.mp3')
            $ current_subcategory = _return[1]
            if current_category != "outfits":
                $ current_page = 0
                $ menu_items = category_items.get(current_subcategory)
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if item.id == char_active.get_equipped(current_category, current_subcategory):
                            current_item = item
                            break
    elif _return[0] == "erozone":
        show screen t_wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen t_wardrobe_outfit_menuitem(20, 50)
            else:
                show screen t_wardrobe_menuitem(20, 50)
        $ renpy.call(active_girl+"_wardrobe_check", "touching", _return[1])
        #call expression char_label pass (text="", face="horny")
    elif _return[0] == "toggle":
        show screen t_wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen t_wardrobe_outfit_menuitem(20, 50)
            else:
                show screen t_wardrobe_menuitem(20, 50)
        $ renpy.call(active_girl+"_wardrobe_check", "toggle", _return[1])
    elif _return == "toggle_schedule":
        $ globals()[active_girl+"_outfits_schedule"] = not globals()[active_girl+"_outfits_schedule"]
    elif _return == "music":
        show screen t_wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen t_wardrobe_outfit_menuitem(20, 50)
            else:
                show screen t_wardrobe_menuitem(20, 50)
        if wardrobe_music:
            $ wardrobe_music = False
            call play_music(active_girl)
            call expression char_label pass (text="", face="annoyed")
        else:
            $ wardrobe_music = True
            call play_music("wardrobe")
            call expression char_label pass (text="", face="happy")
    else: #_return == "Close":
        $ renpy.play('sounds/door2.mp3')
        $ hide_transitions = False
        $ char_active.wear("all")
        $ char_active.clothes_compatible()
        if wardrobe_music:
            call play_music(active_girl)
        return
    jump .after_init
        
screen t_wardrobe_menu(xx, yy):
    tag wardrobe
    zorder 4

    use close_button
    
    frame:
        style "empty"
        pos (xx, yy)
        xysize (540, 548)
        
        # Main Categories
        for i, category in enumerate(wardrobe_categories_sorted):
            $ cat_row = (i // 4) % 2
            $ cat_col = i % 4
            if current_category == category:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/test/"+char_active.char+"_"+category+".png" xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                button:
                    style "empty"
                    pos (14+411*cat_row, 80+110*cat_col)
                    xysize (90, 96)
                    hover_background btn_hover
                    action Return(["category", category])
            else:
                add "interface/wardrobe/test/"+str(interface_color)+"/frame.png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/test/"+char_active.char+"_"+category+".png" xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                button:
                    style "empty"
                    pos (61+377*cat_row, 80+110*cat_col)
                    xysize (44, 96)
                    hover_background btn_hover
                    tooltip category
                    action Return(["category", wardrobe_categories_sorted[i]])
        
        # Background
        frame xysize (340, 548) xpos 100 style "empty" background wardrobe_background
        
        # Character
        add char_active.get_image() zoom char_scale anchor (0.57, 1.0) align (0.5, 1.0) yoffset -2 #yoffset -12
        
        # Switch to body modifications tab
        add "interface/frames/"+str(interface_color)+"/circle.png" pos (373, 62)
        button:
            style "empty"
            pos (373, 62)
            xysize (50, 50)
            background "interface/wardrobe/test/switch.png"
            hover_background image_hover("interface/wardrobe/test/switch.png")
            tooltip "Switch tabs"
            action Return("tabswitch")

        # Outfits Manager
        add "interface/frames/"+str(interface_color)+"/circle.png" pos (373, 117)
        button:
            style "empty"
            pos (373, 117)
            xysize (50, 50)
            background "interface/wardrobe/test/outfits.png"
            hover_background image_hover("interface/wardrobe/test/outfits.png")
            tooltip "Outfits Manager"
            action Return(["category", "outfits"])

        # Studio
        if not renpy.variant('android'):
            add "interface/frames/"+str(interface_color)+"/circle.png" pos (373, 172)
            button:
                style "empty"
                pos (373, 172)
                xysize (50, 50)
                background "interface/wardrobe/test/studio.png"
                hover_background image_hover("interface/wardrobe/test/studio.png")
                tooltip "Open Studio"
                action Return("studio")

        add "interface/panels/"+interface_color+"/wardrobe_panel.png"
        
        #Easter Egg
        vbox:
            xalign 0.5
            ypos 260
            spacing 72
            button style "empty" xysize (120, 60) action Return(["erozone", "boobs"])
            button style "empty" xysize (120, 50) action Return(["erozone", "pussy"])
        
        # Toggles
        if wardrobe_toggles:
            vbox:
                pos (116, 60)
                for item in character_toggles:
                    $ curr_item = item[0]
                    textbutton "{size=12}[curr_item]{/size}":
                        style "empty"
                        ysize 24
                        text_yalign 0.5
                        text_first_indent 26
                        background "interface/frames/"+str(interface_color)+"/check_"+str(char_active.get_worn(curr_item))+".png"
                        tooltip "Show/hide "+str(curr_item)
                        action Return(["toggle", curr_item])
                        
        # User Settings
        hbox:
            spacing 2
            pos (116, 28)
            if not renpy.variant("android"):
                textbutton "{size=12}Toggles{/size}":
                    style "empty"
                    ysize 24
                    text_yalign 0.5
                    text_first_indent 26
                    background "interface/frames/"+str(interface_color)+"/check_"+str(wardrobe_toggles)+".png"
                    tooltip "Expand/Hide toggles"
                    action ToggleVariable("wardrobe_toggles", True, False)
            textbutton "{size=12}Music{/size}":
                style "empty"
                ysize 24
                text_yalign 0.5
                text_first_indent 26
                background "interface/frames/"+str(interface_color)+"/check_"+str(wardrobe_music)+".png"
                tooltip "Toggle music"
                action Return("music")
            textbutton "{size=12}Background{/size}":
                style "empty" 
                ysize 24
                text_yalign 0.5
                text_first_indent 26
                background "interface/frames/"+str(interface_color)+"/check_true.png" 
                tooltip "Change background colour"
                action Return("bg_color") 
                
        # Zoom slider
        # bar:
            # area (25, 290, 255, 30)
            # value VariableValue("char_scale", range=1.0, step=0.01, style=u'bar')
            # top_gutter 0
            # bottom_gutter 0
                
        add "interface/general/"+str(interface_color)+"/button_wide.png" pos (200, -4)
        text char_nickname xalign 0.5 ypos 4 size 16
        
screen t_wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Navigational Buttons Up/Down
    if menu_items_length > items_shown:
        imagebutton:
            pos (xx+480, yy+190)
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            if not current_page <= 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")

        imagebutton:
            pos (xx+480, yy+245)
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            if current_page < math.ceil((menu_items_length-1)/items_shown):
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background
   
        add "interface/panels/"+interface_color+"/icon_panel_1.png"
        
        hbox:
            pos (24, 44)
            spacing 3
            text "[current_category]:" size 18
            text "[current_subcategory]" size 12 yalign 0.5
        
        # Page Counter
        if menu_items_length > items_shown:
            textbutton str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown)+1)):
                style "empty" 
                ysize 32
                pos (270, 37)
                xanchor 1.0
                background "interface/page.png"
                text_yalign 0.5
                text_first_indent 26
                action NullAction()
        
        # Colours
        if current_item:
            hbox:
                pos (283, 31)
                spacing 2
                
                for i in xrange(current_item.layers):
                    button:
                        xysize (32, 44)
                        background current_item.get_color_hex(i)
                        tooltip "Change colour ("+str(i+1)+")"
                        action Return(["item_color", i])
            # Reset Button
            textbutton "R":
                pos (422, 31) 
                xysize (32, 44) 
                background "#d3d3d3"
                tooltip "Reset all colours"
                action Return("item_reset") 
            
        # Add subcategory list
        if len(category_items) > 0:
            for i, subcategory in enumerate(category_items.keys()):
                add "interface/wardrobe/test/icons/"+char_active.char+"/"+current_category+"_"+subcategory+".png" ypos 86 xpos 10+(90*i) zoom 0.2
                button:
                    style "empty"
                    pos (10+90*i, 86)
                    xysize (86, 86)
                    hover_background btn_hover
                    tooltip subcategory
                    action Return(["subcategory", subcategory])
        
        # Add Clothing Items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 5) % 4
                $ col = i % 5
                $ image_zoom = get_zoom(menu_items[i].get_icon(), 83, 85)
                frame:
                    style "empty"
                    pos (12+90*col, 180+90*row)
                    xysize (83, 85)
                    
                    add menu_items[i].get_icon() zoom image_zoom xalign 0.5 yalign 0.5
                if menu_items[i].id == char_active.get_equipped(current_category, current_subcategory, i):
                    button:
                        style "empty"
                        pos (12+90*col, 180+90*row)
                        xysize (83, 85)
                        hover_background btn_hover
                        tooltip "Take off"
                        action Return(["equip", menu_items[i]])
                    
                    add "interface/topbar/icon_check.png" pos (60+90*col, 225+90*row)
                else:   
                    button:
                        style "empty"
                        pos (12+90*col, 180+90*row)
                        xysize (83, 85)
                        hover_background btn_hover
                        # tooltip "Put on"
                        action Return(["equip", menu_items[i]])
                    
                # Whoring req
                if config.developer:
                    text "{color=#b20000}"+str(menu_items[i].whoring)+"{/color}" pos (15+90*col, 180+90*row) size 20 outlines [ (1, "#000", 0, 0) ]
                if menu_items[i].incompatible != None:
                    textbutton "{color=#b20000}!{/color}":
                        pos (64+90*col, 180+90*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with:\n"+"\n".join(str(k) for k in menu_items[i].incompatible)+"\n{size=-4}{color=#009999}Above items will be unequipped.{/color}{/size}"
                        action NullAction()
                        
                # Check current item compatibility, if fails forbid equipping
                if menu_items[i].type in char_active.incompatible_wardrobe:
                    textbutton "{color=#b20000}X{/color}":
                        pos (64+90*col, 180+90*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with your current setup."
                        action NullAction()
                    
        # Add empty items
        for i in xrange(menu_items_length, items_shown):
            $ row = (i // 5) % 4
            $ col = i % 5
            button style "empty" pos (12+90*col, 180+90*row) xysize (83, 85) background "#00000033"
                    
screen t_wardrobe_outfit_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Navigational Buttons Up/Down
    if menu_items_length > 9:
        if not current_page <= 0:
            imagebutton:
                pos (xx+480, yy+190)
                idle "interface/general/"+interface_color+"/button_arrow_up.png"
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Return("dec")
        if current_page < math.ceil((menu_items_length)/10):
            imagebutton:
                pos (xx+480, yy+245)
                idle "interface/general/"+interface_color+"/button_arrow_down.png"
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Return("inc")
    
    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background
   
        add "interface/panels/"+interface_color+"/icon_panel_2.png"
            
        hbox:
            pos (24, 44)
            spacing 3
            text "[current_category]:" size 18
            text "[current_subcategory]" size 12 yalign 0.5
        
        # Page Counter
        if menu_items_length > 9:
            textbutton str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/10))+1):
                style "empty" 
                ysize 32
                pos (270, 37)
                xanchor 1.0
                background "interface/page.png"
                text_yalign 0.5
                text_first_indent 26
                action NullAction()
                
        # Add subcategory list
        for i, subcategory in enumerate(category_items):
            add "interface/wardrobe/test/icons/"+current_category+"_"+subcategory+".png" ypos 88 xpos 10+(90*i) zoom 0.2
            button:
                style "empty"
                pos (10+90*i, 86)
                xysize (86, 86)
                hover_background btn_hover
                tooltip subcategory
                action Return(["subcategory", subcategory])
        
        # Add Outfit Items
        for i in xrange(current_page*10, (current_page*10)+10):
            if i < menu_items_length:
                $ row = (i // 5) % 2
                $ col = i % 5
                
                # Preview Icon
                frame:
                    style "empty"
                    xysize (90, 180)
                    add menu_items[i].get_image() xpos 40+90*col ypos 141+180*row xalign 0.5 zoom 0.18
                    
                # Button Icons
                if current_subcategory == "Delete":
                    button:
                        style "empty"
                        pos (10+90*col, 176+180*row)
                        xysize (90, 180) 
                        hover_background "#cc330040"
                        tooltip "Delete Outfit"
                        action Return(["deloutfit", i])
                elif current_subcategory == "Load":
                    button:
                        style "empty"
                        pos (10+90*col, 176+180*row)
                        xysize (90, 180) 
                        hover_background btn_hover
                        tooltip "Equip Outfit"
                        action Return(["equip", menu_items[i]])
                elif current_subcategory == "Export&Import":
                    textbutton "Export":
                        style "empty"
                        pos (10+90*col, 176+180*row)
                        xysize (90, 180)
                        hover_background btn_hover 
                        text_color "#FFF" 
                        text_outlines [(4, "#000", 0, 0)] 
                        text_align (0.5, 0.95)
                        tooltip "Export Outfit"
                        action Return(["export", menu_items[i]])
                elif current_subcategory == "Schedule":
                    frame:
                        style "empty"
                        pos (12+90*col, 179+180*row)
                        xysize(35, 179)
                        background "#000000B3"
                        vbox:
                            spacing 5
                            xpos 5
                            for x in xrange(6):
                                $ _bg = "interface/wardrobe/test/icons/"+wardrobe_outfit_schedule[x].lower()+".png"
                                $ _bool = str(menu_items[i].schedule[x])
                                
                                if wardrobe_outfit_schedule[x] in ("Day", "Night"):
                                    $ _tooltip = "Worn during the "+wardrobe_outfit_schedule[x]+":\n{size=-4}"+_bool+"{/size}"
                                elif wardrobe_outfit_schedule[x] in ("Rainy", "Cloudy", "Snowy"):
                                    $ _tooltip = "Worn during "+wardrobe_outfit_schedule[x]+" weather:\n{size=-4}"+_bool+"{/size}"
                                else:
                                    $ _tooltip = "Worn during school events:"+"\n{size=-4}"+_bool+"{/size}"
                                    
                                button:
                                    style "empty" 
                                    xysize (25, 25) 
                                    background grayTint(_bg) 
                                    hover_background whiteTint(_bg) 
                                    selected_background _bg 
                                    tooltip _tooltip
                                    action [SelectedIf(menu_items[i].schedule[x] == True), Return(["tagoutfit", i, x])]
                    
        # Add empty items
        for i in xrange(menu_items_length, (current_page*10)+10):
            $ row = (i // 5) % 2
            $ col = i % 5
            if current_subcategory == "Save":
                textbutton "{size=50}+{/size}":
                    style "empty" 
                    pos (10+90*col, 180+180*row)
                    xysize (88, 178)
                    background "#00000033" 
                    hover_background btn_hover 
                    text_color "#FFF" 
                    text_align (0.5, 0.5)
                    tooltip "Save Outfit"
                    action Return("addoutfit")
            elif current_subcategory == "Export&Import":
                textbutton "Import":
                    style "empty"
                    pos (10+90*col, 180+180*row)
                    xysize (88, 178)
                    background "#00000033" 
                    hover_background btn_hover 
                    text_color "#FFF" 
                    text_outlines [(4, "#000", 0, 0)]
                    text_align (0.5, 0.5)
                    tooltip "Import Outfit"
                    action Return("import")
            else:
                button style "empty" pos (10+90*col, 180+180*row) xysize (88, 178) background "#00000033"
                
        # Schedule Toggle
        if current_subcategory == "Schedule":
            textbutton "{size=12}Enable scheduling{/size}":
                style "empty" 
                pos (290, 38)
                xysize (24, 68)
                background "interface/wardrobe/"+str(interface_color)+"/check_"+str(globals()[active_girl+"_outfits_schedule"])+".png"
                text_color "#FFF"
                text_pos (14, 24)
                text_yanchor 0.5 
                tooltip "{size=-4}[active_girl] will automatically wear outfits\nbased on set schedule, time of day and weather.{/size}"
                action Return("toggle_schedule") 
                
            if not globals()[active_girl+"_outfits_schedule"]:
                textbutton "Disabled":
                    style "empty" 
                    pos (10, 178)
                    xysize (447, 360)
                    background "#00000080"
                    text_color "#FFF"
                    text_align (0.5, 0.5)
                    text_size 24
                    action NullAction()  
