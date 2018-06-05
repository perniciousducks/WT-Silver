

label summon_astoria:

    call load_astoria_clothing_saves

    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    #call astoria_door_event

    call update_ast_uniform

    #call ast_chibi("stand","mid","base")

    if one_of_ten < 4:
        call ast_main("Heya, [genie_name]!","tongue_silly","wink","base","mid",xpos="base",ypos="base")
    elif one_of_ten < 7:
        call ast_main("Hello, [genie_name].","smile","base","base","mid",xpos="base",ypos="base")
    else:
        call ast_main("Hi, [genie_name]!","grin","angry","base","mid",xpos="base",ypos="base")

    label astoria_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        "-Talk-":
        #    if not chitchated_with_ast: 
        #        call ast_chit_chat 
        #        jump astoria_talk
        #    else:
            jump astoria_talk 
        #"-Tutoring-":
        "-Inventory-":
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
                jump day_main_menu
            else:
                jump night_main_menu
                    

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
                    $ ast_genie_name = "Dumbledore"
                    call ast_main("Ok, [ast_genie_name].","smile","base","base","down")
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