

# Started first training match against Hufflepuff

label start_training_match:

    call cho_main("","base","base","base","mid", xpos="right", ypos="base", trans="fade")

    # First Hufflepuff match.
    if huffl_matches_won == 0:

        # Intro
        if huffl_match_counter == 0:

            $ huffl_match_counter += 1 # Stat counter

            m "So, when will those Quidditch matches take place?"
            call cho_main("We could arrange one for today. Just for practice, against Hufflepuff.","open","base","base","R")
            m "Really? Just like that?"
            call cho_main("Why yes. The Hufflepuff team wouldn’t take up a chance to play against us for training.","soft","base","raised","mid")
            call cho_main("They’d welcome every opportunity to test us and study our tactics...","open","narrow","angry","mid")
            call cho_main("All I need to do is give their team captain a heads up during classes.","base","base","base","mid")
            m "Great. Get your team ready cause you are going to play today."
            call cho_main("I will, [cho_genie_name]. Wish me luck.","smile","base","base","mid")

        # Repeated
        else:

            $ huffl_match_counter += 1 # Stat counter

            m "Time for another practice match don't you think?"
            call cho_main("I’ll try my best, [cho_genie_name].","base","base","base","mid")
            m "Good luck out there."
            call cho_main("Thank you, Sir.", face="happy")
            call cho_main("I better get going. See you later, [cho_genie_name]!","soft","base","raised","mid")


    # Second Hufflepuff match.
    elif huffl_matches_won == 1:

        $ huffl_match_counter += 1 # Stat counter

        m "Ready to kick some badger ass again?"
        call cho_main("Absolutely!","smile","narrow","angry","mid")
        call cho_main("If we beat them twice, we might have a chance against them in the tourney!","base","narrow","angry","mid")
        m "That’s the spirit! Now go get them tiger!"
        call cho_main("Later, [cho_genie_name]!", face="happy")

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_busy = True
    if quidditch_commentator == "hermione": # Hermione has to commentate.
        $ hermione_busy = True
    $ quidditch_match_in_progress = True

    jump main_room

# Check if Cho won or lost the practice game.
label quidditch_match_return:
    # Cho enters.
    call play_sound("knocking")
    call bld
    ">*knock* *knock* *knock*"

    menu:
        "\"Come in!\"":
            cho "Yes, [cho_genie_name]..."
        "\"Who is it?\"":
            cho "Cho Chang, [cho_genie_name]."
            m "Come on in, [cho_name]!"
            cho "..."

    call cho_walk(action="enter", speed=2.2)


    # Hufflepuff Match
    if cho_tier == 1:

        # First practice game.
        if huffl_matches_won == 0:
            # Win
            if cho_class.get_cloth("bottom").id == cho_cloth_schoolskirt3.id and quidditch_position == "above":
                $ huffl_matches_won = 1
                jump hufflepuff_practice_win_1
            # Lose
            else:
                jump hufflepuff_practice_lost

        # Second practice game.
        else:
            # Win
            if cho_class.get_cloth("bottom").id == cho_cloth_schoolskirt3.id and quidditch_position == "above" and cho_whoring >= 3:
                $ huffl_matches_won = 2
                $ lock_cho_training = True
                jump hufflepuff_practice_win_2
            # Lose
            else:
                jump hufflepuff_practice_lost


    #Slytherin Match
    elif cho_tier == 2:
        jump main_room

    #Gryffindor Match
    elif cho_tier == 3:
        jump main_room


# Lost first hufflepuff match.
label hufflepuff_practice_lost:

    call cho_main("...", mouth="upset", face="neutral", xpos="mid", ypos="base")
    m "So, how did it go?"
    call cho_main("We lost... again...", mouth="soft", eyebrows="sad", face="neutral")
    m "What was the problem?"

    # Low whoring response
    if huffl_matches_won == 1 and cho_whoring < 3:
        if cho_class.get_cloth("bottom").id == cho_cloth_schoolskirt3.id:
            call cho_main("I couldn't focus on the game!","angry","closed","angry","mid")
            call cho_main("This ridiculously short skirt! The whole match it kept on slipping over my bum!","soft","narrow","angry","mid")
            m "So what? It wasn't an issue before... Just ignore it..."
            call cho_main("And let everybody ogle at my bare ass?","open","angry","angry","mid")
            m "Aren't you still wearing panties?"
            call cho_main("Of course I am! And I don't intend to show them to the whole school!","annoyed","narrow","angry","mid")
            call cho_main("Just enough to let Cedric have a peek...","soft","narrow","angry","R")
            g4 "\"Just a peek\" won't do, [cho_name]! You have to reveal everything!"
            g4 "If the entire school knows the color of your panties, that's when you have done your task well!"
            call cho_main("You are asking too much of me, [cho_genie_name]! I'd never be able to do such a thing...","annoyed","narrow","base","mid")
            m "Clearly you just aren't ready yet. We'll get you to be more confident on your broom soon enough..."
            g9 "With your panties on display!"
        else:
            call cho_main("I'm not really sure...","soft","narrow","sad","R")
            call cho_main("Our tactics worked so well last time!","soft","base","sad","mid")
            call cho_main("It might have been a bad idea to change them, don't you think so too, [cho_genie_name]?","annoyed","narrow","sad","mid")
            m "Hmmm..."
            m "Yes, maybe we should try again with out previous tactics."
            call cho_main("Yes, [cho_genie_name].","soft","narrow","sad","mid")

        call cho_main("(...)","annoyed","narrow","angry","mid")
        call cho_main("It's getting late...","soft","narrow","base","R")
        call cho_main("If you don't mind I'd like to go to bed now.","open","base","angry","mid")
        m "Sure. You may leave..."
        call cho_main("Have a good night, Sir.","soft","closed","base","mid")

    # Position response
    elif quidditch_position != "above":
        call cho_main("Our tactic didn't work, [cho_genie_name].","annoyed","narrow","sad","mid")
        call cho_main("Cedric just ignored me for most of the game, and ended up catching the snitch...","soft","narrow","sad","R")
        m "Were you trying to distract him enough?"

        if cho_class.get_cloth("bottom").id == cho_cloth_schoolskirt3.id:
            call cho_main("Of course I was! I tried to let him have a peek up my skirt, but I'm not sure he even noticed that I was wearing one.","soft","narrow","angry","mid")
            m "Interesting..."
            m "Maybe we need to tackle this situation from another angle."
            m "And change our flying tactics to best show it off..."
        else:
            call cho_main("I did! To the best of my ability...","soft","narrow","angry","R")
            call cho_main("Maybe he doesn't like the outfit I'm wearing?","soft","narrow","base","mid")
            m "Yes that might be it."
            m "We'll discuss your outfit next time..."
            m "And change our flying tactics to best show it off..."

        call cho_main("Whatever you say, [cho_genie_name].","annoyed","narrow","angry","R")
        call cho_main("I'll be going to bed now if you don't mind.","soft","narrow","angry","mid")
        call cho_main("Have a good night, Sir.","annoyed","narrow","base","mid")
        m "You too..."

    else:
        call cho_main("Cedric didn't seem too distracted by me... He ended up catching the snitch and...","open","narrow","base","R")
        call cho_main("I'm not sure what the problem was...","annoyed","narrow","sad","mid")
        m "Maybe we aren't using the right tactics."
        call cho_main("Lets try a different approach next time, [cho_genie_name].","open","narrow","angry","mid")
        call cho_main("I should head back to our dorms and get some sleep...","soft","closed","base","mid")
        m "Sure. You may leave..."
        call cho_main("Have a good night, Sir.","soft","base","base","R")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    $ cho_class.equip(cho_outfit_last) # Equip last worn clothes

    if huffl_matches_won == 0:
        $ cho_mood += 5
    else:
        $ cho_mood += 8

    $ cho_busy = True

    jump main_room



# Won first Hufflepuff match.
label hufflepuff_practice_win_1:

    call cho_main("...","annoyed","narrow","angry","R",xpos="mid",ypos="base")
    m "You seem a little on edge..."
    call cho_main("On edge?","scream","shocked","angry","mid")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!","angry","wide","angry","mid")
    call cho_main("You had to have me do this on the day half of \"hufflepuff\" shows up to watch us practice, didn't you!","pout","narrow","angry","R")
    call cho_main("I bet you were probably in on it...","upset","narrow","angry","mid")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    call cho_main("{size=+10}I got it!!!{/size}","scream","base","base","mid")
    call cho_main("I caught the snitch!","smile","closed","base","mid")
    m "Congratulations..."
    call cho_main("That blockhead Cedric didn't stand a chance against me!","open","base","sad","R")
    call cho_main("Usually I'm never fast enough to beat him with my crummy old nimbus...","pout","angry","angry","downR")
    call cho_main("But today, I flew above him as we were both racing after the snitch, just like you said I should.","smile","base","base","mid")
    g9 "Sounds like somebody should get a reward for his efforts!"
    call cho_main("Ah!!! I can't believe I was able to finally catch it!","smile","closed","base","mid")
    m "Is this the first time you've caught one?"
    call cho_main("Uh-hum- This is the first game of quidditch \"Ravenclaw\" has won in over six years!","smile","base","base","mid")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices, [cho_genie_name]...","annoyed","narrow","sad","downR")
    m "oh..."
    call cho_main("\"Ravenclaw\"...{w} isn't very good...","pout","narrow","sad","down")
    call cho_main("But I have a feeling that's going to change this year!","smile","closed","base","mid")
    g9 "And I am happy to be of help!"
    call cho_main("Yes, [cho_genie_name]! Thank you so much!","horny","narrow","base","down")
    call cho_main("If there is any way I can return the favour...?","horny","base","raised","mid")

    if cc_pf_talk.points == 0:
        m "Why don't we start with that, Miss Chang,...{w} favours!"
        m "I did prove the effectiveness of my methods to you. Now it's your turn to stay true to your promise..."
        call cho_main("Of course, Sir.","base","base","base","mid")
        call cho_main("But, if you don't mind...","soft","base","base","R")
    else:
        g9 "You could sell some more favours to me!"
        call cho_main("More chit-chats?","quiver","wink","sad","mid")
        m "I had hoped for something more... advanced."
        call cho_main("More advanced?...","soft","narrow","sad","mid")
        call cho_main("Maybe some other time, Sir.","quiver","closed","sad","mid")

    call cho_main("The whole house is celebrating our win at the moment...{w} And I'd rather not miss spending some time with-","horny","closed","sad","mid")
    g4 "You did well today, [cho_name]."
    g9 "Go and party! You've earned it."
    call cho_main("Thank you, [cho_genie_name]... For everything.","base","narrow","base","mid")
    call cho_main("Have a good night!","smile","base","base","mid")
    m "You too..."

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_class.equip(cho_outfit_last) # Equip last worn clothes

    $ cho_busy = True

    jump main_room




label hufflepuff_practice_win_2:

    call cho_main("I hate you, I hate you, I HATE YOU!","scream","closed","angry","mid",xpos="mid",ypos="base",trans="hpunch")
    m "Did you catch that gold thing?"
    call cho_main("I've never felt so humiliated in my entire life!","open","angry","angry","R")
    g4 "Did you win or what?{w} I'm on the edge of my seat here, girl!"
    call cho_main("At the expense of my dignity!","quiver","base","raised","down")
    m "That's a...{w} yes?"
    call cho_main("Lee Jordan only used to say that I had a nice butt! But-","soft","base","sad","down")
    call cho_main("But, Hermione! Her incompetece as a Quidditch commentator is unmeasurable!","open","base","raised","R")
    call cho_main("I almost miss Jordan's sexist remarks about my body...","open","closed","base","mid")
    g9 "I could tell Hermione to do the same if you'd like."
    call cho_main("Please don't, [cho_genie_name]! I was merely joking!","annoyed","narrow","angry","mid")
    m "Would you say you've had enough practice to play against them in a tourney game?"
    call cho_main("Absolutely! The next time we will confront \"Hufflepuff\", they will be crushed!","smile","angry","angry","mid")
    call cho_main("This should be an easy win for \"Ravenclaw\".","base","closed","base","mid")
    call cho_main("Speaking of which, I need to get back to my team now, [cho_genie_name].","open","wide","base","R")
    call cho_main("Thank you for helping me!","smile","narrow","base","mid")
    m "You're welcome."
    call cho_main("Good night, Sir.","base","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_class.equip(cho_outfit_last) # Equip last worn clothes

    $ cho_busy = True

    jump main_room
