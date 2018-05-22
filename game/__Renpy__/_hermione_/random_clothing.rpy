

#Door Events (Hermione wears random clothing.)

label hermione_door_event:

    ### BAD WEATHER EVENT ###
    if wather_generator >= 81 and wather_generator <= 100: #Rainy and Thundery Weather

        #Activates the event.
        $ hermione_door_event_happened = True #Resets on new day.

        #Hermione wears gloves, stockings, and a scarf.
        if wather_generator >= 81 and wather_generator <= 90: #Thundery Weather

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

            show screen bld1
            with d3


            #One time event:
            if mad > 1:
                call her_main("","annoyed","baseL",xpos="base",ypos="base")
            else:
                call her_main("","base","base",xpos="base",ypos="base")
            pause.2

            m "..."
            m "[hermione_name],..."
            m "What's with all these clothes you are wearing?"

            if not reward_her_wool_clothing: #Gets activated right after.
                call her_main("[genie_name], it's raining outside! I don't want to get a cold.","open","base")
                if whoring < 11:
                    call her_main("Just imagining having to lay down in bed not being able to study,...","annoyed","angryL")
                    call her_main("Really gives me the shudders...","disgust","down_raised")
                    call her_main("I can't afford to risk that, [genie_name]!","open","closed")
                    call her_main("Even a single day in which I'm not able to study is--","open","baseL")
                    g4 "Alright, alright! I get it..."
                else:
                    m "Of course..."
                call her_main("","soft","base")
                pause.2
                m "It looks cute on you."
                m "You can keep it on for now."
                call her_main("Thank you, [genie_name].","base","base")

                $ h_request_wear_neckwear = True
                $ h_request_wear_gloves = True
                $ h_request_wear_stockings = True

                call give_reward(">New clothing items for Hermione have been unlocked!","images/store/gifts/10.png")

            #Repeated event:
            else:
                call her_main("[genie_name], Haven't you had the chance to look out of your window today? It's pouring with rain!","open","base")
                m "So what? You are inside?"
                call her_main("Yes, but it's a bit cold, [genie_name], and my...","soft","baseL",cheeks="blush")
                if whoring < 11:
                    call her_main("I better not mention it...","disgust","down",cheeks="blush")
                elif whoring < 18:
                    call her_main("{size=-5}People can see my... my nipples...{/size}","disgust","down",cheeks="blush")
                else:
                    call her_main("I can't have my nipples poking out all the time, [genie_name]! It's distracting!","annoyed","angryL")

                menu:
                    "-Tell her to take the clothes off-":
                        m "You should take these clothes off when you're in my room, [hermione_name]."
                        call her_main("Fine. Let me take it off, [genie_name].","annoyed","baseL")

                        hide screen hermione_main
                        with d3
                        pause.5

                        $ h_request_wear_neckwear = False
                        $ h_request_wear_gloves = False
                        $ h_request_wear_stockings = False

                        $ hermione_wear_neckwear = False
                        $ hermione_wear_gloves = False
                        $ hermione_wear_stockings = False

                    "-Tell her to keep the stockings on-":
                        m "You should take these clothes off when you're in my room, [hermione_name]."
                        m "But you can keep the stockings on. They are cute."
                        call her_main("Ok, [genie_name]. Let me take it off...","soft","base")

                        hide screen hermione_main
                        with d3
                        pause.5

                        $ h_request_wear_neckwear = False
                        $ h_request_wear_gloves = False
                        $ h_request_wear_stockings = True

                        $ hermione_wear_neckwear = False
                        $ hermione_wear_gloves = False

                    "-Tell her to keep the clothes on-":
                        m "You can keep it on, for now."
                        call her_main("Thank you, [genie_name].","soft","base")

                        $ h_request_wear_neckwear = True
                        $ h_request_wear_gloves = True
                        $ h_request_wear_stockings = True


            #Unlocks rewards.
            $ reward_her_wool_clothing = True                 #Adds clothing to wardrobe

        #Hermione wears a robe.
        else:
            $ hermione_wear_robe        = True

            call update_her_uniform
            call her_chibi("stand","mid","base")

            call bld

            if mad > 1:
                call her_main("","annoyed","baseL",xpos="base",ypos="base")
            else:
                call her_main("","base","base",xpos="base",ypos="base")
            pause.2

            m "You are wearing that robe again?"
            call her_main("Yes, [genie_name].","open","base")
            call her_main("It's raining quite heavily outside, and I didn't want to get wet.","open","base")
            menu:
                "-Tell her to take the robe off-":
                    m "Take it off, would you."
                    call her_main("Of course, [genie_name].","base","base")

                    hide screen hermione_main

                    $ h_request_wear_robe       = False
                    $ hermione_wear_robe        = False

                "-Tell her to keep the robe on-":
                    m "You can keep it on, for now."
                    call her_main("Alright, [genie_name].","base","base")

                    $ h_request_wear_robe       = True

    return
#















