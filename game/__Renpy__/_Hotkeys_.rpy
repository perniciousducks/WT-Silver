#Override renpy hotkeys
# Screenshot - Prnt Scrn
# Fullscreen - F11
# Reload - shift+R
init:
    $ config.keymap['screenshot'].remove('s')
    $ config.keymap['screenshot'].append('K_PRINT')
    $ config.keymap['toggle_fullscreen'].remove('f')
    $ config.keymap['reload_game'].remove('R')
    $ config.keymap['reload_game'].append('shift_R')
    $ config.keymap['console'].append('K_BACKQUOTE')

# Initialize hotkey variables and functions
init -2 python:                
    def custom_menu(items, **kwargs):
        return renpy.display_menu(items, interact=True, screen='custom_menu')
        
    def debug():
        config.debug ^= True
        return "Debug = %s" % config.debug
        
    style.button['daybutton'].background = "#ebc275"
        
    ##############################################################################
    #Hotkeys list
    #
    #List of available inputs:
    #http://www.pygame.org/docs/ref/key.html

    hkey_map = "m"
    hkey_work = "w"
    hkey_book = "b"
    hkey_stats = "c"
    hkey_inventory = "i"
    hkey_sleep = "s"
    hkey_fap = "f"
    hkey_ui_lock = "L"
    
    hkey_hide = "h" 
    hkey_mhide = "mouseup_2"
    
    #Temp vars
    hkey_input = ""
    hkey_chat_hidden = False
    
    #Force change all default menus to use custom one w/ hotkeys
    menu = custom_menu

#Add hotkeys to main_room_menu screen (_main_room_.rpy)
screen hotkeys_main:
    if map_unlocked:
        key hkey_map action Jump("desk")
    if letter_paperwork_unlock_OBJ.read:
        key hkey_work action Jump("paperwork")
    if store_intro_done:
        key hkey_book action Jump("read_book_menu")
    key hkey_stats action [Hide("main_room_menu"), Jump("open_stat_menu")]
    key hkey_inventory action Jump("open_inventory_menu")
    key hkey_fap action Jump("jerk_off")
    
    if daytime:
        key hkey_sleep action Jump("night_start") #Skip to night
    else:
        key hkey_sleep action Jump("day_start") #Skip to next day
        
    key hkey_ui_lock action ToggleVariable("toggle_ui_lock", False, True)

#Add hotkeys to say screen (screens.rpy)
screen hotkeys_say:
    key hkey_hide action ToggleVariable("hkey_chat_hidden", False, True)
    key hkey_mhide action ToggleVariable("hkey_chat_hidden", False, True)
    
init:
    # define our styles
    style menu_choice_daybutton:
        background "#ac8d5aE6"
        hover_background "#97681f"
        insensitive_background "#d1a02eB3"
        xminimum int(config.screen_width * 0.5)
        xmaximum int(config.screen_width * 0.5)
        activate_sound "sounds/click3.mp3"
        
    style menu_choice_nightbutton:
        background "#5d5151E6"
        hover_background "#897e75"
        insensitive_background "#9e8449"
        xminimum int(config.screen_width * 0.5)
        xmaximum int(config.screen_width * 0.5)
        activate_sound "sounds/click3.mp3"
        
    style menu_choice_day:
        size 18
        xalign 0.5
        color "#f9d592"
        hover_color "#ffffff"
        insensitive_color "#444"
        outlines [ (1, "#00000080", 1, 0) ]
        
    style menu_choice_night:
        size 18
        xalign 0.5
        color "#9b8d84"
        hover_color "#ffffff"
        insensitive_color "#444"
        outlines [ (1, "#00000080", 1, 0) ]
        
    style say_who_window:
        #size 14
        #xminimum 200
        #yminimum 34
        #xfill False
        xpos 235
        #text_align 0.5
    
    style say_who_window_day:
        #size 14
        #xminimum 200
        #yminimum 34
        background "interface/frames/gold/namebox.png"
        #xfill False
        xpos 235
        text_align 0.5
        
    style say_who_window_night:
        #size 14
        #xminimum 200
        #yminimum 34
        background "interface/frames/gray/namebox.png"
        xfill False
        xpos 235
        text_align 0.5
        
    style say_two_window_vbox:
        yalign 1.0

#Custom menu w/ hotkeys    
screen custom_menu(items, hotkeys=True):
    zorder 7
    
    add "interface/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign menu_y

        vbox:
            style "menu"
            spacing 1
            
            #Count from here
            $ hkey = 0

            for caption, action, chosen in items:
                
                $ hkey += 1

                if action:

                    button:
                        action action
                        if daytime:
                            style "menu_choice_daybutton"
                        else:
                            style "menu_choice_nightbutton"
                        
                        #Dont add a number if choice number is higher than number of available hotkeys
                        #Add a SHIFT modifier maybe?
                        if hkey < 10:
                            if daytime:
                                text "[hkey]. " + caption style "menu_choice_day"
                            else:
                                text "[hkey]. " + caption style "menu_choice_night"
                        else:
                            if daytime:
                                text caption style "menu_choice_day"
                            else:
                                text caption style "menu_choice_night"
                        
                    #Dont add a hotkey if choice number is higher than number of available hotkeys
                    #Add a SHIFT modifier maybe?
                    if hkey < 10:
                        key str(hkey) action action
                        key "K_KP"+str(hkey) action action #Numpad
                        

                else:
                    if daytime:
                        text caption style "menu_choice_day"
                    else:
                        text caption style "menu_choice_night"