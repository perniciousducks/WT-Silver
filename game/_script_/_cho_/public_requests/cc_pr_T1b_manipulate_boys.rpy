

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
    else:

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
                    call cho_main("*cough*{w=0.6} *guargh!*{w=0.8} *cough*", "open_wide_tongue", "happyCl", "worried", "mid", cheeks="blush", trans=hpunch)
                    call nar(">You hear Cho make some inadvertent gag noises...")
                    m "Is everything okay, girl?"
                    call cho_main("No!{w=0.3} It's not ok!", "angry", "wide", "worried", "mid", cheeks="blush")
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
