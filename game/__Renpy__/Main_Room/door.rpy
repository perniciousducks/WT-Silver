label door:

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    menu:
        "-Examine the door-" if not door_examined:
            $ door_examined = True
            hide screen genie
            show screen chair_left #Empty chair near the desk.
            show screen chair_right
            call gen_chibi("stand","door","base") from _call_gen_chibi_110
            show screen desk
            with Dissolve(0.5)
            m "A sturdy looking door..."
            m "I wonder what's behind it."
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone8
                    with d3
                    call play_sound("knocking") from _call_play_sound_185
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

            call gen_chibi("hide") from _call_gen_chibi_111
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
                
                
                
        "{color=#858585}-Summon Astoria-{/color}" if astoria_busy and astoria_unlocked:
            if daytime:
                call nar(">Astoria is taking classes.") from _call_nar_554
                jump day_main_menu
            else:
                call nar(">Astoria is already asleep.") from _call_nar_555
                jump night_main_menu
        
        "-Summon Astoria-" if not astoria_busy and astoria_unlocked: #Summoning after intro events done.
            call play_music("chipper_doodle") from _call_play_music_207
            jump summon_astoria
            
            

        "{color=#858585}-Summon Susan-{/color}" if susan_unlocked and susan_busy:
            if daytime:
                call nar(">Susan is taking classes.") from _call_nar_556
                jump day_main_menu
            else:
                call nar(">Susan is already asleep.") from _call_nar_557
                jump night_main_menu
        
        "-Summon Susan-" if susan_unlocked and not susan_busy:
            jump summon_susan

            
            
        "{color=#858585}-Summon Hermione-{/color}" if summoning_hermione_unlocked and hermione_takes_classes or hermione_sleeping:
            if hermione_takes_classes:
                call nar(">Hermione is taking classes.") from _call_nar_558
                $ cust_char_1_enabled = True
                $ cust_char_2_enabled = True
                $ cust_char_3_enabled = True
                jump day_main_menu
            elif hermione_sleeping:
                call nar(">Hermione is already asleep.") from _call_nar_559
                jump night_main_menu
        
        "-Summon Hermione-" if summoning_hermione_unlocked and not hermione_takes_classes and not hermione_sleeping:
            jump summon_hermione

                
                
        "{color=#858585}-Summon Luna-{/color}" if luna_known and luna_unlocked and luna_busy:
            if daytime:
                call nar(">Luna is taking classes.") from _call_nar_560
                jump day_main_menu
            else: 
                call nar(">Luna is already asleep.") from _call_nar_561
                jump night_main_menu
            
        "-Summon Luna-" if luna_known and luna_unlocked and not luna_busy:
            call play_music("dark_fog") from _call_play_music_208 # LUNA'S THEME (placeholder probably)
            jump luna_door

            
            
        "{color=#858585}-Summon Cho-{/color}" if cho_met and cho_busy:
            if daytime:
                call nar(">Cho is taking classes.") from _call_nar_562
                jump day_main_menu
            else: 
                call nar(">Cho is already asleep.") from _call_nar_563
                jump night_main_menu
            
        "-Summon Cho-" if cho_met and not cho_busy:
            call play_music("chipper_doodle") from _call_play_music_209 # CHO'S THEME (placeholder probably)
            jump cho_menu
                  

                  
        "{color=#858585}-Summon Snape-{/color}" if hanging_with_snape and snape_busy:
            call nar(">Professor Snape is unavailable.") from _call_nar_564
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Snape-" if hanging_with_snape and not snape_busy:
            call play_music("dark_fog") from _call_play_music_210 # SNAPE'S THEME
            jump summon_snape
            
            
            
        "{color=#858585}-Summon Tonks-{/color}" if tonks_unlocked and tonks_busy:
            call nar(">Tonks is unavailable.") from _call_nar_565
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
        
        "-Summon Tonks-" if tonks_unlocked and not tonks_busy:
            jump summon_tonks
            
            
        "-Never mind-":
            jump day_main_menu
    


