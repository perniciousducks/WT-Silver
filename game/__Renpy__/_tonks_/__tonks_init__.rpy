default tonks_xpos      = 600
default tonks_ypos      = 0
default tonks_zorder    = 5
default tonks_flip      = 1
default use_tonks_head  = False
default tonks_animation = None

default tonks_haircolor = [[243, 158, 189, 255]]

# Chibi
default ton_chibi_xpos      = 500
default ton_chibi_ypos      = 250
default ton_chibi_flip      = 1
default ton_chibi_zorder    = 3
default ton_chibi_animation = None
default ton_chibi_status    = ""

default ton_chibi_stand = "ch_ton blink"
default ton_chibi_shoes = "characters/tonks/chibis/nt_walk_01_shoes.png"

default ton_chibi_walk       = "ch_ton walk"
default ton_chibi_walk_shoes = "ch_ton walk_shoes"

default ton_chibi_top    = "characters/tonks/chibis/nt_top.png"
default ton_chibi_bottom = "characters/tonks/chibis/nt_trousers.png"
default ton_chibi_robe   = "blank"
default ton_chibi_gloves = "blank" # blank is the new defined image, makes our lives easier
default ton_chibi_fix    = "blank"

default ton_cloth_pile = False
default ton_pile_xpos  = 440 # Right side of desk.
default ton_pile_ypos  = 425 # Bit below feet level.

# Stats
default ton_tier           = 1
default ton_friendship     = 0 #Max is 100.
default ton_support        = 0
default ton_reputation     = 0
default ton_clothing_level = 100

# Flags
default tonks_busy              = False
default tonks_unlocked          = False
default tonks_favors_unlocked   = False
default tonks_requests_unlocked = False
default tonks_shaming_unlocked  = False
default tonks_wardrobe_unlocked = False
default chitchated_with_tonks   = False
default tonks_strip_happened    = False #Tonks random clothing event.

default gave_tonks_gift = False
default tonks_mail_list = []
default ton_seen_lun_sex = False

# Names
default tonks_name       = "Tonks"
default ton_genie_name   = "Professor"
default ton_astoria_name = "Cutie"

# Stat Screen
default ton_clothing_upgrades     = 0
default ton_astoria_date_counter  = 0
default ton_hermione_date_counter = 0

default ton_level_up = None
default tonks_shared = False

# Hangout Events

default nt_he_counter = 0

default nt_he_drink = event_class(
    title = "Tonks Firewhisky", start_label = "tonks_hangout",
    events = [
        [
            ["nt_he_wine_intro"],
            ["nt_he_firewhisky_intro"],
            ["nt_he_firewhisky_E1"],
            ["nt_he_firewhisky_E2"],
            ["nt_he_firewhisky_E3"],
            ["nt_he_firewhisky_E4"]
        ]
    ],
    iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

default nt_he_story = event_class(
    title = "Tonks Stories", start_label = "tonks_hangout",
    events = [
        [
            ["nt_he_story_intro_E1"], # Intro
            ["nt_he_story_intro_E2"], # Moody
            ["nt_he_story_intro_E3"], # Brooms and flying carpets
            ["nt_he_story_intro_E4"], # Turning water into wine
            ["nt_he_story_intro_E5"], # Lots of paperwork
            ["nt_he_story_E6"],       # Vampire story
            ["nt_he_story_intro_E7"], # Moody's teaching methods
            ["nt_he_story_E8"],       # Werewold story
            ["nt_he_story_intro_E9"], # Illegal love potion
            ["nt_he_story_intro_E10"], # Dumb game mechanics
            ["nt_he_story_E11"],      # Metamorphmagi
            ["nt_he_story_E12"]       # Invisible clothing charm
        ]
    ],
    iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

# Public requests
default nt_pr_teach = event_class(
    title = "Detention with Tonks.", start_label = "nt_pr_teach_start", start_tier = 1,
    events = [
        [
            ["nt_pr_teach_T1_E1"], # Slytherin boy
            ["nt_pr_teach_T1_E2"], # Ravenclaw boy
            ["nt_pr_teach_T1_E3"], # Potter & Weasley
            ["nt_pr_teach_T1_E4"]  # Slytherin girl
        ],
        [
            ["nt_pr_teach_T2_E1"], # Hufflepuff girl
            ["nt_pr_teach_T2_E2"], # Ravenclaw boy
            ["nt_pr_teach_T2_E3"], # Slytherin boy
            ["nt_pr_teach_T2_E4"]  # Slytherin girl
        ]
    ],
    iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

default nt_pr_grope = event_class(
    title = "Hands-on lessons!", start_label = "nt_pr_grope_start", start_tier = 2,
    events = [
        [
            ["nt_pr_grope_T1_E1"], # Slytherin boy
            ["nt_pr_grope_T1_E2"], # Ravenclaw boy
            ["nt_pr_grope_T1_E3"], # Potter & Weasley
            ["nt_pr_grope_T1_E4"]  # Slytherin girl
        ]# ,
        # [
        #     ["nt_pr_grope_T2_E1"], #
        #     ["nt_pr_grope_T2_E2"], #
        #     ["nt_pr_grope_T2_E3"], #
        #     ["nt_pr_grope_T2_E4"]  #
        # ]
    ],
    iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

default nt_pr_kiss = event_class(
    title = "Oral practice!", start_label = "nt_pr_kiss_start", start_tier = 2,
    events = [
        [
            ["nt_pr_kiss_T1_intro_E1"], # Ravenclaw boy
            ["nt_pr_kiss_T1_E2"],       #
            ["nt_pr_kiss_T1_E3"],       # Slytherin girls
            ["nt_pr_kiss_T1_E4"]        # Slytherin girl
        ]# ,
        # [
        #     ["nt_pr_kiss_T2_E1"], # Slytherin boy
        #     ["nt_pr_kiss_T2_E2"], #
        #     ["nt_pr_kiss_T2_E3"], #
        #     ["nt_pr_kiss_T2_E4"]  #
        # ]
    ],
    iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
)

# Idea for "blowjob pr" name: "Stress Mitigation."

default nt_requests_list = [
    nt_pr_teach,
    nt_pr_grope,
    nt_pr_kiss
]

label reset_tonks_progress:
    $ reset_variables(
        # Stats
        "ton_tier",
        "ton_friendship",
        "ton_support",
        "ton_reputation",
        "ton_clothing_level",

        # Flags
        "tonks_busy",
        "tonks_unlocked",
        "tonks_favors_unlocked",
        "tonks_requests_unlocked",
        "tonks_shaming_unlocked",
        "tonks_wardrobe_unlocked",
        "chitchated_with_tonks",
        "tonks_strip_happened",
        "gave_tonks_gift",
        "ton_seen_lun_sex"

        # Names
        "tonks_name",
        "ton_genie_name",
        "ton_astoria_name",

        # Stat Screen
        "ton_clothing_upgrades",
        "ton_astoria_date_counter",
        "ton_hermione_date_counter",
        "ton_level_up",
        "tonks_shared",

        # Events
        "nt_he_counter",
        "nt_he_drink",
        "nt_pr_teach",
        "nt_pr_grope",
        "nt_pr_kiss",
        "nt_requests_list"
    )
    return
