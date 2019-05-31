

### HERMIONE INITS ###

label her_init:

    if not hasattr(renpy.store,'hermione_base') or reset_persistants:
        label reset_hermione_base:

        #Body
        $ hermione_base             = "characters/hermione/body/base/hermione_base.png"

        #Face
        $ hermione_mouth            = "characters/hermione/face/mouth/nude/base.png"
        $ h_lipstick                = "nude"

        $ hermione_eyes             = "characters/hermione/face/eyes/brown/base.png"
        $ hermione_eyebrows         = "characters/hermione/face/brows/brown/base.png"
        $ h_eye_color               = "brown"
        $ h_eye_shadow              = "blank"

        $ hermione_cheeks           = "characters/hermione/face/extras/cheeks_blank.png"
        $ hermione_tears            = "characters/hermione/face/extras/tears_blank.png"
        $ hermione_extra            = "characters/hermione/face/extras/blank.png"
        $ hermione_emote            = "characters/emotes/blank.png"

        #Positioning
        $ hermione_xpos             = 370
        $ hermione_ypos             = 0
        $ hermione_zorder           = 5
        $ hermione_flip             = 1
        $ use_hermione_head         = False

        $ changeHermione("base", "base", "blank", "blank", "blank", "blank")

        #Breasts
        $ hermione_breasts          = "characters/hermione/body/breasts/breasts_nipfix.png"
        $ h_breasts                 = "breasts_nipfix"

        $ hermione_perm_expand_breasts   = False
        $ hermione_perm_expand_ass       = False

        $ hermione_expand_breasts           = False #Temporary Expand
        $ hermione_expand_breasts_counter   = 0
        $ hermione_expand_ass               = False #Temporary Expand
        $ hermione_expand_ass_counter       = 0


        #Arms
        $ hermione_right_arm        = "characters/hermione/body/arms/right/right_1.png"
        $ h_right_arm               = "right_1"

        $ hermione_left_arm         = "characters/hermione/body/arms/left/left_1.png"
        $ h_left_arm                = "left_1"

        #Legs
        $ hermione_legs             = "characters/hermione/body/legs/legs_1.png"

        #Hair
        $ hermione_hair_base           = "characters/hermione/body/head/curly_brown.png"
        $ hermione_hair_top           = "characters/hermione/body/head/curly_brown_top.png"
        $ h_hair_style              = "curly"
        $ h_hair_color              = "brown"
        $ h_can_color               = ["curly","updo","bobcut"]


        #Actions/Posing
        $ hermione_action        = "none"
        $ hermione_use_action    = False

        $ h_action_top           = ""
        $ h_action_bottom        = ""

        $ hermione_action_a         = "blank.png"
        $ hermione_action_b         = "blank.png"
        $ h_action_a                = "blank.png"
        $ hermione_costume_action_a = "characters/hermione/clothes/custom/blank.png"

        $ u_sperm = "characters/hermione/face/auto_02.png"
        $ hermione_sperm = "characters/hermione/face/auto_02.png" #Not in use yet.



        # Chibi.
        $ her_chibi_stand       = "ch_hem blink_a"
        $ her_chibi_walk        = "ch_hem walk_a"

        $ u_h_animation              = ""
        $ u_h_animation_paused       = ""
        $ u_h_ani_xpos               = 0
        $ u_h_ani_ypos               = 0

        $ her_chibi_xpos        = 540
        $ her_chibi_ypos        = 250
        $ her_chibi_zorder      = 3
        $ her_chibi_flip        = 1




    if not hasattr(renpy.store,'h_request_wear_top') or reset_persistants:
        label reset_hermione_clothing:

        #Save State
        $ h_request_wear_top              = True
        $ h_request_wear_bra              = True
        $ h_request_wear_bottom           = True
        $ h_request_wear_panties          = True

        $ h_request_wear_onepiece         = False
        $ h_request_wear_garterbelt       = False

        $ h_request_wear_neckwear         = False
        $ h_request_wear_gloves           = False
        $ h_request_wear_stockings        = False
        $ h_request_wear_robe             = False

        $ h_request_wear_hat              = False
        $ h_request_wear_glasses          = False
        $ h_request_wear_ears             = False
        $ h_request_wear_makeup           = False
        $ h_request_wear_body_accs        = False

        $ h_request_wear_buttplug         = False
        $ h_request_wear_piercings        = False
        $ h_request_wear_tattoos          = False
        $ h_request_wear_mask             = False
        $ h_request_wear_gag              = False

        $ h_request_wear_outfit           = False


        #Toggle
        $ hermione_wear_top               = True
        $ hermione_wear_bra               = True
        $ hermione_wear_bottom            = True
        $ hermione_wear_panties           = True

        $ hermione_wear_onepiece          = False
        $ hermione_wear_garterbelt        = False

        $ hermione_wear_neckwear          = False
        $ hermione_wear_gloves            = False
        $ hermione_wear_stockings         = False
        $ hermione_wear_robe              = False

        $ hermione_wear_hat               = False
        $ hermione_wear_glasses           = False
        $ hermione_wear_ears              = False
        $ hermione_wear_makeup            = False
        $ hermione_wear_body_accs         = False
        $ hermione_badges                 = False

        $ hermione_wear_buttplug          = False
        $ hermione_wear_piercings         = False
        $ hermione_wear_tattoos           = False
        $ hermione_wear_mask              = False
        $ hermione_wear_gag               = False

        $ hermione_wear_outfit            = False



        #Top
        $ hermione_top              = "characters/hermione/clothes/tops/top_1_g.png"
        $ h_top                     = "top_1_g"
        $ h_top_color               = "base"


        #Bottom
        $ hermione_bottom            = "characters/hermione/clothes/bottoms/skirt_1.png"
        $ h_bottom                   = "skirt_1"
        $ h_bottom_color             = "base"


        #Underwear
        $ hermione_bra              = "characters/hermione/clothes/bras/bra_base.png"
        $ h_bra                     = "bra_base"
        $ h_bra_color               = "base"

        $ hermione_panties          = "characters/hermione/clothes/panties/panties_base.png"
        $ h_panties                 = "panties_base"
        $ h_panties_color           = "base"

        $ hermione_onepiece         = "characters/hermione/clothes/onepieces/blank.png"
        $ h_onepiece                = "blank"
        $ h_onepiece_color          = "base"

        $ hermione_garterbelt       = "characters/hermione/clothes/garterbelts/blank.png"
        $ h_garterbelt              = "blank"
        $ h_garterbelt_color        = "base"


        #Other Clothing
        $ hermione_neckwear         = "characters/hermione/clothes/neckwear/blank.png"
        $ h_neckwear                = "blank"
        $ h_neckwear_color          = "base"

        $ hermione_body_accs_list   = []

        $ hermione_gloves           = "characters/hermione/clothes/gloves/blank.png"
        $ h_gloves                  = "blank"
        $ h_gloves_color            = "base"

        $ hermione_stockings        = "characters/hermione/clothes/stockings/blank.png"
        $ h_stockings               = "blank"
        $ h_stockings_color         = "base"
        $ temp_stockings            = h_stockings

        $ hermione_robe             = "characters/hermione/clothes/robe/robe_basic_g.png"
        $ h_robe                    = "robe_basic_g"
        $ h_robe_color              = "base"

        #Accessories
        $ hermione_makeup_list      = []

        $ hermione_hat              = "characters/hermione/clothes/hats/hair_curly/blank.png"
        $ h_hat                     = "blank"
        $ h_hat_color               = "base"

        $ hermione_glasses          = "characters/hermione/clothes/glasses/blank.png"
        $ h_glasses                 = "blank"
        $ h_glasses_color           = "base"

        $ hermione_ears             = "characters/hermione/clothes/ears/blank.png"
        $ h_ears                    = "blank"


        #Miscellaneous
        $ hermione_buttplug          = "characters/hermione/clothes/plugs/blank.png"
        $ h_buttplug                 = "blank"

        $ hermione_pubic_hair        = "characters/hermione/body/pubic_hair/blank.png"
        $ h_pubic_hair               = "blank"

        $ hermione_panties_overlay  = "characters/hermione/clothes/underwear/blank.png"
        $ hermione_ass_cum          = False
        $ hermione_squirt           = False
        $ hermione_futa             = False

        $ milk_level                = 0
        $ milking                   = 0


        #Piercings
        $ hermione_ear_piercing      = "characters/hermione/clothes/piercings/blank.png"
        $ h_ear_piercing             = "blank"
        $ h_ear_piercing_color       = "base"

        $ hermione_nipple_piercing   = "characters/hermione/clothes/piercings/blank.png"
        $ h_nipple_piercing          = "blank"
        $ h_nipple_piercing_color    = "base"

        $ hermione_belly_piercing    = "characters/hermione/clothes/piercings/blank.png"
        $ h_belly_piercing           = "blank"
        $ h_belly_piercing_color     = "base"

        $ hermione_genital_piercing  = "characters/hermione/clothes/piercings/blank.png"
        $ h_genital_piercing         = "blank"
        $ h_genital_piercing_color   = "base"

        #Tattoos
        $ hermione_tattoos_list      = []
        $ h_tattoos_color            = "base"

        $ hermione_mask              = "characters/hermione/clothes/hats/blank.png"
        $ h_mask                     = "blank"
        $ hermione_gag               = "characters/hermione/face/mouth/nude/gag.png"
        $ h_gag                      = "gag"

        call reset_her_transparency

        #Outfits
        $ hermoine_outfit_GLBL = None
        $ hermione_temp_outfit = None
        $ temp_outfit = None



    ### ADD MORE HERMIONE PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return

label reset_her_transparency:
    $ transparency         = 1

    $ her_top_transp       = 1
    $ her_bottom_transp    = 1

    $ her_bra_transp       = 1
    $ her_onepiece_transp  = 1
    $ her_panties_transp   = 1
    $ her_garter_transp    = 1

    $ her_gloves_transp    = 1
    $ her_stockings_transp = 1
    $ her_robe_transp      = 1

    $ her_outfit_transp    = 1

    return


label her_clothing_lists_init: #Lists update at every game start!

    #Tops
    $ h_top_nipfix_list             = ["onepiece_microdress",
                                       "top_fishnets_1",
                                       ]

    $ h_top_has_no_recolor_list     = ["top_jacket_2",
                                       "top_jacket_open_2",
                                       "top_jacket_3",
                                       "top_jacket_open_3",
                                       "top_jacket_1",
                                       "top_jacket_open_1",
                                       "top_rocker",
                                       "top_fishnets_1",
                                       ]

    $ h_top_remove_bra_list         = ["top_1_g", "top_1_s",
                                       "top_2_g", "top_2_s",
                                       "top_3_g", "top_3_s",
                                       "top_4_g", "top_4_s",
                                       "top_6_g", "top_6_s",
                                       "top_cheer_sexy_g",
                                       "top_cheer_sexy_s",
                                       "top_cheer_sexy_r",
                                       "top_cheer_sexy_h",
                                       "top_cheer_g",
                                       "top_cheer_s",
                                       "top_cheer_r",
                                       "top_cheer_h",
                                       "top_pullover_1",
                                       "top_sweater_1",
                                       ]

    $ h_lift_top_list               = ["top_1_g", "top_1_s",
                                       "top_2_g", "top_2_s",
                                       "top_3_g", "top_3_s",
                                       "top_4_g", "top_4_s",
                                       "top_6_g", "top_6_s",
                                       "top_pullover_1",
                                       "top_pullover_2",
                                       "top_fishnets_1",
                                       "top_rocker",
                                       ]


    #Bottoms
    $ h_skirts_list                 = ["skirt_1",
                                       "skirt_2",
                                       "skirt_3",
                                       "skirt_4",
                                       "skirt_5",
                                       "skirt_1_low",
                                       "skirt_2_low",
                                       "skirt_3_low",
                                       "skirt_4_low",
                                       "skirt_cheer_g",
                                       "skirt_cheer_s",
                                       "skirt_cheer_r",
                                       "skirt_cheer_h",
                                       "skirt_cheer_sexy_g",
                                       "skirt_cheer_sexy_s",
                                       "skirt_cheer_sexy_r",
                                       "skirt_cheer_sexy_h",
                                       ]

    $ h_pants_list                  = ["pants_jeans_long",
                                       "pants_jeans_short",
                                       "pants_retro_shorts",
                                       "pants_rocker",
                                       ]

    #One-pieces & Nighties
    $ h_onepieces_list              = ["onepiece_microdress",
                                       "onepiece_bunny",
                                       "swimsuit_neckband",
                                       "swimsuit_halterless",
                                       "onepiece_bikini_1",
                                       "swimsuit_sport_1",
                                       "swimsuit_sport_2",
                                       "swimsuit_sport_3",
                                       "swimsuit_sport_4",
                                       "onepiece_netsuit_fancy",
                                       "onepiece_netsuit",
                                      ]

    $ h_onepieces_nighties_list     = ["nighty_short",
                                       "nighty_long",
                                       "nighty_dress",
                                      ]

    #Bras                              #Bras that need the nipfix breast variant
    $ h_bra_nipfix_list             = ["bra_base"
                                      ]

                                       #Bras that need the pressed breast variant
    $ h_bra_pressed_list            = ["top_fishnets_1"
                                      ]

    #Piercings
    $ ear_piercings_list            = ["ears_hearts_large",
                                       "ears_hearts",
                                       "ears_pearls",
                                       "ears_straight",
                                       "ears_rings",
                                       "ears_gambler",
                                       "ears_feather",
                                      ]
    $ tongue_piercings_list         = ["tongue_pearls",
                                      ]
    $ nipple_piercings_list         = ["nipples_pearls",
                                      ]
    $ belly_piercings_list          = ["belly_pearls",
                                       "belly_gambler",
                                      ]
    $ genital_piercings_list        = [
                                      ]

    $ gryffindor_robe_list          = ["robe_1_g",
                                       "robe_2_g",
                                       "robe_3_g",
                                       "robe_4_g",
                                       "robe_basic_g",
                                       "robe_open_g",
                                       "robe_quidditch_g"
                                      ]

    $ slytherin_robe_list           = ["robe_1_s",
                                       "robe_2_s",
                                       "robe_3_s",
                                       "robe_4_s",
                                       "robe_basic_s",
                                       "robe_open_s",
                                       "robe_quidditch_s"
                                      ]

    call hermione_face_layers

    return



label her_progress_init:

    if not hasattr(renpy.store,'her_whoring') or reset_persistants:

        #Stats
        $ her_tier       = 1
        $ her_whoring    = 0
        $ her_reputation = 0
        $ her_tutoring   = 0

        $ her_mood       = 0
        $ forest_BJ_progress = 1

        #Flags
        $ hermione_busy           = False
        $ hermione_unlocked       = False
        $ hermione_favors         = False
        $ hermione_tutoring       = False
        $ her_panties_soaked      = False
        $ hermione_favors_convinced = 0

        #Names
        $ genie_name = "Sir"
        $ hermione_name = "Miss Granger"

        #Clothing Flags
        $ hermione_dribble = False
        $ dribble_equippable = False
        $ hermione_wetpanties = False
        $ wetpanties_equippable = False

        #Stat Screen
        $ her_jerk_off_counter = 0



        #Personal Requests
        $ hg_hidden_bj_seen_list = []

        #Public Request Vars.
        $ hg_pr_sex_skip = False

        $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. Turns FALSE after that.
        $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
        $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
        $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        #Public Shaming Flags
        $ her_panties_soaked = False
        $ current_job = 0
        $ transparent_quest = False


        ### HERMIONE EVENT VARS ###
        $ jerked_off_during_hermione_intro = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

        $ tutoring_offer_made = False #If you offered her to tutor her (In hermione_intro_E4). Affects conversation in the next event.

        $ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (hermione_intro_E2)
        $ hermione_is_waiting_02 = False #Turns True at the end of second special event with Snape. Triggers next visit from Hermione

        $ collar = 0

    #Buttplug Events
        $ buttplug_magic_known   = False
        $ buttplug_1_worn        = False
        $ buttplug_2_worn        = False
        $ buttplug_3_worn        = False
        $ buttplug_1_question    = False
        $ buttplug_2_question    = False
        $ buttplug_3_question    = False

    #Clothing Events
        $ hermione_door_event_happened = False

    # Cardgame promotion job
        $ her_shop_help = False
        $ her_shop_help_first = True

    #Rewards
        $ autograph = False #Professor Lockhart's tattoo.

        $ cat_ears_potion_return = False
        $ her_dress_wearable = False

    if not hasattr(renpy.store,'hermione_wardrobe_unlocked') or reset_persistants:
        $ gave_hermione_gift = False
        $ hermione_wardrobe_unlocked = False
        call reset_hermione_clothing # Makes sure she's wearing her default clothing before doing the first tutoring events unlocking the wardrobe.



    ### Hermione Favours ###

    if not hasattr(renpy.store,'hg_pf_dance'): #important!
        $ hg_pf_dance = favor_class(
            tier = 2,
            title = "Dance for me!",
            start_label = "hg_pf_dance",
        )

    if not hasattr(renpy.store,'hg_pf_look_at_ass'): #important!
        $ hg_pf_look_at_ass = favor_class(
            tier = 3,
            title = "Show me that ass!",
            start_label = "hg_pf_look_at_ass",
        )

    if not hasattr(renpy.store,'hg_pf_masturbate'): #important!
        $ hg_pf_masturbate = favor_class(
            tier = 3,
            title = "Touch Yourself!",
            start_label = "hg_pf_masturbate",
        )

    if not hasattr(renpy.store,'hg_pf_handjob'): #important!
        $ hg_pf_handjob = favor_class(
            tier = 3,
            title = "Touch me!",
            start_label = "hg_pf_handjob",
        )

    if not hasattr(renpy.store,'hg_pf_blowjob'): #important!
        $ hg_pf_blowjob = favor_class(
            tier = 4,
            title = "Suck it!",
            max_level = 4,
            start_label = "hg_pf_blowjob",
        )

    if not hasattr(renpy.store,'hg_pf_titjob'): #important!
        $ hg_pf_titjob = favor_class(
            tier = 4,
            title = "Let me fuck them!",
            start_label = "hg_pf_titjob",
        )

    if not hasattr(renpy.store,'hg_pf_sex'): #important!
        $ hg_pf_sex = favor_class(
            tier = 5,
            title = "Let's have sex!",
            start_label = "hg_pf_sex",
        )

    if not hasattr(renpy.store,'hg_pf_anal_sex'): #important!
        $ hg_pf_anal_sex = favor_class(
            tier = 5,
            title = "Time for anal!",
            start_label = "hg_pf_anal_sex",
        )

    if game_difficulty >= 3: #Hardcore
        $ hg_pf_dance.tier = 4
        $ hg_pf_look_at_ass.tier = 5
        $ hg_pf_masturbate.tier = 5
        $ hg_pf_handjob.tier = 5
        $ hg_pf_blowjob.tier = 6
        $ hg_pf_titjob.tier = 6
        $ hg_pf_sex.tier = 7
        $ hg_pf_anal_sex.tier = 8

    $ hg_pf_list = [
                    hg_pf_dance,
                    hg_pf_look_at_ass,
                    hg_pf_masturbate,
                    hg_pf_handjob,
                    hg_pf_blowjob,
                    hg_pf_titjob,
                    hg_pf_sex,
                    hg_pf_anal_sex
        ]



    if not hasattr(renpy.store,'hg_pr_flirt'):
        $ hg_pr_flirt = request_class()
    $ hg_pr_flirt.tier = 1
    $ hg_pr_flirt.title = "She's a flirt"
    $ hg_pr_flirt.start_label = "hg_pr_flirt"
    $ hg_pr_flirt.complete_label = "hg_pr_flirt_complete"

    if not hasattr(renpy.store,'hg_pr_flirt_teacher'):
        $ hg_pr_flirt_teacher = request_class()
    $ hg_pr_flirt_teacher.tier = 1
    $ hg_pr_flirt_teacher.title = "She's bait"
    $ hg_pr_flirt_teacher.start_label = "hg_pr_flirt_teacher"
    $ hg_pr_flirt_teacher.complete_label = "hg_pr_flirt_teacher_complete"

    if not hasattr(renpy.store,'hg_pr_grope'):
        $ hg_pr_grope = request_class()
    $ hg_pr_grope.tier = 1
    $ hg_pr_grope.title = "Let a classmate molest you"
    $ hg_pr_grope.start_label = "hg_pr_grope"
    $ hg_pr_grope.complete_label = "hg_pr_grope_complete"

    if not hasattr(renpy.store,'hg_pr_flash'):
        $ hg_pr_flash = request_class()
    $ hg_pr_flash.tier = 1
    $ hg_pr_flash.title = "Flash your tits to a classmate"
    $ hg_pr_flash.start_label = "hg_pr_flash"
    $ hg_pr_flash.complete_label = "hg_pr_flash_complete"

    if not hasattr(renpy.store,'hg_pr_kiss'):
        $ hg_pr_kiss = request_class()
    $ hg_pr_kiss.tier = 2
    $ hg_pr_kiss.title = "Kiss a girl."
    $ hg_pr_kiss.start_label = "hg_pr_kiss"
    $ hg_pr_kiss.complete_label = "hg_pr_kiss_complete"

    if not hasattr(renpy.store,'hg_pr_handjob'):
        $ hg_pr_handjob = request_class()
    $ hg_pr_handjob.tier = 2
    $ hg_pr_handjob.title = "Give a handjob to a classmate"
    $ hg_pr_handjob.start_label = "hg_pr_handjob"
    $ hg_pr_handjob.complete_label = "hg_pr_handjob_complete"

    if not hasattr(renpy.store,'hg_pr_blowjob'):
        $ hg_pr_blowjob = request_class()
    $ hg_pr_blowjob.tier = 2
    $ hg_pr_blowjob.title = "Give a blowjob to a classmate"
    $ hg_pr_blowjob.start_label = "hg_pr_blowjob"
    $ hg_pr_blowjob.complete_label = "hg_pr_blowjob_complete"

    if not hasattr(renpy.store,'hg_pr_sex'):
        $ hg_pr_sex = request_class()
    $ hg_pr_sex.tier = 2
    $ hg_pr_sex.title = "Have sex with a classmate"
    $ hg_pr_sex.start_label = "hg_pr_sex"
    $ hg_pr_sex.complete_label = "hg_pr_sex_complete"


    $ hg_pr_list = [hg_pr_flirt,
                    hg_pr_flirt_teacher,
                    hg_pr_grope,
                    hg_pr_flash,
                    hg_pr_kiss,
                    hg_pr_handjob,
                    hg_pr_blowjob,
                    hg_pr_sex,
        ]



    if not hasattr(renpy.store,'hg_ps_get_panties'):
        $ hg_ps_get_panties = shaming_class()
    $ hg_ps_get_panties.tier = 1
    $ hg_ps_get_panties.title = "Panty Thief"
    $ hg_ps_get_panties.start_label = "hg_ps_get_panties"
    $ hg_ps_get_panties.complete_label = "hg_ps_get_panties_complete"

    if not hasattr(renpy.store,'hg_ps_buttplug'):
        $ hg_ps_buttplug = shaming_class()
    $ hg_ps_buttplug.tier = 1
    $ hg_ps_buttplug.title = "Wear A Buttplug"
    $ hg_ps_buttplug.start_label = "hg_ps_buttplug"
    $ hg_ps_buttplug.complete_label = "hg_ps_buttplug_complete"

    if not hasattr(renpy.store,'hg_ps_cumslut'):
        $ hg_ps_cumslut = shaming_class()
    $ hg_ps_cumslut.tier = 2
    $ hg_ps_cumslut.title = "Wear My Cum"
    $ hg_ps_cumslut.start_label = "hg_ps_cumslut"
    $ hg_ps_cumslut.complete_label = "hg_ps_cumslut_complete"

    if not hasattr(renpy.store,'hg_ps_walk'):
        $ hg_ps_walk = shaming_class()
    $ hg_ps_walk.tier = 2
    $ hg_ps_walk.title = "Walk Of Shame"
    $ hg_ps_walk.start_label = "hg_ps_walk"
    $ hg_ps_walk.complete_label = "hg_ps_walk_complete"

    $ hg_ps_list = [hg_ps_get_panties,
                    hg_ps_buttplug,
                    hg_ps_cumslut]
#    return


label updated_hermione_favors: # For 1.37

    if not hasattr(renpy.store,'hg_T1_trigger'):
        $ her_tier = 1
        $ hg_T1_trigger          = True # Temporary
        $ hg_T2_jerk_off_trigger = False
        $ hg_T3_strip_trigger    = False
        $ hg_T4_trigger          = True # Temporary
        $ hg_T5_blowjob_trigger  = False
        $ hg_T6_sex_trigger      = False

    if not hasattr(renpy.store,'hg_pf_talk'):
        $ hg_pf_talk   = event_class(title = "Talk to me!", start_label = "hg_pf_talk", start_tier = 1, events = [
            [
            ["hg_pf_talk_T1_intro_E1"],
            ["hg_pf_talk_T1_E1"]
            ],

            [
            ["hg_pf_talk_T2_intro_E1"],
            ["hg_pf_talk_T2_E1"]
            ],

            [
            ["hg_pf_talk_T3_intro_E1"],
            ["hg_pf_talk_T3_E1"]
            ]

            ],
            icons = [None, None, None], #if a tier doesn't need an icon replace with None
            iconset = [["heart_empty", "heart_yellow"],["heart_empty", "heart_yellow"],["heart_empty", "heart_red"]]
            )

    if not hasattr(renpy.store,'hg_pf_admire_panties'):
        $ hg_pf_admire_panties   = event_class(title = "Show me your Panties!", start_label = "hg_pf_admire_panties", start_tier = 1, events = [
            [
            ["hg_pf_admire_panties_T1_intro_E1"],
            ["hg_pf_admire_panties_T1_E1"]
            ],

            [
            ["hg_pf_admire_panties_T2_intro_E1"],
            ["hg_pf_admire_panties_T2_E1"]
            ],

            [
            ["hg_pf_admire_panties_T3_intro_E1"],
            ["hg_pf_admire_panties_T3_E1"],
            ["hg_pf_admire_panties_T3_E2"]
            ]

            ],
            icons = [None, None, None], #if a tier doesn't need an icon replace with None
            iconset = [["heart_empty", "heart_yellow"],["heart_empty", "heart_red"],["heart_empty", "heart_yellow"]]
            )

    if not hasattr(renpy.store,'hg_pf_admire_breasts'):
        $ hg_pf_admire_breasts   = event_class(title = "Show me your tits!", start_label = "hg_pf_admire_breasts", start_tier = 1, events = [
            [
            ["hg_pf_admire_breasts_T1_intro_E1"],
            ["hg_pf_admire_breasts_T1_intro_E2"],
            ["hg_pf_admire_breasts_T1_E2"]
            ],

            [
            ["hg_pf_admire_breasts_T2_intro_E1"],
            ["hg_pf_admire_breasts_T2_intro_E2"],
            ["hg_pf_admire_breasts_T2_E2"]
            ],

            [
            ["hg_pf_admire_breasts_T3_intro_E1"],
            ["hg_pf_admire_breasts_T3_E1"]
            ],

            [
            ["hg_pf_admire_breasts_T4_intro_E1"],
            ["hg_pf_admire_breasts_T4_E1"],
            ["hg_pf_admire_breasts_T4_E2"]
            ]

            ],
            icons = [None, None, None, None], #if a tier doesn't need an icon replace with None
            iconset = [["heart_empty", "heart_yellow"],["heart_empty", "heart_yellow"],["heart_empty", "heart_red"],["heart_empty", "heart_red"]]
            )



    if not hasattr(renpy.store,'hg_pf_grope'):
        $ hg_pf_grope   = event_class(title = "Grope her!", start_label = "hg_pf_grope", start_tier = 1, events = [
            [
            ["hg_pf_grope_T1_fail_intro"],
            ["hg_pf_grope_T1_fail_repeat"],
            ],

            [
            ["hg_pf_grope_T2_intro_E1"],
            ["hg_pf_grope_T2_E1"]
            ],

            [
            ["hg_pf_grope_T3_intro_E1"],
            ["hg_pf_grope_T3_E1"]
            ],

            [
            ["hg_pf_grope_T4_intro_E1"],
            ["hg_pf_grope_T4_intro_E2"],
            ["hg_pf_grope_T4_E2"]
            ]

            ],
            icons = [None, None, None, None], #if a tier doesn't need an icon replace with None
            iconset = [["heart_empty", "heart_black"],["heart_empty", "heart_yellow"],["heart_empty", "heart_yellow"],["heart_empty", "heart_red"]]
            )

    $ hg_favor_list = [
        hg_pf_talk,
        hg_pf_admire_breasts,
        hg_pf_admire_panties,
        hg_pf_grope
        ]

    return
