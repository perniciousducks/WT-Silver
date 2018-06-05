


label summon_susan:

    call load_susan_clothing_saves

    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    #call susan_door_event

    call update_sus_uniform

    #call sus_chibi("stand","mid","base")

    if one_of_ten < 4:
        if daytime:
            call sus_main("Good day, [genie_name].","base","base","base","mid",xpos="base",ypos="base")
        else:
            call sus_main("Good evening, [genie_name].","base","base","base","mid",xpos="base",ypos="base")
    elif one_of_ten < 7:  
        call sus_main("How can I help you, [genie_name]?","base","base","worried","R",xpos="base",ypos="base")
    else:
        call sus_main("You wanted to see me, [genie_name]?","base","base","worried","down",xpos="base",ypos="base")

    label susan_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        #"-Talk-":
        #    if not chitchated_with_ast: 
        #        call ast_chit_chat 
        #        jump susan_requests
        #    else:
        #        jump susan_talk 
        #"-Tutoring-":
        "-Inventory-":
            $ active_girl = "susan"

            call load_susan_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ wardrobe_active = 1 #True
            call sus_main(xpos="wardrobe",ypos="base")
            call screen wardrobe
            
        "-Dismiss her-":
            if daytime:
                call sus_main("I will go back to classes then, [sus_genie_name].","base","base","base","down")
            else:
                call sus_main("Uhm... good night then, [sus_genie_name].","base","base","base","down")

            hide screen susan_main
            #hide screen susan_blink #Susan chibi.

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).
                    
            $ susan_busy = True  
            
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
                    