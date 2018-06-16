

label summon_astoria:

    call load_astoria_clothing_saves

    call play_sound("door") #Sound of a door opening.

    #Events
    if spells_unlocked and not susan_unlocked:
        $ susan_unlocked = True
        $ third_curse_got_cast = True
        $ spells_locked = True
        jump astoria_susan_intro
        
    ### RANDOM CLOTHING EVENTS ###
    call astoria_door_event

    call update_ast_uniform
    call update_sus_uniform

    #call ast_chibi("stand","mid","base")
    
    if one_of_ten < 4:
        call ast_main("Heya, [genie_name]!","tongue_silly","wink","base","mid",xpos="base",ypos="base")
    elif one_of_ten < 7:
        call ast_main("Hello, [genie_name].","smile","base","base","mid",xpos="base",ypos="base")
    else:
        call ast_main("Hi, [genie_name]!","grin","angry","base","mid",xpos="base",ypos="base")

    $ astoria_busy = True
    
    label astoria_requests:

    $ menu_x = 0.1 #Menu is moved to the left.
    $ menu_y = 0.5 #Menu is moved to the middle.

    $ wardrobe_active = False

    menu:
        "-Talk-":
            if not chitchated_with_astoria: 
                call astoria_chit_chat 
                jump astoria_talk
            else:
                jump astoria_talk
                
        "-Spell Training-" if snape_gave_spellbook:
            if not astoria_book_intro_happened:
                $ astoria_book_intro_happened = True
                jump astoria_book_intro
            else:
                jump astoria_spell_training
        "{color=#858585}-Spell Training-{/color}" if spells_unlocked and not snape_gave_spellbook:
            call nar(">You will need to find a book for that.")
            jump astoria_requests
        "{color=#858585}-Hidden-{/color}" if not spells_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump astoria_requests
            
        "-Use a Spell-" if spells_unlocked and not spells_locked:
            label astoria_target_select:
            menu:
                ">Choose a target."
                "-Susan-" if not susan_busy:
                    jump curse_susan
                "{color=#858585}-Susan-{/color}" if susan_busy:
                    call nar(">Susan is unavailable.")
                    jump astoria_target_select
                "{color=#858585}-Hermione-{/color}": #Hermione?
                    call nar(">This feature has not been added yet.")
                    jump astoria_target_select
                "-Never mind-":
                    jump astoria_requests
            
            label curse_susan:
                menu:
                    ">Choose your curse."
                    "-Imperio-" if astoria_spells[0] >= 1:
                        jump imperio_spell_1
                    "-Imperio Tempus-" if astoria_spells[0] >= 2:
                        jump imperio_spell_2
                    "-IMPERIO MAXIMUS-" if astoria_spells[0] >= 3:
                        jump imperio_spell_3
                    "-Imperio Tempo-" if susan_wardrobe_unlocked and not susan_imperio_influence:
                        "Developer Note:" ">This is a temporary spell that will most likely get remove in the future.\n>It currently unlocks Susan's wardrobe for a short amount of time."
                        jump susan_imperio
                    "{color=#858585}-Imperio Tempo-{/color}" if susan_wardrobe_unlocked and susan_imperio_influence:
                        call nar(">Susan is still under the influence of this curse!")
                        jump curse_susan
                        
                    "{color=#858585}-Hidden-{/color}" if not susan_wardrobe_unlocked:
                        call nar(">You haven't unlocked this spell yet.")
                        jump astoria_target_select
                    "{color=#858585}-Hidden-{/color}" if astoria_spells[0] < 1:
                        call nar(">You haven't unlocked this spell yet.")
                        jump astoria_target_select
                    "{color=#858585}-Hidden-{/color}" if astoria_spells[0] < 2:
                        call nar(">You haven't unlocked this spell yet.")
                        jump astoria_target_select
                    "{color=#858585}-Hidden-{/color}" if astoria_spells[0] < 3:
                        call nar(">You haven't unlocked this spell yet.")
                        jump astoria_target_select
                        
                    "-Back-":
                        jump astoria_target_select
        "{color=#858585}-Use a Spell-{/color}" if tonks_unlocked and spells_locked:
            call nar(">You have recently used an unforgivable curse!\n>Tonks will want to have a word with you before you can use another.")
            jump astoria_requests
        "{color=#858585}-Use a Spell-{/color}" if not tonks_unlocked:
            call nar(">You'll need to find a way to deal with the Ministry first before casting any more curses!")
            jump astoria_requests
            
            
        "{color=#858585}-Hidden-{/color}" if not astoria_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump astoria_requests
        "-Inventory-" if astoria_wardrobe_unlocked:
            $ active_girl = "astoria"

            call load_astoria_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ wardrobe_active = 1 #True
            call ast_main(xpos="wardrobe",ypos="base")
            call screen wardrobe
            
        "-Dismiss her-":
            if daytime:
                call ast_main("I will go back to classes then, [ast_genie_name].","smile","base","base","mid")
            else:
                call ast_main("Oh, alright. Good night, [ast_genie_name].","smile","base","base","mid")

            hide screen astoria_main
            #hide screen astoria_blink #Astoria chibi.

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).
                    
            $ astoria_busy = True  
            
            if daytime:
                jump day_resume #Other return events can trigger after this!
            else:
                jump night_resume #Other return events can trigger after this!
                    

label astoria_talk: 
    menu: 
        #"--":
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ ast_genie_name = "Sir"
                    call ast_main("Very well, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Dumbledore-":
                    $ ast_genie_name = "Dumby"
                    call ast_main("[ast_genie_name]!","smile","happyCl","base","mid")
                    m "No, I said Dumbledore!-- Dumbledore!"
                    call ast_main("But I like [ast_genie_name] better!","grin","base","base","mid")
                    m "Damn it."
                    m "Fine, have it your way..."
                    jump astoria_talk
                "-Professor-":
                    $ ast_genie_name = "Professor"
                    call ast_main("Of course, [ast_genie_name].","pout","base","base","R")
                    jump astoria_talk
                "-Old man-":
                    $ ast_genie_name = "Old man"
                    call ast_main("Alrighty, [ast_genie_name].","grin","base","base","mid")
                    jump astoria_talk
                "-Genie-":
                    $ ast_genie_name = "Genie"
                    call ast_main("What?! You are a genie? For real?","scream","wide","wide","wide")
                    call ast_main("That's so cool!","grin","wide","wide","wide")
                    m "(Oh right. Nobody is supposed to know that.)"
                    m "It's just my name, [astoria_name]..."
                    call ast_main("Oh... ok, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Lord Voldemort-":
                    $ ast_genie_name = "Lord Voldemort"
                    call ast_main("Voldemort? Like that mean, evil wizard?","worried","wink","worried","mid")
                    call ast_main("You aren't him, are you?","clench","wide","wide","wide")
                    m "No, just roleplaying..."
                    call ast_main("Oh, alrighty then!","grin","happyCl","base","mid")
                    call ast_main("[ast_genie_name].","smile","narrow","narrow","mid")
                    jump astoria_talk
                "-Daddy-":
                    $ ast_genie_name = "Daddy"
                    call ast_main("Daddy? Don't you think that's a little weird?","worried","wink","worried","mid")
                    m "Not at all!"
                    call ast_main("Hmpf...","pout","angry","angry","R")
                    call ast_main("Alright, why not. Nobody knows about it anyways.","pout","angry","base","R")
                    jump astoria_talk
                "-Master-":
                    $ ast_genie_name = "Master"
                    call ast_main("Hahahaha-- you want me to call you master?","happy","happyCl","worried","mid")
                    call ast_main("That's so silly!","grin","happyCl","base","mid")
                    m "(...)"
                    call ast_main("Well alright... M-master--","grin","ahegao","ahegao","ahegao")
                    call ast_main("Hahahaha--","happy","happyCl","base","mid")
                    m "Are you done now?."
                    call ast_main("Yes... I'm sorry... I will try without laughing next time. Promised.","smile","base","base","mid")
                    jump astoria_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ ast_genie_name = "Sir"
                        call ast_main("I will just call you [ast_genie_name] again.","smile","base","base","mid")
                    else:
                        $ ast_genie_name = temp_name
                        call ast_main("Uhm... ok. I will call you [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk
                
             
        "-From now on I will refer to you as-":
            menu:
                "-Miss Greengrass-":
                    $ astoria_name = "Miss Greengrass"
                    call ast_main("Sure, [ast_genie_name].","smile","base","base","mid")
                    jump astoria_talk
                "-Girl-":
                    $ astoria_name = "Girl"
                    call ast_main("Ok, [ast_genie_name].","smile","base","worried","R")
                    jump astoria_talk
                "-Princess-":
                    $ astoria_name = "Princess"
                    call ast_main("I really do feel like a princess!","happy","angry","angry","mid")
                    call ast_main("After all, I can do whatever I want!","grin","angry","angry","angry")
                    jump astoria_talk
                "-Cutie-":
                    $ astoria_name = "Cutie"
                    call ast_main("Fine... If you really have to, [ast_genie_name].","pout","base","worried","R")
                    jump astoria_talk
                "-Slave-":
                    $ astoria_name = "Slave"
                    call ast_main("I'm not your slave, [ast_genie_name]!","pout","angry","angry","R")
                    m "Of course you aren't! We are just playing a game, that's all..."
                    call ast_main("Oh I like games!","grin","wide","base","wide")
                    call ast_main("Alrighty then!","grin","happyCl","worried","mid")
                    jump astoria_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ astoria_name = "Miss Greengrass"
                    else:
                        $ astoria_name = temp_name
                        call ast_main("That's a bit much, don't you think, [ast_genie_name]?","pout","angry","angry","R")
                        m "Not at all!"
                        m "I will only call you that when we are alone, promised!"
                        call ast_main("Well,... Ok then...","pout","angry","base","mid")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk

                    
        "-Never mind":
            jump astoria_requests