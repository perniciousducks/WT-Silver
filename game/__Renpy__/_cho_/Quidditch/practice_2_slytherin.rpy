

### Stage 1 ###
# cc_st_start (Done)
# cc_st_return_E1 (Done)
# cc_st_hermione_E1 (Done)
## lock training ##

### Stage 2 ###
# cc_st_snape_E1 (Done)
# cc_st_tonks_E1 (Done)
## unlock training ##
# cc_st_return_E2

### Stage 3 ###
## Blackmail Hermione ##
# cc_st_talk (Done)
# cc_st_hermione_blackmail (Done)
# cc_st_tonks_E2
# cc_st_return_E3

label cc_st_start:

    call cho_main("","base","base","base","mid", xpos="right", ypos="base", trans="fade")

    # Intro
    if cc_st.match_counter == 0:
        m "Alright, we need to try out those new tactics!"
        g4 "There is a lot at stake here! We can't afford to lose even a single game!"
        g4 "We can't show any weakness to those Slytherins!"
        cho "Is my success really that important to you, Sir?"
        cho "I'm glad!"
        m "Are you ready [cho_name]?"
        cho "I am!"
        m "Then show me the money."
        cho "What?"
        m "(I can't lose this much gold to Snape. I'll show that bastard!)"
        g9 "Say it,[cho_name]!{w} Show me the money!"
        cho "I don't have any on me, Sir." # embarassed
        g9 "No, no, say the quote!{w} Say \"Show me the money.\""
        cho "Show me the money?" # wink
        g4 "Say it like you mean it, brother!"
        cho "What?"
        g4 "Show me the money!" # loud
        if cc_pf_strip.points >= 2:
            cho "(He knows I'm a girl...why would he say that?)"
        else:
            cho "(I'm a girl...why would he say that?)"
        g4 "Show me the money!" # louder
        cho "May I leave, Sir?"
        g9 "What you gonna do, [cho_name]?"
        cho "Leave?"
        m "..."
        g9 "Return to my office after the game."
        cho "Yes..." # embarrassed.

        # Cho leaves.
        call cho_walk(xpos="door", ypos="base", speed=2)

        call cho_main("(That was weird...)","base","base","base","mid", ypos="head")

        call cho_chibi(action="leave")

        $ cho_busy = True
        $ quidditch_commentator = None # Hermione won't show up.
        $ quidditch_match_in_progress = True
        $ cc_st.match_counter += 1 # Stat counter

        jump main_room


    # Intro 2
    elif cc_st.match_counter == 1:
        m "Let's try this again, shall we?"
        m "I spoke with your teacher, she'll get those nitwits to play again..."
        cho "Professor Tonks, wasn't it?"

        if quidditch_commentator == "tonks":
            cho "Well that's great and all, but..."
            cho "I have my doubts about having her as a commentator."
            m "Are you sure? Even a donkey would be better suited than Hermione."
            cho "There's some truth in that..."
        else: # Hermione
            m "Yep."
            cho "That's Fantastic!"
            cho "I'm really glad we have her as a teacher!"
            m "Make sure to thank her for it...some day."
            cho "I will, [cho_genie_name]."
        pass


    # Repeat.
    else:
        m "Ready for your next match, [cho_name]?"
        if quidditch_commentator == "tonks":
            cho "[cho_genie_name], is Professor Tonks still going to commentate the match?"
            m "Yes. Hermione still hasn't changed her mind about it."
            cho "Alright..."
        else: # Hermione
            m "Be ready to do another practice match today."
            cho "Yes, [cho_genie_name]."
            cho "I hope all my recent practice will pay off.."
        pass


    cho "I shall be back after the game."
    m "Off you go then."

    # Cho leaves.
    call cho_walk(action="leave", speed=2)

    $ cho_busy = True
    if quidditch_commentator == "hermione":
        $ hermione_busy = True
    elif quidditch_commentator == "tonks":
        $ tonks_busy = True

    $ quidditch_match_in_progress = True
    $ cc_st.match_counter += 1 # Stat counter

    jump main_room



label cc_st_return:
    if cc_st.match_counter == 1:
        jump cc_st_return_E1 # Slyth & HG don't attend.

    $ ss_summon_pause = 0 # Can drink with Snape again, now that Slyth plays.

    if quidditch_commentator == "tonks":
        jump cc_st_return_E2

    elif quidditch_commentator == "hermione":
        jump cc_st_return_E3

    else:
        jump cc_st_return_fail


label cc_st_return_E1:
    #Fails
    # This event needs to happen before any other girl can enter.
    # Genie takes a nap and snorts.
    call play_music("stop")
    pause.5

    show screen blktone
    show screen bld1
    with d5
    pause.2

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
    pause.2

    hide screen blktone
    hide screen bld1
    with d5
    pause.8

    call bld
    m "Wha-...?"
    call bld("hide")
    pause.5

    # Cho walks in.
    call cho_walk(action="enter", xpos="desk", ypos="base", speed=2.5)

    # Cho is furious.
    call cho_main("","angry","base","angry","mid", xpos="mid", ypos="base")
    m "..."
    m "What are you doing here? You’re not supposed to be back yet..."
    cho "I’m surprised you could you tell..."
    g4 "Because you just woke me up - in the middle of my nap."
    cho "Oh no, Sir. I'm terribly sorry!"

    menu:
        m "..."
        "Are you mocking me for taking a nap?":
            cho "No, sir."
            m "..."
            g4 "(Damnit, that naive brattiness of hers is turning me on!)"

        "Brats like you need to be punished!":
            cho "Punished? For what?" # angry
            g4 "For being a pain in my ass!"
            g4 "And for waking me up in the middle of my nap!"
            $ cho_mood += 2

    m "Why aren't you on that Quidditch ditch right now?"
    cho "It's a pitch, Sir."
    m "I thought we were going to prepare for the next match, or are we already finished with that?"
    g4 "(Please say yes! I want to do the naughty stuff already!)"
    cho "Yes, we are..."
    g9 "(Yes!)"
    cho "For today, that is..."
    m "(Balls...)"
    cho "We couldn't play today because the entire Slytherin team didn't even bother to show up!"
    cho "And neither did our commentator!"
    m "Hermione?"
    cho "Yes! Where the bloody hell was she?!"
    m "Why are you asking me?"
    m "Did you forget to tell her about today's training?"
    cho "She knew very well that she had to be there!"
    cho "And so did those braindead Slytherins."
    cho "Spineless cowards..."
    cho "They have no interest in training against us!"
    cho "Because why should they... They'll win anyway!"
    cho "They assured me that they would be there today!"
    cho "Such a pathetic bunch of apes!"
    m "A troop."
    cho "What?"
    m "It’s called a troop of apes."
    cho "Whatever..."
    cho "If I see their captain tomorrow, I'm gonna knee him in the groin!"
    g4 "Yikes!"
    m "I'm afraid I can't have you do that..."
    cho "Why not? They deserve it!"
    m "No guy deserves that..."
    m "I’d rather deal with it myself, than let you do that, if you don't mind!"
    cho "Fine..." # disappointed
    cho "But you better do something, quickly! Get those idiots to play!"
    cho "We can't possibly win if we don't know their tactics."
    cho "Or know if our tactics work against them, for that matter..."
    m "I'm on it..."
    cho "And what about Granger?"
    g4 "*Ugh*... her too?"
    cho "Yes!"
    m "At least let me finish the first quest - before taking on another one..."
    cho "You better get that spineless mop's ass back behind that podium!"
    cho "She agreed to do this! We need an announcer!"
    m "I'll talk to her..."
    cho "Then make it quick!"
    cho "Good night, Sir."

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "That girl sure is a piece of work..."

    $ hermione_busy = True
    $ cho_busy = True
    $ cho_mood += 6
    $ lock_cho_practice = True

    $ cc_st.return_E1 = True # Triggers Hermione's return next day.

    jump main_room


label cc_st_return_E2:
    "Dev Note" "Return event 2 - Event not yet written."
    "Dev Note" "You picked the right clothing combination, but Hermione is not yet a commentator."

    # TODO: lock Cho's quidditch clothing and tactic.
    # They worked good enough so

    # Cho mentions that Tonks might be an issue, and would like to try one more time.

    $ hermione_busy = True
    $ cho_busy = True

    $ cc_st.return_E2

    jump main_room


label cc_st_return_E3:
    "Dev Note" "Return event 3 - Event not yet written."
    "Dev Note" "You picked the right clothing combination, and Hermione is not yet a commentator."

    $ her_mood += 6
    $ hermione_busy = True
    $ cho_busy = True

    $ cc_st.return_E3

    jump main_room


label cc_st_return_fail:
    "Dev Note" "Failed match, add writing."
#    m "Well, how did it go?"
#    cho "We lost, Sir."
#    elif quidditch_commentator == "tonks":
#        cho "Could we please get somebody else to commentate the game?"
#        m "Is Miss Tonks not good enough?"
#        cho "No, she's great..."
#        cho "Far better than that half-witt Granger..."
#        m "So what's the issue?"
#        cho "She's not only distracting those Slytherins, but my team as well."

    $ her_mood += 6
    $ cho_mood += 6
    $ hermione_busy = True
    $ cho_busy = True

    jump main_room



label cc_st_hermione_E1:

    # Hermione stands at the door.
    call play_sound("door")
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call bld
    g4 "..."

    # Hermione barges in.
    call her_walk(xpos="desk", ypos="base", speed=2)

    call her_main("","base","base","base","mid", xpos="mid", ypos="base") # annoyed
    pause.5
    call her_main("I can't believe her...","base","base","base","mid", trans="hpunch") # angry
    m "Good day to you too..."
    her "That bitch has been walking around saying that I quit the commentator job."
    m "Who did?"
    her "Cho Chang!"
    g4 "..."
    m "Wait, so you didn't quit?"
    her "I'm quitting now!"
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
    call her_walk(action="leave", speed=2.5)

    call bld
    g4 "(What in the great desert sands do these women want from me...)"

    $ hermione_busy = True

    $ cc_st.hermione_E1 = True

    jump main_room



### Stage 2 ###

label cc_st_snape_E1:
    # hangout event
    sna "Your precious Ravenclaw bird, made any breakthroughs with her yet?"
    m "The little asian?"
    sna "Yes, Miss Chang."
    m "..."
    sna "I wish her best of luck against my team of Slytherins."
    sna "She'll need it."
    m "What kind of game are you playing?"
    sna "Sorry?"
    m "Your team didn't show up to the last practice match!"
    sna "Well, there’s no specific rule that forces the teams to practice against each other..."
    m "There’s not?"
    m "(Actually that does make sense...)"
    sna "Of course not, but it is heavily encouraged for students that are looking to make it professionally."
    m "Do you have something to do with this?"
    sna "I don’t know what you’re talking about..." #Smirk
    g4 "You little weasel..."
    sna "Ha! Do you have another trick up your sleeve?"
    sna "What’s it gonna be? An even shorter skirt? Prohibit her to wear panties?"
    sna "Well, we'll see during the game if it has any effect..."
    g4 "*Grrrrr!*..."
    g4 "Get your team back on that pitch, you coward!"
    sna "No...I don't think I will..."
    g4 "Give me that wine!"
    sna "You want some?"
    call play_sound("spit") # Spits in the cup
    m "I'm gonna win that bet. Then I'll have the last laugh!"
    sna "I wish you good fortune."
    m "..."
    g4 "Get your wine from someplace else, you slacker."
    sna "You won't win by making friends, isn't that right?"
    m "..."
    sna "*Hrhm*... Good riddance, then..."

    ">Snape empties the last drop of wine, before he quietly leaves."
    ">You feel a sense of remorse shortly after he's gone, realizing that you're both just parts of the same coin."
    ">Your friendship level with him has not changed..."

    $ snape_busy = True
    $ ss_summon_pause += 5 # Snape can't be summoned for a couple of days. Can be set to 0 once you talked to Tonks.

    $ cc_st.snape_E1 = True

    jump main_room


label cc_st_tonks_E1:
    # Start hangout event.
    m "I wanted to ask you for a favour..."
    ton "You want me to sell a favour to you?"
    ton "You sure you can afford me?" #Horny
    m "Not that kind of favour."
    ton "Aww..."

    # Tell Tonks about Cho.
    m "You know this Quiddish sport the students play here?"
    ton "Quidditch?"
    m "Close enough."
    m "The next match is coming up, and I require your help with something."
    ton "Of course. What is it?"
    m "You know this little asian girl?"
    ton "Cho Chang?"
    m "Why yes, very good guess."
    ton "Well, I figured you'd be talking about her if it has to do with Quidditch."
    m "She's one of the girls I buy favours from."
    ton "No way!"
    ton "You got that little hotty- *Uhm*... hot-head to sell you favours?"
    m "Once or twice..."
    ton "I'm impressed."
    ton "Tell me everything!"

    menu:
        m "..."
        "Tell her everything":
            pass

        "Don't tell her":
            m "I don't think I should..."
            ton "What? Why not?"
            m "Miss Chang wouldn't like anybody to know."
            ton "I can keep a secret!"
            m "I really shouldn't..."
            ton "Tell me, or I'll jinx your balls off!"
            g4 "*Ghzzz!* Alright! Alright!"
            m "You sure know how to get me to talk..."

    if cc_pf_strip.points >= 2:
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's past relationships (below conversation.)
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's past relationships (below conversation.)
        m "She's been stripping for me."
        ton "Cho?! I can't believe it!"
        g9 "Oh, you better believe it!"
        ton "Holy shit!"
        ton "I'd pay so many galleons to watch that girl take her clothes off..."
        ton "You need to invite me next time!" # angry
        m "And how would I get her to agree to that?"
        ton "Well... *Uhm*..."
        m "It was difficult enough to get her to strip just for me..."
        m "She only did it because I helped her win against Hufflepuff."
        ton "So that was your idea with the skirt? Very clever."
        m "If you help her against Slytherin..."
        g9 "Maybe I can arrange something with the two of you?"
        ton "Or all three of us!" # horny
        g9 "I'm sure that minx would love that!"
        ton "I can't wait!"

    else:
        # Enable special event with Tonks that plays after you blackmailed Hermione, to tell Tonks about Cho's stripping (above conversation.)

        m "We were mostly just chatting..."
        ton "About what?"
        m "Her previous school year... couple of relationships she had."
        ton "Intriguing... a couple?"
        ton "I assume Cedric Diggory was one of them? According to Miss Granger."
        ton "Who else?"
        m "Some of the other contestants of that tourney..."
        ton "The tri wizards tournament?"
        ton "That happened last year right? Such a shame I missed it."
        m "We should hold our own tournament!"
        m "The tri-bitcha... Bi-curious-ishar.."
        m "It’s a work in progress title..."
        m "Anyway..."
        g9 "She said one of them was a girl!"
        ton "Oh my..." # Horny
        ton "I didn't know she was..." # Horny
        g9 "They even made out a couple of times!"
        ton "Fuck!" # Ahegao?
        m "..."
        ton "..."
        m "You alright there?"
        ton "Huh? Oh yes..."
        ton "My mind was just drifting off for a second..."
        m "I can imagine why..."


    # Talk about Slytherin.
    m "..."
    m "I have to help her beat the opposing team in the next match."
    ton "Slytherin? That shouldn't be too difficult."
    m "Really? How so?"
    ton "Their tactics revolve around strength, brute force, and manifesting their dominance on the field!"
    ton "A good strategy for when you're in bed with your partner, but not in Quidditch."
    m "You don't say..."
    g4 "Wait, what?"
    ton "I've seen them play a couple of times. They clearly aren't the brightest bunch..."
    ton "What tactics are you gonna use against them?"
    m "I don't know. They refuse to show up for their training matches."
    ton "Well that's unfortunate..."
    ton "You should ask Snape. Maybe he could get those lazy gits back on the pitch..."

    if cc_st.snape_E1:
        m "I already did. He isn't going to help me out..."
        ton "Well that's just like him."
    else:
        m "I guess I could..."
        ton "Yeah, maybe not..."

    ton "Just leave it to me, Genie."
    ton "I'll get those shits back on the grass..."
    m "(Aren't they playing up in the air?)"
    m "And how will you accomplish that?"
    ton "Oh, don't worry..."
    ton "I promise I'll tell you all about it some other time."

    # You tell Tonks about Hermione.
    m "..."
    if quidditch_commentator == None:
        m "That's not all, though. There's something else I need your help with."
        ton "You can't expect me to fix all of your problems, Genie."
        m "It's about Hermione's role as a commentator..."
        ton "Really? What happened to Miss Granger?"
        m "She quit..."
        ton "Hmm... that's too bad, it was so cute listening to her fumble over her words..."
        m "Could you convince her to change her mind?"
        ton "I can try. But don't get your hopes up..."
        ton "I've saw what she had to go through last game."
        ton "She's still getting mocked about it, that poor thing..."
        m "We need her to do it. We don't have anybody else."
        ton "Well..."
        ton "I could do it."
        m "You can? But I thought -"
        ton "You think I’d be biased?"

    else:
        m "Did you know Hermione wanted to quit her task as a commentator?"
        ton "Did she now? I thought she did well in the Hufflepuff game."
        ton "A bit wooden, but not bad for her first try."
        ton "Speaking in front of such a large crowd and all."
        ton "I thought it was rather cute listening to her fumble her words..."
        ton "What changed her mind?"
        m "Cho helped me convince her to do it."
        ton "Really? How? I'd love to hear it."
        m "*Hmm*... Maybe next time."
        ton "Very well..."
        ton "I'd make for a great commentator, don't you think?"
        m "I thought teachers weren't allowed to-"
        ton "What? Because as a teacher I'd be biased?"


    ton "Well, thanks to your efforts, Hufflepuffs is already out..."
    ton "And now the best we can hope for is to not get last..."
    ton "It's always third or nothing with us Puffs."
    m "(Puffs?)"

    if quidditch_commentator == None:
        ton "Anyhow, I shall talk to Miss Granger..."
        ton "Should she still not want to commentate, then I shall fill in for her."
        $ quidditch_commentator = "tonks"
    else:
        ton "Should Miss Granger change her mind again, I can fill in for her."
        ton "I'm a great talker, as you probably already know."

    g9 "I'm so glad to have you!"
    ton "Aww, you're so sweet!"
    ton "*Hick!*... whoopsie..."

    if daytime:
        ">You finish your drinks before calling it a day."
    else:
        ">You finish your drinks before calling it a night."

    $ tonks_busy = True
    $ lock_cho_practice = False

    $ cc_st.tonks_E1 = True

    jump main_room


label cc_st_hermione_blackmail:

    call her_main("","base","base","base","mid", xpos="mid", ypos="base", trans="fade")

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
        g4 "(Dammit! She doesn't want to nudge one bit!)"
        m "(Did I just reach one of those annoying adventure game roadblocks?)"
        g4 "(Preventing me from progressing this quest, until I find some stupid item or do some other mindless task...)"
        m "(I should just forget about this and have some fun with Cho...)"

        jump hermione_requests


    ### Hermione Blackmail ###

    # After Cho stripped in front of Hermione.
    her "What is it, [genie_name]?"
    m "..."
    g4 "(I'm done playing nice!)"
    m "(Maybe I can blackmail her somehow...)"
    her "[genie_name]?"
    m "[hermione_name], you're going to commentate that match. Whether you like it or not."
    her "No. And you won't get me to change my mind on this."
    g9 "Are you sure about that?"
    her "Why?" # suspicious

    menu:
        m "I'll spread rumours that..."
        "\"You're having sex with your headmaster!\"" if hg_pf_sex.counter > 0:
            $ d_flag_01 = True
            pass
        "\"You like playing with your headmaster's cock!\"" if hg_pf_blowjob.counter > 0 or hg_pf_handjob.counter > 0 or hg_pf_titjob.counter > 0:
            $ d_flag_01 = False
            pass
        "\"You like stripping for your headmaster!\"": # always happens at this stage.
            $ d_flag_01 = None
            pass

    if her_tier == 6:
        her "[genie_name], you can't do that!"
        her "Please don't do that!" # sad.
        m "I do whatever I want."
        her "No you can't. We had an agreement."
        g9 "Did we now?"
        if d_flag_01 == None: # Strip
            her "Yes..."
        else:
            her "I won't ever forgive you if you go through with that!"
            $ her_mood += 4
        her "If you intend to continue selling me favours, I suggest you don't make this public!"
        her "I can't have any of my friends know about how I..."
        if d_flag_01 == True:
            g9 "Fucked your headmaster?"
        elif d_flag_01 == False:
            g9 "Played with my cock?"
        else: # Strip
            g9 "Put on a stip-show for me?"
        her "Earned those points, is what I wanted to say..."
        m "..."
        her "My answer remains: No."

    else: # Tier 3, 4, 5
        if d_flag_01 == False: # Played with cock. 4 + 5 only.
            her "What? That's insane!"
            her "You're bluffing!"
            m "Soon the whole school will know."
            g9 "How well you can handle a cock!"
            $ her_mood += 8
        else:
            her "You can't do that, [genie_name]!"
            her "It's bad enough that Professor Snape knows..."
            m "And soon the whole school will know."
            $ her_mood += 4
        her "No!"
        her "I'll write to the ministry again, I'll have you know!"
        her "You'd be sent to Azkaban for this."
        if d_flag_01 == False:
            m "For what?"
            her "For forcing me to touch you!"
        else:
            m "For watching a harmless dance?"
            her "For forcing me to strip for you!"
        g4 "I didn't force you to-... Damnit..."
        her "*Hpmf*..." # Annoyed


    g4 "(If that doesn’t change her mind then what will?)"
    m "(I need an even smarter idea. Maybe I can ask Cho how we can get Granger to bend...)"
    m "(She said she'd do anything to win that cup, so she better stick true to that.)"
    m "(Maybe with her help we can get Granger to-...)"
    g4 "(Oh, I know! That's just it!)"

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

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # Hermione puts her clothes on if she's naked.
    # TODO: add clothing equip for Hermione.

    call her_walk(xpos="mid", ypos="base", speed=1)
    pause.1

    # Summon Cho.
    call play_sound("door")
    call cho_chibi("stand","door","base")
    with d3

    call chibi_effect(action="thought", chibi="hermione")
    pause 1

    call cho_walk(xpos="680", ypos="base", speed=0.6)
    pause .2

    call her_main("","base","base","base","mid", xpos="270", ypos="base", flip=True)
    call cho_main("Hello, Sir.","base","base","base","mid", xpos="close", ypos="base")
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
    her "I can’t believe you’d stoop as low as blackmail for some stupid Quidditch Cup!"

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
    g9 "Every time you don't, I'll take 50 points from Gryffindor!"
    her "That's just typical of you!"
    m "Make sure to be present..."
    her "..."

    m "You are both dismissed..."
    her "..."

    call her_walk(action="leave", speed=2)
    pause.2

    if daytime:
        call cho_main("Good day, Sir.","base","base","base","mid", ypos="head") # Happy
    else:
        call cho_main("Good night, Sir.","base","base","base","mid", ypos="head") # Happy

    call cho_walk(action="leave", speed=0.6)

    call bld
    g9 "Quest complete!"

    $ cho_mood = 0
    $ hermione_busy = True
    $ cho_busy = True

    $ cc_st.hermione_blackmail = True
    $ quidditch_commentator = "hermione"

    jump main_room



### Stage 3 ###

label cc_st_talk:
    # you haven't talked to Tonks yet.
    if lock_cho_practice:
        cho "Have you gotten those Slytherins pigs to play yet?"
        m "Not yet, but I'm on it."
        cho "Please just hurry up, Sir."
        cho "We need to practice..."

    # played one match with Tonks.
    elif cc_st.match_counter >= 2 and quidditch_commentator == "tonks" and cc_pf_strip.points < 3 and not cc_st.hermione_blackmail:
        cho "So, what is Granger up to?"
        cho "Is she still too frightened to face those jolly Slytherins?"
        m "Well, we have Tonks to do that now..."
        cho "But Tonks isn't even on our side! This won't help!"
        m "And Hermione is?"
        cho "At least Granger is biased, and doesn't befuddle my own team as well as theirs!"
        m "Befuddle?"
        cho "Professor Tonks won't stop flirting with the boys on my team!"
        cho "Those stupid idiots can barely sit on their brooms because of her..."
        m "Why? Is the wood too hard?"
        m "(When do those people realize that carpets are more comfortable...)"
        cho "We need to get that Gryffindor skunk to peeve those Slytherins, so we can get past them!"
        m "..."

    # after strip and before blackmailing Hermione.
    elif quidditch_commentator == "tonks" and cc_pf_strip.points >= 3 and not cc_st.hermione_blackmail:
        m "Would you be willing to help me change Hermione's mind?"
        cho "Of course? And How?"
        m "With-"
        cho "With blackmail?" # excited
        m "...No."
        m "Why don't you try to just ask her politely?"
        cho "Bull-{w=0.3}shit! That's never going to work."
        cho "We already have dirt on her. Why don't we just blackmail her again!"
        m "Like when you forced her to watch your little strip-show?"
        cho "That was fun wasn't it?"
        g9 "Shit yeah, it was!"
        m "We might have to employ such tactics after all, if we want to win."
        m "Feeling any sense of remorse is pointless in a game such as this..."
        cho "You're absolutely correct, Sir!"
        cho "Quidditch is a selfish, relentless game of committing all sorts of atrocities and dishonest acts!"
        m "I wasn't talking about Quidditch..."

    # response when there is no new task for you.
    else:
        cho "I'm confident that we can win this, [cho_genie_name]."
        cho "Slythein has no blasted chance against us!"

    jump cho_requests
