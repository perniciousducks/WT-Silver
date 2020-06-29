

### Manipulate the enemy male Quidditch players ###

### Start ###
label cc_pr_manipulate_boys_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    ### Tier 1 (pre Hufflepuff) ###
    if cho_tier == 1:

        # Intro
        if cc_pr_manipulate_boys.points == 0:
            m "So what do we know about our opponents?"
            call cho_main("Hufflepuff? Well their team isn't the best, but they have a really strong seeker.", "soft", "base", "base", "mid")
            m "Right...{w=0.3} who was that again?"
            call cho_main("Cedric Diggory. How often do I have to repeat that to you, [cho_genie_name]?", "annoyed", "narrow", "base", "mid")
            m "You will know once you get to be my age..."
            call cho_main("Oh- I'm sorry, Sir.", "soft", "narrow", "worried", "mid")
            call cho_main("I should be more respectful of your age.", "soft", "narrow", "base", "downR")
            m "(Because at my age you stop giving a damn...)"
            call cho_main("Cedric is a bit of a block head, but he's quite a competent seeker.", "open", "base", "raised", "R")
            call cho_main("And very popular with the girls...", "soft", "base", "raised", "mid")
            m "Do I sense a little bit of something in your voice?"
            call cho_main("Of course not! We stopped dating ages ago!", "soft", "base", "base", "downR", cheeks="blush")
            call cho_main("I didn't want to be seen with an idiot like him anymore...", "open", "closed", "angry", "mid")
            call cho_main("Not if I'm supposed to be a proper Ravenclaw...", "annoyed", "narrow", "angry", "mid")
            call cho_main("{size=-4}Even if he's cute...{/size}", "normal", "base", "worried", "downR", cheeks="blush") # Small text.
            m "That's good. We can use this to our advantage."
            call cho_main("We can? How?", "soft", "wide", "base", "mid")
            m "You two having history! Which means he'll be much easier to distract during the game."
            m "All you have to do is make him believe something might actually happen."
            call cho_main("What?{w=0.3} I don't want to go out with Cedric again!", "angry", "wide", "base", "mid")
            m "I know, I know, you just have to make him believe that you will."
            call cho_main("Oh-...", "soft", "base", "base", "downR", cheeks="blush")
            call cho_main("Well... how do I do that?", "annoyed", "base", "base", "mid")
            m "It's a little something called {b}seduction{/b}..."
            m "It should be your gender's bread and butter."
            call cho_main("Isn't that a little mean?", "soft", "closed", "base", "mid")
            m "Mean? You're not doing anything wrong, are you?"
            m "You're just talking to him..."
            call cho_main("So I'm just supposed to lead him down the garden path?", "soft", "base", "raised", "mid")
            m "Only if you want Ravenclaw to have a chance at winning."
            call cho_main("*Hmmm*...", "annoyed", "narrow", "base", "R")
            m "And don't worry about him.{w} He's hardly going to complain about having a pretty little thing like you to talk to..."
            g9 "Not to mention look at..."
            call cho_main("Hey!", "soft", "base", "base", "mid")
            m "I'm just saying, he hasn't got anything to be whine about."
            m "And if you are worried about his feelings..."
            m "Maybe you can fool around a little... I'm sure that would make him forget all about the garden path..."
            call cho_main("Sir!", "mad", "narrow", "base", "mid")
            m "I'm just telling you to use what the gods gave you -- to try and win a game."
            call cho_main("Can't I use what they gave me to just catch the snitch?", "annoyed", "narrow", "angry", "mid")
            m "And how's that plan been working out so far?"
            call cho_main("*Ugh!* Fine...{w} Point taken...", "annoyed", "narrow", "angry", "R")
            call cho_main("So I just have to make him think there's something between us again?", "soft", "base", "base", "mid")
            call cho_main("I think I can do that...", "annoyed", "narrow", "base", "down")
            m "Good, let me know how it goes..."
            call cho_main("Yes, [cho_genie_name]!", "base", "base", "base", "mid")

        # Repeated
        else:
            m "Ready to mess with Hufflepuff again?"
            call cho_main("I guess so...", mouth="soft", face="happy")
            g9 "Great! I'll see you later today for your report, [cho_name]!"
            call cho_main("Yes, [cho_genie_name]!", "base", "base", "base", "mid")

    ### Tier 2 (pre Slytherin) ###
    elif cho_tier == 2:

        # Intro
        if cc_pr_manipulate_boys.points == 0:
            m "[cho_name], how well -- in your opinion -- did you do in your last match?"
            call cho_main("I think I did quite well with distracting those Hufflepuffs.", "annoyed", "base", "base", "mid")
            m "Only one Hufflepuff!{w=0.6} We were lucky you could secure that win with such low effort..."
            call cho_main("(...)", "annoyed", "base", "worried", "downR", cheeks="blush")
            m "We have to up our game to win against the next house, don't you think?"
            m "Manipulating just one player won't be enough this time! We have to put our focus on their entire team!"
            call cho_main("You might be right about that, [cho_genie_name].", "soft", "base", "worried", "mid")
            call cho_main("Slytherin's team is quite good overall, and they have some of the best players at this school.", "open", "closed", "base", "mid")
            call cho_main("What do you suggest I should do?", "annoyed", "narrow", "worried", "mid")
            m "Same as with that Diggory boy!"

            menu:
                "\"Be affectionate and flirty!\"":
                    g4 "Just go and talk to them. And flirt with them for a bit..."
                    call cho_main("I suppose I can do that.", "annoyed", "base", "base", "downR")
                    call cho_main("But, Sir... What if someone were to see me with them?", "soft", "narrow", "angry", "mid")

                "\"Make out with them...\"":
                    call cho_main("Make out with?{w=0.6} Those Slytherins-", "soft", "wide", "worried", "mid", cheeks="heavy_blush")
                    call cho_main("*guargh*", "open_tongue", "happyCl", "angry", "mid", cheeks="blush", trans=hpunch)
                    call cho_main("*cough*{w=0.6}-*guargh*!{w=0.8}-*cough*", "open_wide_tongue", "happyCl", "worried", "mid", cheeks="blush", trans=hpunch)
                    call nar(">You hear Cho make some inadvertent gag noises...")
                    m "Is everything okay, girl?"
                    call cho_main("No!{w=0.3} It's not okay!", "angry", "wide", "worried", "mid", cheeks="blush")
                    call cho_main("Why would you think I want to snog with those repulsive, yuck-ugly Slytherin degenerates?!", "open", "wide", "worried", "mid", cheeks="blush")
                    call cho_main("The thought alone utterly disgusts me, [cho_genie_name]!", "open_tongue", "happyCL", "worried", "mid", cheeks="blush")
                    call cho_main("I'll do anything but that!", "mad", "narrow", "worried", "mid")
                    m "So no kissing?"
                    call cho_main("Absolutely not!{w=0.8} Not even with Malfoy...", "angry", "closed", "angry", "mid", cheeks="blush")
                    m "Very well.{w=0.3} Just flirt with them in that case..."
                    call cho_main("And what if someone were to see me with them?", "soft", "narrow", "angry", "mid")

            m "Would that be an issue?"
            call cho_main("Since they are on the enemy team, yes!", "annoyed", "narrow", "angry", "mid")
            call cho_main("What if my team was to find out I hang around Slytherins?", "angry", "base", "base", "mid")
            call cho_main("{b}Slytherins?!{/b}", "clench", "wide", "base", "mid")
            m "So? Just do it in secret then."
            call cho_main("That...{w=0.3} might work.", "annoyed", "base", "base", "R")
            m "Don't you have any classes with them?"
            call cho_main("I do on some days.", "soft", "narrow", "worried", "mid")
            m "Then give them a note to meet you alone once the class is finished.{w=0.6} Easy..."
            call cho_main("I guess I could do that.", "base", "base", "base", "mid")
            m "They can read, right?"
            call cho_main("Yes, I do believe they can read.{w=0.8} But don't take my word for it...", "soft", "narrow", "worried", "mid")
            m "You need to find a way to convince them to throw the game. It's our only chance..."
            #m "Do you have any ideas how you could accomplish that?"
            #call cho_main("I- *uhm*...", "annoyed", "base", "base", "R")
            #call cho_main("I could still try to flirt with them a bit, I guess.", "soft", "base", "worried", "mid")
            #m "I doubt that that will be enough..."
            #call cho_main("", "annoyed", "base", "worried", "mid")
            call cho_main("I'll try my best, [cho_genie_name].", "smile", "narrow", "base", "mid")
            m "Let's just see how it goes."
            m "If anything goes wrong...{w=0.8} just improvise..."
            call cho_main("Very well, Sir.", "base", "base", "base", "mid")
            m "Report back to me later today with your results."
            call cho_main("Yes, Sir!", "smile", "base", "base", "mid")

        # Repeated
        else:
            m "Time to brighten up some Slytherin's day again..."
            g9 "Go and get their players on \"your\" side!"
            call cho_main("I will try my best, [cho_genie_name]!", mouth="smile", face="happy")
            g9 "Report to me later as usual, [cho_name]!"
            call cho_main("Yes, Sir!", "base", "base", "base", "mid")

    ### Tier 2 (pre Gryffindor) ###
    elif cho_tier == 3:
        if not cc_pr_manipulate_boys.is_event_complete(3, 1): # Completed The Twins?

            if not cc_pr_spy_boys.is_event_complete(1, 1):
                # Return if player has not spied on the Twins just yet.

                m "Let’s try and manipulate the girls on the enemy team!"
                call cho_main("You're expecting me to just jump in blind?", "angry", "base", "base", "mid")
                call cho_main("I don't know any of these girls, how do you expect me to manipulate them in any way without knowing what I'm dealing with?", "annoyed", "wide", "base", "mid")
                m "Good point, perhaps we should consider spying on them a bit beforehand."

                call cho_main(xpos="base", ypos="base", trans=fade)

                jump cho_requests_menu

            m "Time to manipulate the enemy a bit."

            m "Today I’d like you to target the boys."
            cho "Okay..."
            m "Let’s start off with the twins."
            m "Remind me what we know about them."
            cho "They mostly focus on trickery and pranks, doing anything for a laugh... ."
            m "Perhaps stooping to the Twins’ level could help you learn more about them."
            cho "What do you mean by that?"
            m "Since they’re tricksters and love disrupting things..."
            m "I suggest trying to find a way to make them use one of their tricks during the game. Surely they wouldn’t be able to help themselves if presented an opportunity."
            cho "Okay then."
            cho "Wish me luck!"
            m "Good luck."

        elif not cc_pr_manipulate_boys.is_event_complete(3, 2): # Completed Ron Weasley?

            if not cc_pr_spy_boys.is_event_complete(1, 2):
                # Return if player has not spied on Ron Weasley just yet.

                m "Let’s try and manipulate-"
                cho "I’m going to stop you there..."
                m "Yes?"
                cho "There’s no way I’ll try this again before I know more about the boys."
                m "Fine..."

                call cho_main(xpos="base", ypos="base", trans=fade)

                jump cho_requests_menu

            m "Let’s target the other Weasley boy this time."
            cho "You actually want me to target that pervert?"
            m "Sort of... He won’t be the main goal of this operation."
            cho "Then, what is?"
            m "Miss Granger is quite protective of her friends isn’t she?"
            cho "Yes... the few times I’ve seen them without her she’s usually just around the corner talking to some teacher or another."
            m "Then use those moments to your advantage... Miss Granger is also part of the game isn’t she?"
            m "If you can somehow spark that jealousy or protectiveness of her friends..."
            m "Angering her enough could transfer to the game... And since she’ll be stuck in the commentator booth the whole time she won’t be able to pull them away from you."
            cho "..."
            cho "That might actually work..."
            cho "If anything it gives me an excuse to piss her off..."
            cho "Not that I’ve needed one previously." #smirk
            m "Then it’s settled, report to me in the evening as usual."
            cho "Will do!"

        elif not cc_pr_manipulate_boys.is_event_complete(3, 3): # Completed Harry Potter?

            if not cc_pr_spy_boys.is_event_complete(1, 3):
                # Return if player has not spied on Harry Potter just yet.
                m "Let’s try and manipulate-"
                cho "I’m going to stop you there..."
                m "Yes?"
                cho "There’s no way I’ll try this again before I know more about the boys."
                m "Fine..."

                call cho_main(xpos="base", ypos="base", trans=fade)

                jump cho_requests_menu

            m "How about we annoy Miss Granger some more?"
            cho "Of course!"
            m "Let’s target her other friend today."
            cho "Harry Po-"
            m "The Potter boy!"
            cho "..." #annoyed
            m "*Ahem*... Yes..."
            m "Try and really get under her skin this time!"
            cho "That shouldn’t be very hard seeing how she reacted last time..."
            cho "Wish me luck!"
            m "Good luck."

        else:
            # Repeated

            m "Let’s manipulate those boys some more!"
            cho "I thought we were done?"
            cho "Although..."
            cho "I could annoy Hermione some more!"
            m "Don’t forget the twi-"
            cho "This will be so much fun!"

            # Cho leaves early!
            call cho_walk(action="leave")
            $ cc_pr_manipulate_boys.inProgress = True

            m "Twins..."
            m "Well, can’t say she lacks motivation anymore..."

            jump end_cho_event


    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_manipulate_boys.inProgress = True

    jump end_cho_event



### Return Events ###

### Tier 1 (pre Hufflepuff) ###

label cc_pr_manipulate_boys_T1_intro_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)
    m "How did it go?"
    call cho_main("It went...{w=0.3} well?", "soft", "base", "raised", "R")
    call cho_main("Maybe a little too well... He tried to kiss me!", "annoyed", "base", "raised", "mid")
    g9 "Really? Nice work!{w=0.6} Did you slip him a little tongue?"
    call cho_main("[cho_genie_name]!{w=0.3} No, of course not!", "soft", "wide", "base", "mid")
    m "Why not?"
    call cho_main("Because I'm not some slut who gives it away for free!", "annoyed", "narrow", "angry", "mid")
    m "It was only a kiss..."
    m "(Now I'm falling asleep)"
    call cho_main("A kiss is very personal!", "soft", "closed", "base", "mid")
    call cho_main("Besides, he didn't even try to make it special!", "annoyed", "narrow", "angry", "R")
    call cho_main("He just leaned in while I was in the middle of a conversation...", "annoyed", "narrow", "angry", "mid")
    m "Sounds special enough to me."
    call cho_main("Well it wasn't! I want a bit of romance...", "soft", "closed", "base", "mid")
    m "At least it sounds like you're doing a good job distracting him."
    call cho_main("If you say so...", "annoyed", "base", "base", "down")
    m "Just keep in mind why we're doing this."
    g4 "You can't chicken out of something as small as a kiss -- if you want Ravenclaw to have a chance!"
    call cho_main("Right, [cho_genie_name]!", "soft", "narrow", "worried", "mid")
    m "That'll be all for now, you can go."
    call cho_main("Thank you, [cho_genie_name].", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 3: # Points til 3.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)
    m "What's my favourite Quidditch player been up to today?"
    call cho_main("I think you'll be happy, [cho_genie_name]!", "base", "narrow", "base", "mid")
    g9 "I like the sound of that! Tell me what happened."
    call cho_main("Well, I thought about the best way to get to Cedric -- and I remembered how much he loved my bum!", "soft", "base", "base", "R")
    m "*Mhmm*... I can't say I blame him..."
    m "Let me guess, you tried the old \"drop your pencil trick\" on him?"
    call cho_main("\"Pencil trick?\"", "mad", "base", "raised", "mid")
    m "Yes. You \"accidentally\" drop your pencil, and then when you have the boy's attention, you bent down and-"
    call cho_main("Sir, we're only allowed to use \"quills\" here.", "soft", "closed", "base", "mid")
    m "So just use \"quills\" instead?"
    call cho_main("That would just make a mess and get ink everywhere...", "annoyed", "narrow", "angry", "mid")
    call cho_main("But I {b}did{/b} try something close to what you described...", "soft", "base", "base", "mid")
    g9 "You did?"
    call cho_main("Yes, Sir.{w=0.3} I pretended to drop my books, and when I bent down to pick them up, I gave Cedric a good view of my bum.", "base", "narrow", "angry", "mid")
    m "So...{w=0.3} you did the \"pencil trick\"...{w=0.8} Just with books."
    call cho_main("I've put my own spin on it. It's different enough...", "soft", "closed", "base", "mid")
    m "No it isn't."
    call cho_main("In any case, I think it worked.", "open", "narrow", "raised", "R")
    call cho_main("He couldn't keep his eyes off my bum for the rest of classes!", "base", "narrow", "angry", "mid")
    g9 "Well done, [cho_name]! You may leave now."
    call cho_main("Thank you, Sir.", "smile", "happyCl", "base", "mid")

    if cho_reputation < 3: # Points til 3.
        $ cho_reputation += 1

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="annoyed", xpos="mid", ypos="base", trans=fade)
    g4 "[cho_name]! Do you have some good news for me?"
    call cho_main("I'm afraid not this time, Sir.", "soft", "narrow", "worried", "mid")
    m "Why not? Tell me what happened..."
    call cho_main("Well, today I saw Cedric again down in the dungeons.", "open", "narrow", "worried", "R")
    g9 "{size=-2}(The dungeons? I like where this is going already!){/size}"
    call cho_main("Before I approached him I removed my Ravenclaw tie, and unbuttoned the top of my blouse.", "open", "closed", "base", "mid")
    m "A very well thought out strategy, girl!"
    call cho_main("I thought it would be enough to get his attention.", "soft", "narrow", "raised", "mid")
    m "Which I assume you got straight away?"
    call cho_main("No, Sir. But somebody else's...", "disgust", "narrow", "worried", "down", cheeks="blush")
    g9 "Intriguing!{w=0.3} Who else did you manage to snag?"
    call cho_main("Professor Slughorn, Sir.", "mad", "base", "worried", "mid", cheeks="blush")
    m "Who?"
    call cho_main("{size=+4}Professor Slughorn!{/size}", "scream", "closed", "angry", "mid", cheeks="blush", trans=hpunch)
    call cho_main("He -- once again -- had to stand in for professor Snape, who couldn't make it in time for his lecture.", "open", "narrow", "angry", "R")
    m "Snape is missing his classes? How often has this been happening?"
    call cho_main("Probably every other week or so.", "annoyed", "narrow", "raised", "R")
    m "{size=-2}(Slacker...){/size}"
    call cho_main("Anyway...{w=0.3} Slughorn sort of crossed paths with me when I was about to confront Cedric...", "open", "narrow", "worried", "mid")
    call cho_main("He came out of nowhere!", "soft", "wide", "base", "mid")
    call cho_main("And he stood so close, he could see right down my cleavage!", "disgust", "narrow", "worried", "down", cheeks="blush")
    g4 "{size=-2}(What a lucky git!){/size}"
    call cho_main("I couldn't move a single muscle! It was like I was frozen in place!", "soft", "narrow", "worried", "R")
    call cho_main("What if something like that would happen during the game?!", "soft", "narrow", "worried", "mid")
    m "You're right. That could be an issue..."
    call cho_main("And the worst thing is, he just kept staring!", "clench", "happyCL", "worried", "mid", cheeks="blush")
    m "And then? What happened?"
    call cho_main("He commended me about how well I did in my last potion lesson with him, so he awarded Ravenclaw five house points for my efforts.", "soft", "narrow", "angry", "mid")
    m "Sounds like a nice guy..."
    call cho_main("But Sir, I ruined my potion during the last lesson I had with him!", "quiver", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("The only reason he gave me those points, is because I let him stare down my shirt!", "disgust", "narrow", "worried", "down", cheeks="blush")
    call cho_main("I feel so dirty because of it...", "disgust", "happyCl", "worried", "down", cheeks="blush")
    m "You shouldn't feel dirty...{w=0.6} Maybe only \"a little\" dirty, if anything..."
    call cho_main("I'm sorry, Sir.{w=0.3} May I have permission to leave?", "soft", "narrow", "worried", "mid")
    m "Permission granted...{w=0.3} But try to be more effective next time."
    call cho_main("I will, Sir.", "open", "narrow", "worried", "down")
    call cho_main("Have a nice day.", "soft", "narrow", "worried", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 3: # Points til 3.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)
    m "So? How did it go?"
    call cho_main("Very well, Sir!", mouth="smile", face="happy")
    g9 "Yeah? Tell me about it!"
    call cho_main("I ran into Cedric on my way to the library...{w} Literally!", "soft", "wide", "base", "mid")
    call cho_main("I bumped into him and hit my head pretty hard...", "soft", "narrow", "worried", "mid")
    m "You poor thing..."
    call cho_main("It's nothing, Sir. I'm more than capable at enduring pain!", "soft", "narrow", "angry", "R")
    m "A useful skill to have, I can imagine..."
    call cho_main("I've grown to be quite tough -- and resistant to all sorts of pain -- after years of playing Quidditch...", "mad", "narrow", "angry", "mid")
    call play_sound("gulp")
    g4 "*gulp!*"
    call cho_main("Anyway, Cedric helped me back up on my feet...", "soft", "narrow", "base", "R")
    call cho_main("But before he could even apologise, I kissed him.", "base", "narrow", "base", "mid", cheeks="blush")
    call cho_main("It just... happened...", "clench", "narrow", "worried", "downR", cheeks="blush")
    m "Well done, girl!"
    call cho_main("It was really nice, though.", "soft", "narrow", "base", "mid")
    call cho_main("He still is a really good kisser!", face="horny")
    call cho_main("Compared to most of the others I had...", "base", "narrow", "base", "mid")
    g4 "!!!"
    call cho_main("Anyhow, I should get going.", "open", "base", "base", "R")
    call cho_main("It's getting late...", "soft", "base", "worried", "mid")
    m "Of course. You are dismissed."
    call cho_main("Good night, [cho_genie_name].", face="happy")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 3: # Points til 3.
        $ cho_reputation += 1

    jump end_cho_event



### Tier 2 (pre Slytherin) ###

label cc_pr_manipulate_boys_T2_intro_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    m "Good evening [cho_name].{w=0.6} How did today's task go?"
    call cho_main("I can't believe you convinced me to do this!", "clench", "narrow", "angry", "mid")
    m "So...{w=0.3} badly I take it?"
    call cho_main("No, it went perfectly...", "angry", "narrow", "worried", "down")
    m "So why the face?"
    call cho_main("Well, I did as you suggested.{w=0.6} I left a note for them to meet me alone after class.", "soft", "base", "worried", "mid")
    m "Great, so did they show?"
    call cho_main("Yes... apparently they could read after all... And they met with me after the lesson.", "soft", "narrow", "worried", "R")
    call cho_main("Once everyone had left and we were alone in the corridor. I didn't really know how to go about it.", "quiver", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("They must have felt how awkward I was as I approached them...{w=0.8} Or they had literally never had any woman approach them before.", "quiver", "base", "worried", "mid", cheeks="blush")
    m "So they didn't get that you were coming onto them?{w=0.6} Surely they can't be that thick..."
    call cho_main("No, sir. They got it alright...{w=0.6} perhaps a little too well.", "annoyed", "base", "worried", "down", cheeks="blush")
    call cho_main("Or they're just used to treating those Slytherin skanks as their personal squeeze toys...", "annoyed", "narrow", "angry", "R")
    m "So, what happened?"
    call cho_main("I came onto them a little bit...{w=0.6} Told them how impressed I was when watching their practice match against Gryffindor.", "open", "closed", "base", "mid")
    call cho_main("Told them that it must be lonely on the pitch with no girls on their team to fool around with.", "soft", "narrow", "angry", "mid")
    call cho_main("I couldn't stand the idea of complimenting them on their looks, so I told them how impressed I am with their pure strength...{w=0.8} which technically isn't a lie.", "horny", "narrow", "worried", "down", cheeks="blush")
    m "Understandable... but what about getting them to take it a bit easier on you during the game itself?"
    call cho_main("I'm getting to it...", "open", "closed", "worried", "mid")
    call cho_main("I was asking them how much the game meant to them, and what I could do to persuade them to take it easy...", "soft", "narrow", "base", "R")
    call cho_main("They didn't really seem to know what I meant. They just do whatever Draco tells them to do.", "soft", "narrow", "base", "mid")
    m "Sounds like trying to make a cat understand how to bark."
    call cho_main("Exactly...", "annoyed", "narrow", "worried", "R")
    call cho_main("I was a bit frustrated at that point, and running out of options on how I could make my intentions even clear to them...", "soft", "narrow", "worried", "mid")
    call cho_main("So lifted my skirt a bit to show them my panties.", "soft", "happyCl", "worried", "mid", cheeks="heavy_blush")
    g9 "You go girl!"
    call cho_main("Well, there's where I messed up...{w=0.6} They took it as an invitation and squeezed my butt cheeks quite hard and painfully.", "quiver", "narrow", "worried", "mid", cheeks="blush")
    m "Ouch, then what happened?"
    call cho_main("I pushed them away of course! I won't just let them grope me as they please!", "open", "wide", "base", "mid")
    call cho_main("But...{w=0.3} I did tell them right after -- if they're kind to me during the game -- that I'll reward them handsomely for it...", "horny", "narrow", "base", "downR", cheeks="blush")
    call cho_main("Not that I have any intentions to do so...", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Of course not..."
    g9 "And what about the butt squeeze?"
    call cho_main("What about it, sir?", "soft", "wide", "base", "mid", cheeks="blush")
    g9 "Did you like it?"
    call cho_main("Sir! They're Slytherins!", "angry", "wide", "base", "mid", cheeks="blush")
    m "That's not what I asked."
    call cho_main("...", "annoyed", "narrow", "angry", "mid")
    call cho_main("Can I please go now, Sir?{w} I've done what you asked of me.", "soft", "narrow", "angry", "R")
    m "Yes, [cho_name]."
    m "You've done a great job today getting closer to beating those pesky Slytherins."
    call cho_main("Thank you, Sir.", "base", "narrow", "base", "mid")
    m "Make sure they'll remember your meeting during the match, and I'm sure any sort of desire to win -- will wash away."
    call cho_main("*Hmph*...", "horny", "narrow", "base", "downR", cheeks="blush")
    call cho_main("I'll do my best.", "soft", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 9: # Points til 9.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    call cho_main("Sir, I managed to corner their seeker when he came out of the boys bathroom.", "soft", "narrow", "base", "mid")
    call cho_main("One of the only times those thugs weren't hanging around with him.", "soft", "narrow", "base", "down")
    m "Him?"
    call cho_main("Malfoy...", "soft", "narrow", "worried", "mid")
    call cho_main("I cornered him and pushed him back into the bathroom.", "annoyed", "narrow", "base", "R")
    m "That's against the school rules, Miss Chang..."
    call cho_main("But I thought.", "soft", "base", "worried", "mid")
    m "Forget I just said that..."
    g9 "What happened after that point?"
    call cho_main("Oh, well... I asked him if he had ever touched a Quidditch player's ass before.", "soft", "base", "base", "R")
    call cho_main("And before he could answer -- I pushed him up onto the wall, and put his hand around my waist -- right on my butt cheeks!", "base", "narrow", "angry", "mid")
    g9 "Impressive!"
    m "And what was his reaction?"
    call cho_main("At first he was mostly surprised by the circumstance...", "soft", "base", "base", "R")
    call cho_main("But then I clenched my cheeks so he could get a good feel of what a real athlete feels like.", "smile", "narrow", "angry", "mid")
    call cho_main("When that happened he went from surprised to shocked.", "base", "narrow", "angry", "mid")
    call cho_main("You should have seen it.{w=0.6} I was actually not as repulsed as I thought I might be.", "horny", "narrow", "base", "mid")
    call cho_main("It was quite thrilling actually.", "base", "narrow", "angry", "mid")
    m "Why wouldn't you be, you've worked hard on your body."
    m "Now you're starting to see some of the benefits."
    call cho_main("Yeah... yeah you're right!", "soft", "wide", "base", "mid")
    m "And he's not going to forget it.{w=0.6} I'm sure the snitch will be the last thing on his mind during the upcoming game!"
    call cho_main("You know...", "soft", "base", "base", "R")
    call cho_main("You're smarter than I gave you credit for... you've not been wrong so far...", "annoyed", "base", "base", "R")
    g9 "That's why I'm the headmaster."
    call cho_main("Will that be all?", "soft", "base", "base", "mid")
    m "Yes [cho_name], good work today!"
    call cho_main("Thanks!", "base", "base", "base", "mid")
    m "Have a good night..."
    call cho_main("Good night, [cho_genie_name].", "smile", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 9: # Points til 9.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_intro_E2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    m "Back already? How did it go?"
    call cho_main("Not too great this time, [cho_genie_name].", "soft", "narrow", "worried", "R")
    m "No? What happened?"
    call cho_main("Nothing, actually. I didn't see any of their team members all day. Not even at the Quidditch pitch...", "annoyed", "narrow", "worried", "mid")
    m "Odd... Were they hiding from you?"
    call cho_main("I believe they were, Sir...", "soft", "closed", "base", "mid")
    g9 "So, are they afraid of confronting you face to face? Why are they avoiding you?"
    call cho_main("I have reason to believe that they were observing me all day.", "soft", "narrow", "angry", "mid")
    m "They were stalking you?"
    call cho_main("You could say that.", "annoyed", "base", "base", "R")
    call cho_main("I swear I could see Malfoy's blonde head around a corner at one point...", "soft", "narrow", "angry", "downR")
    call cho_main("But when I was about to confront them, I heard them running off...", "soft", "narrow", "angry", "mid")
    call cho_main("Cowards...", "angry", "narrow", "angry", "mid")
    m "I think this is a good thing, [cho_name]!"
    call cho_main("You do?", "soft", "wide", "base", "mid")
    m "The fact that they're following you..."
    g4 "It proves that they are weak!{w} They are obsessed with you!"
    call cho_main("You think so?", "annoyed", "base", "raised", "mid")
    m "Yes! As long as you keep teasing them."
    m "They won't be able to keep focus on anything else..."
    g9 "Except your perfect bod!"
    call cho_main("I'll do my best, Sir.", "base", "base", "base", "mid")
    m "You may go now, [cho_name]. Nice work!"
    call cho_main("Thank you, [cho_genie_name]!", "smile", "base", "base", "R")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 9: # Points til 9.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_intro_E3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    m "[cho_name], how was your day?"
    m "Were you successful this time?"
    call cho_main("Sir, I believe they are onto me!", "angry", "narrow", "worried", "mid")
    m "Who are... they?"
    call cho_main("Malfoy and his gang, Sir.", "soft", "base", "base", "R")
    call cho_main("They confronted me, outside the girl's bathroom.", "angry", "narrow", "worried", "down", cheeks="blush")
    g4 "How very rude of them."
    call cho_main("I'm just glad they didn't follow me inside, actually...", "soft", "base", "worried", "mid", cheeks="blush")
    m "But they're boys! They aren't allowed in there!"
    call cho_main("Don't underestimate them, [cho_genie_name].", "soft", "closed", "base", "mid")
    call cho_main("I doubt that anything would stop them from breaking into a girl's most private place...", "soft", "narrow", "angry", "mid")
    g4 "They are ruthless!"
    m "What exactly did they want from you?"
    call cho_main("They questioned me...", "annoyed", "base", "worried", "R")
    call cho_main("About what I'm up to. What my plan is. Why I'm acting...{w=0.8} strangely.", "soft", "narrow", "worried", "downR", cheeks="blush")
    m "Strangely? In what way?"
    call cho_main("Typically, girls from other houses doesn't talk to boys from Slytherin...", "soft", "happyCl", "worried", "mid", cheeks="blush")
    call cho_main("Not to mention flirt with them!", "mad", "narrow", "worried", "down", cheeks="heavy_blush")
    m "So? What did you do?"
    call cho_main("I panicked, [cho_genie_name]!", "clench", "happyCl", "worried", "mid", cheeks="heavy_blush")
    call cho_main("I tried to get out of the situation, although in my haste the only solution I could think of was to-...", "soft", "narrow", "base", "downR", cheeks="blush")
    m "Yes?"
    call cho_main("Flash them, Sir. I flashed them my breasts!", "soft", "narrow", "worried", "mid", cheeks="blush")
    g9 "Nice!"
    call cho_main("I'm sorry, Sir.{w=0.6} I shouldn't have done it!", "disgust", "narrow", "worried", "down", cheeks="heavy_blush")
    g9 "And what was their reaction?"
    call cho_main("I don't know... They were surprised?", "angry", "wink", "raised", "mid", cheeks="blush")
    call cho_main("I closed my eyes through most of it, and then I ran off...", "soft", "base", "worried", "down", cheeks="blush")
    m "*Hmmm*..."
    call cho_main("Did I go too far, [cho_genie_name]?", "soft", "narrow", "worried", "mid", cheeks="blush")
    g9 "No girl, you did great!"
    m "You successfully got yourself out of an intricate situation."
    m "You improvised, just as I taught you."
    call cho_main("Thank you, Sir.", "base", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("But what would you suggest I do next time something like this happens?", "soft", "narrow", "worried", "mid")
    m "Trust your instincts, it worked once didn't it?"
    m "Try it again. Show them your breasts, and see what effects it has on them..."
    call cho_main("Show them my breasts?! But I can't possibly do that!", "clench", "wide", "base", "mid", cheeks="blush")
    m "Why not? Didn't you just do that?"
    m "They {b}have{/b} seen your tits, haven't they?"
    call cho_main("My tits?!", "soft", "wide", "base", "mid", cheeks="heavy_blush")
    call cho_main("*Oh* I mean yes, I guess they have seen them now but...", "soft", "base", "worried", "downR", cheeks="blush")
    g4 "Remember why we are doing this, girl! You need to get into their minds!"
    m "If they want to see your breasts again, or any other part of your body, you show it to them!"
    call cho_main("But, Sir!", "mad", "closed", "worried", "mid", cheeks="blush") # Embarrassed
    m "Do as I say, [cho_name]!"
    g4 "Your mission, should you choose to accept it, is to please them!{w} No matter the cost!"
    call cho_main("What?!", "soft", "wide", "base", "mid")
    m "For now, you are dismissed."
    call cho_main("Sir!", "angry", "base", "angry", "mid")
    g4 "Dismissed!{w} Now go back to your room..."
    call cho_main("Fine...", "annoyed", "narrow", "angry", "mid") # Annoyed
    call cho_main("Good night, [cho_genie_name].", "soft", "narrow", "angry", "mid") # Angry

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 9: # Points til 9.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_E3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    g9 "[cho_name]! You're back."
    call cho_main("(...)", "annoyed", "narrow", "angry", "down") # Annoyed
    g9 "How was your day? Anything exciting to tell me?"
    call cho_main("I- *uhm*...", "soft", "narrow", "base", "down")
    call cho_main("I did what you asked me to...", "soft", "narrow", "worried", "mid")
    g9 "Yes?"
    call cho_main("I... flashed them...", "mad", "closed", "worried", "mid")
    g4 "You showed them your tits again?!"
    call cho_main("What? No!", "soft", "wide", "base", "mid")
    m "But you just said-"
    call cho_main("They... didn't want to see them...", "annoyed", "narrow", "angry", "downR", cheeks="blush")
    m "Oh..."
    m "(Could it be that they aren't into girls?)"
    call cho_main("I was on my way to the Quidditch pitch, somewhere close to the library when they ambushed me...", "soft", "narrow", "base", "R")
    g4 "An ambush?!"
    call cho_main("I tried to be nice to them, even flirt a bit, but I just couldn't!", "soft", "narrow", "worried", "mid")
    call cho_main("It's hard enough to deal with one of those brutes, but three at the same time?!", "angry", "wide", "base", "mid")
    m "There are girls that could handle that with ease..."
    call cho_main("Sir?", "soft", "base", "raised", "mid")
    m "Nothing... go on..."
    call cho_main("They started mocking me... About what I did last time. Called me a slut, among other things...", "soft", "narrow", "angry", "R")
    call cho_main("Even threatened to report it as indecent behaviour...", "angry", "narrow", "angry", "downR")
    call cho_main("I was about to lash back as they were really starting to annoy me...", "angry", "narrow", "worried", "mid")
    call cho_main("But then I remembered what you told me.", "annoyed", "narrow", "base", "mid")
    call cho_main("That I should do my best to be nice to them... and... try and please them...", "annoyed", "base", "worried", "down")
    m "So? What did you do?"
    call cho_main("I asked if they liked it...", "mad", "happyCl", "worried", "mid", cheeks="blush")
    g9 "Liked what?"
    call cho_main("Seeing my breasts, Sir.", "soft", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("Instead of insulting them, I begged them not to report me to a teacher -- and in return -- I'd let them see them again!", "soft", "narrow", "worried", "R", cheeks="blush")
    g9 "And then?"
    call cho_main("They laughed at me!", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call cho_main("Started mocking my breasts even... Calling them small...", "annoyed", "narrow", "angry", "downR", cheeks="blush")
    m "How foolish those boys..."
    call cho_main("Well, I had to show them something else instead...", "soft", "narrow", "worried", "mid", cheeks="blush")
    call cho_main("After all, they asked for it.", "annoyed", "narrow", "worried", "down", cheeks="blush")
    g4 "Intriguing..."
    call cho_main("They asked to see my bum, Sir!", "soft", "narrow", "angry", "mid")
    g9 "I see, they are men of culture..."
    call cho_main("I turned around and lowered my skirt for them...", "annoyed", "base", "base", "down")
    g9 "Sweet!"
    m "And how did they react to it?"
    call cho_main("It seemed like they enjoyed it, Sir.", "soft", "closed", "base", "mid")
    call cho_main("I mean, who wouldn't... I have a great butt.", "soft", "narrow", "angry", "R")
    m "Yes indeed!"
    call cho_main("They did ask why I keep wearing a skirt to school, though.", "annoyed", "base", "raised", "mid")
    call cho_main("Said that it would look a lot better in trousers...{w=0.6} or some tight leggings...", "annoyed", "base", "base", "downR")
    m "They're not wrong... you would look great in some leggings!"
    call cho_main("Anyway, I left before they had a chance to touch it...", "annoyed", "narrow", "base", "mid")
    call cho_main("The last thing I want is their grimy hands on it.", "annoyed", "narrow", "angry", "R")
    m "Well, I believe you made the best out of the situation!"
    call cho_main("I think so too, [cho_genie_name]!", "base", "base", "base", "mid")
    g4 "You may leave now. Exceptionally good work, [cho_name]!"
    call cho_main("Thank you.", "smile", "base", "base", "R")
    m "Dismissed."
    call cho_main("Good night, Sir.", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 9: # Points til 9.
        $ cho_reputation += 1

    jump end_cho_event

### Tier 3 ###

# Intro:
# Cho meets Harry.
# Che meets Ginny. Ginny is teasing Cho actually and she's embarrassed about it.

# Random/Repeatable:
# Cho again tries to flaunt Harry. Maybe he could compliment her ass?
# Ginny watches her while doing squads.They have a little Chat. Ginny reveals that she likes Cho.

label cc_pr_manipulate_boys_T3_twins:

    # Setup
    $ cho.strip("all")
    $ cho.set_body_hue(200)

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    m "Back so soo-..."

    call cho_main(face="angry", xpos="mid", ypos="base", trans=fade)

    menu:
        "-*Ha-ha-ha-ha*-":
            g9 "{i}I'm blue, daba dee bada die, {size=-2}daba dee daba die,{/size} {size=-4}daba dee bada die,{/size} {size=-6}daba dee daba die........{/size}{/i}"
            cho "*glares daggers*"
            m "*Ahem*.. I meant to ask, what happened?"

        "-Feeling blue today?-":
            cho "Oh? What gave it away?" # Rolling eyes
            cho "Was it the grimmace on my face?" # Obviously sarcastic
            g9 "Something like that."
            m "So, what happened?"

        "-What the hell happened?-":
            g4 "You look like a blueberry!"
            m "Or a bilberry!"
            g9 "Or a gummiberry!"
            g9 "Or maybe even a-"
            cho "Could you start acting serious for just a moment?!"
            g9 "I'm berry serious."
            cho "*urghhhh*! I can't believe you!" # Angry noises
            m "Alright, alright. Tell me what happened."

    cho "What does it look like what happened?"
    g9 "Well, to me it looks like you caught a case of the smurfs."
    cho "Those bloody twins!"
    cho "They tricked me into eating one of their darn sweets!"
    cho "You should lock those two up..."
    g9 "I wish I could’ve been there..."
    cho "WHAT?"
    g4 "To stop them I mean!"
    cho "..."
    m "So, why did you come straight to me and not go to your dorm?"
    cho "And pass through my common room?"
    cho "No thank you... your office was the closest thing to their stupid shop."
    if not store_intro_done:
        m "Shop? What shop?"
        cho "Are you kidding me? Surely you must know about them and their shady businesses."
        m "I have no clue what you're talking about."
    cho "..."
    cho "Don’t you have any spare robes or anything?"
    m "I suppo-"

    menu:
        m "(Actually, I might not get another opportunity like this...)"
        "-Let her deal with it-":
            m "You’ll figure something out."
            cho "What!"
            cho "You want me to just go out there without any clothes on?"
            m "Of course... seems like a great exercise."
            cho "Exercise? How is this an exercise to you?"
            m "An exercise in confidence miss Chang."
            cho "You have got to be joking..."
            cho "So, you’re not going to help me?"
            m "This one’s on you Miss Chang."
            cho "*Grrrr* Whatever..."

            # Cho leaves.
            call cho_walk(action="leave")

            $ cho_mood += 20

            m "She sure is a feisty one..."

        "-Offer to fetch her something-":
            call cc_pr_manipulate_boys_twins_branch


    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    $ cho.wear("all")
    $ cho.set_body_hue(0)

    jump end_cho_event

label cc_pr_manipulate_boys_T3_ron:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Mission success?"
    m "Did you manage to sneak up on Rob?"
    cho "Yes! It could not have gone better!"
    m "Great, let’s hear it."
    cho "I found the perfect opportunity to approach him after practice as Hermione was arguing with Madam Hooch about some rule or another. "
    cho "So as she was busy, I went up and praised him on his excellent goal keeping."
    cho "He was quite taken aback by this at first and I doubt he ever recie-"
    m "Surely you didn’t just compliment him... That won’t be enough to annoy Miss Granger!"
    cho "Of course not!"
    cho "The goal was for him to check me out... Which I soon caught him doing."
    m "That boy could do with some lecturing!"
    cho "I know!"
    m "Getting caught checking someone out that quickly..."
    cho "Right..."
    cho "Anyhow, it was if he was trying to stare through my clothing and he was barely paying any attention."
    m "Been there, done that..."
    cho "Yeah, no wonder Hermione is so annoyed at him all the time..."
    cho "It was at that point Madam Hooch turned and walked away from Hermione."
    cho "So without any warning I grabbed and planted Rons hands on my breasts."
    m "Nice..."
    cho "He was so taken aback by this he just froze."
    cho "You should’ve seen Hermione’s expression as she turned and noticed us! It was if someone had flipped a switch in her brain."
    m "Jealousy no doubt..."
    cho "Yeah right, as I said there’s no way anything is going on between those two."
    m "I wasn’t talking about...{w=0.4} Never mind..."
    m "Please, continue..."
    cho "Before I could even blink she has rushed up next to us..."
    cho "And then she smacked Ron right across the face!"
    g9 "*Hah*!"
    g4 "I mean... How could she hit another student like that?!"
    cho "You don’t have to pretend that you care..."
    m "I don’t."
    m "What happened next?"
    cho "She dragged him away, yelling her head off the whole time."
    cho "I wouldn’t be surprised if she’s still going." #smirk
    m "Excellent work!"
    cho "Thank you." #blushes
    m "Hopefully we can remind her about this during the game, spark that jealousy once more."
    cho "If it annoys Hermione then I’m all for it..."
    m "Anything else to report?"
    cho "No, that’s about it."
    m "Great, then that will be all for today."
    cho "..." #giggles sound
    cho "Good night then..."
    m "Good night Miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_boys_T3_harry:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Welcome back, mission success?"
    cho "Yes!"
    cho "I’ve been stalk... eh... following them the entire day today and found a good opportunity as they came out from divination."
    cho "I was flying outside the divination tower and Harry Ron and Hermione were talking at one of the windows."
    cho "Ron and Hermione had their backs turned towards me but I managed to grab Harry’s attention."
    m "Nice, gave him a bit of a show then I presume?"
    cho "Of course..." #smirk
    cho "And I found something out."
    cho "That boy has a broom fetish!"
    m "A what?"
    cho "Broom fetish... it’s when a girl plays with herself using a broom."
    m "Oh... that makes more sense."
    cho "So as I hovered in the window I stuck my tongue out and moved my hips against the wood."
    m "You stuck your tongue out?"
    m "Wasn’t it Hermione that you were going to antagonize?"
    cho "Not like that!"
    cho "I mean in a seductive way!"
    m "Like how?"
    cho "Like this!"
    cho "..." #Cho sticks her tongue out and eyes look seductive."
    m "Whoa!"
    cho "*U ikhe*?" #Tongue still out
    m "Very much... So what was his reaction?"
    cho "Much like Ron he couldn’t focus on their conversation and Hermione soon followed his gaze and noticed me out the window."
    cho "And after staring daggers at me she yanked the boys away by their robes almost making them tumble down the stairs."
    m "Looks like you have her well jealous at this point!"
    m "Hopefully this should be enough to affect her during the finals."
    cho "Let’s hope so..."
    cho "If that’s all I’ll head off for today."
    m "Yes, that will be all."
    cho "Good night then."
    m "Good night, Miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event


label cc_pr_manipulate_boys_twins_branch:
    # Genie visits Mafkin store to fetch some outfit for Cho

    if clothing_store_intro_done:
        m "Madam Mafkin should be able to sort you out."
        cho "Mafkin? Don’t you mean Malkin?"
        m "Pretty sure it’s Mafkin."
        m "I’ll go and check with her and see if there’s anything she can spare for the moment..."
    else:
        m "Surely this place has some sort of seamstress."
        cho "I guess..."
        m "I’ll go and check with her, see if there’s anything she can spare for the moment..."

    cho "Please..."
    cho "I just hope this colour will fade before you get back..."
    #Genie walks past Cho to the door and turns to her, she turns as he stops
    m "I don’t really see why it’s such an issue."
    m "I’ve been known to turn blue and swell up as well and you don’t see me complaining."

    #Cho question mark chibi
    #Genie exits the room

    # SHOW CLOTHING STORE

    if clothing_store_intro_done:
        ">You enter to see an old woman busy sewing together two pieces of long dark fabric."
        ">The woman is dressed almost entirely in pink and has a warm, approachable air to her."

        m "Hello."
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        m "Neither thank you, I'm just here to make a few inquiries."
        maf "Of course sir, what can I help you with?"
        m "Firstly, what type of items do you sell?"
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        m "I see. Do you ever make custom orders?"
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        m "So you're interested in making unique outfits?"
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colours at the moment."
        maf "What did you have in mind?"
    else:
        m "Miss Mafkin... or was it Malkin?"
        maf "It’s Mafkin, Dumbledore... we have been over this before."
        m "I knew she was wrong!"
        maf "Anything I could assist you with?"
        maf "I just got this new plaid fabric in that I was thinking of turning into a kilt."
        maf "It’s the perfect garment for letting the family jewels get some fresh air."
        m "I’m good thank you."
        maf "Then what can I do you for?"

    m "Well... As it happens..."
    m "I’m in quite a pickle... A student was tricked into eating one of the weasel twins’ sweets."
    maf "A sweet?"
    m "Yes, or a candy... whatever you’d call it."
    m "The sweet in question made her turn blue and swell up like a balloon, ruining her clothes in the process."
    maf "I see... that’s an unfortunate situation indeed."
    m "So I require a Female Ravenclaw school uniform."
    maf "Let’s see...{w=0.5} Female Ravenclaw uniform...{w=0.4} Looks like I’m running a bit low on those at the moment, what size is she?"
    m "She’s a B."
    maf "She’s a... B, sir?"
    m "No no, she’s a Human. That’s her size."
    maf "I require her clothing measurements..."
    m "Oh, I see..."
    maf "Or the name of this student, If I’ve had her fitted before I’ll have it stored in my records."
    m "Cho Chang."
    #paper sound
    maf "Cho Chang..."
    maf "Ah yes, here she is..."
    maf "Well, that’s unfortunate..."
    m "You don’t have any clothing her size?"
    maf "I do, but none in Ravenclaw colours."
    maf "She might have to go with one of the other house colours for now until I can get these ones fitted for her."
    m "That sure is unfortunate."

    # Setup
    $ d_flag_01 = False
    $ d_flag_02 = None

    label .choices:

    menu:
        m "In that case I’ll have the..."

        "-Slytherin outfit-":
            $ d_flag_02 = 1

            maf "Are you sure?"
            m "Absolutely, she’ll look great in green!"
            m "But just so I know... how long will it take to get the Ravenclaw outfit ready?"

        "-Gryffindor outfit-":
            $ d_flag_02 = 2

            maf "Are you sure?"
            m "Of course!"
            m "She’s best friends with Miss Granger so I’m sure she wouldn’t mind."
            m "But just so I know... how long will it take to get the Ravenclaw outfit ready?"

        "-Hufflepuff outfit-":
            $ d_flag_02 = 3

            maf "Are you sure?"
            m "Seems like the safest option all things considered."
            m "How long will it take to get the Ravenclaw outfit ready?"

        "-Take the Smurfette Outfit-" if d_flag_01:
            $ d_flag_02 = 4

            maf "Are you sure?"
            m "Of course!"
            g9 "It looks as if it was made just for her."
            maf "Well, you're the judge here."
            m "One more thing, how long will it take to get the Ravenclaw outfit ready?"

        "-Ask for another option-" if not d_flag_01:
            # Genie finds a smurfette costume
            $ d_flag_01 = True

            m "I don’t think she’d be so keen on wearing another house’s colours."
            maf "Well, I don’t recommend it but if that’s the case you can have a look through the pile over there."
            maf "I have a few miscellaneous pieces lying around that she could borrow for the time being."
            maf "There’s not a lot to pick from, but you can take anything you need from it."
            m "Great."
            # Rummage sound.
            m "Hmm, doesn’t seem to be a lot to pick from..."
            # Rummage sound.
            m "What would she fit well in..."
            # Rummage sound.
            m "Hold on a second."
            # Rummage sound.
            m "(Oh, this is just perfect... Although perhaps it’s a bit mean..."
            m "Maybe I should just ask for one of the other house’s clothing pieces instead..."

            jump .choices

    maf "I’ll have it done and delivered by tomorrow morning."
    m "Great, that will be all then."
    maf "Until next time..."

    #Back in Office
    #Genie Walks in
    m "I’m back!"
    cho "Finally!"
    cho "I’ve been freezing my butt off and I couldn’t figure out how to light the fire."
    m "Can’t you use some spell for that?"
    cho "Where do you think I keep my wand?"
    m "Well, most people hide it in their night stand or a drawer or something."
    cho "It’s probably at Fred and George’s still..."
    cho "So, where’s that outfit you were fetching for me?"

    if d_flag_02 == 1:
        # Slytherin

        m "Got it right here, brings out the colour of your eyes for sure!"
        cho  "Such a charmer..."
        #Clothsound
        cho  "Oh, good. You managed to get some school uniforms."
        cho  "I was worried that you’d pick out something-..."
        cho  "These are Slytherin colours!" #big text yelling
        m "They are?"
        m "That’s unfortunate!"
        cho "Why did you assume it would be a good idea...."
        cho "To get Slytherin colours!" #big text yelling
        m "She didn’t have any spare Ravenclaw outfits."
        cho "But why Slytherin..."

        menu:
            "-If you don’t like it you can go without any!-":
                cho "What!"
                m "You heard me..."
                m "I went out of my way to fetch those clothes for you..."
                m "So you can take your smurf looking ass and get out of my office."
                cho "Fine!"
                #Cho storms out
                #Mood very angry

            "-It’s not my fault, Some idiot picked that option!-":
                cho "What?"
                m "It was decided by some unknown external force."
                cho "That doesn’t make any sense!"
                m "I know!"
                cho "..."
                #Cho’s colour changes to normal
                cho "I thought you would know better than to pick a Slytherin uniform for me..."
                m "As I said, not my fault."
                g9 "Although, speaking of colour..."
                m "You’re not blue anymore."
                cho "Thank Merlin for that..."
                cho "Just hand me those clothes..."
                #Cloth sound
                #Clothes equipped
                cho "..."
                cho "This feels wrong..."
                g9 "I knew it!"
                g9 "You look great in green!"
                cho "*Grrr*... I can’t believe you!"
                #Cho storms out
                #Mood angry

            "-Sorry...-":
                cho "..."
                cho "(Well that’s a first...)" #taken aback
                m "Sorry for going out of my way to help you!"
                #Exasperated but not angry
                cho "*Sigh*"
                cho "Why did you think it would be a good idea to pick Slytherin colours..." #pout
                m "As I said, I thought they’d compliment your eyes..."
                cho "..."
                cho "Fine, since you almost apologized..."
                cho "Hand me those clothes."
                #Cloth sound
                #Clothes equipped
                m "See, they don’t look that bad!"
                cho "This feels wrong..."
                m "You look great in any colour!"
                cho "That’s not why..."
                #Cho’s blue colour fades away
                cho "Thanks I guess."
                m "Speaking of colour..."
                m "You’re not blue anymore."
                cho "Finally..."
                cho "Hopefully everyone’s gone to bed by now and I can sneak my way past without anyone noticing."
                cho "So what do I do about my normal uniform?"
                m "I’ve sorted it, Mafkin will have a new set delivered to your room in the morning."
                cho "Oh..."
                cho "Thanks..."
                cho "Good night then."
                #Cho leaves
                #Mood Slightly mad

    elif d_flag_02 == 2:
        # Gryffindor

        m "Got it right here!"
        m "She didn’t have any Ravenclaw uniforms your size so I took the next best thing."
        cho "Next best-"
        cho "Is that a Gryffindor uniform?" #shocked
        g9 "Yes, I knew you’d like it!"
        cho "I...{0.5} I don’t like Gryffindor!"
        g4 "What... but I thought Hermione was like your bestie."
        cho "Bestie?"
        cho "She...{0.4} is...{0.4} not!"
        m "Oh..."

        menu:
            "-I could go back and fetch the Slytherin one instead-":
                cho "No!"
                cho "I mean... that’s fine... you’ve already gone out of your way."
                m "You sure? It’s not that far-"
                cho "Yes... just hand me the clothes."
                #Cloth sound
                #Clothes equipped
                cho "..."
                cho "I guess it’s not that bad..."
                cho "What do you think, do I pull off the red as well as...{w=0.6}Do I pull off the red?"
                m "Looks great!"
                m "They look a bit tight around the chest area, did I end up with a size too small?"
                cho "Oh... no, it’s fine... I’m just a bit cold still." #Embarrassed
                m "You do look a bit blue..."
                cho "Wait, I’m still..."
                #Cho’s blue colour fades away
                cho "Thank Merlin..."
                cho "I’ll be on my way then..."
                #Cho Walks to the door
                cho "..."
                cho "Good night..."
                #Cho leaves
                #Cho Mood stays the same
            "-I’m sure none of the Gryffindors will spot you-":
                cho "If that’s the case then why wear any clothes at all?"
                m "That is an option..."
                cho "No!"
                cho "Give me those..."
                #Cloth sound
                #skirt equipped
                m "Actually, can I change my mi-"
                #Clothes equipped
                cho "No no, we’re good!"
                m "But could you at least-"
                #Cho hurriedly walks to the door
                cho "Nope, these will have to do..."
                cho "Have a good night!"
                m "Come ba-"
                #Cho exits the room
                m "Damn...{w=0.4} well at least she isn’t angry."
                #Cho Mood stays the same

    elif d_flag_02 == 3:
        # Hufflepuff

        m "Got it right here!"
        m "She didn’t have any Ravenclaw uniforms your size so I went wish something mellow."
        cho "Mellow?"
        cho "Wait you don’t mean..." #Worried
        cho "A Hufflepuff uniform!" #Shocked
        m "Sure is, I remembered how you can’t get enough of those badgers!"
        cho "I only dated one of them when the Tri-wizard tournament was happening..."
        cho "And as you remembered, I used it to our advantage to win the match against them."
        m "Sure did!"
        cho "So, don’t you think the Hufflepuffs would assume Cedric threw the match on purpose or start asking questions if they suddenly saw me wearing this?"

        menu:
            "-So what?-":
                cho "So what?!?"
                m "You didn’t have any problems using his weaknesses during the game so why do you care if he gets in trouble with his house?"
                cho "That’s different..."
                m "How is it different?"
                m "I’m sure his teammates weren't happy with him losing focus like that... fraternizing with the enemy..."
                cho "..."
                m "They might already think he threw it on purpose."
                cho "Whatever, just give me the clothes."
                #Cloth sound
                #Clothes equipped
                cho "I can’t believe you turned this around on me like that... you’re the one that made me do those things to begin with..."
                m "Don’t hate the player, hate the game."
                cho "..."
                cho "I’m leaving."
                #Cho leaves
                #Mood Slightly mad

            "-That’s true, maybe you should just head back naked...-":
                cho "What!"
                m "You heard me, make like a bee and buzz off!"
                g9 "And you better hurry up before those sweets wear off or you’ll find it even harder to explain your current state."
                cho "But... surely you can’t be serious!"
                m "I am neither Shirley nor Sirius..."
                cho "*Grrr*... I can’t believe you!"
                #Cho Walks to the door and turns around
                cho "..."
                m "Tick-tock..."
                cho "Fine!"
                #Cho leaves and slams the door
                #Mood very angry

            "-I’m sure none of the Hufflepuffs will spot you-":
                cho "How can you be so sure about-"
                cho "Actually, you’re probably right... you’re a genius!"
                g4 "I am?"
                cho "Of course!"
                cho "You know this castle inside and out and it’s very unlikely any of the Hufflepuffs would be anywhere near the route to the Ravenclaw dorm."
                g9 "Oh yes... that’s it!"
                m "You know me, always got an ace up my sleeve!"
                #Cho’s blue colour fades away
                cho "Thank you [cho_genie_name]..."
                g9 "Of course!"
                g9 "And look at that. You’re not blue anymore!"
                g9 "Also your skin is back to normal."
                cho "Very funny..." #smile
                #Cloth sound
                cho "Let’s try this on then..."
                #Clothes equipped
                cho "So, how do I look?"
                m "Looking good!"
                cho "I better be off then..."
                cho "Good night."
                m "Good night, [cho_name]."
                #Cho leaves
                #Mood stays the same

    elif d_flag_02 == 4:
        # Smurfette

        m "Got it right here."
        cho "Thank you, I knew I could count on-"
        cho "What is this?"
        g9 "I know!"
        g9 "I couldn’t believe it when I found it. The perfect outfit for you!"
        cho "You... are you serious? You actually expect me to wear this?"
        m "Wait, don’t tell me you don’t like it?"
        cho "..."
        cho "Why couldn’t you pick up a normal school uniform like I asked you to?"

        m "Just put it on already."
        cho "..."
        m "Or you could just head back naked!"
        cho "Fine!"
        #Black screen, cloth rustle
        #Cho is now wearing the Smurfette outfit.
        m "Smurfabunga!"
        cho "..." #Looking livid #red cheeks
        m "I think some colour has started to return on your cheeks!"
        m "I also got you this wig."
        cho "I am not wearing the wig!"
        cho "I can’t believe you!"
        #Cho leaves and slams the door

        # Outfit unlock message

    return
