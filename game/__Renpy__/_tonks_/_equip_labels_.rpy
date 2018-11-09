

#tonks EQUIP

label update_ton_uniform:
    hide screen tonks_main

    #Hair
    $ tonks_hair         = "characters/tonks/body/hair/hair_"+str(ton_hair_style)+"_"+str(ton_hair_color)+".png"
    $ tonks_hair_shadow  = "characters/tonks/body/hair/hair_"+str(ton_hair_style)+"_"+str(ton_hair_color)+".png"
    $ tonks_pubic_hair   = "characters/tonks/body/hair/pubes_"+str(ton_pubic_hair)+"_"+str(ton_hair_color)+".png"

    #Top
    $ tonks_top            = "characters/tonks/clothes/tops/base/"+str(ton_top)+".png"

    #Bottom
    $ tonks_bottom         = "characters/tonks/clothes/bottoms/"+str(ton_bottom_color)+"/"+str(ton_bottom)+".png"

    #Underwear
    $ tonks_bra            = "characters/tonks/clothes/underwear/base/"+str(ton_bra)+".png"
    $ tonks_onepiece       = "characters/tonks/clothes/onepieces/base/"+str(ton_onepiece)+".png"
    $ tonks_panties        = "characters/tonks/clothes/underwear/base/"+str(ton_panties)+".png"
    $ tonks_garterbelt     = "characters/tonks/clothes/underwear/base/"+str(ton_garterbelt)+".png"

    $ tonks_neckwear       = "characters/tonks/clothes/neckwear/"+str(ton_neckwear)+".png"
    $ tonks_gloves         = "characters/tonks/clothes/gloves/"+str(ton_gloves)+".png"
    $ tonks_stockings      = "characters/tonks/clothes/stockings/"+str(ton_stockings)+".png"
    $ tonks_robe           = "characters/tonks/clothes/robe/base/"+str(ton_robe)+".png"
    $ tonks_robe_back      = "characters/tonks/clothes/robe/base/"+str(ton_robe)+"_back.png"

    #Accessories
    $ tonks_hat            = "characters/tonks/accessories/hats/"+str(ton_hat)+".png"

    #Piercings
    $ tonks_ear_piercing        = "characters/tonks/accessories/piercings/"+str(ton_ear_piercing_color)+"/"+str(ton_ear_piercing)+".png"
    if tonks_wear_top or tonks_wear_robe:
        $ tonks_nipple_piercing = "characters/tonks/accessories/piercings/"+str(ton_nipple_piercing_color)+"/blank.png"
    else:
        $ tonks_nipple_piercing = "characters/tonks/accessories/piercings/"+str(ton_nipple_piercing_color)+"/"+str(ton_nipple_piercing)+".png"
    $ tonks_belly_piercing      = "characters/tonks/accessories/piercings/"+str(ton_belly_piercing_color)+"/"+str(ton_belly_piercing)+".png"
    $ tonks_intimate_piercing   = "characters/tonks/accessories/piercings/"+str(ton_intimate_piercing_color)+"/"+str(ton_intimate_piercing)+".png"

    call update_ton_body

    return


label update_ton_body:
    hide screen tonks_main

    if tonks_wear_robe:# or tonks_wear_top or tonks_wear_bra:
        $ tonks_boobs = "characters/tonks/body/base/boobs_0.png"
    else:
        if tonks_wear_top and ton_top in ["top_corset_1"]:
            $ tonks_boobs = "characters/tonks/body/base/boobs_0.png" #pressed boobs
        elif tonks_wear_top:
            $ tonks_boobs = "characters/tonks/body/base/boobs_2.png"
        else:
            $ tonks_boobs = "characters/tonks/body/base/boobs_1.png"

    return


#Hair equip.
label set_ton_hair(hair=None,color=None):
    hide screen tonks_main

    if hair != None:
        $ ton_hair_style   = hair
    if color != None:
        $ ton_hair_color   = color

    call update_ton_uniform
    show screen tonks_main

    return

label set_ton_pubic_hair(pubes=None):
    hide screen tonks_main

    if pubes == None:
        $ ton_request_wear_pubic_hair = False
        $ tonks_wear_pubic_hair = False
    else:
        $ ton_request_wear_pubic_hair = True
        $ tonks_wear_pubic_hair = True
        $ ton_pubic_hair = pubes

    call update_ton_uniform
    show screen tonks_main

    return


#Hat equip.
label set_ton_hat(hat=""):
    hide screen tonks_main

    if tonks_wear_hat and ton_hat == hat:
        $ ton_request_wear_hat = False
        $ tonks_wear_hat = False
    else:
        $ ton_request_wear_hat = True
        $ tonks_wear_hat = True
        $ ton_hat = hat

    call update_ton_uniform
    show screen tonks_main

    return

#Top equip.
label set_ton_top(top=""):
    hide screen tonks_main

    if tonks_wear_top and ton_top == top:
        $ ton_request_wear_top = False
        $ tonks_wear_top = False
    else:
        $ ton_request_wear_top = True
        $ tonks_wear_top = True
        $ ton_top = top

    call update_ton_uniform
    show screen tonks_main

    return

#Bottom equip.
label set_ton_bottom(bottom="", color=""):
    hide screen tonks_main

    if tonks_wear_bottom and ton_bottom == bottom and ton_bottom_color == color:
        $ ton_request_wear_bottom = False
        $ tonks_wear_bottom = False
    else:
        if bottom in ["pants_jeans_long","pants_rocker"]: #Those have no recolors!
            $ color = "base"
        $ ton_request_wear_bottom = True
        $ tonks_wear_bottom = True
        $ ton_bottom = bottom
        $ ton_bottom_color = color

    call update_ton_uniform
    show screen tonks_main

    return

#Bra equip.
label set_ton_bra(bra=""):
    hide screen tonks_main

    if tonks_wear_bra and ton_bra == bra:
        $ ton_request_wear_bra = False
        $ tonks_wear_bra = False
    else:
        $ ton_request_wear_bra = True
        $ tonks_wear_bra = True
        $ ton_bra = bra

    call update_ton_uniform
    show screen tonks_main

    return

#One-Piece equip.
label set_ton_onepiece(onepiece=""):
    hide screen tonks_main

    if tonks_wear_onepiece and ton_onepiece == onepiece:
        $ ton_request_wear_onepiece = False
        $ tonks_wear_onepiece = False
    else:
        $ ton_request_wear_onepiece = True
        $ tonks_wear_onepiece = True
        $ ton_onepiece = onepiece

    call update_ton_uniform
    show screen tonks_main

    return

#Panties equip.
label set_ton_panties(panties=""):
    hide screen tonks_main

    if tonks_wear_panties and ton_panties == panties:
        $ ton_request_wear_panties = False
        $ tonks_wear_panties = False
    else:
        $ ton_request_wear_panties = True
        $ tonks_wear_panties = True
        $ ton_panties = panties

    call update_ton_uniform
    show screen tonks_main

    return

#Garterbelt equip.
label set_ton_garterbelt(garter=""):
    hide screen tonks_main

    if tonks_wear_garterbelt and ton_garterbelt == garter:
        $ ton_request_wear_garterbelt = False
        $ tonks_wear_garterbelt = False
    else:
        $ ton_request_wear_garterbelt = True
        $ tonks_wear_garterbelt = True
        $ ton_garterbelt = garter

    call update_ton_uniform
    show screen tonks_main

    return

#Neckwear equip.
label set_ton_neckwear(neck=""):
    hide screen tonks_main

    if tonks_wear_neckwear and ton_neckwear == neck:
        $ ton_request_wear_neckwear = False
        $ tonks_wear_neckwear = False
    else:
        $ ton_request_wear_neckwear = True
        $ tonks_wear_neckwear = True
        $ ton_neckwear = neck

    call update_ton_uniform
    show screen tonks_main

    return

#Gloves equip.
label set_ton_gloves(gloves=""):
    hide screen tonks_main

    if tonks_wear_gloves and ton_gloves == gloves:
        $ ton_request_wear_gloves = False
        $ tonks_wear_gloves = False
    else:
        $ ton_request_wear_gloves = True
        $ tonks_wear_gloves = True
        $ ton_gloves = gloves

    call update_ton_uniform
    show screen tonks_main

    return

#Stockings equip.
label set_ton_stockings(stockings=""):
    hide screen tonks_main

    if tonks_wear_stockings and ton_stockings == stockings:
        $ ton_request_wear_stockings = False
        $ tonks_wear_stockings = False
    else:
        $ ton_request_wear_stockings = True
        $ tonks_wear_stockings = True
        $ ton_stockings = stockings

    call update_ton_uniform
    show screen tonks_main

    return

#Robe equip.
label set_ton_robe(robe=""):
    hide screen tonks_main

    if tonks_wear_robe and ton_robe == robe:
        $ ton_request_wear_robe = False
        $ tonks_wear_robe = False
    else:
        $ ton_request_wear_robe = True
        $ tonks_wear_robe = True
        $ ton_robe = robe

    call update_ton_uniform
    show screen tonks_main

    return

#Piercings equip.
label set_ton_piercing(piercing="", color=""):
    hide screen tonks_main
    if piercing in ear_piercings_list:
        if ton_ear_piercing == piercing and ton_ear_piercing_color == color:
            $ ton_ear_piercing = "blank"
        else:
            $ ton_ear_piercing = piercing_choice
    if piercing in nipple_piercings_list:
        if ton_nipple_piercing == piercing and ton_nipple_piercing_color == color:
            $ ton_nipple_piercing = "blank"
        else:
            $ ton_nipple_piercing = piercing
    if piercing in belly_piercings_list:
        if ton_belly_piercing == piercing and ton_belly_piercing_color == color:
            $ ton_belly_piercing = "blank"
        else:
            $ ton_belly_piercing = piercing
    if piercing in intimate_piercings_list:
        if ton_belly_piercing == piercing and ton_intimate_piercing_color == color:
            $ ton_belly_piercing = "blank"
        else:
            $ ton_belly_piercing = piercing

    if ton_ear_piercing == "blank" and ton_nipple_piercing == "blank" and ton_belly_piercing == "blank" and ton_intimate_piercing == "blank": #No piercings equipped.
        $ ton_request_wear_piercings = False
    else:
        $ ton_request_wear_piercings = True

    call update_ton_uniform
    show screen tonks_main
    return



## Equip Outfit
label set_ton_outfit(outfit):
    hide screen tonks_main
    with d3
    call ton_outfit(outfit)
    pause .5
    show screen tonks_main
    with d5
    return

label ton_outfit(outfit):
    hide screen tonks_main

    if outfit == None:
        $ ton_request_wear_outfit = False
        $ tonks_wear_outfit = False
    else:
        $ tonks_wear_outfit = True

        $ ton_request_wear_top = True
        $ tonks_wear_top = True

        $ tonks_outfit_GLBL = outfit

        if tonks_outfit_GLBL.hair_layer != "":
            $ ton_hair_style = tonks_outfit_GLBL.getHairLayers()
            $ ton_hair_color = 1
        if tonks_outfit_GLBL.top_layers != []:
            $ ton_request_wear_hat = True
            $ ton_hat = tonks_outfit_GLBL.getTopLayers()

    call load_tonks_clothing_saves
    call update_ton_uniform
    show screen tonks_main

    return


label set_tonks_action(action=""):
    hide screen tonks_main

    if action in ["",None]:
        $ ton_request_wear_robe = True
        $ ton_request_wear_top = True
        $ ton_request_wear_bra = True
        $ ton_request_wear_bottom = True
        $ ton_request_wear_panties = True
        $ ton_request_wear_gloves = True
        $ ton_request_wear_stockings = True
        $ ton_request_wear_accs = True

    if action in ["strip","naked","strip_naked"]:
        $ ton_request_wear_robe = False
        $ ton_request_wear_top = False
        $ ton_request_wear_bra = False
        $ ton_request_wear_bottom = False
        $ ton_request_wear_panties = False
        $ ton_request_wear_gloves = False
        $ ton_request_wear_stockings = False
        $ ton_request_wear_accs = False

    call load_tonks_clothing_saves
    call update_ton_body

    return


label load_tonks_clothing_saves:

    #Uniform & Underwear
    if ton_request_wear_top:
        $ tonks_wear_top          = True
    else:
        $ tonks_wear_top          = False

    if ton_request_wear_onepiece:
        $ tonks_wear_onepiece     = True
    else:
        $ tonks_wear_onepiece     = False

    if ton_request_wear_bra:
        $ tonks_wear_bra          = True
    else:
        $ tonks_wear_bra          = False

    if ton_request_wear_bottom:
        $ tonks_wear_bottom       = True
    else:
        $ tonks_wear_bottom       = False

    if ton_request_wear_panties:
        $ tonks_wear_panties      = True
    else:
        $ tonks_wear_panties      = False

    if ton_request_wear_garterbelt:
        $ tonks_wear_garterbelt   = True
    else:
        $ tonks_wear_garterbelt   = False

    #Other Clothing
    if ton_request_wear_neckwear:
        $ tonks_wear_neckwear     = True
    else:
        $ tonks_wear_neckwear     = False

    if ton_request_wear_accs:
        $ tonks_wear_accs    = True
    else:
        $ tonks_wear_accs    = False

    if ton_request_wear_gloves:
        $ tonks_wear_gloves       = True
    else:
        $ tonks_wear_gloves       = False

    if ton_request_wear_stockings:
        $ tonks_wear_stockings    = True
    else:
        $ tonks_wear_stockings    = False

    if ton_request_wear_robe:
        $ tonks_wear_robe         = True
    else:
        $ tonks_wear_robe         = False

    #Head Accessories
    if ton_request_wear_hat:
        $ tonks_wear_hat          = True
    else:
        $ tonks_wear_hat          = False

    if ton_request_wear_glasses:
        $ tonks_wear_glasses      = True
    else:
        $ tonks_wear_glasses      = False

    if ton_request_wear_ears:
        $ tonks_wear_ears         = True
    else:
        $ tonks_wear_ears         = False

    if ton_request_wear_makeup:
        $ tonks_wear_makeup       = True
    else:
        $ tonks_wear_makeup       = False

    if ton_request_wear_piercings:
        $ tonks_wear_piercings    = True
    else:
        $ tonks_wear_piercings    = False

    if ton_request_wear_tattoos:
        $ tonks_wear_tattoos      = True
    else:
        $ tonks_wear_tattoos      = False

    return
