

### Quidditch Outfit Customization ###

label change_quidditch_outfit:
    # Replace this menu with a proper wardrobe panel.
    menu:
        "-Change her bottom-":
            menu:
                "-Pants-":
                    call use_quidditch_pants_1
                "-Short Pants-":
                    call use_quidditch_pants_2
                "-Skirt-":
                    call use_quidditch_skirt_1
                "-Short Skirt-" if huffl_matches_won >= 1:
                    call use_quidditch_skirt_2

            jump change_quidditch_outfit
        "-Remove her coat-":
            call remove_quidditch_coat
        "-Remove her gloves-":
            call remove_quidditch_gloves
        "-Go back-":
            jump cho_training_menu
            
    call update_cho_quidditch_outfit

    jump change_quidditch_outfit



# Wear Pants
label use_quidditch_pants_1:
    m "I'd like you to wear pants for your games again."
    cho "Really? Just my regular pants?"
    m "Yes. Regular ole- pants."
    m "I know what I'm doing..."
    cho "If you say so, [cho_genie_name]."

    $ cho_quidditch_bottom = "pants_long" # For testing.

    return



# Wear Short Pants
label use_quidditch_pants_2:
    if not quid_pants_2_intro:
        $ quid_pants_2_intro = True
        m "Do you happen to have Quidditch pants that are a bit shorter?"
        m "Some sort of hot-pants?"
        cho "I do. I typically wear them in the summer."
        m "Well I'd like you to wear them all the time!"
        cho "Even when it's cold, and raining?"
        g9 "Especially when it's raining."
        cho "Ok, [cho_genie_name]. I'll put them on."
    else:
        m "I'd like you to wear those hot-pants duing your games again."
        cho "Alright. I see nothing wrong with that."
        cho "I just hope it won't get too cold on our next game..."

    $ cho_quidditch_bottom = "pants_short" # For testing.

    return



# Wear Skirt
label use_quidditch_skirt_1:
    if not quid_skirt_1_intro:
        $ quid_skirt_1_intro = True
        m "Why don't you wear a skirt while playing?"
        cho "A skirt?!"
        call cho_main("I couldn't do that!","scream","wide","angry","mid")
        call cho_main("Everyone would be able to see straight up it!","quiver","wide","angry","downR")
        call cho_main("Not to mention all the other player-","horny","suspicious","sad","R")
        call cho_main("Oh...","pout","suspicious","angry","mid")
        call cho_main("So that's your plan then? For me to distract \'the enemy\' with some upskirt?","pout","angry","angry","mid")
        m "If you don't think it would work-"
        call cho_main("Of course it would work! Those \'boys\' are all a bunch of perverts...","open","suspicious","angry","R")
        call cho_main("But I can't go and play a game with a skirt on!","horny","shocked","sad","down")
        call cho_main("All my friends would see!","annoyed","shocked","sad","mid")
        m "They'll forget all about it after you defeat you have won!"
        call cho_main("I highly doubt that...","upset","suspicious","sad","downR")
        m "Then just tell them it was the only way to win. I'm sure they'll understand."
        call cho_main("You... might be right...","open","base","sad","downR")
        call cho_main("Alright! I'll do it!","smile","base","base","mid")
        call cho_main("Go Go \'Ravenclaw\'!","scream","closed","sad","mid")

    else:
        m "I'd like you to wear a skirt for your games."
        cho "Ok, [cho_genie_name]. If I have to."
        m "You have to if you want to win this."
        cho "I hope you're' right."
        cho "This is going to be so embarrassing..."

    $ cho_quidditch_bottom = "skirt_long" # For testing.

    return



label use_quidditch_skirt_2:
    if not quid_skirt_2_intro:
        $ quid_skirt_2_intro = True
        m "Seeing as how the skirt was such a success, how about we up the ante a bit?"
        call cho_main("How do you mean?","open","suspicious","raised","mid")
        m "Well, that skirt seemed a little long to me..."
        m "If you took a few inches off of it, maybe the other players wouldn't be able to keep their eyes off of you."
        call cho_main("Well I suppose I could take another inch or two off...","quiver","suspicious","sad","downR")
        call cho_main("But we better win the next practice against \"Hufflepuff\"!","scream","suspicious","angry","mid")
        m "Hey, the games up to you... All I can give is pointers."
        call cho_main("Hmph... That's not what a coach is supposed to say!","pout","suspicious","angry","mid")
        call cho_main("You're supposed to believe in me!","open","closed","angry","mid")
        m "You've gotta show some commitment to the game first."
        call cho_main("commitment...","angry","shocked","angry","mid")
        call cho_main("Isn't wearing a skirt enough?","pout","suspicious","angry","R")
        m "For now..."
        call cho_main("What's that supposed to mean?","upset","suspicious","angry","mid")
        m "It means stop being such a prude and shorten that skirt!"
        call cho_main("...","pout","base","sad","R")
        call cho_main("fine...","annoyed","suspicious","sad","down")

    else:
        m "I'd like you to wear your short skirt again."
        cho "Why always the short one, [cho_genie_name]?"
        m "Naturally, so the other players probably wouldn't be able to keep their eyes off of you?"
        call cho_main("They already can't keep their eyes off of me...","smile","closed","base","mid")
        m "For now... They'll probably get bored of that skirt after a while..."
        call cho_main("They will not!","scream","shocked","angry","mid")
        m "Are you going to let me coach you or not?"
        call cho_main("...","pout","suspicious","angry","R")
        call cho_main("How much shorter?","horny","suspicious","sad","mid")
        m "Just a few inches..."
        call cho_main("Alright...","base","suspicious","sad","down")

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

    if main_matches_won < 1: # Hasn't won against Hufflepuff yet.
        cho "This is just ridiculous!"
        cho "I will not play Quidditch without a coat on."
        # Maybe she can explain here why the coat is so important for Quidditch. Aerodynamics maybe?
        m "(...)"
        m "(Guess I have to try something else.)"
        $ cho_quidditch_coat = True # For testing.

    else:
        call cho_main("Ugh...","quiver","angry","angry","mid")
        call cho_main("Fine...","pout","angry","angry","R")
        call cho_main("But-{p} I better win!","soft","angry","raised","mid")

        # Remove coat from Quidditch outfit here.
        $ cho_quidditch_coat = False # For testing.

    return


# Remove Gloves
label remove_quidditch_gloves:
    m "You should remove those bulky looking gloves of yours."
    cho "My gloves? But I need them to play!"
    cho "They are made out of pure \"Insert fantasy creature here\" leather! Their friction is necessary If I want to keep a good grip on my broom."
    cho "And how would I even be able to catch the snitch without them?"
    m "With your mouth?"
    cho "That's just stupid!"
    m "Fair enough... Keep them on then."

    $ cho_quidditch_coat = True # For testing.

    return
