label start_wt:
    $ daytime = False
    $ gold = 0
    $ rum_times = 0 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.

    ### HERMIONE_MAIN SCREN FLAGS ###
    $ only_upper = False #When true, legs are not displayed in the hermione_main screen.
    $ no_blinking = False #When True - blinking animation is not displayed.
    $ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    $ legs_02 = False # Turns TRUE when miniskirt is activated.

    $ current_payout = 0 #Used when haggling about price of th favor.

    $ snape_invited_to_watch = False #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
    $ invited_snape_once_already = False #In the "Dance for me" event, after you send Hermione to invite Snape to watch for the first time - turns TRUE.

    $ uni_sperm = False #Triggers universal sperm to show on hermione_main screen.
    $ days_without_an_event = 0 #Counts days since last (any) event took place.

    $ ask_me_once = False #Turns true after Hermione asks you about your true identity, during sex.

    $ tiara = False #When TRUE tiara is displayed on h_head2 and hermione_main screens.

    $ public_whore_ending = False #If TRUE the game will end with "Public Whore Ending".

    $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. Turns FALSE after that.
    $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
    $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
    $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.
    $ ignore_warning = False



### EVENTS ###
    $ event08_happened = False #Turns TRUE after hermione_intro_E1 (Hermone visits first time).
    $ event09 = False #Turns TRUE when you let Hermione in during hermione_intro_E2. Otherwise she will keep coming every morning.
    $ event10 = False #Turns TRUE when you let Hermione in during event_10. Otherwise she will keep coming every morning.
    $ event11_happened = False #Turns TRUE after hermione_intro_E3
    $ event12_happened = False #Turns TRUE after hermione_intro_E4
    $ event13_happened = False #Turns TRUE after hermione_intro_E5
    $ event14_happened = False #Turns TRUE after hermione_intro_E6
    $ event15_happened = False #Turns TRUE after hermione_intro_E7
    $ event16_happened = False #Turns TRUE after event_16

    $ event_chairman_happened = False #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    $ snape_against_chairman_hap = False # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ have_no_dress_hap = False #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ sorry_for_hesterics = False # Turns TRUE after Hermione comes and apologizes for the day (event) before.


    $ slytherin = 180 #Shows amount of points the Slytherin house has.
    $ gryffindor = 53 #Shows amount of points the Gryffindor house has.
    $ hufflepuff = 25 #Shows amount of points the Hufflepuff house has.
    $ ravenclaw = 31 #Shows amount of points the Ravenclaw house has.





    #Misc Flags
    $ lock_public_favors = False #Turns True if reached her_whoring level 05 while public
    $ touched_by_boy = False #Turns true if sent Hermione to get touched by a boy at least once.

    #Duel
    $ potions = 0 #Amount of healing potions Genie has in stock.

    #Map
    call reset_map_init

    #Cheats
    call reset_cheats_init

    #Cupboard
    $ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    $ wine = 0 # Dumbledore's wine you find in the cupboard and use for "Snape dates".

    #Books
    $ found_voucher = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.

    #Clothing
    $ gave_miniskirt = False #Turns True when Hermione has the miniskirt.
    $ gave_the_dress = False #Turns True when Hermione has the dress.





    call play_music("hedwigs_theme")
    show screen blkfade
    with d3
    pause 1

    hide screen blkfade
    show image "images/rooms/_bg_/castle.png"
    with d9

    $ interface_color = "gray"
    $ menu_x = 0.5
    $ menu_y = 0.75

    label choose_your_difficulty:
    menu:
        "-Play with easy difficulty-":
            ">Increased gold and Slytherin-points gain. You will also always find items or gold in your cupboard."
            ">Hermione's bad-mood will decrease faster, and books can be read in one go."
            menu:
                "-Confirm-":
                    ">Game set to easy!"
                    $ game_difficulty = 1
                    $ cheat_reading = True
                "-Choose something else-":
                    jump choose_your_difficulty
        "-Play with normal difficulty-":
            menu:
                "-Confirm-":
                    ">Game set to normal!"
                    $ game_difficulty = 2
                    $ cheat_reading = False
                "-Choose something else-":
                    jump choose_your_difficulty
        "-Play with hardcore difficulty-" if persistent.game_complete:
            ">Hardcore difficulty. Your gold and Slytherin-points gain has been lowered.\n>All hints and guides have been disabled."
            ">Additional rewards and dialogue choices have been added."
            menu:
                "-Confirm-":
                    ">Game set to hardcore!"
                    $ game_difficulty = 3
                    $ cheat_reading = False
                "-Choose something else-":
                    jump choose_your_difficulty

    if persistent.game_complete and game_difficulty <= 2: # Offer for game+
        menu:
            "NEW GAME +" ">Would you like to carry over your gold and possessions from your previous playthrough?"
            "-Yes please-":
                # Code needed here for adding persistant items across games
                $ gold = gold + persistent.gold
                ">[persistent.gold] gold has been added to your founds."

                #$ candy_gift_list = persistent.candy_gift_list
                #$ drink_gift_list = persistent.drink_gift_list
                #$ mag_gift_list   = persistent.mag_gift_list
                #$ toy_gift_list   = persistent.toy_gift_list
                #">All previously bought gift items have been added to your possessions."

                if persistent.wine >= 1:
                    $ wine = wine + persistent.wine # WINE.
                    ">[persistent.wine] bottles of Dumbledore's wine have been added to your possessions."

                #$ scroll_list_A = persistent.scroll_list_A
                #$ scroll_list_B = persistent.scroll_list_B
                #$ scroll_list_C = persistent.scroll_list_C
                #">Your unlocked scrolls have been added to your possessions."

            "-No need-":
                pass

    if game_difficulty <= 2:
        menu:
            "ACTIVATE CHEATS" ">Cheats can be found in the options menu at the top left of the screen."
            "-Activate Cheats-":
                $ cheats_active = True
            "-Disable Cheats-":
                $ cheats_active = False

    menu:
        "Animations" ">Would you like to use chibi animations, or CG images when available?\nThis can be changed in the preferences menu."
        "-Use chibis-":
            $ use_cgs = False
        "-Use CG images-":
            $ use_cgs = True

    if cheats_active or persistent.game_complete:
        menu:
            ">Would you like to skip early sections of the game?"
            "-No, play the intro-":
                pass
            "-Skip to after the duel-" if cheats_active or persistent.game_complete:
                $ skip_duel = True
            "-Skip to Hermione-" if cheats_active or persistent.game_complete:
                $ skip_to_hermione = True
            "-Skip to {color=#007f00}AFTER{/color} Hermione events-" if config.developer:
                $ skip_to_hermione = True
                $ skip_after_hermione = True
                

    show screen achievement_block()

    ### GAME STARTS HERE ###
    stop music fadeout 1
    hide image "images/rooms/_bg_/castle.png"
    show screen blkfade
    with d7
    pause 1.2


    if not persistent.nightmode:
        $ interface_color = "gold"
    $ day = 0

    ### CHARACTER INIT RESET ###
    $ reset_persistants = True
    call reset_genie_base
    call snape_init
    call snape_progress_init
    call reset_hermione_base
    call reset_hermione_clothing
    call her_clothing_lists_init #Everything resets here!
    call her_progress_init #Everything resets here!
    call luna_init
    call luna_progress_init
    call cho_init
    call cho_progress_init
    call susan_init
    call susan_progress_init
    call astoria_init
    call astoria_progress_init
    call tonks_init
    call tonks_progress_init
    call store_init
    call store_items_init
    call wardrobe_init
    $ reset_persistants = False

    ### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
    $ day_of_week = 0 #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ report_chapters = 0 #Shows how many chapters of a current report has been completed so far. Resets to zero when report is finished.
    $ finished_report = 0 #Shows amount of completed reports.

    ###Miscellaneous flags###
    $ phoenix_is_fed = False #When True the graphic of bird food being displayed on top of the phoenix food can.
    $ fire_in_fireplace = False #When True there is a fire going in the fireplace.

    #Event - Examine Room
    $ desk_examined = False #Turns True when you did examine you desk on day one.
    $ cupboard_examined = False
    $ bird_examined = False
    $ door_examined = False
    $ fireplace_examined = False

    #Map
    $ inn_intro = True
    $ pitch_open = True
    $ attic_open = False
    $ clothes_store_intro_done = False

    $ tentacle_cosmetic = False
    $ addicted = False
    
    ### CHEATS / SKIPPING ###
    if skip_duel or skip_to_hermione:
        $ bird_examined = True
        $ desk_examined = True
        $ cupboard_examined = True
        $ door_examined = True
        $ fireplace_examined = True
        $ achievement.unlock("start", True)
        if skip_duel:
            $ skip_duel = False
            $ rum_times = 3 #7 unlocks map!
            $ day = 5

        if skip_to_hermione:
            $ skip_to_hermione = False
            #Add vars
            $ snape_unlocked = True
            $ achievement.unlock("unlocksna", True)
            $ event08_happened = True
            $ event09 = True #You let Hermione in. This event will stop looping now.
            $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
            $ event11_happened = True #Allows next event to start.
            $ event12_happened = True #Allows next event to start.
            $ event13_happened = True #Allows next event to start.
            $ rum_times = 6 #7 unlocks map!
            $ day = 14
            
            if skip_after_hermione:
                $ hermione_unlocked = True
                $ achievement.unlock("unlockher", True)
                $ day = 15
                $ tutoring_hermione_unlocked = True
                $ event14_happened = True
                $ hermione_favors = True
                $ event15_happened = True
                jump day_start
            call hermione_intro_E6 #returns

    ### START ANIMATION ###
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    $ weather_gen = 2
    $ show_weather()

    call room("main_room")
    call gen_chibi("sit_behind_desk")
    pause.1
    hide screen blkfade
    with d3

    call teleport("desk")

    call reset_menu_position

    jump day_start



### EVENT 0 ###

# First event in the game. Gennie finds himself at the desk.
label genie_intro_E1:
    #$ genie_intro.complete("E1")

    call bld
    m "..................?"
    m "Your majesty?"
    m "......................................................."
    g4 "I did it again, didn't I?"
    g4 "Teleported myself to who knows where..."
    m "What's with those ingredients?"
    m "They seem to be way more potent than I thought."
    m "Well, whatever this place is I have no business here..."
    m "Better undo the spell and return to the shop before the princess gets angry with me again..."
    m "....................."
    m "Although..."
    m "There is something odd about this place... it's..."
    m "It's almost brimming with...."
    g4 "{size=+5}MAGIC?!{/size}"
    m "Yes... magic, I can feel it. So powerful and yet somehow..."
    m "....alien."
    m "Interesting..."
    m "I think I will stick around for a little bit..."

    $ achievement.unlock("start")

    return


# Owl intro.
label genie_intro_E2:
    #$ genie_intro.complete("E2")
    call play_sound("owl")
    show screen owl
    call bld
    m "What? An owl?"
    hide screen bld1
    with d3

    return
