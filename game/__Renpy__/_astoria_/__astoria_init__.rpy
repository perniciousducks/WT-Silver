

label astoria_init:
    if not hasattr(renpy.store,'astoria_chibi_animation') or reset_persistants:
        $ astoria_xpos                = 300
        $ astoria_ypos                = 0
        $ astoria_zorder              = 5
        $ astoria_flip                = 1
        $ astoria_animation           = None

        #Chibi
        $ astoria_chibi_xpos          = 500
        $ astoria_chibi_ypos          = 250
        $ astoria_chibi_flip          = 1
        $ astoria_chibi_zorder        = 3
        $ astoria_chibi_animation     = None
        $ astoria_chibi_status        = ""

        $ astoria_chibi_stand         = "ch_cho blink"
        $ astoria_chibi_shoes         = "characters/cho/chibis/cc_walk_01_shoes.png"

        $ astoria_chibi_walk          = "ch_cho walk"
        $ astoria_chibi_walk_shoes    = "ch_cho walk_shoes"

        $ astoria_chibi_top           = "characters/cho/chibis/cc_cloth_shirt_r.png"
        $ astoria_chibi_bottom        = "characters/cho/chibis/cc_cloth_skirt.png"
        $ astoria_chibi_robe          = "blank"
        $ astoria_chibi_gloves        = "blank" #blank is the new defined image, makes our lives easier
        $ astoria_chibi_fix           = "blank"

    if not hasattr(renpy.store,'astoria_cloth_pile') or reset_persistants:
        $ astoria_cloth_pile = False
        $ astoria_pile_xpos = 440 # Right side of desk.
        $ astoria_pile_ypos = 425 # Bit below feet level.
    return


label astoria_progress_init:

    if not hasattr(renpy.store,'astoria_name') or reset_persistants:

        #Flags
        $ astoria_busy = False
        $ astoria_unlocked = False
        $ astoria_wardrobe_unlocked = False
        $ chitchated_with_astoria = False

        #Names
        $ astoria_name = "Miss Greengrass"
        $ ast_genie_name = "Dumby"
        $ ast_susan_name = "Cow"
        $ ast_tonks_name = "Old Hag"

        #Stats
        $ ast_spell_progress = 0 #Training times required to unlock a spell. Resets to 0 after it.
        $ ast_affection      = 0 #Affection level with Tonks.
        $ ast_mood           = 0

        #Events
        $ hermione_on_the_lookout  = False
        $ hermione_finds_astoria   = False
        $ snape_on_the_lookout     = False
        $ tonks_intro_happened     = False
        $ spells_unlocked          = False
        $ snape_gave_spellbook     = False
        $ third_curse_got_cast     = False
        $ astoria_book_intro_happened = False
        $ astoria_intro_completed  = False

        #Tonks events
        $ spells_locked = False
        $ astoria_tonks_event_in_progress = False
        $ astoria_tonks_intro_completed = False
        $ astoria_tonks_1_completed = False
        $ astoria_tonks_2_completed = False
        $ astoria_tonks_3_completed = False
        $ astoria_tonks_4_completed = False
        $ astoria_tonks_5_completed = False
        $ astoria_tonks_6_completed = False

        #Stat Screen
        $ ast_training_counter = 0

    if not hasattr(renpy.store,'gave_astoria_gift') or reset_persistants:
        $ gave_astoria_gift = False

    #Curses on Susan
    if not hasattr(renpy.store,'ag_cs_imperio_sb'):
        $ ag_cs_imperio_sb = favor_class()
    $ ag_cs_imperio_sb.title   = "Imperio on Susan"
    $ ag_cs_imperio_sb.start_label = "ag_cs_imperio_sb"

    $ ag_susan_spells_list = [
        ag_cs_imperio_sb
        ]

    #Curses on Hermione
    if not hasattr(renpy.store,'ag_cs_imperio_hg'):
        $ ag_cs_imperio_hg = favor_class()
    $ ag_cs_imperio_hg.title   = "Imperio on Hermione"
    $ ag_cs_imperio_hg.start_label = "ag_cs_imperio_hg"

    $ ag_hermione_spells_list = [
        ]

    #Curses on Tonks
    if not hasattr(renpy.store,'ag_cs_crucio_nt'):
        $ ag_cs_crucio_nt = favor_class()
    $ ag_cs_crucio_nt.title   = "Crucio on Tonks"
    $ ag_cs_crucio_nt.start_label = "ag_cs_crucio_nt"

    $ ag_tonks_spells_list = [
        ]

    return
