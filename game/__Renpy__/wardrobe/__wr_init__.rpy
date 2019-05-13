

label wardrobe_init:

    if not hasattr(renpy.store,'cho_bg_color') or reset_persistants:

        $ hide_transitions = False
        $ active_girl = "hermione"

        $ wardrobe_page = 0
        $ wardrobe_page_choice = 0
        $ wardrobe_toggle_page = 0
        $ wardrobe_chitchat_active = True

        $ play_wardrobe_music = False
        $ wardrobe_music_active = False
        $ add_wardrobe_sound = False

        $ wr_her_action = "none"

        $ wardrobe_color_update = True
        $ wardrobe_color = "base"

        $ wardrobe_gift_item = 0
        $ wardrobe_costume_selection = 0
        $ wardrobe_uniform_selection = ""

        #Wardrobe Categories
        $ wardrobe_head_category = 0
        $ wardrobe_tops_category = 0
        $ wardrobe_bottoms_category = 0
        $ wardrobe_stockings_category = 0
        $ wardrobe_accessories_category = 0
        $ wardrobe_underwear_category = 0
        $ wardrobe_outfits_category = 0
        $ wardrobe_gifts_category = 0

        #Wardrobe Color Select
        $ wr_background_color            = ["base","red","green","blue"]
        $ wardrobe_hair_style            = "curly"
        $ wardrobe_head_color            = "base"
        $ wardrobe_uniform_color         = "base" #can be: base, red, greed, blue, or yellow.
        $ wardrobe_tops_color            = "base"
        $ wardrobe_bottoms_color         = "base"
        $ wardrobe_other_clothings_color = "base"
        $ wardrobe_accessories_color     = "base"
        $ wardrobe_underwear_color       = "base"
        $ wardrobe_outfits_color         = "base"

        #Wardrobe Icons
        $ icon_xpos_offset = 0
        $ icon_ypos_offset = 0

        $ wardrobe_load_custom_outfit = True

        $ cho_bg_color = [82,150,248,255]
        $ luna_bg_color = [82,150,248,255]

    return

label color_cloth_test:
    $ cho_class.cache_override = True
    $ current_clothing = cho_class.get_cloth("top")
    show screen cloth_test

    $ _return = ui.interact()

    hide screen cloth_test

    if _return[0] == "change_color":
        #$ active_layer = _return[1]
        show screen cloth_test()
        $ current_clothing.set_color(_return[1])
        hide screen cloth_test
        $ cho_class.cache_override = False
    elif _return == "reset":
        $ current_clothing.reset_color()

    jump color_cloth_test


screen cloth_test():
    python:
        if not color_preview == None:
            current_clothing.color[active_layer] = color_preview

    zorder 100
    add cho_class.get_image() xpos 700 yalign 0.5 zoom 0.5 xanchor 0.5 yanchor 0.5

    vbox:
        xpos 850
        ypos 300
        spacing 5
        frame background get_hex_string_tuple(current_clothing.get_color(0)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(1)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(2)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(3)) xsize 50 ysize 50
    vbox:
        xpos 900
        ypos 300
        spacing 5
        textbutton "Channel 1" action Return(["change_color", 0])
        textbutton "Channel 2" action Return(["change_color", 1])
        textbutton "Channel 3" action Return(["change_color", 2])
        textbutton "Channel 4" action Return(["change_color", 3])
        textbutton "Default" action Return("reset")

#label change_color(layer):
    #$ cho_top_school_CLOTH.set_color(layer)

# Equip label from the new wardrobe.
label equip_cho_item(item): # ('_return', will be the id of the clothing item.)

    return

# Toggle 'test_clothing_colors' to True to torn this screen on for Cho.
screen cho_uniform_test():
    tag cho_main

    ### CLOTHES
    if cho_class.get_cloth("bra"):
        add t_cho_bra.get_image() xpos cho_xpos ypos cho_ypos alpha cho_bra_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    #if cho_wear_stockings:
    #    add t_cho_stockings xpos cho_xpos ypos cho_ypos alpha cho_stockings_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    #if cho_wear_garterbelt:
    #    add t_cho_garterbelt xpos cho_xpos ypos cho_ypos alpha cho_panties_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_panties:
        add t_cho_panties.get_image() xpos cho_xpos ypos cho_ypos alpha cho_panties_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_bottom:
        add t_cho_bottom.get_image() xpos cho_xpos ypos cho_ypos alpha cho_bottom_transp xzoom cho_flip zoom (1.0/cho_scaleratio)

    # Tops
    # One image for the torso, one for the left side sleeve layer if the item has sleeves. Sleeves will be ignored if they're set to blank.
    if cho_wear_top:
        # Add left side arm sleeve here, before the torso layer.
        if t_cho_top_L.id in ["top_sweater_1"]: # Automate this process so we don't have to manually add ids to that list. Maybe add a variable to the class or check if the layers start with an 'L_' or 'R_' in the folder.
            add t_cho_top_L.get_image() xpos cho_xpos ypos cho_ypos alpha cho_top_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
        add t_cho_top_mid.get_image() xpos cho_xpos ypos cho_ypos alpha cho_top_transp xzoom cho_flip zoom (1.0/cho_scaleratio)


    # left side glove layer.
    if cho_wear_gloves:
        add cho_gloves xpos cho_xpos ypos cho_ypos alpha cho_gloves_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # 'L'

    # robe torso and left side sleeve that gets put on top of her left side glove, sleeves, and arm.
    #if cho_wear_robe: # Robes will also need the torso and sleeve layers for the different arms.
    #    if t_cho_robe_L != "blank": # left side sleeve.
    #        add t_cho_robe_L xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Sleeve 'L'
    #    add t_cho_robe_mid xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Torso 'mid'



    # right side arm and hand layer, that gets layered on top of her bottom and top items.
    add cho_l_hand xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Arm 'R'

    # right side sleeve layer for the top that gets put on top of her hand.
    if cho_wear_top:
        if t_cho_top_L.id in ["top_sweater_1"]: # right side sleeve.
           add t_cho_top_L.get_image() xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Sleeve 'R'

    # right side glove layer that gets put on top of her hand and top item, but below the robe.
    #if cho_wear_gloves:
    #    add cho_gloves xpos cho_xpos ypos cho_ypos alpha cho_gloves_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Gloves 'R'

    # right side sleeve for the robe that gets put on top of gloves, sleeves, and her arm.
    #if cho_wear_robe:
    #    add cho_robe xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Robe Sleeve 'R'



    #if cho_wear_neckwear:
    #    add cho_neckwear xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    ### ZORDER
    zorder cho_zorder