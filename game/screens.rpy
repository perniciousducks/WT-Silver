# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
    
screen say(who, what, side_image=None):
    zorder 6 #Otherwise the character sprite would be obscuring it.
    
    if side_image:
        add side_image yalign 1.0 yanchor 1.0
    else:
        add SideImage() xalign 0.0 yalign 1.0 yanchor 1.0

    #Hotkeys
    use hotkeys_say
    
    #Add "hidden" window
    if hkey_chat_hidden:
        window:
            xalign 0.5
            yalign 0.99
            if daytime and not persistent.nightmode:
                style "say_who_window_day"
                text "Hidden" color persistent.text_color_day outlines [ (1, persistent.text_outline, 1, 0) ] bold False text_align 0.5 xalign 0.5 yalign 0.5
            else:
                style "say_who_window_night"
                text "Hidden" color persistent.text_color_night outlines [ (1, persistent.text_outline, 1, 0) ] bold False text_align 0.5 xalign 0.5 yalign 0.5
            if who:
                text who id "who" ypos 1000
            text what id "what" ypos 1000
            
        #Add fullscreen CTC button
        button:
            action SetVariable("hkey_chat_hidden", False)
            style "empty"
    else:
        if who:
            window:
                ypos 470
                if daytime and not persistent.nightmode:
                    style "say_who_window_day"
                    text who id "who" color persistent.text_color_day outlines [ (1, persistent.text_outline, 1, 0) ] bold False text_align 0.5 xalign 0.5 yalign 0.5
                else:
                    style "say_who_window_night"
                    text who id "who" color persistent.text_color_night outlines [ (1, persistent.text_outline, 1, 0) ] bold False text_align 0.5 xalign 0.5 yalign 0.5
        window id "window":
            has vbox#:
                #style "say_vbox"            
            if daytime and not persistent.nightmode:
                text what id "what" color persistent.text_color_day outlines [ (1, persistent.text_outline, 1, 0) ]
            else:
                text what id "what" color persistent.text_color_night outlines [ (1, persistent.text_outline, 1, 0) ]

    # Use the quick menu.
    if not hkey_chat_hidden and not who == None:
        use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    add "interface/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign menu_y

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"
    zorder 7

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input
    
screen input(prompt):
    tag input
    zorder 15 #Always on top
    
    button:
        xsize 1080
        ysize 600
        action NullAction()
        style "empty"
        
    window:
        id "window"
        
        has vbox:
            style "say_vbox"
        
        text prompt
        input id "input"
        
    #use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):
    zorder 7
    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu



# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu


# Main Menu
screen main_menu():
    tag menu
    zorder 5

    # The background of the main menu.
    window:
        style "mm_root"
    
    # Version display
    $ ver = config.version[:4]+"."+config.version[4:6] if len(config.version) >=5 else config.version
    text "{color=#fff}{size=-2}[ver]{/size}{/color}" xpos 1024 ypos 228 outlines [ (1, "#000", 0, 0) ]
    text "{color=#c70000}EXPERIMENTAL VERSION{/color}" xpos 10 yalign 0.01 size 24 outlines [(2, "#000", 0, 0)]
    text "Expect bugs, crashes and other weird stuff.\nProceed at your own risk, you have been warned!" xpos 10 yalign 0.05 color "#fff" size 12 outlines [(2, "#000", 0, 0)]
    text "You can find most recent stable build on our {a=https://pastebin.com/6zbuZ5gS}pastebin{/a}." xpos 10 yalign 0.15 color "#fff" size 12 outlines [(2, "#000", 0, 0)]
    
    if update_available:        
        frame:
            style_group "mm"
            xalign .96
            yalign .575

            has vbox

            textbutton _("{size=-6}{color=#7a0000}UPDATE AVAILABLE{/color}{/size}") action OpenURL("https://pastebin.com/6zbuZ5gS")

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .96
        yalign .75

        has vbox

        if not persistent.game_complete:
            textbutton _("New Game") action Start()
        else:
            textbutton _("New Game {size=+3}+{/size}") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm=False)

    frame:
        style_group "mm"
        xalign .96
        yalign .86

        has vbox

        textbutton _("Credits") action Jump("credits")
        
    imagebutton:
        xpos 910
        ypos 560
        xalign 0.5
        yalign 0.5
        idle "logo/patreon.png"
        hover "logo/patreon_hover.png"
        action OpenURL("https://www.patreon.com/SilverStudioGames")
        
    imagebutton:
        xpos 660
        ypos 562
        xalign 0.5
        yalign 0.5
        idle "logo/discord.png"
        hover "logo/discord_hover.png"
        action OpenURL("https://discord.gg/7PD57yt")
    
    #New info
    #add "logo/arrow.png" xpos 760 ypos 500
    #text "{color=#b20000}{size=+10}NEW\nPATREON!{/size}{/color}" xpos 700 ypos 445 outlines [ (3, "#000", 0, 0) ]
    
    if check_for_old_files():
        frame:
            style "empty"
            background "#000"
            xsize 1080
            ysize 600
            button style "empty" action NullAction()
            add "images/misc/old.png" yanchor 1.0 yalign 0.99 xpos 10
            text "{size=+40}WARNING!{/size}" xalign 0.5 xanchor 0.5 ypos 150 color "#7a0000"
            text "We have detected old unusable files in your game folder,\nplease close the game and perform a clean installation." xalign 0.5 xanchor 0.5 ypos 250 color "#FFF"
            textbutton "{size=+30}Quit{/size}" action Quit(confirm=False) xalign 0.5 xanchor 0.5 yalign 0.9


init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



# Extras
screen extras():
    tag menu
    zorder 5

    window:
        style "gm_root"
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("About...") action Start("abouttrainer")
        textbutton _("F.A.Q.") action Start("faq")
        if not persistent.game_complete:
            textbutton _("{color=#858585}Gallery{/color}") action Start("gallery_locked")
        if persistent.game_complete:
            textbutton _("Gallery") action Start("gallery")
        textbutton _("Return") action Start("assmenu") # Sent here from "EXTRAS" menu. Basically just jumps to the title screen.

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        #textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():
    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 11):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 3
        $ rows = 6

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):
                $ is_compatible = check_save_compatibility(FileCurrentPage(), str(i))
                
                if renpy.get_screen("load"):
                    $ current_action = Confirm("{color=#7a0000}Warning!{/color}\nThe save file you're trying to load is incompatible with the current version of the game and may result in broken gameplay and multiple errors.\nDo you still wish to proceed?", yes=FileAction(i), no=NullAction())
                else:
                    $ current_action = FileAction(i)
                
                if is_compatible == True or is_compatible == None:
                    button:
                        xfill True
                        action FileAction(i)
                        has hbox

                        # Add the screenshot.
                        add FileScreenshot(i)

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        
                        if save_name != "":
                            textbutton _("X"):
                                yalign 0.5
                                xpos 235
                                yfill True
                                ymaximum 50
                                action FileDelete(i, persistent.delwarning)
                            text "[file_name]. [file_time!t]\n[save_name!t]" xpos -40 yalign 0.5
                        else:
                            text "[file_name]. [file_time!t]" xoffset 1
                            
                        key "save_delete" action FileDelete(i, persistent.delwarning)
                else:
                    button:
                        xfill True
                        action current_action
                            
                        has hbox

                        # Add the screenshot.
                        add grayTint(FileScreenshot(i))

                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        
                        if save_name != "":
                            textbutton _("X"):
                                yalign 0.5
                                xpos 235
                                yfill True
                                ymaximum 50
                                action FileDelete(i, persistent.delwarning)
                            text "[file_name]. [file_time!t]\n\n{color=#7a0000}NOT COMPATIBLE{/color}" xpos -40 yalign 0.5
                        else:
                            text "[file_name]. [file_time!t]" xoffset 1
                            
                        key "save_delete" action FileDelete(i, persistent.delwarning)

screen save():
    tag menu

    use navigation
    use file_picker

    zorder 5

screen load():
    tag menu

    use navigation
    use file_picker

    zorder 5

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():
    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a four-wide grid.
    if not renpy.variant('android'):
        $ columns = 4
        $ rows = 1
    else:
        $ columns = 3
        $ rows = 1
    grid columns rows:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            if not renpy.variant('android'):
                frame:
                    style_group "pref"
                    has vbox

                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    
            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")
            ####
            frame:
                style_group "pref"
                has vbox
                
                label _("Interface")
                if not renpy.variant('android'):
                    textbutton "Tooltips" action ToggleVariable("persistent.tooltip", True, False)
                    textbutton _("Custom Cursor") action [ToggleVariable("persistent.customcursor", True, False), ToggleVariable("config.mouse", { 'default' : [ ('interface/cursor.png', 0, 0)] }, None) ]
                textbutton _("Nightmode") action ToggleVariable("persistent.nightmode", True, False)
            frame:
                style_group "pref"
                has vbox

                label _("Saybox")
                if not persistent.nightmode:
                    textbutton _("Day {color=[persistent.text_color_day]}text{/color}") action Call("saybox_color")
                textbutton _("Night {color=[persistent.text_color_night]}text{/color}") action Call("saybox_color", False)
                textbutton _("Shadow") action ToggleVariable("persistent.text_outline", "#00000080", "#00000000")
                textbutton _("Default") action [SetVariable("persistent.text_color_day", "#402313"), SetVariable("persistent.text_color_night", "#341c0f"), SetVariable("persistent.text_outline", "#00000000")]
                
            if not main_menu:
                frame:
                    style_group "pref"
                    has vbox
                    
                    label _("Difficulty")
                    hbox:
                        xalign 0.5
                        textbutton _("Easy") text_size 14 text_color "#93b04c66" text_selected_color "#93b04c" xsize 80 action [SetVariable("game_difficulty", 1), SetVariable("cheat_reading", True)]
                        textbutton _("Normal") text_size 14 xsize 80 action [SetVariable("game_difficulty", 2), SetVariable("cheat_reading", False), SelectedIf(game_difficulty==2)]
                        if persistent.game_complete:
                            textbutton _("Hard") text_size 14 text_color "#7a000066" text_selected_color "#7a0000" xsize 80 action [SetVariable("game_difficulty", 3), SetVariable("cheat_reading", False), SelectedIf(game_difficulty==3)]

            # Joystick settings aren't needed, I dont think anyone plays WT with it.
            #frame:
                #style_group "pref"
                #has vbox

                #textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")
            
            # Obsolete, you can click skip button on the saybox instead
            #frame:
            #    style_group "pref"
            #    has vbox

            #   textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                    
            frame:
                style_group "pref"
                has vbox
                
                label _("{size=-4}Animation preference{/size}")
                textbutton _("Chibis") action SetVariable("use_cgs", False)
                textbutton _("Sprites") action SetVariable("use_cgs", True)

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
            frame:
                style_group "pref"
                has vbox
                
                label _("Saving&Loading")
                textbutton _("Autosave") action [ToggleVariable("persistent.autosave", True, False), ToggleVariable("config.has_autosave", True, False), ToggleVariable("config.autosave_on_choice", True, False)]
                textbutton _("Save Del. Warning") action ToggleVariable("persistent.delwarning", True, False)
        if not renpy.variant('android'):
            vbox:#Hotkeys
                frame:
                    style_group "pref"
                    has vbox

                    label _("Hotkeys")
                    textbutton _("Map - [hkey_map]") action None
                    textbutton _("Work - [hkey_work]") action None
                    textbutton _("Books - [hkey_book]") action None
                    textbutton _("Stats - [hkey_stats]") action None
                    textbutton _("Inventory - [hkey_inventory]") action None
                    textbutton _("Sleep - [hkey_sleep]") action None
                    textbutton _("Jerk off - [hkey_fap]") action None
    zorder 5

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen confirm(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            text _(message):
                text_align 0.5
                xalign 0.5

            hbox:
                spacing 100
                xalign .5
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    # Right-click and escape answer "no".
    key "game_menu" action no_action
    zorder 6

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    if renpy.variant('android'):
        hbox:
            style_group "quick"

            xpos 845
            ypos 489
            xanchor 1.0

            textbutton _("Save") action ShowMenu('save') activate_sound "sounds/click3.mp3"
            textbutton _("Auto") action Preference("auto-forward", "toggle") activate_sound "sounds/click3.mp3"
        hbox:
            ypos 600
            if renpy.can_rollback():
                imagebutton idle "interface/frames/"+interface_color+"/arrow.png" action Rollback() activate_sound "sounds/click3.mp3" yanchor 1.0 xanchor 0.5 xpos 180
            imagebutton idle im.Flip("interface/frames/"+interface_color+"/arrow.png", horizontal=True) action Skip(fast=True, confirm=True) activate_sound "sounds/click3.mp3" yanchor 1.0 xanchor 0.5 xpos 800
    else:
        hbox:
            style_group "quick"

            xpos 845
            ypos 489
            xanchor 1.0

            #textbutton _("Back") action Rollback()
            #textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave() activate_sound "sounds/click3.mp3"
            textbutton _("Q.Load") action QuickLoad() activate_sound "sounds/click3.mp3"
            textbutton _("Skip") action Skip() activate_sound "sounds/click3.mp3"
            #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle") activate_sound "sounds/click3.mp3"
            textbutton _("Prefs") action ShowMenu('preferences') activate_sound "sounds/click3.mp3"

init -2:
    style quick_button:
        is default
        background None
        xpadding 8
        ypadding 8

    style quick_button_text:
        is default
        size 10
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"