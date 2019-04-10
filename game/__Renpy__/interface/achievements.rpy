init python:
    #if persistent.achievements == None:
    persistent.achievements = {"firsttime": ["General", "Popped my cherry", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla finibus eleifend blandit. Aliquam viverra augue a Sed ornare vitae velit et molestie. Curabitur et auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla finibus eleifend blandit. Aliquam viverra augue a Sed ornare vitae velit et molestie. Curabitur et auctor. Lorem ipsum dolor sit amet.", False, "interface/icons/book_galadriel_1.png"],
                               "unlockher": ["Characters", "Granger Danger", "Rewarded for unlocking Hermione.", False, "interface/icons/head/head_hermione_2.png"],
                               "unlockcho": ["Characters", "Ming Dynasty", "Rewarded for unlocking Cho.", False, "interface/icons/head/head_cho_2.png"],
                               "unlocklun": ["Characters", "Looney Tunes", "Rewarded for unlocking Luna.", False, "interface/icons/head/head_luna_2.png"],
                               "unlockast": ["Characters", "Greenpeas", "Rewarded for unlocking Astoria.", False, "interface/icons/head/head_astoria_2.png"],
                               "unlockton": ["Characters", "Nymphadoreador", "Rewarded for unlocking Tonks.", False, "interface/icons/head/head_tonks_1.png"],
                               "unlocksus": ["Characters", "Boner", "Rewarded for unlocking Susan.", False, "interface/icons/head/head_susan_2.png"],
                               "mirror": ["General", "Mirror, mirror on the wall..", "Rewarded for unlocking Room of Requirements.", False, "images/rooms/room_of_requirement/mirror_hover.png"],
                               "gold": ["General", "Gold Digger", "Rewarded for collecting 10000 gold coins.", False, "interface/icons/gold.png"],
                               "drunkard": ["General", "Drunken Master", "Collected 25 bottles of wine.", False, "interface/icons/item_wine.png"],
                               "workaholic": ["General", "Workaholic", "Completed 100 reports.", False, "interface/icons/item_scroll.png"],
                               "fireplace": ["General", "Feel the Heat", "Used the fireplace at least 5 times.", False, None],
                               "peta": ["General", "Not another movement..", "Rewarded for not feeding the bird for 50 days in a row.\n{size=-4}Disclaimer: No real nor fictional animals were harmed in the process.{/size}", False, "images/rooms/_objects_/phoenix/phoenix_01.png"],
                               "petpal": ["General", "Petpal", "Rewarded for feeding the bird for 50 days in a row.", False, "images/rooms/_objects_/phoenix/phoenix_01.png"],
                               "postman": ["General", "Postman", "Bought all posters from the token shop.", False, "interface/icons/posters/agrabah.png"],
                               "hats": ["General", "Mad Hatter", "Bought all hat decorations from the token shop.", False, "interface/icons/icon_gambler_hat.png"],
                               "daddy": ["Characters", "Whos your daddy?", "Be called a daddy at least once.", False, "interface/icons/head/head_hermione_2.png"],
                               "wanker": ["General", "Wanker", "Rubbed one out during a very lonely night.", False, "images/animation/06_jerking_02.png"],
                               "bros": ["Characters", "Bros before hoes", "Became good friends with Snape.", False, "characters/snape/head/head_9.png"],
                               "spoiler": ["Characters", "\"Spoiler\"", "My boner just died..", False, "characters/snape/head/head_14.png"],
                               "knock": ["General", "*Knock* *knock*", "Who's there?", False, "images/rooms/_objects_/doors/door_idle.png"],
                               "decorator": ["General", "Decorator", "Applied decoration in the office.", False, "interface/icons/trophies/stag.png"]}
                                 
    class achievement_class(object):
        achievements = {}
    
        def __init__(self):
            self.achievements = persistent.achievements
            
        def unlock(self, id):
            try:
                if persistent.achievements[id][3] == False:
                    self.achievements[id][3] = True
                    persistent.achievements[id][3] = True
                    renpy.show_screen("achievement_window", persistent.achievements[id][1], persistent.achievements[id][4])
            except KeyError:
                return
            
        def lock(self, id):
            self.achievements[id][3] = False
            persistent.achievements[id][3] = False
            
    def achievement_sortfilter(item, sortby="A-z", filtering=None):
        if filtering == "Locked":
            item = filter(lambda x: 'True' in str(x[1][3]), item)
        elif filtering == "Unlocked":
            item = filter(lambda x: 'False' in str(x[1][3]), item)
            
        if sortby == "z-A":
            item = sorted(item, key=lambda x: x[1][1], reverse=True)
        elif current_sorting == "Unlocked":
            item = sorted(item, key=lambda x: 'True' in str(x[1][3]), reverse=True)
        elif current_sorting == "Locked":
            item = sorted(item, key=lambda x: 'True' in str(x[1][3]))
        else:
            item = sorted(item, key=lambda x: x[1][1])
        return item
            
init:
    $ achievement = achievement_class()

screen achievement_window(string="", icon=None, xpos=0, ypos=60):
    tag popup_window
    zorder 100
    
    frame:
        style "empty"
        at popup_animation(time=19.0, xx=-410)
        pos (xpos, ypos)
        xsize 410 
        ysize 96
        
        add "interface/achievements/"+interface_color+"/box.png"
        if icon:
            frame:
                style "empty"
                pos (6, 6)
                xsize 84
                ysize 84
                $ image_zoom = crop_image_zoom(icon, 84, 84)
                add image_zoom[0] zoom image_zoom[1] align (0.5, 0.5)
        add "interface/achievements/glass.png"
        
        vbox:
            spacing 10
            pos (136, 12)
            text "Achievement unlocked!" size 18 xalign 0.5
            text string size 14 xalign 0.5
    timer 20.0 action Hide("achievement_window")
    
transform rotate_circular():
    subpixel True
    
    on show, appear, start:
        rotate 0
        linear 5.0 rotate 360
        repeat
    
####################################
############# Menu #################
####################################
    
label achievement_menu(xx=150, yy=90):
    
    $ hide_transitions = True
    
    # Styling
    if daytime:
        $ btn_hover = "#e3ba7140"
    else:
        $ btn_hover = "#7d75aa40"
    
    $ achievement_categories_sorted = ["All", "General", "Characters"]
    $ achievement_categories_sorted_length = len(achievement_categories_sorted)
    
    $ items_shown = 36
    $ current_page = 0
    $ current_item = None
    $ current_category = achievement_categories_sorted[0]
    $ current_filter = None
    $ current_sorting = "A-z"
    
    $ category_items = list(persistent.achievements.iteritems())
    $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
    $ menu_items_length = len(menu_items)

    label achievement_menu_after_init:
    
    show screen bld1
    show screen achievement_menu(xx, yy)
    show screen achievement_menuitem(xx, yy)
    
    $ _return = ui.interact()
    
    hide screen bld1
    hide screen achievement_menu
    hide screen achievement_menuitem
    
    if _return[0] == "select":
        $ current_item = _return[1]
    elif _return[0] == "category":
        $ current_category = _return[1] 
        if current_category == "All":
            $ category_items = list(persistent.achievements.iteritems())
        else:
            $ category_items = filter(lambda x: current_category in x[1][0], list(persistent.achievements.iteritems()))
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
        pass
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1
    elif _return == "filter":
        if current_filter == None:
            $ current_filter = "Locked"
        elif current_filter == "Locked":
            $ current_filter = "Unlocked"
        else:
            $ current_filter = None
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
    elif _return == "sort":
        if current_sorting == "A-z":
            $ current_sorting = "z-A"
        elif current_sorting == "z-A":
            $ current_sorting = "Unlocked"
        elif current_sorting == "Unlocked":
            $ current_sorting = "Locked"
        else:
            $ current_sorting = "A-z"
        $ menu_items = achievement_sortfilter(category_items, current_sorting, current_filter)
        $ menu_items_length = len(menu_items)
        $ current_page = 0
        $ current_item = None
    else:
        $ hide_transitions = False
        jump day_main_menu
    
    jump achievement_menu_after_init
    
screen achievement_menu(xx, yy):
    tag achievement_menu
    zorder 4
    
    use top_bar_close_button
    
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"
        
        vbox:
            pos (6, 41)
            for i in xrange(0, achievement_categories_sorted_length):
                vbox:
                    if current_category == achievement_categories_sorted[i]:
                        textbutton achievement_categories_sorted[i] xsize 195 ysize 16 style "empty" background "interface/achievements/"+interface_color+"/highlight_left.png" text_xalign 0.5
                    else:
                        textbutton achievement_categories_sorted[i] xsize 195 ysize 16 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left.png" text_xalign 0.5 action Return(["category", achievement_categories_sorted[i]])
                    add "interface/achievements/"+interface_color+"/spacer_left.png"
        vbox:
            pos (6, 384)
            textbutton "Filter: [current_filter]" style "empty" xsize 195 ysize 32 text_align (0.5, 0.5) text_size 12 hover_background btn_hover action Return("filter")
            textbutton "Sort by: [current_sorting]" style "empty" xsize 195 ysize 32 text_align (0.5, 0.5) text_size 12 hover_background btn_hover action Return("sort")
        
screen achievement_menuitem(xx, yy):
    tag achievement_menuitem
    zorder 4
    
    frame:
        style "empty"
        pos (xx+217, yy-53)
        xsize 560
        ysize 507
        
        add "interface/achievements/"+interface_color+"/panel.png"
        
        text "Achievements" size 22 xalign 0.5 ypos 65
        
        text "Unlocked: "+str(len(filter(lambda x: 'True' in str(x[1][3]), menu_items)))+"/[menu_items_length]" size 12 pos (24, 70)
        
        # Page counter
        if menu_items_length > items_shown:
            hbox:
                xanchor 1.0
                pos (540, 24)
                spacing 5
                add "interface/page.png" yanchor 0.5 ypos 53
                text str(current_page+1)+"/"+str(int(math.ceil(menu_items_length/items_shown))+1) ypos 44 size 16
            vbox:
                pos (570, 186)
                spacing 10
                
                imagebutton:
                    idle "interface/frames/"+interface_color+"/arrow_up.png"
                    if not current_page <= 0:
                        hover image_hover("interface/frames/"+interface_color+"/arrow_up.png")
                        action Return("dec")
                    
                imagebutton:
                    idle im.Flip("interface/frames/"+interface_color+"/arrow_up.png", vertical=True)
                    if current_page < math.ceil((menu_items_length-1)/items_shown):
                        hover im.Flip(image_hover("interface/frames/"+interface_color+"/arrow_up.png"), vertical=True)
                        action Return("inc")
        
        # Add items
        for i in xrange(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < menu_items_length:
                $ row = (i // 9) % 4
                $ col = i % 9
                frame:
                    style "empty"
                    xsize 48
                    ysize 48
                    pos (24+58*(col), 113+58*(row)) 
                    add "interface/achievements/"+interface_color+"/iconbox.png"
                    if current_item and current_item[0] == menu_items[i][0]:
                        add "interface/achievements/glow.png" align (0.5, 0.5) zoom 0.105 alpha 0.7 at rotate_circular
                    if menu_items[i][1][4]:
                        if menu_items[i][1][3]:
                            $ image_zoom = crop_image_zoom(menu_items[i][1][4], 42, 42)
                        else:
                            $ image_zoom = crop_image_zoom(menu_items[i][1][4], 42, 42, True)
                        add image_zoom[0] zoom image_zoom[1] align (0.5, 0.5)
                    add "interface/achievements/glass_iconbox.png" pos (3, 2)
                    button xsize 46 ysize 46 style "empty" hover_background btn_hover action Return(["select", menu_items[i]])
                    
        # Add empty items
        #for i in xrange(menu_items_length, items_shown):
            #$ row = (i // 9) % 4
            #$ col = i % 9
            #button xsize 48 ysize 48 style "empty" background "#00000033" xpos 24+58*(col) ypos 113+58*(row)
            
        if current_item:
            frame:
                style "empty"
                xsize 96
                ysize 96
                pos (24, 375)
                add "interface/achievements/"+interface_color+"/icon_selected.png"
                if current_item[1][4]:
                    if current_item[1][3]:
                        $ image_zoom = crop_image_zoom(current_item[1][4], 84, 84)
                    else:
                        $ image_zoom = crop_image_zoom(current_item[1][4], 84, 84, True)
                    add image_zoom[0] zoom image_zoom[1] align (0.5, 0.5)
                add "interface/achievements/glass_selected.png" pos (6, 6)
                
            add "interface/achievements/"+interface_color+"/highlight.png" pos (112, 375)
            add "interface/achievements/"+interface_color+"/spacer.png" pos (120, 398)
            hbox:
                spacing 5
                xalign 0.5
                text current_item[1][1] ypos 380 size 16 xoffset 45
                add "interface/unlocked_"+str(current_item[1][3])+".png" xoffset 45 ypos 377 
            hbox:
                pos (132, 407)
                xsize 410
                text current_item[1][2] size 12