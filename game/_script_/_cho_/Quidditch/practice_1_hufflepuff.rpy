

# Started first training match against Hufflepuff

label cc_ht_start:

    call cho_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # First Hufflepuff match.
    m "So, when will those Quidditch matches take place?"
    call cho_main("We could arrange one for today. Just for practice, against Hufflepuff.", "open", "base", "base", "R")
    m "Really? Just like that?"
    call cho_main("Why yes. The Hufflepuff team wouldn't give up a chance to play against us for training.", "soft", "base", "raised", "mid")
    call cho_main("They'd welcome every opportunity to test us and study our tactics...", "open", "narrow", "angry", "mid")
    call cho_main("All I need to do is give their team captain a heads up during classes.", "base", "base", "base", "mid")
    m "Great. Get your team ready cause you are going to play today."
    call cho_main("I will, [cho_genie_name]. Wish me luck.", "smile", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_quid.commentator == "hermione": # Hermione has to commentate.
        $ hermione_busy = True

    $ cho_quid.in_progress = True

    jump end_cho_event

label cc_ht_return:
    # Cho enters.
    call play_sound("knocking")
    call bld
    "*knock* *knock* *knock*"

    menu:
        "\"Come in!\"":
            cho "Yes, [cho_genie_name]..."
        "\"Who is it?\"":
            cho "Cho Chang, [cho_genie_name]."
            m "Come on in, [cho_name]!"
            cho "..."

    call cho_walk(xpos="mid", ypos="base", action="enter")

    call cho_main("(...)", "annoyed", "narrow", "angry", "R", xpos="mid", ypos="base", trans=d3)
    m "You seem a little on edge..."
    call cho_main("On edge?", "scream", "wide", "angry", "mid")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!", "angry", "wide", "angry", "mid")
    call cho_main("You had to have me do this on the day half of Hufflepuff shows up to watch us practise, didn't you!", "annoyed", "narrow", "angry", "R")
    call cho_main("I bet you were probably in on it...", "upset", "narrow", "angry", "mid")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    call play_music("cho")
    call cho_main("{size=+10}I got it!!!{/size}", "scream", "base", "base", "mid")
    call cho_main("I caught the snitch!", "smile", "happyCl", "base", "mid")
    m "Congratulations..."
    call cho_main("That blockhead Cedric didn't stand a chance against me!", "open", "base", "angry", "R")
    call cho_main("Usually I'm never fast enough to beat him with my crummy old nimbus...", "annoyed", "narrow", "angry", "downR")
    call cho_main("But today, I flew above him as we both raced after the snitch, just like you said I should.", "smile", "base", "base", "mid")
    g9 "Sounds like somebody should get a reward for their efforts!"
    call cho_main("I can't believe I was able to finally catch it!", "grin", "happyCl", "base", "mid")
    m "Is this the first time you've caught one?"
    call cho_main("*Mhmm*...{w=0.3} This is the first game of quidditch Ravenclaw has won in over six years!", "smile", "base", "base", "mid")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices, [cho_genie_name]...", "annoyed", "narrow", "worried", "downR")
    m "Oh..."
    call cho_main("Ravenclaw...{w} isn't very good...", "annoyed", "narrow", "worried", "down")
    call cho_main("But I have a feeling that's going to change this year!", "base", "happyCl", "base", "mid")
    g9 "And I am happy to be of help!"
    call cho_main("Yes, [cho_genie_name]! Thank you so much!", "smile", "narrow", "base", "mid")
    call cho_main("If there is any way I can return the favour...?", "horny", "base", "raised", "mid")
    m "Yes, but we can discuss that after you've won the game."
    g9 "And have you do some more {b}advanced{/b} favours for me."
    call cho_main("More advanced... Sir?", "soft", "narrow", "worried", "mid")
    #m "Would you say you've had enough practice to play against them in a tourney game?"
    #call cho_main("Absolutely! The next time we will confront Hufflepuff, they will be crushed!", "smile", "narrow", "angry", "mid")
    #call cho_main("This should be an easy win for Ravenclaw.", "base", "closed", "base", "mid")
    call cho_main("*Uhm*... [cho_genie_name]...", "horny", "base", "worried", "mid")
    call cho_main("The whole house is celebrating our win at the moment...", "soft", "narrow", "worried", "mid")
    call cho_main("And I'd rather not miss spending some time with-", "horny", "base", "worried", "R")
    g4 "You did well today, [cho_name]."
    call cho_main("", "horny", "base", "base", "mid")
    g9 "Go and party! You've earned it."
    call cho_main("Thank you, [cho_genie_name]... For everything.", "base", "narrow", "base", "mid")
    call cho_main("Have a good night!", "smile", "base", "base", "mid")
    m "You too..."

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    jump end_cho_event


### Quidditch Commentator Quests ###

label cc_ht_hermione_commentator:

    call her_main(xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I mean, I've taken flying lessons... they're mandatory.", "open", "base", "base", "R")
    m "Ah, okay... and here I was hoping that you'd be able to commentate this years quidditch games..."
    call her_main("Me, wasting time on something as stupid as-", "base", "closed", "base", "mid")
    call her_main("Wait...{w=0.3} What did you say?", "open", "squint", "base", "mid")
    m "I was going to ask you if you'd commentate this years quidditch games..."
    call her_main("You want me... to commentate this years wizarding school cup?", "open", "wide", "base", "mid")
    call her_main("I'd be honoured, sir!", "scream", "closed", "base", "mid", trans=hpunch)
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...", "open", "base", "angry", "mid")
    call her_main("Not to mention getting to make all the announcements...", "smile", "base", "base", "R")
    call her_main("The speeches...", "grin", "happy", "base", "mid")

    if her_whoring < 18:
        call her_main("The paper...", "soft", "narrow", "annoyed", "up")
        call her_main("The {heart}{b}preparation{/b}{heart}...", "open_tongue", "narrow", "base", "up")
    else:
        call her_main("Everybody will be focused on me...", "soft", "narrow", "annoyed", "up")

    call her_main("I accept!", "scream", "closed", "angry", "mid", trans=hpunch)
    g4 "I thought you just said you didn't-"
    call her_main("Cho will be so mad!", "crooked_smile", "happy", "base", "mid")
    m "I see..."
    g9 "Congratulations then, [hermione_name]! You got the job."
    call her_main("Ah!!! I better start learning-...{w=0.8} I mean, preparing my opening speech!", "open", "wide", "base", "mid", trans=hpunch)

    call her_walk(action="leave", speed=1.5)

    call bld
    m "Aaaa-nd, she's gone..."
    m "I better tell Cho about the...{w=0.8} news."

    $ hermione_busy = True
    $ cho_quid.commentator = "hermione"
    $ cc_ht.hermione_commentator = True

    jump main_room

### Cho Talk ###

label cc_ht_talk:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if cho_quid.E3_complete and cho_quid.commentator == None:
        call cho_main("Have you asked Hermione to be our commentator yet?", "soft", "base", "base", "mid")
        m "Not yet."
        call cho_main("We can't play if we don't have a commentator.", "soft", "base", "worried", "R")
        call cho_main("Please ask her, Sir.", "annoyed", "base", "worried", "mid")

    elif cho_quid.commentator == "hermione" and cho_quid.lock_practice: # mandatory
        g9 "I've got great news for you! I found us a new commentator!"
        call cho_main("Is it Hermione?", "soft", "narrow", "base", "mid")
        g9 "Yes! Very good guess!"
        call cho_main("It wasn't a guess, [cho_genie_name]. We've discussed her already.", "annoyed", "narrow", "angry", "mid")
        m "Oh, sure..."
        call cho_main("But I'm surprised she even took up the task...", "annoyed", "base", "base", "R")
        g9 "Right away. No questions asked."
        call cho_main("And little miss Granger wasn't even the slightest bit intimidated by her new obligation?", "open", "base", "raised", "mid")
        g9 "Not at all. She seemed rather joyous of her situation."
        call cho_main("Oh...", "annoyed", "base", "worried", "down") # Bit sad.
        call cho_main("Well she just doesn't know what's coming towards her yet!", "annoyed", "narrow", "angry", "mid")
        call cho_main("{size=-4}I hope she gets hit by a bludger as well! I might even tell the boys to aim at her once or twice!{/size}", "angry", "narrow", "angry", "R") # Small text.
        g9 "Make sure you tell everyone your great and very proactive headmaster sorted everything out..."
        call cho_main("Oh, I will. Thank you very much!", "soft", "base", "base", "mid")

        $ cho_quid.lock_training = True # Removes training menu.
        $ hufflepuff_match = "ready" # Able to start main match.
    elif not cc_pf_talk.is_tier_complete(): # Has NOT completed "Talk to me" favour yet.
        # TODO: Posing
        m "Have any ideas on how to beat those huffers?"
        cho "Isn't that your job?"
        m "Oh, yeah..."
        m "(How does she expect me to help her without knowing anything about the opponents?)"
        m "(Maybe I could get her to talk to me and gain more information through favours...)"
    elif cho_whoring < 3: # Has Cho enough confidence?
        # TODO: Posing
        m "So, how about those tactics?"
        cho "I don't know if I can do...{w=0.4} That..."
        m "What do you mean you can't? It's the perfect strategy!"
        cho "But..."
        m "Where's your confidence, your spirit?"
        cho "I'm sorry, [cho_genie_name], forget I said anything..."
        m "(Hmm... She doesn't look very confident to me...)"
        m "(Perhaps I should train her more in private.)"
    else:
        call cho_main("I'm confident that we can win this, [cho_genie_name].", "smile", "base", "base", "mid")

    return
