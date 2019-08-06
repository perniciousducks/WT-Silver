
# Todo : Change all ".purchase" from the outfit_OBJ to ".unlocked"
label update_wr_lists:
    call update_wr_color_list
    call update_wr_head_list
    call update_wr_tops_list
    call update_wr_bottoms_list
    call update_wr_other_clothings_list
    call update_wr_miscellaneous_list
    call update_wr_underwear_list
    call update_wr_outfits_list
    return


### Color List ###
label update_wr_color_list:

    #Hair Color
    $ wr_haircolor = []

    if active_girl in ["hermione"]:

        $ wr_haircolor.append("brown")
        if yellow_dye_ITEM.unlocked:
            $ wr_haircolor.append("blonde")
        if red_dye_ITEM.unlocked:
            $ wr_haircolor.append("red")
        if crimson_dye_ITEM.unlocked:
            $ wr_haircolor.append("crimson")
        if black_dye_ITEM.unlocked:
            $ wr_haircolor.append("black")

        if dark_green_dye_ITEM.unlocked:
            $ wr_haircolor.append("green")
        if dark_blue_dye_ITEM.unlocked:
            $ wr_haircolor.append("blue")
        if purple_dye_ITEM.unlocked:
            $ wr_haircolor.append("purple")
        if pink_dye_ITEM.unlocked:
            $ wr_haircolor.append("pink")
        if gray_dye_ITEM.unlocked:
            $ wr_haircolor.append("gray")

    if active_girl in ["tonks"]:
        $ wr_haircolor.append("pink")
        $ wr_haircolor.append("blonde")
        $ wr_haircolor.append("red")
        $ wr_haircolor.append("crimson")
        $ wr_haircolor.append("black")
        $ wr_haircolor.append("green")
        $ wr_haircolor.append("blue")
        $ wr_haircolor.append("purple")
        $ wr_haircolor.append("brown")
        $ wr_haircolor.append("gray")


    #House Color
    $ wr_housecolor = []

    if active_girl == "hermione":
        if blue_dye_ITEM.unlocked:
            $ wr_housecolor.append("blue")
        if green_dye_ITEM.unlocked:
            $ wr_housecolor.append("green")
        if red_dye_ITEM.unlocked:
            $ wr_housecolor.append("red")
        if yellow_dye_ITEM.unlocked:
            $ wr_housecolor.append("yellow")


    #Cloth Color
    $ wr_clothcolor = []

    if active_girl in ["hermione","luna","tonks","cho"]:
        if dark_blue_dye_ITEM.unlocked:
            $ wr_clothcolor.append("dark_blue")
        if dark_green_dye_ITEM.unlocked:
            $ wr_clothcolor.append("dark_green")
        if crimson_dye_ITEM.unlocked:
            $ wr_clothcolor.append("crimson")
        if orange_dye_ITEM.unlocked:
            $ wr_clothcolor.append("orange")
        if purple_dye_ITEM.unlocked:
            $ wr_clothcolor.append("purple")
        if brown_dye_ITEM.unlocked:
            $ wr_clothcolor.append("brown")
        if black_dye_ITEM.unlocked:
            $ wr_clothcolor.append("black")

        if blue_dye_ITEM.unlocked:
            $ wr_clothcolor.append("blue")
        if green_dye_ITEM.unlocked:
            $ wr_clothcolor.append("green")
        if red_dye_ITEM.unlocked:
            $ wr_clothcolor.append("red")
        if yellow_dye_ITEM.unlocked:
            $ wr_clothcolor.append("yellow")
        if pink_dye_ITEM.unlocked:
            $ wr_clothcolor.append("pink")
        if gray_dye_ITEM.unlocked:
            $ wr_clothcolor.append("gray")
        if white_dye_ITEM.unlocked:
            $ wr_clothcolor.append("white")

    return


### Hair & Head Accessories List ###
label update_wr_head_list:

    $ wr_hair = []
    $ wr_makeup = []
    $ wr_glasses = []
    $ wr_ears = []
    $ wr_hats = []


    if active_girl == "hermione":

        #Hair Style
        $ wr_hair.append("curly")
        if hg_outfit_maid_ITEM.unlocked or hg_lingerie_maid_ITEM.unlocked or hg_dress_yule_ball_ITEM.unlocked: #Updo Hair from Outfits/Sets
            $ wr_hair.append("updo")
        if hg_costume_elizabeth_ITEM.unlocked: #Elizabeth Hair from Outfit.
            $ wr_hair.append("bobcut")

        #Makeup
        if lipstick_red_ITEM.unlocked:
            $ wr_makeup.append("lipstick_red")
        if lipstick_pink_ITEM.unlocked:
            $ wr_makeup.append("lipstick_pink")
        if freckles_makeup_ITEM.unlocked:
            $ wr_makeup.append("freckles")
        if fake_cum_makeup_ITEM.unlocked:
            $ wr_makeup.append("fake_cum")

        #Glasses
        if reading_glasses_ITEM.unlocked:
            $ wr_glasses.append("reading_glasses_black")
        if vintage_glasses_ITEM.unlocked:
            $ wr_glasses.append("vintage_glasses_black")

        #Ears
        if cat_ears_ITEM.unlocked:
            $ wr_ears.append("cat_ears")
        if elf_ears_ITEM.unlocked:
            $ wr_ears.append("elf_ears")

        #Hats
        if hg_witch_ITEM.unlocked:
            $ wr_hats.append("hat_witch")
        if hg_gamble_slut_ITEM.unlocked:
            $ wr_hats.append("hat_gambler")
        if hg_outfit_maid_ITEM.unlocked:
            $ wr_hats.append("hat_maid")
        if hg_dress_yule_ball_ITEM.unlocked:
            $ wr_hats.append("tiara")

    if active_girl == "luna":

        #Hair
        $ wr_hair.append("curly")
        $ wr_hair.append("playful")
        $ wr_hair.append("short")

        if luna_reverted:
            $ wr_glasses.append("spectrespecs")

        #Hats
        if ll_stewardess_ITEM.unlocked or ll_stewardess_short_ITEM.unlocked:
            $ wr_hats.append("hat_stewardess")

    if active_girl == "susan":

        $ wr_hair.append("braided")

    if active_girl == "cho":

        $ wr_hair.append("ponytail")

        $ wr_hats.append("hat_witch")
        $ wr_hats.append("snitch")
        if cc_outfit_sailor_white_ITEM.unlocked or cc_outfit_sailor_black_ITEM.unlocked:
            $ wr_hats.append("bow_sailor_blue")
            $ wr_hats.append("bow_sailor_dark_blue")
            $ wr_hats.append("bow_sailor_green")
            $ wr_hats.append("bow_sailor_red")
            $ wr_hats.append("bow_sailor_yellow")

    return


### Tops List ###
label update_wr_tops_list:

    $ wr_tops_uniform = [] #ADD school clothing and cheerleader tops,...
    $ wr_tops_cheerleader = []  #Cheerleader Tops
    $ wr_tops_normal = []  #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    $ wr_tops_wicked = []  #ADD kinky clothing items like leather, fishnet
    $ wr_tops_misc = []    #ADD Misc top items


    if active_girl == "hermione":

        #Uniform
        $ wr_tops_uniform.append("top_1_g")
        $ wr_tops_uniform.append("top_2_g")
        $ wr_tops_uniform.append("top_3_g")
        $ wr_tops_uniform.append("top_4_g")
        $ wr_tops_uniform.append("top_5_g")
        $ wr_tops_uniform.append("top_6_g")
        $ wr_tops_uniform.append("top_7_g")

        if her_reputation > 15:
            $ wr_tops_uniform.append("top_1_s")
            $ wr_tops_uniform.append("top_2_s")
            $ wr_tops_uniform.append("top_3_s")
            $ wr_tops_uniform.append("top_4_s")
            $ wr_tops_uniform.append("top_5_s")
            $ wr_tops_uniform.append("top_6_s")
            $ wr_tops_uniform.append("top_7_s")

        #Cheerleader
        if hg_cheer_g_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_g")
        if hg_cheer_s_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_s")
        if hg_cheer_r_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_r")
        if hg_cheer_h_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_h")

        if hg_cheer_g_sexy_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_g")
        if hg_cheer_s_sexy_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_s")
        if hg_cheer_r_sexy_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_r")
        if hg_cheer_h_sexy_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_h")

        #Muggle
        if hg_muggle_cold_ITEM.unlocked:
            $ wr_tops_normal.append("top_pullover_1")
        if hg_muggle_cold_sexy_ITEM.unlocked:
            $ wr_tops_normal.append("top_pullover_2")
        if hg_muggle_rainy_ITEM.unlocked:
            $ wr_tops_normal.append("top_sweater_1")
        if hg_muggle_hot_ITEM.unlocked:
            $ wr_tops_normal.append("top_frilled_1")

        #Wicked
        if hg_punk_leather_ITEM.unlocked:
            $ wr_tops_wicked.append("top_jacket_2")
            $ wr_tops_wicked.append("top_jacket_open_2")
            $ wr_tops_wicked.append("top_jacket_3")
            $ wr_tops_wicked.append("top_jacket_open_3")
            $ wr_tops_wicked.append("top_jacket_1")
            $ wr_tops_wicked.append("top_jacket_open_1")

        if hg_punk_rocker_ITEM.unlocked:
            $ wr_tops_wicked.append("top_rocker")
        if hg_lingerie_fishnet_ITEM.unlocked:
            $ wr_tops_wicked.append("top_fishnets_1")

    if active_girl == "luna":

        #Uniform
        $ wr_tops_uniform.append("top_1_r")
        $ wr_tops_uniform.append("top_2_r")
        $ wr_tops_uniform.append("top_3_r")

        if not luna_reverted:
            $ wr_tops_uniform.append("top_1_s")
            $ wr_tops_uniform.append("top_2_s")

        #Cheerleader
        if ll_cheer_r_ITEM.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_r")

        #Muggle
        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_tops_normal.append("top_muggle_1")
            $ wr_tops_normal.append("top_muggle_2")
            $ wr_tops_normal.append("top_muggle_3")

    if active_girl == "susan":

        #Uniform
        $ wr_tops_uniform.append("top_1")
        $ wr_tops_uniform.append("top_2")
        $ wr_tops_uniform.append("top_3")
        $ wr_tops_uniform.append("top_4")
        $ wr_tops_uniform.append("top_5")

    if active_girl == "cho":

        #Uniform
        $ wr_tops_uniform.append("top_school_1")
        $ wr_tops_uniform.append("top_school_2")
        $ wr_tops_uniform.append("top_school_3")
        $ wr_tops_uniform.append("top_school_4")
        $ wr_tops_uniform.append("top_school_5")

        $ wr_tops_uniform.append("top_sweater_1")

        #Muggle
        if cc_muggle_hot_ITEM.unlocked:
            $ wr_tops_normal.append("top_tanktop_1")
            $ wr_tops_normal.append("top_tanktop_2")
        if cc_outfit_sailor_white_ITEM.unlocked:
            $ wr_tops_normal.append("top_sailor_1")
        if cc_outfit_sailor_black_ITEM.unlocked:
            $ wr_tops_normal.append("top_sailor_2")
        if cc_costume_misty_ITEM.unlocked:
            $ wr_tops_normal.append("top_shirt_1")

    if active_girl == "tonks":

        #Uniform
        $ wr_tops_uniform.append("top_auror_1")
        $ wr_tops_uniform.append("top_auror_2")
        $ wr_tops_uniform.append("top_auror_3")

        #Wicked
        $ wr_tops_wicked.append("top_corset_1")

    return


### Bottoms List ###
label update_wr_bottoms_list:

    $ wr_bottoms_uniform = []
    $ wr_bottoms_cheerleader = []  #Add low hanging school skirts
    $ wr_bottoms_skirts = []       #Add skirts
    $ wr_bottoms_pants = []        #Add
    $ wr_bottoms_misc = []         #ADD Misc bottom items


    if active_girl == "hermione":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")
        $ wr_bottoms_uniform.append("skirt_3")
        $ wr_bottoms_uniform.append("skirt_4")
        $ wr_bottoms_uniform.append("skirt_5")
        $ wr_bottoms_uniform.append("skirt_7")

        $ wr_bottoms_uniform.append("skirt_1_low")
        $ wr_bottoms_uniform.append("skirt_2_low")
        $ wr_bottoms_uniform.append("skirt_3_low")
        $ wr_bottoms_uniform.append("skirt_4_low")

        #Cheerleader
        if hg_cheer_g_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_g")
        if hg_cheer_s_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_s")
        if hg_cheer_r_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_r")
        if hg_cheer_h_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_h")

        if hg_cheer_g_sexy_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_g")
        if hg_cheer_s_sexy_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_s")
        if hg_cheer_r_sexy_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_r")
        if hg_cheer_h_sexy_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_h")


        #Pants
        if hg_muggle_rainy_ITEM.unlocked:
            $ wr_bottoms_pants.append("pants_jeans_long")
        if hg_muggle_hot_ITEM.unlocked:
            $ wr_bottoms_pants.append("pants_jeans_short")
        if hg_punk_rocker_ITEM.unlocked or hg_punk_leather_ITEM.unlocked: #ToDo Punk Rocker will get the belted version!
            $ wr_bottoms_pants.append("pants_rocker")

    if active_girl == "luna":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")
        $ wr_bottoms_uniform.append("skirt_3")
        $ wr_bottoms_uniform.append("skirt_4")
        $ wr_bottoms_uniform.append("skirt_5")

        $ wr_bottoms_uniform.append("skirt_1_low")
        $ wr_bottoms_uniform.append("skirt_2_low")
        $ wr_bottoms_uniform.append("skirt_3_low")
        $ wr_bottoms_uniform.append("skirt_4_low")

        #Cheerleader
        if ll_cheer_r_ITEM.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_r")

        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_bottoms_skirts.append("skirt_muggle_1")

    if active_girl == "susan":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")

    return


### Other Clothings List ###
label update_wr_other_clothings_list:

    $ wr_neckwears = []
    $ wr_body_accs = []
    $ wr_gloves = []
    $ wr_stockings = []
    $ wr_robes = []


    if active_girl == "hermione":

        #Neckwear
        $ wr_neckwears.append("tie_striped_g")
        if hg_accs_wool_g_ITEM.unlocked and her_reputation > 15:
            $ wr_neckwears.append("tie_striped_s")

        if hg_accs_wool_g_ITEM.unlocked:
            $ wr_neckwears.append("scarf_striped_g")
        if hg_accs_wool_g_ITEM.unlocked and her_reputation > 15:
            $ wr_neckwears.append("scarf_striped_s")

        if her_whoring >= 14:
            $ wr_neckwears.append("banner_g")
            $ wr_neckwears.append("banner_unicorn")
        if her_whoring >= 17:
            $ wr_neckwears.append("banner_s")
            $ wr_neckwears.append("banner_death")
            $ wr_neckwears.append("collar_leather")
        if her_whoring >= 20:
            $ wr_neckwears.append("collar_bondage")

        if her_whoring >= 7 and hg_punk_rocker_ITEM.unlocked:
            $ wr_neckwears.append("choker_lace")
        if her_whoring >= 7 and hg_dress_yule_ball_ITEM.unlocked:
            $ wr_neckwears.append("necklace_pearls")
        if her_whoring >= 16 and hg_outfit_christmas_ITEM.unlocked:
            $ wr_neckwears.append("collar_xmas")

        if hg_costume_yennefer_ITEM.unlocked:
            $ wr_neckwears.append("choker_leather")
        if her_dress_wearable:
            $ wr_neckwears.append("banner_miss_hogwarts")
        #$ wr_neckwears.append("neck_goggles") #sQuest reward
        if collar == 1:
            $ wr_neckwears.append("collar_slave_shackle") #sQuest collar reward
        if collar == 2:
            $ wr_neckwears.append("collar_slut_shackle") #sQuest collar reward
        if collar == 3:
            $ wr_neckwears.append("collar_whore_shackle") #sQuest collar reward

        #Body Accessories
        if spew_badge_ITEM.unlocked:
            $ wr_body_accs.append("badge_spew")
        if cum_badge_ITEM.unlocked:
            $ wr_body_accs.append("badge_cum")
        if her_whoring >= 24:
            $ wr_body_accs.append("belt_condoms")

        #Gloves
        if hg_accs_wool_g_ITEM.unlocked:
            $ wr_gloves.append("gloves_wool_1")
        if her_whoring >= 10:
            $ wr_gloves.append("gloves_lace_1")
        if hg_lingerie_latex_ITEM.unlocked:
            $ wr_gloves.append("gloves_latex_1")

        if hg_outfit_maid_ITEM.unlocked or hg_lingerie_maid_ITEM.unlocked:
            $ wr_gloves.append("gloves_maid")
        if her_whoring >= 13 and hg_costume_lara_croft_ITEM.unlocked:
            $ wr_gloves.append("gloves_leather_2")
        if her_whoring >= 22 and hg_costume_harley_quinn_ITEM.unlocked:
            $ wr_gloves.append("gloves_leather_1")

        #Stockings
        if hg_accs_wool_g_ITEM.unlocked:
            $ wr_stockings.append("stockings_striped_1")
        if her_whoring >= 8 and hg_cheer_g_ITEM.unlocked:
            $ wr_stockings.append("stockings_cheer_g")
        if her_whoring >= 11 and (hg_cheer_s_ITEM.unlocked or hg_cheer_r_ITEM.unlocked or hg_cheer_h_ITEM.unlocked):
            $ wr_stockings.append("stockings_cheer_h")
            $ wr_stockings.append("stockings_cheer_r")
            $ wr_stockings.append("stockings_cheer_s")
        if her_whoring >= 8 and hg_cheer_g_sexy_ITEM.unlocked:
            $ wr_stockings.append("stockings_cheer_short_g")
        if her_whoring >= 11 and (hg_cheer_s_sexy_ITEM.unlocked or hg_cheer_r_sexy_ITEM.unlocked or hg_cheer_h_sexy_ITEM.unlocked):
            $ wr_stockings.append("stockings_cheer_short_h")
            $ wr_stockings.append("stockings_cheer_short_r")
            $ wr_stockings.append("stockings_cheer_short_s")

        if hg_muggle_cold_ITEM.unlocked:
            $ wr_stockings.append("stockings_pantyhose")
        if hg_muggle_hot_ITEM.unlocked:
            $ wr_stockings.append("stockings_cute")
        if hg_lingerie_maid_ITEM.unlocked:
            $ wr_stockings.append("stockings_high")
        if hg_lingerie_latex_ITEM.unlocked:
            $ wr_stockings.append("stockings_latex")
        if hg_costume_yennefer_ITEM.unlocked:
            $ wr_stockings.append("stockings_silk_1")

        if hg_outfit_maid_ITEM.unlocked or hg_lingerie_silk_ITEM.unlocked:
            $ wr_stockings.append("stockings_lace")

        if hg_punk_leather_ITEM.unlocked:
            $ wr_stockings.append("stockings_fishnets")

        #Robes
        if her_whoring >= 0:
            $ wr_robes.append("robe_1_g")
            $ wr_robes.append("robe_open_g")
        if her_whoring >= 3:
            $ wr_robes.append("robe_3_g")
        if her_whoring >= 6:
            $ wr_robes.append("robe_4_g")
        if her_whoring >= 9:
            $ wr_robes.append("robe_quidditch_g")

        if her_whoring >= 10:
            $ wr_robes.append("robe_1_s")
            $ wr_robes.append("robe_open_s")
            $ wr_robes.append("robe_3_s")
        if her_whoring >= 13:
            $ wr_robes.append("robe_4_s")
        if her_whoring >= 16:
            $ wr_robes.append("robe_quidditch_s")

    if active_girl == "luna":

        #Neck
        if ll_stewardess_ITEM.unlocked or ll_stewardess_short_ITEM.unlocked:
            $ wr_neckwears.append("cloth_tie")

        #Stockings
        if ll_cheer_r_ITEM.unlocked:
            $ wr_stockings.append("stockings_cheer_r")
        if ll_quirky_muggle_ITEM.unlocked:
            $ wr_stockings.append("stockings_muggle_1")
        if ll_dress_orange_ITEM.unlocked:
            $ wr_stockings.append("leggings_1")

    if active_girl == "susan":

        $ wr_neckwears.append("choker_base")

        $ wr_stockings.append("stockings_base")
        $ wr_stockings.append("stockings_lace")
        $ wr_stockings.append("stockings_rose")

    return


### Underwear List ###
label update_wr_underwear_list:

    $ wr_bras = []
    $ wr_panties = []
    $ wr_onepieces = []
    $ wr_garterbelts = []


    if active_girl == "hermione":

        #Bras
        $ wr_bras.append("bra_base")

        if hg_lingerie_silk_ITEM.unlocked:
            $ wr_bras.append("bra_silk")
        if hg_lingerie_lace_ITEM.unlocked:
            $ wr_bras.append("bra_lace")
        if hg_onepiece_sling_ITEM.unlocked:
            $ wr_bras.append("bra_bikini_string")
        if hg_bikini_latex_ITEM.unlocked:
            $ wr_bras.append("bra_bikini")
        if hg_lingerie_latex_ITEM.unlocked:
            $ wr_bras.append("bra_latex")
        if hg_lingerie_maid_ITEM.unlocked:
            $ wr_bras.append("bra_french_maid")

        if hg_punk_leather_ITEM.unlocked:
            $ wr_bras.append("bra_tape")

        if hg_lingerie_fishnet_ITEM.unlocked:
            $ wr_bras.append("top_fishnets_1")

        #Panties
        $ wr_panties.append("panties_base")

        if hg_lingerie_silk_ITEM.unlocked:
            $ wr_panties.append("panties_silk")
        if hg_nighty_silk_ITEM.unlocked:
            $ wr_panties.append("panties_silk_low")
        if hg_lingerie_lace_ITEM.unlocked:
            $ wr_panties.append("panties_lace")
        if hg_onepiece_sling_ITEM.unlocked:
            $ wr_panties.append("panties_bikini_string")
        if hg_bikini_latex_ITEM.unlocked:
            $ wr_panties.append("panties_bikini")
        if hg_lingerie_latex_ITEM.unlocked:
            $ wr_panties.append("panties_latex")
        if hg_lingerie_maid_ITEM.unlocked:
            $ wr_panties.append("panties_french_maid")
        if hg_lingerie_fishnet_ITEM.unlocked:
            $ wr_panties.append("panties_fishnet_string")

        #One-Pieces & Nighties
        if hg_swimsuit_sport_ITEM.unlocked:
            $ wr_onepieces.append("swimsuit_sport_1")
            $ wr_onepieces.append("swimsuit_sport_2")
            $ wr_onepieces.append("swimsuit_sport_3")
            if her_whoring >= 14:
                $ wr_onepieces.append("swimsuit_sport_4")
        $ wr_onepieces.append("swimsuit_halterless")
        $ wr_onepieces.append("swimsuit_neckband")
        $ wr_onepieces.append("onepiece_bunny")
        $ wr_onepieces.append("onepiece_microdress")

        $ wr_onepieces.append("onepiece_netsuit_fancy")
        $ wr_onepieces.append("onepiece_netsuit")

        if hg_onepiece_sling_ITEM.unlocked:
            $ wr_onepieces.append("onepiece_bikini_1")
        if hg_nighty_silk_ITEM.unlocked:
            $ wr_onepieces.append("nighty_short")
        if hg_nightgown_ITEM.unlocked:
            $ wr_onepieces.append("nighty_long")
        $ wr_onepieces.append("nighty_dress")

        #Garterbelts
        if hg_outfit_maid_ITEM.unlocked or hg_lingerie_silk_ITEM.unlocked:
            $ wr_garterbelts.append("garterbelt_lace")

    if active_girl == "luna":

        #Bras
        $ wr_bras.append("bra_basic")
        if ll_lingerie_silk_ITEM.unlocked:
            $ wr_bras.append("bra_silk")

        #Panties
        $ wr_panties.append("panties_basic")
        if ll_lingerie_silk_ITEM.unlocked:
            $ wr_panties.append("panties_silk")
        if ll_stewardess_ITEM.unlocked:
            $ wr_panties.append("panties_thong_1")
        if ll_stewardess_short_ITEM.unlocked:
            $ wr_panties.append("panties_thong_2")

        #One-Pieces
        $ wr_onepieces.append("nighty_long")
        $ wr_onepieces.append("nighty_long_translucent")

    if active_girl == "susan":

        #Bras
        $ wr_bras.append("bra_base")
        $ wr_bras.append("bra_lace")
        $ wr_bras.append("bra_chain")

        #Panties
        $ wr_panties.append("panties_base")
        $ wr_panties.append("panties_lace")

        #One-Pieces
        $ wr_onepieces.append("sling_1")
        $ wr_onepieces.append("sling_2")

    return


### Outfits List ###
label update_wr_outfits_list:

    $ wr_outfits = []
    $ wr_costumes = []
    $ wr_dresses = []
    $ wr_custom_outfits = []


    if active_girl == "hermione":
        python:

            #Outfits
            for i in hermione_outfits_list:
                if i.unlocked:
                    wr_outfits.append(i)
            #Costumes
            for i in hermione_costumes_list:
                if i.unlocked:
                    wr_costumes.append(i)
            #Dresses
            for i in hermione_dresses_list:
                if i.unlocked:
                    wr_dresses.append(i)

    if active_girl == "luna":
        python:

            #Outfits
            for i in luna_outfits_list:
                if i.unlocked:
                    wr_outfits.append(i)
            #Costumes
            for i in luna_costumes_list:
                if i.unlocked:
                    wr_costumes.append(i)
            #Dresses
            for i in luna_dresses_list:
                if i.unlocked:
                    wr_dresses.append(i)

    if active_girl == "susan":
        python:

            #Outfits
            for i in susan_outfits_list:
                if i.unlocked:
                    wr_outfits.append(i)
            #Costumes
            for i in susan_costumes_list:
                if i.unlocked:
                    wr_costumes.append(i)
            #Dresses
            for i in susan_dresses_list:
                if i.unlocked:
                    wr_dresses.append(i)

    return

### Miscellaneous List ###
label update_wr_miscellaneous_list:

    $ wr_potions_list = []
    $ wr_items_list = []
    $ wr_piercings_list = []
    $ wr_tattoos_list = []


    if active_girl == "hermione":

        #Potions
        if potion_inv.has("p_cat_transformation") or potion_inv.has("p_luna_transformation"):
            $ wr_potions_list.append("polyjuice_potion")
        if potion_inv.has("p_breast_expansion") or potion_inv.has("p_ass_expansion"):
            $ wr_potions_list.append("expanding_elixir")
        if potion_inv.has("p_milk_potion"):
            $ wr_potions_list.append("milk_potion")
        if potion_inv.has("p_cum_addiction") or potion_inv.has("p_hypno"):
            $ wr_potions_list.append("love_potion")
        if potion_inv.has("p_transparency"):
            $ wr_potions_list.append("clothes_potion")

        #Items #Butt-plugs, Gags, Brooms,...
        if anal_plugs_ITEM.number > 0:
            if buttplug_1_worn: #Event happened.
                $ wr_items_list.append("buttplug_small")
            if buttplug_2_worn: #Event happened.
                $ wr_items_list.append("buttplug_medium")
            if buttplug_3_worn: #Event happened.
                $ wr_items_list.append("buttplug_large")
        if game_difficulty >= 3 and her_whoring >= 21 and ballgag_and_cuffs_ITEM.number > 0:
            $ wr_items_list.append("item_ballgag_and_cuffs")

        #Piercings
        if her_whoring >= 5:
            $ wr_piercings_list.append("ears_hearts_large")
            $ wr_piercings_list.append("ears_hearts")
            $ wr_piercings_list.append("ears_pearls")
            if hg_gamble_slut_ITEM.unlocked:
                $ wr_piercings_list.append("ears_gambler")

        if her_whoring >= 23:
            $ wr_piercings_list.append("nipples_pearls")
            $ wr_piercings_list.append("belly_pearls")

        if her_whoring >= 11:
            if hg_gamble_slut_ITEM.unlocked:
                $ wr_piercings_list.append("belly_gambler")

        #Tattoos
        if autograph: #Unlocked after flirting with Professor Lockheart.
            $ wr_tattoos_list.append("thigh/signature")

        if her_whoring >= 11:
            $ wr_tattoos_list.append("torso/twist")
            $ wr_tattoos_list.append("thigh/tribal")

        if her_whoring >= 14:
            $ wr_tattoos_list.append("thigh/free")

        if her_whoring >= 17:
            $ wr_tattoos_list.append("pubic/10g_raised")
            $ wr_tattoos_list.append("pubic/10g")
            $ wr_tattoos_list.append("pubic/cock_hole")
            $ wr_tattoos_list.append("pubic/inheat")

        if her_whoring >= 21:
            $ wr_tattoos_list.append("pubic/deatheater")
            $ wr_tattoos_list.append("pubic/fuck_me")
            $ wr_tattoos_list.append("pubic/deposit")

        if her_whoring >= 23:
            $ wr_tattoos_list.append("pubic/Cumslut")
            $ wr_tattoos_list.append("pubic/cum_here")
            $ wr_tattoos_list.append("pubic/cunt")
            $ wr_tattoos_list.append("pubic/mudblood")
            $ wr_tattoos_list.append("pubic/punk_mudblood")

    if active_girl == "luna":
        if potion_inv.has("p_transparency"):
            $ wr_potions_list.append("clothes_potion")

    return
