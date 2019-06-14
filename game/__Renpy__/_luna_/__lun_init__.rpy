

label luna_init:

    if not hasattr(renpy.store,'luna_breasts') or reset_persistants or reset_luna_content:
        label reset_luna_base:

        #Body
        $ luna_base              = "characters/luna/body/base/base_01.png"
        $ luna_breasts           = "characters/luna/body/breasts/breasts_normal.png"
        $ luna_l_arm             = 1
        $ luna_r_arm             = 1
        $ luna_xpos              = 640
        $ luna_ypos              = 0
        $ luna_zorder            = 5
        $ luna_flip              = 1
        $ use_luna_head          = False

        #Hair
        $ luna_hair              = "characters/luna/body/hair/playful_blonde_base.png"
        $ luna_hair_shadow       = "characters/luna/body/hair/playful_blonde_top.png"
        $ lun_hair_style         = "playful"
        $ lun_hair_color         = "blonde"

        #Face
        $ luna_mouth             = "characters/luna/face/mouth/base.png"
        $ luna_eye               = "characters/luna/face/eyes/base.png"
        $ luna_eyebrow           = "characters/luna/face/brow/base.png"
        $ luna_pupil             = "characters/luna/face/pupil/blue/mid.png"
        $ luna_pupil_color       = "blue"

        $ luna_cheeks            = "characters/luna/face/extras/cheeks_blank.png"
        $ luna_tears             = "characters/luna/face/extras/tears_blank.png"
        $ luna_extra             = "characters/luna/face/extras/blank.png"
        $ luna_emote             = "characters/emotes/blank.png"

        #$ changeCho("base","base","base","mid","blank","blank","blank","blank")

        #Cum
        $ luna_cum               = 1
        $ luna_wear_cum          = False
        $ luna_wear_cum_under    = False

        #Chibi
        $ luna_chibi_image       = "characters/luna/chibis/luna_stand.png"
        $ luna_chibi_stand       = "characters/luna/chibis/luna_stand.png"
        $ luna_chibi_blink       = "ch_lun blink_a"
        $ luna_chibi_blink_f     = "ch_lun blink_a_flip"
        $ luna_chibi_walk        = "ch_lun walk_a"
        $ luna_chibi_walk_f      = "ch_lun walk_a_flip"

        $ luna_chibi_xpos        = 500
        $ luna_chibi_ypos        = 250
        $ luna_chibi_xpos_name   = "base" #Memory of chibi position.
        $ luna_chibi_ypos_name   = "base" #Memory of chibi position.
        $ luna_chibi_zorder      = 3

        #CG
        $ hermione_kneel_leg     = False
        $ hermione_kneel_cock    = False


    if not hasattr(renpy.store,'lun_request_wear_top') or reset_persistants or reset_luna_content:
        label reset_luna_clothing:

        #Save State
        $ lun_request_wear_top              = True
        $ lun_request_wear_bra              = True
        $ lun_request_wear_bottom           = True
        $ lun_request_wear_panties          = True

        $ lun_request_wear_onepiece         = False
        $ lun_request_wear_garterbelt       = False

        $ lun_request_wear_neckwear         = False
        $ lun_request_wear_gloves           = False
        $ lun_request_wear_stockings        = False
        $ lun_request_wear_robe             = False

        $ lun_request_wear_hat              = False
        $ lun_request_wear_glasses          = False
        $ lun_request_wear_ears             = False
        $ lun_request_wear_makeup           = False
        $ lun_request_wear_accs             = False

        $ lun_request_wear_buttplug         = False
        $ lun_request_wear_piercings        = False
        $ lun_request_wear_tattoos          = False

        $ lun_request_wear_outfit           = False

        #Toggle
        $ luna_wear_top               = True
        $ luna_wear_bra               = True
        $ luna_wear_bottom            = True
        $ luna_wear_panties           = True

        $ luna_wear_onepiece          = False
        $ luna_wear_garterbelt        = False

        $ luna_wear_neckwear          = False
        $ luna_wear_gloves            = False
        $ luna_wear_stockings         = False
        $ luna_wear_robe              = False

        $ luna_wear_hat               = False
        $ luna_wear_glasses           = False
        $ luna_wear_ears              = False
        $ luna_wear_makeup            = False
        $ luna_wear_accs              = False
        $ luna_badges                 = False
        $ luna_wear_piercings         = False
        $ luna_wear_tattoos           = False

        $ luna_wear_outfit            = False



        #Top
        $ luna_top                 = "characters/luna/clothes/tops/top_1_r.png"
        $ lun_top                     = "top_1_r"
        $ lun_top_color               = "base"

        #Bottom
        $ luna_bottom              = "characters/luna/clothes/bottoms/skirt_1.png"
        $ lun_bottom                  = "skirt_1"
        $ lun_bottom_color            = "base"

        #Underwear
        $ luna_bra                 = "characters/luna/clothes/bras/bra_basic.png"
        $ lun_bra                     = "bra_basic"
        $ lun_bra_color               = "base"

        $ luna_panties             = "characters/luna/clothes/panties/panties_basic.png"
        $ lun_panties                 = "panties_basic"
        $ lun_panties_color           = "base"

        $ luna_onepiece            = "characters/luna/clothes/onepieces/blank.png"
        $ lun_onepiece                = "blank"
        $ lun_onepiece_color          = "base"

        $ luna_garterbelt          = "characters/luna/clothes/garterbelts/blank.png"
        $ lun_garterbelt              = "blank"
        $ lun_garterbelt_color        = "base"


        #Other Clothing
        $ luna_neckwear            = "characters/luna/clothes/neckwear/blank.png"
        $ lun_neckwear                = "blank"
        $ lun_neckwear_color          = "base"

        $ luna_accs_list           = []

        $ luna_gloves              = "characters/luna/clothes/gloves/blank.png"
        $ lun_gloves                  = "blank"
        $ lun_gloves_color            = "base"

        $ luna_stockings           = "characters/luna/clothes/stockings/blank.png"
        $ lun_stockings               = "blank"
        $ lun_stockings_color         = "base"

        $ luna_robe                = "characters/luna/clothes/robe/blank.png"
        $ lun_robe                    = "blank"
        $ lun_robe_color              = "base"


        #Accessories
        $ luna_makeup_list         = []

        $ luna_hat                 = "characters/luna/clothes/hats/hair_playful/blank.png"
        $ lun_hat                     = "blank"
        $ lun_hat_color               = "base"

        $ luna_glasses             = "characters/luna/clothes/glasses/blank.png"
        $ lun_glasses                 = "blank"
        $ lun_glasses_color           = "base"

        $ luna_ears                = "characters/luna/clothes/ears/blank.png"
        $ lun_ears                    = "blank"

        #Outfits
        $ luna_outfit_GLBL = None
        $ luna_temp_outfit = None

        call reset_lun_transparency

    if not hasattr(renpy.store,'lun_cg_path') or reset_persistants or reset_luna_content:
        $ lun_cg_path       = "images/CG/luna_desk2/"
        $ lun_cg_overlay    = lun_cg_path+"blank.png"
        $ lun_cg_base       = lun_cg_path+"base.png"
        $ lun_cg_border     = lun_cg_path+"border.png"
        $ lun_cg_body       = lun_cg_path+"luna_base.png"
        $ lun_cg_hair       = lun_cg_path+str(lun_hair_style)+"_hair.png"
        $ lun_cg_cheeks     = lun_cg_path+"c_base.png"
        $ lun_cg_mouth      = lun_cg_path+"m_base.png"
        $ lun_cg_eyewhite   = lun_cg_path+"eye_white.png"
        $ lun_cg_pupil      = lun_cg_path+"pup_base.png"
        $ lun_cg_eye        = lun_cg_path+"eye_base.png"
        $ lun_cg_eyebrow    = lun_cg_path+"eb_base.png"
        $ lun_cg_eyewear    = lun_cg_path+"glasses.png"
        $ lun_cg_tears      = lun_cg_path+"blank.png"
        $ lun_cg_hairtop    = lun_cg_path+str(lun_hair_style)+"_hair_top.png"
        $ lun_cg_extra_1    = lun_cg_path+"blank.png"
        $ lun_cg_extra_2    = lun_cg_path+"blank.png"
        $ lun_cg_extra_3    = lun_cg_path+"blank.png"
        $ lun_cg_dick       = lun_cg_path+"dick_1.png"
        $ lun_cg_genie      = lun_cg_path+"genie.png"
        $ lun_cg_xpos       = 0
        $ lun_cg_ypos       = 0
        $ lun_cg_xpos_abs   = 0
        $ lun_cg_ypos_abs   = 0
        $ lun_loop_xpos     = [-150, 0, 55, 66, 74, 80, 88, 99, 103, 114, 121, 129, 134, 141, 148, 152, 155]
        $ lun_loop_ypos     = [0, 0, 12, 20, 31, 40, 48, 59, 71, 76, 83, 90, 97, 103, 107, 111, 112]
        $ lun_cg_zoom       = 1

    if not hasattr(renpy.store,'seen_luna_sex_list') or reset_persistants or reset_luna_content:
        $ seen_luna_sex_list       = []

    if not hasattr(renpy.store,'ll_pf_masturbate') or reset_persistants or reset_luna_content:
        $ ll_pf_masturbate = event_class(title = "Masturbate for me!", start_label = "ll_pf_masturbate", start_tier = 2, events = [
            [
            ["ll_pf_masturbate_T1_intro"],
            ["ll_pf_masturbate_T1_intro_E1"],
            ["ll_pf_masturbate_T1_intro_E2"],
            ["ll_pf_masturbate_T1_E3"]
            ]

            ],
            iconset = [["heart_empty", "heart_blue"]]
            )

    if not hasattr(renpy.store,'ll_pf_blowjob') or reset_persistants or reset_luna_content:
        $ ll_pf_blowjob = event_class(title = "Suck it!", start_label = "ll_pf_blowjob", start_tier = 3, events = [
            [
            ["ll_pf_blowjob_T1_intro"],
            ["ll_pf_blowjob_T1_intro_E1"],
            ["ll_pf_blowjob_T1_intro_E2"],
            ["ll_pf_blowjob_T1_E3"]
            ]

            ],
            iconset = [["heart_empty", "heart_blue"]]
            )

    if not hasattr(renpy.store,'ll_pf_sex') or reset_persistants or reset_luna_content:
        $ ll_pf_sex = event_class(title = "Let's have sex!", start_label = "ll_pf_sex", start_tier = 4, events = [
            [
            ["ll_pf_sex_T1_intro"],
            ["ll_pf_sex_T1_E1"],
            ["ll_pf_sex_T1_E2"],
            ["ll_pf_sex_T1_E3"]
            ]

            ],
            iconset = [["heart_empty", "heart_blue"]]
            )

    # $ ll_pf_talk       = favor_class(title = "Talk to me!", tier = 0, start_label = "ll_pf_talk")
    # $ ll_pf_strip      = favor_class(title = "Inspect her body!", tier = 1, start_label = "ll_pf_strip")

    # Favors get added to the list after their intro events.
    # Do not add them manually to this list!

    if not hasattr(renpy.store,'ll_favor_list') or reset_persistants or reset_luna_content:
        $ ll_favor_list = [
            ]



    # Luna Lists
    $ luna_arms_up_list  = ["top_cheer_r",
                            "ll_pyjama",
                            ]

    call luna_face_layers


    return

label reset_lun_transparency:

    $ lun_top_transp       = 1
    $ lun_bottom_transp    = 1

    $ lun_bra_transp       = 1
    $ lun_onepiece_transp  = 1
    $ lun_panties_transp   = 1
    $ lun_garter_transp    = 1

    $ lun_gloves_transp    = 1
    $ lun_stockings_transp = 1
    $ lun_robe_transp      = 1

    $ lun_outfit_transp    = 1

    return



label luna_progress_init:

    # Update 1.3
    if not hasattr(renpy.store,'luna_known') or reset_persistants or reset_luna_content:

        #Stats
        $ lun_whoring = 0
        $ lun_tier = 1
        $ lun_mood = 0

        $ luna_gold = 0
        $ lun_skirt_level = 1
        $ lun_top_level = 1

        $ lun_dom = 0
        $ lun_sub = 0

        #Flags
        $ hat_known = False
        $ luna_known = False
        $ luna_busy = False
        $ luna_unlocked = False
        $ luna_wardrobe_unlocked = False

        $ luna_herm_talk = False
        $ luna_reverted = False
        $ luna_addicted = False

        #Names
        $ lun_genie_name = "Professor"
        $ lun_name = "Miss Lovegood"

    if not hasattr(renpy.store,'gave_luna_gift') or reset_persistants:
        $ gave_luna_gift     = False

    return
