# Astoria wardrobe init
default astoria_class = char_class(char="astoria")

default astoria_hair_base = cloth_class(char="astoria", category="head", subcat="hair", type="hair", id="base", layers=2, color=[[229, 198, 129, 255], [163, 125, 80, 255]])
default astoria_hair_short = cloth_class(char="astoria", category="head", subcat="hair", type="hair", id="short", layers=2, color=[[229, 198, 129, 255], [163, 125, 80, 255]])
default astoria_hair_ann = cloth_class(char="astoria", category="head", subcat="hair", type="hair", id="ann_takamaki", layers=3, color=[[229, 198, 129, 255], [163, 125, 80, 255], [255, 209, 105, 255]], unlocked=False)

# Hats and masks
default astoria_mask_ann = cloth_class(char="astoria", category="head", subcat="hats", type="hat", id="ann_takamaki", layers=2, color=[[173, 18, 18, 255], [238, 188, 187, 255]], whoring=14, incompatible=["bottom", "bra", "garterbelt"], unlocked=False)

# Tops
default astoria_cloth_topschool1 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_1", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
default astoria_cloth_topschool2 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_2", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], whoring=4)
default astoria_cloth_topschool3 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_3", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], whoring=8)
default astoria_cloth_topschool4 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_4", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], whoring=8)
default astoria_cloth_topschool5 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_5", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], whoring=12)
default astoria_cloth_topschool6 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_6", layers=3, color=[[109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], whoring=12)

default astoria_cloth_topann = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="ann_takamaki", layers=3, color=[[173, 18, 18, 255], [232, 232, 232, 255], [238, 188, 187, 255]], whoring=14, incompatible=["bottom", "bra", "garterbelt"], bodyfix={"breasts": ["base_tight", 6, 0, 0, False]}, unlocked=False)

# Bottoms
default astoria_cloth_schoolskirt1 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_1", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]])
default astoria_cloth_schoolskirt2 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_2", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=4)
default astoria_cloth_schoolskirt3 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_3", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=8)
default astoria_cloth_schoolskirt4 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_4", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=12)

# Bras
default astoria_cloth_basicbra1 = cloth_class(char="astoria", category="bras", subcat="bras", type="bra", id="basic_bra_1", layers=2, color=[[213, 62, 65, 255], [234, 236, 234, 255]])
default astoria_cloth_basicbra2 = cloth_class(char="astoria", category="bras", subcat="bras", type="bra", id="basic_bra_2", layers=1, color=[[213, 62, 65, 255]])

# Panties
default astoria_cloth_basicpanties1 = cloth_class(char="astoria", category="panties", subcat="panties", type="panties", id="basic_panties_1", layers=2, color=[[213, 62, 65, 255], [234, 236, 234, 255]])
default astoria_cloth_basicpanties2 = cloth_class(char="astoria", category="panties", subcat="panties", type="panties", id="basic_panties_2", layers=1, color=[[213, 62, 65, 255]])

# Legwear
default astoria_cloth_pantyhose1 = cloth_class(char="astoria", category="legwear", subcat="stockings", type="stockings", id="pantyhose", layers=1, color=[[190, 146, 129, 255]])
default astoria_cloth_stockingsann = cloth_class(char="astoria", category="legwear", subcat="stockings", type="stockings", id="ann_takamaki", layers=2, color=[[99, 42, 42, 255], [181, 135, 135, 255]], whoring=14, unlocked=False)

# Gloves
default astoria_cloth_glovesann = cloth_class(char="astoria", category="misc", subcat="gloves", type="gloves", id="ann_takamaki", layers=1, color=[[249, 139, 225, 255]], unlocked=False)

# accessory
default astoria_cloth_plugann = cloth_class(char="astoria", category="misc", subcat="accessory", type="buttplug", id="ann_takamaki", layers=2, color=[[99, 42, 42, 255], [181, 135, 135, 255]], whoring=14, unlocked=False)

# Temporal save
default astoria_outfit_last = outfit_class(name="Last worn items", group=[astoria_hair_base])

default astoria_outfit_custom = outfit_class(name = "Default", group = [astoria_hair_base.clone(), astoria_cloth_schoolskirt1.clone(), astoria_cloth_topschool1.clone(), astoria_cloth_basicbra1.clone(), astoria_cloth_basicpanties1.clone()], unlocked=True)

# Outfits
default astoria_outfit_anntakamaki = outfit_class(name="Ann Takamaki", group=[astoria_hair_ann.clone(), astoria_mask_ann.clone(), astoria_cloth_topann.clone(), astoria_cloth_stockingsann.clone(), astoria_cloth_plugann.clone(), astoria_cloth_glovesann.clone()])
default astoria_outfit_default = outfit_class(name = "Default", group=[astoria_hair_base.clone(), astoria_cloth_schoolskirt1.clone(), astoria_cloth_topschool1.clone(), astoria_cloth_basicbra1.clone(), astoria_cloth_basicpanties1.clone()])
        
label default_astoria_class_init:
python:
    # Because astoria_class must be defined before clothing, the default clothing can only be set afterwards, like so:
    if not astoria_class.body or not astoria_class.face or not astoria_class.other or not astoria_class.clothing:
        astoria_class.body = {
            "handleft":  ["characters/astoria/body/arms/armfixL.png", 40, 0, 0, False],
            "handright": ["characters/astoria/body/arms/armfixR.png", 40, 0, 0, False],
            "armleft":   ["l_arm_hips", 18, 0, 0, False],
            "armright":  ["r_arm_hips", 2, 0, 0, False],
            "breasts":   ["base", 6, 0, 0, False],
            "base":      ["base_01", 3, 0, 0, False],
            "legs":      [None, 2, 0, 0, False],
            "animation": [None, 2, 0, 0, False]
        }
                    
        astoria_class.face = {
            "tears":    [None, 11, 0, 0, False],
            "cheeks":   [None, 10, 0, 0, False],
            "eyebrows": ["base", 9, 0, 0, False],
            "eyes":     ["base", 8, 0, 0, False],
            "pupils":   ["mid", 7, 0, 0, False],
            "whites":   ["_white_", 6, 0, 0, False],
            "mouth":    ["smile", 13, 0, 0, False]
        }

        astoria_class.other = {
            "cum":   [None, 15, 0, 0, False],
            "emote": [None, 30, 0, 0, False]
        }
                    
        astoria_class.update_paths("body", "face", "other")

        astoria_class.clothing = {
            "hat":        [None, 24, 0, 0, False],
            "hair":       [astoria_hair_base, 12, 0, 0, False],
            "earring":    [None, 22, 0, 0, False],
            "neckwear":   [None, 17, 0, 0, False],
            "robe":       [None, 21, 0, 0, False],
            "gloves":     [None, 41, 0, 0, False],
            "top":        [astoria_cloth_topschool1, 19, 0, 0, False],
            "bra":        [astoria_cloth_basicbra1, 18, 0, 0, False],
            "bottom":     [astoria_cloth_schoolskirt1, 16, 0, 0, False],
            "garterbelt": [None, 15, 0, 0, False],
            "panties":    [astoria_cloth_basicpanties1, 14, 0, 0, False],
            "stockings":  [astoria_cloth_pantyhose1, 13, 0, 0, False],
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
