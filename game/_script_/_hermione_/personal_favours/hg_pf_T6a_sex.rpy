

### Hermione Sex ###

label hg_pf_sex:

    if hg_pf_blowjob.counter < 1:
        m "{size=-4}(Should I ask her to have sex with me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 65
    $ hg_pf_sex.start()


    # End Event
    label end_hg_pf_sex:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ face_on_cg = False
    hide screen ccg

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)


    # Points
    m "Yes, [hermione_name]. [current_payout] points to the Gryffindor house."
    $ gryffindor += current_payout
    call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")


    # Hermione leaves
    call her_walk("door", "base")

    call her_chibi("leave")


    # Increase level
    $ hg_sex.trigger = True
    $ hg_anal.trigger = True
    if her_whoring < 24: #Adds points till 24.
        $ her_whoring += 1

    $ achievement.unlock("nerdgasm")

    jump end_hermione_event

### Fail Events ###

label hg_pf_sex_fail:
    call bld
    m "[hermione_name]..."
    m "Why don't you come over here and I pound your pussy for a bit..."
    g9 "With my cock!"

    $ hg_pf_sex.counter -= 1

    jump too_much

### Tier 1 ###

# Event 1 (i) - First time sex
# Event 2 (i) - Sex with different dialogue
# Event 2 (i) - Anal option
# Event 3 (r) - Regular or anal sex

label hg_pf_sex_T1_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
    m "[hermione_name]?"
    call her_main("[genie_name]?", "soft", "base", "base", "mid")
    m "The favour I will be buying from you today..."
    call her_main(".......?", "base", "base", "base", "mid")
    m "How should I put this delicately...?"
    call her_main("Is it sex, [genie_name]?", "base", "squint", "base", "mid")
    m "Well, yes. How did you...?"
    call her_main("Not a terribly difficult deduction all things considered...", "base", "narrow", "base", "mid_soft")
    m "You don't mind then?"
    call her_main("Of course, I mind, [genie_name]!", "upset", "closed", "base", "mid")
    her "I am not a prostitute!"
    m "But you'll do it anyway??"
    if gryffindor < hufflepuff or gryffindor < slytherin or gryffindor < ravenclaw:
        call her_main("Gryffindor is falling behind again...", "open", "closed", "base", "mid")
    else:
        call her_main("I have to make sure Gryffindor stays in the lead...", "open", "closed", "base", "mid")
    her "What choice do I have...?"
    m "Great!"

    call hg_sex_1

    jump end_hg_pf_sex


label hg_pf_sex_T1_intro_E2:
    call her_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
    m "[hermione_name]..."
    m "Last night I had a dream..."
    g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
    call her_main("In that dream, [genie_name]...", "upset", "closed", "base", "mid", xpos="right", ypos="base")
    call her_main("Did I happen to receive sixtyfive house points afterwards?", "angry", "base", "angry", "mid")
    g9 "Why yes, you did, [hermione_name]."
    call her_main("...............................", "disgust", "narrow", "base", "mid_soft")
    if hermione.is_worn("panties"):
        her "Let me just take my panties off..."
        $ hermione.strip("panties")
    else:
        call her_main("Good I didn't wear my panties today...", "disgust", "base", "base", "down")
    call hg_sex_2

    jump end_hg_pf_sex

label hg_pf_sex_T1_intro_E3:
    call her_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
    m "[hermione_name], are you keeping your pussy wet and ready for me?"
    call her_main("[genie_name]!", "scream", "closed", "angry", "mid")
    m "Just say \"I do\" and come over here, [hermione_name]."
    call her_main("...........", "open", "base", "base", "mid")
    call her_main("I do....", "angry", "narrow", "base", "down")
    stop music fadeout 1.0

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("lie_on_desk")
    with fade
    pause.5

    call bld
    m "*Hmmm*... (Now that I look at it, I feel like fucking her ass...)"

    menu:
        m "(Where should I put it in?)"
        "-Fuck her pussy-":
            m "(On second thought, this hole is still good enough for me...)"
            call hg_sex_2

        "-Poke her butthole!-":
            g4 "(Yes! Let's see if she's willing to take it up her ass!)"
            call hg_anal_sex_1
            $ hg_anal.trigger = True
            $ current_payout = 90

    jump end_hg_pf_sex


label hg_pf_sex_T1_E3: # repeats
    call her_main("", "base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
    m "[hermione_name], are you keeping your pussy wet and ready for me?"
    call her_main("[genie_name]...", "disgust", "base", "worried", "down")
    m "Just say \"I do\" and come over here, [hermione_name]."
    call her_main("...........", "open", "base", "base", "mid")
    call her_main("I do....", "angry", "narrow", "base", "down")
    stop music fadeout 1.0

    call her_chibi_scene("lie_on_desk")
    with fade
    pause.5

    call bld

    menu:
        g4 "(How should I fuck her this time?)"
        "-Use her pussy!-":
            m "(On second thought, this hole is still good enough for me...)"
            call hg_sex_2

        "-Fuck her asshole!-":
            g4 "(Let's see how well she takes it up the ass this time!)"
            $ hg_anal.trigger = True
            $ current_payout = 90
            call hg_anal_sex_2

    jump end_hg_pf_sex

### First Time Sex ###

label hg_sex_1:
    stop music fadeout 1.0
    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("grope_ass_back", trans=fade)
    pause.5

    call her_main(".............", "upset", "closed", "base", "mid", ypos="head")
    call her_main("!!!!!!!!!!!!!!!", "angry", "wide", "base", "stare")
    if hermione.is_worn("panties"):
        m "Relax, [hermione_name]. I'm Just gonna take off your panties."
        $ hermione.strip("panties")
    else:
        m "Relax, [hermione_name]..."
    call her_main("..............", "angry", "base", "angry", "mid")
    m "Are you ready?"
    call her_main("No...", "annoyed", "narrow", "annoyed", "mid")
    m "Good girl."
    show screen blkfade
    with d5
    pause.2

    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris

    if use_cgs:
        $ face_on_cg = True
        $ ccg_folder = "herm_sex"
        $ ccg1 = "blank"
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        hide screen blkfade
        call her_main("", "normal", "worriedCl", "worried", "mid", ypos="head", trans=d5)
    else:
        call her_chibi_scene("sex", trans=d5)
    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}", "scream", "wide", "base", "stare")
    hide screen bld1
    call ctc

    call play_music("playful_tension") # SEX THEME.

    g4 "Your pussy... It's so tight."
    call her_main("................", "normal", "worriedCl", "worried", "mid")
    m "You alright?"
    call her_main("A-ha... It's too big...", "angry", "base", "base", "mid", tears="soft")
    call her_main("You will rip me apart, [genie_name]!")
    m "Nonsense! My cock is of a regular size."
    m "It's not my fault that you are so tiny."
    call her_main("......................", "normal", "worriedCl", "worried", "mid")

    menu:
        "\"You should be ashamed of yourself!\"":
            #$ ccg2 = 20
            call her_main("I am not ashamed, [genie_name]!", "normal", "worriedCl", "worried", "mid")
            call her_main("I am doing this for the sake of my house!")
            call her_main("To help my--")
            call her_main("ah-ha-a...", "open", "worriedCl", "worried", "mid")
            call her_main("My housemates depend on me... ah-a...")
            m "Are you sure that's the only reason?"
            call her_main("I don't know--", "normal", "worriedCl", "worried", "mid")
            call her_main("ah-a...{image=textheart}", "open", "worriedCl", "worried", "mid")
            call her_main("I don't know what you mean, [genie_name].", "angry", "narrow", "base", "down")
            m "It seems to me that you are enjoying this a little bit too much."
            #$ ccg2 = 21
            call her_main("I'm not, [genie_name]!", "angry", "narrow", "base", "down")
            m "Really?"
            call her_main("......................", "normal", "worriedCl", "worried", "mid")
            m "Then why is your pussy so wet?"
            call her_main("....................a-ha.{image=textheart}", "open", "worriedCl", "worried", "mid")
            m "Admit it, you enjoy getting fucked by your [genie_name]!"
            #$ ccg2 = 25
            call her_main("I do not!", "normal", "worriedCl", "worried", "mid")
            m "Stubborn girl..."
            call her_main("Ah-ha...{image=textheart}", "open", "worriedCl", "worried", "mid")

        "\"So... What's new in your life?\"":
            #$ ccg2 = 14
            call her_main("...[genie_name]?", "open", "base", "base", "mid")
            m "Just trying to have a polite conversation."
            #$ ccg2 = 17
            call her_main("Ah-ah...{image=textheart} But... ah...{image=textheart}{image=textheart}", "open", "base", "base", "mid")
            m "Any news from your folks?"
            call her_main("My parents?", "angry", "worriedCl", "worried", "mid", emote="05")
            call her_main("[genie_name], please, *ah-ah* I cannot talk...", "open", "worriedCl", "worried", "mid")
            m "Why not? Enjoying this too much?"
            call her_main("I am not... ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
            m "I think you are."
            call her_main("I am only doing this for the points, [genie_name]...", "open", "worriedCl", "worried", "mid")
            m "Oh, I see..."
            m "So you are like a prostitute then."
            call her_main("What?", "angry", "base", "base", "mid")
            m "Well I pay you to have sex with me. How would you call that?"
            call her_main("...........", "angry", "narrow", "base", "down")
            #$ ccg2 = 19
            call her_main("I am not a prostitute...", "open", "worriedCl", "worried", "mid")
            call her_main("Why are you being so mean to me, [genie_name]?", "angry", "base", "base", "mid", tears="soft")
            m "I think you like it when I'm mean."
            call her_main("I do not!", "mad", "base", "worried", "mid", tears="soft")
            m "Really? Then why is your pussy so wet?"
            call her_main("Not because of that!", "angry", "narrow", "base", "down")
            m "If you say so..."
            #$ ccg2 = 20
            call her_main("A-ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
            call her_main("I am... ah...{image=textheart} not a prostitute...", "shock", "worriedCl", "worried", "mid")

        "\"......................................................\"":
            #$ ccg2 = 14
            call her_main("A-ha... ah...", "open", "worriedCl", "worried", "mid")
            m "*Panting!*"
            call her_main("Ah... ha-aha...", "open", "worriedCl", "worried", "mid")
            m "Oh..."
            call her_main("Ah-ah...", "open", "worriedCl", "worried", "mid")
            m "......................"
            call her_main("Ah... ah...", "open", "worriedCl", "worried", "mid")
            call her_main("Ah... [genie_name]?", "open", "base", "base", "mid")
            m "What is it?"
            #$ ccg2 = 17
            call her_main("Ah... Do you.... like it?", "open", "worriedCl", "worried", "mid")
            m "Do I like drilling your super-tight pussy?"
            m "Very much so, [hermione_name]. Why?"
            call her_main(".....................", "normal", "worriedCl", "worried", "mid")
            call her_main("Ah... You just got so quiet...", "open", "worriedCl", "worried", "mid")
            m "Just enjoying the moment, [hermione_name]."
            m "What about you? You alright?"
            call her_main("Ah... yes...", "open", "worriedCl", "worried", "mid")
            call her_main("It hurts a little though, ah...", "open", "base", "base", "mid")
            call her_main("Your penis is too big... ah...", "open", "worriedCl", "worried", "mid")
            m "Hm..."
            m "You need me to slow down or something?"
            #$ ccg2 = 20
            call her_main("No, [genie_name]... You don't have to...", "open", "base", "base", "mid")
            call her_main("Please, don't mind me... Enjoy yourself.", "normal", "worriedCl", "worried", "mid")
            call her_main("I will... ah... Get used to it eventually... ah...")
            m "As you say, [hermione_name]."
            #$ ccg2 = 21
            call her_main("Ah-a...{image=textheart}", "open", "worriedCl", "worried", "mid")
            m "Yes, this is great!"

    call her_main("Ah-ah...{image=textheart}", "open", "worriedCl", "worried", "mid", ypos="head")

    if daytime:
        m "Going to classes after this?"
    else:
        m "Going to bed after this?"

    #$ ccg2 = 22
    call her_main("Yes, ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    call her_main("If I'll be able to walk...")
    g4 "Ght! {image=textheart} Yes, you always say the right things, [hermione_name]!"
    call her_main("Ah...{image=textheart} ah...{image=textheart}{image=textheart}", "shock", "worriedCl", "worried", "mid")
    #$ ccg2 = 24
    call her_main("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}", "scream", "wide", "base", "stare", trans=hpunch)
    m "Huh? You alright?"
    call nar(">Hermione's legs are shaking...")
    m "[hermione_name]?"
    #$ ccg2 = 28
    call her_main("{image=textheart}{image=textheart}{image=textheart}I think I'm cumming, [genie_name]!{image=textheart}{image=textheart}{image=textheart}", "scream", "wide", "base", "stare")
    g9 "Tch... You nasty slut!"
    #$ ccg2 = 29
    call her_main("AAH! I can't hold it!", "silly", "narrow", "base", "dead")
    g4 "You need to be punished for being such a slut!"
    call nar(">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!")

    if not use_cgs:
        call her_chibi_scene("sex_fast", trans=d5)

    #$ ccg2 = 30
    call her_main("NO! STOP! PLEASE!", "scream", "wide", "base", "stare", trans=hpunch)
    g4 "Who told you you could cum, slut? This is your punishment!"
    call her_main("[genie_name], no, ah-a!{image=textheart}", "open", "worriedCl", "worried", "mid")
    #$ ccg2 = 31
    call her_main("Ah-a...{image=textheart}I will go insane!{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")
    g4 "{size=+7}Grragh!{/size}"
    hide screen bld1
    with d1
    call ctc

    #$ ccg2 = 32
    call her_main("No...{image=textheart} ah...{image=textheart}", "silly", "narrow", "annoyed", "up")
    #$ ccg2 = 33
    call her_main("I think I will...{image=textheart} pass out...{image=textheart}", ypos="head")
    g4 "ARGH! YOU WHORE!"

    menu:
        "-Cum all over Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)

            $ ccg3 = "s3"
            call cum_block
            call ctc

            #$ ccg2 = 42
            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
            hide screen bld1
            call ctc

            if not use_cgs:
                call her_chibi_scene("sex_cum_out_done", trans=d5)

            m "Well, that was rather intense..."
            #$ ccg2 = 28
            call her_main("*heavy panting*", "open_wide_tongue", "narrow", "annoyed", "up")
            m "You alright?"
            call her_main("Ah... yes...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
            #$ ccg2 = 29
            call her_main("My legs are still shaking...{image=textheart}")
            hide screen bld1
            with d1
            call ctc

            hide screen ccg
            $ hermione_flip = 1 #Default
            $ face_on_cg = False
            call her_chibi_scene("sex_cum_in_done", trans=d5)

            if daytime:
                call her_main("But I think I will be able to make it to my classes...", "silly", "narrow", "base", "dead", ypos="head")
            else:
                call her_main("But I think I will be able to make it to the common room...", "silly", "narrow", "base", "dead", ypos="head")

            m "Good."
            m "Did you enjoy getting fucked by your [genie_name]?"
            call her_main("[genie_name], I am only doing this for my house.", "grin", "narrow", "annoyed", "up")
            m "Seriously? Still?"
            call her_main("Could I just get paid now... please?", "open", "worriedCl", "worried", "mid")

            return

        "-Cum inside Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)

            $ ccg3 = "s1"
            call cum_block
            call ctc

            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
            hide screen bld1
            with d1
            call ctc

            if not use_cgs:
                call her_chibi_scene("sex_cum_in_done", trans=d5)

            call her_main("You came inside of me...", "silly", "narrow", "base", "dead")
            g9 "I sure did."
            hide screen bld1
            with d1
            call ctc

            hide screen ccg
            $ face_on_cg = False
            call her_chibi_scene("sex_cum_out_done", trans=d5)

            call her_main("But...", "silly", "narrow", "base", "dead", ypos="head",flip=False)
            m "What?"
            call her_main("What if I get pregnant?", "shock", "worriedCl", "worried", "mid")
            m "Nah, you will be alright..."
            call her_main("How do you know, [genie_name]?", "shock", "worriedCl", "worried", "mid")
            m "We witchers are infertile."
            call her_main("Witchers?", "open", "worriedCl", "worried", "mid")
            m "Sure... You are a witch, that makes me a witcher, right?"
            m "And everyone knows that witchers are infertile..."
            call her_main("[genie_name], you make no sense...", "angry", "base", "base", "mid")
            call her_main("Can I please just get paid now...?")

            return

### Third Time Sex ###

label hg_sex_2:
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d5

    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris

    if use_cgs:
        $ face_on_cg = True
        $ ccg_folder = "herm_sex"
        $ ccg1 = "blank"
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        hide screen blkfade
        call her_main("", "open", "worriedCl", "worried", "mid", ypos="head")
    else:
        call her_chibi_scene("sex", trans=fade)

    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}", "scream", "wide", "base", "stare", ypos="head")
    hide screen bld1
    call ctc

    call play_music("playful_tension") # SEX THEME.

    call her_main("Ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    m "Your pussy feels a bit looser today..."
    #$ ccg2 = 4
    call her_main("Does it...{image=textheart} ah...?{image=textheart}", "open", "worriedCl", "worried", "mid")
    #$ ccg2 = 5
    call her_main("That's all ...ah... because of you [genie_name]...{image=textheart}", "shock", "worriedCl", "worried", "mid")
    #$ ccg2 = 6
    call her_main("You are ruining my cute little pussy with your monstrous penis...{image=textheart}", "silly", "narrow", "annoyed", "up")
    g4 "Agh, you whore!"
    #$ ccg2 = 10
    call her_main("Ah...{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")
    m "Yes! Do you like it when I fuck you like this?"
    call her_main("Yes, [genie_name]...{image=textheart}", "base", "narrow", "base", "mid_soft", ypos="head")

    menu:
        g4 "..."
        "\"Be sweet but passionate.\"":
            m "Yes, you're liking this?"
            #$ ccg2 = 14
            call her_main("I do, [genie_name]... ah...{image=textheart}", "open", "closed", "base", "mid")
            m "Good girl!"
            m "Just relax and take my cock!"
            call her_main("Yes... ah...{image=textheart}", "open", "closed", "base", "mid")
            m "All the way in... all the way..."
            call her_main("Ah...{image=textheart}{image=textheart}", "open", "worriedCl", "worried", "mid")
            m "Yes, my little princess..."
            #$ ccg2 = 15
            call her_main("What?", "angry", "wide", "base", "stare")
            call her_main("No, please don't call me that... ah...{image=textheart}", "angry", "narrow", "base", "down")
            call her_main("My daddy used to call me his little princess when I was little...")
            if genie_name == "Daddy":
                m "Well, you didn't mind calling me daddy earlier!"
                m "Right now I am your daddy!"
            else:
                m "Well, right now I am your daddy!"
            #$ ccg2 = 16
            call her_main("Ah...{image=textheart} ah-ah...{image=textheart}{image=textheart}", "soft", "narrow", "annoyed", "up")
            m "And you are my little princess-slut!"
            #$ ccg2 = 17
            call her_main("Ah...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}", "grin", "narrow", "base", "dead")
            if genie_name == "Daddy":
                her "[genie_name]...{image=textheart}{image=textheart}{image=textheart}"

        "\"Be mean to her!\"":
            m "Yes, you slut!"
            m "I bet you love every second of this!"
            call nar(">You pick up the pace.")
            #$ ccg2 = 17
            call her_main("Ah...{image=textheart} [genie_name]...", "open", "worriedCl", "worried", "mid")
            m "You nasty slut!"
            call her_main("Ah...{image=textheart} ah-a...{image=textheart}", "shock", "worriedCl", "worried", "mid")
            m "You are a disgrace, [hermione_name]!"
            #$ ccg2 = 18
            call her_main("Ah-ah...{image=textheart}{image=textheart}{image=textheart}", "shock", "worriedCl", "worried", "mid")
            m "Your parents sent you here to study, not to screw your teachers, you filthy cunt!"
            #$ ccg2 = 19
            call her_main("Ah-a...{image=textheart} But I am only doing this--", "shock", "worriedCl", "worried", "mid")
            m "Nobody cares why you are doing this, you stupid cocksucker!"
            m "Look at what you've become!"
            m "Butt-naked, cunt full of your headmaster's cock, taking it like a cheap whore!"
            #$ ccg2 = 20
            call her_main("Ah...{image=textheart} No...{image=textheart} stop saying...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")
            call nar(">You pick up the pace some more.","start")

            if not use_cgs:
                call her_chibi_scene("sex_fast", trans=d5)

            call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...","end")
            m "You let me molest you... You suck my cock..."
            m "What are you after that I ask you!?"
            #$ ccg2 = 21
            call her_main("................", "grin", "narrow", "base", "dead")
            call her_main("Ah...{image=textheart} ah....{image=textheart}{image=textheart}{image=textheart}", "shock", "worriedCl", "worried", "mid")
            call her_main(".......................", "angry", "narrow", "base", "down")
            call her_main("{size=-5}I am a whore...{/size}")
            m "Yes! That's exactly what you are!"

    #$ ccg2 = 22
    call her_main("Ah... ah... ah...{image=textheart}", "angry", "narrow", "base", "down", ypos="head")
    call her_main("[genie_name], you think you could... ah...")
    m "What?"
    call her_main("Could you spank me a little... ah...?", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    g4 "Gladly!"
    call slap_her

    #$ ccg2 = 24
    call her_main("Aa-a-ah!{image=textheart}{image=textheart}{image=textheart}", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "You liked that one, huh?"
    call slap_her

    #$ ccg2 = 28
    call her_main("Ah..!{image=textheart} Yes!{image=textheart}{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "And some more!"
    call slap_her

    #$ ccg2 = 29
    call her_main("Ahh! Yes!", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    call nar(">You notice that every time you slap the girl's butt, her pussy clutches your cock ever so slightly...","start")
    ">You love the sensation..."
    ">You unleash another series of slaps on Hermione's ass-cheeks."
    call nar(">Every single one met with a gasp of excitement from the girl.","end")
    #$ ccg2 = 30

    call slap_her
    call slap_her
    call slap_her

    #$ ccg2 = 31
    call her_main("Aah!!!{image=textheart}{image=textheart}{image=textheart} IT HURTS!{image=textheart}{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    #$ ccg2 = 32
    call her_main("It hurts...{image=textheart}{image=textheart}{image=textheart}{w=0.5} It hurts so good...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")
    m "Hm?"
    m "Why are your legs shaking, [hermione_name]?"
    m "Are you cumming?"
    #$ ccg2 = 33
    call her_main("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
    m "Well, I think I will follow your example then."
    call her_main("..............", "silly", "narrow", "base", "dead")
    call nar(">You start fucking Hermione with renewed determination!")
    #$ ccg2 = 34
    call her_main("Ah! No! I can't...{image=textheart} I...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}", "shock", "base", "base", "R", cheeks="blush", tears="soft", ypos="head")
    m "Shut it whore!"
    g4 "Argh!"

    menu:
        "-Cum inside of Hermione-":
            with hpunch
            g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
            call cum_block

            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            $ ccg3 = "s1"

            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)

            call cum_block
            call ctc

            #$ ccg2 = 33
            call her_main("!!!", "silly", "narrow", "base", "dead")
            #$ ccg2 = 38
            call her_main("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}")
            g4 "I'm Not done yet, bitch!"
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            call cum_block
            call her_main("AH! MY WOMB!", "shock", "base", "base", "R", cheeks="blush", tears="soft")
            g4 "{size=+5}SLUT!{/size}"

            hide screen bld1
            with d1
            call ctc

            if not use_cgs:
                call her_chibi_scene("sex_cum_in_done", trans=d5)

            #$ ccg2 = 40
            m "Well, this was pretty great..."
            call her_main("Ah...{image=textheart}", "silly", "narrow", "base", "dead")
            m "You alright there, slut? Ehm, I mean, [hermione_name]."
            call her_main("Yes... I...{image=textheart}", "silly", "narrow", "base", "dead")
            #$ ccg2 = 41
            call her_main("I feel so full...", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("!!!", "scream", "wide", "base", "stare")
            call her_main("You came inside of me, [genie_name]!")
            m "I sure did."
            call her_main("You shouldn't have...", "open", "worriedCl", "worried", "mid")
            m "Didn't you enjoy it?"
            call her_main("....maybe.", "grin", "narrow", "base", "dead")
            #$ ccg2 = 42
            call her_main("I think I came several times...", "soft", "narrow", "annoyed", "up")

            $ face_on_cg = False
            hide screen ccg
            call her_chibi_scene("sex_cum_in_done", trans=d5)

            call her_main("Maybe you are right, [genie_name], and I shouldn't worry so much.", "angry", "wink", "base", "mid", ypos="head",flip=False)
            call her_main("Can I get my payment now?")

            return

        "-Cum all over Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)

            $ ccg3 = "s3"

            call cum_block
            call ctc

            #$ ccg2 = 30
            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
            g4 "{size=+5}You whore! Take this!{/size}"
            call her_main("{size=+5}!!!{/size}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
            hide screen bld1
            with d1
            call ctc

            if not use_cgs:
               call her_chibi_scene("sex_cum_out_done", trans=d5)

            m "Well, that was pretty great..."
            #$ ccg2 = 31
            call her_main("Ah...{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
            m "You alright there, slut?"
            call her_main("Yes... I...", "silly", "narrow", "base", "dead")
            m "Did you enjoy this?"
            #$ ccg2 = 29
            call her_main("....I think so...", "grin", "narrow", "base", "dead")
            call ctc

            $ face_on_cg = False
            hide screen ccg
            call her_chibi_scene("sex_cum_in_done", trans=d5)

            call her_main("I think I came several times, [genie_name]...", "soft", "narrow", "annoyed", "up", ypos="head",flip=False)
            call her_main("Can I get my payment now?", "angry", "wink", "base", "mid")

            return

label hg_sex_luna:
    m "[hermione_name]..."
    m "I have a favour to ask of you..."
    call her_main("Is it sex? {size=-2}Please let it be sex...{/size}", "smile", "base", "base", "R")
    m "You certainly seem eager."
    call her_main(".......", "base", "narrow", "base", "mid_soft")
    call her_main("Well I may have made some plans...", "base", "narrow", "worried", "down")
    her "but I can't tell you what..."
    m "well as long as you bend over my desk I don't really care..."
    call her_main("{image=textheart}{image=textheart}{image=textheart}", "base", "narrow", "worried", "down")
    stop music fadeout 1.0
    hide screen hermione_main
    call blkfade
    # SEX

    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}", "scream", "wide", "base", "stare", ypos="head") #HERMIONE

    call her_chibi_scene("sex", trans=fade)
    call ctc

    call play_music("playful_tension") # SEX THEME.

    call her_main("Ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    m "Your pussy feels drenched today..."
    call her_main("Does it...{image=textheart} ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    call her_main("That's all because of you [genie_name]...{image=textheart}", "shock", "worriedCl", "worried", "mid")

    if daytime:
        call her_main("I've been... looking forward to this all morning...{image=textheart}", "silly", "narrow", "annoyed", "up")
    else:
        call her_main("I've been... looking forward to this all day...{image=textheart}", "silly", "narrow", "annoyed", "up")

    g4 "Agh, you whore!"
    call her_main("Ah...{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")
    m "Yes! Do you like it when I fuck you like this?"
    call her_main("Yes, [genie_name]...", "base", "narrow", "base", "mid_soft")

    call play_sound("knocking")
    call nar(">You hear a knock at the door.")

    menu:
        "\"Who is it?\"":
            m "(Who would be knocking at a time like this?)"
            lun "It's Luna Lovegood sir."
            m "{size=-3}Who's that again, [hermione_name]?{/size}"
            call her_main("the crazy blonde... ah...{image=textheart}... with the nice breasts...", "open", "closed", "base", "mid")
            m "Come in!"
        "-Tell them to go away.-":
            m "Go aw-!"
            call her_main("no [genie_name]... let them in...", "open", "worriedCl", "worried", "mid")
            m "You want to get caught?!"
            call her_main("Ah...{image=textheart} yes...{image=textheart}", "shock", "worriedCl", "worried", "mid")
            m "You are a such a little whore, [hermione_name]!"
            call her_main("Ah-ah...{image=textheart} let them in... please...", "shock", "worriedCl", "worried", "mid")
            m "You asked for it!"
            call her_main("Ah-a...{image=textheart}{image=textheart}{image=textheart}", "shock", "worriedCl", "worried", "mid")
            m "Come in!"

    call nar(">The door opens as Luna Lovegood walks in.")
    call lun_walk("desk", action="enter")

    lun "Hello Professor!"
    #Stop sex
    m "....."
    call her_main("......", "shock", "worriedCl", "worried", "mid")

    lun "I wanted to talk to you about the school uniform."
    m "The uniform?"
    lun "Yes, I have some ideas about some necessary changes and I'd like you to listen."
    m "{size=-3}What's going on here, [hermione_name]?{/size}"

    call her_main("I may have given her a suggestibility serum...", "silly", "narrow", "annoyed", "up")
    m "{size=-3}A suggestibility serum?{/size}"
    lun "Who are you talking to sir?"
    m "Oh, um.... no one, just ignore me..."
    lun "Ok then, I'll ignore you..."
    call her_main("I may have suggested that she come here...", "silly", "narrow", "annoyed", "up")
    call her_main("And that she be unable to see me...", "silly", "narrow", "annoyed", "up")
    m "But what about me and my lack of clothes?"
    her "{image=textheart}"
    lun "*ahem*"
    lun "As I was saying sir, the school uniform simply cannot stay as it is."

    call nar(">You pick up the pace some more.")
    pause.2

    call her_chibi_scene("sex_fast", trans=d5)
    pause.8

    call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...")
    call her_main("Ah...{image=textheart} ah...{image=textheart} ah...{image=textheart}", "angry", "narrow", "base", "down")
    m "{size=-3}So let me get this straight.{/size}"
    m "{size=-3}You drugged your class mate...{/size}"
    m "{size=-3}Just so she would come in here and watch you have sex with your headmaster.{/size}"
    call her_main("Ah... yes...{image=textheart}{image=textheart}{image=textheart}")
    lun "The uniforms us girls are supposed to wear are far too conservative!"
    m "conservative?"
    lun "Indeed! Miss Granger is the only student that is dressing appropriately."
    if cho_whoring > 16:
        lun "And I guess Cho Chang as well."
    if ast_whoring > 16:
        lun "And.. Astoria Greengrass..."
    if sus_whoring > 16:
        lun "...and Susan Bones..."
    if ton_friendship > 50:
        lun "...and perhaps Miss Tonks, but she's our teacher!"
        
    call her_main("ah...", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "{size=-3}What else did you do to her?{/size}"
    call her_main("I may have suggested her to... ah...{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("...act like the a total slut...{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "{size=-3}So just like you then?{/size}"
    call her_main("Yessss...{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    lun "[lun_genie_name], are you listening?"
    m "Sorry [lun_name], go on."
    lun "Thank you. As I was saying I think you need to enact several new policies regarding school uniform."
    lun "Everyone should strive to achieve the same level of perfection as Miss granger."
    call her_main("{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    lun "I've come up with several rules that should help achieve great results and I hoped you would help me out on this."
    m "Alright..."
    lun "{b}Rule number one:{/b} shirts must reveal a minimum of 3 inches of cleavage."
    call her_main("{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    lun "{b}Rule number two:{/b} No skirt over 5 inches worn should be worn."
    call her_main("{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    lun "{b}Rule number three:{/b} No bras to be worn... at {u}any{/u} time."
    call her_main("{image=textheart}{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    lun "And finally, {b}Rule number four:{/b} No panties are allowed at the school grounds."
    call her_main("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")

    m "Why are your legs shaking, [hermione_name]?"
    m "Are you cumming? In front of your classmate?"
    call her_main("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
    m "Well, I think I will follow your example then."
    call her_main("..............", "silly", "narrow", "base", "dead")
    call nar(">You start fucking Hermione with renewed determination!")
    call her_main("Ah! No! I can't...{image=textheart} not in front of...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    lun "Headmaster, are you alr-"
    m "Shut it whore!"
    lun "Yes sir."
    g4 "Argh!"
    with hpunch
    g4 "{size=+7}Argh!!!{/size}"
    call cum_block
    g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

    call her_chibi_scene("sex_cum_out", trans=d5)
    call cum_block
    call ctc

    call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")
    g4 "{size=+5}You fucking whore! Take this!{/size}"
    call her_main("{size=+5}!!!{/size}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    hide screen bld1
    with d1
    call ctc

    call her_chibi_scene("sex_cum_out_done", trans=d5)

    call bld
    m "Well, that was pretty great..."
    call her_main("Ah...{image=textheart}{image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")
    m "You good, slut?"
    call her_main("Yes...", "silly", "narrow", "base", "dead")
    m "Enjoyed yourself?"
    call her_main("....A whole lot...", "grin", "narrow", "base", "dead")
    call ctc

    call blkfade
    call lun_chibi("hide") #Moving it so it won't overlap with Hermione's Chibi (stands at desk).

    call her_main("I think I came several times, [genie_name]...", "soft", "narrow", "annoyed", "up")
    m "Well that'll do for now. You two best head to class."
    call her_main("yes sir...", "grin", "narrow", "base", "dead")
    call her_main("Come on Luna let's go.", "grin", "narrow", "base", "dead")
    lun "Hermione! WHen did you get here?"
    lun "And what are you covered in?"
    call her_main("It doesn't matter...", "soft", "narrow", "annoyed", "up")
    call her_main("{size=-7}You can lick it off later...{/size}", "soft", "narrow", "annoyed", "up")

    return