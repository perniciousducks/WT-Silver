

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

    # Cho leaves
    call cho_walk("mid","leave",2)

    $ cho_busy = True
    if quidditch_commentator == "Hermione": # Hermione has to commentate.
        $ hermione_busy = True
    $ quidditch_match_in_progress = True

    jump main_room





# Check if Cho won or lost the practice game.
label quidditch_match_return:

    # Hufflepuff Match
    if main_matches_won == 0:
        # First practice game.
        if huffl_matches_won == 0:
            # Win
            if cho_quidditch_bottom in ["skirt_long"] and quidditch_position == "above":
                $ huffl_matches_won = 1
                jump hufflepuff_practice_win_1
            # Lose
            else:
                jump hufflepuff_practice_lost
        # Second practice game.
        else:
            # Win
            if cho_quidditch_bottom in ["skirt_short"] and quidditch_position == "above" and cho_whoring >= 3:
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

    # Genie asks if Cedric was distracted by her outfit
    # Cho responds either that he was or wasn’t

    # If he was, but the event failed, he’ll ask why he wasn’t distracted enough
    # Cho responds by saying that she didn’t feel comfortable while flying, almost acted clumsy
    call cho_walk("door","mid",2.2)

    m "So, how did it go?"
    cho "We lost..."

    m "What was the problem?"
    cho "I'm not really sure, [cho_genie_name]."

    if cho_quidditch_bottom in ["pants_long","pants_short"]:
        cho "Cedric didn't seem too distracted by me. He ended up catching the snitch."

    elif cho_quidditch_bottom in ["skirt_short"] and cho_whoring < 2:
        cho "I couldn't really focus on the game too much."
        cho "My skirt just kept on slipping over my bottoms..."
        cho "How I'm supposed to fly with a skirt this short?"
        m "I don't think the skirt was the issue here."
        m "(Maybe I need her to get more confident flying with it.)"

    else:
        cho "I tried my best, however."
        cho "I was trying to distract Cedric with my skirt, just like you've said..."


    # Cho leaves
    call cho_walk("mid","leave",2.2)

    $ cho_mood += 9
    $ cho_busy = True

    jump main_room



# Won first Hufflepuff match.
label hufflepuff_practice_win_1:
    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    menu:
        "\"Come in!\"":
            cho "Yes, [cho_genie_name]..."
        "\"Who is it?\"":
            cho "Cho Chang, [cho_genie_name]."
            m "Ah miss Chong... Come on in!"
            cho "..."

    call play_sound("door")
    call cho_walk("door","mid",2)

    call cho_main("...","annoyed","suspicious","angry","R",xpos="mid",ypos="base")
    m "You seem a little on edge today..."
    call cho_main("On edge?","scream","shocked","angry","mid")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!","angry","wide","angry","mid")
    call cho_main("You had to have me do this on the day half of \"hufflepuff\" shows up to watch the practice didn't you!","pout","suspicious","angry","R")
    call cho_main("I bet you were probably in on it...","upset","suspicious","angry","mid")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    m "Score many... points?"
    m "(I hope this stupid game has points...)"
    call cho_main("As a matter of fact I did!","open","closed","base","mid")
    call cho_main("{size=+10}150 of them!!!{/size}","scream","base","base","mid")
    m "Wow... That seems like a lot!"
    call cho_main("Of course it is, I caught the snitch!","smile","closed","base","mid")
    m "(The snitch? Is this prison rules?)"
    call cho_main("Today, I was racing after the snitch along with that blockhead Cedric Diggory...","open","base","sad","R")
    call cho_main("I'm normally never fast enough to beat him with my crummy old nimbus 2010...","pout","angry","angry","downR")
    call cho_main("But today I just flew above him as we were both after the snitch!","smile","base","base","mid")
    call cho_main("Ah!!! I can't believe I was able to finally catch it!","smile","closed","base","mid")
    m "Is this the first time you've caught the... snitch?"
    call cho_main("Of course! This is the first game of quidditch \"Ravenclaw\" has won in over six years!","smile","base","base","mid")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices, [cho_genie_name]...","annoyed","suspicious","sad","downR")
    m "oh..."
    call cho_main("\"Ravenclaw\"... isn't very good...","pout","suspicious","sad","down")
    call cho_main("But I have a feeling that's going to change this year!","smile","closed","base","mid")

    call cho_walk("mid","leave",2)
    $ cho_busy = True

    jump main_room




label hufflepuff_practice_win_2:
    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    m "Come in..."
    call play_sound("door")
    call cho_walk("door","mid",2)


    call cho_main("I hate you, I hate you, I HATE YOU!","scream","closed","angry","mid",trans="hpunch")
    m "Good hustle. Nice work catching that gold thing..."
    call cho_main("This isn't the time for your stupid jokes!","open","angry","angry","mid")
    call cho_main("I've never felt so humiliated in my entire life!","open","angry","angry","R")
    m "It wasn't that bad, was it? At least you won."
    call cho_main("At the expense of my dignity!","quiver","base","raised","down")
    call cho_main("Lee Jordan only used to say that I had a nice butt!","soft","base","sad","down")
    call cho_main("Hermione is the absolute wors commentator Quidditch has ever seen!","open","base","raised","R")
    m "She wasn't that bad..."
    call cho_main("She is as incompetent as one can possibly be!","open","base","raised","R")
    call cho_main("This just can't go on! I insist you fire Hermione!","open","closed","base","mid")
    call cho_main("Otherwise I'm going to stop listening to your ridiculous coaching!","open","angry","angry","mid")
    m "Ugh... fine..."
    call cho_main("Good...","pout","angry","angry","mid")

    call cho_walk("mid","leave",2)
    $ cho_busy = True

    jump main_room
