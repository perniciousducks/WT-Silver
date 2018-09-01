
label genie_init:


    #Genie
    if not hasattr(renpy.store,'genie_xpos') or reset_persistants:
        $ genie_xpos = 60
        $ genie_ypos = 0
        $ genie_zorder = 4

        #$ genie_head_xpos = 60
        #$ genie_head_ypos = 0
        #$ genie_head_zorder = 8

        $ genie_chibi_xpos=500
        $ genie_chibi_ypos=250
        $ genie_speed = 2.0
        $ genie_chibi_zorder = 2

    if not hasattr(renpy.store,'birthday_happened') or reset_persistants:
        $ secretly_jerking_off = False
        $ birthday_happened = False # Outfit "Present" wardrobe dialogue.

    return
