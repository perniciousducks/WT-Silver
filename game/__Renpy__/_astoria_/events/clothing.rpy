

#Door Events (Astoria wears random clothing.)

label astoria_door_event:

    ### BAD WEATHER EVENT ###
    if weather_gen >= 5: #Rainy and Thundery Weather

        #Astoria wears a robe.
        if weather_gen in [5,6]: #Rainy Weather
            call ast_main("","smile","base","base","mid",xpos="base",ypos="base") 


    return















