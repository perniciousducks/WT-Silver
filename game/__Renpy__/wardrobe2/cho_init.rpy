label cho_wardrobe_init:
    python:
        if not hasattr(renpy.store,'cho_class') or reset_persistants:
            ################
            #              #
            #     INIT     #
            #              #
            ################
            
            character_list = {}
            
            cho_class = char_class(char="cho")
            cho_class.clothing_dictlist = {}
            cho_class.outfits = []
            
            character_clothes_list = []

            # Tops
            cho_cloth_topschool1 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_1", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topschool2 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_2", layers=4, color=[[183, 183, 184, 255], [109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topschool3 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_3", layers=3, color=[[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topschool4 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_4", layers=3, color=[[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topschool5 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_5", layers=3, color=[[183, 183, 184, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topschool6 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_school_6", layers=3, color=[[109, 105, 121, 255], [216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_topshirt1 = cloth_class(char="cho", category="tops", subcat="muggle", type="top", id="top_shirt_1", layers=1, color=[[255, 229, 126, 255]], unlocked=False)
            cho_cloth_topsailor1 = cloth_class(char="cho", category="tops", subcat="muggle", type="top", id="top_sailor_1", layers=2, color=[[252, 252, 253, 255], [89, 116, 194, 255]], unlocked=False)
            cho_cloth_topsweater2 = cloth_class(char="cho", category="tops", subcat="muggle", type="top", id="top_sweater_2", layers=1, color=[[89, 116, 194, 255]])
            cho_cloth_toptanktop1 = cloth_class(char="cho", category="tops", subcat="muggle", type="top", id="top_tanktop_1", layers=1, color=[[230, 230, 231, 255]])
            cho_cloth_toptanktop2 = cloth_class(char="cho", category="tops", subcat="muggle", type="top", id="top_tanktop_2", layers=2, color=[[252, 192, 213, 255], [253, 221, 232, 255]], unlocked=False)
            cho_cloth_topsweater1 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_sweater_1", layers=2, color=[[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
            cho_cloth_robequidditch1 = cloth_class(char="cho", category="tops", subcat="robes", type="robe", id="robe_quidditch_1", layers=2, color=[[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
            cho_cloth_topquid1 = cloth_class(char="cho", category="tops", subcat="school", type="top", id="top_quid_1", layers=2, color=[[64, 84, 141, 255], [213, 161, 13, 255]], unlocked=False, whoring=8)
            
            # Bottoms
            cho_cloth_schoolskirt1 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_1", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]])
            cho_cloth_schoolskirt2 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_2", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=4)
            cho_cloth_schoolskirt3 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_3", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=8)
            cho_cloth_schoolskirt4 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_4", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], whoring=12)
            cho_cloth_pantslong1 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_long_1", layers=1, color=[[230, 230, 231, 255]])
            cho_cloth_pantsshort1 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_short_1", layers=1, color=[[230, 230, 231, 255]], whoring=4)
            cho_cloth_pantsshort2 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_short_2", layers=2, color=[[114, 168, 210, 255], [232, 177, 13, 255]], unlocked=False)
            cho_cloth_pantsshort3 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_short_3", layers=3, color=[[47, 150, 136, 255], [175, 220, 191, 255], [247, 152, 38, 255]], unlocked=False)
            cho_cloth_skirtshort1 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="skirt_short_1", layers=1, color=[[89, 116, 194, 255]], unlocked=False)
            cho_cloth_skirtshort2 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="skirt_short_2", layers=1, color=[[93, 119, 173, 255]], unlocked=False)
            cho_cloth_pantslong2 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_long_2", layers=2, color=[[109, 105, 121, 255], [213, 161, 13, 255]])
            cho_cloth_pantsshort4 = cloth_class(char="cho", category="bottoms", subcat="trousers", type="bottom", id="pants_short_4", layers=2, color=[[109, 105, 121, 255], [213, 161, 13, 255]], whoring=6)
            cho_cloth_quidskirt1 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="quid_skirt_1", layers=2, color=[[64, 84, 141, 255], [213, 161, 13, 255]], unlocked=False, whoring=8)
            
            # Bras
            cho_cloth_basicbra1 = cloth_class(char="cho", category="bras", subcat="bras", type="bra", id="basic_bra_1", layers=2, color=[[230, 230, 231, 255], [89, 116, 194, 255]])
            cho_cloth_bikinitop1 = cloth_class(char="cho", category="bras", subcat="bras", type="bra", id="bikini_top_1", layers=1, color=[[3, 237, 234, 255]], unlocked=False)
            cho_cloth_bikinitop2 = cloth_class(char="cho", category="bras", subcat="bras", type="bra", id="bikini_top_2", layers=1, color=[[138, 22, 17, 255]], unlocked=False)
            cho_cloth_lacebra1 = cloth_class(char="cho", category="bras", subcat="bras", type="bra", id="lace_bra_1", layers=3, color=[[100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]], unlocked=False)
            cho_cloth_sportbra1 = cloth_class(char="cho", category="bras", subcat="bras", type="bra", id="sport_bra_1", layers=1, color=[[156, 204, 249, 255]])
            
            # Panties
            cho_cloth_basicpanties1 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="basic_panties_1", layers=2, color=[[230, 230, 231, 255], [89, 116, 194, 255]])
            cho_cloth_bikinibottom1 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="bikini_bottom_1", layers=1, color=[[213, 161, 13, 255]], unlocked=False, whoring=14)
            cho_cloth_bikinibottom2 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="bikini_bottom_2", layers=1, color=[[213, 161, 13, 255]], unlocked=False, whoring=18)
            cho_cloth_lacepanties1 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="lace_panties_1", layers=3, color=[[100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]], unlocked=False, whoring=12)
            cho_cloth_sportpanties1 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="sport_panties_1", layers=1, color=[[156, 204, 249, 255]])
            cho_cloth_sportpanties2 = cloth_class(char="cho", category="panties", subcat="panties", type="panties", id="sport_panties_2", layers=1, color=[[156, 204, 249, 255]])
            
            # Robes
            cho_cloth_dress1 = cloth_class(char="cho", category="tops", subcat="onepieces", type="top", id="dress_1", layers=2, color=[[231, 29, 41, 255], [242, 162, 73, 255]], armfix=True, unlocked=False)
            
            # Hair
            cho_hair_ponytail = cloth_class(char="cho", category="head", subcat="hair", type="hair", id="ponytail", layers=2, color=[[52, 59, 80, 255], [70, 90, 147, 255]])
            cho_hair_pigtails = cloth_class(char="cho", category="head", subcat="hair", type="hair", id="pigtails", layers=3, color=[[52, 59, 80, 255], [70, 90, 147, 255], [242, 162, 73, 255]], unlocked=False, whoring=8)
            
            # Pelvis
            cho_pubes_thick = cloth_class(char="cho", category="pelvis", subcat="pubes", type="pubes", id="thick", layers=2, color=[[52, 59, 80, 255], [70, 90, 147, 255]])
            cho_pubes_heart = cloth_class(char="cho", category="pelvis", subcat="pubes", type="pubes", id="heart", layers=2, color=[[52, 59, 80, 255], [70, 90, 147, 255]])
            
            cho_tattoopelvis_free = cloth_class(char="cho", category="pelvis", subcat="tattoos", type="tattoo0", id="pelv_free", layers=1, color=[[0, 0, 1, 255]])
            
            cho_piercingpelvis_stud = cloth_class(char="cho", category="pelvis", subcat="piercing", type="piercing0", id="stud", layers=1, color=[[220, 220, 221, 255]])
            
            cho_tattoobreasts_slut = cloth_class(char="cho", category="breasts", subcat="tattoos", type="tattoo1", id="breasts_slut", layers=1, color=[[0, 0, 1, 255]])
            cho_piercingbreasts_barbell = cloth_class(char="cho", category="breasts", subcat="piercing", type="piercing1", id="breast_barbell", layers=1, color=[[220, 220, 221, 255]])
            
            # Hats&stuff
            
            cho_hats_catears = cloth_class(char="cho", category="head", subcat="hats", type="hat", id="catears", layers=1, color=[[70, 90, 147, 255]])
            cho_hats_witch = cloth_class(char="cho", category="head", subcat="hats", type="hat", id="witch", layers=2, color=[[71, 51, 102, 255], [215, 170, 98, 255]])
            cho_glasses1 = cloth_class(char="cho", category="head", subcat="glasses", type="accessory4", id="glasses1", layers=1, color=[[240, 240, 241, 255]])
            cho_goggles2 = cloth_class(char="cho", category="head", subcat="hats", type="hat", id="goggles", layers=2, color=[[137, 150, 193, 255], [165, 165, 166, 255]])
            # Neckwear
            cho_cloth_chokerlace1= cloth_class(char="cho", category="head", subcat="neckwear", type="neckwear", id="choker_lace_1", layers=2, color=[[100, 100, 255, 255], [220, 220, 221, 255]], unlocked=False)
            cho_cloth_tie1= cloth_class(char="cho", category="head", subcat="neckwear", type="neckwear", id="tie_1", layers=2, color=[[216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_chokermedallion= cloth_class(char="cho", category="head", subcat="neckwear", type="neckwear", id="choker_medallion", layers=1, color=[[25, 25, 26, 255]])
            cho_cloth_collarleather1= cloth_class(char="cho", category="head", subcat="neckwear", type="neckwear", id="collar_leather_1", layers=1, color=[[56, 56, 57, 255]])
            
            cho_makeup_blush=cloth_class(char="cho", category="makeup", subcat="blush", type="makeup0", id="blush", layers=1, color=[[238, 113, 196, 255]], unlocked=False)
            
            # Stockings
            cho_cloth_lace_stockings_1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="lace_stockings_1", layers=2, color=[[100, 100, 255, 255], [220, 220, 221, 255]], unlocked=False)
            cho_cloth_fishnet_stockings_1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="fishnet", layers=2, color=[[100, 100, 101, 255], [50, 50, 51, 255]])
            cho_cloth_sailor_stockings_1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="sailor", layers=1, color=[[232, 232, 233, 255]], unlocked=False)
            cho_cloth_quidstocking1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="quid1", layers=2, color=[[64, 84, 141, 255], [213, 161, 13, 255]], unlocked=False, whoring=8)
            
            # Garterbelts
            cho_cloth_lacegarter1 = cloth_class(char="cho", category="legwear", subcat="garterbelts", type="garterbelt", id="lace_garter_1", layers=4, color=[[220, 220, 221, 255], [100, 100, 255, 255], [220, 220, 221, 255], [89, 116, 194, 255]], unlocked=False)
            cho_cloth_house_stockings_1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="house", layers=2, color=[[216, 163, 10, 255], [89, 116, 194, 255]])
            cho_cloth_pantyhose_stockings_1 = cloth_class(char="cho", category="legwear", subcat="stockings", type="stockings", id="pantyhose", layers=1, color=[[190, 146, 129, 255]])
            
            # Accessories
            cho_acc_suspenders = cloth_class(char="cho", category="misc", subcat="accessory", type="accessory3", id="suspenders", layers=2, color=[[137, 22, 17, 255], [229, 140, 33, 255]], unlocked=False)
            cho_earring_feather = cloth_class(char="cho", category="head", subcat="earrings", type="earring", id="feather", layers=3, color=[[232, 232, 232, 255], [70, 90, 147, 255], [136, 91, 34, 255]], unlocked=False)
            cho_earring_basic = cloth_class(char="cho", category="head", subcat="earrings", type="earring", id="basic", layers=1, color=[[220, 220, 221, 255]])
            cho_earring_snitch = cloth_class(char="cho", category="head", subcat="earrings", type="earring", id="snitch", layers=2, color=[[220, 220, 221, 255], [213, 161, 13, 255]], unlocked=False)
            
            # Quidditch seperate category
            choq_cloth_robequidditch1 = cloth_class(char="cho", category="event", subcat="robes", type="robe", id="robe_quidditch_1", layers=2, color=[[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
            choq_cloth_topsweater1 = cloth_class(char="cho", category="event", subcat="tops", type="top", id="top_sweater_1", layers=2, color=[[89, 116, 194, 255], [213, 161, 13, 255]], armfix=True)
            choq_cloth_pantslong2 = cloth_class(char="cho", category="event", subcat="bottoms", type="bottom", id="pants_long_2", layers=2, color=[[109, 105, 121, 255], [213, 161, 13, 255]])
            choq_cloth_pantsshort4 = cloth_class(char="cho", category="event", subcat="bottoms", type="bottom", id="pants_short_4", layers=2, color=[[109, 105, 121, 255], [213, 161, 13, 255]])
            choq_cloth_glovesquidditch1 = cloth_class(char="cho", category="event", subcat="gloves", type="gloves", id="quidditch", layers=1, color=[[213, 161, 13, 255]], armfix=True)
            choq_goggles = cloth_class(char="cho", category="event", subcat="miscellaneous", type="hat", id="goggles", layers=2, color=[[137, 150, 193, 255], [165, 165, 166, 255]])
            choq_goggles_face = cloth_class(char="cho", category="event", subcat="miscellaneous", type="hat", id="goggles_face", layers=2, color=[[137, 150, 193, 255], [165, 165, 166, 255]], unlocked=False)
            choq_cloth_schoolskirt3 = cloth_class(char="cho", category="bottoms", subcat="skirts", type="bottom", id="school_skirt_3", layers=2, color=[[103, 90, 108, 255], [232, 177, 13, 255]], unlocked=False)
            
            cho_outfit_quidditch = outfit_class(name="Quidditch", group=[choq_cloth_topsweater1, choq_cloth_pantslong2, choq_cloth_robequidditch1, choq_cloth_glovesquidditch1, cho_cloth_basicpanties1])
            
            # Temporal save
            cho_outfit_last = outfit_class(name="Last worn items", group=[cho_hair_ponytail])
            
            #Unlockables
            cho_outfit_party = outfit_class(name="Party", group=[cho_hair_ponytail, cho_cloth_skirtshort2, cho_cloth_bikinitop1])
            cho_outfit_trainee = outfit_class(name="Trainee", group=[cho_hair_ponytail, cho_cloth_basicbra1, cho_cloth_basicpanties1, cho_cloth_schoolskirt2, cho_cloth_topschool3, cho_cloth_pantyhose_stockings_1, cho_earring_basic])
            cho_outfit_sailor = outfit_class(name="Sailor", group=[cho_hair_ponytail, cho_cloth_topsailor1, cho_cloth_skirtshort1, cho_cloth_sailor_stockings_1, cho_cloth_bikinibottom2])
            cho_outfit_misty = outfit_class(name="Misty", group=[cho_hair_ponytail, cho_acc_suspenders, cho_cloth_topshirt1, cho_cloth_pantsshort3])
            cho_outfit_bikini = outfit_class(name="Bikini", group=[cho_hair_ponytail, cho_cloth_bikinitop2, cho_cloth_bikinibottom1])
            cho_outfit_lacelingerie = outfit_class(name="Lingerie", group=[cho_hair_ponytail, cho_cloth_chokerlace1, cho_cloth_lacegarter1, cho_cloth_lacepanties1, cho_cloth_lacebra1, cho_cloth_lace_stockings_1, cho_earring_feather])
            cho_outfit_dress1 = outfit_class(name="Lingerie", group=[cho_hair_ponytail, cho_cloth_dress1])
            cho_outfit_cheerleader = outfit_class(name="Cheerleader", group=[cho_hair_pigtails, cho_earring_snitch, cho_cloth_quidstocking1, cho_cloth_sportpanties2, cho_cloth_sportbra1, cho_cloth_quidskirt1, cho_cloth_topquid1, cho_makeup_blush])
            
            cho_outfit_custom = outfit_class(name="Default", group=[cho_hair_ponytail, cho_cloth_topschool1, cho_cloth_schoolskirt1, cho_cloth_basicbra1, cho_cloth_basicpanties1], unlocked=True) # Don't change
        
            ################
            #              #
            #   DEFAULTS   #
            #              #
            ################
        
            cho_class.body = {
                        "armleft":     ["arm_down_l", 18, 0, 0, False],
                        "armright":    ["arm_down_r", 1, 0, 0, False],
                        "breasts":     ["breasts_bikini_tan", 3, 0, 0, False],
                        "base":        ["base_01", 2, 0, 0, False],
                        "legs":        [None, 4, 0, 0, False],
                        "animation":   [None, 1, 0, 0, False]}
                        
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
                        "hair":       [cho_hair_ponytail, 12, 0, 0, False],
                        "earring":    [None, 22, 0, 0, False],
                        "neckwear":   [None, 17, 0, 0, False],
                        "robe":       [None, 21, 0, 0, False],
                        "gloves":     [None, 20, 0, 0, False],
                        "top":        [cho_cloth_topschool1, 19, 0, 0, False],
                        "bra":        [cho_cloth_basicbra1, 18, 0, 0, False],
                        "bottom":     [cho_cloth_schoolskirt1, 16, 0, 0, False],
                        "garterbelt": [None, 15, 0, 0, False],
                        "panties":    [cho_cloth_basicpanties1, 14, 0, 0, False],
                        "stockings":  [cho_cloth_house_stockings_1, 13, 0, 0, False],
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