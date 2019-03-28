

label cho_init:

    if not hasattr(renpy.store,'cho_class') or reset_persistants:

        $ cho_xpos                = 300
        $ cho_ypos                = 0
        $ cho_zorder              = 5
        $ cho_flip                = 1
        
        default use_cho_head = False

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
    return

label cho_progress_init:
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
        $ cho_hermione_talk_intro = False
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
        $ main_match_1_stage = "none"
        $ main_match_2_stage = "none"
        $ main_match_3_seen = "none"

        $ cho_content_complete = False

        # Names
        $ cho_genie_name = "Sir"
        $ cho_name = "Cho"

        #Quidditch

        $ first_cho_favor_done = False

        $ cho_quiz_first_attempt = True
        $ cho_quiz2_first_attempt = True
        $ cho_quiz_failed = False
        $ cho_quiz_assed = False

    if not hasattr(renpy.store,'gave_cho_gift') or reset_persistants:
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
