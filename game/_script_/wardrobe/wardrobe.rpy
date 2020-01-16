default wardrobe_background_day = "#e8c97e"
default wardrobe_background_night = "#7d756e"

default wardrobe_toggles = False
default wardrobe_music = False
default wardrobe_chitchats = True
default wardrobe_requirements = False

label wardrobe(char_label):
    python:
        # TODO: Streamline and unify whoring variables.
        _char_var_list = {
            "hermione": her_whoring,
            "tonks": ton_friendship,
            "astoria": ast_affection,
            "cho": cho_whoring
            }
            
        char_active = eval(active_girl)
        char_nickname = char_active.name
        char_scale = 1.0/globals()[active_girl+"_scaleratio"]
        char_level = _char_var_list[active_girl]
        hide_transitions = True
        
        renpy.start_predict("interface/wardrobe/*.png")
        predict = tuple(x.get_image() for x in char_active.wardrobe_list)
        renpy.start_predict(*predict)

        wardrobe_background = wardrobe_background_day if interface_color == "gold" else wardrobe_background_night
        
        items_shown = 20
        current_page = 0
        current_category = ""
        current_subcategory = ""
        current_item = None
        wardrobe_categories_sorted = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
        wardrobe_categories = char_active.wardrobe
        export_in_progress = False
        item_to_export = None
        wardrobe_outfit_schedule = ("Day", "Night", "Cloudy", "Rainy", "Snowy", "School")

        character_toggles = [(k, v[1]) for k, v in char_active.clothes.iteritems() if k != "hair" and not any(i.isdigit() for i in k)]
        character_toggles.extend([("tattoo", 30), ("piercing", 31), ("makeup", 32), ("accessory", 33)])
        character_toggles.sort(key=lambda x: x[1], reverse=True)
        
        renpy.hide_screen(active_girl+"_main")
        
        # Forbid rollback to avoid bugs and unintended actions
        config.rollback_enabled = False
    
    if wardrobe_music:
        call play_music("wardrobe")
        
    if not renpy.variant("android"):
        show screen mouse_tooltip
    
    label .after_init:
    
    show screen wardrobe_menu(550, 50)
    
    if current_category:
        if current_category == "outfits":
            show screen wardrobe_outfit_menuitem(20, 50)
        else:
            show screen wardrobe_menuitem(20, 50)
    
    $ _return = ui.interact()
    
    hide screen wardrobe_menu
    hide screen wardrobe_menuitem
    hide screen wardrobe_outfit_menuitem
    
    if _return == "tabswitch":
        show screen wardrobe_menu(550, 50)
        $ renpy.call(active_girl+"_wardrobe_check", _return)
        if _return in (None, True):
            $ current_page = 0
            $ current_category = ""
            $ current_subcategory = ""
            $ current_item = None
            $ renpy.play('sounds/click3.mp3')
            if "head" in wardrobe_categories_sorted:
                $ wardrobe_categories_sorted = ("face", "torso", "hips", "legs", "makeup", "breasts", "pelvis", "misc")
                $ char_active.strip("top", "bottom", "robe", "bra", "panties")
            else:
                $ wardrobe_categories_sorted = ("head", "tops", "bottoms", "legwear", "makeup", "bras", "panties", "misc")
                $ char_active.wear("top", "bottom", "robe", "bra", "panties")
    elif _return == "studio":
        $ renpy.play('sounds/click3.mp3')
        call studio(char_label)
    elif _return[0] == "equip":
        show screen wardrobe_menu(550, 50)
        if isinstance(_return[1], DollCloth) and char_active.is_blacklisted(_return[1].type):
            $ renpy.play('sounds/fail.mp3')
        else:
            $ renpy.call(active_girl+"_wardrobe_check", "equip", _return[1])
        $ char_active.reset_blacklist()
    elif _return == "addoutfit":
        $ char_active.create_outfit()
        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
        $ menu_items_length = len(menu_items)
    elif _return[0] == "deloutfit":
        $ char_active.outfits.pop(_return[1])
        $ char_active.update_outfits_schedule(all=True)
        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
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
        $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
        $ menu_items_length = len(menu_items)
    elif _return[0] == "item_color":
        $ active_layer = _return[1]
        show screen wardrobe_menu(550, 50)
        $ current_item.set_color(active_layer)
        $ active_layer = None
    elif _return == "item_reset":
        $ current_item.reset_color()
    elif _return == "bg_color":
        $ active_layer = None
        show screen wardrobe_menu(550, 50)
        $ wardrobe_background = color_picker(get_rgb_list(wardrobe_background), False, "Wardrobe Background Color", pos_xy=[40, 85])
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
                $ menu_items = filter(lambda x: x.unlocked==True, char_active.outfits)
                $ menu_items_length = len(menu_items)
            else:
                if current_category in ("bras", "panties"):
                    $ char_active.strip("top", "bottom", "robe")
                else:
                    if 'head' in wardrobe_categories_sorted:
                        $ char_active.wear("top", "bottom", "robe")
                $ category_items = wardrobe_categories.get(current_category)
                # Default subcategory
                if category_items:
                    $ current_subcategory = category_items.keys()[0]
                    $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
                else:
                    $ category_items = []
                    $ current_subcategory = "No items available"
                    $ menu_items = []
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if char_active.clothes[item.type][0] and item.id == char_active.clothes[item.type][0].id:
                            current_item = item
                            break
    elif _return[0] == "subcategory":
        if current_subcategory != _return[1]:
            $ renpy.play('sounds/scroll.mp3')
            $ current_subcategory = _return[1]
            if current_category != "outfits":
                $ current_page = 0
                $ menu_items = filter(lambda x: x.unlocked==True, category_items.get(current_subcategory))
                $ menu_items_length = len(menu_items)
                # Default selected item
                $ current_item = None
                python:
                    for item in menu_items:
                        if char_active.clothes[item.type][0] and item.id == char_active.clothes[item.type][0].id:
                            current_item = item
                            break
    elif _return[0] == "erozone":
        show screen wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen wardrobe_outfit_menuitem(20, 50)
            else:
                show screen wardrobe_menuitem(20, 50)
        $ renpy.call(active_girl+"_wardrobe_check", "touching", _return[1])
    elif _return[0] == "toggle":
        show screen wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen wardrobe_outfit_menuitem(20, 50)
            else:
                show screen wardrobe_menuitem(20, 50)
        $ renpy.call(active_girl+"_wardrobe_check", "toggle", _return[1])
    elif _return == "toggle_schedule":
        $ globals()[active_girl+"_outfits_schedule"] = not globals()[active_girl+"_outfits_schedule"]
    elif _return == "music":
        show screen wardrobe_menu(550, 50)
        if current_category:
            if current_category == "outfits":
                show screen wardrobe_outfit_menuitem(20, 50)
            else:
                show screen wardrobe_menuitem(20, 50)
        if wardrobe_music:
            $ wardrobe_music = False
            call play_music(active_girl)
            call expression char_label pass (text="", face="annoyed")
        else:
            $ wardrobe_music = True
            call play_music("wardrobe")
            call expression char_label pass (text="", face="happy")
    else: #_return == "Close":
        $ config.rollback_enabled = True
        $ renpy.play('sounds/door2.mp3')
        $ hide_transitions = False
        $ char_active.wear("all")
        #$ char_active.clothes_compatible()
        if wardrobe_music:
            call play_music(active_girl)
        $ renpy.stop_predict("interface/wardrobe/*.png")
        $ renpy.stop_predict(*predict)
        return
    jump .after_init
        
screen wardrobe_menu(xx, yy):
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
                add "interface/wardrobe/{}/frame.png".format(interface_color) xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/icons/{}/categories/{}.png".format(active_girl, category) xpos 14+411*cat_row ypos 80+110*cat_col zoom 0.5
                button:
                    style "empty"
                    pos (14+411*cat_row, 80+110*cat_col)
                    xysize (90, 96)
                    hover_background btn_hover
                    action Return(["category", category])
            else:
                add "interface/wardrobe/{}/frame.png".format(interface_color) xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
                add "interface/wardrobe/icons/{}/categories/{}.png".format(active_girl, category) xpos 61+329*cat_row ypos 80+110*cat_col zoom 0.5
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
        add "interface/frames/{}/circle.png".format(interface_color) pos (373, 62)
        button:
            style "empty"
            pos (373, 62)
            xysize (50, 50)
            background "interface/wardrobe/switch.png"
            hover_background image_hover("interface/wardrobe/switch.png")
            tooltip "Switch tabs"
            action Return("tabswitch")

        # Outfits Manager
        add "interface/frames/{}/circle.png".format(interface_color) pos (373, 117)
        button:
            style "empty"
            pos (373, 117)
            xysize (50, 50)
            background "interface/wardrobe/outfits.png"
            hover_background image_hover("interface/wardrobe/outfits.png")
            tooltip "Outfits Manager"
            action Return(["category", "outfits"])

        # Studio
        if not renpy.variant('android'):
            add "interface/frames/{}/circle.png".format(interface_color) pos (373, 172)
            button:
                style "empty"
                pos (373, 172)
                xysize (50, 50)
                background "interface/wardrobe/studio.png"
                hover_background image_hover("interface/wardrobe/studio.png")
                tooltip "Open Studio"
                action Return("studio")

        add "interface/panels/{}/wardrobe_panel.png".format(interface_color)
        
        #Easter Egg
        vbox:
            xalign 0.5
            ypos 260
            spacing 72
            button style "empty" xysize (120, 60) action Return(["erozone", "boobs"])
            button style "empty" xysize (120, 50) action Return(["erozone", "pussy"])
        
        # Toggles and User Settings
        use dropdown_menu(name="Toggles", pos=(116, 29), items_offset=(-5, 2)):
            for item in character_toggles:
                $ _item = item[0]
                $ _is_worn = char_active.is_worn(_item)
                $ _is_equipped = True if _is_worn in (True, False) else False
                textbutton "[_item]":
                    style interface_style+"_dropdown"
                    background "interface/frames/{}/check_{}.png".format(interface_color, _is_worn)
                    tooltip "Show/hide "+str(_item)
                    action [SensitiveIf(_is_equipped), Return(["toggle", _item])]
        use dropdown_menu(name="Options", pos=(350, 29), items_offset=(-59, 2)):
            textbutton "Music":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.png".format(interface_color, wardrobe_music)
                tooltip "Toggle music"
                action Return("music")
            textbutton "Background":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_true.png".format(interface_color)
                tooltip "Change background colour"
                action Return("bg_color")
            textbutton "Chit-chats":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.png".format(interface_color, wardrobe_chitchats)
                tooltip "Toggle character chit-chats"
                action ToggleVariable("wardrobe_chitchats", True, False)
            textbutton "Requirements":
                style interface_style+"_dropdown"
                background "interface/frames/{}/check_{}.png".format(interface_color, wardrobe_requirements)
                tooltip "Toggle level requirements display"
                action ToggleVariable("wardrobe_requirements", True, False)
                
        # Zoom slider
        # bar:
            # area (25, 290, 255, 30)
            # value VariableValue("char_scale", range=1.0, step=0.01, style=u'bar')
            # top_gutter 0
            # bottom_gutter 0
                
        add "interface/general/{}/button_wide.png".format(interface_color) pos (200, -4)
        text char_nickname xalign 0.5 ypos 4 size 16
        
screen wardrobe_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    # Navigational Buttons Up/Down
    if menu_items_length > items_shown:
        imagebutton:
            pos (xx+480, yy+190)
            idle "interface/general/{}/button_arrow_up.png".format(interface_color)
            if not current_page <= 0:
                hover "interface/general/{}/button_arrow_up_hover.png".format(interface_color)
                action Return("dec")

        imagebutton:
            pos (xx+480, yy+245)
            idle "interface/general/{}/button_arrow_down.png".format(interface_color)
            if current_page < math.ceil((menu_items_length-1)/items_shown):
                hover "interface/general/{}/button_arrow_down_hover.png".format(interface_color)
                action Return("inc")
    
    frame:
        style "empty"
        pos (xx, yy)
        xysize (467, 548)
        background wardrobe_background
   
        add "interface/panels/{}/icon_panel_1.png".format(interface_color)
        
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
                        background Color(tuple(current_item.color[i]))
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
                add "interface/wardrobe/icons/{}/{}_{}.png".format(active_girl, current_category, subcategory) ypos 86 xpos 10+(90*i) zoom 0.2
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
                if char_active.clothes[menu_items[i].type][0] and menu_items[i].id == char_active.clothes[menu_items[i].type][0].id:
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
                if wardrobe_requirements:
                    if menu_items[i].level > her_whoring:
                        textbutton str(menu_items[i].level):
                            style "empty"
                            pos (15+90*col, 180+90*row)
                            text_size 20
                            text_outlines [ (1, "#000", 0, 0) ]
                            text_color "#b20000"
                            tooltip ("{color=#35aae2}[active_girl]'s{/color} level is too low to wear that." if not active_girl.endswith("s") else "{color=#35aae2}[active_girl]'{/color} level is too low to wear that.")
                            action NullAction()
                # Check current item compatibility, if fails forbid equipping
                if char_active.is_blacklisted(menu_items[i].type):
                    textbutton "{color=#b20000}X{/color}":
                        pos (64+90*col, 180+90*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with your current setup."
                        action NullAction()
                elif menu_items[i].blacklist != None:
                    textbutton "{color=#b20000}!{/color}":
                        pos (64+90*col, 180+90*row)
                        background None
                        text_size 20
                        text_outlines [ (1, "#000", 0, 0) ]
                        tooltip "Incompatible with:\n{color=#35aae2}"+"\n".join(str(k) for k in menu_items[i].blacklist)+"{/color}\n{size=-4}{color=#e4cb35}Above items will be unequipped.{/color}{/size}"
                        action NullAction()
                # if menu_items[i].modpath:
                    # textbutton "{color=#00b200}M{/color}":
                        # style "empty"
                        # pos (15+90*col, 240+90*row)
                        # background None
                        # text_size 20
                        # text_outlines [ (1, "#000", 0, 0) ]
                        # tooltip "This item is a part of a mod."
                        # action NullAction()
                    
        # Add empty items
        for i in xrange(menu_items_length, items_shown):
            $ row = (i // 5) % 4
            $ col = i % 5
            button style "empty" pos (12+90*col, 180+90*row) xysize (83, 85) background "#00000033"
                    
screen wardrobe_outfit_menuitem(xx, yy):
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
            add "interface/wardrobe/icons/"+current_category+"_"+subcategory+".png" ypos 88 xpos 10+(90*i) zoom 0.2
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
                    button:
                        style "empty"
                        pos (10+90*col, 176+180*row)
                        xysize (90, 180)
                        hover_background btn_hover 
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
                                $ _bg = "interface/wardrobe/icons/"+wardrobe_outfit_schedule[x].lower()+".png"
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
            $ n = i+1
            if current_subcategory == "Save":
                textbutton "Save\n{size=-5}Slot [n]{/size}":
                    style interface_style+"_menu"
                    pos (10+90*col, 180+180*row)
                    xysize (88, 178)
                    background "#00000033" 
                    hover_background btn_hover 
                    text_align (0.5, 0.5)
                    action Return("addoutfit")
            elif current_subcategory == "Export&Import":
                textbutton "Import\n{size=-5}Slot [n]{/size}":
                    style interface_style+"_menu"
                    pos (10+90*col, 180+180*row)
                    xysize (88, 178)
                    background "#00000033" 
                    hover_background btn_hover
                    text_align (0.5, 0.5)
                    action Return("import")
            else:
                button style "empty" pos (10+90*col, 180+180*row) xysize (88, 178) background "#00000033"
                
        # Schedule Toggle
        if current_subcategory == "Schedule":
            textbutton "Outfit scheduling":
                style interface_style+"_dropdown"
                pos (290, 42)
                background "interface/frames/"+str(interface_color)+"/check_"+str(globals()[active_girl+"_outfits_schedule"])+".png"
                tooltip "{color=#35aae2}[active_girl]{/color} will automatically wear outfits\nbased on set schedule, time of day and weather."
                action Return("toggle_schedule") 
                
            if not globals()[active_girl+"_outfits_schedule"]:
                textbutton "Disabled":
                    style interface_style+"_menu"
                    pos (10, 178)
                    xysize (447, 360)
                    background "#00000080"
                    text_align (0.5, 0.5)
                    text_size 24
                    action NullAction()  
