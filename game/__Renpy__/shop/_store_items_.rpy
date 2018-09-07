label store_items_init:

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
    $ spew_badge_OBJ.description = ">A badge designed to show one's opposition of elf\n slavery."

    if not hasattr(renpy.store,'I_love_cum_badge_OBJ'):
        $ I_love_cum_badge_OBJ = store_item_class()
    $ I_love_cum_badge_OBJ.id = "I_love_cum_badge"
    $ I_love_cum_badge_OBJ.name = "I <3 C.U.M. Badge"
    $ I_love_cum_badge_OBJ.items = ["badge"]
    $ I_love_cum_badge_OBJ.image = "badge_I_love_cum.png"
    $ I_love_cum_badge_OBJ.cost = 15
    $ I_love_cum_badge_OBJ.description = ">A badge that displays ones affection towards semen."

    #Ears
    if not hasattr(renpy.store,'cat_ears_OBJ'):
        $ cat_ears_OBJ = store_item_class()
    $ cat_ears_OBJ.id = "cat_ears"
    $ cat_ears_OBJ.name = "Cat Ears"
    $ cat_ears_OBJ.items = ["ears","tail"]
    $ cat_ears_OBJ.image = "ears_cat.png"
    $ cat_ears_OBJ.cost = 40
    $ cat_ears_OBJ.description = ">A fluffy set of catlike ears that matches one's\n hair-color!"

    if not hasattr(renpy.store,'elf_ears_OBJ'):
        $ elf_ears_OBJ = store_item_class()
    $ elf_ears_OBJ.id = "elf_ears"
    $ elf_ears_OBJ.name = "Elf Ears"
    $ elf_ears_OBJ.items = ["ears"]
    $ elf_ears_OBJ.image = "ears_elf.png"
    $ elf_ears_OBJ.cost = 20
    $ elf_ears_OBJ.description = ">A pointy set of elven ears."

    #Glasses
    if not hasattr(renpy.store,'reading_glasses_OBJ'):
        $ reading_glasses_OBJ = store_item_class()
    $ reading_glasses_OBJ.id = "reading_glasses"
    $ reading_glasses_OBJ.name = "Reading Glasses"
    $ reading_glasses_OBJ.items = ["glasses"]
    $ reading_glasses_OBJ.image = "glasses_reading.png"
    $ reading_glasses_OBJ.cost = 50
    $ reading_glasses_OBJ.description = ">A lot of wizards are into girls wearing these!"

    if not hasattr(renpy.store,'vintage_glasses_OBJ'):
        $ vintage_glasses_OBJ = store_item_class()
    $ vintage_glasses_OBJ.id = "vintage_glasses"
    $ vintage_glasses_OBJ.name = "Vintage Glasses"
    $ vintage_glasses_OBJ.items = ["glasses"]
    $ vintage_glasses_OBJ.image = "glasses_vintage.png"
    $ vintage_glasses_OBJ.cost = 70
    $ vintage_glasses_OBJ.description = ">Wearing these doesn't automatically make you a nerd!"

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
    $ red_lipstick_OBJ.description = ">They call this one the red rocket!"

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
    $ freckles_makeup_OBJ.description = ">A magical item that makes the wearer's freckles more\n pronounced!"

    if not hasattr(renpy.store,'fake_cum_makeup_OBJ'):
        $ fake_cum_makeup_OBJ = store_item_class()
    $ fake_cum_makeup_OBJ.id = "fake_cum_makeup"
    $ fake_cum_makeup_OBJ.name = "Fake Cum"
    $ fake_cum_makeup_OBJ.type = "makeup"
    $ fake_cum_makeup_OBJ.items = ["fake cum"]
    $ fake_cum_makeup_OBJ.image = "makeup_fake_cum.png"
    $ fake_cum_makeup_OBJ.cost = 20
    $ fake_cum_makeup_OBJ.description = ">When she doen't want to wear your real cum just yet.\n Be patient!"

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
    $ brown_dye_OBJ.description = ">Basic shade of brown. Simple yet elegant!"

    if not hasattr(renpy.store,'yellow_dye_OBJ'): # Yellow
        $ yellow_dye_OBJ = store_item_class()
    $ yellow_dye_OBJ.id = "yellow_dye"
    $ yellow_dye_OBJ.name = "Niffler's Gold"
    $ yellow_dye_OBJ.items = ["clothing dye","hair dye"]
    $ yellow_dye_OBJ.image = "dye_yellow.png"
    $ yellow_dye_OBJ.cost = 40
    $ yellow_dye_OBJ.description = ">A very nice shade of yellow."

    if not hasattr(renpy.store,'orange_dye_OBJ'): # Orange
        $ orange_dye_OBJ = store_item_class()
    $ orange_dye_OBJ.id = "orange_dye"
    $ orange_dye_OBJ.name = "Butter Beer"
    $ orange_dye_OBJ.items = ["clothing dye"]
    $ orange_dye_OBJ.image = "dye_orange.png"
    $ orange_dye_OBJ.cost = 60
    $ orange_dye_OBJ.description = ">A very nice shade of orange."

    if not hasattr(renpy.store,'red_dye_OBJ'): # Red
        $ red_dye_OBJ = store_item_class()
    $ red_dye_OBJ.id = "red_dye"
    $ red_dye_OBJ.name = "Weasel Red"
    $ red_dye_OBJ.items = ["clothing dye","hair dye"]
    $ red_dye_OBJ.image = "dye_red.png"
    $ red_dye_OBJ.cost = 60
    $ red_dye_OBJ.description = ">A very nice shade of red."

    if not hasattr(renpy.store,'crimson_dye_OBJ'): # Crimson
        $ crimson_dye_OBJ = store_item_class()
    $ crimson_dye_OBJ.id = "crimson_dye"
    $ crimson_dye_OBJ.name = "Crimson Lion"
    $ crimson_dye_OBJ.items = ["clothing dye","hair dye"]
    $ crimson_dye_OBJ.image = "dye_crimson.png"
    $ crimson_dye_OBJ.cost = 80
    $ crimson_dye_OBJ.description = ">A very rich shade of red."

    if not hasattr(renpy.store,'green_dye_OBJ'): # Green
        $ green_dye_OBJ = store_item_class()
    $ green_dye_OBJ.id = "green_dye"
    $ green_dye_OBJ.name = "Bowtruckle Paint"
    $ green_dye_OBJ.items = ["clothing dye"]
    $ green_dye_OBJ.image = "dye_green.png"
    $ green_dye_OBJ.cost = 60
    $ green_dye_OBJ.description = ">A bright shade of green."

    if not hasattr(renpy.store,'dark_green_dye_OBJ'): # Dark Green
        $ dark_green_dye_OBJ = store_item_class()
    $ dark_green_dye_OBJ.id = "dark_green_dye"
    $ dark_green_dye_OBJ.name = "Serpent Green"
    $ dark_green_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_green_dye_OBJ.image = "dye_dark_green.png"
    $ dark_green_dye_OBJ.cost = 80
    $ dark_green_dye_OBJ.description = ">A darker shade of green."

    if not hasattr(renpy.store,'blue_dye_OBJ'): # Blue
        $ blue_dye_OBJ = store_item_class()
    $ blue_dye_OBJ.id = "blue_dye"
    $ blue_dye_OBJ.name = "Pixie Dye"
    $ blue_dye_OBJ.items = ["clothing dye"]
    $ blue_dye_OBJ.image = "dye_blue.png"
    $ blue_dye_OBJ.cost = 60
    $ blue_dye_OBJ.description = ">A bright shade of blue."

    if not hasattr(renpy.store,'dark_blue_dye_OBJ'): # Dark Blue
        $ dark_blue_dye_OBJ = store_item_class()
    $ dark_blue_dye_OBJ.id = "dark_blue_dye"
    $ dark_blue_dye_OBJ.name = "Raven Blue"
    $ dark_blue_dye_OBJ.items = ["clothing dye","hair dye"]
    $ dark_blue_dye_OBJ.image = "dye_dark_blue.png"
    $ dark_blue_dye_OBJ.cost = 80
    $ dark_blue_dye_OBJ.description = ">A darker shade of blue."

    if not hasattr(renpy.store,'purple_dye_OBJ'): # Purple
        $ purple_dye_OBJ = store_item_class()
    $ purple_dye_OBJ.id = "purple_dye"
    $ purple_dye_OBJ.name = "Pygmy Puff Purple"
    $ purple_dye_OBJ.items = ["clothing dye","hair dye"]
    $ purple_dye_OBJ.image = "dye_purple.png"
    $ purple_dye_OBJ.cost = 120
    $ purple_dye_OBJ.description = ">A very nice shade of purple."

    if not hasattr(renpy.store,'pink_dye_OBJ'): # Pink
        $ pink_dye_OBJ = store_item_class()
    $ pink_dye_OBJ.id = "pink_dye"
    $ pink_dye_OBJ.name = "Pussy Pink"
    $ pink_dye_OBJ.items = ["clothing dye","hair dye"]
    $ pink_dye_OBJ.image = "dye_pink.png"
    $ pink_dye_OBJ.cost = 200
    $ pink_dye_OBJ.description = ">A color so pink, it makes you want to cover your\n whole room with it!"

    if not hasattr(renpy.store,'gray_dye_OBJ'): # Gray
        $ gray_dye_OBJ = store_item_class()
    $ gray_dye_OBJ.id = "gray_dye"
    $ gray_dye_OBJ.name = "Ghostly Gray"
    $ gray_dye_OBJ.items = ["clothing dye","hair dye"]
    $ gray_dye_OBJ.image = "dye_gray.png"
    $ gray_dye_OBJ.cost = 200
    $ gray_dye_OBJ.description = ">A very classy shade of gray."

    if not hasattr(renpy.store,'black_dye_OBJ'): # Black
        $ black_dye_OBJ = store_item_class()
    $ black_dye_OBJ.id = "black_dye"
    $ black_dye_OBJ.name = "Seriously Black"
    $ black_dye_OBJ.items = ["clothing dye","hair dye"]
    $ black_dye_OBJ.image = "dye_black.png"
    $ black_dye_OBJ.cost = 400
    $ black_dye_OBJ.description = ">As black as a Testral."

    if not hasattr(renpy.store,'white_dye_OBJ'): # White
        $ white_dye_OBJ = store_item_class()
    $ white_dye_OBJ.id = "white_dye"
    $ white_dye_OBJ.name = "Patroni White"
    $ white_dye_OBJ.items = ["clothing dye"]
    $ white_dye_OBJ.image = "dye_white.png"
    $ white_dye_OBJ.cost = 400
    $ white_dye_OBJ.description = ">As bright and pure as a Patronus!"

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
    $ hg_cheer_g_OBJ.description = ">A basic Cheerleader attire for Gryffindor's\n  Quidditch team."

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
    $ hg_cheer_s_OBJ.description = ">The Slytherin version of the Cheerleader attire."

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
    $ hg_cheer_r_OBJ.description = ">The Ravenclaw version of the Cheerleader attire."

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
    $ hg_cheer_h_OBJ.description = ">The Hufflepuff version of the Cheerleader attire."

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
    $ hg_lingerie_lace_OBJ.description = ">A lovely lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_silk_OBJ'):
        $ hg_lingerie_silk_OBJ = store_item_class()
    $ hg_lingerie_silk_OBJ.id = "hg_lingerie_silk"
    $ hg_lingerie_silk_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_silk_OBJ.items = ["bra","panties","garter","stockings"]
    $ hg_lingerie_silk_OBJ.cost = 80
    $ hg_lingerie_silk_OBJ.wait_time = 1
    $ hg_lingerie_silk_OBJ.image = "hg_lingerie_silk.png"
    $ hg_lingerie_silk_OBJ.description = ">A smooth and comfortable lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_maid_OBJ'):
        $ hg_lingerie_maid_OBJ = store_item_class()
    $ hg_lingerie_maid_OBJ.id = "hg_lingerie_maid"
    $ hg_lingerie_maid_OBJ.name = "Maid Lingerie"
    $ hg_lingerie_maid_OBJ.items = ["bra","panties","gloves","stockings","hair","hat"]
    $ hg_lingerie_maid_OBJ.cost = 160
    $ hg_lingerie_maid_OBJ.wait_time = 2
    $ hg_lingerie_maid_OBJ.image = "hg_lingerie_maid.png"
    $ hg_lingerie_maid_OBJ.description = ">A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts."

    if not hasattr(renpy.store,'hg_lingerie_latex_OBJ'):
        $ hg_lingerie_latex_OBJ = store_item_class()
    $ hg_lingerie_latex_OBJ.id = "hg_lingerie_latex"
    $ hg_lingerie_latex_OBJ.name = "Latex Lingerie"
    $ hg_lingerie_latex_OBJ.items = ["bra","panties","gloves","stockings"]
    $ hg_lingerie_latex_OBJ.cost = 200
    $ hg_lingerie_latex_OBJ.wait_time = 2
    $ hg_lingerie_latex_OBJ.image = "hg_lingerie_latex.png"
    $ hg_lingerie_latex_OBJ.description = ">A tight and shiny lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_fishnet_OBJ'):
        $ hg_lingerie_fishnet_OBJ = store_item_class()
    $ hg_lingerie_fishnet_OBJ.id = "hg_lingerie_fishnet"
    $ hg_lingerie_fishnet_OBJ.name = "Fishnet Lingerie"
    $ hg_lingerie_fishnet_OBJ.items = ["top","bra","panties"]
    $ hg_lingerie_fishnet_OBJ.cost = 100
    $ hg_lingerie_fishnet_OBJ.wait_time = 1
    $ hg_lingerie_fishnet_OBJ.image = "hg_lingerie_fishnet.png"
    $ hg_lingerie_fishnet_OBJ.description = ">A very revealing set for fishnet lingerie."


    # Nighties
    if not hasattr(renpy.store,'hg_nighty_silk_OBJ'):
        $ hg_nighty_silk_OBJ = store_item_class()
    $ hg_nighty_silk_OBJ.id = "hg_nighty_silk"
    $ hg_nighty_silk_OBJ.name = "Silk Nighty"
    $ hg_nighty_silk_OBJ.items = ["one-piece","panties"]
    $ hg_nighty_silk_OBJ.cost = 80
    $ hg_nighty_silk_OBJ.wait_time = 1
    $ hg_nighty_silk_OBJ.image = "hg_nighty_silk.png"
    $ hg_nighty_silk_OBJ.description = ">A comfortable yet elegant Nightwear set."

    if not hasattr(renpy.store,'hg_nightgown_OBJ'):
        $ hg_nightgown_OBJ = store_item_class()
    $ hg_nightgown_OBJ.id = "hg_nighty_silk"
    $ hg_nightgown_OBJ.name = "Silk Nightgown"
    $ hg_nightgown_OBJ.items = ["one-piece"]
    $ hg_nightgown_OBJ.cost = 80
    $ hg_nightgown_OBJ.wait_time = 1
    $ hg_nightgown_OBJ.image = "hg_nightgown.png"
    $ hg_nightgown_OBJ.description = ">A more free-flowing set of Nightwear."


    # Bikinis
    if not hasattr(renpy.store,'hg_bikini_latex_OBJ'):
        $ hg_bikini_latex_OBJ = store_item_class()
    $ hg_bikini_latex_OBJ.id = "hg_bikini_latex"
    $ hg_bikini_latex_OBJ.name = "Latex Bikini"
    $ hg_bikini_latex_OBJ.items = ["bra","panties"]
    $ hg_bikini_latex_OBJ.cost = 100
    $ hg_bikini_latex_OBJ.wait_time = 1
    $ hg_bikini_latex_OBJ.image = "hg_bikini_latex.png"
    $ hg_bikini_latex_OBJ.description = ">A set for when you want to become one with your\n underwear"

    if not hasattr(renpy.store,'hg_bikini_sling_OBJ'):
        $ hg_bikini_sling_OBJ = store_item_class()
    $ hg_bikini_sling_OBJ.id = "hg_bikini_sling"
    $ hg_bikini_sling_OBJ.name = "Sling Bikini"
    $ hg_bikini_sling_OBJ.items = ["bra","panties"]
    $ hg_bikini_sling_OBJ.cost = 69
    $ hg_bikini_sling_OBJ.wait_time = 1
    $ hg_bikini_sling_OBJ.image = "hg_bikini_sling.png"
    $ hg_bikini_sling_OBJ.description = ">Provides even less coverage than the Latex Bikini"


    # One-pieces
    if not hasattr(renpy.store,'hg_onepiece_sling_OBJ'):
        $ hg_onepiece_sling_OBJ = store_item_class()
    $ hg_onepiece_sling_OBJ.id = "hg_onepiece_sling"
    $ hg_onepiece_sling_OBJ.name = "Sling Monokini"
    $ hg_onepiece_sling_OBJ.items = ["one-piece"]
    $ hg_onepiece_sling_OBJ.cost = 69
    $ hg_onepiece_sling_OBJ.wait_time = 1
    $ hg_onepiece_sling_OBJ.image = "hg_onepiece_sling.png"
    $ hg_onepiece_sling_OBJ.description = ">A Mononoke variant of the Sling Bikini"

    if not hasattr(renpy.store,'hg_onepiece_sport_swimsuit_OBJ'):
        $ hg_onepiece_sport_swimsuit_OBJ = store_item_class()
    $ hg_onepiece_sport_swimsuit_OBJ.id = "hg_onepiece_sport_swimsuit"
    $ hg_onepiece_sport_swimsuit_OBJ.name = "Sports Swimsuits"
    $ hg_onepiece_sport_swimsuit_OBJ.items = ["one-piece"]
    $ hg_onepiece_sport_swimsuit_OBJ.cost = 69
    $ hg_onepiece_sport_swimsuit_OBJ.wait_time = 1
    $ hg_onepiece_sport_swimsuit_OBJ.image = "hg_onepiece_swimsuit_sport.png"
    $ hg_onepiece_sport_swimsuit_OBJ.description = ">Comes in 4 different variants. \nSwimmies not included!"


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
    $ hermione_clothing_sets_list.append(hg_lingerie_fishnet_OBJ)

    #$ hermione_clothing_sets_list.append(hg_nighty_silk_OBJ)
    #$ hermione_clothing_sets_list.append(hg_nightgown_OBJ)

    $ hermione_clothing_sets_list.append(hg_bikini_latex_OBJ)
    $ hermione_clothing_sets_list.append(hg_bikini_sling_OBJ)

    #$ hermione_clothing_sets_list.append(hg_onepiece_sling_OBJ)
    $ hermione_clothing_sets_list.append(hg_onepiece_sport_swimsuit_OBJ)

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



    #Outfits
    if not hasattr(renpy.store,'hg_maid_OBJ'): #important!
        $ hg_maid_OBJ = hermione_outfit()
    $ hg_maid_OBJ.name = "Maid"
    $ hg_maid_OBJ.cost = 250
    $ hg_maid_OBJ.type = "outfit"
    $ hg_maid_OBJ.items = ["outfit","hair","hat","gloves","garter","stockings"]
    $ hg_maid_OBJ.wait_time = 2
    $ hg_maid_OBJ.image = "hg_maid.png"
    $ hg_maid_OBJ.outfit_layers = ["maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"]
    $ hg_maid_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_maid_OBJ.hair_layer = "B"
    $ hg_maid_OBJ.top_layers = "maid_hat"
    $ hg_maid_OBJ.description = ">A classic Maids Outfit for a classy Witch."

    if not hasattr(renpy.store,'hg_heartDancer_OBJ'):
        $ hg_heartDancer_OBJ = hermione_outfit()
    $ hg_heartDancer_OBJ.name = "Heart Dancer"
    $ hg_heartDancer_OBJ.cost = 80
    $ hg_heartDancer_OBJ.type = "dress"
    $ hg_heartDancer_OBJ.items = ["outfit"]
    $ hg_heartDancer_OBJ.wait_time = 1
    $ hg_heartDancer_OBJ.image = "hg_heart.png"
    $ hg_heartDancer_OBJ.outfit_layers = ["heart_legs.png","heart_top.png","heart_collar.png"]
    $ hg_heartDancer_OBJ.breast_layer = "breasts_normal"
    $ hg_heartDancer_OBJ.description = ">A sexy dancers outfit with heart shaped nipple tassels."

    if not hasattr(renpy.store,'hg_pirate_OBJ'):
        $ hg_pirate_OBJ = hermione_outfit()
    $ hg_pirate_OBJ.name = "Pirate"
    $ hg_pirate_OBJ.cost = 75
    $ hg_pirate_OBJ.type = "outfit"
    $ hg_pirate_OBJ.items = ["outfit"]
    $ hg_pirate_OBJ.wait_time = 1
    $ hg_pirate_OBJ.image = "hg_pirate.png"
    $ hg_pirate_OBJ.outfit_layers = ["pirate_legs.png","pirate_pants.png","pirate_top.png"]
    $ hg_pirate_OBJ.breast_layer = "breasts_nipfix"
    $ hg_pirate_OBJ.description = "> A lightweight Pirates outfit with only room for the\n necessities Comes with two canon ball storage compartments."

    if not hasattr(renpy.store,'hg_powerGirl_OBJ'):
        $ hg_powerGirl_OBJ = hermione_outfit()
    $ hg_powerGirl_OBJ.name = "Power Girl"
    $ hg_powerGirl_OBJ.cost = 350
    $ hg_powerGirl_OBJ.type = "costume"
    $ hg_powerGirl_OBJ.items = ["outfit"]
    $ hg_powerGirl_OBJ.wait_time = 3
    $ hg_powerGirl_OBJ.image = "hg_power.png"
    $ hg_powerGirl_OBJ.outfit_layers = ["power_cape.png","power_top.png","power_cape_top.png","power_gloves.png","power_belt.png"]
    $ hg_powerGirl_OBJ.breast_layer = "breasts_normal"
    $ hg_powerGirl_OBJ.hair_layer = "P"
    $ hg_powerGirl_OBJ.description = ">An outfit for when you feel extra heroic\n \"Sometimes it takes balls to be a woman\"."

    if not hasattr(renpy.store,'hg_msMarvel_OBJ'):
        $ hg_msMarvel_OBJ = hermione_outfit()
    $ hg_msMarvel_OBJ.name = "Mrs Marvel"
    $ hg_msMarvel_OBJ.cost = 250
    $ hg_msMarvel_OBJ.type = "costume"
    $ hg_msMarvel_OBJ.items = ["outfit"]
    $ hg_msMarvel_OBJ.wait_time = 2
    $ hg_msMarvel_OBJ.image = "hg_marvel.png"
    $ hg_msMarvel_OBJ.outfit_layers = ["marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"]
    $ hg_msMarvel_OBJ.breast_layer = "breasts_normal"
    $ hg_msMarvel_OBJ.description = ">For the girl that likes the lightningbolt\n better on the chest than the forehead."

    if not hasattr(renpy.store,'hg_harleyQuinn_OBJ'):
        $ hg_harleyQuinn_OBJ = hermione_outfit()
    $ hg_harleyQuinn_OBJ.name = "Harley Quinn"
    $ hg_harleyQuinn_OBJ.cost = 300
    $ hg_harleyQuinn_OBJ.type = "costume"
    $ hg_harleyQuinn_OBJ.items = ["outfit"]
    $ hg_harleyQuinn_OBJ.wait_time = 3
    $ hg_harleyQuinn_OBJ.image = "hg_harley.png"
    $ hg_harleyQuinn_OBJ.outfit_layers = ["harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"]
    $ hg_harleyQuinn_OBJ.breast_layer = "breasts_normal"
    $ hg_harleyQuinn_OBJ.hair_layer = "H"
    $ hg_harleyQuinn_OBJ.description = ">A outfit for when you're actually nuts\n rather than just crazy for them."

    if not hasattr(renpy.store,'hg_ballDress_OBJ'):
        $ hg_ballDress_OBJ = hermione_outfit()
    $ hg_ballDress_OBJ.name = "Ball Dress"
    $ hg_ballDress_OBJ.cost = 1500
    $ hg_ballDress_OBJ.type = "dress"
    $ hg_ballDress_OBJ.items = ["outfit","hair","neckless","tiara"]
    $ hg_ballDress_OBJ.wait_time = 7
    $ hg_ballDress_OBJ.image = "hg_ball_dress.png"
    $ hg_ballDress_OBJ.outfit_layers = ["ball_dress_skirt.png","ball_dress_top.png"]
    $ hg_ballDress_OBJ.breast_layer = "breasts_nipfix"
    $ hg_ballDress_OBJ.hair_layer = "B"
    $ hg_ballDress_OBJ.top_layers = "tiara"
    $ hg_ballDress_OBJ.description = ">A traditional ball dress complete with a imitation\n ball-queen tiara."

    if not hasattr(renpy.store,'hg_christmas_OBJ'):
        $ hg_christmas_OBJ = hermione_outfit()
    $ hg_christmas_OBJ.name = "Christmas Girl"
    $ hg_christmas_OBJ.cost = 50
    $ hg_christmas_OBJ.type = "outfit"
    $ hg_christmas_OBJ.items = ["outfit"]
    $ hg_christmas_OBJ.wait_time = 2
    $ hg_christmas_OBJ.image = "hg_christmas.png"
    $ hg_christmas_OBJ.outfit_layers = ["christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"]
    $ hg_christmas_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_christmas_OBJ.top_layers = "antlers"
    $ hg_christmas_OBJ.description = ">A christmas themed outfit complete with tightly wrapped\n snowglobes."

    if not hasattr(renpy.store,'hg_laraCroft_OBJ'):
        $ hg_laraCroft_OBJ = hermione_outfit()
    $ hg_laraCroft_OBJ.name = "Lara Croft"
    $ hg_laraCroft_OBJ.cost = 270
    $ hg_laraCroft_OBJ.type = "costume"
    $ hg_laraCroft_OBJ.items = ["outfit","gloves"]
    $ hg_laraCroft_OBJ.wait_time = 2
    $ hg_laraCroft_OBJ.image = "hg_lara.png"
    $ hg_laraCroft_OBJ.outfit_layers = ["lara_pants.png","lara_top.png","lara_gloves.png"]
    $ hg_laraCroft_OBJ.breast_layer = "breasts_normal"
    $ hg_laraCroft_OBJ.description = ">An outfit perfectly suited for exploring deep, dark\n and moist caverns."

    if not hasattr(renpy.store,'hg_tifa_OBJ'):
        $ hg_tifa_OBJ = hermione_outfit()
    $ hg_tifa_OBJ.name = "Tifa"
    $ hg_tifa_OBJ.cost = 220
    $ hg_tifa_OBJ.type = "costume"
    $ hg_tifa_OBJ.items = ["outfit"]
    $ hg_tifa_OBJ.wait_time = 2
    $ hg_tifa_OBJ.image = "hg_tifa.png"
    $ hg_tifa_OBJ.outfit_layers = ["tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"]
    $ hg_tifa_OBJ.breast_layer = "breasts_normal"
    $ hg_tifa_OBJ.hair_layer = "T"
    $ hg_tifa_OBJ.description = ">An outfit for when when your sexual fantasies\n are just getting started."

    if not hasattr(renpy.store,'hg_present_OBJ'):
        $ hg_present_OBJ = hermione_outfit()
    $ hg_present_OBJ.name = "Present"
    $ hg_present_OBJ.cost = 35
    $ hg_present_OBJ.type = "outfit"
    $ hg_present_OBJ.items = ["outfit"]
    $ hg_present_OBJ.wait_time = 1
    $ hg_present_OBJ.image = "hg_present.png"
    $ hg_present_OBJ.outfit_layers = ["present_pant.png","present_top.png"]
    $ hg_present_OBJ.breast_layer = "breasts_nipfix"
    $ hg_present_OBJ.description = ">A tightly wrapped gift, scissors not included."

    if not hasattr(renpy.store,'hg_japan_OBJ'):
        $ hg_japan_OBJ = hermione_outfit()
    $ hg_japan_OBJ.name = "Japanese Schoolgirl"
    $ hg_japan_OBJ.cost = 125
    $ hg_japan_OBJ.type = "outfit"
    $ hg_japan_OBJ.items = ["outfit"]
    $ hg_japan_OBJ.wait_time = 2
    $ hg_japan_OBJ.image = "hg_japan.png"
    $ hg_japan_OBJ.outfit_layers = ["japan_pant.png","japan_top.png"]
    $ hg_japan_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_japan_OBJ.description = ">A schoolgirl outfit traditionally worn in Japan."

    if not hasattr(renpy.store,'hg_witch_OBJ'):
        $ hg_witch_OBJ = hermione_outfit()
    $ hg_witch_OBJ.name = "Witch outfit"
    $ hg_witch_OBJ.cost = 250
    $ hg_witch_OBJ.type = "outfit"
    $ hg_witch_OBJ.items = ["outfit","hat"]
    $ hg_witch_OBJ.wait_time = 3
    $ hg_witch_OBJ.image = "hg_witch.png"
    $ hg_witch_OBJ.outfit_layers = ["witch_stockings.png","witch_top.png","witch_cloak.png"]
    $ hg_witch_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_witch_OBJ.top_layers = "witch_hat"
    $ hg_witch_OBJ.description = ">Release your inner witch with this halloween\n inspired outfit."

    if not hasattr(renpy.store,'hg_bio_OBJ'):
        $ hg_bio_OBJ = hermione_outfit()
    $ hg_bio_OBJ.name = "Bioshock outfit"
    $ hg_bio_OBJ.cost = 400
    $ hg_bio_OBJ.type = "outfit"
    $ hg_bio_OBJ.items = ["outfit","hair","choker"]
    $ hg_bio_OBJ.wait_time = 3
    $ hg_bio_OBJ.image = "hg_bio.png"
    $ hg_bio_OBJ.outfit_layers = ["bio_skirt.png","bio_chocker.png","bio_corset.png","bio_jacket.png"]
    $ hg_bio_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_bio_OBJ.hair_layer = "E"
    $ hg_bio_OBJ.description = ">Flick some coins for this Bioshock inspired outfit."

    if not hasattr(renpy.store,'hg_yenn_OBJ'):
        $ hg_yenn_OBJ = hermione_outfit()
    $ hg_yenn_OBJ.name = "Yennefer's costume"
    $ hg_yenn_OBJ.cost = 500
    $ hg_yenn_OBJ.type = "outfit"
    $ hg_yenn_OBJ.items = ["outfit","scarf","choker","stockings"]
    $ hg_yenn_OBJ.wait_time = 3
    $ hg_yenn_OBJ.image = "hg_yenn.png"
    $ hg_yenn_OBJ.outfit_layers = ["yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"]
    $ hg_yenn_OBJ.breast_layer = "breasts_normal"
    $ hg_yenn_OBJ.description = ">A Witcher inspired outfit to fit even the most\n perverted witch"

    if not hasattr(renpy.store,'hg_egypt_OBJ'):
        $ hg_egypt_OBJ = hermione_outfit()
    $ hg_egypt_OBJ.name = "Egyptian Goddess"
    #$ hg_egypt_OBJ.cost = 200
    $ hg_egypt_OBJ.type = "outfit"
    $ hg_egypt_OBJ.unlockable = True #Reward for card game.
    $ hg_egypt_OBJ.image = "hg_egypt.png"
    $ hg_egypt_OBJ.outfit_layers = ["egyptian_top.png","egyptian_bottom.png","egyptian_shackles.png"]
    $ hg_egypt_OBJ.breast_layer = "breasts_normal"

    $ hermione_outfits_list = []
    $ hermione_outfits_list.append(hg_maid_OBJ)
    $ hermione_outfits_list.append(hg_heartDancer_OBJ)
    $ hermione_outfits_list.append(hg_ballDress_OBJ)
    $ hermione_outfits_list.append(hg_pirate_OBJ)
    $ hermione_outfits_list.append(hg_powerGirl_OBJ)
    $ hermione_outfits_list.append(hg_msMarvel_OBJ)
    $ hermione_outfits_list.append(hg_harleyQuinn_OBJ)
    $ hermione_outfits_list.append(hg_christmas_OBJ)
    $ hermione_outfits_list.append(hg_laraCroft_OBJ)
    $ hermione_outfits_list.append(hg_tifa_OBJ)
    $ hermione_outfits_list.append(hg_present_OBJ)
    $ hermione_outfits_list.append(hg_japan_OBJ)
    $ hermione_outfits_list.append(hg_witch_OBJ)
    $ hermione_outfits_list.append(hg_bio_OBJ)
    $ hermione_outfits_list.append(hg_yenn_OBJ)
    $ hermione_outfits_list.append(hg_egypt_OBJ)



    # Astoria
    if not hasattr(renpy.store,'ag_ball_dress_OBJ'):
        $ ag_ball_dress_OBJ = hermione_outfit()
    $ ag_ball_dress_OBJ.name = "Ball Dress"
    $ ag_ball_dress_OBJ.cost = 300
    $ ag_ball_dress_OBJ.type = "dress"
    $ ag_ball_dress_OBJ.items = ["outfit"]
    $ ag_ball_dress_OBJ.wait_time = 4
    $ ag_ball_dress_OBJ.image = "ag_ball_dress.png"
    $ ag_ball_dress_OBJ.outfit_layers = ["ball_dress.png"]
    $ ag_ball_dress_OBJ.description = ">A cute dress for your favourite princess!"

    if not hasattr(renpy.store,'ag_lazy_OBJ'):
        $ ag_lazy_OBJ = hermione_outfit()
    $ ag_lazy_OBJ.name = "Lazy Town Outfit"
    $ ag_lazy_OBJ.cost = 120
    $ ag_lazy_OBJ.type = "costume"
    $ ag_lazy_OBJ.items = ["outfit","hair","bracelet"]
    $ ag_lazy_OBJ.wait_time = 1
    $ ag_lazy_OBJ.image = "ag_lazy.png"
    $ ag_lazy_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress.png","lazy_bracelet.png"]
    $ ag_lazy_OBJ.hair_layer = "L"
    $ ag_lazy_OBJ.description = ">Nobody is lazy at Hogwarts!"

    if not hasattr(renpy.store,'ag_lazy_short_OBJ'): #Not a store item!
        $ ag_lazy_short_OBJ = hermione_outfit()
    $ ag_lazy_short_OBJ.name = "Short Lazy Town Outfit"
    $ ag_lazy_short_OBJ.unlockable = True
    #$ ag_lazy_short_OBJ.cost = 120
    $ ag_lazy_short_OBJ.type = "costume"
    $ ag_lazy_short_OBJ.items = ["outfit","hair","bracelet"]
    $ ag_lazy_short_OBJ.wait_time = 1
    $ ag_lazy_short_OBJ.image = "ag_lazy_short.png"
    $ ag_lazy_short_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress_short.png","lazy_bracelet.png"]
    $ ag_lazy_short_OBJ.hair_layer = "L"
    $ ag_lazy_short_OBJ.description = ">Nobody is lazy at Hogwarts!"

    $ astoria_outfits_list = []
    $ astoria_outfits_list.append(ag_ball_dress_OBJ)
    $ astoria_outfits_list.append(ag_lazy_OBJ)
    $ astoria_outfits_list.append(ag_lazy_short_OBJ)


    if not hasattr(renpy.store,'astoria_outfit_GLBL'):
        $ hermoine_outfit_GLBL = None
        $ astoria_outfit_GLBL = None
        $ susan_outfit_GLBL = None
        $ cho_outfit_GLBL = None
        $ luna_outfit_GLBL = None








    # outfit unlocks/purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'unlocked_clothing_list'):
        $ unlocked_clothing_list = []

    # Setup for 1.5
    # Since we probably have to change the outfits, all purchased outfits will get an .unlocked = True variable,
    # And those outfits will get added to the "unlocked_clothing_list",
    # with which we can unlock all outfits again in the next update if needed, so people don't have to buy and wait for outfits againself.

    python:

        #Outfits
        for i in hermione_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)

        #Sets
        for i in hermione_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)



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


    class outfit_list(list):
        list = []

    class hermione_outfit(object):
        name = ""
        unlockable = False
        unlocked = False
        cost = 0
        type = "outfit"
        items = ["outfit"]
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        image = ""
        description = ""


        def getMenuText(self):
            return "-"+self.name+"-"
        def getOutfitLayers(self):
            return self.outfit_layers
        def getHairLayers(self):
            return self.hair_layer
        def getTopLayers(self):
            return self.top_layers
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]

        def getStoreName(self):
            return self.name
        def getImage(self):
            return self.image
        def getStoreImage(self):
            return "interface/icons/outfit/"+self.image
        def getStoreCost(self):
            return "Cost: "+str(self.cost)+" gold"
        def getStoreWaitTime(self):
            return "Wait Time: "+str(self.wait_time)+" days."
        def getStoreDescription(self):
            return self.description

        def getType(self):
            return self.type
        def getStoreItems(self):
            return self.items
