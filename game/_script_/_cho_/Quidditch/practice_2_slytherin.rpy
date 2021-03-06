

### Cho Intro Slytherin Training ###

label cc_st_intro: # TODO: Move this event to the training into once Slytherin match training has been added. And make it unlock the T2 favours.
    $ cho_quid.slytherin_talk = True

    call play_music("stop")
    call play_sound("door")
    call cho_chibi("stand","mid","base")
    with d3

    call cho_main("Hello, [cho_genie_name]...", "annoyed", "narrow", "worried", "downR", xpos="right", ypos="base")
    m "[cho_name]..."
    m "Where did that high-spirit from your \"big win\" fly off to?"
    call cho_main("Nowhere, [cho_genie_name]...{w=0.6} I'm still very happy we won the game, it's just...", "open", "narrow", "worried", "down") # worried/sad
    call cho_main("I'm a bit worried about the future.", "soft", "narrow", "worried", "mid") # sad/relieved
    m "The future?"
    m "You didn't get pregnant during your little celebration event, did you?"

    call play_music("cho")
    call cho_main("WHAT?!", "clench", "wide", "base", "mid", cheeks="heavy_blush")  # Upset/whatthefuck face
    call cho_main("Sir, why would you even suggest that?!", "angry", "narrow", "angry", "mid", cheeks="blush") # upset
    m "Then what is it?"
    call cho_main("It's about the upcoming quidditch match", "annoyed", "narrow", "angry", "R") # annoyed - eyes R, mouth annoyed
    m "Oh... Of course..."
    call cho_main("[cho_genie_name], I worry that we won't be able to beat Slytherin in the next match.", "annoyed", "narrow", "worried", "mid") # eyebrows sad, eyes mid, mouth pout
    g9 "Slytherin is next?{w=0.6} Sweet!"
    call cho_main("They're an entirely different ballpark compared to Hufflepuff.", "open", "base", "worried", "mid")
    m "Really? Why's that?"
    call cho_main("They're brutal and ruthless!{w} And they think they can get away with anything...", "open", "narrow", "angry", "mid") # eyebrows sad, eyes mid, mouth pout
    m "Then we should do the same, shouldn't we?"
    call cho_main("", "annoyed", "narrow", "base", "mid")
    m "We'll show those Slytherins what {b}we{/b} got -- no problem!"
    call cho_main("...", "base", "base", "base", "mid") # slight smile
    g9 "(And show Snape who's boss.)"
    m "Trust me, our tactics have worked perfectly thus far, haven't they?"
    call cho_main("I-...{w=0.3} yes...", "soft", "base", "raised", "downR")
    call cho_main("You're right! Thank you, [cho_genie_name].", "base", "base", "base", "mid") # happy
    show screen blkfade
    with d5
    hide screen blkfade
    # don't add transition here!

    jump cho_requests


### Cho Slytherin Training ###
label cc_st_start:

    call cho_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # Intro 1
    if cc_st.match_counter == 0:
        m "Alright, we need to try out those new tactics!"
        if cho_quid.bottom in ["skirt_long","skirt_short"] and cho_quid.position == "above":
            call cho_main("New tactics? Aren't we still using the ones from before?", "soft", "narrow", "base", "mid")
            m "Right... Well I'm sure they're good enough to secure a win."
            m "Well, I'm sure they're good enough to secure us another easy win."
            call cho_main("If you say so, [cho_genie_name].", "base", "base", "base", "mid")
        g4 "There is a lot at stake here! We can't afford to lose even a single game!"
        g4 "We can't show any weakness to those Slytherins!"
        call cho_main("Is my success really that important to you, Sir? I'm glad!", "smile", "base", "base", "mid")
        m "(I can't lose this much gold to Snape. I'll show that bastard!)"
        g9 "Return to my office after the game."
        call cho_main("Yes, Sir.", "annoyed", "narrow", "base", "R")

        $ hermione_busy = True
        $ cho_quid.commentator = None # Hermione won't show up.

        pass


    # Intro 2
    elif cc_st.match_counter == 1:
        m "Let's try this again, shall we?"
        m "I spoke with your teacher, she'll get those nitwits to play again..."
        call cho_main("Professor Tonks, wasn't it?", "smile", "base", "base", "mid")
        m "Yep."

        if cho_quid.commentator == "tonks":
            call cho_main("And Professor Tonks will be commentating the match as well?", "soft", "base", "raised", "mid")
            m "That's correct."
            call cho_main("*Hmm*... I have my doubts about her, if I'm honest...", "annoyed", "base", "worried", "R")
            m "Why? Even a donkey would be better suited than Hermione."
            call cho_main("There's some truth in that...", "annoyed", "base", "raised", "down")
            m "Tonks is doing her best to help you. You should at least give her a chance."
            call cho_main("Yes. You're right...", "base", "base", "base", "mid")

        call cho_main("I'm really glad we have her as a teacher.", "base", "base", "base", "down")
        m "Make sure to thank her for it...some day."
        call cho_main("I will, [cho_genie_name].", "smile", "base", "base", "mid")
        call cho_main("Until later...", "base", "base", "base", "mid")
        pass


    # Repeat.
    else:
        m "Ready for your next match, [cho_name]?"
        if cho_quid.commentator == "tonks":
            call cho_main("[cho_genie_name], is Professor Tonks still going to commentate the match?", "soft", "narrow", "worried", "mid")
            m "Yes. Hermione still hasn't changed her mind about it."
            call cho_main("Alright...", "annoyed", "base", "raised", "down")

        else: # Hermione
            call cho_main("Yes, [cho_genie_name].", "base", "base", "angry", "mid")
            call cho_main("I hope all my recent practice will pay off..", "smile", "base", "base", "R")

        call cho_main("I shall be back after the game.", "base", "base", "base", "mid")
        m "Off you go then."
        pass


    # Cho leaves.
    call cho_walk(action="leave")

    $ cho_busy = True
    if cho_quid.commentator == "hermione":
        $ hermione_busy = True
    elif cho_quid.commentator == "tonks":
        $ tonks_busy = True

    $ cho_quid.in_progress = True
    $ cc_st.match_counter += 1 # Stat counter

    jump main_room



label cc_st_return:
    if cc_st.match_counter == 1:
        jump cc_st_return_E1 # Slyth & HG don't attend.

    $ ss_summon_pause = 0 # Can drink with Snape again, now that Slyth plays.

    # First win; can fail.
    if cc_st.win_counter == 0:

        # Win
        if cho_quid.bottom in ["pants_long","pants_short"] and cho_quid.coat == False and cho_quid.position == "front":
            $ cc_st.win_counter = 1
            $ cho_quid.lock_tactic = True
            jump cc_st_return_E2

        # Lose
        else:
            jump cc_st_return_fail

    # Second win; can fail.
    else:

        # Win
        if cho_quid.commentator == "hermione":
            $ cc_st.win_counter = 2
            $ cho_quid.lock_training = True # Removes training menu.
            $ slytherin_match = "ready" # Able to start main match.
            jump cc_st_return_E3

        # Lose
        else:
            jump cc_st_return_fail


label cc_st_return_E1:

    call play_music("stop")
    pause .5

    show screen blktone
    show screen bld1
    with d5
    pause .2

    call play_sound("snore")
    m "...*snore*"
    pause .8
    call play_sound("snore_loud")
    m "...*snooore*"
    pause 1.2
    call play_sound("snore")
    m "...*sno*-{w=0.5}{nw}" # Interrupts

    call play_sound("knocking")
    "*knock knock knock!*"
    pause .2

    hide screen blktone
    hide screen bld1
    with d5
    pause .8

    call bld
    m "Wha-...?"
    call bld("hide")
    pause .5

    # Cho walks in.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    # Cho is furious.
    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid",ypos="base")
    m "..."
    m "What are you doing in here? You're not supposed to be back yet..."
    call cho_main("I'm surprised you could tell...", "soft", "wide", "base", "mid")
    g4 "You just woke me up in the middle of my nap!"
    call cho_main("Oh no, Sir. I'm terribly sorry!", "soft", "base", "raised", "R")

    menu:
        m "..."
        "\"Are you mocking me for taking a nap?\"":
            call cho_main("No, sir.", "soft", "base", "base", "mid")
            m "..."
            g4 "(Damnit, that naivety of hers is turning me on!)"

        "\"Brats like you need to be punished!\"":
            call cho_main("Punished? For what?", "soft", "narrow", "angry", "mid") # angry
            g4 "For being a pain in my ass!"
            call cho_main("", "annoyed", "narrow", "base", "mid")
            g4 "And for waking me up in the middle of my nap!"
            $ cho_mood += 2

    m "Why aren't you on that Quidditch ditch right now?"
    call cho_main("It's a pitch, Sir.", "soft", "narrow", "raised", "mid")
    m "I thought we were going to prepare for the next match, or are we already finished with that?"
    g4 "(Please say yes! I want to do the naughty stuff already!)"
    call cho_main("Yes, we are...", "open", "closed", "base", "mid")
    g9 "(Yes!)"
    call cho_main("For today, that is...", "annoyed", "narrow", "base", "R")
    m "(Balls...)"
    call cho_main("We couldn't play today because the entire Slytherin team didn't even bother to show up!", "annoyed", "narrow", "base", "mid")
    call cho_main("And neither did our commentator!", "soft", "narrow", "base", "mid")
    m "Hermione?"
    call cho_main("Yes! Where the bloody hell was she?!", "angry", "narrow", "angry", "mid", emote="01")
    m "The commentator needs to show up for training too?"
    call cho_main("Yes! And she bloody well needs it.", "soft", "narrow", "base", "down")
    call cho_main("And those braindead Slytherins.", "annoyed", "narrow", "angry", "mid")
    call cho_main("Spineless cowards...", "annoyed", "narrow", "base", "R")
    call cho_main("They have no interest in training against us!", "soft", "base", "base", "mid")
    call cho_main("Because why should they... They'll win anyway!", "angry", "wide", "base", "mid")
    call cho_main("They assured me that they would be there today!", "annoyed", "base", "angry", "R")
    call cho_main("Such a pathetic bunch of apes!", "angry", "base", "angry", "R")
    m "A troop."
    call cho_main("What?", "soft", "narrow", "raised", "mid")
    m "It's called a troop of apes."
    call cho_main("Whatever...", "annoyed", "narrow", "angry", "R")
    call cho_main("If I see their captain tomorrow, I'm gonna knee him in the groin!", "soft", "narrow", "angry", "mid")
    g4 "Yikes!"
    m "I'm afraid I can't have you do that..."
    call cho_main("Why not? They deserve it!", "annoyed", "base", "angry", "mid")
    m "No guy deserves that..."
    m "I'd rather deal with it myself, than let you do that, if you don't mind!"
    call cho_main("Fine...", "annoyed", "base", "base", "down")
    call cho_main("But you better do something, quickly! Get those idiots to play!", "soft", "narrow", "angry", "mid")
    call cho_main("We can't possibly win if we don't know their tactics.", "soft", "base", "base", "R")
    call cho_main("Or know if our tactics work against them, for that matter...", "annoyed", "narrow", "base", "mid")
    m "I'm on it..."
    call cho_main("And what about Granger?", "soft", "narrow", "raised", "mid")
    g4 "*Ugh*... her too?"
    call cho_main("Yes!", "angry", "base", "angry", "mid")
    m "At least let me finish the first quest - before taking on another one..."
    call cho_main("You better get that spineless mop's ass back behind that podium!", "soft", "narrow", "base", "mid")
    call cho_main("She agreed to do this! We need an announcer!", "annoyed", "narrow", "base", "R")
    m "I'll talk to her..."
    call cho_main("Then make it quick!", "annoyed", "narrow", "base", "mid")
    call cho_main("Good night, Sir.", "soft", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "That girl sure is a piece of work..."

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    $ hermione_busy = True
    $ cho_busy = True
    $ cho_mood += 6
    $ cho_quid.lock_practice = True

    $ cc_st.return_E1 = True # Triggers Hermione's return next day.

    jump main_room


label cc_st_return_E2:
    menu:
        "Dev Note" "Return event 2 - Event not yet written."
        "-Got it!-":
            pass

    # TODO: add writing.
    # TODO: lock Cho's quidditch clothing and tactic.
    # They worked good enough so

    # Cho mentions that Tonks might be an issue, and would like to try one more time.

    if cho_quid.commentator == "hermione":
        $ her_mood += 6
        $ hermione_busy = True

        #call cho_main("At the expense of my dignity!","quiver","base","raised","down")
        #m "That's a...{w} yes?"
        #call cho_main("Lee Jordan only used to say that I had a nice butt! But-", "soft", "base", "worried", "down")
        #call cho_main("But, Hermione! Her incompetence as a Quidditch commentator is unmeasurable!","open","base","raised","R")
        #call cho_main("I almost miss Jordan's sexist remarks about my body...","open","closed","base","mid")
        #g9 "I could tell Hermione to do the same if you'd like."
        #call cho_main("Please don't, [cho_genie_name]! I was merely joking!","annoyed","narrow","angry","mid")
    else:
        "Dev Note" "You picked the right clothing combination, but Hermione is not yet a commentator."


    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    if cho_quid.commentator == "tonks":
        $ tonks_busy = True

    $ cho_busy = True

    $ cc_st.return_E2

    jump main_room


label cc_st_return_E3:
    menu:
        "Dev Note" "Return event 3 - Event not yet written."
        "-Got it!-":
            pass

    # TODO: add writing.


    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    if cho_quid.commentator == "hermione":
        $ her_mood += 6
        $ hermione_busy = True
    else:
        "Dev Note" "You picked the right clothing combination, and Hermione is not yet a commentator."
    if cho_quid.commentator == "tonks":
        $ tonks_busy = True

    $ cho_busy = True

    $ cc_st.return_E3

    jump main_room


label cc_st_return_fail:
    menu:
        "Dev Note" "Failed match, add writing."
        "-Got it!-":
            pass
    # TODO: add writing.
#    m "Well, how did it go?"
#    cho "We lost, Sir."
#    elif cho_quid.commentator == "tonks":
#        cho "Could we please get somebody else to commentate the game?"
#        m "Is Miss Tonks not good enough?"
#        cho "No, she's great..."
#        cho "Far better than that half-witt Granger..."
#        m "So what's the issue?"
#        cho "She's not only distracting those Slytherins, but my team as well."

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    if cho_quid.commentator == "hermione":
        $ her_mood += 6
        $ hermione_busy = True
    if cho_quid.commentator == "tonks":
        $ tonks_busy = True

    $ cho_mood += 6
    $ cho_busy = True

    jump main_room



### Quests ###

label cc_st_hermione_E1:

    # Hermione stands at the door.
    call play_sound("door")
    call her_chibi("stand", "door", "base")
    with d3
    pause .5

    call bld
    g4 "..."

    # Hermione barges in.
    call her_walk("desk", "base")

    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base") # annoyed
    pause .5
    call her_main("I can't believe her...", "base", "base", "base", "mid", trans=hpunch) # angry
    m "Good day to you too..."
    her "That bitch has been walking around saying that I quit the commentator job."
    m "Who did?"
    her "Cho Chang!"
    g4 "..."
    m "Wait, so you didn't quit?"
    her "No! How were I supposed to know I needed to show up for Practice?"
    m "(Is she blaming me?)"
    m "Surely there must've been some contract that mentioned it..."
    her "You tell me, you're the one that appointed me."
    m "Oh, right."
    her "So, since I didn't sign anything..."
    her "I quit!"
    g4 "What? You can't do that!"
    her "Why not? After all, I'm terrible at it, aren't I?"
    her "I made such a fool out of myself during the Hufflepuff game..." # Sad, tears
    her "And now with the Slytherin team being next..."
    her "I won't take part of their practice runs just to be laughed at by them..."
    her "I'm not giving those Slytherins that satisfaction!"


    menu:
        m "(...)"
        "Tough luck, Miss Granger!":
            m "You agreed to do this, remember."
            g4 "May I remind you how many house points I gave you?"
            her "No amount of house points was worth the humiliation I got!"
            m "Well, boo- hoo-..."
            her "*Tzzzs!*..."
            her "Good luck finding somebody that is more willing to be the school's laughing stock!"
            $ her_mood += 6

        "We'll look for somebody more competent, then.":
            her "More competent?!"
            m "Surely we can find a replacement for you in no time."
            her "Well if that's the case, it seems like I'm no longer needed..."
            $ her_mood += 2

        "All you need is a bit of practice...":
            if hg_pf_sex.counter == 0:
                g9 "(And a good fucking, but we'll get to that...)"
            else:
                g9 "(And a good fucking...)"
            m "You're a natural at this!"
            her "..."
            her "It doesn't matter..."
            her "Thanks to Cho, everybody now thinks I'm a fraud..."
            her "I don't understand why she feels the need to constantly spread rumours about me."
            m "(Look who's talking...)"

    her "You can tell that bitch to look for somebody else to commentate!"
    her "Because I will not!"
    m "..."
    her "Good day, Sir."

    #Hermione walks out
    call her_walk(action="leave")

    call bld
    g4 "(What in the great desert sands do these women want from me...)"

    $ hermione_busy = True

    $ cc_st.hermione_E1 = True

    jump main_room



### Stage 2 ###

label cc_st_snape_E1:
    # hangout event
    call sna_main("Your precious Ravenclaw bird, made any breakthroughs with her yet?","snape_37", ypos="head")
    m "The little asian?"
    call sna_main("Yes, Miss Chang.","snape_40")
    m "..."
    call sna_main("I wish her best of luck against my team of Slytherins.","snape_02")
    call sna_main("She'll need it.","snape_45")
    g4 "What kind of game are you playing?"
    call sna_main("I'm sorry?","snape_38")
    m "Your team didn't show up to the last practice match!"
    call sna_main("Well, there's no specific rule that forces the teams to practise against each other...","snape_05")
    m "There's not?"
    m "(Actually that does make sense...)"
    call sna_main("Of course not, but it is heavily encouraged for students that are looking to make it professionally.","snape_09")
    m "Do you have something to do with this?"
    call sna_main("I don't know what you're talking about...","snape_47") #Smirk
    g4 "You little weasel..."
    call sna_main("Ha! Do you have another trick up your sleeve?","snape_20")
    call sna_main("What's it gonna be? An even shorter skirt? Prohibit her to wear panties?","snape_13")
    call sna_main("Well, we'll see during the game if it has any effect...","snape_46")
    g4 "*Grrrrr!*..."
    g4 "Get your team back on that pitch, you coward!"
    call sna_main("No...I don't think I will...","snape_41")
    g4 "Give me that wine!"
    call sna_main("You want some?","snape_20")
    call play_sound("spit") # Spits in the cup
    m "I'm gonna win that bet. Then I'll have the last laugh!"
    call sna_main("I wish you good fortune.","snape_22")
    m "..."
    g4 "Get your wine from someplace else, you slacker."
    call sna_main("You won't win by making friends, isn't that right?","snape_18")
    m "..."
    call sna_main("*Hrhm*... Good riddance, then...","snape_12")
    $ renpy.sound.play(["sounds/gulp.mp3"]*3)
    call nar(">Snape empties the last drop of wine, before he quietly leaves.","start")
    ">You feel a sense of remorse shortly after he's gone, realizing that you're both just parts of the same coin."
    call nar(">Your friendship level with him has not changed...{w=1.5}...Probably","end")

    $ snape_busy = True
    $ ss_summon_pause += 5 # Snape can't be summoned for a couple of days. Can be set to 0 once you talked to Tonks.

    $ cc_st.snape_E1 = True

    if daytime:
        jump night_start
    else:
        jump day_start


label cc_st_tonks_E1:
    # Start hangout event.
    m "I wanted to ask you for a favour..."
    call ton_main("Me? Selling a favour to you?","smile","happyCl","base","mid", ypos="head")
    call ton_main("You sure you can afford me?","base","base","raised","mid") #Horny
    m "Not that kind of favour."
    call ton_main("Aww...","upset","base","sad","down")

    # Tell Tonks about Cho.
    m "You know this Quiddish sport the students play here?"
    call ton_main("Quidditch?","upset","base","raised","mid")
    m "Close enough."
    m "The next match is coming up, and I require your help with something."
    call ton_main("Of course. What is it?","base","base","base","mid")
    m "You know this little asian girl?"
    call ton_main("Cho Chang?","open","base","raised","mid")
    m "(Is she like the \"token asian\" of this school?)"
    m "(How is everybody able to guess her name immediately.)"
    m "Yes, the little Ravenclaw minx, correct."
    call ton_main("Well, I figured you'd be talking about her - if it has to do with Quidditch.","open","base","base","R")
    m "She's one of the girls I buy favours from."
    call ton_main("No way!{w=0.8}{nw}","scream","wide","wide","wide", hair="horny")
    call ton_main("You got that little hotty-","open","base","sad","mid")
    call ton_main("*Uhm*... hot-head to sell you favours?","angry","base","sad","R")
    m "Once or twice..."
    call ton_main("I'm impressed.","horny","base","raised","mid")
    call ton_main("Tell me everything!","horny","base","angry","mid")

    menu:
        m "..."
        "Tell her everything":
            pass

        "Don't tell her":
            m "I don't think I should..."
            call ton_main("What? Why not?","open","base","sad","mid")
            m "Miss Chang wouldn't like anybody to know."
            call ton_main("I can keep a secret!","upset","base","worried","R")
            m "I really shouldn't..."
            call ton_main("Tell me, or I'll jinx your balls off!","upset","base","angry","mid", hair="angry")
            g4 "*Ghzzz!* Alright! Alright!"
            m "You sure know how to get me to talk..."

    if cc_pf_strip.points >= 2:
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's past relationships (below conversation.)
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's past relationships (below conversation.)
        m "She's been stripping for me."
        call ton_main("Cho?! And I'm supposed to believe that?","upset","wide","raised","mid")
        g9 "Oh, you better believe it!"
        call ton_main("Holy shit!","upset","wide","wide","wide", hair="horny")
        call ton_main("I'd pay so many galleons to watch that girl take her clothes off...","upset","base","sad","R")
        call ton_main("You need to invite me next time!","angry","base","angry","mid", hair="angry") # angry
        m "And how would I get her to agree to that?"
        call ton_main("Well... *Uhm*...","upset","base","sad","down", hair="horny")
        m "It was difficult enough to get her to strip just for me..."
        m "She only did it because I helped her win against Hufflepuff."
        call ton_main("So that was your idea with the skirt? Very clever.","horny","base","worried","mid")
        m "If you help her against Slytherin..."
        g9 "Maybe I can arrange something with the two of you?"
        call ton_main("Or all three of us!","base","base","angry","mid")
        g9 "I'm sure that minx would love that!"
        call ton_main("I can't wait!","base","happyCl","base","mid")

    else:
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's stripping (above conversation.)

        m "We were mostly just chatting..."
        call ton_main("About what?","open","base","raised","mid")
        m "Her previous school year... couple of relationships she had."
        call ton_main("Intriguing... a couple?","horny","base","base","mid", hair="horny")
        call ton_main("I assume Cedric Diggory was one of them? According to Miss Granger.","open","base","base","L")
        call ton_main("Who else?","base","base","angry","mid")
        m "Some of the other contestants of that tourney..."
        call ton_main("The tri wizards tournament?","open","base","raised","mid")
        call ton_main("That happened last year right? Such a shame I missed it.","upset","base","sad","down")
        #g9 "We should hold our own tournament!"
        #m "The tri-bitcha... Bi-curious-ishar.."
        #m "It's a work in progress title..."
        #m "Anyway..."
        g9 "She said one of them was a girl!"
        call ton_main("Oh my...","upset","base","worried","mid") # Horny
        call ton_main("I didn't know she was...","upset","closed","sad","mid") # Horny
        g9 "They even made out a couple of times!"
        call ton_main("Fuck!","angry","base","sad","ahegao") # Ahegao?
        m "..."
        call ton_main("...","horny","base","base","ahegao")
        m "You alright there?"
        call ton_main("Huh? Oh yes...","open","base","sad","mid")
        call ton_main("My mind was just drifting off for a second...","horny","base","worried","up")
        m "I can imagine why..."


    # Talk about Slytherin.
    m "..."
    m "But to get any further with her, I'll have to help her beat the opposing team in the next match."
    call ton_main("Slytherin? That shouldn't be too difficult.","open","base","raised","mid")
    m "Really? How so?"
    call ton_main("Their tactics revolve around strength, brute force, and manifesting their dominance on the field!","open","closed","angry","mid")
    call ton_main("A good strategy for when you're in bed with your partner, but not in Quidditch.","base","base","angry","mid")
    m "You don't say..."
    g4 "Wait, what?"
    call ton_main("I've seen them play a couple of times. They clearly aren't the brightest bunch...","upset","base","worried","R")
    call ton_main("What tactics are you gonna use against them?","base","base","raised","mid")
    m "I don't know. They refuse to show up for their training matches."
    call ton_main("Well that's unfortunate...","upset","base","sad","L")
    call ton_main("You should ask Snape. Maybe he could get those lazy gits back on the pitch...","open","base","base","mid")

    if cc_st.snape_E1:
        m "I already did. He isn't going to help me out..."
        call ton_main("Well that's just like him.","open","base","angry","R")
    else:
        m "I guess I could..."
        call ton_main("Yeah, maybe not...","open","closed","base","mid")

    call ton_main("Just leave it to me, Genie.","base","base","angry","mid")
    call ton_main("I'll get those shits back on the grass...","angry","base","angry","mid")
    m "(Aren't they playing up in the air?)"
    m "And how will you accomplish that?"
    call ton_main("Oh, don't worry...","smile","happyCl","base","mid")
    call ton_main("I promise I'll tell you all about it some other time.","base","base","angry","mid")

    # You tell Tonks about Hermione.
    m "..."
    if cho_quid.commentator == None:
        m "That's not all, though. There's something else I need your help with."
        call ton_main("You can't expect me to fix all of your problems, Genie.","base","base","base","mid")
        m "It's about Hermione's role as a commentator..."
        call ton_main("Really? What happened to Miss Granger?","upset","base","worried","mid")
        m "She quit..."
        call ton_main("Hmm... that's too bad, it was so cute listening to her fumble over her words...","open","base","sad","R")
        m "Could you convince her to change her mind?"
        call ton_main("I can try. But don't get your hopes up...","upset","base","sad","mid")
        call ton_main("I saw what she had to go through last game.","open","base","sad","mid")
        call ton_main("She's still getting mocked about it, that poor thing...","angry","base","sad","L")
        m "We need her to do it. We don't have anybody else."
        call ton_main("Well...","upset","base","worried","down")
        call ton_main("I could do it.","open","base","sad","mid")
        m "You can? But I thought-"
        call ton_main("You think I'd be biased?","open","base","raised","mid")

    else:
        m "Did you know Hermione wanted to quit her task as a commentator?"
        call ton_main("Did she now? I thought she did well in the Hufflepuff game.","upset","base","raised","mid")
        call ton_main("A bit wooden, but not bad for her first try.","open","base","base","R")
        call ton_main("Speaking in front of such a large crowd and all.","open","base","raised","mid")
        call ton_main("I thought it was rather cute listening to her fumble her words...","base","happyCl","base","mid")
        call ton_main("What changed her mind?","base","base","base","mid")
        m "Cho helped me convince her to do it."
        call ton_main("Really? How?","open","base","raised","mid")
        call ton_main("I'd love to hear it.","horny","base","angry","mid")
        m "*Hmm*... Maybe next time."
        call ton_main("Very well...","upset","base","sad","R")
        call ton_main("I'd make for a great commentator, don't you think?","base","base","base","mid")
        m "I thought teachers weren't allowed to-"
        call ton_main("What? Because as a teacher I'd be biased?","open","base","raised","mid")


    call ton_main("Well, thanks to your efforts, Hufflepuff is already out...","upset","base","angry","R")
    call ton_main("And now the best we can hope for is to not get last...","open","closed","base","mid")
    call ton_main("It's always third or nothing with us Puffs.","open","base","sad","R")
    m "(Puffs?)"

    if cho_quid.commentator == None:
        call ton_main("Anyhow, I shall talk to Miss Granger...","base","base","base","mid")
        call ton_main("Should she still not want to commentate, then I shall fill in for her.","open","base","base","L")
        $ cho_quid.commentator = "tonks"
    else:
        call ton_main("Should Miss Granger change her mind again, I can fill in for her.","base","base","base","mid")
        call ton_main("I'm a great talker, as you probably already know.","smile","happyCl","base","mid")

    g9 "I'm so glad to have you!"
    call ton_main("Aww, you're so sweet!","base","base","sad","mid")
    with hpunch
    $ renpy.play("sounds/hiccup_fem.mp3")
    call ton_main("*Hick!*... whoopsie...","upset","base","base","ahegao")

    if daytime:
        ">You finish your drinks before calling it a day."
    else:
        ">You finish your drinks before calling it a night."

    $ tonks_busy = True
    $ cho_quid.lock_practice = False

    $ cc_st.tonks_E1 = True

    if daytime:
        jump night_start
    else:
        jump day_start


label cc_st_hermione_blackmail:

    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Before Cho stripped in front of Hermione.
    if cc_pf_strip.points < 3:
        m "[hermione_name], may I change your mind about your role in the Slytherin match?"
        her "My answer is still no, [genie_name]."
        g4 "Come on!"
        her "That's my final answer."
        m "..."

        menu:
            "\"I'll give you house points.\"":
                her "Not...{w=0.3}interested."
                g4 "But you're always eager for those points!"
                her "No amount of points would be worth it."
                m "So you don't even want to hear my offer?"
                her "I guess I don't..." # upset
                m "Your loss..."

            "\"You could make fun of those Slytherins.\"":
                if her_tier >= 5:
                    her "That sounds childish, [genie_name]."
                    m "Does it now?"
                    m "So you aren't bothered that they do the same? Calling you all sorts of names?"
                    her "Not in the slightest. They can act like the usual dorks if they want to, that's no concern to me."
                    her "I have no reason to stoop down to their level."
                else:
                    her "And why would I want to do that? I'm not that foolish!"
                    her "Bad-mouthing their entire team would make me an even bigger target than I already am."
                    her "Besides, I wouldn't really be able to mock them with a teacher present."
                    her "Madam Hooch would be unquestionable against that."
                    m "..."

        # Hermione refuses.
        her "I'm sorry [genie_name], but my answer shall remain: No." # annoyed
        g4 "(Dammit! This is such a waste of time!)"
        m "(I might as well continue with Cho's \"Training\" and see if I can come up with some solution to this...)"

        jump hermione_requests


    ### Hermione Blackmail ###

    # After Cho stripped in front of Hermione.
    her "What is it, [genie_name]?"
    m "..."
    g4 "(I'm done playing nice!)"
    her "[genie_name]?"
    m "[hermione_name], you're going to commentate that match. Whether you like it or not."
    her "No. And you won't get me to change my mind on this."
    g9 "Are you sure about that?"
    her "Why?" # suspicious

    menu:
        g9 "[hermione_name]..."
        "\"I heard Cho has a crush on you!\"":
            $ d_flag_01 = True
            her "She has a-... What?"
            pass
        "\"I heard you have a crush on Cho!\"":
            $ d_flag_01 = False
            her "But- That's not true!"
            pass

    her "That's a lie!" # angry
    her "Not even Cho would agree to this!"
    g9 "Why don't we ask her?"
    her "What?"
    her "[genie_name], you can't do this!"
    g9 "Sure I can."

    call nar("> You telepathically call Cho into your office.")

    call hide_characters
    hide screen bld1
    with d3
    pause .2

    # Hermione puts her clothes on if she's naked.
    # TODO: add clothing equip for Hermione.

    call her_walk("mid", "base")
    pause .1

    # Summon Cho.
    call play_sound("door")
    call cho_chibi("stand", "door", "base")
    with d3

    call chibi_emote("thought", "hermione")
    pause 1

    call cho_walk(680, "base")
    pause .2

    call her_main("", "base", "base", "base", "mid", xpos="270", ypos="base", flip=True)
    call cho_main("Hello, Sir.", "base", "base", "base", "mid", xpos="close", ypos="base")
    cho "Granger."
    her "..."
    cho "How can I be of help?"
    m "Miss Granger and I were just discussing about who should commentate the next Squidditch game."
    cho "Oh, did you already blackmail her?"
    her "Blackmailing? Me?!" # chocked
    m "I tried..."
    her "So that's what's going on here. You two are scheming against me!" # angry
    cho "Come on, Hermione. You can't be that scared of those Slytherins. Don't be such a coward..."
    her "I am not!"
    cho "Please! We need somebody to commentate."
    her "I won't do it! And neither of you can change my mind on this!"
    g9 "I bet she can!"
    cho "Me? How so?"

    if d_flag_01: # Cho has crush
        m "Miss Chang, I've heard rumours that you have a huge crush on Hermione..."
        cho "What? That's rubbish!"
        her "..."

    else: # Hermione has crush
        m "Miss Chang, I've heard rumours that Hermione secretly has a crush on you..."
        cho "She does?" # Surprised
        her "No, I don't!"
        her "It's just made up rubbish..."

    g9 "Rubbish or not, I'm sure Miss Granger wouldn't want such rumours to make their rounds now, would she?"
    her "*Pfff*... As if anybody would believe that..."
    cho "Oh, I get it now!"
    cho "You can count on me, Sir!"
    cho "I don't mind if my reputation gets a bit tarnished, from being associated with her."
    cho "For as long as it gets me closer to that cup..."
    her "You're such an idiot, I can't believe it."
    her "I can't believe you'd stoop as low as blackmail for some stupid Quidditch Cup!"

    if d_flag_01: # Cho has crush
        cho "Don't be mean to me, Hermione."
        cho "After all, I really, really like you!"
        her "..." # looks away
        cho "I love your bushy hair, your cute little nose, your gorgeous eyes..."
        cho "Your enormous rack!"
        her "*Tzzzs!*" # Starts to blush
        her "Stop lying!"
        m "She sounds pretty convincing to me..."
        cho "Everybody will know that I have a thing for you, Granger!"
        cho "And, sooner or later, I might even mix in some love potion into your pumpkin juice..."
        her "You'd-... do what?"
        m "(Pumpkin juice? Sounds disgusting.)"
        cho "You wouldn't want all of your friends to see us finally make out, would you?"

    else: # Hermione has crush
        cho "Tell me, Granger..."
        cho "What exactly do you like about me?"
        cho "Is it my hair? Or my strong legs? Or my abs?"
        cho "Would you like me to show you my body again, right now?"
        her "No."
        cho "I should mix in some drops of veritaserum into your pumpkin juice, and ask you again..."
        cho "Maybe then you'll speak the truth... How you really think of me."
        her "You wouldn't!"
        cho "Yes I would!"
        g9 "(I need to get some of that stuff...)"
        m "(The truth potion, not the pumpkin juice... Sounds disgusting...)"
        cho "And I'll make sure that all your friends hear about it. Maybe I'll even let them watch!"

    her "Professor! You can't have her do that. That's insane!"
    m "That's all up to you, Miss Granger."
    g9 "All you gotta do is commentate the next match."
    her "Both matches!"
    m "What?"
    her "The Gryffindor match as well! The one after that, should Ravenclaw even get that far..."
    cho "Oh no you won't! You'd be all in favour of Gryffindor!"
    her "Yes I would. And I'll make sure that you lose."
    m "Great. Finally we can get on with this..."
    m "Miss Granger, you're expected to appear during the practice matches as commentator."
    her "..."
    g9 "Every time you don't, I'll take fifty points from Gryffindor!"
    her "That's just typical of you!"
    m "Make sure to be present..."
    her "..."

    m "You are both dismissed..."
    her "..."

    call her_walk(action="leave")
    pause .2

    if daytime:
        call cho_main("Good day, Sir.", "base", "base", "base", "mid", ypos="head") # Happy
    else:
        call cho_main("Good night, Sir.", "base", "base", "base", "mid", ypos="head") # Happy

    call cho_walk(action="leave")

    call bld
    g9 "Quest complete!"

    $ cho_mood = 0
    $ hermione_busy = True
    $ cho_busy = True

    $ cc_st.hermione_blackmail = True
    $ cho_quid.commentator = "hermione"

    jump main_room



### Stage 3 ###

label cc_st_talk:

    call cho_main(xpos="mid", ypos="base", trans=fade)

    # you haven't talked to Tonks yet.
    if cho_quid.lock_practice:
        call cho_main("Have you gotten those Slytherin pigs to play yet?","open","narrow","base","mid")
        m "Not yet, but I'm on it."
        call cho_main("Please just hurry up, Sir.","annoyed","narrow","base","mid")
        call cho_main("We need to practise...", "annoyed", "narrow", "worried", "R")
        m "Any ideas on how I would do that?"
        call cho_main("How would I know, I'm not a teacher am I... ask one of them.", "annoyed","base","angry","R")
        if cc_st.snape_E1:
            m "Well, I asked Snape..."
            call cho_main("And how did that work out for you?","open","base","base","mid")
            m "It didn't."
            call cho_main("Ask another teacher then...", "angry","base","angry","mid")

    # played one match with Tonks.
    elif cc_st.match_counter >= 2 and cho_quid.commentator == "tonks" and cc_pf_strip.points < 3 and not cc_st.hermione_blackmail:
        call cho_main("So, what is Granger up to?","soft","base","base","mid")
        call cho_main("Is she still too frightened to face those jolly Slytherins?","open","base","base","R")
        m "Well, we have Tonks to do that now..."
        call cho_main("But Tonks isn't even on our side! This won't help!","angry","base","angry","mid")
        m "And Hermione is?"
        call cho_main("At least Granger is biased, and doesn't befuddle my own team as well as theirs!","annoyed","narrow","angry","R")
        m "Befuddle?"
        call cho_main("Professor Tonks won't stop flirting with the boys on my team!","angry","closed","angry","mid")
        call cho_main("Those stupid idiots can barely sit on their brooms because of her...","annoyed","narrow","angry","mid")
        m "Why? Is the wood too hard?"
        m "(When do those people realise that carpets are more comfortable...)"
        call cho_main("We need to get that Gryffindor skunk to peeve those Slytherins, so we can get past them!","annoyed","base","angry","mid")

    # after strip and before blackmailing Hermione.
    elif cho_quid.commentator == "tonks" and cc_pf_strip.points >= 3 and not cc_st.hermione_blackmail:
        m "Would you be willing to help me change Hermione's mind?"
        call cho_main("Of course? And How?","base","base","base","mid")
        m "With-"
        call cho_main("With blackmail?","smile","narrow","angry","mid") # excited
        m "...No."
        m "Why don't you try to just ask her politely?"
        call cho_main("Bull-{w=0.3}shit! That's never going to work.","angry","base","angry","mid")
        call cho_main("We already have dirt on her. Why don't we just blackmail her again!","annoyed","narrow","angry","mid")
        m "Like when you forced her to watch your little strip-show?"
        call cho_main("That was fun wasn't it?","smile","narrow","angry","mid")
        g9 "Shit yeah, it was!"
        m "We might have to employ such tactics after all, if we want to win."
        m "Feeling any sense of remorse is pointless in a game such as this..."
        call cho_main("You're absolutely correct, Sir!","open","closed","base","mid")
        call cho_main("Quidditch is a selfish, relentless game of committing all sorts of atrocities and dishonest acts!","angry","narrow","angry","mid")
        m "I wasn't talking about Quidditch..."

    # response when there is no new task for you.
    else:
        call cho_main("I'm confident that we can win this, [cho_genie_name].","smile","base","base","mid")
        call cho_main("Slythein has no blasted chance against us!","base","narrow","base","mid")

    call cho_main(xpos="base", ypos="base", trans=fade)

    return
