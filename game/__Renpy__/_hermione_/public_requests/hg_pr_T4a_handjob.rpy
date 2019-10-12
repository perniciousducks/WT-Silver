

### Give Classmate A Handjob ###

label hg_pr_handjob:

    if hg_pr_handjob.counter < 1:
        m "{size=-4}(Tell her to give a handjob to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(face="happy", xpos="right", ypos="base", trans="fade")

    #Intro
    if hg_pr_handjob.counter == 0:

        if her_tier < 4 or her_reputation < 12:
            m "[hermione_name], I want you to do something different today..."
            call her_main("...?", "normal", "squint", "angry", "mid")
            m "I want you to give a handjob to one of your classmates."
            jump too_much

        m "[hermione_name], I want you to do something different today..."
        call her_main("...........", "soft", "base", "base", "mid")
        m "I want you to go out there and have sex with one of your classmates."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}", "shock", "wide", "base", "stare")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Now you have done it, [genie_name]! You crossed the line!", "angry", "base", "angry", "mid")
        her "I know I did sell you a couple of rather questionable favours in the past..."
        with vpunch
        call her_main("{size=+5}But THIS?!{/size}", "scream", "base", "angry", "mid", emote="01")
        her "I cannot believe that you would ask one of your pupils to... to..."
        call her_main("We are done here, [genie_name]!", "angry", "base", "angry", "mid", emote="01")
        m "Alright, alright, calm down, would you?"
        call her_main("I most certainly would not, [genie_name]! This is beyond inappropriate!", "scream", "closed", "angry", "mid")
        m "Alright, fine, maybe I really did cross some sort of line this time..."
        call her_main("You think [genie_name]?! You think!!?", "angry", "base", "angry", "mid")
        m "Yes, I apologize..."
        call her_main(".........", "annoyed", "narrow", "annoyed", "mid")
        m "How about we try something less... engaging instead?"
        call her_main("............", "upset", "closed", "base", "mid")
        m "I'll be willing to grant \"Gryffindor\" fifty five points."
        m "All I ask in return is..."
        call her_main("..........?", "angry", "base", "angry", "mid", cheeks="blush")
        m "...that you go out there and give some lucky boy a handjob..."
        call her_main("!!!......", "angry", "base", "angry", "mid")
        m "Oh, come on... Just a harmless handjob."
        call her_main("...","disgust","glance")
        m "Fifty five house points..."
        call her_main("..............", "annoyed", "narrow", "angry", "R")
        call her_main("I am glad that you came to your senses, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
        m "Oh, but of course. Thank you for keeping me in check."
        m "Are you up for it then?"
        call her_main("I am willing to give it a try...", "annoyed", "narrow", "angry", "R")
        m "Splendid... See you tonight then."

    elif her_tier < 5:
        m "Today's favour shall be..."
        call her_main(".........", "angry", "base", "base", "mid")
        m "A Handjob to the boy of your choosing!"
        call her_main("...again?","angry","down_raised")
        m "Sure, why not?"
        m "And another fifty five house points for the \"Gryffindor\" house of course."
        call her_main("..........","annoyed","worriedL")
        m "So... Are you up for that, [hermione_name]?"
        call her_main("I will see what I can do...", "annoyed", "narrow", "angry", "R")
        m "Splendid!"

    elif her_tier < 6:
        m "Ready to go have sex with one of your classmates yet?"
        stop music fadeout 1.0
        call her_main("What?","scream","wide_stare")
        call her_main("Of course not! I would never--", "scream", "closed", "angry", "mid")
        m "How about a handjob then?"
        call her_main("...............", "annoyed", "narrow", "angry", "R")
        m "Oh come on. You did it before."
        call her_main("hm..........", "annoyed", "narrow", "annoyed", "mid")
        her "Fifty five house points?"
        m "Naturally."
        call her_main("Well, alright... I'll see what I can do...","angry","down_raised")

    else:
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "[hermione_name]..."
        m "What do you think about giving one of your classmates another handjob?"
        call her_main("I don't mind, [genie_name].", "annoyed", "narrow", "worried", "down")
        m "Really?"
        call her_main("Yes... I mean, it's just a handjob...", "grin", "base", "base", "R")
        m "Great. Go have fun then!"
        m "And report back to me after your classes, as usual."
        call her_main("Of course, [genie_name].","base","happyCl")

    call her_walk(action="leave", speed=2.5)

    $ current_payout = 55
    $ hg_pr_handjob.inProgress = True

    jump end_hermione_event


label end_hg_pr_handjob:
    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ uni_sperm = False  #Universal sperm.
    $ aftersperm = False #Shows stains on Hermione's uniform.

    $ hg_pr_handjob.inProgress = False

    # Increase Points
    if her_tier == 4:
        if her_whoring < 15: # Points til 15
            $ her_whoring += 1

    if her_reputation < 15: # Points til 15
        $ her_reputation += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pr_handjob_T1_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #if her_whoring >= 15 and her_whoring < 18:

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], how did it go?"
    show screen blktone
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Quite awful... of course...", "annoyed", "squint", "angry", "mid")
    m "Just tell me what happened, [hermione_name]..."
    call her_main("I made a complete fool out of myself, that's what happened, [genie_name].","disgust","glance")
    her "....."
    m "..."
    call her_main("..........","annoyed","worriedL")
    call her_main("I don't want to talk about it...", "annoyed", "narrow", "angry", "R")
    her "You told me to go and touch a boy's penis and I did just that, [genie_name]."
    call her_main("Please, just let me have my points now, [genie_name]...", "open", "base", "base", "mid")
    m "I did not tell you to \"go and touch a boy's penis\", [hermione_name]."
    m "I told you to give one of your classmates a proper handjob."
    call her_main("Well, yes... that was what I meant of course...", "annoyed", "narrow", "annoyed", "mid")
    m "Did you make him cum, then?"
    call her_main("[genie_name]?", "open", "base", "base", "mid")
    m "Did his \"wee-wee\" shoot white stuff at you, [hermione_name]?"
    call her_main("Well...","annoyed","worriedL")
    call her_main("No, it did not...","normal","worriedCl")

    menu:
        "\"Well, this doesn't count then.\"":
            stop music fadeout 4.0
            call her_main("What?", "angry", "wide", "base", "stare")
            her "But, [genie_name], I..."
            m "If you didn't make him cum then that wasn't a proper handjob. Period."
            call her_main("But... But what was it then...?", "angry", "base", "base", "mid")
            m "How should I know? A cock massage?"
            call her_main("Aww...","angry","down_raised")
            her "But I really tried my best..."
            m "No handjob - no payment, [hermione_name]."
            call her_main(".....", "angry", "base", "base", "mid")
            m "You are free to go, [hermione_name]."
            call her_main(".........", "annoyed", "narrow", "angry", "R")

            call her_walk(action="leave", speed=2.5)

            $ her_mood +=9

            $ hg_pr_handjob.inProgress = False

            jump end_hermione_event

        "\"You shall only get half the payment then.\"":
            $ current_payout = 27 #Used when haggling about price of th favour.
            call her_main("Oh...?", "open", "base", "base", "mid")
            m "Is that a Problem, [hermione_name]?"
            call her_main("No [genie_name]... It's only fair I suppose...","angry","down_raised")
            m "Of course it is!"

            jump end_hg_pr_handjob

        "\"Well, you did try. Here are the points.\"":
            call her_main("Really?", "angry", "base", "base", "mid")
            call her_main("Thank you, [genie_name]!", "open", "narrow", "worried", "down")
            call her_main("I promise, I will try harder next time!", "base", "base", "base", "mid")
            call her_main("Ehm... Should you request a similar favour in the future, I mean...","upset","wink")

            jump end_hg_pr_handjob


label hg_pr_handjob_T1_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], how did it go?"
    show screen blktone
    call her_main("It went well, [genie_name]...", "open", "base", "base", "mid",xpos="right",ypos="base")
    call play_music("playful_tension") # SEX THEME.
    her "I asked one if the \"Gryffindor\" boys to let me do \"it\" to him..."
    call her_main("To my surprise he agreed eagerly.", "open", "base", "base", "mid", cheeks="blush")
    m "Shocker..."
    call her_main("So we hid behind one of those huge tapestries in the east wing...", "open", "closed", "base", "mid")
    call her_main("And I... wanked him until he came...", "annoyed", "narrow", "angry", "R")
    her "........."
    call her_main("And I asked him to keep the whole thing a secret, but...", "angry", "base", "base", "mid")
    m "What's the matter, [hermione_name]?"
    m "Doubting the honesty of your fellow \"Gryffindors\"?"
    call her_main("Of course not, [genie_name].", "upset", "closed", "base", "mid")
    call her_main("...........................","angry","down_raised")
    call her_main("Still... Performing this sort of task could really damage my reputation...", "angry", "base", "base", "mid")
    m "Is this your way of asking for a raise, [hermione_name]?"
    m "Fifty Five points is as high as I can go with this one."
    call her_main("Oh... Of course...","angry","down_raised")
    m "Unless, you've changed your mind about having sex with one of your classmates?"
    call her_main("What?", "shock", "wide", "base", "stare")
    call her_main("[genie_name], I am not a prostitute!","angry","down_raised")
    m "Well, in that case..."

    jump end_hg_pr_handjob


label hg_pr_handjob_T1_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    m "[hermione_name], how did it go?"

    $ aftersperm = True #Shows stains on Hermione's uniform.
    $ uni_sperm = True  #Universal sperm.
    $ u_sperm = "characters/hermione/face/auto_08.png"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("Awful, [genie_name]. Simply awful...","scream","worriedCl", xpos="right", ypos="base")
    m "You've got something... in your hair there..."
    call her_main("Huh?", "open", "base", "base", "mid")
    call her_main("Oh, no! I thought I got it all off...", "open", "base", "base", "R", cheeks="blush")
    show screen ctc
    pause
    show screen blkfade
    with d3
    pause.5
    $ uni_sperm = False  #Universal sperm.
    call her_main("", "upset", "closed", "base", "mid")
    hide screen blkfade
    with d3
    pause
    hide screen ctc
    m "Hm... So I suppose you have completed your task?"
    call her_main("I did, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "What's the problem, then?"
    call her_main("..........","annoyed","worriedL")
    call her_main("All boys are jerks! That is the problem, [genie_name]!", "scream", "closed", "angry", "mid")
    call her_main("I gave this one boy a good wanking...", "open", "narrow", "worried", "down")
    her "And do you know how he thanked me?"
    call her_main("He got his spunk all over me...", "scream", "base", "angry", "mid", emote="01")
    call her_main("And he did that on purpose, I know he did!", "scream", "closed", "angry", "mid")
    call her_main("Nasty, good for nothing \"ravenclaws\"...","annoyed","worriedL")
    m "Well, I'd say a job well done."

    jump end_hg_pr_handjob


label hg_pr_handjob_T2_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 18 and her_whoring < 21:

    call her_main(face="neutral", xpos="right", ypos="base")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "[hermione_name], did you complete your task?"
    show screen blktone
    with d3
    call her_main("Ehm...", "open", "base", "base", "mid",xpos="right",ypos="base")
    her "Not yet, [genie_name]..."
    m "Not yet?"
    call her_main("Yes... Let me explain, [genie_name]...","annoyed","worriedL")
    call her_main("uhm... Well...", "open", "base", "base", "mid")
    her "I was wanking this one boy off in one of the empty classrooms..."
    her "And that nasty ghost Peeves walked in..."
    call her_main("Or rather flew in on us...","annoyed","worriedL")
    call her_main("And as soon as he realised what I was doing to the boy...", "open", "base", "base", "mid")
    her "He started to yell obscenities at us..."
    her "So we had to leave in a hurry..."
    m "I see..."
    call her_main("That is not all, [genie_name]...", "annoyed", "narrow", "angry", "R")
    m "Go on..."
    call her_main("Well, I sort of made a promise to the boy...", "open", "narrow", "worried", "down")
    her "I promised to meet him after my classes and..."
    call her_main("...and finish what I have started...", "annoyed", "narrow", "annoyed", "mid")
    m "I see..."
    m "Did you?"
    call her_main("No, [genie_name]. Not yet...", "angry", "base", "base", "mid")
    her "I am going to meet him as soon as we are done here, [genie_name]."
    m "Hm..."
    call her_main("So if you could just give those points in advance...","angry","down_raised")
    her "I would go meet with the boy right away and..."
    call her_main("And give him a proper handjob...", "open", "base", "base", "R", cheeks="blush")

    menu:
        "\"No. You failed this favour, [hermione_name].\"":
            stop music fadeout 3.0
            call her_main("B-but...", "open", "base", "base", "mid", cheeks="blush")
            call her_main("But I gave him my word...", "angry", "wide", "base", "stare")
            her "I swore on Godric Gryffindor's name..."
            call her_main("And now I will have to give him the wank off no matter what...","angry","down_raised")
            m "Well, I didn't force you to give him that promise, did I?"
            call her_main("......", "angry", "base", "base", "mid")
            call her_main("This is just not fair!","scream","worriedCl")

            call her_walk(action="leave", speed=2.5)

            $ her_mood += 20

            $ hg_pr_handjob.inProgress = False

            jump end_hermione_event

        "\"Alright, I think I can trust you.\"":
            call her_main("Thank you, [genie_name].", "base", "base", "base", "mid")
            her "I knew you would understand."
            m "Just make sure you finish your job properly this time."
            call her_main("Of course, [genie_name]. I will give him the wank of his life, I promise!","base","happyCl")

            jump end_hg_pr_handjob


label hg_pr_handjob_T2_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("I did, [genie_name]...", "open", "closed", "base", "mid",xpos="right",ypos="base")
    call her_main("Although I am still not sure how I feel about all of this...","annoyed","worriedL")
    m "You personal feelings are of no concern to me, [hermione_name]."
    m "Just tell me how it went."
    call her_main("Well, there is not much to tell. [genie_name]...", "open", "base", "base", "mid")
    call play_music("playful_tension") # SEX THEME.
    her "Today I gave another handjob to one of my classmates..."
    call her_main("Me, Hermione Granger...", "open", "narrow", "worried", "down")
    call her_main("Giving free handjobs in the school's restroom...","angry","down_raised")
    m "Wait. What do you mean with \"free\"?"
    call her_main("Oh, of course... I get paid with house points for this...", "angry", "base", "base", "mid")
    her "But nobody knows about that..."
    her "And to everyone else this just looks like some harlot who does this for fun..."
    call her_main("They must think I am a slut...", "open", "narrow", "worried", "down")
    call her_main("..............","clench","down_raised")
    call her_main("Do you think I'm a slut, [genie_name]?", "open", "happy", "base", "mid", cheeks="blush")

    menu:
        "\"What? Of course not, [hermione_name]!\"":
            call her_main("..............", "base", "base", "base", "R", cheeks="blush")
            call her_main("You are right, [genie_name]...", "base", "narrow", "worried", "down")
            her "I am making this sacrifice for the glory of the \"Gryffindor\" house."
            call her_main("I am not taking pleasure in this sort of activity...", "soft", "narrow", "annoyed", "up")
            call her_main("Because if I would...", "annoyed", "narrow", "angry", "R")
            her "That would mean I really am a slut..."
            call her_main("And I am not...","angry","down_raised")
            her "......"
            her "I am not a slut..."

        "\"A slut? No... Not yet.\"":
            call her_main("\"Not yet\"??!", "angry", "base", "base", "mid")
            call her_main("..........","angry","down_raised")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Well, of course!","scream","wide_stare")
            call her_main("You are right, as usual, [genie_name]!", "soft", "base", "base", "mid")
            m "Huh?"
            call her_main("I have done a few... naughty things...", "open", "base", "base", "mid")
            her "But that does not mean anything!"
            call her_main("...........", "annoyed", "narrow", "angry", "R")

        "\"Yes, that's exactly what you are.\"":
            call her_main("I was afraid that you would say that, [genie_name]...","mad","worriedCl", tears="soft_blink")
            her "But you are wrong, [genie_name]."
            call her_main("You of all people should understand that I take no pleasure in this...", "angry", "base", "base", "mid", tears="soft")
            call her_main("I just do what needs to be done...", "normal", "base", "base", "R", tears="soft")
            $ her_mood = 10

    call her_main("[genie_name], can I just get paid now, please?", "soft", "base", "base", "R")
    m "Get paid? But you didn't tell me how it went yet?"
    her "I did not?"
    call her_main("[genie_name], I gave a handjob to one of my classmates today...", "open", "base", "base", "mid", cheeks="blush")
    her "I wanked his cock until he came..."
    call her_main("Is that not what you told me to do?","disgust","glance")
    m "That's exactly what I told you to do, [hermione_name]."
    call her_main("Then I would like to get paid now, please.", "annoyed", "closed", "base", "mid")
    m "........"
    m "Fine..."

    jump end_hg_pr_handjob


label hg_pr_handjob_T2_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("Yes, [genie_name]. I did.", "open", "closed", "base", "mid",xpos="right",ypos="base")
    m "Great. Tell me more."
    call play_music("playful_tension") # SEX THEME.
    call her_main("Well, today was a rather busy day...", "open", "base", "base", "mid")
    her "And I had to catch up on some studying..."
    her "So I really had no time to plan this out properly, like I normally would..."
    her "I pretty much just approached the first boy I saw..."
    call her_main("And asked him if he wants me to wank him off.", "annoyed", "narrow", "angry", "R")
    her "a Few minutes later I was already stroking his hard cock in the restroom stall..."
    m "How very efficient of you..."
    call her_main("Thank you, [genie_name].", "annoyed", "narrow", "annoyed", "mid")
    call her_main("So, as I was saying...", "annoyed", "narrow", "angry", "R")
    her "I wanked his cock until he came..."
    call her_main("But after that he said: \"Good job, slut\" and just left me there...","disgust","glance")
    call her_main("Such a mean thing to do...", "annoyed", "narrow", "angry", "R")
    call her_main("It made me feel so cheap... and used.", "upset", "closed", "base", "mid")
    her "But it gets worse..."
    her "......."
    call her_main("I think on some level it also made me feel good somehow...","angry","down_raised")
    her "All these favours I have been selling to you lately, [genie_name]..."
    call her_main("...it's starting to affect me.", "angry", "base", "base", "mid")
    her "[genie_name], what is happening to me?"

    menu:
        "\"This is nothing. Stop overthinking it!\"":
            call her_main(".......", "open", "happy", "base", "mid", cheeks="blush")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("You are probably right, [genie_name]. As usual...", "base", "base", "base", "R", cheeks="blush")
            her "This does not have to mean anything..."

        "\"That is a natural response...\"":
            call her_main("It is?", "open", "happy", "base", "mid", cheeks="blush")
            m "Of course."
            m "You are a girl and he is a boy..."
            m "You got excited and it made you feel good..."
            call her_main("Hm...", "base", "base", "base", "R", cheeks="blush")
            m "Now if you were to give a handjob and feel completely indifferent about it..."
            m "...that would be... unnatural."
            call her_main("I think you are right, [genie_name].", "open", "happy", "base", "mid", cheeks="blush")
            call her_main("As usual.", "base", "base", "base", "R", cheeks="blush") # :)

        "\"Yes! All goes according to plan!\"":
            call her_main("What?", "angry", "wide", "base", "stare")
            m "What?"
            call her_main("[genie_name], did you just say \"All goes according to plan\"?", "angry", "base", "angry", "mid", cheeks="blush")
            m "Did I?"
            m "Oh, yes, of course."
            m "ensuring that \"Gryffindor\" gets the house cup this year."
            m "That's the plan And thanks to your hard work, [hermione_name]..."
            m "All goes according to keik-... I mean, the plan..."
            call her_main("Hm...", "upset", "closed", "base", "mid")

            $ her_mood += 11

    jump end_hg_pr_handjob


label hg_pr_handjob_T3_intro_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 21:

    stop music fadeout 1.0

    # HERMIONE HAS CUM ON HAIR.
    #$ aftersperm = True #Shows stains on Hermione's uniform.
    $ uni_sperm = True  #Universal sperm.
    $ u_sperm = "characters/hermione/face/auto_08.png"

    show screen blktone
    call her_main("[genie_name]...","open","worried", xpos="right", ypos="base")
    m "[hermione_name]..."
    call her_main("I did a bad thing today, [genie_name]...","open","worriedL")
    m "Did you now? Do tell..."
    call play_music("playful_tension") # SEX THEME.
    her "Yes, I did a bad thing... a very bad thing..."
    call her_main("A very bad and foolish thing...", "annoyed", "squint", "angry", "mid")
    her "..."
    m "...................."
    her "......................"
    call her_main("I wanked off one of my best friend's brothers...", "angry", "base", "base", "mid", tears="soft")
    m "Interesting..."
    call her_main("Seemed like such a great idea at first...", "angry", "base", "base", "mid", tears="soft")
    her "And Ron was so up for it..."
    call her_main("But if Ginny were to find out... she...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    call her_main("She would most certainly kill me, [genie_name]...", "angry", "base", "base", "mid", tears="soft")
    m "A handjob, huh? Are you sure that was all you did?"
    call her_main("[genie_name]?", "angry", "base", "base", "mid", tears="soft")
    m "There is something in your hair..."
    call her_main("What? But I swallowed it all... err...", "soft", "base", "base", "mid", tears="soft")
    call her_main("I mean...","clench","worried", cheeks="blush", tears="soft")
    call her_main("*Sigh*", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    her "...I sucked him off, [genie_name]."
    her "I did not plan to... but..."
    call her_main("Ron is always so nice to me...","clench","worried", cheeks="blush", tears="soft")
    call her_main("And I wanted to thank him...*Sob!*","shock","down_raised", cheeks="blush", tears="crying")
    call her_main("And now Ginny will kill me! *Sob!*", "angry", "base", "base", "mid", tears="soft")
    her "She will kill me, [genie_name]!"
    call her_main("And if she does not I will probably die of shame anyway.","shock","down_raised", cheeks="blush", tears="crying")
    her "No, no, no... How will I ever face her...?"
    m "Calm down, [hermione_name]."
    m "I assure you, this is not something a boy would be eager to brag about to his sister."
    call her_main("It is not?","clench","worried", cheeks="blush", tears="soft")
    m "Don't be silly, [hermione_name]."
    call her_main("Hm...", "normal", "base", "base", "R", tears="soft")
    call her_main("You are probably right, [genie_name]...", "soft", "base", "base", "mid", tears="soft")
    her "And I made Ron give me his word that he will keep the whole incident a secret..."
    call her_main("So, I think I should just trust him to keep his word...","open","worriedL")
    call her_main("..........", "soft", "base", "base", "R")
    her "..."
    call her_main("Will I get paid for this, [genie_name]?", "base", "base", "base", "mid")
    m "Of course."

    jump end_hg_pr_handjob


label hg_pr_handjob_T3_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("Yes, I did [genie_name]...","base","suspicious")
    her "More than once actually..."
    m "More than once?"
    call her_main("Five times, [genie_name]...","base","glance")
    her "I got carried away a little I suppose..."
    m "What do you mean \"five times\", [hermione_name]?"
    call her_main("I mean I wanked off five boys today, [genie_name].","base","suspicious")
    m "Very impressive, [hermione_name]."
    call her_main("Thank you, [genie_name].","base","glance")
    m "You don't expect me to multiply your payment by seven or anything, do you?"
    call her_main("Of course not, [genie_name].", "base", "base", "base", "R", cheeks="blush")
    m "Than why do it?"
    call her_main("Well, it sort of just happened...", "open", "happy", "base", "mid", cheeks="blush")
    her "I was wanking off this one boy..."
    her "And another boy walked in on us..."
    her "He called his friends..."
    call her_main("One thing lead to another...","base","glance")
    m "And you ended up jerking off five cocks..."
    call her_main("...yes.", "soft", "narrow", "annoyed", "up")
    m "Well done, miss Granger."
    call her_main("","base","glance")

    jump end_hg_pr_handjob


label hg_pr_handjob_T3_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("Yes I did, [genie_name].", "base", "base", "base", "mid")
    call her_main("But, ehm...","open","worried")
    m "...?"
    call her_main("Well, I did not just wank off one of my classmates...", "open", "base", "base", "mid")
    her "I.............."
    call her_main("...............","clench","down_raised")
    m "Spit it out, [hermione_name]. The suspense is killing me."
    call play_music("playful_tension") # SEX THEME.
    call her_main("I sort of did it during class...", "open", "narrow", "worried", "down")
    m "Impressive..."
    call her_main("Sir, you don't understand.  Let me try and explain.","angry","down_raised")
    hide screen blktone
    with d3
    her "I don't even know what came over me."
    show screen dual_hand_job
    with d5

    call her_main("I was trying to act as nonchalant as I could...")
    her "But, I suddenly had this incredibly pleasant urge to do it during Professor Snape's class."
    her "I couldn't even take notes with my other hand..."
    her "It was wrapped around another thick hot cock too."
    m "You gave two boys handjobs at the same time?!"
    call her_main("Yes Sir.","angry","wink")
    call her_main("And I think I gave them the wank of their life too...", "base", "narrow", "worried", "down")
    her "Because they did not just cum."
    her "Their cocks simply exploded with spunk."
    m "You enjoyed it, didn't you?"
    call her_main("To be completely honest with you, sir... I did.", "grin", "narrow", "base", "dead")
    call her_main("It was exciting.", "smile", "base", "angry", "mid")
    call her_main("God, there was so much.  My hands looked like a candle had dripped hot wax all over them.", "grin", "narrow", "base", "dead")
    call her_main("I didn't know what to do I couldn't just go about the rest of class with huge globs of cum all over my hands.","angry","down_raised")
    her "So I decided to rub it all over the inside of my thighs to keep from having to stain my clothes."
    call her_main("Every time I walked I could smell their cum from between my legs.", "silly", "narrow", "annoyed", "up")
    m "That's quite an interesting story miss Granger."
    hide screen dual_hand_job
    with d5

    show screen blktone
    call her_main("I definitely want them both at the same time.", "silly", "narrow", "base", "dead")
    m "..."
    call her_main("Yeah, two huge cocks exploding massive loads of cum everywhere.", "silly", "narrow", "annoyed", "up")
    m "........"
    call her_main(".......", "silly", "narrow", "annoyed", "up")
    m "Ehm....."
    call her_main("Oh god, I'm sorry [genie_name], I was thinking of something else.", "angry", "wide", "base", "stare")
    m "Yes... sure, OK."
    call her_main("", "base", "base", "base", "mid")

    jump end_hg_pr_handjob
