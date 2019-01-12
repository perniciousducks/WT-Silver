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

# Initialize hotkey variables and functions
init -2 python:                
    def custom_menu(items, **kwargs):
        return renpy.display_menu(items, interact=True, screen='custom_menu')
        
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

#Add hotkeys to say screen (screens.rpy)
screen hotkeys_say:
    key hkey_hide action ToggleVariable("hkey_chat_hidden", False, True)
    key hkey_mhide action ToggleVariable("hkey_chat_hidden", False, True)

#Custom legacy menu w/ hotkeys    
screen custom_menu(items):
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
                        style "menu_choice_button"
                        
                        #Dont add a number if choice number is higher than number of available hotkeys
                        #Add a SHIFT modifier maybe?
                        if hkey < 10:
                            text "[hkey]. " + caption style "menu_choice"
                        else:
                            text caption style "menu_choice"
                        
                    #Dont add a hotkey if choice number is higher than number of available hotkeys
                    #Add a SHIFT modifier maybe?
                    if hkey < 10:
                        key str(hkey) action action
                        key "K_KP"+str(hkey) action action #Numpad
                        

                else:
                    text caption style "menu_caption"