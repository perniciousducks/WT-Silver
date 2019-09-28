
default astoria_xpos      = 300
default astoria_ypos      = 0
default astoria_zorder    = 5
default astoria_flip      = 1
default astoria_animation = None
default use_astoria_head  = False

# Chibi
default ast_chibi_xpos      = 500
default ast_chibi_ypos      = 250
default ast_chibi_flip      = 1
default ast_chibi_zorder    = 3
default ast_chibi_animation = None
default ast_chibi_status    = ""

default ast_chibi_stand = "ch_ast blink"
default ast_chibi_shoes = "characters/astoria/chibis/ag_walk_01_shoes.png"

default ast_chibi_walk       = "ch_ast walk"
default ast_chibi_walk_shoes = "ch_ast walk_shoes"

default ast_chibi_top    = "characters/astoria/chibis/ag_top.png"
default ast_chibi_bottom = "characters/astoria/chibis/ag_skirt.png"
default ast_chibi_robe   = "blank"
default ast_chibi_gloves = "blank" # blank is the new defined image, makes our lives easier
default ast_chibi_fix    = "blank"

default ast_cloth_pile = False
default ast_pile_xpos  = 440 # Right side of desk.
default ast_pile_ypos  = 425 # Bit below feet level.

# Flags
default astoria_busy              = False
default astoria_unlocked          = False
default astoria_wardrobe_unlocked = False
default chitchated_with_astoria   = False

# Names
default astoria_name   = "Astoria"
default ast_genie_name = "Sir"
default ast_susan_name = "Cow"
default ast_tonks_name = "Old Hag"

# Stats
default ast_spell_progress = 0 # Training times required to unlock a spell. Resets to 0 after it.
default ast_affection      = 0 # Affection level with Tonks.
default ast_mood           = 0

# Events
default snape_gave_spellbook        = False

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
    title = "Imperio Training", start_label = "ag_st_imperio", start_tier = 1,
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
        "snape_gave_spellbook",
        "ast_seen_lun_sex",

        # Event objects
        "ag_st_imperio",
        "ag_se_imperio_sb",
        "ag_spell_list",

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
