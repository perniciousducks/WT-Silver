

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
        #"-Talk-":
        #    if not chitchated_with_ast: 
        #        call ast_chit_chat 
        #        jump astoria_requests
        #    else:
        #        jump astoria_talk 
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
                    
