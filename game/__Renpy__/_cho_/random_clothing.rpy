


label cho_random_clothing:

    $ cho_class.wear("all")

    $ random_number = renpy.random.randint(1, 10)

    # Rainy and Thundery Weather.
    if weather_gen >= 5:
        pass

    # Clear Weather.
    else:
        if daytime and random_number in [1,2,3,4,5]: #50% chance:

            if not cho_wardrobe_unlocked and cho_quidd_points >= 3:
                $ cho_class.unequip("all")
                $ cho_class.equip(cho_cloth_topsweater1)
                $ cho_class.equip(cho_cloth_pantslong2)
                
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
                call cho_main(xpos="base",ypos="base")

                #Unlocks Wardrobe.
                call give_reward(">Congratulations! You can now access Cho's wardrobe and change her appearance!","interface/icons/head/head_cho_2.png")
                $ cho_wardrobe_unlocked = True

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item = cc_muggle_hot_ITEM)

                call cho_main(xpos="base",ypos="base") #Resets menu xpos.

                return
            pass

        if daytime and random_number in [6,7,8,9,10]:

            if not cc_party_slut_ITEM.unlocked:
                $ cc_party_slut_ITEM.unlocked = True

                $ cho_class.unequip("all")
                $ cho_class.equip(cho_cloth_bikinitop1)
                $ cho_class.equip(cho_cloth_skirtshort2)

                #call cho_chibi("stand","mid","base")

                pause.2
                call cho_main("","base","base","base","mid",xpos="mid",ypos="base")
                call ctc

                g9 "Wow girl, the hell are you wearing?"
                call cho_main("It's my party outfit...","soft","base","raised","down")
                m "(...)"
                call cho_main("Is it too much?","quiver","wink","raised","mid")
                m "Too much? Are you really asking me that?"
                m "If I'm truely honest with you-"
                g4 "Your body, in an outfit like that,..."
                g4 "Makes me want to whip out my cock and jerk off like a mad-man! You little slut!"
                call cho_main("Oh...","horny","base","raised","down")
                call cho_main("You see, that sort of reaction is just what I wanted to get from the boys...","soft","base","sad","R")
                call cho_main("I'm glad to see it working.","smile","suspicious","base","mid")
                call cho_main("Jerk off any time you want, [cho_genie_name]!","horny","suspicious","angry","mid")
                g4 "Hngggh-!!!"
                call cho_main(xpos="base",ypos="base")


                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Cho have been unlocked!", item = cc_party_slut_ITEM)

                call cho_main(xpos="base",ypos="base",face="horny") #Resets menu xpos.

                return
            pass

    call cho_main("Hello, [cho_genie_name].","base","base","base","mid",xpos="base",ypos="base")

    return
