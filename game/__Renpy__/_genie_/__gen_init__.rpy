
label genie_init:


    #Genie
    if not hasattr(renpy.store,'genie_flip') or reset_persistants:
        label reset_genie_init:

        #Sprite
        $ genie_xpos = 200
        $ genie_ypos = 0
        $ genie_zorder = 4
        $ genie_flip = 1

        $ genie_base = "characters/genie/base/base.png"
        $ genie_face = "characters/genie/face/base.png"

        #Chibi
        $ genie_chibi_xpos=500
        $ genie_chibi_ypos=250
        $ genie_speed = 2.0
        $ genie_chibi_zorder = 2

        $ birthday_happened = False # Outfit "Present" wardrobe dialogue.
        $ secretly_jerking_off = False

    return
