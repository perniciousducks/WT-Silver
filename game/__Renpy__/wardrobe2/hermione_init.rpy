# Astoria wardrobe init
default hermione_class = char_class(char="hermione")

default hermione_hair_base = cloth_class(char="hermione", category="head", subcat="hair", type="hair", id="base", layers=1, color=[[152, 89, 48, 255]])

# Temporal save
default hermione_outfit_last = outfit_class(name="Last worn items", group=[astoria_hair_base])

default hermione_outfit_custom = outfit_class(name = "Default", group = [astoria_hair_base.clone(), astoria_cloth_schoolskirt1.clone(), astoria_cloth_topschool1.clone(), astoria_cloth_basicbra1.clone(), astoria_cloth_basicpanties1.clone()], unlocked=True)

# Outfits
default hermione_outfit_default = outfit_class(name = "Default", group=[astoria_hair_base.clone(), astoria_cloth_schoolskirt1.clone(), astoria_cloth_topschool1.clone(), astoria_cloth_basicbra1.clone(), astoria_cloth_basicpanties1.clone()])
        
label default_hermione_class_init:
python:
    # Because hermione_class must be defined before clothing, the default clothing can only be set afterwards, like so:
    if not hermione_class.body or not hermione_class.face or not hermione_class.other or not hermione_class.clothing:
        hermione_class.body = {
            "armleft":   ["arm_down_l", 18, 0, 0, False],
            "armright":  ["arm_down_r", 2, 0, 0, False],
            "breasts":   ["breasts_01", 6, 0, 0, False],
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
            "top":        [None, 19, 0, 0, False],
            "bra":        [None, 18, 0, 0, False],
            "bottom":     [None, 16, 0, 0, False],
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
