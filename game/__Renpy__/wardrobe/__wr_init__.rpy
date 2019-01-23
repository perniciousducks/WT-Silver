

label wardrobe_init:

    if not hasattr(renpy.store,'wardrobe_music') or reset_persistants:

        $ hide_transitions = False
        $ active_girl = "hermione"

        $ wardrobe_page = 0
        $ wardrobe_page_choice = 0
        $ wardrobe_toggle_page = 0
        $ wardrobe_chitchat_active = True

        $ play_wardrobe_music = False
        $ wardrobe_music_active = False
        $ add_wardrobe_sound = False

        $ wr_her_action = "none"

        $ wardrobe_color_update = True
        $ wardrobe_color = "base"

        $ wardrobe_gift_item = 0
        $ wardrobe_costume_selection = 0
        $ wardrobe_uniform_selection = ""

        #Wardrobe Categories
        $ wardrobe_head_category = 0
        $ wardrobe_tops_category = 0
        $ wardrobe_bottoms_category = 0
        $ wardrobe_stockings_category = 0
        $ wardrobe_accessories_category = 0
        $ wardrobe_underwear_category = 0
        $ wardrobe_outfits_category = 0
        $ wardrobe_gifts_category = 0

        #Wardrobe Color Select
        $ wr_background_color            = ["base","red","green","blue"]
        $ wardrobe_hair_style            = "curly"
        $ wardrobe_head_color            = "base"
        $ wardrobe_uniform_color         = "base" #can be: base, red, greed, blue, or yellow.
        $ wardrobe_tops_color            = "base"
        $ wardrobe_bottoms_color         = "base"
        $ wardrobe_other_clothings_color = "base"
        $ wardrobe_accessories_color     = "base"
        $ wardrobe_underwear_color       = "base"
        $ wardrobe_outfits_color         = "base"

        #Wardrobe Icons
        $ icon_xpos_offset = 0
        $ icon_ypos_offset = 0

        $ wardrobe_load_custom_outfit = True

    return
