

label summon_tonks:
    
    call play_sound("door") from _call_play_sound_89
    $ menu_x = 0.5
    $ menu_y = 0.5

    #ADD Tonks chibi here.
    
    call ton_main("You've called, [ton_genie_name]?","base","base","base","mid",xpos="base",ypos="base") from _call_ton_main_135
    
    label tonks_requests:
    
    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!
    
    menu:
        "-Talk-":
            if not chitchated_with_tonks: 
                call tonks_chit_chat from _call_tonks_chit_chat 
                #jump tonks_talk
                jump tonks_requests
            else:
                #jump tonks_talk
                jump tonks_requests
            
            
        "{color=#858585}-Send Astoria with her-{/color}" if spells_locked and (astoria_busy or not daytime):
            if daytime:
                call nar(">Astoria is currently unavailable.") from _call_nar_223
            else:
                call nar(">It is too late to send Astoria with Tonks today! Try again tomorrow.") from _call_nar_224
            jump tonks_requests
        "-Send Astoria with her-" if spells_locked and daytime and not astoria_busy:
            call blkfade from _call_blkfade_86
            call nar(">You summon Astoria.") from _call_nar_225
            pause.5
            hide screen blkfade
            call ast_main("Hi, [ast_genie_name]!","grin","base","base","mid",xpos="mid",ypos="base",trans="fade") from _call_ast_main_475
            call ast_main("Uhm, hello, Miss Tonks.","worried","base","worried","R") from _call_ast_main_476
            call ton_main("Hello, [ton_astoria_name].","horny","base","raised","L") from _call_ton_main_136
            call ast_main("{size=-2}[ast_tonks_name]...{/size}","pout","narrow","narrow","L") from _call_ast_main_477
            if one_out_of_three == 1:
                m "Astoria, I want you to spend the day with Miss Tonks again."
            if one_out_of_three == 2:
                m "Miss Greengrass, you are going to spend some quality time with Miss Tonks today."
            if one_out_of_three == 3:
                m "Girl, you're going with Miss Tonks today. Like it or not..."
            call ast_main("Again?! Do I really have to?","pout","base","worried","mid") from _call_ast_main_478
            m "Yes."
            call ton_main("Don't worry [ton_astoria_name]. It's gonna be fun!","base","base","base","L") from _call_ton_main_137
            call ton_main("Take care, [ton_genie_name].","base","base","base","mid") from _call_ton_main_138
            call ast_main("...","pout","base","worried","L") from _call_ast_main_479
            call play_sound("door") from _call_play_sound_90
            hide screen tonks_main
            with d3
            
            pause.5
            call play_sound("door") from _call_play_sound_91
            hide screen astoria_main
            hide screen bld1
            with d3
            
            $ astoria_busy = True
            $ tonks_busy = True
            
            $ astoria_tonks_event_in_progress = True
            
            call play_music("brittle_rille") from _call_play_music_99 #Day Theme
            jump day_main_menu
            
            
        "-Never mind-":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)

            if daytime:
                ton "Alright, back to work then..."
            else: 
                ton "Sweet dreams, [ton_genie_name]."

            $ tonks_busy = True
            hide screen bld1
            hide screen tonks_main
            with d3
            call play_sound("door") from _call_play_sound_92

            if daytime:
                call play_music("brittle_rille") from _call_play_music_100 #Day Theme
                jump day_main_menu
            else: 
                call play_music("manatees") from _call_play_music_101 #Night Theme
                jump night_main_menu