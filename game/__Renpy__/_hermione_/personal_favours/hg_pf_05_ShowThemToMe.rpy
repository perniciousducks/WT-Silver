

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
                call her_main("As what?","open","worriedL") from _call_her_main_6612
                menu:
                    "-A Cheerleader-" if hg_gryffCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") from _call_play_sound_204 #Sound of a door opening.
                        call set_hermione_outfit(hg_gryffCheer_OBJ) from _call_set_hermione_outfit_16
                        pass
                    "-A Slytherin Cheerleader-" if hg_slythCheer_OBJ.purchased:
                        her "Fine, let me go change."
                        call play_sound("door") from _call_play_sound_205 #Sound of a door opening.
                        call set_hermione_outfit(hg_slythCheer_OBJ) from _call_set_hermione_outfit_17
                        pass
                    "-Power girl-" if hg_powerGirl_OBJ.purchased:
                        call her_main("In that ridiculous costume?","scream","angryCl") from _call_her_main_6613
                        m "It's not that bad. It has a nice cape."
                        call her_main("...","angry","worriedCl",emote="05") from _call_her_main_6614
                        call her_main("Fine, let me go change.","normal","worriedCl") from _call_her_main_6615
                        call play_sound("door") from _call_play_sound_206 #Sound of a door opening.
                        call set_hermione_outfit(hg_powerGirl_OBJ) from _call_set_hermione_outfit_18
                        pass
                call her_main("","","",xpos="mid") from _call_her_main_6616
                call ctc from _call_ctc_342
                m "very good"
            "\"(Not right now.)\"":
                pass       
    
    hide screen hermione_main
    with d3
    
    $ current_payout = 25 #Used when haggling about price of th favor.
    
    #First time event
    if hg_pf_ShowThemToMe_OBJ.points == 0 and whoring <= 11:
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]...","normal","base",xpos="mid",ypos="base") from _call_her_main_6617
        m "How much will it cost me to see your tits?"
        stop music fadeout 1.0
        call her_main("How much will it cost you to...?","open","base") from _call_her_main_6618
        call play_music("chipper_doodle") from _call_play_music_265 # HERMIONE'S THEME.

        call her_main("[genie_name]!","scream","angryCl") from _call_her_main_6619
        m "Hm... I thought your house could use some extra points..."
        m "But I guess I was wrong..."
        call her_main(".........?","open","base") from _call_her_main_6620
        m "Please don't mind me..."
        m "All I want to do is help you..."
        call her_main(".............","annoyed","worriedL") from _call_her_main_6621
        call her_main("200 house points, [genie_name].","normal","worriedCl") from _call_her_main_6622
        m "So if I give you 200 house points, [hermione_name]..."
        m "You will shamelessly bare your melons before me?"
        call her_main("[genie_name]! No need to be so vulgar!","angry","angry") from _call_her_main_6623
        her "I think I'd better go..."

        menu:
            "\"Wait. 200 points are yours. Show me!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                call her_main("Really?","open","base") from _call_her_main_6624
                m "Well?"
                call her_main("......................................","annoyed","worriedL") from _call_her_main_6625
                her "You have to promise me not to touch them, [genie_name]."
                m "Sure, sure..."
                call her_main("I am only doing this for the honour of my house, [genie_name]!","scream","worriedCl") from _call_her_main_6626

            "\"I will give you 5 points to see your tits.\"":
                call her_main("Five?!","scream","wide_stare") from _call_her_main_6627
                call her_main("[genie_name], I am not going to expose myself for a meagre five points!","angry","angry",emote="01") from _call_her_main_6628
                m "Well, your tits sure aren't worth 200, [hermione_name]!"
                call her_main("(They aren't?)","annoyed","down") from _call_her_main_6629
                call her_main("Maybe one hundred then?","annoyed","angryL") from _call_her_main_6630

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
                call music_block from _call_music_block_20
                jump could_not_flirt
                
                
        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d5

        call h_action("lift_top") from _call_h_action_81

        call play_music("playful_tension") from _call_play_music_266# SEX THEME.

        call her_chibi("lift_top","mid","base") from _call_her_chibi_186
        call ctc from _call_ctc_343

        call bld from _call_bld_120
        m "Hm..."
        call her_head("{size=-5}(My breasts are completely exposed...){/size}","disgust","down_raised",cheeks="blush") from _call_her_head_1518
        m "Come closer [hermione_name], let me take a better look..."
        call her_head("............","annoyed","angryL",cheeks="blush") from _call_her_head_1519

        call her_chibi("stand","mid","base") from _call_her_chibi_187
        pause.2

        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_25

        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."
       
        hide screen genie
        show screen genie_and_tits_01
        call hide_blkfade from _call_hide_blkfade_146
        call ctc from _call_ctc_344

        call bld from _call_bld_121
        call her_head("............","soft","baseL",cheeks="blush") from _call_her_head_1520
        m "Very good..."
        call her_head(".....","annoyed","angryL",cheeks="blush") from _call_her_head_1521
        
        hide screen bld1
        show screen blktone
        call her_main("","annoyed","annoyed",trans="fade",xpos="mid",ypos="base") from _call_her_main_6631
        call ctc from _call_ctc_345
        her "...................................."
    
    #Second event
    else:
        hide screen hermione_main
        with d3

        if whoring >= 6 and whoring <= 8:
            m "[hermione_name]?"
            call her_head("Yes, [genie_name]?","annoyed","angryL") from _call_her_head_1522
            m "I need to see your tits."
            call her_head("............","annoyed","angryL",cheeks="blush") from _call_her_head_1523
            call her_head("Do you promise not to touch, [genie_name]?","annoyed","angryL",cheeks="blush") from _call_her_head_1524
            m "Of course."
            hide screen bld1
            hide screen blktone
            hide screen hermione_main
            with d3
            pause.2

            call her_chibi("lift_top","mid","base") from _call_her_chibi_188
            call ctc from _call_ctc_346

            call bld from _call_bld_122
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."

            hide screen bld1
            call her_chibi("stand","mid","base") from _call_her_chibi_189
            pause.2

            call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_26

            ">Hermione slowly walks towards your desk."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            call hide_blkfade from _call_hide_blkfade_147
            call ctc from _call_ctc_347

            call bld from _call_bld_123
            m "Very good..."
            call play_music("playful_tension") from _call_play_music_267# SEX THEME.
            call h_action("lift_top") from _call_h_action_82
            
            hide screen bld1
            show screen blktone
            call her_main("","annoyed","annoyed",xpos="mid",trans="fade") from _call_her_main_6632
            call ctc from _call_ctc_348
            
            her "...................................."

        elif whoring >= 9:
            m "I need to see your tits, [hermione_name]."
            if whoring >= 17:
                call her_head("Of course [genie_name]","base","ahegao_raised",cheeks="blush") from _call_her_head_1525
            else:
                call her_head("Are you only going to watch, [genie_name]?","angry","worriedCl",cheeks="blush") from _call_her_head_1526
                m "Of course..."
            hide screen hermione_main
            call hide_blktone from _call_hide_blktone_22
            pause.2

            call her_chibi("lift_top","mid","base") from _call_her_chibi_190
            call ctc from _call_ctc_349

            call bld from _call_bld_124
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."

            hide screen bld1
            call her_chibi("stand","mid","base") from _call_her_chibi_191
            pause.2

            call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_27

            ">Hermione slowly walks towards your desk."

            hide screen genie
            show screen genie_and_tits_01
            with d1
            hide screen bld1
            call hide_blkfade from _call_hide_blkfade_148
            call ctc from _call_ctc_350

            call bld from _call_bld_125
            m "Very good..."
            
            call h_action("lift_top") from _call_h_action_83
            hide screen bld1
            show screen blktone
            call her_main("","base","closed",xpos="mid",trans="fade") from _call_her_main_6633
            call ctc from _call_ctc_351

            her "...................................."
            call play_music("playful_tension") from _call_play_music_268# SEX THEME.

    menu:
        "\"Break your promise. Grab the tits!\"":

            #First Time Event.

            #Event Fails
            if whoring >= 6 and whoring <= 8:
                hide screen hermione_main 
                call blkfade from _call_blkfade_199
                
                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") from _call_her_head_1527

                #Start Groping
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                call hide_blkfade from _call_hide_blkfade_149
                call ctc from _call_ctc_352

                call bld from _call_bld_126
                m "Relax, [hermione_name]. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                call play_music("chipper_doodle") from _call_play_music_269 # HERMIONE'S THEME.
                call her_head("No, [genie_name], please! You mustn't do this...","shock","worriedCl") from _call_her_head_1528
                m "This won't take long, just stand still."
                call her_head("[genie_name], I didn't agree to this!","angry","angry",cheeks="blush") from _call_her_head_1529
                with hpunch
                call her_head("You must unhand me now!!!","scream","angry",cheeks="blush",emote="01") from _call_her_head_1530

                call blkfade from _call_blkfade_200
                ">Hermione pulls away from you and covers up hastily."
                call h_action("none") from _call_h_action_84
                call her_head("I think I'd better go...","angry","worriedCl",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1531

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") from _call_her_chibi_192
                call hide_blkfade from _call_hide_blkfade_150
                call ctc from _call_ctc_353

                call bld from _call_bld_127
                m "Go ahead, [hermione_name]. You are not getting paid if you do..."
                call her_head("But I showed you my...","angry","worriedCl",cheeks="blush") from _call_her_head_1532
                call her_head("And you touched me...","angry","angry",cheeks="blush") from _call_her_head_1533
                call her_head("And I am getting nothing?","scream","angry",cheeks="blush",emote="01") from _call_her_head_1534
                m "You are dismissed, [hermione_name]..."
                call her_head("Gr..................","angry","worriedCl",cheeks="blush") from _call_her_head_1535
                call her_head("{size=-5}(Burn in hell, you wretched old---{/size}","angry","worriedCl",cheeks="blush") from _call_her_head_1536
                $ mad += 22
                call music_block from _call_music_block_21
                jump could_not_flirt

            #Event Succeeds
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade from _call_blkfade_201

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") from _call_her_head_1537

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_151
                show screen groping_naked_tits
                with fade
                call ctc from _call_ctc_354

                call bld from _call_bld_128
                m "Relax, [hermione_name]. Just stand still!"
                call her_head("I didn't agree to this, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_1538
                call her_head("I don't think you should...","annoyed","angryL",cheeks="blush") from _call_her_head_1539
                m "Don't you like it...?"
                call her_head("What?","disgust","down_raised",cheeks="blush") from _call_her_head_1540
                m "Don't you like it how I squeeze and pull on your breasts?"
                call her_head("...............","disgust","down_raised",cheeks="blush") from _call_her_head_1541
                m "Admit it, you like it a little bit..."
                call her_head("{size=-5}(So strange to see my breasts in someone else's hands...){/size}","disgust","down_raised",cheeks="blush") from _call_her_head_1542
                call her_head("[genie_name], I am letting you do this to me to help my house out, nothing more!","shock","worriedCl") from _call_her_head_1543
                call play_music("chipper_doodle") from _call_play_music_270 # HERMIONE'S THEME.
                call her_head("Please, unhand me now!","annoyed","angryL",cheeks="blush") from _call_her_head_1544
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."
                call h_action("none") from _call_h_action_85
                call her_head("You promised not to touch, [genie_name]...","annoyed","angryL",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1545
                m "It was hard to resist..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") from _call_her_chibi_193
                call hide_blkfade from _call_hide_blkfade_152
                call ctc from _call_ctc_355

                call bld from _call_bld_129
                call her_head(".............","soft","baseL",cheeks="blush") from _call_her_head_1546
                call her_head("Can I get paid now please?","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_1547
                m "Sure..."
                $ mad += 9

            #Event Also Succeeds
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade from _call_blkfade_202

                ">You reach out and dig your fingers into the girl's ample flesh..."
                call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush",xpos="base",ypos="high") from _call_her_head_1548

                #Start Groping
                hide screen blktone8
                hide screen blktone
                show screen chair_left #Genie's chair.
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_153
                show screen groping_naked_tits
                with fade
                call ctc from _call_ctc_356

                call bld from _call_bld_130
                m "Relax, [hermione_name]. Just stand still!"
                call her_head("But...","disgust","down_raised",cheeks="blush") from _call_her_head_1549
                call her_head("ah...{image=textheart}","shock","worriedCl") from _call_her_head_1550
                call her_head("I didn't agree to this...","disgust","down_raised",cheeks="blush") from _call_her_head_1551
                m "But you like it, don't you?"

                if whoring >= 17:
                    call her_head("I love it [genie_name]!{image=textheart}","open","baseL",cheeks="blush") from _call_her_head_1552
                else:
                    call her_head("I do not, [genie_name]!{image=textheart}","shock","worriedCl") from _call_her_head_1553

                call blktone from _call_blktone_28
                ">You give her tits a couple of firm squeezes..."
                call hide_blktone from _call_hide_blktone_23

                if whoring >= 17:
                    call her_head("[genie_name], you promised not to touch...","base","baseL",cheeks="blush") from _call_her_head_1554
                    m "I know, I know... But it's hard to resist..."
                    call her_head(".................","base","ahegao_raised",cheeks="blush") from _call_her_head_1555
                else:
                    call her_head("[genie_name], you promised not to touch...","angry","worriedCl",cheeks="blush") from _call_her_head_1556
                    m "I know, I know... But it's hard to resist..."
                    call her_head(".................","angry","angry",cheeks="blush") from _call_her_head_1557

                call her_head("....................ah...{image=textheart}","base","ahegao_raised",cheeks="blush") from _call_her_head_1558
                call her_head("[genie_name], you need to stop now...","base","ahegao_raised",cheeks="blush") from _call_her_head_1559
                m "Just a bit longer..."

                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3

                call her_head("[genie_name]... please, stop this...","open","ahegao_raised",cheeks="blush") from _call_her_head_1560
                m "Why? Because you like it too much?"
                call her_head("No it's not that...","base","baseL",cheeks="blush") from _call_her_head_1561
                call her_head("I mean...","open","baseL",cheeks="blush") from _call_her_head_1562

                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3

                call her_head("Ah...{image=textheart} [genie_name], I really need to go...","base","ahegao_raised",cheeks="blush") from _call_her_head_1563
                if daytime:
                    call her_head("That's right... the classes are about to start...","open","baseL",cheeks="blush") from _call_her_head_1564
                else:
                    call her_head("It is getting late...","open","baseL",cheeks="blush") from _call_her_head_1565

                m "Well, alright..."
                call blkfade from _call_blkfade_203

                ">You let go of the girl's breasts..."
                ">Hermione covers up..."

                call h_action("none") from _call_h_action_86
                call play_music("chipper_doodle") from _call_play_music_271 # HERMIONE'S THEME.

                if whoring >= 17:
                    call her_head("Please don't think I forgot that you broke your promise, [genie_name].","base","baseL",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1566
                else:
                    call her_head("Please don't think I forgot that you broke your promise, [genie_name].","annoyed","angryL",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1567

                m "Right..."

                #End Groping
                hide screen chair_left #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                call her_chibi("stand","desk","base") from _call_her_chibi_194
                call hide_blkfade from _call_hide_blkfade_154
                call ctc from _call_ctc_357

                call bld from _call_bld_131

                if whoring >= 17:
                    call her_head("Thank you [genie_name].","open","baseL",cheeks="blush") from _call_her_head_1568
                else:
                    call her_head("Can I have my payment now?","base","ahegao_raised",cheeks="blush") from _call_her_head_1569
                    $ mad +=7


        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."

            #First time event.
            if whoring >= 6 and whoring <= 8:
                call ctc from _call_ctc_358

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
                call ctc from _call_ctc_359

                menu:
                    "\"A Nice set of tits you got there.\"":
                        call her_main("","annoyed","closed") from _call_her_main_6634
                        pause
                        her "Thank--"
                        call play_music("chipper_doodle") from _call_play_music_272 # HERMIONE'S THEME.
                        call her_main("...........","annoyed","base") from _call_her_main_6635
                        call her_main("You are being inappropriate, [genie_name].","annoyed","annoyed") from _call_her_main_6636
                    "\"Hm... I've seen better.\"":
                        $ mad += 7
                        her "Tsk..."
                        her "Are we done then?"

            #Third time event.
            elif whoring >= 12:
                call ctc from _call_ctc_360

                menu:
                    "\"You have great tits, [hermione_name].\"":
                        call her_main("You really think so [genie_name]?","annoyed","base") from _call_her_main_6637
                        call her_main("I am glad you like them, [genie_name]...","base","closed") from _call_her_main_6638
                    "\"Your tits are alright I suppose...\"":
                        call her_main("Huh?","annoyed","base") from _call_her_main_6639
                        her "Does this mean you don't like them, [genie_name]?"
                        call her_main("I'm sorry...","disgust","down_raised") from _call_her_main_6640

            call blktone from _call_blktone_29
            ">You stare at her breasts for a while longer..."
            call hide_blktone from _call_hide_blktone_24
            call ctc from _call_ctc_361

            m "Alright, you can cover up, [hermione_name]..."
            her "............."
            pause.2
            
            call set_hermione_action("none") from _call_set_hermione_action_165
            pause.5
            
            call blkfade from _call_blkfade_204

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
                call blkfade from _call_blkfade_205
                
                call play_music("chipper_doodle") from _call_play_music_273 # HERMIONE'S THEME.
                call her_head("[genie_name]?!!","angry","wide") from _call_her_head_1570
                m "Just stand still, [hermione_name]..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade from _call_hide_blkfade_155
                call ctc from _call_ctc_362
                
                call bld from _call_bld_132
                call nar(">You stare at Hermione's breasts with hunger...") from _call_nar_665
                call her_head("[genie_name], what are you...?","shock","worriedCl") from _call_her_head_1571
                call nar(">You keep stroking your hard cock...") from _call_nar_666
                call her_head("[genie_name], no...","disgust","down_raised",cheeks="blush") from _call_her_head_1572
                call her_head("You must... Put it away...","disgust","down_raised",cheeks="blush") from _call_her_head_1573
                m "Stop whining [hermione_name]. I'm not touching you, am I?"
                call her_head("But...","angry","worriedCl",cheeks="blush") from _call_her_head_1574
                call her_head("But I didn't agree to this!","angry","angry",cheeks="blush") from _call_her_head_1575
                call her_head("I...","angry","worriedCl",cheeks="blush") from _call_her_head_1576
                call her_head("I think I'd better leave now!","angry","worriedCl",cheeks="blush") from _call_her_head_1577

                menu:
                    "\"Leave now, and you'll get no points!\"":

                        call her_head("After {size=+5}this{/size}? Are you kidding me, [genie_name]?","scream","wide",cheeks="blush") from _call_her_head_1578
                        call her_head("I showed you my...","scream","wide",cheeks="blush") from _call_her_head_1579
                        call her_head("..........","annoyed","angryL",cheeks="blush") from _call_her_head_1580
                        call her_head("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry",cheeks="blush") from _call_her_head_1581
                        call blkfade from _call_blkfade_206
                        
                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, [hermione_name]!"

                        call h_action("none") from _call_h_action_87
                        call her_head("I am not setting a foot into your office ever again, [genie_name]!","angry","suspicious",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1582

                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        call her_head("You are a horrible person, [genie_name]...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_head_1583

                        $ mad += 30

                        call music_block from _call_music_block_22
                        jump could_not_flirt

                    "\"Alright, alright. That's enough for now.\"":
                        $ mad +=9
                        pass

                    "-Start jerking your cock faster-":
                        $ mad += 35

                        ">You start jerking your cock furiously!"
                        call her_head("No, [genie_name], stop!","scream","angry",cheeks="blush",emote="01") from _call_her_head_1584
                        ">You jerk it even faster!"
                        call her_head("[genie_name], think I will be leaving now...","annoyed","angryL",cheeks="blush") from _call_her_head_1585
                        g4 "No, wait, I'm almost there!"
                        call blkfade from _call_blkfade_207

                        call her_head("Ew! [genie_name]!","angry","suspicious",cheeks="blush") from _call_her_head_1586
                        call her_head("I'm leaving!","angry","suspicious",cheeks="blush") from _call_her_head_1587
                        call h_action("none") from _call_h_action_88

                        call music_block from _call_music_block_23
                        jump could_not_flirt

            #Second Event.
            elif whoring >= 9 and whoring <= 11:
                hide screen hermione_main
                call blkfade from _call_blkfade_208
                
                ">You take your cock out and start stroking it..."

                call her_head("[genie_name]?","angry","wide") from _call_her_head_1588
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade from _call_hide_blkfade_156
                call ctc from _call_ctc_363
                
                call bld from _call_bld_133
                call her_head("[genie_name], I didn't agree to this...","shock","worriedCl") from _call_her_head_1589
                m "What are you complaining about, [hermione_name]?"
                m "I'm not even touching you..."
                call her_head("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl") from _call_her_head_1590
                call nar(">You pick up the pace...") from _call_nar_667
                m "just stand still, [hermione_name]."
                m "It will be over soon."
                call her_head("..................","shock","worriedCl") from _call_her_head_1591
                call her_head("(It's so big...)","disgust","down_raised",cheeks="blush") from _call_her_head_1592
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                call her_head("..............","disgust","down_raised",cheeks="blush") from _call_her_head_1593
                call her_head("well, so be it...","open","baseL",cheeks="blush") from _call_her_head_1594
                call her_head("You can keep touching yourself, [genie_name]...","open","baseL",cheeks="blush") from _call_her_head_1595
                call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_1596
                call her_head("Not to... em...","open","baseL",cheeks="blush") from _call_her_head_1597
                call her_head("Not to discharge...","annoyed","angryL",cheeks="blush") from _call_her_head_1598
                call her_head("Not in front of me, [genie_name]...","angry","angry") from _call_her_head_1599
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                call her_head(".......................","angry","worriedCl",cheeks="blush") from _call_her_head_1600
                call nar(">You start to stroke your cock even harder...") from _call_nar_668
                g4 "Yes, I know you want this! Yes!"
                call her_head("................","angry","worriedCl",cheeks="blush") from _call_her_head_1601
                call blkfade from _call_blkfade_209
                
                ">You are about to cum..."

                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_head("...............","angry","worriedCl",cheeks="blush") from _call_her_head_1602
                        ">Hermione covers up..."
                        call h_action("none") from _call_h_action_89
                    "-Just start cumming-":
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        call her_head("Proff-- ??","scream","wide",cheeks="blush") from _call_her_head_1603
                        call cum_block from _call_cum_block_67
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d1
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade from _call_hide_blkfade_157
                        with d3
                        call ctc from _call_ctc_364

                        call bld from _call_bld_134
                        $ sperm_on_tits = True
                        call her_head("[genie_name], no, you promised!","scream","angry",cheeks="blush",emote="01") from _call_her_head_1604
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        call her_head("[genie_name], how could you...?","angry","suspicious",cheeks="blush") from _call_her_head_1605
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised") from _call_her_main_6641
                        call ctc from _call_ctc_365
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        her "I need to clean myself up..."
                        
                        hide screen hermione_main
                        call blkfade from _call_blkfade_210

                        call h_action("none") from _call_h_action_90
                        $ sperm_on_tits = False

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base") from _call_her_chibi_195
                        show screen genie
                        
                        call hide_blkfade from _call_hide_blkfade_158
                        call her_main("","angry","angry") from _call_her_main_6642
                        call ctc from _call_ctc_366
                        #call play_music("chipper_doodle") # HERMIONE'S THEME.
                        her "How could you do this to me, [genie_name]?!"
                        her "You gave me your word!"
                        hide screen hermione_main
                        with d3
                        $ mad += 45


            #Event three.
            elif whoring >= 12:
                hide screen hermione_main
                call blkfade from _call_blkfade_211

                ">You take your cock out and start stroking it..."
                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush") from _call_her_head_1606
                ">You stare at Hermione's breasts with hunger..."

                #Start Jerking Off.
                hide screen genie
                hide screen bld1
                hide screen blktone
                show screen chair_left #Genie's chair.
                show screen jerking_off_01
                with d1
                call hide_blkfade from _call_hide_blkfade_159
                call ctc from _call_ctc_367
                
                call bld from _call_bld_135
                if whoring >= 17:
                    call her_head("ah...","base","ahegao_raised",cheeks="blush") from _call_her_head_1607
                    call her_head("It's so big...","open","baseL",cheeks="blush") from _call_her_head_1608
                    call her_head("You just couldn't help yourself, could you [genie_name]?","base","baseL",cheeks="blush") from _call_her_head_1609
                    call her_head("..................","base","ahegao_raised",cheeks="blush") from _call_her_head_1610
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_head("..............","base","ahegao_raised",cheeks="blush") from _call_her_head_1611
                    call her_head("well, so be it...","open","baseL",cheeks="blush") from _call_her_head_1612
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_1613
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") from _call_her_head_1614
                    call her_head("Not to cum on me, [genie_name]...","base","ahegao_raised",cheeks="blush") from _call_her_head_1615
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","base","ahegao_raised",cheeks="blush") from _call_her_head_1616
                    call nar(">You start to stroke your cock even harder...") from _call_nar_669
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","base","ahegao_raised",cheeks="blush") from _call_her_head_1617
                    # SAME AS PREVIOUS EVENT^^^

                else:
                    call her_head("[genie_name], actually I never agreed to this...","shock","worriedCl") from _call_her_head_1618
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching you..."
                    call her_head("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl") from _call_her_head_1619
                    #">You pick up the pace..."
                    m "Just stand still, [hermione_name]."
                    m "It will be over soon."
                    call her_head("..................","shock","worriedCl") from _call_her_head_1620
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    call her_head("..............","disgust","down_raised",cheeks="blush") from _call_her_head_1621
                    call her_head("well, so be it...","open","baseL",cheeks="blush") from _call_her_head_1622
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_1623
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") from _call_her_head_1624
                    call her_head("Not to discharge...","annoyed","angryL",cheeks="blush") from _call_her_head_1625
                    call her_head("Not in front of me, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_1626
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","disgust","down_raised",cheeks="blush") from _call_her_head_1627
                    call nar(">You start to stroke your cock even harder...") from _call_nar_670
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","disgust","down_raised",cheeks="blush") from _call_her_head_1628
                    # SAME AS PREVIOUS EVENT^^^

                    
                call blkfade from _call_blkfade_212
                
                menu:
                    g4 "Argh! (I'm about to cum!)"
                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_head("...............","disgust","down_raised",cheeks="blush") from _call_her_head_1629
                        call her_head("Ehm... I read that that is bad for you, [genie_name]...","disgust","down_raised",cheeks="blush") from _call_her_head_1630
                        m "Huh?"
                        call her_head("It is bad for your health to just hold it in like this...","shock","worriedCl") from _call_her_head_1631
                        call her_head("Em...","disgust","down_raised",cheeks="blush") from _call_her_head_1632
                        call her_head("If you want to you can--","base","baseL",cheeks="blush") from _call_her_head_1633
                        g4 "Argh! You whore!"
                        call her_head("???","mad","wide",cheeks="blush") from _call_her_head_1634

                        call cum_block from _call_cum_block_68

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed.
                        $ sperm_on_tits = True 

                        show screen jerking_off_cum
                        hide screen bld1
                        call hide_blkfade from _call_hide_blkfade_160
                        call ctc from _call_ctc_368

                        call bld from _call_bld_136
                        call her_head("[genie_name], I didn't mean that you can release your... semen on me, [genie_name]...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_1635
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3

                        call her_head("Well, what's done is done I suppose...","base","baseL",cheeks="blush") from _call_her_head_1636
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base") from _call_her_main_6643
                        call ctc from _call_ctc_369

                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        call her_main("Thank you [genie_name].","base","closed") from _call_her_main_6644
                        call her_main("Now I need to clean myself up...","annoyed","closed") from _call_her_main_6645
                        call ctc from _call_ctc_370
                        
                        hide screen hermione_main
                        call blkfade from _call_blkfade_213

                        $ sperm_on_tits = False
                        $ aftersperm = True
                        call h_action("none") from _call_h_action_91

                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base") from _call_her_chibi_196
                        show screen genie
                        call hide_blkfade from _call_hide_blkfade_161

                        call her_main("","base","base") from _call_her_main_6646
                        call ctc from _call_ctc_371
                        her "Well, this should do for now..."
                        hide screen hermione_main

                    "-Just start cumming-":
                        g4 "Argh! You whore!"
                        call her_head("???","mad","wide",cheeks="blush") from _call_her_head_1637

                        call cum_block from _call_cum_block_69

                        g4 "Argh! YES!"

                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        $ sperm_on_tits = True

                        show screen jerking_off_cum
                        call hide_blkfade from _call_hide_blkfade_162
                        call ctc from _call_ctc_372

                        call bld from _call_bld_137
                        call her_head("ah...{image=textheart} It's so hot...{image=textheart}","shock","worriedCl") from _call_her_head_1638
                        call her_head("[genie_name], you promised...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_1639
                        g4 "Oh, this is great, yes..."

                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        call her_head("Well, what's done is done I suppose...","angry","worriedCl",cheeks="blush") from _call_her_head_1640
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        call her_main("","disgust","down_raised",xpos="mid",ypos="base") from _call_her_main_6647
                        call ctc from _call_ctc_373

                        her "My uniform is ruined though..."
                        m "Don't worry, I'm sure no one will notice."
                        m "You did good."
                        call her_main("Thank you [genie_name].","base","closed") from _call_her_main_6648
                        call her_main("Now I need to clean myself up...","annoyed","closed") from _call_her_main_6649
                        call ctc from _call_ctc_374

                        hide screen hermione_main
                        call blkfade from _call_blkfade_214

                        $ sperm_on_tits = False
                        call h_action("none") from _call_h_action_92 #This reloads all her clothing!

                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_left
                        call her_chibi("stand","desk","base") from _call_her_chibi_197
                        call hide_blkfade from _call_hide_blkfade_163

                        call her_main("","base","base") from _call_her_main_6650
                        call ctc from _call_ctc_375

                        her "Well, this should do for now..."
                        hide screen hermione_main
                        
    
    call blkfade from _call_blkfade_215

    $ sperm_on_tits = False
    call h_action("none") from _call_h_action_93 #This reloads all her clothing!

    hide screen jerking_off_01
    hide screen chair_left
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    hide screen groping_01
    hide screen groping_02

    call her_chibi("stand","desk","base") from _call_her_chibi_198
    show screen genie
    call hide_blkfade from _call_hide_blkfade_164
    pause.5
    
    call bld from _call_bld_138
    if whoring <= 16:
        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"

    stop music fadeout 10.0
    
    if whoring <= 16:
        call her_main("..................","annoyed","worriedL",xpos="base",ypos="base") from _call_her_main_6651
    else:
        call her_main("..................","base","happyCl",xpos="base",ypos="base") from _call_her_main_6652

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

        call her_walk("desk","door",3) from _call_her_walk_125

        if whoring >= 6 and whoring <= 8:  
            call her_head("(How humiliating... What have I become...?)","disgust","down_raised",cheeks="blush") from _call_her_head_1641

        elif whoring >= 9 and whoring <= 11:
            call her_head("........................","disgust","down_raised",cheeks="blush") from _call_her_head_1642

        elif whoring >= 12:
            call her_head("{size=-5}(That was so humiliating...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_1643
            call her_head("{size=-5}(No, Hermione, you silly girl!){/size}","angry","angry",cheeks="blush") from _call_her_head_1644
            call her_head("{size=-5}(We are doing this to protect the honour of our house!){/size}","angry","angry",cheeks="blush") from _call_her_head_1645
            call her_head(".................................","base","ahegao_raised",cheeks="blush") from _call_her_head_1646

        elif whoring >= 17 and aftersperm:
            call her_head("{size=-5}(That was so exhilarating...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_1647
            call her_head("{size=-5}(I wonder if anyone will notice my uniform!){/size}","open","ahegao_raised",cheeks="blush") from _call_her_head_1648
            call her_head("{size=-5}(What will people think of me?){/size}","open","ahegao_raised",cheeks="blush") from _call_her_head_1649
            call her_head(".................................","base","ahegao_raised",cheeks="blush") from _call_her_head_1650

        pause.5
        call her_chibi("leave","door","base") from _call_her_chibi_199

    else:
        call her_walk("desk","leave",3) from _call_her_walk_126

    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    if whoring < 9: #Adds points till 9.
        $ whoring +=1

    $ hg_pf_ShowThemToMe_OBJ.points += 1
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme") from _call_play_music_274
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme") from _call_play_music_275
        $ hermione_sleeping = True
        jump night_main_menu
    








