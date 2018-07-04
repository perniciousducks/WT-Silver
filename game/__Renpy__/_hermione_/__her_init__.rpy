

init python:

    class hermione_character_face(silver_character_face):
        description = ""
        id = 0

        eyes = ""
        eye_color = ""
        nose = ""
        cheeks = ""
        mouth = ""
        lipstick = ""
        tears = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def set(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getLayers(self, parent):
            layers = []
            if self.cheeks != "":
                layers.append(parent.root+"body/face/cheeks/"+self.cheeks)
            if self.nose != "":
                layers.append(parent.root+"body/face/nose/"+self.nose)
            if self.mouth != "":
                layers.append(parent.root+"body/face/mouth/"+self.lipstick+"/"+self.mouth)
            if self.eyes != "":
                layers.append(parent.root+"body/face/eyes/"+parent.eye_color+"/"+self.eyes)
            if self.tears != "":
                layers.append(parent.root+"body/face/tears/"+self.tears)
            return layers

    class hermione_character_chibi(silver_character_chibi):
        level_ref = [
        ["characters/hermione/chibis/walk/h_walk_n_01.png","ch_hem blink_n","ch_hem blink_n_flip","ch_hem walk_n","ch_hem walk_n_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_a_01.png","ch_hem blink_a","ch_hem blink_a_flip","ch_hem walk_a","ch_hem walk_a_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_d_01.png","ch_hem blink_d","ch_hem blink_d_flip","ch_hem walk_d","ch_hem walk_d_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_e_01.png","ch_hem blink_e","ch_hem blink_e_flip","ch_hem walk_e","ch_hem walk_e_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_f_01.png","ch_hem blink_f","ch_hem blink_f_flip","ch_hem walk_f","ch_hem walk_f_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_g_01.png","ch_hem blink_g","ch_hem blink_g_flip","ch_hem walk_g","ch_hem walk_g_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"],
        ["characters/hermione/chibis/walk/h_walk_h_01.png","ch_hem blink_h","ch_hem blink_h_flip","ch_hem walk_h","ch_hem walk_h_flip","ch_hem run_a","ch_hem run_a_flip","ch_hem fly_a","ch_hem fly_a_flip"]
        ]

        def setLevel(self, level):
            if level >= 0 and level < len(self.level_ref):
                self.stand_img = self.level_ref[level][0]
                self.blink_img = self.level_ref[level][1]
                self.blink_img_f = self.level_ref[level][2]
                self.walk_img = self.level_ref[level][3]
                self.walk_img_f = self.level_ref[level][4]
                self.run_img = self.level_ref[level][5]
                self.run_img_f = self.level_ref[level][6]
                self.fly_img = self.level_ref[level][7]
                self.fly_img_f = self.level_ref[level][8]

    class hermione_character_uniform(sliver_character_uniform):
        level_ref = [["",""],[1,1],[2,1],[3,2],[4,3],[5,4],[6,4]]

        bot_color = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def setLevel(self, level):
            if level >= 0 and level < len(self.level_ref):
                self.top = self.level_ref[level][0]
                self.bot = self.level_ref[level][1]

        def getLayers(self, parent):
            layers = []
            if self.panties != "" and self.wear_panties and not self.wear_bot:
                layers.append(parent.root+"clothes/underwear/"+self.panties)
            if self.bra != "" and self.wear_bra and not self.wear_top:
                layers.append(parent.root+"clothes/underwear/"+self.bra)
            if self.bot != "" and self.wear_bot:
                layers.append(parent.root+"clothes/uniform/bot/"+self.bot_color+str(self.bot)+".png")
            if self.top != "" and self.wear_top:
                layers.append(parent.root+"clothes/uniform/top/"+str(self.top)+".png")
            return layers


label __init_variables:


    if not hasattr(renpy.store,'reset_char_obj'): #important!
        $ reset_char_obj            = True

    if not hasattr(renpy.store,'hermione_SC'): #important!
        $ hermione_SC = silver_character(
            root = "characters/hermione/",

            xpos = 370,
            ypos = 0,

            name = "Hermione Granger",
            pet_name = "Miss Granger",
            genie_name = "Professor",

            eye_color = "brown",

            screen = "test_herm_obj",
            screen_head = "test_herm_head_obj",

            chibi = hermione_character_chibi(
                stand_img = "characters/hermione/chibis/walk/h_walk_a_01.png",
                blink_img = "ch_hem blink_a",
                blink_img_f = "ch_hem blink_a_flip",
                walk_img = "ch_hem walk_a",
                walk_img_f = "ch_hem walk_a_flip",
                run_img = "ch_hem run_a",
                run_img_f = "ch_hem run_a_flip",
                fly_img = "ch_hem fly_a",
                fly_img_f = "ch_hem fly_a_flip",
                xpos = 540,
                ypos = 250
            ),

            char_ref = Character('Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250),
            h_char_ref = Character('Hermione', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"),

            body = sliver_character_body(
                head = sliver_character_head(
                    expression = None,
                    base = "hermione_base.png",
                    hair = "A_1.png",
                    cheeks = "",
                    glasses = ""
                ),
                left_arm = "left_1.png",
                right_arm = "right_1.png",
                torso = "torso.png",
                torso_pressed = "torso_pressed.png",
                abdomen = "abdomen.png",
                legs = "legs_1.png"

            ),

            uniform = hermione_character_uniform(
                top = 1,
                bot = 1,
                panties = "base_panties_1.png",
                bra = "base_bra_white_1.png",
            ),
            acc = ""
        )

    $ hermione_SC.faces = getCharacterFaces('hermione_face',hermione_character_face)
    $ hermione_SC.setFace(1)

    $ reset_char_obj             = False

    return



### HERMIONE INITS ###

label her_init:

    if not hasattr(renpy.store,'hermione_SC'): #important!
        $ hermione_SC = silver_character(
            root = "characters/hermione/",

            xpos = 370,
            ypos = 0,

            name = "Hermione Granger",
            pet_name = "Miss Granger",
            genie_name = "Professor",

            eye_color = "brown",

            screen = "test_herm_obj",
            screen_head = "test_herm_head_obj",

            chibi = hermione_character_chibi(
                stand_img = "characters/hermione/chibis/walk/h_walk_a_01.png",
                blink_img = "ch_hem blink_a",
                blink_img_f = "ch_hem blink_a_flip",
                walk_img = "ch_hem walk_a",
                walk_img_f = "ch_hem walk_a_flip",
                run_img = "ch_hem run_a",
                run_img_f = "ch_hem run_a_flip",
                fly_img = "ch_hem fly_a",
                fly_img_f = "ch_hem fly_a_flip",
                xpos = 540,
                ypos = 250
            ),

            char_ref = Character('Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250),
            h_char_ref = Character('Hermione', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"),

            body = sliver_character_body(
                head = sliver_character_head(
                    expression = None,
                    base = "hermione_base.png",
                    hair = "A_1.png",
                    cheeks = "",
                    glasses = ""
                ),
                left_arm = "left_1.png",
                right_arm = "right_1.png",
                torso = "torso.png",
                torso_pressed = "torso_pressed.png",
                abdomen = "abdomen.png",
                legs = "legs_1.png"

            ),

            uniform = hermione_character_uniform(
                top = 1,
                bot = 1,
                panties = "base_panties_1.png",
                bra = "base_bra_white_1.png",
            ),
            acc = ""
        )

    if not hasattr(renpy.store,'hermione_base') or reset_persistants:

        #Body
        $ hermione_base             = "characters/hermione/body/base/hermione_base.png"
        $ hermione_body             = "characters/hermione/body/face/preset/body_01.png"     ### REMOVED! NOT IN USE!
        $ h_body                    = "body_01"

        #Face
        $ hermione_mouth            = "characters/hermione/face/mouth/nude/base.png"
        $ h_mouth                   = "base"
        $ h_lipstick                = "nude"

        $ hermione_eyes             = "characters/hermione/face/eyes/brown/base.png"
        $ hermione_eyebrows         = "characters/hermione/face/eyebrows/brown/base.png"
        $ h_eyes                    = "base"
        $ h_eye_color               = "brown"

        $ hermione_cheeks           = "characters/hermione/face/cheeks/00_blank.png"
        $ h_cheeks                  = "00_blank"
        $ h_eye_shadow              = "00_blank"

        $ hermione_tears            = "characters/hermione/face/tears/00_blank.png"
        $ h_tears                   = "00_blank"
        $ h_display_tears           = False

        $ hermione_emote            = "characters/emotes/00_blank.png"
        $ h_emote                   = "00_blank"
        $ hermione_emote_anger      = False
        $ hermione_emote_exclam     = False
        $ hermione_emote_hearts     = False
        $ hermione_emote_question   = False
        $ hermione_emote_sweat      = False
        $ hermione_emote_suprize    = False


        #Breasts
        $ hermione_breasts          = "characters/hermione/body/breasts/breasts_nipfix.png"
        $ h_breasts                 = "breasts_nipfix"

        $ hermione_perm_expand           = False
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
        $ h_action_bra           = ""
        $ h_action_bottom        = ""
        $ h_action_panties       = ""
        $ h_action_gloves        = ""


        $ hermione_action_left_arm  = "characters/hermione/clothes/uniform/action/00_blank.png"
        $ hermione_action_right_arm = "characters/hermione/clothes/uniform/action/00_blank.png"
        $ hermione_action_a         = "characters/hermione/clothes/uniform/action/00_blank.png"
        $ hermione_action_b         = "characters/hermione/clothes/uniform/action/00_blank.png"

        $ h_action_right_arm        = "00_blank.png"
        $ h_action_left_arm         = "00_blank.png"
        $ h_action_a                = "00_blank.png"
        $ h_action_b                = "00_blank.png"

        $ h_action_show_arms        = False
        $ h_action_show_bra         = True
        $ h_action_show_panties     = True
        $ h_action_show_top         = True
        $ h_action_show_skirt       = True

        $ hermione_action_bra       = "characters/hermione/clothes/underwear/base/bra_base.png"
        $ hermione_action_panties   = "characters/hermione/clothes/underwear/base/panties_base.png"
        $ hermione_action_top       = "characters/hermione/clothes/tops/base/uni_top_1.png"
        $ hermione_action_skirt     = "characters/hermione/clothes/bottoms/base/uni_skirt_1.png"

        $ custom_outfit             = 0
        $ hermione_costume          = False
        $ hermione_wear_costume     = False
        $ hermione_costume_action_a = "characters/hermione/clothes/custom/00_blank.png"


        #Positioning
        $ hermione_xpos             = 370
        $ hermione_ypos             = 0
        $ hermione_xpos_name        = "base" #Stored xpos name
        $ hermione_ypos_name        = "base" #Stored xpos name
        $ h_xpos                    = 0   #NOT IN USE
        $ h_ypos                    = 0   #NOT IN USE
        $ hermione_zorder           = 5

        $ hermione_head_xpos        = 605
        $ hermione_head_ypos        = 235
        $ hermione_head_xpos_name   = "base" #Stored xpos name
        $ hermione_head_ypos_name   = "base" #Stored xpos name
        $ hermione_head_zorder      = 8

        $ her_head_only             = 300 #(340,300,290) #NOT IN USE
        $ her_head_tits             = 235 #NOT IN USE



    #if not hasattr(renpy.store,'ADD') or reset_persistants:
    ### ADD MORE BODY PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return




label her_clothing_init:

    if not hasattr(renpy.store,'h_request_wear_top') or reset_persistants:

        #Save State
        $ h_request_wear_top              = True
        $ h_request_wear_bra              = False
        $ h_request_wear_bottom           = True
        $ h_request_wear_panties          = False

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

        #Top
        $ hermione_top              = "characters/hermione/clothes/tops/base/uni_top_1.png"
        $ h_top                     = "uni_top_1"
        $ h_top_color               = "base"


        #Bottom
        $ hermione_skirt            = "characters/hermione/clothes/bottoms/base/uni_skirt_1.png"
        $ h_skirt                   = "uni_skirt_1"
        $ h_skirt_color             = "base"


        #Underwear
        $ hermione_bra              = "characters/hermione/clothes/underwear/base/bra_base.png"
        $ h_bra                     = "bra_base"
        $ h_bra_color               = "base"

        $ hermione_panties          = "characters/hermione/clothes/underwear/base/panties_base.png"
        $ h_panties                 = "panties_base"
        $ h_panties_color           = "base"

        $ hermione_onepiece         = "characters/hermione/clothes/onepieces/base/00_blank.png"
        $ h_onepiece                = "00_blank"
        $ h_onepiece_color          = "base"

        $ hermione_garterbelt       = "characters/hermione/clothes/garterbelts/00_blank.png"
        $ h_garterbelt              = "00_blank"
        $ h_garterbelt_color        = "base"

        $ hermione_panties_overlay      = "characters/hermione/clothes/underwear/00_blank.png"


        #Other Clothing
        $ hermione_neckwear         = "characters/hermione/clothes/neckwear/base/00_blank.png"
        $ h_neckwear                = "00_blank"
        $ h_neckwear_color          = "base"

        $ hermione_body_accs_list   = []

        $ hermione_gloves           = "characters/hermione/clothes/gloves/base/00_blank.png"
        $ h_gloves                  = "00_blank"
        $ h_gloves_color            = "base"

        $ hermione_stockings        = "characters/hermione/clothes/stockings/base/00_blank.png"
        $ h_stockings               = "00_blank"
        $ h_stockings_color         = "base"
        $ temp_stockings            = h_stockings

        $ hermione_robe             = "characters/hermione/clothes/robe/base/gryff_robe.png"
        $ h_robe                    = "gryff_robe"
        $ h_robe_color              = "base"

        #Accessories
        $ hermione_makeup_list      = []

        $ hermione_hat              = "characters/hermione/accessories/hats/00_blank.png"
        $ h_hat                     = "00_blank"
        $ h_hat_color               = "base"

        $ hermione_glasses          = "characters/hermione/accessories/glasses/00_blank.png"
        $ h_glasses                 = "00_blank"
        $ h_glasses_color           = "base"

        $ hermione_ears             = "characters/hermione/accessories/ears/00_blank.png"
        $ h_ears                    = "00_blank"


        #Miscellaneous
        $ hermione_wear_buttplug     = False
        $ hermione_buttplug          = "characters/hermione/accessories/plugs/00_blank.png"
        $ h_buttplug                 = "00_blank"

        $ hermione_pubic_hair        = "characters/hermione/body/pubic_hair/00_blank.png"
        $ h_pubic_hair               = "00_blank"

        #Piercings
        $ hermione_ear_piercing      = "characters/hermione/accessories/piercings/base/00_blank.png"
        $ h_ear_piercing             = "00_blank"
        $ h_ear_piercing_color       = "base"

        $ hermione_nipple_piercing   = "characters/hermione/accessories/piercings/base/00_blank.png"
        $ h_nipple_piercing          = "00_blank"
        $ h_nipple_piercing_color    = "base"

        $ hermione_belly_piercing    = "characters/hermione/accessories/piercings/base/00_blank.png"
        $ h_belly_piercing           = "00_blank"
        $ h_belly_piercing_color     = "base"

        $ hermione_intimate_piercing = "characters/hermione/accessories/piercings/base/00_blank.png"
        $ h_intimate_piercing        = "00_blank"
        $ h_intimate_piercing_color  = "base"

        #Tattoos
        $ hermione_tattoos_list      = []
        $ h_tattoos_color            = "base"

        $ transparency               = 1

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


    #if not hasattr(renpy.store,'ADD') or reset_persistants:
    ### ADD MORE HERMIONE PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return


label her_chibi_init:

    if not hasattr(renpy.store,'hermione_chibi_stand') or reset_persistants:
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

        $ her_chibi_dance_xpos       = 350 #Not in use
        $ her_chibi_dance_ypos       = 180 #Not in use


        $ u_h_animation              = ""
        $ u_h_animation_paused       = ""
        $ u_h_ani_xpos               = 0
        $ u_h_ani_ypos               = 0

        $ hermione_SC.chibi.xpos     = 540
        $ hermione_SC.chibi.ypos     = 250
        $ hermione_chibi_zorder      = 3


    #if not hasattr(renpy.store,'ADD') or reset_persistants:
    ### ADD MORE CHIBI PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return


label her_clothing_lists_init: #Lists update at every game start!

    #Tops
    $ h_top_nipfix_list             = ["onepiece_microdress",
                                       "top_fishnets",
                                      ]

    $ h_top_has_no_recolor_list     = ["wicked_leather_jacket_short_sleeves",
                                       "wicked_leather_jacket_short_sleeves_open",
                                       "wicked_leather_jacket_sleeveless",
                                       "wicked_leather_jacket_sleeveless_open",
                                       "wicked_leather_jacket_sleeves",
                                       "wicked_leather_jacket_sleeves_open",
                                       "wicked_rocker_top",
                                       "top_fishnets",
                                       ]

    $ h_top_remove_bra_list         = ["uni_top_1",
                                       "uni_top_2",
                                       "uni_top_3",
                                       "uni_top_4",
                                       "uni_top_6",
                                       "uni_top_cheer_skimpy",
                                       "uni_top_cheer",
                                       "normal_pullover",
                                       "normal_sweater",
                                       ]

    $ h_lift_top_list               = ["uni_top_1",
                                       "uni_top_2",
                                       "uni_top_3",
                                       "uni_top_4",
                                       "uni_top_6",
                                       "normal_pullover",
                                       "normal_pullover_sexy",
                                       "top_fishnets",
                                       "wicked_rocker_top",
                                       ]


    #Bottoms
    $ h_skirts_list                 = ["uni_skirt_1",
                                       "uni_skirt_2",
                                       "uni_skirt_3",
                                       "uni_skirt_4",
                                       "uni_skirt_5",
                                       "uni_skirt_1_low",
                                       "uni_skirt_2_low",
                                       "uni_skirt_3_low",
                                       "uni_skirt_4_low",
                                       "uni_skirt_cheer",
                                       "uni_skirt_cheer_skimpy",
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
                                       "onepiece_swimsuit",
                                       "onepiece_swimsuit_halterless",
                                       "onepiece_bikini_string",
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
                                      ]
    $ nipple_piercings_list         = ["nipples_pearls",
                                      ]
    $ belly_piercings_list          = ["belly_pearls",
                                      ]
    $ intimate_piercings_list       = [
                                      ]

    return


label her_progress_init:

    #Update 1.3
    if not hasattr(renpy.store,'whoring') or reset_persistants:

        # Hermione levels
        $ whoring = 0 #Default: 0
        $ hg_whoring = 0
        $ hg_whoring_lvl = 0

        $ h_whoring = 0
        $ h_reputation = 21
        $ level = "00" #Hermione's whoring level.

        $ mad = 0 #Every day -1.
        $ being_mean = 0 #+1 every time you are being mean to hermione.

        $ dates = 0 #Tracks how many times Hermione been tutored.
        $ tutoring_events = 0 #Get's +1 point every time a tutoring special event happens.
        $ knowledge = 0
        $ teachers_pet = 0
        $ classmates_pet = 0

        $ genie_name = "sir"
        $ hermione_name = "miss granger"

        $ hermione_dribble = False
        $ dribble_equippable = False
        $ hermione_wetpanties = False
        $ wetpanties_equippable = False

        $ hermione_desperate_done = False


        ### GETTING LETTERS ###
        $ letter_from_hermione_02 = False #Turns true when you get second letter from Hermione.


        $ hermione_takes_classes = False #Turns True when Hermione becomes unavailable for summon after performing personal request in the morning.
        $ hermione_sleeping = False


        ### HERMIONE FAVOURS ###

        #Personal Favor Points
        $ hg_pf_points = [0] * 12
        $ hg_pf_hearts = [0] * 12
        $ hg_pf_complete = [False] * 12


        #Public Request Points
        $ hg_pr_points = [0] * 11
        $ hg_pr_complete = [False] * 11
        $ hg_pr_InProgress = [False] * 11

        #Public Request Vars.
        $ hg_pr_SexWithClassmate_AltFlag = False

        #Public Shaming Flags
        $ hg_ps_PantyThief_SoakedPantiesFlag = False

        $ transparent_quest = False


        ### HERMIONE EVENT VARS ###

        $ v_tutoring = 0
        $ summoning_hermione_unlocked = False #Unlocks after event_14. Adds "Summon Hermione" button to the door.
        $ tutoring_hermione_unlocked = False #Unlocks after event_14.
        $ buying_favors_from_hermione_unlocked = False

        $ jerk_off_session = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

        $ tutoring_offer_made = False #If you offered her to tutor her (In event_12). Affects conversation in the next event.

        $ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (event_09)
        $ hermione_is_waiting_02 = False #Turns True at the end of second special event with Snape. Triggers next visit from Hermione

        $ micro_skirt = False
        $ hair_color = 0
        $ collar = 0
        $ custom_01_worn = False
        $ custom_02_worn = False
        $ custom_03_worn = False
        $ custom_04_worn = False
        $ custom_05_worn = False
        $ custom_06_worn = False
        $ custom_07_worn = False
        $ custom_08_worn = False
        $ custom_09_worn = False
        $ custom_10_worn = False
        $ scene_number = 1
        $ cust_char_1_enabled = False
        $ cust_char_2_enabled = False
        $ cust_char_3_enabled = False

    #Buttplug Events
        $ buttplug_magic_known   = False
        $ buttplug_1_worn        = False
        $ buttplug_2_worn        = False
        $ buttplug_3_worn        = False
        $ buttplug_1_question    = False
        $ buttplug_2_question    = False
        $ buttplug_3_question    = False

    #Custom Variables Previously Defined at desk
        $ current_job = 0
        $ custom_breast = 0
        $ custom_bra = 0
        $ maid_working_unlocked = True

    #Clothing Events
        $ hermione_door_event_happened = False

    #Rewards
    if not hasattr(renpy.store,'reward_her_wool_clothing') or reset_persistants:
        $ reward_her_wool_clothing = False
        $ reward_her_lace_clothing = False
        $ reward_her_latex_clothing = False
        $ autograph = False #Professor Lockhart's tattoo.

    if not hasattr(renpy.store,'reward_her_red_lipstick') or reset_persistants:
        $ reward_her_red_lipstick = False
        $ reward_her_pink_lipstick = False
        $ reward_her_black_lipstick = False


    #Update 1.31
    if not hasattr(renpy.store,'cat_ears_potion_return') or reset_persistants:

        $ cat_ears_potion_return = False


    ### ADD MORE HERMIONE PERSISTANTS HERE. ADD "or reset_persistants" at the end so they will reset when creating a new game.

    return
