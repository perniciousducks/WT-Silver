

label update_outfit_layers:

    ### OUTFITS ###

    #Hermione Outfits.
    $ hg_outfit_maid_ITEM.outfit_layers = ["maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"]
    $ hg_outfit_maid_ITEM.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_maid_ITEM.hair_layer = "updo"
    $ hg_outfit_maid_ITEM.top_layers = "maid_hat"

    $ hg_outfit_pirate_ITEM.outfit_layers = ["pirate_legs.png","pirate_pants.png","pirate_top.png"]
    $ hg_outfit_pirate_ITEM.breast_layer = "breasts_nipfix"

    $ hg_outfit_christmas_ITEM.outfit_layers = ["christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"]
    $ hg_outfit_christmas_ITEM.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_christmas_ITEM.top_layers = "antlers"

    $ hg_outfit_present_ITEM.outfit_layers = ["present_pant.png","present_top.png"]
    $ hg_outfit_present_ITEM.breast_layer = "breasts_nipfix"

    $ hg_outfit_japan_ITEM.outfit_layers = ["japan_pant.png","japan_top.png"]
    $ hg_outfit_japan_ITEM.breast_layer = "breasts_normal_pressed"

    $ hg_outfit_witch_ITEM.outfit_layers = ["witch_stockings.png","witch_top.png","witch_cloak.png"]
    $ hg_outfit_witch_ITEM.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_witch_ITEM.top_layers = "witch_hat"

    $ hg_outfit_egypt_ITEM.outfit_layers = ["egyptian_top.png","egyptian_bottom.png","egyptian_shackles.png"]
    $ hg_outfit_egypt_ITEM.breast_layer = "breasts_normal"


    #Hermione Costumes.
    $ hg_costume_power_girl_ITEM.outfit_layers = ["power_cape.png","power_top.png","power_cape_top.png","power_gloves.png","power_belt.png"]
    $ hg_costume_power_girl_ITEM.breast_layer = "breasts_normal"
    $ hg_costume_power_girl_ITEM.hair_layer = "power_girl"

    $ hg_costume_ms_marvel_ITEM.outfit_layers = ["marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"]
    $ hg_costume_ms_marvel_ITEM.breast_layer = "breasts_normal"

    $ hg_costume_harley_quinn_ITEM.outfit_layers = ["harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"]
    $ hg_costume_harley_quinn_ITEM.breast_layer = "breasts_normal"
    $ hg_costume_harley_quinn_ITEM.hair_layer = "harley"

    $ hg_costume_lara_croft_ITEM.outfit_layers = ["lara_pants.png","lara_top.png","lara_gloves.png"]
    $ hg_costume_lara_croft_ITEM.breast_layer = "breasts_normal"

    $ hg_costume_tifa_ITEM.outfit_layers = ["tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"]
    $ hg_costume_tifa_ITEM.breast_layer = "breasts_normal"
    $ hg_costume_tifa_ITEM.hair_layer = "tifa"

    $ hg_costume_elizabeth_ITEM.outfit_layers = ["bio_skirt.png","bio_chocker.png","bio_corset.png","bio_jacket.png"]
    $ hg_costume_elizabeth_ITEM.breast_layer = "breasts_normal_pressed"
    $ hg_costume_elizabeth_ITEM.hair_layer = "bobcut"

    $ hg_costume_yennefer_ITEM.outfit_layers = ["yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"]
    $ hg_costume_yennefer_ITEM.breast_layer = "breasts_normal"


    #Hermione Dresses.
    $ hg_dress_yule_ball_ITEM.outfit_layers = ["ball_dress_skirt.png","ball_dress_top.png"]
    $ hg_dress_yule_ball_ITEM.breast_layer = "breasts_nipfix"
    $ hg_dress_yule_ball_ITEM.hair_layer = "updo"
    $ hg_dress_yule_ball_ITEM.top_layers = "tiara"

    $ hg_dress_dancer_ITEM.outfit_layers = ["heart_legs.png","heart_top.png","heart_collar.png"]
    $ hg_dress_dancer_ITEM.breast_layer = "breasts_normal"


    # Luna Outfits
    $ ll_pyjama_ITEM.outfit_layers = ["pants_pyjama.png","top_pyjama.png"]

    # Astoria Outfits
    $ ag_boss_uniform_ITEM.outfit_layers = ["uniform_pants.png","uniform_top.png"]
    $ ag_boss_uniform_ITEM.hair_layer = "pigtails"
    $ ag_boss_uniform_ITEM.top_layers = "boss_hat"

    $ ag_costume_lazy_town_ITEM.outfit_layers = ["lazy_tights.png","lazy_dress.png","lazy_bracelet.png"]
    $ ag_costume_lazy_town_ITEM.hair_layer = "stephanie"

    $ ag_costume_lazy_town_short_ITEM.outfit_layers = ["lazy_tights.png","lazy_dress_short.png","lazy_bracelet.png"]
    $ ag_costume_lazy_town_short_ITEM.hair_layer = "stephanie"

    $ ag_dress_yule_ball_ITEM.outfit_layers = ["ball_dress.png"]


    # Susan Outfits


    # Cho Outfits
    $ cc_outfit_quidditch_ITEM.outfit_layers = []
    call update_cho_quidditch_outfit #Adds outfit layers.

    $ cc_dress_red_ITEM.outfit_layers = ["traditional_dress_red.png"]
    $ cc_dress_silver_ITEM.outfit_layers = ["traditional_dress_silver.png"]
    $ cc_dress_black_ITEM.outfit_layers = ["traditional_dress_black.png"]

    $ cc_outfit_sailor_white_ITEM.outfit_layers      = ["../underwear/yellow/panties_bikini_2.png","../stockings/stockings_sailor_1.png","../tops/base/top_sailor_1.png","../bottoms/blue/skirt_sailor.png","../../body/arms/arm_down_l_overlay.png"]
    $ cc_outfit_sailor_white_ITEM.top_layers         = "bow_sailor_yellow"

    $ cc_outfit_sailor_black_ITEM.outfit_layers      = ["../underwear/red/panties_bikini_2.png","../stockings/stockings_sailor_2.png","../tops/base/top_sailor_2.png","../bottoms/dark_blue/skirt_sailor.png","../../body/arms/arm_down_l_overlay.png"]
    $ cc_outfit_sailor_black_ITEM.top_layers         = "bow_sailor_red"

    $ cc_costume_misty_ITEM.outfit_layers      = ["../tops/base/top_shirt_1.png","../bottoms/base/pants_short_1.png","../../body/arms/arm_down_l_overlay.png","../../accessories/body_accs/suspenders_1.png"]


    ### Event Outfits ###

    #Does not have a store item!
    #They don't get added to the outfits list.
    #They don't require 'name', 'cost', 'image', 'description',...


    #Cheerleader outfit for events. Doesn't get added as a wardrobe outfit.
    $ hg_cheer_g_ITEM.outfit_layers = ["../tops/base/top_cheer_g.png","../bottoms/base/skirt_cheer_g.png"]
    $ hg_cheer_s_ITEM.outfit_layers = ["../tops/base/top_cheer_s.png","../bottoms/base/skirt_cheer_s.png"]
    $ hg_cheer_r_ITEM.outfit_layers = ["../tops/base/top_cheer_r.png","../bottoms/base/skirt_cheer_r.png"]
    $ hg_cheer_h_ITEM.outfit_layers = ["../tops/base/top_cheer_h.png","../bottoms/base/skirt_cheer_h.png"]
    $ hg_cheer_g_sexy_ITEM.outfit_layers = ["../tops/base/top_cheer_sexy_g.png","../bottoms/base/skirt_cheer_sexy_g.png"]
    $ hg_cheer_s_sexy_ITEM.outfit_layers = ["../tops/base/top_cheer_sexy_s.png","../bottoms/base/skirt_cheer_sexy_s.png"]
    $ hg_cheer_r_sexy_ITEM.outfit_layers = ["../tops/base/top_cheer_sexy_r.png","../bottoms/base/skirt_cheer_sexy_r.png"]
    $ hg_cheer_h_sexy_ITEM.outfit_layers = ["../tops/base/top_cheer_sexy_h.png","../bottoms/base/skirt_cheer_sexy_h.png"]

    #Hermione Event Outfits
    if not hasattr(renpy.store,'hg_standart_school_ITEM'):
        $ hg_standart_school_ITEM = outfit_class()
    $ hg_standart_school_ITEM.id = "hg_standart_school"
    $ hg_standart_school_ITEM.outfit_layers = ["../bottoms/base/skirt_2.png", "../tops/base/top_1_g.png"]
    $ hg_standart_school_ITEM.breast_layer = "breasts_nipfix"

    if not hasattr(renpy.store,'hg_standart_school_noshirt_ITEM'):
        $ hg_standart_school_noshirt_ITEM = outfit_class()
    $ hg_standart_school_noshirt_ITEM.id = "hg_standart_school_noshirt"
    $ hg_standart_school_noshirt_ITEM.outfit_layers = ["../bottoms/base/skirt_2.png", "../underwear/base/bra_base.png"]
    $ hg_standart_school_noshirt_ITEM.breast_layer = "breasts_nipfix"



    return
