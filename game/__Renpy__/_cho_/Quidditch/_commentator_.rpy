

### Quidditch Commentator Quests ###

label quidditch_commentator_event_1:

    call cho_walk("desk", "base", action="enter", speed=2)

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
    call cho_main("No. Someone has to announce the points after all.","annoyed","narrow","base","mid")
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
            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?","open","narrow","raised","mid")
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...","open","closed","raised","mid")
            call cho_main("Trust me, [cho_genie_name], Luna would be a terrible choice!","soft","angry","angry","mid")
            m "Fine. How about..."
            jump who_shall_commentate

    call cho_main("Hermione Granger?","scream","shocked","raised","mid")
    call cho_main("She wouldn't know the first thing about quidditch!","open","angry","angry","mid")
    call cho_main("You can't pick her!","upset","closed","raised","mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    call cho_main("Absolutely not! I won't talk to that Gryffindor skunk ever again!","scream","closed","angry","mid")
    call cho_main("Didn't I make it clear that I don't want her to \"ever\" be involved in Quidditch again?","annoyed","narrow","angry","mid")
    m "Alright, are there any other students who know Quidditch rules well enough to take this... Jordan boy's place?"
    call cho_main("...","pout","base","base","down")
    m "Well?"
    call cho_main("Well, most of them would be on one of the Quidditch teams...","soft","base","raised","R")
    call cho_main("But Granger wouldn't know anything about Quidditch either!","pout","narrow","angry","mid")
    m "Do you know anybody else suited for the job?"
    call cho_main("{size=-4}Probably anyone at this point...{/size}","pout","base","raised","R")
    call cho_main("(Wait a minute...)","pout","wide","raised","mid")
    call cho_main("No...","smile","base","base","mid") #Mischievous smile
    g9 "I'll ask her... What's the worst that could happen..."
    call cho_main("Yeah, actually you're probably right...","angry","angry","angry","mid")
    m "Don't worry she'll do a-{w=1.0}{nw}"
    g4 "Wait... what did you say?"
    call cho_main("I'm sure she'll do a heckin good job!","smile","angry","angry","mid")
    call cho_main("(She'll flub the whole thing and everyone will laugh at her.)","smile","angry","angry","R") #Mischievous smile
    g9 "Well, great then. I'll ask her in that case!"
    call cho_main("(She'll be humiliated and no one will ever see her as anything but a showoff that knows nothing!)","quiver","angry","angry","down")
    call cho_main("(I can already picture it...{w=0.8} the whole school laughing...)","quiver","base","raised","up")
    m "Miss Chang?"
    call cho_main("Oh, thank you for handling it professor! Boy, you took a load off my mind...","open","base","base","mid",trans="hpunch")
    call cho_main("I'll be heading back to classes now, if you don't mind.","soft","closed","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    call bld
    m "(...)"

    $ cho_busy = True

    jump main_room


label quidditch_commentator_event_2:
    call her_main(xpos="mid",ypos="base",trans="fade")

    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I mean, I've taken flying lessons... they're mandatory.","open","baseL")
    m "Ah, okay... and here I was hoping that you'd be able to commentate this years quidditch games..."
    call her_main("Me, wasting time on something as stu...{w=0.8}{nw}","base","closed")
    call her_main("Wait...{w=0.6} What did you say?","open","suspicious")
    m "I was going to ask you if you'd commentate this years quidditch games..."
    call her_main("You want me... to commentate this years wizarding school cup?","open","wide_stare")
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
    g4 "I thought you just said you didn't..."
    call her_main("Cho will be so mad!","crooked_smile","squint")
    m "I see..."
    g9 "Congratulations then, [hermione_name]! You got the j..."
    call her_main("Ah!!! I better start lear...{w=0.8} I mean, preparing my opening speech!","open","wide_stare",trans="hpunch")

    call her_walk(action="leave", speed=1.7)

    call bld
    m "Aaaa-nd, she's gone..."
    m "I better tell Cho about the...{w=0.8} news."

    $ hermione_busy = True

    jump main_room


label quidditch_commentator_event_3:
    call cho_main(xpos="mid",ypos="base",trans="fade")

    g9 "I've got great news for you! I found us a new commentator!"
    call cho_main("Is it Hermione?","soft","closed","base","mid")
    g9 "Yes! Very good guess!"
    call cho_main("It wasn't a guess, [cho_genie_name]. We've discussed her already.","pout","narrow","angry","mid")
    m "Oh, sure..."
    call cho_main("But I'm surprised she even took up the task...","pout","base","base","R")
    g9 "Right away. No questions asked."
    call cho_main("And little miss Granger wasn't even the slightest bit intimidated by her new obligation?","open","base","raised","mid")
    g9 "Not at all. She seemed rather joyous of her situation."
    call cho_main("Oh...","pout","base","sad","down") # Bit sad.
    call cho_main("Well she just doesn't know what's coming towards her yet!","annoyed","angry","angry","mid") # Mischievious smile
    call cho_main("{size=-4}I hope she gets hit by a bludger as well! I might even tell the boys to aim at her once or twice!{/size}","angry","angry","angry","R") # Small text.
    g9 "Make sure you tell everyone your great and very proactive headmaster sorted everything out..."
    call cho_main("Oh, I will. Thank you very much!","soft","base","base","mid")
    call cho_main("(...)","pout","base","base","R")

    if daytime:
        call cho_main("I do have to head back to classes now.","open","closed","base","down")
    else:
        call cho_main("It's getting a bit late so I'll just head back to the dorms.","open","base","base","R")

    call cho_main("See you for our next training session, [cho_genie_name].","smile","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    $ cho_busy = True

    jump main_room





### Old Content ###
# Might be used for future Quidditch events.

label nothing_to_see_here_001:
    call play_sound("door")
    call cho_main("...","pout","narrow","sad","R",xpos="mid",ypos="base")
    m "Miss Chang... In case you were wondering, I haven't gotten around to firing miss granger yet..."
    call cho_main("Oh... Um... About that...","soft","narrow","raised","R")
    call cho_main("Could you please... not... do that...","open","base","sad","down")
    g4 "What? You want Hermione to keep commentating your games?"
    g4 "What about our strategies?"
    call cho_main("We can still do them...","soft","base","raised","down")
    call cho_main("...","pout","base","raised","R")
    m "[cho_name], is there something you're not telling me?"
    call cho_main("Well...","soft","narrow","raised","R")
    call cho_main("It's just that...","open","narrow","sad","mid")
    call cho_main("People have been a lot nicer to me since that game!","quiver","narrow","sad","mid")
    call cho_main("All the gryffindors are inviting me to parties...","soft","base","raised","down")
    call cho_main("Most of the Slytherins have stopped being racist...","open","closed","angry","mid")
    call cho_main("And the hufflepuff team weren't even upset that i beat them!","open","base","raised","L")
    m "So you want to keep on with my coaching?"
    call cho_main("Of course! It's the only chance Ravenclaw has to win the W.S.C.!","pout","narrow","raised","down")
