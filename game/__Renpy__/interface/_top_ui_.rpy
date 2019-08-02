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
    $ tooltip = ""

    # Outline settings
    $ points_outline = [ (1, "#000", 0, 0) ]
    if daytime and not persistent.nightmode:
        $ daygold_colour = "{color=#000}"
        $ daygold_outline = [ (1, "#e4ba7080", 0, 0) ]
    else:
        $ daygold_colour = "{color=#FFF}"
        $ daygold_outline = [ (1, "#00000080", 0, 0) ]

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
screen top_bar_close_button(xoffset=0, yoffset=0, close_var="Close"):
    imagebutton:
        xpos 1080
        ypos 0
        xoffset xoffset
        yoffset yoffset
        xanchor 1.0
        idle "interface/topbar/buttons/"+interface_color+"/ui_close.png"
        hover image_hover("interface/topbar/buttons/"+interface_color+"/ui_close.png")
        action Return(close_var)
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
                hovered SetVariable("tooltip", "Open menu")
                unhovered SetVariable("tooltip", None)
                action [Hide("main_room_menu"), ToggleVariable("toggle_menu", True, False)]
                activate_sound "sounds/click3.mp3"
            elif not renpy.get_screen("main_room_menu") and toggle_menu:
                hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_menu.png")
                hovered SetVariable("tooltip", "Close menu")
                unhovered SetVariable("tooltip", None)
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
                    hovered SetVariable("tooltip", "Doze Off (s)")
                else:
                    action Jump("day_start")
                    hovered SetVariable("tooltip", "Sleep (s)")
                unhovered SetVariable("tooltip", None)
                activate_sound "sounds/click3.mp3"

        hbox:
            if renpy.variant('android'):
                spacing 10
                xpos 800
            else:
                xpos 900
            # Achievements button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_achievements.png"
                if renpy.get_screen("main_room_menu"):
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_achievements.png")
                    hovered SetVariable("tooltip", "Achievements")
                    unhovered SetVariable("tooltip", None)
                    action [SetVariable("tooltip", None), Hide("main_room_menu"), Jump("achievement_menu")]
                    activate_sound "sounds/click3.mp3"

            # Stats button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_stats.png"
                if renpy.get_screen("main_room_menu"):
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_stats.png")
                    hovered SetVariable("tooltip", "Characters (c)")
                    unhovered SetVariable("tooltip", None)
                    action [SetVariable("tooltip", None), Hide("main_room_menu"), Jump("open_stat_menu")]
                    activate_sound "sounds/click3.mp3"

            # Inventory button
            imagebutton:
                idle "interface/topbar/buttons/"+str(interface_color)+"/ui_inv.png"
                if renpy.get_screen("main_room_menu"):
                    hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_inv.png")
                    hovered SetVariable("tooltip", "Inventory (i)")
                    unhovered SetVariable("tooltip", None)
                    action [SetVariable("tooltip", None), Jump("open_inventory_menu")]
                    activate_sound "sounds/click3.mp3"

            # Work button
            if letter_paperwork_unlock_OBJ.read:
                imagebutton:
                    idle "interface/topbar/buttons/"+str(interface_color)+"/ui_work.png"
                    if renpy.get_screen("main_room_menu"):
                        hover image_hover("interface/topbar/buttons/"+str(interface_color)+"/ui_work.png")
                        hovered SetVariable("tooltip", "Work (w)")
                        unhovered SetVariable("tooltip", None)
                        action [SetVariable("tooltip", None), Jump("paperwork")]
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
                text "{size=-3}{color=#FFF}[total_points] [housepoints]\n[housepoints_y]\nToggle display:[persistent.toggle_points]\n\nSly:[slytherin_place]\nGry:[gryffindor_place]\nRav:[ravenclaw_place]\nHuf:[hufflepuff_place]\nUI lock:[toggle_ui_lock]{/color}{/size}"

        # if tooltip and persistent.tooltip and not renpy.variant('android'):
            # text "{color=#FFF}{size=+4}[tooltip]{/size}{/color}" xalign 0.5 text_align 0.5 ypos 540
            
screen mouse_tooltip():
    zorder 999
    tag tooltip
    
    if persistent.tooltip and tooltip:
        python:
            x, y = renpy.get_mouse_pos()
            xval = 1.0 if x > config.screen_width/2 else .0
            yval = 1.0 if y > config.screen_height/2 else .0
            
        frame:
            style_prefix "dropdown_gm"
            pos (x, y)
            anchor (xval, yval)
            
            text tooltip color "#FFF" size 14

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
                text "{size=-5}{color=#FFF}[slytherin_points]{/color}{/size}" outlines points_outline xpos 17 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[gryffindor_points]{/color}{/size}" outlines points_outline xpos 58 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[ravenclaw_points]{/color}{/size}" outlines points_outline xpos 98 ypos 30 xanchor 0.5
                text "{size=-5}{color=#FFF}[hufflepuff_points]{/color}{/size}" outlines points_outline xpos 139 ypos 30 xanchor 0.5
                # Show placement number
                text "{size=16}{color=#FFF}[slytherin_place]{/color}{/size}" outlines points_outline xpos 17 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[gryffindor_place]{/color}{/size}" outlines points_outline xpos 58 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[ravenclaw_place]{/color}{/size}" outlines points_outline xpos 98 ypos 10 xanchor 0.5
                text "{size=16}{color=#FFF}[hufflepuff_place]{/color}{/size}" outlines points_outline xpos 139 ypos 10 xanchor 0.5

            if toggle_ui_lock and renpy.get_screen("main_room_menu"):
                imagebutton:
                    idle "interface/topbar/hover_zone.png"
                    hovered [SetVariable("toggle_points", True), SetVariable("tooltip", "Toggle banners style")]
                    unhovered [SetVariable("toggle_points", False), SetVariable("tooltip", None)]
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

            # Add overlay token icon if needed
            if renpy.get_screen("weasley_store_room") and store_category == 3:
                add "interface/topbar/icon_token.png" ypos 8 xpos 118

            hbox:
                xpos 40 ypos 11
                text "{size=-4}[daygold_colour][day]{/color}{/size}" outlines daygold_outline
            hbox:
                xpos 140 ypos 11
                # Display tokens in token shop
                if renpy.get_screen("weasley_store_room") and store_category == 3:
                    text "{size=-4}[daygold_colour][geniecard_tokens]{/color}{/size}" outlines daygold_outline
                else:
                    text "{size=-4}[daygold_colour][gold]{/color}{/size}" outlines daygold_outline

screen ui_menu():
    tag ui

    button style "empty" action [SetVariable("toggle_menu", False), Show("main_room_menu")] keysym "game_menu"

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
            if renpy.variant('android'):
                ypos 10
                spacing 5
                xpos 5
            else:
                ypos 20
                xpos 5
            textbutton "Save" action ShowMenu("save") background #000
            textbutton "Load" action ShowMenu("load") background #000
            text "" # space
            if cheats_active and game_difficulty <= 2 and day > 1:
                textbutton "{size=-11}Cheats{/size}" action [SetVariable("toggle_menu", False), Jump("cheats")] background #000
            if day != 1 and renpy.variant('android'):
                textbutton "{size=-11}PrEfErEnCeS{/size}" action ShowMenu("preferences") background #000
            if day != 1 and persistent.game_complete:
                textbutton "{size=-11}Gallery{/size}" action [SetVariable("toggle_menu", False), Jump("scene_gallery")] background #000
            if day != 1:
                textbutton "{size=-11}Decorate{/size}" action [SetVariable("toggle_menu", False), Jump("decorate_room_menu")] background #000

            #if day != 1 and config.developer:
            #    textbutton "{size=-11}Show Chars{/size}" action [SetVariable("toggle_menu", False), Jump("summon_characters")] background #000

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
                hovered [SetVariable("tooltip", "Visit {size=-6}SilverStudioGames{/size} discord")]
                unhovered [SetVariable("tooltip", None)]
                action OpenURL("https://discord.gg/7PD57yt")
                activate_sound "sounds/click3.mp3"
            #Patreon
            imagebutton:
                idle image_alpha("interface/topbar/icon_patreon.png")
                hover "interface/topbar/icon_patreon.png"
                hovered [SetVariable("tooltip", "Visit {size=-6}SilverStudioGames{/size} patreon")]
                unhovered [SetVariable("tooltip", None)]
                action OpenURL("https://www.patreon.com/SilverStudioGames")
                activate_sound "sounds/click3.mp3"
            #Bugfixes
            imagebutton:
                idle image_alpha("interface/topbar/icon_bug.png")
                hover "interface/topbar/icon_bug.png"
                hovered [SetVariable("tooltip", "Open bugfix menu")]
                unhovered [SetVariable("tooltip", None)]
                action [SetVariable("toggle_menu", False), SetVariable("tooltip", None), Jump("bugfix_menu")]
                activate_sound "sounds/click3.mp3"



### Ingame Options Menu ###

label options_menu:
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
        "-Replace Chibi animations with CG images-" if not use_cgs:
            ">The last two of Hermione's personal favours will use CG images."
            $ use_cgs = True
            jump day_main_menu
        "-Replace CG images with Chibi animations-" if use_cgs:
            ">The last two of Hermione's personal favours will now use chibi animations."
            $ use_cgs = False
            jump day_main_menu
        "-Never mind-":
            jump day_main_menu
            
label bugfix_menu:
    menu:
        "-Reset Everyone's Appearance-":
            call reset_hermione_base
            call reset_hermione_clothing
            call reset_luna_base
            call reset_luna_clothing
            call reset_susan_clothing
            $ cho_class.animation(None)
            $ cho_class.wear("all")
            $ astoria_class.animation(None)
            $ astoria_class.wear("all")
            $ tonks_class.animation(None)
            $ tonks_class.wear("all")
            ">Appearance of each girl set back to default."
            jump bugfix_menu
        "-Reset Cho public and personal favours-" if cho_unlocked:
            python:
                for ev in cc_favor_list:
                    ev.reset()
                for ev in cc_requests_list:
                    ev.reset()
            "> Events have been successfully reset."
            jump bugfix_menu
        "-Back-":
            pass
    jump day_main_menu

label custom_save:
    $ temp_name = renpy.input("(Please enter the save name.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name
    "Done."
    jump day_main_menu

label scene_gallery:
    menu:
        "-Watch Ball Ending 1-" if persistent.ending_01:
            $ gallery_active = True
            $ ball_ending_2 = False
            jump ball_ending_E2
        "-Watch Ball Ending 2-" if persistent.ending_02:
            $ gallery_active = True
            $ ball_ending_2 = True
            jump ball_ending_E2

        "-Never mind-":
            jump day_main_menu

label return_gallery:
    call blkfade
    $ gallery_active = False

    jump main_room







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
            menu_title = "Posters"
            item_list.extend(wall_deco_list)
        if current_category == "deco_fireplace":
            menu_title = "Trophies"
            item_list.extend(fireplace_deco_list)
        if current_category == "deco_cupboard":
            menu_title = "Miscellaneous"
            item_list.extend(cupboard_deco_list)
            item_list.extend(misc_deco_list)
            item_list.extend(misc_hat_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475, func_btn=True, func_btn_ico="ui_delete")

    $ _return = ui.interact()

    hide screen bottom_menu
    if category_choice != current_category: # Updates categories.
        $ current_category = _return
    elif isinstance(_return, item_class):
        if _return.number > 0 or _return.unlocked:
            call use_deco_item(_return)
            $ achievement.unlock("decorator")
        else:
            "You haven't unlocked this decoration yet."
            jump deco_menu


    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump day_main_menu
    elif _return == "func":
        menu:
            "> Remove all decorations?"
            "Yes":
                # Loop through all decorations and deactivate them
                python:
                    for i in xrange(len(wall_deco_list)):
                        wall_deco_list[i].active = False
                    for i in xrange(len(fireplace_deco_list)):
                        fireplace_deco_list[i].active = False
                    for i in xrange(len(cupboard_deco_list)):
                        cupboard_deco_list[i].active = False
                    for i in xrange(len(misc_deco_list)):
                        misc_deco_list[i].active = False
                    for i in xrange(len(misc_hat_list)):
                        misc_hat_list[i].active = False

                $ poster_OBJ.room_image = ""
                $ trophy_OBJ.room_image = ""
                $ cupboard_deco = ""
                $ phoenix_deco_OBJ.room_image = ""
                $ fireplace_deco_OBJ.room_image = ""
                $ owl_deco_OBJ.room_image = ""
                $ owl_OBJ.room_image = "owl_idle"
                $ owl_OBJ.idle_image = "owl_with_letter_blink"
                $ owl_OBJ.hover_image = "owl_hover"
            "No":
                jump deco_menu
    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump deco_menu


# List with deco objects
## Same lists get used in the Weasley store.
## Add any deco objects to the lists here.
label update_deco_items:
    if not hasattr(renpy.store,'poster_agrabah_ITEM') or reset_persistants:
        #Posters
        $ poster_agrabah_ITEM = item_class(id="agrabah", name="Agrabah Poster", cost=2, type="poster", image="posters/agrabah", description="A remnant of a distant land and memories about different times. A reminder for when you just want to ponder about what could've been.")
        $ poster_gryffindor_ITEM = item_class(id="gryffindor", name="Gryffindor Poster", cost=2, type="poster", image="posters/gryffindor", description="Make your stance that you support the house of Gryffindor with this themed poster.")
        $ poster_hufflepuff_ITEM = item_class(id="hufflepuff", name="Hufflepuff Poster", cost=2, type="poster", image="posters/hufflepuff", description="Make your stance that you support the house of Hufflepuff with this themed poster.")
        $ poster_ravenclaw_ITEM = item_class(id="ravenclaw", name="Ravenclaw Poster", cost=2, type="poster", image="posters/ravenclaw", description="Make your stance that you support the house of Ravenclaw with this themed poster.")
        $ poster_slytherin_ITEM = item_class(id="slytherin", name="Slytherin Poster", cost=2, type="poster", image="posters/slytherin", description="Make your stance that you support the house of Slytherin with this themed poster.")
        $ poster_hermione_ITEM = item_class(id="hermione", name="Hermione Chibi Poster", cost=2, type="poster", image="posters/hermione", description="A little lewdness for the office, don't worry. With a special illusion charm no one but you will notice a thing....")
        $ poster_harlots_ITEM = item_class(id="harlots", name="Hogwarts Harlots Poster", cost=2, type="poster", image="posters/harlots", description="Hermione showing off her true colours at last with this special poster... illusion charm included...")
        $ poster_stripper_ITEM = item_class(id="stripper", name="Stripper Poster", cost=2, type="poster", image="posters/stripper", description="Hermione showing off how to work the pole... illusion charm included...")
        $ poster_wanted_ITEM = item_class(id="wanted", name="Wanted Poster", cost=2, type="poster", image="posters/wanted", description="A Wild West styled Wanted poster depicting our dear headmaster...")
        #Trophies
        $ trophy_stag_ITEM = item_class(id="stag", name="Stag Head Trophy", cost=3, type="trophy", image="trophies/stag", description="A perfect decoration over your mantelpiece to add a sense of masculinity to the office.")
        $ trophy_crest_ITEM = item_class(id="crest", name="Hogwarts Crest", cost=5, type="trophy", image="trophies/crest", description="A perfect decoration for a headmaster.")
        #Pinups & Misc
        $ pinup_girl_ITEM = item_class(id="_deco_1", name="Girl Pinup", cost=0, type="pinup", image="pinups/girl", description="Spice up your cupboard with this sexy pinup model...\n(Shows up when rumaging through the cupboard).", unlocked=True)
        # HATS HATS HATS HATS HATS HYPE
        $ owl_hat_ITEM = item_class(id="owl_hat", name="Owl Hat", cost=1, type="owl", imagepath="interface/icons/misc/owl_hat.png", description="A hat for an owl. Don't ask, just accept it..")
        $ phoenix_hat_ITEM = item_class(id="phoenix_hat", name="Phoenix Hat", cost=1, type="phoenix", imagepath="interface/icons/misc/phoenix_hat.png", description="A little something to make your friend look less depressed.")
        $ fireplace_hat_ITEM = item_class(id="fireplace_hat", name="Skull Hat", cost=1, type="fireplace", imagepath="interface/icons/misc/fireplace_hat.png", description="Don't let Johnny get a cold!")

        $ owl_black_ITEM = item_class(id="owl_idle_black", name="Black Owl", cost=3, type="mail", imagepath="interface/icons/misc/owl_black.png", description="Magically dye your mail courier black!")

        $ wall_deco_list = [poster_agrabah_ITEM, poster_gryffindor_ITEM, poster_hufflepuff_ITEM, poster_ravenclaw_ITEM, poster_slytherin_ITEM, poster_hermione_ITEM, poster_harlots_ITEM, poster_stripper_ITEM, poster_wanted_ITEM]
        $ fireplace_deco_list = [trophy_crest_ITEM, trophy_stag_ITEM]
        $ cupboard_deco_list = [pinup_girl_ITEM]
        $ misc_deco_list = [owl_black_ITEM]
        $ misc_hat_list = [phoenix_hat_ITEM, owl_hat_ITEM, fireplace_hat_ITEM]

    # Outfits
    if hg_gamble_slut_ITEM.unlocked and hg_gamble_slut_ITEM not in hermione_outfits_list: # Updates image from shop icon to mannequin.
        $ hg_gamble_slut_ITEM.image = "outfits/hg_gambler_slut"
        $ hermione_outfits_list.append(hg_gamble_slut_ITEM)
    return

label use_deco_item(item=None): # Add the 'item' decoration to the room. Remove it when 'item' is currently displayed as a deco.
    if item.type == "poster":
        # Loop through all posters and deactivate them
        python:
            for i in xrange(len(wall_deco_list)):
                wall_deco_list[i].active = False

        if poster_OBJ.room_image == item.id:
            $ poster_OBJ.room_image = ""
        else:
            $ poster_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "trophy":
        python:
            for i in xrange(len(fireplace_deco_list)):
                fireplace_deco_list[i].active = False

        if trophy_OBJ.room_image == item.id:
            $ trophy_OBJ.room_image = ""
        else:
            $ trophy_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "pinup":
        if cupboard_deco == item.id:
            $ cupboard_deco = ""
            $ item.active = False
        else:
            $ cupboard_deco = item.id
            $ item.active = True
    elif item.type == "phoenix":
        if phoenix_deco_OBJ.room_image == item.id:
            $ phoenix_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ phoenix_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "fireplace":
        if fireplace_deco_OBJ.room_image == item.id:
            $ fireplace_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ fireplace_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "owl":
        if owl_deco_OBJ.room_image == item.id:
            $ owl_deco_OBJ.room_image = ""
            $ item.active = False
        else:
            $ owl_deco_OBJ.room_image = item.id
            $ item.active = True
    elif item.type == "mail":
        if owl_OBJ.room_image == item.id:
            $ owl_OBJ.room_image = "owl_idle"
            $ owl_OBJ.idle_image = "owl_with_letter_blink"
            $ owl_OBJ.hover_image = "owl_hover"
            $ item.active = False
        else:
            $ owl_OBJ.room_image = item.id
            $ owl_OBJ.idle_image = "owl_with_letter_blink_black"
            $ owl_OBJ.hover_image = "owl_hover_black"
            $ item.active = True
    return
