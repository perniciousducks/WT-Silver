

label cho_init:

    if not hasattr(renpy.store,'cho_base') or reset_persistants:
        label reset_cho_clothing:

        #Body
        $ cho_base                = "characters/cho/body/base/base_01.png"
        $ cho_arms                = "characters/cho/body/arms/side_arms.png"
        $ cho_l_hand              = "characters/cho/body/arms/left_hand.png"
        $ cho_xpos                = 300
        $ cho_ypos                = 0
        $ cho_zorder              = 5
        $ cho_flip                = 1
        $ use_cho_head            = False

        #Face
        $ cho_mouth               = "characters/cho/face/mouth/base.png"
        $ cho_eye                 = "characters/cho/face/eyes/base.png"
        $ cho_eyewhite            = "characters/cho/face/eyes/_white_.png"
        $ cho_eyebrow             = "characters/cho/face/brow/base.png"
        $ cho_pupil               = "characters/cho/face/pupil/mid.png"

        $ cho_cheeks              = "characters/cho/face/extra/cheeks_blank.png"
        $ cho_tears               = "characters/cho/face/extra/tears_blank.png"
        $ cho_extra               = "characters/cho/face/extra/blank.png"
        $ cho_emote               = "characters/emotes/blank.png"

        $ changeCho("base","base","base","mid","blank","blank","blank","blank")

        #Hair
        $ cho_hair                = "characters/cho/body/hair/hair_A_1_base.png"
        $ cho_hair_shadow         = "characters/cho/body/hair/hair_A_1_top.png"
        $ c_hair_style            = "A"
        $ c_hair_color            = 1



        #Save State
        $ cho_request_wear_top              = True
        $ cho_request_wear_bra              = True
        $ cho_request_wear_bottom           = True
        $ cho_request_wear_panties          = True

        $ cho_request_wear_onepiece         = False
        $ cho_request_wear_garterbelt       = False

        $ cho_request_wear_neckwear         = False
        $ cho_request_wear_gloves           = False
        $ cho_request_wear_stockings        = False
        $ cho_request_wear_robe             = False

        $ cho_request_wear_hat              = False
        $ cho_request_wear_glasses          = False
        $ cho_request_wear_ears             = False
        $ cho_request_wear_makeup           = False
        $ cho_request_wear_accs             = False

        $ cho_request_wear_buttplug         = False
        $ cho_request_wear_piercings        = False
        $ cho_request_wear_tattoos          = False

        $ cho_request_wear_outfit           = False

        #Toggle
        $ cho_wear_top               = True
        $ cho_wear_bra               = True
        $ cho_wear_bottom            = True
        $ cho_wear_panties           = True

        $ cho_wear_onepiece          = False
        $ cho_wear_garterbelt        = False

        $ cho_wear_neckwear          = False
        $ cho_wear_gloves            = False
        $ cho_wear_stockings         = False
        $ cho_wear_robe              = False

        $ cho_wear_hat               = False
        $ cho_wear_glasses           = False
        $ cho_wear_ears              = False
        $ cho_wear_makeup            = False
        $ cho_wear_accs              = False
        $ cho_wear_piercings         = False
        $ cho_wear_tattoos           = False

        $ cho_wear_outfit            = False



        #Clothes
        $ cho_top                 = "characters/cho/clothes/tops/base/top_1.png"
        $ c_top                   = "top_1"
        $ c_top_color             = "base"

        $ cho_bra                 = "characters/cho/clothes/underwear/base/bra_sport.png"
        $ c_bra                   = "bra_sport"
        $ c_bra_color             = "base"

        $ cho_bottom              = "characters/cho/clothes/bottoms/base/skirt_1.png"
        $ c_bottom                = "skirt_1"
        $ c_bottom_color          = "base"

        $ cho_panties             = "characters/cho/clothes/underwear/base/panties_sport.png"
        $ c_panties               = "panties_sport"
        $ c_panties_color         = "base"

        $ cho_onepiece            = "characters/cho/clothes/onepiece/blank.png"
        $ c_onepiece              = "blank"
        $ c_onepiece_color        = "base"

        $ cho_garterbelt          = "characters/cho/clothes/underwear/blank.png"
        $ c_garterbelt            = "blank"
        $ c_garterbelt_color      = "base"

        $ cho_neckwear            = "characters/cho/clothes/neckwear/blank.png"
        $ c_neckwear              = "blank"
        $ c_neckwear_color        = "base"

        $ cho_gloves              = "characters/cho/clothes/gloves/blank.png"
        $ c_gloves                = "blank"
        $ c_gloves_color          = "base"

        $ cho_stockings           = "characters/cho/clothes/stockings/stockings.png"
        $ c_stockings             = "blank"
        $ c_stockings_color       = "base"

        $ cho_robe                = "characters/cho/clothes/robe/quidditch.png"
        $ c_robe                  = "blank"
        $ c_robe_color            = "base"

        #Accessories
        $ cho_hat                 = "characters/cho/accessories/hats/blank.png"
        $ c_hat                   = "blank"
        $ c_hat_color             = "base"

        $ cho_glasses             = "characters/cho/accessories/glasses/blank.png"
        $ c_glasses               = "blank"
        $ c_glasses_color         = "base"

        $ cho_ears                = "characters/cho/accessories/ears/blank.png"
        $ c_ears                  = "blank"

        $ cho_accs                = "characters/cho/accessories/blank.png"

        #Outfits
        $ cho_outfit_GLBL = None
        $ cho_temp_outfit = None


    return


label cho_progress_init:

    # Update 1.3
    if not hasattr(renpy.store,'cho_whoring') or reset_persistants or reset_cho_content:

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
        $ cho_met = False #Replaced! Not in use anymore!

    # Update 1.32
    if not hasattr(renpy.store,'cho_quidd') or reset_persistants or reset_cho_content:

        $ cho_quidd = False
        $ days_since_quidd = 0
        $ cho_quidd_points = 0

    # Update 1.33
    if not hasattr(renpy.store,'first_cho_favor_done') or reset_persistants or reset_cho_content:

        $ cho_unlocked = False

        $ cho_genie_name = "Professor"
        $ cho_name = "Cho"

        $ first_cho_favor_done = False

    # Update 1.34
    if not hasattr(renpy.store,'cho_wardrobe_unlocked') or reset_persistants or reset_cho_content:

        $ cho_wardrobe_unlocked = False



    return
