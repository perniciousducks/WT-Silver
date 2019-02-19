label __init_variables:
    python:
        if not hasattr(renpy.store,'cho_class') or reset_persistants:
            ################
            #              #
            #     INIT     #
            #              #
            ################
            
            character_list = {}
            
            cho_class = char_class(char="cho")
            cho_class.clothing_dictlist = {} #otherwise it doesnt get saved :(
            color_black = [0, 0, 0, 255]
    
            # Tops
            cho_cloth_topsailor1 = cloth_class(char="cho", category="tops", type="top", id="top_sailor_1", layers=3, color=[[252, 252, 253, 255], [89, 116, 194, 255], color_black])
            cho_cloth_topschool1 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_1", layers=5, color=[[183, 183, 184, 255], [124, 120, 136, 255], [216, 163, 10, 255], [89, 116, 194, 255], color_black])
            cho_cloth_topschool2 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_2", layers=5, color=[[183, 183, 184, 255], [124, 120, 136, 255], [216, 163, 10, 255], [89, 116, 194, 255], color_black])
            cho_cloth_topschool3 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_3", layers=4, color=[[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255], color_black])
            cho_cloth_topschool4 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_4", layers=2, color=[[183, 183, 184, 255], color_black])
            cho_cloth_topschool5 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_5", layers=2, color=[[183, 183, 184, 255], color_black])
            cho_cloth_topshirt1 = cloth_class(char="cho", category="tops", type="top", id="top_shirt_1", layers=2, color=[[255, 229, 126, 255], color_black])
            cho_cloth_topsweater1 = cloth_class(char="cho", category="tops", type="top", id="top_sweater_1", layers=3, color=[[20, 29, 83, 255], [213, 161, 13, 255], color_black])
            cho_cloth_toptanktop1 = cloth_class(char="cho", category="tops", type="top", id="top_tanktop_1", layers=2, color=[[230, 230, 231, 255], color_black])
            cho_cloth_toptanktop2 = cloth_class(char="cho", category="tops", type="top", id="top_tanktop_2", layers=3, color=[[252, 192, 213, 255], [253, 221, 232, 255], color_black])

            # Bottoms
            cho_cloth_pantslong1 = cloth_class(char="cho", category="bottoms", type="bottom", id="pants_long_1", layers=2, color=[[230, 230, 231, 255], color_black])
            cho_cloth_pantslong2 = cloth_class(char="cho", category="bottoms", type="bottom", id="pants_long_2", layers=2, color=[[54, 60, 90, 255], color_black])
            cho_cloth_pantsshort1 = cloth_class(char="cho", category="bottoms", type="bottom", id="pants_short_1", layers=2, color=[[230, 230, 231, 255], color_black])
            cho_cloth_pantsshort2 = cloth_class(char="cho", category="bottoms", type="bottom", id="pants_short_2", layers=3, color=[[114, 168, 210, 255], [141, 189, 219, 255], color_black])
            cho_cloth_pantsshort3 = cloth_class(char="cho", category="bottoms", type="bottom", id="pants_short_3", layers=4, color=[[47, 150, 136, 255], [175, 220, 191, 255], [247, 152, 38, 255], color_black])
            cho_cloth_skirtshort1 = cloth_class(char="cho", category="bottoms", type="bottom", id="skirt_short_1", layers=2, color=[[89, 116, 194, 255], color_black])
            cho_cloth_skirtshort2 = cloth_class(char="cho", category="bottoms", type="bottom", id="skirt_short_2", layers=3, color=[[89, 116, 194, 255], [93, 119, 173, 255], color_black])
            
            # Bras
            cho_cloth_basicbra1 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="basic_bra_1", layers=4, color=[[253, 245, 232, 255], [230, 230, 231, 255], [81, 84, 184, 255], color_black])
            cho_cloth_basicbra2 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="basic_bra_2", layers=4, color=[[253, 245, 232, 255], [230, 230, 231, 255], [81, 84, 184, 255], color_black])
            cho_cloth_bikinitop1 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="bikini_top_1", layers=3, color=[[12, 204, 201, 255], [0, 237, 234, 255], color_black])
            cho_cloth_bikinitop2 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="bikini_top_2", layers=2, color=[[138, 22, 17, 255], color_black])
            cho_cloth_lacebra1 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="lace_bra_1", layers=4, color=[[230, 230, 231, 255], [187, 192, 255, 255], [230, 230, 231, 255], color_black])
            cho_cloth_lacebra2 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="lace_bra_2", layers=5, color=[[230, 230, 231, 255], [187, 192, 255, 255], [230, 230, 231, 255], [68, 72, 147, 255], color_black])
            cho_cloth_sportbra1 = cloth_class(char="cho", category="underwear", subcat="bras", type="bra", id="sport_bra_1", layers=3, color=[[155, 203, 248, 255], [251, 252, 254, 255], color_black])
            
            # Panties
            cho_cloth_basicpanties1 = cloth_class(char="cho", category="underwear", type="panties", id="basic_panties_1", layers=4, color=[[230, 230, 231, 255], [220, 220, 221, 255], [173, 23, 48, 255], color_black])
            cho_cloth_basicpanties2 = cloth_class(char="cho", category="underwear", type="panties", id="basic_panties_2", layers=3, color=[[230, 230, 231, 255], [220, 220, 221, 255], color_black])
            cho_cloth_bikinibottom1 = cloth_class(char="cho", category="underwear", type="panties", id="bikini_bottom_1", layers=2, color=[[213, 161, 13, 255], color_black])
            cho_cloth_bikinibottom2 = cloth_class(char="cho", category="underwear", type="panties", id="bikini_bottom_2", layers=2, color=[[213, 161, 13, 255], color_black])
            cho_cloth_lacepanties1 = cloth_class(char="cho", category="underwear", type="panties", id="lace_panties_1", layers=5, color=[[230, 230, 231, 255], [187, 192, 255, 255], [230, 230, 231, 255], [81, 84, 184, 255], color_black])
            cho_cloth_lacepanties2 = cloth_class(char="cho", category="underwear", type="panties", id="lace_panties_2", layers=4, color=[[230, 230, 231, 255], [187, 192, 255, 255], [230, 230, 231, 255], color_black])
            cho_cloth_sportpanties1 = cloth_class(char="cho", category="underwear", type="panties", id="sport_panties_1", layers=3, color=[[156, 204, 249, 255], [211, 234, 250, 255], color_black])
            cho_cloth_sportpanties2 = cloth_class(char="cho", category="underwear", type="panties", id="sport_panties_2", layers=3, color=[[50, 50, 51, 255], [50, 50, 51, 255], color_black])
            
            # Stockings
            cho_cloth_lace_stockings_1 = cloth_class(char="cho", category="stockings", type="stockings", id="lace_stockings_1", layers=4, color=[[50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], color_black])
            
            # Robes
            cho_cloth_robequidditch1 = cloth_class(char="cho", category="robe", type="robe", id="robe_quidditch_1", layers=3, color=[[50, 50, 51, 255], [50, 50, 51, 255], color_black])
            cho_cloth_robequidditch2 = cloth_class(char="cho", category="robe", type="robe", id="robe_quidditch_2", layers=2, color=[[50, 50, 51, 255], color_black])
            
            # Neckwear
            cho_cloth_chokerlace1= cloth_class(char="cho", category="head", type="neckwear", id="choker_lace_1", layers=4, color=[[50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], color_black])
            
            # Garterbelts
            cho_cloth_lacegarter1 = cloth_class(char="cho", category="garterbelts", type="garter", id="lace_garter_1", layers=5, color=[[50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], color_black])
            cho_cloth_lacegarter2 = cloth_class(char="cho", category="garterbelts", type="garter", id="lace_garter_2", layers=5, color=[[50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], [50, 50, 51, 255], color_black])
        
            ################
            #              #
            #   DEFAULTS   #
            #              #
            ################
        
            cho_class.body = {
                        "hair":        ["ponytail_blue_top", 12, 0, 0, False],
                        "hairshadow":  ["ponytail_blue_base", 11, 0, 0, False],
                        "armleft":     ["arm_down_l", 17, 0, 0, False],
                        "armright":    ["arm_down_r", 1, 0, 0, False],
                        "breasts":     ["breasts_bikini_tan", 3, 0, 0, False],
                        "base":        ["base_01", 2, 0, 0, False],
                        "legs":        [None, 5, 1, 0, False]}
                        
            cho_class.face = {
                        "tears":       [None, 11, 0, 0, False],
                        "cheeks":      [None, 10, 0, 0, False],
                        "eyebrows":    ["base", 9, 0, 0, False],
                        "eyes":        ["base", 8, 0, 0, False],
                        "pupils":      ["mid", 7, 0, 0, False],
                        "whites":      ["_white_", 6, 0, 0, False],
                        "mouth":       ["base", 5, 0, 0, False]}

            cho_class.other = {
                        "cum":         [None, 15, 0, 0, False],
                        "emote":       [None, 30, 0, 0, False]}
                        
            cho_class.update_paths("body", "face", "other")

            cho_class.clothing = {
                        "hat":        [None, 24, 0, 0, False],
                        "neckwear":   [None, 18, 0, 0, False],
                        "badge":      [None, 22, 0, 0, False],
                        "robe":       [None, 21, 0, 0, False],
                        "gloves":     [None, 20, 0, 0, False],
                        "top":        [cho_cloth_topschool1, 19, 0, 0, False],
                        "bra":        [cho_cloth_basicbra1, 18, 0, 0, False],
                        "belt":       [None, 17, 0, 0, False],
                        "bottom":     [cho_cloth_skirtshort1, 16, 0, 0, False],
                        "garter":     [None, 15, 0, 0, False],
                        "panties":    [cho_cloth_basicpanties1, 14, 0, 0, False],
                        "stockings":  [None, 13, 0, 0, False],
                        "plug":       [None, 0, 0, 0, False]}