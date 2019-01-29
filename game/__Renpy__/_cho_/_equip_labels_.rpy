

label update_cho_uniform:
    hide screen cho_chang

    #Hair
    $ cho_hair         = "characters/cho/body/hair/" +str(c_hair_style)+ "_" +str(c_hair_color)+ "_base.png"
    $ cho_hair_shadow  = "characters/cho/body/hair/" +str(c_hair_style)+ "_" +str(c_hair_color)+ "_top.png"

    #Top
    $ cho_top            = "characters/cho/clothes/tops/" +str(c_top_color)+ "/" +str(c_top)+ ".png"

    #Bottom
    $ cho_bottom         = "characters/cho/clothes/bottoms/" +str(c_bottom_color)+ "/"+str(c_bottom)+".png"

    #Underwear
    $ cho_bra            = "characters/cho/clothes/underwear/" +str(c_bra_color)+ "/" +str(c_bra)+ ".png"
    $ cho_onepiece       = "characters/cho/clothes/onepieces/" +str(c_onepiece)+ ".png"
    $ cho_panties        = "characters/cho/clothes/underwear/" +str(c_panties_color)+ "/" +str(c_panties)+ ".png"
    $ cho_garterbelt     = "characters/cho/clothes/underwear/" +str(c_garterbelt_color)+ "/" +str(c_garterbelt)+ ".png"

    $ cho_neckwear       = "characters/cho/clothes/neckwear/" +str(c_neckwear)+ ".png"
    $ cho_gloves         = "characters/cho/clothes/gloves/" +str(c_gloves)+ ".png"
    $ cho_stockings      = "characters/cho/clothes/stockings/" +str(c_stockings_color)+ "/" +str(c_stockings)+ ".png"
    $ cho_robe           = "characters/cho/clothes/robe/" +str(c_robe)+ ".png"

    #Accessories
    $ cho_hat            = "characters/cho/accessories/hats/hair_" +str(c_hair_style)+ "/" +str(c_hat)+ ".png"

    #Miscellaneous
    $ cho_buttplug            = "characters/cho/accessories/plugs/" +str(c_buttplug)+ ".png"
    #$ cho_gag                 = "characters/cho/face/mouth/" +str(c_gag)+ ".png"

    #Piercings
    # cho_tongue_piercing gets defined at the same place as her mouth every time the mouth layer gets updated. # NOT SUPPORTED YET!
    $ cho_ear_piercing        = "characters/cho/accessories/piercings/" +str(c_ear_piercing)+ ".png"
    $ cho_nipple_piercing     = "characters/cho/accessories/piercings/" +str(c_nipple_piercing)+ ".png"
    $ cho_belly_piercing      = "characters/cho/accessories/piercings/" +str(c_belly_piercing)+ ".png"
    $ cho_genital_piercing    = "characters/cho/accessories/piercings/" +str(c_genital_piercing)+ ".png"

    return

#Hair equip.
label set_cho_hair(hair=None,color=None):
    hide screen cho_chang

    if hair != None:
        $ c_hair_style   = hair
    if color != None:
        $ c_hair_color   = color

    call update_cho_uniform

    return

#Hat equip.
label set_cho_hat(hat=""):
    hide screen cho_chang

    if cho_wear_hat and c_hat == hat:
        $ cho_request_wear_hat = False
        $ cho_wear_hat = False
    else:
        $ cho_request_wear_hat = True
        $ cho_wear_hat = True
        $ c_hat = hat

    call update_cho_uniform

    return

#Top equip.
label set_cho_top(top="", color=""):
    hide screen cho_chang

    if cho_wear_top and c_top == top and c_top_color == color:
        $ cho_request_wear_top = False
        $ cho_wear_top = False
    else:
        $ cho_request_wear_top = True
        $ cho_wear_top = True
        $ c_top = top
        $ c_top_color = color

    call update_cho_uniform

    return

#Bottom equip.
label set_cho_bottom(bottom="", color=""):
    hide screen cho_chang

    if cho_wear_bottom and c_bottom == bottom and c_bottom_color == color:
        $ cho_request_wear_bottom = False
        $ cho_wear_bottom = False
    else:
        $ cho_request_wear_bottom = True
        $ cho_wear_bottom = True
        $ c_bottom = bottom
        $ c_bottom_color = color

    call update_cho_uniform

    return

#Bra equip.
label set_cho_bra(bra="", color=""):
    hide screen cho_chang

    if cho_wear_bra and c_bra == bra and c_bra_color == color:
        $ cho_request_wear_bra = False
        $ cho_wear_bra = False
    else:
        $ cho_request_wear_bra = True
        $ cho_wear_bra = True
        $ c_bra = bra
        $ c_bra_color = color

    call update_cho_uniform

    return

#One-Piece equip.
label set_cho_onepiece(onepiece=""):
    hide screen cho_chang

    if cho_wear_onepiece and c_onepiece == onepiece:
        $ cho_request_wear_onepiece = False
        $ cho_wear_onepiece = False
    else:
        $ cho_request_wear_onepiece = True
        $ cho_wear_onepiece = True
        $ c_onepiece = onepiece

    call update_cho_uniform

    return

#Panties equip.
label set_cho_panties(panties="", color=""):
    hide screen cho_chang

    if cho_wear_panties and c_panties == panties and c_panties_color == color:
        $ cho_request_wear_panties = False
        $ cho_wear_panties = False
    else:
        $ cho_request_wear_panties = True
        $ cho_wear_panties = True
        $ c_panties = panties
        $ c_panties_color = color

    call update_cho_uniform

    return

#Garterbelt equip.
label set_cho_garterbelt(garter="", color=""):
    hide screen cho_chang

    if cho_wear_garterbelt and c_garterbelt == garter and c_garterbelt_color == color:
        $ cho_request_wear_garterbelt = False
        $ cho_wear_garterbelt = False
    else:
        $ cho_request_wear_garterbelt = True
        $ cho_wear_garterbelt = True
        $ c_garterbelt = garter
        $ c_garterbelt_color = color

    call update_cho_uniform

    return

#Neckwear equip.
label set_cho_neckwear(neck=""):
    hide screen cho_chang

    if cho_wear_neckwear and c_neckwear == neck:
        $ cho_request_wear_neckwear = False
        $ cho_wear_neckwear = False
    else:
        $ cho_request_wear_neckwear = True
        $ cho_wear_neckwear = True
        $ c_neckwear = neck

    call update_cho_uniform

    return

#Body accs equip.
label set_cho_body_accessory(accessory=""):
    if accessory in cho_body_accs_list:
        $ cho_body_accs_list.remove(accessory)
    else:
        $ cho_body_accs_list.append(accessory)

    if cho_body_accs_list == []:
        $ cho_request_wear_body_accs = False
        $ cho_wear_body_accs = False
    else:
        $ cho_request_wear_body_accs = True
        $ cho_wear_body_accs = True
    call update_cho_uniform

    return

#Gloves equip.
label set_cho_gloves(gloves=""):
    hide screen cho_chang

    if cho_wear_gloves and c_gloves == gloves:
        $ cho_request_wear_gloves = False
        $ cho_wear_gloves = False
    else:
        $ cho_request_wear_gloves = True
        $ cho_wear_gloves = True
        $ c_gloves = gloves

    call update_cho_uniform

    return

#Stockings equip.
label set_cho_stockings(stockings="", color=""):
    hide screen cho_chang

    if cho_wear_stockings and c_stockings == stockings and c_stockings_color == color:
        $ cho_request_wear_stockings = False
        $ cho_wear_stockings = False
    else:
        $ cho_request_wear_stockings = True
        $ cho_wear_stockings = True
        $ c_stockings = stockings
        $ c_stockings_color = color

    call update_cho_uniform

    return

#Robe equip.
label set_cho_robe(robe=""):
    hide screen cho_chang

    if cho_wear_robe and c_robe == robe:
        $ cho_request_wear_robe = False
        $ cho_wear_robe = False
    else:
        $ cho_request_wear_robe = True
        $ cho_wear_robe = True
        $ c_robe = robe

    call update_cho_uniform

    return

#Gag equip.
label set_cho_gag(gag=""):
    hide screen cho_chang
    if gag == "None" or gag == "" or gag == "remove":
        $ cho_request_wear_gag = False
        $ cho_wear_gag = False
    else:
        $ cho_request_wear_gag = True
        $ cho_wear_gag = True
        $ c_gag = gag
    call update_cho_uniform

    return

#Piercings equip.
label set_cho_piercing(piercing=""):
    hide screen cho_chang
    if piercing in ear_piercings_list:
        if c_ear_piercing == piercing:
            $ c_ear_piercing = "blank"
        else:
            $ c_ear_piercing = piercing_choice
    if piercing in tongue_piercings_list:
        if c_tongue_piercing == piercing:
            $ c_tongue_piercing = "blank"
        else:
            $ c_tongue_piercing = piercing_choice
    if piercing in nipple_piercings_list:
        if c_nipple_piercing == piercing:
            $ c_nipple_piercing = "blank"
        else:
            $ c_nipple_piercing = piercing
    if piercing in belly_piercings_list:
        if c_belly_piercing == piercing:
            $ c_belly_piercing = "blank"
        else:
            $ c_belly_piercing = piercing
    if piercing in genital_piercings_list:
        if c_belly_piercing == piercing:
            $ c_belly_piercing = "blank"
        else:
            $ c_belly_piercing = piercing

    if c_ear_piercing == "blank" and c_tongue_piercing == "blank" and c_nipple_piercing == "blank" and c_belly_piercing == "blank" and c_genital_piercing == "blank": #No piercings equipped.
        $ cho_request_wear_piercings = False
    else:
        $ cho_request_wear_piercings = True

    call update_cho_uniform

    return



## Equip Outfit
label set_cho_outfit(outfit):
    hide screen cho_chang

    if outfit == None:
        $ cho_request_wear_outfit = False
        $ cho_wear_outfit = False
    else:
        $ cho_request_wear_outfit = True
        $ cho_wear_outfit = True
        $ cho_request_wear_top = True

        $ cho_outfit_GLBL = outfit

        if cho_outfit_GLBL.hair_layer != "":
            $ c_hair_style = cho_outfit_GLBL.getHairLayers()
        if cho_outfit_GLBL.top_layers != []:
            $ cho_request_wear_hat = True
            $ c_hat = cho_outfit_GLBL.getTopLayers()

    call load_cho_clothing_saves
    call update_cho_uniform

    return


#Transparency
label set_cho_transparency(top=None, bottom=None, bra=None, onepiece=None, panties=None, garterbelt=None, gloves=None, stockings=None, robe=None, outfit=None):
    pause.5
    hide screen cho_chang

    if top != None:
        $ cho_top_transp = top
    if bottom != None:
        $ cho_bottom_transp    = bottom

    if bra != None:
        $ cho_bra_transp       = bra
    if onepiece != None:
        $ cho_onepiece_transp  = onepiece
    if panties != None:
        $ cho_panties_transp   = panties
    if garterbelt != None:
        $ cho_garter_transp    = garterbelt

    if gloves != None:
        $ cho_gloves_transp    = gloves
    if stockings != None:
        $ cho_stockings_transp = stockings
    if robe != None:
        $ cho_robe_transp      = robe

    if outfit != None:
        $ cho_outfit_transp    = outfit

    #call update_cho_body #Only need this when there is boobies clipping through!

    return



label update_cho_quidditch_outfit:

    $ cc_outfit_quidditch_ITEM.outfit_layers = []

    if cho_quidd_points == 0:
        $ cc_outfit_quidditch_ITEM.outfit_layers.append("../bottoms/base/pants_yoga_long.png")
    elif cho_quidd_points == 1:
        $ cc_outfit_quidditch_ITEM.outfit_layers.append("../bottoms/base/skirt_2.png")
    elif cho_quidd_points == 2:
        $ cc_outfit_quidditch_ITEM.outfit_layers.append("../bottoms/base/skirt_3.png")
    else:
        $ cc_outfit_quidditch_ITEM.outfit_layers.append("../bottoms/base/skirt_4.png")

    $ cc_outfit_quidditch_ITEM.outfit_layers.append("../tops/base/sweater_1.png")

    if cho_quidd_points in [0,1,2,3, 5,6]: #Not 4 #Wears robe!
        $ cc_outfit_quidditch_ITEM.outfit_layers.append("../robe/robe_quidditch_1.png")

    $ cc_outfit_quidditch_ITEM.outfit_layers.append("../tops/base/sweater_1_overlay.png") #Hand Overlay #Important

    $ cc_outfit_quidditch_ITEM.outfit_layers.append("../gloves/gloves_quidditch.png")

    return


label load_cho_clothing_saves:

    #Uniform & Underwear
    if cho_request_wear_top:
        $ cho_wear_top          = True
    else:
        $ cho_wear_top          = False

    if cho_request_wear_onepiece:
        $ cho_wear_onepiece     = True
    else:
        $ cho_wear_onepiece     = False

    if cho_request_wear_bra:
        $ cho_wear_bra          = True
    else:
        $ cho_wear_bra          = False

    if cho_request_wear_bottom:
        $ cho_wear_bottom       = True
    else:
        $ cho_wear_bottom       = False

    if cho_request_wear_panties:
        $ cho_wear_panties      = True
    else:
        $ cho_wear_panties      = False

    if cho_request_wear_garterbelt:
        $ cho_wear_garterbelt   = True
    else:
        $ cho_wear_garterbelt   = False

    #Other Clothing
    if cho_request_wear_neckwear:
        $ cho_wear_neckwear     = True
    else:
        $ cho_wear_neckwear     = False

    if cho_request_wear_accs:
        $ cho_wear_accs         = True
    else:
        $ cho_wear_accs         = False

    if cho_request_wear_body_accs:
        $ cho_wear_body_accs    = True
    else:
        $ cho_wear_body_accs    = False

    if cho_request_wear_gloves:
        $ cho_wear_gloves       = True
    else:
        $ cho_wear_gloves       = False

    if cho_request_wear_stockings:
        $ cho_wear_stockings    = True
    else:
        $ cho_wear_stockings    = False

    if cho_request_wear_robe:
        $ cho_wear_robe         = True
    else:
        $ cho_wear_robe         = False

    #Head Accessories
    if cho_request_wear_hat:
        $ cho_wear_hat          = True
    else:
        $ cho_wear_hat          = False

    if cho_request_wear_glasses:
        $ cho_wear_glasses      = True
    else:
        $ cho_wear_glasses      = False

    if cho_request_wear_ears:
        $ cho_wear_ears         = True
    else:
        $ cho_wear_ears         = False

    if cho_request_wear_makeup:
        $ cho_wear_makeup       = True
    else:
        $ cho_wear_makeup       = False

    if cho_request_wear_piercings:
        $ cho_wear_piercings    = True
    else:
        $ cho_wear_piercings    = False

    if cho_request_wear_tattoos:
        $ cho_wear_tattoos      = True
    else:
        $ cho_wear_tattoos      = False

    if cho_request_wear_outfit:
        $ cho_wear_outfit      = True
    else:
        $ cho_wear_outfit      = False

    return
