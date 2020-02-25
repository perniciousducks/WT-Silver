

# Started first training match against Hufflepuff

label cc_ht_start:

    call cho_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # First Hufflepuff match.
    if cc_ht.win_counter < 2:

        # Intro
        if cc_ht.match_counter == 0:
            m "So, when will those Quidditch matches take place?"
            call cho_main("We could arrange one for today. Just for practice, against Hufflepuff.", "open", "base", "base", "R")
            m "Really? Just like that?"
            call cho_main("Why yes. The Hufflepuff team wouldn't take up a chance to play against us for training.", "soft", "base", "raised", "mid")
            call cho_main("They'd welcome every opportunity to test us and study our tactics...", "open", "narrow", "angry", "mid")
            call cho_main("All I need to do is give their team captain a heads up during classes.", "base", "base", "base", "mid")
            m "Great. Get your team ready cause you are going to play today."
            call cho_main("I will, [cho_genie_name]. Wish me luck.", "smile", "base", "base", "mid")

        # Repeated
        else:
            m "Time for another practice match don't you think?"
            call cho_main("I'll try my best, [cho_genie_name].", "base", "base", "base", "mid")
            m "Good luck out there."
            call cho_main("Thank you, Sir.", face="happy")
            call cho_main("I better get going. See you later, [cho_genie_name]!", "soft", "base", "raised", "mid")


    # Second Hufflepuff match.
    else:
        m "Ready to kick some badger ass again?"
        call cho_main("Absolutely!", "smile", "narrow", "angry", "mid")
        call cho_main("If we beat them twice, we might have a chance against them in the tourney!", "base", "narrow", "angry", "mid")
        m "That's the spirit! Now go get them tiger!"
        call cho_main("Later, [cho_genie_name]!", face="happy")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho_busy = True
    if cho_quid.commentator == "hermione": # Hermione has to commentate.
        $ hermione_busy = True

    $ cc_ht.match_counter += 1 # Stat counter
    $ cho_quid.in_progress = True

    jump main_room


# Check if Cho won or lost the practice game.
label quidditch_match_return:
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


    # Hufflepuff Match

    # First win, can fail.
    if cc_ht.win_counter == 0:

        # Win (According to Genie; she still lost.)
        if cho_quid.bottom in ["skirt_long", "skirt_short"] and cho_quid.position == "above":
            $ cc_ht.win_counter = 1
            $ cho_quid.lock_tactic = True
            jump cc_ht_return_E1

        # Lose
        else:
            jump cc_ht_return_fail

    # Second win.
    elif cc_ht.win_counter == 1:

        # Win
        if cho_whoring >= 3:
            $ cc_ht.win_counter = 2
            jump cc_ht_return_E2

        # Lose
        else:
            jump cc_ht_return_fail

    # Commentator event.
    else:
        $ cho_quid.lock_practice = True
        jump cc_ht_return_E3


# Lost first hufflepuff match.
label cc_ht_return_fail:

    call cho_main("...", mouth="upset", face="neutral", xpos="mid", ypos="base")
    m "So, how did it go?"
    call cho_main("We lost... again...", mouth="soft", eyebrows="worried", face="neutral")
    m "What was the problem?"

    # Position response.
    if cho_quid.position != "above":
        call cho_main("Our tactic didn't work, [cho_genie_name].", "annoyed", "narrow", "worried", "mid")
        call cho_main("Cedric just ignored me for most of the game, and ended up catching the snitch...", "soft", "narrow", "worried", "R")
        m "Were you trying to distract him enough?"

        if cho_quid.bottom in ["skirt_long", "skirt_short"]:
            call cho_main("Of course I was!", "open", "narrow", "angry", "mid")
            call cho_main("I tried to let him have a peek up my skirt, but I'm not sure he even noticed that I was wearing one.", "soft", "narrow", "angry", "mid")
            m "Interesting..."
            m "Maybe we need to tackle this situation from another angle."
            m "And change our flying tactics to best show it off..."
        else:
            call cho_main("I did! To the best of my ability...", "soft", "narrow", "angry", "R")
            call cho_main("Maybe he doesn't like the outfit I'm wearing?", "soft", "narrow", "base", "mid")
            m "Yes that might be it."
            m "We'll discuss your outfit next time..."
            m "And change our flying tactics to best show it off..."

        call cho_main("Whatever you say, [cho_genie_name].", "annoyed", "narrow", "angry", "R")
        call cho_main("I'll be going to bed now if you don't mind.", "soft", "narrow", "angry", "mid")
        call cho_main("Have a good night, Sir.", "annoyed", "narrow", "base", "mid")

    # Whoring level response (for return_3)
    elif cho_quid.lock_tactic and cho_whoring < 3:
        call cho_main("The same as before, Sir.", "soft", "narrow", "angry", "mid")
        call cho_main("You can't expect me to wear a skirt - and do a good performance at the same time!", "soft", "narrow", "base", "R")
        m "We just have to get you to be more confident on your broom, that's all."
        g9 "And increase your performance that way."
        call cho_main("(...)", "annoyed", "narrow", "base", "R")
        call cho_main("I'll be going to bed now if you don't mind.", "soft", "narrow", "angry", "mid")
        call cho_main("Have a good night, Sir.", "annoyed", "narrow", "base", "mid")
        if cheats_active:
            call nar("{size=+6}> Try again at recklesness level {color=#7a0000}3{/color}.{/size}")


    # Outfit response.
    else:
        call cho_main("Cedric didn't seem too distracted by me... He ended up catching the snitch and...", "open", "narrow", "base", "R")
        call cho_main("I'm not sure what the problem was...", "annoyed", "narrow", "worried", "mid")
        m "Maybe it's your attire. It's not really suited for this..."
        call cho_main("But it's the school's official Quidditch clothing!", "annoyed", "narrow", "base", "mid")
        m "We'll try a different outfit next time."
        call cho_main("If you say so...", "soft", "narrow", "worried", "down")
        call cho_main("I should head back to our dorms and get some sleep...", "annoyed", "narrow", "worried", "mid")
        m "Sure. You may leave..."
        call cho_main("Have a good night, Sir.", "soft", "base", "base", "R")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    if cc_ht.win_counter == 0:
        $ cho_mood += 5
    else:
        $ cho_mood += 8

    $ cho_busy = True

    jump main_room


label cc_ht_return_E1:

    call cho_main("(...)", "annoyed", "narrow", "angry", "R", xpos="mid", ypos="base")
    m "Well, how did it go?"
    call cho_main("I couldn't focus on the game!", "angry", "closed", "angry", "mid")
    call cho_main("This ridiculously short skirt! The whole match it kept on slipping over my bum!", "soft", "narrow", "angry", "mid")
    m "So what? Just ignore it..."
    call cho_main("And let everybody ogle at my bare ass?", "open", "narrow", "angry", "mid")
    m "Aren't you still wearing panties?"
    call cho_main("Of course I am! And I don't intend to show them to the whole school!", "annoyed", "narrow", "angry", "mid")
    call cho_main("I'm only going to let Cedric have a peek...", "soft", "narrow", "angry", "R")
    g4 "But \"Just a peek\" won't do, [cho_name]!"
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    m "How successful would you say were our tactics?"
    m "Was he following the \"Snitch\" or the \"Snatch?\""
    call cho_main("The what?!", "angry", "wide", "base", "mid")
    m "Was he hooked on your outfit?"
    call cho_main("I *uhm*... I'd say so.", "soft", "base", "base", "R")
    call cho_main("He was following me most of the time.", "annoyed", "base", "base", "mid")
    m "Splendid!"
    g9 "I love it when a plan comes together!"
    call cho_main("But...we lost?", "annoyed", "base", "worried", "mid")
    g9 "I see this as an absolute win!"
    call cho_main("", "annoyed", "narrow", "base", "mid")
    m "We'll stick with those tactics, but I expect you to do better next time."
    g4 "If the entire school knows the colour of your panties, that's when you have done your task well!"

    if cho_whoring < 3:
        call cho_main("You are asking too much of me, [cho_genie_name]! I'd never be able to do such a thing...", "annoyed", "narrow", "worried", "down")
        m "Clearly you just aren't ready yet. We'll get you to be more confident on your broom soon enough..."
        g9 "With your panties on display!"
        call cho_main("*Phmpf*...", "annoyed", "narrow", "base", "R")
    else:
        call cho_main("You better be right about this, Sir.", "annoyed", "narrow", "base", "mid")

    call cho_main("It's getting late...", "soft", "narrow", "base", "mid")
    call cho_main("If you don't mind I'd like to go to bed now.", "open", "base", "angry", "mid")
    m "Sure. You may leave..."
    call cho_main("Have a good night, Sir.", "soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(...)"

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    $ cho_busy = True

    $ cc_ht.return_E1 = True

    jump main_room


label cc_ht_return_E2:

    call cho_main("(...)", "annoyed", "narrow", "angry", "R", xpos="mid", ypos="base")
    m "You seem a little on edge..."
    call cho_main("On edge?", "scream", "wide", "angry", "mid")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!", "angry", "wide", "angry", "mid")
    call cho_main("You had to have me do this on the day half of hufflepuff shows up to watch us practise, didn't you!", "annoyed", "narrow", "angry", "R")
    call cho_main("I bet you were probably in on it...", "upset", "narrow", "angry", "mid")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    call play_music("cho")
    call cho_main("{size=+10}I got it!!!{/size}", "scream", "base", "base", "mid")
    call cho_main("I caught the snitch!", "smile", "closed", "base", "mid")
    m "Congratulations..."
    call cho_main("That blockhead Cedric didn't stand a chance against me!", "open", "base", "worried", "R")
    call cho_main("Usually I'm never fast enough to beat him with my crummy old nimbus...", "pout", "narrow", "angry", "downR")
    call cho_main("But today, I flew above him as we were both racing after the snitch, just like you said I should.", "smile", "base", "base", "mid")
    g9 "Sounds like somebody should get a reward for their efforts!"
    call cho_main("I can't believe I was able to finally catch it!", "smile", "closed", "base", "mid")
    m "Is this the first time you've caught one?"
    call cho_main("*Mhmm*... This is the first game of quidditch Ravenclaw has won in over six years!", "smile", "base", "base", "mid")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices, [cho_genie_name]...", "annoyed", "narrow", "worried", "downR")
    m "oh..."
    call cho_main("Ravenclaw...{w} isn't very good...", "annoyed", "narrow", "worried", "down")
    call cho_main("But I have a feeling that's going to change this year!", "smile", "closed", "base", "mid")
    g9 "And I am happy to be of help!"
    call cho_main("Yes, [cho_genie_name]! Thank you so much!", "horny", "narrow", "base", "down")
    call cho_main("If there is any way I can return the favour...?", "horny", "base", "raised", "mid")
    m "Yes, but we should discuss that after you've won the game."
    m "Then you can do some more advanced favours for me."
    call cho_main("More advanced...favours?", "soft", "narrow", "worried", "mid")
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

    $ cho_busy = True

    $ cc_ht.return_E2 = True

    jump main_room


### Quidditch Commentator Quests ###

label cc_ht_return_E3:

    call play_music("stop")
    call cho_main("[cho_genie_name], there's been a disaster!", "scream", "closed", "angry", "mid", xpos="mid", ypos="base")
    call play_music("night")
    m "Off to a good start..."
    call cho_main("[cho_genie_name], something terrible happened to Lee Jordan!", "quiver", "narrow", "worried", "mid")
    m "Lee Jordan?{w=0.5} Is that a famous basketball player I'm not aware of?"
    call cho_main("What?{w=0.5} No Sir, Lee is our quidditch commentator!", "soft", "narrow", "base", "mid")
    call cho_main("He got hit in the throat by a bludger!", "quiver", "base", "raised", "down")
    call cho_main("Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season.", "soft", "closed", "worried", "mid")
    call cho_main("What are we going to do! We can't have a \"W.S.C.\" without a commentator!", "soft", "base", "worried", "mid")
    m "Can't you play without one?"
    call cho_main("No. Someone has to announce the points after all.", "annoyed", "narrow", "base", "mid")
    m "I see..."

    label who_shall_commentate:
    menu:
        m "How about we ask..."
        "\"Hermione\"":
            pass
        "\"Astoria\"" if astoria_unlocked:
            call cho_main("That brat?", "scream", "wide", "raised", "mid")
            call cho_main("Not a chance!", "open", "closed", "angry", "mid")
            call cho_main("Besides, [cho_genie_name], did you forget that she's a slytherin?", "open", "narrow", "angry", "mid")
            m "Right. No slytherins. Got it."
            m "How about..."
            jump who_shall_commentate
        "\"Luna\"" if luna_unlocked:
            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?", "open", "narrow", "raised", "mid")
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...", "open", "closed", "raised", "mid")
            call cho_main("Trust me, [cho_genie_name], Luna would be a terrible choice!", "soft", "narrow", "angry", "mid")
            m "Fine. How about..."
            jump who_shall_commentate

    call cho_main("Hermione Granger?", "scream", "wide", "raised", "mid")
    call cho_main("She wouldn't know the first thing about quidditch!", "open", "narrow", "angry", "mid")
    call cho_main("You can't pick her!", "upset", "closed", "raised", "mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    call cho_main("Absolutely not! I won't talk to that Gryffindor skunk ever again!", "scream", "closed", "angry", "mid")
    call cho_main("Didn't I make it clear that I don't want her to \"ever\" be involved in Quidditch again?", "annoyed", "narrow", "angry", "mid")
    m "Alright, are there any other students who know Quidditch rules well enough to take this... Jordan boy's place?"
    call cho_main("...", "annoyed", "base", "base", "down")
    m "Well?"
    call cho_main("Well, most of them would be on one of the Quidditch teams...", "soft", "base", "raised", "R")
    call cho_main("But Granger wouldn't know anything about Quidditch either!", "annoyed", "narrow", "angry", "mid")
    m "Do you know anybody else suited for the job?"
    call cho_main("{size=-4}Probably anyone at this point...{/size}", "annoyed", "base", "raised", "R")
    call play_music("stop")
    call cho_main("(Wait a minute...)", "annoyed", "wide", "raised", "mid")
    call play_music("cho")
    call cho_main("No...", "smile", "base", "base", "mid") #Mischievous smile
    g9 "I'll ask her... What's the worst that could happen..."
    call cho_main("Yeah, actually you're probably right...", "angry", "narrow", "angry", "mid")
    m "Don't worry she'll do a-{w=1.0}{nw}"
    g4 "Wait... what did you say?"
    call cho_main("I'm sure she'll do a heckin' good job!", "smile", "narrow", "angry", "mid")
    call cho_main("(She'll flub the whole thing and everyone will laugh at her.)", "smile", "narrow", "angry", "R") #Mischievous smile
    g9 "Well, great then. I'll ask her in that case!"
    call cho_main("(She'll be humiliated and no one will ever see her as anything but a showoff that knows nothing!)", "quiver", "narrow", "angry", "down")
    call cho_main("(I can already picture it...{w=0.8} the whole school laughing...)", "quiver", "base", "raised", "up")
    m "Miss Chang?"
    call cho_main("Oh, thank you for handling it professor! Boy, you took a load off my mind...", "open", "base", "base", "mid",trans=hpunch)
    call cho_main("I'll be heading back to bed, if you don't mind.", "soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(...)"

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    $ cho_busy = True

    $ cc_ht.return_E3 = True

    jump main_room


label cc_ht_hermione_commentator:

    call her_main(xpos="mid", ypos="base",trans=fade)
    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I mean, I've taken flying lessons... they're mandatory.", "open", "base", "base", "R")
    m "Ah, okay... and here I was hoping that you'd be able to commentate this years quidditch games..."
    call her_main("Me, wasting time on something as stu...{w=0.8}{nw}", "base", "closed", "base", "mid")
    call her_main("Wait...{w=0.6} What did you say?", "open", "squint", "base", "mid")
    m "I was going to ask you if you'd commentate this years quidditch games..."
    call her_main("You want me... to commentate this years wizarding school cup?", "open", "wide", "base", "mid")
    call her_main("I'd be honoured, sir!", "scream", "closed", "base", "mid",trans=hpunch)
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...", "open", "base", "angry", "mid")
    call her_main("Not to mention getting to make all the announcements...", "smile", "base", "base", "R")
    call her_main("The speeches...", "grin", "happy", "base", "mid")

    if her_whoring < 18:
        call her_main("The paper...", "soft", "narrow", "annoyed", "up")
        call her_main("The {heart}{i}preparation{/i}{heart}...", "open_tongue", "narrow", "base", "up")
    else:
        call her_main("Everybody will be focused on me...", "soft", "narrow", "annoyed", "up")

    call her_main("I accept!", "scream", "closed", "angry", "mid",trans=hpunch)
    g4 "I thought you just said you didn't..."
    call her_main("Cho will be so mad!", "crooked_smile", "happy", "base", "mid")
    m "I see..."
    g9 "Congratulations then, [hermione_name]! You got the j..."
    call her_main("Ah!!! I better start lear...{w=0.8} I mean, preparing my opening speech!", "open", "wide", "base", "mid",trans=hpunch)

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

    call cho_main(xpos="mid", ypos="base", trans=fade)

    if cc_ht.return_E3 and cho_quid.commentator == None:
        call cho_main("Have you asked Hermione to be our commentator yet?", "soft", "base", "base", "mid")
        m "Not yet."
        call cho_main("We can't play if we don't have a commentator.", "soft", "base", "worried", "R")
        call cho_main("Please ask her, Sir.", "annoyed", "base", "worried", "mid")

    elif cho_quid.commentator == "hermione" and cho_quid.lock_practice: # mandatory
        g9 "I've got great news for you! I found us a new commentator!"
        call cho_main("Is it Hermione?", "soft", "closed", "base", "mid")
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

    elif cho_quid.lock_tactic and cho_whoring < 3: # Won once. Confidence not high enough.
        call cho_main("Do I really have to wear the skirt for the game?", "open", "base", "worried", "mid")
        call cho_main("Everyone can see right under it.", "soft", "base", "worried", "down")
        m "You say that like it's a bad thing..."
        call cho_main("Because it is!", "angry", "narrow", "angry", "mid")
        call cho_main("I'm not some harlot that likes to give everyone a glimps of her panties.", "open", "narrow", "angry", "R")
        m "You aren't yet..."
        call cho_main("What do you mean, Sir?", "annoyed", "narrow", "angry", "mid")

    else:
        call cho_main("I'm confident that we can win this, [cho_genie_name].", "smile", "base", "base", "mid")

    call cho_main(xpos="base", ypos="base", trans=fade)

    return
