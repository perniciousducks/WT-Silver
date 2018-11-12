

label update_lun_uniform:
    hide screen luna_main

    #Hair
    $ luna_hair         = "characters/luna/body/hair/hair_"+str(lun_hair_style)+"_"+str(lun_hair_color)+"_base.png"
    $ luna_hair_shadow  = "characters/luna/body/hair/hair_"+str(lun_hair_style)+"_"+str(lun_hair_color)+"_top.png"

    #Top
    $ luna_top            = "characters/luna/clothes/tops/base/"+str(lun_top)+".png"

    #Bottom
    $ luna_bottom         = "characters/luna/clothes/bottoms/"+str(lun_bottom_color)+"/"+str(lun_bottom)+".png"

    #Underwear
    $ luna_bra            = "characters/luna/clothes/underwear/base/"+str(lun_bra)+".png"
    $ luna_onepiece       = "characters/luna/clothes/onepieces/base/"+str(lun_onepiece)+".png"
    $ luna_panties        = "characters/luna/clothes/underwear/base/"+str(lun_panties)+".png"
    $ luna_garterbelt     = "characters/luna/clothes/underwear/base/"+str(lun_garterbelt)+".png"

    $ luna_neckwear       = "characters/luna/clothes/neckwear/"+str(lun_neckwear)+".png"
    $ luna_gloves         = "characters/luna/clothes/gloves/"+str(lun_gloves)+".png"
    $ luna_stockings      = "characters/luna/clothes/stockings/"+str(lun_stockings)+".png"
    $ luna_robe           = "characters/luna/clothes/robe/"+str(lun_robe)+".png"

    #Accessories
    $ luna_hat            = "characters/luna/accessories/hats/hair_A/"+str(lun_hat)+".png" #/hair_"+str(lun_hair_style)+"/
    $ luna_glasses        = "characters/luna/accessories/glasses/base/"+str(lun_glasses)+".png"
    $ luna_ears           = "characters/luna/accessories/ears/"+str(lun_ears)+".png"

    return

#Hair equip.
label set_lun_hair(hair=None,color=None):
    hide screen luna_main

    if hair != None:
        $ lun_hair_style   = hair
    if color != None:
        $ lun_hair_color   = color

    call update_lun_uniform
    show screen luna_main

    return

#Hat equip.
label set_lun_hat(hat=""):
    hide screen luna_main

    if luna_wear_hat and lun_hat == hat:
        $ lun_request_wear_hat = False
        $ luna_wear_hat = False
    else:
        $ lun_request_wear_hat = True
        $ luna_wear_hat = True
        $ lun_hat = hat

    call update_lun_uniform
    show screen luna_main

    return

#Top equip.
label set_lun_top(top=""):
    hide screen luna_main

    if luna_wear_top and lun_top == top:
        $ lun_request_wear_top = False
        $ luna_wear_top = False
    else:
        $ lun_request_wear_top = True
        $ luna_wear_top = True
        $ lun_top = top

    call update_lun_uniform
    show screen luna_main

    return

#Bottom equip.
label set_lun_bottom(bottom="", color=""):
    hide screen luna_main

    if luna_wear_bottom and lun_bottom == bottom and lun_bottom_color == color:
        $ lun_request_wear_bottom = False
        $ luna_wear_bottom = False
    else:
        if bottom in ["skirt_cheer_r","pants_pyjama"]: #Those have no recolors!
            $ color = "base"
        $ lun_request_wear_bottom = True
        $ luna_wear_bottom = True
        $ lun_bottom = bottom
        $ lun_bottom_color = color

    call update_lun_uniform
    show screen luna_main

    return

#Bra equip.
label set_lun_bra(bra=""):
    hide screen luna_main

    if luna_wear_bra and lun_bra == bra:
        if lun_corruption > 8:
            $ lun_request_wear_bra = False
            $ luna_wear_bra = False
        else:
            pass
    else:
        $ lun_request_wear_bra = True
        $ luna_wear_bra = True
        $ lun_bra = bra

    call update_lun_uniform
    show screen luna_main

    return

#One-Piece equip.
label set_lun_onepiece(onepiece=""):
    hide screen luna_main

    if luna_wear_onepiece and lun_onepiece == onepiece:
        $ lun_request_wear_onepiece = False
        $ luna_wear_onepiece = False
    else:
        $ lun_request_wear_onepiece = True
        $ luna_wear_onepiece = True
        $ lun_onepiece = onepiece

    call update_lun_uniform
    show screen luna_main

    return

#Panties equip.
label set_lun_panties(panties=""):
    hide screen luna_main

    if luna_wear_panties and lun_panties == panties:
        if lun_corruption > 8:
            $ lun_request_wear_panties = False
            $ luna_wear_panties = False
        else:
            pass
    else:
        $ lun_request_wear_panties = True
        $ luna_wear_panties = True
        $ lun_panties = panties

    call update_lun_uniform
    show screen luna_main

    return

#Garterbelt equip.
label set_lun_garterbelt(garter=""):
    hide screen luna_main

    if luna_wear_garterbelt and lun_garterbelt == garter:
        $ lun_request_wear_garterbelt = False
        $ luna_wear_garterbelt = False
    else:
        $ lun_request_wear_garterbelt = True
        $ luna_wear_garterbelt = True
        $ lun_garterbelt = garter

    call update_lun_uniform
    show screen luna_main

    return

#Neckwear equip.
label set_lun_neckwear(neck=""):
    hide screen luna_main

    if luna_wear_neckwear and lun_neckwear == neck:
        $ lun_request_wear_neckwear = False
        $ luna_wear_neckwear = False
    else:
        $ lun_request_wear_neckwear = True
        $ luna_wear_neckwear = True
        $ lun_neckwear = neck

    call update_lun_uniform
    show screen luna_main

    return

#Stockings equip.
label set_lun_stockings(stockings=""):
    hide screen luna_main

    if luna_wear_stockings and lun_stockings == stockings:
        $ lun_request_wear_stockings = False
        $ luna_wear_stockings = False
    else:
        $ lun_request_wear_stockings = True
        $ luna_wear_stockings = True
        $ lun_stockings = stockings

    call update_lun_uniform
    show screen luna_main

    return

#Robe equip.
label set_lun_robe(robe=""):
    hide screen luna_main

    if luna_wear_robe and lun_robe == robe:
        $ lun_request_wear_robe = False
        $ luna_wear_robe = False
    else:
        $ lun_request_wear_robe = True
        $ luna_wear_robe = True
        $ lun_robe = robe

    call update_lun_uniform
    show screen luna_main

    return

#Glasses equip.
label set_lun_glasses(glasses=""):
    hide screen luna_main

    if luna_wear_glasses and lun_glasses == glasses:
        $ lun_request_wear_glasses = False
        $ luna_wear_glasses = False
    else:
        $ lun_request_wear_glasses = True
        $ luna_wear_glasses = True
        $ lun_glasses = glasses

    call update_lun_uniform
    show screen luna_main

    return

#Ears equip.
label set_lun_ears(ears=""):
    hide screen luna_main

    if luna_wear_ears and lun_ears == ears:
        $ lun_request_wear_ears = False
        $ luna_wear_ears = False
    else:
        $ lun_request_wear_ears = True
        $ luna_wear_ears = True
        $ lun_ears = ears

    call update_lun_uniform
    show screen luna_main

    return

## Equip Outfit
label set_lun_outfit(outfit):
    hide screen luna_main
    with d3
    call luna_outfit(outfit)
    pause .5
    show screen luna_main
    with d5
    return

label luna_outfit(outfit):
    hide screen luna_main

    if outfit == None:
        $ lun_request_wear_outfit = False
        $ luna_wear_outfit = False
    else:
        $ luna_wear_outfit = True

        $ lun_request_wear_top = True
        $ luna_wear_top = True

        $ luna_outfit_GLBL = outfit

        if luna_outfit_GLBL.hair_layer != "":
            $ lun_hair_style = luna_outfit_GLBL.getHairLayers()
            $ lun_hair_color = 1
        if luna_outfit_GLBL.top_layers != []:
            $ lun_request_wear_hat = True
            $ lun_hat = luna_outfit_GLBL.getTopLayers()

    call load_luna_clothing_saves
    call update_lun_uniform
    show screen luna_main

    return




label load_luna_clothing_saves:

    #Uniform & Underwear
    if lun_request_wear_top:
        $ luna_wear_top          = True
    else:
        $ luna_wear_top          = False

    if lun_request_wear_onepiece:
        $ luna_wear_onepiece     = True
    else:
        $ luna_wear_onepiece     = False

    if lun_request_wear_bra:
        $ luna_wear_bra          = True
    else:
        $ luna_wear_bra          = False

    if lun_request_wear_bottom:
        $ luna_wear_bottom       = True
    else:
        $ luna_wear_bottom       = False

    if lun_request_wear_panties:
        $ luna_wear_panties      = True
    else:
        $ luna_wear_panties      = False

    if lun_request_wear_garterbelt:
        $ luna_wear_garterbelt   = True
    else:
        $ luna_wear_garterbelt   = False

    #Other Clothing
    if lun_request_wear_neckwear:
        $ luna_wear_neckwear     = True
    else:
        $ luna_wear_neckwear     = False

    if lun_request_wear_accs:
        $ luna_wear_accs    = True
    else:
        $ luna_wear_accs    = False

    if lun_request_wear_gloves:
        $ luna_wear_gloves       = True
    else:
        $ luna_wear_gloves       = False

    if lun_request_wear_stockings:
        $ luna_wear_stockings    = True
    else:
        $ luna_wear_stockings    = False

    if lun_request_wear_robe:
        $ luna_wear_robe         = True
    else:
        $ luna_wear_robe         = False

    #Head Accessories
    if lun_request_wear_hat:
        $ luna_wear_hat          = True
    else:
        $ luna_wear_hat          = False

    if lun_request_wear_glasses:
        $ luna_wear_glasses      = True
    else:
        $ luna_wear_glasses      = False

    if lun_request_wear_ears:
        $ luna_wear_ears         = True
    else:
        $ luna_wear_ears         = False

    if lun_request_wear_makeup:
        $ luna_wear_makeup       = True
    else:
        $ luna_wear_makeup       = False

    if lun_request_wear_piercings:
        $ luna_wear_piercings    = True
    else:
        $ luna_wear_piercings    = False

    if lun_request_wear_tattoos:
        $ luna_wear_tattoos      = True
    else:
        $ luna_wear_tattoos      = False

    return
