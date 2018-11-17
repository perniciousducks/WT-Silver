label store_items_init:

    #Single Clothing Items
    $ cs_clothing_list = []

    #Badges
    if not hasattr(renpy.store,'spew_badge_ITEM'):
        $ spew_badge_ITEM = store_item_class()
    $ spew_badge_ITEM.id = "spew_badge"
    $ spew_badge_ITEM.name = "S.P.E.W. Badge"
    $ spew_badge_ITEM.items = ["badge"]
    $ spew_badge_ITEM.image = "badge_spew.png"
    $ spew_badge_ITEM.cost = 5
    $ spew_badge_ITEM.description = ">A badge designed to show one's opposition of elf\n slavery."

    if not hasattr(renpy.store,'I_love_cum_badge_ITEM'):
        $ I_love_cum_badge_ITEM = store_item_class()
    $ I_love_cum_badge_ITEM.id = "I_love_cum_badge"
    $ I_love_cum_badge_ITEM.name = "I <3 C.U.M. Badge"
    $ I_love_cum_badge_ITEM.items = ["badge"]
    $ I_love_cum_badge_ITEM.image = "badge_I_love_cum.png"
    $ I_love_cum_badge_ITEM.cost = 15
    $ I_love_cum_badge_ITEM.description = ">A badge that displays ones affection towards semen."

    #Ears
    if not hasattr(renpy.store,'cat_ears_ITEM'):
        $ cat_ears_ITEM = store_item_class()
    $ cat_ears_ITEM.id = "cat_ears"
    $ cat_ears_ITEM.name = "Cat Ears"
    $ cat_ears_ITEM.items = ["ears","tail"]
    $ cat_ears_ITEM.image = "ears_cat.png"
    $ cat_ears_ITEM.cost = 40
    $ cat_ears_ITEM.description = ">A fluffy set of catlike ears that matches one's\n hair-color!"

    if not hasattr(renpy.store,'elf_ears_ITEM'):
        $ elf_ears_ITEM = store_item_class()
    $ elf_ears_ITEM.id = "elf_ears"
    $ elf_ears_ITEM.name = "Elf Ears"
    $ elf_ears_ITEM.items = ["ears"]
    $ elf_ears_ITEM.image = "ears_elf.png"
    $ elf_ears_ITEM.cost = 20
    $ elf_ears_ITEM.description = ">A pointy set of elven ears."

    #Glasses
    if not hasattr(renpy.store,'reading_glasses_ITEM'):
        $ reading_glasses_ITEM = store_item_class()
    $ reading_glasses_ITEM.id = "reading_glasses"
    $ reading_glasses_ITEM.name = "Reading Glasses"
    $ reading_glasses_ITEM.items = ["glasses"]
    $ reading_glasses_ITEM.image = "glasses_reading.png"
    $ reading_glasses_ITEM.cost = 50
    $ reading_glasses_ITEM.description = ">A lot of wizards are into girls wearing these!"

    if not hasattr(renpy.store,'vintage_glasses_ITEM'):
        $ vintage_glasses_ITEM = store_item_class()
    $ vintage_glasses_ITEM.id = "vintage_glasses"
    $ vintage_glasses_ITEM.name = "Vintage Glasses"
    $ vintage_glasses_ITEM.items = ["glasses"]
    $ vintage_glasses_ITEM.image = "glasses_vintage.png"
    $ vintage_glasses_ITEM.cost = 70
    $ vintage_glasses_ITEM.description = ">Wearing these doesn't automatically make you a nerd!"

    $ cs_accessories_list = []
    $ cs_accessories_list.append(spew_badge_ITEM)
    $ cs_accessories_list.append(I_love_cum_badge_ITEM)
    $ cs_accessories_list.append(cat_ears_ITEM)
    $ cs_accessories_list.append(elf_ears_ITEM)
    $ cs_accessories_list.append(reading_glasses_ITEM)
    $ cs_accessories_list.append(vintage_glasses_ITEM)
    python:
        for i in cs_accessories_list:
            i.type = "accessory"



    #Makeup
    if not hasattr(renpy.store,'lipstick_red_ITEM'):
        $ lipstick_red_ITEM = store_item_class()
    $ lipstick_red_ITEM.id = "lipstick_red"
    $ lipstick_red_ITEM.name = "Red Lipstick"
    $ lipstick_red_ITEM.type = "makeup"
    $ lipstick_red_ITEM.items = ["lipstick"]
    $ lipstick_red_ITEM.image = "lipstick_red.png"
    $ lipstick_red_ITEM.cost = 100
    $ lipstick_red_ITEM.description = ">They call this one the red rocket!"

    if not hasattr(renpy.store,'lipstick_pink_ITEM'):
        $ lipstick_pink_ITEM = store_item_class()
    $ lipstick_pink_ITEM.id = "lipstick_pink"
    $ lipstick_pink_ITEM.name = "Pink Lipstick"
    $ lipstick_pink_ITEM.type = "makeup"
    $ lipstick_pink_ITEM.items = ["lipstick"]
    $ lipstick_pink_ITEM.unlockable = True #Unlocked from potion event.
    $ lipstick_pink_ITEM.image = "lipstick_pink.png"

    if not hasattr(renpy.store,'freckles_makeup_ITEM'):
        $ freckles_makeup_ITEM = store_item_class()
    $ freckles_makeup_ITEM.id = "freckles_makeup"
    $ freckles_makeup_ITEM.name = "Freckles"
    $ freckles_makeup_ITEM.type = "makeup"
    $ freckles_makeup_ITEM.items = ["freckles"]
    $ freckles_makeup_ITEM.image = "makeup_freckles.png"
    $ freckles_makeup_ITEM.cost = 20
    $ freckles_makeup_ITEM.description = ">A magical item that makes the wearer's freckles more\n pronounced!"

    if not hasattr(renpy.store,'fake_cum_makeup_ITEM'):
        $ fake_cum_makeup_ITEM = store_item_class()
    $ fake_cum_makeup_ITEM.id = "fake_cum_makeup"
    $ fake_cum_makeup_ITEM.name = "Fake Cum"
    $ fake_cum_makeup_ITEM.type = "makeup"
    $ fake_cum_makeup_ITEM.items = ["fake cum"]
    $ fake_cum_makeup_ITEM.image = "makeup_fake_cum.png"
    $ fake_cum_makeup_ITEM.cost = 20
    $ fake_cum_makeup_ITEM.description = ">When she doen't want to wear your real cum just yet.\n Be patient!"

    $ cs_miscellaneous_list = []
    $ cs_miscellaneous_list.append(lipstick_red_ITEM)
    $ cs_miscellaneous_list.append(lipstick_pink_ITEM)
    $ cs_miscellaneous_list.append(freckles_makeup_ITEM)
    $ cs_miscellaneous_list.append(fake_cum_makeup_ITEM)


    # Dyes
    if not hasattr(renpy.store,'brown_dye_ITEM'): # Brown
        $ brown_dye_ITEM = store_item_class()
    $ brown_dye_ITEM.id = "brown_dye"
    $ brown_dye_ITEM.name = "Mud-Blood Brown"
    $ brown_dye_ITEM.items = ["clothing dye","hair dye"]
    $ brown_dye_ITEM.image = "dye_brown.png"
    $ brown_dye_ITEM.cost = 20
    $ brown_dye_ITEM.description = ">Basic shade of brown. Simple yet elegant!"

    if not hasattr(renpy.store,'yellow_dye_ITEM'): # Yellow
        $ yellow_dye_ITEM = store_item_class()
    $ yellow_dye_ITEM.id = "yellow_dye"
    $ yellow_dye_ITEM.name = "Niffler's Gold"
    $ yellow_dye_ITEM.items = ["clothing dye","hair dye"]
    $ yellow_dye_ITEM.image = "dye_yellow.png"
    $ yellow_dye_ITEM.cost = 40
    $ yellow_dye_ITEM.description = ">A very nice shade of yellow."

    if not hasattr(renpy.store,'orange_dye_ITEM'): # Orange
        $ orange_dye_ITEM = store_item_class()
    $ orange_dye_ITEM.id = "orange_dye"
    $ orange_dye_ITEM.name = "Butter Beer"
    $ orange_dye_ITEM.items = ["clothing dye"]
    $ orange_dye_ITEM.image = "dye_orange.png"
    $ orange_dye_ITEM.cost = 60
    $ orange_dye_ITEM.description = ">A very nice shade of orange."

    if not hasattr(renpy.store,'red_dye_ITEM'): # Red
        $ red_dye_ITEM = store_item_class()
    $ red_dye_ITEM.id = "red_dye"
    $ red_dye_ITEM.name = "Weasel Red"
    $ red_dye_ITEM.items = ["clothing dye","hair dye"]
    $ red_dye_ITEM.image = "dye_red.png"
    $ red_dye_ITEM.cost = 60
    $ red_dye_ITEM.description = ">A very nice shade of red."

    if not hasattr(renpy.store,'crimson_dye_ITEM'): # Crimson
        $ crimson_dye_ITEM = store_item_class()
    $ crimson_dye_ITEM.id = "crimson_dye"
    $ crimson_dye_ITEM.name = "Crimson Lion"
    $ crimson_dye_ITEM.items = ["clothing dye","hair dye"]
    $ crimson_dye_ITEM.image = "dye_crimson.png"
    $ crimson_dye_ITEM.cost = 80
    $ crimson_dye_ITEM.description = ">A very rich shade of red."

    if not hasattr(renpy.store,'green_dye_ITEM'): # Green
        $ green_dye_ITEM = store_item_class()
    $ green_dye_ITEM.id = "green_dye"
    $ green_dye_ITEM.name = "Bowtruckle Paint"
    $ green_dye_ITEM.items = ["clothing dye"]
    $ green_dye_ITEM.image = "dye_green.png"
    $ green_dye_ITEM.cost = 60
    $ green_dye_ITEM.description = ">A bright shade of green."

    if not hasattr(renpy.store,'dark_green_dye_ITEM'): # Dark Green
        $ dark_green_dye_ITEM = store_item_class()
    $ dark_green_dye_ITEM.id = "dark_green_dye"
    $ dark_green_dye_ITEM.name = "Serpent Green"
    $ dark_green_dye_ITEM.items = ["clothing dye","hair dye"]
    $ dark_green_dye_ITEM.image = "dye_dark_green.png"
    $ dark_green_dye_ITEM.cost = 80
    $ dark_green_dye_ITEM.description = ">A darker shade of green."

    if not hasattr(renpy.store,'blue_dye_ITEM'): # Blue
        $ blue_dye_ITEM = store_item_class()
    $ blue_dye_ITEM.id = "blue_dye"
    $ blue_dye_ITEM.name = "Pixie Dye"
    $ blue_dye_ITEM.items = ["clothing dye"]
    $ blue_dye_ITEM.image = "dye_blue.png"
    $ blue_dye_ITEM.cost = 60
    $ blue_dye_ITEM.description = ">A bright shade of blue."

    if not hasattr(renpy.store,'dark_blue_dye_ITEM'): # Dark Blue
        $ dark_blue_dye_ITEM = store_item_class()
    $ dark_blue_dye_ITEM.id = "dark_blue_dye"
    $ dark_blue_dye_ITEM.name = "Raven Blue"
    $ dark_blue_dye_ITEM.items = ["clothing dye","hair dye"]
    $ dark_blue_dye_ITEM.image = "dye_dark_blue.png"
    $ dark_blue_dye_ITEM.cost = 80
    $ dark_blue_dye_ITEM.description = ">A darker shade of blue."

    if not hasattr(renpy.store,'purple_dye_ITEM'): # Purple
        $ purple_dye_ITEM = store_item_class()
    $ purple_dye_ITEM.id = "purple_dye"
    $ purple_dye_ITEM.name = "Pygmy Puff Purple"
    $ purple_dye_ITEM.items = ["clothing dye","hair dye"]
    $ purple_dye_ITEM.image = "dye_purple.png"
    $ purple_dye_ITEM.cost = 120
    $ purple_dye_ITEM.description = ">A very nice shade of purple."

    if not hasattr(renpy.store,'pink_dye_ITEM'): # Pink
        $ pink_dye_ITEM = store_item_class()
    $ pink_dye_ITEM.id = "pink_dye"
    $ pink_dye_ITEM.name = "Pussy Pink"
    $ pink_dye_ITEM.items = ["clothing dye","hair dye"]
    $ pink_dye_ITEM.image = "dye_pink.png"
    $ pink_dye_ITEM.cost = 200
    $ pink_dye_ITEM.description = ">A color so pink, it makes you want to cover your\n whole room with it!"

    if not hasattr(renpy.store,'gray_dye_ITEM'): # Gray
        $ gray_dye_ITEM = store_item_class()
    $ gray_dye_ITEM.id = "gray_dye"
    $ gray_dye_ITEM.name = "Ghostly Gray"
    $ gray_dye_ITEM.items = ["clothing dye","hair dye"]
    $ gray_dye_ITEM.image = "dye_gray.png"
    $ gray_dye_ITEM.cost = 200
    $ gray_dye_ITEM.description = ">A very classy shade of gray."

    if not hasattr(renpy.store,'black_dye_ITEM'): # Black
        $ black_dye_ITEM = store_item_class()
    $ black_dye_ITEM.id = "black_dye"
    $ black_dye_ITEM.name = "Seriously Black"
    $ black_dye_ITEM.items = ["clothing dye","hair dye"]
    $ black_dye_ITEM.image = "dye_black.png"
    $ black_dye_ITEM.cost = 400
    $ black_dye_ITEM.description = ">As black as a Testral."

    if not hasattr(renpy.store,'white_dye_ITEM'): # White
        $ white_dye_ITEM = store_item_class()
    $ white_dye_ITEM.id = "white_dye"
    $ white_dye_ITEM.name = "Patroni White"
    $ white_dye_ITEM.items = ["clothing dye"]
    $ white_dye_ITEM.image = "dye_white.png"
    $ white_dye_ITEM.cost = 400
    $ white_dye_ITEM.description = ">As bright and pure as a Patronus!"

    $ cs_dye_list = []
    $ cs_dye_list.append(brown_dye_ITEM)
    $ cs_dye_list.append(yellow_dye_ITEM)
    $ cs_dye_list.append(orange_dye_ITEM)
    $ cs_dye_list.append(red_dye_ITEM)
    $ cs_dye_list.append(crimson_dye_ITEM)
    $ cs_dye_list.append(green_dye_ITEM)
    $ cs_dye_list.append(dark_green_dye_ITEM)
    $ cs_dye_list.append(blue_dye_ITEM)
    $ cs_dye_list.append(dark_blue_dye_ITEM)
    $ cs_dye_list.append(purple_dye_ITEM)
    $ cs_dye_list.append(pink_dye_ITEM)
    $ cs_dye_list.append(gray_dye_ITEM)
    $ cs_dye_list.append(black_dye_ITEM)
    $ cs_dye_list.append(white_dye_ITEM)
    python:
        for i in cs_dye_list:
            i.type = "dye"


    # Clothing Sets
    if not hasattr(renpy.store,'hg_cheer_g_ITEM'):
        $ hg_cheer_g_ITEM = store_item_class()
    $ hg_cheer_g_ITEM.id = "hg_cheer_g"
    $ hg_cheer_g_ITEM.name = "Gryffindor Cheerleader"
    $ hg_cheer_g_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_g_ITEM.cost = 80
    $ hg_cheer_g_ITEM.wait_time = 2
    $ hg_cheer_g_ITEM.image = "hg_cheer_g.png"
    $ hg_cheer_g_ITEM.description = ">A basic Cheerleader attire for Gryffindor's\n  Quidditch team."

    if not hasattr(renpy.store,'hg_cheer_g_sexy_ITEM'): #Not a store item!
        $ hg_cheer_g_sexy_ITEM = store_item_class()
    $ hg_cheer_g_sexy_ITEM.id = "hg_cheer_g_sexy"
    $ hg_cheer_g_sexy_ITEM.name = "Sexy Gryffindor Cheerleader"
    $ hg_cheer_g_sexy_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_g_sexy_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_g_sexy_ITEM.image = "hg_cheer_g_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_s_ITEM'):
        $ hg_cheer_s_ITEM = store_item_class()
    $ hg_cheer_s_ITEM.id = "hg_cheer_s"
    $ hg_cheer_s_ITEM.name = "Slythrin Cheerleader"
    $ hg_cheer_s_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_s_ITEM.cost = 80
    $ hg_cheer_s_ITEM.wait_time = 2
    $ hg_cheer_s_ITEM.image = "hg_cheer_s.png"
    $ hg_cheer_s_ITEM.description = ">The Slytherin version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_s_sexy_ITEM'):  #Not a store item!
        $ hg_cheer_s_sexy_ITEM = store_item_class()
    $ hg_cheer_s_sexy_ITEM.id = "hg_cheer_s_sexy"
    $ hg_cheer_s_sexy_ITEM.name = "Sexy Slythrin Cheerleader"
    $ hg_cheer_s_sexy_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_s_sexy_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_s_sexy_ITEM.image = "hg_cheer_s_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_r_ITEM'):
        $ hg_cheer_r_ITEM = store_item_class()
    $ hg_cheer_r_ITEM.id = "hg_cheer_r"
    $ hg_cheer_r_ITEM.name = "Ravenclaw Cheerleader"
    $ hg_cheer_r_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_r_ITEM.cost = 80
    $ hg_cheer_r_ITEM.wait_time = 2
    $ hg_cheer_r_ITEM.image = "hg_cheer_r.png"
    $ hg_cheer_r_ITEM.description = ">The Ravenclaw version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_r_sexy_ITEM'):  #Not a store item!
        $ hg_cheer_r_sexy_ITEM = store_item_class()
    $ hg_cheer_r_sexy_ITEM.id = "hg_cheer_r_sexy"
    $ hg_cheer_r_sexy_ITEM.name = "Sexy Ravenclaw Cheerleader"
    $ hg_cheer_r_sexy_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_r_sexy_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_r_sexy_ITEM.image = "hg_cheer_r_sexy.png"

    if not hasattr(renpy.store,'hg_cheer_h_ITEM'):
        $ hg_cheer_h_ITEM = store_item_class()
    $ hg_cheer_h_ITEM.id = "hg_cheer_h"
    $ hg_cheer_h_ITEM.name = "Hufflepuff Cheerleader"
    $ hg_cheer_h_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_h_ITEM.cost = 80
    $ hg_cheer_h_ITEM.wait_time = 2
    $ hg_cheer_h_ITEM.image = "hg_cheer_h.png"
    $ hg_cheer_h_ITEM.description = ">The Hufflepuff version of the Cheerleader attire."

    if not hasattr(renpy.store,'hg_cheer_h_sexy_ITEM'):  #Not a store item!
        $ hg_cheer_h_sexy_ITEM = store_item_class()
    $ hg_cheer_h_sexy_ITEM.id = "hg_cheer_h_sexy"
    $ hg_cheer_h_sexy_ITEM.name = "Sexy Hufflepuff Cheerleader"
    $ hg_cheer_h_sexy_ITEM.items = ["top","bottom","stockings"]
    $ hg_cheer_h_sexy_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_cheer_h_sexy_ITEM.image = "hg_cheer_h_sexy.png"


    # Lingerie
    if not hasattr(renpy.store,'hg_lingerie_lace_ITEM'):
        $ hg_lingerie_lace_ITEM = store_item_class()
    $ hg_lingerie_lace_ITEM.id = "hg_lingerie_lace"
    $ hg_lingerie_lace_ITEM.name = "Lace Lingerie"
    $ hg_lingerie_lace_ITEM.items = ["bra","panties"]
    $ hg_lingerie_lace_ITEM.cost = 40
    $ hg_lingerie_lace_ITEM.wait_time = 1
    $ hg_lingerie_lace_ITEM.image = "hg_lingerie_lace.png"
    $ hg_lingerie_lace_ITEM.description = ">A lovely lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_silk_ITEM'):
        $ hg_lingerie_silk_ITEM = store_item_class()
    $ hg_lingerie_silk_ITEM.id = "hg_lingerie_silk"
    $ hg_lingerie_silk_ITEM.name = "Silk Lingerie"
    $ hg_lingerie_silk_ITEM.items = ["bra","panties","garter","stockings"]
    $ hg_lingerie_silk_ITEM.cost = 80
    $ hg_lingerie_silk_ITEM.wait_time = 1
    $ hg_lingerie_silk_ITEM.image = "hg_lingerie_silk.png"
    $ hg_lingerie_silk_ITEM.description = ">A smooth and comfortable silk bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_maid_ITEM'):
        $ hg_lingerie_maid_ITEM = store_item_class()
    $ hg_lingerie_maid_ITEM.id = "hg_lingerie_maid"
    $ hg_lingerie_maid_ITEM.name = "Maid Lingerie"
    $ hg_lingerie_maid_ITEM.items = ["bra","panties","gloves","stockings","hair","hat"]
    $ hg_lingerie_maid_ITEM.cost = 160
    $ hg_lingerie_maid_ITEM.wait_time = 2
    $ hg_lingerie_maid_ITEM.image = "hg_lingerie_maid.png"
    $ hg_lingerie_maid_ITEM.description = ">A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts."

    if not hasattr(renpy.store,'hg_lingerie_latex_ITEM'):
        $ hg_lingerie_latex_ITEM = store_item_class()
    $ hg_lingerie_latex_ITEM.id = "hg_lingerie_latex"
    $ hg_lingerie_latex_ITEM.name = "Latex Lingerie"
    $ hg_lingerie_latex_ITEM.items = ["bra","panties","gloves","stockings"]
    $ hg_lingerie_latex_ITEM.cost = 200
    $ hg_lingerie_latex_ITEM.wait_time = 2
    $ hg_lingerie_latex_ITEM.image = "hg_lingerie_latex.png"
    $ hg_lingerie_latex_ITEM.description = ">A tight and shiny lace bra and panty set."

    if not hasattr(renpy.store,'hg_lingerie_fishnet_ITEM'):
        $ hg_lingerie_fishnet_ITEM = store_item_class()
    $ hg_lingerie_fishnet_ITEM.id = "hg_lingerie_fishnet"
    $ hg_lingerie_fishnet_ITEM.name = "Fishnet Lingerie"
    $ hg_lingerie_fishnet_ITEM.items = ["top","bra","panties"]
    $ hg_lingerie_fishnet_ITEM.cost = 100
    $ hg_lingerie_fishnet_ITEM.wait_time = 1
    $ hg_lingerie_fishnet_ITEM.image = "hg_lingerie_fishnet.png"
    $ hg_lingerie_fishnet_ITEM.description = ">A very revealing set for fishnet lingerie."


    # Nighties
    if not hasattr(renpy.store,'hg_nighty_silk_ITEM'):
        $ hg_nighty_silk_ITEM = store_item_class()
    $ hg_nighty_silk_ITEM.id = "hg_nighty_silk"
    $ hg_nighty_silk_ITEM.name = "Silk Nighty"
    $ hg_nighty_silk_ITEM.items = ["one-piece","panties"]
    $ hg_nighty_silk_ITEM.cost = 80
    $ hg_nighty_silk_ITEM.wait_time = 1
    $ hg_nighty_silk_ITEM.image = "hg_nighty_silk.png"
    $ hg_nighty_silk_ITEM.description = ">A comfortable yet elegant Nightwear set."

    if not hasattr(renpy.store,'hg_nightgown_ITEM'):
        $ hg_nightgown_ITEM = store_item_class()
    $ hg_nightgown_ITEM.id = "hg_nighty_silk"
    $ hg_nightgown_ITEM.name = "Silk Nightgown"
    $ hg_nightgown_ITEM.items = ["one-piece"]
    $ hg_nightgown_ITEM.cost = 80
    $ hg_nightgown_ITEM.wait_time = 1
    $ hg_nightgown_ITEM.image = "hg_nightgown.png"
    $ hg_nightgown_ITEM.description = ">A more free-flowing set of Nightwear."


    # Bikinis
    if not hasattr(renpy.store,'hg_bikini_latex_ITEM'):
        $ hg_bikini_latex_ITEM = store_item_class()
    $ hg_bikini_latex_ITEM.id = "hg_bikini_latex"
    $ hg_bikini_latex_ITEM.name = "Latex Bikini"
    $ hg_bikini_latex_ITEM.items = ["bra","panties"]
    $ hg_bikini_latex_ITEM.cost = 100
    $ hg_bikini_latex_ITEM.wait_time = 1
    $ hg_bikini_latex_ITEM.image = "hg_bikini_latex.png"
    $ hg_bikini_latex_ITEM.description = ">A set for when you want to become one with your\n underwear"

    if not hasattr(renpy.store,'hg_bikini_sling_ITEM'):
        $ hg_bikini_sling_ITEM = store_item_class()
    $ hg_bikini_sling_ITEM.id = "hg_bikini_sling"
    $ hg_bikini_sling_ITEM.name = "Sling Bikini"
    $ hg_bikini_sling_ITEM.items = ["bra","panties"]
    $ hg_bikini_sling_ITEM.cost = 69
    $ hg_bikini_sling_ITEM.wait_time = 1
    $ hg_bikini_sling_ITEM.image = "hg_bikini_sling.png"
    $ hg_bikini_sling_ITEM.description = ">Provides even less coverage than the Latex Bikini"


    # One-pieces
    if not hasattr(renpy.store,'hg_onepiece_sling_ITEM'):
        $ hg_onepiece_sling_ITEM = store_item_class()
    $ hg_onepiece_sling_ITEM.id = "hg_onepiece_sling"
    $ hg_onepiece_sling_ITEM.name = "Sling Monokini"
    $ hg_onepiece_sling_ITEM.items = ["one-piece"]
    $ hg_onepiece_sling_ITEM.cost = 69
    $ hg_onepiece_sling_ITEM.wait_time = 1
    $ hg_onepiece_sling_ITEM.image = "hg_onepiece_sling.png"
    $ hg_onepiece_sling_ITEM.description = ">A Mononoke variant of the Sling Bikini"

    if not hasattr(renpy.store,'hg_onepiece_sport_swimsuit_ITEM'):
        $ hg_onepiece_sport_swimsuit_ITEM = store_item_class()
    $ hg_onepiece_sport_swimsuit_ITEM.id = "hg_onepiece_sport_swimsuit"
    $ hg_onepiece_sport_swimsuit_ITEM.name = "Sports Swimsuits"
    $ hg_onepiece_sport_swimsuit_ITEM.items = ["one-piece"]
    $ hg_onepiece_sport_swimsuit_ITEM.cost = 69
    $ hg_onepiece_sport_swimsuit_ITEM.wait_time = 1
    $ hg_onepiece_sport_swimsuit_ITEM.image = "hg_onepiece_swimsuit_sport.png"
    $ hg_onepiece_sport_swimsuit_ITEM.description = ">Comes in 4 different variants. \nSwimmies not included!"


    # Accessories
    if not hasattr(renpy.store,'hg_accs_wool_g_ITEM'): # Not a store item!
        $ hg_accs_wool_g_ITEM = store_item_class()
    $ hg_accs_wool_g_ITEM.id = "hg_wool_accs_g"
    $ hg_accs_wool_g_ITEM.name = "Gryffindor Wool Accessories"
    $ hg_accs_wool_g_ITEM.items = ["scarf","gloves","stockings"]
    $ hg_accs_wool_g_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_accs_wool_g_ITEM.image = "hg_accs_wool_g.png"

    # Clothing
    if not hasattr(renpy.store,'hg_muggle_cold_ITEM'): # Not a store item!
        $ hg_muggle_cold_ITEM = store_item_class()
    $ hg_muggle_cold_ITEM.id = "hg_muggle_cold"
    $ hg_muggle_cold_ITEM.name = "Cold Weather Clothing"
    $ hg_muggle_cold_ITEM.items = ["pullover","skirt","pantyhose"]
    $ hg_muggle_cold_ITEM.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_cold_ITEM.image = "hg_muggle_cold.png"

    if not hasattr(renpy.store,'hg_muggle_cold_sexy_ITEM'): # Not a store item!
        $ hg_muggle_cold_sexy_ITEM = store_item_class()
    $ hg_muggle_cold_sexy_ITEM.id = "hg_muggle_cold_sexy"
    $ hg_muggle_cold_sexy_ITEM.name = "Sexy Cold Weather Clothing"
    $ hg_muggle_cold_sexy_ITEM.items = ["pullover","skirt","pantyhose"]
    $ hg_muggle_cold_sexy_ITEM.unlockable = True # Not purchasable. Upgradable after buying base version and then speaking to Tonks.
    $ hg_muggle_cold_sexy_ITEM.image = "hg_muggle_cold_sexy.png"

    if not hasattr(renpy.store,'hg_muggle_hot_ITEM'): # Not a store item!
        $ hg_muggle_hot_ITEM = store_item_class()
    $ hg_muggle_hot_ITEM.id = "hg_muggle_hot"
    $ hg_muggle_hot_ITEM.name = "Hot Weather Clothing"
    $ hg_muggle_hot_ITEM.items = ["top","hot pants","stockings"]
    $ hg_muggle_hot_ITEM.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_hot_ITEM.image = "hg_muggle_hot.png"

    if not hasattr(renpy.store,'hg_muggle_rainy_ITEM'): # Not a store item!
        $ hg_muggle_rainy_ITEM = store_item_class()
    $ hg_muggle_rainy_ITEM.id = "hg_muggle_rainy"
    $ hg_muggle_rainy_ITEM.name = "Rainy Weather Clothing"
    $ hg_muggle_rainy_ITEM.items = ["sweater","long jeans"]
    $ hg_muggle_rainy_ITEM.unlockable = True # Not purchasable. Unlocks randomly when summoning Hermione.
    $ hg_muggle_rainy_ITEM.image = "hg_muggle_rainy.png"

    if not hasattr(renpy.store,'hg_punk_rocker_ITEM'):
        $ hg_punk_rocker_ITEM = store_item_class()
    $ hg_punk_rocker_ITEM.id = "hg_punk_rocker"
    $ hg_punk_rocker_ITEM.name = "Punk Rocker"
    $ hg_punk_rocker_ITEM.items = ["top","bottom","gloves","choker"]
    $ hg_punk_rocker_ITEM.cost = 180
    $ hg_punk_rocker_ITEM.wait_time = 2
    $ hg_punk_rocker_ITEM.image = "hg_punk_rocker.png"
    $ hg_punk_rocker_ITEM.description = ">A punk-rock set of clothes for the more rebellious\n type of witch."

    if not hasattr(renpy.store,'hg_punk_leather_ITEM'):
        $ hg_punk_leather_ITEM = store_item_class()
    $ hg_punk_leather_ITEM.id = "hg_punk_leather"
    $ hg_punk_leather_ITEM.name = "Punk Leather"
    $ hg_punk_leather_ITEM.items = ["top","bottom","bra","stockings"]
    $ hg_punk_leather_ITEM.cost = 300
    $ hg_punk_leather_ITEM.wait_time = 3
    $ hg_punk_leather_ITEM.image = "hg_punk_leather.png"
    $ hg_punk_leather_ITEM.description = ">A punk-leather set for wicked witches!\n The sleeve-length of the Leather-jacket can be changed."

    $ hermione_clothing_sets_list = []
    $ hermione_clothing_sets_list.append(hg_cheer_g_ITEM)
    $ hermione_clothing_sets_list.append(hg_cheer_g_sexy_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_s_ITEM)
    $ hermione_clothing_sets_list.append(hg_cheer_s_sexy_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_r_ITEM)
    $ hermione_clothing_sets_list.append(hg_cheer_r_sexy_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_cheer_h_ITEM)
    $ hermione_clothing_sets_list.append(hg_cheer_h_sexy_ITEM) #Unlockable

    $ hermione_clothing_sets_list.append(hg_lingerie_lace_ITEM)
    $ hermione_clothing_sets_list.append(hg_lingerie_silk_ITEM)
    $ hermione_clothing_sets_list.append(hg_lingerie_maid_ITEM)
    $ hermione_clothing_sets_list.append(hg_lingerie_latex_ITEM)
    $ hermione_clothing_sets_list.append(hg_lingerie_fishnet_ITEM)

    #$ hermione_clothing_sets_list.append(hg_nighty_silk_ITEM)
    #$ hermione_clothing_sets_list.append(hg_nightgown_ITEM)

    $ hermione_clothing_sets_list.append(hg_bikini_latex_ITEM)
    $ hermione_clothing_sets_list.append(hg_bikini_sling_ITEM)

    #$ hermione_clothing_sets_list.append(hg_onepiece_sling_ITEM)
    $ hermione_clothing_sets_list.append(hg_onepiece_sport_swimsuit_ITEM)

    $ hermione_clothing_sets_list.append(hg_accs_wool_g_ITEM) #Unlockable

    $ hermione_clothing_sets_list.append(hg_muggle_cold_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_cold_sexy_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_hot_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_muggle_rainy_ITEM) #Unlockable
    $ hermione_clothing_sets_list.append(hg_punk_rocker_ITEM)
    $ hermione_clothing_sets_list.append(hg_punk_leather_ITEM)
    python:
        for i in hermione_clothing_sets_list:
            i.type = "set"


    # Luna Sets
    if not hasattr(renpy.store,'ll_cheer_r_ITEM'):
        $ ll_cheer_r_ITEM = store_item_class()
    $ ll_cheer_r_ITEM.id = "ll_cheer_r"
    $ ll_cheer_r_ITEM.name = "Ravenclaw Cheerleader" #British english...
    $ ll_cheer_r_ITEM.cost = 80
    $ ll_cheer_r_ITEM.items = ["top","bottom","stockings"]
    $ ll_cheer_r_ITEM.wait_time = 2
    $ ll_cheer_r_ITEM.image = "ll_cheer_r.png"
    $ ll_cheer_r_ITEM.description = ">The Ravenclaw version of the Cheerleader attire."

    if not hasattr(renpy.store,'ll_lingerie_silk_ITEM'):
        $ ll_lingerie_silk_ITEM = store_item_class()
    $ ll_lingerie_silk_ITEM.id = "ll_lingerie_silk"
    $ ll_lingerie_silk_ITEM.name = "Silk Lingerie"
    $ ll_lingerie_silk_ITEM.items = ["bra","panties"]
    $ ll_lingerie_silk_ITEM.cost = 80
    $ ll_lingerie_silk_ITEM.wait_time = 1
    $ ll_lingerie_silk_ITEM.image = "ll_lingerie_silk.png"
    $ ll_lingerie_silk_ITEM.description = ">A smooth and comfortable silk bra and panty set."

    if not hasattr(renpy.store,'ll_pyjama_ITEM'):
        $ ll_pyjama_ITEM = store_item_class()
    $ ll_pyjama_ITEM.id = "ll_pyjama"
    $ ll_pyjama_ITEM.name = "Pyjama" #British english...
    #$ ll_pyjama_ITEM.unlockable = True
    $ ll_pyjama_ITEM.cost = 40
    $ ll_pyjama_ITEM.items = ["top","bottom"]
    $ ll_pyjama_ITEM.wait_time = 1
    $ ll_pyjama_ITEM.image = "ll_pyjama.png"
    $ ll_pyjama_ITEM.description = ">A quirky pyjama for a quirky girl."

    $ luna_clothing_sets_list = []
    $ luna_clothing_sets_list.append(ll_cheer_r_ITEM)
    $ luna_clothing_sets_list.append(ll_lingerie_silk_ITEM)
    $ luna_clothing_sets_list.append(ll_pyjama_ITEM)
    python:
        for i in luna_clothing_sets_list:
            i.type = "set"


    # Astoria Sets
    if not hasattr(renpy.store,'ag_boss_uniform_ITEM'): #Like in Hugo Boss...
        $ ag_boss_uniform_ITEM = store_item_class()
    $ ag_boss_uniform_ITEM.id = "ag_boss_uniform"
    $ ag_boss_uniform_ITEM.name = "Boss Uniform"
    $ ag_boss_uniform_ITEM.cost = 500
    $ ag_boss_uniform_ITEM.items = ["top","bottom","hair","hat"]
    $ ag_boss_uniform_ITEM.wait_time = 3
    $ ag_boss_uniform_ITEM.image = "ag_boss_uniform.png"
    $ ag_boss_uniform_ITEM.description = ">A uniform I designed with an old friend of mine.\n Makes me wonder what happened to Hugo..."

    if not hasattr(renpy.store,'ag_lingerie_lace_ITEM'):
        $ ag_lingerie_lace_ITEM = store_item_class()
    $ ag_lingerie_lace_ITEM.id = "ag_lingerie_lace"
    $ ag_lingerie_lace_ITEM.name = "Lace Lingerie"
    $ ag_lingerie_lace_ITEM.cost = 80
    $ ag_lingerie_lace_ITEM.items = ["bra","panties"]
    $ ag_lingerie_lace_ITEM.wait_time = 1
    $ ag_lingerie_lace_ITEM.image = "ag_lingerie_lace.png"
    $ ag_lingerie_lace_ITEM.description = ">A cute lace lingerie set."

    if not hasattr(renpy.store,'ag_lingerie_lewd_ITEM'):
        $ ag_lingerie_lewd_ITEM = store_item_class()
    $ ag_lingerie_lewd_ITEM.id = "ag_lingerie_lewd"
    $ ag_lingerie_lewd_ITEM.name = "Lewd Lingerie"
    $ ag_lingerie_lewd_ITEM.cost = 120
    $ ag_lingerie_lewd_ITEM.items = ["bra","panties"]
    $ ag_lingerie_lewd_ITEM.wait_time = 1
    $ ag_lingerie_lewd_ITEM.image = "ag_lingerie_lewd.png"
    $ ag_lingerie_lewd_ITEM.description ="> A very rewealing lingerie set."

    if not hasattr(renpy.store,'ag_nighty_silk_ITEM'):
        $ ag_nighty_silk_ITEM = store_item_class()
    $ ag_nighty_silk_ITEM.id = "ag_nighty_silk"
    $ ag_nighty_silk_ITEM.name = "Silk Nighty"
    $ ag_nighty_silk_ITEM.cost = 140
    $ ag_nighty_silk_ITEM.items = ["nighty","panties","stockings"]
    $ ag_nighty_silk_ITEM.wait_time = 1
    $ ag_nighty_silk_ITEM.image = "ag_nighty_silk.png"
    $ ag_nighty_silk_ITEM.description = ">+2 attack points while pillow-fighting!"

    $ astoria_clothing_sets_list = []
    $ astoria_clothing_sets_list.append(ag_boss_uniform_ITEM)
    $ astoria_clothing_sets_list.append(ag_lingerie_lace_ITEM)
    $ astoria_clothing_sets_list.append(ag_lingerie_lewd_ITEM)
    $ astoria_clothing_sets_list.append(ag_nighty_silk_ITEM)
    python:
        for i in astoria_clothing_sets_list:
            i.type = "set"


    # Susan Sets

    #ADD

    $ susan_clothing_sets_list = []
    #$ susan_clothing_sets_list.append()


    # Cho Sets

    if not hasattr(renpy.store,'cc_muggle_party_OBJ'): # Not a store item!
        $ cc_muggle_hot_ITEM = store_item_class()
    $ cc_muggle_hot_ITEM.id = "cc_muggle_hot"
    $ cc_muggle_hot_ITEM.name = "Hot Weather Clothing"
    $ cc_muggle_hot_ITEM.items = ["top","pants","stockings"]
    $ cc_muggle_hot_ITEM.unlockable = True # Not purchasable. Unlocks randomly when summoning Cho.
    $ cc_muggle_hot_ITEM.image = "cc_muggle_hot.png"

    if not hasattr(renpy.store,'cc_party_slut_ITEM'): # Not a store item!
        $ cc_party_slut_ITEM = store_item_class()
    $ cc_party_slut_ITEM.id = "cc_party"
    $ cc_party_slut_ITEM.name = "Party Clothing"
    $ cc_party_slut_ITEM.items = ["bra","skirt"]
    $ cc_party_slut_ITEM.unlockable = True
    $ cc_party_slut_ITEM.image = "cc_party.png"

    $ cho_clothing_sets_list = []
    $ cho_clothing_sets_list.append(cc_muggle_hot_ITEM)
    $ cho_clothing_sets_list.append(cc_party_slut_ITEM)
    python:
        for i in cho_clothing_sets_list:
            i.type = "set"


    ### OUTFITS ###

    #Hermione Outfits.
    if not hasattr(renpy.store,'hg_outfit_maid_ITEM'): #important!
        $ hg_outfit_maid_ITEM = store_item_class()
    $ hg_outfit_maid_ITEM.id = "hg_outfit_maid"
    $ hg_outfit_maid_ITEM.name = "Maid"
    $ hg_outfit_maid_ITEM.cost = 250
    $ hg_outfit_maid_ITEM.type = "outfit"
    $ hg_outfit_maid_ITEM.items = ["outfit","hair","hat","gloves","garter","stockings"]
    $ hg_outfit_maid_ITEM.wait_time = 2
    $ hg_outfit_maid_ITEM.image = "hg_maid.png"
    $ hg_outfit_maid_ITEM.description = ">A classic Maids Outfit for a classy Witch."

    if not hasattr(renpy.store,'hg_outfit_pirate_ITEM'): #Also gets unlocked from mirror event.
        $ hg_outfit_pirate_ITEM = store_item_class()
    $ hg_outfit_pirate_ITEM.id = "hg_outfit_pirate"
    $ hg_outfit_pirate_ITEM.name = "Pirate"
    $ hg_outfit_pirate_ITEM.cost = 75
    $ hg_outfit_pirate_ITEM.type = "outfit"
    $ hg_outfit_pirate_ITEM.items = ["outfit"]
    $ hg_outfit_pirate_ITEM.wait_time = 1
    $ hg_outfit_pirate_ITEM.image = "hg_pirate.png"
    $ hg_outfit_pirate_ITEM.description = "> A lightweight Pirates outfit with only room for the\n necessities. Comes with two canon ball storage compartments."

    if not hasattr(renpy.store,'hg_outfit_christmas_ITEM'):
        $ hg_outfit_christmas_ITEM = store_item_class()
    $ hg_outfit_christmas_ITEM.id = "hg_outfit_christmas"
    $ hg_outfit_christmas_ITEM.name = "Christmas Girl"
    $ hg_outfit_christmas_ITEM.cost = 50
    $ hg_outfit_christmas_ITEM.type = "outfit"
    $ hg_outfit_christmas_ITEM.items = ["outfit"]
    $ hg_outfit_christmas_ITEM.wait_time = 2
    $ hg_outfit_christmas_ITEM.image = "hg_christmas.png"
    $ hg_outfit_christmas_ITEM.description = ">A christmas themed outfit complete with tightly wrapped\n snowglobes."

    if not hasattr(renpy.store,'hg_outfit_present_ITEM'):
        $ hg_outfit_present_ITEM = store_item_class()
    $ hg_outfit_present_ITEM.id = "hg_outfit_present"
    $ hg_outfit_present_ITEM.name = "Present"
    $ hg_outfit_present_ITEM.cost = 35
    $ hg_outfit_present_ITEM.type = "outfit"
    $ hg_outfit_present_ITEM.items = ["outfit"]
    $ hg_outfit_present_ITEM.wait_time = 1
    $ hg_outfit_present_ITEM.image = "hg_present.png"
    $ hg_outfit_present_ITEM.description = ">A tightly wrapped gift, scissors not included."

    if not hasattr(renpy.store,'hg_outfit_japan_ITEM'):
        $ hg_outfit_japan_ITEM = store_item_class()
    $ hg_outfit_japan_ITEM.id = "hg_outfit_japan"
    $ hg_outfit_japan_ITEM.name = "Japanese Schoolgirl"
    $ hg_outfit_japan_ITEM.cost = 125
    $ hg_outfit_japan_ITEM.type = "outfit"
    $ hg_outfit_japan_ITEM.items = ["outfit"]
    $ hg_outfit_japan_ITEM.wait_time = 2
    $ hg_outfit_japan_ITEM.image = "hg_japan.png"
    $ hg_outfit_japan_ITEM.description = ">A schoolgirl outfit traditionally worn in Japan."

    if not hasattr(renpy.store,'hg_outfit_witch_ITEM'):
        $ hg_outfit_witch_ITEM = store_item_class()
    $ hg_outfit_witch_ITEM.id = "hg_outfit_witch"
    $ hg_outfit_witch_ITEM.name = "Witch outfit"
    $ hg_outfit_witch_ITEM.cost = 250
    $ hg_outfit_witch_ITEM.type = "outfit"
    $ hg_outfit_witch_ITEM.items = ["outfit","hat"]
    $ hg_outfit_witch_ITEM.wait_time = 3
    $ hg_outfit_witch_ITEM.image = "hg_witch.png"
    $ hg_outfit_witch_ITEM.description = ">Release your inner witch with this halloween\n inspired outfit."

    if not hasattr(renpy.store,'hg_outfit_egypt_ITEM'):
        $ hg_outfit_egypt_ITEM = store_item_class()
    $ hg_outfit_egypt_ITEM.id = "hg_outfit_egypt"
    $ hg_outfit_egypt_ITEM.name = "Egyptian Goddess"
    #$ hg_outfit_egypt_ITEM.cost = 200
    $ hg_outfit_egypt_ITEM.type = "outfit"
    $ hg_outfit_egypt_ITEM.unlockable = True #Reward for card game.
    $ hg_outfit_egypt_ITEM.image = "hg_egypt.png"


    #Hermione Costumes.
    if not hasattr(renpy.store,'hg_costume_power_girl_ITEM'):
        $ hg_costume_power_girl_ITEM = store_item_class()
    $ hg_costume_power_girl_ITEM.id = "hg_costume_power_girl"
    $ hg_costume_power_girl_ITEM.name = "Power Girl"
    $ hg_costume_power_girl_ITEM.cost = 350
    $ hg_costume_power_girl_ITEM.type = "outfit"
    $ hg_costume_power_girl_ITEM.items = ["outfit"]
    $ hg_costume_power_girl_ITEM.wait_time = 3
    $ hg_costume_power_girl_ITEM.image = "hg_power.png"
    $ hg_costume_power_girl_ITEM.description = ">An outfit for when you feel extra heroic\n \"Sometimes it takes balls to be a woman\"."

    if not hasattr(renpy.store,'hg_costume_ms_marvel_ITEM'):
        $ hg_costume_ms_marvel_ITEM = store_item_class()
    $ hg_costume_ms_marvel_ITEM.id = "hg_costume_ms_marvel"
    $ hg_costume_ms_marvel_ITEM.name = "Mrs Marvel"
    $ hg_costume_ms_marvel_ITEM.cost = 250
    $ hg_costume_ms_marvel_ITEM.type = "outfit"
    $ hg_costume_ms_marvel_ITEM.items = ["outfit"]
    $ hg_costume_ms_marvel_ITEM.wait_time = 2
    $ hg_costume_ms_marvel_ITEM.image = "hg_marvel.png"
    $ hg_costume_ms_marvel_ITEM.description = ">For the girl that likes the lightningbolt\n better on the chest than the forehead."

    if not hasattr(renpy.store,'hg_costume_harley_quinn_ITEM'):
        $ hg_costume_harley_quinn_ITEM = store_item_class()
    $ hg_costume_harley_quinn_ITEM.id = "hg_costume_harley_quinn"
    $ hg_costume_harley_quinn_ITEM.name = "Harley Quinn"
    $ hg_costume_harley_quinn_ITEM.cost = 300
    $ hg_costume_harley_quinn_ITEM.type = "outfit"
    $ hg_costume_harley_quinn_ITEM.items = ["outfit"]
    $ hg_costume_harley_quinn_ITEM.wait_time = 3
    $ hg_costume_harley_quinn_ITEM.image = "hg_harley.png"
    $ hg_costume_harley_quinn_ITEM.description = ">A outfit for when you're actually nuts\n rather than just crazy for them."

    if not hasattr(renpy.store,'hg_costume_lara_croft_ITEM'):
        $ hg_costume_lara_croft_ITEM = store_item_class()
    $ hg_costume_lara_croft_ITEM.id = "hg_costume_lara_croft"
    $ hg_costume_lara_croft_ITEM.name = "Lara Croft"
    $ hg_costume_lara_croft_ITEM.cost = 270
    $ hg_costume_lara_croft_ITEM.type = "outfit"
    $ hg_costume_lara_croft_ITEM.items = ["outfit","gloves"]
    $ hg_costume_lara_croft_ITEM.wait_time = 2
    $ hg_costume_lara_croft_ITEM.image = "hg_lara.png"
    $ hg_costume_lara_croft_ITEM.description = ">An outfit perfectly suited for exploring deep, dark\n and moist caverns."

    if not hasattr(renpy.store,'hg_costume_tifa_ITEM'):
        $ hg_costume_tifa_ITEM = store_item_class()
    $ hg_costume_tifa_ITEM.id = "hg_costume_tifa"
    $ hg_costume_tifa_ITEM.name = "Tifa"
    $ hg_costume_tifa_ITEM.cost = 220
    $ hg_costume_tifa_ITEM.type = "outfit"
    $ hg_costume_tifa_ITEM.items = ["outfit"]
    $ hg_costume_tifa_ITEM.wait_time = 2
    $ hg_costume_tifa_ITEM.image = "hg_tifa.png"
    $ hg_costume_tifa_ITEM.description = ">An outfit for when when your sexual fantasies\n are just getting started."

    if not hasattr(renpy.store,'hg_costume_elizabeth_ITEM'):
        $ hg_costume_elizabeth_ITEM = store_item_class()
    $ hg_costume_elizabeth_ITEM.id = "hg_costume_elizabeth"
    $ hg_costume_elizabeth_ITEM.name = "Bioshock outfit"
    $ hg_costume_elizabeth_ITEM.cost = 400
    $ hg_costume_elizabeth_ITEM.type = "outfit"
    $ hg_costume_elizabeth_ITEM.items = ["outfit","hair","choker"]
    $ hg_costume_elizabeth_ITEM.wait_time = 3
    $ hg_costume_elizabeth_ITEM.image = "hg_bio.png"
    $ hg_costume_elizabeth_ITEM.description = ">Flick some coins for this Bioshock inspired outfit."

    if not hasattr(renpy.store,'hg_costume_yennefer_ITEM'):
        $ hg_costume_yennefer_ITEM = store_item_class()
    $ hg_costume_yennefer_ITEM.id = "hg_costume_yennefer"
    $ hg_costume_yennefer_ITEM.name = "Yennefer's costume"
    $ hg_costume_yennefer_ITEM.cost = 500
    $ hg_costume_yennefer_ITEM.type = "outfit"
    $ hg_costume_yennefer_ITEM.items = ["outfit","scarf","choker","stockings"]
    $ hg_costume_yennefer_ITEM.wait_time = 3
    $ hg_costume_yennefer_ITEM.image = "hg_yenn.png"
    $ hg_costume_yennefer_ITEM.description = ">A Witcher inspired outfit to fit even the most\n perverted witch"


    #Hermione Dresses.
    if not hasattr(renpy.store,'hg_dress_yule_ball_ITEM'):
        $ hg_dress_yule_ball_ITEM = store_item_class()
    $ hg_dress_yule_ball_ITEM.id = "hg_dress_yule_ball"
    $ hg_dress_yule_ball_ITEM.name = "Ball Dress"
    $ hg_dress_yule_ball_ITEM.cost = 1500
    $ hg_dress_yule_ball_ITEM.type = "outfit"
    $ hg_dress_yule_ball_ITEM.items = ["outfit","hair","neckless","tiara"]
    $ hg_dress_yule_ball_ITEM.wait_time = 7
    $ hg_dress_yule_ball_ITEM.image = "hg_ball_dress.png"
    $ hg_dress_yule_ball_ITEM.description = ">A traditional ball dress complete with a imitation\n ball-queen tiara."

    if not hasattr(renpy.store,'hg_dress_dancer_ITEM'):
        $ hg_dress_dancer_ITEM = store_item_class()
    $ hg_dress_dancer_ITEM.id = "hg_dress_dancer"
    $ hg_dress_dancer_ITEM.name = "Heart Dancer"
    $ hg_dress_dancer_ITEM.cost = 80
    $ hg_dress_dancer_ITEM.type = "outfit"
    $ hg_dress_dancer_ITEM.items = ["outfit"]
    $ hg_dress_dancer_ITEM.wait_time = 1
    $ hg_dress_dancer_ITEM.image = "hg_heart.png"
    $ hg_dress_dancer_ITEM.description = ">A sexy dancers outfit with heart shaped nipple tassels."



    $ hermione_outfits_list = []
    $ hermione_outfits_list.append(hg_outfit_maid_ITEM)
    $ hermione_outfits_list.append(hg_outfit_pirate_ITEM)
    $ hermione_outfits_list.append(hg_outfit_christmas_ITEM)
    $ hermione_outfits_list.append(hg_outfit_present_ITEM)
    $ hermione_outfits_list.append(hg_outfit_japan_ITEM)
    $ hermione_outfits_list.append(hg_outfit_witch_ITEM)
    $ hermione_outfits_list.append(hg_outfit_egypt_ITEM)

    $ hermione_outfits_list.append(hg_costume_power_girl_ITEM)
    $ hermione_outfits_list.append(hg_costume_ms_marvel_ITEM)
    $ hermione_outfits_list.append(hg_costume_harley_quinn_ITEM)
    $ hermione_outfits_list.append(hg_costume_lara_croft_ITEM)
    $ hermione_outfits_list.append(hg_costume_tifa_ITEM)
    $ hermione_outfits_list.append(hg_costume_elizabeth_ITEM)
    $ hermione_outfits_list.append(hg_costume_yennefer_ITEM)

    $ hermione_outfits_list.append(hg_dress_yule_ball_ITEM)
    $ hermione_outfits_list.append(hg_dress_dancer_ITEM)


    # Luna Outfits

    #ADD

    $ luna_outfits_list = []
    #$ luna_outfits_list.append()


    # Astoria
    if not hasattr(renpy.store,'ag_costume_lazy_town_ITEM'):
        $ ag_costume_lazy_town_ITEM = store_item_class()
    $ ag_costume_lazy_town_ITEM.id = "ag_costume_lazy_town"
    $ ag_costume_lazy_town_ITEM.name = "Lazy Town Outfit"
    $ ag_costume_lazy_town_ITEM.cost = 120
    $ ag_costume_lazy_town_ITEM.type = "outfit"
    $ ag_costume_lazy_town_ITEM.items = ["outfit","hair","bracelet"]
    $ ag_costume_lazy_town_ITEM.wait_time = 1
    $ ag_costume_lazy_town_ITEM.image = "ag_lazy.png"
    $ ag_costume_lazy_town_ITEM.description = ">Nobody is lazy at Hogwarts!"

    if not hasattr(renpy.store,'ag_costume_lazy_town_short_ITEM'): #Not a store item!
        $ ag_costume_lazy_town_short_ITEM = store_item_class()
    $ ag_costume_lazy_town_short_ITEM.id = "ag_costume_lazy_town_short"
    $ ag_costume_lazy_town_short_ITEM.name = "Short Lazy Town Outfit"
    $ ag_costume_lazy_town_short_ITEM.unlockable = True
    #$ ag_costume_lazy_town_short_ITEM.cost = 120
    $ ag_costume_lazy_town_short_ITEM.type = "outfit"
    $ ag_costume_lazy_town_short_ITEM.items = ["outfit","hair","bracelet"]
    $ ag_costume_lazy_town_short_ITEM.wait_time = 1
    $ ag_costume_lazy_town_short_ITEM.image = "ag_lazy_short.png"
    $ ag_costume_lazy_town_short_ITEM.description = ">Nobody is lazy at Hogwarts!"

    if not hasattr(renpy.store,'ag_dress_yule_ball_ITEM'):
        $ ag_dress_yule_ball_ITEM = store_item_class()
    $ ag_dress_yule_ball_ITEM.id = "ag_dress_yule_ball"
    $ ag_dress_yule_ball_ITEM.name = "Ball Dress"
    $ ag_dress_yule_ball_ITEM.cost = 300
    $ ag_dress_yule_ball_ITEM.type = "outfit"
    $ ag_dress_yule_ball_ITEM.items = ["outfit"]
    $ ag_dress_yule_ball_ITEM.wait_time = 4
    $ ag_dress_yule_ball_ITEM.image = "ag_ball_dress.png"
    $ ag_dress_yule_ball_ITEM.description = ">A cute dress for your favourite princess!"

    $ astoria_outfits_list = []
    $ astoria_outfits_list.append(ag_costume_lazy_town_ITEM)
    $ astoria_outfits_list.append(ag_costume_lazy_town_short_ITEM)

    $ astoria_outfits_list.append(ag_dress_yule_ball_ITEM)


    # Susan Outfits

    #ADD

    $ susan_outfits_list = []
    #$ susan_outfits_list.append()


    # Cho Outfits
    if not hasattr(renpy.store,'cc_outfit_quidditch_ITEM'):
        $ cc_outfit_quidditch_ITEM = store_item_class()
    $ cc_outfit_quidditch_ITEM.id = "cc_outfit_quidditch"
    $ cc_outfit_quidditch_ITEM.name = "Quidditch Outfit"
    $ cc_outfit_quidditch_ITEM.unlockable = True
    #$ cc_outfit_quidditch_ITEM.cost = 100
    $ cc_outfit_quidditch_ITEM.type = "outfit"
    $ cc_outfit_quidditch_ITEM.items = ["outfit"]
    $ cc_outfit_quidditch_ITEM.wait_time = 1
    $ cc_outfit_quidditch_ITEM.image = "cc_quidditch.png"
    $ cc_outfit_quidditch_ITEM.description = ">Cho's Quidditch outfit."

    if not hasattr(renpy.store,'cc_dress_traditional_ITEM'):
        $ cc_dress_traditional_ITEM = store_item_class()
    $ cc_dress_traditional_ITEM.id = "cc_dress_traditional"
    $ cc_dress_traditional_ITEM.name = "Traditional Dress"
    $ cc_dress_traditional_ITEM.cost = 300
    $ cc_dress_traditional_ITEM.type = "outfit"
    $ cc_dress_traditional_ITEM.items = ["outfit"]
    $ cc_dress_traditional_ITEM.wait_time = 4
    $ cc_dress_traditional_ITEM.image = "cc_traditional_dress.png"
    $ cc_dress_traditional_ITEM.description = ">A traditional dress inspired by chinese culture."

    $ cho_outfits_list = []
    $ cho_outfits_list.append(cc_outfit_quidditch_ITEM)

    $ cho_outfits_list.append(cc_dress_traditional_ITEM)





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
        for i in luna_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in susan_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in cho_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)

        #Sets
        for i in hermione_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in luna_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in susan_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in cho_clothing_sets_list:
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
        number = 0 #Amount of items of this type that you possess. Can be used for weasley store and gift items.
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
