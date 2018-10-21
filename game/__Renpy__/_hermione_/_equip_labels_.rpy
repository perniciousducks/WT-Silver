

###EQUIPPING LABELS###

#Hair equip.
label set_her_hair(hair_style="A", color=1): #Not in use
    hide screen hermione_main
    $ h_hair_style = hair_style
    $ h_hair_color = color
    call update_her_hair #Hermione_layering.rpy
    show screen hermione_main
    return

label set_her_hair_style(hair_style = "A"):
    hide screen hermione_main
    $ h_hair_style = hair_style
    call update_her_hair #Hermione_layering.rpy
    call update_her_uniform #updates cat ears
    show screen hermione_main
    return

label set_her_hair_color(hair_color = 1):
    hide screen hermione_main
    $ h_hair_color = hair_color
    call update_her_hair #Hermione_layering.rpy
    call update_her_uniform #updates cat ears
    show screen hermione_main
    return

#Makeup equip.
label set_h_makeup(makeup = ""):
    hide screen hermione_main
    if makeup in hermione_makeup_list:
        $ hermione_makeup_list.remove(makeup)
    else:
        $ hermione_makeup_list.append(makeup)

    if hermione_makeup_list == []:
        $ h_request_wear_makeup = False
        $ hermione_wear_makeup = False
    else:
        $ h_request_wear_makeup = True
        $ hermione_wear_makeup = True
    call update_her_uniform
    show screen hermione_main
    return

#Glasses equip.
label set_h_glasses(glasses="", color=""):
    hide screen hermione_main
    if h_request_wear_glasses and (h_glasses == glasses and h_glasses_color == color):
        $ h_request_wear_glasses = False
        $ hermione_wear_glasses = False
    else:
        $ h_request_wear_glasses = True
        $ hermione_wear_glasses = True
        $ h_glasses = glasses
        $ h_glasses_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Ears equip.
label set_h_ears(ears=""):
    hide screen hermione_main
    if h_request_wear_ears and h_ears == ears:
        $ h_request_wear_ears = False
        $ hermione_wear_ears = False
    else:
        $ h_request_wear_ears = True
        $ hermione_wear_ears = True
        $ h_ears = ears
        if h_ears == "elf_ears":
            call set_her_hair_style("B")
    call update_her_uniform
    show screen hermione_main
    return

#Hat equip.
label set_h_hat(hat=""):
    hide screen hermione_main
    if h_request_wear_hat and h_hat == hat:
        $ h_request_wear_hat = False
        $ hermione_wear_hat = False
    else:
        $ h_request_wear_hat = True
        $ hermione_wear_hat = True
        $ h_hat = hat
    call update_her_uniform
    show screen hermione_main
    return

#Top equip.
label set_h_top(top="", color=""):
    hide screen hermione_main
    $ h_request_wear_top = True
    $ hermione_wear_top = True
    if h_request_wear_bottom:
        $ hermione_wear_bottom = True
    $ h_top = top
    $ h_top_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Bottom equip.
label set_h_bottom(bottom="", color=""):
    hide screen hermione_main
    $ h_request_wear_bottom = True
    $ hermione_wear_bottom = True
    if h_request_wear_top:
        $ hermione_wear_top = True
    $ h_skirt = bottom
    $ h_skirt_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Bra equip.
label set_h_bra(bra="", color=""):
    hide screen hermione_main
    $ h_request_wear_bra = True
    $ hermione_wear_bra = True
    if h_bra == bra and h_bra_color == color:
        pass
    else:
        $ h_bra = bra
        $ h_bra_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Onepiece equip.
label set_h_onepiece(onepiece=""):
    hide screen hermione_main
    if h_onepiece == onepiece and hermione_wear_onepiece: #Off toggle
        $ h_request_wear_onepiece = False
        $ hermione_wear_onepiece = False
    else:
        $ h_request_wear_onepiece = True
        $ hermione_wear_onepiece = True
        $ h_onepiece = onepiece
    call update_her_uniform
    show screen hermione_main
    return

#Panties equip.
label set_h_panties(panties="", color=""):
    hide screen hermione_main
    $ h_request_wear_panties = True
    $ hermione_wear_panties = True
    if h_panties == panties and h_panties_color == color: #Off toggle
        pass
    else:
        $ h_panties = panties
        $ h_panties_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Garterbelt equip.
label set_h_garterbelt(garterbelt="", color=""):
    hide screen hermione_main
    if h_garterbelt == garterbelt and hermione_wear_garterbelt:
        $ h_request_wear_garterbelt = False
        $ hermione_wear_garterbelt = False
    else:
        $ h_request_wear_garterbelt = True
        $ hermione_wear_garterbelt = True
        $ h_garterbelt = garterbelt
        $ h_garterbelt_color = color
    call update_her_uniform
    show screen hermione_main
    return

#Neackwear equip.
label set_h_neckwear(neck=""):
    hide screen hermione_main
    if h_neckwear == neck and hermione_wear_neckwear: #Off toggle
        $ h_request_wear_neckwear = False
        $ hermione_wear_neckwear = False
    else:
        $ h_request_wear_neckwear = True
        $ hermione_wear_neckwear = True
        $ h_neckwear = neck
    call update_her_uniform
    show screen hermione_main
    return

#Body accs equip.
label set_h_body_accessory(accessory=""):
    if accessory in hermione_body_accs_list:
        $ hermione_body_accs_list.remove(accessory)
    else:
        $ hermione_body_accs_list.append(accessory)

    if hermione_body_accs_list == []:
        $ h_request_wear_body_accs = False
        $ hermione_wear_body_accs = False
    else:
        $ h_request_wear_body_accs = True
        $ hermione_wear_body_accs = True
    call update_chibi_uniform
    call update_her_uniform
    show screen hermione_main
    return

#Gloves Equip.
label set_h_gloves(gloves=""):
    hide screen hermione_main
    if h_gloves == gloves and hermione_wear_gloves: #Off toggle
        $ h_request_wear_gloves = False
        $ hermione_wear_gloves = False
    else:
        $ h_request_wear_gloves = True
        $ hermione_wear_gloves = True
        $ h_gloves = gloves
    call update_her_uniform
    show screen hermione_main
    return

#Stockings equip.
label set_h_stockings(stockings=""):
    hide screen hermione_main
    if h_stockings == stockings: #Off toggle
        $ h_request_wear_stockings = False
        $ hermione_wear_stockings = False
    else:
        $ h_request_wear_stockings = True
        $ hermione_wear_stockings = True
        $ h_stockings = stockings
    call update_her_uniform
    show screen hermione_main
    return

#Robe equip.
label set_h_robe(robe=""):
    hide screen hermione_main
    if h_robe == robe:
        $ h_request_wear_robe = False
        $ hermione_wear_robe = False
    else:
        $ h_request_wear_robe = True
        $ hermione_wear_robe = True
        $ h_robe = robe
    call update_her_uniform
    show screen hermione_main
    return

#Buttplug equip.
label set_h_buttplug(buttplug=""):
    hide screen hermione_main
    if buttplug == "None" or buttplug == "" or buttplug == "remove":
        $ h_request_wear_buttplug = False
        $ hermione_wear_buttplug = False
    else:
        $ h_request_wear_buttplug = True
        $ hermione_wear_buttplug = True
        $ h_buttplug = buttplug
    call update_her_uniform
    show screen hermione_main
    return

#Piercings equip.
label set_h_piercing(piercing="", color=""):
    hide screen hermione_main
    if piercing in ear_piercings_list:
        if h_ear_piercing == piercing and h_ear_piercing_color == color:
            $ h_ear_piercing = "00_blank"
        else:
            $ h_ear_piercing = piercing_choice
    if piercing in nipple_piercings_list:
        if h_nipple_piercing == piercing and h_nipple_piercing_color == color:
            $ h_nipple_piercing = "00_blank"
        else:
            $ h_nipple_piercing = piercing
    if piercing in belly_piercings_list:
        if h_belly_piercing == piercing and h_belly_piercing_color == color:
            $ h_belly_piercing = "00_blank"
        else:
            $ h_belly_piercing = piercing
    if piercing in intimate_piercings_list:
        if h_belly_piercing == piercing and h_intimate_piercing_color == color:
            $ h_belly_piercing = "00_blank"
        else:
            $ h_belly_piercing = piercing

    if h_ear_piercing == "00_blank" and h_nipple_piercing == "00_blank" and h_belly_piercing == "00_blank" and h_intimate_piercing == "00_blank": #No piercings equipped.
        $ h_request_wear_piercings = False
        $ hermione_wear_piercings = False
    else:
        $ h_request_wear_piercings = True
        $ hermione_wear_piercings = True

    call update_her_uniform
    show screen hermione_main
    return

## Outfit Equips
label set_hermione_outfit(outfit): #This gets used outside the wardrobe.
    show screen blkfade
    hide screen hermione_main
    with d3
    call h_outfit_OBJ(outfit)
    pause .5
    show screen hermione_main
    hide screen blkfade
    with d5
    return

label h_outfit_OBJ(outfit):
    if outfit == None:
        $ h_request_wear_outfit = False
        $ hermione_costume = False
        call update_her_uniform
        call h_update_hair
    else:
        $ h_request_wear_outfit = True
        $ hermione_costume = True

        $ h_request_wear_top = True
        $ hermione_wear_top = True

        $ hermoine_outfit_GLBL = outfit

        if hermoine_outfit_GLBL.hair_layer != "":
            $ h_hair_style = hermoine_outfit_GLBL.getHairLayers()
            $ h_hair_color = 1
        if hermoine_outfit_GLBL.top_layers != []:
            $ h_request_wear_hat = True
            $ h_hat = hermoine_outfit_GLBL.getTopLayers()

        call load_hermione_clothing_saves
        call update_her_uniform
        call h_update_hair

    return

label h_equip_temp_outfit(outfit):
    if temp_outfit_GLBL == None:
        $ temp_outfit_GLBL = hermoine_outfit_GLBL
        $ temp_weir = h_request_wear_outfit
        $ temp_costume = hermione_costume

    call h_outfit_OBJ(outfit)
    return

label h_unequip_temp_outfit():
    $ hermoine_outfit_GLBL = temp_outfit_GLBL
    if temp_weir and  temp_costume:
        call h_outfit_OBJ(temp_outfit_GLBL)
    else:
        call h_outfit_OBJ(None)
    $ temp_outfit_GLBL = None
    return


#Hermione Action

label set_hermione_action(action="", update=""):
    hide screen hermione_main
    call h_action(action,update)

    show screen hermione_main
    with d3

    return


label h_action(action =  "", update=""):

    if action == "" or action == "none" or action == "None" or action == 0:

        $ hermione_action = "none"
        $ hermione_use_action = False

        $ h_right_arm        = "right_1"
        $ h_left_arm         = "left_1"
        $ h_action_top = ""
        $ h_action_bottom = ""
        $ h_action_gloves = ""

        $ h_action_a = "00_blank.png"
        $ h_action_b = "00_blank.png"
        $ hermione_action_a = "characters/hermione/body/arms/left/00_blank.png"
        $ hermione_action_b = "characters/hermione/body/arms/left/00_blank.png"
        $ hermione_costume_action_a = "characters/hermione/clothes/custom/00_blank.png"
        $ milking           = 0


        if update == "update":

            call load_hermione_clothing_saves

    else:

        if hermione_costume:
            if action in hermoine_outfit_GLBL.actions:
                $ hermione_use_action = True
                $ h_action_a = hermoine_outfit_GLBL.getActionImage(action)
            else:
                $ hermione_use_action = False
                $ h_action_a = "00_blank.png"

        else:

            ### LIFT SKIRT ###
            if action == "lift_skirt":
                $ hermione_action = "lift_skirt"
                $ hermione_use_action = True

            ### LIFT TOP ###
            if action == "lift_top":
                $ hermione_action = "lift_top"
                $ hermione_use_action = True

            ### HOLD BOOK ###
            if action == "hold_book":
                $ hermione_action = "hold_book"
                $ hermione_use_action = True

            ### LIFT BREASTS ###
            if action == "lift_breasts" or action == "lift_breasts_large":
                $ hermione_action = "lift_breasts"
                $ hermione_use_action = True

                if action == "lift_breasts_large":
                    $ hermione_expand_breasts = True



            ### NAKED ACTIONS ###

            #Lift breasts
            if action == "lift_breasts_naked" or action == "lift_breasts_large_naked":
                $ hermione_action = "lift_breasts"
                $ hermione_use_action = True

                $ hermione_wear_bottom = False
                $ hermione_wear_panties = False
                $ hermione_wear_garterbelt = False
                $ hermione_wear_stockings = False

                if action == "lift_breasts_large_naked":
                    $ hermione_expand_breasts = True

            #Hands Behind
            if action == "hands_behind":
                $ hermione_action = "hands_behind"
                $ hermione_use_action = True

            #Covering
            if action == "covering":
                $ hermione_action = "covering"
                $ hermione_use_action = True

            if action == "covering_uniform":
                $ hermione_action = "covering_uniform"
                $ hermione_use_action = True

            if action == "covering_cloak":
                $ hermione_action = "covering_cloak"
                $ hermione_use_action = True

            #Fingering
            if action == "fingering":
                $ hermione_action = "fingering"
                $ hermione_use_action = True

            #Covering Top
            if action == "covering_top":
                $ hermione_action = "covering_top"
                $ hermione_use_action = True

            #Pinch
            if action == "pinch":
                $ hermione_action = "pinch"
                $ hermione_use_action = True

            #Hands Cuffed
            if action == "hands_cuffed":
                $ hermione_action = "hands_cuffed"
                $ hermione_use_action = True

            #Milk Breasts
            if action == "milk_breasts":
                $ hermione_action = "milk_breasts"
                $ hermione_use_action = True


            ### NO hermione_action CHANGE ###

            #Temporarily expand Hermione #Resets after 5 days.
            if action == "expand_breasts":
                $ hermione_expand_breasts_counter = 5
                $ hermione_expand_breasts = True

            if action == "expand_ass":
                $ hermione_expand_ass_counter = 5
                $ hermione_expand_ass = True

            if action == "expand_all":
                $ hermione_expand_breasts_counter = 5
                $ hermione_expand_ass_counter = 5
                $ hermione_expand_breasts = True
                $ hermione_expand_ass = True

            #Strip Naked
            if action == "hands_free" or action == "naked" or action == "strip":
                $ hermione_wear_top = False
                $ hermione_wear_bra = False
                $ hermione_wear_bottom = False
                $ hermione_wear_panties = False
                $ hermione_wear_garterbelt = False
                $ hermione_wear_neckwear = False
                $ hermione_wear_body_accs = False
                $ hermione_wear_gloves = False
                $ hermione_wear_stockings = False
                $ hermione_wear_robe = False


    call update_her_uniform #calls update_her_action, update_chibi_uniform, and h_update_body;

    return

label set_h_action_vars:
    $ hermione_action_right_arm = "characters/hermione/body/arms/right/"+str(h_action_right_arm)
    $ hermione_action_left_arm = "characters/hermione/body/arms/left/"+(h_action_left_arm)
    $ hermione_action_a = "characters/hermione/clothes/uniform/action/"+str(h_action_a)
    $ hermione_action_b = "characters/hermione/clothes/uniform/action/"+str(h_action_b)
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/"+str(h_action_a)
    return
