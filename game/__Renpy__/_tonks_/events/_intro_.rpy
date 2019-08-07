

### Tonks Intro ###

label tonks_intro_E1:

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "(...)"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "(Can't I even have one quiet day here?...)"
    m "Who is it?"
    ton "It’s Tonks-"
    ton "*Ugh*..."
    m "..................."
    ton "I meant, Nymphadora Tonks, Sir."
    m "(Nympho...{w=0.6}what?)"
    ton "Ministry of Magic, Auror division.{w=0.8} May I come in, Sir?"

    if letter_favor_complaint_OBJ.read:
        g4 "(Oh shit, the fuzz!!!)"
        m "(I thought they would have forgotten about those damn letters by now...)"
        ton "Sir, I’m here to discuss an important matter with you regarding your students."
        m "(Governments are all the same with their bloody rules.)"
        ton "Sir?"
        m "(...)"
    else:
        m "(Another female?)"
        m "(She sounds a bit too old to be a student...)"
        m "(...)"

    menu:
        m "(Should I let her in?)"
        "\"Please, come on in.\"":
            g9 "(Better to just let my charm play...)"
        "\"Not right now.\"":
            ton "But, Sir."
            ton "I've traveled half the country just to get here."
            m "........................."
            ton "Via apparation, of course. It only took me a couple of seconds..."
            ton "But still, It's quite a long walk up here from Hogsmeade..."
            ton "I'd just like to get this over with. May I come in, Sir?"
            m "(I wouldn't mind having a look at her...)"
            m "(There is something special about women in uniform...)"
            ton "Sir?"
            m "*Uhm* Yes, you may enter..."

    call play_sound("door")

    #Tonks walks in

    call ton_main("Thank you, Professor.","base","base","base","mid", xpos="right", ypos="base")
    m "(Oh shit, she’s hot...)"
    call ton_main("I apologize for arriving unannounced...{w=0.8} And a couple of days late...","open","base","base","R")
    g9 "Please, I'm glad you could make it."
    call ton_main("I was occupied with some unfinished Ministry-business,... Took me a lot longer to solve than I had anticipated...","open","base","base","mid")

    call ton_main("I had quite the \"pleasant\" encounter with a group of centaurs.","open","base","worried","R")
    m "Centaurs?!"
    call ton_main("*Mhmm*...","base","base","base","mid", hair="horny")
    call ton_main("As usual, they went outside the territory which was assigned to them by the ministry.","open","base","base","mid")
    call ton_main("I had to get them to comply with our rules, to the best of my abilities...","base","base","base","mid")
    m "Is that so?..."

    menu:
        "-Start jerking off!-":
            $ masturbating = True
            $ jerked_off_during_tonks_intro = True
            g9 "Tell me more!"

        "-Pay attention.-":
            $ masturbating = False
            $ jerked_off_during_tonks_intro = False
            m "Tell me about it..."

    if masturbating:
        call ton_main("Oh,...about the centaurs?","open","base","worried","mid")
        m "Yes, centaurs!"
        g4 "Half of a man, and the other half that of a horse?"
        call ton_main("Yes?","base","base","raised","mid")
        m "With the bottom half being that of a{w=0.2}.{w=0.2}.{w=0.2}.{w=0.6}horse?!"
        call ton_main("Of course, Sir.","base","base","base","mid")
        g9 "(Sweet!)"
        m "Just wanted to check if I still knew my mythology..."
        g4 "(And it wasn't just dudes with horse-heads...)"
        m "(That would have been weird...)"

        call hide_characters
        hide screen bld1
        with d3
        pause.2

        call gen_chibi("jerking_off_behind_desk")
        with d3
        pause.8

        call nar("You take out your cock and start jerking off.")

        call ton_main("They are fascinating creatures, aren't they, Professor?","base","base","base","R")
        m "What?{w} Oh yes, very fascinating..."

        call nar(">*Fap!* *Fap!* *Fap!*")
        m "Don't mind me... Please continue..."
        g9 "I'd like to hear more about the things you did with those centaurs!"
        call ton_main("I'm sorry Professor, but that's classified information.","open","closed","worried","mid")
        call ton_main("The Ministry would be furious if they knew that I've told you!","open","base","worried","mid")
        call ton_main("(Not that I'd mention any of it... They'd probably have me sacked on the spot if they knew...)","angry","base","worried","R")
        call ton_main("(I did the job. That's all that should matter to them...)","upset","base","base","down")
        g4 "Come on!..."
        call ton_main("I'm sorry, Professor, but I really shouldn't!","open","base","base","mid")
        call ton_main("And sharing stories is not why I came here.","base","base","base","R")
        m "(Balls...)"

        # Stop Masturbating
        $ masturbating = False
        call hide_characters
        hide screen bld1
        with d3
        pause.2

        call gen_chibi("sit_behind_desk")
        with d3
        pause.8

    else:
        call ton_main("Of course, Sir.","base","base","base","mid")
        call ton_main("I had to make a compelling offer so they'd peacefully return to their assigned territory, which isn't easy...","open","base","base","mid")
        m "(...)"
        call ton_main("You'd never be able to guess how I did it... It's quite the story.","horny","base","base","R", hair="horny")
        call ton_main("However, I wouldn't be able to tell you, sadly...{w} Strictly confidential Ministry knowledge...","base","base","raised","mid")
        m "(Why? Did she suck them off?)"
        call ton_main("Okay then, let’s get this over with.","base","base","base","mid")

    call ton_main("Professor Dumbledore, are you aware of why the Ministry has sent me here?","open","base","base","mid")

    if letter_favor_complaint_OBJ.read:
        m "More or less..."
        call ton_main("We have received a letter by a certain \"Miss Hermione Granger\", about ongoing favour trading at this school.","open","base","base","mid")
        m "Yes she very much enjoys doing that..."
        call ton_main("Trading favours?","base","base","raised","mid")
        m "(I wish...)"
        m "No. She enjoys writing letters...{w} lots of 'em..."
    else:
        m "I can’t say that I am."
        call ton_main("So you haven't had any complaints from students in regards to \"favour trading\"?","open","base","raised","mid")
        g4 "(Oh, fuck...)"
        g9 "That depends...{w=0.3} What sort of favours are you referring to?"
        call ton_main("...","base","base","angry","mid")
        call ton_main("Well, we’ve received a letter from \"Miss Hermione Granger.\"","open","base","base","L")
        m "Oh, good..."
        g4 "..."

    call ton_main("I take it you’re acquainted with Miss Granger?","open","base","base","mid")
    m "Quite..."
    call ton_main("Fantastic! Let's get right to it then!","smile","base","base","mid")
    call ton_main("Now, to address the concerns this student has presented to the ministry.","base","base","base","mid")
    m "..."
    show screen blktone
    m "(I need to be smart about this...)"
    hide screen blktone

    menu:
        m "..."
        "\"I never even touched her!\"":
            call ton_main("Sir?","open","wide","wide","wide")
            call ton_main("I'm sorry Professor, I wasn't accusing you of-","open","base","sad","mid")
            m "I did not have sexual relations with that woman."
            call ton_main("Professor! I wasn't implying that-...","angry","base","raised","mid")
            call ton_main("In the letter she wrote, Miss Granger never accused you of selling favours to your students...","open","base","base","L")
            call ton_main("Nonetheless, she was very persistent that certain other teachers weren't behaving as adequately...","open","base","base","mid")

        "\"What did she want?\"":
            call ton_main("Miss Granger wrote about several students, most commonly girls of the \"Slytherin-house\", that were inquired to do favours for their male teachers.","open","base","base","R")
            m "So what?"
            call ton_main("According to her letter, those favours tend to be of very \"sexual\" nature...","base","base","raised","mid", hair="horny")

    m "(Shit...)"
    call ton_main("Professor, if a student engages in sexual acts with their teachers, consensual or not, don't you think it would be of the Ministry's best interest to stop it?","open","base","raised","mid")
    m "..........................................{w} No?"
    call ton_main("I'm sorry?","upset","base","raised","mid")
    g4 "Well, I can’t say I’m very well versed in these...{w=0.8} very,{w=0.6} very rare occurrences."
    m "I was actually just about to begin my own investigation in the matter."
    call ton_main("The Ministry has sent me specifically to investigate, in case there is any truth to Miss Granger's concerns...","open","base","base","L")
    call ton_main("I’ll be happy to look into this for you.","base","base","base","mid")
    m "Now, now. I wouldn't want you to waste your time with this."
    call ton_main("Investigating is in my job description, after all...","base","base","angry","mid")
    call ton_main("I’ll just stay for a little while to investigate the claims and question the students.","open","base","base","R")
    m "That shouldn’t be necessary."
    call ton_main("Do have some confidence in me, Professor. This is what I was trained for...","horny","base","base","mid")
    m "................................."
    call ton_main("I’ve already gotten a room down in Hogsmeade.","open","base","base","R")
    call ton_main("I’ll be staying there, so no worries about accommodations.","base","base","base","mid")
    m "Great..."
    call ton_main("I will begin the investigation right away!","base","happyCl","base","mid")
    call ton_main("Good day to you sir.","base","base","base","mid")

    # Tonks leaves.
    call play_sound("door")
    call hide_characters

    call bld
    m "This can't be good..."

    $ snape_busy = True

    $ tonks_intro.E1_complete = True
    # Don't add event pause here!

    jump main_room


label tonks_intro_E2:

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    ton "Professor, it’s Tonks."
    ton "May I come in?"
    m "(Her again...)"

    menu:
        m "(...)"
        "\"Come in...\"":
            pass

        "\"Not now, I'm busy!\"":
            call bld
            ton "But Sir, I need to tell you about my current investigations!"
            m "That will have to wait, I'm afraid..."
            ton "Please, hear me out, Professor!"
            ton "The students have been very cautious to even speak about the \"favour trading\" in my presence, which I find very odd."
            ton "You'd think that if those girls were innocent, they'd be telling me about it."
            m "....................."
            ton "Be that as it may, I believe that with time, they will all eventually open up to me..."
            m "Good for you..."
            ton "Or they will, as soon as I can get my hands on some \"Veritasetum\"!"
            ton "But Professor Snape has been very reluctant to provide me with a vial of his..."
            ton "{size=-4}Very suspicious if you ask me... Very suspicious indeed...{/size}"
            ton "Either way, it's only a matter of time until this will all be cleared up!"
            m "Great! I can't wait to hear about it..."
            ton "Of course, Sir."
            ton "I'll gladly spare some of my time and tell you right now, if you don't mind."
            m "Wait, what?"
            ton "I'm coming in..."
            g4 "(Shit!)"

    call play_sound("door")

    call ton_main("Professor.","base","base","base","mid", xpos="right", ypos="base")
    m "Hey! If it isn't..."

    menu:
        m "(What was her name again?...)"
        "\"Tonks!\"":
            pass
        "\"Nymphadora!\"":
            call ton_main("Sir?","angry","base","worried","mid")
            m "What? Isn't that your name, or did I get it wrong again?"
            call ton_main("I'm sorry, Sir.{w} I thought that, when I was a student here, that I made it very clear that I wouldn't want to be called Nymphador-","open","base","sad","down")
            call ton_main("Please, just call me Tonks, Professor.","base","base","base","mid")
            m "Fine..."
        "\"Nympho-whora!\"":
            call ton_main("What?!","open","wide","wide","wide")
            call ton_main("I'm sorry, Professor. I clearly must have misheard you...","open","closed","angry","mid")
            call ton_main("Sir, what did you just call me?","angry","base","angry","mid")
            m "*Uhm*...{w}wasn't that your name?"
            call ton_main("My name is \"Tonks\", Professor!","upset","base","angry","mid")
            call ton_main("You of all people should know this...","upset","base","angry","R")
            m ".............."
            m "(Tonks...)"
            m "(Still a weird fucking name...)"

    m "Found any evidence yet?"
    call ton_main("Sadly no, Professor.","open","base","base","mid")
    call ton_main("I haven't gotten a chance to do my job properly so far.","upset","base","base","mid")
    call ton_main("I’ve been rather occupied listening to Miss Granger's own investigations...","open","base","base","R")
    call ton_main("That girl sure is something, isn't she?","base","base","base","mid")
    call ton_main("Not that I mind listening to her.","horny","base","base","R", hair="horny")
    call ton_main("She gave me a very long report that went well into the evening, whilst I enjoyed a glass of firewhiskey...","open","base","base","mid")
    call ton_main("She has been very thorough in documenting the happenings she's witnessed...","base","base","base","mid")
    m "I can imagine that..."
    call ton_main("Anyhow... Other than her documentation, she had no proof of any illicit activities.{w} It's all just accusations.","open","base","base","R")
    call ton_main("As much as I wish they were true...","horny","base","base","R", hair="horny")
    m "Huh?"
    call ton_main("So I could conclude my investigations early, of course...","base","closed","worried","mid")
    call ton_main("And bring this favour trading business to an end, once and for all.","base","base","base","mid")
    m "Best of luck with that..."
    call ton_main("Thank you, Professor.","base","base","base","mid")
    call ton_main("I really should get going.{w} Lots that needs to be taken care of.","open","base","base","R")
    m "Don't overwork yourself..."
    call ton_main("I won't Professor.{w} Have a good night.","base","base","base","mid")

    # Tonks leaves.
    call hide_characters

    call bld
    m "Shit..."
    m "I better talk to Snape about this..."

    $ tonks_intro.E2_complete = True
    $ nt_event_pause += 1

    jump main_room


label tonks_intro_E3:

    call bld
    call play_sound("knocking")
    "*Knock-knock-knock*"

    call play_sound("knocking")
    "*Knock-knock-knock*"

    m "............"
    call play_sound("knocking")

    ton "Professor Dumbledore, may I come in?"
    m "(It's that hot Ministry chick again...)"

    menu:
        "Yes, please come on in.":
            pass
        "Not right now.":
            ton "But it's urgent, Sir. I need to talk to you about Miss Granger's favour trading accusations..."
            g4 "(Shit. That can't be good.)"
            m "Do you mind coming another time, I’m very busy...{w} watering the bird."
            ton "Watering what?"
            ton "Sir, I’m coming in."
        "Who is it?":
            ton "It's Tonks."
            m "Who?"
            ton "..."
            ton "Nymphadora Tonks..."
            m "(That Nympho again...)"
            ton "Sir, I’m coming in."

    #Tonks enters the office
    call play_sound("door")

    call ton_main("Professor...","base","base","base","mid", xpos="right", ypos="base")
    m "How’s the investigation going? Nothing to report I gather?"
    call ton_main("On the contrary...","open","wide","wide","wide")
    call ton_main("It's worse than I could have ever imagined!","open","base","angry","mid", hair="angry")
    g4 "(........)"
    call ton_main("This school truly has changed since I was a student here.","open","base","base","mid")
    call ton_main("I never thought I would see Hogwarts in a state such as this...","open","base","angry","down")
    call ton_main("Corrupted! Right down to the core!","angry","base","angry","mid", hair="angry")
    g4 "(What's the matter with her hair?!)"
    call ton_main("You don't have to search for too long to uncover the vile debaucheries that are happening at this school...","open","base","angry","mid", hair="angry")
    g4 "(Snape you fucking idiot! You blew it!!!)"
    call ton_main("Teachers taking advantage of their students, selling them favours in return for sexual acts...","open","base","angry","R", hair="angry")
    call ton_main("While they abuse their authority and power to do the most despicable things to them...","open","base","base","R", hair="horny")
    call ton_main("But the Dumbledore I know would never allow such disgracefulness at his school...","angry","base","angry","mid", hair="angry")
    m "(...)"
    call ton_main("I had this suspicion... Since the very day I got here...","open","base","angry","mid", hair="angry")
    # Tonks threatens Genie.
    # Maybe have her chibi point her wand at him?

    call ton_main("Now tell me, who are you?{w} And you better tell the truth!","angry","base","angry","mid", hair="angry")
    g4 "(Shit, how often is this going to happen to me?)"

    menu:
        g4 "I am..."
        "Albus Dumbledore!":
            call ton_main("You are most certainly {b}not{/b} Albus Dumbledore!","upset","base","angry","mid")
            g4 "No wait, it was Albertus Dumblerdore! That's it!"
            m "(Yes, that was probably it...)"
        "You know who!":
            call ton_main("What?","base","wide","wide","wide")
            m "You...{w=0.8} know...{w=0.8} who..."
            call ton_main("That can't be true!","open","base","worried","mid")
            m "You know who I am. You said it yourself earlier."
            m "(If only I could remember what she called me...)"
        "The danger!":
            call ton_main("What?","base","wide","wide","wide")
            g4 "I am the one who knocks..."

    call ton_main("I've had enough of this!","angry","base","angry","mid")
    call ton_main("Reveal who you are, dark wizard!","open","base","angry","mid")
    g4 "I'm not a dark wizard, you racist twat!"
    call ton_main("How dare you call me a racist!","angry","base","angry","mid", hair="angry")
    g4 "Bring it! Do your worst, witch!"
    call hide_characters
    hide screen bld1
    with d3

    # Glass break animation.
    # Duel won't happen and Tonks just casts a spell.

    call play_music("boss_theme")
    call play_sound("glass_break")
    pause.1

    show screen snape_glass
    pause 3
    show screen blkfade
    with d5

    hide screen snape_glass
    hide screen blkfade
    with d5
    pause.1

    call gen_chibi("hide")
    show screen dumbledore
    call cast_spell("revelio")
    call ton_main("Revelio!","open","base","base","mid", hair="angry", ypos="head")
    call bld("hide")
    pause.6

    call gen_chibi("sit_behind_desk")
    hide screen dumbledore
    with d9
    pause.6

    call ton_main("","open","wide","wide","wide", xpos="right", ypos="base")
    m "(...)"
    call ton_main("No way!","open","base","base","mid")
    m "What just happened?"
    call ton_main("What... are you...?","open","base","worried","down")
    m "(Can she see through the illusion?)"
    call ton_main("Wait a minute... Are you...{w} a Genie?","base","base","raised","mid")
    g4 "(This witch knows her shit!)"
    m "..."

    call play_music("playful")
    g9 "Some people would say I'm \"the\" Genie, actually!"
    m "The most powerful being in the entire universe... Multiple universes even...."
    m "Glad my reputation precedes me..."
    call ton_main("How curious. I've never had one before...","horny","base","raised","down", hair="horny") # Tonks looks horny.
    m "I'm sorry- what?"
    call ton_main("I meant, I've never had the pleasure of meeting a Genie before. This is brilliant!","smile","base","base","mid")
    m "(Is she hitting on me?!)"
    m "I'm flattered... But how were you able to tell?"
    call ton_main("I'm an Auror. It's my job to identify and catch magical beings...","open","base","base","R")
    call ton_main("But, if you are here, what happened to Professor Dumbledore?{w} Did he use one of your wishes and wish himself away?","open","base","worried","mid")
    m "No... I don't do that anymore."
    m "I'm what you would call a \"free\" Genie..."
    call ton_main("So? What happened to him?","upset","base","raised","mid")
    m "I believe we traded places when one of my magical inventions went wrong..."
    call ton_main("You don't say?! Is he okay?","open","base","base","mid")
    m "I think so.{w} He travelled to my universe, and I’m stuck in this dull place..."
    m "Believe me, there are a lot more brothels in Agrabah.{w} I bet he's having the time of his life..."
    call ton_main("So, you just poofed in here and decided to turn this school into your own private brothel...","open","base","angry","mid")
    call ton_main("Because you were bored?!","upset","base","angry","mid")
    m "Hey! I'm an immortal being... boredom is my worst enemy."
    m "And I didn’t do much, just a nudge in the right direction at the very best."
    call ton_main("You need to bring him back, the real Dumbledore, immediately!","angry","base","angry","mid", hair="angry")
    m "I don't know how,... yet.{w} We’re still working on it..."
    call ton_main("We? Who else knows about this?","angry","base","worried","R")
    m "That Snape guy."
    call ton_main("But of course!{w} After all he was mentioned in Miss Granger's letter as one of the main offenders.","open","wide","wide","wide")
    call ton_main("That sleazy, vile snake...{w} Naturally he'd be all over an opportunity such as this.","angry","base","angry","R", hair="angry")
    m "(Snake? Have I been saying his name wrong this entire time?...)"
    m "(I hate when that happens...)"
    call ton_main("And to think I got fooled by that creep when I questioned him about it.","angry","base","angry","down")
    m "(...)"
    call ton_main("He's a very skilled liar, I'll give him that.","upset","base","angry","down")
    m "Are you going to lock us up now?"
    call ton_main("I very well should! It would be the moral thing to do.","open","base","angry","mid")
    m "(Shit...)"
    call ton_main("But that won't bring back Professor Dumbledore...","upset","base","angry","R")
    call ton_main("You and Professor Snape should be locked up in the tiniest cell in Azkaban for what you’ve done...","angry","base","angry","mid")
    g4 "No, plase! I hate confined spaces!"
    call ton_main("And stay there for the rest of your lives...","open","base","angry","mid")
    g4 "You can't do that to me, I'm immortal! I'd go insane!"
    call ton_main("You should have thought about that before deciding to fuck your own students!","angry","base","angry","mid")
    g4 "But I haven't even gotten to that part yet!"
    call ton_main("And you never will! Unless...","open","base","base","mid")
    m "Unless what?"
    call ton_main("You let me join in on the fun!","base","base","raised","mid", hair="horny")
    m "..."
    g4 "What?" #screenshake
    call ton_main("The ministry sent me to investigate what they assumed to be a silly rumour a student made up...","open","base","angry","R")
    call ton_main("And whilst I could just squash the rumour and go back to a dull desk job.","open","base","raised","mid")
    call ton_main("I simply couldn't pass up an opportunity such as this...","base","base","base","mid", hair="horny")
    call ton_main("Keeping quiet would be far more beneficial to me...","horny","base","base","mid", hair="horny")
    m "How so?"
    call ton_main("I know for a fact that the Ministry has been looking at any excuse to have an adversary here at Hogwarts.","open","base","base","R")
    m "Then what are you suggesting?"
    call ton_main("Hire me as a teacher.","base","base","base","mid")
    call ton_main("I could teach the students a thing or two about the \"Defence against the Dark Arts\"...","open","base","base","mid")
    m "(...)"
    call ton_main("And if you and Snape want this favour trading to continue, you'll need somebody who can keep things quiet with the ministry.","upset","base","angry","mid")
    m "Do I even have a choice?"
    call ton_main("The alternative would be me bringing this to the ministry’s attention.","open","base","raised","mid")
    g9 "Then welcome aboard!"
    call ton_main("Don't worry. I'm not here to spoil your little act.","base","base","base","mid")
    m "That's a relief..."
    call ton_main("I'll inform the other teachers about my stay.","open","base","base","R")
    call ton_main("And the Ministry too of course. I know they'd love to have a ministry person teaching at Hogwarts, at the request of Professor Dumbledore himself, no less.","base","base","base","mid")
    call ton_main("If only they knew...","horny","base","base","mid")
    call ton_main("In any case, Profess-","open","base","base","R")
    call ton_main("I'm sorry, what would you like me to call you?","angry","base","raised","mid")

    menu:
        m "You can call me..."
        "Professor":
            $ ton_genie_name = "Professor"
            call ton_main("Very well.","base","base","base","mid")
        "Genie":
            $ ton_genie_name = "Genie"
            call ton_main("Very well.","base","base","base","mid")
        "Daddy":
            $ ton_genie_name = "Daddy"
            call ton_main("What? Are you serious?!","open","wide","wide","wide")
            call ton_main("*Ha*-*Ha*-*Ha!*...{w} you're too funny!","smile","base","sad","mid", hair="happy")
            g4 "(What?- Now it's yellow!)"
            call ton_main("Are all Genies this desperate?","smile","base","sad","mid", hair="happy")
            m "Desperate? Why Desperate?..."
            call ton_main("Nothing...","base","base","base","mid", hair="happy")
            call ton_main("Very well,... \"Daddy\"! {image=textheart}{image=textheart}{image=textheart}","horny","base","base","mid", hair="horny")
            g9 "*He*-*He*-*He*-He*..."

    call ton_main("Call me to your office whenever you require my help, Sir.","base","base","base","mid")
    m "I most certainly will..."

    #Tonks leaves
    call play_sound("door")
    call hide_characters

    call bld
    m "What an interesting turn of events..."
    g9 "Who could have guessed that she's a pervert as well?!"

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton")
    $ tonks_busy = True

    $ tonks_intro.E3_complete = True
    $ nt_event_pause += 1

    jump main_room
