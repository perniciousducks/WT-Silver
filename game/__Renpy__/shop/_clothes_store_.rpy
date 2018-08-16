

label clothes_store:
    call blktone

    if clothes_intro_done == False:
        ">You enter to see an old woman busy sewing together two pieces of long dark fabric."
        ">The woman is dressed almost entirely in pink and has a warm, approachable air to her."
        m "Hello."
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        m "Neither thank you, I'm just here to make a few inquiries."
        maf "Of course sir, what could I help you with?"
        m "Firstly, what type of items do you sell?"
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        m "I see. Do you ever make custom orders?"
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        m "So you're interested in making unique outfits?"
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colors at the moment."
        maf "What did you have in mind?"
        m "A few things. I haven't decided on anything specific yet."
        m "Well, while your making up your mind, feel free to browse the store."
        $ clothes_intro_done = True
        jump open_clothes_store

    if outfit_ready:
        maf "here to pick up your order?"
        m "yes."
        maf "one moment, let me go fetch it"
        maf "..."
        maf "here you are."

        jump pickup_outfit

    if outfit_order_placed:
        maf "I'm sorry luv, but I'm still quite busy working on your item."
        maf "Come back once it's' ready. I will send you an owl."

        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu

    maf "Well, what can I get for you today?"
    jump open_clothes_store


label buy_outfit:

        #if clothes_store_order_choice.unlocked:
        #    call cust_excuse("You already own this set.")
        #    jump return_clothes_store
        #else:
            if clothes_store_order_choice == hg_cheer_g_OBJ:
                m "I'd like to order a cheerleader outfit."
                maf "A cheerleader outfit? Those horribly crass things popular in America?"
                maf "Why on earth would you want to buy that?"
                m "Well I was speaking to Madam Hooch and she was practically begging me to start a Cheer squad for each house."
                maf "Madam Hooch said that?"
                m "Yes, of course I said no but I did agree to a one student trial for Gryffindor."
                maf "Well, that seems fair enough. Did you have any preference as to the design?"
                m "Not really, just make it sporty I suppose."
                maf "Ok, well come and see me in a few days and I will have it for you."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_cheer_s_OBJ:
                m "I'd like to order another cheerleader outfit."
                maf "Another cheerleader outfit? I thought you said that it was only a one person trial?"
                m "It was at first but due to the success of the Gryffindor cheerleader Slytherin demanded one aswell."
                maf "Those Slytherins never could stand being second."
                maf "So do you just want the same basic design modified to suit?"
                m "Maybe make this one a little more sporty if you know what I mean."
                maf "Well you can come pick it up in a few days."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_cheer_r_OBJ:
                m "I'd like to order another cheerleader outfit."
                maf "Another cheerleader outfit? I thought you said that it was only a one person trial?"
                m "It was at first but due to the success of the Gryffindor cheerleader Slytherin demanded one aswell."
                maf "Those Slytherins never could stand being second."
                maf "So do you just want the same basic design modified to suit?"
                m "Maybe make this one a little more sporty if you know what I mean."
                maf "Well you can come pick it up in a few days."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_cheer_h_OBJ:
                m "I'd like to order another cheerleader outfit."
                maf "Another cheerleader outfit? I thought you said that it was only a one person trial?"
                m "It was at first but due to the success of the Gryffindor cheerleader Slytherin demanded one aswell."
                maf "Those Slytherins never could stand being second."
                maf "So do you just want the same basic design modified to suit?"
                m "Maybe make this one a little more sporty if you know what I mean."
                maf "Well you can come pick it up in a few days."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_maid_OBJ:
                m "I'd like to order a maid outfit."
                maf "A maid costume, what on earth for? Surely the cleaning elves keep your office tidy."
                m "It's going to be a present."
                maf "For whom?"
                m "I'm afraid I can't say."
                maf "Well as long as it's not for a student..."
                maf "Did you have any style in mind?"
                m "Prefrerebly a french maid."
                maf "..."
                maf "Well I should have it available for pickup in a few days after I get the materials in."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_nighty_silk_OBJ:
                m "I'd like to order another custom outfit today."
                maf "Certainly Sir. These outfits have started to become the highlight of my job. Everything else seems quite conservative by comparison."
                m "Well I can assure you that this outfit is not conservative."
                maf "Hmmm?"
                m "I'd like to order a girls Nightgown."
                maf "Well that doesn't seem overl-"
                m "Made of silk."
                maf "Ahh. I assume that you also want it transparent?"
                m "If it's possible."
                maf "Of course it is possible, who do you take me for?"
                maf "I just have to order in the materials, although silks not cheap."
                m "Don't worry about the cost."
                maf "As you wish Sir, it should be ready in a couple of days."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_ballDress_OBJ:
                if not sorry_for_hesterics:
                    m "Do you sell Dresses?"
                    maf "A dress? Are we talking ball-dresses, or more burlesque?"
                    m "Hmm... Balls actually."
                    maf "How surprising."
                    m "I was thinking that I could have a custom one made. For a very good girl of mine."
                if sorry_for_hesterics:
                    m "Do you sell Ball Dresses?"
                    maf "Hmmm, we do although they're nothing special. Why?"
                    m "A 'girl' approached me with a problem. Apparently she's unable to aquire a dress for this years autumn ball."
                    maf "How tragic, well I'm sure that one of these cheap ones will suffice."
                    m "I was thinking that I could have a custom one made. She is a very good girl."
                maf "I see. Would I be correct in assuming that this girls measurements are the same as the other outfits you've had me make?"
                m "Yes you would."
                maf "Well then I'll make her the best dress this school's ever seen. From what I've heard she's earned it..."
                maf "It should be ready in about a week."
                m "A week? Why so long?"
                maf "A ball dress isn't something that's thrown together. It requires love and attention. It doesn't come cheap either."
                m "Well, thank you."
                maf "You're welcome."
                jump place_outfit_order

            if clothes_store_order_choice == hg_msMarvel_OBJ:
                m "Tell me Madam Mafkin, have you ever heard of super-heroes?"
                maf "Yes yes, those people in the comic books. My grandson is quite fond of them."
                m "Fantastic, I was wondering if it would be possible for you to make me a costume."
                maf "Certainly, who did you have in mind?"
                m "Do you know Ms Marvel?"
                maf "I'm afraid not..."
                maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
                m "Thank you very much."
                maf "No need to thank me sir. Payment will suffice."
                jump place_outfit_order

            if clothes_store_order_choice == hg_heartDancer_OBJ:
                m "Have you ever seen a burlesque show Madam?"
                maf "I've done more than that, I've designed a few of the outfits for them!"
                m "Splendid, I was wondering if I could commision one."
                maf "Most Certainly, any particular color in mind?"
                m "Ideally red."
                maf "As you wish."
                m "Thank you very much."
                maf "You're quite welcome sir."
                jump place_outfit_order

            if clothes_store_order_choice == hg_powerGirl_OBJ:
                m "I was wondering if it would be possible for you to make me a super hero costume."
                maf "Certainly, who did you have in mind?"
                m "Do you know Power Girl?"
                maf "I'm afraid not..."
                maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
                m "Thank you very much."
                maf "No need to thank me sir. Payment will suffice."
                jump place_outfit_order

            if clothes_store_order_choice == hg_harleyQuinn_OBJ:
                m "I was wondering if it would be possible for you to make me a super villain costume."
                maf "Certainly, who did you have in mind?"
                m "Do you know Harley Quinn?"
                maf "I'm afraid not..."
                maf "But I'm sure that my grandson has a comic of hers. I'll just have to wrestle it out of his grubby little hands."
                m "Thank you very much."
                maf "You're quite welcome."
                jump place_outfit_order

            if clothes_store_order_choice == hg_laraCroft_OBJ:
                m "I was wondering if it would be possible for you to make me another costume."
                maf "Certainly, what are you after?"
                m "I don't suppose that you know Lara croft?"
                maf "I'm afraid not..."
                m "She's a video game character..."
                maf "Well my little muggle grandson loves video games. I'm sure he can show me what she looks like."
                m "Thank you very much."
                maf "You're welcome. I'm seeing him tonight so I should be able to complete this one slightly faster than usual."
                m "Fantastic."
                jump place_outfit_order

            if clothes_store_order_choice == hg_christmas_OBJ:
                m "I was wondering if it would be possible for you to make me a festive costume."
                maf "Certainly, what what holiday are you looking to \"celebrate\"?"
                m "Christmas."
                maf "At this time of year?"
                m "It's never to early to start the festivities..."
                maf "Evidently not. I'll have it done as soon as I can. "
                m "Thank you very much."
                maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you.."
                m "Thank you."
                jump place_outfit_order

            if clothes_store_order_choice == hg_pirate_OBJ:
                m "I want a pirate outfit"
                maf "ok"
                jump place_outfit_order

            if clothes_store_order_choice == hg_bio_OBJ:
                m "Have you ever heard of bioshock infinite?"
                maf "Biology what now?"
                m "..."
                m "It might be something to ask your grandson about..."
                maf "I assume you want the costume from whatever that is?"
                m "If it's not too much..."
                maf "Consider it done!"
                m "Thank you very much."
                maf "You're welcome."
                jump place_outfit_order

            if clothes_store_order_choice == hg_yenn_OBJ:
                m "Have you ever heard of the sorceress yennefer?"
                maf "Of course! The mother of a universe hopper isn't quickly forgotten..."
                m "Think you could make a copy of her outfit?"
                maf "Certainly."
                m "Thank you very much."
                maf "You can thank me with coin!"
                jump place_outfit_order

            "> This outfit/Set is Missing Texts!"
            jump place_outfit_order


label place_outfit_order:
    $ outfit_OBJ = clothes_store_order_choice
    if gold >= outfit_OBJ.cost:
        $ gold -= outfit_OBJ.cost
        $ outfit_wait_time = outfit_OBJ.wait_time
        $ outfit_order = clothes_store_order_choice
        $ outfit_order_placed = True

        call give_reward("> Your order has been made.","images/store/31.png")
        maf "I'll send you an owl when it's done."

        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu

    else:
        m "I don't have [outfit_OBJ.cost] gold."
        m "Well this is depressing."
        jump return_clothes_store

label outfit_purchase_check:
    if outfit_wait_time <= 0:
        $ outfit_ready = True
        $ letters += 1
    else:
       $ outfit_wait_time -= 1
return

label pickup_outfit:

    if outfit_order_placed: # OUTFIT
        if outfit_order in hermione_outfits_list:
            call display_package(">A "+outfit_order.name+R" outfit has been added to Hermione's Wardrobe.")
        else:
            call display_package(">A "+outfit_order.name+R" set has been added to Hermione's Wardrobe.")
        $ outfit_order.unlocked = True
        $ clothes_store_selection = None
        $ clothes_store_order_choice = None
        call receive_package

    maf "Anything else I can help you with?"

    menu:
        "-Open the store-":
            jump return_clothes_store
        "-Leave-":
            m "Not right now."
            maf "Very well then."

            if daytime:
                maf "Good day, Professor."
                jump day_main_menu
            else:
                maf "Good night, Professor."
                jump night_main_menu

label display_package(str1):
    $ the_gift = "images/store/07.png"
    show screen gift
    with d3
    "[str1]"
    hide screen gift
    with d3
return

label receive_package:
    if letters >= 1:
        $ letters -= 1
    $ outfit_order = None
    $ outfit_order_placed = False
    $ outfit_ready = False
return

label cust_excuse(text="Meh, you cant use this yet"): #custom text option for other ideas
    show screen blktone5
    ">[text]"
    hide screen blktone5
    return

label existing_stock:
    menu:

        "-Tops-":#Jeans#Stockings#Fishnet Stockings#Lace Bra and Panties#Cup-less Lace Bra#Silk Bra and Panties
            label existing_stock_tops:
            menu:
                "{color=#858585}-Muggle Pullover- (50 Gold)-{/color}"if "normal_pullover" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_tops
                "-Muggle Pullover- (50 Gold)" if "normal_pullover" not in cs_existing_stock:
                    maf "A cute pink pullover. Has a heart shaped hole for her cleavage that can magically appear if you want!"
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 2 to be worn.<"
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("normal_pullover", 50)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                "{color=#858585}-Muggle Sweater- (60 Gold)-{/color}"if "normal_sweater" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_tops
                "-Muggle Sweater- (60 Gold)" if "normal_sweater" not in cs_existing_stock:
                    maf "The sweater she has worn in movie 3! When she punched that rascal Malfoy in the face! Loved that scene."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 2 to be worn.<"
                    menu:
                        "-Buy the item (60 gold)-":
                            call cs_buy_stock("normal_sweater", 60)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                #"{color=#858585}-Waitress Top- (100 Gold)-{/color}"if "normal_waitress_top" in cs_existing_stock:
                #    call cust_excuse(">You already own this.")
                #    jump existing_stock_tops
                #"-Waitress Top- (100 Gold)" if "normal_waitress_top" not in cs_existing_stock:
                #    maf "Very cute looking top if I may say so myself."
                #    if cheats_active or game_difficulty <= 2:
                #        ">Requires a whoring level of 8 to be worn.<"
                #    menu:
                #        "-Buy the item (100 gold)-":
                #            call cs_buy_stock("normal_waitress_top", 100)
                #            jump existing_stock_tops
                #        "-Never mind-":
                #            jump existing_stock_tops

                "{color=#858585}-Leather Jacket Short Sleeves- (200 Gold)-{/color}"if "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_tops
                "-Leather Jacket Short Sleeves- (200 Gold)" if "wicked_leather_jacket_short_sleeves" not in cs_existing_stock:
                    maf "A black leather jacket with short sleeves. Can also be worn open of course."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 17 to be worn.<"
                    menu:
                        "-Buy the item (200 gold)-":
                            call cs_buy_stock("wicked_leather_jacket_short_sleeves", 200)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                "{color=#858585}-Leather Jacket No Sleeves- (200 Gold)-{/color}"if "wicked_leather_jacket_sleeveless" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_tops
                "-Leather Jacket No Sleeves- (200 Gold)" if "wicked_leather_jacket_sleeveless" not in cs_existing_stock:
                    maf "A black leather jacket with no sleeves. Can also be worn open of course."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 17 to be worn.<"
                    menu:
                        "-Buy the item (200 gold)-":
                            call cs_buy_stock("wicked_leather_jacket_sleeveless", 200)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                "{color=#858585}-Leather Jacket Long Sleeves- (200 Gold)-{/color}"if "wicked_leather_jacket_sleeves" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_tops
                "-Leather Jacket Long Sleeves- (200 Gold)" if "wicked_leather_jacket_sleeves" not in cs_existing_stock:
                    maf "A black leather jacket with long sleeves. Can also be worn open of course."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 17 to be worn.<"
                    menu:
                        "-Buy the item (200 gold)-":
                            call cs_buy_stock("wicked_leather_jacket_sleeves", 200)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                "{color=#858585}-Fishnets Top- (60 Gold)-{/color}"if "top_fishnets" in cs_existing_stock:
                    call cust_excuse("You already own this. - Requires whoring level 20 for it to appear in the wardrobe.")
                    jump existing_stock_tops
                "-Fishnets Top- (60 Gold)" if "top_fishnets" not in cs_existing_stock:
                    maf "This fishnets top hides nothing! What girl would possibly want to wear this on school grounds?"
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 20 to be worn.<"
                    menu:
                        "-Buy the item (60 gold)-":
                            call cs_buy_stock("top_fishnets", 60)
                            jump existing_stock_tops
                        "-Never mind-":
                            jump existing_stock_tops

                "-Return-":
                    jump existing_stock


        "-Pants and Skirts-":#Jeans#Stockings#Fishnet Stockings#Lace Bra and Panties#Cup-less Lace Bra#Silk Bra and Panties
            label existing_stock_pants_skirts:
            menu:
                "{color=#858585}-Belted Mini Skirt- (75 Gold)-{/color}"if "skirt_belted_mini" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_pants_skirts
                "-Belted Mini Skirt- (75 Gold)" if "skirt_belted_mini" not in cs_existing_stock:
                    maf "A short skirt with a belt. Very trendy!"
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 8 to be worn.<"
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("skirt_belted_mini", 75)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Belted Micro Skirt- (150 Gold)-{/color}"if "skirt_belted_micro" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_pants_skirts
                "-Belted Micro Skirt- (150 Gold)" if "skirt_belted_micro" not in cs_existing_stock:
                    maf "A very short skirt with a belt. Very revealing! Lets just hope the girl is wearing a pair of underwear!"
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 17 to be worn.<"
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("skirt_belted_micro", 150)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Jeans- (75 Gold)-{/color}"if "pants_jeans_long" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_pants_skirts
                "-Jeans- (75 Gold)" if "pants_jeans_long" not in cs_existing_stock:
                    maf "A pair of standard muggle jeans, albeit a little low slung."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 2 to be worn.<"
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("pants_jeans_long", 75)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts

                "{color=#858585}-Short Jeans- (150 Gold)-{/color}"if "pants_jeans_short" in cs_existing_stock:
                    call cust_excuse(">You already own this.")
                    jump existing_stock_pants_skirts
                "-Short Jeans- (150 Gold)" if "pants_jeans_short" not in cs_existing_stock:
                    maf "A pair of short daisy dukes."
                    if cheats_active or game_difficulty <= 2:
                        ">Requires a whoring level of 11 to be worn.<"
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("pants_jeans_short", 150)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts

                #"{color=#858585}-Retro Shorts- (170 Gold)-{/color}"if "pants_retro_shorts" in cs_existing_stock:
                #    call cust_excuse(">You already own this.")
                #    jump existing_stock_pants_skirts
                #"-Retro Shorts- (170 Gold)" if "pants_retro_shorts" not in cs_existing_stock:
                #    maf "A pair of skin tight retro shorts. Just the right thing to highlight a magnificent behind."
                #    if cheats_active or game_difficulty <= 2:
                #        ">Requires a whoring level of 17 to be worn.<"
                #    menu:
                #        "-Buy the item (170 gold)-":
                #            call cs_buy_stock("pants_retro_shorts", 170)
                #            jump existing_stock_pants_skirts
                #        "-Never mind-":
                #            jump existing_stock_pants_skirts

                "-Return-":
                    jump existing_stock

        "-Stockings-":
            label existing_stock_stockings:
            menu:
                "{color=#858585}-Gryffindor Stockings- (50 Gold)-{/color}"if "stockings_gryff" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_stockings
                "-Gryffindor Stockings- (50 Gold)" if "stockings_gryff" not in cs_existing_stock:
                    maf "A pair of cheerful school stockings, in Gryffindor's colours."
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("stockings_gryff", 50)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings

                "{color=#858585}-Slytherin Stockings- (50 Gold)-{/color}"if "stockings_slyth" in cs_existing_stock:
                    call cust_excuse("You already own this. - Requires whoring level 9 for it to appear in the wardrobe.")
                    jump existing_stock_stockings
                "-Slytherin Stockings- (50 Gold)" if "stockings_slyth" not in cs_existing_stock:
                    maf "A pair of cheerful school stockings, in Slytherin's colours."
                    ">Requires a whoring level of 9 to be worn.<"
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("stockings_slyth", 50)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings

                "{color=#858585}-Fishnet Stockings- (75 Gold)-{/color}"if "stockings_fishnet_black" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_stockings
                "-Fishnet Stockings- (75 Gold)" if "stockings_fishnet_black" not in cs_existing_stock:
                    maf "A pair of sultry fishnet stockings."
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("stockings_fishnet_black", 75)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings

                "{color=#858585}-Lace Stockings- (30 Gold)-{/color}"if "stockings_lace_black" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_stockings
                "-Lace Stockings- (30 Gold)" if "stockings_lace_black" not in cs_existing_stock:
                    maf "A pair of black lace stockings."
                    menu:
                        "-Buy the item (30 gold)-":
                            call cs_buy_stock("stockings_lace_black", 30)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings


                "-Return-":
                    jump existing_stock




        "-Accessories-":
            label accessories:
            menu:
                "{color=#858585}-\"S.P.E.W.\" badge-{/color}"if "SPEW_badge" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-\"S.P.E.W.\" badge-" if "SPEW_badge" not in cs_existing_stock:
                    maf "A badge designed to show one's opposition of elf slavery."
                    menu:
                        "-Buy the item (100 gold)-":
                            call cs_buy_stock("SPEW_badge",100)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-\"I <3 C.U.M.\" badge-{/color}"if "CUM_badge" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-\"I <3 C.U.M.\" badge-" if "CUM_badge" not in cs_existing_stock:
                    maf "A badge that displays ones affection towards semen."
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("CUM_badge",150)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-Freckles-{/color}"if "freckles" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-Freckles-" if "freckles" not in cs_existing_stock:
                    maf "Some lovely freckle paint. Now non-toxic!"
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("freckles",50)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-reading glasses-{/color}"if "reading_glasses" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-reading glasses-" if "reading_glasses" not in cs_existing_stock:
                    maf "I wish I only needed fake reading glasses."
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("reading_glasses",75)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-vintage glasses-{/color}"if "vintage_glasses" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-vintage glasses-" if "vintage_glasses" not in cs_existing_stock:
                    maf "These old glasses used to be quite fashionable."
                    menu:
                        "-Buy the item (60 gold)-":
                            call cs_buy_stock("vintage_glasses",60)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-fake cum-{/color}"if "fake_cum" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-fake cum-" if "fake_cum" not in cs_existing_stock:
                    maf "it's Just a little bit of margarita mix..."
                    menu:
                        "-Buy the item (100 gold)-":
                            call cs_buy_stock("fake_cum",100)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-Cat ears-{/color}"if "cat_ears" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-Cat Ears-" if "cat_ears" not in cs_existing_stock:
                    maf "it's a pair of cat ears..."
                    maf "and it even comes with a clip on tail..."
                    menu:
                        "-Buy the item (70 gold)-":
                            call cs_buy_stock("cat_ears",70)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-Transparency Potion-{/color}"if "transparency" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-Transparency Potion-" if "transparency" not in cs_existing_stock:
                    maf "This renders the users clothes slightly see through."
                    maf "I'd save this for private occasions if I was you..."
                    menu:
                        "-Buy the item (130 gold)-":
                            call cs_buy_stock("transparency",130)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-elf ears-{/color}"if "elf_ears" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-elf ears-" if "elf_ears" not in cs_existing_stock:
                    maf "A pair of fake elf ears."
                    maf "The real ones are much harder to import..."
                    menu:
                        "-Buy the item (80 gold)-":
                            call cs_buy_stock("elf_ears",80)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "-Never mind-":
                    jump existing_stock
        "-Return-":
            jump clothes_menu

label cs_buy_stock(item_id = "", cost):
    if gold >= cost and item_id != "":
        if item_id in cs_existing_stock:
            m "I already own this."
            return
        else:
            $ gold -= cost
            $ cs_existing_stock.append(item_id)
            maf "Thank you very much."
            return
    else:
        m "I don't have enough gold for this."
        return

label open_clothes_store:
    $ cs_gui_OBJ = cs_gui_outfit_class() #This will reset all clothes store variables.
    $ mannequin_preview = "hg_mannequin.png"
    $ clothes_store_selection = None


    label return_clothes_store:

        call update_clothes_store_lists


    #Set mannequin outfit
    #call mannequin_01("preview_main",xpos="cs_main",ypos="base")

    #call mannequin_02("preview_left",xpos="cs_preview_left",ypos="cs_preview")
    #call mannequin_03("preview_mid",xpos="cs_preview_mid",ypos="cs_preview")
    #call mannequin_04("preview_right",xpos="cs_preview_right",ypos="cs_preview")

    call screen cs_gui



label cs_select:
    $ mannequin_preview = clothes_store_selection.image
    #$ clothes_store_order_choice = clothes_store_selection
    call screen cs_gui

label cs_buy:
    $ renpy.play('sounds/door2.mp3') #closing wardrobe page
    $ clothes_store_order_choice = clothes_store_selection.image
    #$ clothes_store_order_choice = clothes_store_selection
    jump clothes_menu

label cs_buy_item:
    if gold > selected_item.cost:
        $ selected_item.unlocked = True #Unlocks item.
        $ selected_item = None
        call cust_excuse("Item purchased!")
    else:
        call cust_excuse("You don't have enough gold for this!")
    jump return_clothes_store

label close_clothes_store:
    $ renpy.play('sounds/door2.mp3') #closing wardrobe page

    m "That's all for today, thank you."
    maf "You're welcome, sir. Come back any time."

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu


screen cs_gui():

    if cs_gui_OBJ.category in [0,1]:
        $ UI_xpos_offset = 0
        $ UI_ypos_offset = 0
    else:
        $ UI_xpos_offset = 150
        $ UI_ypos_offset = 77

    tag clothes_menu
    zorder 5

    imagemap:
        cache False

        # Outfits & Sets
        if cs_gui_OBJ.category in [0,1]:

            # Main Interface
            if clothes_store_selection == None:
                ground "interface/store/"+str(interface_color)+"/clothing_panel_main.png"
                hover "interface/store/"+str(interface_color)+"/clothing_panel_main_hover.png"

            else:
                ground "interface/store/"+str(interface_color)+"/clothing_panel_full.png"
                hover "interface/store/"+str(interface_color)+"/clothing_panel_full_hover.png"

            add cs_gui_OBJ.getMannequinPreview() xpos 600 ypos 0 zoom 1.0/scaleratio

            # Left Button
            imagebutton:
                xpos 977
                ypos 544
                idle "interface/general/"+interface_color+"/button_arrow_left.png"

                if cs_gui_OBJ.character > 1:
                    hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
                    action Jump("cs_gui_character_back")

            # Right Button
            imagebutton:
                xpos 1029
                ypos 544
                idle "interface/general/"+interface_color+"/button_arrow_right.png"

                if cs_gui_OBJ.character < 5:
                    hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
                    action Jump("cs_gui_character_forward")

            # Bag of Gold Icon
            if clothes_store_selection != None:

                imagebutton:
                    xpos 705
                    ypos 490
                    idle "interface/general/gold_bag.png"

                    hover "interface/general/gold_bag_hover.png"
                    action [SetVariable("clothes_store_order_choice",clothes_store_selection), Jump("buy_outfit")]



        # Clothing Items & Dyes
        else:

            # Main Interface
            xpos 150
            ypos 77
            ground "interface/store/"+str(interface_color)+"/items_panel.png"
            hover "interface/store/"+str(interface_color)+"/items_panel_hover.png"

            text "Clothing Items" xalign 0.5 yalign 0.5 xpos 309-UI_xpos_offset ypos 130-UI_ypos_offset size 24


        # Always Active

        # Close Button
        imagebutton:
            xpos 1028-UI_xpos_offset
            ypos 11-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_close.png"
            hover "interface/general/"+interface_color+"/button_close_hover.png"
            action Jump("close_clothes_store")

        # Outfits Buttons
        imagebutton:
            xpos 725-UI_xpos_offset
            ypos 105-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_select.png"
            if cs_gui_OBJ.category != 0: # Outfits
                hover "interface/general/"+interface_color+"/button_select_hover.png"
                action [SetVariable("clothes_store_category","outfits"), Jump("change_cs_category")]
        if cs_gui_OBJ.category == 0: # Outfits
            text "Outfits" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121-UI_ypos_offset size 16
        else:
            text "Outfits" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121-UI_ypos_offset size 14

        # Sets Button
        imagebutton:
            xpos 725-UI_xpos_offset
            ypos 149-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_select.png"
            if cs_gui_OBJ.category != 1: # Sets
                hover "interface/general/"+interface_color+"/button_select_hover.png"
                action [SetVariable("clothes_store_category","sets"), Jump("change_cs_category")]
        if cs_gui_OBJ.category == 1: # Sets
            text "Sets" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121+44-UI_ypos_offset size 16
        else:
            text "Sets" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121+44-UI_ypos_offset size 14

        # Items Button
        imagebutton:
            xpos 725-UI_xpos_offset
            ypos 193-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_select.png"
            if cs_gui_OBJ.category != 2: # Items
                hover "interface/general/"+interface_color+"/button_select_hover.png"
                action [SetVariable("clothes_store_category","items"), Jump("change_cs_category")]
        if cs_gui_OBJ.category == 2: # Items
            text "Items" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121+88-UI_ypos_offset size 16
        else:
            text "Items" xalign 0.5 yalign 0.5 xpos 767-UI_xpos_offset ypos 121+88-UI_ypos_offset size 14

        # Up Button
        imagebutton:
            xpos 725-UI_xpos_offset
            ypos 240-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_arrow_up.png"

            if cs_gui_OBJ.current_page > 0:
                hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
                action Jump("cs_gui_index_up")

        # Down Button
        imagebutton:
            xpos 725-UI_xpos_offset
            ypos 292-UI_ypos_offset
            idle "interface/general/"+interface_color+"/button_arrow_down.png"

            if cs_gui_OBJ.current_page < cs_gui_OBJ.getTotalPages():
                hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
                action Jump("cs_gui_index_down")



        # Outfits & Sets
        if cs_gui_OBJ.category in [0,1]:
            if clothes_store_selection != None:
                text clothes_store_selection.getStoreName() xpos 83 ypos 458 size 16
                text clothes_store_selection.getStoreDescription() xpos 85 ypos 490 size 12

                text clothes_store_selection.getType() xpos 509 ypos 458 size 16

                for i in range(0,len(clothes_store_selection.getStoreItems() )):
                    $ row = i % 3
                    $ col = i % 2

                    text "+"+clothes_store_selection.getStoreItems()[i] xpos 511+(80*col) ypos (490+(12*row)) size 12

                text clothes_store_selection.getStoreWaitTime() xpos 83 ypos 557 size 16
                text clothes_store_selection.getStoreCost() xpos 509 ypos 557 size 16


            $ page_list = cs_gui_OBJ.getListOfItems()

            $ index = 0
            for i in range(0,3):
                if index < len(page_list):
                    hotspot(70+(227*i),(107),175,284) clicked [SetVariable("clothes_store_selection",page_list[index]),Jump("cs_select")]

                    add page_list[index].getStoreImage() xpos (-7+(227*i)) ypos 30 zoom 0.6/scaleratio
                    $ index = index+1

        # Items
        if cs_gui_OBJ.category in [2]:

            if cs_show_clothing: #Toggle Clothing Items
                hotspot (470-UI_xpos_offset,109-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_clothing",False), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_true.png" xpos 470-UI_xpos_offset ypos 104-UI_ypos_offset
            else:
                hotspot (470-UI_xpos_offset,109-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_clothing",True), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_false.png" xpos 470-UI_xpos_offset ypos 104-UI_ypos_offset
            text "Clothing" xpos 492-UI_xpos_offset ypos 113-UI_ypos_offset size 10

            if cs_show_accs: #Toggle Accessory Items
                hotspot (470+100-UI_xpos_offset,109-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_accs",False), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_true.png" xpos 470+100-UI_xpos_offset ypos 104-UI_ypos_offset
            else:
                hotspot (470+100-UI_xpos_offset,109-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_accs",True), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_false.png" xpos 470+100-UI_xpos_offset ypos 104-UI_ypos_offset
            text "Accs." xpos 492+100-UI_xpos_offset ypos 113-UI_ypos_offset size 10

            if cs_show_misc: #Toggle Dye Items
                hotspot (470-UI_xpos_offset,109+22-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_misc",False), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_true.png" xpos 470-UI_xpos_offset ypos 104+22-UI_ypos_offset
            else:
                hotspot (470-UI_xpos_offset,109+22-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_misc",True), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_false.png" xpos 470-UI_xpos_offset ypos 104+22-UI_ypos_offset
            text "Misc." xpos 492-UI_xpos_offset ypos 113+22-UI_ypos_offset size 10

            if cs_show_dyes: #Toggle Dye Items
                hotspot (470+100-UI_xpos_offset,109+22-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_dyes",False), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_true.png" xpos 470+100-UI_xpos_offset ypos 104+22-UI_ypos_offset
            else:
                hotspot (470+100-UI_xpos_offset,109+22-UI_ypos_offset,18,18) clicked [SetVariable("cs_show_dyes",True), Jump("return_clothes_store")]
                add "interface/general/"+str(interface_color)+"/check_false.png" xpos 470+100-UI_xpos_offset ypos 104+22-UI_ypos_offset
            text "Dyes" xpos 492+100-UI_xpos_offset ypos 113+22-UI_ypos_offset size 10

            $ page_list = cs_gui_OBJ.getListOfItems()

            $ index = 0
            for i in range(0,4):
                if index < len(page_list):
                    hotspot (172-UI_xpos_offset, (164-UI_ypos_offset+(90*i)), 83, 83) clicked [SetVariable("selected_item",page_list[index]),Jump("cs_buy_item")]

                    add page_list[index].getStoreImage() xalign 0.5 xpos 217-UI_xpos_offset yalign 0.5 ypos (202-UI_ypos_offset+(+90*i)) zoom 0.4

                    text page_list[index].getStoreName() xpos 269-UI_xpos_offset ypos (170-UI_ypos_offset+(90*i)) size 16
                    text page_list[index].getStoreDescription() xpos 269-UI_xpos_offset ypos (196-UI_ypos_offset+(90*i)) size 12
                    text page_list[index].getStoreCost() xpos 269+270-UI_xpos_offset ypos (170-UI_ypos_offset+(90*i)) size 16

                    for j in range(0, len(page_list[index].getStoreItems() )):
                        $ col = j % 3

                        text "+"+page_list[index].getStoreItems()[j] xpos 269-UI_xpos_offset+(110*col) ypos (196+32-UI_ypos_offset+(90*i)) size 12

                    $ index = index+1



label change_cs_category:
    if clothes_store_category == "outfits":
        $ cs_gui_OBJ.category = 0
    if clothes_store_category == "sets":
        $ cs_gui_OBJ.category = 1
    if clothes_store_category == "items":
        $ cs_gui_OBJ.category = 2
    $ cs_gui_OBJ.current_page = 0
    jump return_clothes_store

label cs_gui_character_forward:
    $ cs_gui_OBJ.character = cs_gui_OBJ.character+1
    $ cs_gui_OBJ.current_page = 0
    $ clothes_store_selection = None
    jump return_clothes_store
label cs_gui_character_back:
    $ cs_gui_OBJ.character = cs_gui_OBJ.character-1
    $ cs_gui_OBJ.current_page = 0
    $ clothes_store_selection = None
    jump return_clothes_store

label cs_gui_index_up:
    $ cs_gui_OBJ.current_page = cs_gui_OBJ.current_page-1
    call screen cs_gui
label cs_gui_index_down:
    $ cs_gui_OBJ.current_page = cs_gui_OBJ.current_page+1
    call screen cs_gui

label update_clothes_store_lists:

    $ cs_inventory_list = []
    if cs_gui_OBJ.category == 0: #Outfits
        if cs_gui_OBJ.character == 1: #Hermione
            python:
                for i in hermione_outfits_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)

        elif cs_gui_OBJ.character == 2: #Luna
            $ cs_inventory_list = []

        elif cs_gui_OBJ.character == 3: #Susan
            $ cs_inventory_list = []

        elif cs_gui_OBJ.character == 4: #Astoria
            python:
                for i in astoria_outfits_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)

        else: #Cho
            $ cs_inventory_list = []


    #Sets
    if cs_gui_OBJ.category == 1:
        if cs_gui_OBJ.character == 1: #Hermione
            python:
                for i in hermione_clothing_sets_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)

        elif cs_gui_OBJ.character == 2: #Luna
            $ cs_inventory_list = []

        elif cs_gui_OBJ.character == 3: #Susan
            $ cs_inventory_list = []

        elif cs_gui_OBJ.character == 4: #Astoria
            python:
                for i in astoria_clothing_sets_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)

        else: #Cho
            $ cs_inventory_list = []


    #Items
    if cs_gui_OBJ.category == 2:
        python:
            if cs_show_clothing:
                for i in cs_clothing_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)
            if cs_show_accs:
                for i in cs_accessories_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)
            if cs_show_misc:
                for i in cs_miscellaneous_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)
            if cs_show_dyes:
                for i in cs_dye_list:
                    if not i.unlockable: #Unlockables DO NOT get added to the Shop!
                        if not i.unlocked:
                            cs_inventory_list.append(i)

    $ cs_gui_OBJ.current_page = 0

    return


init python:

    class cs_gui_outfit_class(object):
        current_page = 0
        character = 1
        category = 0
        preview = "interface/icons/outfit/hg_mannequin.png"

        def getListOfItems(self):
            if self.category in [0,1]: # 0=Outfits, 1=Sets
                return cs_inventory_list [ (self.current_page *3) : min ( ((self.current_page+1)*3) , len (cs_inventory_list) ) ]
            else:
                return cs_inventory_list [ (self.current_page *4) : min ( ((self.current_page+1)*4) , len (cs_inventory_list) ) ]
        def getNamesOfItems(self):
            return [i.name for i in self.getListOfItems()]
        def getTotalPages(self):
            if self.category in [0,1]: # 0=Outfits, 1=Sets
                return len(cs_inventory_list)/3
            else: #Item Store
                return len(cs_inventory_list)/4
        def getMannequinPreview(self):
            if clothes_store_selection == None:
                if self.character == 1: # Hermione
                    return "interface/icons/outfit/hg_mannequin.png"
                elif self.character == 2: # Luna
                    return "interface/icons/outfit/ll_mannequin.png" # Placeholder
                elif self.character == 3: # Susan
                    return "interface/icons/outfit/sb_mannequin.png"
                elif self.character == 4: # Astoria
                    return "interface/icons/outfit/ag_mannequin.png"
                elif self.character == 5: # Cho
                    return "interface/icons/outfit/cc_mannequin.png" # Placeholder
                else:
                    return "interface/icons/outfit/hg_mannequin.png"
            else:
                return clothes_store_selection.getStoreImage()
