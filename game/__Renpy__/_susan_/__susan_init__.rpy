

label susan_init:

    if not hasattr(renpy.store,'susan_base') or reset_persistants:
        label reset_susan_clothing:

        #Body
        $ susan_base                = "characters/susan/body/base/base_01.png"
        $ susan_breasts               = "characters/susan/body/base/boobs_nipfix.png"
        $ susan_l_arm               = "characters/susan/body/arms/l_arm_back.png"
        $ susan_r_arm               = "characters/susan/body/arms/r_arm_thigh.png"
        $ susan_xpos                = 300
        $ susan_ypos                = 0
        $ susan_zorder              = 5
        $ susan_flip                = 1
        $ use_susan_head            = False

        #Face
        $ susan_mouth               = "characters/susan/face/mouth/base.png"
        $ sus_mouth                 = "base"
        $ sus_lipstick              = "nude"

        $ susan_eye                 = "characters/susan/face/eyes/base.png"
        $ susan_eye_bg            = "characters/susan/face/eyes/_white_.png"
        $ susan_pupil               = "characters/susan/face/pupil/mid.png"
        $ sus_eye_color             = "green"

        $ susan_eyebrow             = "characters/susan/face/brow/base.png"

        $ susan_cheeks              = "characters/susan/face/extras/cheeks_blank.png"
        $ susan_tears               = "characters/susan/face/extras/tears_blank.png"
        $ susan_extra               = "characters/susan/face/extras/blank.png"
        $ susan_emote               = "characters/emotes/blank.png"

        #$ changeCho("base","base","base","mid","blank","blank","blank","blank")

        #Chibi
        $ sus_chibi_xpos          = 500
        $ sus_chibi_ypos          = 250
        $ sus_chibi_flip          = 1
        $ sus_speed               = 2.0
        $ sus_chibi_zorder        = 3

        $ susan_chibi_stand         = "ch_sus blink"
        $ susan_chibi_shoes         = "characters/susan/chibis/sb_walk_01_shoes.png"

        $ susan_chibi_walk          = "ch_sus walk"
        $ susan_chibi_walk_shoes    = "ch_sus walk_shoes"

        $ susan_chibi_top           = "characters/susan/chibis/sb_cloth_shirt_h.png"
        $ susan_chibi_bottom        = "characters/susan/chibis/sb_cloth_skirt.png"
        $ susan_chibi_robe          = "characters/susan/chibis/blank.png"

        #Hair
        $ susan_hair                = "characters/susan/body/hair/braided_red_base.png"
        $ susan_hair_shadow         = "characters/susan/body/hair/braided_red_top.png"
        $ sus_hair_style            = "braided"
        $ sus_hair_color            = "red"

        #Clothes

        #Save State
        $ sus_request_wear_top              = True
        $ sus_request_wear_bra              = True
        $ sus_request_wear_bottom           = True
        $ sus_request_wear_panties          = True

        $ sus_request_wear_onepiece         = False
        $ sus_request_wear_garterbelt       = False

        $ sus_request_wear_neckwear         = False
        $ sus_request_wear_gloves           = False
        $ sus_request_wear_stockings        = False
        $ sus_request_wear_robe             = False

        $ sus_request_wear_hat              = False
        $ sus_request_wear_glasses          = False
        $ sus_request_wear_ears             = False
        $ sus_request_wear_makeup           = False
        $ sus_request_wear_accs             = False

        $ sus_request_wear_buttplug         = False
        $ sus_request_wear_piercings        = False
        $ sus_request_wear_tattoos          = False

        $ sus_request_wear_outfit           = False

        #Toggle
        $ susan_wear_top               = True
        $ susan_wear_bra               = True
        $ susan_wear_bottom            = True
        $ susan_wear_panties           = True

        $ susan_wear_onepiece          = False
        $ susan_wear_garterbelt        = False

        $ susan_wear_neckwear          = False
        $ susan_wear_gloves            = False
        $ susan_wear_stockings         = False
        $ susan_wear_robe              = False

        $ susan_wear_hat               = False
        $ susan_wear_glasses           = False
        $ susan_wear_ears              = False
        $ susan_wear_makeup            = False
        $ susan_wear_accs              = False
        $ susan_badges                 = False
        $ susan_wear_piercings         = False
        $ susan_wear_tattoos           = False

        $ susan_wear_outfit            = False

        #Top
        $ susan_top                 = "characters/susan/clothes/tops/top_1.png"
        $ sus_top                     = "top_1"
        $ sus_top_color               = "base"

        #Bottom
        $ susan_bottom              = "characters/susan/clothes/bottoms/skirt_1.png"
        $ sus_bottom                  = "skirt_1"
        $ sus_bottom_color            = "base"

        #Underwear
        $ susan_bra                 = "characters/susan/clothes/bras/bra_base.png"
        $ sus_bra                     = "bra_base"
        $ sus_bra_color               = "base"

        $ susan_panties             = "characters/susan/clothes/panties/panties_base.png"
        $ sus_panties                 = "panties_base"
        $ sus_panties_color           = "base"

        $ susan_onepiece            = "characters/susan/clothes/onepieces/blank.png"
        $ sus_onepiece                = "blank"
        $ sus_onepiece_color          = "base"

        $ susan_garterbelt          = "characters/susan/clothes/garterbelts/blank.png"
        $ sus_garterbelt              = "blank"
        $ sus_garterbelt_color        = "base"


        #Other Clothing
        $ susan_neckwear            = "characters/susan/clothes/neckwear/blank.png"
        $ sus_neckwear                = "blank"
        $ sus_neckwear_color          = "base"

        $ susan_accs_list           = []

        $ susan_gloves              = "characters/susan/clothes/gloves/blank.png"
        $ sus_gloves                  = "blank"
        $ sus_gloves_color            = "base"

        $ susan_stockings           = "characters/susan/clothes/stockings/blank.png"
        $ sus_stockings               = "blank"
        $ sus_stockings_color         = "base"

        $ susan_robe                = "characters/susan/clothes/robe/blank.png"
        $ sus_robe                    = "blank"
        $ sus_robe_color              = "base"


        #Accessories
        $ susan_makeup_list         = []

        $ susan_hat                 = "characters/susan/clothes/hats/blank.png"
        $ sus_hat                     = "blank"
        $ sus_hat_color               = "base"

        $ susan_glasses             = "characters/susan/clothes/glasses/blank.png"
        $ sus_glasses                 = "blank"
        $ sus_glasses_color           = "base"

        $ susan_ears                = "characters/susan/clothes/ears/blank.png"
        $ sus_ears                    = "blank"

        #Outfits
        $ susan_outfit_GLBL = None
        $ susan_temp_outfit = None

        #Cum layers
        $ susan_face_covered        = False
        $ susan_face_cum            = "characters/susan/face/cum/cum_0.png"

        $ susan_body_covered        = False
        $ susan_body_cum            = "characters/susan/face/cum/cum_3.png"

        $ susan_aftersperm          = False
        $ susan_clothes_cum         = "characters/susan/face/cum/aftersperm.png"

    #if not hasattr(renpy.store,'ADD') or reset_persistants:


    call susan_face_layers

    return


label susan_progress_init:

    if not hasattr(renpy.store,'susan_busy') or reset_persistants:

        #Stats
        $ sus_whoring = 0
        $ sus_mood = 0

        #Flags
        $ susan_busy = False
        $ susan_unlocked = False
        $ susan_wardrobe_unlocked = False
        $ chitchated_with_susan = False

        #Favour stuff
        $ susan_imperio_influence = False
        $ susan_imperio_counter = 0 #Maybe the higher Astoria's spell level gets, the longer this lasts?

        #Names
        $ susan_name = "Miss Bones"
        $ sus_genie_name = "Sir"

        #Stats Screen
        $ sus_curse_counter = 2 #She got cursed twice beforeyou unlock her. Poor girl...

    if not hasattr(renpy.store,'gave_susan_gift') or reset_persistants:
        $ gave_susan_gift    = False

    return
