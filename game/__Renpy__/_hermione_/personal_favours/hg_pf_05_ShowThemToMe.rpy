

### HERMIONE PERSONAL FAVOUR 5 ###

### LOOK AT HER TITS! ###

label hg_pf_ShowThemToMe: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_ShowThemToMe_OBJ.points == 0:
        m "{size=-4}(I feel like gazing upon those titties.){/size}"
    else:
        m "{size=-4}(I feel like gazing upon those titties again.){/size}"

    if hg_pf_ShowThemToMe_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
            
    if whoring < 6:
        jump too_much
        
    if hg_gryffCheer_OBJ.purchased or hg_slythCheer_OBJ.purchased or hg_powerGirl_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                if whoring < 15:
                    jump too_much
                call her_main("As what?","open","worriedL") 
                menu:
                    "-A Cheerleader-" if hg_gryffCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_gryffCheer_OBJ) 
                        pass
                    "-A Slytherin Cheerleader-" if hg_slythCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_slythCheer_OBJ) 
                        pass
                    "-Power girl-" if hg_powerGirl_OBJ.purchased:
                        call her_main("In that ridiculous costume?","scream","angryCl") 
                        m "It's not that bad. It has a nice cape."
                        call her_main("...","angry","worriedCl",emote="05") 
                        call her_main("Fine, let me go change.","normal","worriedCl") 
                        call play_sound("door") #Sound of a door opening.
                        call set_hermione_outfit(hg_powerGirl_OBJ) 
                        pass
                call her_main("","","",xpos="mid") 
                call ctc 
                m "very good"
            "\"(Not right now.)\"":
                pass       
    
    hide screen hermione_main
    with d3
    
    $ current_payout = 25 #Used when haggling about price of th favor.
    
    #First time event
    if hg_pf_ShowThemToMe_OBJ.points == 0 and whoring <= 11:
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
                $mad = +12
                her "Tsk!"
                call music_block 
                jump could_not_flirt
                
                
        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d5

        call h_action("lift_top") 

        call play_music("playful_tension") # SEX THEME.

        call her_chibi("lift_top","mid","base") 
        call ctc 

        call bld 
        m "Hm..."
        call her_head("{size=-5}(My breasts are completely exposed...){/size}","disgust","down_raised",cheeks="blush") 
        m "Come closer [hermione_name], let me take a better look..."
        call her_head("............","annoyed","angryL",cheeks="blush") 

        call her_chibi("stand","mid","base") 
        pause.2

        call her_walk_desk_blkfade 

        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."
       
        hide screen genie
        show screen genie_and_tits_01
        call hide_blkfade 
        call ctc 

        call bld 
        call her_head("............","soft","baseL",cheeks="blush") 
        m "Very good..."
        call her_head(".....","annoyed","angryL",cheeks="blush") 
        
        hide screen bld1
        show screen blktone
        call her_main("","annoyed","annoyed",trans="fade",xpos="mid",ypos="base") 
        call ctc 
        her "...................................."
    
    #Second event
    else:
        hide screen hermione_main
        with d3

        if whoring >= 6 and whoring <= 8:
            m "[hermione_name]?"
            call her_head("Yes, [genie_name]?","annoyed","angryL") 
            m "I need to see your tits."
            call her_head("............","annoyed","angryL",cheeks="blush") 
            call her_head("Do you promise not to touch, [genie_name]?","annoyed","angryL",cheeks="blush") 
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
            call h_action("lift_top") 
            
            hide screen bld1
            show screen blktone
            call her_main("","annoyed","annoyed",xpos="mid",trans="fade") 
            call ctc 
            
            her "...................................."

        elif whoring >= 9:
            m "I need to see your tits, [hermione_name]."
            if whoring >= 17:
                call her_head("Of course [genie_name]","base","ahegao_raised",cheeks="blush") 
            else:
                call her_head("Are you only going to watch, [genie_name]?","angry","worriedCl",cheeks="blush") 
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
            
            call h_action("lift_top") 
            hide screen bld1
            show screen blktone
            call her_main("","base","closed",xpos="mid",trans="fade") 
            call ctc 

            her "...................................."
            call play_music("playful_tension") # SEX THEME.

    menu:
        "\"Break your promise. Grab the tits!\"":

            #First Time Event.

            #Event Fails
            if whoring >= 6 and whoring <= 8:
                hide screen hermione_main 
                call blkfade 
                
                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") 

                #Start Groping
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                call hide_blkfade 
                call ctc 

                call bld 
                m "Relax, [hermione_name]. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("No, [genie_name], please! You mustn't do this...","shock","worriedCl") 
                m "This won't take long, just stand still."
                call her_head("[genie_name], I didn't agree to this!","angry","angry",cheeks="blush") 
                with hpunch
                call her_head("You must unhand me now!!!","scream","angry",cheeks="blush",emote="01") 

                call blkfade 
                ">Hermione pulls away from you and covers up hastily."
                call h_action("none") 
                call her_head("I think I'd better go...","angry","worriedCl",cheeks="blush",xpos="base",ypos="base") 

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") 
                call hide_blkfade 
                call ctc 

                call bld 
                m "Go ahead, [hermione_name]. You are not getting paid if you do..."
                call her_head("But I showed you my...","angry","worriedCl",cheeks="blush") 
                call her_head("And you touched me...","angry","angry",cheeks="blush") 
                call her_head("And I am getting nothing?","scream","angry",cheeks="blush",emote="01") 
                m "You are dismissed, [hermione_name]..."
                call her_head("Gr..................","angry","worriedCl",cheeks="blush") 
                call her_head("{size=-5}(Burn in hell, you wretched old---{/size}","angry","worriedCl",cheeks="blush") 
                $ mad += 22
                call music_block 
                jump could_not_flirt

            #Event Succeeds
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade 

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") 

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade 
                show screen groping_naked_tits
                with fade
                call ctc 

                call bld 
                m "Relax, [hermione_name]. Just stand still!"
                call her_head("I didn't agree to this, [genie_name]...","annoyed","angryL",cheeks="blush") 
                call her_head("I don't think you should...","annoyed","angryL",cheeks="blush") 
                m "Don't you like it...?"
                call her_head("What?","disgust","down_raised",cheeks="blush") 
                m "Don't you like it how I squeeze and pull on your breasts?"
                call her_head("...............","disgust","down_raised",cheeks="blush") 
                m "Admit it, you like it a little bit..."
                call her_head("{size=-5}(So strange to see my breasts in someone else's hands...){/size}","disgust","down_raised",cheeks="blush") 
                call her_head("[genie_name], I am letting you do this to me to help my house out, nothing more!","shock","worriedCl") 
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("Please, unhand me now!","annoyed","angryL",cheeks="blush") 
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."
                call h_action("none") 
                call her_head("You promised not to touch, [genie_name]...","annoyed","angryL",cheeks="blush",xpos="base",ypos="base") 
                m "It was hard to resist..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") 
                call hide_blkfade 
                call ctc 

                call bld 
                call her_head(".............","soft","baseL",cheeks="blush") 
                call her_head("Can I get paid now please?","angry","worriedCl",cheeks="blush",emote="05") 
                m "Sure..."
                $ mad += 9

            #Event Also Succeeds
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade 

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") 

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade 
                show screen groping_naked_tits
                with fade
                call ctc 

                call bld 
                m "Relax, [hermione_name]. Just stand still!"
                call her_head("But...","disgust","down_raised",cheeks="blush") 
                call her_head("ah...{image=textheart}","shock","worriedCl") 
                call her_head("I didn't agree to this...","disgust","down_raised",cheeks="blush") 
                m "But you like it, don't you?"

                if whoring >= 17:
                    call her_head("I love it [genie_name]!{image=textheart}","open","baseL",cheeks="blush") 
                else:
                    call her_head("I do not, [genie_name]!{image=textheart}","shock","worriedCl") 

                call blktone 
                ">You give her tits a couple of firm squeezes..."
                call hide_blktone 

                if whoring >= 17:
                    call her_head("[genie_name], you promised not to touch...","base","baseL",cheeks="blush") 
                    m "I know, I know... But it's hard to resist..."
                    call her_head(".................","base","ahegao_raised",cheeks="blush") 
                else:
                    call her_head("[genie_name], you promised not to touch...","angry","worriedCl",cheeks="blush") 
                    m "I know, I know... But it's hard to resist..."
                    call her_head(".................","angry","angry",cheeks="blush") 

                call her_head("....................ah...{image=textheart}","base","ahegao_raised",cheeks="blush") 
                call her_head("[genie_name], you need to stop now...","base","ahegao_raised",cheeks="blush") 
                m "Just a bit longer..."

                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3

                call her_head("[genie_name]... please, stop this...","open","ahegao_raised",cheeks="blush") 
                m "Why? Because you like it too much?"
                call her_head("No it's not that...","base","baseL",cheeks="blush") 
                call her_head("I mean...","open","baseL",cheeks="blush") 

                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3

                call her_head("Ah...{image=textheart} [genie_name], I really need to go...","base","ahegao_raised",cheeks="blush") 
                if daytime:
                    call her_head("That's right... the classes are about to start...","open","baseL",cheeks="blush") 
                else:
                    call her_head("It is getting late...","open","baseL",cheeks="blush") 

                m "Well, alright..."
                call blkfade 

                ">You let go of the girl's breasts..."
                ">Hermione covers up..."

                call h_action("none") 
                call play_music("chipper_doodle") # HERMIONE'S THEME.

                if whoring >= 17:
                    call her_head("Please don't think I forgot that you broke your promise, [genie_name].","base","baseL",cheeks="blush",xpos="base",ypos="base") 
                else:
                    call her_head("Please don't think I forgot that you broke your promise, [genie_name].","annoyed","angryL",cheeks="blush",xpos="base",ypos="base") 

                m "Right..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") 
                call hide_blkfade 
                call ctc 

                call bld 

                if whoring >= 17:
                    call her_head("Thank you [genie_name].","open","baseL",cheeks="blush") 
                else:
                    call her_head("Can I have my payment now?","base","ahegao_raised",cheeks="blush") 
                    $ mad +=7


        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."

            #First time event.
            if whoring >= 6 and whoring <= 8:
                call ctc 

                menu:
                    "-Nod your head in approval-":
                        ">You Look at the girl's tits for a while and then nod in approval..."
                        her "......................"
                    "-Shake your head in disapproval-":
                        $ mad += 3
                        ">You Look at the girl's tits for a while and then shake your head in disappointment..."
                        her ".....................?"

            #Second time event.
            elif whoring >= 9 and whoring <= 11:
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
                        $ mad += 7
                        her "Tsk..."
                        her "Are we done then?"

            #Third time event.
            elif whoring >= 12:
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
            
            call set_hermione_action("none") 
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
            if whoring >= 6 and whoring <= 8:
                $ mad += 2
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                call blkfade 
                
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_head("[genie_name]?!!","angry","wide") 
                m "Just stand still, [hermione_name]..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade 
                call ctc 
                
                call bld 
                call nar(">You stare at Hermione's breasts with hunger...") 
                call her_head("[genie_name], what are you...?","shock","worriedCl") 
                call nar(">You keep stroking your hard cock...") 
                call her_head("[genie_name], no...","disgust","down_raised",cheeks="blush") 
                call her_head("You must... Put it away...","disgust","down_raised",cheeks="blush") 
                m "Stop whining [hermione_name]. I'm not touching you, am I?"
                call her_head("But...","angry","worriedCl",cheeks="blush") 
                call her_head("But I didn't agree to this!","angry","angry",cheeks="blush") 
                call her_head("I...","angry","worriedCl",cheeks="blush") 
                call her_head("I think I'd better leave now!","angry","worriedCl",cheeks="blush") 

                menu:
                    "\"Leave now, and you'll get no points!\"":

                        call her_head("After {size=+5}this{/size}? Are you kidding me, [genie_name]?","scream","wide",cheeks="blush") 
                        call her_head("I showed you my...","scream","wide",cheeks="blush") 
                        call her_head("..........","annoyed","angryL",cheeks="blush") 
                        call her_head("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry",cheeks="blush") 
                        call blkfade 
                        
                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, [hermione_name]!"

                        call h_action("none") 
                        call her_head("I am not setting a foot into your office ever again, [genie_name]!","angry","suspicious",cheeks="blush",xpos="base",ypos="base") 

                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        call her_head("You are a horrible person, [genie_name]...","angry","suspicious",cheeks="blush",tears="messy") 

                        $ mad += 30

                        call music_block 
                        jump could_not_flirt

                    "\"Alright, alright. That's enough for now.\"":
                        $ mad +=9
                        pass

                    "-Start jerking your cock faster-":
                        $ mad += 35

                        ">You start jerking your cock furiously!"
                        call her_head("No, [genie_name], stop!","scream","angry",cheeks="blush",emote="01") 
                        ">You jerk it even faster!"
                        call her_head("[genie_name], think I will be leaving now...","annoyed","angryL",cheeks="blush") 
                        g4 "No, wait, I'm almost there!"
                        call blkfade 

                        call her_head("Ew! [genie_name]!","angry","suspicious",cheeks="blush") 
                        call her_head("I'm leaving!","angry","suspicious",cheeks="blush") 
                        call h_action("none") 

                        call music_block 
                        jump could_not_flirt

            #Second Event.
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade 
                
                ">You take your cock out and start stroking it..."

                call her_head("[genie_name]?","angry","wide") 
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade 
                call ctc 
                
                call bld 
                call her_head("[genie_name], I didn't agree to this...","shock","worriedCl") 
                m "What are you complaining about, [hermione_name]?"
                m "I'm not even touching you..."
                call her_head("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl") 
                call nar(">You pick up the pace...") 
                m "just stand still, [hermione_name]."
                m "It will be over soon."
                call her_head("..................","shock","worriedCl") 
                call her_head("(It's so big...)","disgust","down_raised",cheeks="blush") 
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                call her_head("..............","disgust","down_raised",cheeks="blush") 
                call her_head("well, so be it...","open","baseL",cheeks="blush") 
                call her_head("You can keep touching yourself, [genie_name]...","open","baseL",cheeks="blush") 
                call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") 
                call her_head("Not to... em...","open","baseL",cheeks="blush") 
                call her_head("Not to discharge...","annoyed","angryL",cheeks="blush") 
                call her_head("Not in front of me, [genie_name]...","angry","angry") 
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                call her_head(".......................","angry","worriedCl",cheeks="blush") 
                call nar(">You start to stroke your cock even harder...") 
                g4 "Yes, I know you want this! Yes!"
                call her_head("................","angry","worriedCl",cheeks="blush") 
                call blkfade 
                
                ">You are about to cum..."

                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_head("...............","angry","worriedCl",cheeks="blush") 
                        ">Hermione covers up..."
                        call h_action("none") 
                    "-Just start cumming-":
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        call her_head("Proff-- ??","scream","wide",cheeks="blush") 
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
                        call her_head("[genie_name], no, you promised!","scream","angry",cheeks="blush",emote="01") 
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        call her_head("[genie_name], how could you...?","angry","suspicious",cheeks="blush") 
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised") 
                        call ctc 
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        her "I need to clean myself up..."
                        
                        hide screen hermione_main
                        call blkfade 

                        call h_action("none") 
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
                        $ mad += 45


            #Event three.
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade 

                ">You take your cock out and start stroking it..."
                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush") 
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade 
                call ctc 
                
                call bld 
                if whoring >= 17:
                    call her_head("ah...","base","ahegao_raised",cheeks="blush") 
                    call her_head("It's so big...","open","baseL",cheeks="blush") 
                    call her_head("You just couldn't help yourself, could you [genie_name]?","base","baseL",cheeks="blush") 
                    call her_head("..................","base","ahegao_raised",cheeks="blush") 
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_head("..............","base","ahegao_raised",cheeks="blush") 
                    call her_head("well, so be it...","open","baseL",cheeks="blush") 
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") 
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") 
                    call her_head("Not to cum on me, [genie_name]...","base","ahegao_raised",cheeks="blush") 
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","base","ahegao_raised",cheeks="blush") 
                    call nar(">You start to stroke your cock even harder...") 
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","base","ahegao_raised",cheeks="blush") 
                    # SAME AS PREVIOUS EVENT^^^

                else:
                    call her_head("[genie_name], actually I never agreed to this...","shock","worriedCl") 
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching you..."
                    call her_head("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl") 
                    #">You pick up the pace..."
                    m "Just stand still, [hermione_name]."
                    m "It will be over soon."
                    call her_head("..................","shock","worriedCl") 
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_head("..............","disgust","down_raised",cheeks="blush") 
                    call her_head("well, so be it...","open","baseL",cheeks="blush") 
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") 
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") 
                    call her_head("Not to discharge...","annoyed","angryL",cheeks="blush") 
                    call her_head("Not in front of me, [genie_name]...","annoyed","angryL",cheeks="blush") 
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","disgust","down_raised",cheeks="blush") 
                    call nar(">You start to stroke your cock even harder...") 
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","disgust","down_raised",cheeks="blush") 
                    # SAME AS PREVIOUS EVENT^^^

                    
                call blkfade 
                
                menu:
                    g4 "Argh! (I'm about to cum!)"
                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_head("...............","disgust","down_raised",cheeks="blush") 
                        call her_head("Ehm... I read that that is bad for you, [genie_name]...","disgust","down_raised",cheeks="blush") 
                        m "Huh?"
                        call her_head("It is bad for your health to just hold it in like this...","shock","worriedCl") 
                        call her_head("Em...","disgust","down_raised",cheeks="blush") 
                        call her_head("If you want to you can--","base","baseL",cheeks="blush") 
                        g4 "Argh! You whore!"
                        call her_head("???","mad","wide",cheeks="blush") 

                        call cum_block 

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True 

                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade 
                        call ctc 

                        call bld 
                        call her_head("[genie_name], I didn't mean that you can release your... semen on me, [genie_name]...","angry","worriedCl",cheeks="blush",emote="05") 
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3

                        call her_head("Well, what's done is done I suppose...","base","baseL",cheeks="blush") 
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
                        call h_action("none") 

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
                        call her_head("???","mad","wide",cheeks="blush") 

                        call cum_block 

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        call hide_blkfade 
                        call ctc 

                        call bld 
                        call her_head("ah...{image=textheart} It's so hot...{image=textheart}","shock","worriedCl") 
                        call her_head("[genie_name], you promised...","angry","worriedCl",cheeks="blush",emote="05") 
                        g4 "Oh, this is great, yes..."

                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        call her_head("Well, what's done is done I suppose...","angry","worriedCl",cheeks="blush") 
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
                        call h_action("none") #This reloads all her clothing!

                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base") 
                        call hide_blkfade 

                        call her_main("","base","base") 
                        call ctc 

                        her "Well, this should do for now..."
                        hide screen hermione_main
                        
    
    call blkfade 

    $ sperm_on_tits = False
    call h_action("none") #This reloads all her clothing!

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
    if whoring <= 16:
        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"

    stop music fadeout 10.0
    
    if whoring <= 16:
        call her_main("..................","annoyed","worriedL",xpos="base",ypos="base") 
    else:
        call her_main("..................","base","happyCl",xpos="base",ypos="base") 

    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    
    if whoring >= 6 and whoring <= 8:
        $ new_request_08_heart = 1
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 9 and whoring <= 11:
        $ new_request_08_heart = 2
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 12:
        $ new_request_08_heart = 3
        $ hg_pf_ShowThemToMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

    
    hide screen bld1
    hide screen hermione_main
    with d3

    #Door reaction.
    if whoring >= 6:

        call her_walk("desk","door",3) 

        if whoring >= 6 and whoring <= 8:  
            call her_head("(How humiliating... What have I become...?)","disgust","down_raised",cheeks="blush") 

        elif whoring >= 9 and whoring <= 11:
            call her_head("........................","disgust","down_raised",cheeks="blush") 

        elif whoring >= 12:
            call her_head("{size=-5}(That was so humiliating...){/size}","base","ahegao_raised",cheeks="blush") 
            call her_head("{size=-5}(No, Hermione, you silly girl!){/size}","angry","angry",cheeks="blush") 
            call her_head("{size=-5}(We are doing this to protect the honour of our house!){/size}","angry","angry",cheeks="blush") 
            call her_head(".................................","base","ahegao_raised",cheeks="blush") 

        elif whoring >= 17 and aftersperm:
            call her_head("{size=-5}(That was so exhilarating...){/size}","base","ahegao_raised",cheeks="blush") 
            call her_head("{size=-5}(I wonder if anyone will notice my uniform!){/size}","open","ahegao_raised",cheeks="blush") 
            call her_head("{size=-5}(What will people think of me?){/size}","open","ahegao_raised",cheeks="blush") 
            call her_head(".................................","base","ahegao_raised",cheeks="blush") 

        pause.5
        call her_chibi("leave","door","base") 

    else:
        call her_walk("desk","leave",3) 

    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    if whoring < 9: #Adds points till 9.
        $ whoring +=1

    $ hg_pf_ShowThemToMe_OBJ.points += 1
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme") 
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme") 
        $ hermione_sleeping = True
        jump night_main_menu
    








