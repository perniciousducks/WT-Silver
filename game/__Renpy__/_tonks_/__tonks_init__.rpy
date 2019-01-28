

label tonks_init:

    if not hasattr(renpy.store,'tonks_base') or reset_persistants:
        label reset_tonks_clothing:

        #Body
        $ tonks_base                = "characters/tonks/body/base/base_01.png"
        $ tonks_boobs               = "characters/tonks/body/base/boobs_0.png"
        $ tonks_l_arm               = "characters/tonks/body/arms/l_arm_hips.png"
        $ tonks_l_hand              = "characters/tonks/body/arms/l_hand_hips.png"
        $ tonks_r_arm               = "characters/tonks/body/arms/r_arm_up.png"
        $ tonks_xpos                = 600
        $ tonks_ypos                = 0
        $ tonks_zorder              = 5
        $ tonks_flip                = 1
        $ use_tonks_head            = False

        #Face
        $ tonks_mouth               = "characters/tonks/face/mouth/base.png"

        $ tonks_eye                 = "characters/tonks/face/eyes/base.png"
        $ tonks_eye_bg              = "characters/tonks/face/eyes/_white_.png"
        $ tonks_pupil               = "characters/tonks/face/pupil/mid.png"

        $ tonks_eyebrow             = "characters/tonks/face/brow/base.png"

        $ tonks_cheeks              = "characters/tonks/face/extras/cheeks_blank.png"
        $ tonks_tears               = "characters/tonks/face/extras/tears_blank.png"
        $ tonks_extra               = "characters/tonks/face/extras/blank.png"
        $ tonks_emote               = "characters/emotes/blank.png"

        $ changeTonks("base","base","base","mid","blank","blank","blank","blank")

        #Hair
        $ tonks_hair_shadow         = "characters/tonks/body/hair/_hair_shadow_.png"
        $ tonks_hair                = "characters/tonks/body/hair/short_pink.png"
        $ ton_hair_style            = "short"
        $ ton_hair_color            = "pink"
        $ tonks_pubic_hair          = "characters/tonks/body/hair/pubes_arrow_pink.png"
        $ ton_pubic_hair            = "arrow"

        #Clothes

        #Save State
        $ ton_request_wear_top              = True
        $ ton_request_wear_bra              = True
        $ ton_request_wear_bottom           = False
        $ ton_request_wear_panties          = True

        $ ton_request_wear_onepiece         = False
        $ ton_request_wear_garterbelt       = False

        $ ton_request_wear_neckwear         = True
        $ ton_request_wear_gloves           = True
        $ ton_request_wear_stockings        = True
        $ ton_request_wear_robe             = True

        $ ton_request_wear_hat              = False
        $ ton_request_wear_glasses          = False
        $ ton_request_wear_ears             = False
        $ ton_request_wear_makeup           = False
        $ ton_request_wear_accs             = False

        $ ton_request_wear_pubic_hair       = False
        $ ton_request_wear_buttplug         = False
        $ ton_request_wear_piercings        = True
        $ ton_request_wear_tattoos          = False
        $ ton_request_wear_mask             = False
        $ ton_request_wear_gag              = False

        $ ton_request_wear_outfit           = False

        #Toggle
        $ tonks_wear_top               = True
        $ tonks_wear_bra               = True
        $ tonks_wear_bottom            = False
        $ tonks_wear_panties           = True

        $ tonks_wear_onepiece          = False
        $ tonks_wear_garterbelt        = False

        $ tonks_wear_neckwear          = True
        $ tonks_wear_gloves            = True
        $ tonks_wear_stockings         = True
        $ tonks_wear_robe              = True

        $ tonks_wear_hat               = False
        $ tonks_wear_glasses           = False
        $ tonks_wear_ears              = False
        $ tonks_wear_makeup            = False
        $ tonks_wear_accs              = False
        $ tonks_badges                 = False

        $ tonks_wear_pubic_hair        = False
        $ tonks_wear_piercings         = True
        $ tonks_wear_tattoos           = False
        $ tonks_wear_mask              = False
        $ tonks_wear_gag               = False

        $ tonks_wear_outfit            = False



        #Top
        $ tonks_top                 = "characters/tonks/clothes/tops/base/top_auror_1.png"
        $ ton_top                     = "top_auror_1"
        $ ton_top_color               = "base"

        #Bottom
        $ tonks_bottom               = "characters/tonks/clothes/bottoms/base/blank.png"
        $ ton_bottom                   = "blank"
        $ ton_bottom_color             = "base"

        #Underwear
        $ tonks_bra                 = "characters/tonks/clothes/underwear/base/blank.png"
        $ ton_bra                     = "blank"
        $ ton_bra_color               = "base"

        $ tonks_panties             = "characters/tonks/clothes/underwear/base/blank.png"
        $ ton_panties                 = "blank"
        $ ton_panties_color           = "base"

        $ tonks_onepiece            = "characters/tonks/clothes/onepieces/blank.png"
        $ ton_onepiece                = "blank"
        $ ton_onepiece_color          = "base"

        $ tonks_garterbelt          = "characters/tonks/clothes/underwear/base/blank.png"
        $ ton_garterbelt              = "blank"
        $ ton_garterbelt_color        = "base"


        #Other Clothing
        $ tonks_neckwear            = "characters/tonks/clothes/neckwear/choker_beads.png"
        $ ton_neckwear                = "choker_beads"
        $ ton_neckwear_color          = "base"

        $ tonks_accs_list           = []
        $ tonks_accs                = "characters/tonks/accessories/blank.png"

        $ tonks_gloves              = "characters/tonks/clothes/gloves/auror_gloves.png"
        $ ton_gloves                  = "auror_gloves"
        $ ton_gloves_color            = "base"

        $ tonks_stockings           = "characters/tonks/clothes/stockings/stockings_auror.png"
        $ ton_stockings               = "stockings_auror"
        $ ton_stockings_color         = "base"

        $ tonks_robe                = "characters/tonks/clothes/robe/auror_coat.png"
        $ tonks_robe_back           = "characters/tonks/clothes/robe/auror_coat_back.png"
        $ ton_robe                    = "auror_coat"
        $ ton_robe_color              = "base"


        #Accessories
        $ tonks_makeup_list         = []

        $ tonks_hat                 = "characters/tonks/accessories/hats/blank.png"
        $ ton_hat                     = "blank"
        $ ton_hat_color               = "base"

        $ tonks_glasses             = "characters/tonks/accessories/glasses/blank.png"
        $ ton_glasses                 = "blank"
        $ ton_glasses_color           = "base"

        $ tonks_ears                = "characters/tonks/accessories/ears/blank.png"
        $ ton_ears                    = "blank"

        #Miscellaneous
        $ tonks_buttplug            = "characters/tonks/accessories/plugs/blank.png"
        $ ton_buttplug                = "blank"
        $ tonks_mask                = "characters/tonks/accessories/masks/blank.png"
        $ ton_mask                    = "blank"
        $ tonks_gag                 = "characters/tonks/face/mouth/gag.png"
        $ ton_gag                     = "gag"

        #Piercings
        $ tonks_ear_piercing        = "characters/tonks/accessories/piercings/ears_rings.png"
        $ ton_ear_piercing            = "ears_rings"
        $ ton_ear_piercing_color      = "base"

        $ tonks_tongue_piercing     = "characters/tonks/accessories/piercings/blank.png"
        $ ton_tongue_piercing         = "tongue_pearls"
        $ ton_tongue_piercing_color   = "base"

        $ tonks_nipple_piercing     = "characters/tonks/accessories/piercings/nipples_pearls.png"
        $ ton_nipple_piercing         = "nipples_pearls"
        $ ton_nipple_piercing_color   = "base"

        $ tonks_belly_piercing      = "characters/tonks/accessories/piercings/belly_pearls.png"
        $ ton_belly_piercing          = "belly_pearls"
        $ ton_belly_piercing_color    = "base"

        $ tonks_genital_piercing    = "characters/tonks/accessories/piercings/blank.png"
        $ ton_genital_piercing        = "blank"
        $ ton_genital_piercing_color  = "base"

        call reset_ton_transparency

        #Outfits
        $ tonks_outfit_GLBL = None
        $ tonks_temp_outfit = None

        #Cum layers
        $ tonks_face_covered        = False
        $ tonks_face_cum            = "characters/tonks/face/cum/cum_0.png"

        $ tonks_body_covered        = False
        $ tonks_body_cum            = "characters/tonks/face/cum/cum_3.png"

        $ tonks_aftersperm          = False
        $ tonks_clothes_cum         = "characters/tonks/face/cum/aftersperm.png"


    call tonks_face_layers

    return

label reset_ton_transparency:
    $ ton_top_transp       = 1
    $ ton_bottom_transp    = 1

    $ ton_bra_transp       = 1
    $ ton_onepiece_transp  = 1
    $ ton_panties_transp   = 1
    $ ton_garter_transp    = 1

    $ ton_gloves_transp    = 1
    $ ton_stockings_transp = 1
    $ ton_robe_transp      = 1

    $ ton_outfit_transp    = 1

    return



label tonks_progress_init:

    if not hasattr(renpy.store,'tonks_unlocked') or reset_persistants:

        #Stats
        $ ton_friendship = 0 #Max is 100.
        $ ton_support = 0
        $ ton_reputation = 0
        $ ton_clothing_level = 100

        #Flags
        $ tonks_busy = False
        $ tonks_unlocked = False
        $ tonks_wardrobe_unlocked = False
        $ chitchated_with_tonks = False
        $ tonks_strip_happened = False #Tonks random clothing event.

        #Names
        $ tonks_name = "Tonks"
        $ ton_genie_name = "Professor"
        $ ton_astoria_name = "Cutie"

        #Stat Screen
        $ ton_clothing_upgrades = 0
        $ ton_astoria_date_counter = 0
        $ ton_hermione_date_counter = 0

    if not hasattr(renpy.store,'gave_tonks_gift') or reset_persistants:
        $ gave_tonks_gift    = False

    return
