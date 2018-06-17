

label summon_tonks:
    
    call play_sound("door") 
    $ menu_x = 0.5
    $ menu_y = 0.5

    #ADD Tonks chibi here.
    
    call ton_main("You've called, [ton_genie_name]?","base","base","base","mid",xpos="base",ypos="base") 
    
    label tonks_requests:
    
    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!
    
    menu:
        "-Talk-":
            if not chitchated_with_tonks: 
                call tonks_chit_chat 
                #jump tonks_talk
                jump tonks_requests
            else:
                #jump tonks_talk
                jump tonks_requests
            
            
        "{color=#858585}-Send Astoria with her-{/color}" if spells_locked and (astoria_busy or not daytime):
            if daytime:
                call nar(">Astoria is currently unavailable.") 
            else:
                call nar(">It is too late to send Astoria with Tonks today! Try again tomorrow.") 
            jump tonks_requests
        "-Send Astoria with her-" if spells_locked and daytime and not astoria_busy:
            call blkfade 
            call nar(">You summon Astoria.") 
            pause.5
            hide screen blkfade
            call ast_main("Hi, [ast_genie_name]!","grin","base","base","mid",xpos="mid",ypos="base",trans="fade") 
            call ast_main("Uhm, hello, Miss Tonks.","worried","base","worried","R") 
            call ton_main("Hello, [ton_astoria_name].","horny","base","raised","L") 
            call ast_main("{size=-2}[ast_tonks_name]...{/size}","pout","narrow","narrow","L") 
            if one_out_of_three == 1:
                m "Astoria, I want you to spend the day with Miss Tonks again."
            if one_out_of_three == 2:
                m "Miss Greengrass, you are going to spend some quality time with Miss Tonks today."
            if one_out_of_three == 3:
                m "Girl, you're going with Miss Tonks today. Like it or not..."
            call ast_main("Again?! Do I really have to?","pout","base","worried","mid") 
            m "Yes."
            call ton_main("Don't worry [ton_astoria_name]. It's gonna be fun!","base","base","base","L") 
            call ton_main("Take care, [ton_genie_name].","base","base","base","mid") 
            call ast_main("...","pout","base","worried","L") 
            call play_sound("door") 
            hide screen tonks_main
            with d3
            
            pause.5
            call play_sound("door") 
            hide screen astoria_main
            hide screen bld1
            with d3
            
            $ astoria_busy = True
            $ tonks_busy = True
            
            $ astoria_tonks_event_in_progress = True
            
            call play_music("brittle_rille") #Day Theme
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
            call play_sound("door") 

            if daytime:
                call play_music("brittle_rille") #Day Theme
                jump day_main_menu
            else: 
                call play_music("manatees") #Night Theme
                jump night_main_menu