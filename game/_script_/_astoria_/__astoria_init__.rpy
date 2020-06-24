# Main
default astoria_xpos = 300
default astoria_ypos = 0
default astoria_zorder = 15
default astoria_flip = 1
default astoria_animation = None
default use_astoria_head  = False

# Flags
default astoria_busy              = False
default astoria_unlocked          = False
default astoria_wardrobe_unlocked = False
default chitchated_with_astoria   = False
default astoria_outfits_schedule = True

# Names
default astoria_name   = "Astoria"
default ast_genie_name = "Sir"
default ast_susan_name = "Cow"
default ast_tonks_name = "Old Hag"

# Stats
default ast_spell_progress = 0 # Training times required to unlock a spell. Resets to 0 after it.
default ast_whoring = 0 # Affection level
default ast_mood = 0

# Events
default snape_gave_spellbook = False
default ast_seen_lun_sex = False
default astoria_chitchats_seen = set()

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
    iconset = [["heart_empty", "heart_red"]],
    complete = True
)

default ag_spell_list = []

label update_astoria_spells:
    $ del ag_spell_list[:] # Clear list
    if not ag_st_imperio.is_complete():
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
        "ast_whoring",
        "ast_mood",

        # Events
        "snape_gave_spellbook",
        "ast_seen_lun_sex",
        "astoria_chitchats_seen",

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
