
default astoria_xpos      = 300
default astoria_ypos      = 0
default astoria_zorder    = 5
default astoria_flip      = 1
default astoria_animation = None

# Chibi
default astoria_chibi_xpos      = 500
default astoria_chibi_ypos      = 250
default astoria_chibi_flip      = 1
default astoria_chibi_zorder    = 3
default astoria_chibi_animation = None
default astoria_chibi_status    = ""

default astoria_chibi_stand = "ch_cho blink"
default astoria_chibi_shoes = "characters/cho/chibis/cc_walk_01_shoes.png"

default astoria_chibi_walk       = "ch_cho walk"
default astoria_chibi_walk_shoes = "ch_cho walk_shoes"

default astoria_chibi_top    = "characters/cho/chibis/cc_cloth_shirt_r.png"
default astoria_chibi_bottom = "characters/cho/chibis/cc_cloth_skirt.png"
default astoria_chibi_robe   = "blank"
default astoria_chibi_gloves = "blank" # blank is the new defined image, makes our lives easier
default astoria_chibi_fix    = "blank"

default astoria_cloth_pile = False
default astoria_pile_xpos  = 440 # Right side of desk.
default astoria_pile_ypos  = 425 # Bit below feet level.

# Flags
default astoria_busy              = False
default astoria_unlocked          = False
default astoria_wardrobe_unlocked = False
default chitchated_with_astoria   = False

# Names
default astoria_name   = "Miss Greengrass"
default ast_genie_name = "Dumby"
default ast_susan_name = "Cow"
default ast_tonks_name = "Old Hag"

# Stats
default ast_spell_progress = 0 # Training times required to unlock a spell. Resets to 0 after it.
default ast_affection      = 0 # Affection level with Tonks.
default ast_mood           = 0

# Events
default hermione_on_the_lookout     = False
default hermione_finds_astoria      = False
default snape_on_the_lookout        = False
default tonks_intro_happened        = False
default spells_unlocked             = False
default snape_gave_spellbook        = False
default third_curse_got_cast        = False
default astoria_book_intro_happened = False
default astoria_intro_completed     = False

default ast_seen_lun_sex = False

# Tonks events
default spells_locked                   = False
default astoria_tonks_event_in_progress = False
default astoria_tonks_intro_completed   = False
default astoria_tonks_1_completed       = False
default astoria_tonks_2_completed       = False
default astoria_tonks_3_completed       = False
default astoria_tonks_4_completed       = False
default astoria_tonks_5_completed       = False
default astoria_tonks_6_completed       = False

# Stat Screen
default ast_training_counter = 0

default gave_astoria_gift = False

# Imperius Curse
default ag_st_imperio = event_class(
    title = "Imperio Curse Training", start_label = "ag_st_imperio", start_tier = 1,
    events = [
        [
            ["ag_st_imperio_E1"],
            ["ag_st_imperio_E2"],
            ["ag_st_imperio_E3"],
            ["ag_st_imperio_E4"],
            ["ag_st_imperio_E5"]
        ]
    ],
    icons = [None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "star_yellow"]],
    complete = False
)

default ag_se_imperio_sb = event_class(
    title = "Cast Imperio on Susan", start_label = "ag_se_imperio_sb", start_tier = 1,
    events = [
        [
            ["ag_se_imperio_sb_E1"],
            ["ag_se_imperio_sb_E2"],
            ["ag_se_imperio_sb_E3"]
        ]
    ],
    icons = [None], # If a tier doesn't need an icon replace with None
    iconset = [["star_empty", "heart_yellow"]],
    complete = True
)

default ag_spell_list = []

label update_astoria_spells:
    $ del ag_spell_list[:] # Clear list
    if ag_st_imperio.complete == False:
        $ ag_spell_list.append(ag_st_imperio)
    else:
        $ ag_spell_list.append(ag_se_imperio_sb) # Susan
    return

label reset_astoria_progress:
    #TODO Add Astoria's event class variables to the list below to reset event progress
    $ reset_variables(
        # Flags
        "astoria_busy",
        "astoria_unlocked",
        "astoria_wardrobe_unlocked",
        "chitchated_with_astoria",

        # Names
        "astoria_name",
        "ast_genie_name",
        "ast_susan_name",
        "ast_tonks_name",

        # Stats
        "ast_spell_progress",
        "ast_affection",
        "ast_mood",

        # Events
        "hermione_on_the_lookout",
        "hermione_finds_astoria",
        "snape_on_the_lookout",
        "tonks_intro_happened",
        "spells_unlocked",
        "snape_gave_spellbook",
        "third_curse_got_cast",
        "astoria_book_intro_happened",
        "astoria_intro_completed",
        "ast_seen_lun_sex",

        # Tonks events
        "spells_locked",
        "astoria_tonks_event_in_progress",
        "astoria_tonks_intro_completed",
        "astoria_tonks_1_completed",
        "astoria_tonks_2_completed",
        "astoria_tonks_3_completed",
        "astoria_tonks_4_completed",
        "astoria_tonks_5_completed",
        "astoria_tonks_6_completed",

        # Stat Screen
        "ast_training_counter",
        "gave_astoria_gift"
    )
    return
