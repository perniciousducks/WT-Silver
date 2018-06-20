

#Door Events (Hermione wears random clothing.)

label hermione_door_event:

    ### BAD WEATHER EVENT ###
    if weather_gen >= 5: #Rainy and Thundery Weather

        #Hermione wears gloves, stockings, and a scarf.
        if weather_gen == 5: #Rainy Weather

            $ hermione_wear_neckwear    = True
            $ hermione_wear_gloves      = True
            $ hermione_wear_stockings   = True

            if h_neckwear == "00_blank" or whoring <= 8:
                $ h_neckwear = "neck_scarf_striped" #Change to Scarf
            if h_gloves == "00_blank":
                $ h_gloves = "gloves_wool_short"
            if h_stockings == "00_blank":
                $ h_stockings = "stockings_striped"

            call update_her_uniform 
            call her_chibi("stand","mid","base") 

            if mad > 1:
                call her_main("","annoyed","baseL",xpos="base",ypos="base") 
            else:
                call her_main("","base","base",xpos="base",ypos="base") 

            #One time event.
            if not reward_her_wool_clothing: #Gets activated right after.
                
                $ hermione_door_event_happened = True #Fix for her greeting response later.
                
                pause.2
                m "..."
                m "[hermione_name],..."
                m "What's with all these clothes you are wearing?"

                call her_main("[genie_name], it's raining outside! I don't want to get a cold.","open","base") 
                m "It's not raining in here..."
                call her_main("Yes, but it's a bit cold, [genie_name], and my...","soft","baseL",cheeks="blush") 
                
                if whoring < 11:
                    call her_main("I better not mention it...","disgust","down",cheeks="blush") 
                elif whoring < 18:
                    call her_main("{size=-5}People can see my... my nipples...{/size}","disgust","down",cheeks="blush") 
                else:
                    call her_main("I can't have my nipples poking out all the time, [genie_name]! It's distracting!","annoyed","angryL") 
                    
                call her_main("","soft","base") 
                pause.2
                m "Alright,... It looks cute on you."
                m "You can keep it on for now."
                call her_main("Thank you, [genie_name].","base","base") 

                $ h_request_wear_neckwear = True
                $ h_request_wear_gloves = True
                $ h_request_wear_stockings = True

                #Unlocks rewards.
                call give_reward(">New clothing items for Hermione have been unlocked!","images/store/gifts/10.png") 
                $ reward_her_wool_clothing = True                 #Adds clothing to wardrobe

            #Repeated event.
            else:
            
                pause.8 #Shows Hermione with cold weather clothes for a bit.
                call load_hermione_clothing_saves 
          

        #Hermione wears a robe.
        else: #6 #Thundery Weather
            $ hermione_wear_robe        = True

            call update_her_uniform 
            call her_chibi("stand","mid","base") 

            if mad > 1:
                call her_main("","annoyed","baseL",xpos="base",ypos="base") 
            else:
                call her_main("","base","base",xpos="base",ypos="base") 
            
            if not h_request_wear_robe:   
                pause.8 #Shows Hermione with robe for a bit.
            call load_hermione_clothing_saves 


    return















