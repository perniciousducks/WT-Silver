<<<<<<< HEAD

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
        if "blonde_dye" in cs_existing_stock:
            $ wr_haircolor.append("2")
        if "red_dye" in cs_existing_stock:
            $ wr_haircolor.append("3")
        if "crimson_dye" in cs_existing_stock:
            $ wr_haircolor.append("4")
        if "black_dye" in cs_existing_stock:
            $ wr_haircolor.append("5")

        if "green_dye" in cs_existing_stock:
            $ wr_haircolor.append("6")
        if "blue_dye" in cs_existing_stock:
            $ wr_haircolor.append("7")
        if "purple_dye" in cs_existing_stock:
            $ wr_haircolor.append("8")
        if "pink_dye" in cs_existing_stock:
            $ wr_haircolor.append("9")
        if "white_dye" in cs_existing_stock:
            $ wr_haircolor.append("10")


    #House Color
    $ wr_housecolor = []

    if active_girl == "hermione":
        if "blue_dye" in cs_existing_stock:
            $ wr_housecolor.append("blue")
        if "green_dye" in cs_existing_stock:
            $ wr_housecolor.append("green")
        if "red_dye" in cs_existing_stock:
            $ wr_housecolor.append("red")
        if "blonde_dye" in cs_existing_stock:
            $ wr_housecolor.append("yellow")


    #Cloth Color
    $ wr_clothcolor = []

    if active_girl == "hermione":
        if "blue_dye" in cs_existing_stock:
            $ wr_clothcolor.append("dark_blue")
        if "green_dye" in cs_existing_stock:
            $ wr_clothcolor.append("dark_green")
        if "red_dye" in cs_existing_stock:
            $ wr_clothcolor.append("crimson")
        if "blonde_dye" in cs_existing_stock:      #Temp name
            $ wr_clothcolor.append("orange")
        if "purple_dye" in cs_existing_stock:
            $ wr_clothcolor.append("purple")
        if "black_dye" in cs_existing_stock:    #Temp name
            $ wr_clothcolor.append("brown")
        if "black_dye" in cs_existing_stock:
            $ wr_clothcolor.append("black")

        if "blue_dye" in cs_existing_stock:
            $ wr_clothcolor.append("blue")
        if "green_dye" in cs_existing_stock:
            $ wr_clothcolor.append("green")
        if "red_dye" in cs_existing_stock:
            $ wr_clothcolor.append("red")
        if "blonde_dye" in cs_existing_stock:
            $ wr_clothcolor.append("yellow")
        if "pink_dye" in cs_existing_stock:
            $ wr_clothcolor.append("pink")
        if "black_dye" in cs_existing_stock:    #Temp name
            $ wr_clothcolor.append("gray")
        if "white_dye" in cs_existing_stock:
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
        $ wr_hair.append("B")
        #if hg_ ADD _OBJ.purchased: #Add Elizabeth Outfit.
        $ wr_hair.append("E")

        #Makeup
        $ wr_makeup.append("lipstick")
        if "freckles" in cs_existing_stock:
            $ wr_makeup.append("freckles")
        if "fake_cum" in cs_existing_stock:
            $ wr_makeup.append("fake_cum")

        #Glasses
        if "reading_glasses" in cs_existing_stock:
            $ wr_glasses.append("reading_glasses")
        if "vintage_glasses" in cs_existing_stock:
            $ wr_glasses.append("vintage_glasses")

        #Ears
        if "cat_ears" in cs_existing_stock:
            $ wr_ears.append("cat_ears")
        if "elf_ears" in cs_existing_stock:
            $ wr_ears.append("elf_ears")

        #Hats
        if hg_ballDress_OBJ.purchased:
            $ wr_hats.append("tiara")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Tops List ###
label update_wr_tops_list:

    $ wr_tops_uniform = [] #ADD school clothing and cheerleader tops,...
    $ wr_tops_normal = []  #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    $ wr_tops_wicked = []  #ADD kinky clothing items like leather, fishnet
    $ wr_tops_misc = []    #ADD Misc top items


    if active_girl == "hermione":

        #Uniform
        $ wr_tops_uniform.append("uni_top_1")
        $ wr_tops_uniform.append("uni_top_2")
        if whoring < 11:
            $ wr_tops_uniform.append("uni_top_3")
        $ wr_tops_uniform.append("uni_top_4")
        if whoring >= 11:
            $ wr_tops_uniform.append("uni_top_5")
        $ wr_tops_uniform.append("uni_top_6")

        if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased:
            $ wr_tops_uniform.append("uni_top_cheer")
            $ wr_tops_uniform.append("uni_top_cheer_skimpy")

        #Muggle
        if "normal_pullover" in cs_existing_stock:
            $ wr_tops_normal.append("normal_pullover")
            $ wr_tops_normal.append("normal_pullover_sexy")
        if "normal_sweater" in cs_existing_stock:
            $ wr_tops_normal.append("normal_sweater")
        #if "normal_waitress_top" in cs_existing_stock:
        #    $ wr_tops_normal.append("normal_waitress_top")

        #Wicked
        if "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_short_sleeves")
            $ wr_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
        if "wicked_leather_jacket_sleeveless" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeveless")
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
        if "wicked_leather_jacket_sleeves" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeves")
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeves_open")

        if hg_rocker_OBJ.purchased:
            $ wr_tops_wicked.append("wicked_rocker_top")
        if whoring >= 19 and "top_fishnets" in cs_existing_stock:
            $ wr_tops_wicked.append("top_fishnets")

        #Misc. Tops
        #if whoring >= 17:
        #    $ wr_tops_misc.append("top_ripped_tie_striped")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Bottoms List ###
label update_wr_bottoms_list:

    $ wr_bottoms_uniform = []
    $ wr_bottoms_uniform_low = []  #Add low hanging school skirts
    $ wr_bottoms_skirts = []       #Add skirts
    $ wr_bottoms_pants = []        #Add
    $ wr_bottoms_misc = []         #ADD Misc bottom items


    if active_girl == "hermione":

        #Uniform
        $ wr_bottoms_uniform.append("uni_skirt_1")
        $ wr_bottoms_uniform.append("uni_skirt_2")
        $ wr_bottoms_uniform.append("uni_skirt_3")
        $ wr_bottoms_uniform.append("uni_skirt_4")
        $ wr_bottoms_uniform.append("uni_skirt_5")

        if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased:
            $ wr_bottoms_uniform.append("uni_skirt_cheer")
            $ wr_bottoms_uniform.append("uni_skirt_cheer_skimpy")

        #Uniform Low
        $ wr_bottoms_uniform_low.append("uni_skirt_1_low")
        $ wr_bottoms_uniform_low.append("uni_skirt_2_low")
        $ wr_bottoms_uniform_low.append("uni_skirt_3_low")
        #if micro_skirt unlocked/purchased:
        #$ wr_bottoms_uniform_low.append("uni_skirt_4_low") #micro skirt

        #Skirts
        if "skirt_belted_mini" in cs_existing_stock:
            $ wr_bottoms_skirts.append("skirt_belted_mini")
        if "skirt_belted_micro" in cs_existing_stock:
            $ wr_bottoms_skirts.append("skirt_belted_micro")

        #Pants
        if "pants_jeans_long" in cs_existing_stock:
            $ wr_bottoms_pants.append("pants_jeans_long")
        if "pants_jeans_short" in cs_existing_stock:
            $ wr_bottoms_pants.append("pants_jeans_short")
        #if "pants_retro_shorts" in cs_existing_stock:
        #    $ wr_bottoms_pants.append("pants_retro_shorts")
        if hg_rocker_OBJ.purchased:
            $ wr_bottoms_pants.append("pants_rocker")

    #if active_girl == "luna":

    #if active_girl == "astoria":

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
        $ wr_neckwears.append("neck_tie_striped")
        if reward_her_wool_clothing:
            $ wr_neckwears.append("neck_scarf_striped")
        if whoring >= 14:
            $ wr_neckwears.append("neck_banner")
            $ wr_neckwears.append("neck_leather_collar")
        if whoring >= 17:
            $ wr_neckwears.append("neck_bondage_collar")

        if whoring >= 7 and hg_rocker_OBJ.purchased:
            $ wr_neckwears.append("neck_lace_choker")
        if whoring >= 7 and hg_ballDress_OBJ.purchased:
            $ wr_neckwears.append("neck_pearl_necklace")
        if whoring >= 16 and hg_christmas_OBJ.purchased:
            $ wr_neckwears.append("neck_xmas")

        if whoring >= 20 and hg_ballDress_OBJ.purchased:
            $ wr_neckwears.append("neck_miss_hogwarts")
        #$ wr_neckwears.append("neck_goggles") #sQuest reward
        if collar == 1:
            $ wr_neckwears.append("neck_slave_shackle") #sQuest collar reward
        if collar == 2:
            $ wr_neckwears.append("neck_slut_shackle") #sQuest collar reward
        if collar == 3:
            $ wr_neckwears.append("neck_whore_shackle") #sQuest collar reward

        #Body Accessories
        if "SPEW_badge" in cs_existing_stock:
            $ wr_body_accs.append("badge_SPEW")
        if "CUM_badge" in cs_existing_stock:
            $ wr_body_accs.append("badge_I_love_cum")
        if whoring >= 24:
            $ wr_body_accs.append("belt_band_of_condoms")

        #Gloves
        if reward_her_wool_clothing:
            $ wr_gloves.append("gloves_wool_short")
        if whoring >= 10:
            $ wr_gloves.append("gloves_lace")
        if whoring >= 19:
            $ wr_gloves.append("gloves_latex")

        if whoring >= 13 and hg_maid_OBJ.purchased:
            $ wr_gloves.append("gloves_french_maid")
        if whoring >= 13 and hg_laraCroft_OBJ.purchased:
            $ wr_gloves.append("gloves_leather_short")
        #if whoring >= 19 and hg_powerGirl_OBJ.purchased:
        #    $ wr_gloves.append("gloves_latex_hero_blue")
        if whoring >= 22 and hg_harleyQuinn_OBJ.purchased:
            $ wr_gloves.append("gloves_leather")
        #$ wr_gloves.append("gloves_egyptian") #ADD Egypt Outfit

        #Stockings
        if reward_her_wool_clothing:
            $ wr_stockings.append("stockings_striped")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_striped_vibe") #Will be in accessories instead
        if whoring >= 8 and (hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased):
            $ wr_stockings.append("stockings_cheer")
            $ wr_stockings.append("stockings_cheer_short")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_cheer_vibe") #Will be in accessories instead
 
        if whoring >= 5:
            $ wr_stockings.append("stockings_pantyhose")
            $ wr_stockings.append("stockings_cute")
        if whoring >= 17:
            $ wr_stockings.append("stockings_high")
        if whoring >= 20:
            $ wr_stockings.append("stockings_latex")

        if "stockings_lace_black" in cs_existing_stock:
            $ wr_stockings.append("stockings_lace")

        if "stockings_fishnet_black" in cs_existing_stock:
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

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Underwear List ###
label update_wr_underwear_list:

    $ wr_bras = []
    $ wr_panties = []
    $ wr_onepieces = []
    $ wr_garterbelts = []


    if active_girl == "hermione":

        #Bra
        if whoring >= 10:
            $ wr_bras.append("bra_base")
            $ wr_bras.append("bra_silk")
            $ wr_bras.append("bra_lace")

        if whoring >= 16:
            $ wr_bras.append("bra_bikini_string")
            $ wr_bras.append("bra_bikini")

        if whoring >= 19:
            $ wr_bras.append("bra_latex")
            $ wr_bras.append("bra_french_maid")

        if whoring >= 22:
            $ wr_bras.append("bra_tape")

        if whoring >= 22 and "top_fishnets" in cs_existing_stock:
            $ wr_bras.append("top_fishnets")

        #Panties
        if whoring >= 10:
            $ wr_panties.append("panties_base")
            $ wr_panties.append("panties_silk")
            $ wr_panties.append("panties_silk_low")
            $ wr_panties.append("panties_lace")

        if whoring >= 16:
            $ wr_panties.append("panties_bikini_string")
            $ wr_panties.append("panties_bikini")
            $ wr_panties.append("panties_latex")

        if whoring >= 19:
            $ wr_panties.append("panties_french_maid")
            $ wr_panties.append("panties_fishnet_string")

        #One-Pieces & Nighties
        $ wr_onepieces.append("onepiece_swimsuit_halterless")
        $ wr_onepieces.append("onepiece_swimsuit")
        $ wr_onepieces.append("onepiece_bunny")
        $ wr_onepieces.append("onepiece_microdress")
        $ wr_onepieces.append("onepiece_bikini_string")

        if whoring >= 19: #and "" in cs_existing_stock:
            $ wr_onepieces.append("nighty_short")
            $ wr_onepieces.append("nighty_long")
            $ wr_onepieces.append("nighty_dress")

        #Garterbelts
        if whoring >= 10: #and "garterbelt_lace" in cs_existing_stock:
            $ wr_garterbelts.append("garterbelt_lace")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Outfits List ###
label update_wr_outfits_list:

    $ wr_outfits = []
    $ wr_costumes = []
    $ wr_outfits_onepieces = []
    $ wr_swimsuits = []
    $ wr_dresses = []


    if active_girl == "hermione":

        #Outfits
        $ hg_purchased_outfits = []
        if hg_maid_OBJ.purchased:
            $ wr_outfits.append("maid")
            $ hg_purchased_outfits.append(hg_maid_OBJ)
        if hg_gryffCheer_OBJ.purchased:
            $ wr_outfits.append("cheer")
            $ hg_purchased_outfits.append(hg_gryffCheer_OBJ)
        if hg_slythCheer_OBJ.purchased:
            $ wr_outfits.append("s_cheer")
            $ hg_purchased_outfits.append(hg_slythCheer_OBJ)
        if hg_christmas_OBJ.purchased:
            $ wr_outfits.append("christmas")
            $ hg_purchased_outfits.append(hg_christmas_OBJ)
        if hg_present_OBJ.purchased:
            $ wr_outfits.append("present")
            $ hg_purchased_outfits.append(hg_present_OBJ)
        if hg_rocker_OBJ.purchased:
            $ wr_outfits.append("rocker")
            $ hg_purchased_outfits.append(hg_rocker_OBJ)
        if hg_japan_OBJ.purchased:
            $ wr_outfits.append("japan")
            $ hg_purchased_outfits.append(hg_japan_OBJ)

        #Costumes
        $ hg_purchased_costumes = []
        if hg_pirate_OBJ.purchased:
            $ wr_costumes.append("pirate")
            $ hg_purchased_costumes.append(hg_pirate_OBJ)
        if hg_powerGirl_OBJ.purchased:
            $ wr_costumes.append("power")
            $ hg_purchased_costumes.append(hg_powerGirl_OBJ)
        if whoring >= 7 and hg_msMarvel_OBJ.purchased:
            $ wr_costumes.append("marvel")
            $ hg_purchased_costumes.append(hg_msMarvel_OBJ)
        if hg_harleyQuinn_OBJ.purchased:
            $ wr_costumes.append("harley")
            $ hg_purchased_costumes.append(hg_harleyQuinn_OBJ)
        if hg_laraCroft_OBJ.purchased:
            $ wr_costumes.append("lara")
            $ hg_purchased_costumes.append(hg_laraCroft_OBJ)
        if hg_tifa_OBJ.purchased:
            $ wr_costumes.append("tifa")
            $ hg_purchased_costumes.append(hg_tifa_OBJ)
        if hg_witch_OBJ.purchased:
            $ wr_costumes.append("witch")
            $ hg_purchased_costumes.append(hg_witch_OBJ)

        #One-Pieces
        #$ hg_purchased_onepieces = []
        #if hg_silkNightgown_OBJ.purchased:
        #    $ wr_outfits_onepieces.append("nightgown")
        #    $ hg_purchased_onepieces.append(hg_silkNightgown_OBJ)

        #Swimsuits
        $ hg_purchased_swimsuits = []
        #if .purchased:
        #    $ wr_swimsuits.append("")
        #    $ hg_purchased_swimsuits.append()

        #Dresses
        $ hg_purchased_dresses = []
        if hg_heartDancer_OBJ.purchased:
            $ wr_dresses.append("heart")
            $ hg_purchased_dresses.append(hg_heartDancer_OBJ)
        if hg_ballDress_OBJ.purchased:
            $ wr_dresses.append("ball_dress")
            $ hg_purchased_dresses.append(hg_ballDress_OBJ)

    #if active_girl == "luna":

    #if active_girl == "astoria":

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
        
        if "Polyjuice Potion" in p_inv or "Cat Transformation Potion" in p_inv or "Luna Transformation Potion" or "Clone Potion" in p_inv:
            $ wr_potions_list.append("polyjuice_potion")
        if "Expanding Elixir" in p_inv or "Breast Expansion Potion" in p_inv or "Ass Expansion Potion" in p_inv:
            $ wr_potions_list.append("expanding_elixir")
        if "Milk Potion" in p_inv:
            $ wr_potions_list.append("milk_potion")
        if "Cum Addiction Potion" in p_inv or "Hypno Potion" in p_inv:
            $ wr_potions_list.append("love_potion")
        if "Transparency Potion" in p_inv:
            $ wr_potions_list.append("clothes_potion")

        #Items #Butt-plugs, Gags, Brooms,...
        
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
=======

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
        if "blonde_dye" in cs_existing_stock:
            $ wr_haircolor.append("2")
        if "red_dye" in cs_existing_stock:
            $ wr_haircolor.append("3")
        if "crimson_dye" in cs_existing_stock:
            $ wr_haircolor.append("4")
        if "black_dye" in cs_existing_stock:
            $ wr_haircolor.append("5")

        if "green_dye" in cs_existing_stock:
            $ wr_haircolor.append("6")
        if "blue_dye" in cs_existing_stock:
            $ wr_haircolor.append("7")
        if "purple_dye" in cs_existing_stock:
            $ wr_haircolor.append("8")
        if "pink_dye" in cs_existing_stock:
            $ wr_haircolor.append("9")
        if "white_dye" in cs_existing_stock:
            $ wr_haircolor.append("10")


    #House Color
    $ wr_housecolor = []

    if active_girl == "hermione":
        if "blue_dye" in cs_existing_stock:
            $ wr_housecolor.append("blue")
        if "green_dye" in cs_existing_stock:
            $ wr_housecolor.append("green")
        if "red_dye" in cs_existing_stock:
            $ wr_housecolor.append("red")
        if "blonde_dye" in cs_existing_stock:
            $ wr_housecolor.append("yellow")


    #Cloth Color
    $ wr_clothcolor = []

    if active_girl == "hermione":
        if "blue_dye" in cs_existing_stock:
            $ wr_clothcolor.append("dark_blue")
        if "green_dye" in cs_existing_stock:
            $ wr_clothcolor.append("dark_green")
        if "red_dye" in cs_existing_stock:
            $ wr_clothcolor.append("crimson")
        if "blonde_dye" in cs_existing_stock:      #Temp name
            $ wr_clothcolor.append("orange")
        if "purple_dye" in cs_existing_stock:
            $ wr_clothcolor.append("purple")
        if "black_dye" in cs_existing_stock:    #Temp name
            $ wr_clothcolor.append("brown")
        if "black_dye" in cs_existing_stock:
            $ wr_clothcolor.append("black")

        if "blue_dye" in cs_existing_stock:
            $ wr_clothcolor.append("blue")
        if "green_dye" in cs_existing_stock:
            $ wr_clothcolor.append("green")
        if "red_dye" in cs_existing_stock:
            $ wr_clothcolor.append("red")
        if "blonde_dye" in cs_existing_stock:
            $ wr_clothcolor.append("yellow")
        if "pink_dye" in cs_existing_stock:
            $ wr_clothcolor.append("pink")
        if "black_dye" in cs_existing_stock:    #Temp name
            $ wr_clothcolor.append("gray")
        if "white_dye" in cs_existing_stock:
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
        $ wr_hair.append("B")
        #if hg_ ADD _OBJ.purchased: #Add Elizabeth Outfit.
        $ wr_hair.append("E")

        #Makeup
        $ wr_makeup.append("lipstick")
        if "freckles" in cs_existing_stock:
            $ wr_makeup.append("freckles")
        if "fake_cum" in cs_existing_stock:
            $ wr_makeup.append("fake_cum")

        #Glasses
        if "reading_glasses" in cs_existing_stock:
            $ wr_glasses.append("reading_glasses")
        if "vintage_glasses" in cs_existing_stock:
            $ wr_glasses.append("vintage_glasses")

        #Ears
        if "cat_ears" in cs_existing_stock:
            $ wr_ears.append("cat_ears")
        if "elf_ears" in cs_existing_stock:
            $ wr_ears.append("elf_ears")

        #Hats
        if hg_ballDress_OBJ.purchased:
            $ wr_hats.append("tiara")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Tops List ###
label update_wr_tops_list:

    $ wr_tops_uniform = [] #ADD school clothing and cheerleader tops,...
    $ wr_tops_normal = []  #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    $ wr_tops_wicked = []  #ADD kinky clothing items like leather, fishnet
    $ wr_tops_misc = []    #ADD Misc top items


    if active_girl == "hermione":

        #Uniform
        $ wr_tops_uniform.append("uni_top_1")
        $ wr_tops_uniform.append("uni_top_2")
        if whoring < 11:
            $ wr_tops_uniform.append("uni_top_3")
        $ wr_tops_uniform.append("uni_top_4")
        if whoring >= 11:
            $ wr_tops_uniform.append("uni_top_5")
        $ wr_tops_uniform.append("uni_top_6")

        if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased:
            $ wr_tops_uniform.append("uni_top_cheer")
            $ wr_tops_uniform.append("uni_top_cheer_skimpy")

        #Muggle
        if "normal_pullover" in cs_existing_stock:
            $ wr_tops_normal.append("normal_pullover")
            $ wr_tops_normal.append("normal_pullover_sexy")
        if "normal_sweater" in cs_existing_stock:
            $ wr_tops_normal.append("normal_sweater")
        #if "normal_waitress_top" in cs_existing_stock:
        #    $ wr_tops_normal.append("normal_waitress_top")

        #Wicked
        if "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_short_sleeves")
            $ wr_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
        if "wicked_leather_jacket_sleeveless" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeveless")
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
        if "wicked_leather_jacket_sleeves" in cs_existing_stock:
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeves")
            $ wr_tops_wicked.append("wicked_leather_jacket_sleeves_open")

        if hg_rocker_OBJ.purchased:
            $ wr_tops_wicked.append("wicked_rocker_top")
        if whoring >= 19 and "top_fishnets" in cs_existing_stock:
            $ wr_tops_wicked.append("top_fishnets")

        #Misc. Tops
        #if whoring >= 17:
        #    $ wr_tops_misc.append("top_ripped_tie_striped")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Bottoms List ###
label update_wr_bottoms_list:

    $ wr_bottoms_uniform = []
    $ wr_bottoms_uniform_low = []  #Add low hanging school skirts
    $ wr_bottoms_skirts = []       #Add skirts
    $ wr_bottoms_pants = []        #Add
    $ wr_bottoms_misc = []         #ADD Misc bottom items


    if active_girl == "hermione":

        #Uniform
        $ wr_bottoms_uniform.append("uni_skirt_1")
        $ wr_bottoms_uniform.append("uni_skirt_2")
        $ wr_bottoms_uniform.append("uni_skirt_3")
        $ wr_bottoms_uniform.append("uni_skirt_4")
        $ wr_bottoms_uniform.append("uni_skirt_5")

        if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased:
            $ wr_bottoms_uniform.append("uni_skirt_cheer")
            $ wr_bottoms_uniform.append("uni_skirt_cheer_skimpy")

        #Uniform Low
        $ wr_bottoms_uniform_low.append("uni_skirt_1_low")
        $ wr_bottoms_uniform_low.append("uni_skirt_2_low")
        $ wr_bottoms_uniform_low.append("uni_skirt_3_low")
        #if micro_skirt unlocked/purchased:
        #$ wr_bottoms_uniform_low.append("uni_skirt_4_low") #micro skirt

        #Skirts
        if "skirt_belted_mini" in cs_existing_stock:
            $ wr_bottoms_skirts.append("skirt_belted_mini")
        if "skirt_belted_micro" in cs_existing_stock:
            $ wr_bottoms_skirts.append("skirt_belted_micro")

        #Pants
        if "pants_jeans_long" in cs_existing_stock:
            $ wr_bottoms_pants.append("pants_jeans_long")
        if "pants_jeans_short" in cs_existing_stock:
            $ wr_bottoms_pants.append("pants_jeans_short")
        #if "pants_retro_shorts" in cs_existing_stock:
        #    $ wr_bottoms_pants.append("pants_retro_shorts")
        if hg_rocker_OBJ.purchased:
            $ wr_bottoms_pants.append("pants_rocker")

    #if active_girl == "luna":

    #if active_girl == "astoria":

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
        $ wr_neckwears.append("neck_tie_striped")
        if reward_her_wool_clothing:
            $ wr_neckwears.append("neck_scarf_striped")
        if whoring >= 14:
            $ wr_neckwears.append("neck_banner")
            $ wr_neckwears.append("neck_leather_collar")
        if whoring >= 17:
            $ wr_neckwears.append("neck_bondage_collar")

        if whoring >= 7 and hg_rocker_OBJ.purchased:
            $ wr_neckwears.append("neck_lace_choker")
        if whoring >= 7 and hg_ballDress_OBJ.purchased:
            $ wr_neckwears.append("neck_pearl_necklace")
        if whoring >= 16 and hg_christmas_OBJ.purchased:
            $ wr_neckwears.append("neck_xmas")

        if whoring >= 20 and hg_ballDress_OBJ.purchased:
            $ wr_neckwears.append("neck_miss_hogwarts")
        #$ wr_neckwears.append("neck_goggles") #sQuest reward
        if collar == 1:
            $ wr_neckwears.append("neck_slave_shackle") #sQuest collar reward
        if collar == 2:
            $ wr_neckwears.append("neck_slut_shackle") #sQuest collar reward
        if collar == 3:
            $ wr_neckwears.append("neck_whore_shackle") #sQuest collar reward

        #Body Accessories
        if "SPEW_badge" in cs_existing_stock:
            $ wr_body_accs.append("badge_SPEW")
        if "CUM_badge" in cs_existing_stock:
            $ wr_body_accs.append("badge_I_love_cum")
        if whoring >= 24:
            $ wr_body_accs.append("belt_band_of_condoms")

        #Gloves
        if reward_her_wool_clothing:
            $ wr_gloves.append("gloves_wool_short")
        if whoring >= 10:
            $ wr_gloves.append("gloves_lace")
        if whoring >= 19:
            $ wr_gloves.append("gloves_latex")

        if whoring >= 13 and hg_maid_OBJ.purchased:
            $ wr_gloves.append("gloves_french_maid")
        if whoring >= 13 and hg_laraCroft_OBJ.purchased:
            $ wr_gloves.append("gloves_leather_short")
        #if whoring >= 19 and hg_powerGirl_OBJ.purchased:
        #    $ wr_gloves.append("gloves_latex_hero_blue")
        if whoring >= 22 and hg_harleyQuinn_OBJ.purchased:
            $ wr_gloves.append("gloves_leather")
        #$ wr_gloves.append("gloves_egyptian") #ADD Egypt Outfit

        #Stockings
        if reward_her_wool_clothing:
            $ wr_stockings.append("stockings_striped")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_striped_vibe") #Will be in accessories instead
        if whoring >= 8 and (hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased):
            $ wr_stockings.append("stockings_cheer")
            $ wr_stockings.append("stockings_cheer_short")
            #if whoring  >= 22 and "vibrators" in cs_existing_stock:
            #    $ wr_stockings.append("stockings_cheer_vibe") #Will be in accessories instead
 
        if whoring >= 5:
            $ wr_stockings.append("stockings_pantyhose")
            $ wr_stockings.append("stockings_cute")
        if whoring >= 17:
            $ wr_stockings.append("stockings_high")
        if whoring >= 20:
            $ wr_stockings.append("stockings_latex")

        if "stockings_lace_black" in cs_existing_stock:
            $ wr_stockings.append("stockings_lace")

        if "stockings_fishnet_black" in cs_existing_stock:
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

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Underwear List ###
label update_wr_underwear_list:

    $ wr_bras = []
    $ wr_panties = []
    $ wr_onepieces = []
    $ wr_garterbelts = []


    if active_girl == "hermione":

        #Bra
        if whoring >= 10:
            $ wr_bras.append("bra_base")
            $ wr_bras.append("bra_silk")
            $ wr_bras.append("bra_lace")

        if whoring >= 16:
            $ wr_bras.append("bra_bikini_string")
            $ wr_bras.append("bra_bikini")

        if whoring >= 19:
            $ wr_bras.append("bra_latex")
            $ wr_bras.append("bra_french_maid")

        if whoring >= 22:
            $ wr_bras.append("bra_tape")

        if whoring >= 22 and "top_fishnets" in cs_existing_stock:
            $ wr_bras.append("top_fishnets")

        #Panties
        if whoring >= 10:
            $ wr_panties.append("panties_base")
            $ wr_panties.append("panties_silk")
            $ wr_panties.append("panties_silk_low")
            $ wr_panties.append("panties_lace")

        if whoring >= 16:
            $ wr_panties.append("panties_bikini_string")
            $ wr_panties.append("panties_bikini")
            $ wr_panties.append("panties_latex")

        if whoring >= 19:
            $ wr_panties.append("panties_french_maid")
            $ wr_panties.append("panties_fishnet_string")

        #One-Pieces & Nighties
        $ wr_onepieces.append("onepiece_swimsuit_halterless")
        $ wr_onepieces.append("onepiece_swimsuit")
        $ wr_onepieces.append("onepiece_bunny")
        $ wr_onepieces.append("onepiece_microdress")
        $ wr_onepieces.append("onepiece_bikini_string")

        if whoring >= 19: #and "" in cs_existing_stock:
            $ wr_onepieces.append("nighty_short")
            $ wr_onepieces.append("nighty_long")
            $ wr_onepieces.append("nighty_dress")

        #Garterbelts
        if whoring >= 10: #and "garterbelt_lace" in cs_existing_stock:
            $ wr_garterbelts.append("garterbelt_lace")

    #if active_girl == "luna":

    #if active_girl == "astoria":

    return


### Outfits List ###
label update_wr_outfits_list:

    $ wr_outfits = []
    $ wr_costumes = []
    $ wr_outfits_onepieces = []
    $ wr_swimsuits = []
    $ wr_dresses = []


    if active_girl == "hermione":

        #Outfits
        $ hg_purchased_outfits = []
        if hg_maid_OBJ.purchased:
            $ wr_outfits.append("maid")
            $ hg_purchased_outfits.append(hg_maid_OBJ)
        if hg_gryffCheer_OBJ.purchased:
            $ wr_outfits.append("cheer")
            $ hg_purchased_outfits.append(hg_gryffCheer_OBJ)
        if hg_slythCheer_OBJ.purchased:
            $ wr_outfits.append("s_cheer")
            $ hg_purchased_outfits.append(hg_slythCheer_OBJ)
        if hg_christmas_OBJ.purchased:
            $ wr_outfits.append("christmas")
            $ hg_purchased_outfits.append(hg_christmas_OBJ)
        if hg_present_OBJ.purchased:
            $ wr_outfits.append("present")
            $ hg_purchased_outfits.append(hg_present_OBJ)
        if hg_rocker_OBJ.purchased:
            $ wr_outfits.append("rocker")
            $ hg_purchased_outfits.append(hg_rocker_OBJ)
        if hg_japan_OBJ.purchased:
            $ wr_outfits.append("japan")
            $ hg_purchased_outfits.append(hg_japan_OBJ)

        #Costumes
        $ hg_purchased_costumes = []
        if hg_pirate_OBJ.purchased:
            $ wr_costumes.append("pirate")
            $ hg_purchased_costumes.append(hg_pirate_OBJ)
        if hg_powerGirl_OBJ.purchased:
            $ wr_costumes.append("power")
            $ hg_purchased_costumes.append(hg_powerGirl_OBJ)
        if whoring >= 7 and hg_msMarvel_OBJ.purchased:
            $ wr_costumes.append("marvel")
            $ hg_purchased_costumes.append(hg_msMarvel_OBJ)
        if hg_harleyQuinn_OBJ.purchased:
            $ wr_costumes.append("harley")
            $ hg_purchased_costumes.append(hg_harleyQuinn_OBJ)
        if hg_laraCroft_OBJ.purchased:
            $ wr_costumes.append("lara")
            $ hg_purchased_costumes.append(hg_laraCroft_OBJ)
        if hg_tifa_OBJ.purchased:
            $ wr_costumes.append("tifa")
            $ hg_purchased_costumes.append(hg_tifa_OBJ)
        if hg_witch_OBJ.purchased:
            $ wr_costumes.append("witch")
            $ hg_purchased_costumes.append(hg_witch_OBJ)

        #One-Pieces
        #$ hg_purchased_onepieces = []
        #if hg_silkNightgown_OBJ.purchased:
        #    $ wr_outfits_onepieces.append("nightgown")
        #    $ hg_purchased_onepieces.append(hg_silkNightgown_OBJ)

        #Swimsuits
        $ hg_purchased_swimsuits = []
        #if .purchased:
        #    $ wr_swimsuits.append("")
        #    $ hg_purchased_swimsuits.append()

        #Dresses
        $ hg_purchased_dresses = []
        if hg_heartDancer_OBJ.purchased:
            $ wr_dresses.append("heart")
            $ hg_purchased_dresses.append(hg_heartDancer_OBJ)
        if hg_ballDress_OBJ.purchased:
            $ wr_dresses.append("ball_dress")
            $ hg_purchased_dresses.append(hg_ballDress_OBJ)

    #if active_girl == "luna":

    #if active_girl == "astoria":

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
        
        if "Polyjuice Potion" in p_inv or "Cat Transformation Potion" in p_inv or "Luna Transformation Potion" or "Clone Potion" in p_inv:
            $ wr_potions_list.append("polyjuice_potion")
        if "Expanding Elixir" in p_inv or "Breast Expansion Potion" in p_inv or "Ass Expansion Potion" in p_inv:
            $ wr_potions_list.append("expanding_elixir")
        if "Milk Potion" in p_inv:
            $ wr_potions_list.append("milk_potion")
        if "Cum Addiction Potion" in p_inv or "Hypno Potion" in p_inv:
            $ wr_potions_list.append("love_potion")
        if "Transparency Potion" in p_inv:
            $ wr_potions_list.append("clothes_potion")

        #Items #Butt-plugs, Gags, Brooms,...
        if gift_item_inv[AnalPlugs.id] > 0:
            $ wr_items_list.append("buttplugs")
        
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
>>>>>>> Persistants-and-buttplug-change
