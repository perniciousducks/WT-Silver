# cc_st_intro  automatically plays when starting slytherin tier

# cc_st_start unlocks once you've convinced Cho to use tactics against slytherin (Will need some work as I don't know the code)
# cc_st_return_E1 Is the return event as Slytherin wont practice, practice locks after this event as Slytherins doesn't show up
#To play practice again you need to talk to Tonks to convince them to play again cc_st_tonks_E1 (cc_st_snape_E1 is optional until you talk to tonks)
# Hermione shows up next day after this event saying that she wont play cc_st_hermione_E1 once she leaves it unlocks the ability to blackmail her cc_st_hermione_blackmail

# cc_st_return_E2 Is the return event when Cho has practiced against Slytherins. Once this event finished one of two requirements to start the main match is completed (other being blackmail Hermione)
#cc_st_hermione_blackmail is one of two requirements to play the main match (other being cc_st_return_E2)


### Cho Slytherin Training ###
label cc_st_start:

    call cho_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # Intro 1
    if not cho_quid.slytherin_prepared:
        m "Alright, we need to try out those new tactics!"
        g4 "There is a lot at stake here! We can't afford to lose even a single game!"
        g4 "We can't show any weakness to those Slytherins!"
        call cho_main("I'm glad my success is that important to you, Sir.", "smile", "happyCl", "base", "mid", cheeks="blush")

        show screen blktone
        with d3
        m "(I can't lose this much gold to Snape. I'll show that bastard!)"
        hide screen blktone
        with d3

        g9 "Return to my office after the game."
        call cho_main("Yes, Sir.", "base", "narrow", "base", "mid")

    # Intro 2 (For successful match against Slytherins) (playing is one of two needed requirements for match to unlock alongside with Blackmailing Hermione)
    else:
        m "Let's try this again, shall we?"
        m "I spoke with your teacher, she'll get those nitwits to play again..."
        call cho_main("Professor Tonks, was it?", "smile", "base", "base", "mid")
        m "Yep."
        call cho_main("I'm really glad we have her as a teacher.", "base", "happyCl", "base", "mid", cheeks="blush")
        m "Make sure to thank her for it... some day."
        call cho_main("I will, [cho_genie_name].", "smile", "base", "base", "mid")
        call cho_main("Off I go then...", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho_busy = True
    $ hermione_busy = True

    $ cho_quid.in_progress = True

    jump main_room


label cc_st_return:
    if not cho_quid.slytherin_prepared:
        # Cho goes unprepared and fails.

        stop music fadeout 5.0

        call play_sound("snore")
        m "...*snore*{w=1.0}{nw}"
        pause .8
        call play_sound("snore_loud")
        m "...{cps=10}*snooore*{/cps}{w=1.0}{nw}"
        pause 1.2
        call play_sound("snore")
        m "...*sno*-{w=0.5}{nw}" # Interrupts

        call play_sound("knocking")
        "*knock knock knock!*"
        pause .2

        m "Wha-...?"

        call cho_walk(action="enter", xpos="desk", ypos="base")

        # Cho is furious.
        call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid",ypos="base", trans=d3)
        m "..."
        m "What are you doing in here? You're not supposed to be back yet..."
        call cho_main("I'm surprised you could tell...", "soft", "wide", "base", "mid")
        g4 "You just woke me up in the middle of my nap!"
        call cho_main("Oh no, Sir. I'm terribly sorry!", "soft", "base", "raised", "R")

        menu:
            m "..."
            "\"Are you mocking me for taking a nap?\"":
                call play_music("cho")

                call cho_main("No, sir.", "soft", "base", "base", "mid")
                m "..."
                g4 "(Damn it, that naivety of hers is turning me on!)"

            "\"Brats like you need to be punished!\"":
                $ cho_mood += 2
                call play_music("cho")

                call cho_main("Punished? For what?", "soft", "narrow", "angry", "mid") # angry
                g4 "For being a pain in my ass!"
                call cho_main("", "annoyed", "narrow", "base", "mid")
                g4 "And for waking me up in the middle of my nap!"

        m "Why aren't you on that Quidditch ditch right now?"
        call cho_main("It's a pitch, Sir.", "soft", "narrow", "raised", "mid")
        m "I thought we were going to prepare for the next match, or are we already finished with that?"

        show screen blktone
        with d3
        g4 "(Please say yes! I want to do the naughty stuff already!)"
        hide screen blktone
        with d3

        call cho_main("Yes, we are...", "open", "closed", "base", "mid")
        g9 "(Yes!)"
        call cho_main("For today, that is...", "annoyed", "narrow", "base", "R")
        m "(Balls...)"
        call cho_main("We couldn't play today because the entire Slytherin team didn't even bother to show up!", "annoyed", "narrow", "base", "mid")
        call cho_main("Spineless cowards...", "annoyed", "narrow", "angry", "downR")
        call cho_main("They have no interest in training against us!", "open", "narrow", "angry", "mid")
        call cho_main("Because why should they... They'll win anyway!", "open", "narrow", "angry", "R")
        call cho_main("They assured me that they would be there today...", "annoyed", "narrow", "angry", "downR")
        call cho_main("Such a pathetic bunch of apes!", "annoyed", "narrow", "angry", "R")
        m "A troop."
        call cho_main("What?", "soft", "narrow", "raised", "mid")
        m "It's called a troop of apes."
        call cho_main("Whatever...", "annoyed", "narrow", "angry", "R")
        call cho_main("If I see their captain tomorrow, I'm gonna knee him in the groin!", "soft", "narrow", "angry", "mid")
        g4 "Yikes!"
        m "I'm afraid I can't have you do that..."
        call cho_main("Why not? They deserve it!", "annoyed", "base", "angry", "mid")
        m "No guy deserves that..."
        m "I'd rather deal with it myself, if you don't mind."
        call cho_main("Fine...", "annoyed", "narrow", "angry", "downR")
        call cho_main("But you better do something, quickly! Get those idiots to play!", "soft", "narrow", "angry", "mid")
        call cho_main("We can't possibly win if we don't know their tactics.", "soft", "base", "base", "R")
        call cho_main("Or know if our tactics work against them, for that matter...", "annoyed", "narrow", "base", "mid")
        m "I'm on it..."
        call cho_main("And that's not all... I heard some people saying that Hermione won't commentate anymore!", "angry", "narrow", "angry", "mid", emote="01")
        g4 "What?"
        call cho_main("I know, you better do something about it!", "open", "narrow", "angry", "mid")
        g4 "*Ugh*... Do I have to?"
        call cho_main("Yes!", "angry", "base", "angry", "mid")
        call cho_main("Get that spineless mop's ass back behind that podium!", "soft", "narrow", "base", "mid")
        m "{size=-6}At least let me finish the first quest -- before taking on another one...{/size}"
        call cho_main("She agreed to do this! We need an announcer!", "annoyed", "narrow", "base", "R")
        m "I'll talk to her..."
        call cho_main("Then make it quick!", "annoyed", "narrow", "base", "mid")
        call cho_main("Good night, Sir.", "soft", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        m "That girl sure is a piece of work..."

        $ cho.equip(cho_outfit_last) # Equip last worn clothes

        $ hermione_busy = True
        $ cho_mood += 6
        $ cho_quid.lock_practice = True

        jump end_cho_event
    else:
        # Cho has been prepared and trained.

        #Cho enters
        m "Welcome back..."
        cho "..." #Annoyed
        m "Don't tell me they didn't show up again... Tonks assured me she'd get them to-"
        cho "No they did show up alright."
        g9 "Excellent!"
        m "Then what about our strategy, do you think it will work during the game?"
        cho "I can't believe I flaunted my ass at them... but yes, I believe it will work."
        cho "Crabbe and Goyle especially should be a great help, turning the game to my favour."
        cho "I'm sure not even malfoy would be able to get them to behave at that point."
        cho "So long as they don't give my ass too much of a bludgering..."
        m "Just make sure to pick the right moment to distract them and I'm sure you'll be fine."
        m "Very well then, I guess we're ready to take those snakes on for the main match!"
        if cc_st.hermione_blackmail == False: #Is this right?
            cho "What about Granger?"
            m "What about her?"
            cho "Is she commentating or what? We can't play without a commentator."
            m "Oh, that's true... I'll talk to her..."
            cho "Good."
        else:
            cho "I suppose..." #
        m "Well then, the match looms ever so closer... I hope you're ready."
        cho "You bet your ass I am!"
        m "..."
        cho "Don't even say it..."
        m "I... wasn't-"
        cho "Sure you weren't..."
        cho "I'll head off to bed then."
        m "*MHHMMMM*" #Big text
        # Cho leaves
        m "*NNNNGH!!!*"
        m "You'll be betting your ass on it!" #Big text
        cho "I heard that!"#Cho outside door (small text)
        m "Damnit..."

        #Match requirement practice game finished (still need to blackmail Hermione if not already done)

### Stage 3 ###

label cc_st_talk:

    call cho_main(xpos="right", ypos="base", trans=fade)

    # you haven't talked to Tonks yet.
    if cho_quid.lock_practice:
        call cho_main("Have you gotten those Slytherin pigs to play yet?","open","narrow","base","mid")
        m "Not yet, but I'm on it."
        call cho_main("Please just hurry up, Sir.","annoyed","narrow","base","mid")
        call cho_main("We need to try out those tactics...", "annoyed", "narrow", "worried", "R")
        m "Any ideas on how to get them to practice against you?"
        call cho_main("How would I know, I'm not a teacher, am I?...{w} Ask one of them.", "open","narrow","base","mid")
        if cc_st.snape_E1:
            m "Well, I asked Snape..."
            call cho_main("And how did that work out for you?","open","narrow","raised","mid")
            m "It didn't."
            call cho_main("Ask another teacher then...", "annoyed","narrow","base","mid")
    elif cc_st.hermione_blackmail == False: #TODO Is this correct? I added this section #TODO expressions
        cho "Will Hermione commentate the match or not?"
        m "Probably..."
        cho "What do you mean probably?"
        m "I haven't confronted her about it yet."
        cho "Then do it!"

    # response when there is no new task for you.
    else:
        call cho_main("I'm confident that we can win this, [cho_genie_name].","smile","base","base","mid")
        call cho_main("Slythein has no blasted chance against us!","base","narrow","base","mid")

    #call cho_main(xpos="base", ypos="base", trans=fade)

    return
