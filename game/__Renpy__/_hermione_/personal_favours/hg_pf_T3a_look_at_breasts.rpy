

### Hermione Show Breasts ###

label hg_pf_look_at_breasts: #LV.3 (Whoring = 6 - 8)

    call reset_menu_position

    if hg_pf_look_at_breasts_OBJ.points == 0:
        m "{size=-4}(I feel like gazing upon those titties.){/size}"
    else:
        m "{size=-4}(I feel like gazing upon those titties again.){/size}"

    if hg_pf_look_at_breasts_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    if her_whoring < 6:
        jump too_much

    hide screen hermione_main
    with d3

    $ current_payout = 25 #Used when haggling about price of th favor.

    #First time event
    if hg_pf_look_at_breasts_OBJ.points == 0 and her_whoring <= 11:
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]...","normal","base",xpos="mid",ypos="base")
        m "How much will it cost me to see your tits?"
        stop music fadeout 1.0
        call her_main("How much will it cost you to...?","open","base")
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        call her_main("[genie_name]!","scream","angryCl")
        m "Hm... I thought your house could use some extra points..."
        m "But I guess I was wrong..."
        call her_main(".........?","open","base")
        m "Please don't mind me..."
        m "All I want to do is help you..."
        call her_main(".............","annoyed","worriedL")
        call her_main("200 house points, [genie_name].","normal","worriedCl")
        m "So if I give you 200 house points, [hermione_name]..."
        m "You will shamelessly bare your melons before me?"
        call her_main("[genie_name]! No need to be so vulgar!","angry","angry")
        her "I think I'd better go..."

        menu:
            "\"Wait. 200 points are yours. Show me!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                call her_main("Really?","open","base")
                m "Well?"
                call her_main("......................................","annoyed","worriedL")
                her "You have to promise me not to touch them, [genie_name]."
                m "Sure, sure..."
                call her_main("I am only doing this for the honour of my house, [genie_name]!","scream","worriedCl")

            "\"I will give you 5 points to see your tits.\"":
                call her_main("Five?!","scream","wide_stare")
                call her_main("[genie_name], I am not going to expose myself for a meagre five points!","angry","angry",emote="01")
                m "Well, your tits sure aren't worth 200, [hermione_name]!"
                call her_main("(They aren't?)","annoyed","down")
                call her_main("Maybe one hundred then?","annoyed","angryL")

                menu:
                    "\"Fine. 100 it is! Bare them already!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "So be it... For a hundred points..."
                    "\"25 house points that's my final offer!\"":
                        $ current_payout = 25 #Used when haggling about price of th favor.
                        her "..............."
                        her "Well, so be it..."

            "\"Fine, leave. I don't care...\"":
                her "Tsk!"

                call her_walk(action="leave", speed=2.5)

                $mad = +12

                jump end_hermione_event


        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d5

        call set_her_action("lift_top")

        call play_music("playful_tension") # SEX THEME.

        call her_chibi("lift_top","mid","base")
        call ctc

        call bld
        m "Hm..."
        call her_main("{size=-5}(My breasts are completely exposed...){/size}","disgust","down_raised",cheeks="blush",ypos="head")
        m "Come closer [hermione_name], let me take a better look..."
        call her_main("............","annoyed","angryL",cheeks="blush")

        hide screen bld1
        call her_chibi("stand","mid","base")
        pause.2

        call her_walk_desk_blkfade

        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."

        hide screen genie
        show screen genie_and_tits_01
        call hide_blkfade
        call ctc

        call her_main("............","soft","baseL",cheeks="blush")
        m "Very good..."
        call her_main(".....","annoyed","angryL",cheeks="blush")

        show screen blktone
        call her_main("","annoyed","annoyed",trans="fade",xpos="mid",ypos="base")
        call ctc
        her "...................................."

    #Second event
    else:
        hide screen hermione_main
        with d3

        if her_whoring >= 6 and her_whoring <= 8:
            m "[hermione_name]?"
            call her_main("Yes, [genie_name]?","annoyed","angryL",ypos="head")
            m "I need to see your tits."
            call her_main("............","annoyed","angryL",cheeks="blush")
            call her_main("Do you promise not to touch, [genie_name]?","annoyed","angryL",cheeks="blush")
            m "Of course."
            hide screen bld1
            hide screen blktone
            hide screen hermione_main
            with d3
            pause.2

            call her_chibi("lift_top","mid","base")
            call ctc

            call bld
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."

            hide screen bld1
            call her_chibi("stand","mid","base")
            pause.2

            call her_walk_desk_blkfade

            ">Hermione slowly walks towards your desk."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            call hide_blkfade
            call ctc

            call bld
            m "Very good..."
            call play_music("playful_tension") # SEX THEME.
            call set_her_action("lift_top")

            hide screen bld1
            show screen blktone
            call her_main("","annoyed","annoyed",xpos="mid",trans="fade")
            call ctc

            her "...................................."

        elif her_whoring >= 9:
            m "I need to see your tits, [hermione_name]."
            if her_whoring >= 17:
                call her_main("Of course [genie_name]","base","ahegao_raised",cheeks="blush",ypos="head")
            else:
                call her_main("Are you only going to watch, [genie_name]?","angry","worriedCl",cheeks="blush",ypos="head")
                m "Of course..."
            hide screen hermione_main
            call hide_blktone
            pause.2

            call her_chibi("lift_top","mid","base")
            call ctc

            call bld
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."

            hide screen bld1
            call her_chibi("stand","mid","base")
            pause.2

            call her_walk_desk_blkfade

            ">Hermione slowly walks towards your desk."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            hide screen bld1
            call hide_blkfade
            call ctc

            call bld
            m "Very good..."

            call set_her_action("lift_top")
            hide screen bld1
            show screen blktone
            call her_main("","base","closed",xpos="mid",ypos="base",trans="fade")
            call ctc

            her "...................................."
            call play_music("playful_tension") # SEX THEME.

    menu:
        "\"Break your promise. Grab the tits!\"":

            #First Time Event.

            #Event Fails
            if her_whoring >= 6 and her_whoring <= 8:
                hide screen hermione_main
                call blkfade

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_main("[genie_name], what are you doing?","mad","wide",cheeks="blush",ypos="head")

                #Start Groping
                hide screen blktone
                show screen chair_left
                hide screen bld1
                show screen groping_naked_tits
                call hide_blkfade
                call ctc

                call bld
                m "Relax, [hermione_name]. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("No, [genie_name], please! You mustn't do this...","shock","worriedCl")
                m "This won't take long, just stand still."
                call her_main("[genie_name], I didn't agree to this!","angry","angry",cheeks="blush")
                with hpunch
                call her_main("You must unhand me now!!!","scream","angry",cheeks="blush",emote="01")

                call blkfade
                ">Hermione pulls away from you and covers up hastily."

                call set_her_action("none","update")
                call her_main("I think I'd better go...","angry","worriedCl",cheeks="blush",xpos="base",ypos="base")

                #End Groping
                hide screen chair_left
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call bld
                m "Go ahead, [hermione_name]. You are not getting paid if you do..."
                call her_main("But I showed you my...","angry","worriedCl",cheeks="blush")
                call her_main("And you touched me...","angry","angry",cheeks="blush")
                call her_main("And I am getting nothing?","scream","angry",cheeks="blush",emote="01")
                m "You are dismissed, [hermione_name]..."
                call her_main("Gr..................","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(Burn in hell, you wretched old-{/size}","angry","worriedCl",cheeks="blush")

                call her_walk(action="leave", speed=2.5)

                $ her_mood += 22

                jump end_hermione_event

            #Event Succeeds
            elif her_whoring >= 9 and her_whoring <= 11:
                hide screen hermione_main
                call blkfade

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_main("[genie_name], what are you doing?","mad","wide",cheeks="blush",ypos="head")

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left
                hide screen bld1
                call hide_blkfade
                show screen groping_naked_tits
                with fade
                call ctc

                call bld
                m "Relax, [hermione_name]. Just stand still!"
                call her_main("I didn't agree to this, [genie_name]...","annoyed","angryL",cheeks="blush")
                call her_main("I don't think you should...","annoyed","angryL",cheeks="blush")
                m "Don't you like it...?"
                call her_main("What?","disgust","down_raised",cheeks="blush")
                m "Don't you like it how I squeeze and pull on your breasts?"
                call her_main("...............","disgust","down_raised",cheeks="blush")
                m "Admit it, you like it a little bit..."
                call her_main("{size=-5}(So strange to see my breasts in someone else's hands...){/size}","disgust","down_raised",cheeks="blush")
                call her_main("[genie_name], I am letting you do this to me to help my house out, nothing more!","shock","worriedCl")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("Please, unhand me now!","annoyed","angryL",cheeks="blush")
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."

                call set_her_action("none","update")
                call her_main("You promised not to touch, [genie_name]...","annoyed","angryL",cheeks="blush")
                m "It was hard to resist..."

                #End Groping
                hide screen bld1
                call gen_chibi("sit_behind_desk")
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call her_main(".............","soft","baseL",cheeks="blush")
                call her_main("Can I get paid now please?","angry","worriedCl",cheeks="blush",emote="05")
                m "Sure..."

                $ her_mood += 9

            #Event Also Succeeds
            elif her_whoring >= 12:
                hide screen hermione_main
                call blkfade

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_main("[genie_name], what are you doing?","mad","wide",cheeks="blush",ypos="head")

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left
                hide screen bld1
                call hide_blkfade
                show screen groping_naked_tits
                with fade
                call ctc

                call bld
                m "Relax, [hermione_name]. Just stand still!"
                call her_main("But...","disgust","down_raised",cheeks="blush")
                call her_main("ah...{image=textheart}","shock","worriedCl")
                call her_main("I didn't agree to this...","disgust","down_raised",cheeks="blush")
                m "But you like it, don't you?"

                if her_whoring >= 17:
                    call her_main("I love it [genie_name]!{image=textheart}","open","baseL",cheeks="blush")
                else:
                    call her_main("I do not, [genie_name]!{image=textheart}","shock","worriedCl")

                call blktone
                ">You give her tits a couple of firm squeezes..."
                call hide_blktone

                if her_whoring >= 17:
                    call her_main("[genie_name], you promised not to touch...","base","baseL",cheeks="blush")
                    m "I know, I know... But it's hard to resist..."
                    call her_main(".................","base","ahegao_raised",cheeks="blush")
                else:
                    call her_main("[genie_name], you promised not to touch...","angry","worriedCl",cheeks="blush")
                    m "I know, I know... But it's hard to resist..."
                    call her_main(".................","angry","angry",cheeks="blush")

                call her_main("....................ah...{image=textheart}","base","ahegao_raised",cheeks="blush")
                call her_main("[genie_name], you need to stop now...","base","ahegao_raised",cheeks="blush")
                m "Just a bit longer..."

                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3

                call her_main("[genie_name]... please, stop this...","open","ahegao_raised",cheeks="blush")
                m "Why? Because you like it too much?"
                call her_main("No it's not that...","base","baseL",cheeks="blush")
                call her_main("I mean...","open","baseL",cheeks="blush")

                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3

                call her_main("Ah...{image=textheart} [genie_name], I really need to go...","base","ahegao_raised",cheeks="blush")
                if daytime:
                    call her_main("That's right... the classes are about to start...","open","baseL",cheeks="blush")
                else:
                    call her_main("It is getting late...","open","baseL",cheeks="blush")

                m "Well, alright..."
                call blkfade

                ">You let go of the girl's breasts..."
                ">Hermione covers up..."

                call set_her_action("none","update")
                call play_music("chipper_doodle") # HERMIONE'S THEME.

                if her_whoring >= 17:
                    call her_main("Please don't think I forgot that you broke your promise, [genie_name].","base","baseL",cheeks="blush")
                else:
                    call her_main("Please don't think I forgot that you broke your promise, [genie_name].","annoyed","angryL",cheeks="blush")

                m "Right..."

                #End Groping
                hide screen chair_left
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base")
                call hide_blkfade
                call ctc

                call bld

                if her_whoring >= 17:
                    call her_main("Thank you [genie_name].","open","baseL",cheeks="blush")
                else:
                    call her_main("Can I have my payment now?","base","ahegao_raised",cheeks="blush")
                    $ her_mood +=7


        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."

            #First time event.
            if her_whoring >= 6 and her_whoring <= 8:
                call ctc

                menu:
                    "-Nod your head in approval-":
                        ">You Look at the girl's tits for a while and then nod in approval..."
                        her "......................"
                    "-Shake your head in disapproval-":
                        $ her_mood += 3
                        ">You Look at the girl's tits for a while and then shake your head in disappointment..."
                        her ".....................?"

            #Second time event.
            elif her_whoring >= 9 and her_whoring <= 11:
                call ctc

                menu:
                    "\"A Nice set of tits you got there.\"":
                        call her_main("","annoyed","closed")
                        pause
                        her "Thank--"
                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                        call her_main("...........","annoyed","base")
                        call her_main("You are being inappropriate, [genie_name].","annoyed","annoyed")
                    "\"Hm... I've seen better.\"":
                        $ her_mood += 7
                        her "Tsk..."
                        her "Are we done then?"

            #Third time event.
            elif her_whoring >= 12:
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

        "\"Start jerking off.\"":

            #First Time Event.
            if her_whoring >= 6 and her_whoring <= 8:
                $ her_mood += 2
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                call blkfade

                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("[genie_name]?!!","angry","wide",ypos="head")
                m "Just stand still, [hermione_name]..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left
                show screen jerking_off_01
                with d1
                call hide_blkfade
                call ctc

                call bld
                call nar(">You stare at Hermione's breasts with hunger...")
                call her_main("[genie_name], what are you...?","shock","worriedCl")
                call nar(">You keep stroking your hard cock...")
                call her_main("[genie_name], no...","disgust","down_raised",cheeks="blush")
                call her_main("You must... Put it away...","disgust","down_raised",cheeks="blush")
                m "Stop whining [hermione_name]. I'm not touching you, am I?"
                call her_main("But...","angry","worriedCl",cheeks="blush")
                call her_main("But I didn't agree to this!","angry","angry",cheeks="blush")
                call her_main("I...","angry","worriedCl",cheeks="blush")
                call her_main("I think I'd better leave now!","angry","worriedCl",cheeks="blush")

                menu:
                    "\"Leave now, and you'll get no points!\"":

                        call her_main("After {size=+5}this{/size}? Are you kidding me, [genie_name]?","scream","wide",cheeks="blush")
                        call her_main("I showed you my...","scream","wide",cheeks="blush")
                        call her_main("..........","annoyed","angryL",cheeks="blush")
                        call her_main("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry",cheeks="blush")
                        call blkfade

                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, [hermione_name]!"

                        call set_her_action("none","update")
                        call her_main("I am not setting a foot into your office ever again, [genie_name]!","angry","suspicious",cheeks="blush")

                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        call her_main("You are a horrible person, [genie_name]...","angry","suspicious",cheeks="blush",tears="messy")

                        call her_walk(aciton="leave", speed=2.5)

                        $ her_mood += 30

                        jump end_hermione_event

                    "\"Alright, alright. That's enough for now.\"":
                        $ her_mood +=9

                        pass

                    "-Start jerking your cock faster-":
                        $ her_mood += 35

                        ">You start jerking your cock furiously!"
                        call her_main("No, [genie_name], stop!","scream","angry",cheeks="blush",emote="01")
                        ">You jerk it even faster!"
                        call her_main("[genie_name], think I will be leaving now...","annoyed","angryL",cheeks="blush")
                        g4 "No, wait, I'm almost there!"
                        call set_her_action("none","update")

                        call her_main("Ew! [genie_name]!","angry","suspicious",cheeks="blush")
                        call her_main("I'm leaving!","angry","suspicious",cheeks="blush")

                        call her_walk(action="leave", speed=2.5)

                        jump end_hermione_event

            #Second Event.
            elif her_whoring >= 9 and her_whoring <= 11:
                hide screen hermione_main
                call blkfade

                ">You take your cock out and start stroking it..."

                call her_main("[genie_name]?","angry","wide",ypos="head")
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left
                show screen jerking_off_01
                call hide_blkfade
                call ctc

                call her_main("[genie_name], I didn't agree to this...","shock","worriedCl")
                m "What are you complaining about, [hermione_name]?"
                m "I'm not even touching you..."
                call her_main("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl")
                call nar(">You pick up the pace...")
                m "just stand still, [hermione_name]."
                m "It will be over soon."
                call her_main("..................","shock","worriedCl")
                call her_main("(It's so big...)","disgust","down_raised",cheeks="blush")
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                call her_main("..............","disgust","down_raised",cheeks="blush")
                call her_main("well, so be it...","open","baseL",cheeks="blush")
                call her_main("You can keep touching yourself, [genie_name]...","open","baseL",cheeks="blush")
                call her_main("But you must promise me not to...","soft","baseL",cheeks="blush")
                call her_main("Not to... em...","open","baseL",cheeks="blush")
                call her_main("Not to discharge...","annoyed","angryL",cheeks="blush")
                call her_main("Not in front of me, [genie_name]...","angry","angry")
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                call her_main(".......................","angry","worriedCl",cheeks="blush")
                call nar(">You start to stroke your cock even harder...")
                g4 "Yes, I know you want this! Yes!"
                call her_main("................","angry","worriedCl",cheeks="blush")
                call blkfade

                ">You are about to cum..."

                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_main("...............","angry","worriedCl",cheeks="blush")
                        ">Hermione covers up..."
                        call set_her_action("none","update")
                    "-Just start cumming-":
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        call her_main("Proff-- ??","scream","wide",cheeks="blush")
                        call cum_block
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d1
                        $ no_blinking = True #When True - blinking animation is not displayed.
                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade
                        with d3
                        call ctc

                        call bld
                        $ sperm_on_tits = True
                        call her_main("[genie_name], no, you promised!","scream","angry",cheeks="blush",emote="01")
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3
                        call her_main("[genie_name], how could you...?","angry","suspicious",cheeks="blush")
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base")
                        call ctc
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        her "I need to clean myself up..."

                        hide screen hermione_main
                        call blkfade

                        call set_her_action("none","update")
                        $ sperm_on_tits = False

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        show screen genie

                        call hide_blkfade
                        call her_main("","angry","angry")
                        call ctc
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        her "How could you do this to me, [genie_name]?!"
                        her "You gave me your word!"
                        hide screen hermione_main
                        with d3
                        $ her_mood += 45


            #Event three.
            elif her_whoring >= 12:
                hide screen hermione_main
                call blkfade

                ">You take your cock out and start stroking it..."
                call her_main("[genie_name]?","base","ahegao_raised",cheeks="blush",ypos="head")
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left
                show screen jerking_off_01
                with d1
                call hide_blkfade
                call ctc

                if her_whoring >= 17:
                    call her_main("ah...","base","ahegao_raised",cheeks="blush")
                    call her_main("It's so big...","open","baseL",cheeks="blush")
                    call her_main("You just couldn't help yourself, could you [genie_name]?","base","baseL",cheeks="blush")
                    call her_main("..................","base","ahegao_raised",cheeks="blush")
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_main("..............","base","ahegao_raised",cheeks="blush")
                    call her_main("well, so be it...","open","baseL",cheeks="blush")
                    call her_main("But you must promise me not to...","soft","baseL",cheeks="blush")
                    call her_main("Not to... ehm...","open","baseL",cheeks="blush")
                    call her_main("Not to cum on me, [genie_name]...","base","ahegao_raised",cheeks="blush")
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_main(".......................","base","ahegao_raised",cheeks="blush")
                    call nar(">You start to stroke your cock even harder...")
                    g4 "Yes, I know you want this! Yes!"
                    call her_main("................","base","ahegao_raised",cheeks="blush")
                    # SAME AS PREVIOUS EVENT^^^

                else:
                    call her_main("[genie_name], actually I never agreed to this...","shock","worriedCl")
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching you..."
                    call her_main("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl")
                    #">You pick up the pace..."
                    m "Just stand still, [hermione_name]."
                    m "It will be over soon."
                    call her_main("..................","shock","worriedCl")
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_main("..............","disgust","down_raised",cheeks="blush")
                    call her_main("well, so be it...","open","baseL",cheeks="blush")
                    call her_main("But you must promise me not to...","soft","baseL",cheeks="blush")
                    call her_main("Not to... ehm...","open","baseL",cheeks="blush")
                    call her_main("Not to discharge...","annoyed","angryL",cheeks="blush")
                    call her_main("Not in front of me, [genie_name]...","annoyed","angryL",cheeks="blush")
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_main(".......................","disgust","down_raised",cheeks="blush")
                    call nar(">You start to stroke your cock even harder...")
                    g4 "Yes, I know you want this! Yes!"
                    call her_main("................","disgust","down_raised",cheeks="blush")
                    # SAME AS PREVIOUS EVENT^^^


                call blkfade

                menu:
                    g4 "Argh! (I'm about to cum!)"
                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_main("...............","disgust","down_raised",cheeks="blush",ypos="head")
                        call her_main("Ehm... I read that that is bad for you, [genie_name]...","disgust","down_raised",cheeks="blush")
                        m "Huh?"
                        call her_main("It is bad for your health to just hold it in like this...","shock","worriedCl")
                        call her_main("Em...","disgust","down_raised",cheeks="blush")
                        call her_main("If you want to you can--","base","baseL",cheeks="blush")
                        g4 "Argh! You whore!"
                        call her_main("???","mad","wide",cheeks="blush")

                        call cum_block

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade
                        call ctc

                        call bld
                        call her_main("[genie_name], I didn't mean that you can release your... semen on me, [genie_name]...","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3

                        call her_main("Well, what's done is done I suppose...","base","baseL",cheeks="blush")
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base")
                        call ctc

                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        call her_main("Thank you [genie_name].","base","closed")
                        call her_main("Now I need to clean myself up...","annoyed","closed")
                        call ctc

                        hide screen hermione_main
                        call blkfade

                        $ sperm_on_tits = False
                        $ aftersperm = True
                        call set_her_action("none","update")

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        show screen genie
                        call hide_blkfade

                        call her_main("","base","base")
                        call ctc
                        her "Well, this should do for now..."
                        hide screen hermione_main

                    "-Just start cumming-":
                        g4 "Argh! You whore!"
                        call her_main("???","mad","wide",cheeks="blush",ypos="head")

                        call cum_block

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        call hide_blkfade
                        call ctc

                        call bld
                        call her_main("ah...{image=textheart} It's so hot...{image=textheart}","shock","worriedCl")
                        call her_main("[genie_name], you promised...","angry","worriedCl",cheeks="blush",emote="05")
                        g4 "Oh, this is great, yes..."

                        $ no_blinking = False #When True - blinking animation is not displayed.
                        hide screen jerking_off_cum
                        with d3
                        call her_main("Well, what's done is done I suppose...","angry","worriedCl",cheeks="blush")
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base")
                        call ctc

                        her "My uniform is ruined though..."
                        m "Don't worry, I'm sure no one will notice."
                        m "You did good."
                        call her_main("Thank you [genie_name].","base","closed")
                        call her_main("Now I need to clean myself up...","annoyed","closed")
                        call ctc

                        hide screen hermione_main
                        call blkfade

                        $ sperm_on_tits = False
                        call set_her_action("none","update") #This reloads all her clothing!

                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base")
                        call hide_blkfade

                        call her_main("","base","base")
                        call ctc

                        her "Well, this should do for now..."
                        hide screen hermione_main



### End Show Breasts ###

label end_hg_show_breasts:
    call blkfade

    $ sperm_on_tits = False
    call set_her_action("none","update") #This reloads all her clothing!

    hide screen jerking_off_01
    hide screen chair_left
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    hide screen groping_01
    hide screen groping_02

    call her_chibi("stand","desk","base")
    show screen genie
    call hide_blkfade
    pause.5

    call bld
    if her_whoring < 21:
        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"

    stop music fadeout 10.0

    if her_whoring <= 16:
        call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    else:
        call her_main("..................","base","happyCl",xpos="base",ypos="base")

    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."

    if her_whoring >= 6 and her_whoring < 9:
        $ hg_pf_look_at_breasts_OBJ.level = 1 #Event hearts level (0-3)

    if her_whoring >= 9 and her_whoring < 12:
        $ hg_pf_look_at_breasts_OBJ.level = 2 #Event hearts level (0-3)

    if her_whoring >= 12:
        $ hg_pf_look_at_breasts_OBJ.level = 3 #Event hearts level (0-3)


    hide screen bld1
    hide screen hermione_main
    with d3

    #Door reaction.
    if her_whoring >= 6:

        call her_walk(xpos="door", ypos="base", speed=3)

        if her_whoring < 9:
            call her_main("(How humiliating... What have I become...?)","disgust","down_raised",cheeks="blush",ypos="head")

        elif her_whoring < 12:
            call her_main("........................","disgust","down_raised",cheeks="blush",ypos="head")

        elif her_whoring >= 17 and aftersperm:
            call her_main("{size=-5}(That was so exhilarating...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
            call her_main("{size=-5}(I wonder if anyone will notice my uniform!){/size}","open","ahegao_raised",cheeks="blush",ypos="head")
            call her_main("{size=-5}(What will people think of me?){/size}","open","ahegao_raised",cheeks="blush",ypos="head")
            call her_main(".................................","base","ahegao_raised",cheeks="blush",ypos="head")

        else:
            call her_main("{size=-5}(That was so humiliating...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
            call her_main("{size=-5}(No, Hermione, you silly girl!){/size}","angry","angry",cheeks="blush",ypos="head")
            call her_main("{size=-5}(We are doing this to protect the honour of our house!){/size}","angry","angry",cheeks="blush",ypos="head")
            call her_main(".................................","base","ahegao_raised",cheeks="blush",ypos="head")

    call her_chibi(action="leave")

    if her_whoring < 9: #Adds points till 9.
        $ her_whoring +=1

    $ hg_pf_look_at_breasts_OBJ.points += 1

    jump end_hermione_event
