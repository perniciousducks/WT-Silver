

label cho_init:

    if not hasattr(renpy.store,'cho_class') or reset_persistants:

        $ cho_xpos                = 300
        $ cho_ypos                = 0
        $ cho_zorder              = 5
        $ cho_flip                = 1

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

        #Stats
        $ cho_whoring = 0
        $ cho_mood = 0

        #Flags
        $ cho_busy = False
        $ days_since_cho = 0
        $ cho_known = False
        $ cho_unlocked = False
        $ cho_wardrobe_unlocked = False

        $ chof2_first = True

        #Names
        $ cho_genie_name = "Professor"
        $ cho_name = "Cho"

        #Quidditch
        $ cho_quidd = False
        $ days_since_quidd = 0
        $ cho_quidd_points = 0

        $ first_cho_favor_done = False

    if not hasattr(renpy.store,'gave_cho_gift') or reset_persistants:
        $ gave_cho_gift      = False

    return
