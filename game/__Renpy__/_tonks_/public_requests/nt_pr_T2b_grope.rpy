

### Grope me ###

# (Tonks lets her students play with her tits, ass,...)

label nt_pr_grope_start:
    call ton_main("","base","base","base","mid", xpos="right", ypos="base", trans="fade")

    if ton_tier == 2:

        if nt_pr_grope.points == 0:
            m "Ready for the next step?"
            call ton_main("*Mmmm*... You make it sound so ominous.","horny","base","base","mid")
            call ton_main("What shall I do next with my students...","base","base","angry","mid")
            if nt_pr_kiss.counter == 0:
                call ton_main("Want me to make out with them?","horny","base","base","ahegao")
                m "Maybe, but not right now..."
            else:
                call ton_main("Want me to make out with them again?","horny","base","angry","mid")
            m "I was thinking you could take a few of these boys to second base."
            call ton_main("Second base?! Already?","base","base","raised","mid")
            m "We're trying to earn you a reputation as a favour trader."
            m "Making your students write lines in their underwear isn't going to cut it..."
            call ton_main("I suppose you might be right...","open","base","base","up")
            call ton_main("I'm not sure if the students will be ready for it though...","upset","base","worried","R")
            m "Please, you sound like you're talking about a pop-quiz."
            m "All you have to do is get them to grope your chest a little..."
            call ton_main("My breasts?","horny","base","angry","mid")
            g9 "I can't imagine any of them saying no to that..."
            call ton_main("*Mmm*... Well if you say so...{w} You are the expert.","base","base","angry","mid")
            m "That I am."
            m "Now get out there and buy some favours!"
            call ton_main("Yes, sir!","open","closed","base","mid")
            call ton_main("(This is way better than being an auror!)","horny","base","base","ahegao")

        else:
            m "Think you're up for messing around with your students again?"
            m "Let them cop a feel?"
            call ton_main("Consider it done, [ton_genie_name].", face="horny")
            m "I'll see you after class..."

    elif ton_tier >= 3: # Not in 1.37

        if nt_pr_grope.points == 0: # Tell her to be even lewder for the next level of favors.

            "Dev Note" "Write 2nd intro."

        else: # Repeat
            m "Would you like to mess around with your students again?"
            call ton_main("And let them grope their teacher?","base","base","base","mid")
            g9 "Any way they like!"
            call ton_main("That sounds perfect!","base","base","base","mid")
            m "I'll see you after class..."
            call ton_main("Yes, [ton_genie_name]...{image=textheart}","base","base","base","mid")

    # Tonks leaves

    $ nt_pr_grope.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_grope_T1_E1: # Tier 1 - Event 1 - Slytherin boy
    call play_sound("door")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans="fade")

    if ton_reputation <= 7 and nt_pr_grope.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("Remember that \"Slytherin boy?\"...","horny","base","angry","mid")
                call ton_main("I let him play with his favourite pair of tits again...","base","base","angry","mid")
                m "Well done, [tonks_name]... We'll talk next time."
                call ton_main("Yes, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points(house="s", points=40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                jump end_tonks_event

    m "How were classes today, [tonks_name]?"
    m "Taught your students some valuable lessons?"
    call ton_main("I'm not sure about valuable...","open","base","base","R")
    call ton_main("But I do know that he isn't going to forget it anytime soon!","horny","base","angry","mid")
    m "That's what I like to hear!"
    call ton_main("Remember that \"Slytherin cutie\" I held back to write lines?","base","base","angry","mid")
    m "Vaguely."
    call ton_main("Well, I decided to hold him back after class again.","open","closed","base","mid")
    call ton_main("He tried to put on a proud \"Slytherin\" facade, claiming that I had no right to hold him back.","open","base","angry","mid")
    call ton_main("Saying I was lucky he didn't \"report me\" for making him pull down his pants...","angry","base","angry","mid")
    call ton_main("It was all empty words, of course...","open","closed","base","mid")
    call ton_main("And I could tell by the {b}bulge{/b} in his pants that he {b}wanted{/b} to be there - more than anything.","horny","base","angry","mid")
    call ton_main("Still, I let him act tough...just so he wouldn't run away...","open","base","base","L")
    m "So? How did you manage to get him to grab a handful?"
    call ton_main("I let him know today wasn't a \"punishment.\"","base","base","angry","mid")
    call ton_main("Asked what kept him distracted in class...","open","base","base","R")
    call ton_main("What he was constantly staring at...","horny","base","angry","mid")
    call ton_main("He didn't want to say it at first...","open","base","base","R")
    call ton_main("So I leaned in closer...{w} Let him feel my breath on his neck...","open","closed","angry","mid")
    call ton_main("And then I whispered the truth into his ear...","open","base","base","mid")
    call ton_main("That he's' a dirty-little \"tit-addict!\"","horny","base","angry","mid")
    g9 "You naughty girl!"
    call ton_main("*Ugh*... He went redder than a tomato when I said that.","horny","base","base","ahegao")
    call ton_main("And as both you and I know there's only one cure for that...","open","closed","base","mid")
    call ton_main("So I grabbed his wrist and forced it up to my chest!","base","base","angry","mid")
    m "Just like that?"
    call ton_main("He was hardly going to grab them himself!","upset","base","base","R")
    call ton_main("Besides, grabbing them is the only way to get them off his mind...","open","closed","base","mid")
    call ton_main("Or at least that's what I told him...","base","base","angry","mid")
    m "And he believed you?"
    call ton_main("Maybe... Maybe not...","base","base","base","R")
    call ton_main("All I know is that he wasn't afraid to give it a go.","horny","base","base","mid")
    m "I gather that he enjoyed himself?"
    call ton_main("He just sat there, silently groping my tits for several minutes...","horny","base","angry","mid")
    call ton_main("*Ugh*... It took everything I had not to hold him down and jump his bone...","open_wide_tongue","base","base","ahegao")
    m "[tonks_name]..."
    call ton_main("Right, well after letting him play with them for a little while, I sent him back to class.","smile","happyCl","base","mid")
    m "Think you'll gain any reputation from this encounter?"
    call ton_main("*Hmmm*... I'm not sure if he'll talk...","upset","base","base","R")
    call ton_main("But the fact I ask students to stay behind after class should start spreading some rumours.","base","base","angry","mid")
    m "Good to hear. That'll be all then, [tonks_name]."
    call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    call increase_house_points(house="s", points=40)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    call play_sound("door")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans="fade")

    if ton_reputation <= 7 and nt_pr_grope.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("That shy \"Ravenclaw boy\" stayed behind in class again...","base","base","base","mid")
                call ton_main("He almost suffocated himself in between my cleavage...","smile","happyCl","base","mid")
                m "Well done, [tonks_name]... We'll talk next time."
                call ton_main("Yes, [ton_genie_name]. Have a good night.","base","base","base","mid")
                call increase_house_points(house="r", points=20)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                jump end_tonks_event

    m "So, how are you finding the education industry?"
    call ton_main("Fun!","smile","happyCl","base","mid")
    call ton_main("I never though lesson planning and marking tests would actually be enjoyable, but there's something rather cathartic to it...","open","base","base","mid")
    m "And your...other tasks?"
    call ton_main("Oh, of course messing around with our students is a nice bonus!","horny","base","base","mid")
    m "Speaking of..."
    call ton_main("Don't worry, I've got a story for you, old man.","base","base","angry","mid")
    call ton_main("Remember that shy \"Ravenclaw boy\" I had touch himself for me the other day?","open","base","base","R")
    m "Maybe, but go on..."
    call ton_main("He stayed behind after class today...","base","base","base","mid")
    m "He asked you to buy a favour from him?"
    call ton_main("No,...he's too shy. He wouldn't have the courage to do that...","open","base","worried","down")
    call ton_main("He just - sort of - stayed in his seat after class...while looking down at his desk.","open","base","worried","mid")
    call ton_main("I waited until every other student had left, and then locked the door...","open","closed","base","mid")
    g9 "Who wouldn't want to be locked-up together with you!"
    call ton_main("It's more to keep the other students out...","angry","base","worried","R")
    call ton_main("But that doesn't mean he didn't gasp a little when I did it.","horny","base","angry","mid")
    call ton_main("So, after that, I went over and asked if there was anything wrong.","open","closed","base","mid")
    call ton_main("He just began mumbling about being sorry I had to give him detention...","open","base","base","mid")
    call ton_main("And promised he'd never do anything bad in class again...","open","base","base","R")
    call ton_main("Those poor \"Ravenclaws\" sure do care about school!","smile","happyCl","base","mid")
    call ton_main("I made sure to let him know he was forgiven...","base","base","base","mid")
    m "How very wholesome of you..."
    call ton_main("However,...after this was done, he didn't give any inclination he wanted to get up from his seat...","open","closed","base","mid")
    call ton_main("So, I figured he wanted to fool around again...","base","base","angry","mid")
    call ton_main("And boy was I right!","horny","base","base","ahegao")
    call ton_main("His face lit right up, when I asked if he wanted to buy another favour...","base","base","base","mid")
    call ton_main("Perhaps cupping a feel of his teacher's tits!","horny","base","angry","mid")
    g9 "Naughty!"
    call ton_main("He had such and awe-struck look on his face... looking pretty nervous at first...","angry","base","base","ahegao")
    call ton_main("It made it difficult for me to tell where his mind was going, that cheeky bugger!","angry","closed","angry","mid")
    m "Which was?"
    call ton_main("Straight in for the motorboat!","base","base","angry","mid")
    m "Good on him..."
    g9 "Did he do the noise as well?"
    call ton_main("No...{w} it was more like a hug if I'm being honest.","upset","base","angry","up")
    call ton_main("He just went in, face first into my cleavage, while locking his hands together behind my back.","open","base","angry","mid")
    call ton_main("I thought I would've needed a lot more coaxing-into...","smile","happyCl","base","mid")
    m "I suppose guys might be a bit different in that regard..."
    m "So where did it go from there?"
    call ton_main("Nowhere, really...{w} He just stared nuzzling his face into my tits...","open","base","worried","L")
    call ton_main("Grinding himself against my thigh, while giving me the tightest hug of his life...","angry","base","base","ahegao")
    m "Sound's like heaven..."
    call ton_main("It was pretty cute if you ask me.","base","happyCl","base","mid")
    m "How long did this \"hug\" last exactly?"
    call ton_main("*Pfff*... Five...maybe ten minutes...","upset","base","angry","up")
    call ton_main("Eventually, it all got a bit to much...and he broke-off the hug...","open","base","base","R")
    call ton_main("Stammered a thanks, and ran-off.","angry","base","sad","down")
    m "Did even get to reward any points?"
    call ton_main("I did, even if he wasn't there to hear it...","base","happyCl","base","mid")
    m "Very good. That'll be all then."
    call ton_main("Have a good night, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    call increase_house_points(house="r", points=20)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys
    call play_sound("door")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans="fade")

    if ton_reputation <= 7 and nt_pr_grope.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I let those two \"Gryffindors\" feel me up again...","open","base","base","R")
                call ton_main("Of course they didn't get any points for it...","base","base","angry","mid")
                m "Great job, [tonks_name]..."
                call ton_main("Thank you, [ton_genie_name]. Have a good night.","base","base","base","mid")
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                jump end_tonks_event

    m "I think I noticed a few extra points for \"Gryffindor\" today..."
    m "Does that mean what I think it does?"
    call ton_main("Perhaps...","base","base","base","mid")
    m "So,...you let one of Granger's friends cop a feel?"
    call ton_main("Kind of...","upset","base","base","R")
    call ton_main("It might have been \"two boys\" today...","open","base","base","R")
    m "Nice, selling two favours in one day should get the word around..."
    call ton_main("Well... it wasn't exactly two favours...","angry","base","base","down")
    m "Oh... Wait, Oh...{w} I see..."
    call ton_main("They're such good friends! I don't think I could manage splitting them apart...","smile","happyCl","base","mid")
    call ton_main("Besides, I've already fooled around a little with them, so they were barely any convincing involved...","base","base","angry","mid")
    m "I'm sure there wasn't... so how was it?"
    call ton_main("Honestly? Pretty fucking hot...","horny","base","angry","mid")
    call ton_main("Having four hands grabbing at you at once is {b}intense{/b}...","horny","base","angry","ahegao")
    m "I bet...{w=0.3} So did they just play with your tits?"
    call ton_main("They did at first...{w} But then I quickly found one of their hands somewhere else...","base","base","angry","mid")
    call ton_main("Pretty soon after that, they each moved the other onto my ass as well...","horny","base","base","ahegao")
    call ton_main("*Ugh*... I had to draw the line once they tried groping me under my shirt...","angry","base","base","ahegao")
    m "*Mmmm*... did you?"
    call ton_main("I don't think I would have been able to stop them at all if I didn't...","open","closed","base","mid")
    call ton_main("Or myself, for that matter...","upset","base","base","ahegao")
    call ton_main("Not that it would have been the worst-thing-in-the-world to let them touch my tits directly...","open","base","base","R")
    call ton_main("Anyhow, I offered them some house-points for it,...but to my surprise they both kindly refused...","open","closed","base","mid")
    call ton_main("Said they'd much rather have a go-at-it again...","base","base","angry","mid")
    m "Think they'll spread the word this time?"
    call ton_main("They were both pitching a pretty-big-tent when they left class... that was noticeable to say the least...","smile","happyCl","base","mid")
    m "Very good, [tonks_name], very good..."
    call ton_main("Thank you, sir.","base","happyCl","base","mid")
    call ton_main("Now, if you don't mind,...I think I better head to my room for some...{w} \"unwinding\"...","angry","base","worried","R")
    m "Have a good night then..."
    call ton_main("Night, [ton_genie_name]!","smile","happyCl","base","mid")

    # Tonks leaves

    # No points for Gryffindor.
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    call play_sound("door")
    call ton_main("Hi, [ton_genie_name].", face="horny", xpos="mid", ypos="base", trans="fade")

    if ton_reputation <= 7 and nt_pr_grope.points < 4: # First time.
        pass
    else: # Repeat.
        menu:
            m "(...)"
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                call ton_main("I tried my luck with that \"Slytherin girl\" again...","open","base","base","mid")
                call ton_main("She's the hardest nut to crack, I tell you...","open","base","worried","R") # hardest instead of tough in the UK.
                m "You will have better luck next time, [tonks_name]..."
                call ton_main("I hope so too, [ton_genie_name]... Have a good night.","base","base","worried","mid")
                call increase_house_points(house="s", points=40)
                if ton_reputation < 9: # Points til 9.
                    $ ton_reputation += 1
                jump end_tonks_event

    m "How's my favourite teacher doing today?"
    call ton_main("Never been better!","smile","happyCl","base","mid")
    m "I take it you were able to buy a favour then?"
    call ton_main("You bet! Even if she might not have wanted to sell it at first...","base","base","angry","mid")
    g9 "A She?"
    call ton_main("Remember that naive \"Slytherin\" that couldn't keep her eyes off me?","open","base","angry","mid")
    m "I think so..."
    call ton_main("Well, I held her back after class again.","open","closed","base","mid")
    call ton_main("Of course she made a fit about it... Not that she made any efforts to leave, though...","open","base","worried","R")
    call ton_main("So, I sat her down, and had a little conversation with her.","base","base","base","mid")
    m "About what?"
    call ton_main("You know,... girl talk...","open","closed","base","mid")
    call ton_main("How it's okay to be a little - \"sexually confused\" sometimes...","open","base","base","R")
    call ton_main("And that - maybe - she just needed to get it all out of her system...","base","base","base","mid")
    m "How did she take that?"
    call ton_main("She kept insisting of not having the slightest idea of what I was talking about.","base","base","angry","mid")
    call ton_main("Even though her eyes were glued to my chest as she spoke....","base","base","base","down")
    m "*Mhmm*................"
    call ton_main("Eventually, I just grabbed her wrist and pulled it up to meet my chest...","horny","base","angry","mid")
    m "Just like that?"
    call ton_main("*Mhmm*... It was fantastic!","base","base","base","ahegao")
    call ton_main("You should have seen the war-of-emotions taking place behind her eyes!","horny","base","angry","mid")
    call ton_main("It was incredible! I love seeing \"Slytherins\" get all flustered like that.","base","base","angry","mid")
    m "Sweet... What happened next?"
    call ton_main("She calmed down a bit once I offered her points for this little favour...","base","happyCl","base","mid")
    m "That calmed her down?"
    call ton_main("Apparently. After all, this wasn't the first favour I bought off her...","horny","base","angry","mid")
    m "Did she start playing with you after that?"
    call ton_main("Not exactly, she just sat there face bright-red, whilst she let me hold her hands against my breasts...","angry","base","worried","down")
    call ton_main("And I let her go a couple of seconds after that...","open","base","worried","L")
    m "Do you think she'll spread the word that you're buying favours?"
    call ton_main("I can't say... I think she's still pretty conflicted about the whole thing...","upset","base","worried","down")
    m "Do you really think she's a lesbian?"
    call ton_main("Maybe... she does seem a little {b}curious{/b}...","open","base","base","mid")
    call ton_main("Couple that with her being a stubborn \"Slytherin\"...","open","base","base","R")
    call ton_main("She's a whole mix of confused emotions... but she'll figure it out.","base","base","base","mid")
    m "Let's hope this isn't a hopeless cause..."
    call ton_main("Don't be silly,...she's perfect!{w} Just the way I like them.","horny","base","base","ahegao")
    m "........................"
    m "Well, keep me informed... That should be all for now..."
    call ton_main("Yes, [ton_genie_name]!","base","base","base","mid")

    # Tonks leaves

    call increase_house_points(house="s", points=40)
    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event



### Tier 2 ###

label nt_pr_grope_T2_E1: # Tier 2 - Event 1
    #Begrudgingly talks about how pretty tonks is


label nt_pr_grope_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy again
    #breastfeeding and mommy play



label nt_pr_grope_T2_E3: # Tier 2 - Event 3
    #hufflepuff girl comes in asking for another favour
    #ends up sucking tonks boobs



label nt_pr_grope_T2_E4: # Tier 2 - Event 4 -
    #Tonks has her a slyhterin girl sit there and do work while she has no top on
