
label genie_init:


    #Genie
    if not hasattr(renpy.store,'genie_xpos') or reset_persistants:
        label reset_genie_init:

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

        $ genie_sprite_base = "characters/genie/base_1.png"
        $ genie_sprite_exp = "characters/genie/exp_1.png"
        $ genie_sprite_xpos = 200
        $ genie_sprite_ypos = 0
        $ genie_sprite_flip = 1

        $ birthday_happened = False # Outfit "Present" wardrobe dialogue.
        $ secretly_jerking_off = False

    return
