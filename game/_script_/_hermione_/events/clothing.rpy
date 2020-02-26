label hermione_summon_setup:
    $ random_number = renpy.random.randint(1, 10)

    if not hermione_wardrobe_unlocked:
        $ hermione_wardrobe_unlocked = True

        #call set_her_action("hold_book") # This will only be used once in the game, here.

        call her_walk(action="enter", xpos="mid", ypos="base")

        call play_music("hermione")
        call ctc

        m "(...)"
        call her_main("Is anything wrong, [genie_name]?", "soft", "base", "base", "mid", trans=d3)
        g4 "Why are you holding all those... \"things\"?"
        call her_main("My books?", "open", "narrow", "worried", "down")
        call her_main("I wasn't sure which ones I'd need, so I brought all of them!", "grin", "happyCl", "base", "mid")
        m "Brought them for what?"
        call her_main("My tutoring lessons...", "soft", "squint", "base", "mid")
        call her_main("I hope you're still planning to lecture me, [genie_name].", "annoyed", "base", "base", "mid")
        g9 "Oh, I'll give you a lecture for sure."
        m "But we're going to have to do it my way.{w}\nThere's no need for those books."
        call her_main("No need?", "normal", "base", "worried", "mid")
        m "No."
        call her_main("Too bad, I love books.", "annoyed", "narrow", "worried", "down")
        hide screen hermione_main
        with d5
        pause.2

        call her_chibi("stand","mid","base",flip=True)
        with d5
        pause.5

        #call set_her_action("none","update")

        g9 "{size=-2}And soon you'll love cock!{/size}"
        $ renpy.play('sounds/punch01.mp3') #Hermione lays books onto the floor.
        pause.2

        call her_chibi("stand","mid","base",flip=False)
        with d5
        pause.2

        call her_main("Yes?", "soft", "base", "base", "mid",trans=d5)
        m "I didn't say anything..."
        call her_main("If you say so, [genie_name].", "open", "base", "base", "R")
        call her_main("Is it ok if we could start right away with the lessons?", "soft", "base", "base", "mid")
        m "Well... Of course..."

        call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base",trans=fade)

        return

    # weather_gen 1-3   = good weather
    # weather_gen 4     = cloudy weather
    # weather_gen 5-6   = bad weather
    # raining           = bool
    # snowing           = bool
    # blizzard          = bool
    # storm             = bool

    # Sunny
    
    #
    #
    # TODO: Remove obsolete variables and fix the code after clothes have been added.
    #
    # if weather_gen in [1] and 1 > 2:

        # if her_tier >= 3 and daytime and not hg_muggle_hot_ITEM.unlocked:
            # $ hg_muggle_hot_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_frilled_1"
                # $ h_bottom = "pants_jeans_short"
                # $ h_stockings = "stockings_cute"

                # call update_her_uniform

                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # g4 "(Wow! Look at her!)"
                # g9 "That's quite a sexy outfit, [hermione_name]!"
                # if her_whoring < 11:
                    # call her_main("Uhm... Thank you, [genie_name].", "soft", "base", "base", "R")
                    # call her_main("I normally don't wear something like this.", "open", "base", "base", "mid")
                    # call her_main("(Showing so much cleavage...)", "disgust", "narrow", "worried", "down", cheeks="blush")
                    # call her_main("But the weather is just too hot today.", "base", "base", "base", "R")
                    # g9 "You should wear this more often!"
                # else:
                    # call her_main("Thank you, [genie_name].", "base", "narrow", "base", "mid_soft")

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_hot_ITEM)


    # # Cloudy
    # if weather_gen in [4] and 1 > 2:

        # #One time event.
        # if not hg_accs_wool_g_ITEM.unlocked:
            # $ hg_accs_wool_g_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = True
                # $ hermione_wear_gloves      = True
                # $ hermione_wear_stockings   = True
                # $ h_neckwear = "scarf_striped_g"
                # $ h_gloves = "gloves_wool_1"
                # $ h_stockings = "stockings_striped_1"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "..."
                # m "[hermione_name],..."
                # m "What's with all these clothes you are wearing?"
                # call her_main("It's a bit cold outside, [genie_name]... and my...", "soft", "base", "base", "R", cheeks="blush")

                # if her_whoring < 11:
                    # call her_main("I better not mention it...", "disgust", "narrow", "worried", "down", cheeks="blush")
                # elif her_whoring < 18:
                    # call her_main("{size=-5}People can see my... my nipples...{/size}", "disgust", "narrow", "worried", "down", cheeks="blush")
                # else:
                    # call her_main("I can't have my nipples poking out all the time, [genie_name]! It's distracting!", "annoyed", "narrow", "angry", "R")

                # call her_main("", "soft", "base", "base", "mid")
                # pause.2
                # m "Alright,... It looks cute on you."
                # m "You can keep it on for now."
                # call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")

                # $ h_request_wear_top = True
                # $ h_request_wear_bottom = True
                # $ h_request_wear_neckwear = True
                # $ h_request_wear_gloves = True
                # $ h_request_wear_stockings = True

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_accs_wool_g_ITEM)


    # # Raining
    # if raining and 1 > 2:

        # if her_tier >= 2 and not hg_muggle_rainy_ITEM.unlocked:
            # $ hg_muggle_rainy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wet_clothes = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ h_top = "top_sweater_1"
                # $ h_bottom = "pants_jeans_long"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "disgust", "narrow", "worried", "down", xpos="base", ypos="base")
                # call ctc

                # m "Damn girl. You look drenched..."
                # call her_main("I'm sorry, [genie_name], but... It's raining cats and dogs out there!", "open", "base", "base", "mid")
                # call her_main("I couldn't find my robe so I just put on a sweater and some jeans...", "open", "base", "base", "R")
                # call her_main("I hope you don't mind my uniform not being up for standards. I didn't want it to get wet.", "disgust", "narrow", "worried", "down")
                # m "It's fine, [hermione_name]."
                # g9 "Besides, I wouldn't mind seeing you in jeans more often!"
                # call her_main("Thank you, [genie_name].", "normal", "base", "base", "R")
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_rainy_ITEM)

        # # Robe
        # else:

            # $ hermione_wear_robe = True
            # call update_her_uniform
            # call play_sound("door")
            # call her_chibi("stand","mid","base")
            # with d3

            # call play_music("hermione")
            # if her_mood > 1:
                # call her_main("", "annoyed", "base", "base", "R", xpos="base", ypos="base")
            # else:
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # if not h_request_wear_robe:
                # pause.5 #Shows Hermione with robe for a bit.

    # # Snow
    # if snowing or blizzard and 1 > 2:

        # if her_tier >= 2 and not hg_muggle_cold_ITEM.unlocked:
            # $ hg_muggle_cold_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings = True
                # $ h_top = "top_pullover_1"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "New outfit?"
                # call her_main("Yes, [genie_name]. I brought it with me from home. It's a bit too cold for just my normal uniform...", "open", "base", "base", "R")
                # call her_main("Do you like it?", "soft", "base", "base", "mid")
                # g9 "I do, [hermione_name]. It's cute."
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_ITEM)

        # elif her_tier >= 3 and not hg_muggle_cold_sexy_ITEM.unlocked:
            # $ hg_muggle_cold_sexy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_pullover_2"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # m "That's quite the cute outfit, [hermione_name]."
                # call her_main("Thank you, [genie_name]. I made some changes to the old one...", "open", "base", "base", "R")
                # call her_main("Do you like it?", "soft", "base", "base", "mid")
                # g9 "Very much so, [hermione_name]. I love the breast window."
                # $ her_mood -= 10
                # if her_mood < 0:
                    # $ her_mood = 0

            # else:
                # call update_her_uniform
                # call play_sound("door")
                # call her_chibi("stand","mid","base")
                # with d3

                # call play_music("hermione")
                # call her_main("", "base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_sexy_ITEM)
            
    if hermione_outfits_schedule:
        $ hermione.equip_random_outfit()

    call play_sound("door")
    call her_chibi("stand","mid","base")
    with d3

    #Hermione greeting.
    call play_music("hermione")
    
    if her_mood > 0:
        if 5 > her_mood >= 1:
            call her_main("Yes, [genie_name]?", "soft", "base", "worried", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > her_mood >= 5:
            call her_main("*sigh*... Yes, [genie_name]?", "annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > her_mood >= 10:
            call her_main("What is it, [genie_name]?", "open", "closed", "annoyed", "mid", xpos="base", ypos="base", trans=d3)
            call her_main("", "upset", "base", "annoyed", "mid")
        elif 30 > her_mood >= 20:
            call her_main("What do you want, \"[genie_name]\"?", "upset", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 40 > her_mood >= 30:
            call her_main("*Hmph*...", "normal", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 50 > her_mood >= 40:
            call her_main("*Tsk*", "angry", "base", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif her_mood >= 50:
            call her_main("I have nothing to tell you, sir!", "mad", "narrow", "angry", "L", xpos="base", ypos="base", trans=d3)
            
        call describe_mood("Hermione", her_mood)
    else:
        if daytime:
            call her_main("Good morning, [genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
             call her_main("Good evening, [genie_name].", "base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
