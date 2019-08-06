

### CALL WARDROBE LABELS ###

label wardrobe: #NOT IN USE
    call reset_wardrobe_vars
    #call update_wr_lists       #updates all lists

    if active_girl == "hermione":
        call her_main(xpos="wardrobe")
    #if active_girl == "luna":
    #    call lun_main("",xpos="wardrobe")
    if active_girl == "susan":
        call sus_main(xpos="wardrobe")

    hide screen main_room_menu
    call screen wardrobe

label reset_wardrobe_vars:
    $ wardrobe_page = 0
    $ wardrobe_page_choice = 0
    $ hide_transitions = True
    $ wardrobe_toggle_page = 0            #default page
    $ wardrobe_head_category = 0          #default page
    $ wardrobe_tops_category = 0          #default page
    $ wardrobe_bottoms_category = 0       #default page
    $ wardrobe_stockings_category = 0     #default page
    $ wardrobe_accessories_category = 0   #default page
    $ wardrobe_underwear_category = 0     #default page
    $ wardrobe_outfits_category = 0       #default page
    $ wardrobe_gifts_category = 0         #default page
    $ wardrobe_load_custom_outfit = True  #False = save custom outfit.

    $ wr_action_list = []

    if active_girl == "hermione":
        $ wr_action_list = ["no pose"]
        if her_whoring >= 9:
            $ wr_action_list.append("lift top")
        if her_whoring >= 6:
            $ wr_action_list.append("lift bottom")
        if her_whoring >= 11:
            $ wr_action_list.append("covering")
        if her_whoring >= 14:
            $ wr_action_list.append("presenting")
            $ wr_action_list.append("behind")
        if her_whoring >= 17:
            $ wr_action_list.append("fingering")
            $ wr_action_list.append("pinching")
        if her_whoring >= 20:
            $ wr_action_list.append("cuffed")
        if her_whoring >= 14:
            $ wr_action_list.append("strip")

        $ wr_base_hair_style = "curly" #Throwaway variable. Doesn't get updated.
        $ wr_base_hair_color = "brown" #Throwaway variable. Doesn't get updated.

    elif active_girl == "luna":
        $ wr_base_hair_style = "curly"
        $ wr_base_hair_color = "blonde"
    elif active_girl == "susan":
        $ wr_base_hair_style = "braided"
        $ wr_base_hair_color = "red"

    $ wardrobe_head_color             = "base"
    $ wardrobe_uniform_color          = "base"
    $ wardrobe_tops_color             = "base"
    $ wardrobe_bottoms_color          = "base"
    $ wardrobe_stockings_color        = "base"
    $ wardrobe_other_clothings_color  = "base"
    $ wardrobe_accessories_color      = "base"
    $ wardrobe_underwear_color        = "base"
    $ wardrobe_outfits_color          = "base"

    #Music
    if play_wardrobe_music:
        if not wardrobe_music_active:
            $ wardrobe_music_active = True
            call play_music("my_immortal")

    return

label return_to_wardrobe:
    if not hide_transitions:
        if active_girl == "hermione":
            call her_main(face="happy",xpos="wardrobe",ypos="base",trans="fade")
        if active_girl == "luna":
            call lun_main(eye="base", mouth='base',xpos="wardrobe",ypos="base",trans="fade")
        if active_girl == "susan":
            call sus_main(face="happy",xpos="wardrobe",ypos="base",trans="fade")

        $ hide_transitions = True
        call screen wardrobe

    else:
        $ hide_transitions = True

        if active_girl == "hermione":
            call her_main(face="happy",xpos="wardrobe",ypos="base")
        if active_girl == "luna":
            call lun_main(eye="base", mouth='base',xpos="wardrobe",ypos="base")
        if active_girl == "susan":
            call sus_main(face="happy",xpos="wardrobe",ypos="base")

        call screen wardrobe


### UPDATE WARDROBE COLOR PALETTE ###

label update_wardrobe_color:

    if active_girl == "hermione":
        call her_main(xpos="wardrobe",ypos="base")
    if active_girl == "luna":
        call lun_main(xpos="wardrobe",ypos="base")
    if active_girl == "susan":
        call sus_main(xpos="wardrobe",ypos="base")

    hide screen main_room_menu
    call screen wardrobe

label wardrobe_update:

    if wardrobe_page_choice == 0: #Default
        call update_wr_color_list
        $ wardrobe_page = 0
    if wardrobe_page != 1 and wardrobe_page_choice == 1:
        call update_wr_head_list
        $ wardrobe_page = 1
    if wardrobe_page != 2 and wardrobe_page_choice == 2:
        call update_wr_tops_list
        $ wardrobe_page = 2
    if wardrobe_page != 3 and wardrobe_page_choice == 3:
        call update_wr_bottoms_list
        $ wardrobe_page = 3
    if wardrobe_page != 4 and wardrobe_page_choice == 4:
        call update_wr_other_clothings_list
        $ wardrobe_page = 4
    if wardrobe_page != 5 and wardrobe_page_choice == 5:
        call update_wr_miscellaneous_list
        $ wardrobe_page = 5
    if wardrobe_page != 6 and wardrobe_page_choice == 6:
        call update_wr_underwear_list
        call update_wr_other_clothings_list #For stockings
        $ wardrobe_page = 6
    if wardrobe_page != 7 and wardrobe_page_choice == 7:
        call update_wr_outfits_list
        $ wardrobe_page = 7
    if wardrobe_page != 8 and wardrobe_page_choice == 8: #gifts
        $ wardrobe_page = 8

    #Music
    if play_wardrobe_music:
        if not wardrobe_music_active:
            $ wardrobe_music_active = True
            call play_music("my_immortal")
    else:
        if wardrobe_music_active:
            $ wardrobe_music_active = False
            call music_block

    #Sound Effects
    if add_wardrobe_sound: #False by default. Only happens on a "wardrobe_page" change.
        if wardrobe_page == 0:
            $ renpy.play('sounds/door2.mp3') #closing wardrobe page
        else:
            $ renpy.play('sounds/scroll.mp3') #opening wardrobe page
    $ add_wardrobe_sound = False

    if active_girl == "hermione":
        call wr_her_clothing_reset
        call her_main(xpos="wardrobe",ypos="base")
    if active_girl == "luna":
        call wr_lun_clothing_reset
        call lun_main(xpos="wardrobe",ypos="base")
    if active_girl == "susan":
        call wr_sus_clothing_reset
        call sus_main(xpos="wardrobe",ypos="base")

    hide screen main_room_menu
    call screen wardrobe

label wr_her_clothing_reset:
    #Reload Clothing
    call load_hermione_clothing_saves

    #Qol stuff
    if wardrobe_page != 6:
        if hermione_action != "none":
            $ hermione_use_action = True
    else: #Underwear page Qol
        $ hermione_use_action = False #Hide Action so Underwear can be turned on.
        $ hermione_wear_robe = False
        if her_whoring >= 12:
            $ hermione_wear_top = False
            $ hermione_wear_bottom = False

    call update_her_uniform

    return

label wr_lun_clothing_reset:
    #Reload Clothing
    call load_luna_clothing_saves

    #Qol stuff
    if wardrobe_page != 6:
        pass
    #    if luna_action != "none":
    #        $ luna_use_action = True
    else: #Underwear page Qol
        $ luna_wear_robe = False
        $ luna_wear_top = False
        $ luna_wear_bottom = False

    call update_lun_uniform

    return

label wr_sus_clothing_reset:
    #Reload Clothing
    call load_susan_clothing_saves

    #Qol stuff
    if wardrobe_page != 6:
        pass
    #    if susan_action != "none":
    #        $ susan_use_action = True
    else: #Underwear page Qol
        $ susan_wear_robe = False
        $ susan_wear_top = False
        $ susan_wear_bottom = False

    call update_sus_uniform

    return

### CLOSE WARDROBE LABELS ###

label hide_wardrobe:
    call ctc
    call screen wardrobe

label close_wardrobe:
    $ renpy.play('sounds/door2.mp3') #closing wardrobe page
    #Music
    if wardrobe_music_active:
        $ wardrobe_music_active = False
        call music_block

    if active_girl == "hermione":
        call set_her_face(change="all")
        call her_main(xpos="base",ypos="base") #reset hermione face and position to default
        jump hermione_requests

    if active_girl == "luna":
        call lun_main(xpos="base",ypos="base")
        pause.2
        call lun_chibi("stand","mid","base")
        jump luna_requests
    if active_girl == "susan":
        call sus_main(xpos="base",ypos="base")
        jump susan_requests

### Pose/Action ###

#Change Hermione's Pose/Action
label wardrobe_change_her_action:
    hide screen hermione_main

    if wr_her_action == "no pose":
        call set_her_action("none","update")
    if wr_her_action == "lift top":
        call set_her_action("lift_top")
    if wr_her_action == "lift bottom":
        call set_her_action("lift_skirt")
    if wr_her_action == "presenting":
        call set_her_action("lift_breasts")
    if wr_her_action == "behind":
        call set_her_action("hands_behind")
    if wr_her_action == "covering":
        call set_her_action("covering")
    if wr_her_action == "fingering":
        call set_her_action("fingering")
    if wr_her_action == "pinching":
        call set_her_action("pinch")
    if wr_her_action == "cuffed":
        call set_her_action("hands_cuffed")
    if wr_her_action == "strip":
        call set_her_action("naked")

    call her_main(xpos="wardrobe")
    call screen wardrobe



### Randomizing Her Face ###
label touched_her_boobies:
    if her_whoring >= 0 and her_whoring < 11:
        call set_her_face(mouth="annoyed", eyes="annoyed")
    elif her_whoring >= 11 and her_whoring < 14:
        call set_her_face(mouth="happy", eyes="happy")
    else:
        call set_her_face(mouth="naughty", eyes="naughty")

    call her_main(xpos="wardrobe")
    call screen wardrobe

label touched_her_crotch:
    if her_whoring >= 0 and her_whoring < 5:
        call set_her_face(mouth="angry", eyes="angry")
    elif her_whoring >= 5 and her_whoring < 17:
        call set_her_face(mouth="annoyed", eyes="annoyed")
    elif her_whoring >= 17 and her_whoring < 20:
        call set_her_face(mouth="happy", eyes="happy")
    else:
        call set_her_face(mouth="naughty", eyes="naughty")

    call her_main(xpos="wardrobe")
    call screen wardrobe

### TOGGLE LABELS ###

label wardrobe_chitchat_toggle:

    if wardrobe_chitchat_active:
        $ wardrobe_chitchat_active = False
    else:
        $ wardrobe_chitchat_active = True

    call screen wardrobe

# Top Toggle #
label top_toggle:
    if active_girl == "hermione":
        call her_top_toggle
    #if active_girl == "luna":
    #    call lun_top_toggle
    #if active_girl == "astoria":
    #    call ast_top_toggle

label her_top_toggle:
    hide screen hermione_main
    if h_request_wear_top:
        $ h_request_wear_top = False
        $ hermione_wear_top = False
    else:
        $ h_request_wear_top = True
        $ hermione_wear_top = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Bra Toggle #
label her_bra_toggle:
    hide screen hermione_main
    if h_request_wear_bra: #Toggle OFF
        $ h_request_wear_bra = False
        $ hermione_wear_bra = False
        call update_her_uniform

        if her_whoring >= 11 and her_whoring < 15:
            call set_her_face(mouth="annoyed", eyes="annoyed")
        else: #21+
            call set_her_face(mouth="naughty", eyes="naughty")

    else: #Toggle ON
        $ h_request_wear_bra = True
        $ hermione_wear_bra = True
        call update_her_uniform

        if her_whoring >= 11 and her_whoring < 15:
            call set_her_face(mouth="annoyed", eyes="annoyed")
        elif her_whoring >= 15 and her_whoring < 21:
            call set_her_face(mouth="neutral", eyes="neutral")
        else: #21+
            call set_her_face(mouth="happy", eyes="happy")

    call her_main(xpos="wardrobe",ypos="base")
    hide screen wardrobe
    call screen wardrobe

# One-Piece Toggle #
label her_onepiece_toggle:
    if h_onepiece == "blank":
        hide screen wardrobe
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_onepiece:
        $ h_request_wear_onepiece = False
        $ hermione_wear_onepiece = False
    else:
        $ h_request_wear_onepiece = True
        $ hermione_wear_onepiece = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Bottom Toggle #
label her_bottom_toggle:
    hide screen hermione_main
    if h_request_wear_bottom:
        $ h_request_wear_bottom = False
        $ hermione_wear_bottom = False
    else:
        $ h_request_wear_bottom = True
        $ hermione_wear_bottom = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Panties Toggle
label her_panties_toggle:
    hide screen hermione_main
    if h_request_wear_panties: #Toggle OFF
        $ h_request_wear_panties = False
        $ hermione_wear_panties = False
        call update_her_uniform

        if her_whoring < 15:
            call set_her_face(mouth="annoyed", eyes="annoyed")
        else: #21+
            call set_her_face(mouth="naughty", eyes="naughty")

    else: #Toggle ON
        $ h_request_wear_panties = True
        $ hermione_wear_panties = True
        call update_her_uniform

        if her_whoring < 15:
            call set_her_face(mouth="annoyed", eyes="annoyed")
        elif her_whoring >= 15 and her_whoring < 21:
            call set_her_face(mouth="neutral", eyes="neutral")
        else: #21+
            call set_her_face(mouth="happy", eyes="happy")

    call her_main(xpos="wardrobe",ypos="base")
    hide screen wardrobe
    call screen wardrobe

# Garterbelt Toggle #
label her_garterbelt_toggle:
    if h_garterbelt == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_garterbelt:
        $ h_request_wear_garterbelt = False
        $ hermione_wear_garterbelt = False
    else:
        $ h_request_wear_garterbelt = True
        $ hermione_wear_garterbelt = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

### Other Clothings ###
# Neckwear Toggle #
label her_neckwear_toggle:
    if h_neckwear == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_neckwear:
        $ h_request_wear_neckwear = False
        $ hermione_wear_neckwear = False
    else:
        $ h_request_wear_neckwear = True
        $ hermione_wear_neckwear = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Body Accessories Toggle #
label her_body_accs_toggle:
    if hermione_body_accs_list == []: #Empty list
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_body_accs:
        $ h_request_wear_body_accs = False
        $ hermione_wear_body_accs = False
    else:
        $ h_request_wear_body_accs = True
        $ hermione_wear_body_accs = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Gloves Toggle #
label her_gloves_toggle:
    if h_gloves == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_gloves:
        $ h_request_wear_gloves = False
        $ hermione_wear_gloves = False
    else:
        $ h_request_wear_gloves = True
        $ hermione_wear_gloves = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Stockings Toggle #
label her_stockings_toggle:
    if h_stockings == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_stockings:
        $ h_request_wear_stockings = False
        $ hermione_wear_stockings = False
    else:
        $ h_request_wear_stockings = True
        $ hermione_wear_stockings = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Robe Toggle #
label her_robe_toggle:
    hide screen hermione_main
    if h_request_wear_robe:
        $ h_request_wear_robe = False
        $ hermione_wear_robe = False
    else:
        $ h_request_wear_robe = True
        $ hermione_wear_robe = True
    call update_her_uniform
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe

# Outfit Toggle #
label her_outfit_toggle:
    if hermoine_outfit_GLBL == None:
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if hermione_wear_outfit:
        $ h_request_wear_outfit = False
        $ hermione_wear_outfit = False
    else:
        $ h_request_wear_outfit = True
        $ hermione_wear_outfit = True
    call update_her_uniform
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe

### ACCESSORIES TOGGLE ###

# Hat Toggle #
label her_hat_toggle:
    if h_hat == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_hat:
        $ h_request_wear_hat = False
        $ hermione_wear_hat = False
    else:
        $ h_request_wear_hat = True
        $ hermione_wear_hat = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Glasses Toggle #
label her_glasses_toggle:
    if h_glasses == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_glasses:
        $ h_request_wear_glasses = False
        $ hermione_wear_glasses = False
    else:
        $ h_request_wear_glasses = True
        $ hermione_wear_glasses = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Ears Toggle #
label her_ears_toggle:
    if h_ears == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_ears:
        $ h_request_wear_ears = False
        $ hermione_wear_ears = False
    else:
        $ h_request_wear_ears = True
        $ hermione_wear_ears = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Makeup Toggle #
label her_makeup_toggle:
    if hermione_makeup_list == []: #Empty list
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_makeup:
        $ h_request_wear_makeup = False
        $ hermione_wear_makeup = False
    else:
        $ h_request_wear_makeup = True
        $ hermione_wear_makeup = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Piercings Toggle #
label her_piercings_toggle:
    if h_ear_piercing == "blank" and h_nipple_piercing == "blank" and h_belly_piercing == "blank" and h_genital_piercing == "blank":
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_piercings:
        $ h_request_wear_piercings = False
        $ hermione_wear_piercings = False
    else:
        $ h_request_wear_piercings = True
        $ hermione_wear_piercings = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Tattoos Toggle #
label her_tattoos_toggle:
    if hermione_tattoos_list == []: #Empty list
        ">No item equipped."
        call screen wardrobe
    hide screen hermione_main
    if h_request_wear_tattoos:
        $ h_request_wear_tattoos = False
        $ hermione_wear_tattoos = False
    else:
        $ h_request_wear_tattoos = True
        $ hermione_wear_tattoos = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

#label her_toggle: #NOT WORKING Might work with: getattr()
#    hide screen hermione_main
#    if h_request_wear_"+str(toggle_obj)+":
#        $ h_request_wear_"+str(toggle_obj)+" = False
#        $ hermione_wear_"+str(toggle_obj)+" = False
#    else:
#        $ h_request_wear_"+str(toggle_obj)+" = True
#        $ hermione_wear_"+str(toggle_obj)+" = True
#    call update_her_uniform
#    show screen hermione_main
#    call screen wardrobe










### MISCELLANEOUS SECTION ###

## Piercings ##
label equip_piercing:
    if active_girl == "hermione":
        call set_her_piercing(piercing_choice)
    jump return_to_wardrobe



## Tattoos ##
label equip_tattoo:
    if tattoo_choice in hermione_tattoos_list:
        $ hermione_tattoos_list.remove(tattoo_choice)
    else:
        $ hermione_tattoos_list.append(tattoo_choice)

    if hermione_tattoos_list == []:
        $ h_request_wear_tattoos = False
        $ hermione_wear_tattoos = False
    else:
        $ h_request_wear_tattoos = True
        $ hermione_wear_tattoos = True

    jump return_to_wardrobe



label wardrobe_fail(text=""):
    hide screen wardrobe
    if text != "":
        call nar(">[text]")

    return




### GIFTS SECTION ###

## Gifts ##
label wardrobe_give_gift:
    call give_her_gift(wardrobe_gift_item)
    jump return_to_wardrobe

## Potions ## Not in use ## Move to Accessories
label wardrobe_give_potion:
    hide screen wardrobe_gifts
    $ renpy.jump("potion_scene_"+str(wardrobe_potion))
