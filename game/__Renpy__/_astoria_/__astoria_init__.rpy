

label astoria_init:

    #Body
    $ cc_base                = "characters/astoria/base/base_01.png" 
    $ cc_arms                = "characters/astoria/base/side_arms.png" 
    $ cc_l_hand              = "characters/astoria/base/left_hand.png" 
    $ cc_hair                = "characters/astoria/base/hair_01.png" 
    $ cc_hair_shadow         = "characters/astoria/base/hair_shadow.png" 
    $ cc_xpos                = 300
    $ cc_ypos                = 0
    $ cc_zorder              = 5

    #Face
    $ cc_mouth               = "characters/astoria/mouth/mouth_01.png" 
    $ cc_eye                 = "characters/astoria/eye/eye_01.png" 
    $ cc_eyebrow             = "characters/astoria/eye/eyebrow_01.png" 
    $ cc_pupil               = "characters/astoria/eye/pupil_01.png" 
    $ cc_tears               = "characters/astoria/tears/tears_0.png" 

    #Clothes
    $ cc_vest                = "characters/astoria/clothes/uniform/vest.png" 
    $ cc_top                 = "characters/astoria/clothes/uniform/top.png" 
    $ cc_acc                 = "characters/astoria/clothes/uniform/tie.png" 
    $ cc_skirt               = "characters/astoria/clothes/uniform/skirt.png" 
    $ cc_stock               = "characters/astoria/clothes/uniform/stockings.png" 
    $ cc_bra                 = "characters/astoria/clothes/workout/bra.png" 
    $ cc_panties             = "characters/astoria/clothes/workout/panties.png" 

    $ cc_wear_top            = True
    $ cc_wear_bra            = True
    $ cc_wear_skirt          = True
    $ cc_wear_panties        = True
    $ cc_wear_stockings      = True 
    $ cc_wear_vest           = True
    $ cc_wear_acc            = True

    return


label astoria_progress_init:

    ##Favour stuff
    

    ##Stats
    $ astoria_spell_progress = 0
    $ astoria_spell = "imperio"
    $ astoria_points = 0

    ##Flags
    $ astoria_busy = False
    $ days_since_astoria = 0
    $ astoria_arrival_day = 30
    $ astoria_arrvial_whoring = 9


return
