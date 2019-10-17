default use_cho_head = False

default cho_xpos                = 300
default cho_ypos                = 0
default cho_zorder              = 5
default cho_flip                = 1
default cho_animation           = None

#Chibi
default cho_chibi_xpos          = 500
default cho_chibi_ypos          = 250
default cho_chibi_flip          = 1
default cho_chibi_zorder        = 3
default cho_chibi_animation     = None
default cho_chibi_status        = ""

default cho_chibi_stand         = "ch_cho blink"
default cho_chibi_shoes         = "characters/cho/chibis/cc_walk_01_shoes.png"

default cho_chibi_walk          = "ch_cho walk"
default cho_chibi_walk_shoes    = "ch_cho walk_shoes"

default cho_chibi_top           = "characters/cho/chibis/cc_cloth_shirt_r.png"
default cho_chibi_bottom        = "characters/cho/chibis/cc_cloth_skirt.png"
default cho_chibi_robe          = "blank"
default cho_chibi_gloves        = "blank" #blank is the new defined image, makes our lives easier
default cho_chibi_fix           = "blank"

default cho_cloth_pile = False
default cho_pile_xpos = 440 # Right side of desk.
default cho_pile_ypos = 425 # Bit below feet level.

# Stats
default cho_tier                = 1
default cho_whoring             = 0
default cho_reputation          = 0
default cho_mood                = 0
default cho_jerk_off_counter    = 0

# Flags
default cho_known               = False
default cho_unlocked            = False
default cho_training_unlocked   = False
default cho_favors_unlocked     = False
default cho_requests_unlocked   = False
default cho_shaming_unlocked    = False
default cho_strip_complete      = False
default cho_wardrobe_unlocked   = False
default cho_busy                = False
default cho_chatted             = False
default has_cho_panties         = False
default cho_panties_soaked      = False

# Intro
default jerked_off_during_cho_intro = False

# Quidditch Training
default cho_training_state      = "quiz_start"
default quid_hint_icon          = "" # Icon: "{image=interface/check_True.png} "
default cho_quiz_complete       = False
default snape_quid_help         = False # True after Failing the Quiz.
default lock_cho_training       = False
default lock_cho_practice       = False
default quidditch_commentator   = None
default quidditch_position      = "front"

# Quidditch Outfit
default quid_outfit_intro       = []
default cho_quidditch_top       = "sweater" # For testing.
default cho_quidditch_bottom    = "pants_long" # For testing.
default cho_quidditch_coat      = True # For testing.
default cho_quidditch_gloves    = True # For testing.

# Quidditch Matches
default quidditch_match_in_progress = False
default huffl_match_counter   = 0

default huffl_matches_won     = 0 # Goes up to 2

default start_match           = 0 # No match will trigger at 0
default main_match_1_stage    = "none"
default main_match_2_stage    = "none"
default main_match_3_seen     = "none"

default hufflepuff_match      = ""
default slytherin_match       = ""
default gryffindor_match      = ""

default cho_content_complete  = False

# Names
default cho_genie_name = "Sir"
default cho_name = "Cho"

default gave_cho_gift      = False

# Cho Favors
# cc_pf = Cho Chang Personal Favor
default cc_pf_talk = event_class(title = "Talk to me!", start_label = "cc_pf_talk", start_tier = 1,
    events = [
        [
            ["cc_pf_talk_T1_intro_E1"],
            ["cc_pf_talk_T1_intro_E2"],
            ["cc_pf_talk_T1_E3"]
        ],
        [
            ["cc_pf_talk_T2_intro_E1"],
            ["cc_pf_talk_T2_intro_E2"],
            ["cc_pf_talk_T2_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_yellow"], ["heart_empty", "heart_green"]]
)

default cc_pf_strip = event_class(title = "Inspect her body!", start_label = "cc_pf_strip", start_tier = 2,
    events = [
        [
            ["cc_pf_strip_T1_intro_E1"],
            ["cc_pf_strip_T1_intro_E2"],
            ["cc_pf_strip_T1_intro_E3"], ["cc_pf_strip_T1_E3"]
        ]
    ],
    iconset = [["heart_empty", "heart_green"]]
)

default cc_favor_list = [cc_pf_talk, cc_pf_strip]

# Public requests
# cc_pr = Cho Chang Public Request
default cc_pr_manipulate = event_class(title = "Manipulate the enemy!", start_label = "cc_pr_manipulate_start",
    events = [
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
    icons = ["huff", "slyt"], #if a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

default cc_requests_list = [cc_pr_manipulate]

label reset_cho_progress:
    $ reset_variables(
        # Stats
        "cho_tier",
        "cho_whoring",
        "cho_reputation",
        "cho_mood",
        "cho_jerk_off_counter",

        # Flags
        "cho_known",
        "cho_unlocked",
        "cho_training_unlocked",
        "cho_favors_unlocked",
        "cho_requests_unlocked",
        "cho_shaming_unlocked",
        "cho_strip_complete",
        "cho_wardrobe_unlocked",
        "cho_busy",
        "cho_chatted",
        "has_cho_panties",
        "cho_panties_soaked",

        # Intro
        "jerked_off_during_cho_intro",

        # Quidditch Training
        "cho_training_state",
        "quid_hint_icon",
        "cho_quiz_complete",
        "snape_quid_help",
        "lock_cho_training",
        "lock_cho_practice",
        "quidditch_commentator",
        "quidditch_position",

        # Quidditch Outfit
        "quid_outfit_intro",
        "cho_quidditch_top",
        "cho_quidditch_bottom",
        "cho_quidditch_coat",
        "cho_quidditch_gloves",

        # Quidditch Matches
        "quidditch_match_in_progress",
        "huffl_match_counter",
        "huffl_matches_won",
        "start_match",
        "main_match_1_stage",
        "main_match_2_stage",
        "main_match_3_seen",
        "hufflepuff_match",
        "slytherin_match",
        "gryffindor_match",
        "cho_content_complete",

        # Event objects
        "cc_pf_talk",
        "cc_pf_strip",
        "cc_favor_list",

        "cc_pr_manipulate",
        "cc_requests_list",

        # Names
        "cho_genie_name",
        "cho_name",
        "gave_cho_gift"
    )
    return
