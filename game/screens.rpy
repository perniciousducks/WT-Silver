# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
    
screen say:
    zorder 6 #Otherwise the character sprite would be obscuring it.

    #Hotkeys
    use hotkeys_say

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False
    
    #Add "hidden" window
    if hkey_chat_hidden:
        window:
            xalign 0.5
            yalign 1.0
            style "say_who_window"
            text "Hidden" xalign 0.5 yalign 0.5
        #Add fullscreen CTC button
        button:
            action SetVariable("hkey_chat_hidden", False)
            style "empty"

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:
        # The one window variant.
        vbox:
            if hkey_chat_hidden:
                ypos 1000
                
            style "say_two_window_vbox"
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                if who:
                    text who id "who"

                text what id "what"

    else:
        # The two window variant.
        vbox:
            #Its the easiest way to hide the chat window without breaking the game, really
            if hkey_chat_hidden:
                ypos 1000
                
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:
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

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:
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
screen main_menu:
    tag menu
    zorder 5

    # The background of the main menu.
    window:
        style "mm_root"
    
    # Version display
    text "{color=#fff}{size=-4}%s{/size}{/color}" % config.version xpos 1020 ypos 250 outlines [ (1, "#000", 0, 0) ]

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .96
        yalign .75

        has vbox

        if not persistent.game_complete:
            textbutton _("New Game") action Start()
        if persistent.game_complete:
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
    add "logo/arrow.png" xpos 760 ypos 500
    text "{color=#b20000}{size=+10}NEW\nPATREON!{/size}{/color}" xpos 700 ypos 445 outlines [ (3, "#000", 0, 0) ]


init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



# Extras
screen extras:
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
screen navigation:

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
        textbutton _("Help") action Help()
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

screen file_picker:

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

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

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

screen save:
    tag menu

    use navigation
    use file_picker

    zorder 5

screen load:
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

screen preferences:
    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
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

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
                
            frame:
                style_group "pref"
                has vbox
                
                label _("Other")
                text _("Save Deletion warning")
                textbutton "Yes" action SetField(persistent, 'delwarning', True)
                textbutton "No" action SetField(persistent, 'delwarning', False)
                text _("Custom cursor")
                textbutton _("Yes") action [SetField(persistent, 'customcursor', True), SetVariable("config.mouse", { 'default' : [ ('interface/cursor.png', 0, 0)] })]
                textbutton _("No") action [SetField(persistent, 'customcursor', False), SetVariable("config.mouse", None)]
                text _("Autosaving")
                textbutton "Yes" action [SetField(persistent, 'autosave', True), SetVariable("config.has_autosave", True), SetVariable("config.autosave_on_choice", True)]
                textbutton "No" action [SetField(persistent, 'autosave', False), SetVariable("config.has_autosave", False), SetVariable("config.autosave_on_choice", False)]
                #textbutton _("[delwarning!t]") action ToggleVariable("delwarning", True, False)


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

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
            #Hotkeys
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

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

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
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 0.1

        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 4

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


# Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    #config.default_afm_time = 10
    #config.default_afm_enable = False
