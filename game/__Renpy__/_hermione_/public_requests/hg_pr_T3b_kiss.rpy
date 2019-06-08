

### Make Out With A Girl ###

label hg_pr_kiss:

    if hg_pr_kiss.counter < 1:
        m "{size=-4}(Tell her to go make out with one of her female classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(face="happy", xpos="right", ypos="base", trans="fade")

    #Intro.
    if hg_pr_kiss.counter == 0:
        m "Have You ever kissed another girl, [hermione_name]?"
        call her_main("?!","normal","frown")

        if her_tier < 3 or her_reputation < 6:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("I am not a... lesbian, [genie_name].","open","base")
        m "Silly girl... You don't need to be a lesbian to kiss girls."
        m "I mean, I do it and I am not a lesbian either."
        call her_main("...............","angry","angry")
        her "[genie_name]--"
        m "No, \"[genie_name]s\"! This is your task for today!"
        m "Go find a cute little thing and plant a \"smooch\" on her!"
        call her_main("[genie_name], but I am--","open","worried")
        m "Dismissed, [hermione_name]."
        call her_main("[genie_name]!......","normal","frown")
        m "I said you're dismissed."
        call her_main("*Humph!*...","annoyed","frown")

    elif her_tier < 4:
        m "[hermione_name], forty five house points are up for grabs today!"
        m "Are you interested?"
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("It depends...","normal","base")
        her "Will I have to do something depraved again?"
        m "\"Depraved\"??! When did I ever--?"
        call her_main("Really, [genie_name]?","open","angryCl")
        m "Fine, fine... But all I want you to do today is to make out with another girl."
        call her_main("Oh, is that all?","angry","angry") # :(
        m "Yes... Pretty basic stuff for you, right?"
        m "And you will be getting forty five house points afterwards of course."
        call her_main(".............","normal","frown")
        m "So... Are you up for it?"
        call her_main("I will see what I can do, [genie_name]...","annoyed","angryL")
        m "Great. See you after your classes then."
        call her_main("................","annoyed","annoyed")

    elif her_tier < 5:
        m "[hermione_name], forty five house points are up for grabs today!"
        m "Are you interested?"
        call her_main("I suppose...","annoyed","ahegao")
        m "Great. All you need to do is make out with another girl."
        call her_main("I see...","annoyed","down")
        m "Up for the task, [hermione_name]?"
        call her_main("I suppose...","annoyed","worriedL")
        m "Great. See you after your classes then."

    else:
        m "[hermione_name], forty five house points are up for grabs today!"
        m "Are you interested?"
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Sure, why not?","base","base")
        m "Great."
        m "I want you to make out with another girl today."
        call her_main("Alright.","soft","baseL")
        call her_main("I know a couple of girls who are hungry for attention and wouldn't mind putting on a little show.","smile","glance")
        m "Great. See you after your classes then."

    call her_walk(action="leave", speed=2.5)

    $ current_payout += 45
    $ hg_pr_kiss.inProgress = True

    jump end_hermione_event


label end_hg_pr_kiss:
    $ gryffindor += current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ hg_pr_kiss.inProgress = False

    # Increase Points
    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    if her_reputation < 12: # Points til 12
        $ her_reputation += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pr_kiss_T1_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #if her_whoring >= 12 and her_whoring < 15: # LEVEL 05

    stop music fadeout 1.0
    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name]..."
    m "Did you succeed in completing your task?"
    show screen blktone
    call her_main("I...","open","worried")
    m "I told you to make out with another girl..."
    m "Did you do it?"
    call her_main("I...","open","worriedL")
    her "I tried, [genie_name]. I really did."
    m "And?"
    call her_main("Well...","annoyed","worriedL")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    her "It was awkward and embarrassing..."
    m "did you do it or not?"
    call her_main("...no I did not, [genie_name]...","annoyed","angryL")
    her "All I did was making a complete fool out of myself..."
    call her_main("In front of the entire class...","angry","angry")
    m "Tell me what happened, [hermione_name]."
    call her_main("No, I will not, [genie_name].","annoyed","angryL")
    her "Not in a million years!"
    call her_main("Why do I have to perform such ridiculous tasks anyway?!","shock","worriedCl")
    her "What is the point of all this?"
    call her_main("I hate this!","scream","angryCl")
    call her_main("...............","annoyed","angryL")
    her "................."
    m ".............."
    m "You are not getting paid, you know that, right?"
    call her_main("I don't care...","scream","angryCl")

    call her_walk(action="leave", speed=2.5)

    $ her_mood +=12

    $ hg_pr_kiss.inProgress = False

    jump end_hermione_event


label hg_pr_kiss_T1_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("I did, [genie_name]...","open","closed")
    m "Good. Give me the details."
    call her_main("Well, I kissed a girl. Just like you told me to, [genie_name].","annoyed","suspicious")
    m "I guess it was embarrassing for you, girl?"
    call her_main("Very much so, [genie_name].","annoyed","angryL")
    m "Did you enjoy it though?"
    call her_main("*Humph!*...","annoyed","annoyed")
    m "So you kissed a girl and you liked it?"
    call her_main("Yes...","disgust","glance")
    m "Did your tongues touch?"
    call her_main("Yes...","disgust","glance")
    her "It was a proper deep kiss, if that's what you want to know."
    her "Can I just get my payment now?"
    call her_main("Please, [genie_name]...","annoyed","angryL")
    m "Well, alright..."

    jump end_hg_pr_kiss


label hg_pr_kiss_T1_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("Yes, I did, [genie_name].","open","closed")
    m "Good. Tell me how it went."
    call her_main("It went well, [genie_name].","open","closed")
    m "Great. Give me the details."
    call her_main("What would you like to know, [genie_name]?","open","angryCl")
    m "Tell me everything! Was the girl pretty?"
    m "Did she return your kiss?"
    call her_main("She was relatively pretty, [genie_name].","open","suspicious")
    her "And she did return my kiss..."
    call her_main("...........","annoyed","closed")
    call her_main("Anything else, [genie_name]?","open","suspicious")
    m "...."
    m "Why are you being difficult, [hermione_name]?"
    call her_main("With all due respect, [genie_name]...","open","angryCl")
    her "You told me to make out with another girl, and I did..."
    call her_main("Now, I would like to get paid if you would be so kind.","normal","base")
    m "......................"

    menu:
        "\"Fine. Here is your payment, girl.\"":
            jump end_hg_pr_kiss

        "\"I don't appreciate your attitude, [hermione_name].\"":
            call her_main("Well, that is unfortunate, [genie_name].","open","angryCl")
            m "Sure is..."
            m "Because you are not getting paid you insolent, little witch."
            stop music fadeout 1.0
            call her_main("What?","normal","base")
            call her_main("[genie_name], you can't do that!","open","worried")
            m "Dismissed."
            call her_main("B-but--","open","worriedL")
            call her_main("[genie_name], please!","open","worried")
            her "The girl was from \"Hufflepuff\" and--"
            m "Too late for that, [hermione_name]."
            m "You are dismissed."
            call her_main("......","angry","base",tears="soft")

            call her_walk(action="leave", speed=2.5)

            $ her_mood +=25

            $ hg_pr_kiss.inProgress = False

            jump end_hermione_event


label hg_pr_kiss_T2_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 15 and her_whoring <= 17: # LEVEL 06. Event level 02.

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("I did, [genie_name]...","open","closed")
    m "Well, don't just stand there. Give me the details."
    call her_main("Ehm, alright...","open","base")
    her "The girl was from \"Ravenclaw\"..."
    call her_main("I think she may have been an underclassman, but I did not ask...","soft","baseL")
    her "We got to talking about boys..."
    call her_main("And she told me that she never kissed one...","open","closed")
    her "And that she is worried that she might be very bad at it..."
    call her_main("So I just offered my help...","base","base")
    call play_music("playful_tension") # SEX THEME.
    her "And then we spent some time in one of the bathroom stalls..."
    call her_main("Making out...","base","base")
    call her_main("She caught on real quick... I think she could be really good at it with some practice...","open","base")
    call her_main("Also she was quite adorable...","base","base")
    call her_main("She kept calling me \"[hermione_name]\"...","smile","baseL")
    m "Hm..."
    m "I Don't recall sending you out with a task to confuse little kids, [hermione_name]."
    call her_main("\"Little kids\"? [genie_name], please...","smile","glance")
    her "You should have seen that girl..."
    her "A little petite? Maybe... But definitely not a \"kid\"."
    call her_main("And I assure you that she was anything but confused.","smile","angry")
    her "In fact, at the end of our \"Study session\" she got rather obnoxious..."
    call her_main("And it sort of felt as if she was taking advantage of me...","open","base")
    m "Oh... Well, in that case..."
    call her_main("","base","base")

    jump end_hg_pr_kiss


label hg_pr_kiss_T2_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name]. Did you complete your task?"
    show screen blktone
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("I did, [genie_name].","open","closed")
    m "Tell me how it went."
    call her_main("Well... Ehm...","open","base")
    her "There is this one girl who is into girls..."
    her "I thought she would be the ideal candidate for my task..."
    her "so I told her that I am curious and that I would like to kiss her..."
    call her_main("She said that we should go to the girls' restroom for that...","open","down")
    her "But I just kissed her right there in the corridor..."
    call her_main("And she kissed me back but...","open","base")
    call her_main("It got weird really fast...","angry","down_raised")
    her "The way she kissed me..."
    call her_main("She did it like a boy would, [genie_name]...","angry","base")
    call her_main("Aggressive but confident...","angry","down_raised")
    call her_main("Naturally a small group of spectators gathered up around us right away...","upset","closed")
    call her_main("Mostly boys of course...","open","base", cheeks="blush")
    call her_main("Some of them even cheered us on...","open","worriedCl", cheeks="blush")
    call her_main(".....","base","suspicious")
    her "By the way, the girl I kissed, [genie_name]..."
    m "Hm...?"
    call her_main("She is one of those unpopular kids...","open","closed")
    her "I know that other students make fun of her sometimes..."
    call her_main("But today changed everything...","base","suspicious")
    her "I Single-handedly turned that girl from a social outcast..."
    call her_main("Into \"that lesbian girl who made out with Hermione Granger\"!","smile","angry")
    m "Wow... You are just like some kind of hero or something..."
    call her_main("I suppose I am, [genie_name]...","base","glance")
    her "I changed that poor girl's life..."
    m "Now you are just pulling on my heartstrings..."

    jump end_hg_pr_kiss


label hg_pr_kiss_T2_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("[genie_name]?","open","closed", xpos="right", ypos="base")
    m "Yes, [hermione_name]?"
    call her_main("May I ask you a question, [genie_name]?","open","base")
    m "By all means."
    call her_main("Ehm...","annoyed","angryL")
    call her_main("Why are boys so into watching girls make out with each other, [genie_name]?","disgust","glance")

    menu:
        m "..."
        "\"Who knows? Boys are weird.\"":
            call her_main("Yes, they are, aren't they...?","angry","down_raised")
            m "Yes, yes..."
            m "And that is why young girls such as yourself...."
            m "Are often interested in a much older gentleman..."
            call her_main("??!","angry","base")
            call her_main("That is not what I meant, [genie_name]...","annoyed","annoyed")

        "\"You wouldn't understand, girl.\"":
            call her_main("Hm...","upset","closed")
            call her_main("What about you, [genie_name]?","angry","base")
            her "Where you like that when you were a boy?"
            m "You mean if I enjoyed watching two girls going at it?"
            m "Well of course."
            m "I still do..."
            call her_main("Oh...","upset","closed")

        "\"Kissing girls? Where?!!\"":
            call her_main("Tsk!......................","angry","angry", emote="01")

    call her_main("Well, I am only asking you this, [genie_name], because...","open","down")
    call her_main("...it is sort of becoming a new trend in our school...","angry","base")
    her "Some girls are willing to do this simply to catch the attention of the boy they fancy..."
    m "Are you one of those girls, [hermione_name]?"
    call her_main("I suppose...","angry","down_raised")
    call her_main("I mean, only because of the favours you buy from me, [genie_name]...","upset","closed")
    m "Good... Tell me more."
    call her_main("Well, as you know, I am quite popular...","smile","happyCl", emote="06")
    call her_main("So all I had to do is just mention that I would not mind doing it today...","base","happyCl")
    her "And I had half a dozen girls lined up instantly..."
    call her_main("I chose a girl from \"Gryffindor\" of course...","base","base")
    call her_main("And we put on a little show right in the middle of the classroom...","open","base")
    m "Good... Tongue and everything?"
    call her_main("Tongue and everything, [genie_name].","annoyed","worriedL")
    m "Nicely done."
    call her_main("","base","base")

    jump end_hg_pr_kiss


label hg_pr_kiss_T3_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 18: # LEVEL 07+

    call her_main(face="happy", xpos="right", ypos="base")
    m "[hermione_name]..."
    show screen blktone
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Good evening, [genie_name].","open","closed")
    m "Did you complete your task, girl?"
    call her_main("I did, [genie_name].","soft","base")
    m "I'm all ears..."
    call her_main("Well, I kissed that annoying blond girl from \"Slytherin\"...","annoyed","suspicious")
    m "Hm... \"annoying\", huh?"
    m "Because she happens to be from \"Slytherin\"."
    call her_main("Precisely so, [genie_name].","open","closed")
    m "Hm..."
    m "Don't you think that that's a little bit of prejudice on your part?"
    m "Or shall I say that you are being a \"housist\"?"
    call her_main("...a \"housist\", [genie_name]?","annoyed","annoyed")
    m "Well, you know... It's like \"sexist\" or \"ageist\"..."
    m "You just put an \"ist\" after something and it automatically becomes a bad thing..."
    call her_main("\"housist\" is not an actual word, [genie_name]...","soft","baseL")
    m "It's not? Well, give it time..."
    call her_main(".............?","annoyed","annoyed")
    m "\"Housophobic\"...?"
    m "No, wait, I got it!"
    m "\"Housophobe\"!"
    call her_main("Stop it, [genie_name]. I am not any of those weird words...","normal","frown")
    her "\"Slytherins\" are evil and annoying. Nobody likes them, and that is a fact!"
    m "Fine, whatever. Back to the \"girl-kissing\" then."
    call her_main("...............","annoyed","worriedL")
    her "Like I was saying..."
    call her_main("I kissed that girl from \"Slytherin\"...","open","base")
    call her_main("Normally I would never do it, of course...","annoyed","angryL")
    her "Not with someone from that wretched house anyways..."
    call her_main("But she approached me first and practically begged me to do it with her...","annoyed","annoyed")
    call her_main("And today of all days...","annoyed","angryL")
    her "to be honest..."
    call her_main("She was quite attractive...","annoyed","annoyed")
    call her_main("For someone from \"slytherin\" that is...","upset","closed")
    call her_main("I did not ask her why she needed this so desperately...","open","closed")
    her "She was probably just trying to boost her own popularity at my expense..."
    her "Or it could also be that someone from the school staff bought this favour from her..."
    call her_main("The same way you buy favours from me, [genie_name]...","open","annoyed", cheeks="blush")
    m "(Snape?)"
    call her_main("If that is the case I am sure that it was professor Snape...","angry","angry")
    m "What? He would never..."
    call her_main("You should really investigate Professor Snape's activities, [genie_name]...","annoyed","angryL")
    m "Of course..."
    m "Putting him on my \"naughty boys list\" as we speak..."
    call her_main("..........","disgust","glance")
    m "What happened next, [hermione_name]?"
    call her_main("Oh, right...","open","down")
    her "Well, we made out for a while..."
    her "She was very... passionate."
    call her_main("So I imagine it was quite a spectacle...","angry","wink")
    her "The boys were cheering and whistling..."
    call her_main("So we decided to \"snowball\" a little...","base","down")
    m "I'm sorry, you decided to do what?"
    call her_main("To \"snowball\", [genie_name].","angry","wink")
    call her_main("It is when one girl spits into another girl's mouth...","base","glance")
    her "We call it \"snowballing\"..."
    her "The boys really go crazy from that for some reason..."
    m "I imagine they do..."
    call her_main("So she spat into my mouth...","open","closed")
    her "And then I spat into hers..."
    call her_main("Although I would much rather spit in her face!","angry","angry", cheeks="blush")
    call her_main("Then she returned my spit...","annoyed","angryL")
    call her_main("And I had to fight the urge to slap her smug face for doing that...","angry","angry", cheeks="blush")
    call her_main("But I don't think the boys would appreciate that...","upset","closed")
    m "Well... You would be surprised..."
    call her_main("In any case, After that we kissed some more...","base","down")
    her "And then the break was over..."
    call her_main("And we had to run to class...","angry","wink")
    m "*Sigh...* Nonchalant and innocent schooldays..."
    m "Home assignments... Classes..."
    m "Schoolgirls \"snowballing\" in the courtyard..."
    m "Well done, [hermione_name]."
    call her_main("","grin","baseL")

    jump end_hg_pr_kiss


label hg_pr_kiss_T3_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="happy", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("I did, [genie_name].","open","closed")
    call her_main("Only... ehm...","grin","baseL")
    m "What is it?"
    call her_main("Well... I have this friend...","base","base")
    her "Her name is Ginny Weasley..."
    call her_main("And... uhm...","base","baseL", cheeks="blush")
    her "I'm Not sure how to say this..."
    m "Just say it, [hermione_name]."
    call her_main("Well, we decided to skip the potions class together...","open","base")
    her "And study for the upcoming Herbology test instead..."
    her "So me and Ginny, we were studying..."
    her "And we got to talking about boys..."
    m "Naturally..."
    call play_music("playful_tension") # SEX THEME.
    call her_main("And then I sort of kissed her...","open","baseL", cheeks="blush")
    call her_main("And Ginny returned my kiss with such passion...","base","glance")
    her "that we sort of ended up doing more than just kissing..."
    g9 "And afterwards you had a pillow fight in lingerie?"
    call her_main("Err... No...","open","squint", cheeks="blush")
    m "What did you do then?"
    call her_main("I am not telling you, [genie_name].","base","baseL", cheeks="blush") # :)
    her "You sent me out to kiss a girl..."
    her "And I did just that."
    call her_main("The rest shall remain private.","angry","wink")
    m "Now you are just being cruel, you little witch."
    call her_main("My points please.","smile","glance")
    m "Fine..."

    jump end_hg_pr_kiss
