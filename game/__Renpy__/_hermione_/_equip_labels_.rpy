

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
label set_h_onepiece(onepiece="", color=""):
    hide screen hermione_main
    if h_onepiece == onepiece and h_onepiece_color == color and hermione_wear_onepiece: #Off toggle
        $ h_request_wear_onepiece = False
        $ hermione_wear_onepiece = False
    else:
        $ h_request_wear_onepiece = True
        $ hermione_wear_onepiece = True
        $ h_onepiece = onepiece
        $ h_onepiece_color = color
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
