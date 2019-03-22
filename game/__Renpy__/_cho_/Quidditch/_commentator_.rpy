

### Quidditch Commentator Quests ###

label quidditch_commentator_event_1:
    call play_sound("door")

    call cho_main("[cho_genie_name], there's been a disaster!","scream","closed","angry","mid",xpos="mid",ypos="base")
    m "What? Did something happen during your game?"
    call cho_main("Why would-... [cho_genie_name], Ravenclaw wasn't even playing today...","open","angry","angry","mid")
    call cho_main("I'm talking about what happened to Lee Jordan, our commentator!","quiver","angry","angry","R")
    m "You have a commentator for practice games?"
    call cho_main("The commentators need to practice too!","open","angry","raised","mid")
    m "So what happened to him?"
    call cho_main("he was hit in the throat by a bludger during yesterdays game between gryffindor and slytherin.","quiver","base","raised","down")
    m "Ouch..."
    call cho_main("Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season.","soft","closed","sad","mid")
    call cho_main("What are we going to do! We can't have a \"W.S.C.\" without a commentator!","soft","base","sad","mid")
    m "Can't you play without one?"
    cho "No! Someone has to announce the points after all."
    m "Fine..."

    label who_shall_commentate:
    menu:
        m "How about we ask..."
        "\"Hermione\"":
            pass
        "\"Astoria\"" if astoria_unlocked:
            call cho_main("That brat?","scream","shocked","raised","mid")
            call cho_main("Not a chance!","open","closed","angry","mid")
            call cho_main("Besides, [cho_genie_name], did you forget that she's a slytherin?","open","angry","angry","mid")
            m "Right. No slytherins. Got it."
            m "How about..."
            jump who_shall_commentate
        "\"Luna\"" if luna_unlocked:
            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?","open","suspicious","raised","mid")
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...","open","closed","raised","mid")
            call cho_main("Trust me, [cho_genie_name], Luna would be a terrible choice!","soft","angry","angry","mid")
            m "Fine. How about..."
            jump who_shall_commentate

    call cho_main("Hermione Granger?","scream","shocked","raised","mid")
    call cho_main("She wouldn't know the first thing about quidditch!","open","angry","angry","mid")
    call cho_main("You can't pick her!","upset","closed","raised","mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    cho "Absolutely not! I won't talk to that Gryffindor skunk ever again!"
    cho "Didn't I make it clear that I don't want her to \"ever\" be involved in Quidditch again?"

    # ADD bridge here!

    m "Do you know of anybody else suited for the job?"
    cho "(...)"
    cho "No..."
    m "I'll ask her. She'll probably say no anyways."
    cho "I hope that's the case..."
    cho "I'll be heading back to classes now, if you don't mind."
    m "Have fun."

    # Cho leaves.

    jump main_room


label quidditch_commentator_event_2:
    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I know {b}EVERYTHING{/b} about quidditch!","open","angry",xpos="close",ypos="base")
    m "Not too humble, are we?"
    call her_main("Do you really think that I, Hermione Granger, would be lacking in a subject so basic as quidditch?","open","closed")
    call her_main("Not to mention I've been dragged along to every single one of Harry and Ron's games...","open","angry")
    m "So you'd know enough to commentate then?"
    call her_main("Wait,... you want me to commentate this years wizarding school cup?","open","wide_stare")
    call her_main("I'd be honoured, sir!","scream","closed",trans="hpunch")
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...","open","angry")
    call her_main("Not to mention getting to make all the announcements...","smile","baseL")
    call her_main("The speeches...","grin","squint")

    if her_whoring < 18:
        call her_main("The paper...","soft","ahegao")
        call her_main("The {image=textheart}{i}preparation{/i}{image=textheart}...","open_tongue","ahegao_raised")
    else:
        call her_main("Everybody will be focused on me...","soft","ahegao")

    call her_main("I accept!","scream","angryCl",trans="hpunch")
    m "Congratulations, [hermione_name]! You got the j..."
    call her_main("Yay!","smile","happy")
    call her_main("Ah!!! I better start preparing my opening announcements in front of the mirror!!!","open","wide_stare",trans="hpunch")

    call her_walk("mid","leave",1.7)

    m "Aaaa-nd, she's gone..."
    m "I better tell Cho about the news."

    $ hermione_busy = True

    jump main_room


label quidditch_commentator_event_3:
    g9 "I've got great news for you! I found us a new commentator!"
    cho "Is it Hermione?"
    g4 "Yes! Very good guess!"
    m "How did you know?"
    cho "Wasn't that difficult, after all she was our only possible option!!!" # Slightly angry
    m "I'm sure she'll be great."
    cho "Don't make me regret this, [cho_genie_name]!"
    g9 "Cheer up! This will be fun!"
    cho "(...)"

    if daytime:
        cho "I have to head back to classes."
    else:
        cho "It's getting late. I have to head back to out dorms."

    cho "See you for our next training session, [cho_genie_name]."

    # Cho leaves.
    call cho_walk("mid","leave",2.5)

    $ cho_busy = True

    jump main_room





### Old Content ###
# Might be used for future Quidditch events.

label nothing_to_see_here_001:
    call play_sound("door")
    call cho_main("...","pout","suspicious","sad","R",xpos="mid",ypos="base")
    m "Miss Chang... In case you were wondering, I haven't gotten around to firing miss granger yet..."
    call cho_main("Oh... Um... About that...","soft","suspicious","raised","R")
    call cho_main("Could you please... not... do that...","open","base","sad","down")
    g4 "What? You want Hermione to keep commentating your games?"
    g4 "What about our strategies?"
    call cho_main("We can still do them...","soft","base","raised","down")
    call cho_main("...","pout","base","raised","R")
    m "[cho_name], is there something you're not telling me?"
    call cho_main("Well...","soft","suspicious","raised","R")
    call cho_main("It's just that...","open","suspicious","sad","mid")
    call cho_main("People have been a lot nicer to me since that game!","quiver","suspicious","sad","mid")
    call cho_main("All the gryffindors are inviting me to parties...","soft","base","raised","down")
    call cho_main("Most of the Slytherins have stopped being racist...","open","closed","angry","mid")
    call cho_main("And the hufflepuff team weren't even upset that i beat them!","open","base","raised","L")
    m "So you want to keep on with my coaching?"
    call cho_main("Of course! It's the only chance Ravenclaw has to win the W.S.C.!","pout","suspicious","raised","down")
