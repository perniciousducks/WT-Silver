

label cho_init:
    pass

if not hasattr(renpy.store,'cc_base') or reset_persistants:

    #Body
    $ cc_base                = "characters/cho/base/base_01.png" 
    $ cc_arms                = "characters/cho/base/side_arms.png" 
    $ cc_l_hand              = "characters/cho/base/left_hand.png" 
    $ cc_hair                = "characters/cho/base/hair_01.png" 
    $ cc_hair_shadow         = "characters/cho/base/hair_shadow.png" 
    $ cc_xpos                = 300
    $ cc_ypos                = 0
    $ cc_zorder              = 5

    #Face
    $ cc_mouth               = "characters/cho/mouth/mouth_01.png" 
    $ cc_eye                 = "characters/cho/eye/eye_01.png" 
    $ cc_eyebrow             = "characters/cho/eye/eyebrow_01.png" 
    $ cc_pupil               = "characters/cho/eye/pupil_01.png" 
    $ cc_tears               = "characters/cho/tears/tears_0.png" 

    #Clothes
    $ cc_vest                = "characters/cho/clothes/uniform/vest.png" 
    $ cc_top                 = "characters/cho/clothes/uniform/top.png" 
    $ cc_acc                 = "characters/cho/clothes/uniform/tie.png" 
    $ cc_skirt               = "characters/cho/clothes/uniform/skirt.png" 
    $ cc_stock               = "characters/cho/clothes/uniform/stockings.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 

    $ cc_wear_top            = True
    $ cc_wear_bra            = True
    $ cc_wear_skirt          = True
    $ cc_wear_panties        = True
    $ cc_wear_stockings      = True 
    $ cc_wear_vest           = True
    $ cc_wear_acc            = True

#if not hasattr(renpy.store,'ADD') or reset_persistants:

return


label cho_progress_init:
    pass

if not hasattr(renpy.store,'cho_whoring') or reset_persistants:
    ##Favour stuff
    $ chof2_first = True

    ##Stats
    $ cho_whoring = 0
    $ cho_mad = 0
    $ cho_points = 0

    ##Flags
    $ cho_busy = False
    $ days_since_cho = 0
    $ cho_known = False
    $ cho_met = False

#if not hasattr(renpy.store,'ADD') or reset_persistants:

return
