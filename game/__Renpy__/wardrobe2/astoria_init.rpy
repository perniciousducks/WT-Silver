label astoria_wardrobe_init:
    python:
        if not hasattr(renpy.store,'astoria_class') or reset_persistants:
            ################
            #              #
            #     INIT     #
            #              #
            ################
            
            astoria_class = char_class(char="astoria")
            astoria_class.clothing_dictlist = {}
            astoria_class.outfits = []
            
            astoria_hair_base = cloth_class(char="astoria", category="head", subcat="hair", type="hair", id="base", layers=1, color=[[229, 198, 129, 255]])
            
            # Tops
            astoria_cloth_topschool1 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_1", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            astoria_cloth_topschool2 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_2", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            astoria_cloth_topschool3 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_3", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            astoria_cloth_topschool4 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_4", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            astoria_cloth_topschool5 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_5", layers=3, color=[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            astoria_cloth_topschool6 = cloth_class(char="astoria", category="tops", subcat="school", type="top", id="top_school_6", layers=3, color=[[109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]])
            
            # Bottoms
            astoria_cloth_schoolskirt1 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_1", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]])
            astoria_cloth_schoolskirt2 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_2", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=4)
            astoria_cloth_schoolskirt3 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_3", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=8)
            astoria_cloth_schoolskirt4 = cloth_class(char="astoria", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_4", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=12)
            
            # Legwear
            astoria_cloth_pantyhose1 = cloth_class(char="astoria", category="legwear", subcat="stockings", type="stockings", id="pantyhose", layers=1, color=[[190, 146, 129, 255]])
            
            # Temporal save
            astoria_outfit_last = outfit_class(name="Last worn items", group=[astoria_hair_base])
        
            ################
            #              #
            #   DEFAULTS   #
            #              #
            ################
        
            astoria_class.body = {
                        "handleft":    ["characters/astoria/body/arms/armfixL.png", 40, 0, 0, False],
                        "handright":   ["characters/astoria/body/arms/armfixR.png", 40, 0, 0, False],
                        "armleft":     ["l_arm_hips", 18, 0, 0, False],
                        "armright":    ["r_arm_hips", 2, 0, 0, False],
                        "breasts":     ["base", 6, 0, 0, False],
                        "base":        ["base_01", 3, 0, 0, False],
                        "legs":        [None, 2, 0, 0, False],
                        "animation":   [None, 2, 0, 0, False]}
                        
            astoria_class.face = {
                        "tears":       [None, 11, 0, 0, False],
                        "cheeks":      [None, 10, 0, 0, False],
                        "eyebrows":    ["base", 9, 0, 0, False],
                        "eyes":        ["base", 8, 0, 0, False],
                        "pupils":      ["mid", 7, 0, 0, False],
                        "whites":      ["_white_", 6, 0, 0, False],
                        "mouth":       ["smile", 5, 0, 0, False]}

            astoria_class.other = {
                        "cum":         [None, 15, 0, 0, False],
                        "emote":       [None, 30, 0, 0, False]}
                        
            astoria_class.update_paths("body", "face", "other")

            astoria_class.clothing = {
                        "hat":        [None, 24, 0, 0, False],
                        "hair":       [astoria_hair_base, 12, 0, 0, False],
                        "earring":    [None, 22, 0, 0, False],
                        "neckwear":   [None, 17, 0, 0, False],
                        "robe":       [None, 21, 0, 0, False],
                        "gloves":     [None, 20, 0, 0, False],
                        "top":        [astoria_cloth_topschool1, 19, 0, 0, False],
                        "bra":        [None, 18, 0, 0, False],
                        "bottom":     [astoria_cloth_schoolskirt1, 16, 0, 0, False],
                        "garterbelt": [None, 15, 0, 0, False],
                        "panties":    [None, 14, 0, 0, False],
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
                        "makeup4":    [None, 11, 0, 0, False]}
    return