

label start_ht:

    $ daytime = True
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

    $ p_level_04_active = False #When turns TRUE public favors of level 04 become available.
    $ p_level_05_active = False #When turns TRUE public favors of level 05 become available.
    $ p_level_06_active = False #When turns TRUE public favors of level 06 become available.
    $ p_level_07_active = False #When turns TRUE public favors of level 07 become available.

    $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. "Lazy Akabur bug". Turns FALSE after that.
    $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
    $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
    $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.
    $ ignore_warning = False




### JERKING OFF FLAGS ###
    $ cum_on_panties = False #True when choose to cum on Hermione's panties.


### EVENTS ###
    $ event08_happened = False #Turns TRUE after event_08 (Hermone visits first time).
    $ event09 = False #Turns TRUE when you let Hermione in during event_09. Otherwise she will keep coming every morning.
    $ event10 = False #Turns TRUE when you let Hermione in during event_10. Otherwise she will keep coming every morning.
    $ event11_happened = False #Turns TRUE after event_11
    $ event12_happened = False #Turns TRUE after event_12
    $ event13_happened = False #Turns TRUE after event_13
    $ event14_happened = False #Turns TRUE after event_14
    $ event15_happened = False #Turns TRUE after event_15
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
    $ map_unlocked = False # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.

    #Cupboard
    $ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    $ wine = 0 # Dumbledore's wine you find in the cupboard and use for "Snape dates".

    #Scrolls
    $ sscroll_ = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    #Books
    $ dear_waifu_completed_once = False # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
    $ found_dahrs_ticket_once = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.

    #Clothing
    $ vouchers = 0 #Shows the amount of DAHR's vouchers in your possession.
    $ gave_miniskirt = False #Turns True when Hermione has the miniskirt.
    $ gave_the_dress = False #Turns True when Hermione has the dress.





    call play_music("hedwigs_theme")
    show screen blkfade
    with d3
    pause 1

    hide screen blkfade
    show image "images/backgrounds/castle.png"
    with d9
    pause 3

    $ interface_color = "gray"
    $ menu_x = 0.5
    $ menu_y = 0.75

    if persistent.game_complete: # Offer for game+
        menu:
            "NEW GAME +" ">Would you like to carry over your gold and possessions from your previous playthrough?"
            "\"Yes, please.\"":
                # Code needed here for adding persistant items across games
                $ gold = gold + persistent.gold
                ">[persistent.gold] gold has been added to your founds."

                #if persistent.lolipop >= 1:
                #    $ candy = candy + persistent.lolipop # LOLIPOP.
                #    ">[persistent.lolipop] pieces of candy have been added to your possessions."

                #if persistent.choco >= 1:
                #    $ chocloate = chocolate + persistent.choco # CHOCOLATE.
                #    ">[persistent.choco] bars of chocolate have been added to your possessions."

                #if persistent.owl >= 1:
                #    $ owl = owl + persistent.owl # PLUSH OWL.
                #    ">[persistent.owl] plush owls have been added to your possessions."

                #if persistent.beer >= 1:
                #    $ beer = beer + persistent.beer # Beer.
                #    ">[persistent.beer] bottles of butterbeer have been added to your possessions."

                #if persistent.edu_mag >= 1:
                #    $ edu_mag = edu_mag + persistent.edu_mag # edu_mag.
                #    ">[persistent.edu_mag] issues of Educational magazines have been added to your possessions."

                #if persistent.girl_mag >= 1:
                #    $ girl_mag = girl_mag + persistent.girl_mag # girl_mag.
                #    ">[persistent.girl_mag] issues of girly magazines have been added to your possessions."

                #if persistent.adult_mag >= 1:
                #    $ adult_mag = adult_mag + persistent.adult_mag # adult_mag.
                #    ">[persistent.adult_mag] issues of adult magazines have been added to your possessions."

                #if persistent.porn_mag >= 1:
                #    $ porn_mag = porn_mag + persistent.porn_mag # porn_mag.
                #    ">[persistent.porn_mag] issues of porn magazines have been added to your possessions."

                #if persistent.krum >= 1:
                #    $ krum = krum + persistent.krum # VIKTOR KRUM POSTER.
                #    ">[persistent.krum] posters of Viktor Krum have been added to your possessions."

                #if persistent.lin >= 1:
                #    $ lingerie = lingerie + persistent.lin # lin.
                #    ">[persistent.lin] packs of sexy lingerie have been added to your possessions."

                #if persistent.con >= 1:
                #    $ condoms = condoms + persistent.con # CONDOMS.
                #    ">[persistent.con] packs of condoms have been added to your possessions."

                #if persistent.vib >= 1:
                #    $ vibrator = vibrator + persistent.vib # VIBRATOR.
                #    ">[persistent.vib] vibrators have been added to your possessions."

                #if persistent.lube >= 1:
                #    $ anal_lube = anal_lube + persistent.lube # ANAL LUBRICANT.
                #    ">[persistent.lube] jars of anal lubricant have been added to your possessions."

                #if persistent.gag >= 1:
                #    $ ballgag = ballgag + persistent.gag # BALLGAG.
                #    ">[persistent.gag] pairs of ball gags and handcuffs have been added to your possessions."

                #if persistent.anal_plugs >= 1:
                #    $ anal_plugs = anal_plugs + persistent.anal_plugs # ANAL PLUG.
                #    ">[persistent.anal_plugs] assortments of anal plugs have been added to your possessions."

                #if persistent.strap >= 1:
                #    $ strap_on = strap_on + persistent.strap # STRAP-ON.
                #    ">[persistent.strap] Thestral Strap-ons have been added to your possessions."

                #if persistent.broom >= 1:
                #    $ broom = broom + persistent.broom # BROOM.
                #    ">[persistent.broom] \"Lady Speed Stick-2000\" brooms have been added to your possessions."

                #if persistent.doll >= 1:
                #    $ sex_doll = sex_doll + persistent.doll # SEXDOLL.
                #    ">[persistent.doll] \"Joanne\" sex dolls have been added to your possessions."

                if persistent.wine >= 1:
                    $ wine = wine + persistent.wine # WINE.
                    ">[persistent.wine] bottles of Dumbledore's wine have been added to your possessions."

                if persistent.ss_ is not None:
                    $ sscroll_ = persistent.ss_
                    $ tmp = len(persistent.ss_)
                    ">[tmp] scrolls have been added to your possessions."


            "\"No need.\"":
                pass

    label choose_your_difficulty:
    menu:
        "Choose a difficutly."
        "-Play with easy difficulty-":
            ">Increased gold and Slythering-points gain.\n>You will always find items or gold in your cupboard."
            ">Hermione's bad-mood will decrease faster.\n>Books can be read in one go."
            menu:
                ">Easy difficulty."
                "-Choose this difficulty-":
                    ">Game set to easy!"
                    $ game_difficulty = 1
                    $ hardcore_difficulty_active = False
                    $ cheat_reading = True
                "-Choose something else-":
                    jump choose_your_difficulty
        "-Play with normal difficulty-":
            menu:
                ">Normal difficulty."
                "-Choose this difficulty-":
                    ">Game set to normal!"
                    $ game_difficulty = 2
                    $ hardcore_difficulty_active = False
                    $ cheat_reading = False
                "-Choose something else-":
                    jump choose_your_difficulty
        #"-Play with hardcore difficulty-": #Not implemented yet.
        #    ">Hardcore difficulty. You gold and Slythering-points gain has been lowered.\n>All hints and guides have been disabled."
        #    ">Additional rewards and dialogue choices have been added.\n>Those will be removed when changing difficulty!"
        #    menu:
        #        ">Hardcore difficulty."
        #        "-Choose this difficulty-":
        #            ">Game set to hardcore!"
        #            $ game_difficulty = 3
        #            $ hardcore_difficulty_active = True #hardcore rewards #gets reset on difficulty change
        #            $ cheat_reading = False
        #        "-Choose something else-":
        #            jump choose_your_difficulty

    if not hardcore_difficulty_active:
        menu:
            "ACTIVATE CHEATS" ">Cheats can be found in the cupboard menu."
            "-Activate Cheats-":
                $ cheats_active = True
                $ avogadro_law = True
            "-Disable Cheats-":
                $ cheats_active = False
                $ avogadro_law = False

    menu:
        "Use chibi animations or image sprites." ">This will only affect a couple of scenes.\n>This can be changed in the cupboard menu."
        "-Use chibis-":
            $ use_cgs = False
        "-Use sprites-":
            $ use_cgs = True

    menu:
        ">Would you like to skip the intro?"
        "-Play the intro-":
            jump intro
        "-Skip the intro-":
            jump hp
        "-Skip to after the duel-" if cheats_active:
            $ skip_duel = True
            jump hp
        "-Skip to Hermione-" if cheats_active:
            $ skip_to_hermione = True
            jump hp




### GAME STARTS HERE ###

label hp:

    stop music fadeout 1
    hide image "images/backgrounds/castle.png"
    show screen blkfade
    with d7
    pause 1.2


$ interface_color = "gold"
$ day = 0



### CHARACTER INIT RESET ###
$ reset_persistants            = True

#Genie
call  reset_genie_base

#Snape
call snape_init
call snape_progress_init

#Hermione
call reset_hermione_base
call reset_hermione_clothing

call her_clothing_lists_init #Everything resets here!
call her_progress_init #Everything resets here!

#Luna
call luna_init
call luna_progress_init

#Cho
call cho_init
call cho_progress_init

#Susan
call susan_init
call susan_progress_init

#Astoria
call astoria_init
call astoria_progress_init

#Tonks
call tonks_init
call tonks_progress_init

#Store
call store_init
call store_items_init

#Wardrobe Reset
call wardrobe_init


### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
$ day_of_week = 0 #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
$ report_chapters = 0 #Shows how many chapters of a current report has been completed so far. Resets to zero when report is finished.
$ finished_report = 0 #Shows amount of completed reports.
$ job_lvl = 1 #Show how many reports you are allowed to complete per week.


###Miscellaneous flags###
$ hold_all_the_events_please = False #When TRUE all the story events will be put on hold.
$ phoenix_is_fed = False #When True the graphic of bird food being displayed on top of the phoenix food can.
$ fire_in_fireplace = False #When True there is a fire going in the fireplace.
$ fawkes_intro_done = False


$ gifts12 = []




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

$ hermione_desperate_done = False
$ gave_tinyminiskirt = False
$ addicted = False

$ reset_persistants            = False


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

$ menu_x = 0.5
$ menu_y = 0.5


jump day_start
