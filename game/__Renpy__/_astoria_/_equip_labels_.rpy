

#ASTORIA EQUIP

label update_ast_uniform:
    hide screen astoria_main
    
    #Top
    $ astoria_top            = "characters/astoria/clothes/tops/base/"+str(ast_top)+".png"
    
    #Bottom
    $ astoria_skirt          = "characters/astoria/clothes/bottoms/base/"+str(ast_skirt)+".png"

    #Underwear
    $ astoria_bra            = "characters/astoria/clothes/underwear/base/"+str(ast_bra)+".png"
    $ astoria_onepiece       = "characters/astoria/clothes/onepieces/base/"+str(ast_onepiece)+".png"
    $ astoria_panties        = "characters/astoria/clothes/underwear/base/"+str(ast_panties)+".png"
    $ astoria_garterbelt     = "characters/astoria/clothes/underwear/base/"+str(ast_garterbelt)+".png"
    
    $ astoria_neckwear       = "characters/astoria/clothes/neckwear/base/"+str(ast_neckwear)+".png"
    $ astoria_gloves         = "characters/astoria/clothes/gloves/base/"+str(ast_gloves)+".png"
    $ astoria_stockings      = "characters/astoria/clothes/stockings/base/"+str(ast_stockings)+".png"
    $ astoria_robe           = "characters/astoria/clothes/robe/base/"+str(ast_robe)+".png"
    
    return
    
    
#Top equip.    
label set_ast_top(top=""):
    hide screen astoria_main
    
    $ ast_request_wear_top = True
    $ astoria_wear_top = True
    $ ast_top = top
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Bottom equip.    
label set_ast_bottom(bottom=""):
    hide screen astoria_main
    
    $ ast_request_wear_bottom = True
    $ astoria_wear_bottom = True
    $ ast_skirt = bottom
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Bra equip.    
label set_ast_bra(bra=""):
    hide screen astoria_main
    
    $ ast_request_wear_bra = True
    $ astoria_wear_bra = True
    $ ast_bra = bra
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#One-Piece equip.    
label set_ast_onepiece(onepiece=""):
    hide screen astoria_main
    
    $ ast_request_wear_onepiece = True
    $ astoria_wear_onepiece = True
    $ ast_onepiece = onepiece
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Panties equip.    
label set_ast_panties(panties=""):
    hide screen astoria_main
    
    $ ast_request_wear_panties = True
    $ astoria_wear_panties = True
    $ ast_panties = panties
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Garterbelt equip.    
label set_ast_garterbelt(garter=""):
    hide screen astoria_main
    
    if astoria_wear_garterbelt:
        $ ast_request_wear_garterbelt = False
        $ astoria_wear_garterbelt = False
        $ ast_garterbelt = garter
    else:
        $ ast_request_wear_garterbelt = True
        $ astoria_wear_garterbelt = True
        $ ast_garterbelt = garter
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Stockings equip.    
label set_ast_stockings(stockings=""):
    hide screen astoria_main
    
    if astoria_wear_stockings:
        $ ast_request_wear_stockings = False
        $ astoria_wear_stockings = False
        $ ast_stockings = stockings
    else:
        $ ast_request_wear_stockings = True
        $ astoria_wear_stockings = True
        $ ast_stockings = stockings
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Robe equip.    
label set_ast_robe(robe=""):
    hide screen astoria_main
    
    if astoria_wear_robe:
        $ ast_request_wear_robe = False
        $ astoria_wear_robe = False
        $ ast_robe = robe
    else:
        $ ast_request_wear_robe = True
        $ astoria_wear_robe = True
        $ ast_robe = robe
    
    call update_ast_uniform
    show screen astoria_main
    
    return