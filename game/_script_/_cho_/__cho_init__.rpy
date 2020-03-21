# Main
default cho_xpos = 300
default cho_ypos = 0
default cho_zorder = 15
default cho_flip = 1
default cho_animation = None
default use_cho_head = False

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
default cho_outfits_schedule = True

# Intro
default jerked_off_during_cho_intro = False

# Quidditch Outfit
default quid_outfit_intro       = []

# Quidditch Matches
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
    iconset = [["heart_empty", "heart_blue"], ["heart_empty", "heart_blue"]]
)

default cc_pf_strip = event_class(title = "Inspect her body!", start_label = "cc_pf_strip", start_tier = 2,
    events = [
        [
            ["cc_pf_strip_T1_intro_E1"],
            ["cc_pf_strip_T1_intro_E2"],
            ["cc_pf_strip_T1_intro_E3"], ["cc_pf_strip_T1_E3"]
        ]
    ],
    iconset = [["heart_blue", "heart_blue"]]
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

        # Quidditch Outfit
        "quid_outfit_intro",

        # Quidditch Matches
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
