
label genie_init:


    #Genie
    if not hasattr(renpy.store,'gen_chibi_stand') or reset_persistants:
        label reset_genie_base:

        #Sprite
        $ genie_xpos       = 200
        $ genie_ypos       = 0
        $ genie_zorder     = 4
        $ genie_flip       = 1
        $ use_genie_head   = False

        $ genie_base = "characters/genie/base/base.png"
        $ genie_face = "characters/genie/face/base.png"

        #Chibi
        $ gen_chibi_xpos   = 500
        $ gen_chibi_ypos   = 190
        $ gen_speed        = 2.0
        $ gen_chibi_zorder = 2
        $ gen_chibi_flip   = 1
        $ gen_chibi_stand  = "characters/genie/chibis/walk_01.png"
        $ gen_chibi_walk   = "genie_walk_ani"
        
        $ genie_cum_chibi_xpos = -45
        $ genie_cum_chibi_ypos = -5

        $ imagination      = 1
        $ bdsm_imagination = 1
        $ speed_writing    = 0
        $ speed_reading    = 0

        $ birthday_happened = False # Outfit "Present" wardrobe dialogue.
        $ masturbating = False

        $ genie_quid_position = "???" # For stats.

    return
