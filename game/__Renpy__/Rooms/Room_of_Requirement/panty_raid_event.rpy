

label panty_raid_event: #LV.8 (Whoring = 21 - 23)
    call room("main_room")
    show screen blkfade
    with d3

    call reset_menu_position

    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"

    m "This event is written by WaxerRed."


    menu:
        "Path 1":
            $ pathvalue = 0
        "Path 2":
            $ pathvalue = 1
        "Path 3":
            $ pathvalue = 2
        "Path 4":
            $ pathvalue = 3

    call hide_blkfade

    #First Level
    if pathvalue == 0:
        m "[hermione_name] How would you feel about going out and earning 35 points for your house?"
        call her_main("I would love too... if it didn't involve me humiliating myself in front of my peers.", mouth="open", eye="base")
        m "Well then perhaps today is your lucky day."
        call her_main("Really?", mouth="normal", eye="base")
        m "Yes in fact you may wish to remain as unseen as possible during your activities today."
        call her_main("", mouth="soft", eye="squint")
        call her_main("", mouth="normal", eye="base")
        m "I would like for you to recover the most revered of sacred objects in this academy, no in the world!"
        call her_main("Oh! You want me to recover a magical artifact?", mouth="open", eye="surprised")
        call her_main("", mouth="normal", eye="base")
        m "Something like that."
        call her_main("I am glad you're finally asking me to properly utilize my abilities as one of Hogwarts top students.", mouth="smile", eye="happy")
        call her_main("I only wish you would have asked this of me early! Never fear I am happy to complete a task such of this for you!",mouth="open",eye="base")
        call her_main("", mouth="normal", eye="base")
        m "Exactly, now all the information I have for this 'artifact' is an ancient riddle. Are you ready?"
        call her_main("Of course [genie_name]", mouth="open", eye="soft")
        call her_main("", mouth="normal", eye="base")
        m "Good, now here we go. \"I am sought by many, yet the same number already possess me.\""
        call her_main("Mmmm I see, alright.", mouth="annoyed", eye="squint")
        m "\"The more I am used, the more valuable I become.\""
        call her_main("The sword of Gryffindor...no no the elder wand?", mouth="open", eye="base")
        call her_main("", mouth="normal", eye="base")
        m "\"The only thing men covet more than my form is the secret I hid.\""
        call her_main("Interesting...Interesting.", mouth="open", eye="base")
        call her_main("", mouth="normal", eye="base")
        m "... \"Sometimes I am plain and white, but I look my best when I am skimpy and black.\""
        call her_main("", mouth="annoyed", eye="annoyed")
        m "No wait! \"skimpy and pink.\""
        call her_main("This is an ancient riddle?")
        m "Hush, \"In order to find me you must bend down low to hell, then look up to heaven.\""
        call her_main("...", mouth="disgust", eye="frown")
        m "What else, what else... \"No schoolgirl fetish would be complete without me.\""
        call her_main("[genie_name].")
        m "\"The answer is on page 74, Spell: seitnaP backwards.\""
        call her_main("PROFESSOR!", mouth="scream", eye="wide")
        call her_main("", mouth="normal", eye="base")
        m "Hmm yes? Did you figure it out?"
        call her_main("If you wanted my -ahem- 'undergarments' you could have just asked.", mouth="disgust", eye="suspicious")
        m "Panties? My jove I think you got it girl. Incredible!"
        call her_main("[genie_name], my classes start soon can I just give them to you and get my points?", mouth="upset", eye="frown")
        m "So eager so eager, but where's the challenge in giving me yours?"
        call her_main("Huh?", mouth="annoyed", eye="surprised")
        m "This is meant to be a treasure hunt! Go out and find someone's panties out in the world!"
        call her_main("But I-how?", mouth="open")
        m "You're a bright young gal, I'm sure you'll think of something."
        call her_main("I'll do my best, [genie_name]", mouth="smile", eye="happy")
        call her_walk("mid","leave",2.5) #leave makes her walk to door and disappear with door noise

        show screen blkfade
        call hide_blkfade

        call her_walk("door","mid",2.5) #door is point A, mid is point B, 2.5 is how long it takes for her to walk.

        call her_main("My assignment.", mouth="smile", eye="happy")
        "She elegantly drops a pair frilly pink panties on your desk."
        call her_main("And extra credit.")
        "She adds a matching pink lingerie bra to the spoils on your desk."
        g9 "You absolute minx!"
        call her_main("I'll take that as a compliment [genie_name]")
        g9 "You've outdone yourself, how did you manage this?"
        call her_main("A good witch never revels her secrets.", mouth="open", eye="wink")
        m "Well you've certainly left me impressed."
        call her_main("Does that mean I earned some extra house points?", mouth="grin", eye="happy")
        m "I think the situation calls for it. 90 points to Gry-... [hermione_name]"
        call her_main("Yes?", mouth="upset", eye="concerned")
        m "Why is there a price tag on these?"
        call her_main("...!", mouth="shock", eye="wide")
        call her_main("Uh.....Well the person I stole these from must have forgotten to take them off.", mouth="open", eye="squint")
        m "I see...Well whoever you took the from must be a bit slow to forget something so simple, don't you agree?"
        call her_main("Uhh...", mouth="base", eye="down")
        m "They're an idiot?"
        call her_main("Yeah, they're an idiot.", mouth="crooked_smile", eye="worried")
        m "A bloated scatterbrained idiot!"
        call her_main("[genie_name]!", mouth="scream", eye="wide")
        m "Yes, [hermione_name]?"
        call her_main("Fine...", mouth="annoyed", eye="annoyed")
        call her_main("it was me!", mouth="angry", eye="down")
        call her_main("I couldn't do it, so I bought them at a shop!", mouth="clench", eye="narrow")
        g4 "You're the bloated, scatterbrained idiot?"
        m "[hermione_name]..."
        call her_main("I'm surprised that despite regularly forgetting your own name, you remembered all that.", mouth="disgust", eye="angry")
        m "Do not question the great Doubledoor!"
        call her_main("Sir, this has been embarrassing enough can I please just be dismissed?", mouth="annoyed", eye="annoyed")
        menu:
            "\"Cheaters never Prosper.\"":
                m "Well, I must say I am disappointed with your actions [hermione_name]"
                call her_main("I am sorry [genie_name], it won't happen again!", mouth="soft", eye="down")
                m "I should hope not, dismissed."
                call her_main("Yes sir.")
                call her_walk("mid","leave",2.5)
            "\"Yes, they do.\"":
                m "Well, I must say I am impressed with your actions [hermione_name]."
                call her_main("I am sorry [genie_name] I wo- wait what?", mouth="shock", eye="shocked")
                m "I never imagined you possessed such \"out of the box\" problem solving!"
                call her_main("Really?", mouth="open", eye="happy")
                m "You fumbled the landing, but otherwise cheated like a pro!"
                call her_main("Thank you...", mouth="smile", eye="soft")
                call her_main("Cheated?", mouth="smile", eye="soft")
                m "Exactly! Now I won't overburden you with compliments take your house points and go. 35 points to Gryffindor!"
                call her_main("Thank you [genie_name]", mouth="smile", eye="base", cheeks="blush")
                call her_main("{size=-5}I guess?{/size}")
                call her_walk("mid","leave",2.5)

    #Second Level
    if pathvalue == 1:
        call her_walk("door","mid",2.5)
        m "Up for trying your hand at that favour again?"
        call her_main(" Do I have a choice?", mouth="open", eye="annoyed")
        m "Certainly, if you don't mind those 'Slytherin Harlots' taking the house cup!"
        call her_main(" I Do mind!", mouth="scream", eye="wide")
        m "Then you better head on out and steal some girl's panties!"
        call her_main("...35 points?", mouth="clench", eye="base")
        m "35 points."
        call her_main("Fine.", mouth="upset", eye="glanceL")
        call her_walk("mid","leave",2.5)

        show screen blkfade
        with d3
        call hide_blkfade

        call her_walk("door","mid",2.5)
        "She drops a slightly used pair of plain panties on your desk."
        m "I don't see any tags, did you learn from your previous error?"
        call her_main(" Yes sir.", mouth="disgust", eye="down")
        menu:
            "\"Let her Go.\"":
                m "Well quality leaves a bit to be desired but a good step forward. 35 points to Gryffindor."
                call her_main(" Thank you, [genie_name]", mouth="open", eye="frown")
                call her_walk("mid","leave",2.5)
            "\"Ask for details.\"":
                m "So, who was the lucky lady?"
                call her_main("In this scenario, no one.", mouth="open", eye="base")
                m "Come on now."
                call her_main("Ginny Weasley.", mouth="open", eye="base")
                m "Interesting {size=-5}I don't know who that is.{/size} How did you do it?"
                call her_main(" I offered to do her laundry along with mine this week.", mouth="open", eye="down")
                m "And?"
                call her_main(" And while I was working, I grabbed one of her *ahem* 'panties' and shoved them in my pocket.", mouth="clench", eye="down")
                m "And?"
                call her_main(" And if she asked what happens... I'll just say they must have gotten lost in the wash.", mouth="smile", eye="happy")
                m "And?"
                call her_main(" And... that’s really it.", mouth="open", eye="base")
                m "How dull, 35 stupid house points to Gryffindor."
                call her_main(" Do those count the same as regular points?", mouth="annoyed", eye="annoyed")
                m "I guess..."
                call her_main("Goodnight then sir.", mouth="open", eye="base")
                call her_walk("mid","leave",2.5)

    # Third Level
    elif pathvalue == 2:
        call her_walk("door","mid",2.5)
        m "Hello [hermione_name], Up for another panty raid?"
        call her_main("...", mouth="annoyed", eye="annoyed")
        m "35 points!"
        call her_main("...", eye="glance")
        m "Surely that's worth risking your entire reputation over!"
        call her_main("...", mouth="upset", eye="angryCl")
        call her_main("Fine.", mouth="mad", eye="angry")
        m "That ‘a girl."
        call her_walk("mid","leave",2.5)

        show screen blkfade
        call hide_blkfade

        call her_walk("door","mid",2.5)
        m "Hello [hermione_name], you're looking good."
        call her_main("Uh-huh. Sir, if I'm not mistaken Hogwarts does not have a 'linguistic' class, do we?", mouth="open", eye="base")
        call her_main("", mouth="normal", eye="base")
        m "(Why is she asking me? Oh Right 'headmaster' Rumbleboar)"
        m " Do you really think we have a class you don't know about?"
        call her_main("True...then, do you know how many \"Connie's\" attend Hogwarts.", mouth="open", eye="base")
        call her_main("There aren't any in Gryffindor or Ravenclaw I believe, but I'm not sure for some of the other houses.", mouth="open", eye="soft")
        m "I feel as though I am missing some context."
        call her_main("Uhmmm... alright, I was in their Gryffindor girl’s dorm... working on my 'task.'")
        m "The perfect hunting grounds."
        call her_main("I am loathe to agree with you but yes. I had the pick of the litter with no absence of choice. Speaking of...")
        "She drops a bunched-up ball of about half a dozen girl's panties on your desk, coming in an array of different sizes, designs and colours."
        call her_main("I usually don’t conduct such a shotgun approach to work but...", mouth="smile", eye="happy", cheeks="blush")
        m "In this instance it served you well, full marks for stealing panties from your schoolmates."
        call her_main("That would fluster me, if I hadn't told my dorm mates time and time again, it is all of our responsibilities to keep our dorm tidy.", mouth="annoyed", eye="base")
        call her_main("Loss of said property is just desserts for leaving their undergarments strewn around like a hurricane blew through their drawers.", mouth="open", eye="base")
        m "Yes, Yes, but how does this connect back to a ‘Connie’?"
        call her_main("Right... Well, I obviously choose a time that I believed all my dorm mates would be gone.", mouth="smile", eye="happy")
        call her_main("But, just as I was shoving the last pair into my bag, Katie Bell walked in...", mouth="concerned", eye="closed")
        call her_main("She caught me red handed!", mouth="shock", eye="shocked")
        m "Or caught silky handed! Panty handed? Damn this sounded better in my head, give me a minute I can come up with something that works..."
        call her_main("I've never been more embarrassed in my entire life!", mouth="soft", eye="concerned", cheeks="blush")
        m "Pff, as if you've never said 'that' before"
        call her_main("I mean it! And I was mortified standing there holding her panties while trying to stutter an excuse.", mouth="open", eye="concerned", cheeks="blush")
        m "And what did she do?"
        call her_main("Well...that's the odd thing, while I was floundering like a fish she was just grinning at me. And then she said and I quote-", mouth="open", eye="base")
        call her_main("\"Heh, I always had a feeling about you Granger. But if you want them, you'll need to do me a favor. Meet me tonight and we can help Connie with her Linguistic homework.\"", mouth="base", eye="baseL")
        m "Connie with her lingust?- oh."
        call her_main("As embarrassing as initial circumstances are, I would never turn down a request to help a student with homework! But I don't think we have a linguistic class or what Connie she was-", mouth="annoyed", eye="annoyed")
        m "Cunnilingus [hermione_name]. She was asking for Cunnilingus."
        call her_main("Huh? But she said she wanted study help.")
        m "It was a metaphor. She was assuming you were a bit more 'worldly' than you really are."
        call her_main("I am plenty worldly!", mouth="angry", eye="angry")
        call her_main(".... What’s Cunnilingus?", mouth="upset", eye="worried")
        m "Sigh, she was asking for Dinner beneath the bridge."
        call her_main("Dinner? But if she wanted to eat with me why didn't she-", mouth="open", eye="base")
        m "Metaphor, [hermione_name]. She wanted you to sip from her furry cup."
        call her_main("Huh?", mouth="annoyed", eye="annoyed")
        m "Muff Diving"
        call her_main("Stop not making sense!", mouth="clench", eye="angry")
        m "Are you really supposed to be this school’s top student? She was asking you to eat her out."
        call her_main("...What?", mouth="open", eye="soft")
        m "Alright work with me. She wanted you..."
        m "Still with me here?"
        call her_main("{size=-5}Yes obviously, does he think I'm an idiot?{/size}", mouth="annoyed", eye="frown")
        call her_main("She wanted me...", mouth="open", eye="soft")
        m "To take your tongue..."
        call her_main("Take my tongue?", mouth="clench", eye="suspicious")
        m "And stick it in her vagina"
        call her_main("WHAT?!", mouth="shock", eye="wide")
        call her_main("Why would she want that?!", mouth="upset", eye="frown")
        m "Because in my experience it feels awesome. Wait, did that make it sound like I have a vagin-"
        call her_main("You're wrong! She- She-", mouth="shock", eye="worried")
        m "What? Have you really never done it before?"
        call her_main("OF COURSE NOT!", mouth="angry", eye="angry")
        m "I mean, I assumed you didn't have any friends. But to get to your age and never eat another girl out? How shameful."
        call her_main("Not everyone in this school is as gross as you!", mouth="annoyed", eye="annoyed")
        m "well, there's one way to prove me wrong. Go find ‘Katie’ and ask her yourself."
        call her_main("Maybe I will...", mouth="open", eye="closed")
        call her_main("She'll, HOLD ON!", mouth="scream", eye="wide_stare")
        m "What?"
        call her_main("I-I-I-I-I", mouth="open", eye="worriedCl")
        m "Just spit it out!"
        call her_main("I was so nervous with her that I just said yes! She'll be expecting me soon!", mouth="mad", eye="concerned")
        m "Well, you better get to it [hermione_name]!"
        call her_main("But I- But I- I couldn't- ", mouth="open", eye="down", cheeks="blush")
        call her_main("I'll just have to inform her that it was a misunderstanding, yes that will have to do.", mouth="soft", eye="narrow")
        m "Sure, and risk her spilling the beans to your entire dorm that the proud Hermione Granger steals girls’ panties."
        call her_main("...", mouth="upset", eye="concerned")
        m "Hey, for sixty points would you let me watc-"
        call her_main("Absolutely not!", mouth="scream", eye="angry")
        call her_walk("mid","leave",2)

    #Fourth Level
    elif pathvalue == 3:
        call her_walk("door","mid",2.5)
        m "I have a riddle for you [hermione_name]"
        call her_main("Oh, this ought to be fun. You can make it a 'hard' one [genie_name].", mouth="grin", eye="happy")
        m "\"I am as soft and pure as a baby kitten, though far more desirable.\""
        call her_main("Hmmmm...", mouth="soft", eye="concerned")
        call her_main("Boobs? Is it a Titjob?", mouth="open", eye="base")
        call her_main("", mouth="normal", eye="base")
        m "Nope, in this case contrary to a titjob, it being small and tight is usually more enjoyable here."
        call her_main("Sex?", mouth="annoyed", eye="suspicious")
        m "Nope... \"While boys may want me, they wouldn’t be caught dead ever just buying me for themselves.\""
        call her_main(" Well that definitely rules out sex.", mouth="open", eye="baseL")
        m "\"The less of me there is, the more...'desirable' I become to behold.\""
        call her_main(" Oh! Oh! Panties!", mouth="crooked_smile", eye="closed")
        g9 "Spot on."
        call her_main(" Do you want mine or someone else’s?", mouth="smile", eye="happy")
        m "Someone else's if you don't mind, [hermione_name]."
        call her_main(" On it! I'll be back soon.", mouth="grin", eye="happy")
        call her_walk("mid","leave",2.5)

        show screen blkfade
        call hide_blkfade

        call her_walk("door","mid",2.5)
        call her_main(" Hello my sweet [genie_name], I hope I didn't keep you waiting long... it took longer than expected.", mouth="smile", eye="happy")
        "She drops a pair of laced white panties on your desk."
        m "No trouble at all [hermione_name]. And you have excellent taste as always."
        call her_main("You're too kind [genie_name].", mouth="grin", eye="happy", cheeks="blush")

        hide screen genie
        ">You take your cock out and start stroking it..."
        call gen_chibi("jerking_off_behind_desk")
        call her_main("Mmmm, [genie_name] need any help with that?", mouth="base", eye="ahegao_raised", cheeks="blush")
        m "These already feel a little damp in the middle. Why don’t you tell me why that is?"
        call her_main("Oh you know, girls will be girls and all.", mouth="open", eye="ahegao", cheeks="blush")
        m "You know, charming the panties off someone is just a figure of speech."
        call her_main("Not any more...I'd like to think Katie was quite pleased with me.", mouth="smile", eye="ahegao", cheeks="blush")
        m "Katie? Katie Bell? The same delicious dyke that wanted you to clam joust with her?"
        call her_main("Maybe...Although, Katie keeps raising the fee every time I ask.", mouth="smile", eye="ahegao_squint", cheeks="blush")
        call her_main("Not that I mind.", mouth="open", eye="happy", cheeks="blush")
        m "Ugh!"

        call gen_chibi("cumming_behind_desk")

        call her_main("Oh, poor [genie_name], I had no idea you were so pent up. You can start calling me out more than twice a day, if two a day isn't enough.", mouth="smile", eye="baseL", cheeks="blush")

        call gen_chibi("came_on_desk")

        m "During the day? But what about your classes?"
        call her_main("Hmm? Oh well missing one or two wouldn't hurt. Especially if the headmaster has an important 'assignment' for me.", mouth="grin", eye="happy")
        m "I'll consider it. Now let's circle back to you, Katie and your binge of her minge."
        call her_main(" PROFESSOR! How dare you! I would never even think to shamelessly do something so heinous with a classmate and give you all the juicy details...", mouth="annoyed", eye="base")
        call her_main(" For less than 40 house points.", mouth="soft", eye="wink")
        m "Maybe next time [hermione_name]. I'm a little...spent for tonight."
        call her_main(" We both know you can go more if you wanted, but you’re right, we can leave things off for later.", mouth="soft", eye="base")
        call her_main(" See you tomorrow [genie_name].", mouth="smile", eye="wink")
        m "Later gator."

        call her_walk("mid","leave",2)

        m "...Hmmm. wait, I don't think I ever gave her points."


    call blkfade
    # call h_unequip_temp_outfit
    call her_chibi("hide")
    hide screen main_room

    jump enter_room_of_req
