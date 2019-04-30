


label cho_random_clothing:

    $ cho_class.wear("all")

    $ random_number = renpy.random.randint(1, 10)

    # Rainy and Thundery Weather.
    if weather_gen >= 5:
        pass
    # Clear Weather.
    else:
        if daytime and random_number < 6: #50% chance for event:
            # Unlock wardrobe
            if not cho_wardrobe_unlocked:
                if main_matches_won >= 1:
                    $ cc_muggle_hot_ITEM.unlocked = True
                    
                    $ cho_class.unequip("all")
                    $ cho_class.equip(cho_outfit_trainee)

                    #call cho_chibi("stand","mid","base")

                    pause.2
                    call cho_main("","base","base","base","mid",xpos="mid",ypos="base", animation=moveFade)
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
                    call cho_main(xpos="base",ypos="base")

                    #Unlocks Wardrobe.
                    call give_reward(">Congratulations! You can now access Cho's wardrobe and change her appearance!","interface/icons/head/head_cho_2.png")
                    $ cho_wardrobe_unlocked = True

                    #Unlocks rewards.
                    call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item = cc_muggle_hot_ITEM)

                    call cho_main(xpos="base",ypos="base") #Resets menu xpos.

                    return
                pass
            else:
                if not cc_party_slut_ITEM.unlocked:
                    $ cc_party_slut_ITEM.unlocked = True

                    $ cho_class.unequip("all")
                    $ cho_class.equip(cho_outfit_party)

                    #call cho_chibi("stand","mid","base")

                    pause.2
                    call cho_main("","base","base","base","mid",xpos="mid",ypos="base", animation=moveFade)
                    call ctc

                    g9 "Wow girl, what are you wearing?"
                    call cho_main("It's my party outfit...","soft","base","raised","down")
                    m "(...)"
                    call cho_main("Is it too much?","quiver","wink","raised","mid")
                    m "Too much? Are you really asking me that?"
                    m "If I'm truely honest with you-"
                    g4 "Your body, in an outfit like that,..."
                    g4 "Really shows off your best assets."
                    call cho_main("Oh...","horny","base","raised","down")
                    call cho_main("You see, that sort of reaction is just what I wanted to get from the boys...","soft","base","sad","R")
                    call cho_main("Stare at my assets any time you want, [cho_genie_name]!","horny","narrow","angry","mid")
                    g4 "Hngggh-!!!"
                    call cho_main(xpos="base",ypos="base")

                    #Unlocks rewards.
                    call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item = cc_party_slut_ITEM)

                    call cho_main(xpos="base",ypos="base",face="horny") #Resets menu xpos.

                    return

    if cho_mood != 0:
        call cho_main("[cho_genie_name]...",face="annoyed",xpos="base",ypos="base", animation=moveFade)
        ">Cho is upset with you."
    else:
        call cho_main("Hello, [cho_genie_name].",face="happy",xpos="base",ypos="base", animation=moveFade)
    $ cho_animation = None

    return
