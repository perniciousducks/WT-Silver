

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
    
    $ sus_request_wear_top = True
    $ susan_wear_top = True
    $ sus_top = top
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Bottom equip.    
label set_sus_bottom(bottom=""):
    hide screen susan_main
    
    $ sus_request_wear_bottom = True
    $ susan_wear_bottom = True
    $ sus_skirt = bottom
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Bra equip.    
label set_sus_bra(bra=""):
    hide screen susan_main
    
    $ sus_request_wear_bra = True
    $ susan_wear_bra = True
    $ sus_bra = bra
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#One-Piece equip.    
label set_sus_onepiece(onepiece=""):
    hide screen susan_main
    
    $ sus_request_wear_onepiece = True
    $ susan_wear_onepiece = True
    $ sus_onepiece = onepiece
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Panties equip.    
label set_sus_panties(panties=""):
    hide screen susan_main
    
    $ sus_request_wear_panties = True
    $ susan_wear_panties = True
    $ sus_panties = panties
    
    call update_sus_uniform
    show screen susan_main
    
    return
    
#Garterbelt equip.    
label set_sus_garterbelt(garter=""):
    hide screen susan_main
    
    if susan_wear_garterbelt:
        $ sus_request_wear_garterbelt = False
        $ susan_wear_garterbelt = False
        $ sus_garterbelt = garter
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
    
    if susan_wear_stockings:
        $ sus_request_wear_stockings = False
        $ susan_wear_stockings = False
        $ sus_stockings = stockings
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
    
    if susan_wear_robe:
        $ sus_request_wear_robe = False
        $ susan_wear_robe = False
        $ sus_robe = robe
    else:
        $ sus_request_wear_robe = True
        $ susan_wear_robe = True
        $ sus_robe = robe
    
    call update_sus_uniform
    show screen susan_main
    
    return