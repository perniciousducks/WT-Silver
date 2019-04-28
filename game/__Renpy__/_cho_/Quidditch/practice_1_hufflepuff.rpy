

# Started first training match against Hufflepuff

label start_training_match:

    # First Hufflepuff match.
    if huffl_matches_won == 0:

        # Intro
        if huffl_match_counter == 0:

            $ huffl_match_counter += 1 # Stat counter

            m "So, when will those Quidditch matches take place?"
            cho "We could arrange one for today. Just for practice, against Hufflepuff."
            m "Really? Just like that?"
            cho "Why yes. The Hufflepuff team wouldn’t take up a chance to play against us for training."
            cho "They’d welcome every opportunity to test us and study our tactics..."
            cho "All I need to do is give their team captain a heads up during classes."
            m "Great. Get your team ready cause you are going to play today."
            cho "I will, [cho_genie_name]. Wish me luck."

        # Repeated
        else:

            $ huffl_match_counter += 1 # Stat counter

            m "Time for another practice match don't you think?"
            cho "I’ll try my best, [cho_genie_name]."
            m "Good luck out there."
            cho "Thanks."
            cho "I better get going. See you later, [cho_genie_name]!"


    # Second Hufflepuff match.
    elif huffl_matches_won == 1:

        $ huffl_match_counter += 1 # Stat counter

        m "Ready to kick some badger ass again?"
        cho "Absolutely!"
        cho "If we beat them twice, we might have a chance against them in the tourney!"
        m "That’s the spirit! Now go get them tiger!"
        cho "Later, [cho_genie_name]!"

    # Cho leaves.
    call cho_walk(speed=2, action="leave")

    $ cho_busy = True
    if quidditch_commentator == "hermione": # Hermione has to commentate.
        $ hermione_busy = True
    $ quidditch_match_in_progress = True

    jump main_room





# Check if Cho won or lost the practice game.
label quidditch_match_return:

    $ cho_outift_last.save() # Temporarily save last worn clothes

    $ cho_class.equip(cho_outfit_quidditch) # Equip quidditch set

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
    if main_matches_won == 0:

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


    #Gryffindor Match
    elif main_matches_won == 1:
        jump main_room

    #Slytherin Match
    elif main_matches_won == 2:
        jump main_room


# Lost first hufflepuff match.
label hufflepuff_practice_lost:

    call cho_main("...",mouth="upset",face="neutral",xpos="mid",ypos="base")
    m "So, how did it go?"
    call cho_main("We lost... again...",mouth="soft",eyebrows="sad",face="neutral")
    m "What was the problem?"

    # Low whoring response
    if cho_class.get_cloth("bottom").id == cho_cloth_schoolskirt3.id and cho_whoring < 3:
        cho "I couldn't focus on the game!"
        cho "This ridiculously short skirt! The whole match it kept on slipping over my bottoms!"
        m "So what? Just ignore it..."
        cho "Ignore it? And let everyone ogle at my bare ass?"
        m "Aren't you still wearing panties?"
        cho "Of course I am! And I don't intent to show them to the whole school!"
        cho "Just enough to let Cedric have a peek..."
        g4 "\"Just a peek\" won't do, [cho_name]! You have to reveal everything!"
        g4 "If the entire school knows the color of your panties, that's when you have done your task well!"
        cho "You are asking too much of me, [cho_genie_name]! I'd never be able to do such a thing..."
        m "Give it some time, girl. We'll get you to be more confident on your broom soon enough..."
        g9 "With your panties on display!"
        cho "(...)"
        cho "It's getting late..."
        cho "If you don't mind I'd like to go to bed now."
        m "Sure. You may leave..."
        cho "Have a good night, Sir."

    # Position response
    elif quidditch_position != "above":
        cho "Our tactic didn't work, [cho_genie_name]."
        cho "Cedric just ignored me for most of the game and ended up catching the snitch..."
        m "Were you trying to distract him enough?"
        cho "Of course I was! I tried to let him have a peek up my skirt, but I'm not sure he even noticed that I was wearing one."
        m "Interesting..."
        m "Maybe we need to tackle this situation from another angle."
        cho "Whatever you say, [cho_genie_name]."
        cho "I'll be going to bed now if you don't mind."
        cho "Have a good night, Sir."
        m "You too..."

    else:
        cho "Cedric didn't seem too distracted by me... He ended up catching the snitch and..."
        cho "I'm not sure what the problem was..."
        m "Maybe we aren't using the right tactics."
        cho "Lets try a different approach next time, [cho_genie_name]."
        cho "I have to head back to our dorms and get some sleep..."
        m "Sure. You may go..."
        cho "Have a good night, Sir."

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    $ cho_class.equip(cho_outift_last) # Equip last worn clothes

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
    cho "Yes, [cho_genie_name]! Thank you so much!"
    cho "If there is any way I can return the favour...?"

    if cc_pf_talk_OBJ.points == 0:
        m "Why don't we start with that, Miss Chang,...{w} favours!"
        m "I did prove the effectiveness of my methods to you. Now it's your turn to stay true to your promise..."
        cho "Of course, Sir."
        cho "But, if you don't mind..."
    else:
        g9 "You could sell some more favours to me!"
        cho "Is it just talking?"
        m "I had hoped for something more... advanced."
        cho "(...)"
        cho "If you don't mind, maybe some other time, Sir."

    cho "The whole house is celebrating our win at the moment... And I'd rather not miss spending some time with-"
    g4 "You did well today, [cho_name]."
    g9 "Go and party! You've earned it."
    cho "Thank you, [cho_genie_name],... for everything."
    cho "Have a good night!"

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_class.equip(cho_outift_last) # Equip last worn clothes

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
    cho "Please don't, [cho_genie_name]! I was merely joking!"
    m "Would you say you've had enough practive to play against them in a tourney game?"
    cho "Absolutely! The next time we will confront \"Hufflepuff\", they will be crushed!"
    cho "This should be an easy win for \"Ravenclaw\"."
    cho "Speaking of which, I need to get back to my team now, [cho_genie_name]."
    cho "Thank you for helping me!"
    m "You're welcome."
    cho "Good night, Sir."

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_class.equip(cho_outift_last) # Equip last worn clothes

    $ cho_busy = True

    jump main_room
