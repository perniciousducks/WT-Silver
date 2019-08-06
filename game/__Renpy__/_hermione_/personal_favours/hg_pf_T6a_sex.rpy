

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
    hide screen g_c_c_u

    call hg_chibi_transition("stand", xpos="desk", ypos="base", flip=False, trans="fade")

    if her_mood != 0:
        call her_main("","annoyed","angry", xpos="mid", ypos="base")
    else:
        call her_main("","base","base", xpos="mid", ypos="base")


    # Points
    m "Yes, [hermione_name]. [current_payout] points to the \"Gryffindor\" house."
    $ gryffindor += current_payout
    call her_main("Thank you, [genie_name]...","soft","baseL")


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_chibi(action="leave")


    # Increase level
    $ hg_T6_sex_trigger = True
    if her_whoring < 24: #Adds points till 24.
        $ her_whoring += 1

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
    call her_main("","base","base", xpos="right", ypos="base", trans="fade")
    m "[hermione_name]?"
    call her_main("[genie_name]?","soft","base")
    m "The favour I will be buying from you today..."
    call her_main(".......?","base","base")
    m "How should I put this delicately...?"
    call her_main("Is it sex, [genie_name]?","base","suspicious")
    m "Well, yes. How did you...?"
    call her_main("Not a terribly difficult deduction all things considered...","base","glance")
    m "You don't mind then?"
    call her_main("Of course, I mind, [genie_name]!","upset","closed")
    her "I am not a prostitute!"
    m "But you'll do it anyway??"
    call her_main("\"Gryffindor\" is falling behind again...","open","closed")
    her "What choice do I have...?"
    m "Great!"

    call hg_sex_1

    jump end_hg_pf_sex


label hg_pf_sex_T1_intro_E2:
    call her_main("","base","base", xpos="right", ypos="base", trans="fade")
    m "[hermione_name]..."
    m "Last night I had a dream..."
    g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
    call her_main("In that dream, [genie_name]...","upset","closed", xpos="right", ypos="base")
    call her_main("Did I happen to receive 65 house points afterwards?","angry","angry")
    g9 "Why yes, you did, [hermione_name]."
    call her_main("...............................","disgust","glance")
    her "Let me just take my panties off..."

    call hg_sex_2

    jump end_hg_pf_sex


label hg_pf_sex_T1_intro_E3:
    call her_main("","base","base", xpos="right", ypos="base", trans="fade")
    m "[hermione_name], are you keeping your pussy wet and ready for me?"
    call her_main("[genie_name]!","scream","angryCl")
    m "Just say \"I do\" and come over here, [hermione_name]."
    call her_main("...........","open","base")
    call her_main("I do....","angry","down_raised")
    stop music fadeout 1.0

    call her_walk_desk_blkfade

    call hg_chibi_transition("admire_ass", flip=True, trans="fade")
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
            $ current_payout = 90

    jump end_hg_pf_sex


label hg_pf_sex_T1_E3: # repeats
    call her_main("","base","base", xpos="right", ypos="base", trans="fade")
    m "[hermione_name], are you keeping your pussy wet and ready for me?"
    call her_main("[genie_name]!","scream","angryCl")
    m "Just say \"I do\" and come over here, [hermione_name]."
    call her_main("...........","open","base")
    call her_main("I do....","angry","down_raised")
    stop music fadeout 1.0

    call hg_chibi_transition("admire_ass", flip=True, trans="fade")
    pause.5

    call bld

    menu:
        g4 "(How should I fuck her this time?)"
        "-Use her pussy!-":
            m "(On second thought, this hole is still good enough for me...)"
            call hg_sex_2

        "-Fuck her asshole!-":
            g4 "(Let's see how well she takes it up the ass this time!)"
            call hg_anal_sex_2

    jump end_hg_pf_sex



### First Time Sex ###

label hg_sex_1:
    stop music fadeout 1.0
    call her_walk_desk_blkfade

    call hg_chibi_transition("grope_ass", flip=True, trans="fade")
    pause.5

    call her_main(".............","upset","closed", ypos="head")
    call her_main("!!!!!!!!!!!!!!!","angry","wide")
    m "Relax, [hermione_name]. I'm Just gonna take off your panties."
    call her_main("..............","angry","angry")
    m "Are you ready?"
    call her_main("No...","annoyed","annoyed")
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
        call her_main("","normal","worriedCl", ypos="head")
        show screen ccg

    call hg_chibi_transition(action="sex", trans="d5")
    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide")
    hide screen bld1
    call ctc

    call play_music("playful_tension") # SEX THEME.

    g4 "Your pussy... It's so tight."
    call her_main("................","normal","worriedCl")
    m "You alright?"
    call her_main("A-ha... It's too big...","angry","base", tears="soft")
    call her_main("You will rip me apart, [genie_name]!")
    m "Nonsense! My cock is of a regular size."
    m "It's not my fault that you are so tiny."
    call her_main("......................","normal","worriedCl")

    menu:
        "\"You should be ashamed of yourself!\"":
            #$ ccg2 = 20
            call her_main("I am not ashamed, [genie_name]!","normal","worriedCl")
            call her_main("I am doing this for the sake my house!")
            call her_main("To help my--")
            call her_main("ah-ha-a...","open","worriedCl")
            call her_main("My classmates depend on me... ah-a...")
            m "Are you sure that's the only reason?"
            call her_main("I don't know--","normal","worriedCl")
            call her_main("ah-a...","open","worriedCl")
            call her_main("I don't know what you mean, [genie_name].","angry","down_raised")
            m "It seems to me that you are enjoying this a little bit too much."
            #$ ccg2 = 21
            call her_main("I'm not, [genie_name]!","angry","down_raised")
            m "Really?"
            call her_main("......................","normal","worriedCl")
            m "Then why is your pussy so wet?"
            call her_main("....................a-ha.{image=textheart}","open","worriedCl")
            m "Admit it, you enjoy getting fucked by your [genie_name]!"
            #$ ccg2 = 25
            call her_main("I do not!","normal","worriedCl")
            m "Stubborn girl..."
            call her_main("Aha...{image=textheart}","open","worriedCl")

        "\"So... What's new in your life?\"":
            #$ ccg2 = 14
            call her_main("...[genie_name]?","open","base")
            m "Just trying to have a polite conversation."
            #$ ccg2 = 17
            call her_main("Ah-ah... But... ah...","open","base")
            m "Any news from your folks?"
            call her_main("My parents?","angry","worriedCl", emote="05")
            call her_main("[genie_name], please, I cannot talk...","open","worriedCl")
            m "Why not? Enjoying this too much?"
            call her_main("I am not... ah...{image=textheart}","open","worriedCl")
            m "I think you are."
            call her_main("I am only doing this for the points, [genie_name]...","open","worriedCl")
            m "Oh, I see..."
            m "So you are like a prostitute then."
            call her_main("What?","angry","base")
            m "Well I pay you to have sex with me. How would you call that?"
            call her_main("...........","angry","down_raised")
            #$ ccg2 = 19
            call her_main("I am not a prostitute...","open","worriedCl")
            call her_main("Why are you being so mean to me, [genie_name]?","angry","base", tears="soft")
            m "I think you like it when I'm mean."
            call her_main("I do not!","mad","worried", tears="soft")
            m "Really? Then why is your pussy so wet?"
            call her_main("Not because of that!","angry","down_raised")
            m "If you say so..."
            #$ ccg2 = 20
            call her_main("A-ah...{image=textheart}","open","worriedCl")
            call her_main("I am... ah...{image=textheart} not a prostitute...","shock","worriedCl")

        "\"......................................................\"":
            #$ ccg2 = 14
            call her_main("A-ha... ah...","open","worriedCl")
            m "*Panting!*"
            call her_main("Ah... ha-aha...","open","worriedCl")
            m "Oh..."
            call her_main("Ah-ah...","open","worriedCl")
            m "......................"
            call her_main("Ah... ah...","open","worriedCl")
            call her_main("Ah... [genie_name]?","open","base")
            m "What is it?"
            #$ ccg2 = 17
            call her_main("Ah... Do you.... like it?","open","worriedCl")
            m "Do I like drilling your super-tight pussy?"
            m "Very much so, [hermione_name]. Why?"
            call her_main(".....................","normal","worriedCl")
            call her_main("Ah... You just got so quiet...","open","worriedCl")
            m "Just enjoying the moment, [hermione_name]."
            m "What about you? You alright?"
            call her_main("Ah... yes...","open","worriedCl")
            call her_main("It hurts a little though, ah...","open","base")
            call her_main("Your penis is too big... ah...","open","worriedCl")
            m "Hm..."
            m "You need me to slow down or something?"
            #$ ccg2 = 20
            call her_main("No, [genie_name]... You don't have to...","open","base")
            call her_main("Please, don't mind me... Enjoy your moment.","normal","worriedCl")
            call her_main("I will... ah... Get used to it eventually... ah...")
            m "As you say, [hermione_name]."
            #$ ccg2 = 21
            call her_main("Ah-a...{image=textheart}","open","worriedCl")
            m "Yes, this is great!"

    call her_main("Ah-ah...{image=textheart}","open","worriedCl", ypos="head")

    if daytime:
        m "Going to classes after this?"
    else:
        m "Going to bed after this?"

    #$ ccg2 = 22
    call her_main("Yes, ah...{image=textheart}","open","worriedCl")
    call her_main("If I'll be able to walk...")
    g4 "Ght! {image=textheart} Yes, you always say the right things, [hermione_name]!"
    call her_main("Ah...{image=textheart} ah...{image=textheart}{image=textheart}","shock","worriedCl")
    #$ ccg2 = 24
    call her_main("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}","scream","wide", trans="hpunch")
    m "Huh? You alright?"
    call nar(">Hermione's legs are shaking...")
    m "[hermione_name]?"
    #$ ccg2 = 28
    call her_main("{image=textheart}{image=textheart}{image=textheart}I think I'm cumming, [genie_name]!{image=textheart}{image=textheart}{image=textheart}","scream","wide")
    g9 "Tch... You nasty slut!"
    #$ ccg2 = 29
    call her_main("AAH! I can't hold it!","silly","dead")
    g4 "You need to be punished for being such a slut!"
    call nar(">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!")

    call hg_chibi_transition(action="sex_fast", trans="d5")

    #$ ccg2 = 30
    call her_main("NO! STOP! PLEASE!","scream","wide", trans="hpunch")
    g4 "Who told you you could cum, slut? This is your punishment!"
    call her_main("[genie_name], no, ah-a!{image=textheart}","open","worriedCl")
    #$ ccg2 = 31
    call her_main("Ah-a...{image=textheart}I will go insane!{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
    g4 "{size=+7}Grragh!{/size}"
    hide screen bld1
    with d1
    call ctc

    #$ ccg2 = 32
    call her_main("No...{image=textheart} ah...{image=textheart}","silly","ahegao")
    #$ ccg2 = 33
    call her_main("I think I will...{image=textheart} pass out...{image=textheart}", ypos="head")
    g4 "ARGH! YOU WHORE!"

    menu:
        "-Cum all over Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            call hg_chibi_transition(action="sex_cumming_out", trans="d5")

            $ ccg3 = "s3"
            call cum_block
            call ctc

            #$ ccg2 = 42
            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
            hide screen bld1
            call ctc

            call hg_chibi_transition(action="sex_cumming_out_blink", trans="d5")

            m "Well, that was rather intense..."
            #$ ccg2 = 28
            call her_main("*heavy panting*","open_wide_tongue","ahegao")
            m "You alright?"
            call her_main("Ah... yes...","silly","dead")
            #$ ccg2 = 29
            call her_main("My legs are still shaking...")
            hide screen bld1
            with d1
            call ctc

            hide screen ccg
            $ hermione_flip = 1 #Default
            $ face_on_cg = False
            call hg_chibi_transition(action="sex_creampie_pause", trans="d5")

            if daytime:
                call her_main("But I think I will be able to make it to my classes...","silly","dead", ypos="head")
            else:
                call her_main("But I think I will be able to make it to the common room...","silly","dead", ypos="head")

            m "Good."
            m "Did you enjoy getting fucked by your [genie_name]?"
            call her_main("[genie_name], I am only doing this for my house.","grin","ahegao")
            m "Seriously? Still?"
            call her_main("Could I just get paid now... please?","open","worriedCl")

            return

        "-Cum inside Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            call hg_chibi_transition(action="sex_creampie", trans="d5")

            $ ccg3 = "s1"
            call cum_block
            call ctc

            #$ ccg2 = 41
            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
            hide screen bld1
            with d1
            call ctc

            call hg_chibi_transition(action="sex_creampie_pause", trans="d5")

            #$ ccg2 = 40
            call her_main("You came inside of me...","silly","dead")
            g9 "I sure did."
            hide screen bld1
            with d1
            call ctc

            hide screen ccg
            $ face_on_cg = False
            call hg_chibi_transition(action="sex_cumming_out_blink", trans="d5")

            call her_main("But...","silly","dead", ypos="head",flip=False)
            m "What?"
            call her_main("What if I get pregnant?","shock","worriedCl")
            m "Nah, you will be alright..."
            call her_main("How do you know, [genie_name]?","shock","worriedCl")
            m "We witchers are infertile."
            call her_main("Witchers?","open","worriedCl")
            m "Sure... You are a witch, that make me a witcher, right?"
            m "And everyone knows that witchers are infertile..."
            call her_main("[genie_name], you make no sense...","angry","base")
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
        call her_main("","open","worriedCl", ypos="head")
        show screen ccg

    call hg_chibi_transition(action="sex", trans="fade")
    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide", ypos="head")
    hide screen bld1
    call ctc

    call play_music("playful_tension") # SEX THEME.

    call her_main("Ah...{image=textheart}","open","worriedCl")
    m "Your pussy feels a bit looser today..."
    #$ ccg2 = 4
    call her_main("Does it...{image=textheart} ah...?{image=textheart}","open","worriedCl")
    #$ ccg2 = 5
    call her_main("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl")
    #$ ccg2 = 6
    call her_main("You are ruining my little pussy with your monstrous penis...{image=textheart}","silly","ahegao")
    g4 "Agh, you whore!"
    #$ ccg2 = 10
    call her_main("Ah...{image=textheart}{image=textheart}","silly","ahegao")
    m "Yes! Do you like it when I fuck you like this?"
    call her_main("Yes, [genie_name]...","base","glance", ypos="head")

    menu:
        g4 "..."
        "\"Be sweet but passionate.\"":
            m "Yes, you're liking this?"
            #$ ccg2 = 14
            call her_main("I do, [genie_name]... ah...{image=textheart}","open","closed")
            m "Good girl!"
            m "Just relax and take my cock!"
            call her_main("Yes... ah...{image=textheart}","open","closed")
            m "All the way in... all the way..."
            call her_main("Ah...{image=textheart}{image=textheart}","open","worriedCl")
            m "Yes, my little princess..."
            #$ ccg2 = 15
            call her_main("What?","angry","wide")
            call her_main("No, please don't call me that... ah...{image=textheart}","angry","down_raised")
            call her_main("My daddy used to call me his little princess when I was little...")
            m "Well, right now I am your daddy!"
            #$ ccg2 = 16
            call her_main("Ah...{image=textheart} ah-ah...{image=textheart}{image=textheart}","soft","ahegao")
            m "And you are my little princess-slut!"
            #$ ccg2 = 17
            call her_main("Ah...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","grin","dead")

        "\"Be mean to her!\"":
            m "Yes, you slut!"
            m "I bet you love every second of this!"
            call nar(">You pick up the pace.")
            #$ ccg2 = 17
            call her_main("Ah...{image=textheart} [genie_name]...","open","worriedCl")
            m "You nasty slut!"
            call her_main("Ah...{image=textheart} ah-a...{image=textheart}","shock","worriedCl")
            m "You are a disgrace, [hermione_name]!"
            #$ ccg2 = 18
            call her_main("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
            m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
            #$ ccg2 = 19
            call her_main("Ah-a...{image=textheart} But I am only doing this--","shock","worriedCl")
            m "Nobody cares why you are doing this, cocksucker!"
            m "Look at what you've become!"
            m "Butt-naked, on your professor's old cock, like a cheap whore!"
            #$ ccg2 = 20
            call her_main("Ah...{image=textheart} No...{image=textheart} stop saying...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
            call nar(">You pick up the pace some more.","start")

            call hg_chibi_transition(action="sex_fast", trans="d5")

            call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...","end")
            m "You let me molest you... You suck my cock..."
            m "What are you after that I ask you!?"
            #$ ccg2 = 21
            call her_main("................","grin","dead")
            call her_main("Ah...{image=textheart} ah....{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
            call her_main(".......................","angry","down_raised")
            call her_main("{size=-5}I am a whore...{/size}")
            m "Yes! That's exactly what you are!"

    #$ ccg2 = 22
    call her_main("Ah... ah... ah...","angry","down_raised", ypos="head")
    call her_main("[genie_name], you think you could... ah...")
    m "What?"
    call her_main("Could you spank me a little... ah...?","silly","worried", cheeks="blush", tears="soft")
    g4 "Gladly!"
    call slap_her

    #$ ccg2 = 24
    call her_main("Aa-a-ah!{image=textheart}{image=textheart}{image=textheart}","shock","baseL", cheeks="blush", tears="soft")
    m "You liked that one, huh?"
    call slap_her

    #$ ccg2 = 28
    call her_main("Ah..!{image=textheart} Yes!{image=textheart}{image=textheart}{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    m "And some more!"
    call slap_her

    #$ ccg2 = 29
    call her_main("Ahh! Yes!","silly","worried", cheeks="blush", tears="soft")
    call nar(">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second...","start")
    ">You love the sensation..."
    ">You unleash another series of slaps on Hermione's ass-cheeks."
    call nar(">Every single one met with a gasp of excitement from the girl.","end")
    #$ ccg2 = 30

    call slap_her
    call slap_her
    call slap_her

    #$ ccg2 = 31
    call her_main("Aah!!!{image=textheart}{image=textheart}{image=textheart} IT HURTS!{image=textheart}{image=textheart}{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    #$ ccg2 = 32
    call her_main("It hurts...{image=textheart}{image=textheart}{image=textheart} It hurts...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
    m "Hm?"
    m "Why your legs are shaking, [hermione_name]?"
    m "Are you cumming?"
    #$ ccg2 = 33
    call her_main("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
    m "Well, I think I will follow your example then."
    call her_main("..............","silly","dead")
    call nar(">You start fucking Hermione with renewed determination!")
    #$ ccg2 = 34
    call her_main("Ah! No! I can't...{image=textheart} I...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL", cheeks="blush", tears="soft", ypos="head")
    m "Shut it whore!"
    g4 "Argh!"

    menu:
        "-Cum inside of Hermione-":
            with hpunch
            g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
            call cum_block

            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            $ ccg3 = "s1"

            call hg_chibi_transition(action="sex_creampie", trans="d5")

            call cum_block
            call ctc

            #$ ccg2 = 33
            call her_main("!!!","silly","dead")
            #$ ccg2 = 38
            call her_main("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}")
            g4 "I'm Not done yet, bitch!"
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            call cum_block
            call her_main("AH! MY BELLY!","shock","baseL", cheeks="blush", tears="soft")
            g4 "{size=+5}SLUT!{/size}"

            hide screen bld1
            with d1
            call ctc

            call hg_chibi_transition(action="sex_creampie_pause", trans="d5")

            #$ ccg2 = 40
            m "Well, this was pretty great..."
            call her_main("Ah...{image=textheart}","silly","dead")
            m "You alright there, slut? Ehm, I mean, [hermione_name]."
            call her_main("Yes... I...","silly","dead")
            #$ ccg2 = 41
            call her_main("I feel so full...","open_wide_tongue","ahegao")
            call her_main("!!!","scream","wide")
            call her_main("You came inside of me, [genie_name]!")
            m "I sure did."
            call her_main("You shouldn't have...","open","worriedCl")
            m "Didn't you enjoy it?"
            call her_main("....maybe.","grin","dead")
            #$ ccg2 = 42
            call her_main("I think I came several times...","soft","ahegao")

            $ face_on_cg = False
            hide screen ccg
            call hg_chibi_transition(action="sex_creampie_pause", trans="d5")

            call her_main("Maybe you are right, [genie_name], and I shouldn't worry so much.","angry","wink", ypos="head",flip=False)
            call her_main("Can I get my payment now?")

            return

        "-Cum all over Hermione-":
            with hpunch
            g4 "{size=+7}Argh!!!{/size}"
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            call hg_chibi_transition(action="sex_cumming_out", trans="d5")

            $ ccg3 = "s3"

            call cum_block
            call ctc

            #$ ccg2 = 30
            call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
            g4 "{size=+5}You whore! Take this!{/size}"
            call her_main("{size=+5}!!!{/size}","silly","worried", cheeks="blush", tears="soft")
            hide screen bld1
            with d1
            call ctc

            call hg_chibi_transition(action="sex_cumming_out_blink", trans="d5")

            m "Well, that was pretty great..."
            #$ ccg2 = 31
            call her_main("Ah...{image=textheart}","silly","worried", cheeks="blush", tears="soft")
            m "You alright there, slut?"
            call her_main("Yes... I...","silly","dead")
            m "Didn't you enjoy this?"
            #$ ccg2 = 29
            call her_main("....I think so...","grin","dead")
            call ctc

            $ face_on_cg = False
            hide screen ccg
            call hg_chibi_transition(action="sex_creampie_pause", trans="d5")

            call her_main("I think I came several times, [genie_name]...","soft","ahegao", ypos="head",flip=False)
            call her_main("Can I get my payment now?","angry","wink")
            $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

            return


label hg_sex_luna:
    m "[hermione_name]..."
    m "I have a favour to ask of you..."
    call her_main("Is it sex? {size=-2}Please let it be sex...{/size}","smile","baseL")
    m "You certainly seem eager."
    call her_main(".......","base","glance")
    call her_main("Well I may have made some plans...","base","down")
    her "but I can't tell you what..."
    m "well as long as you bend over my desk I don't really care..."
    call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down")
    stop music fadeout 1.0
    hide screen hermione_main
    call blkfade
    # SEX

    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide", ypos="head") #HERMIONE

    call hg_chibi_transition(action="sex", trans="fade")
    call ctc

    call play_music("playful_tension") # SEX THEME.

    call her_main("Ah...{image=textheart}","open","worriedCl")
    m "Your pussy feels drenched today..."
    call her_main("Does it...{image=textheart} ah...{image=textheart}","open","worriedCl")
    call her_main("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl")

    if daytime:
        call her_main("I've been... looking forward to this all morning...{image=textheart}","silly","ahegao")
    else:
        call her_main("I've been... looking forward to this all day...{image=textheart}","silly","ahegao")

    g4 "Agh, you whore!"
    call her_main("Ah...{image=textheart}{image=textheart}","silly","ahegao")
    m "Yes! Do you like it when I fuck you like this?"
    call her_main("Yes, [genie_name]...","base","glance")

    call play_sound("knocking")
    call nar(">You hear a knock at the door.")

    menu:
        "\"Who is it?\"":
            m "(Who would be knocking at a time like this?)"
            lun "It's Luna Lovegood sir."
            m "{size=-3}Who's that again, [hermione_name]?{/size}"
            call her_main("the crazy blonde... ah...{image=textheart}... with the nice breasts...","open","closed")
            m "Come in!"
        "-Tell them to go away.-":
            m "Go aw-!"
            call her_main("no [genie_name]... let them in...","open","worriedCl")
            m "You want to get caught?!"
            call her_main("Ah...{image=textheart} yes...{image=textheart}","shock","worriedCl")
            m "You are a such a little whore, [hermione_name]!"
            call her_main("Ah-ah...{image=textheart} let them in... please...","shock","worriedCl")
            m "You asked for it!"
            call her_main("Ah-a...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
            m "Come in!"

    call nar(">The door opens as Luna Lovegood walks in.")
    call play_sound("door") #Sound of a door opening.

    call luna_init
    call lun_walk("door","desk",2.5)

    lun "Hello Professor!"
    #Stop sex
    m "....."
    call her_main("......","shock","worriedCl")

    lun "I wanted to talk to you about the school uniform."
    m "The uniform?"
    lun "Yes, I have some ideas about some necessary changes and I'd like you to listen."
    m "{size=-3}What's going on here, [hermione_name]?{/size}"

    call her_main("I may have given her a suggestibility serum...","silly","ahegao")
    m "{size=-3}A suggestibility serum?{/size}"
    lun "Who are you talking to sir?"
    m "Oh, um.... no one, just ignore me..."
    lun "Ok then, I'll ignore you..."
    call her_main("I may have suggested that she come here...","silly","ahegao")
    call her_main("And that she be unable to see me...","silly","ahegao")
    lun "As I was saying sir, the school uniform simply cannot stay as it is."

    call nar(">You pick up the pace some more.")
    pause.2

    call hg_chibi_transition(action="sex_fast", trans="d5")
    pause.8

    call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...")
    call her_main("Ah... ah... ah...","angry","down_raised")
    m "{size=-3}So let me get this straight.{/size}"
    m "{size=-3}You drugged your class mate...{/size}"
    m "{size=-3}Just so she would come in here and watch you have sex with your headmaster.{/size}"
    call her_main("Ah... yes...{image=textheart}{image=textheart}{image=textheart}")
    lun "The girls uniform is far too conservative!"
    m "conservative?"
    lun "Indeed! Ms Granger is the only student that is dressing appropriately."
    call her_main("ah...","silly","worried", cheeks="blush", tears="soft")
    m "{size=-3}What else did you do to her?{/size}"
    call her_main("I may have told her to... ah...{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    call her_main("act like the biggest slut she knows...{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    m "{size=-3}So you then?{/size}"
    call her_main("yessss...{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    lun "Sir please, pay attention."
    m "Sorry Miss Lovesgood, go on."
    lun "Thank you. As I was saying I think you need to enact several new policies regarding the girls school uniform."
    lun "Everyone should strive to achieve the same level of perfection as Miss granger."
    call her_main("{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    lun "I've come up with several rules that will help with this and I'd like you to enforce them."
    m "alright..."
    lun "rule number one: shirts must reveal a minimum of 3 inches of cleavage."
    call her_main("{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    lun "Rule number two: No skirt over 5 inches in length my be worn."
    call her_main("{image=textheart}{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    lun "rule number three: No bras to be worn at anytime."
    call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    lun "And finally, rule number four: No panties to be worn at anytime."
    call her_main("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","worried", cheeks="blush", tears="soft")

    m "Why are your legs shaking, [hermione_name]?"
    m "Are you cumming? In front of your classmate?"
    call her_main("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
    m "Well, I think I will follow your example then."
    call her_main("..............","silly","dead")
    call nar(">You start fucking Hermione with renewed determination!")
    call her_main("Ah! No! I can't...{image=textheart} not in front of...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL", cheeks="blush", tears="soft")
    m "Shut it whore!"
    lun "Yes sir."
    g4 "Argh!"
    with hpunch
    g4 "{size=+7}Argh!!!{/size}"
    call cum_block
    g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

    call hg_chibi_transition(action="sex_cumming_out", trans="d5")
    call cum_block
    call ctc

    call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
    g4 "{size=+5}You whore! Take this!{/size}"
    call her_main("{size=+5}!!!{/size}","silly","worried", cheeks="blush", tears="soft")
    hide screen bld1
    with d1
    call ctc

    call hg_chibi_transition(action="sex_cumming_out_blink", trans="d5")

    call bld
    m "Well, that was pretty great..."
    call her_main("Ah...{image=textheart}","silly","worried", cheeks="blush", tears="soft")
    m "You alright there, slut?"
    call her_main("Yes... I...","silly","dead")
    m "Didn't you enjoy this?"
    call her_main("....I think so...","grin","dead")
    call ctc

    call blkfade
    call lun_chibi("hide") #Moving it so it won't overlap with Hermione's Chibi (stands at desk).

    call her_main("I think I came several times, [genie_name]...","soft","ahegao")
    m "Well that'll do for now. You two best head to class."
    call her_main("yes sir...","grin","dead")
    call her_main("Come on Luna let's go.","grin","dead")
    lun "Hermione! WHen did you get here?"
    lun "And what are you covered in?"
    call her_main("It doesn't matter...","soft","ahegao")
    call her_main("{size=-7}You can lick it off later...{/size}","soft","ahegao")

    return
