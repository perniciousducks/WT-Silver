

###EQUIPPING LABELS###

#Hair equip.
label set_her_hair(style="", color=""): #Not in use
    hide screen hermione_main
    if style  != "":
        $ h_hair_style = style
    if color != "":
        $ h_hair_color = color

    #Hair
    if h_hair_style in ["curly","updo","bobcut"]:
        $ hermione_hair_base = "characters/hermione/body/head/" +str(h_hair_style)+ "_" +str(h_hair_color)+ ".png"
        $ hermione_hair_top = "characters/hermione/body/head/" +str(h_hair_style)+ "_" +str(h_hair_color)+ "_top.png"
    else:
        $ hermione_hair_base = "characters/hermione/body/head/misc/" +str(h_hair_style)+ ".png"
        $ hermione_hair_top = "characters/hermione/body/head/misc/" +str(h_hair_style)+ "_top.png"

    #Ears
    if h_ears == "cat_ears":
        if h_hair_style in ["curly","updo","bobcut"]:
            $ hermione_ears = "characters/hermione/clothes/ears/hair_"+str(h_hair_style)+"/"+str(h_ears)+"_"+str(h_hair_color)+".png"
        else:
            $ hermione_ears = "characters/hermione/clothes/ears/hair_curly/"+str(h_ears)+"_"+str(h_hair_color)+".png"
    else:
        $ hermione_ears = "characters/hermione/clothes/ears/"+str(h_ears)+".png"

    #Hat
    if h_hair_style in ["curly","updo","bobcut"]:
        $ hermione_hat = "characters/hermione/clothes/hats/hair_"+str(h_hair_style)+"/"+str(h_hat)+".png"
    else:
        $ hermione_hat = "characters/hermione/clothes/hats/hair_curly/"+str(h_hat)+".png"

    return

#Makeup equip.
label set_her_makeup(makeup = ""):
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

    return

#Glasses equip.
label set_her_glasses(glasses=""):
    hide screen hermione_main
    if h_request_wear_glasses and h_glasses == glasses:
        $ h_request_wear_glasses = False
        $ hermione_wear_glasses = False
    else:
        $ h_request_wear_glasses = True
        $ hermione_wear_glasses = True
        $ h_glasses = glasses
    call update_her_uniform

    return

#Ears equip.
label set_her_ears(ears=""):
    hide screen hermione_main
    if h_request_wear_ears and h_ears == ears:
        $ h_request_wear_ears = False
        $ hermione_wear_ears = False
    else:
        $ h_request_wear_ears = True
        $ hermione_wear_ears = True
        $ h_ears = ears
        if h_ears == "elf_ears":
            call set_her_hair(style="updo")
    call update_her_uniform

    return

#Hat equip.
label set_her_hat(hat=""):
    hide screen hermione_main
    if h_request_wear_hat and h_hat == hat:
        $ h_request_wear_hat = False
        $ hermione_wear_hat = False
    else:
        $ h_request_wear_hat = True
        $ hermione_wear_hat = True
        $ h_hat = hat
    call update_her_uniform

    return

#Top equip.
label set_her_top(top="", color=""):
    hide screen hermione_main
    $ h_request_wear_top = True
    $ hermione_wear_top = True
    if h_request_wear_bottom:
        $ hermione_wear_bottom = True
    $ h_top = top
    $ h_top_color = color
    call update_her_uniform

    return

#Bottom equip.
label set_her_bottom(bottom="", color=""):
    hide screen hermione_main
    $ h_request_wear_bottom = True
    $ hermione_wear_bottom = True
    if h_request_wear_top:
        $ hermione_wear_top = True
    $ h_bottom = bottom
    $ h_bottom_color = color
    call update_her_uniform

    return

#Bra equip.
label set_her_bra(bra="", color=""):
    hide screen hermione_main
    $ h_request_wear_bra = True
    $ hermione_wear_bra = True
    if h_bra == bra and h_bra_color == color:
        pass
    else:
        $ h_bra = bra
        $ h_bra_color = color
    call update_her_uniform

    return

#Onepiece equip.
label set_her_onepiece(onepiece=""):
    hide screen hermione_main
    if h_onepiece == onepiece and hermione_wear_onepiece: #Off toggle
        $ h_request_wear_onepiece = False
        $ hermione_wear_onepiece = False
    else:
        $ h_request_wear_onepiece = True
        $ hermione_wear_onepiece = True
        $ h_onepiece = onepiece
    call update_her_uniform

    return

#Panties equip.
label set_her_panties(panties="", color=""):
    hide screen hermione_main
    $ h_request_wear_panties = True
    $ hermione_wear_panties = True
    if h_panties == panties and h_panties_color == color: #Off toggle
        pass
    else:
        $ h_panties = panties
        $ h_panties_color = color
    call update_her_uniform

    return

#Garterbelt equip.
label set_her_garterbelt(garterbelt="", color=""):
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

    return

#Neackwear equip.
label set_her_neckwear(neck=""):
    hide screen hermione_main
    if h_neckwear == neck and hermione_wear_neckwear: #Off toggle
        $ h_request_wear_neckwear = False
        $ hermione_wear_neckwear = False
    else:
        $ h_request_wear_neckwear = True
        $ hermione_wear_neckwear = True
        $ h_neckwear = neck
    call update_her_uniform

    return

#Body accs equip.
label set_her_body_accessory(accessory=""):
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

    return

#Gloves Equip.
label set_her_gloves(gloves=""):
    hide screen hermione_main
    if h_gloves == gloves and hermione_wear_gloves: #Off toggle
        $ h_request_wear_gloves = False
        $ hermione_wear_gloves = False
    else:
        $ h_request_wear_gloves = True
        $ hermione_wear_gloves = True
        $ h_gloves = gloves
    call update_her_uniform

    return

#Stockings equip.
label set_her_stockings(stockings=""):
    hide screen hermione_main
    if h_stockings == stockings: #Off toggle
        $ h_request_wear_stockings = False
        $ hermione_wear_stockings = False
    else:
        $ h_request_wear_stockings = True
        $ hermione_wear_stockings = True
        $ h_stockings = stockings
    call update_her_uniform

    return

#Robe equip.
label set_her_robe(robe=""):
    hide screen hermione_main
    if h_robe == robe and hermione_wear_robe:
        $ h_request_wear_robe = False
        $ hermione_wear_robe = False
    else:
        $ h_request_wear_robe = True
        $ hermione_wear_robe = True
        $ h_robe = robe
    call update_her_uniform

    return

#Buttplug equip.
label set_her_buttplug(buttplug=""):
    hide screen hermione_main
    if buttplug == "None" or buttplug == "" or buttplug == "remove":
        $ h_request_wear_buttplug = False
        $ hermione_wear_buttplug = False
    else:
        $ h_request_wear_buttplug = True
        $ hermione_wear_buttplug = True
        $ h_buttplug = buttplug
    call update_her_uniform

    return

#Mask equip.
label set_her_mask(mask=""):
    hide screen hermione_main
    if mask == "None" or mask == "" or mask == "remove":
        $ h_request_wear_mask = False
        $ hermione_wear_mask = False
    else:
        $ h_request_wear_mask = True
        $ hermione_wear_mask = True
        $ h_mask = mask
    call update_her_uniform

    return

#Gag equip.
label set_her_gag(gag=""):
    hide screen hermione_main
    if gag == "None" or gag == "" or gag == "remove":
        $ h_request_wear_gag = False
        $ hermione_wear_gag = False
    else:
        $ h_request_wear_gag = True
        $ hermione_wear_gag = True
        $ h_gag = gag
    call update_her_uniform

    return

#Piercings equip.
label set_her_piercing(piercing=""):
    hide screen hermione_main
    if piercing in ear_piercings_list:
        if h_ear_piercing == piercing:
            $ h_ear_piercing = "blank"
        else:
            $ h_ear_piercing = piercing_choice
    if piercing in nipple_piercings_list:
        if h_nipple_piercing == piercing:
            $ h_nipple_piercing = "blank"
        else:
            $ h_nipple_piercing = piercing
    if piercing in belly_piercings_list:
        if h_belly_piercing == piercing:
            $ h_belly_piercing = "blank"
        else:
            $ h_belly_piercing = piercing
    if piercing in genital_piercings_list:
        if h_belly_piercing == piercing:
            $ h_belly_piercing = "blank"
        else:
            $ h_belly_piercing = piercing

    if h_ear_piercing == "blank" and h_nipple_piercing == "blank" and h_belly_piercing == "blank" and h_genital_piercing == "blank": #No piercings equipped.
        $ h_request_wear_piercings = False
        $ hermione_wear_piercings = False
    else:
        $ h_request_wear_piercings = True
        $ hermione_wear_piercings = True

    call update_her_uniform

    return

## Outfit Equips
label set_hermione_outfit(outfit): #This gets used outside the wardrobe.
    show screen blkfade
    hide screen hermione_main
    with d3
    call set_her_outfit(outfit)
    pause .5
    show screen hermione_main
    hide screen blkfade
    with d5
    return

label set_her_outfit(outfit):
    hide screen hermione_main
    if outfit == None:
        $ h_request_wear_outfit = False
        $ hermione_wear_outfit = False
        call update_her_uniform
    else:
        $ h_request_wear_outfit = True
        $ hermione_wear_outfit = True

        $ h_request_wear_top = True
        $ hermione_wear_top = True

        $ hermoine_outfit_GLBL = outfit

        if hermoine_outfit_GLBL.top_layers != []:
            $ h_request_wear_hat = True
            $ h_hat = hermoine_outfit_GLBL.getTopLayers()
        else:
            $ h_request_wear_hat = False
        if hermoine_outfit_GLBL.hair_layer != "":
            call set_her_hair(style=hermoine_outfit_GLBL.getHairLayers() )

        call load_hermione_clothing_saves
        call update_her_uniform

    return

label h_equip_temp_outfit(outfit):
    $ temp_outfit_GLBL = hermoine_outfit_GLBL  #Saves equipped outfit.
    $ temp_wear_outfit = h_request_wear_outfit #Saves equip state.
    $ temp_wear_top = h_request_wear_top       #Saves equip state.

    call set_her_outfit(outfit)
    return

label h_unequip_temp_outfit():
    hide screen hermione_main
    $ hermoine_outfit_GLBL = temp_outfit_GLBL
    $ h_request_wear_outfit = temp_wear_outfit
    $ h_request_wear_top = temp_wear_top

    if h_request_wear_outfit:
        call set_her_outfit(hermoine_outfit_GLBL)
    else:
        call set_her_outfit(None)
    $ temp_outfit_GLBL = None
    return

label set_her_transparency(top=None, bottom=None, bra=None, onepiece=None, panties=None, garterbelt=None, gloves=None, stockings=None, robe=None, outfit=None):
    pause.5
    hide screen hermione_main

    if top != None:
        $ her_top_transp = top
    if bottom != None:
        $ her_bottom_transp    = bottom

    if bra != None:
        $ her_bra_transp       = bra
    if onepiece != None:
        $ her_onepiece_transp  = onepiece
    if panties != None:
        $ her_panties_transp   = panties
    if garterbelt != None:
        $ her_garter_transp    = garterbelt

    if gloves != None:
        $ her_gloves_transp    = gloves
    if stockings != None:
        $ her_stockings_transp = stockings
    if robe != None:
        $ her_robe_transp      = robe

    if outfit != None:
        $ her_outfit_transp    = outfit

    call update_her_body

    return

#Hermione Action

label set_her_action(action =  "", update=""):
    hide screen hermione_main

    if action == "" or action == "none" or action == "None" or action == None:

        $ hermione_action = "none"
        $ hermione_use_action = False

        $ h_right_arm        = "right_1"
        $ h_left_arm         = "left_1"
        $ h_action_top = ""
        $ h_action_bottom = ""

        $ h_action_a = "blank.png"
        $ hermione_action_a = "characters/hermione/body/arms/left/blank.png"
        $ hermione_action_b = "characters/hermione/body/arms/left/blank.png"
        $ hermione_costume_action_a = "characters/hermione/clothes/custom/blank.png"
        $ milking           = 0


        if update == "update":

            call load_hermione_clothing_saves

    else:

        if hermione_wear_outfit:
            if action in hermoine_outfit_GLBL.actions:
                $ hermione_use_action = True
                $ h_action_a = hermoine_outfit_GLBL.getActionImage(action)
            else:
                $ hermione_use_action = False
                $ h_action_a = "blank.png"

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
                $ hermione_expand_breasts = True

            if action == "expand_ass":
                $ hermione_expand_ass = True

            if action == "expand_all":
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


    call update_her_uniform #calls update_her_action, update_chibi_uniform, and update_her_body;

    return



label load_hermione_clothing_saves:

    #Uniform & Underwear
    if h_request_wear_top:
        $ hermione_wear_top          = True
    else:
        $ hermione_wear_top          = False

    if h_request_wear_onepiece:
        $ hermione_wear_onepiece     = True
    else:
        $ hermione_wear_onepiece     = False

    if h_request_wear_bra:
        $ hermione_wear_bra          = True
    else:
        $ hermione_wear_bra          = False

    if h_request_wear_bottom:
        $ hermione_wear_bottom       = True
    else:
        $ hermione_wear_bottom       = False

    if h_request_wear_panties:
        $ hermione_wear_panties      = True
    else:
        $ hermione_wear_panties      = False

    if h_request_wear_garterbelt:
        $ hermione_wear_garterbelt   = True
    else:
        $ hermione_wear_garterbelt   = False

    #Other Clothing
    if h_request_wear_neckwear:
        $ hermione_wear_neckwear     = True
    else:
        $ hermione_wear_neckwear     = False

    if h_request_wear_body_accs:
        $ hermione_wear_body_accs    = True
    else:
        $ hermione_wear_body_accs    = False

    if h_request_wear_gloves:
        $ hermione_wear_gloves       = True
    else:
        $ hermione_wear_gloves       = False

    if h_request_wear_stockings:
        $ hermione_wear_stockings    = True
    else:
        $ hermione_wear_stockings    = False

    if h_request_wear_robe:
        $ hermione_wear_robe         = True
    else:
        $ hermione_wear_robe         = False

    #Head Accessories
    if h_request_wear_hat:
        $ hermione_wear_hat          = True
    else:
        $ hermione_wear_hat          = False

    if h_request_wear_glasses:
        $ hermione_wear_glasses      = True
    else:
        $ hermione_wear_glasses      = False

    if h_request_wear_ears:
        $ hermione_wear_ears         = True
    else:
        $ hermione_wear_ears         = False

    if h_request_wear_makeup:
        $ hermione_wear_makeup       = True
    else:
        $ hermione_wear_makeup       = False

    if h_request_wear_piercings:
        $ hermione_wear_piercings    = True
    else:
        $ hermione_wear_piercings    = False

    if h_request_wear_tattoos:
        $ hermione_wear_tattoos      = True
    else:
        $ hermione_wear_tattoos      = False

    if h_request_wear_mask:
        $ hermione_wear_mask = True
    else:
        $ hermione_wear_mask = False

    if h_request_wear_gag:
        $ hermione_wear_gag = True
    else:
        $ hermione_wear_gag = False

    if h_request_wear_outfit:
        $ hermione_wear_outfit = True
    else:
        $ hermione_wear_outfit = False

    return
