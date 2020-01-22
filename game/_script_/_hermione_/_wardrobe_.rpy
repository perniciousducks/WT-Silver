###############
## Character ##
###############

default hermione = Doll(name="hermione", 
                        clothes={"hat":        [None, 15, True],
                                 "hair":       [None, 4, True],
                                 "earring":    [None, 14, True],
                                 "neckwear":   [None, 16, True],
                                 "robe":       [None, 22, True],
                                 "gloves":     [None, 14, True],
                                 "top":        [None, 15, True],
                                 "bra":        [None, 9, True],
                                 "bottom":     [None, 8, True],
                                 "garterbelt": [None, 7, True],
                                 "panties":    [None, 6, True],
                                 "stockings":  [None, 5, True],
                                 "buttplug":   [None, -1, True],
                                 "pubes":      [None, 3, True],
                                 "tattoo0":    [None, 1, True],
                                 "tattoo1":    [None, 1, True],
                                 "tattoo2":    [None, 1, True],
                                 "tattoo3":    [None, 1, True],
                                 "tattoo4":    [None, 1, True],
                                 "piercing0":  [None, 2, True],
                                 "piercing1":  [None, 2, True],
                                 "piercing2":  [None, 2, True],
                                 "piercing3":  [None, 2, True],
                                 "piercing4":  [None, 2, True],
                                 "accessory0": [None, 12, True],
                                 "accessory1": [None, 12, True],
                                 "accessory2": [None, 12, True],
                                 "accessory3": [None, 12, True],
                                 "accessory4": [None, 12, True],
                                 "makeup0":    [None, 3, True],
                                 "makeup1":    [None, 3, True],
                                 "makeup2":    [None, 3, True],
                                 "makeup3":    [None, 3, True],
                                 "makeup4":    [None, 3, True]},
                        face={"tears":    [None, 12, True],
                              "cheeks":   [None, 7, True],
                              "eyebrows": ["base", 11, True],
                              "eyes":     ["base", 8, True],
                              "pupils":   ["mid", 9, True],
                              "mouth":    ["base", 13, True]},
                        body={"armleft": ["down", 3], 
                              "armright":["down", 0], 
                              "base":    ["front", 1], 
                              "breasts": ["normal", 2]})
                              
###############
##   Hair    ##
###############

default her_hair_base = DollCloth("hermione", ("head", "hair"), "hair", "base", [[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]])

################
## Schoolgirl ##
################

default her_top_school1 = DollCloth("hermione", ("tops", "school"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_top_school2 = DollCloth("hermione", ("tops", "school"), "top", "top_school_2", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_top_school3 = DollCloth("hermione", ("tops", "school"), "top", "top_school_3", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_top_school4 = DollCloth("hermione", ("tops", "school"), "top", "top_school_4", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_top_school5 = DollCloth("hermione", ("tops", "school"), "top", "top_school_5", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_top_school6 = DollCloth("hermione", ("tops", "school"), "top", "top_school_6", [[109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]])
default her_bottom_school1 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]])
default her_bottom_school2 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]])
default her_bottom_school3 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]])
default her_bottom_school4 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]])
default her_stockings_base1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "stockings_1", [[219, 165, 13, 255], [146, 63, 30, 255]])
default her_panties_base1 = DollCloth("hermione", ("panties", "panties"), "panties", "basic_panties_1", [[232, 232, 232, 255], [202, 60, 1, 255]])
default her_bra_base1 = DollCloth("hermione", ("bras", "bras"), "bra", "basic_bra_1", [[232, 232, 232, 255], [202, 60, 1, 255], [167, 77, 42, 255], [237, 179, 14, 255]])

default her_accessory_house_emblem = DollCloth("hermione", ("misc", "accessory"), "accessory0", "house_emblem", [[167, 77, 42, 255], [237, 179, 14, 255]], zorder=16)

default her_outfit_default = DollOutfit([her_hair_base, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1, her_accessory_house_emblem], True)
default her_outfit_default_no_vest = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1, her_accessory_house_emblem], True)
default her_outfit_default_no_tie_open_shirt = DollOutfit([her_hair_base, her_top_school5, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1, her_accessory_house_emblem], True)
default her_outfit_last = DollOutfit([her_hair_base])

###########################
## Leather Bikini Outfit ##
###########################
default her_panties_bikini1 = DollCloth("hermione", ("panties", "panties"), "panties", "bikini_panties_1", [[138, 0, 0, 255], [252, 135, 0, 255]])
default her_bra_bikini1 = DollCloth("hermione", ("bras", "bras"), "bra", "bikini_bra_1", [[138, 0, 0, 255], [252, 135, 0, 255]])

default her_outfit_bikini1 = DollOutfit([her_hair_base, her_panties_bikini1, her_bra_bikini1], price=100)

########################
## Rave Bikini Outfit ##
########################

default her_panties_bikini2 = DollCloth("hermione", ("panties", "panties"), "panties", "bikini_panties_2", [[55, 55, 55, 255], [197, 142, 35, 255]])
default her_bra_bikini2 = DollCloth("hermione", ("bras", "bras"), "bra", "bikini_bra_2", [[55, 55, 55, 255], [197, 142, 35, 255]])

default her_outfit_bikini2 = DollOutfit([her_hair_base, her_panties_bikini2, her_bra_bikini2], price=100)

#################
## Maid Outfit ##
#################

default her_top_maid1 = DollCloth("hermione", ("tops", "school"), "top", "maid_dress_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]])
default her_stockings_maid1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "maid_stockings_1", [[53, 33, 30, 255]])
default her_hat_maid1 = DollCloth("hermione", ("head", "hats"), "hat", "maid_hat_1", [[236, 243, 244, 255]])
default her_neckwear_maid1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_1", [[40, 51, 61, 255], [236, 243, 244, 255]])
default her_neckwear_maid2 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_2", [[236, 243, 244, 255]])
default her_gloves_maid1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "maid_gloves_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]])

default her_outfit_maid = DollOutfit([her_hair_base, her_top_maid1, her_stockings_maid1, her_hat_maid1, her_neckwear_maid1, her_neckwear_maid2, her_gloves_maid1], price=250)

##################
## Poker Outfit ##
##################

default her_hat_poker1 = DollCloth("hermione", ("head", "hats"), "hat", "poker_hat_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]])
default her_hat_poker2 = DollCloth("hermione", ("head", "hats"), "hat", "poker_hat_2", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]])
default her_neckwear_poker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "poker_bowtie_1", [[232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]])
default her_stockings_poker1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_1", [[26, 26, 35, 255], [153, 22, 10, 255]])
default her_stockings_poker2 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_2", [[26, 26, 35, 255], [153, 22, 10, 255]])
default her_panties_poker1 = DollCloth("hermione", ("panties", "panties"), "panties", "poker_panties_1", [[26, 26, 35, 255], [153, 22, 10, 255], [255, 179, 3, 255]])
default her_bra_poker1 = DollCloth("hermione", ("bras", "bras"), "bra", "poker_bra_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]], blacklist=["panties", "top", "bottom"])
default her_gloves_poker1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "poker_gloves_1", [[232, 232, 232, 255], [255, 179, 3, 255]])
default her_earring_poker1 = DollCloth("hermione", ("head", "earrings"), "earring", "poker_earring_1", [[255, 179, 3, 255]])
default her_piercing2_poker1 = DollCloth("hermione", ("torso", "piercing"), "piercing2", "poker_belly_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]])

default her_outfit_poker = DollOutfit([her_hair_base, her_hat_poker1, her_hat_poker2, her_neckwear_poker1, her_stockings_poker1, her_stockings_poker2, her_panties_poker1, her_bra_poker1, her_gloves_poker1, her_earring_poker1, her_piercing2_poker1], price=250)

##################
## Bunny Outfit ##
##################

default her_top_bunny1 = DollCloth("hermione", ("tops", "school"), "top", "bunny_top_1", [[48, 48, 48, 255]], blacklist=["panties", "bra"], zorder=7)
default her_stockings_bunny1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "bunny_stockings_1", [[81, 81, 81, 255]])
default her_tattoo3_bunny1 = DollCloth("hermione", ("hips", "tattoos"), "tattoo3", "bunny_tattoo1", [[0, 0, 1, 255]])
default her_hat_bunny1 = DollCloth("hermione", ("head", "hats"), "hat", "bunny_hat_1", [[48, 48, 48, 255], [232, 232, 232, 255]])
default her_gloves_bunny1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "bunny_gloves_1", [[232, 232, 232, 255]])
default her_neckwear_bunny1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", [[232, 232, 232, 255], [48, 48, 48, 255]])

default her_outfit_bunny = DollOutfit([her_hair_base, her_top_bunny1, her_stockings_bunny1, her_tattoo3_bunny1, her_hat_bunny1, her_gloves_bunny1, her_neckwear_bunny1], price=250)

################
## Ball Dress ##
################

default her_top_ball1 = DollCloth("hermione", ("tops", "school"), "top", "ball_dress_1", [[240, 120, 161, 255], [247, 222, 231, 255]], blacklist=["bottom"])
#default her_gloves_bunny1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "bunny_gloves_1", [[232, 232, 232, 255]])
default her_earring_pearls1 = DollCloth("hermione", ("head", "earrings"), "earring", "pearl_1", [[233, 166, 253, 255]])
default her_neckwear_pearls1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "ball_pearls_1", [[233, 166, 253, 255]])
default her_accessory_ball_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "ball_sash", [[247, 222, 231, 255], [161, 82, 159, 255]], zorder=16)

default her_outfit_ball = DollOutfit([her_hair_base, her_neckwear_pearls1, her_top_ball1, her_earring_pearls1, her_accessory_ball_sash1], price=1000)

#####################
## Yennefer Outfit ##
#####################

default her_top_yen1 = DollCloth("hermione", ("tops", "school"), "top", "yen_top", [[9, 32, 47, 255]])
default her_bottom_yen_skirt1 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "yen_skirt", [[26, 26, 26, 255]])
default her_stockings_yen1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "yen_stockings", [[76, 76, 76, 255]])
default her_accessory_yen_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "yen_sash", [[25, 25, 25, 255], [51, 51, 51, 255]], zorder=9)
default her_accessory_yen_belt1 = DollCloth("hermione", ("misc", "accessory"), "accessory3", "yen_belt", [[52, 37, 31, 255], [146, 142, 137, 255]], zorder=10)
default her_accessory_yen_feathers1 = DollCloth("hermione", ("misc", "accessory"), "accessory2", "yen_feathers", [[42, 190, 199, 255]], zorder=16)
default her_accessory_yen_scarf1 = DollCloth("hermione", ("misc", "accessory"), "accessory1", "yen_scarf", [[9, 32, 47, 255]], zorder=17)
default her_accessory_yen_corset1 = DollCloth("hermione", ("misc", "accessory"), "accessory0", "yen_corset", [[37, 27, 27, 255], [19, 14, 11, 255]], zorder=16)
default her_neckwear_yen_choker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "yen_choker", [[30, 29, 28, 255]])
default her_gloves_yen1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "yen_gloves", [[52, 37, 31, 255]], zorder=16)

default her_outfit_yennefer = DollOutfit([her_hair_base, her_top_yen1, her_bottom_yen_skirt1, her_accessory_yen_sash1, her_stockings_yen1, her_accessory_yen_feathers1, her_accessory_yen_scarf1, her_neckwear_yen_choker1, her_gloves_yen1, her_accessory_yen_corset1, her_accessory_yen_belt1], price=250)