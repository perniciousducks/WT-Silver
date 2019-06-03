

label hg_pf_admire_breasts_transition:
    stop music fadeout 1.0
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3
    pause.2

    # Setup Pose
    $ hermione_wear_bra = False
    call set_her_action("lift_top")

    call her_chibi("lift_top","mid","base")
    call ctc


    call bld
    if her_tier <= 2:
        m "Hm..."
        call her_main("{size=-5}(My breasts are completely exposed...){/size}","disgust","down_raised", cheeks="blush", ypos="head")
        m "Come closer [hermione_name], let me take a better look..."
    else:
        m "Hm..."
        m "Come closer [hermione_name], let me take a better look..."


    # Move to desk
    hide screen bld1
    call her_chibi("stand","mid","base")
    pause.2

    call her_walk_desk_blkfade

    ">Hermione slowly walks towards your desk."

    call hg_chibi_transition("admire_breasts")
    call ctc

    if her_tier <= 2:
        call her_main("............","annoyed","angryL", cheeks="blush", xpos="mid", ypos="base")
        m "Very good..."
        call her_main(".....","annoyed","angry", cheeks="blush")
        call ctc

        show screen blktone
        call her_main("....................................","annoyed","annoyed")

    elif her_tier == 3:
        call her_main("","base","closed", xpos="mid", ypos="base")
        call ctc

        m "Very good..."
        call play_music("playful_tension") # SEX THEME.
        her "...................................."
        call ctc

    else:
        call her_main("","base","glance", cheeks="blush", xpos="mid", ypos="base")
        call ctc

        m "Very good..."
        call play_music("playful_tension") # SEX THEME.
        call her_main("............","base","glance", cheeks="blush")
        call ctc

    return













### Tier 2 ###

label hg_pf_admire_breasts_T2:

    call hg_pf_admire_breasts_transition

    menu:
        "\"Break your promise. Grab the tits!\"":     # Event will fail.
            jump hg_pf_admire_breasts_T2_touch

        "\"Keep promise. Admire visually.\"":
            call hg_pf_admire_breasts_T2_promise

            jump end_hg_pf_admire_breasts

        "\"Start jerking off.\"":                      # 2/3 branches will fail.
            jump hg_pf_admire_breasts_T2_masturbate



label hg_pf_admire_breasts_T2_promise: # Call label

    ">You take a long look at Hermione's naked tits..."

    #First time event.
    #if her_whoring >= 6 and her_whoring <= 8:
    call ctc

    menu:
        "-Nod your head in approval-":
            ">You Look at the girl's tits for a while and then nod in approval..."
            her "......................"

            return

        "-Shake your head in disapproval-":
            $ her_mood += 3
            ">You Look at the girl's tits for a while and then shake your head in disappointment..."
            her ".....................?"

            return



label hg_pf_admire_breasts_T2_touch: # Not a Call label

    #Event Fails
    # if her_whoring >= 6 and her_whoring <= 8:
    hide screen hermione_main
    call blkfade

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?","mad","wide", cheeks="blush", ypos="head")

    # Start Groping
    call hg_chibi_transition("grope_breasts")
    call ctc

    call bld
    m "Relax, [hermione_name]. Just stand still!"
    m "Oh... Those are some nice titties you've got..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("No, [genie_name], please! You mustn't do this...","shock","worriedCl")
    m "This won't take long, just stand still."
    call her_main("[genie_name], I didn't agree to this!","angry","angry", cheeks="blush")
    with hpunch
    call her_main("You must unhand me now!!!","scream","angry", cheeks="blush",emote="01")

    # End Groping
    call blkfade

    ">Hermione pulls away from you and covers up hastily."

    call set_her_action("none","update")

    call hg_chibi_transition(xpos="desk", ypos="base")

    call her_main("I think I'd better go...","angry","worriedCl", cheeks="blush", xpos="mid", ypos="base")
    m "Go ahead, [hermione_name]. You are not getting paid if you do..."
    call her_main("But I showed you my...","angry","worriedCl", cheeks="blush")
    call her_main("And you touched me...","angry","angry", cheeks="blush")
    call her_main("And I am getting nothing?","scream","angry", cheeks="blush",emote="01")
    m "You are dismissed, [hermione_name]..."
    call her_main("Gr..................","angry","worriedCl", cheeks="blush")
    call her_main("{size=-5}(Burn in hell, you wretched old-{/size}","angry","worriedCl", cheeks="blush")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 22

    jump end_hermione_event



label hg_pf_admire_breasts_T2_masturbate: # Not a Call label

    #First Time Event.
    # if her_whoring >= 6 and her_whoring <= 8:
    $ her_mood += 2
    hide screen hermione_main
    with d3

    ">You take your cock out and start stroking it..."
    call blkfade

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]?!!","angry","wide", ypos="head")
    m "Just stand still, [hermione_name]..."

    # Start Jerking Off.
    hide screen bld1
    hide screen blktone
    call hg_chibi_transition("jerk_off", trans="fade")
    call ctc

    call bld
    call nar(">You stare at Hermione's breasts with hunger...")
    call her_main("[genie_name], what are you...?","shock","worriedCl")
    call nar(">You keep stroking your hard cock...")
    call her_main("[genie_name], no...","disgust","down_raised", cheeks="blush")
    call her_main("You must... Put it away...","disgust","down_raised", cheeks="blush")
    m "Stop whining [hermione_name]. I'm not touching you, am I?"
    call her_main("But...","angry","worriedCl", cheeks="blush")
    call her_main("But I didn't agree to this!","angry","angry", cheeks="blush")
    call her_main("I...","angry","worriedCl", cheeks="blush")
    call her_main("I think I'd better leave now!","angry","worriedCl", cheeks="blush")

    menu:
        "\"Leave now, and you'll get no points!\"":
            $ her_mood += 30

            call her_main("After {size=+5}this{/size}? Are you kidding me, [genie_name]?","scream","wide", cheeks="blush")
            call her_main("I showed you my...","scream","wide", cheeks="blush")
            call her_main("..........","annoyed","angryL", cheeks="blush")
            call her_main("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry", cheeks="blush")
            call blkfade

            ">Hermione pulls away from you and covers up..."
            g4 "Don't you dare to leave me in this state, [hermione_name]!"

            call set_her_action("none","update")
            call hg_chibi_transition("stand","desk","base", flip=False, trans="fade")

            call her_main("I am not setting a foot into your office ever again, [genie_name]!","angry","suspicious", cheeks="blush", xpos="mid", ypos="base")

            g4 "Come on, now. Just say something dirty! I'm almost there!"
            call her_main("You are a horrible person, [genie_name]...","angry","suspicious", cheeks="blush", tears="messy")

            call her_walk(action="leave", speed=2)

            jump end_hermione_event

        "\"Alright, alright. That's enough for now.\"":
            $ her_mood += 9

            jump end_hg_pf_admire_breasts

        "-Start jerking your cock faster-":
            $ her_mood += 35

            ">You start jerking your cock furiously!"
            call her_main("No, [genie_name], stop!","scream","angry", cheeks="blush",emote="01")
            ">You jerk it even faster!"
            call her_main("[genie_name], think I will be leaving now...","annoyed","angryL", cheeks="blush")
            g4 "No, wait, I'm almost there!"
            call set_her_action("none","update")

            call her_main("Ew! [genie_name]!","angry","suspicious", cheeks="blush")

            call hg_chibi_transition("stand","desk","base", flip=False, trans="fade")

            call her_main("I'm leaving!","angry","suspicious", cheeks="blush")

            call her_walk(action="leave", speed=2)

            jump end_hermione_event











label hg_pf_admire_breasts_T3:

    call hg_pf_admire_breasts_transition

    menu:
        "\"Break your promise. Grab the tits!\"":
            call hg_pf_admire_breasts_T3_touch

        "\"Keep promise. Admire visually.\"":
            call hg_pf_admire_breasts_T3_promise

        "\"Start jerking off.\"":
            call hg_pf_admire_breasts_T3_masturbate


    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T3_promise:
    ">You take a long look at Hermione's naked tits..."
    # elif her_whoring >= 9 and her_whoring <= 11:
    call ctc

    menu:
        "\"A Nice set of tits you got there.\"":
            call her_main("","annoyed","closed")
            call ctc

            her "Thank-"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("...........","annoyed","base")
            call her_main("You are being inappropriate, [genie_name].","annoyed","annoyed")

            return

        "\"Hm... I've seen better.\"":
            $ her_mood += 7

            her "Tsk..."
            her "Are we done then?"

            return


label hg_pf_admire_breasts_T3_touch:
    # elif her_whoring >= 9 and her_whoring <= 11:
    hide screen hermione_main
    call blkfade

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?","mad","wide", cheeks="blush", ypos="head")

    # Start Groping
    call hg_chibi_transition("grope_breasts")
    call ctc

    call bld
    m "Relax, [hermione_name]. Just stand still!"
    call her_main("I didn't agree to this, [genie_name]...","annoyed","angryL", cheeks="blush")
    call her_main("I don't think you should...","annoyed","angryL", cheeks="blush")
    m "Don't you like it...?"
    call her_main("What?","disgust","down_raised", cheeks="blush")
    m "Don't you like it how I squeeze and pull on your breasts?"
    call her_main("...............","disgust","down_raised", cheeks="blush")
    m "Admit it, you like it a little bit..."
    call her_main("{size=-5}(So strange to see my breasts in someone else's hands...){/size}","disgust","down_raised", cheeks="blush")
    call her_main("[genie_name], I am letting you do this to me to help my house out, nothing more!","shock","worriedCl")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Please, unhand me now!","annoyed","angryL", cheeks="blush")
    show screen blkfade
    with d5

    ">Hermione pulls away from you suddenly and covers up."

    call set_her_action("none","update")
    call her_main("You promised not to touch, [genie_name]...","annoyed","angryL", cheeks="blush")
    m "It was hard to resist..."

    # End Groping
    call hg_chibi_transition(xpos="desk", ypos="base")
    pause.8

    call her_main(".............","soft","baseL", cheeks="blush")
    call her_main("Can I get paid now please?","angry","worriedCl", cheeks="blush",emote="05")
    m "Sure..."

    $ her_mood += 9

    return


label hg_pf_admire_breasts_T3_masturbate:

    # elif her_whoring >= 9 and her_whoring <= 11:
    hide screen hermione_main
    call blkfade

    ">You take your cock out and start stroking it..."

    call her_main("[genie_name]?","angry","wide", ypos="head")
    ">You stare at Hermione's breasts with hunger..."

    #Start Jerking Off.
    hide screen bld1
    hide screen blktone
    call hg_chibi_transition("jerk_off", trans="fade")
    call ctc

    call her_main("[genie_name], I didn't agree to this...","shock","worriedCl")
    m "What are you complaining about, [hermione_name]?"
    m "I'm not even touching you..."
    call her_main("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl")
    call nar(">You pick up the pace...")
    m "just stand still, [hermione_name]."
    m "It will be over soon."
    call her_main("..................","shock","worriedCl")
    call her_main("(It's so big...)","disgust","down_raised", cheeks="blush")
    m "Yes... Yes, like this..."
    m "Yes, with your tits all naked..."
    call her_main("..............","disgust","down_raised", cheeks="blush")
    call her_main("well, so be it...","open","baseL", cheeks="blush")
    call her_main("You can keep touching yourself, [genie_name]...","open","baseL", cheeks="blush")
    call her_main("But you must promise me not to...","soft","baseL", cheeks="blush")
    call her_main("Not to... em...","open","baseL", cheeks="blush")
    call her_main("Not to discharge...","annoyed","angryL", cheeks="blush")
    call her_main("Not in front of me, [genie_name]...","angry","angry")
    m "Fine, whatever..."
    m "Oh, you little slut. You nasty little slut!"
    call her_main(".......................","angry","worriedCl", cheeks="blush")
    call nar(">You start to stroke your cock even harder...")
    g4 "Yes, I know you want this! Yes!"
    call her_main("................","angry","worriedCl", cheeks="blush")

    ">You are about to cum..."

    menu:
        "-Hold it as promised-":
            g4 "Oh, alright..."
            g4 "I'd better stop now I suppose..."
            call her_main("...............","angry","worriedCl", cheeks="blush")
            ">Hermione covers up..."
            call set_her_action("none","update")

            return

        "-Just start cumming-":
            #call play_music("chipper_doodle") # HERMIONE'S THEME.
            g4 "Argh! You whore!"
            call her_main("Proff- ??","scream","wide", cheeks="blush")
            call cum_block
            g4 "Argh! YES!"
            hide screen bld1
            with d1

            $ no_blinking = True #When True - blinking animation is not displayed.

            show screen jerking_off_cum
            with d5
            call ctc

            $ sperm_on_tits = True
            call her_main("[genie_name], no, you promised!","scream","angry", cheeks="blush",emote="01")
            g4 "Oh, this is great, yes..."
            $ no_blinking = False #When True - blinking animation is not displayed.
            hide screen jerking_off_cum
            with d3

            call her_main("[genie_name], how could you...?","angry","suspicious", cheeks="blush")
            m "Oh, this was quite amazing..."
            show screen blktone8
            with d3
            call her_main("","disgust","down_raised", xpos="mid", ypos="base")
            call ctc

            her "My uniform..."
            her "It's ruined...."
            m "Don't worry, I will give you your house points, [hermione_name]."
            m "You did good."
            hide screen blktone8
            with d3

            her "................"
            her "I need to clean myself up..."

            hide screen hermione_main
            show screen blkfade
            with d5

            call set_her_action("none","update")
            $ sperm_on_tits = False

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")

            hide screen blkfade
            with d5
            call her_main("","angry","angry")
            call ctc

            her "How could you do this to me, [genie_name]?!"
            her "You gave me your word!"
            hide screen hermione_main
            with d3

            $ her_mood += 45

            return



### Tier 4 ###

label hg_pf_admire_breasts_T4:

    call hg_pf_admire_breasts_transition

    menu:
        "\"Break your promise. Grab the tits!\"":
            call hg_pf_admire_breasts_T4_touch

        "\"Keep promise. Admire visually.\"":
            call hg_pf_admire_breasts_T4_promise

        "\"Start jerking off.\"":
            call hg_pf_admire_breasts_T4_masturbate

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T4_promise: # Call label
    ">You take a long look at Hermione's naked tits..."
    # elif her_whoring >= 12:

    call ctc

    menu:
        "\"You have great tits, [hermione_name].\"":
            call her_main("You really think so [genie_name]?","annoyed","base")
            call her_main("I am glad you like them, [genie_name]...","base","closed")
        "\"Your tits are alright I suppose...\"":
            call her_main("Huh?","annoyed","base")
            her "Does this mean you don't like them, [genie_name]?"
            call her_main("I'm sorry...","disgust","down_raised")

    call blktone
    ">You stare at her breasts for a while longer..."
    call hide_blktone
    call ctc

    m "Alright, you can cover up, [hermione_name]..."
    her "............."
    pause.2

    call set_her_action("none","update")
    pause.5

    call blkfade

    ">Hermione covers up..."

    #End Admiring
    hide screen hermione_main
    hide screen chair_left
    hide screen genie_and_tits_01
    hide screen blktone
    hide screen bld1

    return



label hg_pf_admire_breasts_T4_touch: # Call label
    # Event Also Succeeds
    # elif her_whoring >= 12:
    hide screen hermione_main
    call blkfade

    ">You reach out and dig your fingers into the girl's ample flesh..."
    call her_main("[genie_name], what are you doing?","mad","wide", cheeks="blush", ypos="head")

    # Start Groping
    call hg_chibi_transition("grope_breasts")
    call ctc

    call bld
    m "Relax, [hermione_name]. Just stand still!"
    call her_main("But...","disgust","down_raised", cheeks="blush")
    call her_main("ah...{image=textheart}","shock","worriedCl")
    call her_main("I didn't agree to this...","disgust","down_raised", cheeks="blush")
    m "But you like it, don't you?"

    if her_whoring >= 17:
        call her_main("I love it [genie_name]!{image=textheart}","open","baseL", cheeks="blush")
    else:
        call her_main("I do not, [genie_name]!{image=textheart}","shock","worriedCl")

    call blktone
    ">You give her tits a couple of firm squeezes..."
    call hide_blktone

    if her_whoring >= 17:
        call her_main("[genie_name], you promised not to touch...","base","baseL", cheeks="blush")
        m "I know, I know... But it's hard to resist..."
        call her_main(".................","base","ahegao_raised", cheeks="blush")
    else:
        call her_main("[genie_name], you promised not to touch...","angry","worriedCl", cheeks="blush")
        m "I know, I know... But it's hard to resist..."
        call her_main(".................","angry","angry", cheeks="blush")

    call her_main("....................ah...{image=textheart}","base","ahegao_raised", cheeks="blush")
    call her_main("[genie_name], you need to stop now...","base","ahegao_raised", cheeks="blush")
    m "Just a bit longer..."

    call nar(">You keep on massaging the girl's breasts...")

    call her_main("[genie_name]... please, stop this...","open","ahegao_raised", cheeks="blush")
    m "Why? Because you like it too much?"
    call her_main("No it's not that...","base","baseL", cheeks="blush")
    call her_main("I mean...","open","baseL", cheeks="blush")

    call nar(">You pull the tits in opposite directions and then squish them together...")

    call her_main("Ah...{image=textheart} [genie_name], I really need to go...","base","ahegao_raised", cheeks="blush")
    if daytime:
        call her_main("That's right... the classes are about to start...","open","baseL", cheeks="blush")
    else:
        call her_main("It is getting late...","open","baseL", cheeks="blush")

    m "Well, alright..."
    call blkfade

    ">You let go of the girl's breasts..."
    ">Hermione covers up..."

    call set_her_action("none","update")
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    if her_whoring >= 17:
        call her_main("Please don't think I forgot that you broke your promise, [genie_name].","base","baseL", cheeks="blush")
    else:
        call her_main("Please don't think I forgot that you broke your promise, [genie_name].","annoyed","angryL", cheeks="blush")

    m "Right..."

    return



label hg_pf_admire_breasts_T4_masturbate: # Call label
    # elif her_whoring >= 12:
    hide screen hermione_main
    call blkfade

    ">You take your cock out and start stroking it..."
    call her_main("[genie_name]?","base","ahegao_raised", cheeks="blush", ypos="head")
    ">You stare at Hermione's breasts with hunger..."

    # Start Jerking off.
    hide screen bld1
    hide screen blktone
    call hg_chibi_transition("jerk_off", trans="fade")
    call ctc

    if her_whoring < 17:
        call her_main("[genie_name], actually I never agreed to this...","shock","worriedCl")
        m "What are you complaining about, [hermione_name]?"
        m "I'm not even touching you..."
        call her_main("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl")
        m "Just stand still, [hermione_name]."
        m "It will be over soon."
        call her_main("..................","shock","worriedCl")
        m "Yes... Yes, like this..."
        m "Yes, with your tits all naked..."
        call her_main("..............","disgust","down_raised", cheeks="blush")
        call her_main("well, so be it...","open","baseL", cheeks="blush")
        call her_main("But you must promise me not to...","soft","baseL", cheeks="blush")
        call her_main("Not to... ehm...","open","baseL", cheeks="blush")
        call her_main("Not to discharge...","annoyed","angryL", cheeks="blush")
        call her_main("Not in front of me, [genie_name]...","annoyed","angryL", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................","disgust","down_raised", cheeks="blush")
        call nar(">You start to stroke your cock even harder...")
        g4 "Yes, I know you want this! Yes!"
        call her_main("................","disgust","down_raised", cheeks="blush")

    else: # Different posing than above.
        call her_main("ah...","base","ahegao_raised", cheeks="blush")
        call her_main("It's so big...","open","baseL", cheeks="blush")
        call her_main("You just couldn't help yourself, could you [genie_name]?","base","baseL", cheeks="blush")
        call her_main("..................","base","ahegao_raised", cheeks="blush")
        m "Yes... Yes, like this..."
        m "Yes, with your tits all naked..."
        call her_main("..............","base","ahegao_raised", cheeks="blush")
        call her_main("well, so be it...","open","baseL", cheeks="blush")
        call her_main("But you must promise me not to...","soft","baseL", cheeks="blush")
        call her_main("Not to... ehm...","open","baseL", cheeks="blush")
        call her_main("Not to cum on me, [genie_name]...","base","ahegao_raised", cheeks="blush")
        m "Fine, whatever..."
        m "Oh, you little slut. You nasty little slut!"
        call her_main(".......................","base","ahegao_raised", cheeks="blush")
        call nar(">You start to stroke your cock even harder...")
        g4 "Yes, I know you want this! Yes!"
        call her_main("................","base","ahegao_raised", cheeks="blush")


    # Genie cums.
    menu:
        g4 "Argh! (I'm about to cum!)"
        "-Hold it in-":
            g4 "Oh, alright..."
            g4 "I'd better stop now I suppose..."
            call her_main("...............","disgust","down_raised", cheeks="blush", ypos="head")
            call her_main("Ehm... I read that that is bad for you, [genie_name]...","disgust","down_raised", cheeks="blush")
            m "Huh?"
            call her_main("It is bad for your health to just hold it in like this...","shock","worriedCl")
            call her_main("Em...","disgust","down_raised", cheeks="blush")
            call her_main("If you want to you can--","base","baseL", cheeks="blush")
            g4 "Argh! You whore!"
            call her_main("???","mad","wide", cheeks="blush")

            call cum_block

            g4 "Argh! YES!"

            $ no_blinking = True #When True - blinking animation is not displayed.
            $ sperm_on_tits = True

            show screen jerking_off_cum
            with d5
            call ctc

            call bld
            call her_main("[genie_name], I didn't mean that you can release your... semen on me, [genie_name]...","angry","worriedCl", cheeks="blush",emote="05")
            g4 "Oh, this is great, yes..."
            $ no_blinking = False #When True - blinking animation is not displayed.
            hide screen jerking_off_cum
            with d5

            call her_main("Well, what's done is done I suppose...","base","baseL", cheeks="blush")
            m "Oh, this was quite amazing..."
            show screen blktone8
            with d3
            call her_main("","disgust","down_raised", xpos="mid", ypos="base")
            call ctc

            her "My uniform is ruined though..."
            m "Don't worry, I will give you your house points, [hermione_name]."
            m "You did good."

            hide screen blktone8
            call her_main("Thank you [genie_name].","base","closed")
            call her_main("Now I need to clean myself up...","annoyed","closed")
            call ctc

            hide screen hermione_main
            show screen blkfade
            with d5

            $ sperm_on_tits = False
            $ aftersperm = True
            call set_her_action("none","update")

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen blkfade
            with d5

            call her_main("","base","base")
            call ctc
            her "Well, this should do for now..."
            hide screen hermione_main

            return

        "-Just start cumming-":
            g4 "Argh! You whore!"
            call her_main("???","mad","wide", cheeks="blush", ypos="head")

            call cum_block

            g4 "Argh! YES!"

            $ no_blinking = True #When True - blinking animation is not displayed.
            $ sperm_on_tits = True

            show screen jerking_off_cum
            call hide_blkfade
            call ctc

            call her_main("ah...{image=textheart} It's so hot...{image=textheart}","shock","worriedCl")
            call her_main("[genie_name], you promised...","angry","worriedCl", cheeks="blush",emote="05")
            g4 "Oh, this is great, yes..."

            $ no_blinking = False #When True - blinking animation is not displayed.
            hide screen jerking_off_cum
            with d3

            call her_main("Well, what's done is done I suppose...","angry","worriedCl", cheeks="blush")
            m "Oh, this was quite amazing..."

            show screen blktone8
            call her_main("","disgust","down_raised", xpos="mid", ypos="base")
            call ctc

            her "My uniform is ruined though..."
            m "Don't worry, I'm sure no one will notice."
            m "You did good."

            hide screen blktone8
            call her_main("Thank you [genie_name].","base","closed")
            call her_main("Now I need to clean myself up...","annoyed","closed")
            call ctc

            hide screen hermione_main
            call blkfade

            $ sperm_on_tits = False
            call set_her_action("none","update") #This reloads all her clothing!

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen blkfade
            with d5

            call her_main("","base","base")
            call ctc

            her "Well, this should do for now..."
            hide screen hermione_main

            return
