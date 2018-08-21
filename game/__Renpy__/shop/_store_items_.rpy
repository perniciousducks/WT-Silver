label __init_variables:

    #Single Clothing Items
    $ cs_clothing_list = []

    #Badges
    if not hasattr(renpy.store,'spew_badge_OBJ'):
        $ spew_badge_OBJ = store_item_class()
    $ spew_badge_OBJ.id = "spew_badge"
    $ spew_badge_OBJ.name = "S.P.E.W. Badge"
    $ spew_badge_OBJ.items = ["badge"]
    $ spew_badge_OBJ.image = "badge_spew.png"
    $ spew_badge_OBJ.cost = 5
    $ spew_badge_OBJ.description = "> A badge designed to show one's opposition of elf\n  slavery."

    if not hasattr(renpy.store,'I_love_cum_badge_OBJ'):
        $ I_love_cum_badge_OBJ = store_item_class()
    $ I_love_cum_badge_OBJ.id = "I_love_cum_badge"
    $ I_love_cum_badge_OBJ.name = "I <3 C.U.M. Badge"
    $ I_love_cum_badge_OBJ.items = ["badge"]
    $ I_love_cum_badge_OBJ.image = "badge_I_love_cum.png"
    $ I_love_cum_badge_OBJ.cost = 15
    $ I_love_cum_badge_OBJ.description = "> A badge that displays ones affection towards semen."

    #Ears
    if not hasattr(renpy.store,'cat_ears_OBJ'):
        $ cat_ears_OBJ = store_item_class()
    $ cat_ears_OBJ.id = "cat_ears"
    $ cat_ears_OBJ.name = "Cat Ears"
    $ cat_ears_OBJ.items = ["ears","tail"]
    $ cat_ears_OBJ.image = "ears_cat.png"
    $ cat_ears_OBJ.cost = 40
    $ cat_ears_OBJ.description = "> A fluffy set of catlike ears that matches one's\n  hair-color!"

    if not hasattr(renpy.store,'elf_ears_OBJ'):
        $ elf_ears_OBJ = store_item_class()
    $ elf_ears_OBJ.id = "elf_ears"
    $ elf_ears_OBJ.name = "Elf Ears"
    $ elf_ears_OBJ.items = ["ears"]
    $ elf_ears_OBJ.image = "ears_elf.png"
    $ elf_ears_OBJ.cost = 20
    $ elf_ears_OBJ.description = "> A pointy set of elven ears."

    #Glasses
    if not hasattr(renpy.store,'reading_glasses_OBJ'):
        $ reading_glasses_OBJ = store_item_class()
    $ reading_glasses_OBJ.id = "reading_glasses"
    $ reading_glasses_OBJ.name = "Reading Glasses"
    $ reading_glasses_OBJ.items = ["glasses"]
    $ reading_glasses_OBJ.image = "glasses_reading.png"
    $ reading_glasses_OBJ.cost = 50
    $ reading_glasses_OBJ.description = "> A lot of wizards are into girls wearing these!"

    if not hasattr(renpy.store,'vintage_glasses_OBJ'):
        $ vintage_glasses_OBJ = store_item_class()
    $ vintage_glasses_OBJ.id = "vintage_glasses"
    $ vintage_glasses_OBJ.name = "Vintage Glasses"
    $ vintage_glasses_OBJ.items = ["glasses"]
    $ vintage_glasses_OBJ.image = "glasses_vintage.png"
    $ vintage_glasses_OBJ.cost = 70
    $ vintage_glasses_OBJ.description = "> Wearing these doesn't automatically make you a nerd!"

    $ cs_accessories_list = []
    $ cs_accessories_list.append(spew_badge_OBJ)
    $ cs_accessories_list.append(I_love_cum_badge_OBJ)
    $ cs_accessories_list.append(cat_ears_OBJ)
    $ cs_accessories_list.append(elf_ears_OBJ)
    $ cs_accessories_list.append(reading_glasses_OBJ)
    $ cs_accessories_list.append(vintage_glasses_OBJ)
    python:
        for i in cs_accessories_list:
            i.type = "accessory"



    #Makeup
    if not hasattr(renpy.store,'red_lipstick_OBJ'):
        $ red_lipstick_OBJ = store_item_class()
    $ red_lipstick_OBJ.id = "red_lipstick"
    $ red_lipstick_OBJ.name = "Red Lipstick"
    $ red_lipstick_OBJ.type = "makeup"
    $ red_lipstick_OBJ.items = ["lipstick"]
    $ red_lipstick_OBJ.image = "lipstick_red.png"
    $ red_lipstick_OBJ.cost = 100
    $ red_lipstick_OBJ.description = "> They call this one the red rocket!"

    if not hasattr(renpy.store,'pink_lipstick_OBJ'):
        $ pink_lipstick_OBJ = store_item_class()
    $ pink_lipstick_OBJ.id = "pink_lipstick"
    $ pink_lipstick_OBJ.name = "Pink Lipstick"
    $ pink_lipstick_OBJ.type = "makeup"
    $ pink_lipstick_OBJ.items = ["lipstick"]
    $ pink_lipstick_OBJ.unlockable = True #Unlocked from potion event.
    $ pink_lipstick_OBJ.image = "lipstick_pink.png"

    if not hasattr(renpy.store,'freckles_makeup_OBJ'):
        $ freckles_makeup_OBJ = store_item_class()
    $ freckles_makeup_OBJ.id = "freckles_makeup"
    $ freckles_makeup_OBJ.name = "Freckles"
    $ freckles_makeup_OBJ.type = "makeup"
    $ freckles_makeup_OBJ.items = ["freckles"]
    $ freckles_makeup_OBJ.image = "makeup_freckles.png"
    $ freckles_makeup_OBJ.cost = 20
    $ freckles_makeup_OBJ.description = "> A magical item that makes the wearer's freckles more\n  pronounced!"

    if not hasattr(renpy.store,'fake_cum_makeup_OBJ'):
        $ fake_cum_makeup_OBJ = store_item_class()
    $ fake_cum_makeup_OBJ.id = "fake_cum_makeup"
    $ fake_cum_makeup_OBJ.name = "Fake Cum"
    $ fake_cum_makeup_OBJ.type = "makeup"
    $ fake_cum_makeup_OBJ.items = ["fake cum"]
    $ fake_cum_makeup_OBJ.image = "makeup_fake_cum.png"
    $ fake_cum_makeup_OBJ.cost = 20
    $ fake_cum_makeup_OBJ.description = "> When she doen't want to wear your real cum just yet.\n  Be patient!"

    $ cs_miscellaneous_list = []
    $ cs_miscellaneous_list.append(red_lipstick_OBJ)
    $ cs_miscellaneous_list.append(pink_lipstick_OBJ)
    $ cs_miscellaneous_list.append(freckles_makeup_OBJ)
    $ cs_miscellaneous_list.append(fake_cum_makeup_OBJ)


    # Dyes
    if not hasattr(renpy.store,'brown_dye_OBJ'): # Brown
        $ brown_dye_OBJ = store_item_class()
    $ brown_dye_OBJ.id = "brown_dye"
    $ brown_dye_OBJ.name = "Mud-Blood Brown"
    $ brown_dye_OBJ.items = ["clothing dye","hair dye"]
    $ brown_dye_OBJ.image = "dye_brown.png"
    $ brown_dye_OBJ.cost = 20
    $ brown_dye_OBJ.description = "> Basic shade of brown. Simple yet elegant!"

    if not hasattr(renpy.store,'yellow_dye_OBJ'): # Yellow
        $ yellow_dye_OBJ = store_item_class()
    $ yellow_dye_OBJ.id = "yellow_dye"
    $ yellow_dye_OBJ.name = "Niffler's Gold"
    $ yellow_dye_OBJ.items = ["clothing dye","hair dye"]
    $ yellow_dye_OBJ.image = "dye_yellow.png"
    $ yellow_dye_OBJ.cost = 40
    $ yellow_dye_OBJ.description = "> A very nice shade of yellow."

    if not hasattr(renpy.store,'orange_dye_OBJ'): # Orange
        $ orange_dye_OBJ = store_item_class()
    $ orange_dye_OBJ.id = "orange_dye"
    $ orange_dye_OBJ.name = "Butter Beer"
    $ orange_dye_OBJ.items = ["clothing dye"]
    $ orange_dye_OBJ.image = "dye_orange.png"
    $ orange_dye_OBJ.cost = 60
    $ orange_dye_OBJ.description = "> A very nice shade of orange."

    if not hasattr(renpy.store,'red_dye_OBJ'): # Red
        $ red_dye_OBJ = store_item_class()
    $ red_dye_OBJ.id = "red_dye"
    $ red_dye_OBJ.name = "Weasel Red"
    $ red_dye_OBJ.items = ["clothing dye","hair dye"]
    $ red_dye_OBJ.image = "dye_red.png"
    $ red_dye_OBJ.cost = 60
    $ red_dye_OBJ.description = "> A very nice shade of red."

    if not hasattr(renpy.store,'crimson_dye_OBJ'): # Crimson
        $ crimson_dye_OBJ = store_item_class()
    $ crimson_dye_OBJ.id = "crimson_dye"
    $ crimson_dye_OBJ.name = "Crimson Lion"
    $ crimson_dye_OBJ.items = ["clothing dye","hair dye"]
    $ crimson_dye_OBJ.image = "dye_crimson.png"
    $ crimson_dye_OBJ.cost = 80
    $ crimson_dye_OBJ.description = "> A very rich shade of red."

    if not hasattr(renpy.store,'green_dye_OBJ'): # Green
        $ green_dye_OBJ = store_item_class()
    $ green_dye_OBJ.id = "green_dye"
    $ green_dye_OBJ.name = "Bowtruckle Paint"
    $ green_dye_OBJ.items = ["clothing dye"]
    $ green_dye_OBJ.image = "dye_green.png"
    $ green_dye_OBJ.cost = 60
    $ green_dye_OBJ.description = "> A bright shade of green."

    if not hasattr(renpy.store,'dark_green_dye_OBJ'): # Dark Green
        $ dark_green_dye_OBJ = store_item_class()
    $ dark_green_dye_OBJ.id = "dark_green_dye"
    $ dark_green_dye_OBJ.name = "Serpent Green"
    $ dark_green_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_green_dye_OBJ.image = "dye_dark_green.png"
    $ dark_green_dye_OBJ.cost = 80
    $ dark_green_dye_OBJ.description = "> A darker shade of green."

    if not hasattr(renpy.store,'blue_dye_OBJ'): # Blue
        $ blue_dye_OBJ = store_item_class()
    $ blue_dye_OBJ.id = "blue_dye"
    $ blue_dye_OBJ.name = "Pixie Dye"
    $ blue_dye_OBJ.items = ["clothing dye"]
    $ blue_dye_OBJ.image = "dye_blue.png"
    $ blue_dye_OBJ.cost = 60
    $ blue_dye_OBJ.description = "> A bright shade of blue."

    if not hasattr(renpy.store,'dark_blue_dye_OBJ'): # Dark Blue
        $ dark_blue_dye_OBJ = store_item_class()
    $ dark_blue_dye_OBJ.id = "dark_blue_dye"
    $ dark_blue_dye_OBJ.name = "Raven Blue"
    $ dark_blue_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_blue_dye_OBJ.image = "dye_dark_blue.png"
    $ dark_blue_dye_OBJ.cost = 80
    $ dark_blue_dye_OBJ.description = "> A darker shade of blue."

    if not hasattr(renpy.store,'purple_dye_OBJ'): # Purple
        $ purple_dye_OBJ = store_item_class()
    $ purple_dye_OBJ.id = "purple_dye"
    $ purple_dye_OBJ.name = "Pygmy Puff Purple"
    $ purple_dye_OBJ.items = ["clothing dye","hair dye"]
    $ purple_dye_OBJ.image = "dye_purple.png"
    $ purple_dye_OBJ.cost = 120
    $ purple_dye_OBJ.description = "> A very nice shade of purple."

    if not hasattr(renpy.store,'pink_dye_OBJ'): # Pink
        $ pink_dye_OBJ = store_item_class()
    $ pink_dye_OBJ.id = "pink_dye"
    $ pink_dye_OBJ.name = "Pussy Pink"
    $ pink_dye_OBJ.items = ["clothing dye","hair dye"]
    $ pink_dye_OBJ.image = "dye_pink.png"
    $ pink_dye_OBJ.cost = 200
    $ pink_dye_OBJ.description = "> A color so pink, it makes you want to cover your\n  whole room with it!"

    if not hasattr(renpy.store,'gray_dye_OBJ'): # Gray
        $ gray_dye_OBJ = store_item_class()
    $ gray_dye_OBJ.id = "gray_dye"
    $ gray_dye_OBJ.name = "Ghostly Gray"
    $ gray_dye_OBJ.items = ["clothing dye","hair dye"]
    $ gray_dye_OBJ.image = "dye_gray.png"
    $ gray_dye_OBJ.cost = 200
    $ gray_dye_OBJ.description = "> A very classy shade of gray."

    if not hasattr(renpy.store,'black_dye_OBJ'): # Black
        $ black_dye_OBJ = store_item_class()
    $ black_dye_OBJ.id = "black_dye"
    $ black_dye_OBJ.name = "Seriously Black"
    $ black_dye_OBJ.items = ["clothing dye","hair dye"]
    $ black_dye_OBJ.image = "dye_black.png"
    $ black_dye_OBJ.cost = 400
    $ black_dye_OBJ.description = "> As black as a Testral."

    if not hasattr(renpy.store,'white_dye_OBJ'): # White
        $ white_dye_OBJ = store_item_class()
    $ white_dye_OBJ.id = "white_dye"
    $ white_dye_OBJ.name = "Patroni White"
    $ white_dye_OBJ.items = ["clothing dye"]
    $ white_dye_OBJ.image = "dye_white.png"
    $ white_dye_OBJ.cost = 400
    $ white_dye_OBJ.description = "> As bright and pure as a Patronus!"

    $ cs_dye_list = []
    $ cs_dye_list.append(brown_dye_OBJ)
    $ cs_dye_list.append(yellow_dye_OBJ)
    $ cs_dye_list.append(orange_dye_OBJ)
    $ cs_dye_list.append(red_dye_OBJ)
    $ cs_dye_list.append(crimson_dye_OBJ)
    $ cs_dye_list.append(green_dye_OBJ)
    $ cs_dye_list.append(dark_green_dye_OBJ)
    $ cs_dye_list.append(blue_dye_OBJ)
    $ cs_dye_list.append(dark_blue_dye_OBJ)
    $ cs_dye_list.append(purple_dye_OBJ)
    $ cs_dye_list.append(pink_dye_OBJ)
    $ cs_dye_list.append(gray_dye_OBJ)
    $ cs_dye_list.append(black_dye_OBJ)
    $ cs_dye_list.append(white_dye_OBJ)
    python:
        for i in cs_dye_list:
            i.type = "dye"


    # Clothing Sets
    if not hasattr(renpy.store,'hg_cheer_g_OBJ'):
        $ hg_cheer_g_OBJ = store_item_class()
    $ hg_cheer_g_OBJ.id = "hg_cheer_g"
    $ hg_cheer_g_OBJ.name = "Gryffindor Cheerleader"
    $ hg_cheer_g_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_g_OBJ.cost = 80
    $ hg_cheer_g_OBJ.wait_time = 2
    $ hg_cheer_g_OBJ.image = "hg_cheer_g.png"
    $ hg_cheer_g_OBJ.description = "> A basic Cheerleader attire for Gryffindor's\n  Quidditch team."

    if not hasattr(renpy.store,'hg_cheer_g_sexy_OBJ'): #Not a store item!
        $ hg_cheer_g_sexy_OBJ = store_item_class()
    $ hg_cheer_g_sexy_OBJ.id = "hg_cheer_g_sexy"
    $ hg_cheer_g_sexy_OBJ.name = "Sexy Gryffindor Cheerleader"
    $ hg_cheer_g_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_g_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_g_sexy_OBJ.image = "hg_cheer_g_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_s_OBJ'):
        $ hg_cheer_s_OBJ = store_item_class()
    $ hg_cheer_s_OBJ.id = "hg_cheer_s"
    $ hg_cheer_s_OBJ.name = "Slythrin Cheerleader"
    $ hg_cheer_s_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_s_OBJ.cost = 80
    $ hg_cheer_s_OBJ.wait_time = 2
    $ hg_cheer_s_OBJ.image = "hg_cheer_s.png"
    $ hg_cheer_s_OBJ.description = "> The Slytherin version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_s_sexy_OBJ'):  #Not a store item!
        $ hg_cheer_s_sexy_OBJ = store_item_class()
    $ hg_cheer_s_sexy_OBJ.id = "hg_cheer_s_sexy"
    $ hg_cheer_s_sexy_OBJ.name = "Sexy Slythrin Cheerleader"
    $ hg_cheer_s_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_s_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_s_sexy_OBJ.image = "hg_cheer_s_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_r_OBJ'):
        $ hg_cheer_r_OBJ = store_item_class()
    $ hg_cheer_r_OBJ.id = "hg_cheer_r"
    $ hg_cheer_r_OBJ.name = "Ravenclaw Cheerleader"
    $ hg_cheer_r_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_r_OBJ.cost = 80
    $ hg_cheer_r_OBJ.wait_time = 2
    $ hg_cheer_r_OBJ.image = "hg_cheer_r.png"
    $ hg_cheer_r_OBJ.description = "> The Ravenclaw version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_r_sexy_OBJ'):  #Not a store item!
        $ hg_cheer_r_sexy_OBJ = store_item_class()
    $ hg_cheer_r_sexy_OBJ.id = "hg_cheer_r_sexy"
    $ hg_cheer_r_sexy_OBJ.name = "Sexy Ravenclaw Cheerleader"
    $ hg_cheer_r_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_r_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_r_sexy_OBJ.image = "hg_cheer_r_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_h_OBJ'):
        $ hg_cheer_h_OBJ = store_item_class()
    $ hg_cheer_h_OBJ.id = "hg_cheer_h"
    $ hg_cheer_h_OBJ.name = "Hufflepuff Cheerleader"
    $ hg_cheer_h_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_h_OBJ.cost = 80
    $ hg_cheer_h_OBJ.wait_time = 2
    $ hg_cheer_h_OBJ.image = "hg_cheer_h.png"
    $ hg_cheer_h_OBJ.description = "> The Hufflepuff version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_h_sexy_OBJ'):  #Not a store item!
        $ hg_cheer_h_sexy_OBJ = store_item_class()
    $ hg_cheer_h_sexy_OBJ.id = "hg_cheer_h_sexy"
    $ hg_cheer_h_sexy_OBJ.name = "Sexy Hufflepuff Cheerleader"
    $ hg_cheer_h_sexy_OBJ.items = ["top","bottom","stockings"]
    $ hg_cheer_h_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_h_sexy_OBJ.image = "hg_cheer_h_sexy.png"


    # Lingerie
    if not hasattr(renpy.store,'hg_lingerie_lace_OBJ'):
        $ hg_lingerie_lace_OBJ = store_item_class()
    $ hg_lingerie_lace_OBJ.id = "hg_lingerie_lace"
    $ hg_lingerie_lace_OBJ.name = "Lace Lingerie"
    $ hg_lingerie_lace_OBJ.items = ["bra","panties"]
    $ hg_lingerie_lace_OBJ.cost = 40
    $ hg_lingerie_lace_OBJ.wait_time = 1
    $ hg_lingerie_lace_OBJ.image = "hg_lingerie_lace.png"
    $ hg_lingerie_lace_OBJ.description = "> A lovely lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_silk_OBJ'):
        $ hg_lingerie_silk_OBJ = store_item_class()
    $ hg_lingerie_silk_OBJ.id = "hg_lingerie_silk"
    $ hg_lingerie_silk_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_silk_OBJ.items = ["bra","panties","garter","stockings"]
    $ hg_lingerie_silk_OBJ.cost = 80
    $ hg_lingerie_silk_OBJ.wait_time = 1
    $ hg_lingerie_silk_OBJ.image = "hg_lingerie_silk.png"
    $ hg_lingerie_silk_OBJ.description = "> A smooth and comfortable lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_maid_OBJ'):
        $ hg_lingerie_maid_OBJ = store_item_class()
    $ hg_lingerie_maid_OBJ.id = "hg_lingerie_maid"
    $ hg_lingerie_maid_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_maid_OBJ.items = ["bra","panties","gloves","stockings","hair","hat"]
    $ hg_lingerie_maid_OBJ.cost = 160
    $ hg_lingerie_maid_OBJ.wait_time = 2
    $ hg_lingerie_maid_OBJ.image = "hg_lingerie_maid.png"
    $ hg_lingerie_maid_OBJ.description = "> A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts."

    if not hasattr(renpy.store,'hg_lingerie_latex_OBJ'):
        $ hg_lingerie_latex_OBJ = store_item_class()
    $ hg_lingerie_latex_OBJ.id = "hg_lingerie_latex"
    $ hg_lingerie_latex_OBJ.name = "Latex Lingerie"
    $ hg_lingerie_latex_OBJ.items = ["bra","panties","gloves","stockings"]
    $ hg_lingerie_latex_OBJ.cost = 200
    $ hg_lingerie_latex_OBJ.wait_time = 2
    $ hg_lingerie_latex_OBJ.image = "hg_lingerie_latex.png"
    $ hg_lingerie_latex_OBJ.description = "> A tight and shiny lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_fishnet_OBJ'):
        $ hg_lingerie_fishnet_OBJ = store_item_class()
    $ hg_lingerie_fishnet_OBJ.id = "hg_lingerie_fishnet"
    $ hg_lingerie_fishnet_OBJ.name = "Fishnet Lingerie"
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
    $ hg_nighty_silk_OBJ.items = ["one-piece","panties"]
    $ hg_nighty_silk_OBJ.cost = 80
    $ hg_nighty_silk_OBJ.wait_time = 1
    $ hg_nighty_silk_OBJ.image = "hg_nighty_silk.png"
    $ hg_nighty_silk_OBJ.description = "> A comfortable yet elegant Nightwear set."

    if not hasattr(renpy.store,'hg_nightgown_OBJ'):
        $ hg_nightgown_OBJ = store_item_class()
    $ hg_nightgown_OBJ.id = "hg_nighty_silk"
    $ hg_nightgown_OBJ.name = "Silk Nightgown"
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
    $ hg_bikini_latex_OBJ.items = ["bra","panties"]
    $ hg_bikini_latex_OBJ.cost = 100
    $ hg_bikini_latex_OBJ.wait_time = 1
    $ hg_bikini_latex_OBJ.image = "hg_bikini_latex.png"
    $ hg_bikini_latex_OBJ.description = "> A set for when you want to become one with your\n underwear"

    if not hasattr(renpy.store,'hg_bikini_sling_OBJ'):
        $ hg_bikini_sling_OBJ = store_item_class()
    $ hg_bikini_sling_OBJ.id = "hg_bikini_sling"
    $ hg_bikini_sling_OBJ.name = "Sling Bikini"
    $ hg_bikini_sling_OBJ.items = ["bra","panties"]
    $ hg_bikini_sling_OBJ.cost = 69
    $ hg_bikini_sling_OBJ.wait_time = 1
    $ hg_bikini_sling_OBJ.image = "hg_bikini_sling.png"
    $ hg_bikini_sling_OBJ.description = "> Provides even less coverage than the Latex Bikini"


    # One-pieces
    if not hasattr(renpy.store,'hg_onepiece_sling_OBJ'):
        $ hg_onepiece_sling_OBJ = store_item_class()
    $ hg_onepiece_sling_OBJ.id = "hg_onepiece_sling"
    $ hg_onepiece_sling_OBJ.name = "Sling Monokini"
    $ hg_onepiece_sling_OBJ.items = ["one-piece"]
    $ hg_onepiece_sling_OBJ.cost = 69
    $ hg_onepiece_sling_OBJ.wait_time = 1
    $ hg_onepiece_sling_OBJ.image = "hg_onepiece_sling.png"
    $ hg_onepiece_sling_OBJ.description = "> A Mononoke variant of the Sling Bikini"


    # Accessories
    if not hasattr(renpy.store,'hg_accs_wool_g_OBJ'): # Not a store item!
        $ hg_accs_wool_g_OBJ = store_item_class()
    $ hg_accs_wool_g_OBJ.id = "hg_wool_accs_g"
    $ hg_accs_wool_g_OBJ.name = "Gryffindor Wool Accessories"
    $ hg_accs_wool_g_OBJ.items = ["scarf","gloves","stockings"]
    $ hg_accs_wool_g_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_accs_wool_g_OBJ.image = "hg_accs_wool_g.png"

    # Clothing
    if not hasattr(renpy.store,'hg_muggle_cold_OBJ'): # Not a store item!
        $ hg_muggle_cold_OBJ = store_item_class()
    $ hg_muggle_cold_OBJ.id = "hg_muggle_cold"
    $ hg_muggle_cold_OBJ.name = "Cold Weather Clothing"
    $ hg_muggle_cold_OBJ.items = ["pullover","skirt","pantyhose"]
    $ hg_muggle_cold_OBJ.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_cold_OBJ.image = "hg_muggle_cold.png"

    if not hasattr(renpy.store,'hg_muggle_cold_sexy_OBJ'): # Not a store item!
        $ hg_muggle_cold_sexy_OBJ = store_item_class()
    $ hg_muggle_cold_sexy_OBJ.id = "hg_muggle_cold_sexy"
    $ hg_muggle_cold_sexy_OBJ.name = "Sexy Cold Weather Clothing"
    $ hg_muggle_cold_sexy_OBJ.items = ["pullover","skirt","pantyhose"]
    $ hg_muggle_cold_sexy_OBJ.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_muggle_cold_sexy_OBJ.image = "hg_muggle_cold_sexy.png"

    if not hasattr(renpy.store,'hg_muggle_hot_OBJ'): # Not a store item!
        $ hg_muggle_hot_OBJ = store_item_class()
    $ hg_muggle_hot_OBJ.id = "hg_muggle_hot"
    $ hg_muggle_hot_OBJ.name = "Hot Weather Clothing"
    $ hg_muggle_hot_OBJ.items = ["top","skirt","stockings"]
    $ hg_muggle_hot_OBJ.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_hot_OBJ.image = "hg_muggle_hot.png"

    if not hasattr(renpy.store,'hg_muggle_rainy_OBJ'): # Not a store item!
        $ hg_muggle_rainy_OBJ = store_item_class()
    $ hg_muggle_rainy_OBJ.id = "hg_muggle_rainy"
    $ hg_muggle_rainy_OBJ.name = "Rainy Weather Clothing"
    $ hg_muggle_rainy_OBJ.items = ["sweater","long jeans"]
    $ hg_muggle_rainy_OBJ.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_rainy_OBJ.image = "hg_muggle_rainy.png"

    if not hasattr(renpy.store,'hg_punk_rocker_OBJ'):
        $ hg_punk_rocker_OBJ = store_item_class()
    $ hg_punk_rocker_OBJ.id = "hg_punk_rocker"
    $ hg_punk_rocker_OBJ.name = "Punk Rocker"
    $ hg_punk_rocker_OBJ.items = ["top","bottom","gloves","choker"]
    $ hg_punk_rocker_OBJ.cost = 180
    $ hg_punk_rocker_OBJ.wait_time = 2
    $ hg_punk_rocker_OBJ.image = "hg_punk_rocker.png"
    $ hg_punk_rocker_OBJ.description = ">A punk-rock set of clothes for the more rebellious\n type of witch."

    if not hasattr(renpy.store,'hg_punk_leather_OBJ'):
        $ hg_punk_leather_OBJ = store_item_class()
    $ hg_punk_leather_OBJ.id = "hg_punk_leather"
    $ hg_punk_leather_OBJ.name = "Punk Leather"
    $ hg_punk_leather_OBJ.items = ["top","bottom","bra","stockings"]
    $ hg_punk_leather_OBJ.cost = 300
    $ hg_punk_leather_OBJ.wait_time = 3
    $ hg_punk_leather_OBJ.image = "hg_punk_leather.png"
    $ hg_punk_leather_OBJ.description = ">A punk-leather set for wicked witches!\n The sleeve-length of the Leather-jacket can be changed."

    $ hermione_clothing_sets_list = []
    $ hermione_clothing_sets_list.append(hg_cheer_g_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_g_sexy_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_s_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_s_sexy_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_r_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_r_sexy_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_h_OBJ)
    $ hermione_clothing_sets_list.append(hg_cheer_h_sexy_OBJ) #Unlockable

    $ hermione_clothing_sets_list.append(hg_lingerie_lace_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_silk_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_maid_OBJ)
    $ hermione_clothing_sets_list.append(hg_lingerie_latex_OBJ)

    #$ hermione_clothing_sets_list.append(hg_nighty_silk_OBJ)
    #$ hermione_clothing_sets_list.append(hg_nightgown_OBJ)

    $ hermione_clothing_sets_list.append(hg_bikini_latex_OBJ)
    $ hermione_clothing_sets_list.append(hg_bikini_sling_OBJ)

    #$ hermione_clothing_sets_list.append(hg_onepiece_sling_OBJ)

    $ hermione_clothing_sets_list.append(hg_accs_wool_g_OBJ) #Unlockable

    $ hermione_clothing_sets_list.append(hg_muggle_cold_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_cold_sexy_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_hot_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_rainy_OBJ) #Unlockable
    $ hermione_clothing_sets_list.append(hg_punk_rocker_OBJ)
    $ hermione_clothing_sets_list.append(hg_punk_leather_OBJ)
    python:
        for i in hermione_clothing_sets_list:
            i.type = "set"


    # Astoria
    if not hasattr(renpy.store,'ag_boss_uniform_OBJ'): #Like in Hugo Boss...
        $ ag_boss_uniform_OBJ = store_item_class()
    $ ag_boss_uniform_OBJ.id = "ag_boss_uniform"
    $ ag_boss_uniform_OBJ.name = "Boss Uniform"
    $ ag_boss_uniform_OBJ.cost = 500
    $ ag_boss_uniform_OBJ.items = ["top","bottom","hair","hat"]
    $ ag_boss_uniform_OBJ.wait_time = 3
    $ ag_boss_uniform_OBJ.image = "ag_boss_uniform.png"
    $ ag_boss_uniform_OBJ.description = ">A uniform I designed with an old friend of mine.\n Makes me wonder what happened to Hugo..."

    #Lingerie
    if not hasattr(renpy.store,'ag_lingerie_lace_OBJ'):
        $ ag_lingerie_lace_OBJ = store_item_class()
    $ ag_lingerie_lace_OBJ.id = "ag_lingerie_lace"
    $ ag_lingerie_lace_OBJ.name = "Lace Lingerie"
    $ ag_lingerie_lace_OBJ.cost = 80
    $ ag_lingerie_lace_OBJ.items = ["bra","panties"]
    $ ag_lingerie_lace_OBJ.wait_time = 1
    $ ag_lingerie_lace_OBJ.image = "ag_lingerie_lace.png"
    $ ag_lingerie_lace_OBJ.description = ">A cute lace lingerie set."

    if not hasattr(renpy.store,'ag_lingerie_lewd_OBJ'):
        $ ag_lingerie_lewd_OBJ = store_item_class()
    $ ag_lingerie_lewd_OBJ.id = "ag_lingerie_lewd"
    $ ag_lingerie_lewd_OBJ.name = "Lewd Lingerie"
    $ ag_lingerie_lewd_OBJ.cost = 120
    $ ag_lingerie_lewd_OBJ.items = ["bra","panties"]
    $ ag_lingerie_lewd_OBJ.wait_time = 1
    $ ag_lingerie_lewd_OBJ.image = "ag_lingerie_lewd.png"
    $ ag_lingerie_lewd_OBJ.description ="> A very rewealing lingerie set."

    #One-Piece
    if not hasattr(renpy.store,'ag_nighty_silk_OBJ'):
        $ ag_nighty_silk_OBJ = store_item_class()
    $ ag_nighty_silk_OBJ.id = "ag_nighty_silk"
    $ ag_nighty_silk_OBJ.name = "Silk Nighty"
    $ ag_nighty_silk_OBJ.cost = 140
    $ ag_nighty_silk_OBJ.items = ["nighty","panties","stockings"]
    $ ag_nighty_silk_OBJ.wait_time = 1
    $ ag_nighty_silk_OBJ.image = "ag_nighty_silk.png"
    $ ag_nighty_silk_OBJ.description = ">+2 attack points while pillow-fighting!"

    $ astoria_clothing_sets_list = []
    $ astoria_clothing_sets_list.append(ag_boss_uniform_OBJ)
    $ astoria_clothing_sets_list.append(ag_lingerie_lace_OBJ)
    $ astoria_clothing_sets_list.append(ag_lingerie_lewd_OBJ)
    $ astoria_clothing_sets_list.append(ag_nighty_silk_OBJ)
    python:
        for i in astoria_clothing_sets_list:
            i.type = "set"





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
        quantity = 0 #Amount of items of this type that you posess. Can be used for weasley store and gift items.
        cost = 0
        wait_time = 1
        description = ""

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
            if self.type == "outfit" or self.type == "set":
                return "interface/icons/"+self.type+"/"+self.image
            else:
                return "interface/icons/"+self.image #Images aren't stored in a folder.

        def getType(self):
            return self.type
        def getStoreItems(self):
            return self.items
