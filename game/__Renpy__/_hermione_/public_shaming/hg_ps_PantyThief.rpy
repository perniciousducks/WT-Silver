

### Panty Thief ###

################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label hg_ps_PantyThief: #(Whoring = 3 - 5)
    hide screen hermione_main
    with d3
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    m "[hermione_name]?"
    call her_main("I am listening, [genie_name].",xpos="right",ypos="base") from _call_her_main_5564
    m "I will need your panties..."
    
    if whoring <=2:
        jump too_much
    
    if hg_ps_PantyThief_OBJ.points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_heart = 1 #Event hearts level (0-3)
        $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)
        
        call her_main("W-what?","open","worried") from _call_her_main_5565
        her "My... panties...?"
        her "[genie_name], this is..."
        m "This is the favour I will be buying from you today, [hermione_name]..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my...."
        call play_music("chipper_doodle") from _call_play_music_231 # HERMIONE'S THEME.
        call her_main("...panties, [genie_name]?","angry","angry") from _call_her_main_5566
        m "Yes I do..."
        call her_main("May I ask what you are planning to do with them...?","disgust","glance") from _call_her_main_5567
        m "Ehm...I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from \"Slytherin\"..."
        m "Are selling favours for house points, [hermione_name]?"
        call her_main("Yes I do!","angry","angry") from _call_her_main_5568
        call her_main("(Those \"Slytherin\" tramps have no dignity.)","annoyed","angryL") from _call_her_main_5569
        m "Well, there you go then!"
        call her_main("Huh?","disgust","glance") from _call_her_main_5570
        m "Beat them at their own game!"
        call her_main("What?","open","base") from _call_her_main_5571
        m "Yes! Don't just put the \"Gryffindor\" house back on top..."
        m "But do it by beating them at their own game!"
        call her_main("[genie_name]...","open","worried") from _call_her_main_5572
        m "As headmaster, I cannot play favourites. But you know how I feel about \"Gryffindor\"..."
        m "I wish I could give you the points but that would ruin the system..."
        hide screen hermione_main
        with d3
        call nar(">Suddenly Hermione extends her arm to you...","start") from _call_nar_581
        call nar(">You see that she is clutching a little piece of fabric in her fist...","end") from _call_nar_582
        #">Her panties? You can't help but wonder when she managed to take them off..."
        m "??!"
        call nar(">You acquired Hermione's panties...") from _call_nar_583
        call her_main("Just take them, [genie_name]...","mad","worried",tears="soft") from _call_her_main_5573
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, [genie_name]! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        call her_main("...........","normal","baseL",tears="soft") from _call_her_main_5574
        call her_main("...I hope nobody will notice that I have no underwear on today...","annoyed","worriedL") from _call_her_main_5575
        call her_main("Oh, and I will be back tonight to pick them up, [genie_name].","open","base") from _call_her_main_5576
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        call her_main(".............","angry","worriedCl",emote="05") from _call_her_main_5577
        jump hg_ps_PantyThief_ends

    else: #<========================================================================================== FIRST EVENT!
        if hg_ps_PantyThief_OBJ.points >= 1:
            her "Again, [genie_name]?"
            m "Yes, again..."
        her "Here..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            call nar(">Hermione pulls her panties out of her pocket...") from _call_nar_584
            m "What?"
            call her_main("Yes, I had a feeling that you might ask for these today, [genie_name].","base","base") from _call_her_main_5578
            m "A feeling?"
            call her_main("Well, to be completely honest I just do not bother to wear them much anymore...","grin","baseL") from _call_her_main_5579
        else:
            hide screen hermione_main
            with d3
            call nar(">Hermione takes off her panties and hands them over to you...") from _call_nar_585
        call nar(">Hermione's panties acquired.") from _call_nar_586
        call her_main("Well, the classes are about to start, so I'd better go now...","soft","base") from _call_her_main_5580
    
    label hg_ps_PantyThief_ends:
        
    $ hg_ps_PantyThief_OBJ.inProgress = True #True when Hermione has no panties on.
    
    hide screen blktone
    
    call her_walk("mid","leave",2) from _call_her_walk_115
    
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu
        
label hg_ps_PantyThief_soaked:### PANTIES SOAKED IN CUM ###
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        call her_main("Hm....?","annoyed","down",xpos="right",ypos="base") from _call_her_main_5581
        call her_main("[genie_name]? What is this?","angry","angry") from _call_her_main_5582
        her "What have you done to them?"
        call her_main("They are covered in something slimy...","normal","frown") from _call_her_main_5583
        
        menu:
            "\"An experiment went wrong\"":
                call her_main("An experiment went wrong, [genie_name]?","open","base") from _call_her_main_5584
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? He-he..."
                call her_main(".....................?","normal","frown") from _call_her_main_5585
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                call her_main("................................","angry","angry") from _call_her_main_5586
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [genie_name]!"
                her ".........................."
                
        call her_main("Well, these will require some serious cleaning before I can put them on again...","annoyed","down") from _call_her_main_5587
        m "Or you could put them on now."
        call her_main("What?","open","base") from _call_her_main_5588
        call her_main("I really would rather not, [genie_name]...","soft","baseL") from _call_her_main_5589
        
        menu:
            "\"Put them on or lose the points!\"":
                $ mad +=7
                call her_main("What?","scream","wide_stare") from _call_her_main_5590
                her "[genie_name], you are joking, right?"
                m "I am not..."
                call her_main("B-but...","open","base") from _call_her_main_5591
                call her_main("........................................","normal","worriedCl") from _call_her_main_5592
                call her_main("(Must you always have your way, [genie_name]?)","angry","angry") from _call_her_main_5593
                m "What was that, [hermione_name]?"
                call her_main("It's nothing, [genie_name].","scream","angryCl") from _call_her_main_5594
                her "Putting my panties back on!"
                hide screen hermione_main
                call nar(">Hermione hesitantly puts on her panties...","start") from _call_nar_587
                ">A tiny stream of cum trickles down one of her legs..."
                call nar(">Hermione looks very uncomfortable...","end") from _call_nar_588
                call her_main("......................","angry","worriedCl",emote="05") from _call_her_main_5595
            "\"Well, suit yourself...\"":
                pass
                
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        call her_main("My panties...","annoyed","down",xpos="right",ypos="base") from _call_her_main_5596
        call her_main("What happened to them [genie_name]?","annoyed","down") from _call_her_main_5597
        
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
                
        hide screen hermione_main
        call nar(">Hermione gives her cum-soaked underwear a quizzical look...") from _call_nar_589
        call her_main("Seems like these will require some serious cleaning before I can put them on again...","annoyed","down") from _call_her_main_5598
        m "Why not put them on now?"
        call her_main("Hm....?","annoyed","suspicious") from _call_her_main_5599
        call her_main("Well, I suppose I could wear them one more time before putting them into laundry...","annoyed","down") from _call_her_main_5600
        hide screen hermione_main
        call nar(">Hermione puts the panties on...") from _call_nar_590
        call her_main("(This feels funny...)","angry","worriedCl",emote="05") from _call_her_main_5601
        call her_main("Will this be all, [genie_name]?","upset","wink") from _call_her_main_5602
        
    if whoring >= 9 and whoring <= 15: #LEVEL 04+ (THIRD EVENT)
        call her_main("My panties...","annoyed","down",xpos="right",ypos="base") from _call_her_main_5603
        if hg_ps_PantyThief_SoakedPantiesFlag:
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        call her_main("Hm... That smell...","annoyed","worriedL") from _call_her_main_5604
        her "It's familiar somehow..."
        call her_main("What exactly did you do to them, [genie_name]?","base","base") from _call_her_main_5605
        
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                call her_main("No, don't answer that... I think I know...","smile","baseL") from _call_her_main_5606
            "\"You gave them to me like this!\"":
                her "I don't think so, [genie_name]."
                her "But it's alright if you don't want to tell me, [genie_name]..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                call her_main("I knew it...","smile","glance") from _call_her_main_5607
                her "They reek of semen!"
                
        call her_main("Hm...","grin","baseL") from _call_her_main_5608
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?","smile","glance") from _call_her_main_5609
        
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Well, if I must..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        call her_main("I am only doing this to give my house a fair chance at winning the cup this year...","base","happyCl") from _call_her_main_5610
        m "Right..."
        hide screen hermione_main
        call nar(">Hermione swiftly slides her drenched panties on...") from _call_nar_591
        
    elif whoring > 15: ###New variant of the event
        call her_main("My panties...","base","ahegao_raised",xpos="right",ypos="base") from _call_her_main_5611
        if hg_ps_PantyThief_OBJ.points >= 1:
            her "You came all over them again..."
        else:
            her "You came all over them..."
        call her_main("Hm...","grin","baseL") from _call_her_main_5612
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?","smile","glance") from _call_her_main_5613
        
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Yes [genie_name]..."
                call her_main("I am only doing this to give my house a fair chance at winning the cup this year.","smile","happyCl") from _call_her_main_5614
                call her_main("I don't like how it feels at all...","base","ahegao_raised") from _call_her_main_5615
                m "Right..."
                hide screen hermione_main
                call nar(">Hermione swiftly slides her drenched panties on...") from _call_nar_592
                call her_main("...","soft","ahegao") from _call_her_main_5616
            "\"Why don't you clean them now?\"":
                $ cleaned_panties = True
                call her_main("Clean them How? You don't have a wash basin in here.","open","base") from _call_her_main_5617
                m "You're right, you'll have to use your mouth then."
                call her_main("My mouth?!","scream","wide_stare") from _call_her_main_5618
                m "What's the big deal? It wouldn't be the first time you've tasted my cum."
                call her_main("It's a bit different! I wore these panties before I gave them to you.","scream","angryCl") from _call_her_main_5619
                call her_main("Not to mention that your cum is all cold and slimey...","scream","worriedCl") from _call_her_main_5620
                m "Well in that case hand them back."
                call her_main("What? Can't I just put them on?","angry","wink") from _call_her_main_5621 
                m "I'm afraid not, you clean them now or you hand them back."
                call her_main("{size=-4}Fine...{/size}","angry","down_raised") from _call_her_main_5622
                m "What was that?"
                call her_main("I said I'll clean them ok!","shock","worriedCl") from _call_her_main_5623
                m "Well..."
                call her_main("...","angry","down_raised") from _call_her_main_5624
                call nar(">Hermione reluctantly puts her cum-soaked panties in her mouth.") from _call_nar_593
                call her_main("Mmmmhhhhh!","full","ahegao_intense") from _call_her_main_5625
                m "That's it, not as bas as you thought now is it?"
                call her_main("...","full","narrow") from _call_her_main_5626
                m "Make sure you get them nice and clean now..."
                call her_main("*gulp*","full_cum","down",cheeks="blush") from _call_her_main_5627
                m "That's it. Do you think they're clean yet."
                call her_main("*Mmmhhhmmm*","full_cum","dead") from _call_her_main_5628
                m "Well then you can probably take them out of your mouth."
                call her_main("*Ahhhhh*","open_wide_tongue","ahegao") from _call_her_main_5629
                m "There, nice and clean."
                call her_main("*Yes [genie_name]*","soft","ahegao") from _call_her_main_5630
    
    jump back_from_soaked
    
label hg_ps_PantyThief_complete: # WHORING LEVEL 02 <=================
    $ hg_ps_PantyThief_OBJ.complete = True
    
    call play_sound("door") from _call_play_sound_199 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_116
    pause.5
    
    call her_main("Good evening, [genie_name]...","base","base",xpos="right",ypos="base") from _call_her_main_5631
    call play_music("chipper_doodle") from _call_play_music_232 # HERMIONE'S THEME.
    
    menu:
        "\"Here are your panties.\"":
            if hg_ps_PantyThief_SoakedPantiesFlag:
                jump hg_ps_PantyThief_soaked
            else:
                her "Thank you, [genie_name]."
                her "And my payment?"
                m "Of course."
                
        "\"How was your day, [hermione_name]?\"":
            if  whoring <= 5: #WHORING LVL 02. EVENT LEVEL: 01
                $ new_request_03_heart = 1 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)
                $ sc34CG(1, 10)
                call her_main("Oh...","soft","base",xpos="base",ypos="base") from _call_her_main_5632
                her "Quite ordinary actually..."
                call her_main("Although... I couldn't help but worry that somebody would notice somehow...","soft","baseL") from _call_her_main_5633
                call her_main(".....","annoyed","worriedL") from _call_her_main_5634
                hide screen sccg 
                call her_main("Can I have my panties back now?","open","base",xpos="right",ypos="base",trans="fade") from _call_her_main_5635
                m "Of course..."
                hide screen hermione_main
                with d3
                call nar(">You give Hermione her panties back...") from _call_nar_594
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("And my payment?","open","base") from _call_her_main_5636
                    m "Yes, yes..."
                    
            elif whoring >= 6 and whoring <= 8: #WHORING LVL 03. EVENT LEVEL 02.
                $ new_request_03_heart = 2 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 2 #Event hearts level (0-3)
                $ sc34CG(1, 5)
                call her_main("Oh...","soft","base",xpos="base",ypos="base") from _call_her_main_5637
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                call her_main("I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"...","open","closed") from _call_her_main_5638
                call her_main("I felt bad that I had to give the speech without any underwear on...","annoyed","angryL") from _call_her_main_5639
                hide screen sccg
                call her_main(xpos="right",ypos="base",trans="fade") from _call_her_main_5640
                
                menu:
                    "\"You little hypocrite!\"":
                        $ mad +=5
                        call her_main("[genie_name]?","open","base") from _call_her_main_5641
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behaviour..."
                        #m "What would you call this?"
                        #call her_main("I know you are right, [genie_name]...","annoyed","angryL")
                        call her_main("(But we need the points...)","annoyed","angryL") from _call_her_main_5642
                        call her_main("Can I have my payment now please?","disgust","glance") from _call_her_main_5643
                        m "What about your panties?"
                        call her_main("Oh, them too of course...","angry","worriedCl",emote="05") from _call_her_main_5644 
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            pass
                    "\"It's for the greater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        call her_main("I shall remain a symbol of righteousness to my peers, no matter what!","open","closed") from _call_her_main_5645
                        call her_main("Can I have my panties back now, please?","open","base") from _call_her_main_5646
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            her "And my payment."
                            
            elif whoring >= 9: #WHORING LVL 04. EVENT LEVEL 03.
                $ new_request_03_heart = 3 #Event hearts level (0-3)
                $ hg_ps_PantyThief_OBJ.hearts_level = 3 #Event hearts level (0-3)
                $ sc34CG(1, 11)
                call her_main("Another ordinary day at hogwarts...","open","closed",xpos="base",ypos="base") from _call_her_main_5647
                her "Nothing worth mentioning happened today..."
                call her_main("Although I have to admit...","annoyed","worriedL") from _call_her_main_5648
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                hide screen sccg
                call her_main("Can I have my panties back now please?","base","base",xpos="right",ypos="base",trans="fade") from _call_her_main_5649
                m "Of course..."
                hide screen hermione_main
                with d3
                call nar(">You give Hermione her panties back...") from _call_nar_595
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("And my payment?","base","base") from _call_her_main_5650
                    m "Yes, yes..."
                    
    label back_from_soaked:
    if hg_ps_PantyThief_SoakedPantiesFlag and whoring >= 9 and whoring <= 15 :
        m "You can go now."
        call her_main("What about my points?","scream","angryCl") from _call_her_main_5651
        m "You still want points after I just gave you a gift?"
        her "What gift?"
        m "You're wearing it"
        her "What, semen soaked panties?"
        m "if you'd prefer the points then just take them off"
        call her_main("well... I am already wearing them","annoyed","worriedL") from _call_her_main_5652
        m "then say thank you for the gift"
        call her_main("Thank you, [genie_name]...","annoyed","suspicious") from _call_her_main_5653
        m "You can go now."
        her "Good night, [genie_name]."
    elif hg_ps_PantyThief_SoakedPantiesFlag and whoring > 15:
        $ hg_ps_PantyThief_OBJ.hearts_level = 4 #Event hearts level (0-4)
        m "You can go now."
        call her_main("yes, [genie_name]","angry","down_raised") from _call_her_main_5654
        m "After you say thank you. "
        call her_main("Thank you for what?","angry","wink") from _call_her_main_5655
        m "For my cum"
        call her_main("...","base","down") from _call_her_main_5656
        call her_main("Thank you for your cum [genie_name]...","grin","dead") from _call_her_main_5657
        m "You may go now."
        her "Good night, [genie_name]."
    else:
        $ gryffindor +=15
        m "Fifteen points to \"Gryffindor\", [hermione_name]. Well deserved." 
        her "Thank you, [genie_name]..."
        m "You can go now."
        her "Good night, [genie_name]."
        #m "Yes, good night..."
    
    if whoring <= 5:
        $ whoring +=1
    
    $ hg_ps_PantyThief_OBJ.points += 1
    $ hg_ps_PantyThief_OBJ.inProgress = False #False when favor is not in progress
    $ hg_ps_PantyThief_SoakedPantiesFlag = False #TRUE if you jerked off in panties
    
    hide screen hermione_main
    hide screen blkfade
    hide screen bld1
    hide screen blktone 
    call her_chibi("stand","mid","base") from _call_her_chibi_174
    show screen genie
    with d3
    
    call her_walk("mid","leave",2) from _call_her_walk_117
    
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu

