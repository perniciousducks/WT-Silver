label door:

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    menu:
        "-Examine the door-" if not door_examined:
            $ door_examined = True
            hide screen genie
            show screen chair_left #Empty chair near the desk.
            show screen chair_right
            call gen_chibi("stand","door","base")
            show screen desk
            with Dissolve(0.5)
            m "A sturdy looking door..."
            m "I wonder what's behind it."
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone8
                    with d3
                    call play_sound("knocking")
                    "*Knock-knock-knock*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "No reply..."
                    jump examining_the_door
                "-Put your ear on it-":
                    show screen blktone8
                    with d3
                    ">You put your ear on the door and listen intently..."
                    m "I don't hear anything."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "-Kick the door-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Thump!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "This door could take a thousand kicks like that and it still wouldn't break..."
                    m "It doesn't look like it's locked though..."
                    jump examining_the_door
                "-Leave it alone-":
                    m "Who knows what kind of dangers could be lurking behind that door?"
                    m "I think I'll let it be for now..."
                    pass

            call gen_chibi("hide")
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            show screen genie
            with d3
            jump day_main_menu

        "-Explore the Castle-" if door_examined:
            if cataloug_found:
                hide screen main_room_menu
                call screen map_screen
            else:
                m "I would almost certainly get lost without a map."
                m "Maybe there is one hidden somewhere in this room..."
                jump day_main_menu


        #Astoria
        "{color=#858585}-Summon Astoria-{/color}" if astoria_busy and astoria_unlocked:
            if daytime:
                call nar(">Astoria is taking classes.")
                jump day_main_menu
            else:
                call nar(">Astoria is already asleep.")
                jump night_main_menu
        "-Summon Astoria-" if not astoria_busy and astoria_unlocked: #Summoning after intro events done.
            call play_music("chipper_doodle")
            jump summon_astoria


        #Susan
        "{color=#858585}-Summon Susan-{/color}" if susan_unlocked and susan_busy:
            if daytime:
                call nar(">Susan is taking classes.")
                jump day_main_menu
            else:
                call nar(">Susan is already asleep.")
                jump night_main_menu
        "-Summon Susan-" if susan_unlocked and not susan_busy:
            jump summon_susan


        #Hermione
        "{color=#858585}-Summon Hermione-{/color}" if hermione_unlocked and hermione_busy:
            if daytime:
                call nar(">Hermione is taking classes.")
                $ cust_char_1_enabled = True
                $ cust_char_2_enabled = True
                $ cust_char_3_enabled = True
                jump day_main_menu
            else:
                call nar(">Hermione is already asleep.")
                jump night_main_menu
        "-Summon Hermione-" if hermione_unlocked and not hermione_busy:
            jump summon_hermione



        #Luna
        "{color=#858585}-Summon Luna-{/color}" if luna_known and luna_unlocked and luna_busy:
            if daytime:
                call nar(">Luna is taking classes.")
                jump day_main_menu
            else:
                call nar(">Luna is already asleep.")
                jump night_main_menu
        "-Summon Luna-" if luna_known and luna_unlocked and not luna_busy:
            if not luna_reverted:
                call play_music("dark_fog") # LUNA'S THEME (placeholder probably)
            else:
                call play_music("chipper_doodle") # LUNA'S THEME (placeholder probably)
            jump luna_door


        #Cho
        "{color=#858585}-Summon Cho-{/color}" if cho_unlocked and cho_busy:
            if daytime:
                call nar(">Cho is taking classes.")
                jump day_main_menu
            else:
                call nar(">Cho is already asleep.")
                jump night_main_menu
        "-Summon Cho-" if cho_unlocked and not cho_busy:
            call play_music("chipper_doodle") # CHO'S THEME (placeholder probably)
            jump cho_menu


        #Snape
        "{color=#858585}-Summon Snape-{/color}" if snape_unlocked and snape_busy:
            call nar(">Professor Snape is unavailable.")
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
        "-Summon Snape-" if snape_unlocked and not snape_busy:
            call play_music("dark_fog") # SNAPE'S THEME
            jump summon_snape


        #Tonks
        "{color=#858585}-Summon Tonks-{/color}" if tonks_unlocked and tonks_busy:
            call nar(">Tonks is unavailable.")
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
        "-Summon Tonks-" if tonks_unlocked and not tonks_busy:
            jump summon_tonks


        #NVM
        "-Never mind-":
            jump day_main_menu
