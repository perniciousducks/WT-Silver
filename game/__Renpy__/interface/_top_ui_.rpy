init python:
    def ui_dropped(drags, drops):
        drags[0].snap(clamp(drags[0].target_x, 20, 740), 0)
        return

    def text_points(points):
        if points < 1000:
            return str(points)
        else:
            return  str(round(points/1000.0, 1))+"{size=-2}k{/size}"

    def image_hover(image):
        return im.MatrixColor(image, im.matrix.brightness(0.12))

    def image_alpha(image):
        return im.MatrixColor(image, im.matrix.opacity(0.5))

label house_points:
    # Debug
    if config.debug:
        $ total_points = slytherin+gryffindor+ravenclaw+hufflepuff

    # Temp variables
    $ toggle_ui_lock = True
    $ toggle_points = False
    $ toggle_menu = False
    $ ui_hint = ""

    # Outline settings
    $ points_outline = [ (1, "#000", 0, 0) ]
    if daytime:
        $ daygold_colour = "{color=#000}"
        $ daygold_outline = [ (1, "#e4ba70", 0, 0) ]
    else:
        $ daygold_colour = "{color=#FFF}"
        $ daygold_outline = [ (1, "#000", 0, 0) ]

    #If points variable value exceedes one thousand make it a decimal number instead and round to x.x
    #Remember, "slytherin_points" is a string! If you need points integer use i.e. "slytherin" variable instead.
    $ slytherin_points = text_points(slytherin)
    $ gryffindor_points = text_points(gryffindor)
    $ ravenclaw_points = text_points(ravenclaw)
    $ hufflepuff_points = text_points(hufflepuff)

    #Check who's in the lead
    $ housepoints = [slytherin, gryffindor, ravenclaw, hufflepuff]
    $ housepoints_sorted = sorted(housepoints, reverse=True)

    $ slytherin_place = housepoints_sorted.index(housepoints[0])+1
    $ gryffindor_place = housepoints_sorted.index(housepoints[1])+1
    $ ravenclaw_place = housepoints_sorted.index(housepoints[2])+1
    $ hufflepuff_place = housepoints_sorted.index(housepoints[3])+1

    # Set banners yanchor depending on the placement (ascending)
    $ housepoints_y = [None, 0.0, 0.25, 0.5, 0.75]

    return

#Close Button
screen top_bar_close_button(offsetx = 0, offsety = 0, close_var=lambda : "Close", flip=-1):
    imagebutton:
        xpos 1080 -offsetx
        ypos 0 -offsety
        xanchor 1.0
        idle "interface/topbar/buttons/"+interface_color+"/ui_close.png"
        hover image_hover("interface/topbar/buttons/"+interface_color+"/ui_close.png")
        action Return(close_var())
        keysym "game_menu"

#Top Bar UI
screen ui_top_bar():
    tag ui
    zorder 2

    if toggle_menu:
        use ui_menu

    add "interface/topbar/"+str(interface_color)+"/bar.png"
    use ui_stats
    use ui_points

    # Don't display buttons in the shops or on day 1
    if not renpy.get_screen("clothing_store_room") and not renpy.get_screen("weasley_store_room") and day != 1:
        # Menu button
        imagebutton:
            xpos 0
            idle "interface/topbar/buttons/"+str(interface_color)+"/ui_menu.png"
            if renpy.get_screen("main_room_menu"):
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_menu.png")
                hovered SetVariable("ui_hint", "Open menu")
                unhovered SetVariable("ui_hint", "")
                action [Hide("main_room_menu"), ToggleVariable("toggle_menu", True, False)]
                activate_sound "sounds/click3.mp3"
            elif not renpy.get_screen("main_room_menu") and toggle_menu:
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_menu.png")
                hovered SetVariable("ui_hint", "Close menu")
                unhovered SetVariable("ui_hint", "")
                action [Show("main_room_menu"), ToggleVariable("toggle_menu", True, False)]
                activate_sound "sounds/click3.mp3"

        # Sleep button
        imagebutton:
            xpos 1080
            xanchor 1.0
            idle "interface/topbar/buttons/"+str(interface_color)+"/ui_sleep.png"
            if renpy.get_screen("main_room_menu"):
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_sleep.png")
                if daytime:
                    action Jump("night_start")
                    hovered SetVariable("ui_hint", "Doze Off (s)")
                else:
                    action Jump("day_start")
                    hovered SetVariable("ui_hint", "Sleep (s)")
                unhovered SetVariable("ui_hint", "")
                activate_sound "sounds/click3.mp3"

        hbox:
            xpos 900
            # Stats button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_stats.png"
                if renpy.get_screen("main_room_menu"):
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_stats.png")
                    hovered SetVariable("ui_hint", "Statistics (c)")
                    unhovered SetVariable("ui_hint", "")
                    action [SetVariable("ui_hint", ""), Hide("main_room_menu"), Jump("open_stat_menu")]
                    activate_sound "sounds/click3.mp3"

            # Inventory button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_inv.png"
                if renpy.get_screen("main_room_menu"):
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_inv.png")
                    hovered SetVariable("ui_hint", "Inventory (i)")
                    unhovered SetVariable("ui_hint", "")
                    action [SetVariable("ui_hint", ""), Jump("open_inventory_menu")]
                    activate_sound "sounds/click3.mp3"

            # Work button
            if letter_paperwork_unlock_OBJ.read:
                imagebutton:
                    idle "interface/topbar/buttons/"+str(interface_color)+"/ui_work.png"
                    if renpy.get_screen("main_room_menu"):
                        hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_work.png")
                        hovered SetVariable("ui_hint", "Work (w)")
                        unhovered SetVariable("ui_hint", "")
                        action [SetVariable("ui_hint", ""), Jump("paperwork")]
                        activate_sound "sounds/click3.mp3"

        ## Toggle UI lock button
        #imagebutton:
        #    xpos 1047
        #    idle "interface/topbar/buttons/"+str(interface_color)+"/ui_%s.png" % toggle_ui_lock
        #    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_%s.png" % toggle_ui_lock)
        #    action ToggleVariable("toggle_ui_lock", False, True)
        #    activate_sound "sounds/click3.mp3"

        #Debug
        if config.debug:
            hbox:
                xpos 10 ypos 40
                text "{size=-5}{color=#FFF}[total_points] [housepoints]\n[housepoints_y]\nToggle display:[persistent.toggle_points]\n\nSly:[slytherin_place]\nGry:[gryffindor_place]\nRav:[ravenclaw_place]\nHuf:[hufflepuff_place]\nUI lock:[toggle_ui_lock]{/color}{/size}"

        if not ui_hint == "" and persistent.ui_hint:
            text "{color=#FFF}{size=+4}[ui_hint]{/size}{/color}" xalign 0.5 text_align 0.5 ypos 540

screen ui_points():
    tag ui
    drag:
        drag_name "ui_points"
        draggable not toggle_ui_lock
        dragged ui_dropped
        drag_handle(0, 0, 1.0, 1.0)
        xpos 540 ypos 0
        xanchor 0.5
        frame:
            style "empty"
            xsize 162
            ysize 64
            xanchor 0.5

            if not persistent.toggle_points and not toggle_points:
                add "interface/topbar/slytherin.png" yanchor housepoints_y[slytherin_place]
                add "interface/topbar/gryffindor.png" yanchor housepoints_y[gryffindor_place]
                add "interface/topbar/ravenclaw.png" yanchor housepoints_y[ravenclaw_place]
                add "interface/topbar/hufflepuff.png" yanchor housepoints_y[hufflepuff_place]
            else:
                # Add empty banners
                add "interface/topbar/slytherin_empty.png" yanchor 0
                add "interface/topbar/gryffindor_empty.png" yanchor 0
                add "interface/topbar/ravenclaw_empty.png" yanchor 0
                add "interface/topbar/hufflepuff_empty.png" yanchor 0
                # Show points
                text "{size=-7}{color=#FFF}[slytherin_points]{/color}{/size}" outlines points_outline xpos 17 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[gryffindor_points]{/color}{/size}" outlines points_outline xpos 58 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[ravenclaw_points]{/color}{/size}" outlines points_outline xpos 98 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[hufflepuff_points]{/color}{/size}" outlines points_outline xpos 139 ypos 30 xanchor 0.5
                # Show placement number
                text "{size=-2}{color=#FFF}[slytherin_place]{/color}{/size}" outlines points_outline xpos 17 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[gryffindor_place]{/color}{/size}" outlines points_outline xpos 58 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[ravenclaw_place]{/color}{/size}" outlines points_outline xpos 98 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[hufflepuff_place]{/color}{/size}" outlines points_outline xpos 139 ypos 10 xanchor 0.5

            if toggle_ui_lock and renpy.get_screen("main_room_menu"):
                imagebutton:
                    idle "interface/topbar/hover_zone.png"
                    hovered [SetVariable("toggle_points", True), SetVariable("ui_hint", "Toggle banners style")]
                    unhovered [SetVariable("toggle_points", False), SetVariable("ui_hint", "")]
                    action ToggleVariable("persistent.toggle_points", True, False)
                    activate_sound "sounds/click3.mp3"

screen ui_stats():
    tag ui
    drag:
        drag_name "ui_stats"
        draggable not toggle_ui_lock
        dragged ui_dropped
        xpos 200
        frame:
            style "empty"
            xsize 217
            ysize 26
            add "interface/topbar/"+str(interface_color)+"/stats.png" xalign 0.5 yalign 1.0

            hbox:
                xpos 40 ypos 11
                text "{size=-6}[daygold_colour][day]{/color}{/size}" outlines daygold_outline
            hbox:
                xpos 140 ypos 11
                text "{size=-6}[daygold_colour][gold]{/color}{/size}" outlines daygold_outline

screen ui_menu():
    tag ui

    button:
        style "empty"
        action [SetVariable("toggle_menu", False), Show("main_room_menu")]
        keysym "game_menu"
    button:
        ypos 34
        xsize 102
        ysize 204
        action NullAction()
        style "empty"
    frame:
        style "empty"
        ypos 34
        add "interface/topbar/"+str(interface_color)+"/menu.png"
        vbox:
            style_group "mm"
            ypos 20
            xpos -5
            textbutton "Save" action ShowMenu("save") background #000
            textbutton "Load" action ShowMenu("load") background #000
            text "" # space
            if cheats_active and game_difficulty <= 2 and day > 1:
                textbutton "{size=-11}Cheats{/size}" action [SetVariable("toggle_menu", False), Jump("cheats")] background #000
            if day != 1:
                textbutton "{size=-11}Decorate{/size}" action [SetVariable("toggle_menu", False), Jump("decorate_room_menu")] background #000
            if day != 1:
                textbutton "{size=-11}Show Chars{/size}" action [SetVariable("toggle_menu", False), Jump("summon_characters")] background #000

        hbox:
            xpos 50
            ypos 185
            spacing 5
            yanchor 0.5
            xanchor 0.5
            #Discord
            imagebutton:
                idle image_alpha("interface/topbar/icon_discord.png")
                hover "interface/topbar/icon_discord.png"
                hovered [SetVariable("ui_hint", "Visit {size=-6}SilverGamesStudios{/size} discord")]
                unhovered [SetVariable("ui_hint", "")]
                action OpenURL("https://discord.gg/7PD57yt")
                activate_sound "sounds/click3.mp3"
            #Patreon
            imagebutton:
                idle image_alpha("interface/topbar/icon_patreon.png")
                hover "interface/topbar/icon_patreon.png"
                hovered [SetVariable("ui_hint", "Visit {size=-6}SilverGamesStudios{/size} patreon")]
                unhovered [SetVariable("ui_hint", "")]
                action OpenURL("https://www.patreon.com/SilverStudioGames")
                activate_sound "sounds/click3.mp3"
            #Bugfixes
            imagebutton:
                idle image_alpha("interface/topbar/icon_bug.png")
                hover "interface/topbar/icon_bug.png"
                hovered [SetVariable("ui_hint", "Open bugfix menu")]
                unhovered [SetVariable("ui_hint", "")]
                action [SetVariable("toggle_menu", False), SetVariable("ui_hint", ""), Jump("bugfix_menu")]
                activate_sound "sounds/click3.mp3"


#Moved from cupbord.rpy #Remove when not needed.
label options_menu:
    menu:
        "-Save and Load-":
            call screen save()

        "-Change Save Name-":
            jump custom_save

        "-Options-":
            menu:
                "-Change Game Difficulty-" if game_difficulty <= 2:
                    menu:
                        "-Enable Easy Difficulty-":
                            $ game_difficulty = 1
                            $ cheat_reading = True
                            "Game set to easy difficulty!"
                            "Increased gold reward from reports and other sources!"
                            "Rummaging through your cupboard is more rewarding!"
                            "Snape will be more generous with Slytherin-points!"
                            "Hermione won't stay mad at you for as long!"
                            jump day_main_menu
                        "-Enable Normal Difficulty-":
                            $ game_difficulty = 2
                            $ cheat_reading = False
                            "Game set to normal difficulty!"
                            jump day_main_menu
                        "-Back-":
                            jump day_main_menu
                "-Replace Chibis with Sprites-" if not use_cgs:
                    ">The last two personal favours will use sprites now."
                    $ use_cgs = True
                    jump day_main_menu
                "-Replace Sprites with Chibis-" if use_cgs:
                    ">The last two personal favours will use chibi animations again."
                    $ use_cgs = False
                    jump day_main_menu
                "-Back-":
                    jump day_main_menu

        "-Cheats-" if cheats_active and game_difficulty <= 2 and day > 1:
            jump cheats

        "-Bugfix-":
            label bugfix_menu:
            menu:
                "-Reset Everyone's Appearance-":
                    call reset_hermione_base
                    call reset_hermione_clothing
                    call reset_luna_base
                    call reset_luna_clothing
                    call reset_astoria_clothing
                    call reset_susan_clothing
                    call reset_cho_clothing
                    call reset_tonks_clothing
                    ">Appearance of each girl set back to default."
                    jump day_main_menu
                "-Reset ALL Luna content-" if hat_known:
                    $ reset_luna_content = True
                    call luna_init
                    call luna_progress_init
                    $ reset_luna_content = False
                    ">Luna content reset!"
                    jump day_main_menu
                "-Never mind-":
                    jump day_main_menu



        "-Display Characters-" if day != 1:
            jump summon_characters

        "-Never mind-":
            jump day_main_menu



label custom_save:
    $ temp_name = renpy.input("(Please enter the save name.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name
    "Done."
    jump day_main_menu


label decorate_room_menu:
    $ current_category = None

    label deco_menu:
    call update_deco_items

    python:

        category_list = []
        # Use the category item's name for the button images inside the 'interface/topbar/buttons/color/' folder.
        category_list.append("deco_wall")
        category_list.append("deco_fireplace")
        category_list.append("deco_cupboard")

        if current_category == None:
            menu_title = "Wall Deco"
            current_category = category_list[0]
            category_choice = category_list[0]

        item_list = []
        if current_category == "deco_wall":
            menu_title = "Wall Deco"
            item_list.extend(wall_deco_list)
            item_list.extend(toy_gift_list) # For Testing
        if current_category == "deco_fireplace":
            menu_title = "Fireplace Deco"
            item_list.extend(fireplace_deco_list)
            item_list.extend(candy_gift_list) # For Testing
        if current_category == "deco_cupboard":
            menu_title = "Cupboard Deco"
            item_list.extend(cupboard_deco_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    $ _return = ui.interact()

    hide screen bottom_menu
    if category_choice != current_category: # Updates categories.
        $ current_category = _return

    elif isinstance(_return, item_class):
        if _return.number > 0 or _return.unlocked:
            call use_deco_item(_return)
        else:
            "You haven't unlocked this decoration yet."
            jump deco_menu


    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump day_main_menu

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump deco_menu


# List with deco objects
## Same lists get used in the Weasley store.
## Add any deco objects to the lists here.
label update_deco_items:
    $ wall_deco_list = []
    $ fireplace_deco_list = []
    $ cupboard_deco_list = []

    return

label use_deco_item(item=None): # Add the 'item' decoration to the room. Remove it when 'item' is currently displayed as a deco.

    return
