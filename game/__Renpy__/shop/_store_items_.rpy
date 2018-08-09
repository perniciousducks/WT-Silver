label __init_variables:



    # Dyes
    if not hasattr(renpy.store,'brown_dye_OBJ'): # Brown
        $ brown_dye_OBJ = store_item_class()
    $ brown_dye_OBJ.id = "brown_dye"
    $ brown_dye_OBJ.name = "Mud-Blood Brown"
    $ brown_dye_OBJ.type = "dye"
    $ brown_dye_OBJ.items = ["clothing dye","hair dye"]
    $ brown_dye_OBJ.image = "dye_brown.png"
    $ brown_dye_OBJ.cost = 20
    $ brown_dye_OBJ.description = "> Basic shade of brown. Simple yet elegant!"

    if not hasattr(renpy.store,'yellow_dye_OBJ'): # Yellow
        $ yellow_dye_OBJ = store_item_class()
    $ yellow_dye_OBJ.id = "yellow_dye"
    $ yellow_dye_OBJ.name = "Niffler's Gold"
    $ yellow_dye_OBJ.type = "dye"
    $ yellow_dye_OBJ.items = ["clothing dye","hair dye"]
    $ yellow_dye_OBJ.image = "dye_yellow.png"
    $ yellow_dye_OBJ.cost = 40
    $ yellow_dye_OBJ.description = "> A very nice shade of yellow."

    if not hasattr(renpy.store,'orange_dye_OBJ'): # Orange
        $ orange_dye_OBJ = store_item_class()
    $ orange_dye_OBJ.id = "orange_dye"
    $ orange_dye_OBJ.name = "Butter Beer"
    $ orange_dye_OBJ.type = "dye"
    $ orange_dye_OBJ.items = ["clothing dye"]
    $ orange_dye_OBJ.image = "dye_orange.png"
    $ orange_dye_OBJ.cost = 60
    $ orange_dye_OBJ.description = "> A very nice shade of orange."

    if not hasattr(renpy.store,'red_dye_OBJ'): # Red
        $ red_dye_OBJ = store_item_class()
    $ red_dye_OBJ.id = "red_dye"
    $ red_dye_OBJ.name = "Weasel Red"
    $ red_dye_OBJ.type = "dye"
    $ red_dye_OBJ.items = ["clothing dye","hair dye"]
    $ red_dye_OBJ.image = "dye_red.png"
    $ red_dye_OBJ.cost = 60
    $ red_dye_OBJ.description = "> A very nice shade of red."

    if not hasattr(renpy.store,'crimson_dye_OBJ'): # Crimson
        $ crimson_dye_OBJ = store_item_class()
    $ crimson_dye_OBJ.id = "crimson_dye"
    $ crimson_dye_OBJ.name = "Crimson Lion"
    $ crimson_dye_OBJ.type = "dye"
    $ crimson_dye_OBJ.items = ["clothing dye","hair dye"]
    $ crimson_dye_OBJ.image = "dye_crimson.png"
    $ crimson_dye_OBJ.cost = 80
    $ crimson_dye_OBJ.description = "> A very rich shade of red."

    if not hasattr(renpy.store,'green_dye_OBJ'): # Green
        $ green_dye_OBJ = store_item_class()
    $ green_dye_OBJ.id = "green_dye"
    $ green_dye_OBJ.name = "Bowtruckle Paint"
    $ green_dye_OBJ.type = "dye"
    $ green_dye_OBJ.items = ["clothing dye"]
    $ green_dye_OBJ.image = "dye_green.png"
    $ green_dye_OBJ.cost = 60
    $ green_dye_OBJ.description = "> A bright shade of green."

    if not hasattr(renpy.store,'dark_green_dye_OBJ'): # Dark Green
        $ dark_green_dye_OBJ = store_item_class()
    $ dark_green_dye_OBJ.id = "dark_green_dye"
    $ dark_green_dye_OBJ.name = "Serpent Green"
    $ dark_green_dye_OBJ.type = "dye"
    $ dark_green_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_green_dye_OBJ.image = "dye_dark_green.png"
    $ dark_green_dye_OBJ.cost = 80
    $ dark_green_dye_OBJ.description = "> A darker shade of green."

    if not hasattr(renpy.store,'blue_dye_OBJ'): # Blue
        $ blue_dye_OBJ = store_item_class()
    $ blue_dye_OBJ.id = "blue_dye"
    $ blue_dye_OBJ.name = "Pixie Dye"
    $ blue_dye_OBJ.type = "dye"
    $ blue_dye_OBJ.items = ["clothing dye"]
    $ blue_dye_OBJ.image = "dye_blue.png"
    $ blue_dye_OBJ.cost = 60
    $ blue_dye_OBJ.description = "> A bright shade of blue."

    if not hasattr(renpy.store,'dark_blue_dye_OBJ'): # Dark Blue
        $ dark_blue_dye_OBJ = store_item_class()
    $ dark_blue_dye_OBJ.id = "dark_blue_dye"
    $ dark_blue_dye_OBJ.name = "Raven Blue"
    $ dark_blue_dye_OBJ.type = "dye"
    $ dark_blue_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_blue_dye_OBJ.image = "dye_dark_blue.png"
    $ dark_blue_dye_OBJ.cost = 80
    $ dark_blue_dye_OBJ.description = "> A darker shade of blue."

    if not hasattr(renpy.store,'purple_dye_OBJ'): # Purple
        $ purple_dye_OBJ = store_item_class()
    $ purple_dye_OBJ.id = "purple_dye"
    $ purple_dye_OBJ.name = "Pygmy Puff Purple"
    $ purple_dye_OBJ.type = "dye"
    $ purple_dye_OBJ.items = ["clothing dye","hair dye"]
    $ purple_dye_OBJ.image = "dye_purple.png"
    $ purple_dye_OBJ.cost = 120
    $ purple_dye_OBJ.description = "> A very nice shade of purple."

    if not hasattr(renpy.store,'pink_dye_OBJ'): # Pink
        $ pink_dye_OBJ = store_item_class()
    $ pink_dye_OBJ.id = "pink_dye"
    $ pink_dye_OBJ.name = "Pussy Pink"
    $ pink_dye_OBJ.type = "dye"
    $ pink_dye_OBJ.items = ["clothing dye","hair dye"]
    $ pink_dye_OBJ.image = "dye_pink.png"
    $ pink_dye_OBJ.cost = 200
    $ pink_dye_OBJ.description = "> A color so pink, it makes you want to\n  cover your whole room with it!"

    if not hasattr(renpy.store,'gray_dye_OBJ'): # Gray
        $ gray_dye_OBJ = store_item_class()
    $ gray_dye_OBJ.id = "gray_dye"
    $ gray_dye_OBJ.name = "Ghostly Gray"
    $ gray_dye_OBJ.type = "dye"
    $ gray_dye_OBJ.items = ["clothing dye","hair dye"]
    $ gray_dye_OBJ.image = "dye_gray.png"
    $ gray_dye_OBJ.cost = 200
    $ gray_dye_OBJ.description = "> A very classy shade of gray."

    if not hasattr(renpy.store,'black_dye_OBJ'): # Black
        $ black_dye_OBJ = store_item_class()
    $ black_dye_OBJ.id = "black_dye"
    $ black_dye_OBJ.name = "Seriously Black"
    $ black_dye_OBJ.type = "dye"
    $ black_dye_OBJ.items = ["clothing dye","hair dye"]
    $ black_dye_OBJ.image = "dye_black.png"
    $ black_dye_OBJ.cost = 400
    $ black_dye_OBJ.description = "> As black as a Testral."

    if not hasattr(renpy.store,'white_dye_OBJ'): # White
        $ white_dye_OBJ = store_item_class()
    $ white_dye_OBJ.id = "white_dye"
    $ white_dye_OBJ.name = "Patroni White"
    $ white_dye_OBJ.type = "dye"
    $ white_dye_OBJ.items = ["clothing dye"]
    $ white_dye_OBJ.image = "dye_white.png"
    $ white_dye_OBJ.cost = 400
    $ white_dye_OBJ.description = "> As bright and pure as a Patronus!"

    $ dye_list = []
    $ dye_list.append(brown_dye_OBJ)
    $ dye_list.append(yellow_dye_OBJ)
    $ dye_list.append(orange_dye_OBJ)
    $ dye_list.append(red_dye_OBJ)
    $ dye_list.append(crimson_dye_OBJ)
    $ dye_list.append(green_dye_OBJ)
    $ dye_list.append(dark_green_dye_OBJ)
    $ dye_list.append(blue_dye_OBJ)
    $ dye_list.append(dark_blue_dye_OBJ)
    $ dye_list.append(purple_dye_OBJ)
    $ dye_list.append(pink_dye_OBJ)
    $ dye_list.append(gray_dye_OBJ)
    $ dye_list.append(black_dye_OBJ)
    $ dye_list.append(white_dye_OBJ)


    # Clothing Sets
    if not hasattr(renpy.store,'hg_cheer_g_OBJ'):
        $ hg_cheer_g_OBJ = store_item_class()
    $ hg_cheer_g_OBJ.id = "hg_cheer_g"
    $ hg_cheer_g_OBJ.name = "Gryffindor Cheerleader"
    $ hg_cheer_g_OBJ.type = "set"
    $ hg_cheer_g_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_g_OBJ.cost = 80
    $ hg_cheer_g_OBJ.wait_time = 2
    $ hg_cheer_g_OBJ.image = "hg_cheer_g.png"
    $ hg_cheer_g_OBJ.description = "> A basic Cheerleader attire for Gryffindor's\n  Quidditch team.\n> Inludes a ."

    if not hasattr(renpy.store,'hg_cheer_g_sexy_OBJ'):
        $ hg_cheer_g_sexy_OBJ = store_item_class()
    $ hg_cheer_g_sexy_OBJ.id = "hg_cheer_g_sexy"
    $ hg_cheer_g_sexy_OBJ.name = "Sexy Gryffindor Cheerleader"
    $ hg_cheer_g_sexy_OBJ.type = "set"
    $ hg_cheer_g_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_g_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after speaking to Tonks.
    $ hg_cheer_g_sexy_OBJ.cost = 140
    $ hg_cheer_g_sexy_OBJ.wait_time = 1
    $ hg_cheer_g_sexy_OBJ.image = "hg_cheer_g_sexy.png"
    $ hg_cheer_g_sexy_OBJ.description = "> A sexy version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_s_OBJ'):
        $ hg_cheer_s_OBJ = store_item_class()
    $ hg_cheer_s_OBJ.id = "hg_cheer_s"
    $ hg_cheer_s_OBJ.name = "Slythrin Cheerleader"
    $ hg_cheer_s_OBJ.type = "set"
    $ hg_cheer_s_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_s_OBJ.cost = 80
    $ hg_cheer_s_OBJ.wait_time = 2
    $ hg_cheer_s_OBJ.image = "hg_cheer_s.png"
    $ hg_cheer_s_OBJ.description = "> The Slytherin version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_s_sexy_OBJ'):
        $ hg_cheer_s_sexy_OBJ = store_item_class()
    $ hg_cheer_s_sexy_OBJ.id = "hg_cheer_s_sexy"
    $ hg_cheer_s_sexy_OBJ.name = "Sexy Slythrin Cheerleader"
    $ hg_cheer_s_sexy_OBJ.type = "set"
    $ hg_cheer_s_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_s_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after speaking to Tonks.
    $ hg_cheer_s_sexy_OBJ.cost = 140
    $ hg_cheer_s_sexy_OBJ.wait_time = 1
    $ hg_cheer_s_sexy_OBJ.image = "hg_cheer_s_sexy.png"
    $ hg_cheer_s_sexy_OBJ.description = "> The sexy version of the Slytherin Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_r_OBJ'):
        $ hg_cheer_r_OBJ = store_item_class()
    $ hg_cheer_r_OBJ.id = "hg_cheer_r"
    $ hg_cheer_r_OBJ.name = "Ravenclaw Cheerleader"
    $ hg_cheer_r_OBJ.type = "set"
    $ hg_cheer_r_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_r_OBJ.cost = 80
    $ hg_cheer_r_OBJ.wait_time = 2
    $ hg_cheer_r_OBJ.image = "hg_cheer_r.png"
    $ hg_cheer_r_OBJ.description = "The Ravenclaw version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_r_sexy_OBJ'):
        $ hg_cheer_r_sexy_OBJ = store_item_class()
    $ hg_cheer_r_sexy_OBJ.id = "hg_cheer_r_sexy"
    $ hg_cheer_r_sexy_OBJ.name = "Sexy Ravenclaw Cheerleader"
    $ hg_cheer_r_sexy_OBJ.type = "set"
    $ hg_cheer_r_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_r_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after speaking to Tonks.
    $ hg_cheer_r_sexy_OBJ.cost = 140
    $ hg_cheer_r_sexy_OBJ.wait_time = 1
    $ hg_cheer_r_sexy_OBJ.image = "hg_cheer_r_sexy.png"
    $ hg_cheer_r_sexy_OBJ.description = "> The sexy version of the Ravenclaw Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_h_OBJ'):
        $ hg_cheer_h_OBJ = store_item_class()
    $ hg_cheer_h_OBJ.id = "hg_cheer_h"
    $ hg_cheer_h_OBJ.name = "Hufflepuff Cheerleader"
    $ hg_cheer_h_OBJ.type = "set"
    $ hg_cheer_h_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_h_OBJ.cost = 80
    $ hg_cheer_h_OBJ.wait_time = 2
    $ hg_cheer_h_OBJ.image = "hg_cheer_h.png"
    $ hg_cheer_h_OBJ.description = "> The Hufflepuff version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_h_sexy_OBJ'):
        $ hg_cheer_h_sexy_OBJ = store_item_class()
    $ hg_cheer_h_sexy_OBJ.id = "hg_cheer_h_sexy"
    $ hg_cheer_h_sexy_OBJ.name = "Sexy Hufflepuff Cheerleader"
    $ hg_cheer_h_sexy_OBJ.type = "set"
    $ hg_cheer_h_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_h_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after speaking to Tonks.
    $ hg_cheer_h_sexy_OBJ.cost = 140
    $ hg_cheer_h_sexy_OBJ.wait_time = 1
    $ hg_cheer_h_sexy_OBJ.image = "hg_cheer_h_sexy.png"
    $ hg_cheer_h_sexy_OBJ.description = "> The sexy version of the Hufflepuff cheerleader attire."


    # Lingerie
    if not hasattr(renpy.store,'hg_lingerie_lace_OBJ'):
        $ hg_lingerie_lace_OBJ = store_item_class()
    $ hg_lingerie_lace_OBJ.id = "hg_lingerie_lace"
    $ hg_lingerie_lace_OBJ.name = "Lace Lingerie"
    $ hg_lingerie_lace_OBJ.type = "set"
    $ hg_lingerie_lace_OBJ.items = ["bra","panties"]
    $ hg_lingerie_lace_OBJ.cost = 40
    $ hg_lingerie_lace_OBJ.wait_time = 1
    $ hg_lingerie_lace_OBJ.image = "hg_lingerie_lace.png"
    $ hg_lingerie_lace_OBJ.description = "> A lovely lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_silk_OBJ'):
        $ hg_lingerie_silk_OBJ = store_item_class()
    $ hg_lingerie_silk_OBJ.id = "hg_lingerie_silk"
    $ hg_lingerie_silk_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_silk_OBJ.type = "set"
    $ hg_lingerie_silk_OBJ.items = ["bra","panties"]
    $ hg_lingerie_silk_OBJ.cost = 80
    $ hg_lingerie_silk_OBJ.wait_time = 1
    $ hg_lingerie_silk_OBJ.image = "hg_lingerie_silk.png"
    $ hg_lingerie_silk_OBJ.description = "> A smooth and comfortable lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_maid_OBJ'):
        $ hg_lingerie_maid_OBJ = store_item_class()
    $ hg_lingerie_maid_OBJ.id = "hg_lingerie_maid"
    $ hg_lingerie_maid_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_maid_OBJ.type = "set"
    $ hg_lingerie_maid_OBJ.items = ["bra","panties","gloves","stockings","hair","hat"]
    $ hg_lingerie_maid_OBJ.cost = 160
    $ hg_lingerie_maid_OBJ.wait_time = 2
    $ hg_lingerie_maid_OBJ.image = "hg_lingerie_maid.png"
    $ hg_lingerie_maid_OBJ.description = "> A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts."

    if not hasattr(renpy.store,'hg_lingerie_latex_OBJ'):
        $ hg_lingerie_latex_OBJ = store_item_class()
    $ hg_lingerie_latex_OBJ.id = "hg_lingerie_latex"
    $ hg_lingerie_latex_OBJ.name = "Latex Lingerie"
    $ hg_lingerie_latex_OBJ.type = "set"
    $ hg_lingerie_latex_OBJ.items = ["bra","panties","gloves","stockings"]
    $ hg_lingerie_latex_OBJ.cost = 200
    $ hg_lingerie_latex_OBJ.wait_time = 2
    $ hg_lingerie_latex_OBJ.image = "hg_lingerie_latex.png"
    $ hg_lingerie_latex_OBJ.description = "> A tight and shiny lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_fishnet_OBJ'):
        $ hg_lingerie_fishnet_OBJ = store_item_class()
    $ hg_lingerie_fishnet_OBJ.id = "hg_lingerie_fishnet"
    $ hg_lingerie_fishnet_OBJ.name = "Fishnet Lingerie"
    $ hg_lingerie_fishnet_OBJ.type = "set"
    $ hg_lingerie_fishnet_OBJ.items = ["top","bra","panties"]
    $ hg_lingerie_fishnet_OBJ.cost = 100
    $ hg_lingerie_fishnet_OBJ.wait_time = 1
    $ hg_lingerie_fishnet_OBJ.image = "hg_lingerie_fishnet.png"
    $ hg_lingerie_fishnet_OBJ.description = "> A tight and shiny lace bra and panty set."


    # Nighties
    if not hasattr(renpy.store,'hg_nighty_silk_OBJ'):
        $ hg_nighty_silk_OBJ = store_item_class()
    $ hg_nighty_silk_OBJ.id = "hg_nighty_silk"
    $ hg_nighty_silk_OBJ.name = "Silk Nighty"
    $ hg_nighty_silk_OBJ.type = "set"
    $ hg_nighty_silk_OBJ.items = ["one-piece","panties"]
    $ hg_nighty_silk_OBJ.cost = 80
    $ hg_nighty_silk_OBJ.wait_time = 1
    $ hg_nighty_silk_OBJ.image = "hg_nighty_silk.png"
    $ hg_nighty_silk_OBJ.description = "> A comfortable yet elegant Nightwear set."

    if not hasattr(renpy.store,'hg_nightgown_OBJ'):
        $ hg_nightgown_OBJ = store_item_class()
    $ hg_nightgown_OBJ.id = "hg_nighty_silk"
    $ hg_nightgown_OBJ.name = "Silk Nightgown"
    $ hg_nightgown_OBJ.type = "set"
    $ hg_nightgown_OBJ.items = ["one-piece"]
    $ hg_nightgown_OBJ.cost = 80
    $ hg_nightgown_OBJ.wait_time = 1
    $ hg_nightgown_OBJ.image = "hg_nightgown.png"
    $ hg_nightgown_OBJ.description = "> A more free-flowing set of Nightwear."


    # Bikinis
    if not hasattr(renpy.store,'hg_bikini_latex_OBJ'):
        $ hg_bikini_latex_OBJ = store_item_class()
    $ hg_bikini_latex_OBJ.id = "hg_bikini_latex"
    $ hg_bikini_latex_OBJ.name = "Latex Bikini"
    $ hg_bikini_latex_OBJ.type = "set"
    $ hg_bikini_latex_OBJ.items = ["bra","panties"]
    $ hg_bikini_latex_OBJ.cost = 100
    $ hg_bikini_latex_OBJ.wait_time = 1
    $ hg_bikini_latex_OBJ.image = "hg_bikini_latex.png"
    $ hg_bikini_latex_OBJ.description = "> A set for when you want to become one with your underwear"

    if not hasattr(renpy.store,'hg_bikini_sling_OBJ'):
        $ hg_bikini_sling_OBJ = store_item_class()
    $ hg_bikini_sling_OBJ.id = "hg_bikini_sling"
    $ hg_bikini_sling_OBJ.name = "Sling Bikini"
    $ hg_bikini_sling_OBJ.type = "set"
    $ hg_bikini_sling_OBJ.items = ["bra","panties"]
    $ hg_bikini_sling_OBJ.cost = 69
    $ hg_bikini_sling_OBJ.wait_time = 1
    $ hg_bikini_sling_OBJ.image = "hg_bikini_sling.png"
    $ hg_bikini_sling_OBJ.description = "Temp J"


    # One-pieces
    if not hasattr(renpy.store,'hg_onepiece_sling_OBJ'):
        $ hg_onepiece_sling_OBJ = store_item_class()
    $ hg_onepiece_sling_OBJ.id = "hg_onepiece_sling"
    $ hg_onepiece_sling_OBJ.name = "Sling Monokini"
    $ hg_onepiece_sling_OBJ.type = "set"
    $ hg_onepiece_sling_OBJ.items = ["one-piece"]
    $ hg_onepiece_sling_OBJ.cost = 69
    $ hg_onepiece_sling_OBJ.wait_time = 1
    $ hg_onepiece_sling_OBJ.image = "hg_onepiece_sling.png"
    $ hg_onepiece_sling_OBJ.description = "Temp J"



    if not hasattr(renpy.store,'hg_muggle_cold_OBJ'):
        $ hg_muggle_cold_OBJ = store_item_class()
    $ hg_muggle_cold_OBJ.id = "hg_muggle_cold"
    $ hg_muggle_cold_OBJ.name = "Cold Weather Clothing"
    $ hg_muggle_cold_OBJ.type = "set"
    $ hg_muggle_cold_OBJ.items = ["pullover A","pullover B","long jeans"]
    $ hg_muggle_cold_OBJ.cost = 80
    $ hg_muggle_cold_OBJ.wait_time = 1
    $ hg_muggle_cold_OBJ.image = "hg_muggle_cold.png"
    $ hg_muggle_cold_OBJ.description = "> A more muggle styled set of clothes for cold weather."

    if not hasattr(renpy.store,'hg_muggle_hot_OBJ'):
        $ hg_muggle_hot_OBJ = store_item_class()
    $ hg_muggle_hot_OBJ.id = "hg_muggle_hot"
    $ hg_muggle_hot_OBJ.name = "Hot Weather Clothing"
    $ hg_muggle_hot_OBJ.type = "set"
    $ hg_muggle_hot_OBJ.items = ["top","short jeans"]
    $ hg_muggle_hot_OBJ.cost = 100
    $ hg_muggle_hot_OBJ.wait_time = 1
    $ hg_muggle_hot_OBJ.image = "hg_muggle_hot.png"
    $ hg_muggle_hot_OBJ.description = "> A more muggle styled set of clothes for warm weather"

    if not hasattr(renpy.store,'hg_muggle_rainy_OBJ'):
        $ hg_muggle_rainy_OBJ = store_item_class()
    $ hg_muggle_rainy_OBJ.id = "hg_muggle_rainy"
    $ hg_muggle_rainy_OBJ.name = "Rainy Weather Clothing"
    $ hg_muggle_rainy_OBJ.type = "set"
    $ hg_muggle_rainy_OBJ.items = ["sweater","long jeans"]
    $ hg_muggle_rainy_OBJ.cost = 60
    $ hg_muggle_rainy_OBJ.wait_time = 1
    $ hg_muggle_rainy_OBJ.image = "hg_muggle_rainy.png"
    $ hg_muggle_rainy_OBJ.description = "> A more muggle styled set of clothes for rainy weather."

    if not hasattr(renpy.store,'hg_punk_rocker_OBJ'):
        $ hg_punk_rocker_OBJ = store_item_class()
    $ hg_punk_rocker_OBJ.id = "hg_punk_rocker"
    $ hg_punk_rocker_OBJ.name = "Rocker"
    $ hg_punk_rocker_OBJ.type = "set"
    $ hg_punk_rocker_OBJ.items = ["top","bottom","gloves","choker"]
    $ hg_punk_rocker_OBJ.cost = 180
    $ hg_punk_rocker_OBJ.wait_time = 2
    $ hg_punk_rocker_OBJ.image = "hg_punk_rocker.png"
    $ hg_punk_rocker_OBJ.description = "> A punk-rock set of clothes for the more rebellious type of witch."

    $ hermione_clothing_sets_list = []
    $ hermione_clothing_sets_list.append(hg_cheer_g_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_g_sexy_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_s_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_s_sexy_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_r_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_r_sexy_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_h_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_h_sexy_OBJ)

    $ hermione_clothing_sets_list.append(hg_lingerie_lace_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_silk_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_maid_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_latex_OBJ)

    $ hermione_clothing_sets_list.append(hg_nighty_silk_OBJ)
    $ hermione_clothing_sets_list.append(hg_nightgown_OBJ)

    $ hermione_clothing_sets_list.append(hg_bikini_latex_OBJ)
    $ hermione_clothing_sets_list.append(hg_bikini_sling_OBJ)

    $ hermione_clothing_sets_list.append(hg_onepiece_sling_OBJ)

    $ hermione_clothing_sets_list.append(hg_muggle_cold_OBJ)
    $ hermione_clothing_sets_list.append(hg_muggle_hot_OBJ)
    $ hermione_clothing_sets_list.append(hg_muggle_rainy_OBJ)
    $ hermione_clothing_sets_list.append(hg_punk_rocker_OBJ)


    # Astoria
    if not hasattr(renpy.store,'ag_boss_uniform_OBJ'): #Like in Hugo Boss...
        $ ag_boss_uniform_OBJ = store_item_class()
    $ ag_boss_uniform_OBJ.name = "Boss Uniform"
    $ ag_boss_uniform_OBJ.cost = 500
    $ ag_boss_uniform_OBJ.type = "set"
    $ ag_boss_uniform_OBJ.items = ["top","bottom","hair","hat"]
    $ ag_boss_uniform_OBJ.wait_time = 3
    $ ag_boss_uniform_OBJ.image = "ag_boss_uniform.png"
    $ ag_boss_uniform_OBJ.hair_layer = "N"
    $ ag_boss_uniform_OBJ.description = "> A uniform I designed with an old friend of mine.\n  Makes me wonder what happened to Hugo..."

    $ astoria_clothing_sets_list = []
    $ astoria_clothing_sets_list.append(ag_boss_uniform_OBJ)





    return

init python:

    class store_item_class(object):
        id = ""
        name = ""
        type = ""
        items = []
        image = ""
        unlockable = False #If True, prevents this item to be shown in the shop.
        unlocked = False #Set to True once unlocked or purchased.
        cost = 60
        wait_time = 1
        description = "> Item for Purchase."

        def getStoreName(self):
            return self.name
        def getStoreWaitTime(self):
            if self.wait_time == 1:
                return "Wait Time: "+str(self.wait_time)+" day."
            else:
                return "Wait Time: "+str(self.wait_time)+" days."
        def getStoreDescription(self):
            return self.description
        def getStoreCost(self):
            return "Cost: "+str(self.cost)+" gold"
        def getStoreImage(self):
            return "interface/icons/"+self.type+"s/"+self.image
        def getStoreImageZoom(self):
            if self.type in ["dye"]:
                return 0.8
            else:
                return 1.0

        def getType(self):
            return self.type
        def getStoreItems(self):
            return self.items
