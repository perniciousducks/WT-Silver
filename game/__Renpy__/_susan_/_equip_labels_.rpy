

#SUSAN EQUIP

label update_sus_uniform:
    hide screen susan_main
    
    #Top
    $ susan_top            = "characters/susan/clothes/tops/base/"+str(sus_top)+".png"
    
    #Bottom
    $ susan_skirt          = "characters/susan/clothes/bottoms/base/"+str(sus_skirt)+".png"

    #Underwear
    $ susan_bra            = "characters/susan/clothes/underwear/base/"+str(sus_bra)+".png"
    $ susan_onepiece       = "characters/susan/clothes/onepieces/base/"+str(sus_onepiece)+".png"
    $ susan_panties        = "characters/susan/clothes/underwear/base/"+str(sus_panties)+".png"
    $ susan_garterbelt     = "characters/susan/clothes/underwear/base/"+str(sus_garterbelt)+".png"
    
    $ susan_neckwear       = "characters/susan/clothes/neckwear/base/"+str(sus_neckwear)+".png"
    $ susan_gloves         = "characters/susan/clothes/gloves/base/"+str(sus_gloves)+".png"
    $ susan_stockings      = "characters/susan/clothes/stockings/base/"+str(sus_stockings)+".png"
    $ susan_robe           = "characters/susan/clothes/robe/base/"+str(sus_robe)+".png"
    
    return
    
    
#Top equip.    
label set_sus_top(top=""):
    hide screen susan_main
    
    if susan_wear_top and sus_top == top:
        $ sus_request_wear_top = False
        $ susan_wear_top = False
    else:
        $ sus_request_wear_top = True
        $ susan_wear_top = True
        $ sus_top = top
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Bottom equip.    
label set_sus_bottom(bottom=""):
    hide screen susan_main
    
    if susan_wear_bottom and sus_skirt == bottom:
        $ sus_request_wear_bottom = False
        $ susan_wear_bottom = False
    else:
        $ sus_request_wear_bottom = True
        $ susan_wear_bottom = True
        $ sus_skirt = bottom
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Bra equip.    
label set_sus_bra(bra=""):
    hide screen susan_main
    
    if susan_wear_bra and sus_bra == bra:
        $ sus_request_wear_bra = False
        $ susan_wear_bra = False
    else:
        $ sus_request_wear_bra = True
        $ susan_wear_bra = True
        $ sus_bra = bra
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#One-Piece equip.    
label set_sus_onepiece(onepiece=""):
    hide screen susan_main
    
    if susan_wear_onepiece and sus_onepiece == onepiece:
        $ sus_request_wear_onepiece = False
        $ susan_wear_onepiece = False
    else:
        $ sus_request_wear_onepiece = True
        $ susan_wear_onepiece = True
        $ sus_onepiece = onepiece
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Panties equip.    
label set_sus_panties(panties=""):
    hide screen susan_main
    
    if susan_wear_panties and sus_panties == panties:
        $ sus_request_wear_panties = False
        $ susan_wear_panties = False
    else:
        $ sus_request_wear_panties = True
        $ susan_wear_panties = True
        $ sus_panties = panties
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Garterbelt equip.    
label set_sus_garterbelt(garter=""):
    hide screen susan_main
    
    if susan_wear_garterbelt and sus_garterbelt == garter:
        $ sus_request_wear_garterbelt = False
        $ susan_wear_garterbelt = False
    else:
        $ sus_request_wear_garterbelt = True
        $ susan_wear_garterbelt = True
        $ sus_garterbelt = garter
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Stockings equip.    
label set_sus_stockings(stockings=""):
    hide screen susan_main
    
    if susan_wear_stockings and sus_stockings == stockings:
        $ sus_request_wear_stockings = False
        $ susan_wear_stockings = False
    else:
        $ sus_request_wear_stockings = True
        $ susan_wear_stockings = True
        $ sus_stockings = stockings
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Robe equip.    
label set_sus_robe(robe=""):
    hide screen susan_main
    
    if susan_wear_robe and sus_robe == robe:
        $ sus_request_wear_robe = False
        $ susan_wear_robe = False
    else:
        $ sus_request_wear_robe = True
        $ susan_wear_robe = True
        $ sus_robe = robe
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
    
    
    
    
    
label load_susan_clothing_saves:

    #Uniform & Underwear
    if sus_request_wear_top:
        $ susan_wear_top          = True
    else:
        $ susan_wear_top          = False

    if sus_request_wear_onepiece:
        $ susan_wear_onepiece     = True
    else:
        $ susan_wear_onepiece     = False

    if sus_request_wear_bra:
        $ susan_wear_bra          = True
    else:
        $ susan_wear_bra          = False

    if sus_request_wear_bottom:
        $ susan_wear_bottom       = True
    else:
        $ susan_wear_bottom       = False

    if sus_request_wear_panties:
        $ susan_wear_panties      = True 
    else:
        $ susan_wear_panties      = False

    if sus_request_wear_garterbelt:
        $ susan_wear_garterbelt   = True 
    else:
        $ susan_wear_garterbelt   = False

    #Other Clothing
    if sus_request_wear_neckwear:
        $ susan_wear_neckwear     = True
    else:
        $ susan_wear_neckwear     = False

    if sus_request_wear_accs:
        $ susan_wear_accs    = True
    else:
        $ susan_wear_accs    = False

    if sus_request_wear_gloves:
        $ susan_wear_gloves       = True
    else:
        $ susan_wear_gloves       = False

    if sus_request_wear_stockings:
        $ susan_wear_stockings    = True
    else:
        $ susan_wear_stockings    = False

    if sus_request_wear_robe:
        $ susan_wear_robe         = True
    else:
        $ susan_wear_robe         = False

    #Head Accessories
    if sus_request_wear_hat:
        $ susan_wear_hat          = True
    else:
        $ susan_wear_hat          = False

    if sus_request_wear_glasses:
        $ susan_wear_glasses      = True
    else:
        $ susan_wear_glasses      = False

    if sus_request_wear_ears:
        $ susan_wear_ears         = True
    else:
        $ susan_wear_ears         = False

    if sus_request_wear_makeup:
        $ susan_wear_makeup       = True
    else:
        $ susan_wear_makeup       = False

    if sus_request_wear_piercings:
        $ susan_wear_piercings    = True
    else:
        $ susan_wear_piercings    = False

    if sus_request_wear_tattoos:
        $ susan_wear_tattoos      = True
    else:
        $ susan_wear_tattoos      = False

    return