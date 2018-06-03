

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
    
    if astoria_wear_top and ast_top == top:
        $ ast_request_wear_top = False
        $ astoria_wear_top = False
    else:
        $ ast_request_wear_top = True
        $ astoria_wear_top = True
        $ ast_top = top
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Bottom equip.    
label set_ast_bottom(bottom=""):
    hide screen astoria_main
    
    if astoria_wear_bottom and ast_skirt == bottom:
        $ ast_request_wear_bottom = False
        $ astoria_wear_bottom = False
    else:
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
    
    if astoria_wear_onepiece and ast_onepiece == onepiece:
        $ ast_request_wear_onepiece = False
        $ astoria_wear_onepiece = False
    else:
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
    
    if astoria_wear_garterbelt and ast_garterbelt == garter:
        $ ast_request_wear_garterbelt = False
        $ astoria_wear_garterbelt = False
    else:
        $ ast_request_wear_garterbelt = True
        $ astoria_wear_garterbelt = True
        $ ast_garterbelt = garter
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Neckwear equip.    
label set_ast_neckwear(neck=""):
    hide screen astoria_main
    
    if astoria_wear_neckwear and ast_neckwear == neck:
        $ ast_request_wear_neckwear = False
        $ astoria_wear_neckwear = False
    else:
        $ ast_request_wear_neckwear = True
        $ astoria_wear_neckwear = True
        $ ast_neckwear = neck
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
#Stockings equip.    
label set_ast_stockings(stockings=""):
    hide screen astoria_main
    
    if astoria_wear_stockings and ast_stockings == stockings:
        $ ast_request_wear_stockings = False
        $ astoria_wear_stockings = False
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
    
    if astoria_wear_robe and ast_robe == robe:
        $ ast_request_wear_robe = False
        $ astoria_wear_robe = False
    else:
        $ ast_request_wear_robe = True
        $ astoria_wear_robe = True
        $ ast_robe = robe
    
    call update_ast_uniform
    show screen astoria_main
    
    return
    
    
    
    
    
    
label load_astoria_clothing_saves:

    #Uniform & Underwear
    if ast_request_wear_top:
        $ astoria_wear_top          = True
    else:
        $ astoria_wear_top          = False

    if ast_request_wear_onepiece:
        $ astoria_wear_onepiece     = True
    else:
        $ astoria_wear_onepiece     = False

    if ast_request_wear_bra:
        $ astoria_wear_bra          = True
    else:
        $ astoria_wear_bra          = False

    if ast_request_wear_bottom:
        $ astoria_wear_bottom       = True
    else:
        $ astoria_wear_bottom       = False

    if ast_request_wear_panties:
        $ astoria_wear_panties      = True 
    else:
        $ astoria_wear_panties      = False

    if ast_request_wear_garterbelt:
        $ astoria_wear_garterbelt   = True 
    else:
        $ astoria_wear_garterbelt   = False

    #Other Clothing
    if ast_request_wear_neckwear:
        $ astoria_wear_neckwear     = True
    else:
        $ astoria_wear_neckwear     = False

    if ast_request_wear_accs:
        $ astoria_wear_accs    = True
    else:
        $ astoria_wear_accs    = False

    if ast_request_wear_gloves:
        $ astoria_wear_gloves       = True
    else:
        $ astoria_wear_gloves       = False

    if ast_request_wear_stockings:
        $ astoria_wear_stockings    = True
    else:
        $ astoria_wear_stockings    = False

    if ast_request_wear_robe:
        $ astoria_wear_robe         = True
    else:
        $ astoria_wear_robe         = False

    #Head Accessories
    if ast_request_wear_hat:
        $ astoria_wear_hat          = True
    else:
        $ astoria_wear_hat          = False

    if ast_request_wear_glasses:
        $ astoria_wear_glasses      = True
    else:
        $ astoria_wear_glasses      = False

    if ast_request_wear_ears:
        $ astoria_wear_ears         = True
    else:
        $ astoria_wear_ears         = False

    if ast_request_wear_makeup:
        $ astoria_wear_makeup       = True
    else:
        $ astoria_wear_makeup       = False

    if ast_request_wear_piercings:
        $ astoria_wear_piercings    = True
    else:
        $ astoria_wear_piercings    = False

    if ast_request_wear_tattoos:
        $ astoria_wear_tattoos      = True
    else:
        $ astoria_wear_tattoos      = False

    return