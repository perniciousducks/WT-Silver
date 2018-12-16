


label cho_random_clothing:
    call load_cho_clothing_saves

    $ cho_wear_outfit = False
    $ cho_wear_top         = True
    $ cho_wear_bottom      = True

    $ random_number = renpy.random.randint(1, 10)

    # Rainy and Thundery Weather.
    if weather_gen >= 5:
        pass

    # Clear Weather.
    else:
        if daytime and random_number in [1,2,3,4,5]: #50% chance:

            if not cc_muggle_hot_ITEM.unlocked and cho_quidd_points >= 3:
                $ cc_muggle_hot_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ cho_wear_neckwear    = False
                $ cho_wear_gloves      = False
                $ cho_wear_stockings   = True
                $ c_top = "top_tanktop_2"
                $ c_top_color = "base"
                $ c_bottom = "pants_jeans_short"
                $ c_bottom_color = "base"
                $ c_stockings = "stockings"

                call update_cho_uniform
                #call cho_chibi("stand","mid","base")

                pause.2
                call cho_main("","base","base","base","mid",xpos="mid",ypos="base")
                call ctc

                g9 "Got a new outfit, [cho_name]?"
                call cho_main("Yes, [cho_genie_name].","smile","base","raised","R")
                call cho_main("I thought about our Quidditch training a bit more, and how effective it is.","open","base","base","downR")
                call cho_main("So I figured, maybe, if I applied those training methods to my daily school life,...","soft","base","sad","mid")
                call cho_main("It will help me get even more popular...","quiver","base","raised","down")
                g9 "You most certainly will, [cho_name]! I can promise you that!"
                call cho_main("I hope so too...","soft","base","raised","mid")
                call cho_main("Do you like my new outfit?","smile","closed","raised","mid")
                g9 "Absolutely!"
                call cho_main("Thank you.","base","base","base","mid")
                hide screen cho_chang
                with d3
                call cho_main(xpos="base",ypos="base")

                #Unlocks Wardrobe.
                call give_reward(">Congratulations! You can now access Cho's wardrobe and change her appearance!","interface/icons/head/head_cho_2.png")
                $ cho_wardrobe_unlocked = True

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item = cc_muggle_hot_ITEM)

                call cho_main(xpos="base",ypos="base") #Resets menu xpos.

                return

            pass

    call load_cho_clothing_saves
    call update_cho_uniform

    call cho_main("Hello, [cho_genie_name].","base","base","base","mid",xpos="base",ypos="base")






    return
