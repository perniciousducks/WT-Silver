

#Door Events (Astoria wears random clothing.)

label astoria_door_event:

    ### BAD WEATHER EVENT ###
    if weather_gen >= 5: #Rainy and Thundery Weather

        #Astoria wears a robe.
        if weather_gen in [5,6]: #Rainy Weather

            $ astoria_wear_robe = True

            call update_ast_uniform

            call ast_main("","smile","base","base","mid",xpos="base",ypos="base")
            
            if not ast_request_wear_robe:   
                pause.8 #Shows Astoria with robe for a bit.
            call load_astoria_clothing_saves


    return















