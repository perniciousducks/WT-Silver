

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
    
    if astoria_wear_top:
        $ ast_request_wear_top = False
        $ astoria_wear_top = False
    else:
        $ ast_request_wear_top = True
        $ astoria_wear_top = True
        $ ast_top = top
    
    call update_ast_uniform
    
    show screen astoria_main
    
    return