init python:
    def upgrades_sortfilter(item, sortby=False):
        return item

default upgrades_show_locked = False

default her_upgrade_school2 = DollOutfit([her_hair_base, her_top_school2, her_bottom_school2, her_panties_base1, her_bra_base1, her_stockings_base1])

default her_upgrade_school3 = DollOutfit([her_hair_base, her_top_school3, her_bottom_school3, her_panties_base1, her_bra_base1, her_stockings_base1])

default her_upgrade_school4 = DollOutfit([her_hair_base, her_top_school4, her_bottom_school4, her_panties_base1, her_bra_base1, her_stockings_base1])

label upgrades:
    $ screenshot_image = ScreenshotImage.capture()
    $ renpy.call_in_new_context("upgrades_menu")
    jump tonks_talk

label upgrades_menu(xx=150, yy=90):

    $ upgrades_dict = {
                    "Tonks": {"ico": "head_tonks_1", "flag": tonks_unlocked, "outfits": {"school": []}},
                    "Hermione": {"ico": "head_hermione_2", "flag": hermione_unlocked, "outfits": {"school": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other2": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4, her_outfit_bikini1], "other3": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other4": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4, her_outfit_bikini1], "other5": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other6": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4], "other7": [her_outfit_default, her_upgrade_school2, her_upgrade_school3, her_upgrade_school4]}},
                    "Cho": {"ico": "head_cho_2", "flag": cho_unlocked, "outfits": {"school": []}},
                    "Luna": {"ico": "head_luna_2", "flag": luna_unlocked, "outfits": {"school": []}},
                    "Astoria": {"ico": "head_astoria_2", "flag": astoria_unlocked, "outfits": {"school": []}},
                    "Susan": {"ico": "head_susan_2", "flag": susan_unlocked, "outfits": {"school": []}}
                    }

    $ upgrades_categories_sorted = ["Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"]
    $ upgrades_categories_sorted_length = len(upgrades_categories_sorted)

    $ current_category = last_character.capitalize() if last_character else upgrades_categories_sorted[0]
    $ current_item = 0
    $ current_subcategory = "overview"
    $ current_sorting = upgrades_show_locked

    $ category_items = []
    $ menu_items = category_items
    $ menu_items_length = len(menu_items)

    if not renpy.variant("android"):
        show screen mouse_tooltip

    show screen upgrades_menu(xx, yy)
    show screen upgrades_menuitem(xx, yy)
    with d3

    label .after_init:
    $ _return = ui.interact()

    if _return[0] == "category":
        $ current_category = _return[1]
        $ category_items = 0
        $ menu_items = upgrades_sortfilter([], current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_item = 0
    elif _return[0] == "subcat":
        if _return[1] != current_subcategory:
            $ current_subcategory = _return[1]
    else:
        hide screen upgrades_menu
        hide screen upgrades_menuitem
        return

    jump .after_init

screen upgrades_menu(xx, yy):
    tag upgrades_menu
    zorder 30
    modal True

    add im.Blur(screenshot_image, 2)

    use close_button
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"

        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "Show locked:" style "empty" xsize 195 ysize 32 text_align (0.4, 0.5) text_size 12 hover_background btn_hover action ToggleVariable("upgrades_show_locked", True, False)
                add "interface/frames/"+str(interface_color)+"/check_"+str(upgrades_show_locked).lower()+".png" xalign 0.8 ypos 4
        vbox:
            pos (6, 6)
            for category in upgrades_categories_sorted:
                if upgrades_dict[category]["flag"]:
                    frame:
                        style "empty"
                        xysize (195, 50)
                        vbox:
                            textbutton category:
                                style "empty"
                                xysize (195, 48)
                                text_align (0.6, 0.5)
                                text_xanchor 0.5
                                text_size 20
                                if current_category == category:
                                    background "interface/achievements/"+interface_color+"/highlight_left_b.png"
                                else:
                                    hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png"
                                    action Return(["category", category])

                            add "interface/achievements/"+interface_color+"/spacer_left.png"
                        add "interface/achievements/"+interface_color+"/iconbox.png" yoffset 1
                        $ image_zoom = crop_image_zoom("interface/icons/head/"+upgrades_dict.get(category).get("ico")+".png", 42, 42)

                        frame:
                            style "empty"
                            xsize 42
                            ysize 42
                            add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                        add "interface/achievements/glass_iconbox.png" pos (3, 3)

screen upgrades_menuitem(xx, yy):
    tag upgrades_menuitem
    zorder 30
    frame:
        style "empty"
        style_prefix interface_style
        pos (xx+217, yy-53)
        xysize (560, 507)

        add "interface/achievements/"+interface_color+"/panel.png"

        text "Outfit Upgrades" size 22 xalign 0.5 ypos 65

        vpgrid:
            cols 1
            xysize (548, 400)
            pos (6, 101)
            draggable True
            mousewheel True
            scrollbars "vertical"
            xfill True
            yfill True

            # Logic
            for i in upgrades_dict[current_category]["outfits"].itervalues():
                if len(i) > 0 and (i[0].unlocked or upgrades_show_locked):
                    grid 5 1:
                        for x in xrange(5):
                            if x < len(i):
                                frame:
                                    style "empty"
                                    background Solid("#00000080")
                                    xysize (100, 100)
                                    add i[x].get_image() align (1.0, 1.0) zoom 0.1
                                    if i[x].unlocked:
                                        add "interface/topbar/icon_check.png" align (1.0, 1.0)
                                    elif (len(i) <= x+1) and (x > 0) and i[x-1].unlocked:
                                        text "Locked"
                            else:
                                add Null()
