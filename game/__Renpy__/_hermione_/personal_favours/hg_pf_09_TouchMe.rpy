

label hg_pf_TouchMe: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TouchMe_OBJ.points == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(I feel like getting another handjob!){/size}"

    if hg_pf_TouchMe_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_gryffCheer_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL") from _call_her_main_4598
                m "A Cheerleader."
                if whoring >= 17:
                    call her_main("A Cheerleader?","annoyed","annoyed") from _call_her_main_4599
                    m "For gryffindor."
                    call her_main("...","upset","wink") from _call_her_main_4600
                    call her_main("Fine, at least it's gryffindor.","annoyed","worriedL") from _call_her_main_4601
                    call play_sound("door") from _call_play_sound_176 #Sound of a door opening.
                    call set_hermione_outfit(hg_gryffCheer_OBJ) from _call_set_hermione_outfit_13
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    $ current_payout = 45 #Used when haggling about price of th favor.
    
    call bld from _call_bld_101

    #First Event.
    if hg_pf_TouchMe_OBJ.points == 0:

        m "[hermione_name]."
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base") from _call_her_main_4602
        m "Do you know what a \"handjob\" is?"

        if whoring < 12:
            jump too_much

        call her_main("Why?","annoyed","annoyed") from _call_her_main_4603
        m "I feel like getting one..."
        call her_main("[genie_name]!","angry","angry") from _call_her_main_4604
        m "Just another favour. No big deal, right?"
        call her_main("......","disgust","glance") from _call_her_main_4605
        call her_main("{size=-7}I want 100 house points for this...{/size}","angry","worriedCl",emote="05") from _call_her_main_4606
        m "Huh? What was that?"
        call her_main("I want 100 house points for this!!!","scream","worriedCl") from _call_her_main_4607
        m "100 house points, huh?"
        m "And you will stroke my cock and everything?"
        call her_main("{size=-7}Yes...{/size}","disgust","glance") from _call_her_main_4608
        m "Sorry, I couldn't hear you..."
        call her_main("Yes, I said yes! I will stroke your cock, [genie_name]!","scream","worriedCl") from _call_her_main_4609
    
        $ new_request_16_heart = 1
        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        label back_to_handjob_choices:

        menu:
            m "..."
            "\"You will get 15 house points.\"":
                $ mad +=7
                call her_main("For 15 house points I suppose I could let you molest me a little, but that is all you'll be getting, [genie_name].","annoyed","angryL") from _call_her_main_4610
                her "I will not stoop as low as to sell handjobs for 15 house points."
                her "That is just insulting, [genie_name]."
                jump back_to_handjob_choices

            "\"you will get 45 house points.\"":
                if mad > 7: #You could spam points into infinity with the choice above.
                    $ mad = 7
                call her_main(".....","annoyed","angryL") from _call_her_main_4611
                call her_main("45 house points...?","open","down") from _call_her_main_4612
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                call her_main("Yes, it is a yes, [genie_name].","annoyed","annoyed") from _call_her_main_4613
                m "Great!"

            "\"you will get 100 house points.\"":
                call play_music("chipper_doodle") from _call_play_music_174 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 house points?!","scream","wide_stare") from _call_her_main_4614
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "Is that a \"yes\" then?"
                call her_main("Of course!","smile","happyCl") from _call_her_main_4615
                call her_main("If it will bring \"Gryffindor\" 100 house points, I don't mind touching your... thing a little.","smile","happyCl",emote="06") from _call_her_main_4616


        call play_music("playful_tension") from _call_play_music_175# SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        show screen chair_left
        hide screen desk
        show screen desk
        call gen_chibi("jerking_off","on_girl","base") from _call_gen_chibi_67

        hide screen bld1
        hide screen blktone
        with fade
        call ctc from _call_ctc_267

        show screen bld1
        call her_main("...........","open","base",xpos="right",ypos="base") from _call_her_main_4617
        m "Whenever you're ready, [hermione_name]."
        pause.5

        label event_01_round_02:
        hide screen hermione_main
        call blkfade from _call_blkfade_145

        ">Hermione puts her slender hands on your cock..."
        m "Good. Now stroke it."
        call her_head("Right...","angry","worriedCl",emote="05") from _call_her_head_963 
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide") from _call_her_chibi_150
        call gen_chibi("handjob","desk","base") from _call_gen_chibi_68
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_104
        call ctc from _call_ctc_268

        call play_music("playful_tension") from _call_play_music_176# SEX THEME.
        call blktone from _call_blktone_24
        g9 "Nice..."

        if hg_pf_TouchMe_OBJ.points == 0:
            call her_main("!!!","shock","wide",xpos="right",ypos="base") from _call_her_main_4618
            call her_main("Are you about to finish, [genie_name]?!") from _call_her_main_4619
            m "About to finish?"
            m "Don't be ridiculous [hermione_name], we are just getting started."
            call her_main("Oh...","angry","worriedCl",emote="05") from _call_her_main_4620
            call her_main("......") from _call_her_main_4621
            call her_main("You will give me a warning though, won't you, [genie_name]?","upset","wink") from _call_her_main_4622 
        else:
            call her_main("[genie_name]...?","angry","worriedCl",emote="05",xpos="right",ypos="base") from _call_her_main_4623    
            m "What is it?"
            call her_main("Will you warn me before... uhm... you now...","angry","worriedCl",emote="05") from _call_her_main_4624

        $ d_flag_01 = False #If TRUE Genie promised to warn her.

        menu:
            m "..."
            "\"Of course I'll let you know when it's time.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                call her_main("Thank you, [genie_name].","normal","worriedCl") from _call_her_main_4625 
            "\"I myself don't always know when...\"":
                call her_main("Really? But I thought...","open","base") from _call_her_main_4626
                call her_main("Well, never mind then...","normal","worriedCl") from _call_her_main_4627 

        call her_main("........","open","base") from _call_her_main_4628 
        m "............."
        call her_main(".............","normal","worriedCl") from _call_her_main_4629
        call her_main("Err... [genie_name]?") from _call_her_main_4630 
        m "Yes, what is it?"
        call her_main("How long do you think this will take?","open","base") from _call_her_main_4631 
        m "Why?"

        if daytime:
            call her_main("Well, it's just that my classes are about to start...","upset","wink") from _call_her_main_4632
        else: 
            call her_main("Well, it's just that I have this paper that I need to finish...","upset","wink") from _call_her_main_4633
            call her_main("It's due tomorrow, and it's getting pretty late...") from _call_her_main_4634

        m "Do you need the points or not?"
        call her_main("I do, [genie_name]! I'm sorry...","base","happyCl") from _call_her_main_4635
        call her_main("I will just keep on stroking it then...") from _call_her_main_4636
        m "Well, there is something you could do to speed up the process..."
        call her_main("Really? What is it [genie_name]?","base","base") from _call_her_main_4637 

        menu:
            m "..."
            "\"Tell me how much of a whore you are!\"":
                call her_main("What?","angry","angry") from _call_her_main_4638
                call her_main("But I'm not...") from _call_her_main_4639
                m "No need to be honest, [hermione_name]."
                m "Just make things up."
                call her_main("Really?","upset","wink") from _call_her_main_4640 
                m "Sure. Just have fun with it."
                call her_main("Well, in that case...","open","down") from _call_her_main_4641
                call her_main("I am a... whore.") from _call_her_main_4642
                m "Heh... good. Go on."
                call her_main("I am a big whore...","open","down") from _call_her_main_4643 
                m "Yes, you are."
                call her_main("I am the biggest whore in England!","annoyed","annoyed") from _call_her_main_4644
                call her_main("I try to act innocent, but in truth all I think about is cock!") from _call_her_main_4645
                m "Yes, you little slut!"
                call her_main("Yes! I am a slut!","annoyed","angryL") from _call_her_main_4646
                call her_main("I crave cock all the time.") from _call_her_main_4647
                m "Very nice!"
                m "But, like I said, you don't have to be honest."
                call her_main("What?","shock","wide") from _call_her_main_4648
                call her_main("[genie_name], those things I say are not true!","upset","wink") from _call_her_main_4649 
                g9 "Heh... I know. I'm just messing with you."
                call her_main("[genie_name]!","disgust","glance") from _call_her_main_4650 
                m "You are doing a great job, though. Keep at it!"
                call her_main(".....","open","down") from _call_her_main_4651
                call her_main("I love cock...") from _call_her_main_4652
                call her_main("And I love... spunk...","clench","down_raised") from _call_her_main_4653
                call her_main("And semen... and sperm...") from _call_her_main_4654
                call her_main("I love to drink sperm...") from _call_her_main_4655
                call her_main("I want you to feed me your sperm, [genie_name]!","open_tongue","glance") from _call_her_main_4656 
                g4 "!!!"
                call her_main("Or better yet, pump me full of it, [genie_name]!","smile","glance") from _call_her_main_4657
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            
            "\"Stick your tongue out and look at me!\"":
                call her_main("What?","base","base") from _call_her_main_4658 
                m "Just do it, slut."
                call her_main("Like this?","open_wide_tongue","squintL") from _call_her_main_4659 
                m "Yes, good. Keep looking into my eyes and stroke my cock."
                call her_main(".....................","open_wide_tongue","base") from _call_her_main_4660 
                m "Yes... Good..."
                call her_main("...........","open_wide_tongue","base") from _call_her_main_4661
                call her_main("...........") from _call_her_main_4662
                call her_main("I can't keep my mouth open for so long, [genie_name]. I will start to drool...","open","base") from _call_her_main_4663 
                m "But I want you to drool..."
                call her_main("What? But I will look silly!","open","base") from _call_her_main_4664 
                m "That's the point, [hermione_name]!"
                call her_main(".......","annoyed","worriedL") from _call_her_main_4665 
                m "Don't you want to be done with this as soon as possible?"
                call her_main("............","normal","worriedCl") from _call_her_main_4666
                call her_main("A-ha.....","open_wide_tongue","base") from _call_her_main_4667 
                m "Good, [hermione_name]."
                call her_main("..............","open_wide_tongue","base") from _call_her_main_4668 
                m "Yes, keep on stroking my cock."
                call her_main("..................","open_wide_tongue","base") from _call_her_main_4669
                g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
                call her_main(".................","open_wide_tongue","angryCl") from _call_her_main_4670 
                m "No, keep on looking at me!"
                call her_main(".....................","open_wide_tongue","base") from _call_her_main_4671 
                m "Yes, you little slut!"
                call her_main("......................","open_wide_tongue","angry") from _call_her_main_4672 
                m "I want to cum in that mouth, yes..."
                call her_main("................","open_wide_tongue","angry") from _call_her_main_4673 
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

            "\"Give my cock a kiss!\"":
                call her_main("Excuse me?","angry","angry") from _call_her_main_4674 
                m "You know, just a little kiss, right on the tip."
                call her_main(".............","angry","angry") from _call_her_main_4675
                call her_main("...with my lips?","shock","wide") from _call_her_main_4676 
                m "Sure... That will speed things up, I'm telling you."
                call her_main("*sigh!*..............","open","down") from _call_her_main_4677
                call her_main("Well, I might as well, I suppose...") from _call_her_main_4678
                call nar(">Hermione gives the tip of your engorged cock a tender kiss.") from _call_nar_526

                hide screen hermione_main
                hide screen blktone
                call blkfade from _call_blkfade_146

                call gen_chibi("handjob_kiss","desk","base") from _call_gen_chibi_69
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                call hide_blkfade from _call_hide_blkfade_105
                pause 2

                call gen_chibi("handjob","desk","base") from _call_gen_chibi_70
                pause.5

                show screen blktone
                call her_main("Like this?","open","down") from _call_her_main_4679 
                m "Wasn't that bad, was it?"
                call her_main("No, I suppose not...","upset","wink") from _call_her_main_4680 
                m "Can you do it again, then?"
                call her_main("I could...","normal","worriedCl") from _call_her_main_4681 
                m "Do it!"
                call her_main("Well, alright...","open","base") from _call_her_main_4682
                call nar(">Hermione gives your cock another kiss...") from _call_nar_527

                hide screen hermione_main
                hide screen blktone
                call blkfade from _call_blkfade_147

                call gen_chibi("handjob_kiss","desk","base") from _call_gen_chibi_71
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                call hide_blkfade from _call_hide_blkfade_106
                pause 3

                call nar(">This time she lingers a moment longer...") from _call_nar_528
                pause.8

                call blkfade from _call_blkfade_148
                call gen_chibi("handjob","desk","base") from _call_gen_chibi_72
                call hide_blkfade from _call_hide_blkfade_107
                pause.5

                call blktone from _call_blktone_25
                m "Good... Now do it again and just stay there for a while."
                call her_main("You mean with my lips touching your... cock, [genie_name]?","open","base") from _call_her_main_4683
                call her_main("No, I will look stupid...","annoyed","worriedL") from _call_her_main_4684 
                m "Don't be silly, [hermione_name]. Nobody is watching."
                call her_main("You are, [genie_name].","open","down") from _call_her_main_4685 
                m "But that's the whole point!"
                call her_main("......","annoyed","annoyed") from _call_her_main_4686 
                m "It will make me cum in no time!"
                call her_main("...............","annoyed","angryL") from _call_her_main_4687 
                m "And then you can just get out and and take care of your business today."
                call her_main(".............","disgust","glance") from _call_her_main_4688
                call her_main("Well, alright then....","open","down") from _call_her_main_4689
                call nar(">Hermione reaches down with her lips again...","start") from _call_nar_529
                call nar(">She touches the tip of your cock with her lips and keeps them there...","end") from _call_nar_530

                hide screen hermione_main
                hide screen blktone
                call blkfade from _call_blkfade_149

                call gen_chibi("handjob_kiss","desk","base") from _call_gen_chibi_73
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                call hide_blkfade from _call_hide_blkfade_108
                call ctc from _call_ctc_269

                call blktone from _call_blktone_26
                m "Very good..."
                m "Now touch it with your tongue."
                call her_main("??!","open_tongue","") from _call_her_main_4690
                m "That's the last thing I will be asking of you today."
                her "............"
                call nar(">You feel the tip of Hermione's tongue warily rubbing against the head of your cock...") from _call_nar_531
                m "Yes, like this..."
                call nar(">Hermione wiggles her tongue a little....") from _call_nar_532
                m "Yes... Good..."

                call blkfade from _call_blkfade_150
                hide screen hermione_main
                call gen_chibi("handjob","desk","base") from _call_gen_chibi_74
                hide screen blktone
                call hide_blkfade from _call_hide_blkfade_109
                pause.8

                show screen blktone
                call her_main("So, did it work? Are you ready to... finish, [genie_name]?","open","down") from _call_her_main_4691 
                g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"

        menu:
            m "..."
            "-Give her a warning-":
                g4 "Here it comes, [hermione_name]! You better be ready!"
                call her_main("What? So soon?!","shock","wide") from _call_her_main_4692 
                g4 "{size=+5}Yeah, you did a great job!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen hermione_main
                call blkfade from _call_blkfade_151

                call her_head("No, [genie_name], wait, I--","angry","base") from _call_her_head_964 
                g4 "{size=+5}Too late for that, slut!{/size}"
                call her_head("*whimper*","angry","down_raised") from _call_her_head_965       
                ">Hermione suddenly slides your already dripping cock under her shirt..."
                g4 "?!!"
                ">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man."

                call cum_block from _call_cum_block_49

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_966 
                
                call gen_chibi("cumming_under_shirt","desk","base") from _call_gen_chibi_75
                hide screen blktone
                call hide_blkfade from _call_hide_blkfade_110
                stop music fadeout 1.0
                call ctc from _call_ctc_270
                        
                $ aftersperm = True
                call her_main(".......................","angry","wide") from _call_her_main_4693                
                m "..........................."
                call her_main(".......................","angry","wide") from _call_her_main_4694    
                m "....................?"
                call her_main(".......................","angry","down_raised") from _call_her_main_4695    
                m "...What the fuck just happened?"

                call play_music("chipper_doodle") from _call_play_music_177 # HERMIONE'S THEME.

                show screen bld1
                call her_main("I don't know... I suppose I just panicked...","angry","worriedCl",emote="05") from _call_her_main_4696

                if daytime:
                    call her_main("My classes are about to start and I didn't want you to ruin my uniform, [genie_name]...","angry","worriedCl",emote="05") from _call_her_main_4697 
                    m "So you'll go to classes like this now?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_main("What choice do I have?","angry","down_raised") from _call_her_main_4698
                    call her_main("I can't just skip a class...") from _call_her_main_4699
                else:
                    call her_main("At this hour The \"Gryffindor\" common room will be full of people...","angry","worriedCl",emote="05") from _call_her_main_4700
                    call her_main("I didn't want to have to return there all covered in your... spunk, [genie_name].") from _call_her_main_4701
                    call her_main("Oh, it's getting pretty late...","angry","base") from _call_her_main_4702 
                    m "So you will go like this, instead?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_main("What choice do I have?","angry","down_raised") from _call_her_main_4703     
                    
                call ctc from _call_ctc_271
                call blkfade from _call_blkfade_152

                ">Hermione releases your still pulsating cock."
                
                call her_chibi("stand","mid","base") from _call_her_chibi_151
                call gen_chibi("stand","desk","base") from _call_gen_chibi_76
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_111
                pause.5

                call her_main("Ew... Your sperm, [genie_name]...","angry","down_raised") from _call_her_main_4704
                call her_main("It's everywhere under my uniform...","angry","base") from _call_her_main_4705          
                m "Just put it in your mouth next time."
                call her_main("I... don't think so, [genie_name].","annoyed","annoyed") from _call_her_main_4706
                call her_main("I really need to go. Can I just get paid now?") from _call_her_main_4707


            "-Just start cumming-":

                with hpunch
                g4 "ARGH!"
                call blkfade from _call_blkfade_153

                call her_head("WHAT?!","shock","wide") from _call_her_head_967               
                g4 "Take this!"

                call cum_block from _call_cum_block_50

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_968 
                
                call gen_chibi("cumming_on_shirt","desk","base") from _call_gen_chibi_77
                hide screen blktone
                call hide_blkfade from _call_hide_blkfade_112
                call ctc from _call_ctc_272
                        
                $ aftersperm = True

                show screen bld1
                call her_main(".......................","angry","wide") from _call_her_main_4708  
                call gen_chibi("cumming_on_shirt_pause") from _call_gen_chibi_78                
                m "Yes... I Feel so much better now..."
                pause.5
                
                $ g_c_u_pic = "images/animation/15_cum_21.png"
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True
                
                call her_main("","soft","base",tears="soft") from _call_her_main_4709
                pause.5
                her ".........."
                m "Well, I think that's about it..."
                pause.2

                hide screen hermione_main
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide") from _call_gen_chibi_79
                call her_chibi("stand","desk","base") from _call_her_chibi_152
                show screen genie
                hide screen bld1
                with fade
                pause.8

                show screen bld1
                call her_main("[genie_name]! What have you done?!","scream","worriedCl") from _call_her_main_4710
                m "What?"

                if d_flag_01: #If TRUE Genie promised to warn her.
                    call play_music("chipper_doodle") from _call_play_music_178 # HERMIONE'S THEME.
                    $ mad += 11
                    call her_main("You promised to give me a warning, [genie_name]!","angry","angry") from _call_her_main_4711
                    m "Oh, that's right... My bad."
                    call her_main("My uniform is ruined...","annoyed","angryL") from _call_her_main_4712
                    her "...I would like to get paid now."

                else:

                    if daytime:
                        call her_main("My uniform is ruined now!","annoyed","angryL") from _call_her_main_4713
                        call her_main("My classes are about to start and I can't go looking like this!","open","down") from _call_her_main_4714
                        m "Of course you can, just wipe it off or something..."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","annoyed","annoyed") from _call_her_main_4715
                    else:
                        call her_main("My uniform is ruined!","annoyed","angryL") from _call_her_main_4716
                        her "Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                        m "Why not? You look hot, [hermione_name]!"
                        call her_main("[genie_name]!!!","annoyed","annoyed") from _call_her_main_4717
                        m "Alright, alright. Just wipe it off or something."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","annoyed","annoyed") from _call_her_main_4718


    #Second Event.
    elif hg_pf_TouchMe_OBJ.points == 1:
    
        $ new_request_16_heart = 2
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base") from _call_her_main_4719
        m "Do you know what a \"handjob\" is?"
        call her_main("You have asked me that already, [genie_name].","disgust","glance") from _call_her_main_4720
        m "Ah, that's right."
        m "Well, I want you to play with my cock again."
        call her_main("[genie_name], you are being vulgar again...","upset","closed") from _call_her_main_4721
        m "Fine, fine."
        m "[hermione_name], I would like to buy another favour from you today."
        call her_main("Of course, [genie_name].","annoyed","angryL") from _call_her_main_4722
        g9 "The favour being you playing with my cock!"
        call her_main("..............","disgust","glance") from _call_her_main_4723
        m "Oh, come on. For the honour of the \"Gryffindors\"?"
        call her_main(".............","angry","angry") from _call_her_main_4724
        g9 "Play with my cock for the honour of the \"Gryffindors\", [hermione_name]!"
        call her_main("Stop saying that, [genie_name]...","scream","angry",emote="01") from _call_her_main_4725
        m "Come on [hermione_name], it's not like I'm asking you to do this for free."
        call her_main(".......","annoyed","angryL") from _call_her_main_4726
        stop music fadeout 4.0

        jump event_01_round_02 #Sets up handjob.


    #Third Event.
    elif hg_pf_TouchMe_OBJ.points >= 2:
    
        $ new_request_16_heart = 3
        $ hg_pf_TouchMe_OBJ.hearts_level = 3 #Event hearts level (0-3)
        
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base") from _call_her_main_4727
        m "You don't mind giving me another handjob, do you?"
        
        if whoring <= 16:
            call her_main("As long as I am getting paid...","grin","baseL") from _call_her_main_4728
            m "Well, come here then. Time to earn those points."
        else:
            call her_main("Of course not [genie_name]...","grin","baseL") from _call_her_main_4729
            m "Well, come here then."
        
        
        hide screen hermione_main          
        hide screen bld1
        call blkfade from _call_blkfade_154

        stop music fadeout 3.0
        call her_head("Do you like it when I do it like this, [genie_name]?","grin","baseL") from _call_her_head_969
        g9 "Actually, yes! Very nice!"
        call play_music("chipper_doodle") from _call_play_music_179 # HERMIONE'S THEME.
        
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide") from _call_her_chibi_153
        call gen_chibi("handjob","desk","base") from _call_gen_chibi_80
        
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_113
        call ctc from _call_ctc_273

        call blktone from _call_blktone_27
        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        call her_main("Thank you, [genie_name].","base","happyCl",xpos="right",ypos="base") from _call_her_main_4730
        call her_main("I figured the better I do this, the sooner it'll be over.") from _call_her_main_4731
        m "Hm..."
        
        menu:
            m "..."
            "\"What do you think of my cock?\"":
                call her_main("Huh?","open","base") from _call_her_main_4732
                call her_main("Oh, that's right...") from _call_her_main_4733
                call her_main("I need to compliment your penis! I completely forgot about that!","angry","worriedCl",emote="05") from _call_her_main_4734         
                m "Well, you don't have to--"
                call her_main("[genie_name], let me be honest with you...","upset","closed") from _call_her_main_4735         
                m "Yes?"
                call her_main("You have the biggest penis I have ever seen!","smile","angry") from _call_her_main_4736         
                m "Well I suppo--"
                call her_main("Not done yet!","scream","angryCl") from _call_her_main_4737         
                m "Apologies."
                call her_main("Your penis is so big it almost scares me!","angry","down_raised") from _call_her_main_4738      
                g9 "You little mynx. You know exactly what to say..."
                call her_main("And yet I lust for it...","soft","ahegao") from _call_her_main_4739
                call her_main("Any woman would be happy to have your huge penis inside of her!") from _call_her_main_4740
                m "...you're good!"
                call her_main("There is more!","scream","angryCl") from _call_her_main_4741         
                m "By all means..."
                call her_main("I think your magnificent cock is a blessing to this world!","scream","angryCl") from _call_her_main_4742         
                m "Well, I wouldn't go that far--"
                call her_main("Listen to me, [genie_name]!","scream","angryCl") from _call_her_main_4743
                call her_main("I think a statue dedicated to your magnificent penis shall be erected in every city!") from _call_her_main_4744
                call her_main("So that people of the world could worship your phallus freely!") from _call_her_main_4745
                m "OK, I think I've heard enough."
                call her_main("Too much?","angry","wink") from _call_her_main_4746         
                m "Yeah, just a bit."
                call her_main("Sorry...","angry","worriedCl",emote="05") from _call_her_main_4747         
                m "No biggie. Just keep on stroking it."
                call her_main(".................","soft","ahegao") from _call_her_main_4748  
                call nar(">Hermione keeps on stroking your cock.","start") from _call_nar_533
                call nar(">She is doing a great job of it too.","end") from _call_nar_534 
                m "Yes, yes... Like that."
                
            "\"Call yourself a whore!\"":
                call her_main("Excuse me?","open","base") from _call_her_main_4749
                call her_main("Oh, that's right! I'm supposed to degrade myself, right?","annoyed","suspicious") from _call_her_main_4750  
                m "Well, you don't have to, but..."
                call her_main("That's alright, I don't mind.","upset","closed") from _call_her_main_4751
                call her_main("Alright then! I am a whore!","base","base") from _call_her_main_4752  
                m "Good. Glad we established that."
                m "Now I want you to say..."
                
                menu:
                    m "..."
                    "\"I am a worthless slut!\"":
                        call her_main("Of course.","angry","wink") from _call_her_main_4753
                        call her_main("I am a worthless slut.","soft","ahegao") from _call_her_main_4754
                        call her_main("A dirty little slut, that's what I am.") from _call_her_main_4755
                        m "Yes! Good!"
                    "\"I live to suck cock!\"":
                        call her_main("Em...","angry","wink") from _call_her_main_4756
                        call her_main("I live to suck penis, er... I mean cock...","base","base") from _call_her_main_4757  
                        m "Really? Well why don't you suck on this one then?"
                        call her_main("[genie_name], I am just repeating after you...","smile","angry") from _call_her_main_4758  
                        m "Really? Could've fooled me...."
                        call her_main("....................","angry","wink") from _call_her_main_4759
                        m ".................."
                    "\"I love to swallow cum!\"":
                        call her_main("I love to... ehm... swallow cum.","angry","wink") from _call_her_main_4760  
                        m "You hesitated there for a moment."
                        call her_main("Yes, I know....","angry","wink") from _call_her_main_4761
                        call her_main("Let me try again...") from _call_her_main_4762
                        call her_main("I love to swallow cum!","soft","ahegao") from _call_her_main_4763
                        call her_main("It is truly the best to swallow cum!") from _call_her_main_4764
                        call her_main("I love it!") from _call_her_main_4765
                        call her_main("...................................","grin","dead") from _call_her_main_4766
                        call her_main("How was that, [genie_name]?","angry","wink") from _call_her_main_4767  
                        m "Perfect." 
                        
            "\"This is really good. Did you practice?\"":
                call her_main("Hm?","base","happyCl") from _call_her_main_4768
                call her_main("Sort of... Well not really...") from _call_her_main_4769
                call her_main("I had a talk with the girls, and...","angry","wink") from _call_her_main_4770
                m "About handjobs?"
                call her_main("Among other things...","smile","happyCl",emote="06") from _call_her_main_4771    
                m "So those girls of yours, they know a lot about such things?"
                call her_main("Actually, yes. I was surprised myself.","shock","wide") from _call_her_main_4772
                call her_main("All sorts of weird sexual things seem to be happening lately in our school...","grin","baseL") from _call_her_main_4773
                call her_main("Can't say I approve of that...") from _call_her_main_4774
                call her_main("But they did teach me quite a few... tricks.","base","happyCl") from _call_her_main_4775    
                m "Really? Like what?"
                call her_main("Well, let's see...","base","down") from _call_her_main_4776
                call her_main("If I put one of my hands here...") from _call_her_main_4777
                call her_main("And another one here...") from _call_her_main_4778
                m "Oh, I see... Yes, this feels quite good."
                call her_main("Does it?","angry","wink") from _call_her_main_4779
                call her_main("So Ginny was right about this one...","grin","baseL") from _call_her_main_4780
                g4 "What did you just say?"
                call her_main("Ginny Weasley, she taught me this one.","base","happyCl") from _call_her_main_4781    
                m "Oh, right..."
                
                #if not handjob_practice_with_ginny:
                #    call nar(>Your curiosity about Ginny grows!)
                #$ handjob_practice_with_ginny = True
                
                call her_main("She said any boy would fall in love with me if I did this to him...","base","down") from _call_her_main_4782
                call her_main("There is also this thing when I form a ring with my fingers...") from _call_her_main_4783
                call her_main("And then I put one finger here...") from _call_her_main_4784
                m "Hm... I don't feel anything..."
                call her_main("Really?","angry","down_raised") from _call_her_main_4785
                call her_main("Hm...") from _call_her_main_4786
                call her_main("Oh! That's right!","base","down") from _call_her_main_4787
                call her_main("The finger goes here! Silly me!") from _call_her_main_4788
                with hpunch
                with kissiris
                g4 "Oh!!! By the great desert sands, yes!"
                call her_main("Really? That good?","smile","happyCl",emote="06") from _call_her_main_4789
                call her_main("What if I keep doing this but stick my finger here and press a little...","base","down") from _call_her_main_4790    
                g4 "[hermione_name], you are killing me!"
                call her_main("Really? Really?!","smile","happyCl",emote="06") from _call_her_main_4791
                call her_main("This is actually quite fun!") from _call_her_main_4792
                call her_main("Err... I mean...","angry","wink") from _call_her_main_4793
                call her_main("I am only doing this to help my house of course...") from _call_her_main_4794
                m "Yes, yes... The \"Gryffindor\" honour and all that."
                m "You just keep massaging that spot..."
                m "Oh, yes..."
                call her_main("...............","base","down") from _call_her_main_4795
                
        m "Yes... Keep stroking it."
        call her_main("..............","angry","wink") from _call_her_main_4796
        m "Now I want you to say..."
        
        menu:
            m "..."
            "{size=-4}\"I fantasize about being raped by my father.\"{/size}":
                $ mad += 11
                call her_main("I do not!","angry","angry") from _call_her_main_4797
                m "I know. Just say it."
                call her_main("My father? That's disgusting, [genie_name]!","angry","angry",emote="01") from _call_her_main_4798
                m "Humour me."
                call her_main("...........","annoyed","annoyed") from _call_her_main_4799
                call her_main("Well...","open","down") from _call_her_main_4800
                call her_main("Sometimes I fantasize about being raped...") from _call_her_main_4801
                call her_main(".......") from _call_her_main_4802
                m "I see. And in those fantasies of yours..."
                m "Who is doing the raping?"
                call her_main("My father...?","angry","base") from _call_her_main_4803
                m "Do you enjoy it?"
                call her_main("No. I cry and beg for him to stop!","angry","down_raised") from _call_her_main_4804
                m "Heh... Nice."
                call her_main(".......","angry","down_raised") from _call_her_main_4805
                m "Well, this wasn't that hard, was--"
                call her_main("I scream for my Mommy but she is still at work...","mad","worried",tears="soft") from _call_her_main_4806
                m "Huh?"
                call her_main("My daddy takes me to my room...","normal","worriedCl") from _call_her_main_4807
                call her_main("He throws me on my bed!") from _call_her_main_4808
                call her_main("I cry \"No, daddy, please, I'm still a virgin!\"","scream","worriedCl") from _call_her_main_4809
                call gen_chibi("handjob_pause") from _call_gen_chibi_81
                call her_main("But He doesn't listen! He rips my panties off!","grin","dead") from _call_her_main_4810
                call her_main("I beg him to stop! I scream and I scream!","angry","base",tears="soft") from _call_her_main_4811
                m "Uhm, [hermione_name]?"
                call her_main("Yes?","angry","base",tears="soft") from _call_her_main_4812
                m "You are not stroking my cock anymore..."
                call her_main("Oh, I am sorry, [genie_name].","grin","worriedCl",emote="05") from _call_her_main_4813
                call her_main("I got lost in thought...") from _call_her_main_4814
                call gen_chibi("handjob") from _call_gen_chibi_82
                call her_main("But everything I just said is not true of course!","open","base") from _call_her_main_4815
                call her_main("I never have fantasies like that!") from _call_her_main_4816
                m "Right."
                
            "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
                call her_main("What?!","angry","wide") from _call_her_main_4817
                call her_main("That's disgusting.","annoyed","suspicious") from _call_her_main_4818
                call her_main("Dogs carry {size=+5}STD{/size}s, [genie_name].","open","closed") from _call_her_main_4819
                m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
                m "Means that they can only be spread to the same species."
                call her_main("............","open","suspicious") from _call_her_main_4820
                m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
                call her_main("What does getting \"knotted\" mean?","normal","frown") from _call_her_main_4821
                m "Ehm... Well..."
                m "Ah, it doesn't matter."
                m "Just say the thing!"
                call her_main("Fine!","normal","base") from _call_her_main_4822
                call her_main("Sometimes I get lonely and let my dog mount me.","open","suspicious") from _call_her_main_4823
                m "That sounded so fake..."
                call her_main("Because we don't even own a dog!","normal","frown") from _call_her_main_4824
                m "Fine, whatever, let's just move on then..."
                
            "{size=-4}\"-Manual user input-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.

                $ tmp_name = renpy.input("(Use keyboard to enter the phrase.)")

                $ tmp_name = tmp_name.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if tmp_name == "":
                    $ tmp_name="I'm a whore."
                    call her_main("Hm...?","annoyed","worriedL") from _call_her_main_4825
                    call her_main("Should I just say \"I'm a whore\" as usual?") from _call_her_main_4826
                if one_out_of_three == 1:
                    call her_main("I don't want to say that...","annoyed","worriedL") from _call_her_main_4827
                    m "Oh, just do it, [hermione_name]."
                    call her_main("...........","annoyed","worriedL") from _call_her_main_4828
                    call her_main("[tmp_name]","scream","angryCl") from _call_her_main_4829
                    g9 "He-he..."
                elif one_out_of_three == 2:
                    call her_main("Huh?","annoyed","worriedL") from _call_her_main_4830
                    call her_main("What does That have to do with anything?") from _call_her_main_4831
                    m "Just say it."
                    call her_main("......","annoyed","worriedL") from _call_her_main_4832
                    m "Come on, humour me."
                    call her_main("[tmp_name]","scream","angryCl") from _call_her_main_4833
                    g9 "He-he..."
                elif one_out_of_three == 3:
                    call her_main("...........","annoyed","worriedL") from _call_her_main_4834
                    call her_main("Do I really have to?") from _call_her_main_4835
                    m "Just say it."
                    call her_main("[tmp_name]","scream","angryCl") from _call_her_main_4836
                    g9 "He-he..."
        
        #CUMMING
        m "Hm..."
        m "I love that thing you do with the palm of your hand!"
        call her_main("You noticed...?","angry","wink") from _call_her_main_4837
        call her_main("Shall I do it some more then?") from _call_her_main_4838
        call blkfade from _call_blkfade_155
        
        ">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(I think this is it! Should I give her a waring?){/size}"
        
        menu:
            m "..."
            "\"(Yes, I must warn her).\"":
                g4 "I think I'm about to--"
                if whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                ">Hermione swiftly pulls her shirt up..."
                ">She then pushes your already dribbling cock against her belly and covers it up again..."
                ">The sensation of her skin under your engorged cock almost makes you lightheaded..."
                ">Hermione placed your cock a bit higher than you would expect..."
                ">You can feel her incredibly soft tits rubbing against the tip of your cock..."
               
                call cum_block from _call_cum_block_51

                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                call play_music("chipper_doodle") from _call_play_music_180 # HERMIONE'S THEME.
                
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_970 
                
                call gen_chibi("cumming_under_shirt") from _call_gen_chibi_83
                hide screen blktone
                call hide_blkfade from _call_hide_blkfade_114
                call ctc from _call_ctc_274 
                        
                $ aftersperm = True
                
                g4 "Argh! You whore!"
                show screen blktone
                call her_main("Yes, [genie_name]! Just let it out!","base","down") from _call_her_main_4839       
                g4 "Argh! Fucking slut!"
                call her_main("Ah!! It's so hot!","smile","glance") from _call_her_main_4840
                call her_main("And it's getting everywhere! So much of it!","soft","ahegao") from _call_her_main_4841
                call her_main("...[genie_name].") from _call_her_main_4842
                g4 "Argh!!!"
                m "............"
                m "I think I am done..."
                call her_main("Ah, alright...","angry","wink") from _call_her_main_4843
                call her_main("..............","base","down") from _call_her_main_4844
                call her_main("You came so much this time, [genie_name]...","soft","ahegao") from _call_her_main_4845    
                call ctc from _call_ctc_275
                call blkfade from _call_blkfade_156
                
                ">Hermione releases your still pulsating cock."
                
                hide screen chair_left
                hide screen desk
                call her_chibi("stand","desk","base") from _call_her_chibi_154
                call gen_chibi("hide") from _call_gen_chibi_84
                show screen genie
                show screen bld1
                hide screen blkfade
                
                if daytime:
                    call her_main("Well, I think I'd better go now... my Classes are about to start.","base","base",xpos="right",ypos="base") from _call_her_main_4846
                else:
                    call her_main("Well, I think I'd better go now...  It's getting late.","base","base",xpos="right",ypos="base") from _call_her_main_4847 
                    
                m "Will you be alright in those clothes?"
                call her_main("What?","open","down") from _call_her_main_4848
                call her_main("Oh. Yes, I will be fine...","grin","baseL") from _call_her_main_4849
                call her_main("It may soak through a little here and there, but I doubt that anyone will notice.","base","happyCl") from _call_her_main_4850    
                m "Hm... You could just put it in your mouth next time, and avoid the trouble..."
                call her_main("And swallow your hot spunk like that, [genie_name]?","angry","wink") from _call_her_main_4851    
                m "Would keep your clothes clean."
                
                if whoring <= 15:
                    call her_main("With all due respect [genie_name]...","upset","closed") from _call_her_main_4852
                    call her_main("Not for the meagre 45 points...","angry","wink") from _call_her_main_4853
                    call her_main("Speaking of which. Can I get may payment now please?") from _call_her_main_4854
                else:
                    call her_main("Maybe next time...","angry","wink") from _call_her_main_4855
                    call her_main("Can I get may payment now please?","angry","wink") from _call_her_main_4856   

            "\"(Nah... no need).\"":
                g4 "Here! Take this, whore!"
                if whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                with hpunch
                g4 "ARGH!"
                call blkfade from _call_blkfade_157
                
                call her_head("WHAT?!","shock","wide") from _call_her_head_971               
                g4 "Take this!"

                call cum_block from _call_cum_block_52
                
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_972 
                
                call gen_chibi("cumming_under_shirt") from _call_gen_chibi_85

                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_115
                call ctc from _call_ctc_276
                
                $ aftersperm = True
                call her_head(".......................","angry","wide") from _call_her_head_973  
                call gen_chibi("cumming_on_shirt_pause") from _call_gen_chibi_86        
                m "Yes... I Feel so much better now..."
                call ctc from _call_ctc_277
                
                hide screen hermione_main
                with d3
                
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True
                
                show screen bld1
                call her_main("","soft","base",tears="soft",xpos="right",ypos="base") from _call_her_main_4857
                call ctc from _call_ctc_278
                her ".........."
                m "Well, I think that's about it..."
                call blkfade from _call_blkfade_158
                
                call her_chibi("stand","desk","base") from _call_her_chibi_155
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide") from _call_gen_chibi_87
                show screen genie
                call play_music("chipper_doodle") from _call_play_music_181 # HERMIONE'S THEME.
                
                hide screen blkfade
                call her_main("[genie_name]! What have you done?","scream","worriedCl") from _call_her_main_4858
                
                m "What?"
                call her_main("You came all over me, [genie_name]...","scream","worriedCl") from _call_her_main_4859
                call her_main("What a mess...","angry","down_raised") from _call_her_main_4860
                call her_main("[genie_name], you should have warned me.","upset","closed") from _call_her_main_4861
                m "It's your fault, [hermione_name]!"
                call her_main("My fault?","angry","base") from _call_her_main_4862
                m "Yes! You got me going too well..."
                m "I forgot about everything else..."     
                call her_main("Oh...","angry","wink") from _call_her_main_4863
                her "Well, what's done is done..."
                call her_main("I will just wipe it off and hope that nobody will notice...","grin","dead") from _call_her_main_4864
                call her_main("Can I get my payment now?","angry","wink") from _call_her_main_4865
    
    label done_with_handjob:

    call blkfade from _call_blkfade_159

    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    call h_action("none") from _call_h_action_75 #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01  
    hide screen groping_01
    hide screen groping_02
    hide screen groping_naked_tits

    call her_chibi("stand","desk","base") from _call_her_chibi_156

    hide screen chair_left
    show screen genie 
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main(trans="fade",xpos="right",ypos="base") from _call_her_main_4866
    
    m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"." 
    $ gryffindor +=current_payout
    
    call her_main("Thank you, [genie_name]...","soft","baseL") from _call_her_main_4867
    
    $ hg_pf_TouchMe_OBJ.points += 1
    
    if whoring < 15:
        $ whoring +=1
    
    if whoring >= 12 and whoring < 15:
        $ new_request_16_heart = 1
        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

    if whoring >= 15 and whoring < 18:
        $ new_request_16_heart = 2
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)
    
    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2
    
    call her_walk("desk","leave",2.5) from _call_her_walk_107

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    if daytime:
        call play_music("day_theme") from _call_play_music_182
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme") from _call_play_music_183
        $ hermione_sleeping = True
        jump night_main_menu     
    

label hg_pf_TouchMe_KissSuck: #Jumps here after event #03 and if WHORING >= LEVEL 07 ### KISS SUCK! ###
    ">Hermione swiftly puts the tip of your cock on her lips, as if to give it a kiss..."
    ">The simple gesture makes your dick practically explode with pleasure and waves of cum."
    
    call cum_block from _call_cum_block_53
    
    g4 "{size=+5}ARGH! YES!!!{/size}"
    call gen_chibi("handjob_kiss","desk","base") from _call_gen_chibi_88
    
    hide screen hermione_main
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_116
    call ctc from _call_ctc_279
    
    call bld from _call_bld_102
    call her_head("*Gulp!-Gulp!-Gulp!*") from _call_her_head_974
    g4 "Argh! You little whore!"
    g4 "Yes, you slut! Drink my cum! Drink all of it!"
    her "*Gulp!-Gulp!-Gulp!*"
    g4 "Argh... Yes!"
    call nar(">You notice that Hermione is barely able to keep up with the amount of hot cum your cock is pumping into her mouth.") from _call_nar_535
    her "*Gulp!-Gulp!-Gulp!*"
    g4 "Ah..."
    g4 "This feels great..."
    her "*Gulp!* *Gulp!* *Gulp!*"
    m "I think that's it, [hermione_name]..."
    m "You can let go now..."
    call blkfade from _call_blkfade_160
    
    hide screen chair_left
    hide screen desk
    call her_chibi("stand","desk","base") from _call_her_chibi_157
    call gen_chibi("hide") from _call_gen_chibi_89
    show screen genie
    with d3
    
    call her_main("","full_cum","dead",xpos="mid",xpos="base") from _call_her_main_4868
    call ctc from _call_ctc_280
    her "........................................."
    call her_main("GULP!!!","cum","worriedCl") from _call_her_main_4869
    call her_main("Gu-ah-a...","open_wide_tongue","down_raised") from _call_her_main_4870
    
    hide screen blkfade
    call her_main(trans="fade",xpos="right",xpos="base") from _call_her_main_4871
    pause.5
    
    show screen bld1
    call her_main("I swallowed it all, [genie_name]!","grin","dead") from _call_her_main_4872
    m "Good girl..."
    call her_main("At one point I thought I was going to choke...","grin","dead") from _call_her_main_4873
    her "There was so much of it..."
    m "Well, the deed is done, and your uniform is perfectly clean."
    call her_main("Yes! I know! It's So much easier this way!","base","down") from _call_her_main_4874
    
    if daytime:
        call her_main("I can just go to classes now as if nothing ever happened.","angry","wink") from _call_her_main_4875
    else:
        call her_main("I can just go and spend some time with the guys in the common room now and nobody will know...","base","down") from _call_her_main_4876
        
    m "Yes... With your belly full of semen..."
    call her_main("[genie_name]!","angry","base") from _call_her_main_4877
    her "...Can I just get paid now, please, [genie_name]?"
    
    jump done_with_handjob
    













