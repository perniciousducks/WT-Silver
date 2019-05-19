default use_cho_head = False # This has to be left outside of any label, default doesn't overwrite the save variables but if the variable doesn't exist it sets it to = Value, in this case its False

label cho_init:

    if not hasattr(renpy.store,'cho_chibi_animation') or reset_persistants:

        $ cho_xpos                = 300
        $ cho_ypos                = 0
        $ cho_zorder              = 5
        $ cho_flip                = 1
        $ cho_animation           = None

        #Chibi
        $ cho_chibi_xpos          = 500
        $ cho_chibi_ypos          = 250
        $ cho_chibi_flip          = 1
        $ cho_chibi_zorder        = 3
        $ cho_chibi_animation     = None
        $ cho_chibi_status        = ""

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
        $ cho_tier                = 1
        $ cho_whoring             = 0
        $ cho_reputation          = 0
        $ cho_mood                = 0
        $ cho_jerk_off_counter    = 0

        # Flags
        $ cho_known               = False
        $ cho_unlocked            = False
        $ cho_training_unlocked   = False
        $ cho_favors_unlocked     = False
        $ cho_requests_unlocked   = False
        $ cho_shaming_unlocked    = False
        $ cho_strip_complete      = False
        $ cho_wardrobe_unlocked   = False
        $ cho_busy                = False
        $ cho_chatted             = False
        $ has_cho_panties         = False
        $ cho_panties_soaked      = False


        # Intro
        $ cho_intro_state         = "event_1"
        $ jerked_off_during_cho_intro = False
        $ cho_plan                = [] # Talk with Snape about Cho.

        # Quidditch Training
        $ cho_training_state      = "quiz_start"
        $ quid_hint_icon          = "" # Icon: "{image=interface/check_True.png} "
        $ cho_quiz_complete       = False
        $ snape_quid_help         = False # True after Failing the Quiz.
        $ lock_cho_training       = False
        $ lock_cho_practice       = False
        $ quidditch_commentator   = "none"
        $ quidditch_position      = "front"

        # Quidditch Outfit
        $ quid_outfit_intro       = []
        $ cho_quidditch_top       = "sweater" # For testing.
        $ cho_quidditch_bottom    = "pants_long" # For testing.
        $ cho_quidditch_coat      = True # For testing.
        $ cho_quidditch_gloves    = True # For testing.

        # Quidditch Matches
        $ quidditch_match_in_progress = False
        $ huffl_match_counter   = 0
        $ gryff_match_counter   = 0
        $ slyth_match_counter   = 0

        $ huffl_matches_won     = 0 # Goes up to 2
        $ gryff_matches_won     = 0 # Goes up to 2
        $ slyth_matches_won     = 0 # Goes up to 2

        $ start_match           = 0 # No match will trigger at 0
        $ main_match_1_stage    = "none"
        $ main_match_2_stage    = "none"
        $ main_match_3_seen     = "none"

        $ cho_content_complete  = False

        # Names
        $ cho_genie_name = "Sir"
        $ cho_name = "Cho"


        $ gave_cho_gift      = False


    ### Cho Favors ###

    # cc = Cho Chang.
    # pf = Personal Favor.
    # pr = Public Requests.

    if not hasattr(renpy.store,'cc_pf_talk'):
        $ cc_pf_talk    = favor_class(title = "Talk to me!",       tier = 1, start_label = "cc_pf_talk")
        $ cc_pf_strip   = favor_class(title = "Inspect her body!", tier = 2, start_label = "cc_pf_strip")
        $ cc_pf_blowjob = favor_class(title = "Suck it!",          tier = 3, start_label = "cc_pf_blowjob")
        $ cc_pf_sex     = favor_class(title = "Let's have sex!",   tier = 4, start_label = "cc_pf_sex")

    $ cc_favor_list = [
        cc_pf_talk,
        cc_pf_strip,
        cc_pf_blowjob,
        cc_pf_sex
        ]

    if not hasattr(renpy.store,'cc_pr_flirt'): # Not in use
        $ cc_pr_flirt   = event_class(title = "Get Flirty!", start_label = "cc_pr_flirt_start", events = [
            [
            ["cc_pr_flirt_T1_intro"], ["cc_pr_flirt_T1_E1"],
            ["cc_pr_flirt_T1_E2"],
            ["cc_pr_flirt_T1_E3"]
            ],

            [
            ["cc_pr_flirt_T2_intro"], ["cc_pr_flirt_T2_E1"],
            ["cc_pr_flirt_T2_E2"],
            ["cc_pr_flirt_T2_E3"]
            ]

            ],
            icons = ["interface/huff.png", "interface/slyt.png"]
            )

    if not hasattr(renpy.store,'cc_pr_manipulate'):
        $ cc_pr_manipulate   = event_class(title = "Manipulate the enemy!", start_label = "cc_pr_manipulate_start", events = [
            [
            ["cc_pr_manipulate_T1_intro_E1"], ["cc_pr_manipulate_T1_E1"],
            ["cc_pr_manipulate_T1_E2"],
            ["cc_pr_manipulate_T1_E3"]
            ],

            [
            ["cc_pr_manipulate_T2_intro_E1"], ["cc_pr_manipulate_T2_E1"],
            ["cc_pr_manipulate_T2_intro_E2"],
            ["cc_pr_manipulate_T2_intro_E3"], ["cc_pr_manipulate_T2_E3"]
            ]

            ],
            icons = ["interface/huff.png", "interface/slyt.png"] #if a tier doesn't need an icon replace with None
            )

    $ cc_requests_list = [
        cc_pr_manipulate
        ]

    return
