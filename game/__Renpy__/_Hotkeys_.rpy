#Override renpy hotkeys
# Screenshot - Prnt Scrn
# Fullscreen - F11
# Reload - shift+R
init python:
    config.keymap['screenshot'].remove('s')
    config.keymap['screenshot'].append('K_PRINT')
    config.keymap['toggle_fullscreen'].remove('f')
    config.keymap['reload_game'].remove('R')
    config.keymap['reload_game'].append('shift_R')
    config.keymap['console'].append('K_BACKQUOTE')

    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['hide_windows'].remove('h')
    # config.keymap['hide_windows'].remove('joy_hide')

    # Initialize hotkey variables and functions
    # List of available inputs: http://www.pygame.org/docs/ref/key.html
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

# Add hotkeys to main_room screen (_main_room_.rpy)
screen hotkeys_main():
    tag hotkeys_main

    if map_unlocked:
        key hkey_map action Jump("desk")
    if letter_min_work.read:
        key hkey_work action Jump("paperwork")
    if store_intro_done:
        key hkey_book action Jump("read_book_menu")
    key hkey_stats action Jump("stats_menu")
    key hkey_inventory action Jump("inventory_menu")
    key hkey_fap action Jump("jerk_off")

    if daytime:
        key hkey_sleep action Jump("night_start") #Skip to night
    else:
        key hkey_sleep action Jump("day_start") #Skip to next day

    key hkey_ui_lock action ToggleVariable("toggle_ui_lock", False, True)

# Add hotkeys to say screen (screens.rpy)
screen hotkeys_say():
    tag hotkeys_say
    if renpy.variant('android'):
        key "game_menu" action ToggleVariable("hkey_chat_hidden", False, True)
    else:
        key hkey_hide action ToggleVariable("hkey_chat_hidden", False, True)
        key hkey_mhide action ToggleVariable("hkey_chat_hidden", False, True)
