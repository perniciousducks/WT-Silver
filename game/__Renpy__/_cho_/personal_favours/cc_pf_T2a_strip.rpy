

### Let Cho Strip ###

label cc_pf_strip:

    # Start Event
    $ cc_pf_strip.start()

    # End Event Jump
    label end_cho_strip_event:

        if cho_whoring < 9: # Points til 9
            $ cho_whoring += 1

    jump end_cho_event



### Tier 1 (pre Slytherin) ###

label cc_pf_strip_T1_intro_E1:
    m "It's time for your next favour, [cho_name]."
    call cho_main("I- *uhm*...{w} I think I'm ready.","horny","base","sad","downR")
    call cho_main("What would you like me to do, [cho_genie_name]?","soft","base","sad","mid")
    m "First, come a bit closer..."
    call cho_main("Very well, Sir.","base","base","base","mid")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main(xpos="mid", ypos="base", trans="fade")
    call ctc

    m "How often do you typically exercise, Miss Chang?"
    call cho_main("As often as I can, [cho_genie_name]!","soft","base","base","mid")
    m "Which is... how often? Twice a week?"
    call cho_main("Three times a day, Sir!","base","narrow","base","mid")
    with hpunch
    g4 "What?!"
    m "(I don't even jerk off that often!)"
    m "I find that a bit hard to believe... You're not embellishing the truth, are you?"
    call cho_main("I'm not, Sir! It's necessary for someone in my position!","open","closed","angry","mid")
    call cho_main("I wake up every morning before dawn, then run around the Quidditch pitch until the sun rises!","open","narrow","angry","mid")
    call cho_main("My body's at the absolute peak of human condition!","open","narrow","angry","R")
    g4 "It is quite impressive..."
    call cho_main("Glad to hear it, [cho_genie_name].","base","closed","base","mid")
    m "I assume you get complimented often?"
    call cho_main("Sometimes...","soft","base","base","R")
    g9 "And I suspect you have many admirers?"
    call cho_main("Oh, umm... maybe?","quiver","base","sad","down")
    call cho_main("But that's \"not\" why I take such great care of my body, Sir!","open","narrow","angry","mid")
    m "Of course not..."
    call cho_main("Quidditch is a hard game for anyone, as I'm sure you know...","open","closed","base","mid")
    call cho_main("But that goes double for girls! I have to train twice as hard as the boys if I want to stand a chance!","open","closed","base","mid")
    m "That's very commendable of you..."
    call cho_main("Thank you, Sir.","base","base","base","mid")

    # Ask her to strip.
    g9 "So, Why don't you show me what you are made of?{w} Let me have a proper look at you!"
    call cho_main("Sir?","soft","wink","raised","mid")
    m "I need you to remove your clothes."
    call cho_main("!!!","soft","wide","base","mid")
    m "Go on, girl. Start with the top..."
    call cho_main("No!","scream","closed","angry","mid", trans="hpunch")
    call cho_main("Why are you even asking me to do such a thing?!","angry","narrow","angry","mid")
    m "Have you already forgotten that I'm here to train you?"
    call cho_main("And I'm very thankful for that, Sir, but...","open","closed","base","mid")
    m "Am I not your trusted mentor?"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    m "Your strong advisor..."
    g9 "Your guardian angel!"
    call cho_main("I don't think taking off my clothes will be necessary for our training, [cho_genie_name].","annoyed","narrow","angry","R")
    m "I'm very disappointed I've got to say..."
    m "You aren't this shy with undressing in front of your team, are you?"
    call cho_main("Sir, that's entirely different!","angry","closed","sad","mid")
    m "How so?"
    call cho_main("I'm just not comfortable doing this in front of you, Sir!","quiver","closed","sad","mid")
    call cho_main("You're really old...","soft","narrow","sad","downR")
    m "Pardon me?"
    call cho_main("I meant... you're our headmaster! It just feels wrong to me!","soft","narrow","sad","mid")
    m "Are you one of those shy girls, Miss Chang?"
    call cho_main("No, Sir. I wouldn't say I'm shy, but...","soft","narrow","sad","downR")
    m "Well then prove me you aren't, girl!"
    g9 "Let me see it!"

    # Cho stays reluctant.
    call cho_main("Is there no other way I could repay the favour?","annoyed","narrow","sad","mid")
    m "Well, yes- Several.{w} But we'll get to those later..."
    call cho_main("Later, Sir?","soft","base","raised","mid")
    g4 "Girl, I wouldn't be asking you this if it wasn't absolutely necessary for your training!"
    call cho_main("Of course, [cho_genie_name].","annoyed","base","sad","down")
    m "All that's required of you is to cooperate..."
    call cho_main("(...)","annoyed","base","sad","mid")
    m "Now take of your top..."
    call cho_main("(...)","annoyed","narrow","angry","mid")
    call cho_main("Only my top?","soft","narrow","sad","mid")
    g9 "Would you like to take off \"more\"?"
    call cho_main("I didn't mean it like that!","angry","narrow","angry","mid")
    m "[cho_name], it's only the two of us in here. No need to worry."
    call cho_main("I'm not worried about others, [cho_genie_name]!","annoyed","narrow","angry","mid")
    call cho_main("For as long as nobody else will find out...{w} You have to promise me that, Sir!","soft","narrow","angry","R")
    g9 "Promised! Now take it off!"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    m "*He-hem*{w} Slowly..."
    pause.5
    call cho_main("","quiver","closed","sad","mid")
    pause.8

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    $ cho_cloth_pile = True
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","quiver","narrow","sad","mid")
    call ctc

    g4 "Magnificent."
    g4 "Simply...{w} magnificent..."
    call cho_main("Thank you, Sir.","soft","narrow","sad","R")

    menu:
        "\"Your posture is remarkable!\"":
            call cho_main("I'm glad you noticed!","base","base","sad","mid") # Happy
            call cho_main("I'm relieved you actually show interest in my body status, Sir!","smile","base","base","mid")
            m "(Oh- You have no idea, girl!)"
            call cho_main("I thought you just wanted to gush at my body like all the other teachers...","soft","narrow","sad","mid")
            m "Who?{w} Which other teachers are you talking about?{w} Snape?!"
            call cho_main("No, not Snape...","annoyed","narrow","angry","R")
            call cho_main("(...)","annoyed","base","sad","downR")
            call cho_main("Promise me you won't tell her!","quiver","narrow","sad","mid")
            m "Her?!"
            call cho_main("Madame Hooch, Sir.","soft","narrow","sad","mid")
            m "Ah, the old, gray haired lady..."
            call cho_main("Yes, she's been eyeing me a lot lately...","quiver","base","sad","downR")
            call cho_main("Even more so after our recent game against Hufflepuff. I wonder why...","horny","narrow","sad","R")
            g9 "I can't blame her... Your body is very pleasant to look at!"
            call cho_main("Thank you, Sir.","base","base","base","mid")

        "\"You have marvelous abs!\"":
            call cho_main("*Uhmm*...","quiver","narrow","sad","R") # Embarrassed
            g4 "As if Michelangelo himself carved them onto your flesh..."
            m "I must say I'm very impressed!"
            call cho_main("Thank you, Sir.","soft","narrow","sad","downR")

    m "Not every girl I get to see here has such fine...{w} contours..."
    call cho_main("Other girls?","soft","wide","base","mid")
    call cho_main("Sir, you aren't training anybody else in Quidditch besides me, are you?","soft","narrow","angry","mid")
    m "What? Of course not..."
    call cho_main("Then which other girls are you talking about?","annoyed","narrow","angry","mid")
    g4 "(Shit! I better just tell her the truth.)"
    m "Just...{w} Granger..."
    call cho_main("*Phewww*{w} You scared me there for a second, Sir...","smile","narrow","sad","mid")
    m "You... don't mind about it?"
    call cho_main("Please. Why should I care what Granger does for you in here?","soft","narrow","angry","R")
    call cho_main("I suspected she was one of those girls buying favours from her teachers!","soft","closed","angry","mid")
    call cho_main("With how many points she's earned for her house lately,... to win the house cup...","open","narrow","angry","R")
    call cho_main("But as long as you don't help any \"Gryffindor\" or \"Slytherin\" sluts win the Quidditch cup, everything will be fine.","base","narrow","base","mid")
    m "That's a relief..."

    call cho_main("Besides, she clearly doesn't hold a candle against me!","open","narrow","base","R")
    call cho_main("All she does is sit on her arse all day, studying in the library...","soft","narrow","angry","mid")
    m "(...)"
    call cho_main("You can't expect somebody who's as lazy as her to look as great as I do!","soft","closed","base","mid")

    menu:
        "\"Yeah, she's gross.\"":
            m  "Miss Granger's body is nothing compared to yours."
            call cho_main("I wholeheartedly agree, Sir!","base","narrow","angry","mid")
            m  "Her tits sag too much, and her fat hips are disgusting..."
            call blktone
            g4 "(Something deep inside me just died saying this...)"
            call hide_blktone
            call cho_main("She really is a...","open","closed","raised","mid")
            call cho_main("... stupid...","angry","closed","angry","mid")
            call cho_main("... fat...","angry","narrow","angry","mid")
            call cho_main("... cow, isn't she?","quiver","narrow","angry","mid")
            m "Speaking of Hermione..."
            g9 "Why don't you show me \"your\"{w} very much \"superior\"{w} hips?"
            call cho_main("Are you asking me to take off my skirt?","soft","wink","raised","mid")
            m "Yes, my dear."

        "\"Nope, you lose\"":
            $ cho_mood +=6

            call cho_main("What?!","scream","wide","angry","mid", trans="hpunch")
            call cho_main("","angry","narrow","angry","mid")
            m "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!"
            m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
            call cho_main("But she doesn't even do work-outs!","angry","narrow","angry","downR")
            m "Let's just forget about her, shall we?"
            m "And continue where we left off..."
            call cho_main("And where would that be?","annoyed","narrow","angry","mid")
            m "Your Quidditch training, Miss Chang."
            call cho_main("I'm not sure I want to after what you've just said...","annoyed","narrow","angry","R")
            m "Why? What did I say?"
            call cho_main("That Granger's body is better?! We both know that isn't true.","angry","narrow","angry","mid")
            m "Do you expect me to apologize?"
            call cho_main("Yes!{w} Admit that I'm sexier!","annoyed","closed","angry","mid") # Snobby
            g9 "You are indeed, \"very sexy\", Miss Chang!"
            call cho_main("Thank you, Sir.","base","narrow","base","mid")
            m "Now take of that skirt, would you..."
            call cho_main("(...)","annoyed","narrow","angry","mid")


    call cho_main("Please don't tell anybody about what I'm doing in here, Sir.","quiver","narrow","sad","mid")
    call cho_main("It could really tarnish my reputation.","soft","narrow","sad","R")
    m "I'd never think of it..."
    call cho_main("I will take off my skirt now!","scream","closed","angry","mid") # Scream
    call cho_main("","horny","narrow","sad","R")
    g9 "(!!!)"
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","base","mid")
    call ctc

    g4 "YES!"
    g4 "Look at those thighs!"
    g4 "Those tree-trunks!"
    g9 "Even the great \"Chun Lee\" would be jealous of those!"
    call cho_main("I'm sorry Sir, who's that?","soft","wink","raised","mid")
    m "One of the best female street fighters, if you know how to play with her..."
    call cho_main("(Play with her?!)","angry","wide","base","mid")
    g9 "Speaking of which!{w} I don't believe we are done here just yet."
    call cho_main("We aren't? But I did exactly what you wanted!","quiver","wide","sad","mid")
    g9 "You've still got some clothes on..."
    call cho_main("Sir, is this why you are helping me?","open","closed","angry","mid")
    call cho_main("Might this be all just part of a sick scheme to get to see me naked?","annoyed","narrow","angry","mid")
    m "(...)"

    menu:
        "\"It absolutely is!\"":
            $ cho_mood += 20
            $ cho_mad_about_stripping = True # Flag that enables different dialogue that is a bit more "lewd" in the next favor repeat.
            call cho_main("","angry","wide","base","mid") # Shock
            g9 "Now take off that bra of yours and show me those titties!"
            call cho_main("[cho_genie_name], how can you talk to me like that!","scream","closed","angry","mid", trans="hpunch")
            call cho_main("I'm your student!","open","narrow","angry","mid")
            g9 "And a very pretty one at that!"
            call cho_main("You disgust me, Professor...","angry","narrow","angry","mid")

        "\"Of course not...\"":
            $ cho_mood += 6
            $ cho_mad_about_stripping = False
            call cho_main("Aye right...","soft","narrow","raised","mid") # Expression of disbelieve...
            call cho_main("And I'm supposed to believe that.","open","narrow","base","R")
            call cho_main("You're practically foaming out of your mouth just looking at me, Sir...","soft","narrow","angry","mid")
            g4 "I'm not...{w} that's just..."
            #if butterbeer_ITEM.number > 0:
            g4 "Butterbeer..."
            call cho_main("This is as far as I will go, Sir!","annoyed","narrow","angry","mid")

    call cho_main("If you want a bimbo to strip for you, I suggest you call Hermione instead...","open","narrow","angry","mid")
    pause.5

    hide screen cho_chang
    $ cho_class.wear("all")
    $ cho_cloth_pile = False
    call cho_main("","angry","angry","angry","mid")
    pause.8

    call cho_main("We are done here!","angry","angry","angry","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "She'll do it next time, I'm sure..."

    jump end_cho_strip_event


label cc_pf_strip_T1_intro_E2:
    call cho_main("","upset","base","base","R")
    m "[cho_name], to continue your training where we left off..."
    g9 "I'd like you to undress, once again!"
    call cho_main("Of course, Sir.","annoyed","base","angry","downR")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("Down to my undergarments, [cho_genie_name]?","soft","closed","base","mid", xpos="mid", ypos="base", trans="fade")
    call cho_main("Or would you like me to take off all of it?","soft","narrow","base","mid")
    m "*Uhm*... All of it?"
    call cho_main("Very well, Sir.","soft","closed","base","mid")
    g4 "(Please don't let this be a trick question.)"
    call cho_main("","upset","narrow","base","mid")
    pause.4

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    $ cho_cloth_pile = True
    call cho_main("","upset","narrow","base","mid")
    pause.5

    call cho_main("","upset","narrow","angry","mid")
    call ctc

    call cho_main("I'm a very good trainee, [cho_genie_name]!","soft","narrow","angry","mid")
    g9 "Yes you are!"
    call cho_main("If my trainer requires me to take off my clothing and strip for him...","soft","closed","base","mid")
    call cho_main("Then I have no other choice but to indulge...","soft","narrow","base","R")
    call cho_main("I see nothing wrong with that...","annoyed","narrow","angry","mid")
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","annoyed","narrow","base","mid")
    call ctc

    call cho_main("Would you perhaps like me to climb on top of your desk as well?","soft","narrow","raised","mid")
    call cho_main("And dance for you like some common harlot?","soft","narrow","base","R")

    # You saw Hermione strip before.
    if hg_T3_strip_trigger:
        m "If it's not too much trouble..."
        call cho_main("Of course not, [cho_genie_name].","soft","closed","base","mid")
        g4 "(I'm having a bit of a deja vu!)" # In-game font doesn't support special characters. déjà vu!
    else:
        g9 "Yes please!"
        call cho_main("Whatever you say, Sir!","soft","closed","base","mid")
    call cho_main("Like I said, I'd go to any lengths just to please my trainer...","soft","narrow","base","mid")

    # Climbs desk.
    call hide_characters
    show screen blkfade
    with d5
    call play_sound("climb_desk")
    pause 1

    "To your surprise, the athletic petite girl rather playfully climbs on top of your desk."
    pause.5
    g9 "Nice!"
    pause.2

    call cho_chibi("stand","on_desk","on_desk", flip=False)
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call cho_main("After all, I promised I'd do anything to win that Quidditch cup...","soft","narrow","angry","mid")
    call cho_main("If stripping for you is what it takes- then...","soft","base","angry","down")
    call play_music("sad")
    call cho_main("Then...","angry","base","sad","down")
    call cho_main("I- I'll do it...","soft","narrow","sad","down")
    m "(Shit. Is she crying?)"
    m "(Can she even cry?)"
    m "Are you alright, girl?"
    call cho_main("No.{w} I'm already regretting climbing up here!!!","angry","closed","sad","mid")
    call cho_main("(What were you thinking, Cho?!)","angry","narrow","sad","down")
    m "You can come back down if it's too much for yo-"
    call cho_main("Shut up!","scream","closed","angry","mid", trans="hpunch") # Scream
    call cho_main("Can't you see what I'm trying to do here?","angry","angry","angry","mid")
    m "Not really, no."
    call cho_main("I-I'm... testing my limits, Sir.","angry","narrow","sad","down")
    call cho_main("And I believe I've reached them!","angry","closed","sad","mid")
    m "For real? You are still wearing clothes..."
    call cho_main("I thought{w=0.2}, if I could go as far as embarrassing myself in front of my headmaster...","soft","narrow","sad","down")
    call cho_main("Doing the same in front of the school won't feel as bad in comparison.","annoyed","narrow","sad","down")
    call cho_main("Sir, I don't think I can do this after all.","soft","narrow","sad","mid")
    call cho_main("Could I get your permission to leave and never come back?","angry","narrow","sad","mid")

    menu:
        "\"Yes, but take off those clothes first...\"":
            call play_music("stop")
            call cho_main("Yes! Thank you, Sir!","quiver","closed","sad","mid")
            call cho_main("Even after I've given up you're still believing in me!","soft","narrow","sad","mid")
            m "What?{w=0.2} *Ahem* I mean..."
            g9 "Of course!{w=0.2} I always did!"
            call cho_main("I may not like it. But this is all just part of my training...","soft","base","sad","R")
            m "*Uhhhh*... Sure..."
            call play_music("cho_theme")
            call cho_main("It's one of many challenges I have to face before I can call myself a Quidditch champion!","soft","closed","angry","mid")
            call cho_main("This is just about facing my inner demons, isn't it?","soft","narrow","angry","mid")
            call cho_main("Overcoming my fears...","soft","narrow","angry","R")
            call cho_main("Failure, and embarrassment...","soft","closed","base","mid")
            call cho_main("(Come on Cho, you can do it!!!)","horny","closed","sad","mid")
            call cho_main("*Uhm*...","horny","narrow","sad","down")
            call cho_main("What would you like me to do first, [cho_genie_name]?","soft","narrow","sad","mid")
            call cho_main("Remove my bra...","soft","narrow","base","mid")
            call cho_main("Or take off my panties?","horny","narrow","sad","down")

        "\"Yes, you are dismissed...\"":
            $ cho_mood += 6
            call play_music("stop")
            call cho_main("What?!","soft","wide","base","mid")
            call cho_main("But Sir!","soft","wide","sad","mid")
            m "You can go now..."
            call cho_main("You can't do that!","scream","narrow","angry","mid", trans="hpunch")
            call cho_main("","angry","narrow","angry","mid")
            g4 "Didn't you just beg me to do just that?"
            call play_music("sad")
            call cho_main("I begged you to help me win the Quidditch cup!","angry","angry","angry","mid")
            call cho_main("And to be my trainer!{w} To be a \"good\" trainer!","soft","narrow","angry","mid")
            call cho_main("How can I overcome my fear of losing if I can't even do... this!","soft","base","sad","down")
            call cho_main("You're supposed to encourage me! Get me through any challenges I'm confronted with.","soft","narrow","angry","mid")
            m "Including stripping?"
            call cho_main("Including bloody stripping!","scream","closed","angry","mid", trans="hpunch")
            call cho_main("","annoyed","narrow","angry","mid")
            m "To my defence. I got some mixed messages from you earlier..."
            call cho_main("(...)","annoyed","narrow","angry","R") # Annoyed
            call play_music("stop")
            m "Very well then..."
            m "Take of your clothes, [cho_name]."
            call cho_main("Yes, Sir!","soft","closed","base","mid")
            call cho_main("Would you like me to take off my bra first?","soft","narrow","angry","mid")
            call cho_main("Or pull down my panties so you can get a nice look at my lower half?","soft","narrow","base","mid")

    m "(...)"
    menu:
        m "First, I'd like you to..."
        "\"Show me those big, juicy \"Quaffles\" of yours!\"":
            call play_music("cho_theme")
            call cho_main("*uhhh*...","upset","wide","base","mid")
            g9 "Those two mean, hearty \"bludgers\"!"
            call cho_main("Sir? Could it be that you are talking about my breasts?","soft","narrow","sad","mid")
            m "Yes indeed! Very good."
            m "I had hoped you would eventually catch on."
            m "Because I had also run out of balls to compare them to..."
            call cho_main("Promise me that you won't laugh when I show you my...","soft","narrow","sad","R")
            call cho_main("\"Bludgers\"!","angry","closed","sad","mid")
            m "Why would I ever laugh at a pretty girl like you, Miss Chang?"
            call cho_main("Because they...{w} aren't as big as Hermione's...","soft","narrow","sad","downR")
            call cho_main("Hers are more closer to \"Quaffles\" than mine...","soft","base","sad","mid")
            m "And there will always be a pair of \"Beaters\" that prefer to play with your...{w} balls."
            call cho_main("Only two?...","upset","base","sad","downR")
            g9 "Don't forget to count those lucky enough to get hit by those \"bludgers\"!"
            call cho_main("","upset","base","raised","mid")
            m "Speaking of which..."
            call cho_main("Yes?","soft","base","sad","mid")
            g4 "I'd like you to hit me with them!"
            call cho_main("With my breasts?","open","wide","base","mid")
            g9 "Yes! Hit me full force!{w} Take off that bra!"
            call cho_main("*Ugh!*...","angry","narrow","base","down")
            call cho_main("{size=-4}I can't believe I'm actually going to do this!{/size}","angry","closed","sad","mid")
            call cho_main("","soft","narrow","sad","mid")
            pause.4

            # Remove bra.
            hide screen cho_chang
            $ cho_class.strip("bra")
            show screen cho_chang
            with d3
            pause.8

            call cho_main("","horny","narrow","sad","mid")
            call ctc

            g4 "Simply wonderful, Miss Chang."
            m "Those are some stellar breasts you got there."
            call cho_main("(...)","base","narrow","sad","downR")
            g4 "Some \"outstanding\" boobies!"
            call cho_main("...","annoyed","narrow","base","mid")
            m "Would you mind if I smack them?"
            call cho_main("What?! Of course I would mind!","soft","wide","base","mid")
            m "I just want to beat them around a bit..."
            call cho_main("","annoyed","narrow","angry","mid")
            g9 "After all, they are two soft, meaty \"bludgers\"!"
            g9 "And I'm a \"beater\"!"

            $ genie_quid_position = "beater"

            call cho_main("You are childish.{w} That's what you are...","soft","narrow","angry","mid")
            m "You're the one playing games."
            call cho_main("(...)","annoyed","narrow","angry","mid")
            call cho_main("Fine...{w} But Only once!","soft","narrow","angry","R")
            call cho_main("Twice,...{w} maybe...","angry","narrow","sad","downR")
            g9 "That's a hundred percent more than I had hoped for!"

            call slap_her
            call cho_main("*Ouch!*","angry","wide","base","mid")
            call slap_her
            call slap_her
            call slap_her
            call cho_main("Stop it!","scream","closed","sad","mid")
            call cho_main("That was more than twice!","soft","narrow","angry","mid")
            m "I stopped counting halfway through..."

        "\"Let me catch sight of that \"Snitch\"!\"":
            call play_music("cho_theme")
            call cho_main("Don't you mean \"Snatch\", Sir?","annoyed","narrow","angry","mid")
            g9 "Potato, Potato!"
            call cho_main("Your motives were nothing but for your own perverted gains, weren't they? From the very start.","soft","narrow","base","mid") # Annoyed
            m "More or less..."
            m "However, I never lied about wanting to help you win the Quidditch cup!"
            g4 "(Since I've bet a fortune on it...)"
            m "And I wouldn't be able to call myself a man if I was lying!"
            call cho_main("And you'd be called a dead man, if you try to trick me!","angry","narrow","angry","mid")
            m "Well technically I'm a gen-"
            call play_sound("kick")
            call cho_main("","annoyed","angry","angry","mid", trans="vpunch")
            g4 "*Aaaaah!*"
            call nar("Cho does a daunting stomp on your desk...")
            call cho_main("Don't think for a second I wouldn't do it! After all of this!","scream","narrow","angry","mid")
            call cho_main("","angry","narrow","angry","mid")
            call play_sound("gulp")
            g4 "*Gulp*"
            m "Yes, Ma'am."
            call cho_main("(...)","upset","closed","base","mid")
            call cho_main("","upset","narrow","sad","down")
            pause.4

            # Remove panties.
            hide screen cho_chang
            $ cho_class.strip("panties")
            show screen cho_chang
            with d3
            pause.5

            call cho_main("","horny","narrow","sad","mid")
            call ctc

            call cho_main("Happy, Sir?","soft","narrow","sad","mid")
            m "Very."
            g9 "Finally I get the appeal of Quidditch."
            call cho_main("Really?","soft","base","raised","mid")
            m "Yes..."
            g9 "You see, I think I've become quite a bit of a seeker myself!"

            $ genie_quid_position = "seeker"

            call cho_main("(...)","annoyed","base","base","mid")
            m "And I believe I've just found my very own golden snatch!"
            call cho_main("","annoyed","narrow","angry","mid")
            m "You should consider yourself lucky, Miss Chang."
            call cho_main("Why?...","soft","narrow","raised","mid")
            g9 "It's very pretty."
            call cho_main("*Ugh*...","angry","narrow","base","down")


    call cho_main("Sir, will that be all then?","soft","narrow","angry","mid")
    call cho_main("May I go now?","soft","narrow","angry","R")
    m "Haven't you forgotten something?"
    call cho_main("Didn't I do enough for you already?","angry","angry","angry","mid")
    g9 "For me, you did more than enough!{p=0.6}I'm more than pleased with what you've shown me..."
    call cho_main("*Ugh*...","angry","narrow","base","mid") # Disgusted
    m "But, wasn't your goal earlier to undress entirely?"
    m "To prove to yourself that you \"could\" do it?"
    call cho_main("{size=-4}I hoped you'd just forget about that...{/size}","angry","narrow","sad","down") # Small text.
    g9 "Well, I didn't!"
    m "I'm here to help you mature and boost your confidence."
    m "A body like yours is nothing you need to hide away!"
    call cho_main("","base","narrow","sad","mid")
    m "Don't you think so too?{w} After all the work you put into it?"
    g4 "It should be celebrated! And seen by everyone!"
    call cho_main("You're making me blush, [cho_genie_name]...","soft","narrow","sad","downR")
    g9 "You can do it, [cho_name]! Only one more piece to go..."
    call cho_main("Yes, Sir!","angry","closed","sad","mid")
    call cho_main("","base","narrow","sad","mid")
    pause.4

    # Cho strips completely.
    hide screen cho_chang
    $ cho_class.strip("all")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","sad","mid")
    call ctc

    m "See, that wasn't very hard was it?"
    call cho_main("No...","soft","narrow","base","down")
    call cho_main("No! You're right!","smile","base","base","mid")
    m "And you have a very beautiful body if I might add."
    call cho_main("Thank you, Sir.","soft","narrow","sad","mid")
    m "I can see why Hermione is so jealous."
    call cho_main("","upset","base","base","mid")
    pause.8
    call cho_main("She is?","scream","wide","base","mid", trans="vpunch")
    call cho_main("","horny","base","base","down")
    m "Look who perked up all of a sudden."
    call cho_main("She should be jealous, these thighs could break a broom in half if I tried hard enough.","smile","narrow","angry","mid")
    call ctc

    call play_sound("gulp")
    g4 "*Gulp!*"
    m "I don't doubt it."

    call cho_main("Thank you.","base","closed","base","mid")
    m "For what?"
    call cho_main("Teaching me.{p=0.4}I couldn't have imagined showing myself off like this before... but.","horny","narrow","sad","downR")
    m "Yes?"
    call cho_main("Well, your methods have clearly worked so far...","soft","narrow","base","R")
    call cho_main("And I feel more confident than ever!","soft","wide","base","mid")
    m "That's great news, and hey..."
    m "If distracting doesn't work, you could just crush your opponents with those thighs of yours."
    call cho_main("That's true...","smile","narrow","base","mid")
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    call cho_chibi("stand","desk","base", flip=False)

    pause 1

    hide screen blkfade
    with d5
    pause.2

    call cho_main("Will this be all then, Sir?","soft","base","base","R")
    m "Yes Miss Chang, great work today..."
    m "I doubt you'll have any problems distracting anyone with a body like that."
    m "You're dismissed."
    call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
    call hide_characters
    hide screen bld1
    with d3
    pause.1

    call cho_walk(xpos="door", ypos="base", speed=2.5)

    call bld
    m "Miss Chang."
    hide screen bld1
    with d3
    pause.3

    call cho_chibi("stand","door","base", flip=False)
    with d3
    pause.2

    call cho_main("Yes?","soft","base","raised","mid", ypos="head")
    m "Aren't you forgetting about something?"
    call cho_main("Sir?","soft","narrow","base","mid")
    m "You're still naked...{w} I wouldn't go out there if I were you..."
    call cho_main("Oh, yes of course!","soft","wide","base","mid", trans="hpunch")

    call cho_walk(xpos="desk", ypos="base", speed=2)
    pause.5
    call chibi_effect("thought","cho")
    pause.8

    # Cho puts clothes back on.
    call play_sound("equip")
    hide screen cho_chang
    $ cho_class.wear("all")
    $ update_chibi_image("Cho")
    $ cho_cloth_pile = False
    pause.8

    call cho_main("(...)","upset","narrow","sad","down", xpos="right", ypos="base")
    call cho_main("*Uhm*...","soft","narrow","sad","mid")
    if daytime:
        call cho_main("Have a good day...","soft","base","base","R")
    else:
        call cho_main("Have a good night...","soft","base","base","R")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.5)

    call bld
    m "She's so cute..."
    g9 "And sexy!"
    m "But also a bit intimidating..."

    jump end_cho_strip_event


label cc_pf_strip_T1_intro_E3:
    g9 "[cho_name], how would you like to do another strip-tease for me?"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    g9 "You did such a phenomenal job last time!"
    call cho_main("Another strip show?","soft","narrow","angry","R")
    g9 "Yes Indeed! Come a bit closer..."
    call cho_main("(...)","angry","narrow","base","down")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("Sir, Those favours were never about my training, were they?","soft","narrow","angry","mid", xpos="mid", ypos="base", trans="fade")
    m "I never said they were!"
    call cho_main("","annoyed","narrow","angry","mid")
    pause.8
    m "You keep me happy by doing favours for me, and in return, I will train you..."
    m "That was the deal."
    call cho_main("I never expected that they would require me to do...{w} this!","annoyed","base","sad","down")
    g9 "But you did it anyway! Commendable!"
    call cho_main("Please stop it with your compliments, Sir!","open","closed","angry","mid")
    call cho_main("And explain to me why those favours have to be so...","annoyed","narrow","sad","downR")
    call cho_main("perverted?","soft","narrow","angry","R") # Small text
    m "You see,..."
    m "It can get pretty lonely in this room."
    m "There's not even a television set up here..."
    call cho_main("(...)","annoyed","narrow","angry","mid")
    pause.8

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    $ cho_cloth_pile = True
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","quiver","narrow","sad","R")
    call ctc

    call cho_main("Does Granger do these sorts of things for you too?","soft","base","sad","mid")
    g9 "She does a lot of things for me. You need to be more specific!"
    call cho_main("I meant buying \"sexual favours\".{w} Doing tasks that are, let's say, a little audacious...","soft","narrow","sad","downR")
    m "Are you talking about stripping, girl?"
    call cho_main("Yes, Sir.","quiver","narrow","sad","downR")
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","base","sad","mid")
    call ctc

    # Check if Hermione has already stripped for you.
    if not hg_T3_strip_trigger:

        # Cho demands that you get Hermione to strip, so Cho has something to blackmail her should anything happen.
        # Cho gets dressed again and storms off.

        m "Actually, she doesn't..."
        call cho_main("What? But I thought she'd-","soft","wide","base","mid")
        call cho_main("Why do you ask me to do these favours, and not Granger?","open","angry","angry","mid", trans="hpunch")
        m "Lets just say, she isn’t as progressive as you...{w} yet."
        call cho_main("You haven’t even seen her naked?","angry","base","base","mid")
        call cho_main("What favours are you even buying from her?","open","base","angry","mid")
        m "Just chit-chats, mostly..."
        call cho_main("Make her strip too!","angry","narrow","angry","mid")
        g4 "It’s not that easy, girl!"
        call cho_main("Well then get on with it!","angry","closed","angry","mid")
        call cho_main("What’s the worst that could happen?","soft","narrow","angry","R")
        m "She could report me, and I’d get kicked out of this school most likely."
        m "She’s reported me to that ministry before..."
        call cho_main("The \"Ministry of Magic\"?!","open","base","raised","mid")
        call cho_main("If they were to regulate the school rules more strictly, my chance of winning the Quidditch cup would be back down to zero!","angry","wide","sad","mid")
        call cho_main("And if Granger ever was to find out about me stripping for our headmaster, it would mean the end of my Quidditch career for sure!","quiver","base","sad","downR")
        m "So? What do you suggest we do?"
        call cho_main("Isn't it obvious?! Ask her to do more advanced favours!","soft","narrow","angry","mid")
        call cho_main("If I could get a hold of something to blackmail her with, she'd never dare to report to the ministry!","quiver","narrow","angry","R")
        m "That doesn't sound too bad of an idea..."
        call cho_main("Until then, don't expect me to undress for you until you've solved this situation...","soft","narrow","angry","mid")
        m "(Bollocks...)"
        call cho_main("","annoyed","closed","angry","mid")
        pause.5

        hide screen cho_chang
        $ cho_class.wear("all")
        $ cho_cloth_pile = False
        call cho_main("","angry","closed","angry","mid")
        pause.8

        call cho_main("Good day, Sir!","soft","narrow","angry","mid")

        # Cho leaves.
        call cho_walk(action="leave", speed=2.5)

        # Event failed, no progress.
        $ cc_pf_strip.fail()
        jump end_cho_event


    # After you got Hermione to strip.
    m "She does indeed."
    call cho_main("Really?!{w} You got that cow to take off her clothes?","soft","wide","base","mid")
    call cho_main("Did you get any prove of it?","soft","base","sad","mid")
    m "What?{w} Why would I need to do that?"
    call cho_main("To blackmail her!{w} To prove that she's in on this whole \"favour trading\" business too...","open","narrow","angry","mid")
    m "We had an eye witness, for what it's worth..."
    call cho_main("Seriously?! Who was it?","smile","base","base","mid")
    m "Snape..."
    call cho_main("What?! Professor Snape?","scream","wide","base","mid", trans="hpunch")
    call cho_main("","smile","wide","base","mid")
    m "He sort of just walked in on the action.{w} After all, the door wasn't locked..."
    call cho_main("That's too funny! I wish I could have been there when that happened!","smile","base","base","R")
    g9 "She was dancing on my desk, right here, butt naked!"
    call cho_main("That sounds sooo embarrassing!","soft","narrow","sad","up")
    m "As far as I know, that door isn't locked right now either..."
    m "Aren't you scared that Snape might walk in on you too?"
    call cho_main("*Hmmmm*","annoyed","base","base","R")

    call hide_characters
    show screen blkfade
    with d3
    call play_sound("desk")
    pause 3

    ">You watch as Cho slowly climbs onto your desk..."

    call cho_chibi("stand","on_desk","on_desk")
    hide screen bld1
    hide screen blkfade
    with d3
    call ctc

    call cho_main("I'm not scared at all, Sir!","smile","narrow","angry","mid")
    call cho_main("","horny","narrow","angry","mid")
    pause.4

    # Remove bra.
    hide screen cho_chang
    $ cho_class.strip("bra")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","angry","mid")
    call ctc

    call cho_main("It's just Professor Snape, after all...","soft","narrow","base","R")
    call cho_main("Everybody knows that he's a creep! Nobody would believe a word he says.","horny","base","angry","down")
    m "So...{w} what if it's not Snape, but some other teacher that makes their way in here?"
    call cho_main("*Huh?*{w} Oh no!","soft","wide","base","mid")
    call cho_main("For a second I forgot we even had other teachers at this school!","open","wide","sad","L")
    call cho_main("What if Professor McGonagal stumbles in here while-{w} while I-...","angry","closed","sad","mid")

    call play_sound("desk")
    call hide_characters
    show screen blkfade
    with d3
    pause 1.0

    call cho_chibi("stand","desk","base", flip=True)
    hide screen bld1
    hide screen blkfade
    with d3
    call teleport(position="cho", effect=False)
    pause.5

    call bld
    m "Don't worry. That won't happen."
    call cho_chibi("stand","desk","base")
    with d3
    pause.5

    call cho_main("Are you sure, Sir?","soft","narrow","sad","mid")
    m "You have my word on it..."
    call cho_main("O-{w}okay...","soft","narrow","sad","R")
    m "Now then, Miss Chang!{w} It's time for the grand finale..."
    g9 "Take off your panties!"
    call cho_main("(...)","annoyed","base","sad","down")
    call cho_main("Very well, Sir.","base","base","base","mid")
    pause.4

    # Remove panties.
    hide screen cho_chang
    $ cho_class.strip("panties")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","angry","mid")
    call ctc

    g4 "I've got to say, once again I'm very impressed by you!"
    call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
    call cho_main("You can have those, by the way.","base","narrow","angry","mid")
    call nar(">Cho throws a pair of panties onto your desk.")
    call cho_main("You can keep them, for now...","soft","narrow","base","R")
    g9 "I appreciate the notion!"
    call cho_main("","base","narrow","base","mid")
    pause.8

    # Panties acquired message!
    $ has_cho_panties = True

    m "Well then, Miss Chang..."
    m "You may leave now.{w} Dismissed."
    call cho_main("Wait Sir!{w} I can't leave just yet!","open","wide","base","mid")
    m "Why not? Don't tell me you want some points now after all..."
    call cho_main("No Sir, but...{w} I don't believe we are done here...","angry","base","sad","R")
    g9 "We aren't?"
    call cho_main("May I request something of you, Sir?","soft","narrow","sad","mid")
    m "Yes?{w} What is it?"

    # Cho asks you to summon Hermione.
    call cho_main("Could you please...","soft","base","sad","downR")
    call cho_main("*Uhm*...","quiver","narrow","sad","downR")
    call cho_main("Could you please summon Hermione?","soft","narrow","sad","mid")

    with hpunch
    g4 "What?"
    call cho_main("It’s time someone throws \"high and mighty\" Granger off her high horse!","open","narrow","angry","mid")
    call cho_main("She’s been a pain in my butt for years now...","angry","angry","angry","downR")
    call cho_main("This is going to be my revenge!","soft","narrow","angry","mid")
    m "Are you sure that this is such a good idea? Aren’t you scared she’ll tattle about it?"
    call cho_main("No.{w} Granger is clever...","soft","closed","base","mid")
    call cho_main("She could destroy my reputation, sure,...","soft","base","base","R")
    call cho_main("But, should that happen, I now have the means to take her down with me!","base","narrow","angry","mid")
    call cho_main("I’m not the only one stripping for you, after all.","soft","narrow","base","mid")
    m "I suppose you're right..."
    call cho_main("I can’t believe how depraved Granger actually is...","horny","narrow","angry","down")
    call cho_main("Stripping for her headmaster. What a slut...","soft","narrow","angry","mid")
    m "Aren’t you doing exactly the same?"
    call cho_main("Yes, but I’m not a whore stripping for points, unlike her!","open","closed","base","mid")
    m "Still makes you a slut..."
    call cho_main("I’m untouchable! I’ll show that bitch she can’t mess with me!","angry","angry","angry","R")
    call cho_main("This is gonna be so much fun!","smile","narrow","angry","mid")

    call cho_walk(xpos="570",ypos="base", speed=1.5)
    pause 2.0

    call cho_main("Call her already!","annoyed","narrow","angry","R", ypos="head", flip=True)
    m "I'm on it..."

    hide screen bld1
    with d3
    pause 1.0

    # Summon Hermione.
    call play_sound("door")
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call her_main("You wanted to see me, Sir?","soft","closed", ypos="head")
    call her_main("Cho?","soft","shocked", ypos="head")
    call cho_main("Hey there, Granger!","horny","narrow","angry","mid", ypos="head", flip=True) # Grinning
    call her_main("What? Why are you-","disgust","shocked", ypos="head")

    call her_walk(xpos="660",ypos="base", speed=2)

    call cho_main("","smile","narrow","angry","mid", xpos="mid", ypos="base", flip=True)
    call her_main("What the bloody hell is going on here?!","scream","closed", xpos="base", ypos="base", trans="hpunch") # Scream
    call her_main("","angry","angry")

    call cho_main("You know, just the usual...","soft","base","base","L")
    call cho_main("Like stripping for our dear headmaster!","smile","angry","angry","L")
    call cho_main("I trust that you're more than familiar with it...","soft","closed","base","L")
    call her_main("You've told her?","clench","angry")
    call cho_main("So you really \"did\" do it!","open","wide","base","L")
    call her_main("It's none of your business what I do at this school! You slut!","angry","angryL")
    call cho_main("Are you sure about that? I believe there are some people that would think otherwise...","angry","narrow","base","mid")
    call cho_main("Your friends...{w} the other students...{w} our teachers...","soft","narrow","angry","L")
    call cho_main("Maybe even the ministry?","smile","narrow","angry","L")
    call her_main("You wouldn't dare!!!","upset","squint")
    call cho_main("Indeed, I wouldn't.","soft","closed","base","mid")
    call cho_main("And neither would you!","smile","narrow","angry","L")
    call cho_main("Which is why we brought you here...","open","base","base","mid")
    call cho_main("To have some fun!","base","narrow","angry","mid")

    call her_main("Sir, I demand that you stop this nonsense!","open","angry")
    call cho_main("I don't think that's very likely to happen, Granger...","soft","narrow","angry","mid")
    call cho_main("We both know what he would prefer...","soft","closed","base","mid")
    m "..."
    call cho_main("And who he prefers...","smile","angry","angry","mid")
    call her_main("You think that's he prefers you over me?{w} Please...","soft","angryL")
    call cho_main("Why don't we just ask him?","base","narrow","base","mid")
    call cho_main("Tell us, Professor...","soft","narrow","base","R")
    call cho_main("How do you like the athletic, immaculate, nude body of your favourite student?","smile","narrow","angry","mid")
    call cho_main("It's so much better than Miss Granger's, isn't it?","base","narrow","angry","mid")
    call ctc

    $ cho_strip_complete = True # Unlocks Wardrobe on next summon.

    call cc_pf_strip_T1_hermione

    jump end_cho_strip_event


label cc_pf_strip_T1_E3: # Repeats
    m "[cho_name], why don't you come a bit closer?"
    call cho_main("Of course, [cho_genie_name]...","base","narrow","base","mid")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("","base","base","base","R", xpos="mid", ypos="base", trans="fade")
    call ctc

    g9 "I’m in the mood for another strip-tease!"
    call cho_main("Funny you should say that, [cho_genie_name]...","soft","base","raised","downR")
    call cho_main("","horny","narrow","angry","mid")
    pause.4

    # Remove top & robe.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    $ cho_cloth_pile = True
    show screen cho_chang
    with d3
    pause.5

    call cho_main("Because so am I!","base","narrow","angry","mid")
    call cho_main("Enjoy yourself, Sir...","soft","closed","base","mid")
    call cho_main("","base","narrow","angry","mid")
    pause.4

    # Remove bottom.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    show screen cho_chang
    with d3
    pause.5

    g4 "*Argh!* You little minx!"

    call cho_main("Are we going to invite Granger again?","quiver","narrow","raised","down")
    call cho_main("I would like to have some fun with her...","smile","narrow","angry","mid")
    call cho_main("Let her watch...","horny","narrow","angry","mid")
    pause.4

    # Remove bra.
    hide screen cho_chang
    $ cho_class.strip("bra")
    show screen cho_chang
    with d3
    pause.5

    g9 "The more, the merrier!"
    call cho_main("","base","narrow","angry","mid")
    pause.4

    # Remove panties.
    hide screen cho_chang
    $ cho_class.strip("panties")
    show screen cho_chang
    with d3
    call ctc

    call cho_main("Catch, [cho_genie_name]!","soft","base","base","mid")
    call nar("Cho throws her panties at you.")

    # Panties acquired message!
    $ has_cho_panties = True

    g9 "Nice!"
    call cho_main("I'd like to have them back after this, mind you.","soft","base","raised","R")
    m "Of course..."
    call cho_main("Anything else you'd like, Sir?","base","base","base","mid")

    menu:
        "\"Hop on my desk!\"":
            call cho_main("Sounds like fun idea, [cho_genie_name]!","base","closed","base","mid")
            call hide_characters
            show screen blkfade
            with d3
            call play_sound("desk")
            pause 2

            call cho_chibi("stand","on_desk","on_desk", flip=False)
            hide screen bld1
            hide screen blkfade
            with d3
            pause 1

            call cho_main("How is the view down there, Sir?","base","narrow","base","down")
            g9 "Couldn't be any better!"

            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call cho_chibi("stand","on_desk","on_desk", flip=True) # Facing the door.
            with d3
            pause.8

        "\"Let Granger have a good look at you!\"":
            call cho_main("I'll make sure of it, Sir!","quiver","narrow","angry","mid")

            call cho_walk(xpos="570",ypos="base", speed=2)

    call cho_main("Now, if you don't mind, Sir...","soft","base","base","R", xpos="mid", ypos="base", flip=True)
    call cho_main("I'd like you to call that \"Gryffindor slut\" to your office!","soft","base","base","L")
    g9 "On it!"
    pause.8
    call cho_main("(...)","annoyed","narrow","angry","L")
    m "(...)"

    call hide_characters
    hide screen bld1
    with d3
    pause.5

    # Hermione enters.
    call play_sound("door")
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call chibi_effect("thought","hermione")
    pause.8

    call her_walk(xpos="660", ypos="base", speed=2)

    call cho_main("","horny","narrow","angry","L", xpos="mid", ypos="base", flip=True)
    call her_main("You wanted to see me, Professor?","soft","closed", xpos="base", ypos="base")
    g9 "Yes, but I wasn't the only one."
    call her_main("(...)","annoyed","angryL")
    call cho_main("Hi, Granger!","smile","narrow","angry","L")
    call her_main("Let me guess, we are here to marvel at your insecurity again?","soft","closed")
    call cho_main("Granger, instead of spitting out insults, why don't you join me and have some fun for once?","soft","base","raised","L")
    call cho_main("Strip down for your headmaster as well, like you usually do...","smile","narrow","angry","L")
    call cho_main("Or would it bother you too much, now that I'm here?","horny","narrow","base","L")
    call her_main("*glare*","angry","angry")
    call cho_main("Maybe then you'd have a chance to win against me!{w} And earn some useless \"Gryffindor\" points while you're at it.","soft","base","base","L")
    call her_main("I don't think that will be necessary...","soft","closed")
    call cho_main("Well, we all already know how this is going to turn out don't we, [cho_genie_name]?","soft","base","base","mid")
    call cho_main("My body is still better than Miss Granger's, isn't it?","smile","angry","angry","L")
    call her_main("","annoyed","angry")
    call ctc

    call cc_pf_strip_T1_hermione

    jump end_cho_strip_event


label cc_pf_strip_T1_hermione: # Call label. # Almost complete. Missing 1 menu branch.

    menu:
        "\"Definitely!\"":
            $ cho_mood = 0
            $ her_mood += 10

            #cho "You see, Granger..."
            #cho "Tits aren't everything!"

            call her_main("What?!","open","wide")
            call cho_main("See, I told you! How could he pick a walking bush on legs over this!","smile","narrow","angry","L")
            call her_main("","angry","angry")
            call cho_main("Now tell her. Tell her why my body is superior compared to hers.","soft","closed","base","mid")
            m "..."
            m "Well, you're more flexible for one..."
            call cho_main("That's right, I am!","soft","wide","base","mid")
            call her_main("*Humph.*","annoyed","angryL")
            call cho_main("And? What else?","smile","narrow","base","L")
            g4 "And Cho's thighs are probably the most impressive ones I’ve seen in the last hund-... decade or more!"
            call her_main("Well in that case...","soft","closed")
            call her_main("In that case I’ll give you a great opportunity to stare at them indefinitely.","angry","angry")
            call cho_main("What are you talking about, Granger?","soft","narrow","raised","L")

            # Hermione walks towards the desk to pick up Cho's clothing.
            call her_walk(xpos="desk", ypos="base", speed=1.6)
            pause.2
            if cho_chibi_xpos == 570: # Close to the middle.
                call cho_chibi("stand","570","base", flip=False) # Facing the desk.
                with d3
            pause.6

            call cho_main("What are you doing?","soft","narrow","base","L", ypos="head", flip=True)

            # Hermione picks them up and runs off.
            call bld("hide")
            pause.2
            call play_sound("equip")
            $ cho_cloth_pile = False
            pause.5

            call cho_main("My clothes!","angry","wide","base","L", ypos="head", flip=True)

            call play_sound("running")
            call her_walk(xpos="door", ypos="base", speed=1.4)
            call her_chibi("stand","door","base", flip=False)
            with d3

            call her_main("Hey seeker, looks like someone will have to seek their way to their dorm without any clothes tonight.","open","angry", ypos="head")
            call cho_main("Hey!","angry","narrow","angry","L", ypos="head", flip=True)

            # Hermione leaves out of the door.
            hide screen bld1
            call her_chibi("stand","door","base", flip=True)
            with d3
            pause.2

            call her_chibi("leave")

            # Cho runs out the door.
            if cho_chibi_xpos == 350: # On desk
                call play_sound("climb_desk")
                show screen blkfade
                with d3
                pause 1

                hide screen bld1
                hide screen blkfade
                call cho_chibi("stand","desk","base", flip=True)
                with d3
                pause.2

                call cho_main("Give them back you bitch!","scream","narrow","angry","L", ypos="head", flip=True, trans="hpunch")

                call play_sound("running")
                call cho_walk(action="leave", speed=1.2)

            else:
                hide screen bld1
                call cho_chibi("stand","570","base", flip=True) # Facing the door.
                with d3
                pause.2

                call cho_main("Give them back you bitch!","scream","narrow","angry","L", ypos="head", flip=True, trans="hpunch")

                call play_sound("running")
                call cho_walk(action="leave", speed=1)

            call bld
            m "Did she just?"
            m "(...)"
            m "I don't think she's coming back..."

            return

        "\"Not even close.\"":
            $ cho_mood += 15
            call cho_main("Not even clo-","soft","wide","base","mid")
            call her_main("","smile","baseL")
            call cho_main("Professor, could you please repeat that for me?","angry","closed","angry","mid")
            m "Hermione's body is superior."
            call her_main("No surprise there...","base","baseL")
            call cho_main("No!{w} It clearly isn't!","scream","angry","angry","mid", trans="hpunch")
            call cho_main("Are you mad, old man?","angry","narrow","angry","mid")
            call her_main("Don't use that tone with the headmaster...","soft","closed")
            call cho_main("Nobody asked you!","angry","angry","angry","L")
            call her_main("He's the wisest wizard at our school...{w} Surely his word should be final...","smile","glance")
            m "I'd use the word astute but I'll take wise..."
            call cho_main("Why are you siding with her all of a sudden?","annoyed","narrow","angry","mid")
            m "Good question."
            m "Miss Granger, why don't you show Miss Chang why your body is superior to hers..."
            g9 "Share with us your two most compelling arguments..."
            call her_main("Sir?","soft","wink")
            call cho_main("He's talking about your \"tits\", you dimwit!","angry","closed","angry","mid")
            call her_main("(...)","clench","down_raised") # Embarrassed
            call cho_main("","annoyed","narrow","angry","mid")
            g9 "Yes Miss Granger!{w} Your very round{w}, handsomely sphered{w}, perfectly sized{w}, very voluptuous and-"
            call her_main("I got it, Professor!","clench","worriedCl")
            call cho_main("(Cow tits...)","annoyed","narrow","angry","R")
            call her_main("Here...","base","glance")

            # Hermione lifts her top
            call set_her_action("lift_top")

            call her_main("","base","glance")
            call ctc

            call her_main("Have a good look.","soft","glance")
            call cho_main("(...)","annoyed","narrow","angry","downR") # Tries to look away.
            call her_main("And you'd better take in what a real pair looks like, slut.","smile","angryL")
            call cho_main("I'd rather not, or I might barf...","soft","narrow","angry","R") #
            g9 "Very nice, Miss Granger!"

            menu:
                "\"Ten points to Gryffindor!\"":
                    $ gryffindor += 10
                    call cho_main("(...)","annoyed","narrow","angry","mid")
                    call her_main("Thank you.","soft","glance")

                "\"Fifty points to Gryffindor!\"":
                    $ cho_mood += 10
                    $ gryffindor += 50
                    call cho_main("(Fifty?!)","soft","wide","base","mid") # Shocked
                    call her_main("Thank you.","soft","glance")
                    call cho_main("","angry","closed","angry","mid")

            g9 "For exposing those magnificent breasts."

            call set_her_action("none")

            call her_main("Any time, Professor.","soft","glance")
            call cho_main("(I bloody hate her!)","angry","angry","angry","L")

            call her_main("If you don't mind, Sir.","open","baseL")
            call her_main("I'd like to leave now.","soft","base")
            call cho_main("By all means, just go already.","soft","narrow","angry","R")
            call her_main("Did something not go as you expected?","smile","baseL")
            call her_main("Did you think having me here when you exposed yourself would make me jealous...","soft","closed")
            call cho_main("(...)","annoyed","angry","angry","L")
            call her_main("Thank you for inviting me, Professor.","soft","glance")
            call her_main("I \"did\" enjoy this little obscene \"freak-show\" you arranged for me...","grin","glance")
            call cho_main("You'll regret this, Granger!","angry","narrow","angry","L")

            if daytime:
                call her_main("Have a nice day, Professor.","soft","closed")
            else:
                call her_main("Have a good night, Professor.","soft","closed")

            m "(...)"
            call her_main("See you in class Chang!","grin","glanceL")
            call cho_main("*Tzzzz!*","angry","closed","angry","mid")
            call cho_main("Cow...","annoyed","narrow","angry","R")

            # Hermione leaves.
            call her_walk(action="leave", speed=2)

            # Cho stands close to your desk.
            call hide_characters
            show screen blkfade
            call cho_chibi("stand","desk","base", flip=False)
            with d3

            hide screen blkfade
            call cho_main("I thought you were on my side, Sir!","soft","narrow","angry","mid", xpos="mid", ypos="base", flip=False, trans="fade")
            m "I'm on nobody's side, because nobody is on my side..."
            call cho_main("You were supposed to have my back! Not Granger's!","angry","closed","angry","mid")
            call cho_main("That \"whore\" doesn't deserve your praise!","soft","narrow","angry","mid")
            m "She made some good arguments..."
            g9 "\"A couple\" of good arguments, to be precise!"
            call cho_main("They're barely larger than mine...","annoyed","narrow","base","downR")
            call cho_main("You'll see, Sir.{w} I'm better than her.{w} And I'll prove it to you...","soft","narrow","angry","mid")
            g9 "Well, that is yet to be seen."

            # Cho gets dressed.
            hide screen cho_chang
            $ cho_class.wear("all")
            $ cho_cloth_pile = False
            hide screen blkfade

            call cho_main("Sir, my *uhm*...{w} my panties...","soft","base","angry","R", xpos="mid", ypos="base", trans="fade")
            m "Oh, of course..."
            call cho_main("","annoyed","narrow","angry","mid")
            pause.5
            m "Give me just a moment..."
            $ renpy.sound.play("sounds/sniff.mp3")
            call nar("You miss Chang's panties one last sniff before handing them back to the girl.")
            g4 "There."
            call cho_main("(Pervert...)","annoyed","narrow","angry","R")
            call cho_main("I think it's time for me to go now.","soft","closed","angry","mid")
            call cho_main("Until next time, [cho_genie_name].","soft","narrow","angry","mid")

            # Cho leaves.
            call cho_walk(action="leave", speed=2.5)

            call bld
            g4 "Damn!"
            g9 "For somebody that does a lot of exercising, she smells really nice!"
            m "Maybe I should be a bit nicer to her next time..."

            $ has_cho_panties = False

            return


        "\"Let Hermione assess you.\"":
            $ her_mood += 6
            call cho_main("Her?","soft","wide","base","mid")
            call her_main("I couldn't care less about the way she looks!","soft","angry")
            call cho_main("(...)","annoyed","narrow","angry","L")
            m "Are you sure about that? I've seen you staring..."
            call cho_main("","base","narrow","angry","L")
            call her_main("Because she just so happens to be standing there, butt naked!{w} In your office!","angry","angryCl")
            m "I'd like you to rate Miss Chang's figure, truthfully, and to the best of your ability."
            call her_main("Really? Do I have to?","annoyed","base")
            g9 "You do! I'd really like to hear your opinion on Miss Chang's shamelessly exposed body!"
            call cho_main("*Mhmm*","base","closed","base","mid") # Self assured.
            call her_main("Fine...","soft","angryL")
            call her_main("\"Poor\", I'd say...","soft","closed")
            call cho_main("How dare you!{w} You snobby skunk!","scream","angry","angry","L", trans="hpunch")
            call her_main("","base","baseL")
            m "(Is that better or worse than \"troll\"?)" # Snape explained school ratings during the match.
            call cho_main("Our Professor asked you to rate my body truthfully!","angry","angry","angry","L")
            call her_main("Which I did!{w} And it's at \"dreadful\" now!","soft","closed")
            call cho_main("\"Dreadful\"?!","soft","wide","base","mid")
            call cho_main("You're a lying bitch, Granger!","angry","closed","angry","mid")
            call her_main("Sir, you can't let her talk to me like that!","angry","angry")
            m "Bitch isn't even a proper curse word."
            m "You can say that on TV..."
            call cho_main("Granger, why don't you tell us which part of my immaculate body deserves such a poor rating?","soft","narrow","angry","L")
            call her_main("Very well...","soft","closed")
            call her_main("For one, you are a narcissistic bitch!{w} That makes the presumption her body is superior to all others...","open","angry")
            call cho_main("Because it is.","smile","narrow","angry","mid")
            call her_main("Not to mention that you have even fever curves than some of the boys I know...","grin","angry")
            call cho_main("","annoyed","narrow","angry","mid")
            call her_main("Maybe once your Quidditch endeavours all fail, you can apply for a profession to model male underwear...","soft","closed")
            call cho_main("I wonder where you're getting \"your\" undergarments from...","soft","closed","base","mid")
            call cho_main("Stealing them from Madam Pomfrey, are you?","smile","narrow","angry","mid")
            call her_main("I do not!!!","open","wide")
            m "Girls, we all know what really counts is how we appear on the inside."
            call her_main("","angry","angryCl")
            call cho_main("Oh- Shut up!","angry","narrow","angry","mid")
            call her_main("Professor, you're the one who continuously asks us to expose ourselves!","soft","angry")
            m "Well yes. I also never claimed that \"I\" was pretty on the inside."
            m "You of all people should know better by now..."
            call her_main("Despicable...","angry","angryL")
            call cho_main("Don't worry, Granger!","soft","narrow","angry","L")
            call cho_main("If you were to start doing hourly exercises, our Professor might even be attracted to you by the end of the year...","soft","closed","raised","mid")
            call her_main("Hourly exercises?","soft","wide") # Shocked
            call cho_main("But I wouldn't say all hope is lost!","smile","narrow","angry","L")
            call cho_main("While your figure might be a bit repulsive on the eyes...","soft","closed","base","mid")
            call cho_main("I don't mind looking at those \"huge melons\" of yours.","soft","narrow","base","L")
            call her_main("How dare you talk of them like that!","angry","angryL")
            g9 "*Heh*... melons..."
            call her_main("Sir, I’d like to leave now.","open","angry")

            call cho_main("Already missing your books, are you?","annoyed","narrow","base","L")
            call her_main("I am not.{w} And I don't appreciate being made fun of!","angry","angryCl")

            if daytime:
                call her_main("Good day, Sir.","soft","angry")
                call cho_main("See ya around, Granger...","smile","narrow","angry","L")
                call her_main("*Hmpf*","annoyed","angryL")

            else:
                call her_main("Good night, Sir.","soft","angry")
                call cho_main("Nighty-night, Granger...","soft","narrow","angry","L")
                call her_main("*Tzzzzzh!*","annoyed","angryL")

            # Hermione leaves.
            call her_walk(action="leave", speed=1.5)

            show screen blkfade
            call cho_chibi("stand","desk","base", flip=False)
            with d3

            hide screen blkfade
            call cho_main("I have to say, [cho_genie_name], doing these favours is fun!","smile","narrow","base","mid", xpos="mid", ypos="base", flip=False, trans="fade")
            m "I'm glad you're enjoying yourself."
            call cho_main("Believe me, Sir. I am.","smile","narrow","angry","mid")
            call cho_main("","horny","narrow","angry","mid")
            pause.4

            # Cho gets dressed.
            hide screen cho_chang
            $ cho_class.wear("all")
            $ cho_cloth_pile = False
            show screen cho_chang
            with d3
            pause.5

            call cho_main("Now, if you excuse me...","soft","base","base","mid")

            if daytime:
                call cho_main("I have to head back to classes.","soft","base","base","R")
                m "I still got your-"
                call cho_main("See ya next time, [cho_genie_name]!","smile","narrow","angry","mid")
            else:
                call cho_main("I have to head back to our dorms.","soft","base","base","R")
                m "Don't you want your-"
                call cho_main("Sweet dreams, [cho_genie_name]!","smile","narrow","angry","mid")

            call cho_walk(action="leave", speed=2.5)

            call bld
            g9 "Nice, I still got her panties!"

            $ has_cho_panties = True

            return



### Tier 2 (pre Gryffindor) ###

label cc_pf_strip_T2_E1:

    # Cho asks if you could give her house points for once.
    call cho_main("But, before that, may I ask you about something?","soft","base","sad","mid")
    m "Sure..."
    call cho_main("Does Granger only ask for house points? To do this sort of thing?","open","base","base","mid")
    m "She does."
    call cho_main("And, just out of curiosity, how much do you pay her for such a favour?","soft","base","base","R")
    call blktone
    m "(What should I tell her? Should I exaggerate a bit to get her more motivated?)"

    menu:
        "\"Five points.\"":
            $ current_payout = 5

            call hide_blktone
            call cho_main("Only five points? I expected more, Sir.","horny","narrow","sad","downR")
            call cho_main("I've gotten more points for answering Quidditch questions to Madam Hooch!","open","base","base","mid")
            m "I'm sure that wasn't the only reason she gave you those points..."
            call cho_main("Just to be clear... She completely undresses?{w} For five mere points?","soft","narrow","raised","mid")
            m "Yep."
            call cho_main("What a slut! I can't believe it!","smile","narrow","angry","R")
            g9 "Sometimes I only reward her with two points!{w} If she doesn't sway her hips enough..."
            call cho_main("You don't say!","smile","base","angry","mid")
            m "Why were you asking?"

        "\"One-hundred points!\"":
            $ current_payout = 30
            $ cho_mood += 6

            call hide_blktone
            call cho_main("So many? But...","soft","wide","base","mid")
            call cho_main("Sir, don't you think that's a bit outrageous?","open","closed","angry","mid")
            call cho_main("People in house \"Ravenclaw\" work hard to earn that amount of points!","open","base","raised","L")
            call cho_main("And you're telling me that you give that cow \"one-hundred bloody points\"{w}, for showing you her tits?!","angry","narrow","angry","mid")
            m "Not just her tits, [cho_name]."
            g4 "Everything!!!"
            call cho_main("Sir, how can you agree to such a thing?","angry","closed","angry","mid")
            m "Calm down, would you. I was joking..."
            m "She doesn't get that many points from me. It's closer to thirty..."
            call cho_main("That's still far too many points!","annoyed","narrow","angry","mid")
            m "Why are you even so invested in this all of a sudden?"
            call cho_main("(...)","annoyed","narrow","angry","R")

    call cho_main("I thought,...{w} maybe...{w} just this once...","angry","base","sad","down")
    call cho_main("You could give me house points as well?","soft","base","sad","mid")
    m "Really? I thought you didn't give a flying fuck about that house cup?"
    call cho_main("Sir?!","angry","wide","base","mid") # Shock
    m "Why do you want points all of a sudden?"
    call cho_main("I have my reasons....","annoyed","narrow","angry","mid")
    call cho_main("And, as I've said, this will be a one-time-only request of mine. I promise!","open","base","base","R")
    call cho_main("I'm a fair sportsman, [cho_genie_name]. You know that...","base","closed","base","mid")
    call cho_main("I'd never subject myself to earning house-points this way!","soft","narrow","angry","mid")
    call cho_main("Unlike a certain other student at this school...","angry","narrow","angry","R")
    m "And yet you asked me for that very thing?{w} I wonder why, Miss Chang..."
    call cho_main("Just as additional motivation, Sir!","angry","closed","sad","mid")
    m "Additional motivation, so so..."
    call cho_main("Yes.","soft","narrow","sad","mid")
    m "Does that motivation come from the noble deed of earning those points for your house?"
    g4 "Or getting that dirty, corruptive feeling from the way you acquired them?"
    call cho_main("(...)","angry","closed","sad","mid") # Embarrassed
    g9 "Stripping down for points! Don't you know what that would make you?"
    call cho_main("*Uhm*","soft","narrow","sad","mid")
    m "You'd be just as cheap as Hermione..."
    call cho_main("Please, Sir.{w} Don't compare me to that whore!","annoyed","narrow","angry","mid")
    g9 "Yes, Miss Chang. A whore!"
    call cho_main("That's not why-","angry","closed","sad","mid")
    call cho_main("Please, Sir. Just this once!","soft","narrow","sad","mid")
    call cho_main("I won't ask for payment ever again!","soft","base","sad","mid")
    call cho_main("I'll strip naked for you, for... [current_payout] house points!","angry","closed","sad","mid") # Embarrassed

    menu:
        "\"Yes! Make your house proud, you slut! Earn those points!\"":
            call cho_main("Yes, Sir!","base","narrow","angry","mid")
            g9 "Take of those panties!"

        "\"No. You are better than that...\"":
            $ cho_mood += 6
            call cho_main("But Sir! I asked for them!","soft","wide","sad","mid")
            m "And I'm sure you wouldn't want to sink as low as Miss Granger, would you?"
            call cho_main("Yes! I would!","angry","closed","angry","mid")
            call cho_main("That's the entire reason I want them!!!","open","narrow","angry","R")
            m "Seriously?"
            call cho_main("Give me those points, or I will walk right out of here!","open","narrow","angry","mid")
            m "Fine. If you're that insistent on [current_payout] meager points..."
            call cho_main("Thank you.","soft","closed","base","mid")





    jump main_room
