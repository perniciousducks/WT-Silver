

### Quidditch Outfit Customization ###

# Wear Pants
label use_quidditch_pants_1:

    # Intro
    if "pants_1" not in quid_outfit_intro:
        $ quid_outfit_intro.append("pants_1")

    m "I'd like you to wear trousers for your games again."
    call cho_main("Really? Just my regular pants?","annoyed","base","raised","mid")
    m "Yes. Regular ole- pants."
    m "I know what I'm doing..."
    call cho_main("If you say so, [cho_genie_name].","base","base","base","mid")

    $ cho_quidditch_bottom = "pants_long" # For testing.

    return



# Wear Short Pants
label use_quidditch_pants_2:

    # Intro
    if "pants_2" not in quid_outfit_intro:
        $ quid_outfit_intro.append("pants_2")

        m "Do you happen to have Quidditch trousers that are a bit shorter?"
        m "Some sort of hot-pants?"
        call cho_main("I do. I typically wear them in the summer.","open","base","raised","mid")
        m "Well I'd like you to wear them all the time!"
        call cho_main("Even when it's cold, and raining?","soft","base","sad","mid")
        g9 "Especially when it's raining."
        call cho_main("Ok, [cho_genie_name]. I'll put them on.","annoyed","base","base","mid")

    # Repeat
    else:
        m "I'd like you to wear those hot-pants duing your games again."
        call cho_main("Alright. I see nothing wrong with that.","soft","base","base","down")
        call cho_main("I just hope it won't get too cold on our next game...","annoyed","base","sad","mid")

    $ cho_quidditch_bottom = "pants_short" # For testing.

    return



# Wear Skirt
label use_quidditch_skirt_1:

    # Intro
    if "skirt_1" not in quid_outfit_intro:
        $ quid_outfit_intro.append("skirt_1")
        m "Why don't you wear a skirt while playing?"
        call cho_main("A skirt?!","soft","wide","base","mid")
        call cho_main("I couldn't do that!","scream","wide","angry","mid")
        call cho_main("Everyone would be able to see straight up it!","quiver","wide","angry","downR")
        call cho_main("Not to mention all the other players-","horny","narrow","sad","R")
        call cho_main("Oh...","pout","narrow","angry","mid")
        call cho_main("So that's your plan then? For me to distract \'the enemy\' with some upskirt?","pout","angry","angry","mid")
        m "If you don't think it would work-"
        call cho_main("Of course it would work! Those \'boys\' are all a bunch of perverts...","open","narrow","angry","R")
        call cho_main("But I can't go and play a game with a skirt on!","horny","wide","sad","down")
        call cho_main("All my friends would see!","annoyed","shocked","sad","mid")
        m "They'll forget all about it after you have won!"
        call cho_main("I highly doubt that...","upset","narrow","sad","downR")
        m "Then just tell them it was the only way to win. I'm sure they'll understand."
        call cho_main("You... might be right...","open","base","sad","downR")
        call cho_main("Alright! I'll do it!","smile","base","base","mid")
        call cho_main("Go Go \'Ravenclaw\'!","scream","closed","sad","mid")

    # Repeat
    else:
        m "I'd like you to wear a skirt for your games."
        call cho_main("Ok, [cho_genie_name]. If I have to.","soft","base","base","R")
        m "You have to if you want to win this."
        call cho_main("I hope you're' right.","soft","closed","angry","mid")
        call cho_main("This is going to be so embarrassing...","quiver","base","sad","down")

    $ cho_quidditch_bottom = "skirt_long" # For testing.

    return



label use_quidditch_skirt_2: # Not in use.

    # Intro
    if "skirt_2" not in quid_outfit_intro:
        $ quid_outfit_intro.append("skirt_2")
        m "Seeing as how the skirt was such a success, how about we up the ante a bit?"
        call cho_main("How do you mean?","open","narrow","raised","mid")
        m "Well, that skirt seemed a little long to me..."
        m "If you took a few inches off of it, maybe the other players wouldn't be able to keep their eyes off of you."
        call cho_main("Well I suppose I could take another inch or two off...","quiver","narrow","sad","downR")
        call cho_main("But we better win the next practice against \"Hufflepuff\"!","scream","narrow","angry","mid")
        m "Hey, the games up to you... All I can give is pointers."
        call cho_main("Hmph... That's not what a coach is supposed to say!","pout","narrow","angry","mid")
        call cho_main("You're supposed to believe in me!","open","closed","angry","mid")
        m "You've gotta show some commitment to the game first."
        call cho_main("commitment...","angry","shocked","angry","mid")
        call cho_main("Isn't wearing a skirt enough?","pout","narrow","angry","R")
        m "For now..."
        call cho_main("What's that supposed to mean?","upset","narrow","angry","mid")
        m "It means stop being such a prude and shorten that skirt!"
        call cho_main("...","pout","base","sad","R")
        call cho_main("fine...","annoyed","narrow","sad","down")

    # Repeat
    else:
        m "I'd like you to wear your short skirt again."
        cho "Why always the short one, [cho_genie_name]?"
        m "Naturally, so the other players probably wouldn't be able to keep their eyes off of you?"
        call cho_main("They already can't keep their eyes off of me...","smile","closed","base","mid")
        m "For now... They'll probably get bored of that skirt after a while..."
        call cho_main("They will not!","scream","shocked","angry","mid")
        m "Are you going to let me coach you or not?"
        call cho_main("...","pout","narrow","angry","R")
        call cho_main("How much shorter?","horny","narrow","sad","mid")
        m "Just a few inches..."
        call cho_main("Alright...","base","narrow","sad","down")

    $ cho_quidditch_bottom = "skirt_short" # For testing.

    return



# Remove Coat
label remove_quidditch_coat:
    m "It's about time you lose that robe of yours while you play."
    call cho_main("What? I'll freeze!","open","shocked","raised","mid")
    m "You're a witch aren't you?"
    m "Get creative..."
    call cho_main("I suppose I can use a warmth charm...","pout","base","raised","R")
    call cho_main("But everyone will see my butt!","quiver","base","raised","down")
    g4 "That's the point."
    call cho_main("But, but, but!","open","closed","sad","mid")
    g9 "That's probably what the crowd will be chanting..."

    if cho_tier < 2: # Hasn't won against Hufflepuff yet.
        call cho_main("I'm sorry [cho_genie_name], but you expect me to play without the most basic equipment and expect me to win!","open","shocked","raised","mid")
        m "What do you even need that coat for?"
        call cho_main("To keep dry should it start raining, for one.{w} And to keep my broom steady if the wind is too strong.","soft","base","base","R")
        call cho_main("After all, flying is all about aerodynamics, [cho_genie_name].","open","closed","base","mid")
        call cho_main("Playing without a coat on is out of the question!","annoyed","base","angry","mid")
        m "Fair enough..."
        m "(Guess I have to try something else then.)"

        return "fail"

    else:
        call cho_main("*Ugh*...","quiver","angry","angry","mid")
        call cho_main("Fine...","pout","angry","angry","R")
        call cho_main("But-{w} I better win!","soft","angry","raised","mid")

    return


# Remove Gloves
label remove_quidditch_gloves: # Not in use.
    m "You should remove those bulky looking gloves of yours."
    cho "My gloves? But I need them to play!"
    cho "They are made out of pure \"Insert fantasy creature here\" leather! Their friction is necessary If I want to keep a good grip on my broom."
    cho "And how would I even be able to catch the snitch without them?"
    m "With your mouth?"
    cho "That's just stupid!"
    m "Fair enough... Keep them on then."

    return
