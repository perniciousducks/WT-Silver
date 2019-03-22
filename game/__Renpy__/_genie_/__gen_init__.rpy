
label genie_init:


    #Genie
    if not hasattr(renpy.store,'genie_chibi_stand') or reset_persistants:
        label reset_genie_base:

        #Sprite
        $ genie_xpos = 200
        $ genie_ypos = 0
        $ genie_zorder = 4
        $ genie_flip = 1
        $ use_genie_head      = False

        $ genie_base = "characters/genie/base/base.png"
        $ genie_face = "characters/genie/face/base.png"

        #Chibi
        $ genie_chibi_xpos=500
        $ genie_chibi_ypos=250
        $ genie_speed = 2.0
        $ genie_chibi_zorder = 2
        $ genie_chibi_stand = "characters/genie/chibis/walk_01.png"
        $ genie_chibi_walk = "genie_walk_ani"

        $ imagination = 1
        $ bdsm_imagination = 1
        $ speed_writing = 0
        $ speed_reading = 0

        $ birthday_happened = False # Outfit "Present" wardrobe dialogue.
        $ masturbating = False

    return
