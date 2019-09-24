

# Quest Items
default puzzle_box_ITEM   = item_class(id="puzzle_box", name="Puzzle Box", type="quest item", image="icon_puzzle", description="A wooden box with a slide puzzle located on top of it. It was found hidden behind one of the loose bricks in the fireplace. Who knows what's inside.", event="start_slide_puzzle")
default collar_quest_ITEM = item_class(id="collar_quest", name="Collar", type="quest item", image="icon_collar", description="Quest Item!")
default lootbox_quest_ITEM = item_class(id="lootbox", name="Pack of cards", type="quest item", image="cards", description="A pack of cards.", cost=100, event="card_lootbox")
default sealed_scroll_ITEM = scroll_class(id="sealed_scroll", name="Forbidden Scroll", cost=300, type="scroll", image="item_scroll_sealed", description="The recipe for a powerful and forbidden potion that transforms you into any magical creature you desire.", event="examine_sealed_scroll")

default forbidden_scroll_list = [sealed_scroll_ITEM]

# Gift items
default lollipop_ITEM          = item_class(id="lollipop", name="Lollipop Candy",              cost=20, type="candy", image="item_lollipop", description="A lollipop candy. An adult candy for kids or kids candy for adults?")
default chocolate_ITEM         = item_class(id="chocolate", name="Chocolate",                  cost=40, type="candy", image="item_chocolate", description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
default plush_owl_ITEM         = item_class(id="plush_owl", name="Plush owl",                  cost=35, type="toy", image="item_plush_owl", description="A Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
default butterbeer_ITEM        = item_class(id="butterbeer", name="Butterbeer",                cost=50, type="drink", image="item_butterbeer", description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
default science_mag_ITEM       = item_class(id="science_mag", name="Educational Magazines",    cost=30, type="mag", image="item_mag_science", description="Educational magazines. \nthe Trusty companions of every social outcast.")
default girls_mag_ITEM         = item_class(id="girls_mag", name="Girly Magazines",            cost=45, type="mag", image="item_mag_girls", description="Girly magazines. \nAll cool girls are reading these.")
default adult_mag_ITEM         = item_class(id="adult_mag", name="Adult magazines",            cost=60, type="mag", image="item_mag_adult", description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
default porn_mag_ITEM          = item_class(id="porn_mag", name="Porn magazines",              cost=80, type="mag", image="item_mag_porn", description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
default krum_poster_ITEM       = item_class(id="krum_poster", name="Viktor Krum Poster",       cost=25, type="mag", image="item_krum_poster", description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
default sexy_lingerie_ITEM     = item_class(id="sexy_lingerie", name="Sexy Lingerie",          cost=75, type="", image="item_sexy_lingerie", description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
default sexy_stockings_ITEM    = item_class(id="sexy_stockings", name="Sexy Stockings",        cost=50, type="", image="item_sexy_stockings", description="")
default pink_condoms_ITEM      = item_class(id="pink_condoms", name="A Pack Of Condoms",       cost=50, type="toy", image="item_condoms_pink", description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
default vibrator_ITEM          = item_class(id="vibrator", name="Vibrator",                    cost=55, type="toy", image="item_vibrator", description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
default anal_lube_ITEM         = item_class(id="anal_lube", name="Jar of anal lubricant",      cost=60, type="toy", image="item_anal_lube", description="A Jar of anal lube, Buy this for your loved one - show that you care.")
default ballgag_and_cuffs_ITEM = item_class(id="ballgag_and_cuffs", name="Ball gag and cuffs", cost=70, type="toy", image="item_ballgag_and_cuffs", description="Ball gag and cuffs, Turn your soulmate into your cellmate.")
default anal_plugs_ITEM        = item_class(id="anal_plugs", name="Anal plugs",                cost=85, type="toy", image="item_anal_plugs", description="Anal plugs decorated with actual tails. Sizes vary to satisfy expert practitioners and beginner alike.")
default testral_strapon_ITEM   = item_class(id="testral_strapon", name="Thestral Strap-on",    cost=200,type="toy", image="item_strap_on_testral", description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")
default broom_2000_ITEM        = item_class(id="broom_2000", name="Lady Speed Stick-2000",     cost=500,type="toy", image="item_broom", description="The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")
default sexdoll_ITEM           = item_class(id="sexdoll", name="Sex doll \"Joanne\"",          cost=350,type="toy", image="item_sexdoll", description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
default anal_beads_ITEM        = item_class(id="anal_beads", name="Anal beads",                cost=65, type="toy", image="item_anal_beads", description="Anal beads engraved with a strange inscription \"Property of L.C.\".")

default wine_ITEM       = item_class(id="wine", name="Wine",             cost=60, type="drink", image="item_wine", description="Add description. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
default firewhisky_ITEM = item_class(id="firewhisky", name="firewhisky", cost=80, type="drink", image="item_whisky", description="Add description. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")

default candy_gift_list = [
    lollipop_ITEM,
    chocolate_ITEM,
]
default drink_gift_list = [
    butterbeer_ITEM,
    wine_ITEM,
    firewhisky_ITEM
]
default mag_gift_list = [
    krum_poster_ITEM,
    science_mag_ITEM,
    girls_mag_ITEM,
    adult_mag_ITEM,
    porn_mag_ITEM,
]
default toy_gift_list = [
    plush_owl_ITEM,
    pink_condoms_ITEM,
    sexy_lingerie_ITEM,
    vibrator_ITEM,
    anal_lube_ITEM,
    ballgag_and_cuffs_ITEM,
    anal_plugs_ITEM,
    testral_strapon_ITEM,
    broom_2000_ITEM,
    sexdoll_ITEM,
    anal_beads_ITEM,
]

# Posters
default poster_agrabah_ITEM = item_class(id="agrabah", name="Agrabah Poster", cost=2, type="poster", image="posters/agrabah", description="A remnant of a distant land and memories about different times. A reminder for when you just want to ponder about what could've been.")
default poster_gryffindor_ITEM = item_class(id="gryffindor", name="Gryffindor Poster", cost=2, type="poster", image="posters/gryffindor", description="Make your stance that you support the house of Gryffindor with this themed poster.")
default poster_hufflepuff_ITEM = item_class(id="hufflepuff", name="Hufflepuff Poster", cost=2, type="poster", image="posters/hufflepuff", description="Make your stance that you support the house of Hufflepuff with this themed poster.")
default poster_ravenclaw_ITEM = item_class(id="ravenclaw", name="Ravenclaw Poster", cost=2, type="poster", image="posters/ravenclaw", description="Make your stance that you support the house of Ravenclaw with this themed poster.")
default poster_slytherin_ITEM = item_class(id="slytherin", name="Slytherin Poster", cost=2, type="poster", image="posters/slytherin", description="Make your stance that you support the house of Slytherin with this themed poster.")
default poster_hermione_ITEM = item_class(id="hermione", name="Hermione Chibi Poster", cost=2, type="poster", image="posters/hermione", description="A little lewdness for the office, don't worry. With a special illusion charm no one but you will notice a thing....")
default poster_harlots_ITEM = item_class(id="harlots", name="Hogwarts Harlots Poster", cost=2, type="poster", image="posters/harlots", description="Hermione showing off her true colours at last with this special poster... illusion charm included...")
default poster_stripper_ITEM = item_class(id="stripper", name="Stripper Poster", cost=2, type="poster", image="posters/stripper", description="Hermione showing off how to work the pole... illusion charm included...")
default poster_wanted_ITEM = item_class(id="wanted", name="Wanted Poster", cost=2, type="poster", image="posters/wanted", description="A Wild West styled Wanted poster depicting our dear headmaster...")
default poster_tonks_ITEM = item_class(id="tonks", name="Tonks Chibi Poster", hidden=True, cost=2, type="poster", image="posters/tonks", description="Somebody anonymous sent us this poster of what we can only suspect is Professor Tonks in the nude!")

# Trophies
default trophy_stag_ITEM = item_class(id="stag", name="Stag Head Trophy", cost=3, type="trophy", image="trophies/stag", description="A perfect decoration over your mantelpiece to add a sense of masculinity to the office.")
default trophy_crest_ITEM = item_class(id="crest", name="Hogwarts Crest", cost=5, type="trophy", image="trophies/crest", description="A perfect decoration for a headmaster.")

# Pinups & Misc
default pinup_girl_ITEM = item_class(id="_deco_1", name="Girl Pinup", cost=0, type="pinup", image="pinups/girl", description="Spice up your cupboard with this sexy pinup model...\n(Shows up when rumaging through the cupboard).", unlocked=True)

# Hats
default owl_hat_ITEM = item_class(id="owl_hat", name="Owl Hat", cost=1, type="owl", imagepath="interface/icons/misc/owl_hat.png", description="A hat for an owl. Don't ask, just accept it..")
default phoenix_hat_ITEM = item_class(id="phoenix_hat", name="Phoenix Hat", cost=1, type="phoenix", imagepath="interface/icons/misc/phoenix_hat.png", description="A little something to make your friend look less depressed.")
default fireplace_hat_ITEM = item_class(id="fireplace_hat", name="Skull Hat", cost=1, type="fireplace", imagepath="interface/icons/misc/fireplace_hat.png", description="Don't let Johnny get a cold!")

default owl_black_ITEM = item_class(id="owl_idle_black", name="Black Owl", cost=3, type="mail", imagepath="interface/icons/misc/owl_black.png", description="Magically dye your mail courier black!")

default wall_deco_list = [
    poster_agrabah_ITEM,
    poster_gryffindor_ITEM,
    poster_hufflepuff_ITEM,
    poster_ravenclaw_ITEM,
    poster_slytherin_ITEM,
    poster_hermione_ITEM,
    poster_harlots_ITEM,
    poster_stripper_ITEM,
    poster_wanted_ITEM,
    poster_tonks_ITEM,
]
default fireplace_deco_list = [
    trophy_crest_ITEM,
    trophy_stag_ITEM,
]
default cupboard_deco_list = [
    pinup_girl_ITEM
]
default misc_deco_list = [
    owl_black_ITEM
]
default misc_hat_list = [
    fireplace_hat_ITEM,
    phoenix_hat_ITEM,
    owl_hat_ITEM,
]

# Scroll Items
default scroll_1_ITEM = scroll_class(id="scroll_1",   name="The room",           cost=1,   type="scroll", image="item_scroll", scroll_image="1", comments=["This is a first ever draft of the Dumbledore's office.","Not a very exciting thing to look at, sure. But holds great historical value."])
default scroll_2_ITEM = scroll_class(id="scroll_2",   name="The calendar",       cost=2,   type="scroll", image="item_scroll", scroll_image="2", comments=["The calendar...","On the early stages of development I toyed with an idea of implementing an actual in-game calendar into the gameplay...","I soon realised how much more difficult it would be to create a game like that...","And since I personally believe that any time limits in any game always work against the fun factor I decided to abandon the idea...","Later on I used this drawing as a parchment paper for letters to be written on..."])
default scroll_3_ITEM = scroll_class(id="scroll_3",   name="The girl",           cost=10,  type="scroll", image="item_scroll", scroll_image="3", comments=["A couple of very early drawings of Hermione..."])
default scroll_4_ITEM = scroll_class(id="scroll_4",   name="Deepthroating",      cost=60,  type="scroll", image="item_scroll", scroll_image="4", comments=["The deepthroating scene...","My first attempt.","Been deemed unworthy and ended up here."])
default scroll_5_ITEM = scroll_class(id="scroll_5",   name="Poster 01",          cost=50,  type="scroll", image="item_scroll", scroll_image="5", comments=["The game poster...","Hermione is Dahr's work. The rest is me..."])
default scroll_6_ITEM = scroll_class(id="scroll_6",   name="Poster 02",          cost=50,  type="scroll", image="item_scroll", scroll_image="6", comments=["Alternative game poster.","This one has never been released."])
default scroll_7_ITEM = scroll_class(id="scroll_7",   name="Chibi-dancing",      cost=20,  type="scroll", image="item_scroll", scroll_image="7", comments=["Some chibi closeups.","The one on the left never made it into the final game..."])
default scroll_8_ITEM = scroll_class(id="scroll_8",   name="Game items",         cost=10,  type="scroll", image="item_scroll", scroll_image="8", comments=["A banch of items that I ended up not using...","I blame dahr and his awesome artwork."])
default scroll_9_ITEM = scroll_class(id="scroll_9",   name="Panties no panties", cost=50,  type="scroll", image="item_scroll", scroll_image="9", comments=["The drawing of Hermione from the poster. (by Dahr)","I like one on the right with her panties still on."])
default scroll_10_ITEM = scroll_class(id="scroll_10", name="A lot of pegs",      cost=50,  type="scroll", image="item_scroll", scroll_image="10", comments=["Another ithing that never made it into the final game...","The idea here was that the more you level up Hermione the more pegs she would let you to put on her...","And the nipple chain was supposed to be worn to class under the uniform."])
default scroll_11_ITEM = scroll_class(id="scroll_11", name="House-elf brothel",  cost=80,  type="scroll", image="item_scroll", scroll_image="11", comments=["The house-elf brothel... Just another thing that never happened."])
default scroll_12_ITEM = scroll_class(id="scroll_12", name="Me and Lola",        cost=10,  type="scroll", image="item_scroll", scroll_image="12", comments=["A drawing featuring yours truly as a Durmstrung mage and Lola as a student...","The drawing itself is by Dahr of course."])
default scroll_13_ITEM = scroll_class(id="scroll_13", name="Hard training",      cost=80,  type="scroll", image="item_scroll", scroll_image="13", comments=["Another one of those side-quests that never happened...","This one was about--","No, I better not. Who knows, maybe we will get to adding those quests eventually."])
default scroll_14_ITEM = scroll_class(id="scroll_14", name="Wizard's Chess",     cost=50,  type="scroll", image="item_scroll", scroll_image="14", comments=["Another sub-quest...","This one involving the school's wizard chess club."])
default scroll_15_ITEM = scroll_class(id="scroll_15", name="Tutoring books",     cost=10,  type="scroll", image="item_scroll", scroll_image="15", comments=["There is more then one way for a pretty girl to carry her books around.","I thought it would be cool to change the way Hermione carries the books as she progresses with her training.","Since the whole tutoring arc got canceled I am showing it here..."])

default scroll_16_ITEM = scroll_class(id="scroll_16", name="Extra gifts 01",     cost=10,  type="scroll", image="item_scroll", scroll_image="16", comments=["A couple of items that didn't make it into the final game...","The one on the left is an actual live house-elf to give as a present.","The one on the right is a portrait of a pervy but wise wizard. Supposed to be helping with studying..."])
default scroll_17_ITEM = scroll_class(id="scroll_17", name="Extra gifts 02",     cost=10,  type="scroll", image="item_scroll", scroll_image="17", comments=["Few more items...","A newspaper, a bottle of perfume and a magical hat that says things you want to hear..."])
default scroll_18_ITEM = scroll_class(id="scroll_18", name="Fiction books",      cost=10,  type="scroll", image="item_scroll", scroll_image="18", comments=["The fiction books...","The top row are my sketches, the bottom row are finalised drawings by dahr."])
default scroll_19_ITEM = scroll_class(id="scroll_19", name="Singer whore",       cost=60,  type="scroll", image="item_scroll", scroll_image="19", comments=["A drawing of a famous singer.","Has no connection to this game and is here for no reason whatsoever."])
default scroll_20_ITEM = scroll_class(id="scroll_20", name="Casting",            cost=60,  type="scroll", image="item_scroll", scroll_image="20", comments=["It took me a while to come up with a proper look for Hermione...","Version \"A\" was my first attempt. And I liked it up until the moment when I started to hate it...","Version \"B\" was my second attempt. And it's good. But her confident and semi-aggressive facial features didn't fit the character well...","Version \"C\" is the one that got the role. The Hermione that we all grew to care for by now, I'm sure."])
default scroll_21_ITEM = scroll_class(id="scroll_21", name="Witch robe 01",      cost=20,  type="scroll", image="item_scroll", scroll_image="21", comments=["Sub-quests that never happened.","You are allowed to feel bad for rushing me.","If you did not rush me you are allowed to feel angry at people who did."])
default scroll_22_ITEM = scroll_class(id="scroll_22", name="Witch robe 02",      cost=20,  type="scroll", image="item_scroll", scroll_image="22", comments=["Hermione presenting her body to Genie...","This would have been a quite memorable scene..."])
default scroll_23_ITEM = scroll_class(id="scroll_23", name="Witch robe 03",      cost=20,  type="scroll", image="item_scroll", scroll_image="23", comments=["Didn't expect this one, did you?","In case you're wondering this is still Hermione."])
default scroll_24_ITEM = scroll_class(id="scroll_24", name="Witch robe 04",      cost=20,  type="scroll", image="item_scroll", scroll_image="24", comments=[".................................","Sub-quests of course..."])
default scroll_25_ITEM = scroll_class(id="scroll_25", name="The walk",           cost=80,  type="scroll", image="item_scroll", scroll_image="25", comments=["Another sub-quest...","We had a rather lengthy discussion with Dahr about this one...","I was sort of against it, but then Dahr sent me this picture and it made me shut up."])
default scroll_26_ITEM = scroll_class(id="scroll_26", name="Durmstrang",         cost=80,  type="scroll", image="item_scroll", scroll_image="26", comments=["One the very early stages of development I had an idea of representing outcomes of your failed or successfully completed sub quests with a simplistic plates, or photographs...","At first many of the sub-quests involved deciding on how to spend the Hogwarts budget...","Spend your money to finance the school quiddich team, or to hire new teachers and such..."])
default scroll_27_ITEM = scroll_class(id="scroll_27", name="Gag ball",           cost=80,  type="scroll", image="item_scroll", scroll_image="27", comments=["Isn't she adorable?"])
default scroll_28_ITEM = scroll_class(id="scroll_28", name="New clothes 01",     cost=50,  type="scroll", image="item_scroll", scroll_image="28", comments=["Another (rather lengthy) sub-quest..."])
default scroll_29_ITEM = scroll_class(id="scroll_29", name="New clothes 02",     cost=50,  type="scroll", image="item_scroll", scroll_image="29", comments=[".........."])
default scroll_30_ITEM = scroll_class(id="scroll_30", name="The gang",           cost=10,  type="scroll", image="item_scroll", scroll_image="30", comments=["One of the very early sketches related to the quiddich sub-quests..."])

default scroll_31_ITEM = scroll_class(id="scroll_31", name="Silver",           cost=10,  type="scroll", image="item_scroll_silver", scroll_image="31", comments=[""])
default scroll_32_ITEM = scroll_class(id="scroll_32", name="New characters!",   cost=50,  type="scroll", image="item_scroll_silver", scroll_image="32", comments=["More and more characters got added along the way..."])
default scroll_33_ITEM = scroll_class(id="scroll_33", name="Lion, Witch, & Wardrobe 1",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="33", comments=["The very first wardrobe that got added to silver."])
default scroll_34_ITEM = scroll_class(id="scroll_34", name="Lion, Witch, & Wardrobe 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="34", comments=["The second one already had almost all features from the current one, but didn't look that great..."])
default scroll_35_ITEM = scroll_class(id="scroll_35", name="Lion, Witch, & Wardrobe 3",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="35", comments=["The wardrobe got a brand new design, with tons of new features!","Every other girl available in silver has one too!"])

default scroll_37_ITEM = scroll_class(id="scroll_37", name="Map 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="37", comments=["First try at the new map.","We removed all the text and labels and replaced them with icons."])

default scroll_list_A = [
    scroll_1_ITEM, scroll_2_ITEM,
    scroll_3_ITEM, scroll_4_ITEM,
    scroll_5_ITEM, scroll_6_ITEM,
    scroll_7_ITEM, scroll_8_ITEM,
    scroll_9_ITEM, scroll_10_ITEM,
    scroll_11_ITEM, scroll_12_ITEM,
    scroll_13_ITEM ,scroll_14_ITEM,
    scroll_15_ITEM,
]
default scroll_list_B = [
    scroll_16_ITEM, scroll_17_ITEM,
    scroll_18_ITEM, scroll_19_ITEM,
    scroll_20_ITEM, scroll_21_ITEM,
    scroll_22_ITEM, scroll_23_ITEM,
    scroll_24_ITEM, scroll_25_ITEM,
    scroll_26_ITEM, scroll_27_ITEM,
    scroll_28_ITEM, scroll_29_ITEM,
    scroll_30_ITEM,
]
default scroll_list_C = [
    scroll_31_ITEM, scroll_32_ITEM,
    scroll_33_ITEM, scroll_34_ITEM,
    scroll_35_ITEM, scroll_37_ITEM,
]

# Badges
default spew_badge_ITEM      = item_class(id="spew_badge", name="S.P.E.W. Badge",       type="accessory", items=["badge"],       image="badge_spew",        cost=5,  description=">A badge designed to show one's opposition of elf\n slavery.")
default cum_badge_ITEM       = item_class(id="cum_badge", name="I <3 C.U.M. Badge",     type="accessory", items=["badge"],       image="badge_cum",  cost=15, description=">A badge that displays ones affection towards semen.")
default cat_ears_ITEM        = item_class(id="cat_ears", name="Cat Ears",               type="accessory", items=["ears","tail"], image="ears_cat",          cost=40, description=">A fluffy set of catlike ears that matches one's\n hair-color!")
default elf_ears_ITEM        = item_class(id="elf_ears", name="Elf Ears",               type="accessory", items=["ears"],        image="ears_elf",          cost=20, description=">A pointy set of elven ears.")
default reading_glasses_ITEM = item_class(id="reading_glasses", name="Reading Glasses", type="accessory", items=["glasses"],     image="glasses_reading",   cost=50, description=">A lot of wizards are into girls wearing these!")
default vintage_glasses_ITEM = item_class(id="vintage_glasses", name="Vintage Glasses", type="accessory", items=["glasses"],     image="glasses_vintage",   cost=70, description=">Wearing these doesn't automatically make you a nerd!")

default accs_list=[
    spew_badge_ITEM,
    cum_badge_ITEM,
    cat_ears_ITEM,
    elf_ears_ITEM,
    reading_glasses_ITEM,
    vintage_glasses_ITEM
]

# Makeup
default lipstick_red_ITEM    = item_class(id="lipstick_red", name="Red Lipstick",   type="makeup", items=["lipstick"], image="lipstick_red",    cost=100, description=">They call this one the red rocket!")
default lipstick_pink_ITEM   = item_class(id="lipstick_pink", name="Pink Lipstick", type="makeup", items=["lipstick"], image="lipstick_pink",   unlockable=True)
default freckles_makeup_ITEM = item_class(id="freckles_makeup", name="Freckles",    type="makeup", items=["freckles"], image="makeup_freckles", cost=20,  description=">A magical item that makes the wearer's freckles more\n pronounced!")
default fake_cum_makeup_ITEM = item_class(id="fake_cum_makeup", name="Fake Cum",    type="makeup", items=["fake cum"], image="makeup_fake_cum", cost=20,  description=">When she doen't want to wear your real cum just yet.\n Be patient!")

default misc_list=[
    lipstick_red_ITEM,
    lipstick_pink_ITEM,
    freckles_makeup_ITEM,
    fake_cum_makeup_ITEM,
]

# Dyes
default brown_dye_ITEM      = item_class(id="brown_dye", name="Mud-Blood Brown",    type="dye", items=["clothing dye","hair dye"], image="dye_brown",      cost=20,  description=">Basic shade of brown. Simple yet elegant!")
default yellow_dye_ITEM     = item_class(id="yellow_dye", name="Niffler's Gold",    type="dye", items=["clothing dye","hair dye"], image="dye_yellow",     cost=40,  description=">A very nice shade of yellow.")
default orange_dye_ITEM     = item_class(id="orange_dye", name="Butter Beer",       type="dye", items=["clothing dye"],            image="dye_orange",     cost=60,  description=">A very nice shade of orange.")
default red_dye_ITEM        = item_class(id="red_dye", name="Weasel Red",           type="dye", items=["clothing dye","hair dye"], image="dye_red",        cost=60,  description=">A very nice shade of red.")
default crimson_dye_ITEM    = item_class(id="crimson_dye", name="Crimson Lion",     type="dye", items=["clothing dye","hair dye"], image="dye_crimson",    cost=80,  description=">A very rich shade of red.")
default green_dye_ITEM      = item_class(id="green_dye", name="Bowtruckle Paint",   type="dye", items=["clothing dye"],            image="dye_green",      cost=60,  description=">A bright shade of green.")
default dark_green_dye_ITEM = item_class(id="dark_green_dye", name="Serpent Green", type="dye", items=["clothing dye","hair dye"], image="dye_dark_green", cost=80,  description=">A darker shade of green.")
default blue_dye_ITEM       = item_class(id="blue_dye", name="Pixie Dye",           type="dye", items=["clothing dye"],            image="dye_blue",       cost=60,  description=">A bright shade of blue.")
default dark_blue_dye_ITEM  = item_class(id="dark_blue_dye", name="Raven Blue",     type="dye", items=["clothing dye","hair dye"], image="dye_dark_blue",  cost=80,  description=">A darker shade of blue.")
default purple_dye_ITEM     = item_class(id="purple_dye", name="Pygmy Puff Purple", type="dye", items=["clothing dye","hair dye"], image="dye_purple",     cost=100, description=">A very nice shade of purple.")
default pink_dye_ITEM       = item_class(id="pink_dye", name="Pussy Pink",          type="dye", items=["clothing dye","hair dye"], image="dye_pink",       cost=120, description=">A color so pink, it makes you want to cover your\n whole room with it!")
default gray_dye_ITEM       = item_class(id="gray_dye", name="Ghostly Gray",        type="dye", items=["clothing dye","hair dye"], image="dye_gray",       cost=120, description=">A very classy shade of gray.")
default black_dye_ITEM      = item_class(id="black_dye", name="Seriously Black",    type="dye", items=["clothing dye","hair dye"], image="dye_black",      cost=200, description=">As black as a Testral.")
default white_dye_ITEM      = item_class(id="white_dye", name="Patroni White",      type="dye", items=["clothing dye"],            image="dye_white",      cost=200, description=">As bright and pure as a Patronus!")

default dye_list=[
    brown_dye_ITEM,
    yellow_dye_ITEM,
    orange_dye_ITEM,
    red_dye_ITEM,
    crimson_dye_ITEM,
    green_dye_ITEM,
    dark_green_dye_ITEM,
    blue_dye_ITEM,
    dark_blue_dye_ITEM,
    purple_dye_ITEM,
    pink_dye_ITEM,
    gray_dye_ITEM,
    black_dye_ITEM,
    white_dye_ITEM,
]

# Hermione Outfits
default hg_outfit_maid_ITEM = costume_class(
    id = "hg_outfit_maid", name = "Maid", type = "outfit", items = ["outfit","hair","hat","gloves","garter","stockings"],
    cost = 250, wait_time=2, image = "outfits/hg_maid", description = ">A classic Maids Outfit for a classy Witch.",
    # Layers
    outfit_layers = ["stockings/stockings_lace", "bottoms/costume/skirt_maid", "tops/costume/top_maid","gloves/gloves_maid"],
    breast_layer = "breasts_normal_pressed",
    hair_layer = "updo",
    top_layers = "hat_maid"
)
default hg_outfit_pirate_ITEM = costume_class(
    id = "hg_outfit_pirate", name = "Pirate", type = "outfit", items = ["outfit"],
    cost = 75, wait_time = 1, image = "outfits/hg_pirate", description = "> A lightweight Pirates outfit with only room for the\n necessities. Comes with two canon ball storage compartments.",
    # Layers
    outfit_layers = ["stockings/stockings_pirate","bottoms/costume/pants_pirate","tops/costume/top_pirate"],
    breast_layer = "breasts_nipfix"
)
default hg_outfit_christmas_ITEM = costume_class(
    id = "hg_outfit_christmas", name = "Christmas Girl", type = "outfit", items = ["outfit"],
    cost = 50, wait_time = 2, image = "outfits/hg_christmas", description = ">A christmas themed outfit complete with tightly wrapped\n snowglobes.",
    # Layers
    outfit_layers = ["bottoms/costume/skirt_xmas_1","tops/costume/top_xmas_1","gloves/gloves_wool_1","neckwear/collar_xmas"],
    breast_layer  = "breasts_normal_pressed",
    top_layers    = "antlers"
)
default hg_outfit_present_ITEM = costume_class(
    id = "hg_outfit_present", name = "Present", type = "outfit", items = ["outfit"],
    cost = 35, wait_time = 1, image = "outfits/hg_present", description = ">A tightly wrapped gift, scissors not included.",
    # Layers
    outfit_layers = ["bottoms/costume/skirt_xmas_2","tops/costume/top_xmas_2"],
    breast_layer  = "breasts_nipfix"
)
default hg_outfit_japan_ITEM = costume_class(
    id = "hg_outfit_japan", name = "Japanese Schoolgirl", type = "outfit", items = ["outfit"],
    cost = 125, wait_time = 2, image = "outfits/hg_japan", description = ">A schoolgirl outfit traditionally worn in Japan.",
    # Layers
    outfit_layers = ["bottoms/costume/skirt_japan","tops/costume/top_japan"],
    breast_layer  = "breasts_normal_pressed"
)
default hg_outfit_egypt_ITEM = costume_class(
    id = "hg_outfit_egypt", name = "Egyptian Goddess", type = "outfit", image = "outfits/hg_egypt", unlockable = True,
    # Layers
    outfit_layers = ["bottoms/costume/skirt_egyptian","tops/costume/top_egyptian","gloves/wrist_shackles"],
    breast_layer  = "breasts_normal"
)
default hg_gamble_slut_ITEM = costume_class(
    id="hg_gamble_slut", name="Poke Her Nips", type="outfit_token", image="icon_gambler_hat",
    cost=14, wait_time=1, description=">An outfit that doesn't leave much for the mind's desire, perfect for a lewd card loving girl.",
    # Layers
    outfit_layers = ["onepieces/onepiece_gambler_cards","stockings/stockings_gambler_cards","onepieces/onepiece_gambler","stockings/stockings_gambler","gloves/wrist_cuffs_1","neckwear/choker_bow_tie_1","piercings/ears_gambler","piercings/belly_gambler"],
    breast_layer  = "breasts_normal",
    top_layers    = "hat_gambler"
)
default hg_witch_ITEM = costume_class(
    id="hg_witch", name="Witch Outfit", type="outfit", items=["outfit","hat"],
    cost=250, wait_time=3, image="outfits/hg_witch", description=">Release your inner witch with this halloween\n inspired outfit.",
    # Layers
    outfit_layers = ["robe/robe_witch_back","stockings/stockings_striped_2","onepieces/witch_top_1","robe/robe_witch"],
    breast_layer  = "breasts_normal",
    top_layers    = "hat_witch"
)
default hg_witch_skimpy_ITEM = costume_class(
    id="hg_witch_skimpy", name="Sexy Witch", type="outfit", items=["outfit","hat"], unlockable=True, image="outfits/hg_witch_skimpy",
    # Layers
    outfit_layers = ["robe/robe_witch_back","stockings/stockings_striped_2","onepieces/witch_top_2","robe/robe_witch"],
    breast_layer  = "breasts_normal",
    top_layers    = "hat_witch"
)

# Hermione Costumes
default hg_costume_power_girl_ITEM = costume_class(
    id="hg_costume_power_girl", name="Power Girl", type="outfit", items=["outfit"],
    cost=350, wait_time=3, image="outfits/hg_power", description=">An outfit for when you feel extra heroic\n \"Sometimes it takes balls to be a woman\".",
    # Layers
    outfit_layers = ["robe/robe_power_girl_back","onepieces/onepiece_power_girl_1","robe/robe_power_girl","gloves/gloves_power_girl","accs/belt_power_girl"],
    breast_layer  = "breasts_normal",
    hair_layer    = "power_girl"
)
default hg_costume_ms_marvel_ITEM = costume_class(
    id="hg_costume_ms_marvel", name="Mrs Marvel", type="outfit", items=["outfit"],
    cost=250, wait_time=2, image="outfits/hg_marvel", description=">For the girl that likes the lightningbolt\n better on the chest than the forehead.",
    # Layers
    outfit_layers = ["stockings/stockings_ms_marvel","onepieces/onepiece_ms_marvel","accs/belt_ms_marvel","gloves/gloves_ms_marvel"],
    breast_layer  = "breasts_normal"
)
default hg_costume_harley_quinn_ITEM = costume_class(
    id="hg_costume_harley_quinn", name="Harley Quinn",   type="outfit", items=["outfit"],
    cost=300, wait_time=3, image="outfits/hg_harley", description=">A outfit for when you're actually nuts\n rather than just crazy for them.",
    # Layers
    outfit_layers = ["bottoms/costume/pants_harley","tops/costume/top_harley","gloves/gloves_harley","neckwear/collar_leather"],
    breast_layer  = "breasts_normal",
    hair_layer    = "harley"
)
default hg_costume_lara_croft_ITEM = costume_class(
    id="hg_costume_lara_croft", name="Lara Croft", type="outfit", items=["outfit","gloves"],
    cost=270, wait_time=2, image="outfits/hg_lara", description=">An outfit perfectly suited for exploring deep, dark\n and moist caverns.",
    # Layers
    outfit_layers = ["bottoms/costume/pants_lara","tops/costume/top_lara","gloves/gloves_leather_2"],
    breast_layer  = "breasts_normal"
)
default hg_costume_tifa_ITEM = costume_class(
    id="hg_costume_tifa", name="Tifa", type="outfit", items=["outfit"],
    cost=220, wait_time=2, image="outfits/hg_tifa", description=">An outfit for when when your sexual fantasies\n are just getting started.",
    # Layers
    outfit_layers = ["bottoms/costume/skirt_tifa","tops/costume/top_tifa","gloves/gloves_tifa"],
    breast_layer  = "breasts_normal",
    hair_layer    = "tifa"
)
default hg_costume_elizabeth_ITEM = costume_class(
    id="hg_costume_elizabeth", name="Bioshock outfit", type="outfit", items=["outfit","hair","choker"],
    cost=400, wait_time=3, image="outfits/hg_bio", description=">Flick some coins for this Bioshock inspired outfit.",
    # Layers
    outfit_layers = ["bottoms/skirt_long_1","tops/top_corset_1","neckwear/choker_leather","tops/top_jacket_4"],
    breast_layer  = "breasts_normal_pressed",
    hair_layer    = "bobcut"
)
default hg_costume_yennefer_ITEM = costume_class(
    id="hg_costume_yennefer", name="Yennefer's costume", type="outfit", items=["outfit","choker","stockings"],
    cost=500, wait_time=3, image="outfits/hg_yenn", description=">A Witcher inspired outfit to fit even the most\n perverted witch",
    # Layers
    outfit_layers = ["stockings/stockings_silk_1","bottoms/pants_silk_1","bottoms/costume/skirt_yennefer","tops/costume/top_yennefer","gloves/gloves_leather_1","neckwear/scarf_silk","accs/belt_leather"],
    breast_layer  = "breasts_normal"
)

# Hermione Dresses
default hg_dress_yule_ball_ITEM = costume_class(
    id="hg_dress_yule_ball", name="Ball Dress", type="outfit", items=["outfit","hair","neckless","tiara"],
    cost=1500, wait_time=7, image="outfits/hg_ball_dress", description=">A traditional ball dress complete with a imitation\n ball-queen tiara.",
    # Layers
    outfit_layers = ["onepieces/onepiece_ball_dress"],
    breast_layer  = "breasts_nipfix",
    hair_layer    = "updo",
    top_layers    = "tiara"
)
default hg_dress_dancer_ITEM = costume_class(
    id="hg_dress_dancer", name="Heart Dancer",  type="outfit", items=["outfit"],
    cost=80, wait_time=1, image="outfits/hg_heart", description=">A sexy dancers outfit with heart shaped nipple tassels.",
    # Layers
    outfit_layers = ["bottoms/costume/skirt_heart_dancer","tops/costume/top_heart_dancer","neckwear/collar_heart_dancer"],
    breast_layer  = "breasts_normal"
)

default hermione_outfits_list = [
    hg_outfit_maid_ITEM,
    hg_outfit_pirate_ITEM,
    hg_outfit_christmas_ITEM,
    hg_outfit_present_ITEM,
    hg_outfit_japan_ITEM,
    hg_witch_ITEM,
    hg_witch_skimpy_ITEM,
    hg_outfit_egypt_ITEM,
]
default hermione_costumes_list = [
    hg_costume_power_girl_ITEM,
    hg_costume_ms_marvel_ITEM,
    hg_costume_harley_quinn_ITEM,
    hg_costume_lara_croft_ITEM,
    hg_costume_tifa_ITEM,
    hg_costume_elizabeth_ITEM,
    hg_costume_yennefer_ITEM,
]
default hermione_dresses_list = [
    hg_dress_dancer_ITEM,
    hg_dress_yule_ball_ITEM,
]

# Hermione Cheerleader
default hg_cheer_g_ITEM = costume_class(
    id="hg_cheer_g", name="Gryffindor Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_g",
    cost=80, wait_time=2, description=">A basic Cheerleader attire for Gryffindor's\n  Quidditch team.",
    outfit_layers = ["tops/top_cheer_g","bottoms/skirt_cheer_g"]
)
default hg_cheer_s_ITEM = costume_class(
    id="hg_cheer_s", name="Slythrin Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_s",
    cost=80, wait_time=2, description=">The Slytherin version of the Cheerleader attire.",
    outfit_layers = ["tops/top_cheer_s","bottoms/skirt_cheer_s"]
)
default hg_cheer_r_ITEM      = costume_class(
    id="hg_cheer_r", name="Ravenclaw Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_r",
    cost=80, wait_time=2, description=">The Ravenclaw version of the Cheerleader attire.",
    outfit_layers = ["tops/top_cheer_r","bottoms/skirt_cheer_r"]
)
default hg_cheer_h_ITEM      = costume_class(
    id="hg_cheer_h", name="Hufflepuff Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_h",
    cost=80, wait_time=2, description=">The Hufflepuff version of the Cheerleader attire.",
    outfit_layers = ["tops/top_cheer_h","bottoms/skirt_cheer_h"]
)
default hg_cheer_g_sexy_ITEM = costume_class(
    id="hg_cheer_g_sexy", name="Sexy Gryffindor Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_g_sexy", unlockable=True,
    outfit_layers = ["tops/top_cheer_sexy_g","bottoms/skirt_cheer_sexy_g"]
)
default hg_cheer_s_sexy_ITEM = costume_class(
    id="hg_cheer_s_sexy", name="Sexy Slythrin Cheerleader",   type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_s_sexy", unlockable=True,
    outfit_layers = ["tops/top_cheer_sexy_s","bottoms/skirt_cheer_sexy_s"]
)
default hg_cheer_r_sexy_ITEM = costume_class(
    id="hg_cheer_r_sexy", name="Sexy Ravenclaw Cheerleader",  type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_r_sexy", unlockable=True,
    outfit_layers = ["tops/top_cheer_sexy_r","bottoms/skirt_cheer_sexy_r"]
)
default hg_cheer_h_sexy_ITEM = costume_class(
    id="hg_cheer_h_sexy", name="Sexy Hufflepuff Cheerleader", type="set", items=["top","bottom","stockings"], image="outfits/hg_cheer_h_sexy", unlockable=True,
    outfit_layers = ["tops/top_cheer_sexy_h","bottoms/skirt_cheer_sexy_h"]
)

# Hermione Event Outfits
default hg_standart_school_ITEM = costume_class(
    id = "hg_standart_school",
    outfit_layers = ["bottoms/skirt_2", "tops/top_1_g"],
    breast_layer = "breasts_nipfix"
)
default hg_standart_school_noshirt_ITEM = costume_class(
    id = "hg_standart_school_noshirt",
    outfit_layers = ["bottoms/skirt_2", "bras/bra_base"],
    breast_layer = "breasts_nipfix"
)

# Hermione Lingerie
default hg_lingerie_lace_ITEM    = item_class(id="hg_lingerie_lace", name="Lace Lingerie",       type="set", items=["bra","panties"],                                   image="outfits/hg_lingerie_lace",    cost=40,  wait_time=1, description=">A lovely lace bra and panty set.")
default hg_lingerie_silk_ITEM    = item_class(id="hg_lingerie_silk", name="Silk Lingerie",       type="set", items=["bra","panties","garter","stockings"],              image="outfits/hg_lingerie_silk",    cost=80,  wait_time=1, description=">A smooth and comfortable silk bra and panty set.")
default hg_lingerie_maid_ITEM    = item_class(id="hg_lingerie_maid", name="Maid Lingerie",       type="set", items=["bra","panties","gloves","stockings","hair","hat"], image="outfits/hg_lingerie_maid",    cost=160, wait_time=2, description=">A revealing piece of maid clothing that only serves\n  to highlight the wearer's breasts.")
default hg_lingerie_latex_ITEM   = item_class(id="hg_lingerie_latex", name="Latex Lingerie",     type="set", items=["bra","panties","gloves","stockings"],              image="outfits/hg_lingerie_latex",   cost=200, wait_time=2, description=">A tight and shiny lace bra and panty set.")
default hg_lingerie_fishnet_ITEM = item_class(id="hg_lingerie_fishnet", name="Fishnet Lingerie", type="set", items=["top","bra","panties"],                             image="outfits/hg_lingerie_fishnet", cost=100, wait_time=1, description=">A very revealing set for fishnet lingerie.")

# Hermione One-pieces
default hg_nighty_silk_ITEM    = item_class(id="hg_nighty_silk", name="Silk Nighty",         type="set", items=["one-piece","panties"], cost=80,  wait_time=1, image="outfits/hg_nighty_silk",             description=">A comfortable yet elegant Nightwear set.")
default hg_nightgown_ITEM      = item_class(id="hg_nighty_silk", name="Silk Nightgown",      type="set", items=["one-piece"],           cost=80,  wait_time=1, image="outfits/hg_nightgown",               description=">A more free-flowing set of Nightwear.")
default hg_bikini_latex_ITEM   = item_class(id="hg_bikini_latex", name="Latex Bikini",       type="set", items=["bra","panties"],       cost=100, wait_time=1, image="outfits/hg_bikini_latex",            description=">A set for when you want to become one with your\n underwear")
default hg_bikini_sling_ITEM   = item_class(id="hg_bikini_sling", name="Sling Bikini",       type="set", items=["bra","panties"],       cost=69,  wait_time=1, image="outfits/hg_bikini_sling",            description=">Provides even less coverage than the Latex Bikini")
default hg_onepiece_sling_ITEM = item_class(id="hg_onepiece_sling", name="Sling Monokini",   type="set", items=["one-piece"],           cost=69,  wait_time=1, image="outfits/hg_onepiece_sling",          description=">A Mononoke variant of the Sling Bikini")
default hg_swimsuit_sport_ITEM = item_class(id="hg_swimsuit_sport", name="Sports Swimsuits", type="set", items=["one-piece"],           cost=69,  wait_time=1, image="outfits/hg_onepiece_swimsuit_sport", description=">Comes in 4 different variants. \nSwimmies not included!")

# Hermione Wicked Clothing
default hg_punk_rocker_ITEM  = item_class(id="hg_punk_rocker", name="Punk Rocker",   type="set", items=["top","bottom","gloves","choker"], cost=180, wait_time=2, image="outfits/hg_punk_rocker", description=">A punk-rock set of clothes for the more rebellious\n type of witch.")
default hg_punk_leather_ITEM = item_class(id="hg_punk_leather", name="Punk Leather", type="set", items=["top","bottom","bra","stockings"], cost=300, wait_time=3, image="outfits/hg_punk_leather", description=">A punk-leather set for wicked witches!\n The sleeve-length of the Leather-jacket can be changed.")

# Hermione Unlockable Clothing
default hg_accs_wool_g_ITEM      = item_class(id="hg_wool_accs_g", name="Gryffindor Wool Accessories",     type="set", items=["scarf","gloves","stockings"], image="outfits/hg_accs_wool_g", unlockable=True)
default hg_muggle_cold_ITEM      = item_class(id="hg_muggle_cold", name="Cold Weather Clothing",           type="set", items=["pullover","skirt","pantyhose"], image="outfits/hg_muggle_cold", unlockable=True)
default hg_muggle_cold_sexy_ITEM = item_class(id="hg_muggle_cold_sexy", name="Sexy Cold Weather Clothing", type="set", items=["pullover","skirt","pantyhose"], image="outfits/hg_muggle_cold_sexy", unlockable=True)
default hg_muggle_hot_ITEM       = item_class(id="hg_muggle_hot", name="Hot Weather Clothing",             type="set", items=["top","hot pants","stockings"], image="outfits/hg_muggle_hot", unlockable=True)
default hg_muggle_rainy_ITEM     = item_class(id="hg_muggle_rainy", name="Rainy Weather Clothing",         type="set", items=["sweater","long jeans"], image="outfits/hg_muggle_rainy", unlockable=True)

default hermione_clothing_sets_list=[
    hg_cheer_g_ITEM,
    hg_cheer_s_ITEM,
    hg_cheer_r_ITEM,
    hg_cheer_h_ITEM,
    hg_lingerie_lace_ITEM,
    hg_lingerie_silk_ITEM,
    hg_lingerie_maid_ITEM,
    hg_lingerie_latex_ITEM,
    hg_lingerie_fishnet_ITEM,
    hg_nighty_silk_ITEM,
    hg_nightgown_ITEM,
    hg_bikini_latex_ITEM,
    hg_bikini_sling_ITEM,
    hg_onepiece_sling_ITEM,
    hg_swimsuit_sport_ITEM,
    hg_punk_rocker_ITEM,
    hg_punk_leather_ITEM,
]

default hg_unlockable_clothing_sets_list = [
    hg_cheer_g_sexy_ITEM,
    hg_cheer_s_sexy_ITEM,
    hg_cheer_r_sexy_ITEM,
    hg_cheer_h_sexy_ITEM,
    hg_accs_wool_g_ITEM,
    hg_muggle_cold_ITEM,
    hg_muggle_cold_sexy_ITEM,
    hg_muggle_hot_ITEM,
    hg_muggle_rainy_ITEM,
]

# Luna Outfits

default ll_stewardess_ITEM = costume_class(
    id="ll_stewardess", name="Stewardess Outfit", type="outfit", items=["outfit","hat","neckless","thong"],
    cost=80, wait_time=2, image="outfits/ll_stewardess", description=">For immediate access into the mile-high club!",
    # Layers
    outfit_layers = ["panties/panties_thong_1","onepieces/onepiece_stewardess_1","neckwear/cloth_tie"],
    top_layers    = "hat_stewardess"
)
default ll_stewardess_short_ITEM = costume_class(
    id="ll_stewardess_short", name="Short Stewardess Outfit", type="outfit", items=["outfit","hat","neckless","thong"], image="outfits/ll_stewardess_short", unlockable=True,
    # Layers
    outfit_layers = ["panties/panties_thong_2","onepieces/onepiece_stewardess_2","neckwear/cloth_tie"],
    top_layers    = "hat_stewardess"
)
default ll_dress_orange_ITEM = costume_class(
    id="ll_dress_orange", name="Ball Dress", type="outfit", items=["outfit","earrings","stockings"],
    cost=200, wait_time=3, image="outfits/ll_dress_orange", description=">A cute dress in a questionable color.",
    # Layers
    outfit_layers = ["stockings/leggings_1","onepieces/onepiece_ball_dress","piercings/ears_starts_1"]
)

default luna_outfits_list = []
default luna_costumes_list = [
    ll_stewardess_ITEM,
    ll_stewardess_short_ITEM,
]
default luna_dresses_list = [
    ll_dress_orange_ITEM,
]

# Luna Sets
default ll_cheer_r_ITEM       = item_class(id="ll_cheer_r", name="Ravenclaw Cheerleader", type="set", items=["top","bottom","stockings"], cost=80, wait_time=2, image="outfits/ll_cheer_r", description=">The Ravenclaw version of the Cheerleader attire.")
default ll_lingerie_silk_ITEM = item_class(id="ll_lingerie_silk", name="Silk Lingerie",   type="set", items=["bra","panties"], cost=80, wait_time=1, image="outfits/ll_lingerie_silk", description=">A smooth and comfortable silk bra and panty set.")

default ll_quirky_muggle_ITEM = item_class(id="ll_quirky_muggle", name="Quirky Muggle", type="set", items=["top","bottom","stockings"], image="outfits/ll_muggle_1", unlockable=True)

default luna_clothing_sets_list = [
    ll_cheer_r_ITEM,
    ll_lingerie_silk_ITEM,
    ll_quirky_muggle_ITEM,
]

# Astoria Outfits
default ag_boss_uniform_ITEM = costume_class(
    id="ag_boss_uniform", name="Boss Uniform", type="outfit", items=["outfit","hair","hat"],
    cost=500, wait_time=3, image="outfits/ag_boss_uniform", description=">A uniform I designed with an old friend of mine.\n Makes me wonder what happened to Hugo...",
    # Layers
    outfit_layers = ["bottoms/pants_uniform","tops/top_uniform"],
    hair_layer    = "pigtails",
    top_layers    = "boss_hat"
)
default ag_costume_lazy_town_ITEM = costume_class(
    id="ag_costume_lazy_town", name="Lazy Town Outfit", type="outfit", items=["outfit","hair","bracelet"],
    cost=120, wait_time=1, image="outfits/ag_lazy", description=">Nobody is lazy at Hogwarts!",
    # Layers
    outfit_layers = ["stockings/leggings_1","onepieces/onepiece_striped_1","gloves/wrist_bracelet_1"],
    hair_layer    = "stephanie"
)
default ag_costume_lazy_town_short_ITEM = costume_class(
    id="ag_costume_lazy_town_short", name="Short Lazy Town Outfit", type="outfit", items=["outfit","hair","bracelet"],  image="outfits/ag_lazy_short", unlockable=True,
    # Layers
    outfit_layers = ["stockings/leggings_1","onepieces/onepiece_striped_2","gloves/wrist_bracelet_1"],
    hair_layer    = "stephanie"
)
default ag_dress_yule_ball_ITEM = costume_class(
    id="ag_dress_yule_ball", name="Ball Dress", type="outfit", items=["outfit"],
    cost=300, wait_time=4, image="outfits/ag_ball_dress", description=">A cute dress for your favourite princess!",
    # Layers
    outfit_layers = ["onepieces/onepiece_ball_dress"]
)

default astoria_outfits_list=[
    #ag_boss_uniform_ITEM,
]
default astoria_costumes_list = [
    #ag_costume_lazy_town_ITEM,
    #ag_costume_lazy_town_short_ITEM,
]
default astoria_dresses_list=[
    #ag_dress_yule_ball_ITEM,
]

# Astoria Sets
default ag_lingerie_lace_ITEM = item_class(id="ag_lingerie_lace", name="Lace Lingerie", type="set", items=["bra","panties"], cost=80,  wait_time=1, image="outfits/ag_lingerie_lace", description=">A cute lace lingerie set.")
default ag_lingerie_lewd_ITEM = item_class(id="ag_lingerie_lewd", name="Lewd Lingerie", type="set", items=["bra","panties"], cost=120, wait_time=1, image="outfits/ag_lingerie_lewd", description ="> A very rewealing lingerie set.")
default ag_nighty_silk_ITEM   = item_class(id="ag_nighty_silk", name="Silk Nighty", type="set", items=["nighty","panties","stockings"], cost=140, wait_time=1, image="outfits/ag_nighty_silk", description=">+2 attack points while pillow-fighting!")

default astoria_clothing_sets_list = [
    #ag_lingerie_lace_ITEM,
    #ag_lingerie_lewd_ITEM,
    #ag_nighty_silk_ITEM,
]

# Susan Outfits
default susan_outfits_list = []
default susan_costumes_list = []
default susan_dresses_list = []

# Susan Sets
default susan_clothing_sets_list = []

# Cho Outfits
default cc_outfit_quidditch_ITEM = costume_class(
    id="cc_outfit_quidditch", name="Quidditch Outfit", type="outfit", items=["outfit"], image="outfits/cc_quidditch", unlockable=True, outfit_layers = []
)
default cc_dress_red_ITEM = costume_class(
    id="cc_dress_red", name="Traditional Dress in Red", type="outfit", items=["outfit"],
    cost=100, wait_time=3, image="outfits/cc_dress_red", description=">A traditional dress inspired by chinese culture.",
    # Layers
    outfit_layers = ["onepieces/onepiece_ball_dress"]
)
default cc_dress_silver_ITEM = costume_class(
    id="cc_dress_silver", name="Traditional Dress in Silver", type="outfit", items=["outfit"],
    cost=100, wait_time=3, image="outfits/cc_dress_silver", description=">A traditional dress inspired by chinese culture."
    # No layers
)
default cc_dress_black_ITEM = costume_class(
    id="cc_dress_black", name="Traditional Dress in Black", type="outfit", items=["outfit"],
    cost=100, wait_time=3, image="outfits/cc_dress_black", description=">A traditional dress inspired by chinese culture."
    # No layers
)
default cc_outfit_sailor_white_ITEM = costume_class(
    id="cc_outfit_sailor_white", name="White Sailor Outfit", type="outfit", items=["outfit","top","skirt","thong","stockings","hat"],
    cost=240, wait_time=3, image="outfits/cc_sailor_white", description=">Slutty sailor outfit. Unlocks all items as separate\n and re-colourable items!",
    # Layers
    outfit_layers = ["panties/panties_bikini_2","stockings/stockings_sailor_1","tops/top_sailor_1","bottoms/skirt_sailor","../body/arms/arm_down_l_overlay"],
    top_layers    = "bow_sailor_yellow"
)
default cc_outfit_sailor_black_ITEM = costume_class(
    id="cc_outfit_sailor_black", name="Black Sailor Outfit", type="outfit", items=["outfit","top","skirt","thong","stockings","hat"],
    cost=240, wait_time=3, image="outfits/cc_sailor_black", description=">Slutty sailor outfit. Unlocks all items as separate\n and re-colourable items!",
    # Layers
    outfit_layers = ["panties/panties_bikini_2","stockings/stockings_sailor_2","tops/top_sailor_2","bottoms/skirt_sailor","../body/arms/arm_down_l_overlay"],
    top_layers    = "bow_sailor_red"
)
default cc_costume_misty_ITEM = costume_class(
    id="cc_costume_misty", name="Misty Costume", type="outfit", items=["outfit","top","pants","suspenders"],
    cost=100, wait_time=2, image="outfits/cc_misty", description=">For trainers that want to be the very best!\n To train them is your cause!",
    # Layers
    outfit_layers = ["tops/top_shirt_1","bottoms/pants_short_1","../body/arms/arm_down_l_overlay","accs/suspenders_1"]
)

default cho_outfits_list = [
    cc_outfit_quidditch_ITEM,
    cc_outfit_sailor_white_ITEM,
    # cc_outfit_sailor_black_ITEM
]
default cho_costumes_list = [
    cc_costume_misty_ITEM
]
default cho_dresses_list = [
    cc_dress_red_ITEM,
    # cc_dress_silver_ITEM,
    # cc_dress_black_ITEM
]

# Cho Sets
default cc_muggle_hot_ITEM = item_class(id="cc_muggle_hot", name="Hot Weather Clothing", type="set", items=["top","pants","stockings"], image="outfits/cc_muggle_hot", unlockable=True)
default cc_party_slut_ITEM = item_class(id="cc_party", name="Party Clothing",            type="set", items=["bra","skirt"],             image="outfits/cc_party", unlockable=True)

default cc_lingerie_lace_ITEM = item_class(id="cc_lingerie_lace", name="Lace Lingerie", type="set", items=["bra","panties","garter","stockings","choker","earrings"], image="outfits/cc_lingerie_lace", cost=500, wait_time=5, description=">This lingerie set turns even the toughest tomboy\n into a cute and sexy princess!")
default cc_bikini_micro_ITEM  = item_class(id="cc_bikini_micro", name="Micro Bikini",   type="set", items=["bra","panties"],                                          image="outfits/cc_bikini_micro", cost=69, wait_time=1, description=">The regular size bikinis are out of stock...")

default cho_clothing_sets_list = [
    cc_muggle_hot_ITEM,
    cc_party_slut_ITEM,
    cc_lingerie_lace_ITEM,
    cc_bikini_micro_ITEM,
]

# Old outfits linked to new outfits (using the variable names)
default outfit_linking = {
    # cc_outfit_quidditch_ITEM.id:    "cho_outfit_quidditch",
    cc_party_slut_ITEM.id:          "cho_outfit_party",
    cc_muggle_hot_ITEM.id:          "cho_outfit_trainee",
    cc_outfit_sailor_white_ITEM.id: "cho_outfit_sailor",
    cc_costume_misty_ITEM.id:       "cho_outfit_misty",
    cc_bikini_micro_ITEM.id:        "cho_outfit_bikini",
    cc_lingerie_lace_ITEM.id:       "cho_outfit_lacelingerie",
    cc_dress_red_ITEM.id:           "cho_outfit_dress1"
}

# Tonks Outfits
default tonks_outfits_list = []
default tonks_costumes_list = []
default tonks_dresses_list = []

label default_items_init:
    #TODO Fix: game_difficulty adjustment does not affect item cost after game has started
    if game_difficulty <= 1:
        $ wine_ITEM.cost = 40
        $ firewhisky_ITEM.cost = 60
    elif game_difficulty == 2:
        $ wine_ITEM.cost = 60
        $ firewhisky_ITEM.cost = 80
    else:
        $ wine_ITEM.cost = 140
        $ firewhisky_ITEM.cost = 160
