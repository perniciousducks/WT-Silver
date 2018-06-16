

label hg_pf_TitJob: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TitJob_OBJ.points == 0:
        m "{size=-4}(Should I ask her for a titjob?){/size}"
    else:
        g9 "{size=-4}(I feel like putting my cock between those tits again!){/size}"

    if hg_pf_TitJob_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_powerGirl_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL") from _call_her_main_2352
                m "Power Girl."
                if whoring >= 18:
                    call her_main("A super hero?","annoyed","annoyed") from _call_her_main_2353
                    m "Do you have a problem with that?"
                    call her_main("...","upset","wink") from _call_her_main_2354
                    call her_main("I suppose not, I mean if it keeps my uniform clean...","annoyed","worriedL") from _call_her_main_2355
                    call play_sound("door") from _call_play_sound_94 #Sound of a door opening.
                    call set_hermione_outfit(hg_powerGirl_OBJ) from _call_set_hermione_outfit_10
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    $ current_payout = 45 #Used when haggling about price of th favor.
    
    call bld from _call_bld_62

    #First Event.
    if hg_pf_TitJob_OBJ.points == 0:
        m "Now [hermione_name]."
        call her_main("Yes, [genie_name]?","base","base",xpos="right",ypos="base") from _call_her_main_2356
        m "Have you ever given someone a titjob?"

        if whoring < 15:
            jump too_much

        call her_main("A titjob?","annoyed","annoyed") from _call_her_main_2357
        m "It's where you wrap those fat tits of your around a cock and then shake them up and down and up and..."
        call her_main("[genie_name]!","angry","angry") from _call_her_main_2358
        m "So have you ever given a boy a titjob?"
        call her_main("......","disgust","glance") from _call_her_main_2359
        call her_main("{size=-7}No...{/size}","angry","worriedCl",emote="05") from _call_her_main_2360
        m "Hmmm? What was that?"
        call her_main("No!!!","scream","worriedCl") from _call_her_main_2361
        m "Well today is your lucky day!"
        call her_main("Lucky? How would you call this lucky?","disgust","glance") from _call_her_main_2362
        m "it's not every day you learn something new."
        call her_main("I'm in school! It's my job to learn something new everyday!","scream","angryCl") from _call_her_main_2363
        m "At least this is something you'll be able to use in the real world."
        call her_main("......","disgust","glance") from _call_her_main_2364
        call her_main("{size=-7}I want 100 points...{/size}","angry","worriedCl",emote="05") from _call_her_main_2365
        m "Speak up [hermione_name]."
        call her_main("I want 100 points!","scream","worriedCl") from _call_her_main_2366

        label back_to_titjob_choices:
        menu:
            m "..."
            "\"You will get 15 house points and I promise not to cum on you.\"":
                $ mad +=7
                call her_main("You expect me to give you a titjob for 15 points!","annoyed","angryL") from _call_her_main_2367
                her "I don't know who you think I am but I am not going to do this for 15 measly points!"
                call her_main("(Besides, I don't really mind being covered in his sticky load...)","annoyed","angryL") from _call_her_main_2368
                jump back_to_titjob_choices
            "\"you will get 45 house points.\"":
                if mad > 7: #You could spam points into infinity with the choice above.
                    $ mad = 7
                call her_main(".....","annoyed","angryL") from _call_her_main_2369
                call her_main("45 house points...?","open","down") from _call_her_main_2370
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                call her_main("Yes, yes it is, [genie_name].","annoyed","annoyed") from _call_her_main_2371
                m "Great!"
            "\"you will get 100 house points.\"":
                call play_music("chipper_doodle") from _call_play_music_102 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 house points?!","scream","wide_stare") from _call_her_main_2372
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "SO that's a yes?"
                call her_main("Of course!","smile","happyCl") from _call_her_main_2373
                call her_main("For 100 points I'll give you the best damn titjob of your life!","smile","happyCl",emote="06") from _call_her_main_2374

        # GENIE STANDS WITH HIS COCK OUT
        hide screen hermione_main  
        hide screen bld1
        call blkfade from _call_blkfade_98

        call play_music("playful_tension") from _call_play_music_103# SEX THEME.                                                                                                                                                                                 #HERMIONE
        hide screen genie
        show screen chair_left
        show screen desk
        call her_chibi("stand","mid","base") from _call_her_chibi_98
        call gen_chibi("hold_dick","desk","base") from _call_gen_chibi_45
        call hide_blkfade from _call_hide_blkfade_54
        call ctc from _call_ctc_145

        show screen bld1
        call her_main("...........","open","base") from _call_her_main_2375
        call her_main("(It's so big...)","base","down") from _call_her_main_2376
        m "Get to it [hermione_name]."
        call her_main("Right...","angry","worriedCl",emote="05") from _call_her_main_2377
        call her_main("","annoyed","annoyed") from _call_her_main_2378
        pause.2

        #First and Second Event.
        label titjob_round_2:

        #Hermione removes her top.
        $ hermione_wear_bra = False
        call set_hermione_action("lift_top") from _call_set_hermione_action_79
        pause.5
                
        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update") from _call_set_hermione_action_80
        pause.5

        hide screen hermione_main
        hide screen bld1
        call blkfade from _call_blkfade_99
                                                                                                                                                                                       #HERMIONE
        hide screen genie
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide") from _call_her_chibi_99
        call gen_chibi("titjob","mid","base") from _call_gen_chibi_46

        if hermione_costume:
            call h_action("lift_top") from _call_h_action_38
        else:
            call h_action("lift_breasts") from _call_h_action_39

        call nar(">Hermione clumsily wraps her tits around your cock...") from _call_nar_367
        m "That's a start. Now, up and down..."
        call her_head("Alright...","angry","worriedCl",emote="05",xpos="base",ypos="high") from _call_her_head_600 
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_55
        call ctc from _call_ctc_146

        call play_music("playful_tension") from _call_play_music_104# SEX THEME.
        call bld from _call_bld_63
        g9 "mmmm..."

        if hg_pf_TitJob_OBJ.points == 0:
            call her_head("...","base","base") from _call_her_head_601
            call her_head("Does it... feel good?","base","squint") from _call_her_head_602
            m "Good?"
            m "It feels amazing."
            call her_head("Oh...","base","squint") from _call_her_head_603
            call her_head("......") from _call_her_head_604
            call her_head("Thank you [genie_name]","base","baseL") from _call_her_head_605

        call her_head("[genie_name]...?","soft","base") from _call_her_head_606    
        m "What is it?"
        call her_head("Promise me you won't cum on my... face...","upset","wink") from _call_her_head_607

        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"I promise not to cover that sweet little face of yours...\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                call her_head("Thank you, [genie_name].","base","squint") from _call_her_head_608 
            "\"Hmmmm... We'll see how I feel later...\"":
                call her_head("Hmmmmph.","annoyed","annoyed") from _call_her_head_609
                call her_head("At least avoid my hair...","normal","worriedCl") from _call_her_head_610 

        call her_head("........","open","base") from _call_her_head_611 
        m "............."
        call her_head(".............","normal","worriedCl") from _call_her_head_612
        call her_head("Err... [genie_name]?") from _call_her_head_613 
        m "Yes, what is it?"
        call her_head("Are you almost there?","open","base") from _call_her_head_614 
        m "Why?"

        if daytime:
            call her_head("Well, it's just that my classes are about to start...","upset","wink") from _call_her_head_615
        else: 
            call her_head("Well, it's just that I promised Ginny that we'd hang out tonight...","upset","wink") from _call_her_head_616
            call her_head("She's pretty upset that I'm spending so much time in here...") from _call_her_head_617

        
        #if not hanging_out_with_ginny:
        #    m "(Isn't Ginny that hot redhead?!)"
        #    call nar(>Your curiosity about Ginny grows!)
        #$ hanging_out_with_ginny = True
                
        m "Do you need the points or not?"
        call her_head("I do, [genie_name]! I'm sorry...","grin","worriedCl") from _call_her_head_618
        call her_head("I'll just keep on stroking it then...") from _call_her_head_619
        m "Well, you could make this finish up a little faster..."
        call her_head("Really? What can I do [genie_name]?","base","baseL") from _call_her_head_620 

        menu:
            m "..."
            "\"Tell me how much you love your tits.\"":
                call her_head("What?","upset","wink") from _call_her_head_621
                call her_head("My breasts?") from _call_her_head_622
                m "you know, How good they feel..."
                m "The looks that you get because of them."
                call her_head("Oh, alright then...","base","base") from _call_her_head_623 
                call her_head("There was this one time in the library...","smile","baseL") from _call_her_head_624
                call her_head("It was empty apart from this first year boy sitting across from me...") from _call_her_head_625
                m "Heh... good. Go on."
                call her_head("Well it was so hot that I'd taken my vest off...","base","squint") from _call_her_head_626 
                m "I bet it was hot..."
                call her_head("He was trying to act sly but I could tell that he kept sneaking glances at them...","base","baseL") from _call_her_head_627
                call her_head("So I started undoing the buttons... Slowly at first, not enough for him to suspect anything....","base","glance") from _call_her_head_628
                m "mmmmm, you little slut."
                call her_head("By the third button he couldn't take his eyes off of me.","base","down") from _call_her_head_629
                call her_head("As I slowly undid the fourth he moved his hands under the desk...") from _call_her_head_630
                m "Really?"
                call her_head("Really... I could almost hear him stroking it...","base","ahegao_raised") from _call_her_head_631
                call her_head("When I undid the fifth button he could almost see my nipples...","open","baseL") from _call_her_head_632 
                g9 "Do you have no shame?"
                call her_head("[genie_name]! I was just trying to cool down...","base","down") from _call_her_head_633 
                m "I'm just kidding, keep going."
                call her_head(".....","base","glance") from _call_her_head_634
                call her_head("By the sixth button almost nothing was hidden...") from _call_her_head_635
                call her_head("He could see my naked tits...","base","suspicious") from _call_her_head_636
                call her_head("and he just stared at them... not even trying to hide what he was doing...") from _call_her_head_637
                call her_head("when I undid the final button it was too much for him...") from _call_her_head_638
                call her_head("He shot his cum under the table, covering my legs and feet in his hot cum!","silly","ahegao") from _call_her_head_639 
                g4 "!!!"
                call her_head("Come on [genie_name] cover me as well! Cum all over my tits!","grin","ahegao") from _call_her_head_640
                with hpunch
                g4 "{size=-4}(Here it comes! Where should I aim for?){/size}"
            
            "\"Stick your tongue out tilt you head down!\"":
                call her_head("What?","base","base") from _call_her_head_641 
                m "Just do it, slut."
                call her_head("Like this?","open_wide_tongue","squintL") from _call_her_head_642 
                m "Yes, good. Tilt your head down as far as it'll go."
                call her_head(".....................","open_wide_tongue","base") from _call_her_head_643 
                m "Yes... Good..."
                call her_head("...........","open_wide_tongue","base") from _call_her_head_644
                call her_head("...........") from _call_her_head_645
                call her_head("I can't keep my mouth open for so long, [genie_name]. I will start to drool...","open","base") from _call_her_head_646 
                m "But I want you to drool... all over those perfect tits of yours"
                call her_head("What? You think they're perfect?","open","base") from _call_her_head_647 
                m "As perfect as any mortal, [hermione_name]!"
                call her_head(".......","base","ahegao_raised") from _call_her_head_648 
                m "Now stick it back out again and try to get it as close to the tip of my cock as you can"
                call her_head("............","normal","worriedCl") from _call_her_head_649
                call her_head("A-ha.....","open_wide_tongue","base") from _call_her_head_650 
                m "Good, [hermione_name]."
                call her_head("..............","open_wide_tongue","base") from _call_her_head_651 
                m "Yes, keep on stroking my cock."
                ">You thrust up as she pushes her tits down causing the tip of your cock to touch her wet tongue."
                call her_head("..................","open_wide_tongue","base") from _call_her_head_652
                g4 "Oh that's good..."
                call her_head(".................","open_wide_tongue","base") from _call_her_head_653 
                ">You thrust into her tongue again."
                m "That's it slut taste it!"
                call her_head(".....................","open_wide_tongue","angryCl") from _call_her_head_654 
                m "Yes, you big titted whore!"
                call her_head("......................","open_wide_tongue","angry") from _call_her_head_655 
                m "I want to cum in that little slutty mouth of yours..."
                call her_head("................","open_wide_tongue","angry") from _call_her_head_656 
                g4 "{size=-4}(Here it comes! Where should I aim for?){/size}"

        menu:
            m "..."
            "-cum in her mouth-":
                $ mad += 3
                g4 "Here it comes, [hermione_name]! You better be ready!"
                call her_head("What? already?!","shock","wide") from _call_her_head_657 
                g4 "{size=+5}Yeah, your tits felt great!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen bld1
                call blkfade from _call_blkfade_100

                call her_head("No, [genie_name], wait, not on my fa--","angry","base") from _call_her_head_658 
                g4 "{size=+5}Open wide slut!!{/size}"
                call her_head("Not in my mou-","scream","wide") from _call_her_head_659       
                ">You grab the back of Hermione's head and force your cock into her open mouth..."
                call her_head("!!!!!!!","shock","worriedCl") from _call_her_head_660 
                ">The sensation of her warm mouth and squirming tongue overwhelm you and you start cumming like crazy"

                call cum_block from _call_cum_block_40

                g4 "{size=+5}ARGH! YES!!! Take it, slut!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_661 
                
                call gen_chibi("titjob_cum_in_mouth","mid","base") from _call_gen_chibi_47
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_56
                stop music fadeout 1.0
                call ctc from _call_ctc_147

                call bld from _call_bld_64 
                call her_head(".......................","full_cum","down",cheeks="blush") from _call_her_head_662                
                m "mmmmmm that felt great...."
                call her_head(".......................","full_cum","down",cheeks="blush") from _call_her_head_663    
                m "How are you feeling?"
                call her_head(".......................","full_cum","down",cheeks="blush") from _call_her_head_664    
                m "[hermione_name]?"

                call play_music("chipper_doodle") from _call_play_music_105 # HERMIONE'S THEME.

                hide screen bld1
                call gen_chibi("titjob_pause","mid","base") from _call_gen_chibi_48
                pause.5

                show screen bld1
                call nar(">Hermione opens her mouth, letting your cum fall out onto her tits.") from _call_nar_368
                call her_head("*ptui*","open_wide_tongue_cum","angry") from _call_her_head_665

                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                call her_head("Why on earth did you cum in my mouth!","angry","worriedCl",emote="05") from _call_her_head_666
                m "well you did say not to cum on your face."
                pause.5
                hide screen bld1
                call blkfade from _call_blkfade_101

                ">Hermione releases your still pulsating cock."
                pause.5

                call gen_chibi("hold_dick","desk","base") from _call_gen_chibi_49
                call her_chibi("stand","mid","base") from _call_her_chibi_100
                call hide_blkfade from _call_hide_blkfade_57
                pause.5

                show screen bld1
                call her_main("Ughhh... you came so much! I had to swallow most of it!","angry","worriedCl",emote="05",xpos="right",ypos="base") from _call_her_main_2379
                m "That's your fault for doing such a great job..."
                call her_main("I don't want to hear it...","angry","worriedCl",emote="05") from _call_her_main_2380
                if daytime:
                    call her_main("My classes are about to start and now I'm covered in your sperm...","angry","worriedCl",emote="05") from _call_her_main_2381 
                else:
                    call her_main("At this hour The \"Gryffindor\" common room will be full of people...","angry","worriedCl",emote="05") from _call_her_main_2382
                    call her_main("And now I'm going to have to go there, smelling like... spunk...") from _call_her_main_2383
                    call her_main("Maybe if I just run to bed no one will be able to tell...","angry","base") from _call_her_main_2384 
                    
                m "You could have swallowed..."
                m "Then there wouldn't have been any clean up."
                call her_main("Swallow all of that?","angry","down_raised") from _call_her_main_2385
                call her_main("I don't think I have enough room in my stomach...") from _call_her_main_2386
                call her_main("Is that all [genie_name]?","annoyed","closed") from _call_her_main_2387
                call blkfade from _call_blkfade_102

                $ aftersperm = True

                jump done_with_titjob

            "-cover her tits-":
                with hpunch
                g4 "ARGH!"
                call blkfade from _call_blkfade_103

                call her_head("WHAT?!","shock","wide") from _call_her_head_667               
                g4 "Take this slut!"

                call cum_block from _call_cum_block_41

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_668 
                
                call gen_chibi("titjob_cum_on_tits","mid","base") from _call_gen_chibi_50
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_58
                call ctc from _call_ctc_148

                call bld from _call_bld_65
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True
                call her_head(".......................","angry","wide") from _call_her_head_669          
                m "Yes... That's it..."
                call her_head("..........","soft","base",tears="soft") from _call_her_head_670
                m "Well, I think that's about it..."
                her ".........."
                hide screen bld1
                call blkfade from _call_blkfade_104

                call gen_chibi("hold_dick","desk","base") from _call_gen_chibi_51
                call her_chibi("stand","mid","base") from _call_her_chibi_101
                pause 1
                call hide_blkfade from _call_hide_blkfade_59
                pause.5

                call her_main("","annoyed","baseL",xpos="right",ypos="base") from _call_her_main_2388
                call ctc from _call_ctc_149

                if daytime:
                    call her_main("[genie_name]! How could you cum so much?!","scream","worriedCl") from _call_her_main_2389
                    call her_main("It's like you dumped a bucket of spunk over my chest!","annoyed","angryL") from _call_her_main_2390
                    call her_main("My classes are about to start and I can't go looking like this!","open","down") from _call_her_main_2391
                    m "Of course you can, just wipe it off or something..."
                    m "Nobody will even notice... Except for the smell maybe..."
                    call her_main("...I would like to get paid now.","annoyed","annoyed") from _call_her_main_2392
                else:
                    call her_main("How can one person cum so much!","annoyed","angryL") from _call_her_main_2393
                    her "how Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                    m "Just wipe it off or something."
                    m "It's not like it'll be the first time you've gone to bed smelling like cum."
                    call her_main("...I would like to get paid now.","annoyed","annoyed") from _call_her_main_2394
                
                call blkfade from _call_blkfade_105

                $ uni_sperm = False
                $ aftersperm = True

                jump done_with_titjob
        
    #Second Event.
    elif hg_pf_TitJob_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="right",ypos="base") from _call_her_main_2395
        m "How do you feel about wrapping those nice tits of yours around my cock again?"
        call her_main("Only nice?","upset","closed") from _call_her_main_2396
        m "Fine, fine."
        m "How do you feel about wrapping those perfect tits of yours around my cock again?"
        call her_main("Of course, [genie_name].","base","glance") from _call_her_main_2397
        m "You like it when I call them perfect don't you?"
        call her_main(".............","base","down") from _call_her_main_2398
        g9 "you don't have to say anything, just bring those perfect tits over here."
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","worriedCl") from _call_her_main_2399
        call her_main("yes [genie_name]","grin","baseL") from _call_her_main_2400
        stop music fadeout 4.0

        jump titjob_round_2

    #Third Event.
    elif hg_pf_TitJob_OBJ.points >= 2:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="right",ypos="base") from _call_her_main_2401
        m "You don't mind wrapping those perfect tits of yours around my cock again, do you?"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised") from _call_her_main_2402
        if whoring < 21:
            call her_main("As long as I am getting paid...","soft","squintL") from _call_her_main_2403
            m "Well, come here then. Time to earn those points."
        else:
            call her_main("Of course not [genie_name]...","open","baseL") from _call_her_main_2404
            m "Well, come here then."
            call her_main("","base","glance") from _call_her_main_2405
            pause.1
        
        jump start_titfuck


label start_titfuck:

        #Hermione removes her top.
        $ hermione_wear_bra = False
        call set_hermione_action("lift_top","skip_update") from _call_set_hermione_action_81
        pause.5
                
        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update") from _call_set_hermione_action_82
        pause.5

        hide screen bld1
        call blkfade from _call_blkfade_106
        pause.8
 
        hide screen genie
        show screen chair_left
        show screen desk
        call her_chibi("hide") from _call_her_chibi_102
        call gen_chibi("titjob","mid","base") from _call_gen_chibi_52
        
        ">Hermione wraps her plump tits around your cock..."

        call h_action("lift_breasts","skip_update") from _call_h_action_40

        stop music fadeout 3.0
        call her_head("Do you like it when I do it like this, [genie_name]?","grin","baseL",xpos="base",ypos="high") from _call_her_head_671
        ">Hermione starts alternating her breasts as she titfucks you."
        g9 "Actually, yes! Very nice!"
        call play_music("chipper_doodle") from _call_play_music_106 # HERMIONE'S THEME.
        
        call hide_blkfade from _call_hide_blkfade_60
        call ctc from _call_ctc_150

        show screen bld1
        call her_head("...","base","glance") from _call_her_head_672
        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        call her_head("Thank you, [genie_name].","base","happyCl") from _call_her_head_673
        call her_head("I figured with how nice you've been it's the least I could do...") from _call_her_head_674
        m "Hm..."

        menu:
            m "..."
            "\"What do you think of my cock?\"":
                call her_head("Huh?","open","base") from _call_her_head_675
                call her_head("Your cock?","angry","worriedCl",emote="05") from _call_her_head_676         
                m "What do you think abo-"
                call her_head("It's amazing....","upset","closed") from _call_her_head_677         
                m "go on..."
                call her_head("If I have the perfect tits then this...","soft","ahegao") from _call_her_head_678   
                call nar(">She squeezes her tits around your cock.") from _call_nar_369
                call her_head("This is the perfect cock","grin","dead") from _call_her_head_679         
                m "Perfect?"
                call her_head("Perfect.","base","down") from _call_her_head_680      
                call her_head("Perfect size...","soft","down") from _call_her_head_681
                call her_head("Perfect shape...") from _call_her_head_682
                call nar("Hermione tilts her head down and licks the tip of your cock.") from _call_nar_370
                call her_head("...","open_tongue","ahegao") from _call_her_head_683  
                call her_head("Perfect taste...","soft","ahegao") from _call_her_head_684         
                m "..."
                call her_head("I think your perfect cock should be shared around the school. ","scream","angryCl") from _call_her_head_685         
                m "Well, I wouldn't go that far--"
                call her_head("Listen to me, [genie_name]!","soft","ahegao") from _call_her_head_686
                call her_head("I think your perfect cock should be worshipped as part of the school curriculem!") from _call_her_head_687
                call her_head("Girls will be required to come in and bask in it's glory!") from _call_her_head_688
                m "OK, I think I've heard enough."
                call her_head("Too much?","angry","wink") from _call_her_head_689         
                m "Yeah, just a bit."
                call her_head("Sorry [genie_name], I got a bit carried away...","angry","worriedCl",emote="05") from _call_her_head_690         
                m "No biggie. Just keep on massaging it with those big tits of yours."
                call her_head(".................","soft","ahegao") from _call_her_head_691  

                call nar(">Hermione keeps on stroking your cock.","start") from _call_nar_371
                call nar(">She spits on it to help lubricate it.","end") from _call_nar_372

                m "Yes, yes... That's it slut."
                
            "\"Call yourself a big titted whore!\"":
                call her_head("Excuse me?","open","base") from _call_her_head_692
                call her_head("Oh... I am a big tittedwhore!","soft","ahegao") from _call_her_head_693  
                m "Good. Glad we established that."
                m "Now I want you to say..."

                menu:
                    m "..."
                    "\"I am a shameless cumslut!\"":
                        call her_head("Of course.","base","down") from _call_her_head_694
                        call her_head("I am a shameless cumslut.","soft","ahegao") from _call_her_head_695
                        call her_head("A dirty little slut who's addicted to the the taste of my headmaster's cum...","grin","dead") from _call_her_head_696
                        m "Yes! Good!"
                    "\"I love being covered in cum!\"":
                        call her_head("I love being covered in cum!","soft","ahegao") from _call_her_head_697
                        call her_head("hot...") from _call_her_head_698
                        call her_head("sticky...") from _call_her_head_699
                        call her_head("smelly...") from _call_her_head_700
                        call her_head("cum...") from _call_her_head_701
                        call her_head("...................................","grin","dead") from _call_her_head_702
                        call her_head("How was that, [genie_name]?","angry","wink") from _call_her_head_703  
                        m "Perfect." 

            "\"This is really good. Did you practice?\"":
                call her_head("Hm?","base","happyCl") from _call_her_head_704
                call her_head("Sort of... Well not on another cock...","angry","wink") from _call_her_head_705
                m "On what then?"
                call her_head("Well I spoke to Ginny...","grin","baseL") from _call_her_head_706    
                m "A friend of yours?"
                call her_head("yes. I asked if she had any tips for this sort of thing...","base","baseL") from _call_her_head_707
                call her_head("She said the best way to improve was practice...","base","squint") from _call_her_head_708
                m "Practice on what?"
                call her_head("On Ginny","smile","baseL") from _call_her_head_709 
                call her_head("Well... on her... arm.","angry","wink") from _call_her_head_710    
                m "You titfucked your friends arm?"
                call her_head("Just as practice!","grin","worriedCl",emote="05") from _call_her_head_711
                call her_head("She even game me some tips...") from _call_her_head_712
                call her_head("How does this feel?","base","down") from _call_her_head_713
                m "mmmmm... Yes, this feels quite good."
                call her_head("Does it?","angry","wink") from _call_her_head_714
                call her_head("Ginny seemed to enjoy it a lot as well...","base","ahegao_raised") from _call_her_head_715
                g4 "She enjoyed it?"
                call her_head("Of course she did!","base","happyCl") from _call_her_head_716    
                call her_head("Who wouldn't love feeling my perfect tits...","base","closed") from _call_her_head_717
                call her_head("Although I think she might have enjoyed it...","open","down") from _call_her_head_718
                call her_head("A little too much...","soft","squintL") from _call_her_head_719
                m "How so?"
                call her_head("Well...","soft","squintL") from _call_her_head_720
                call her_head("She might have started...") from _call_her_head_721
                call her_head("Playing with herself...","grin","ahegao") from _call_her_head_722
                with hpunch
                with kissiris
                g4 "Yes, keep going slut"
                call her_head("As I was \"Practicing\" on her arm she might have...","open","baseL") from _call_her_head_723
                call her_head("cum...","soft","ahegao") from _call_her_head_724    
                g4 "[hermione_name], you little slut!"
                call her_head("It was just practice!","grin","worriedCl",emote="05") from _call_her_head_725
                call her_head("Err... I mean...","angry","wink") from _call_her_head_726
                call her_head("It's not like I enjoyed it as well...","angry","down_raised") from _call_her_head_727
                m "Yes, yes... you're not a slut at all..."
                m "Mmmmm, why don't you spit on it a little..."
                m "Oh, yes..."
                call her_head("...............","base","down") from _call_her_head_728

        m "Yes... Keep stroking it."
        call her_head("..............","angry","wink") from _call_her_head_729
        m "Now I want you to say..."

        menu:
            m "..."
            "{size=-4}\"I love teasing my father with my big tits.\"{/size}":
                call her_head("I do not!","angry","down_raised") from _call_her_head_730
                m "I know. Just say it."
                call her_head("My father? That's gross, [genie_name]! How could you suggest that I want to fu-","soft","ahegao") from _call_her_head_731
                m "Come on... Just make something up."
                call her_head("...........","angry","wink") from _call_her_head_732
                call her_head("Well...","open","down") from _call_her_head_733
                call her_head("Sometimes when I hug him...") from _call_her_head_734
                call her_head(".......") from _call_her_head_735
                m "Go on [hermione_name]..."
                call her_head("I press my tits into him...","soft","ahegao") from _call_her_head_736
                m "Do you think he enjoys it?"
                call her_head("I'm not sure...","annoyed","base") from _call_her_head_737
                call her_head("I think so...","soft","squintL") from _call_her_head_738
                call her_head("He always tries to cover his croutch afterwards...","base","closed") from _call_her_head_739
                call her_head("He even says I'm too old for hugs...","annoyed","closed") from _call_her_head_740
                call her_head("But I make sure to give him a big one every night before I go to bed...") from _call_her_head_741
                call her_head("So that he'll think of me...","base","down") from _call_her_head_742
                call her_head("And how good I felt...","grin","dead") from _call_her_head_743
                call her_head("Pressing into him...","soft","ahegao") from _call_her_head_744
                m "That's it slut."
                call her_head("Then I give him a kiss on the forehead...","soft","squintL") from _call_her_head_745
                call her_head("Making sure that he can see down my blouse...","grin","worriedCl",emote="05") from _call_her_head_746
                call her_head("{image=textheart}{image=textheart}{image=textheart}") from _call_her_head_747
                call her_head("But all of that is not true of course!","open","base") from _call_her_head_748
                call her_head("None of that happens! It was just for you to imagine!") from _call_her_head_749
                m "Right..."
            "{size=-4}\"I love teasing my schoolmates with my perfect tits.\"{/size}":
                call her_head("I love teasing my schoolmates with my perfect tits...","soft","ahegao") from _call_her_head_750
                m "Of course you do..."
                call her_head("I love the jealous looks from the other girls...","base","down") from _call_her_head_751
                m "I bet they're jealous..."
                call her_head("I love teasing ron and harry during breakfast...","base","glance") from _call_her_head_752
                call her_head("Sometimes I'll walk around with only one button done up...","base","suspicious") from _call_her_head_753
                call her_head("Other times I'll just wear my vest with nothing on underneath...") from _call_her_head_754
                m "And how do you feel..."
                call her_head("So good...","silly","dead") from _call_her_head_755
                call her_head("One time when I was walking back from your office at night I was barely covering them...","angry","wink") from _call_her_head_756
                call her_head("And as I rounded a corner...","soft","ahegao") from _call_her_head_757
                call her_head("A second year boy ran head first into them...","grin","ahegao") from _call_her_head_758
                m "Head first into your tits?"
                call her_head("All I could see was the top of his head...","grin","dead") from _call_her_head_759
                m "What did he do?"
                call her_head("He tried to pull away...") from _call_her_head_760
                m "Tried?"
                call her_head("Well I may have held him there...","base","glance") from _call_her_head_761
                call her_head("Just for a little bit...","base","down") from _call_her_head_762
                call her_head("Just to tell him it was alright...","base","suspicious") from _call_her_head_763
                m "You little slut."
                call her_head("I think I might have broken him though...","base","down") from _call_her_head_764
                call her_head("Because when I let him go he said nothing. He just stepped back slowly and walked away.","soft","ahegao") from _call_her_head_765
                m "I bet I know where he went..."
                call her_head("so do i...","soft","ahegao") from _call_her_head_766
        
        #CUMMING
        m "Hm..."
        m "I love your slutty tits.!"
        call her_head("Thank you [genie_name].","soft","ahegao") from _call_her_head_767
        call her_head("Shall I rub them some more then?") from _call_her_head_768
        call nar(">Hermione presses her tits together against your cock and starts rubbing it very quickly...") from _call_nar_373
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Almost there! where should I aim?){/size}"

        menu:
            m "..."
            "\"(In her mouth).\"":
                g4 "Take this whore"
                hide screen bld1
                call blkfade from _call_blkfade_107

                ">You grab Hermione by the back of her head, tilting it down "
                call her_head("What are you-","angry","wink") from _call_her_head_769
                ">You thrust up into her wet mouth, the sensation of it driving you over the edge."
               
                call cum_block from _call_cum_block_42

                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                call play_music("chipper_doodle") from _call_play_music_107 # HERMIONE'S THEME.
                
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_770 
                
                call gen_chibi("titjob_cum_in_mouth") from _call_gen_chibi_53
                call hide_blkfade from _call_hide_blkfade_61
                call ctc from _call_ctc_151
                
                call bld from _call_bld_66
                g4 "Argh! You whore!"
                call her_head("{image=textheart}{image=textheart}{image=textheart}","full_cum","dead") from _call_her_head_771       
                g4 "Argh! you big titted slut! Take it all!"
                call her_head("......","full_cum","dead") from _call_her_head_772
                m "............"
                m "Ok, I think I am done..."
                call her_head("..............","full_cum","dead") from _call_her_head_773
                call her_head("........","full_cum","dead") from _call_her_head_774
                call her_head("...","full_cum","dead") from _call_her_head_775
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_head("*GULP*","cum","worriedCl") from _call_her_head_776 #play noise here
                hide screen bld1
                call ctc from _call_ctc_152
                call blkfade from _call_blkfade_108

                pause.5
                ">Hermione releases your cock from between her tits."
                pause 1

                call gen_chibi("stand","desk","base") from _call_gen_chibi_54
                call her_chibi("stand","mid","base") from _call_her_chibi_103

                call h_action("none","skip_update") from _call_h_action_41

                call hide_blkfade from _call_hide_blkfade_62
                pause.5

                show screen bld1
                call her_main("","soft","glance",xpos="right",ypos="base") from _call_her_main_2406
                call ctc from _call_ctc_153

                if daytime:
                    call her_main("Well, I think I'd better go now... my Classes are about to start.","base","base") from _call_her_main_2407
                else:
                    call her_main("Well, I think I'd better go now... It's getting late.","base","base") from _call_her_main_2408 
                m "So you're alright with swallowing now?"
                call her_main("What?","open","down") from _call_her_main_2409
                call her_main("Oh. I suppose so...","grin","baseL") from _call_her_main_2410
                call her_main("I mean it doesn't taste that bad and it means that I don't have to clean up afterwards.","base","happyCl") from _call_her_main_2411    
                m "Hm... Are you sure you don't want people seeing your tits covered in cum..."
                call her_main("What? walk around school covered in your cum [genie_name]?","angry","wink") from _call_her_main_2412    
                m "It would keep your clothes clean."

                if whoring < 21:
                    call her_main("With all due respect [genie_name]...","upset","closed") from _call_her_main_2413
                    call her_main("I don't plan on getting a reputation as a cum loving whore...","angry","wink") from _call_her_main_2414
                    call her_main("Not like those \"Slytherin\" girls...") from _call_her_main_2415
                else:
                    call her_main("Hmmmmm...","soft","squintL") from _call_her_main_2416
                    call her_main("Maybe if you ask nicely...","soft","squintL") from _call_her_main_2417  
                call her_main("Is that all [genie_name]?","annoyed","closed") from _call_her_main_2418 

                call blkfade from _call_blkfade_109 

                jump done_with_titjob
                

            "\"(On her tits).\"":
                g4 "Here! Take this you bit titted whore!"
                with hpunch
                g4 "ARGH!"
                hide screen bld1
                call blkfade from _call_blkfade_110

                call her_head("What? Already?!","shock","wide") from _call_her_head_777               
                g4 "Yeah, you're tits felt great slut!"

                call cum_block from _call_cum_block_43

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_head("!!!!!!!!!!!","shock","wide") from _call_her_head_778

                call gen_chibi("titjob_cum_on_tits") from _call_gen_chibi_55
                call hide_blkfade from _call_hide_blkfade_63
                call ctc from _call_ctc_154
  
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                show screen bld1
                call her_head(".......................","angry","wide") from _call_her_head_779          
                m "Aghhh... I Feel so much better now..."
                hide screen bld1
                call ctc from _call_ctc_155
                call blkfade from _call_blkfade_111

                call gen_chibi("stand","desk","base") from _call_gen_chibi_56
                call her_chibi("stand","mid","base") from _call_her_chibi_104

                call h_action("none","skip_update") from _call_h_action_42

                call hide_blkfade from _call_hide_blkfade_64
                pause.5

                show screen bld1
                call her_main("","upset","closed",xpos="right",ypos="base") from _call_her_main_2419
                call ctc from _call_ctc_156

                her ".........."
                m "Well, I think that's about it..."

                call play_music("chipper_doodle") from _call_play_music_108 # HERMIONE'S THEME.
                call her_main("[genie_name]!","annoyed","angryL") from _call_her_main_2420
                m "What?"
                call her_main("You covered my chest in cum, [genie_name]...","angry","worriedCl") from _call_her_main_2421
                call her_main("There's so much...","open","baseL") from _call_her_main_2422
                m "It's your fault, [hermione_name]!"
                call her_main("My fault?","angry","base") from _call_her_main_2423
                m "Yes! It's those perfect tits of yours..."
                m "They just felt too good..."     
                call her_main("Oh...","shock","wide") from _call_her_main_2424
                her "Well, I suppose it's not too bad then..."
                call her_main("I'll just wipe it off and hope that nobody notices...","upset","closed") from _call_her_main_2425
                m "You could lick them clean."
                call her_main("You want me to lick your cum off of my tits?","soft","ahegao") from _call_her_main_2426
                call her_main("I don't think so, [genie_name]...","soft","ahegao") from _call_her_main_2427
                her "{size=-5}Maybe next time...{/size}"
                call her_main("Is that all [genie_name]?","angry","wink") from _call_her_main_2428

                call blkfade from _call_blkfade_112

                $ aftersperm = True

                jump done_with_titjob

label done_with_titjob:

    $ gryffindor += current_payout #35

    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    hide screen hermione_main
    
    call h_action("none") from _call_h_action_43

    call gen_chibi("hide") from _call_gen_chibi_57
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") from _call_her_chibi_105
    pause.1
    call hide_blkfade from _call_hide_blkfade_65
    pause.5
    
    call bld from _call_bld_67
    m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"." 
    $ gryffindor +=current_payout
    
    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base") from _call_her_main_2429
    
    if whoring < 18:
        $ whoring +=1
    
    $ hg_pf_TitJob_OBJ.points += 1

    if hg_pf_TitJob_OBJ.points <= 3:
        $ hg_pf_TitJob_OBJ.hearts_level = hg_pf_TitJob_OBJ.points
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    
    $ custom_outfit_old = temp_outfit

    jump end_hg_pf #Resets screens. Hermione walks out. Resets Hermione.      








