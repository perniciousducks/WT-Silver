

### Flirt With Teacher ###

##(Level 02) (15 pt.) (Flirt with teachers). (Available during daytime only).
label hg_pr_FlirtTeacher:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    if hg_pr_FlirtTeacher_OBJ.points < 1:
        m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    call bld from _call_bld_90
    
    m "[hermione_name], I want you to be especially flirtatious with your teachers today."

    if whoring < 3 or hg_pr_FlirtClassmate_OBJ.points < 2:
        jump too_much
   
    #Intro
    if hg_pr_FlirtTeacher_OBJ.points == 0 and whoring < 9:
        call her_main("I will do my best, [genie_name]!","base","base",xpos="right",ypos="base") from _call_her_main_3492
        call her_main("I am glad you finally decided to act, [genie_name]!","open","base") from _call_her_main_3493
        m "Huh?"
        call her_main("You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?","normal","frown") from _call_her_main_3494 
        call her_main("I am honoured to pose as bait in this noble endeavor.","open","closed") from _call_her_main_3495
        m "Ehm... Yeah, that's exactly what I'm doing."
        call her_main("Splendid! You can count on me, [genie_name]!","normal","frown") from _call_her_main_3496

    #Second time event.
    else:
        call her_main("I shall provide you with a detailed report later tonight, [genie_name].","normal","frown",xpos="right",ypos="base") from _call_her_main_3497
        m "I will be waiting..."
    
    her "Well, I'd better go now. Classes are about to start..."
    
    $ hg_pr_FlirtTeacher_OBJ.inProgress = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.

    
label hg_pr_FlirtTeacher_complete:

    call play_sound("door") from _call_play_sound_108 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_91
    call bld from _call_bld_91
    

    #First level.
    call her_main("Good evening, [genie_name].","base","base",xpos="right",ypos="base") from _call_her_main_3498
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "Tell me how many teachers did you flirt with, [hermione_name]?"
            m "Give me the details."
            show screen blktone
            with d3
    
            #First level.
            if  whoring >= 3 and whoring < 6:

                #Event A
                if one_out_of_three == 1: ### Flitwick
                    call play_music("chipper_doodle") from _call_play_music_141 # HERMIONE'S THEME.
                    call her_main("Well, I tried flirting with Professor Flitwick...","open","worriedL",xpos="right",ypos="base") from _call_her_main_3499
                    call her_main("But it didn't really work...","annoyed","frown") from _call_her_main_3500
                    call her_main("..............................","annoyed","angryL") from _call_her_main_3501
                    m "How exciting..."
                    m "Is this all you have for me today, [hermione_name]?"
                    call her_main("Y-yes...","open","worried") from _call_her_main_3502
                    her "But [genie_name], I know for a fact that professor Flitwick is \"dirty\"!"
                    her "Everyone knows that because of his height..."
                    call her_main("He sometimes... ehm...","soft","baseL") from _call_her_main_3503
                    call her_main("He likes to look up girl's skirts, [genie_name]!","annoyed","worriedL") from _call_her_main_3504
                    m "Don't we all?"
                    call her_main("What?","open","base") from _call_her_main_3505
                    m "I said, don't we all hate it and must be outraged by the a man like Professor Flick-flick."
                    call her_main("Er... It's \"Professor Flitwick\", [genie_name].","normal","frown") from _call_her_main_3506
                    m "Right. Putting him on my \"Naughty boys list\" as we speak."
                    call her_main("......................","annoyed","suspicious") from _call_her_main_3507
                    m "Well, I hate to admit it but you did a lousy job of today's favour, [hermione_name]."
                    call her_main("................................","annoyed","angryL") from _call_her_main_3508

                    menu:
                        "\"Here are your point's though.\"":
                            call her_main("Really?","angry","worried") from _call_her_main_3509
                            call her_main("Thank you so much [genie_name]!","smile","happyCl") from _call_her_main_3510
                        "\"No points for you!\"":

                            call her_main("But [genie_name], I did my best!","angry","worried") from _call_her_main_3511
                            call her_main("You are going back on your promise [genie_name]!","mad","worried",tears="soft") from _call_her_main_3512
                            m "......................."
                            stop music fadeout 1.0
                            call her_main("How unbecoming of a school headmaster!","scream","worriedCl") from _call_her_main_3513
                            m "You are dismissed, [hermione_name]."
                            call her_main("Tsk!","angry","angry",emote="01") from _call_her_main_3514
                            $ mad += 18
                            call music_block from _call_music_block_11
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
                          
                #Event B 
                elif one_out_of_three == 2: ### Snape
                    call her_main("..................","soft","baseL",xpos="right",ypos="base") from _call_her_main_3515
                    her "............................"
                    m "[hermione_name]?"
                    call her_main("Yes, [genie_name]... I'm sorry... I just...","open","worried") from _call_her_main_3516
                    call her_main("............","soft","baseL") from _call_her_main_3517
                    m "Did you do what I asked you to do?"
                    call her_main("I tried, [genie_name]. I really did...","open","base") from _call_her_main_3518
                    m "Who did you try to flirt with?"
                    call her_main(".........","soft","baseL") from _call_her_main_3519
                    call her_main("Professor Snape, [genie_name].","annoyed","angryL") from _call_her_main_3520
                    call play_music("chipper_doodle") from _call_play_music_142 # HERMIONE'S THEME.
                    m "Severus? Interesting..."
                    m "How did it go?"
                    call her_main("It was awful [genie_name]...","normal","frown") from _call_her_main_3521
                    her "I am sorry, but I really hate professor Snape, [genie_name]!"
                    m "I'm sure the feeling is mutual..."
                    m "Tell me what happened."
                    call her_main("Nothing happened, [genie_name]. He just laughed at me...","annoyed","frown") from _call_her_main_3522
                    call her_main("I may not have much feminine charm, but I tried to be nice...","annoyed","worriedL") from _call_her_main_3523
                    call her_main("And he just started laughing in my face!","scream","angryCl") from _call_her_main_3524
                    call her_main("...it is really scary to see professor Snape laugh...","angry","worriedCl",emote="05") from _call_her_main_3525
                    her "........"
                    her "I am awful at flirting, I am sorry [genie_name]..."
                    call her_main("But I know that professor Snape is \"dirty\"!","angry","angry") from _call_her_main_3526
                    her "If you were to send someone else to him the outcome would be different, I know it!"
                    m "Someone else?"
                    call her_main("Yes! Someone with more experience at this...","upset","wink") from _call_her_main_3527
                    her "Someone..."
                    her "Someone, uhm..."
                    m "Sluttier?"
                    call her_main("Yes, I suppose...","disgust","glance") from _call_her_main_3528
                    m "Don't you give up, [hermione_name]. We will make a slut err--"
                    m "I mean a woman out of you yet!"
                    call her_main("...................","annoyed","annoyed") from _call_her_main_3529

                    menu:
                        "\"Here are your points, [hermione_name].\"":
                            pass
                        "\"...But you get no points this time\"":
                            call her_main("But I did my best...","annoyed","angryL") from _call_her_main_3530
                            call her_main("And I feel so humiliated now...","angry","worriedCl",emote="05") from _call_her_main_3531
                            call her_main("But I understand and won't argue with your decision...","normal","worriedCl") from _call_her_main_3532
                            call music_block from _call_music_block_12
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
                
                #Event C
                elif one_out_of_three == 3: ### Filch
                    stop music fadeout 1.0
                    call her_main("I tried to flirt with mr.Filch, [genie_name]...","open","worriedL",xpos="right",ypos="base") from _call_her_main_3533
                    m "I see. {size=-5}(No idea who that is.){/size}"
                    call play_music("chipper_doodle") from _call_play_music_143 # HERMIONE'S THEME.
                    call her_main("Yes, I know that technically mr.Filch is not a teacher...","open","worried") from _call_her_main_3534
                    m "Huh?"
                    call her_main("But he is part of the school's staff...","base","base") from _call_her_main_3535
                    her "And we did hit it off quite well too!"
                    her "He was surprisingly sweet."
                    her "But I don't think he is \"dirty\", [genie_name]."
                    m "Gotcha... Mr.Fil{size=+7}TH{/size} is off the list then."
                    call her_main("It's \"Mr.Filch\", [genie_name]...","normal","frown") from _call_her_main_3536
                    m "What did I say?"
            
            #Second Level.
            elif whoring >= 6 and whoring < 9:

                #Event A
                if one_out_of_three == 1: ### Slughorn
                    stop music fadeout 1.0
                    call her_main("Well, professor Slughorn invited me over to one of his...","open","worriedL",xpos="right",ypos="base") from _call_her_main_3537
                    her "Rather disturbing tea-parties..."
                    call play_music("chipper_doodle") from _call_play_music_144 # HERMIONE'S THEME.
                    call her_main("There were plenty of girls...","open","closed") from _call_her_main_3538
                    her "But all of them were much younger then me..."
                    call her_main("Almost every guest was a freshman...","annoyed","suspicious") from _call_her_main_3539
                    call her_main("We had tea and some cake...","open","closed") from _call_her_main_3540
                    her "Everything was pretty harmless..."
                    m "Did you flirt with the man or not?"
                    her "I did..."
                    call her_main("Or at least I tried...","annoyed","suspicious") from _call_her_main_3541
                    her "Professor Slughorn seems to be more interested in much younger girls..."
                    m "You almost sound jealous, [hermione_name]."
                    call her_main("What?!","angry","wide") from _call_her_main_3542
                    call her_main("That is preposterous!","annoyed","angryL") from _call_her_main_3543
                    m "Here are your points..."
                    her "...................."
                
                #Event B
                elif one_out_of_three == 2: ### Lockhart
                    $ autograph = True #This unlocks the Lockheart tattoo in the wardrobe now.
                    $ h_request_wear_tattoos = True
                    $ hermione_wear_tattoos = True
                    $ hermione_tattoos_list.append("thigh/signature") #LOCKHEART TATTOO
                    
                    call play_music("chipper_doodle") from _call_play_music_145 # HERMIONE'S THEME.
                    call her_main("I had an amazing day, [genie_name]!","smile","happyCl",emote="06",xpos="right",ypos="base") from _call_her_main_3544
                    m "Do tell, [hermione_name]..."
                    call her_main("I had a class with professor Lockhart today...","grin","baseL") from _call_her_main_3545
                    her "[genie_name] Lockhart is so charming and smart and..."
                    call her_main("And perfect...","base","ahegao_raised") from _call_her_main_3546
                    m "Please spare me your schoolgirl crush, [hermione_name]."
                    call her_main("[genie_name] Lockhart was even kind enough to give me his autograph...","smile","happyCl",emote="06") from _call_her_main_3547
                    m "How kind of him indeed."
                    call her_main("Yes, I can't wait to show it to the girls!","grin","baseL") from _call_her_main_3548
                    m "Hm... Can I see it?"
                    call her_main("[genie_name]?","base","base") from _call_her_main_3549
                    m "The Autograph, [hermione_name]. Can I see it?"
                    call her_main("Well... Em... It's in a rather private area, [genie_name].","upset","wink") from _call_her_main_3550
                    m "What? Well, then professor Goldenheart surely is \"dirty\"!"
                    call her_main("It's professor Lockhart, [genie_name]...","annoyed","angryL") from _call_her_main_3551
                    her "And... Ehm..."
                    her "Well, it's not {size=+5}that{/size} private..."
                    m "Show it to me then!"
                    call her_main("No, [genie_name]! That would be inappropriate!","disgust","glance") from _call_her_main_3552

                    menu: 
                        "{size=-3}\"Lockhart will be out of this school in no time!\"{/size}":
                            call her_main("Because of me?","scream","wide_stare") from _call_her_main_3553
                            call her_main("[genie_name], please!","mad","worried",tears="soft") from _call_her_main_3554
                            m "Show me!"
                            call her_main("No, it's embarrassing!","scream","worriedCl") from _call_her_main_3555

                            menu:
                                "\"Fine. Here are your points.\"":
                                    call her_main("Thank you for understanding, [genie_name].","base","happyCl") from _call_her_main_3556
                                "\"Show me or I won't pay you!\"":
                                    call her_main("What?!","scream","wide_stare") from _call_her_main_3557
                                    call her_main("...............","annoyed","down") from _call_her_main_3558
                                    call her_main("..................","annoyed","worriedL") from _call_her_main_3559
                                    call her_main("Well, alright, but only to clear my idol's name...","angry","angry") from _call_her_main_3560
                                    pause.5
             
                                    call her_main("Here....","disgust","down_raised",cheeks="blush",xpos="mid",ypos="base",trans="fade") from _call_her_main_3561
                                    
                                    call set_hermione_action("lift_skirt") from _call_set_hermione_action_106
                                    pause.5
                                    
                                    m "Hm..."
                                    call her_main("","angry","annoyed",emote="01",xpos="right",ypos="base") from _call_her_main_3562
                                    call ctc from _call_ctc_258
                                    
                                    call her_main("As you can see Professor Lockhart is nothing but an embodiment of everything pure and courageous!","annoyed","annoyed") from _call_her_main_3563
                                    pause
                                    m "Do I? From this?"
                                    her "You should not worry about professor Lockhart, [genie_name]."
                                    her "He is not \"dirty\"."
                                    m "Ah, what do I care..."
                                    call her_main("............?","angry","annoyed",emote="01") from _call_her_main_3564
                                    
                                    call set_hermione_action("none") from _call_set_hermione_action_107
                                    
                                    call her_main("","angry","angry") from _call_her_main_3565
                                    call ctc from _call_ctc_259
                                    $ mad += 18

                        "\"Fine... Here are your points.\"":
                            call her_main("Thank you for understanding, [genie_name].","base","happyCl") from _call_her_main_3566
                           
                #Event C
                elif one_out_of_three == 3: ### Filch
                    call play_music("chipper_doodle") from _call_play_music_146 # HERMIONE'S THEME.
                    call her_main("Well, I spent quite some time by flirting with mr.Filch today.","soft","base",xpos="right",ypos="base") from _call_her_main_3567
                    call her_main("What a well read and exceptionally well mannered gentleman mr.Filch is.","open","closed") from _call_her_main_3568
                    m "........"
                    call her_main("But I don't think anyone knows him like that...","soft","baseL") from _call_her_main_3569
                    her "I don't think anyone knows mr.Filch like I do."
                    call her_main("I feel like he really opened up to me, [genie_name].","base","base") from _call_her_main_3570
                    m "Right..."
                    m "This, mr.Fli{size=+7}nt{/size}--"
                    call her_main("It's mr.Filch, [genie_name].","open","angryCl") from _call_her_main_3571
                    m "Yeah, whatever... Is he a teacher here then?"
                    her "Mr.Filch? A teacher? No, [genie_name]..."
                    call her_main("He is the caretaker...","base","base") from _call_her_main_3572
                    m "A caretaker...?"
                    m "You mean he is a janitor?"
                    call her_main("Well...","open","worriedL") from _call_her_main_3573
                    m "[hermione_name], I did not send you out there to charm school janitors!"
                    call her_main("But mr.Filch is part of the school staff, [genie_name]!","open","base") from _call_her_main_3574

                    menu:
                        "\"Just take your points and go!\"":
                            call her_main(".........................","normal","base") from _call_her_main_3575
                        "\"Favour failed! No points for you!\"":
                            $ mad +=15
                            call her_main("But [genie_name]?","normal","frown") from _call_her_main_3576
                            m "You are dismissed, [hermione_name]."
                            call her_main(".........................................","angry","angry") from _call_her_main_3577
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
            
            #Third level.
            elif whoring >= 9:

                #Event A
                if one_out_of_three == 1: ### Filch
                    stop music fadeout 1.0
                    call her_main(".............................","normal","worriedCl",xpos="right",ypos="base") from _call_her_main_3578
                    her "....................................."
                    m "[hermione_name]?"
                    call her_main("[genie_name], I.....","angry","worriedCl",emote="05") from _call_her_main_3579
                    m "What is it? What happened?"
                    call her_main("Well...","annoyed","worriedL") from _call_her_main_3580
                    her "It's mr.Filch, [genie_name]..."
                    m "The janitor?"
                    call her_main("I flirted with him a little...","open","base") from _call_her_main_3581
                    her "And it went great at first..."
                    call her_main(".......................","annoyed","worriedL") from _call_her_main_3582
                    m "................?"
                    call her_main("And then...","open","base") from _call_her_main_3583
                    call her_main("Not sure if I should...","annoyed","worriedL") from _call_her_main_3584
                    m "[hermione_name], if you are not going to speak up, you may as well leave."
                    call play_music("chipper_doodle") from _call_play_music_147 # HERMIONE'S THEME.
                    call her_main("He showed me his \"thing\", [genie_name]!","scream","worriedCl") from _call_her_main_3585
                    m "His what?"
                    call her_main("His... manhood, [genie_name].","angry","worriedCl",emote="05") from _call_her_main_3586
                    g9 "Way to go, Janitor-guy!"
                    call her_main("What?!","scream","wide_stare") from _call_her_main_3587
                    m "*Khem* I mean, this is unspeakable!"
                    call her_main("Yes... Vile crooked thing all covered in veins...","angry","base",tears="soft") from _call_her_main_3588
                    m "Spare me the grisly details, [hermione_name]."
                    call her_main("Why would he do such a thing?","mad","worriedCl",tears="soft_blink") from _call_her_main_3589
                    her "One second we were just talking and then..."
                    m "Well, your noble  sacrifice shall not go unnoticed, [hermione_name]!"
                    m "Fifteen points to \"Gryf--"
                    call her_main("Professor, please wait.","soft","base",tears="soft") from _call_her_main_3590
                    m "Huh?"
                    call her_main("Well, aren't you going to do something about this?","open","base") from _call_her_main_3591
                    m "Well..."
                    call her_main("What if I am not the first victim..?","angry","angry") from _call_her_main_3592
                    her "Some unfortunate freshman could be traumatized for life!"
                    m "And who wouldn't be really?"
                    call her_main("Does this mean you will take action, [genie_name]?","open","base") from _call_her_main_3593
                    m "uhm... Yeah, sure..."
                    m "There! Putting it on my \"to-do-list\"..."
                    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
                    m "Yes, first thing tomorrow."
                    call her_main("Thank you [genie_name].","open","closed") from _call_her_main_3594
                    call her_main("Can I have my points now?","smile","happyCl") from _call_her_main_3595
    
                #Event B
                elif one_out_of_three == 2: ### Snape
                    call play_music("chipper_doodle") from _call_play_music_148 # HERMIONE'S THEME.
                    call her_main("Professor Snape!","angry","angry",emote="01",xpos="right",ypos="base") from _call_her_main_3596
                    m "Ehm... Yeah, I'm pretty sure it's Dumbledore or something..."
                    call her_main("[genie_name], please, you need to listen to me!","open","base") from _call_her_main_3597
                    m "Yes, yes, [hermione_name], I'm listening."
                    call her_main("I just confirmed that professor Snape is corrupted and \"dirty\", [genie_name]!","open","angryCl") from _call_her_main_3598
                    m "Tell me what happened."
                    
                    hide screen hermione_main
                    hide screen blktone
                    call blkfade from _call_blkfade_142
                    
                    call her_head("Well, during classes today...","open","base",xpos="base",ypos="base") from _call_her_head_952
                    call her_head("I have been doing my best to attract professor Snape's attention...","open","baseL") from _call_her_head_953
                    call her_head("I have been giving him \"dreamy looks\"...","open","down") from _call_her_head_954
                    call her_head("And I've been eyeing his crotch...","soft","baseL") from _call_her_head_955
                    m "You..."
                    m "Eyed his crotch?"
                    call her_head("Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly...","open","angryCl") from _call_her_head_956
                    m "Where do you get this stuff?"
                    call her_head("Women's magazines...","open","worriedL") from _call_her_head_957
                    call her_head("Well, anyway, it worked, [genie_name].","normal","frown") from _call_her_head_958
                    
                    hide screen blkfade
                    show screen snape_groping
                    with fade
                    call ctc from _call_ctc_260
                    
                    call her_head("As soon as the class was over, professor Snape grabbed my buttocks, [genie_name]!","angry","angry") from _call_her_head_959
                    m "The fiend!"
                    m "Did you enjoy it, though?"
                    call her_head("[genie_name], I am only doing this--","scream","angryCl") from _call_her_head_960
                    m "Go \"Gryffindors\"! honour and all that. Yes, I remember."
                    call ctc from _call_ctc_261
                    
                    hide screen snape_groping
                    with fade
                    
                    m "Here are your points."
                    show screen blktone
                    call her_main("","disgust","glance",xpos="right",ypos="base") from _call_her_main_3599
  
                #Event C
                elif one_out_of_three == 3: ### Lockhart
                    stop music fadeout 1.0
                    call her_main("Professor Lockhart!","annoyed","frown",xpos="right",ypos="base") from _call_her_main_3600
                    m "Got it! Adding him to the \"Naughty list\"!"
                    call her_main("No, [genie_name], it's not that...","open","worried") from _call_her_main_3601
                    call her_main("Or...","annoyed","angryL") from _call_her_main_3602
                    her "I'm not sure..."
                    call her_main("I used to adore him...","open","worried") from _call_her_main_3603
                    call her_main("But he...","soft","baseL") from _call_her_main_3604
                    her "He just..."
                    call her_main("How is this possible?","mad","worriedCl",tears="soft_blink") from _call_her_main_3605
                    her "I can't believe this..."
                    hide screen hermione_main
                    with d3
                    call play_music("playful_tension") from _call_play_music_149# SEX THEME.
                    m "{size=-4}(Agh! The suspense is killing me!){/size}" 
                    m "{size=-4}(Did he force her to blow him?){/size}"
                    m "{size=-4}(Did he rape her?){/size}"
                    g4 "What was it, [hermione_name]? Speak up!"
                    call her_main("Huh?","open","base") from _call_her_main_3606
                    m "What did Professor Lockhart do to you?"
                    call her_main("Ehm... Nothing, [genie_name]...","soft","baseL") from _call_her_main_3607
                    m "Nothing?!"
                    call her_main("Yes, I sort of cornered mr.Lockhart today...","open","worried") from _call_her_main_3608
                    call her_main("And I also may have sort of made a pass at him...","open","base") from _call_her_main_3609
                    m "Seriously?"
                    call her_main("Yes... Not sure what had gotten into me, [genie_name]...","angry","worriedCl",emote="05") from _call_her_main_3610
                    m "Way to go, [hermione_name]!"
                    call her_main("Hear me out first [genie_name], please!","scream","worriedCl") from _call_her_main_3611
                    m "My apologies. Please continue."
                    call her_main("Well, I always knew that mr.Lockhart was a true gentleman and...","open","base") from _call_her_main_3612
                    her "And... and I just wanted to clear his name from any suspicions once and for all..."
                    call her_main("...............","annoyed","worriedL") from _call_her_main_3613
                    her "Well mr.Lockhart did not reject me..."
                    m "You are killing me [hermione_name]!"
                    m "He didn't reject you, he didn't rape you..."
                    m "What the hell happened then?"
                    call her_main(".............","normal","worriedCl") from _call_her_main_3614
                    call play_music("chipper_doodle") from _call_play_music_150 # HERMIONE'S THEME.
                    call her_main("I made him cry, [genie_name]...","angry","worriedCl",emote="05") from _call_her_main_3615
                    m "..............wait.......what?"
                    call her_main("He gave me a bewildered look and then started to sob...","angry","worried") from _call_her_main_3616
                    her "He looked like he was genuinely afraid of me, [genie_name]."
                    call her_main("I think...","annoyed","worriedL") from _call_her_main_3617
                    her "I think mr.Lockhart might be afraid of women..."
                    m "Afraid of women?"
                    m "What is that supposed to mean?"
                    call her_main("That he is into boys, [genie_name]?","angry","worriedCl",emote="05") from _call_her_main_3618
                    m "Oh..."
                    call her_main("............","upset","wink") from _call_her_main_3619
                    m "..........."
                    m "Well, I bet it was a traumatizing experience for you, [hermione_name]."
                    call her_main("It was, [genie_name]...","open","base") from _call_her_main_3620
                    m "Well, I hope these points will make you feel better."
    
    $ gryffindor +=15
    m "The \"Gryffindors\" gets 15 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_FlirtTeacher_OBJ.points += 1
    $ hg_pr_FlirtTeacher_OBJ.inProgress = False
    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1
    if whoring >= 5 and hg_pr_FlirtTeacher_OBJ.points >= 2:
        $ hg_pr_FlirtTeacher_OBJ.complete = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.

