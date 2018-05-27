label door:

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    menu:
        "-Examine the door-" if not door_examined:
            $ door_examined = True
            hide screen genie
            call gen_chibi("stand","door","base")
            show screen chair_left #Empty chair near the desk.
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
                
        "{color=#858585}-Summon Hermione-{/color}" if summoning_hermione_unlocked and hermione_takes_classes or hermione_sleeping:
            if hermione_takes_classes:
                call nar(">Hermione is taking classes.")
                $ cust_char_1_enabled = True
                $ cust_char_2_enabled = True
                $ cust_char_3_enabled = True
                jump day_main_menu
            elif hermione_sleeping:
                call nar(">Hermione is already asleep.")
                jump night_main_menu
        
        "-Summon Hermione-" if summoning_hermione_unlocked and not hermione_takes_classes and not hermione_sleeping:
            if hermione_takes_classes:
                call nar(">Hermione is taking classes.")
                jump day_main_menu
            elif hermione_sleeping:
                call nar(">Hermione is already asleep.")
                jump night_main_menu
                
            else:
                jump summon_hermione

        "{color=#858585}-Summon Luna-{/color}" if luna_known and luna_unlocked and luna_busy:
            call nar(">Luna is unavailable.")
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Luna-" if luna_known and luna_unlocked and not luna_busy:
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # LUNA'S THEME (placeholder probably)
            jump luna_door

        "{color=#858585}-Summon Cho-{/color}" if cho_met and cho_busy:
            call nar(">Cho is unavailable.")
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Cho-" if cho_met and not cho_busy:
            call play_music("chipper_doodle") # CHO'S THEME (placeholder probably)
            jump cho_menu
                            
        "{color=#858585}-Summon Snape-{/color}" if hanging_with_snape and snape_busy:
            call nar(">Professor Snape is unavailable.")
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Snape-" if hanging_with_snape and not snape_busy:
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
            jump summon_snape
        "-Never mind-":
            jump day_main_menu
    


