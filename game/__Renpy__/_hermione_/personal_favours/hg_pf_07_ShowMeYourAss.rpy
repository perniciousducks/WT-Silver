

label hg_pf_ShowMeYourAss: #LV.3 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_ShowMeYourAss_OBJ.points == 0:
        m "{size=-4}(I feel like checking out that ass.){/size}"
    else:
        m "{size=-4}(I feel like checking out that ass again.){/size}"

    if hg_pf_ShowMeYourAss_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    $ current_payout = 50 #Used when haggling about price of th favor.
    
    if hg_pf_ShowMeYourAss_OBJ.points == 0 and whoring < 15: # LEVEL 04 # FIRST TIME.
        
        call bld from _call_bld_57
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]...","normal","base") from _call_her_main_1848
        m "How much will it cost for you to get naked and show me that perfect ass of yours?"
        stop music fadeout 1.0
        if whoring < 9:
            call her_main("Get naked and show you my...?","angry","shocked") from _call_her_main_1849
            jump too_much
        else:
            $ current_payout = 50 #Used when haggling about price of the favor.
            call her_main("Get naked and show you my...?","open","base") from _call_her_main_1850

        call play_music("chipper_doodle") from _call_play_music_90 # HERMIONE'S THEME.
        call her_main("[genie_name]!","scream","angryCl") from _call_her_main_1851
        m "Come on..."
        m "It's not like I haven't seen it all before."
        call her_main("......","open","base") from _call_her_main_1852
        call her_main(".............","annoyed","worriedL") from _call_her_main_1853
        call her_main("50 house points, [genie_name].","normal","worriedCl") from _call_her_main_1854
        m "So if I give you 50 house points, [hermione_name]..."
        m "You will shamelessly strip naked and present your lovely ass?"
        call her_main("[genie_name]! There's no reason to be so detestable!","angry","angry") from _call_her_main_1855
        her "I think I want 70 points now..."

        menu:
            "\"Fine. 70 points are yours. Show me!\"":
                $ current_payout = 70 #Used when haggling about price of th favor.
                call her_main("Really?","open","base") from _call_her_main_1856
                m "Well?"
                call her_main("...","annoyed","worriedL") from _call_her_main_1857
                her "You have to promise me not to touch, [genie_name]..."
                m "Sure, sure..."
                call her_main("And you most certainly must not touch yourself!","scream","worriedCl") from _call_her_main_1858

            "\"I will give you 50 points to see your ass.\"":
                call her_main("Fifty?","annoyed","frown") from _call_her_main_1859
                call her_main("Well alright then...","annoyed","angryL") from _call_her_main_1860
                call her_main("but if you expect to touch me it'll cost you extra...","annoyed","down") from _call_her_main_1861
                call her_main("at least one hundred points","annoyed","angryL") from _call_her_main_1862

                menu:
                    "\"Fine. 100 it is! strip already!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        call her_main("(I didn't think he'd agree to this...)","annoyed","worriedL") from _call_her_main_1863
                        call her_main("W-Well alright then...","normal","worriedCl") from _call_her_main_1864
                    "\"50 house points it is then\"":
                        her "Well, so be it."
                        call her_main("but you better keep your hands you yourself...","annoyed","angryL") from _call_her_main_1865

            "\"Fine, leave. I don't care...\"":
                $ mad = +12
                her "Tsk!"
                call music_block from _call_music_block_6
                jump could_not_flirt
                
                
        m "Alright, alright..."
        g9 "Just get naked already!"

        hide screen bld1
        show screen blktone
        call her_main("...","annoyed","annoyed",xpos="mid",ypos="base") from _call_her_main_1866

        #Remove Top Animation
        call set_hermione_action("lift_top") from _call_set_hermione_action_46
        pause.5
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_47
        pause.2

        call her_main("{size=-5}(I can't believe I'm going to strip for him...){/size}","disgust","down_raised",cheeks="blush") from _call_her_main_1867
        m "That's it [hermione_name], now your skirt..."
        call her_main("............","annoyed","angryL",cheeks="blush") from _call_her_main_1868

        #Remove Skirt Animation
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_48
        pause.5
        call h_action("naked") from _call_h_action_7 #Removes all clothing.
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_49
        pause.2
        call ctc from _call_ctc_111

        call her_main("............","soft","baseL",cheeks="blush") from _call_her_main_1869
        m "Very nice..."
        call her_main(".....","annoyed","angryL",cheeks="blush") from _call_her_main_1870
        m "Now turn around..."
        call blkfade from _call_blkfade_72
        
        call her_main("","annoyed","annoyed") from _call_her_main_1871
        call ctc from _call_ctc_112
        her "...................................."
        call her_chibi("stand","mid","base",flip=True) from _call_her_chibi_74

        hide screen hermione_main
        with d3
        show screen hermione_ass
        with d3
        call ctc from _call_ctc_113

        call hide_blkfade from _call_hide_blkfade_34
        

    #Second and Third Event
    else: #Whoring 12+ or whoring (9+ and .points > 1)
        
        show screen bld1
        call her_main(xpos="right",ypos="base") from _call_her_main_1872
        pause.5
        
        if whoring < 12:
            m "[hermione_name]?"
            call her_main("Yes, [genie_name]?","annoyed","angryL") from _call_her_main_1873
        m "I need to see your ass, [hermione_name]."

        if whoring < 12:
            call her_main("............","annoyed","angryL",cheeks="blush") from _call_her_main_1874
            call her_main("Do you promise not to touch, [genie_name]?","annoyed","angryL",cheeks="blush") from _call_her_main_1875
            m "Of course."
        elif whoring < 15:
            call her_main("Are you only going to watch, [genie_name]?","angry","worriedCl",cheeks="blush") from _call_her_main_1876
            m "Of course..."
        else:
            call her_main("anything for you [genie_name]","base","ahegao_raised",cheeks="blush") from _call_her_main_1877
        call ctc from _call_ctc_114


        #Remove Top Animation
        call set_hermione_action("lift_top") from _call_set_hermione_action_50
        pause.5
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_51
        pause.2


        m "Hm..."
        m "That's it [hermione_name], now the skirt..."
            

        #Remove Skirt Animation
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_52
        pause.5
        call h_action("naked") from _call_h_action_8 #Removes all clothing.
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_53
        pause.2
        call ctc from _call_ctc_115


        m "Very nice..."

        if whoring < 15:
            call her_main(".....","annoyed","angryL",cheeks="blush") from _call_her_main_1878
        else:
            call her_main("............","soft","baseL",cheeks="blush") from _call_her_main_1879

        m "Now turn around..."
        call blkfade from _call_blkfade_73
        
        call her_main("","","") from _call_her_main_1880
        pause.5

        call her_chibi("stand","mid","base",flip=True) from _call_her_chibi_75
        hide screen hermione_main
        with d3
        show screen hermione_ass
        with d3
        call ctc from _call_ctc_116

        show screen blktone
        call hide_blkfade from _call_hide_blkfade_35

        if whoring < 15:
            call her_head("....................................","annoyed","annoyed") from _call_her_head_464
        else:
            call her_head("....................................","base","closed") from _call_her_head_465
            call play_music("playful_tension") from _call_play_music_91# SEX THEME.
        call ctc from _call_ctc_117


    menu:
        "\"Grab her ass!\"":

            hide screen hermione_ass
            call blkfade from _call_blkfade_74
            
            ">You walk over to Hermione, reach out and dig your fingers into the girl's soft flesh..."
            call her_head("[genie_name], what are you doing?","mad","wide",cheeks="blush") from _call_her_head_466

            hide screen genie
            hide screen desk
            show screen chair_left
            show screen desk
            call gen_chibi("groping","mid","base") from _call_gen_chibi_33
            hide screen blktone
            call hide_blkfade from _call_hide_blkfade_36
            call ctc from _call_ctc_118

            m "Relax, [hermione_name]. Just stand still!"

            show screen blktone
            show screen hermione_ass
            with fade
            call ctc from _call_ctc_119

            #FIRST EVENT. HERMIONE OUTRAGED.
            if whoring < 12 and current_payout < 100:

                m "Oh... This is a nice ass you've got here..."
                call play_music("chipper_doodle") from _call_play_music_92 # HERMIONE'S THEME.
                call her_head("No, [genie_name], please! You mustn't do this...","shock","worriedCl") from _call_her_head_467
                m "This won't take long, just stand still and look forward."
                call her_head("[genie_name], I didn't agree to this!","angry","angry",cheeks="blush") from _call_her_head_468
                with hpunch
                call her_head("You must let go of me now!!!","scream","angry",cheeks="blush",emote="01") from _call_her_head_469
                call blkfade from _call_blkfade_75
                
                ">Hermione pulls away from you and covers up hastily."

                call h_action("none") from _call_h_action_9

                call her_head("I think I'd better go...","angry","worriedCl",cheeks="blush") from _call_her_head_470
                hide screen chair_left #Genie's chair.
                hide screen desk
                call gen_chibi("hide") from _call_gen_chibi_34
                call her_chibi("stand","mid","base") from _call_her_chibi_76
                show screen genie
                hide screen hermione_ass
                hide screen blktone
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_37
                call ctc from _call_ctc_120

                call bld from _call_bld_58
                m "Go ahead, [hermione_name]. You've earned your points.'"
                call her_main("Hmmmph...","angry","worriedCl",cheeks="blush",xpos="right",ypos="base") from _call_her_main_1881
                call her_main("You'd have gotten a better look if you could just keep your hands to yourself...","angry","angry",cheeks="blush") from _call_her_main_1882
                m "That will be all [hermione_name]..."
                call her_main("......","angry","worriedCl",cheeks="blush") from _call_her_main_1883
                call her_main("{size=-5}(I guess letting him grab me isn't too bad...{/size}","angry","worriedCl",cheeks="blush") from _call_her_main_1884

                $ mad += 7

            #SECOND EVENT. A BIT ANGRY.
            elif whoring < 15:

                if current_payout < 100:
                    $ mad += 3
                    call her_head("I didn't agree to this, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_471
                else:
                    call her_head("I know I agreed to this [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_472
                    call her_head("But as the headmaster of this school...","annoyed","angryL",cheeks="blush") from _call_her_head_473
                call her_head("I don't know if you should be...","annoyed","angryL",cheeks="blush") from _call_her_head_474
                m "Don't you like it...?"
                call her_head("What?","disgust","down_raised",cheeks="blush") from _call_her_head_475
                m "Don't you like it how I squeeze and pull your cheeks?"
                call her_head("...............","disgust","down_raised",cheeks="blush") from _call_her_head_476
                m "Admit it, you like it a little bit..."
                m "Maybe even a lot..."
                call her_head("{size=-5}(It feels so weird to let him grope me...){/size}","disgust","down_raised",cheeks="blush") from _call_her_head_477
                call her_head("[genie_name], I am letting you do this to me to help my house!","shock","worriedCl") from _call_her_head_478
                call her_head("It doesn't matter how good it feels...","shock","worriedCl") from _call_her_head_479
                m "So you admit that it does feel good."
                call play_music("chipper_doodle") from _call_play_music_93 # HERMIONE'S THEME.
                call her_head("Please, let go of me now!","annoyed","angryL",cheeks="blush") from _call_her_head_480
                call blkfade from _call_blkfade_76
                
                ">Hermione pulls away from you suddenly and covers up."

                call h_action("none") from _call_h_action_10

                if current_payout < 100:
                    call her_head("You promised not to grab me, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_481
                    m "It was hard to resist..."
                else:
                    call her_head("Even though I agreed to let you grab me, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_482
                    call her_head("you didn't need to be so rough...","annoyed","angryL",cheeks="blush") from _call_her_head_483
                    m "sorry, It was hard to resist..."
                    call her_head("..........","base","closed") from _call_her_head_484

                hide screen chair_left #Genie's chair.
                hide screen desk
                call gen_chibi("hide") from _call_gen_chibi_35
                call her_chibi("stand","mid","base") from _call_her_chibi_77
                show screen genie
                hide screen hermione_ass
                hide screen blktone
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_38
                call ctc from _call_ctc_121

                show screen bld1
                if current_payout < 100:
                    call her_main("well if you wanted to touch you should have offered to pay me more.","soft","baseL",cheeks="blush",xpos="right",ypos="base") from _call_her_main_1885
                    call her_main("speaking of which Can I get paid now please?","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_1886
                else:
                    call her_main("I'd like to get paid now please [genie_name].","angry","worriedCl",cheeks="blush",emote="05",xpos="right",ypos="base") from _call_her_main_1887
                m "Sure..."

            #THIRD EVENT. ENJOYS A LITTLE.
            elif whoring >= 15:

                call her_head("But...","disgust","down_raised",cheeks="blush") from _call_her_head_485
                call her_head("ah...{image=textheart}","shock","worriedCl") from _call_her_head_486

                if current_payout < 100:
                    call her_head("I didn't agree to this...","disgust","down_raised",cheeks="blush") from _call_her_head_487
                else:
                    call her_head("please [genie_name], not so rough...{image=textheart}","shock","worriedCl") from _call_her_head_488

                m "But you like it, don't you?"

                if whoring >= 18:
                    call her_head("I love it [genie_name]!{image=textheart}","open","baseL",cheeks="blush") from _call_her_head_489
                else:
                    call her_head("maybe... [genie_name]{image=textheart}","shock","worriedCl") from _call_her_head_490

                call nar(">You give her cheeks a couple of firm squeezes...") from _call_nar_208
                
                if whoring >= 18 or current_payout == 100:
                    if current_payout < 100:
                        call her_head("[genie_name], you promised not to touch...","base","baseL",cheeks="blush") from _call_her_head_491
                        m "I know, I know... but admit it, you wanted me to..."
                        call her_head(".................{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised",cheeks="blush") from _call_her_head_492
                    else:
                        call her_head("[genie_name], please...{image=textheart}","base","baseL",cheeks="blush") from _call_her_head_493
                else:
                    call her_head("[genie_name], you promised not to touch...","angry","worriedCl",cheeks="blush") from _call_her_head_494
                    m "I know, I know... but admit it, you wanted me to..."
                    call her_head("ah{image=textheart}... of course not [genie_name]{image=textheart}","angry","angry",cheeks="blush") from _call_her_head_495

                call her_head("mmmm.......................{image=textheart}","base","ahegao_raised",cheeks="blush") from _call_her_head_496
                call her_head("[genie_name], you need to stop now...","base","ahegao_raised",cheeks="blush") from _call_her_head_497
                m "Just a bit longer..."
                
                call nar(">You keep on groping her ass cheeks...") from _call_nar_209
                
                call her_head("[genie_name]... please, stop this...","open","ahegao_raised",cheeks="blush") from _call_her_head_498
                m "Why? Because you like it too much?"
                call her_head("No it's not that...","base","baseL",cheeks="blush") from _call_her_head_499
                call her_head("I mean...","open","baseL",cheeks="blush") from _call_her_head_500
                
                call nar(">You pull the cheeks apart in opposite directions and then squish them together...") from _call_nar_210
                
                call her_head("Ah...{image=textheart} [genie_name], I really need to go... before I-","base","ahegao_raised",cheeks="blush") from _call_her_head_501

                if daytime:
                    call her_head("am late for class... they're about to start...","open","baseL",cheeks="blush") from _call_her_head_502
                else:
                    call her_head("am late to bed... It is getting very... late...","open","baseL",cheeks="blush") from _call_her_head_503

                m "Well, alright..."
                call blkfade from _call_blkfade_77
                
                ">You let go of the girl's ass..."
                ">Hermione covers up..."

                call h_action("none") from _call_h_action_11

                call play_music("chipper_doodle") from _call_play_music_94 # HERMIONE'S THEME.

                if current_payout < 100:
                    if whoring >= 18:
                        call her_head("Please don't think I forgot that you broke your promise, [genie_name].","base","baseL",cheeks="blush") from _call_her_head_504
                        call her_head("I expect you to make it up to me later...","base","baseL",cheeks="blush") from _call_her_head_505
                    else:
                        call her_head("Please don't think I forgot that you broke your promise, [genie_name].","annoyed","angryL",cheeks="blush") from _call_her_head_506
                    m "Right..."
                
            call ctc from _call_ctc_122

            hide screen hermione_main
            call blkfade from _call_blkfade_78
   
        "\"Keep your hands to yourself, Just look.\"":

            call nar(">You take a long look at Hermione's naked ass...") from _call_nar_211
            call ctc from _call_ctc_123

            #First Event
            if whoring >= 9 and whoring < 15:

                menu:
                    "-\"You have a fantastic ass girl\"-":
                        m "you should start wearing shorter skirts to show it off a little..."
                        call her_head(".....................","base","closed") from _call_her_head_507
                    "-\"You're ass is alright...\"-":
                        ">You Look at her ass some more whilst making some disapproving tuts..."
                        call her_head(".....................","annoyed","frown") from _call_her_head_508
                        $ mad +=3

            #Second Event
            elif whoring >= 15 and whoring < 18:
                
                menu:
                    "\"Nice little ass you got there.\"":
                        call her_head("","annoyed","closed") from _call_her_head_509
                        call ctc from _call_ctc_124
                        call her_head("Thank you [genie_name].","base","closed") from _call_her_head_510 
                        call play_music("chipper_doodle") from _call_play_music_95 # HERMIONE'S THEME.
                        call her_head("(Maybe he should grab it next time...)","annoyed","annoyed") from _call_her_head_511
                        
                    "\"Hm... I've seen better.\"":
                        $ mad += 9
                        her "Tsk..."
                        her "well in that case Are we done?"

            #Third Event
            elif whoring >= 18:
                
                menu:
                    "\"You have an amazing ass, [hermione_name].\"":
                        call her_head("You really think so [genie_name]?","annoyed","base") from _call_her_head_512
                        call her_head("I am glad you like it, [genie_name]...","base","closed") from _call_her_head_513
                    "\"Your ass is ok... I suppose...\"":
                        call her_head("Huh?","annoyed","base") from _call_her_head_514
                        call her_head("Does this mean you don't like it, [genie_name]?","annoyed","base") from _call_her_head_515
                        call her_head("I'm sorry... I'll try to work out some more.","disgust","down_raised") from _call_her_head_516


            call nar(">You stare at her ass for a while longer...") from _call_nar_212
            call ctc from _call_ctc_125

            m "Alright, you can get dressed now [hermione_name]..."

            if whoring < 15 or mad > 1:
                call her_head(".............","annoyed","base") from _call_her_head_517
            else:
                call her_head(".............","base","closed") from _call_her_head_518

            call ctc from _call_ctc_126

            hide screen hermione_main
            call blkfade from _call_blkfade_79



        "\"Start jerking off.\"":

            hide screen hermione_ass
            call blkfade from _call_blkfade_80
            
            ">You take your cock out and start stroking it..."

            hide screen chair_left #Genie's chair.
            show screen chair_left #Genie's chair.
            hide screen desk
            show screen desk
            call gen_chibi("jerking_off","mid","base") from _call_gen_chibi_36
            hide screen bld1
            hide screen blktone
            call hide_blkfade from _call_hide_blkfade_39
            call play_music("chipper_doodle") from _call_play_music_96
            call ctc from _call_ctc_127

            #First Event.
            if whoring >= 9 and whoring < 15:
                $ mad += 2

                show screen blktone
                show screen hermione_ass
                call her_head("Are you enjoying the view [genie_name]","angry","wide") from _call_her_head_519
                m "yes I am [hermione_name]. just stand still and let me look a little longer..."
                
                call nar(">You stare at Hermione's ass with hunger...") from _call_nar_213
                call her_head("[genie_name], how much longer do I have to stand here?","shock","worriedCl") from _call_her_head_520
                call nar(">You keep stroking your hard cock...") from _call_nar_214
                m "Not too much longer now..."
                call her_head("[genie_name]...","disgust","down_raised",cheeks="blush") from _call_her_head_521
                call her_head("You're not... touching yourself are you...?","disgust","down_raised",cheeks="blush") from _call_her_head_522
                m "ah... of course not [hermione_name]. you know I'd never do... such a thing..."
                call her_head("hmmm.....","angry","worriedCl",cheeks="blush") from _call_her_head_523
                call her_head("well if you did do such a thing...","angry","angry",cheeks="blush") from _call_her_head_524
                call her_head("I'd hope that you would make the right decision...'","angry","worriedCl",cheeks="blush") from _call_her_head_525
                call her_head("and not... {size=-5}cum...{/size} on me...","angry","worriedCl",cheeks="blush") from _call_her_head_526

                menu:
                    "\"Of course not\"":
                        call her_head("good.","scream","wide",cheeks="blush") from _call_her_head_527
                        call her_head("I mean seeing as how I stripped naked and showed you my...","scream","wide",cheeks="blush") from _call_her_head_528
                        call her_head("..........","annoyed","angryL",cheeks="blush") from _call_her_head_529
                        call her_head("not {size=-5}cumming{/size} on me is the least you could do...","angry","angry",cheeks="blush") from _call_her_head_530

                        call nar(">Hermione starts looking at you from the corner of her eye ...") from _call_nar_215

                        call her_head("Are you ready to...","angry","suspicious",cheeks="blush") from _call_her_head_531
                        g4 "Almost there [hermione_name]!"
                        call her_head("Do it, [genie_name]... cum for me...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_head_532

                    "-Start jerking your cock faster-":
                        call nar(">You start jerking your cock furiously!") from _call_nar_216
                        call her_head("...","scream","angry",cheeks="blush",emote="01") from _call_her_head_533
                        call nar(">You jerk it even faster!") from _call_nar_217
                        call her_head("you're going to do it aren't you...","annoyed","angryL",cheeks="blush") from _call_her_head_534
                        g4 "almost there slut!"
                        call her_head("make me stand here...","angry","suspicious",cheeks="blush") from _call_her_head_535
                        call her_head("while you cum all over me!","angry","suspicious",cheeks="blush") from _call_her_head_536

            #Second Event.
            elif whoring >= 15 and whoring < 18:

                show screen blktone
                show screen hermione_ass
                call her_head("Are you enjoying the view [genie_name]","angry","wide") from _call_her_head_537
                m "I'm enjoying it immensely"
                call her_head("[genie_name], are you... touching yourself...","shock","worriedCl") from _call_her_head_538
                m "Don't blame me [hermione_name]..."
                call her_head("well who am I supposed to blame, [genie_name]?","shock","worriedCl") from _call_her_head_539
                call nar(">You pick up the pace...") from _call_nar_218
                m "Blame yourself [hermione_name]..."
                m "Or rather, blame that perfect little ass of yours!"
                call her_head("..................","shock","worriedCl") from _call_her_head_540
                call her_head("(his cock is so big...)","disgust","down_raised",cheeks="blush") from _call_her_head_541
                m "Yes... Yes, like that..."
                m "Try shaking it a little..."
                call her_head("..............","disgust","down_raised",cheeks="blush") from _call_her_head_542
                call her_head("Well, so be it...","open","baseL",cheeks="blush") from _call_her_head_543
                call her_head("You can keep touching yourself, [genie_name]...","open","baseL",cheeks="blush") from _call_her_head_544
                call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_545
                call her_head("Not to... em...","open","baseL",cheeks="blush") from _call_her_head_546
                call her_head("Not to cum...","annoyed","angryL",cheeks="blush") from _call_her_head_547
                call her_head("Not on me, [genie_name]...","angry","angry") from _call_her_head_548
                m "Are you sure..."
                m "I bet you'd love to have your ass covered in my cum, wouldn't you!"
                call her_head(".......................","angry","worriedCl",cheeks="blush") from _call_her_head_549
                call nar(">You start to stroke your cock even harder...") from _call_nar_219
                g4 "Yes, I know you want this! Yes!"
                call her_head("................","angry","worriedCl",cheeks="blush") from _call_her_head_550

                call nar(">You are about to cum...") from _call_nar_220

            #Third Event.
            elif whoring >= 18:

                show screen blktone
                show screen hermione_ass
                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush") from _call_her_head_551

                if whoring >= 21:
                    call her_head("ah...","base","ahegao_raised",cheeks="blush") from _call_her_head_552
                    call nar(">Hermione looks back and sees you stroking your cock.") from _call_nar_221
                    call her_head("It's so big...","open","baseL",cheeks="blush") from _call_her_head_553
                    call her_head("You just couldn't help yourself, could you [genie_name]?","base","baseL",cheeks="blush") from _call_her_head_554
                    call her_head("..................","base","ahegao_raised",cheeks="blush") from _call_her_head_555
                    m "Yes... Yes, like that..."
                    m "Yes, shake that ass [hermione_name]..."
                    call her_head("..............","base","ahegao_raised",cheeks="blush") from _call_her_head_556
                    call her_head("well, so be it...","open","baseL",cheeks="blush") from _call_her_head_557
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_558
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") from _call_her_head_559
                    call her_head("Not to cum... on me, [genie_name]...","base","ahegao_raised",cheeks="blush") from _call_her_head_560
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","base","ahegao_raised",cheeks="blush") from _call_her_head_561
                    ">You start to stroke your cock even harder..."
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","base","ahegao_raised",cheeks="blush") from _call_her_head_562
                    
                else:
                    call her_head("[genie_name], actually I never agreed to this...","shock","worriedCl") from _call_her_head_563
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching your ass..."
                    call her_head("Yes, but you are... touching yourself, [genie_name].","shock","worriedCl") from _call_her_head_564
                    m "Just stand still, you fat assed bitch."
                    m "It will be over soon."
                    call her_head("..................","shock","worriedCl") from _call_her_head_565
                    m "Yes... Yes, like that..."
                    m "Yes, with your ass all naked..."
                    call her_head("..............","disgust","down_raised",cheeks="blush") from _call_her_head_566
                    call her_head("well, so be it...","open","baseL",cheeks="blush") from _call_her_head_567
                    call her_head("But you must promise me not to...","soft","baseL",cheeks="blush") from _call_her_head_568
                    call her_head("Not to... ehm...","open","baseL",cheeks="blush") from _call_her_head_569
                    call her_head("Not to discharge...","annoyed","angryL",cheeks="blush") from _call_her_head_570
                    call her_head("Not on me, [genie_name]...","annoyed","angryL",cheeks="blush") from _call_her_head_571
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    call her_head(".......................","disgust","down_raised",cheeks="blush") from _call_her_head_572
                    call nar(">You start to stroke your cock even harder...") from _call_nar_222
                    g4 "Yes, I know you want this! Yes!"
                    call her_head("................","disgust","down_raised",cheeks="blush") from _call_her_head_573


            ### GENIE STARTS CUMMING ###

            #First and second event.
            if whoring < 18:
                menu:
                    "-Cum on the floor-":

                        hide screen blktone
                        call blkfade from _call_blkfade_81

                        g4 "Argh! You fat assed slut!"
                        call her_head("Proff-- ??","scream","wide",cheeks="blush") from _call_her_head_574

                        call cum_block from _call_cum_block_27

                        g4 "Argh! YES!"
                        
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        call hide_blkfade from _call_hide_blkfade_40
                        call ctc from _call_ctc_128

                        show screen bld1
                        call her_head("[genie_name]!","scream","angry",cheeks="blush",emote="01") from _call_her_head_575
                        g4 "Oh, that's better..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3

                        call her_head("[genie_name], you came so much...","angry","suspicious",cheeks="blush") from _call_her_head_576

                        hide screen hermione_ass
                        call gen_chibi("stand","desk","base") from _call_gen_chibi_37
                        call her_chibi("stand","mid","base") from _call_her_chibi_78
                        hide screen bld1
                        hide screen blktone
                        with fade
                        call ctc from _call_ctc_129

                        call bld from _call_bld_59
                        m "Oh, this was quite amazing..."

                        call her_main("","disgust","down_raised",xpos="right",ypos="base") from _call_her_main_1888
                        pause.5

                        her "the floor..."
                        her "It's covered...."
                        m "all because of your ass, [hermione_name]."
                        her "................"
                        call her_main("I need to get dressed...","open","closed") from _call_her_main_1889
                        call ctc from _call_ctc_130

                        hide screen hermione_main
                        call blkfade from _call_blkfade_82

                    "-cum on her ass-":

                        hide screen blktone
                        call blkfade from _call_blkfade_83

                        g4 "Argh! You fat assed whore!"
                        call her_head("Proff-- ??","scream","wide",cheeks="blush") from _call_her_head_577
                        call cum_block from _call_cum_block_28

                        g4 "Argh! YES!"

                        hide screen bld1
                        call gen_chibi("cumming","on_girl","base") from _call_gen_chibi_38
                        hide screen bld1
                        call hide_blkfade from _call_hide_blkfade_41
                        call ctc from _call_ctc_131

                        show screen bld1
                        with d3
                        $ hermione_ass_cum = True
                        call her_head("[genie_name], no, you promised!","scream","angry",cheeks="blush",emote="01") from _call_her_head_578
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        call ctc from _call_ctc_132

                        
                        hide screen hermione_ass
                        call gen_chibi("stand","desk","base") from _call_gen_chibi_39
                        call her_chibi("stand","mid","base") from _call_her_chibi_79
                        hide screen bld1
                        hide screen blktone
                        with fade
                        call ctc from _call_ctc_133

                        call bld from _call_bld_60
                        m "Oh, this was quite amazing..."
                        call her_main("","disgust","down_raised",xpos="right",ypos="base") from _call_her_main_1890
                        pause.5

                        if whoring < 15:
                            call her_main("How could you do this to me, [genie_name]?!","scream","angry") from _call_her_main_1891
                            call her_main("My ass is covered in cum!","angry","angry") from _call_her_main_1892
                        else:
                            call her_main("[genie_name], how could you...?","angry","suspicious",cheeks="blush") from _call_her_main_1893
                            call her_main("My ass...","disgust","down") from _call_her_main_1894
                            call her_main("It's covered....","disgust","down_raised") from _call_her_main_1895
        
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        call ctc from _call_ctc_134

                        hide screen hermione_main
                        call blkfade from _call_blkfade_84

                        if whoring < 15:
                            $ mad += 20
                        else:
                            $ mad += 10


            #Third Event.
            else: #18+

                menu:
                    g4 "Argh! (I'm about to cum!)"

                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        call her_head("...............","disgust","down_raised",cheeks="blush") from _call_her_head_579
                        call her_head("Ehm... I mean I know I said not to cum on me...","disgust","down_raised",cheeks="blush") from _call_her_head_580
                        m "Huh?"
                        call her_head("But I wouldn't mind if you ...","shock","worriedCl") from _call_her_head_581
                        call her_head("Came...","disgust","down_raised",cheeks="blush") from _call_her_head_582
                        call her_head("On my ass--","base","baseL",cheeks="blush") from _call_her_head_583
                        g4 "Argh! You whore!"
                        call her_head("???","mad","wide",cheeks="blush") from _call_her_head_584

                        call cum_block from _call_cum_block_29

                        g4 "Argh! YES!"

                        $ hermione_ass_cum = True
                        call gen_chibi("cumming","on_girl","base") from _call_gen_chibi_40
                        hide screen hermione_ass
                        hide screen bld1
                        hide screen blktone
                        hide screen blkfade
                        call ctc from _call_ctc_135

                        show screen blktone
                        show screen hermione_ass
                        with fade

                        call her_head("that's it [genie_name], release your... semen on me...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_585
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 

                        call her_head("ah{image=textheart}, what's done is done I suppose...","base","baseL",cheeks="blush") from _call_her_head_586

                    "-Just start cumming-":
                        g4 "Argh! You fat assed whore!"
                        call her_head("???","mad","wide",cheeks="blush") from _call_her_head_587

                        call cum_block from _call_cum_block_30

                        g4 "Argh! YES!"

                        $ hermione_ass_cum = True
                        hide screen hermione_ass
                        call gen_chibi("cumming","on_girl","base") from _call_gen_chibi_41
                        hide screen bld1
                        hide screen blktone
                        hide screen blkfade
                        call ctc from _call_ctc_136

                        show screen blktone
                        show screen hermione_ass
                        with fade

                        call her_head("ah...{image=textheart} It's so hot...{image=textheart}","shock","worriedCl") from _call_her_head_588
                        call her_head("there's so much...{image=textheart}","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_589
                        g4 "Oh, this is great, yes..."
                        call her_head("ah...{image=textheart}","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_590
                        
                        call her_head("Well, what's done is done I suppose...","angry","worriedCl",cheeks="blush") from _call_her_head_591

                hide screen hermione_ass
                call gen_chibi("stand","desk","base") from _call_gen_chibi_42
                call her_chibi("stand","mid","base") from _call_her_chibi_80
                hide screen blktone
                with fade
                pause.5

                call bld from _call_bld_61
                m "Oh, this was quite amazing..."
                call her_main("","disgust","down_raised",xpos="right",ypos="base") from _call_her_main_1896
                pause.5
                her "My ass is covered though..."
                m "Don't worry, it still looks great, [hermione_name]."
                m "Maybe even better now..."
                call her_main("Thank you [genie_name].","base","closed") from _call_her_main_1897
                call her_main("although I do need to clean myself up...","annoyed","closed") from _call_her_main_1898
                call ctc from _call_ctc_137

                hide screen hermione_main
                call blkfade from _call_blkfade_85

                        
    
    $ hermione_ass_cum = False

    call h_action("none") from _call_h_action_12 #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01  
    hide screen groping_01
    hide screen groping_02

    call her_chibi("stand","desk","base") from _call_her_chibi_81

    hide screen chair_left
    show screen genie 
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main("","","",trans="fade",xpos="right",ypos="base") from _call_her_main_1899

    if whoring < 18:
        if whoring < 15:
            call her_main("Can I have my payment now?","base","ahegao_raised",cheeks="blush") from _call_her_main_1900
            if current_payout < 100:
                $ mad +=7

        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"
        stop music fadeout 10.0
    
        call her_main("..................","annoyed","worriedL") from _call_her_main_1901
        her "Thank you [genie_name]..."

    else:
        call her_main("..................","base","happyCl") from _call_her_main_1902


    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    
    $ new_request_08_heart = 1
    $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 1 #Event hearts level (0-3)

    if whoring >= 9 and whoring < 12:
        $ new_request_08_heart = 1
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 12 and whoring < 15:
        $ new_request_08_heart = 2
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 15:
        $ new_request_08_heart = 3
        $ hg_pf_ShowMeYourAss_OBJ.hearts_level = 3 #Event hearts level (0-3)

    if whoring < 12:
        $ whoring +=1

    $ hg_pf_ShowMeYourAss_OBJ.points += 1
    
    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2
    
    call her_walk("desk","door",2.5) from _call_her_walk_59

    #First event.
    if whoring >= 9 and whoring < 12:
        call her_head("(How degrading... why do i keep agreeing to this...?)","disgust","down_raised",cheeks="blush") from _call_her_head_592

    #Second event.
    elif whoring >= 12 and whoring < 15:
        call her_head("........................","disgust","down_raised",cheeks="blush") from _call_her_head_593

    #Third event.
    elif whoring >= 12:
        call her_head("{size=-5}(That was so exhilerating...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_594
        call her_head("{size=-5}(No, Hermione, you silly girl!){/size}","angry","angry",cheeks="blush") from _call_her_head_595
        call her_head("{size=-5}(it was shameful! good girls don't get turned on by stripping for their headmaster!){/size}","angry","angry",cheeks="blush") from _call_her_head_596
        call her_head(".................................","base","ahegao_raised",cheeks="blush") from _call_her_head_597
    elif whoring >= 18 and aftersperm:
        call her_head("{size=-5}(That was so exhilarating...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_598
        call her_head("{size=-5}(i wonder what he'll ask me to do next...?){/size}","open","ahegao_raised",cheeks="blush") from _call_her_head_599
    
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    call her_chibi("leave","door","base") from _call_her_chibi_82
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    if daytime:
        call play_music("day_theme") from _call_play_music_97
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme") from _call_play_music_98
        $ hermione_sleeping = True
        jump night_main_menu     
    









