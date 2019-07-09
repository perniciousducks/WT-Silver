

label astoria_init:

    if not hasattr(renpy.store,'astoria_wear_outfit') or reset_persistants:
        label reset_astoria_clothing:

        #Body
        $ astoria_base                = "characters/astoria/body/base/base_01.png"
        $ astoria_l_arm               = "characters/astoria/body/arms/hip_l.png"
        $ astoria_r_arm               = "characters/astoria/body/arms/hip_r.png"
        $ astoria_l_hand              = "characters/astoria/body/arms/hip_l_top.png"
        $ astoria_r_hand              = "characters/astoria/body/arms/hip_r_top.png"
        $ astoria_xpos                = 300
        $ astoria_ypos                = 0
        $ astoria_zorder              = 5
        $ astoria_flip                = 1
        $ use_astoria_head            = False

        #Face
        $ astoria_mouth               = "characters/astoria/face/mouth/smile.png"
        $ ast_mouth                   = "base"
        $ ast_lipstick                = "nude"

        $ astoria_eye                 = "characters/astoria/face/eyes/eye_base.png"
        $ astoria_eye_bg              = "characters/astoria/face/eyes/eye_base_bg.png"
        $ astoria_pupil               = "characters/astoria/face/eyes/pupil_mid.png"
        $ ast_eye_color               = "blue"

        $ astoria_eyebrow             = "characters/astoria/face/brow/base.png"

        $ astoria_cheeks              = "characters/astoria/face/extras/cheeks_blank.png"
        $ astoria_tears               = "characters/astoria/face/extras/cheeks_blank.png"
        $ astoria_extra               = "characters/astoria/face/extras/blank.png"
        $ astoria_emote               = "characters/emotes/blank.png"

        #Hair
        $ astoria_hair                = "characters/astoria/body/hair/straight_blonde_base.png"
        $ astoria_hair_shadow         = "characters/astoria/body/hair/straight_blonde_top.png"
        $ ast_hair_style              = "straight"
        $ ast_hair_color              = "blonde"

        $ changeAstoria("smile","base","base","mid","blank","blank","blank","blank")



        #Clothes

        #Save State
        $ ast_request_wear_top              = True
        $ ast_request_wear_bra              = True
        $ ast_request_wear_bottom           = True
        $ ast_request_wear_panties          = True

        $ ast_request_wear_onepiece         = False
        $ ast_request_wear_garterbelt       = False

        $ ast_request_wear_neckwear         = False
        $ ast_request_wear_gloves           = False
        $ ast_request_wear_stockings        = False
        $ ast_request_wear_robe             = False

        $ ast_request_wear_hat              = False
        $ ast_request_wear_glasses          = False
        $ ast_request_wear_ears             = False
        $ ast_request_wear_makeup           = False
        $ ast_request_wear_accs             = False

        $ ast_request_wear_buttplug         = False
        $ ast_request_wear_piercings        = False
        $ ast_request_wear_tattoos          = False

        $ ast_request_wear_outfit           = False

        #Toggle
        $ astoria_wear_top               = True
        $ astoria_wear_bra               = True
        $ astoria_wear_bottom            = True
        $ astoria_wear_panties           = True

        $ astoria_wear_onepiece          = False
        $ astoria_wear_garterbelt        = False

        $ astoria_wear_neckwear          = False
        $ astoria_wear_gloves            = False
        $ astoria_wear_stockings         = False
        $ astoria_wear_robe              = False

        $ astoria_wear_hat               = False
        $ astoria_wear_glasses           = False
        $ astoria_wear_ears              = False
        $ astoria_wear_makeup            = False
        $ astoria_wear_accs              = False
        $ astoria_badges                 = False
        $ astoria_wear_piercings         = False
        $ astoria_wear_tattoos           = False

        $ astoria_wear_outfit            = False



        #Top
        $ astoria_top                 = "characters/astoria/clothes/tops/top_1.png"
        $ ast_top                     = "top_1"
        $ ast_top_color               = "base"

        #Bottom
        $ astoria_bottom               = "characters/astoria/clothes/bottoms/skirt_1.png"
        $ ast_bottom                   = "skirt_1"
        $ ast_bottom_color             = "base"

        #Underwear
        $ astoria_bra                 = "characters/astoria/clothes/bras/lace_bra.png"
        $ ast_bra                     = "lace_bra"
        $ ast_bra_color               = "base"

        $ astoria_panties             = "characters/astoria/clothes/panties/lace_panties.png"
        $ ast_panties                 = "lace_panties"
        $ ast_panties_color           = "base"

        $ astoria_onepiece            = "characters/astoria/clothes/onepieces/blank.png"
        $ ast_onepiece                = "blank"
        $ ast_onepiece_color          = "base"

        $ astoria_garterbelt          = "characters/astoria/clothes/garterbelts/blank.png"
        $ ast_garterbelt              = "blank"
        $ ast_garterbelt_color        = "base"


        #Other Clothing
        $ astoria_neckwear            = "characters/astoria/clothes/neckwear/blank.png"
        $ ast_neckwear                = "blank"
        $ ast_neckwear_color          = "base"

        $ astoria_accs_list           = []

        $ astoria_gloves              = "characters/astoria/clothes/gloves/blank.png"
        $ ast_gloves                  = "blank"
        $ ast_gloves_color            = "base"

        $ astoria_stockings           = "characters/astoria/clothes/stockings/blank.png"
        $ ast_stockings               = "blank"
        $ ast_stockings_color         = "base"

        $ astoria_robe                = "characters/astoria/clothes/robe/robe_1_s.png"
        $ ast_robe                    = "robe_1_s"
        $ ast_robe_color              = "base"


        #Accessories
        $ astoria_makeup_list         = []

        $ astoria_hat                 = "characters/astoria/clothes/hats/hair_straight/blank.png"
        $ ast_hat                     = "blank"
        $ ast_hat_color               = "base"

        $ astoria_glasses             = "characters/astoria/clothes/glasses/blank.png"
        $ ast_glasses                 = "blank"
        $ ast_glasses_color           = "base"

        $ astoria_ears                = "characters/astoria/clothes/ears/blank.png"
        $ ast_ears                    = "blank"


        $ astoria_extra_1             = "characters/astoria/extras/blank.png"
        $ astoria_extra_2             = "characters/astoria/extras/blank.png"
        $ astoria_extra_3             = "characters/astoria/extras/blank.png"

        #Outfits
        $ astoria_outfit_GLBL = None
        $ astoria_temp_outfit = None


    call astoria_face_layers

    return


label astoria_progress_init:

    if not hasattr(renpy.store,'astoria_name') or reset_persistants:

        #Flags
        $ astoria_busy = False
        $ astoria_unlocked = False
        $ astoria_wardrobe_unlocked = False
        $ chitchated_with_astoria = False

        #Names
        $ astoria_name = "Miss Greengrass"
        $ ast_genie_name = "Dumby"
        $ ast_susan_name = "Cow"
        $ ast_tonks_name = "Old Hag"

        #Stats
        $ ast_spell_progress = 0 #Training times required to unlock a spell. Resets to 0 after it.
        $ ast_affection      = 0 #Affection level with Tonks.
        $ ast_mood           = 0

        #Events
        $ hermione_on_the_lookout  = False
        $ hermione_finds_astoria   = False
        $ snape_on_the_lookout     = False
        $ tonks_intro_happened     = False
        $ spells_unlocked          = False
        $ snape_gave_spellbook     = False
        $ third_curse_got_cast     = False
        $ astoria_book_intro_happened = False
        $ astoria_intro_completed  = False

        #Tonks events
        $ spells_locked = False
        $ astoria_tonks_event_in_progress = False
        $ astoria_tonks_intro_completed = False
        $ astoria_tonks_1_completed = False
        $ astoria_tonks_2_completed = False
        $ astoria_tonks_3_completed = False
        $ astoria_tonks_4_completed = False
        $ astoria_tonks_5_completed = False
        $ astoria_tonks_6_completed = False

        #Stat Screen
        $ ast_training_counter = 0

    if not hasattr(renpy.store,'gave_astoria_gift') or reset_persistants:
        $ gave_astoria_gift = False



    #Curses on Susan
    if not hasattr(renpy.store,'ag_cs_imperio_sb'):
        $ ag_cs_imperio_sb = favor_class()
    $ ag_cs_imperio_sb.title   = "Imperio on Susan"
    $ ag_cs_imperio_sb.start_label = "ag_cs_imperio_sb"

    $ ag_susan_spells_list = [
        ag_cs_imperio_sb
        ]

    #Curses on Hermione
    if not hasattr(renpy.store,'ag_cs_imperio_hg'):
        $ ag_cs_imperio_hg = favor_class()
    $ ag_cs_imperio_hg.title   = "Imperio on Hermione"
    $ ag_cs_imperio_hg.start_label = "ag_cs_imperio_hg"

    $ ag_hermione_spells_list = [
        ]

    #Curses on Tonks
    if not hasattr(renpy.store,'ag_cs_crucio_nt'):
        $ ag_cs_crucio_nt = favor_class()
    $ ag_cs_crucio_nt.title   = "Crucio on Tonks"
    $ ag_cs_crucio_nt.start_label = "ag_cs_crucio_nt"

    $ ag_tonks_spells_list = [
        ]

    return
