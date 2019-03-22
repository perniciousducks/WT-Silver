

label cho_init:

    if not hasattr(renpy.store,'cho_body_accs_list') or reset_persistants:
        label reset_cho_clothing:

        #Body
        $ cho_base                = "characters/cho/body/base/base_01.png"
        $ cho_l_arm               = "characters/cho/body/arms/arm_down_l.png"
        $ cho_r_arm               = "characters/cho/body/arms/arm_down_r.png"
        $ cho_l_hand              = "characters/cho/body/arms/arm_down_l_overlay.png"
        $ cho_breasts             = "characters/cho/body/breasts/breasts_bikini_tan.png"
        $ cho_breasts_tan         = "characters/cho/body/breasts/breasts_sport_bra_tan.png"
        $ cho_hips_tan            = "characters/cho/body/hips/hips_sport_bra_tan.png"

        $ cho_xpos                = 300
        $ cho_ypos                = 0
        $ cho_zorder              = 5
        $ cho_flip                = 1
        $ use_cho_head            = False

        #Face
        $ cho_mouth               = "characters/cho/face/mouth/base.png"
        $ cho_eye                 = "characters/cho/face/eyes/base.png"
        $ cho_eye_bg              = "characters/cho/face/eyes/_white_.png"
        $ cho_eyebrow             = "characters/cho/face/brow/base.png"
        $ cho_pupil               = "characters/cho/face/pupil/mid.png"

        $ cho_cheeks              = "characters/cho/face/extra/cheeks_blank.png"
        $ cho_tears               = "characters/cho/face/extra/tears_blank.png"
        $ cho_extra               = "characters/cho/face/extra/blank.png"
        $ cho_emote               = "characters/emotes/blank.png"

        $ changeCho("base","base","base","mid","blank","blank","blank","blank")

        #Chibi
        $ cho_chibi_xpos          = 500
        $ cho_chibi_ypos          = 250
        $ cho_chibi_xpos_name     = "base" #Memory of chibi position.
        $ cho_chibi_ypos_name     = "base" #Memory of chibi position.
        $ cho_chibi_flip          = 1
        $ cho_chibi_zorder        = 3

        $ cho_chibi_stand         = "ch_cho blink"
        $ cho_chibi_shoes         = "characters/cho/chibis/cc_walk_01_shoes.png"

        $ cho_chibi_walk          = "ch_cho walk"
        $ cho_chibi_walk_shoes    = "ch_cho walk_shoes"

        $ cho_chibi_top           = "characters/cho/chibis/cc_cloth_shirt_r.png"
        $ cho_chibi_bottom        = "characters/cho/chibis/cc_cloth_skirt.png"
        $ cho_chibi_robe          = "characters/cho/chibis/blank.png"

        #Hair
        $ cho_hair                = "characters/cho/body/hair/ponytail_blue_base.png"
        $ cho_hair_shadow         = "characters/cho/body/hair/ponytail_blue_top.png"
        $ c_hair_style            = "ponytail"
        $ c_hair_color            = "blue"



        #Save State
        $ cho_request_wear_top              = True
        $ cho_request_wear_bra              = True
        $ cho_request_wear_bottom           = True
        $ cho_request_wear_panties          = True

        $ cho_request_wear_onepiece         = False
        $ cho_request_wear_garterbelt       = False

        $ cho_request_wear_neckwear         = False
        $ cho_request_wear_body_accs        = False
        $ cho_request_wear_gloves           = False
        $ cho_request_wear_stockings        = False
        $ cho_request_wear_robe             = False

        $ cho_request_wear_hat              = True
        $ cho_request_wear_glasses          = False
        $ cho_request_wear_ears             = False
        $ cho_request_wear_makeup           = False
        $ cho_request_wear_accs             = False

        $ cho_request_wear_buttplug         = False
        $ cho_request_wear_piercings        = False
        $ cho_request_wear_tattoos          = False
        $ cho_request_wear_mask             = False
        $ cho_request_wear_gag              = False

        $ cho_request_wear_outfit           = False

        #Toggle
        $ cho_wear_top               = True
        $ cho_wear_bra               = True
        $ cho_wear_bottom            = True
        $ cho_wear_panties           = True

        $ cho_wear_onepiece          = False
        $ cho_wear_garterbelt        = False

        $ cho_wear_neckwear          = False
        $ cho_wear_body_accs         = False
        $ cho_wear_gloves            = False
        $ cho_wear_stockings         = False
        $ cho_wear_robe              = False

        $ cho_wear_hat               = True
        $ cho_wear_glasses           = False
        $ cho_wear_ears              = False
        $ cho_wear_makeup            = False
        $ cho_wear_accs              = False

        $ cho_wear_buttplug          = False
        $ cho_wear_piercings         = False
        $ cho_wear_tattoos           = False
        $ cho_wear_mask              = False
        $ cho_wear_gag               = False

        $ cho_wear_outfit            = False



        #Clothes
        $ cho_top                 = "characters/cho/clothes/tops/base/top_1.png"
        $ c_top                   = "top_1"
        $ c_top_color             = "base"

        $ cho_bra                 = "characters/cho/clothes/underwear/base/bra_sport.png"
        $ c_bra                   = "bra_sport"
        $ c_bra_color             = "base"

        $ cho_bottom              = "characters/cho/clothes/bottoms/base/skirt_2.png"
        $ c_bottom                = "skirt_2"
        $ c_bottom_color          = "base"

        $ cho_panties             = "characters/cho/clothes/underwear/base/panties_sport_1.png"
        $ c_panties               = "panties_sport_1"
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

        $ cho_stockings           = "characters/cho/clothes/stockings/base/stockings.png"
        $ c_stockings             = "blank"
        $ c_stockings_color       = "base"

        $ cho_robe                = "characters/cho/clothes/robe/quidditch.png"
        $ c_robe                  = "blank"
        $ c_robe_color            = "base"

        #Accessories
        $ cho_hat                 = "characters/cho/clothes/hats/hair_ponytail/snitch.png"
        $ c_hat                   = "snitch"
        $ c_hat_color             = "base"

        $ cho_glasses             = "characters/cho/clothes/glasses/blank.png"
        $ c_glasses               = "blank"
        $ c_glasses_color         = "base"

        $ cho_ears                = "characters/cho/clothes/ears/blank.png"
        $ c_ears                  = "blank"

        $ cho_body_accs_list      = []

        #Miscellaneous
        $ cho_buttplug            = "characters/cho/clothes/plugs/blank.png"
        $ c_buttplug                = "blank"
        $ cho_gag                 = "characters/cho/face/mouth/gag.png"
        $ c_gag                     = "gag"

        #Piercings
        $ cho_ear_piercing        = "characters/cho/clothes/piercings/blank.png"
        $ c_ear_piercing            = "blank"
        $ c_ear_piercing_color      = "base"

        $ cho_tongue_piercing     = "characters/cho/clothes/piercings/blank.png"
        $ c_tongue_piercing         = "blank"
        $ c_tongue_piercing_color   = "base"

        $ cho_nipple_piercing     = "characters/cho/clothes/piercings/blank.png"
        $ c_nipple_piercing         = "blank"
        $ c_nipple_piercing_color   = "base"

        $ cho_belly_piercing      = "characters/cho/clothes/piercings/blank.png"
        $ c_belly_piercing          = "blank"
        $ c_belly_piercing_color    = "base"

        $ cho_genital_piercing    = "characters/cho/clothes/piercings/blank.png"
        $ c_genital_piercing        = "blank"
        $ c_genital_piercing_color  = "base"

        call reset_cho_transparency

        #Outfits
        $ cho_outfit_GLBL = None
        $ cho_temp_outfit = None


    call cho_face_layers

    return

label reset_cho_transparency:
    $ cho_top_transp       = 1
    $ cho_bottom_transp    = 1

    $ cho_bra_transp       = 1
    $ cho_onepiece_transp  = 1
    $ cho_panties_transp   = 1
    $ cho_garter_transp    = 1

    $ cho_gloves_transp    = 1
    $ cho_stockings_transp = 1
    $ cho_robe_transp      = 1

    $ cho_outfit_transp    = 1

    return


label cho_progress_init:
    if not hasattr(renpy.store,'main_match_1_seen') or reset_persistants or reset_cho_content:
        $ main_match_1_seen = False
    if not hasattr(renpy.store,'cho_whoring') or reset_persistants or reset_cho_content:

        # Stats
        $ cho_whoring = 0
        $ cho_mood = 0
        $ cho_jerk_off_counter = 0

        # Flags
        $ cho_busy = False
        $ cho_wardrobe_unlocked = False

        # Intro
        $ cho_known               = False
        $ cho_intro_1_complete    = False
        $ cho_intro_2_complete    = False
        $ cho_snape_talk_complete = False
        $ cho_unlocked            = False

        # Quidditch Training
        $ cho_training_unlocked   = False
        $ cho_training_intro_complete = False
        $ lock_cho_training       = False
        $ lock_cho_practice       = False
        $ quidditch_commentator   = "None"
        $ quidditch_position      = "front"

        # Quidditch Outfit
        $ cho_quidditch_top    = "sweater" # For testing.
        $ cho_quidditch_bottom = "pants_long" # For testing.
        $ quid_pants_1_intro = False
        $ quid_pants_2_intro = False
        $ quid_skirt_1_intro = False
        $ quid_skirt_2_intro = False
        $ cho_quidditch_coat   = True # For testing.
        $ cho_quidditch_gloves = True # For testing.

        # Quidditch Matches
        $ quidditch_match_in_progress = False
        $ huffl_match_counter   = 0
        $ gryff_match_counter   = 0
        $ slyth_match_counter   = 0

        $ huffl_matches_won     = 0 # Goes up to 2
        $ gryff_matches_won     = 0 # Goes up to 2
        $ slyth_matches_won     = 0 # Goes up to 2

        $ start_match           = 0 # No match will trigger at 0
        $ main_matches_won      = 0 # Goes up to 3
        $ main_match_1_seen = False
        $ main_match_2_seen = False
        $ main_match_3_seen = False

        $ cho_content_complete = False

        # Names
        $ cho_genie_name = "Sir"
        $ cho_name = "Cho"

        #Quidditch

        $ first_cho_favor_done = False
        $ gave_cho_gift      = False


    ### Cho Favours ###

    # cc = Cho Chang.
    # pf = Personal Favour.
    # A1 = A is the tier at which the favour gets unlocked, 1 is the position in the menu/list.

    if not hasattr(renpy.store,'cc_pf_A1_Talking_OBJ'):
        $ cc_pf_A1_Talking_OBJ = favor_class(title = "Talk to me",       tier = 0, start_label = "cc_pf_A1_Talking")

        $ cc_pf_B1_Groping_OBJ = favor_class(title = "Molest her body!", tier = 1, start_label = "cc_pf_B1_Groping")

        $ cc_pf_C1_Blowjob_OBJ = favor_class(title = "Suck it!",         tier = 2, start_label = "cc_pf_C1_Blowjob")

        $ cc_pf_D1_Sex_OBJ     = favor_class(title = "Let's have sex!",  tier = 3, start_label = "cc_pf_D1_Sex")

    $ cc_favor_list = [
        cc_pf_A1_Talking_OBJ,
        cc_pf_B1_Groping_OBJ,
        cc_pf_C1_Blowjob_OBJ,
        cc_pf_D1_Sex_OBJ,
        ]

    return
