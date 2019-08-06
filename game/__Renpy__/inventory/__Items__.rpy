

label store_items_init:

    if not hasattr(renpy.store,'lollipop_ITEM'):
        $ lollipop_ITEM          = item_class(id="lollipop", name="Lollipop Candy",              cost=20, type="candy", image="item_lollipop", description="A lollipop candy. An adult candy for kids or kids candy for adults?")
        $ chocolate_ITEM         = item_class(id="chocolate", name="Chocolate",                  cost=40, type="candy", image="item_chocolate", description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
        $ plush_owl_ITEM         = item_class(id="plush_owl", name="Plush owl",                  cost=35, type="toy", image="item_plush_owl", description="A Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
        $ butterbeer_ITEM        = item_class(id="butterbeer", name="Butterbeer",                cost=50, type="drink", image="item_butterbeer", description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
        $ science_mag_ITEM       = item_class(id="science_mag", name="Educational Magazines",    cost=30, type="mag", image="item_mag_science", description="Educational magazines. \nthe Trusty companions of every social outcast.")
        $ girls_mag_ITEM         = item_class(id="girls_mag", name="Girly Magazines",            cost=45, type="mag", image="item_mag_girls", description="Girly magazines. \nAll cool girls are reading these.")
        $ adult_mag_ITEM         = item_class(id="adult_mag", name="Adult magazines",            cost=60, type="mag", image="item_mag_adult", description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
        $ porn_mag_ITEM          = item_class(id="porn_mag", name="Porn magazines",              cost=80, type="mag", image="item_mag_porn", description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
        $ krum_poster_ITEM       = item_class(id="krum_poster", name="Viktor Krum Poster",       cost=25, type="mag", image="item_krum_poster", description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
        $ sexy_lingerie_ITEM     = item_class(id="sexy_lingerie", name="Sexy Lingerie",          cost=75, type="", image="item_sexy_lingerie", description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
        $ sexy_stockings_ITEM    = item_class(id="sexy_stockings", name="Sexy Stockings",        cost=50, type="", image="item_sexy_stockings", description="")
        $ pink_condoms_ITEM      = item_class(id="pink_condoms", name="A Pack Of Condoms",       cost=50, type="toy", image="item_condoms_pink", description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
        $ vibrator_ITEM          = item_class(id="vibrator", name="Vibrator",                    cost=55, type="toy", image="item_vibrator", description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
        $ anal_lube_ITEM         = item_class(id="anal_lube", name="Jar of anal lubricant",      cost=60, type="toy", image="item_anal_lube", description="A Jar of anal lube, Buy this for your loved one - show that you care.")
        $ ballgag_and_cuffs_ITEM = item_class(id="ballgag_and_cuffs", name="Ball gag and cuffs", cost=70, type="toy", image="item_ballgag_and_cuffs", description="Ball gag and cuffs, Turn your soulmate into your cellmate.")
        $ anal_plugs_ITEM        = item_class(id="anal_plugs", name="Anal plugs",                cost=85, type="toy", image="item_anal_plugs", description="Anal plugs decorated with actual tails. Sizes vary to satisfy expert practitioners and beginner alike.")
        $ testral_strapon_ITEM   = item_class(id="testral_strapon", name="Thestral Strap-on",    cost=200,type="toy", image="item_strap_on_testral", description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")
        $ broom_2000_ITEM        = item_class(id="broom_2000", name="Lady Speed Stick-2000",     cost=500,type="toy", image="item_broom", description="The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")
        $ sexdoll_ITEM           = item_class(id="sexdoll", name="Sex doll \"Joanne\"",          cost=350,type="toy", image="item_sexdoll", description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
        $ anal_beads_ITEM        = item_class(id="anal_beads", name="Anal beads",                cost=65, type="toy", image="item_anal_beads", description="Anal beads engraved with a strange inscription \"Property of L.C.\".")
        #$ _ITEM = item_class(id="", name="", cost=50, type="", image="", description="")

    if not hasattr(renpy.store,'firewhisky_ITEM'):
        $ wine_ITEM              = item_class(id="wine", name="Wine", cost=60, type="drink", image="item_wine", description="Add description. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
        $ firewhisky_ITEM       = item_class(id="firewhisky", name="firewhisky", cost=80, unlockable=True ,type="drink", image="item_wine", description="Add description. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")

    if game_difficulty <= 1:
        $ wine_ITEM.cost = 40
        $ firewhisky_ITEM.cost = 60
    elif game_difficulty == 2:
        $ wine_ITEM.cost = 60
        $ firewhisky_ITEM.cost = 80
    else:
        $ wine_ITEM.cost = 140
        $ firewhisky_ITEM.cost = 160

    $ candy_gift_list = [
        lollipop_ITEM, chocolate_ITEM,
    ]

    $ drink_gift_list = [
        butterbeer_ITEM, wine_ITEM, firewhisky_ITEM
    ]

    $ mag_gift_list = [
        krum_poster_ITEM, science_mag_ITEM, girls_mag_ITEM, adult_mag_ITEM, porn_mag_ITEM,
    ]

    $ toy_gift_list = [
        plush_owl_ITEM, pink_condoms_ITEM, sexy_lingerie_ITEM, vibrator_ITEM, anal_lube_ITEM, ballgag_and_cuffs_ITEM,
        anal_plugs_ITEM, testral_strapon_ITEM, broom_2000_ITEM, sexdoll_ITEM, anal_beads_ITEM,
    ]

    #sexy_lingerie_ITEM #sexy_stockings_ITEM


    ### Scroll Items ###
    if not hasattr(renpy.store,'sealed_scroll_ITEM'):
        $ sealed_scroll_ITEM = scroll_class(id="sealed_scroll",   name="Forbidden Scroll",  cost=300,   type="scroll", image="item_scroll_sealed", description=">Quest Item!")
        $ scroll_1_ITEM = scroll_class(id="scroll_1",   name="The room",           cost=1,   type="scroll", image="item_scroll", scroll_image="1", comments=["This is a first ever draft of the Dumbledore's office.","Not a very exciting thing to look at, sure. But holds great historical value."])
        $ scroll_2_ITEM = scroll_class(id="scroll_2",   name="The calendar",       cost=2,   type="scroll", image="item_scroll", scroll_image="2", comments=["The calendar...","On the early stages of development I toyed with an idea of implementing an actual in-game calendar into the gameplay...","I soon realized how much more difficult it would be to create a game like that...","And since I personally believe that any time limits in any game always work against the fun factor I decided to abandon the idea...","Later on I used this drawing as a parchment paper for letters to be written on..."])
        $ scroll_3_ITEM = scroll_class(id="scroll_3",   name="The girl",           cost=10,  type="scroll", image="item_scroll", scroll_image="3", comments=["A couple of very early drawings of Hermione..."])
        $ scroll_4_ITEM = scroll_class(id="scroll_4",   name="Deeptroating",       cost=60,  type="scroll", image="item_scroll", scroll_image="4", comments=["The deepthroating scene...","My first attempt.","Been deemed unworthy and ended up here."])
        $ scroll_5_ITEM = scroll_class(id="scroll_5",   name="Poster 01",          cost=50,  type="scroll", image="item_scroll", scroll_image="5", comments=["The game poster...","Hermione is Dahr's work. The rest is me..."])
        $ scroll_6_ITEM = scroll_class(id="scroll_6",   name="Poster 02",          cost=50,  type="scroll", image="item_scroll", scroll_image="6", comments=["Alternative game poster.","This one has never been released."])
        $ scroll_7_ITEM = scroll_class(id="scroll_7",   name="Chibi-dancing",      cost=20,  type="scroll", image="item_scroll", scroll_image="7", comments=["Some chibi closeups.","The one on the left never made it into the final game..."])
        $ scroll_8_ITEM = scroll_class(id="scroll_8",   name="Game items",         cost=10,  type="scroll", image="item_scroll", scroll_image="8", comments=["A banch of items that I ended up not using...","I blame dahr and his awesome artwork."])
        $ scroll_9_ITEM = scroll_class(id="scroll_9",   name="Panties no panties", cost=50,  type="scroll", image="item_scroll", scroll_image="9", comments=["The drawing of Hermione from the poster. (by Dahr)","I like one on the right with her panties still on."])
        $ scroll_10_ITEM = scroll_class(id="scroll_10", name="A lot of pegs",      cost=50,  type="scroll", image="item_scroll", scroll_image="10", comments=["Another ithing that never made it into the final game...","The idea here was that the more you level up Hermione the more pegs she would let you to put on her...","And the nipple chain was supposed to be worn to class under the uniform."])
        $ scroll_11_ITEM = scroll_class(id="scroll_11", name="House-elf brothel",  cost=80,  type="scroll", image="item_scroll", scroll_image="11", comments=["The house-elf brothel... Just another thing that never happened."])
        $ scroll_12_ITEM = scroll_class(id="scroll_12", name="Me and Lola",        cost=10,  type="scroll", image="item_scroll", scroll_image="12", comments=["A drawing featuring yours truly as a Durmstrung mage and Lola as a student...","The drawing itself is by Dahr of course."])
        $ scroll_13_ITEM = scroll_class(id="scroll_13", name="Hard training",      cost=80,  type="scroll", image="item_scroll", scroll_image="13", comments=["Another one of those side-quests that never happened...","This one was about--","No, I better not. Who knows, maybe we will get to adding those quests eventually."])
        $ scroll_14_ITEM = scroll_class(id="scroll_14", name="Wizard's Chess",     cost=50,  type="scroll", image="item_scroll", scroll_image="14", comments=["Another sub-quest...","This one involving the school's wizard chess club."])
        $ scroll_15_ITEM = scroll_class(id="scroll_15", name="Tutoring books",     cost=10,  type="scroll", image="item_scroll", scroll_image="15", comments=["There is more then one way for a pretty girl to carry her books around.","I thought it would be cool to change the way Hermione carries the books as she progresses with her training.","Since the whole tutoring arc got canceled I am showing it here..."])

        $ scroll_16_ITEM = scroll_class(id="scroll_16", name="Extra gifts 01",     cost=10,  type="scroll", image="item_scroll", scroll_image="16", comments=["A couple of items that didn't make it into the final game...","The one on the left is an actual live house-elf to give as a present.","The one on the right is a portrait of a pervy but wise wizard. Supposed to be helping with studying..."])
        $ scroll_17_ITEM = scroll_class(id="scroll_17", name="Extra gifts 02",     cost=10,  type="scroll", image="item_scroll", scroll_image="17", comments=["Few more items...","A newspaper, a bottle of perfume and a magical hat that says things you want to hear..."])
        $ scroll_18_ITEM = scroll_class(id="scroll_18", name="Fiction books",      cost=10,  type="scroll", image="item_scroll", scroll_image="18", comments=["The fiction books...","The top row are my sketches, the bottom row are finalized drawings by dahr."])
        $ scroll_19_ITEM = scroll_class(id="scroll_19", name="Singer whore",       cost=60,  type="scroll", image="item_scroll", scroll_image="19", comments=["A drawing of a famous singer.","Has no connection to this game and is here for no reason whatsoever."])
        $ scroll_20_ITEM = scroll_class(id="scroll_20", name="Casting",            cost=60,  type="scroll", image="item_scroll", scroll_image="20", comments=["It took me a while to come up with a proper look for Hermione...","Version \"A\" was my first attempt. And I liked it up until the moment when I started to hate it...","Version \"B\" was my second attempt. And it's good. But her confident and semi-aggressive facial features didn't fit the character well...","Version \"C\" is the one that got the role. The Hermione that we all grew to care for by now, I'm sure."])
        $ scroll_21_ITEM = scroll_class(id="scroll_21", name="Witch robe 01",      cost=20,  type="scroll", image="item_scroll", scroll_image="21", comments=["Sub-quests that never happened.","You are allowed to feel bad for rushing me.","If you did not rush me you are allowed to feel angry at people who did."])
        $ scroll_22_ITEM = scroll_class(id="scroll_22", name="Witch robe 02",      cost=20,  type="scroll", image="item_scroll", scroll_image="22", comments=["Hermione presenting her body to Genie...","This would have been a quite memorable scene..."])
        $ scroll_23_ITEM = scroll_class(id="scroll_23", name="Witch robe 03",      cost=20,  type="scroll", image="item_scroll", scroll_image="23", comments=["Didn't expect this one, did you?","In case you're wondering this is still Hermione."])
        $ scroll_24_ITEM = scroll_class(id="scroll_24", name="Witch robe 04",      cost=20,  type="scroll", image="item_scroll", scroll_image="24", comments=[".................................","Sub-quests of course..."])
        $ scroll_25_ITEM = scroll_class(id="scroll_25", name="The walk",           cost=80,  type="scroll", image="item_scroll", scroll_image="25", comments=["Another sub-quest...","We had a rather lengthy discussion with Dahr about this one...","I was sort of against it, but then Dahr sent me this picture and it made me shut up."])
        $ scroll_26_ITEM = scroll_class(id="scroll_26", name="Durmstrang",         cost=80,  type="scroll", image="item_scroll", scroll_image="26", comments=["One the very early stages of development I had an idea of representing outcomes of your failed or successfully completed sub quests with a simplistic plates, or photographs...","At first many of the sub-quests involved deciding on how to spend the Hogwarts budget...","Spend your money to finance the school quiddich team, or to hire new teachers and such..."])
        $ scroll_27_ITEM = scroll_class(id="scroll_27", name="Gag ball",           cost=80,  type="scroll", image="item_scroll", scroll_image="27", comments=["Isn't she adorable?"])
        $ scroll_28_ITEM = scroll_class(id="scroll_28", name="New clothes 01",     cost=50,  type="scroll", image="item_scroll", scroll_image="28", comments=["Another (rather lengthy) sub-quest..."])
        $ scroll_29_ITEM = scroll_class(id="scroll_29", name="New clothes 02",     cost=50,  type="scroll", image="item_scroll", scroll_image="29", comments=[".........."])
        $ scroll_30_ITEM = scroll_class(id="scroll_30", name="The gang",           cost=10,  type="scroll", image="item_scroll", scroll_image="30", comments=["One of the very early sketches related to the quiddich sub-quests..."])

        #Silver Scroll.
        $ scroll_31_ITEM = scroll_class(id="scroll_31", name="Silver",           cost=10,  type="scroll", image="item_scroll_silver", scroll_image="31", comments=[""])
        $ scroll_32_ITEM = scroll_class(id="scroll_32", name="New characters!",   cost=50,  type="scroll", image="item_scroll_silver", scroll_image="32", comments=["More and more characters got added along the way..."])
        $ scroll_33_ITEM = scroll_class(id="scroll_33", name="Lion, Witch, & Wardrobe 1",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="33", comments=["The very first wardrobe that got added to silver."])
        $ scroll_34_ITEM = scroll_class(id="scroll_34", name="Lion, Witch, & Wardrobe 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="34", comments=["The second one already had almost all features from the current one, but didn't look that great..."])
        $ scroll_35_ITEM = scroll_class(id="scroll_35", name="Lion, Witch, & Wardrobe 3",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="35", comments=["The wardrobe got a brand new design, with tons of new features!","Every other girl available in silver has one too!"])

        $ scroll_37_ITEM = scroll_class(id="scroll_37", name="Map 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="37", comments=["First try at the new map.","We removed all the text and labels and replaced them with icons."])

    $ forbidden_scroll_list = [
        sealed_scroll_ITEM,
    ]

    $ scroll_list_A = [
        scroll_1_ITEM, scroll_2_ITEM, scroll_3_ITEM, scroll_4_ITEM, scroll_5_ITEM,
        scroll_6_ITEM, scroll_7_ITEM, scroll_8_ITEM, scroll_9_ITEM, scroll_10_ITEM,
        scroll_11_ITEM, scroll_12_ITEM, scroll_13_ITEM ,scroll_14_ITEM, scroll_15_ITEM,
    ]

    $ scroll_list_B = [
        scroll_16_ITEM, scroll_17_ITEM, scroll_18_ITEM, scroll_19_ITEM, scroll_20_ITEM,
        scroll_21_ITEM, scroll_22_ITEM, scroll_23_ITEM, scroll_24_ITEM, scroll_25_ITEM,
        scroll_26_ITEM, scroll_27_ITEM, scroll_28_ITEM, scroll_29_ITEM, scroll_30_ITEM,
    ]

    $ scroll_list_C = [
        scroll_31_ITEM, scroll_32_ITEM, scroll_33_ITEM, scroll_34_ITEM, scroll_35_ITEM,
        scroll_37_ITEM,
    ]



    #Badges
    if not hasattr(renpy.store,'spew_badge_ITEM'):
        $ spew_badge_ITEM      = item_class(id="spew_badge", name="S.P.E.W. Badge",       type="accessory", items=["badge"],       image="badge_spew",        cost=5,  description=">A badge designed to show one's opposition of elf\n slavery.")
        $ cum_badge_ITEM       = item_class(id="cum_badge", name="I <3 C.U.M. Badge",     type="accessory", items=["badge"],       image="badge_cum",  cost=15, description=">A badge that displays ones affection towards semen.")
        $ cat_ears_ITEM        = item_class(id="cat_ears", name="Cat Ears",               type="accessory", items=["ears","tail"], image="ears_cat",          cost=40, description=">A fluffy set of catlike ears that matches one's\n hair-color!")
        $ elf_ears_ITEM        = item_class(id="elf_ears", name="Elf Ears",               type="accessory", items=["ears"],        image="ears_elf",          cost=20, description=">A pointy set of elven ears.")
        $ reading_glasses_ITEM = item_class(id="reading_glasses", name="Reading Glasses", type="accessory", items=["glasses"],     image="glasses_reading",   cost=50, description=">A lot of wizards are into girls wearing these!")
        $ vintage_glasses_ITEM = item_class(id="vintage_glasses", name="Vintage Glasses", type="accessory", items=["glasses"],     image="glasses_vintage",   cost=70, description=">Wearing these doesn't automatically make you a nerd!")

    $ accs_list=[
        spew_badge_ITEM, cum_badge_ITEM,
        cat_ears_ITEM, elf_ears_ITEM,
        reading_glasses_ITEM, vintage_glasses_ITEM
        ]

    #Makeup
    if not hasattr(renpy.store,'lipstick_red_ITEM'):
        $ lipstick_red_ITEM    = item_class(id="lipstick_red", name="Red Lipstick",   type="makeup", items=["lipstick"], image="lipstick_red",    cost=100, description=">They call this one the red rocket!")
        $ lipstick_pink_ITEM   = item_class(id="lipstick_pink", name="Pink Lipstick", type="makeup", items=["lipstick"], image="lipstick_pink",   unlockable=True)
        $ freckles_makeup_ITEM = item_class(id="freckles_makeup", name="Freckles",    type="makeup", items=["freckles"], image="makeup_freckles", cost=20,  description=">A magical item that makes the wearer's freckles more\n pronounced!")
        $ fake_cum_makeup_ITEM = item_class(id="fake_cum_makeup", name="Fake Cum",    type="makeup", items=["fake cum"], image="makeup_fake_cum", cost=20,  description=">When she doen't want to wear your real cum just yet.\n Be patient!")

    $ misc_list=[
        lipstick_red_ITEM, lipstick_pink_ITEM,
        freckles_makeup_ITEM, fake_cum_makeup_ITEM,
        ]

    # Dyes
    if not hasattr(renpy.store,'brown_dye_ITEM'):
        $ brown_dye_ITEM      = item_class(id="brown_dye", name="Mud-Blood Brown",    type="dye", items=["clothing dye","hair dye"], image="dye_brown",      cost=20,  description=">Basic shade of brown. Simple yet elegant!")
        $ yellow_dye_ITEM     = item_class(id="yellow_dye", name="Niffler's Gold",    type="dye", items=["clothing dye","hair dye"], image="dye_yellow",     cost=40,  description=">A very nice shade of yellow.")
        $ orange_dye_ITEM     = item_class(id="orange_dye", name="Butter Beer",       type="dye", items=["clothing dye"],            image="dye_orange",     cost=60,  description=">A very nice shade of orange.")
        $ red_dye_ITEM        = item_class(id="red_dye", name="Weasel Red",           type="dye", items=["clothing dye","hair dye"], image="dye_red",        cost=60,  description=">A very nice shade of red.")
        $ crimson_dye_ITEM    = item_class(id="crimson_dye", name="Crimson Lion",     type="dye", items=["clothing dye","hair dye"], image="dye_crimson",    cost=80,  description=">A very rich shade of red.")
        $ green_dye_ITEM      = item_class(id="green_dye", name="Bowtruckle Paint",   type="dye", items=["clothing dye"],            image="dye_green",      cost=60,  description=">A bright shade of green.")
        $ dark_green_dye_ITEM = item_class(id="dark_green_dye", name="Serpent Green", type="dye", items=["clothing dye","hair dye"], image="dye_dark_green", cost=80,  description=">A darker shade of green.")
        $ blue_dye_ITEM       = item_class(id="blue_dye", name="Pixie Dye",           type="dye", items=["clothing dye"],            image="dye_blue",       cost=60,  description=">A bright shade of blue.")
        $ dark_blue_dye_ITEM  = item_class(id="dark_blue_dye", name="Raven Blue",     type="dye", items=["clothing dye","hair dye"], image="dye_dark_blue",  cost=80,  description=">A darker shade of blue.")
        $ purple_dye_ITEM     = item_class(id="purple_dye", name="Pygmy Puff Purple", type="dye", items=["clothing dye","hair dye"], image="dye_purple",     cost=100, description=">A very nice shade of purple.")
        $ pink_dye_ITEM       = item_class(id="pink_dye", name="Pussy Pink",          type="dye", items=["clothing dye","hair dye"], image="dye_pink",       cost=120, description=">A color so pink, it makes you want to cover your\n whole room with it!")
        $ gray_dye_ITEM       = item_class(id="gray_dye", name="Ghostly Gray",        type="dye", items=["clothing dye","hair dye"], image="dye_gray",       cost=120, description=">A very classy shade of gray.")
        $ black_dye_ITEM      = item_class(id="black_dye", name="Seriously Black",    type="dye", items=["clothing dye","hair dye"], image="dye_black",      cost=200, description=">As black as a Testral.")
        $ white_dye_ITEM      = item_class(id="white_dye", name="Patroni White",      type="dye", items=["clothing dye"],            image="dye_white",      cost=200, description=">As bright and pure as a Patronus!")

    $ dye_list=[
        brown_dye_ITEM, yellow_dye_ITEM, orange_dye_ITEM, red_dye_ITEM, crimson_dye_ITEM,
        green_dye_ITEM, dark_green_dye_ITEM, blue_dye_ITEM, dark_blue_dye_ITEM, purple_dye_ITEM,
        pink_dye_ITEM, gray_dye_ITEM, black_dye_ITEM, white_dye_ITEM,
        ]

    #Quest Items
    if not hasattr(renpy.store,'puzzle_box_ITEM'):
        $ puzzle_box_ITEM = item_class(id="puzzle_box",   name="Puzzle Box",  type="quest item", image="icon_puzzle", description=">Quest Item!")
    if not hasattr(renpy.store,'collar_quest_ITEM'):
        $ collar_quest_ITEM = item_class(id="collar_quest",   name="Collar",  type="quest item", image="icon_collar", description=">Quest Item!")


    #Hermione Outfits.
    if not hasattr(renpy.store,'hg_outfit_maid_ITEM'):
        $ hg_outfit_maid_ITEM      = costume_class(id="hg_outfit_maid", name="Maid",                 type="outfit", items=["outfit","hair","hat","gloves","garter","stockings"], cost=250, wait_time=2, image="outfits/hg_maid", description=">A classic Maids Outfit for a classy Witch.")
        $ hg_outfit_pirate_ITEM    = costume_class(id="hg_outfit_pirate", name="Pirate",             type="outfit", items=["outfit"],       cost=75, wait_time=1, image="outfits/hg_pirate", description="> A lightweight Pirates outfit with only room for the\n necessities. Comes with two canon ball storage compartments.")
        $ hg_outfit_christmas_ITEM = costume_class(id="hg_outfit_christmas", name="Christmas Girl",  type="outfit", items=["outfit"],       cost=50, wait_time=2, image="outfits/hg_christmas", description=">A christmas themed outfit complete with tightly wrapped\n snowglobes.")
        $ hg_outfit_present_ITEM   = costume_class(id="hg_outfit_present", name="Present",           type="outfit", items=["outfit"],       cost=35, wait_time=1, image="outfits/hg_present", description=">A tightly wrapped gift, scissors not included.")
        $ hg_outfit_japan_ITEM     = costume_class(id="hg_outfit_japan", name="Japanese Schoolgirl", type="outfit", items=["outfit"],       cost=125, wait_time=2, image="outfits/hg_japan", description=">A schoolgirl outfit traditionally worn in Japan.")
        $ hg_outfit_egypt_ITEM     = costume_class(id="hg_outfit_egypt", name="Egyptian Goddess",    type="outfit", image="outfits/hg_egypt", unlockable=True)
        $ hg_gamble_slut_ITEM      = costume_class(id="hg_gamble_slut", name="Poke Her Nips",        type="outfit_token", image="icon_gambler_hat", cost=14, wait_time=1, description=">An outfit that doesn't leave much for the mind's desire, perfect for a lewd card loving girl.")

    if not hasattr(renpy.store,'hg_witch_ITEM'):
        $ hg_witch_ITEM        = costume_class(id="hg_witch", name="Witch Outfit",      type="outfit", items=["outfit","hat"], cost=250, wait_time=3, image="outfits/hg_witch", description=">Release your inner witch with this halloween\n inspired outfit.")
        $ hg_witch_skimpy_ITEM = costume_class(id="hg_witch_skimpy", name="Sexy Witch", type="outfit", items=["outfit","hat"], unlockable=True,       image="outfits/hg_witch_skimpy")

    #Hermione Costumes.
    if not hasattr(renpy.store,'hg_costume_power_girl_ITEM'):
        $ hg_costume_power_girl_ITEM   = costume_class(id="hg_costume_power_girl", name="Power Girl",       type="outfit", items=["outfit"],                      cost=350, wait_time=3, image="outfits/hg_power", description=">An outfit for when you feel extra heroic\n \"Sometimes it takes balls to be a woman\".")
        $ hg_costume_ms_marvel_ITEM    = costume_class(id="hg_costume_ms_marvel", name="Mrs Marvel",        type="outfit", items=["outfit"],                      cost=250, wait_time=2, image="outfits/hg_marvel", description=">For the girl that likes the lightningbolt\n better on the chest than the forehead.")
        $ hg_costume_harley_quinn_ITEM = costume_class(id="hg_costume_harley_quinn", name="Harley Quinn",   type="outfit", items=["outfit"],                      cost=300, wait_time=3, image="outfits/hg_harley", description=">A outfit for when you're actually nuts\n rather than just crazy for them.")
        $ hg_costume_lara_croft_ITEM   = costume_class(id="hg_costume_lara_croft", name="Lara Croft",       type="outfit", items=["outfit","gloves"],             cost=270, wait_time=2, image="outfits/hg_lara", description=">An outfit perfectly suited for exploring deep, dark\n and moist caverns.")
        $ hg_costume_tifa_ITEM         = costume_class(id="hg_costume_tifa", name="Tifa",                   type="outfit", items=["outfit"],                      cost=220, wait_time=2, image="outfits/hg_tifa", description=">An outfit for when when your sexual fantasies\n are just getting started.")
        $ hg_costume_elizabeth_ITEM    = costume_class(id="hg_costume_elizabeth", name="Bioshock outfit",   type="outfit", items=["outfit","hair","choker"],      cost=400, wait_time=3, image="outfits/hg_bio", description=">Flick some coins for this Bioshock inspired outfit.")
        $ hg_costume_yennefer_ITEM     = costume_class(id="hg_costume_yennefer", name="Yennefer's costume", type="outfit", items=["outfit","choker","stockings"], cost=500, wait_time=3, image="outfits/hg_yenn", description=">A Witcher inspired outfit to fit even the most\n perverted witch")

    #Hermione Dresses.
    if not hasattr(renpy.store,'hg_dress_yule_ball_ITEM'):
        $ hg_dress_yule_ball_ITEM = costume_class(id="hg_dress_yule_ball", name="Ball Dress", type="outfit", items=["outfit","hair","neckless","tiara"], cost=1500, wait_time=7, image="outfits/hg_ball_dress", description=">A traditional ball dress complete with a imitation\n ball-queen tiara.")
        $ hg_dress_dancer_ITEM    = costume_class(id="hg_dress_dancer", name="Heart Dancer",  type="outfit", items=["outfit"],                           cost=80,   wait_time=1, image="outfits/hg_heart", description=">A sexy dancers outfit with heart shaped nipple tassels.")

    $ hermione_outfits_list=[
        hg_outfit_maid_ITEM, hg_outfit_pirate_ITEM, hg_outfit_christmas_ITEM, hg_outfit_present_ITEM,
        hg_outfit_japan_ITEM, hg_witch_ITEM, hg_witch_skimpy_ITEM, hg_outfit_egypt_ITEM,
        ]
    if hg_gamble_slut_ITEM.unlocked and hg_gamble_slut_ITEM not in hermione_outfits_list: # Updates image from shop icon to mannequin.
        $ hg_gamble_slut_ITEM.image = "outfits/hg_gambler_slut"
        $ hermione_outfits_list.append(hg_gamble_slut_ITEM)

    $ hermione_costumes_list = [
        hg_costume_power_girl_ITEM, hg_costume_ms_marvel_ITEM, hg_costume_harley_quinn_ITEM, hg_costume_lara_croft_ITEM,
        hg_costume_tifa_ITEM, hg_costume_elizabeth_ITEM, hg_costume_yennefer_ITEM,
        ]

    $ hermione_dresses_list = [
        hg_dress_dancer_ITEM, hg_dress_yule_ball_ITEM,
        ]

    # Clothing Sets
    if not hasattr(renpy.store,'hg_cheer_g_ITEM'):
        $ hg_cheer_g_ITEM      = costume_class(id="hg_cheer_g", name="Gryffindor Cheerleader",           type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_g",      cost=80, wait_time=2, description=">A basic Cheerleader attire for Gryffindor's\n  Quidditch team.")
        $ hg_cheer_s_ITEM      = costume_class(id="hg_cheer_s", name="Slythrin Cheerleader",             type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_s",      cost=80, wait_time=2, description=">The Slytherin version of the Cheerleader attire.")
        $ hg_cheer_r_ITEM      = costume_class(id="hg_cheer_r", name="Ravenclaw Cheerleader",            type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_r",      cost=80, wait_time=2, description=">The Ravenclaw version of the Cheerleader attire.")
        $ hg_cheer_h_ITEM      = costume_class(id="hg_cheer_h", name="Hufflepuff Cheerleader",           type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_h",      cost=80, wait_time=2, description=">The Hufflepuff version of the Cheerleader attire.")
        $ hg_cheer_g_sexy_ITEM = costume_class(id="hg_cheer_g_sexy", name="Sexy Gryffindor Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_g_sexy", unlockable=True)
        $ hg_cheer_s_sexy_ITEM = costume_class(id="hg_cheer_s_sexy", name="Sexy Slythrin Cheerleader",   type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_s_sexy", unlockable=True)
        $ hg_cheer_r_sexy_ITEM = costume_class(id="hg_cheer_r_sexy", name="Sexy Ravenclaw Cheerleader",  type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_r_sexy", unlockable=True)
        $ hg_cheer_h_sexy_ITEM = costume_class(id="hg_cheer_h_sexy", name="Sexy Hufflepuff Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_h_sexy", unlockable=True)

    # Lingerie
    if not hasattr(renpy.store,'hg_lingerie_lace_ITEM'):
        $ hg_lingerie_lace_ITEM    = item_class(id="hg_lingerie_lace", name="Lace Lingerie",       type="set", items=["bra","panties"],                                   image="outfits/hg_lingerie_lace",    cost=40,  wait_time=1, description=">A lovely lace bra and panty set.")
        $ hg_lingerie_silk_ITEM    = item_class(id="hg_lingerie_silk", name="Silk Lingerie",       type="set", items=["bra","panties","garter","stockings"],              image="outfits/hg_lingerie_silk",    cost=80,  wait_time=1, description=">A smooth and comfortable silk bra and panty set.")
        $ hg_lingerie_maid_ITEM    = item_class(id="hg_lingerie_maid", name="Maid Lingerie",       type="set", items=["bra","panties","gloves","stockings","hair","hat"], image="outfits/hg_lingerie_maid",    cost=160, wait_time=2, description=">A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts.")
        $ hg_lingerie_latex_ITEM   = item_class(id="hg_lingerie_latex", name="Latex Lingerie",     type="set", items=["bra","panties","gloves","stockings"],              image="outfits/hg_lingerie_latex",   cost=200, wait_time=2, description=">A tight and shiny lace bra and panty set.")
        $ hg_lingerie_fishnet_ITEM = item_class(id="hg_lingerie_fishnet", name="Fishnet Lingerie", type="set", items=["top","bra","panties"],                             image="outfits/hg_lingerie_fishnet", cost=100, wait_time=1, description=">A very revealing set for fishnet lingerie.")

    # One-pieces
    if not hasattr(renpy.store,'hg_nighty_silk_ITEM'):
        $ hg_nighty_silk_ITEM    = item_class(id="hg_nighty_silk", name="Silk Nighty",         type="set", items=["one-piece","panties"], cost=80,  wait_time=1, image="outfits/hg_nighty_silk",             description=">A comfortable yet elegant Nightwear set.")
        $ hg_nightgown_ITEM      = item_class(id="hg_nighty_silk", name="Silk Nightgown",      type="set", items=["one-piece"],           cost=80,  wait_time=1, image="outfits/hg_nightgown",               description=">A more free-flowing set of Nightwear.")
        $ hg_bikini_latex_ITEM   = item_class(id="hg_bikini_latex", name="Latex Bikini",       type="set", items=["bra","panties"],       cost=100, wait_time=1, image="outfits/hg_bikini_latex",            description=">A set for when you want to become one with your\n underwear")
        $ hg_bikini_sling_ITEM   = item_class(id="hg_bikini_sling", name="Sling Bikini",       type="set", items=["bra","panties"],       cost=69,  wait_time=1, image="outfits/hg_bikini_sling",            description=">Provides even less coverage than the Latex Bikini")
        $ hg_onepiece_sling_ITEM = item_class(id="hg_onepiece_sling", name="Sling Monokini",   type="set", items=["one-piece"],           cost=69,  wait_time=1, image="outfits/hg_onepiece_sling",          description=">A Mononoke variant of the Sling Bikini")
        $ hg_swimsuit_sport_ITEM = item_class(id="hg_swimsuit_sport", name="Sports Swimsuits", type="set", items=["one-piece"],           cost=69,  wait_time=1, image="outfits/hg_onepiece_swimsuit_sport", description=">Comes in 4 different variants. \nSwimmies not included!")

    # Wicked Clothing
    if not hasattr(renpy.store,'hg_punk_rocker_ITEM'):
        $ hg_punk_rocker_ITEM  = item_class(id="hg_punk_rocker", name="Punk Rocker",   type="set", items=["top","bottom","gloves","choker"], cost=180, wait_time=2, image="outfits/hg_punk_rocker", description=">A punk-rock set of clothes for the more rebellious\n type of witch.")
        $ hg_punk_leather_ITEM = item_class(id="hg_punk_leather", name="Punk Leather", type="set", items=["top","bottom","bra","stockings"], cost=300, wait_time=3, image="outfits/hg_punk_leather", description=">A punk-leather set for wicked witches!\n The sleeve-length of the Leather-jacket can be changed.")

    # Unlockable Clothing
    if not hasattr(renpy.store,'hg_accs_wool_g_ITEM'): # Not a store item!
        $ hg_accs_wool_g_ITEM      = item_class(id="hg_wool_accs_g", name="Gryffindor Wool Accessories",     type="set", items=["scarf","gloves","stockings"], image="outfits/hg_accs_wool_g", unlockable=True)
        $ hg_muggle_cold_ITEM      = item_class(id="hg_muggle_cold", name="Cold Weather Clothing",           type="set", items=["pullover","skirt","pantyhose"], image="outfits/hg_muggle_cold", unlockable=True)
        $ hg_muggle_cold_sexy_ITEM = item_class(id="hg_muggle_cold_sexy", name="Sexy Cold Weather Clothing", type="set", items=["pullover","skirt","pantyhose"], image="outfits/hg_muggle_cold_sexy", unlockable=True)
        $ hg_muggle_hot_ITEM       = item_class(id="hg_muggle_hot", name="Hot Weather Clothing",             type="set", items=["top","hot pants","stockings"], image="outfits/hg_muggle_hot", unlockable=True)
        $ hg_muggle_rainy_ITEM     = item_class(id="hg_muggle_rainy", name="Rainy Weather Clothing",         type="set", items=["sweater","long jeans"], image="outfits/hg_muggle_rainy", unlockable=True)

    $ hermione_clothing_sets_list=[
        hg_cheer_g_ITEM, hg_cheer_s_ITEM, hg_cheer_r_ITEM, hg_cheer_h_ITEM,
        hg_lingerie_lace_ITEM, hg_lingerie_silk_ITEM, hg_lingerie_maid_ITEM, hg_lingerie_latex_ITEM, hg_lingerie_fishnet_ITEM,
        hg_nighty_silk_ITEM, hg_nightgown_ITEM, hg_bikini_latex_ITEM, hg_bikini_sling_ITEM, hg_onepiece_sling_ITEM, hg_swimsuit_sport_ITEM,
        hg_punk_rocker_ITEM, hg_punk_leather_ITEM,
        ]

    $ hg_unlockable_clothing_sets_list=[
        hg_cheer_g_sexy_ITEM, hg_cheer_s_sexy_ITEM, hg_cheer_r_sexy_ITEM, hg_cheer_h_sexy_ITEM,
        hg_accs_wool_g_ITEM,
        hg_muggle_cold_ITEM, hg_muggle_cold_sexy_ITEM, hg_muggle_hot_ITEM, hg_muggle_rainy_ITEM,
        ]


    # Luna Outfits
    if not hasattr(renpy.store,'ll_pyjama_ITEM'):
        $ ll_pyjama_ITEM           = costume_class(id="ll_pyjama", name="Pyjama",          type="outfit", items=["outfit"],  cost=40, wait_time=1, image="outfits/ll_pyjama", description=">A quirky pyjama for a quirky girl.")
    if not hasattr(renpy.store,'ll_stewardess_ITEM'):
        $ ll_stewardess_ITEM       = costume_class(id="ll_stewardess",       name="Stewardess Outfit",         type="outfit", items=["outfit","hat","neckless","thong"], cost=80, wait_time=2, image="outfits/ll_stewardess", description=">For immediate access into the mile-high club!")
        $ ll_stewardess_short_ITEM = costume_class(id="ll_stewardess_short", name="Short Stewardess Outfit",   type="outfit", items=["outfit","hat","neckless","thong"], image="outfits/ll_stewardess_short",  unlockable=True)
    if not hasattr(renpy.store,'ll_dress_orange_ITEM'):
        $ ll_dress_orange_ITEM  = costume_class(id="ll_dress_orange", name="Ball Dress",   type="outfit", items=["outfit","earrings","stockings"],  cost=200, wait_time=3, image="outfits/ll_dress_orange", description=">A cute dress in a questionable color.")

    $ luna_outfits_list=[
        ll_pyjama_ITEM,
        ]
    $ luna_costumes_list=[
        ll_stewardess_ITEM,
        ll_stewardess_short_ITEM,
        ]
    $ luna_dresses_list=[
        ll_dress_orange_ITEM,
        ]

    # Luna Sets
    if not hasattr(renpy.store,'ll_cheer_r_ITEM'):
        $ ll_cheer_r_ITEM       = item_class(id="ll_cheer_r", name="Ravenclaw Cheerleader", type="set", items=["top","bottom","stockings"], cost=80, wait_time=2, image="outfits/ll_cheer_r", description=">The Ravenclaw version of the Cheerleader attire.")
        $ ll_lingerie_silk_ITEM = item_class(id="ll_lingerie_silk", name="Silk Lingerie",   type="set", items=["bra","panties"],            cost=80, wait_time=1, image="outfits/ll_lingerie_silk", description=">A smooth and comfortable silk bra and panty set.")
    if not hasattr(renpy.store,'ll_quirky_muggle_ITEM'):
        $ ll_quirky_muggle_ITEM = item_class(id="ll_quirky_muggle", name="Quirky Muggle", type="set", items=["top","bottom","stockings"], image="outfits/ll_muggle_1", unlockable=True)

    $ luna_clothing_sets_list=[
        ll_cheer_r_ITEM, ll_lingerie_silk_ITEM, ll_quirky_muggle_ITEM,
        ]


    # Astoria Outfits
    if not hasattr(renpy.store,'ag_boss_uniform_ITEM'):
        $ ag_boss_uniform_ITEM            = costume_class(id="ag_boss_uniform", name="Boss Uniform",                      type="outfit", items=["outfit","hair","hat"],       cost=500, wait_time=3, image="outfits/ag_boss_uniform", description=">A uniform I designed with an old friend of mine.\n Makes me wonder what happened to Hugo...")
        $ ag_costume_lazy_town_ITEM       = costume_class(id="ag_costume_lazy_town", name="Lazy Town Outfit",             type="outfit", items=["outfit","hair","bracelet"],  cost=120, wait_time=1, image="outfits/ag_lazy", description=">Nobody is lazy at Hogwarts!")
        $ ag_costume_lazy_town_short_ITEM = costume_class(id="ag_costume_lazy_town_short", name="Short Lazy Town Outfit", type="outfit", items=["outfit","hair","bracelet"],  image="outfits/ag_lazy_short", unlockable=True)
        $ ag_dress_yule_ball_ITEM         = costume_class(id="ag_dress_yule_ball", name="Ball Dress",                     type="outfit", items=["outfit"],                    cost=300, wait_time=4, image="outfits/ag_ball_dress", description=">A cute dress for your favourite princess!")

    $ astoria_outfits_list=[
        ag_boss_uniform_ITEM,
        ]
    $ astoria_costumes_list=[
        ag_costume_lazy_town_ITEM, ag_costume_lazy_town_short_ITEM,
        ]
    $ astoria_dresses_list=[
        ag_dress_yule_ball_ITEM,
        ]

    # Astoria Sets
    if not hasattr(renpy.store,'ag_lingerie_lace_ITEM'):
        $ ag_lingerie_lace_ITEM = item_class(id="ag_lingerie_lace", name="Lace Lingerie", type="set", items=["bra","panties"],                cost=80,  wait_time=1, image="outfits/ag_lingerie_lace", description=">A cute lace lingerie set.")
        $ ag_lingerie_lewd_ITEM = item_class(id="ag_lingerie_lewd", name="Lewd Lingerie", type="set", items=["bra","panties"],                cost=120, wait_time=1, image="outfits/ag_lingerie_lewd", description ="> A very rewealing lingerie set.")
        $ ag_nighty_silk_ITEM   = item_class(id="ag_nighty_silk", name="Silk Nighty",     type="set", items=["nighty","panties","stockings"], cost=140, wait_time=1, image="outfits/ag_nighty_silk", description=">+2 attack points while pillow-fighting!")

    $ astoria_clothing_sets_list=[
        ag_lingerie_lace_ITEM, ag_lingerie_lewd_ITEM, ag_nighty_silk_ITEM,
        ]


    # Susan Outfits
    $ susan_outfits_list=[
        ]
    $ susan_costumes_list=[
        ]
    $ susan_dresses_list=[
        ]

    # Susan Sets
    $ susan_clothing_sets_list=[
        ]


    # Cho Outfits
    if not hasattr(renpy.store,'cc_outfit_sailor_white_ITEM'):
        $ cc_outfit_quidditch_ITEM  = costume_class(id="cc_outfit_quidditch", name="Quidditch Outfit",   type="outfit", items=["outfit"], image="outfits/cc_quidditch", unlockable=True)
        $ cc_dress_red_ITEM         = costume_class(id="cc_dress_red", name="Traditional Dress in Red", type="outfit", items=["outfit"], cost=100, wait_time=3, image="outfits/cc_dress_red", description=">A traditional dress inspired by chinese culture.")
        $ cc_dress_silver_ITEM      = costume_class(id="cc_dress_silver", name="Traditional Dress in Silver", type="outfit", items=["outfit"], cost=100, wait_time=3, image="outfits/cc_dress_silver", description=">A traditional dress inspired by chinese culture.")
        $ cc_dress_black_ITEM       = costume_class(id="cc_dress_black", name="Traditional Dress in Black", type="outfit", items=["outfit"], cost=100, wait_time=3, image="outfits/cc_dress_black", description=">A traditional dress inspired by chinese culture.")

        $ cc_outfit_sailor_white_ITEM       = costume_class(id="cc_outfit_sailor_white", name="White Sailor Outfit", type="outfit", items=["outfit","top","skirt","thong","stockings","hat"], cost=240, wait_time=3, image="outfits/cc_sailor_white", description=">Slutty sailor outfit. Unlocks all items as separate\n and re-colourable items!")
        $ cc_outfit_sailor_black_ITEM       = costume_class(id="cc_outfit_sailor_black", name="Black Sailor Outfit", type="outfit", items=["outfit","top","skirt","thong","stockings","hat"], cost=240, wait_time=3, image="outfits/cc_sailor_black", description=">Slutty sailor outfit. Unlocks all items as separate\n and re-colourable items!")

    if not hasattr(renpy.store,'cc_costume_misty_ITEM'):
        $ cc_costume_misty_ITEM     = costume_class(id="cc_costume_misty", name="Misty Costume", type="outfit", items=["outfit","top","pants","suspenders"], cost=100, wait_time=2, image="outfits/cc_misty", description=">For trainers that want to be the very best!\n To train them is your cause!")

    $ cho_outfits_list=[
        cc_outfit_quidditch_ITEM, cc_outfit_sailor_white_ITEM
        ] #cc_outfit_sailor_black_ITEM
    $ cho_costumes_list=[
        cc_costume_misty_ITEM
        ]
    $ cho_dresses_list=[
        cc_dress_red_ITEM
        ] # cc_dress_silver_ITEM, cc_dress_black_ITEM

    # Cho Sets
    if not hasattr(renpy.store,'cc_muggle_hot_ITEM'):
        $ cc_muggle_hot_ITEM = item_class(id="cc_muggle_hot", name="Hot Weather Clothing", type="set", items=["top","pants","stockings"], image="outfits/cc_muggle_hot", unlockable=True)
        $ cc_party_slut_ITEM = item_class(id="cc_party", name="Party Clothing",            type="set", items=["bra","skirt"],             image="outfits/cc_party", unlockable=True)

    if not hasattr(renpy.store,'cc_lingerie_lace_ITEM'):
        $ cc_lingerie_lace_ITEM  = item_class(id="cc_lingerie_lace", name="Lace Lingerie", type="set", items=["bra","panties","garter","stockings","choker","earrings"], image="outfits/cc_lingerie_lace", cost=500, wait_time=5, description=">This lingerie set turns even the toughest tomboy\n into a cute and sexy princess!")
        $ cc_bikini_micro_ITEM   = item_class(id="cc_bikini_micro", name="Micro Bikini",   type="set", items=["bra","panties"],                                          image="outfits/cc_bikini_micro", cost=69, wait_time=1, description=">The regular size bikinis are out of stock...")

    $ cho_clothing_sets_list=[
        cc_muggle_hot_ITEM, cc_party_slut_ITEM, cc_lingerie_lace_ITEM, cc_bikini_micro_ITEM,
        ]

    ###Outfit linked to old outfits###
    $ outfit_linking = {}

    #outfit_linking[cc_outfit_quidditch_ITEM.id] = cho_outfit_quidditch
    $ outfit_linking[cc_party_slut_ITEM.id] = cho_outfit_party
    $ outfit_linking[cc_muggle_hot_ITEM.id] = cho_outfit_trainee
    $ outfit_linking[cc_outfit_sailor_white_ITEM.id] = cho_outfit_sailor
    $ outfit_linking[cc_costume_misty_ITEM.id] = cho_outfit_misty
    $ outfit_linking[cc_bikini_micro_ITEM.id] = cho_outfit_bikini
    $ outfit_linking[cc_lingerie_lace_ITEM.id] = cho_outfit_lacelingerie
    $ outfit_linking[cc_dress_red_ITEM.id] = cho_outfit_dress1

    #Tonks Outfits
    $ tonks_outfits_list=[
        ]
    $ tonks_costumes_list=[
        ]
    $ tonks_dresses_list=[
        ]

    ### Outfit Class Update ###

    #Add the outfit layers from your (above) outfit item in 'update_outfit_layers'
    #Those layers update on every game start.

    call update_outfit_layers

    return





### Item Classes ###

init -2 python:

    #Items Main
    class item_class(object):
        id = ""
        name = ""
        type = ""
        items = []
        image = ""
        imagepath = "interface/icons/box_blue_2.png"
        unlockable = False #If True, prevents this item to be shown in the shop.
        unlocked = False #Set to True once unlocked or purchased.
        number = 0 #Amount of items of this type that you possess. Can be used for weasley store and gift items.
        cost = 0
        wait_time = 1
        description = ""

        #Used in decorations
        active = False # Check if decoration is used or not

        #Used in decorations
        active = False # Check if decoration is used or not

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_name(self):
            return self.name

        def get_image(self):
            if self.image != "":
                self.imagepath = "interface/icons/"+str(self.image)+".png"
                return self.imagepath
            else:
                return self.imagepath

        # Need to simplify this
        def get_cost(self):
            if self.type == "poster" or self.type == "trophy" or self.type == "outfit_token":
                if self.cost == 1:
                    return ""+str(self.cost)+" token"
                else:
                    return ""+str(self.cost)+" tokens"
            else:
                return ""+str(self.cost)+" gold"

        def get_wait_time(self):
            if self.wait_time == 1:
                return "Wait Time: "+str(self.wait_time)+" day."
            else:
                return "Wait Time: "+str(self.wait_time)+" days."

        def get_items(self):
            return self.items
        def get_type(self):
            return self.type
        def get_description(self):
            return self.description
        def get_buttom_right(self):
            return ""

    #Outfit Items
    class costume_class(item_class):
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"

        def getOutfitLayers(self):
            return self.outfit_layers
        def getHairLayers(self):
            return self.hair_layer
        def getTopLayers(self):
            return self.top_layers
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]

    #Book Items
    class silver_book_lib(object):
        read_books = []
        write_books = []
        fiction_books = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_all(self):
            all_books = []
            all_books.extend(self.read_books)
            all_books.extend(self.write_books)
            all_books.extend(self.fiction_books)
            return all_books
        def get_edu(self):
            edu_books = []
            edu_books.extend(self.read_books)
            edu_books.extend(self.write_books)
            return edu_books
        def get_fic(self):
            return self.fiction_books

        def isDone(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    return book.done
            return None

    class book_class(item_class):
        chapters = 0
        progress = 0
        done = False
        effect = ""

        def __repr__(self):
            return self.id
        def getMenuText(self):
            return "-"+str(self.name)+"-"
        def getMenuTextDone(self):
            return "-"+str(self.name)+"-{image=check_08}"

        def get_description(self):
            out_des = ""
            if len(self.description) > 90:
                out_des = self.description[0:90] + "..."
            else:
                out_des = self.description
            return out_des

    class educational_book(book_class):
        pass

    class fiction_book(book_class):
        chapter_description = []
        def getChapterDesc(self):
           return self.chapter_description[self.progress-1] #"Chapter "+str(self.progress)+": "+

    #Scroll Items
    class scroll_class(item_class):
        scroll_image = ""
        comments = []

        def get_comment(self):
            return self.comments[renpy.random.randint(0, len(self.comments)-1)]
