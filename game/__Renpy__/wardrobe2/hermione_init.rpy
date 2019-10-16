# Astoria wardrobe init
default hermione_class = char_class(char="hermione")

default hermione_hair_base = cloth_class(char="hermione", category="head", subcat="hair", type="hair", id="base", layers=1, color=[[152, 89, 48, 255]])

# Tops

default hermione_cloth_topschool1 = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_1", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})
default hermione_cloth_topschool2     = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_2", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], whoring=4, bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})
default hermione_cloth_topschool3     = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_3", layers=3, color=[[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], whoring=8, bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})
default hermione_cloth_topschool4     = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_4", layers=3, color=[[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], whoring=8, bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})
default hermione_cloth_topschool5     = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_5", layers=3, color=[[183, 183, 184, 255], [167, 77, 42, 255], [237, 179, 14, 255]], whoring=12, bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})
default hermione_cloth_topschool6     = cloth_class(char="hermione", category="tops", subcat="school", type="top", id="top_school_6", layers=3, color=[[109, 105, 121, 255], [167, 77, 42, 255], [237, 179, 14, 255]], whoring=12, bodyfix={"breasts": ["breasts_01_tight", 6, 0, 0, False]})

# Bottoms

default hermione_cloth_schoolskirt1 = cloth_class(char="hermione", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_1", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]])
default hermione_cloth_schoolskirt2 = cloth_class(char="hermione", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_2", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=4)
default hermione_cloth_schoolskirt3 = cloth_class(char="hermione", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_3", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=8)
default hermione_cloth_schoolskirt4 = cloth_class(char="hermione", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_4", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=12)

# Temporal save
default hermione_outfit_last = outfit_class(name="Last worn items", group=[astoria_hair_base])

default hermione_outfit_custom = outfit_class(name = "Default", group = [hermione_hair_base.clone(), hermione_cloth_topschool1.clone(), hermione_cloth_schoolskirt1.clone()], unlocked=True)

# Outfits
default hermione_outfit_default = outfit_class(name = "Default", group=[hermione_hair_base.clone(), hermione_cloth_topschool1.clone(), hermione_cloth_schoolskirt1.clone()])
        
label default_hermione_class_init:
python:
    # Because hermione_class must be defined before clothing, the default clothing can only be set afterwards, like so:
    if not hermione_class.body or not hermione_class.face or not hermione_class.other or not hermione_class.clothing:
        hermione_class.body = {
            "armleft":   ["arm_down_l", 18, 0, 0, False],
            "armright":  ["arm_down_r", 2, 0, 0, False],
            "breasts":   ["breasts_01", 4, 0, 0, False],
            "base":      ["base_01", 3, 0, 0, False],
            "legs":      [None, 2, 0, 0, False],
            "animation": [None, 2, 0, 0, False]
        }
                    
        hermione_class.face = {
            "tears":    [None, 11, 0, 0, False],
            "cheeks":   [None, 10, 0, 0, False],
            "eyebrows": ["base", 9, 0, 0, False],
            "eyes":     ["base", 8, 0, 0, False],
            "pupils":   ["mid", 7, 0, 0, False],
            "whites":   ["_white_", 6, 0, 0, False],
            "mouth":    ["base", 13, 0, 0, False]
        }

        hermione_class.other = {
            "cum":   [None, 15, 0, 0, False],
            "emote": [None, 30, 0, 0, False]
        }
                    
        hermione_class.update_paths("body", "face", "other")

        hermione_class.clothing = {
            "hat":        [None, 24, 0, 0, False],
            "hair":       [hermione_hair_base, 12, 0, 0, False],
            "earring":    [None, 22, 0, 0, False],
            "neckwear":   [None, 17, 0, 0, False],
            "robe":       [None, 21, 0, 0, False],
            "gloves":     [None, 41, 0, 0, False],
            "top":        [hermione_cloth_topschool1, 19, 0, 0, False],
            "bra":        [None, 18, 0, 0, False],
            "bottom":     [hermione_cloth_schoolskirt1, 16, 0, 0, False],
            "garterbelt": [None, 15, 0, 0, False],
            "panties":    [None, 14, 0, 0, False],
            "stockings":  [None, 13, 0, 0, False],
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
