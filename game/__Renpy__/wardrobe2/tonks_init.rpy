label tonks_wardrobe_init:
    python:
        if not hasattr(renpy.store,'tonks_class') or reset_persistants:
            ################
            #              #
            #     INIT     #
            #              #
            ################
            
            tonks_class = char_class(char="tonks")
            tonks_class.clothing_dictlist = {}
            tonks_class.outfits = []
            
            tonks_hair_base = cloth_class(char="tonks", category="head", subcat="hair", type="hair", id="base", layers=1, color=[[243, 158, 189, 255]])
            
            tonks_cloth_top_auror = cloth_class(char="tonks", category="tops", subcat="auror", type="top", id="auror", layers=2, color=[[28, 27, 31, 255], [124, 42, 50, 255]])
            tonks_cloth_top_auror2 = cloth_class(char="tonks", category="tops", subcat="auror", type="top", id="auror2", layers=1, color=[[124, 42, 50, 255]])
            tonks_cloth_top_corset = cloth_class(char="tonks", category="tops", subcat="school", type="top", id="corset", layers=1, color=[[247, 206, 146, 255]])
            
            tonks_cloth_jeans = cloth_class(char="tonks", category="bottoms", subcat="trousers", type="bottom", id="jeans", layers=1, color=[[51, 104, 105, 255]])
            
            tonks_cloth_panties_base = cloth_class(char="tonks", category="panties", subcat="panties", type="panties", id="base", layers=1, color=[[124, 42, 50, 255]])
            
            tonks_cloth_garterbase = cloth_class(char="tonks", category="legwear", subcat="stockings", type="stockings", id="auror", layers=2, color=[[45, 45, 48, 255], [177, 168, 172, 255]])
            
            tonks_cloth_garterbase = cloth_class(char="tonks", category="bras", subcat="bras", type="bra", id="bikini", layers=2, color=[[124, 42, 50, 255], [177, 168, 172, 255]])
            
            # Temporal save
            tonks_outfit_last = outfit_class(name="Last worn items", group=[tonks_hair_base])
        
            ################
            #              #
            #   DEFAULTS   #
            #              #
            ################
        
            tonks_class.body = {
                        "handleft":    ["characters/tonks/body/arms/armfixL.png", 40, 0, 0, False],
                        "handright":   ["characters/tonks/body/arms/armfixR.png", 40, 0, 0, False],
                        "armleft":     ["l_arm_hips", 18, 0, 0, False],
                        "armright":    ["r_arm_hips", 2, 0, 0, False],
                        "breasts":     ["base", 6, 0, 0, False],
                        "base":        ["base_01", 3, 0, 0, False],
                        "legs":        [None, 2, 0, 0, False],
                        "animation":   [None, 2, 0, 0, False]}
                        
            tonks_class.face = {
                        "tears":       [None, 11, 0, 0, False],
                        "cheeks":      [None, 10, 0, 0, False],
                        "eyebrows":    ["base", 9, 0, 0, False],
                        "eyes":        ["base", 8, 0, 0, False],
                        "pupils":      ["mid", 7, 0, 0, False],
                        "whites":      ["_white_", 6, 0, 0, False],
                        "mouth":       ["base", 5, 0, 0, False]}

            tonks_class.other = {
                        "cum":         [None, 15, 0, 0, False],
                        "emote":       [None, 30, 0, 0, False]}
                        
            tonks_class.update_paths("body", "face", "other")

            tonks_class.clothing = {
                        "hat":        [None, 24, 0, 0, False],
                        "hair":       [tonks_hair_base, 12, 0, 0, False],
                        "earring":    [None, 22, 0, 0, False],
                        "neckwear":   [None, 17, 0, 0, False],
                        "robe":       [None, 21, 0, 0, False],
                        "gloves":     [None, 20, 0, 0, False],
                        "top":        [tonks_cloth_top_auror, 19, 0, 0, False],
                        "bra":        [None, 18, 0, 0, False],
                        "bottom":     [tonks_cloth_jeans, 16, 0, 0, False],
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
                        "makeup4":    [None, 11, 0, 0, False]}
    return