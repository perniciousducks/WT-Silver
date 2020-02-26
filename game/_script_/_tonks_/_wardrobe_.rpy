###############
## Character ##
###############

default tonks = Doll(name="tonks", 
                        clothes={"hat":        [None, 15, True],
                                 "hair":       [None, 4, True],
                                 "earring":    [None, 14, True],
                                 "neckwear":   [None, 11, True],
                                 "robe":       [None, 28, True],
                                 "gloves":     [None, 21, True],
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
                        body={"armleft": ["on_hips", 3], 
                              "armright":["on_hips", 1], 
                              "base":    ["front", 0], 
                              "breasts": ["normal", 2]})

##################
## Auror Outfit ##
##################

default ton_hair_base = DollCloth("tonks", ("head", "hair"), "hair", "base", [[243, 158, 189, 255]])
default ton_neckwear_beads = DollCloth("tonks", ("head", "neckwear"), "neckwear", "choker_beads",[[45, 45, 48, 255], [177, 168, 172, 255]])
default ton_gloves_auror = DollCloth("tonks", ("misc", "gloves"), "gloves", "auror_gloves",[[45, 45, 48, 255]], armfix=True)
default ton_top_auror  = DollCloth("tonks", ("tops", "auror"), "top", "auror",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True)
default ton_top_auror2 = DollCloth("tonks", ("tops", "auror"), "top", "auror2",[[124, 42, 50, 255]], armfix=True)
default ton_robe_auror = DollCloth("tonks", ("tops", "robes"), "robe", "auror_coat",[[40, 40, 41, 255], [174, 165, 169, 255]], armfix=True)
default ton_bottoms_leggings = DollCloth("tonks", ("bottoms", "trousers"), "bottom", "leggings",[[45, 45, 48, 255]], armfix=True)
default ton_bottoms_leggings_hole = DollCloth("tonks", ("bottoms", "trousers"), "bottom", "leggings_hole",[[45, 45, 48, 255]], level=60, armfix=True)
default ton_stockings_auror = DollCloth("tonks", ("legwear", "stockings"), "stockings", "auror",[[45, 45, 48, 255], [177, 168, 172, 255]], armfix=True)

##########
## Misc ##
##########

default ton_top_corset = DollCloth("tonks", ("tops", "auror"), "top", "corset",[[247, 206, 146, 255]], blacklist=("bra"))
default ton_bottoms_jeans = DollCloth("tonks", ("bottoms", "trousers"), "bottom", "jeans",[[51, 104, 105, 255]])
default ton_panties_base = DollCloth("tonks", ("panties", "panties"), "panties", "base",[[124, 42, 50, 255]])
default ton_bra_base = DollCloth("tonks", ("bras", "bras"), "bra", "bikini",[[124, 42, 50, 255], [177, 168, 172, 255]])

default ton_outfit_default = DollOutfit([ton_hair_base, ton_neckwear_beads, ton_gloves_auror, ton_top_auror, ton_robe_auror, ton_bottoms_leggings, ton_stockings_auror], True)
default ton_outfit_last = DollOutfit([ton_hair_base])