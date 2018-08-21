
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

    #Wardrobe Color
    $ wr_background_color = []

    $ wr_background_color.append("base")
    $ wr_background_color.append("red")
    $ wr_background_color.append("green")
    $ wr_background_color.append("blue")


    #Hair Color
    $ wr_haircolor = []

    if active_girl == "hermione":

        $ wr_haircolor.append("1")
        if yellow_dye_OBJ.unlocked: #if "blonde_dye" in cs_existing_stock:
            $ wr_haircolor.append("2")
        if red_dye_OBJ.unlocked: #if "red_dye" in cs_existing_stock:
            $ wr_haircolor.append("3")
        if crimson_dye_OBJ.unlocked: #if "crimson_dye" in cs_existing_stock:
            $ wr_haircolor.append("4")
        if black_dye_OBJ.unlocked: #if "black_dye" in cs_existing_stock:
            $ wr_haircolor.append("5")

        if dark_green_dye_OBJ.unlocked: #if "green_dye" in cs_existing_stock:
            $ wr_haircolor.append("6")
        if dark_blue_dye_OBJ.unlocked: #if "blue_dye" in cs_existing_stock:
            $ wr_haircolor.append("7")
        if purple_dye_OBJ.unlocked: #if "purple_dye" in cs_existing_stock:
            $ wr_haircolor.append("8")
        if pink_dye_OBJ.unlocked: #if "pink_dye" in cs_existing_stock:
            $ wr_haircolor.append("9")
        if gray_dye_OBJ.unlocked: #if "white_dye" in cs_existing_stock:
            $ wr_haircolor.append("10")


    #House Color
    $ wr_housecolor = []

    if active_girl == "hermione":
        if blue_dye_OBJ.unlocked: #if "blue_dye" in cs_existing_stock:
            $ wr_housecolor.append("blue")
        if green_dye_OBJ.unlocked: #if "green_dye" in cs_existing_stock:
            $ wr_housecolor.append("green")
        if red_dye_OBJ.unlocked: #if "red_dye" in cs_existing_stock:
            $ wr_housecolor.append("red")
        if yellow_dye_OBJ.unlocked: #if "blonde_dye" in cs_existing_stock:
            $ wr_housecolor.append("yellow")


    #Cloth Color
    $ wr_clothcolor = []

    if active_girl == "hermione":
        if dark_blue_dye_OBJ.unlocked:
            $ wr_clothcolor.append("dark_blue")
        if dark_green_dye_OBJ.unlocked:
            $ wr_clothcolor.append("dark_green")
        if crimson_dye_OBJ.unlocked:
            $ wr_clothcolor.append("crimson")
        if orange_dye_OBJ.unlocked:
            $ wr_clothcolor.append("orange")
        if purple_dye_OBJ.unlocked:
            $ wr_clothcolor.append("purple")
        if brown_dye_OBJ.unlocked:
            $ wr_clothcolor.append("brown")
        if black_dye_OBJ.unlocked:
            $ wr_clothcolor.append("black")

        if blue_dye_OBJ.unlocked:
            $ wr_clothcolor.append("blue")
        if green_dye_OBJ.unlocked:
            $ wr_clothcolor.append("green")
        if red_dye_OBJ.unlocked:
            $ wr_clothcolor.append("red")
        if yellow_dye_OBJ.unlocked:
            $ wr_clothcolor.append("yellow")
        if pink_dye_OBJ.unlocked:
            $ wr_clothcolor.append("pink")
        if gray_dye_OBJ.unlocked:
            $ wr_clothcolor.append("gray")
        if white_dye_OBJ.unlocked:
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
        $ wr_hair.append("A")
        if hg_maid_OBJ.unlocked or hg_lingerie_maid_OBJ.unlocked or hg_ballDress_OBJ.unlocked: #Updo Hair from Outfits/Sets
            $ wr_hair.append("B")
        if hg_bio_OBJ.unlocked: #Elizabeth Hair from Outfit.
            $ wr_hair.append("E")

        #Makeup
        if red_lipstick_OBJ.unlocked:
            $ wr_makeup.append("red_lipstick")
        if pink_lipstick_OBJ.unlocked:
            $ wr_makeup.append("pink_lipstick")
        if freckles_makeup_OBJ.unlocked:
            $ wr_makeup.append("freckles")
        if fake_cum_makeup_OBJ.unlocked:
            $ wr_makeup.append("fake_cum")

        #Glasses
        if reading_glasses_OBJ.unlocked:
            $ wr_glasses.append("reading_glasses")
        if vintage_glasses_OBJ.unlocked:
            $ wr_glasses.append("vintage_glasses")

        #Ears
        if cat_ears_OBJ.unlocked:
            $ wr_ears.append("cat_ears")
        if elf_ears_OBJ.unlocked:
            $ wr_ears.append("elf_ears")

        #Hats
        if hg_maid_OBJ.unlocked:
            $ wr_hats.append("witch_hat")
        if hg_witch_OBJ.unlocked:
            $ wr_hats.append("maid_hat")
        if hg_ballDress_OBJ.unlocked:
            $ wr_hats.append("tiara")

    #if active_girl == "luna":

    if active_girl == "astoria":

        #Hair
        $ wr_hair.append("A")
        if ag_lazy_OBJ.unlocked or ag_lazy_short_OBJ.unlocked:
            $ wr_hair.append("L")
        if ag_boss_uniform_OBJ.unlocked:
            $ wr_hair.append("N")

        #Hats
        if ag_boss_uniform_OBJ.unlocked:
            $ wr_hats.append("boss_hat")

    if active_girl == "susan":

        $ wr_hair.append("A")

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
        if whoring < 11:
            $ wr_tops_uniform.append("top_3_g")
        $ wr_tops_uniform.append("top_4_g")
        if whoring >= 11:
            $ wr_tops_uniform.append("top_5_g")
        $ wr_tops_uniform.append("top_6_g")

        #Cheerleader
        if hg_cheer_g_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_g")
        if hg_cheer_s_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_s")
        if hg_cheer_r_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_r")
        if hg_cheer_h_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_h")

        if hg_cheer_g_sexy_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_g")
        if hg_cheer_s_sexy_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_s")
        if hg_cheer_r_sexy_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_r")
        if hg_cheer_h_sexy_OBJ.unlocked:
            $ wr_tops_cheerleader.append("top_cheer_sexy_h")

        #Muggle
        if hg_muggle_cold_OBJ.unlocked:
            $ wr_tops_normal.append("normal_pullover")
        if hg_muggle_cold_sexy_OBJ.unlocked:
            $ wr_tops_normal.append("normal_pullover_sexy")
        if hg_muggle_rainy_OBJ.unlocked:
            $ wr_tops_normal.append("normal_sweater")
        if hg_muggle_hot_OBJ.unlocked:
            $ wr_tops_normal.append("normal_waitress_top")

        #Wicked
        if hg_punk_leather_OBJ.unlocked:
            $ wr_tops_wicked.append("leather_jacket_short_sleeves")
            $ wr_tops_wicked.append("leather_jacket_short_sleeves_open")
            $ wr_tops_wicked.append("leather_jacket_sleeveless")
            $ wr_tops_wicked.append("leather_jacket_sleeveless_open")
            $ wr_tops_wicked.append("leather_jacket_sleeves")
            $ wr_tops_wicked.append("leather_jacket_sleeves_open")

        if hg_punk_rocker_OBJ.unlocked:
            $ wr_tops_wicked.append("top_rocker")
        if hg_lingerie_fishnet_OBJ.unlocked:
            $ wr_tops_wicked.append("top_fishnets")

    if active_girl == "astoria":

        #Uniform
        $ wr_tops_uniform.append("shirt_1")
        $ wr_tops_uniform.append("shirt_2")
        $ wr_tops_uniform.append("shirt_3")
        $ wr_tops_uniform.append("shirt_4")
        if ag_boss_uniform_OBJ.unlocked:
            $ wr_tops_uniform.append("shirt_boss")

    if active_girl == "susan":

        #Uniform
        $ wr_tops_uniform.append("shirt_1")

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

        $ wr_bottoms_uniform.append("skirt_1_low")
        $ wr_bottoms_uniform.append("skirt_2_low")
        $ wr_bottoms_uniform.append("skirt_3_low")
        $ wr_bottoms_uniform.append("skirt_4_low") #micro skirt

        #Cheerleader
        if hg_cheer_g_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_g")
        if hg_cheer_s_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_s")
        if hg_cheer_r_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_r")
        if hg_cheer_h_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_h")

        if hg_cheer_g_sexy_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_g")
        if hg_cheer_s_sexy_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_s")
        if hg_cheer_r_sexy_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_r")
        if hg_cheer_h_sexy_OBJ.unlocked:
            $ wr_bottoms_cheerleader.append("skirt_cheer_sexy_h")

        #Skirts
        if hg_muggle_cold_OBJ.unlocked: #Temporary
            $ wr_bottoms_skirts.append("skirt_belted_mini")
        if hg_muggle_cold_sexy_OBJ.unlocked:
            $ wr_bottoms_skirts.append("skirt_belted_micro")

        #Pants
        if hg_muggle_rainy_OBJ.unlocked:
            $ wr_bottoms_pants.append("pants_jeans_long")
        if hg_muggle_hot_OBJ.unlocked:
            $ wr_bottoms_pants.append("pants_jeans_short")
        if hg_punk_rocker_OBJ.unlocked or hg_punk_leather_OBJ.unlocked: #ToDo Punk Rocker will get the belted version!
            $ wr_bottoms_pants.append("pants_rocker")

    if active_girl == "astoria":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")
        $ wr_bottoms_uniform.append("skirt_2")

        #Pants
        if ag_boss_uniform_OBJ.unlocked:
            $ wr_bottoms_pants.append("pants_boss")

    if active_girl == "susan":

        #Uniform
        $ wr_bottoms_uniform.append("skirt_1")

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
        if hg_accs_wool_g_OBJ.unlocked:
            $ wr_neckwears.append("scarf_striped_g")
        if whoring >= 14:
            $ wr_neckwears.append("banner_g")
            $ wr_neckwears.append("banner_unicorn")
        if whoring >= 17:
            $ wr_neckwears.append("banner_s")
            $ wr_neckwears.append("banner_death")
            $ wr_neckwears.append("collar_leather")
        if whoring >= 20:
            $ wr_neckwears.append("collar_bondage")

        if whoring >= 7 and hg_punk_rocker_OBJ.unlocked:
            $ wr_neckwears.append("choker_lace")
        if whoring >= 7 and hg_ballDress_OBJ.unlocked:
            $ wr_neckwears.append("necklace_pearls")
        if whoring >= 16 and hg_christmas_OBJ.unlocked:
            $ wr_neckwears.append("collar_xmas")

        if hg_yenn_OBJ.unlocked:
            $ wr_neckwears.append("choker_leather")
            $ wr_neckwears.append("scarf_silk")
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
        if spew_badge_OBJ.unlocked:
            $ wr_body_accs.append("badge_SPEW")
        if I_love_cum_badge_OBJ.unlocked:
            $ wr_body_accs.append("badge_I_love_cum")
        if whoring >= 24:
            $ wr_body_accs.append("belt_band_of_condoms")

        #Gloves
        if hg_accs_wool_g_OBJ.unlocked:
            $ wr_gloves.append("gloves_wool_short_g")
        if hg_christmas_OBJ.unlocked:
            $ wr_gloves.append("gloves_wool_short_xmas")
        if whoring >= 10:
            $ wr_gloves.append("gloves_lace")
        if hg_lingerie_latex_OBJ.unlocked:
            $ wr_gloves.append("gloves_latex")

        if hg_maid_OBJ.unlocked or hg_lingerie_maid_OBJ.unlocked:
            $ wr_gloves.append("gloves_french_maid")
        if whoring >= 13 and hg_laraCroft_OBJ.unlocked:
            $ wr_gloves.append("gloves_leather_short")
        if whoring >= 22 and hg_harleyQuinn_OBJ.unlocked:
            $ wr_gloves.append("gloves_leather")
        #$ wr_gloves.append("gloves_egyptian") #ADD Egypt Outfit

        #Stockings
        if hg_accs_wool_g_OBJ.unlocked:
            $ wr_stockings.append("stockings_striped_g")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_striped_vibe") #Will be in accessories instead
        if whoring >= 8 and hg_cheer_g_OBJ.unlocked:
            $ wr_stockings.append("stockings_cheer_g")
        if whoring >= 11 and (hg_cheer_s_OBJ.unlocked or hg_cheer_r_OBJ.unlocked or hg_cheer_h_OBJ.unlocked):
            $ wr_stockings.append("stockings_cheer_h")
            $ wr_stockings.append("stockings_cheer_r")
            $ wr_stockings.append("stockings_cheer_s")
        if whoring >= 8 and hg_cheer_g_sexy_OBJ.unlocked:
            $ wr_stockings.append("stockings_cheer_short_g")
        if whoring >= 11 and (hg_cheer_s_sexy_OBJ.unlocked or hg_cheer_r_sexy_OBJ.unlocked or hg_cheer_h_sexy_OBJ.unlocked):
            $ wr_stockings.append("stockings_cheer_short_h")
            $ wr_stockings.append("stockings_cheer_short_r")
            $ wr_stockings.append("stockings_cheer_short_s")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_cheer_vibe") #Will be in accessories instead

        if hg_muggle_cold_OBJ.unlocked:
            $ wr_stockings.append("stockings_pantyhose")
        if hg_muggle_hot_OBJ.unlocked:
            $ wr_stockings.append("stockings_cute")
        if hg_lingerie_maid_OBJ.unlocked:
            $ wr_stockings.append("stockings_high")
        if hg_lingerie_latex_OBJ.unlocked:
            $ wr_stockings.append("stockings_latex")
        if hg_yenn_OBJ.unlocked:
            $ wr_stockings.append("stockings_silk_flowers")

        if hg_maid_OBJ.unlocked or hg_lingerie_silk_OBJ.unlocked:
            $ wr_stockings.append("stockings_lace")

        if hg_punk_leather_OBJ.unlocked:
            $ wr_stockings.append("stockings_fishnets")

        #Robes
        if whoring >= 0:
            $ wr_robes.append("gryff_robe_shirt_none")
            $ wr_robes.append("gryff_robe_off")
        if whoring >= 3:
            $ wr_robes.append("gryff_robe_gap_wide")
        if whoring >= 6:
            $ wr_robes.append("gryff_robe_seethrough")
        if whoring >= 9:
            $ wr_robes.append("gryff_quidditch")

        if whoring >= 10:
            $ wr_robes.append("slyth_robe_shirt_none")
            $ wr_robes.append("slyth_robe_off")
            $ wr_robes.append("slyth_robe_gap_wide")
        if whoring >= 13:
            $ wr_robes.append("slyth_robe_seethrough")
        if whoring >= 16:
            $ wr_robes.append("slyth_quidditch")

    if active_girl == "astoria":
        if ag_nighty_silk_OBJ.unlocked:
            $ wr_stockings.append("nighty_stockings")

        $ wr_robes.append("slyth_1")

    if active_girl == "susan":

        $ wr_neckwears.append("chain_chocker")

        $ wr_stockings.append("stockings")

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

        if hg_lingerie_silk_OBJ.unlocked:
            $ wr_bras.append("bra_silk")
        if hg_lingerie_lace_OBJ.unlocked:
            $ wr_bras.append("bra_lace")
        if hg_onepiece_sling_OBJ.unlocked:
            $ wr_bras.append("bra_bikini_string")
        if hg_bikini_latex_OBJ.unlocked:
            $ wr_bras.append("bra_bikini")
        if hg_lingerie_latex_OBJ.unlocked:
            $ wr_bras.append("bra_latex")
        if hg_lingerie_maid_OBJ.unlocked:
            $ wr_bras.append("bra_french_maid")

        if hg_punk_leather_OBJ.unlocked:
            $ wr_bras.append("bra_tape")

        if hg_lingerie_fishnet_OBJ.unlocked:
            $ wr_bras.append("top_fishnets")

        #Panties
        $ wr_panties.append("panties_base")

        if hg_lingerie_silk_OBJ.unlocked:
            $ wr_panties.append("panties_silk")
        if hg_nighty_silk_OBJ.unlocked:
            $ wr_panties.append("panties_silk_low")
        if hg_lingerie_lace_OBJ.unlocked:
            $ wr_panties.append("panties_lace")
        if hg_onepiece_sling_OBJ.unlocked:
            $ wr_panties.append("panties_bikini_string")
        if hg_bikini_latex_OBJ.unlocked:
            $ wr_panties.append("panties_bikini")
        if hg_lingerie_latex_OBJ.unlocked:
            $ wr_panties.append("panties_latex")
        if hg_lingerie_maid_OBJ.unlocked:
            $ wr_panties.append("panties_french_maid")
        if hg_lingerie_fishnet_OBJ.unlocked:
            $ wr_panties.append("panties_fishnet_string")

        #One-Pieces & Nighties
        $ wr_onepieces.append("onepiece_swimsuit_halterless")
        $ wr_onepieces.append("onepiece_swimsuit")
        $ wr_onepieces.append("onepiece_bunny")
        $ wr_onepieces.append("onepiece_microdress")

        if hg_onepiece_sling_OBJ.unlocked:
            $ wr_onepieces.append("onepiece_bikini_string")
        if hg_nighty_silk_OBJ.unlocked:
            $ wr_onepieces.append("nighty_short")
        if hg_nightgown_OBJ.unlocked:
            $ wr_onepieces.append("nighty_long")
        $ wr_onepieces.append("nighty_dress")

        #Garterbelts
        if hg_maid_OBJ.unlocked or hg_lingerie_silk_OBJ.unlocked:
            $ wr_garterbelts.append("garterbelt_lace")

    #if active_girl == "luna":

    if active_girl == "astoria":

        #Bras
        $ wr_bras.append("clear_bra")
        if ag_lingerie_lace_OBJ.unlocked:
            $ wr_bras.append("lace_bra")
        if ag_lingerie_lewd_OBJ.unlocked:
            $ wr_bras.append("lewd_bra")

        if ag_nighty_silk_OBJ.unlocked:
            $ wr_onepieces.append("nighty")

        #Panties
        $ wr_panties.append("clear_panties")
        if ag_lingerie_lace_OBJ.unlocked:
            $ wr_panties.append("lace_panties")
        if ag_lingerie_lewd_OBJ.unlocked:
            $ wr_panties.append("lewd_panties")
        if ag_nighty_silk_OBJ.unlocked:
            $ wr_panties.append("nighty_panties")

    if active_girl == "susan":
        #$ wr_bras.append("")
        $ wr_bras.append("lace_bra")
        #$ wr_bras.append("chain_bra")

        $ wr_onepieces.append("sling_1")
        $ wr_onepieces.append("sling_2")

        #$ wr_panties.append("")
        $ wr_panties.append("lace_panties")
        $ wr_panties.append("chain_panties")

    return


### Outfits List ###
label update_wr_outfits_list:

    $ wr_outfits = []
    $ wr_costumes = []
    $ wr_dresses = []
    $ wr_custom_outfits = []


    if active_girl == "hermione":

        #Outfits
        if hg_maid_OBJ.unlocked:
            $ wr_outfits.append(hg_maid_OBJ)
        if hg_christmas_OBJ.unlocked:
            $ wr_outfits.append(hg_christmas_OBJ)
        if hg_present_OBJ.unlocked:
            $ wr_outfits.append(hg_present_OBJ)
        if hg_japan_OBJ.unlocked:
            $ wr_outfits.append(hg_japan_OBJ)

        #Costumes
        if hg_pirate_OBJ.unlocked:
            $ wr_costumes.append(hg_pirate_OBJ)
        if hg_powerGirl_OBJ.unlocked:
            $ wr_costumes.append(hg_powerGirl_OBJ)
        if hg_msMarvel_OBJ.unlocked:
            $ wr_costumes.append(hg_msMarvel_OBJ)
        if hg_harleyQuinn_OBJ.unlocked:
            $ wr_costumes.append(hg_harleyQuinn_OBJ)
        if hg_laraCroft_OBJ.unlocked:
            $ wr_costumes.append(hg_laraCroft_OBJ)
        if hg_tifa_OBJ.unlocked:
            $ wr_costumes.append(hg_tifa_OBJ)
        if hg_witch_OBJ.unlocked:
            $ wr_costumes.append(hg_witch_OBJ)
        if hg_bio_OBJ.unlocked:
            $ wr_costumes.append(hg_bio_OBJ)
        if hg_yenn_OBJ.unlocked:
            $ wr_costumes.append(hg_yenn_OBJ)

        #Dresses
        if hg_heartDancer_OBJ.unlocked:
            $ wr_dresses.append(hg_heartDancer_OBJ)
        if hg_ballDress_OBJ.unlocked:
            $ wr_dresses.append(hg_ballDress_OBJ)


    if active_girl == "astoria":
        #Costumes
        if ag_lazy_OBJ.unlocked:
            $ wr_costumes.append(ag_lazy_OBJ)
        if ag_lazy_short_OBJ.unlocked:
            $ wr_costumes.append(ag_lazy_short_OBJ)
        #Dresses
        if ag_ball_dress_OBJ.unlocked:
            $ wr_dresses.append(ag_ball_dress_OBJ)

    #if active_girl == "susan":

    return

### Miscellaneous List ###
label update_wr_miscellaneous_list:

    $ wr_potions_list = []
    $ wr_items_list = []
    $ wr_piercings_list = []
    $ wr_tattoos_list = []


    if active_girl == "hermione":

        #Potions
        $ wr_potions_list.append("universal_potion") #Potion that can be used day AND night!
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
        if gift_item_inv[AnalPlugs.id] > 0:
            if buttplug_1_worn: #Event happened.
                $ wr_items_list.append("buttplug_small")
            if buttplug_2_worn: #Event happened.
                $ wr_items_list.append("buttplug_medium")
            if buttplug_3_worn: #Event happened.
                $ wr_items_list.append("buttplug_large")

        #Piercings
        if whoring >= 5:
            $ wr_piercings_list.append("ears_hearts_large")
            $ wr_piercings_list.append("ears_hearts")
            $ wr_piercings_list.append("ears_pearls")

        if whoring >= 23:
            $ wr_piercings_list.append("nipples_pearls")
            $ wr_piercings_list.append("belly_pearls")

        #Tattoos
        if autograph: #Unlocked after flirting with Professor Lockheart.
            $ wr_tattoos_list.append("thigh/signature")

        if whoring >= 11:
            $ wr_tattoos_list.append("torso/twist")
            $ wr_tattoos_list.append("thigh/tribal")

        if whoring >= 14:
            $ wr_tattoos_list.append("thigh/free")

        if whoring >= 17:
            $ wr_tattoos_list.append("pubic/10g_raised")
            $ wr_tattoos_list.append("pubic/10g")
            $ wr_tattoos_list.append("pubic/cock_hole")
            $ wr_tattoos_list.append("pubic/inheat")

        if whoring >= 21:
            $ wr_tattoos_list.append("pubic/deatheater")
            $ wr_tattoos_list.append("pubic/fuck_me")
            $ wr_tattoos_list.append("pubic/deposit")

        if whoring >= 23:
            $ wr_tattoos_list.append("pubic/Cumslut")
            $ wr_tattoos_list.append("pubic/cum_here")
            $ wr_tattoos_list.append("pubic/cunt")
            $ wr_tattoos_list.append("pubic/mudblood")
            $ wr_tattoos_list.append("pubic/punk_mudblood")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return
