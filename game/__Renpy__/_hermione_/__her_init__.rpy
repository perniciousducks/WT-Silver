

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
        $ hermione_hair_a           = "characters/hermione/body/head/A_1.png"
        $ hermione_hair_b           = "characters/hermione/body/head/A_1_2.png"
        $ h_hair_style              = "A"
        $ h_hair_color              = 1
        $ h_can_color               = ["A","B"]


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
        $ hermione_chibi_xpos_name        = "base" #Stored xpos name
        $ hermione_chibi_ypos_name        = "base" #Stored ypos name
        $ hermione_chibi_stand       = "characters/hermione/chibis/walk/h_walk_a_01.png"
        $ hermione_chibi_stand_f     = "characters/hermione/chibis/walk/h_walk_a_01.png"
        $ hermione_chibi_stand_nude  = "characters/hermione/chibis/walk/h_walk_n_01.png" #NOT IN USE
        $ hermione_chibi_blink       = "ch_hem blink_a"
        $ hermione_chibi_blink_f     = "ch_hem blink_a_flip"
        $ hermione_chibi_walk        = "ch_hem walk_a"
        $ hermione_chibi_walk_f      = "ch_hem walk_a_flip"
        $ hermione_chibi_run         = "ch_hem run_a"
        $ hermione_chibi_run_f       = "ch_hem run_a_flip"
        $ hermione_chibi_fly         = "ch_hem fly_a"
        $ hermione_chibi_fly_f       = "ch_hem fly_a_flip"

        $ u_h_animation              = ""
        $ u_h_animation_paused       = ""
        $ u_h_ani_xpos               = 0
        $ u_h_ani_ypos               = 0

        $ hermione_chibi_xpos        = 540
        $ hermione_chibi_ypos        = 250
        $ hermione_chibi_zorder      = 3




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

        $ h_request_wear_outfit = False


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
        $ hermione_wear_piercings         = False
        $ hermione_wear_tattoos           = False

        $ hermione_wear_outfit = False



        #Top
        $ hermione_top              = "characters/hermione/clothes/tops/base/top_1_g.png"
        $ h_top                     = "top_1_g"
        $ h_top_color               = "base"


        #Bottom
        $ hermione_bottom            = "characters/hermione/clothes/bottoms/base/skirt_1.png"
        $ h_bottom                   = "skirt_1"
        $ h_bottom_color             = "base"


        #Underwear
        $ hermione_bra              = "characters/hermione/clothes/underwear/base/bra_base.png"
        $ h_bra                     = "bra_base"
        $ h_bra_color               = "base"

        $ hermione_panties          = "characters/hermione/clothes/underwear/base/panties_base.png"
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

        $ hermione_hat              = "characters/hermione/accessories/hats/hair_A/blank.png"
        $ h_hat                     = "blank"
        $ h_hat_color               = "base"

        $ hermione_glasses          = "characters/hermione/accessories/glasses/blank.png"
        $ h_glasses                 = "blank"
        $ h_glasses_color           = "base"

        $ hermione_ears             = "characters/hermione/accessories/ears/blank.png"
        $ h_ears                    = "blank"


        #Miscellaneous
        $ hermione_wear_buttplug     = False
        $ hermione_buttplug          = "characters/hermione/accessories/plugs/blank.png"
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
        $ hermione_ear_piercing      = "characters/hermione/accessories/piercings/base/blank.png"
        $ h_ear_piercing             = "blank"
        $ h_ear_piercing_color       = "base"

        $ hermione_nipple_piercing   = "characters/hermione/accessories/piercings/base/blank.png"
        $ h_nipple_piercing          = "blank"
        $ h_nipple_piercing_color    = "base"

        $ hermione_belly_piercing    = "characters/hermione/accessories/piercings/base/blank.png"
        $ h_belly_piercing           = "blank"
        $ h_belly_piercing_color     = "base"

        $ hermione_intimate_piercing = "characters/hermione/accessories/piercings/base/blank.png"
        $ h_intimate_piercing        = "blank"
        $ h_intimate_piercing_color  = "base"

        #Tattoos
        $ hermione_tattoos_list      = []
        $ h_tattoos_color            = "base"

        $ transparency               = 1

        #Outfits
        $ hermoine_outfit_GLBL = None
        $ hermione_temp_outfit = None
        $ temp_outfit = None



    ### ADD MORE HERMIONE PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return



label her_clothing_lists_init: #Lists update at every game start!

    #Tops
    $ h_top_nipfix_list             = ["onepiece_microdress",
                                       "top_fishnets",
                                      ]

    $ h_top_has_no_recolor_list     = ["leather_jacket_short_sleeves",
                                       "leather_jacket_short_sleeves_open",
                                       "leather_jacket_sleeveless",
                                       "leather_jacket_sleeveless_open",
                                       "leather_jacket_sleeves",
                                       "leather_jacket_sleeves_open",
                                       "top_rocker",
                                       "top_fishnets",
                                       ]

    $ h_top_remove_bra_list         = ["top_1_g",
                                       "top_2_g",
                                       "top_3_g",
                                       "top_4_g",
                                       "top_6_g",
                                       "top_cheer_sexy_g",
                                       "top_cheer_sexy_s",
                                       "top_cheer_sexy_r",
                                       "top_cheer_sexy_h",
                                       "top_cheer_g",
                                       "top_cheer_s",
                                       "top_cheer_r",
                                       "top_cheer_h",
                                       "normal_pullover",
                                       "normal_sweater",
                                       ]

    $ h_lift_top_list               = ["top_1_g",
                                       "top_2_g",
                                       "top_3_g",
                                       "top_4_g",
                                       "top_6_g",
                                       "normal_pullover",
                                       "normal_pullover_sexy",
                                       "top_fishnets",
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
                                       "skirt_belted_mini",
                                       "skirt_belted_micro",
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
                                       "onepiece_bikini_string",
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
    $ h_bra_pressed_list            = ["top_fishnets"
                                      ]

    #Piercings
    $ ear_piercings_list            = ["ears_hearts_large",
                                       "ears_hearts",
                                       "ears_pearls",
                                       "ears_straight",
                                       "ears_rings",
                                      ]
    $ nipple_piercings_list         = ["nipples_pearls",
                                      ]
    $ belly_piercings_list          = ["belly_pearls",
                                      ]
    $ intimate_piercings_list       = [
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

    $ h_mouth_list                  = ["angry",
                                       "annoyed",
                                       "base",
                                       "clench",
                                       "crooked_smile",
                                       "cum",
                                       "disgust",
                                       "full",
                                       "full_cum",
                                       "gag",
                                       "grin",
                                       "mad",
                                       "mouthpiece",
                                       "mouthpiece_drool",
                                       "normal",
                                       "open",
                                       "open_tongue",
                                       "open_wide_tongue",
                                       "open_wide_tongue_cum",
                                       "scream",
                                       "shock",
                                       "silly",
                                       "smile",
                                       "soft",
                                       "upset"
                                       ]

    $ h_eye_list                    = ["ahegao",
                                       "ahegao_intense",
                                       "ahegao_mad",
                                       "ahegao_raised",
                                       "ahegao_squint",
                                       "ahegao_wide",
                                       "angry",
                                       "angryCl",
                                       "angryL",
                                       "annoyed",
                                       "base",
                                       "baseL",
                                       "closed",
                                       "concerned",
                                       "dead",
                                       "dead_mad",
                                       "down",
                                       "down_raised",
                                       "frown",
                                       "glance",
                                       "glanceL",
                                       "happy",
                                       "happyCl",
                                       "narrow",
                                       "shocked",
                                       "shocked_raised",
                                       "silly",
                                       "soft",
                                       "squint",
                                       "squintL",
                                       "surprised",
                                       "suspicious",
                                       "wide",
                                       "wide_stare",
                                       "wideL",
                                       "wink",
                                       "worried",
                                       "worriedCl",
                                       "worriedL"
                                       ]
    return



label her_progress_init:

    if not hasattr(renpy.store,'her_whoring') or reset_persistants:

        #Stats
        $ her_whoring = 0
        $ her_reputation = 0
        $ her_tutoring = 0

        $ mad = 0
        $ forest_BJ_progress = 1

        #Flags
        $ hermione_busy = False
        $ hermione_unlocked = False
        $ hermione_favors = False
        $ hermione_tutoring = False

        $ hermione_desperate_done = False

        #Names
        $ genie_name = "sir"
        $ hermione_name = "miss granger"

        #Clothing Flags
        $ hermione_dribble = False
        $ dribble_equippable = False
        $ hermione_wetpanties = False
        $ wetpanties_equippable = False

        #Stat Screen
        $ her_jerk_off_counter = 0

        #Public Request Vars.
        $ hg_pr_SexWithClassmate_AltFlag = False

        $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. "Lazy Akabur bug". Turns FALSE after that.
        $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
        $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
        $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        #Public Shaming Flags
        $ hg_ps_PantyThief_SoakedPantiesFlag = False
        $ current_job = 0
        $ transparent_quest = False


        ### HERMIONE EVENT VARS ###
        $ jerk_off_session = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

        $ tutoring_offer_made = False #If you offered her to tutor her (In event_12). Affects conversation in the next event.

        $ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (event_09)
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

    #Rewards
        $ autograph = False #Professor Lockhart's tattoo.

        $ cat_ears_potion_return = False
        $ her_dress_wearable = False

        $ hg_hidden_blowjob_character_list = ["snape"]
        $ hg_hidden_blowjob_seen_list = []

    ### ADD MORE HERMIONE PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return
