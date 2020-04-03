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

default her_hair_base = DollCloth("hermione", ("head", "hair"), "hair", "base", [[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]], unlocked=True)

################
## Schoolgirl ##
################

default her_top_school1 = DollCloth("hermione", ("tops", "school"), "top", "top_school_1", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school2 = DollCloth("hermione", ("tops", "school"), "top", "top_school_2", [[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school3 = DollCloth("hermione", ("tops", "school"), "top", "top_school_3", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)
default her_top_school4 = DollCloth("hermione", ("tops", "school"), "top", "top_school_4", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=4)
default her_top_school5 = DollCloth("hermione", ("tops", "school"), "top", "top_school_5", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
default her_top_school6 = DollCloth("hermione", ("tops", "school"), "top", "top_school_6", [[109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=10)
default her_top_school7 = DollCloth("hermione", ("tops", "school"), "top", "top_school_7", [[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True, level=13)
default her_bottom_school1 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_1", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True)
default her_bottom_school2 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_2", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=4)
default her_bottom_school3 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_3", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=10)
default her_bottom_school4 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "school_skirt_4", [[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=True, level=19)
default her_stockings_base1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "stockings_1", [[219, 165, 13, 255], [146, 63, 30, 255]], unlocked=True)
default her_panties_base1 = DollCloth("hermione", ("panties", "panties"), "panties", "basic_panties_1", [[232, 232, 232, 255], [202, 60, 1, 255]], unlocked=True)
default her_bra_base1 = DollCloth("hermione", ("bras", "bras"), "bra", "basic_bra_1", [[232, 232, 232, 255], [202, 60, 1, 255], [167, 77, 42, 255], [237, 179, 14, 255]], unlocked=True)

default her_accessory_house_emblem = DollCloth("hermione", ("misc", "accessory"), "accessory0", "house_emblem", [[167, 77, 42, 255], [237, 179, 14, 255]], zorder=16, unlocked=True)

default her_outfit_default = DollOutfit([her_hair_base, her_top_school1, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1], True)
default her_outfit_default_no_vest = DollOutfit([her_hair_base, her_top_school3, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1])
default her_outfit_default_no_tie_open_shirt = DollOutfit([her_hair_base, her_top_school5, her_bottom_school1, her_panties_base1, her_bra_base1, her_stockings_base1])
default her_outfit_last = DollOutfit([her_hair_base])

###########################
## Leather Bikini Outfit ##
###########################
default her_panties_bikini1 = DollCloth("hermione", ("panties", "panties"), "panties", "bikini_panties_1", [[138, 0, 0, 255], [252, 135, 0, 255]], level=19)
default her_bra_bikini1 = DollCloth("hermione", ("bras", "bras"), "bra", "bikini_bra_1", [[138, 0, 0, 255], [252, 135, 0, 255]], level=19)

default her_outfit_bikini1 = DollOutfit([her_hair_base, her_panties_bikini1, her_bra_bikini1], price=500)

########################
## Rave Bikini Outfit ##
########################

default her_panties_bikini2 = DollCloth("hermione", ("panties", "panties"), "panties", "bikini_panties_2", [[55, 55, 55, 255], [197, 142, 35, 255]], level=19)
default her_bra_bikini2 = DollCloth("hermione", ("bras", "bras"), "bra", "bikini_bra_2", [[55, 55, 55, 255], [197, 142, 35, 255]], level=19)

default her_outfit_bikini2 = DollOutfit([her_hair_base, her_panties_bikini2, her_bra_bikini2], price=500)

#################
## Maid Outfit ##
#################

default her_top_maid1 = DollCloth("hermione", ("tops", "school"), "top", "maid_dress_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]], level=4)
default her_stockings_maid1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "maid_stockings_1", [[53, 33, 30, 255]], level=4)
default her_hat_maid1 = DollCloth("hermione", ("head", "hats"), "hat", "maid_hat_1", [[236, 243, 244, 255]], level=4)
default her_neckwear_maid1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_1", [[40, 51, 61, 255], [236, 243, 244, 255]], level=4)
default her_neckwear_maid2 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "maid_choker_2", [[236, 243, 244, 255]], level=4)
default her_gloves_maid1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "maid_gloves_1", [[40, 51, 61, 255], [236, 243, 244, 255], [53, 63, 84, 255]], level=4)

default her_outfit_maid = DollOutfit([her_hair_base, her_top_maid1, her_stockings_maid1, her_hat_maid1, her_neckwear_maid1, her_neckwear_maid2, her_gloves_maid1], price=500)

##################
## Poker Outfit ##
##################

default her_hat_poker1 = DollCloth("hermione", ("head", "hats"), "hat", "poker_hat_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]], level=4)
default her_hat_poker2 = DollCloth("hermione", ("head", "hats"), "hat", "poker_hat_2", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255]], level=4)
default her_neckwear_poker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "poker_bowtie_1", [[232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]], level=4)
default her_stockings_poker1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_1", [[26, 26, 35, 255], [153, 22, 10, 255]], level=13)
default her_stockings_poker2 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "poker_stockings_2", [[26, 26, 35, 255], [153, 22, 10, 255]], level=13)
default her_panties_poker1 = DollCloth("hermione", ("panties", "panties"), "panties", "poker_panties_1", [[26, 26, 35, 255], [153, 22, 10, 255], [255, 179, 3, 255]], level=19)
default her_bra_poker1 = DollCloth("hermione", ("bras", "bras"), "bra", "poker_bra_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]], blacklist=["panties", "top", "bottom"], level=19)
default her_gloves_poker1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "poker_gloves_1", [[232, 232, 232, 255], [255, 179, 3, 255]], level=4)
default her_earring_poker1 = DollCloth("hermione", ("head", "earrings"), "earring", "poker_earring_1", [[255, 179, 3, 255]], level=4)
default her_piercing2_poker1 = DollCloth("hermione", ("torso", "piercing"), "piercing2", "poker_belly_1", [[26, 26, 35, 255], [232, 232, 232, 255], [153, 22, 10, 255], [255, 179, 3, 255]])

default her_outfit_poker = DollOutfit([her_hair_base, her_hat_poker1, her_hat_poker2, her_neckwear_poker1, her_stockings_poker1, her_stockings_poker2, her_panties_poker1, her_bra_poker1, her_gloves_poker1, her_earring_poker1, her_piercing2_poker1], price=500)

##################
## Bunny Outfit ##
##################

default her_top_bunny1 = DollCloth("hermione", ("tops", "school"), "top", "bunny_top_1", [[48, 48, 48, 255]], blacklist=["panties", "bra"], zorder=7, level=19)
default her_stockings_bunny1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "bunny_stockings_1", [[81, 81, 81, 255]], level=19)
default her_tattoo3_bunny1 = DollCloth("hermione", ("hips", "tattoos"), "tattoo3", "bunny_tattoo1", [[0, 0, 1, 255]])
default her_hat_bunny1 = DollCloth("hermione", ("head", "hats"), "hat", "bunny_hat_1", [[48, 48, 48, 255], [232, 232, 232, 255]], level=13)
default her_gloves_bunny1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "bunny_gloves_1", [[232, 232, 232, 255]], level=4)
default her_neckwear_bunny1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bunny_bowtie_1", [[232, 232, 232, 255], [48, 48, 48, 255]], level=4)

default her_outfit_bunny = DollOutfit([her_hair_base, her_top_bunny1, her_stockings_bunny1, her_tattoo3_bunny1, her_hat_bunny1, her_gloves_bunny1, her_neckwear_bunny1], price=500)

################
## Ball Dress ##
################

default her_hair_updo = DollCloth("hermione", ("head", "hair"), "hair", "updo", [[152, 89, 48, 255], [195, 137, 89, 255]])
default her_top_ball1 = DollCloth("hermione", ("tops", "school"), "top", "ball_dress_1", [[255, 140, 174, 255], [242, 218, 255, 255]], blacklist=["bottom"])
default her_earring_pearls1 = DollCloth("hermione", ("head", "earrings"), "earring", "pearl_1", [[233, 166, 253, 255]], level=4)
default her_neckwear_pearls1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "ball_pearls_1", [[233, 166, 253, 255]], level=4)
default her_accessory_ball_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "ball_sash", [[247, 222, 231, 255], [161, 82, 159, 255]], zorder=16, level=4)

default her_outfit_ball = DollOutfit([her_hair_updo, her_neckwear_pearls1, her_top_ball1, her_earring_pearls1, her_accessory_ball_sash1], price=1000)

#####################
## Yennefer Outfit ##
#####################

default her_top_yen1 = DollCloth("hermione", ("tops", "school"), "top", "yen_top", [[9, 32, 47, 255]], level=10)
default her_bottom_yen_skirt1 = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "yen_skirt", [[26, 26, 26, 255]], level=4)
default her_stockings_yen1 = DollCloth("hermione", ("legwear", "stockings"), "stockings", "yen_stockings", [[76, 76, 76, 255]], level=10)
default her_accessory_yen_sash1 = DollCloth("hermione", ("misc", "accessory"), "accessory4", "yen_sash", [[25, 25, 25, 255], [51, 51, 51, 255]], zorder=9, level=13)
default her_accessory_yen_belt1 = DollCloth("hermione", ("misc", "accessory"), "accessory3", "yen_belt", [[52, 37, 31, 255], [146, 142, 137, 255]], zorder=10, level=4)
default her_accessory_yen_feathers1 = DollCloth("hermione", ("misc", "accessory"), "accessory2", "yen_feathers", [[42, 190, 199, 255]], zorder=16, level=4)
default her_accessory_yen_scarf1 = DollCloth("hermione", ("misc", "accessory"), "accessory1", "yen_scarf", [[9, 32, 47, 255]], zorder=17, level=4)
default her_accessory_yen_corset1 = DollCloth("hermione", ("misc", "accessory"), "accessory0", "yen_corset", [[37, 27, 27, 255], [19, 14, 11, 255]], zorder=16, level=10)
default her_neckwear_yen_choker1 = DollCloth("hermione", ("head", "neckwear"), "neckwear", "yen_choker", [[30, 29, 28, 255]], level=4)
default her_gloves_yen1 = DollCloth("hermione", ("misc", "gloves"), "gloves", "yen_gloves", [[52, 37, 31, 255]], zorder=16, level=4)

default her_outfit_yennefer = DollOutfit([her_hair_base, her_top_yen1, her_bottom_yen_skirt1, her_accessory_yen_sash1, her_stockings_yen1, her_accessory_yen_feathers1, her_accessory_yen_scarf1, her_neckwear_yen_choker1, her_gloves_yen1, her_accessory_yen_corset1, her_accessory_yen_belt1], price=500)

#######################
## Pizza Slut Outfit ##
#######################

default her_bottom_pizza = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "pizza_skirt", [[180, 50, 10, 255], [235, 199, 44, 255]], level=4)
default her_top_pizza = DollCloth("hermione", ("tops", "school"), "top", "pizza_top", [[180, 50, 10, 255]], level=19)
default her_panties_pizza = DollCloth("hermione", ("panties", "panties"), "panties", "pizza_panties", [[180, 50, 10, 255]], level=19)

default her_outfit_pizza = DollOutfit([her_hair_base, her_bottom_pizza, her_top_pizza, her_panties_pizza])

#####################
## Bioshock Outfit ##
#####################

default her_hair_bioshock = DollCloth("hermione", ("head", "hair"), "hair", "bio_hair", [[31, 29, 27, 255], [54, 50, 48, 255]], level=4)
default her_bottom_bioshock = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "bioshock_skirt", [[12, 1, 72, 255]], level=4)
default her_top_bioshock = DollCloth("hermione", ("tops", "school"), "top", "bioshock_corset", [[225, 224, 232, 255], [46, 46, 48, 255], [232, 232, 232, 255]], level=4)
default her_neckwear_bioshock = DollCloth("hermione", ("head", "neckwear"), "neckwear", "bioshock_choker", [[12, 1, 72, 255]], level=4)
default her_robe_bioshock = DollCloth("hermione", ("tops", "robes"), "robe", "bioshock_robe", [[12, 1, 72, 255], [232, 232, 232, 255]], level=4)

default her_outfit_bioshock = DollOutfit([her_hair_bioshock, her_robe_bioshock, her_bottom_bioshock, her_top_bioshock, her_neckwear_bioshock], price=500)

##############
## Swimsuit ##
##############

default her_top_swimsuit_1 = DollCloth("hermione", ("tops", "school"), "top", "swimsuit_top_1", [[22, 27, 48, 255], [224, 198, 16, 255]], blacklist=["panties", "bra"], zorder=7, level=13)

default her_outfit_swimsuit = DollOutfit([her_hair_base, her_top_swimsuit_1], price=500)

#####################
## Egyptian Outfit ##
#####################

default her_top_egypt = DollCloth("hermione", ("tops", "school"), "top", "egypt_top", [[240, 237, 250, 255]], blacklist=["bra"], level=19)
default her_bottom_egypt = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "egypt_loincloth", [[240, 237, 250, 255], [227, 182, 101, 255], [47, 151, 255, 255]], blacklist=["panties"], level=13)
default her_gloves_egypt = DollCloth("hermione", ("misc", "gloves"), "gloves", "egypt_armband", [[227, 182, 101, 255]], level=4)
default her_neckwear_egypt = DollCloth("hermione", ("head", "neckwear"), "neckwear", "egypt_neck", [[227, 182, 101, 255], [94, 209, 236, 255], [47, 151, 255, 255]], level=4)

default her_outfit_egypt = DollOutfit([her_hair_base, her_neckwear_egypt, her_top_egypt, her_bottom_egypt, her_gloves_egypt], price=500)

#######################
## Latex dress Outfit ##
#######################

default her_top_latex_dress_1 = DollCloth("hermione", ("tops", "school"), "top", "latex_dress_1", [[250, 139, 241, 255], [255, 173, 22, 255]], blacklist=["bra"], level=19)

default her_outfit_latex_dress = DollOutfit([her_hair_base, her_top_latex_dress_1], price=500)

####################
## Nightie Outfit ##
####################

default her_top_nightie = DollCloth("hermione", ("tops", "school"), "top", "nightie", [[255, 172, 184, 215]], level=13)

default her_outfit_nightie = DollOutfit([her_hair_base, her_top_nightie], price=500)

#################
## Tifa Outfit ## TODO: Set levels
#################

default her_top_tifa = DollCloth("hermione", ("tops", "school"), "top", "tifa_top", [[232, 232, 232, 255]])
default her_accessory_tifa_belt = DollCloth("hermione", ("misc", "accessory"), "accessory3", "tifa_belt", [[50, 50, 50, 255], [154, 154, 154, 255]])
default her_accessory_tifa_suspenders = DollCloth("hermione", ("misc", "accessory"), "accessory4", "tifa_suspenders", [[86, 61, 67, 255], [154, 154, 154, 255]], zorder=16)
default her_gloves_tifa = DollCloth("hermione", ("misc", "gloves"), "gloves", "tifa_gloves", [[72, 63, 70, 255], [228, 107, 98, 255], [125, 120, 127, 255], [189, 167, 158, 255]])
default her_bottom_tifa = DollCloth("hermione", ("bottoms", "skirts"), "bottom", "tifa_skirt", [[72, 63, 70, 255]])

default her_outfit_tifa = DollOutfit([her_hair_base, her_top_tifa, her_accessory_tifa_belt, her_accessory_tifa_suspenders, her_gloves_tifa, her_bottom_tifa], price=500)

#######################
## Ms. Marvel Outfit ## TODO: Set levels
#######################

default her_top_msmarv = DollCloth("hermione", ("tops", "school"), "top", "msmarv_suit", [[64, 70, 99, 255], [123, 136, 181, 255], [255, 236, 134, 255]], zorder=7, blacklist=["panties", "bra"])
default her_accessory_msmarv_ribbon = DollCloth("hermione", ("misc", "accessory"), "accessory3", "msmarv_ribbon", [[206, 41, 22, 255]])
default her_gloves_msmarv = DollCloth("hermione", ("misc", "gloves"), "gloves", "msmarv_gloves", [[64, 70, 99, 255], [123, 136, 181, 255]])
default her_stockings_msmarv = DollCloth("hermione", ("legwear", "stockings"), "stockings", "msmarv_stockings", [[64, 70, 99, 255], [123, 136, 181, 255]])

default her_outfit_msmarv = DollOutfit([her_hair_base, her_top_msmarv, her_accessory_msmarv_ribbon, her_gloves_msmarv, her_stockings_msmarv], price=500)

#######################
## Heart Slut Outfit ## TODO: Set levels
#######################

default her_top_hslut = DollCloth("hermione", ("tops", "school"), "top", "hslut_top", [[226, 95, 95, 255], [242, 242, 242, 255]])
default her_gloves_hslut = DollCloth("hermione", ("misc", "gloves"), "gloves", "hslut_gloves", [[242, 242, 242, 255]])
default her_stockings_hslut = DollCloth("hermione", ("legwear", "stockings"), "stockings", "hslut_socks", [[242, 242, 242, 255]])
default her_panties_hslut = DollCloth("hermione", ("panties", "panties"), "panties", "hslut_panties", [[226, 95, 95, 255]])
default her_bra_hslut = DollCloth("hermione", ("bras", "bras"), "bra", "hslut_pasties", [[226, 95, 95, 255], [226, 95, 95, 255]])
default her_earring_hslut = DollCloth("hermione", ("head", "earrings"), "earring", "hslut_earring", [[226, 95, 95, 255]])
default her_neckwear_hslut = DollCloth("hermione", ("head", "neckwear"), "neckwear", "hslut_choker", [[242, 242, 242, 255], [226, 95, 95, 255]])
default her_garterbelt_hslut = DollCloth("hermione", ("legwear", "garterbelts"), "garterbelt", "hslut_garter", [[226, 95, 95, 255], [249, 148, 148, 255]])

default her_outfit_hslut = DollOutfit([her_hair_base, her_top_hslut, her_gloves_hslut, her_stockings_hslut, her_panties_hslut, her_bra_hslut, her_earring_hslut, her_neckwear_hslut, her_garterbelt_hslut], price=500)

##########
## MISC ##
##########

default her_tattoo3_lockhart = DollCloth("hermione", ("hips", "tattoos"), "tattoo3", "lockhart_tattoo", [[70, 70, 70, 255]], unlocked=False)
