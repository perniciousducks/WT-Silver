default tonks_class = char_class(char="tonks")

default tonks_hair_base = cloth_class(char="tonks", category="head", subcat="hair", type="hair", id="base", layers=1, color=[[243, 158, 189, 255]])

# Miscellaneous
default tonks_cloth_choker_beads = cloth_class(char="tonks", category="head", subcat="neckwear", type="neckwear", id="choker_beads", layers=2, color=[[45, 45, 48, 255], [177, 168, 172, 255]])
default tonks_cloth_gloves_auror = cloth_class(char="tonks", category="misc", subcat="gloves", type="gloves", id="auror_gloves", layers=1, color=[[45, 45, 48, 255]], armfix=True)

# Tops
default tonks_cloth_top_auror  = cloth_class(char="tonks", category="tops", subcat="auror", type="top", id="auror", layers=2, color=[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True)
default tonks_cloth_top_auror2 = cloth_class(char="tonks", category="tops", subcat="auror", type="top", id="auror2", layers=1, color=[[124, 42, 50, 255]], armfix=True)
default tonks_cloth_top_corset = cloth_class(char="tonks", category="tops", subcat="auror", type="top", id="corset", layers=1, color=[[247, 206, 146, 255]], bodyfix={"breasts": ["base_tight", 6, 0, 0, False]}, incompatible=["bra"], armfix=True)

# Bottoms
default tonks_cloth_jeans         = cloth_class(char="tonks", category="bottoms", subcat="trousers", type="bottom", id="jeans", layers=1, color=[[51, 104, 105, 255]])
default tonks_cloth_leggings      = cloth_class(char="tonks", category="bottoms", subcat="trousers", type="bottom", id="leggings", layers=1, color=[[45, 45, 48, 255]])
default tonks_cloth_leggings_hole = cloth_class(char="tonks", category="bottoms", subcat="trousers", type="bottom", id="leggings_hole", layers=1, color=[[45, 45, 48, 255]])

# Underwear
default tonks_cloth_panties_base = cloth_class(char="tonks", category="panties", subcat="panties", type="panties", id="base", layers=1, color=[[124, 42, 50, 255]])

default tonks_cloth_bra_base = cloth_class(char="tonks", category="bras", subcat="bras", type="bra", id="bikini", layers=2, color=[[124, 42, 50, 255], [177, 168, 172, 255]])

# Legwear
default tonks_cloth_garterbase = cloth_class(char="tonks", category="legwear", subcat="stockings", type="stockings", id="auror", layers=2, color=[[45, 45, 48, 255], [177, 168, 172, 255]], armfix=True)

# Robes
default tonks_cloth_auror_coat = cloth_class(char="tonks", category="tops", subcat="robes", type="robe", id="auror_coat", layers=2, color=[[40, 40, 41, 255], [174, 165, 169, 255]], armfix=True)

# Temporal save
default tonks_outfit_last   = outfit_class(name="Last worn items", group=[tonks_hair_base])
default tonks_outfit_custom = outfit_class(name="Default", group=[tonks_hair_base.clone(), tonks_cloth_leggings_hole.clone(), tonks_cloth_top_auror.clone(), tonks_cloth_choker_beads.clone(), tonks_cloth_gloves_auror.clone(), tonks_cloth_auror_coat.clone()], unlocked=True)
        
label default_tonks_class_init:
python:
    # Because tonks_class must be defined before clothing, the default clothing can only be set afterwards, like so:
    if not tonks_class.body or not tonks_class.face or not tonks_class.other or not tonks_class.clothing:
        tonks_class.body = {
            "handleft":  [None, 20, 0, 0, False],
            "handright": ["armfixR", 4, 0, 0, False],
            "armleft":   ["l_arm_hips", 18, 0, 0, False],
            "armright":  ["r_arm_hips", 2, 0, 0, False],
            "breasts":   ["base", 6, 0, 0, False],
            "base":      ["base_01", 3, 0, 0, False],
            "legs":      [None, 2, 0, 0, False],
            "animation": [None, 2, 0, 0, False]
        }
                    
        tonks_class.face = {
            "tears":    [None, 11, 0, 0, False],
            "cheeks":   [None, 10, 0, 0, False],
            "eyebrows": ["base", 9, 0, 0, False],
            "eyes":     ["base", 8, 0, 0, False],
            "pupils":   ["mid", 7, 0, 0, False],
            "whites":   ["_white_", 6, 0, 0, False],
            "mouth":    ["base", 5, 0, 0, False]
        }

        tonks_class.other = {
            "cum":   [None, 15, 0, 0, False],
            "emote": [None, 30, 0, 0, False]
        }
                    
        tonks_class.update_paths("body", "face", "other")

        tonks_class.clothing = {
            "hat":        [None, 24, 0, 0, False],
            "hair":       [tonks_hair_base, 12, 0, 0, False],
            "earring":    [None, 22, 0, 0, False],
            "neckwear":   [tonks_cloth_choker_beads, 17, 0, 0, False],
            "robe":       [tonks_cloth_auror_coat, 21, 0, 0, False],
            "gloves":     [tonks_cloth_gloves_auror, 19, 0, 0, False],
            "top":        [tonks_cloth_top_auror, 17, 0, 0, False],
            "bra":        [None, 16, 0, 0, False],
            "bottom":     [tonks_cloth_leggings, 15, 0, 0, False],
            "garterbelt": [tonks_cloth_garterbase, 14, 0, 0, False],
            "panties":    [None, 13, 0, 0, False],
            "stockings":  [None, 12, 0, 0, False],
            "buttplug":   [None, 0, 0, 0, False],
            "pubes":      [None, 11, 0, 0, False],
            "tattoo0":    [None, 10, 0, 0, False],
            "tattoo1":    [None, 10, 0, 0, False],
            "tattoo2":    [None, 10, 0, 0, False],
            "tattoo3":    [None, 10, 0, 0, False],
            "tattoo4":    [None, 10, 0, 0, False],
            "piercing0":  [None, 10, 0, 0, False],
            "piercing1":  [None, 10, 0, 0, False],
            "piercing2":  [None, 10, 0, 0, False],
            "piercing3":  [None, 10, 0, 0, False],
            "piercing4":  [None, 10, 0, 0, False],
            "accessory0": [None, 20, 0, 0, False],
            "accessory1": [None, 20, 0, 0, False],
            "accessory2": [None, 20, 0, 0, False],
            "accessory3": [None, 20, 0, 0, False],
            "accessory4": [None, 20, 0, 0, False],
            "makeup0":    [None, 11, 0, 0, False],
            "makeup1":    [None, 11, 0, 0, False],
            "makeup2":    [None, 11, 0, 0, False],
            "makeup3":    [None, 11, 0, 0, False],
            "makeup4":    [None, 11, 0, 0, False]
        }
