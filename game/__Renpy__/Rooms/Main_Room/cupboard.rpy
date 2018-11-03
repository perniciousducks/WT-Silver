

label cupboard:
    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_left #Empty chair near the desk.
            hide screen genie
            call gen_chibi("stand","behind_desk","base",flip=True)
            show screen desk
            with Dissolve(0.5)

            m "Hm....."
            m "A cupboard..."
            m "Maybe I should rummage through this one later..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu

        "-Rummage through the cupboard-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Rummage through the cupboard-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard

        "-Your possessions-" if not day == 1:
            label possessions:

            menu:
                "-Gift Items-" if cataloug_found:
                    label possessions_gift_items:
                        $ choices = []
                        python:
                            for i in gift_list:
                                if gift_item_inv[i.id] > 0:
                                    choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
                        $ choices.append(("-Never mind-", "nvm"))
                        $ result = renpy.display_menu(choices)
                        if result == "nvm":
                            jump possessions
                        else:
                            $ the_gift = result.image
                            show screen gift
                            with d3
                            ">[result.description]"
                            hide screen gift
                            with d3
                            jump possessions_gift_items

                "-Clothing-"if False:
                    label possessions_clothing:
                    menu:
                        "-Never mind-":
                            jump possessions

                "-Potion Items-" if False:
                    label possessions_potions:
                    menu:
                        "-Crafting Items-" if False:
                            label possessions_potion_items:
                            menu:
                                "-Never mind-":
                                    jump possessions_potions
                        "-Potions-":
                            label possessions_complete_potions:
                            menu:
                                "-Cum Addiction Potion-" if "Cum Addiction Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Ass Expansion Potion-" if "Ass Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Breast Expansion Potion-" if "Breast Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Cat Transformation Potion-" if "Cat Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Luna Transformation Potion-" if "Luna Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Lamia Transformation Potion-" if "Lamia Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Transparency Potion-" if "Transparency Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Never mind-":
                                    jump possessions_potions
                        "-Never mind-":
                            jump possessions

                "-Tentacle Scroll-" if tentacle_owned:
                    ">Should I use this scroll..."
                    menu:
                        "\"(Yes, let's do it!)\"":
                            jump tentacle_scene_intro
                        "\"(Not right now.)\"":
                            jump possessions
                "-Tentacle Scroll-" if tent_scroll and not tentacle_owned:
                    m "It's missing the key ingredient."
                    jump possessions

                "-The Ball Dress-" if "ball_dress" in gifts12 and not gave_the_dress:
                    $ the_gift = "images/store/01.png" # DRESS.
                    show screen gift
                    with d3
                    m "A fancy night dress I bought..."
                    m "I hope it's the right size."
                    hide screen gift
                    with d3
                    jump possessions

                #"-\"S.P.E.W.\" Badge-" if badge_01 == 1:
                    $ the_gift = "images/store/29.png" # S.P.E.W. BADGE
                    show screen gift
                    with d3
                    m "A \"S.P.E.W.\" Badge..."
                    hide screen gift
                    with d3
                    jump possessions

                #"-Fishnet stockings-" if nets == 1:
                    $ the_gift = "images/store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    hide screen gift
                    with d3
                    jump possessions

                #"-School miniskirt-" if have_miniskirt:
                    $ the_gift = "images/store/07.png" # MINISKIRT.
                    show screen gift
                    with d3
                    m "A school miniskirt... Improves grades drastically."
                    hide screen gift
                    with d3
                    jump possessions

                "-Dumbledor's Wine-([wine])" if wine >= 1:
                    $ the_gift = "images/store/27.png" # WINE.
                    show screen gift
                    with d3
                    ">A bottle of wine from professor dumbledore's personal stash..."
                    hide screen gift
                    with d3
                    jump possessions

                "-Unknown potion-([potions])" if  potions >= 1:
                    $ the_gift = "images/store/32.png" # HEALING POTION.
                    show screen gift
                    with d3
                    ">A potion of some sort..."
                    hide screen gift
                    with d3
                    jump possessions
                "Box with a puzzle on it" if found_puzzle_1 == True:
                    jump start_slide_puzzle
                "-Never mind-":
                    jump cupboard

        "-Potion crafting-" if shop_found:
            jump potion_menu

        "-Options-":
            menu:
                "-Save and Load-":
                    call screen save()

                "-Change Save Name-":
                    jump custom_save

                "-Change Game Difficulty-":
                    menu:
                        "-Enable Easy Difficulty-":                                 #CHANGE IN 00_HT_Start, Start of game option.
                            #if hardcore_difficulty_active:
                            #    "Warning: This will permanently remove your hardcore difficulty rewards!"
                            #    menu:
                            #        "Do you want to continue?"
                            #        "-Yes, change difficulty to easy-":
                            #            menu:
                            #                "Are you really sure?"
                            #                "-Yes, change difficulty to easy-":
                            #                    pass
                            #                "-No, go back-":
                            #                    jump day_main_menu
                            #        "-No, go back-":
                            #            jump day_main_menu
                            $ game_difficulty = 1
                            $ cheat_reading = True
                            $ hardcore_difficulty_active = False #removes hardcore rewards
                            "Game set to easy difficulty!"
                            "Increased gold reward from reports and other sources!" #CHANGE IN 01_hp_main_day and 15_mail.
                            "Rummaging through your cupboard is more rewarding!"    #CHANGE IN 11_cupboard, label rummaging.
                            "Snape will be more generous with Slytherin-points!"    #CHANGE IN 06_points.
                            "Hermione won't stay mad at you for as long!"           #CHANGE IN 01_hp_main_day.
                            jump day_main_menu
                        "-Enable Normal Difficulty-":
                            #if hardcore_difficulty_active:
                            #    "Warning: This will permanently remove your hardcore difficulty rewards!"
                            #    menu:
                            #        "Do you want to continue?"
                            #        "-Yes, change difficulty to normal-":
                            #            menu:
                            #                "Are you really sure?"
                            #                "-Yes, change difficulty to normal-":
                            #                    pass
                            #                "-No, go back-":
                            #                    jump day_main_menu
                            #        "-No, go back-":
                            #            jump day_main_menu
                            $ game_difficulty = 2
                            $ cheat_reading = False
                            $ hardcore_difficulty_active = False #removes hardcore rewards
                            "Game set to normal difficulty!"
                            jump day_main_menu
                        #"-Enable Hardcore Difficulty-": #Original Game Difficulty
                        #    "This will not add hardcore difficulty rewards!"
                        #    "To get hardcore difficulty rewards you will need to start a new game in hardcore difficulty and stay in said difficulty!"
                        #    $ game_difficulty = 3
                        #    $ cheat_reading = False
                        #    "Game set to hard difficulty!"
                        #    jump day_main_menu
                        #"-Cheat add hardcore difficulty rewards-":
                        #    if hardcore_difficulty_active:
                        #        ">Rewards are now disabled."
                        #        $ hardcore_difficulty_active = False
                        #    else:
                        #        ">Rewards are now active."
                        #        $ hardcore_difficulty_active = True
                        #        jump day_main_menu
                        "-Back-":
                            jump day_main_menu
                "-Replace Chibis with Sprites-" if not use_cgs:
                    ">The last two personal favours will use sprites now."
                    $ use_cgs = True
                    jump cupboard
                "-Replace Sprites with Chibis-" if use_cgs:
                    ">The last two personal favours will use chibi animations again."
                    $ use_cgs = False
                    jump cupboard
                "-Back-":
                    jump cupboard

        "-Cheats-" if cheats_active and day > 1:
            jump cheats

        "-Reset ALL Luna content-" if hat_known:
            $ reset_luna_content = True
            call luna_init
            call luna_progress_init
            $ reset_luna_content = False
            ">Luna content reset!"
            jump cupboard

        "-Never mind-":
            jump day_main_menu

label scrolls_menu:
    menu:
        "-Sacred scrolls volume I-" if cataloug_found:
            $ scrolls_range = range(1,16)
        "-Sacred scrolls volume II-" if cataloug_found:
            $ scrolls_range = range(16,31)
        "-Never Mind-":
            jump day_main_menu

    label sc_col_men:
    python:
        scrolls_menu = []
        for scroll in scrolls_range:
            sc = sacred_scrolls[scroll]
            if sscroll_[sc.id]:
                scrolls_menu.append( ("-S."+str(sc.id)+": "+str(sc.name)+"-", scroll) )
        scrolls_menu.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(scrolls_menu)

    if result == "nvm":
        jump scrolls_menu
    else:
        $ the_gift = "images/misc/extras/"+str(result)+".png" # SACRED SCROLL
        show screen gift
        show screen ctc
        with d3
        pause
        hide screen gift
        hide screen ctc
        with d3
        jump sc_col_men


label custom_save:
    $ temp_name = renpy.input("(Please enter the save name.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
    $ save_name = temp_name
    "Done."
    jump cupboard

label rummaging:

    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.

    hide screen genie
    show screen rum_screen
    with d3
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..."

    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ potions += 1
            call give_reward(">You found some sort of potion...","images/store/32.png")

            show screen genie
            hide screen rum_screen
            hide screen bld1
            with d3

            if daytime:
                jump night_start
            else:
                jump day_start

    if rum_times >= 7 and not cataloug_found:
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","images/store/31.png")

        show screen genie
        hide screen rum_screen
        hide screen bld1
        with d3

        if daytime:
            jump night_start
        else:
            jump day_start

    # Item Reward.
    $ random_number = renpy.random.randint(1, 5)

    if game_difficulty >= 2:               #Normal and hardcore difficulty
        if random_number in [1,2,3,4]: # Found something. 80% chance.
            jump rum_rewards
        else:
            ">...You find nothing of value."
            show screen genie
            hide screen rum_screen

            hide screen bld1
            with d3

            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
    else:                                  #Easy difficulty
        jump rum_rewards

label rum_rewards:
    $ random_number = renpy.random.randint(1, 20)

    if game_difficulty <= 2: #Easy and Normal difficulty.

        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            if random_number in [1,2]:
                call rum_block(Lollipop)
            elif random_number in [3]:
                call rum_block(PlushOwl)
            elif random_number in [4,5]:
                call rum_block(Chocolate)
            elif random_number in [6]:
                call rum_block(SexyLingerie)
            else:
                if random_number <= 12:
                    call rum_block("gold1")
                else:
                    call rum_block("wine")

        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            if random_number in [1,2]:
                call rum_block(Lollipop)
            elif random_number in [3]:
                call rum_block(PornMagazines)
            elif random_number in [4]:
                call rum_block(SexyLingerie)
            elif random_number in [5]:
                call rum_block(Chocolate)
            elif random_number in [6]:
                call rum_block(ViktorKrumPoster)
            else:
                if random_number <= 14:
                    call rum_block("gold2")
                else:
                    call rum_block("wine")

        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            if random_number in [1]:
                call rum_block(Vibrator)
            elif random_number in [2,3]:
                call rum_block(PackOfCondoms)
            elif random_number in [4,5]:
                call rum_block(Butterbeer)
            elif random_number in [6]:
                call rum_block(ViktorKrumPoster)
            else:
                if random_number <= 16:
                    call rum_block("gold3")
                else:
                    call rum_block("wine")

        if whoring >= 18: # Lv 7+
            if random_number in [1]:
                call rum_block(SpeedStick2000)
            elif random_number in [2,3,4]:
                call rum_block(Butterbeer)
            elif random_number in [5]:
                call rum_block(Chocolate)
            elif random_number in [6]:
                call rum_block(ViktorKrumPoster)
            elif random_number in [7]:
                call rum_block(AnalPlugs)
            elif random_number in [8]:
                call rum_block(ThestralStrapon)
            else:
                if random_number <= 18:
                    call rum_block("gold4")
                else:
                    call rum_block("wine")

    else: # Hardcore difficulty. # Sex items only.

        if random_number in [1]:
            call rum_block(PornMagazines)
        elif random_number in [2]:
            call rum_block(Vibrator)
        elif random_number in [3]:
            call rum_block(SexyLingerie)
        elif random_number in [4]:
            call rum_block(PackOfCondoms)
        elif random_number in [5]:
            call rum_block(AnalPlugs) #Butt Plug
        elif random_number in [6]:
            call rum_block(AnalBeads) #Snek
        elif random_number in [7]:
            call rum_block(JarOfLube)
        elif random_number in [8]:
            call rum_block(ThestralStrapon)
        elif random_number in [9]:
            call rum_block(BallGagAndCuffs)
        elif random_number in [10]:
            call rum_block(SexDollJoanne)
        else:
            if whoring >= 21: # Lv 7+
                call rum_block(Butterbeer)
            else:
                call rum_block("wine")

    show screen genie
    hide screen rum_screen

    hide screen bld1
    with d3

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label rum_block(item = None):
    if isinstance(item, gift_item):
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ gift_item_inv[item.id] += 1
        $ the_gift = item.image
        show screen gift
        with d3
        ">You found [item.name]..."
        ">[item.description]"
        hide screen gift
        with d3
    else:
        if "wine" in item:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ wine += 1
            $ the_gift = "images/store/27.png" # WINE
            show screen gift
            with d3
            ">You found a bottle of wine from professor dumbledore's personal stash..."
            hide screen gift
            with d3
        if "gold" in item:
            if item == "gold1":
                $ tmp_gold = gold1
            if item == "gold2":
                $ tmp_gold = gold2
            if item == "gold3":
                $ tmp_gold = gold3
            if item == "gold4":
                $ tmp_gold = gold4
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ the_gift = "images/store/28.png" # GOLD.
            show screen gift
            with d3
            ">You found [tmp_gold] gold..."
            $ gold += tmp_gold
            hide screen gift
            with d3
    return



######################
label already_did:
    show screen bld1
    with d3
    m "I already did that today..."
    hide screen bld1
    with d3
    return
