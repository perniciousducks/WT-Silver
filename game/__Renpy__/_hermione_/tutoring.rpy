label l_tutoring_check:
    if v_tutoring == 0:
        jump l_tutoring
    elif v_tutoring == 1 and whoring >= 1:
        jump l_tutoring
    elif v_tutoring == 2 and whoring >= 2:
        jump l_tutoring
    elif v_tutoring == 3 and whoring >= 3:
        jump l_tutoring
    elif v_tutoring == 4 and whoring >= 5:
        jump l_tutoring
    elif v_tutoring == 5 and whoring >= 8:
        jump l_tutoring
    elif v_tutoring == 6 and whoring >= 11:
        jump l_tutoring
    elif v_tutoring == 7 and whoring >= 14:
        if gift_item_inv[6] >= 1:# Adult magazines
            jump l_tutoring
        else:
            m "I need to buy adult magazines for this lesson."
    elif v_tutoring == 8 and whoring >= 17:
        if gift_item_inv[7] >= 1:# Porn magazines
            jump l_tutoring
        else:
            m "I need to buy porn magazines for this lesson."
    elif v_tutoring == 9 and whoring >= 20:
        if gift_item_inv[11] >= 1:# Vibrator
            jump l_tutoring
        else:
            m "I need to buy a vibrator for this lesson."
    elif v_tutoring == 10 and whoring >= 23:
        if gift_item_inv[14] >= 1:# Anal plugs
            jump l_tutoring
        else:
            m "I need to buy anal plugs for this lesson."
    elif v_tutoring == 11 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 12 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 13 and whoring >= 23:
        jump l_tutoring
    else:
        m "Not the right time. Soon..."

    jump day_time_requests

label l_tutoring:
    $ d_flag_01 = False

    if v_tutoring == 0:   # Whoring lvl 0
        
        call her_main("Of course, sir.","open","base") from _call_her_main_2511
        her "I'll go get my books then."
        
        hide screen hermione_main
        play sound sd_door
        call blkfade from _call_blkfade_114
      
        play sound sd_door
        pause.3

        call h_action("hold_book") from _call_h_action_46
        call her_main("","base","base",xpos="mid",ypos="base") from _call_her_main_2512
        
        call hide_blkfade from _call_hide_blkfade_70

        call ctc from _call_ctc_227
       
        call her_main("Again, thank you for doing this for me, sir...","open","base",xpos="base",ypos="base") from _call_her_main_2513
        m "..........."
        call her_main("Sir?","soft","baseL") from _call_her_main_2514
        m "It's time to talk about your future, child."
        stop music fadeout 1.0
        call her_main("I'm not a child anymore, professor!","normal","frown") from _call_her_main_2515
        m "In a way you're right, but..."
        her "..........."
        m "I can tutor you, but you need to understand certain things about magic."
        m "With proper training, you can learn to increase your magic ability."
        play music ms_manatees fadein 1 fadeout 1
        call her_main("Yes?","soft","baseL") from _call_her_main_2516
        m "Certain emotions like love and hate, pleasure and pain..."
        g9 "{size=-2}(If she falls for that, I'm a true genius!){/size}"
        call her_main("I've been studying magic for years and I've never heard of such a thing.","normal","base") from _call_her_main_2517
        g4 "{size=-2}(Shit.){/size}"
        m "And that's exactly why you're still a child. You still have much to learn about magic."
        call her_main("Please stop that, professor. Nobody considers me a child anymore.","open","base") from _call_her_main_2518
        m "Yes, technically..."
        call her_main("Technically?!","open","base") from _call_her_main_2519
        g4 "Enough of this. You came to me to ask for my help, and if it starts like that..."
        call her_main("Yes, I suppose you are right...","angry","angry") from _call_her_main_2520
        call her_main("Alright, I'm ready to study hard with you!","base","base") from _call_her_main_2521
        g9 "{size=-2}(Yes!){/size}"
        call her_main("What was that?","open","annoyed",cheeks="blush") from _call_her_main_2522
        m "Uh, yes I'm glad you're beginning to understand, child."
        her "..........."
        m "Alright, I want you to take some time and think about what I've said. Next time we'll start with your first lesson."
        call her_main("Can't we start now?","open","base") from _call_her_main_2523
        m "Miss Granger, you're not the only student I must take care of."
        call her_main("You're tutoring someone else?","open","base") from _call_her_main_2524
        m "{size=-2}(If only...){/size}"
        m "I must take care of all the students of this school."
        m "But yes, there is another girl who needs..."
        call her_main("A Slytherin girl?!","scream","wide") from _call_her_main_2525
        g9 "That is none of your business, miss Granger."
        call her_main("Yes, professor. I'm sorry, but with all the recent events I'm a little on edge.","angry","angry") from _call_her_main_2526
        m "Apology accepted, and now goodnight!"
        call her_main("Good night, professor, and thanks again for taking some of your precious time to help me.","base","base") from _call_her_main_2527
        hide screen hermione_main
        
        call nar("You dismiss Hermione.") from _call_nar_402
        
        call her_walk("mid","door",3) from _call_her_walk_73
        
        call her_head("{size=-4}(I'm glad the professor agreed to tutor me!){/size}","base","worriedCl",cheeks="blush",xpos="base",ypos="base") from _call_her_head_897
        call her_head("{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}","annoyed","baseL") from _call_her_head_898
        call her_chibi("leave") from _call_her_chibi_112
        
        $ v_tutoring = 1
        $ aftercum = False
        jump day_start

    if v_tutoring == 1:   # Whoring lvl 1
        
        hide screen hermione_main
        call h_action("hold_book") from _call_h_action_47

        call her_main("","base","base",trans="fade") from _call_her_main_2528
        m "Miss Granger, time for your first lesson."
        call her_main("Yes, professor.","soft","baseL") from _call_her_main_2529
        m "You've brought your books again, I don't think we'll need them for the moment."
        call her_main("Too bad, I love books.","normal","base") from _call_her_main_2530
        hide screen hermione_main
        with d3

        call h_action("none") from _call_h_action_48

        g9 "{size=-2}(And soon you'll love cock!){/size}"
        $ renpy.play('sounds/punch01.mp3') #Hermione lays books onto the floor.

        call her_main("Yes?","soft","baseL") from _call_her_main_2531
        m "It's nothing, I was just thinking about our next lesson."
        call her_main("{size=-2}(The elderly...){/size}","angry","angry") from _call_her_main_2532
        m "............."
        m "Anyway, have you thought about what we discussed?"
        call her_main("Not really, I'm not sure what you mean by \"emotions\".","normal","base") from _call_her_main_2533
        g9 "{size=-2}(You'll learn soon enough, girl.){/size}"
        m "For example, what was your state of mind when you heard those rumours about the Slytherin girls?"
        call her_main("Please don't bring that up, sir! it really makes me mad!","scream","wide") from _call_her_main_2534
        m "And what is this feeling?"
        call her_main("...{w=0.5}an emotion, I suppose...","normal","base") from _call_her_main_2535
        m "Yes, and don't you have emotions you prefer over others?"
        call her_main("When I have the best score at a test.","smile","happyCl") from _call_her_main_2536
        m "{size=-2}(This girl is a monomaniac...){/size}"
        m "Don't you have other passions, things you like to do?"
        call her_main("Yes! Studying and reading books.","smile","happyCl") from _call_her_main_2537
        g4 "{size=-2}(By all the ancient gods...){/size}"
        m "Things are not going in the right direction..."
        call her_main("And what direction is that, sir?","normal","base") from _call_her_main_2538
        g9 "{size=-2}(You impaled on my cock!){/size}"
        m "Adulthood, Miss Granger, adulthood..."
        call her_main("I am by far the most mature of my peers, professor. What more can you ask?","open","closed") from _call_her_main_2539
        m "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn."
        m "I'm tired of all this, and I have work to do. Goodnight, child."
        call her_main("Tutoring one of those filthy Slytherin girls, maybe?","open","annoyed",cheeks="blush") from _call_her_main_2540
        m "Maybe that's the right direction, think about what all those girls do with professors."
        call her_main("But...{w=0.5} that's so wrong...{w=0.8} I don't know if I want to think about that.","open","base") from _call_her_main_2541
        m "If you want to progress and to restore the Gryffindor pride, you must!"
        call her_main("Yes, you're right! It's my mission! I'll do my best, professor.","grin","angry",cheeks="blush") from _call_her_main_2542
        g9 "{size=-2}(She is so naive, it's adorable.){/size}"
        m "Good, now time to go to bed, child."
        call her_main("{size=-2}(Tsh... Like I'm going to bed at this time, I need to study more.){/size}","normal","frown") from _call_her_main_2543
        hide screen hermione_main
        call nar("You dismiss Hermione.") from _call_nar_403
        
        call her_walk("mid","door",2) from _call_her_walk_74
        
        call her_head("{size=-4}(Filthy whores...){/size}","angry","angryCl",cheeks="blush") from _call_her_head_899
        call her_head("{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels so good!){/size}","base","worriedCl",cheeks="blush") from _call_her_head_900
        call her_chibi("leave") from _call_her_chibi_113
        
        $ v_tutoring = 2
        $ aftercum = False
        jump day_start

    elif v_tutoring == 2:   # Whoring lvl 2
        m "Good, you didn't bring your books this time."
        call her_main("Not that I agree with it. All the knowledge I need is in those books.","annoyed","angryL") from _call_her_main_2544
        m "Books can't teach you everything, some knowlege only comes with practice and experience!"
        call her_main("Maybe... I mean, you're not chosen as the head of Hogwarts by chance.","annoyed","suspicious") from _call_her_main_2545
        m "Sometimes you seem to forget that, Miss Granger."
        call her_main("That sounded like something professor Snape would say...","open","suspicious") from _call_her_main_2546
        call her_main(".........","annoyed","suspicious") from _call_her_main_2547
        call her_main("Sorry about that, he thinks he's always right and it annoys me.","smile","happyCl") from _call_her_main_2548
        m "Not unlike you, miss Granger..."
        call her_main("I suppose you have a point...","annoyed","angryL",cheeks="blush") from _call_her_main_2549
        m "From now on I hope it's clear."
        call her_main("Yes, professor Dumbledore.","disgust","down_raised",cheeks="blush") from _call_her_main_2550
        m "So, have you thought about emotions and their usefulness in the practice of magic?"
        call her_main("Yes, first I tried to cast a spell while thinking of the behavior of those Slytherin girls.","open","closed") from _call_her_main_2551
        call her_main("It made me so angry and confused that I lost my focus and failed miserably.","annoyed","base") from _call_her_main_2552
        call her_main("I don't think it helps at all.","annoyed","suspicious") from _call_her_main_2553
        m "That's your problem Miss Granger, you think you already know the answer and don't follow my instructions."
        m "I don't care about the behavior of those girls."
        call her_main("What? Professor! You don't care?!","scream","wide_stare") from _call_her_main_2554
        g9 "{size=-2}(Oh, I do care, just not in the way you think.){/size}"
        m "For this exercise, Miss Granger, for this exercise. Don't get on your high horse."
        call her_main(".........","annoyed","ahegao") from _call_her_main_2555
        call her_main("Sorry about that, {w=0.5}again.","open","suspicious") from _call_her_main_2556
        m "I need you to focus on what those girls do with professors, not their behavior in general."
        call her_main("But...","open","base",cheeks="blush") from _call_her_main_2557
        m "Last time you were talking about your sacred duty and at the first hurdle you hesitate."
        call her_main("{size=-2}(\"Sacred\"? Don't exagerate, old man){/size}","annoyed","down") from _call_her_main_2558
        call her_main("{size=-2}(Or not! Maybe I'll be remembered later for being the savior of Gryffindor house!){/size}","open","worriedCl",cheeks="blush") from _call_her_main_2559
        call her_main("Yes, you're right! It {b}is{/b} my sacred duty!","smile","baseL") from _call_her_main_2560
        g9 "{size=-2}(It works every time, it's too easy... She looks so proud of herself.){/size}"
        call her_main("I'll do my best, professor!","open","base",cheeks="blush") from _call_her_main_2561
        g9 "I'm excited too... uh, I'm sure you will."
        call her_main("I'm glad you have such high confidence in me.","grin","worriedCl") from _call_her_main_2562
        m "And I'm glad you're starting to believe in this. I think you have the potential to master this branch of magic."
        call her_main("You seem tired, professor.","open","suspicious") from _call_her_main_2563
        g11 "{size=-2}(Tired of waiting to annihilate your ass.){/size}"
        call her_main("Yes, professor?","annoyed","base") from _call_her_main_2564
        g9 "Yes we can!"
        m "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?"
        call her_main("Sleep? I must study first.","open","closed") from _call_her_main_2565
        m "I wasn't thinking about that, but you're right, time to go to bed!"
        m "Just make sure to think about what you learned today."
        hide screen hermione_main
        call nar("You dismiss Hermione.") from _call_nar_404
        
        call her_walk("mid","door",2) from _call_her_walk_75
        
        call her_head("{size=-4}(Hmm, I wonder what he {b}was{/b} thinking about.){/size}","base","down_raised",cheeks="blush") from _call_her_head_901
        call her_head("{size=-4}(Probably all the problems caused by those harlots.){/size}","base","glance",cheeks="blush") from _call_her_head_902
        call her_head("{size=-4}(Well, I will never be like them, so no need to worry.){/size}","silly","glance",cheeks="blush") from _call_her_head_903
        call her_chibi("leave") from _call_her_chibi_114
        
        $ v_tutoring = 3
        $ aftercum = False
        jump day_start

    elif v_tutoring == 3:   # Whoring lvl 3
        call her_main("Sir, I want to apologize for doubting you.","open","base") from _call_her_main_2566
        m "Yes?"
        call her_main("Your \"atypical\" method works!","angry","worriedCl",emote="05") from _call_her_main_2567
        m "{size=-2}(Impossible!){/size}"
        m "It works? I mean, yes, naturally it works!"
        m "I'm glad you've succeeded. Now tell me more."
        call her_main("I managed to levitate a heavy rock while thinking about the behavior of two girls I saw earlier in the library.","open","closed") from _call_her_main_2568
        call her_main("Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that.","mad","angry",cheeks="blush") from _call_her_main_2569
        her "It felt weird but... {w=0.5}good at the same time."
        m "{size=-2}(She is so ignorant of life! Unbelievable.){/size}"
        m "You've never felt such a sensation before?"
        call her_main("Generally I get angry and rush to stop such behavior.","clench","worried",cheeks="blush",tears="soft") from _call_her_main_2570
        call her_main("But yesterday, I don't know, I just watched without interrupting them.","open","worriedCl",cheeks="blush") from _call_her_main_2571
        call her_main("And when I pictured it, as you told me to, it worked.","open","base",cheeks="blush") from _call_her_main_2572
        call her_main("I feel at the same level as those harlots, I'm so ashamed.","angry","angry",cheeks="blush") from _call_her_main_2573
        m "But you succeeded."
        g9 "{size=-2}(To my surprise...){/size}"
        call her_main("Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2574
        g9 "{size=-2}(In your dreams.){/size}"
        m "Good, good. Now I want to know more about those two girls."
        call her_main("It's not very relevant, professor. And I'm not sure this is appropriate.","annoyed","angryL",cheeks="blush") from _call_her_main_2575
        m "How will you improve yourself if I can't guide you?"
        m "And for that, I must know more."
        call her_main("Alright, but it's embarassing.","annoyed","angryL",cheeks="blush") from _call_her_main_2576
        g9 "{size=-2}(Ooh, I hope they were naked!){/size}"
        call her_main("I went to the library to study interactions between plants...","open","closed") from _call_her_main_2577
        g11 "{size=-2}(Yeah, yeah, come on...){/size}"
        call her_main("... and I heard muffled sounds.","base","baseL",cheeks="blush") from _call_her_main_2578
        call her_main("I was hoping to catch a teacher doing bad things with one of those Slytherin whores.","annoyed","angryL",cheeks="blush") from _call_her_main_2579
        call her_main("I slowly headed towards the sounds and I discovered two girls in an alcove.","open","base",cheeks="blush") from _call_her_main_2580
        call her_main("I remained hidden to observe them.","grin","wink",cheeks="blush") from _call_her_main_2581
        g11 "{size=-2}(Come on!){/size}"
        call her_main("Yes, professor?","base","ahegao_raised",cheeks="blush") from _call_her_main_2582
        m "Yes, no, please continue."
        call her_main("They were kissing passionately.","open","worriedCl",cheeks="blush") from _call_her_main_2583
        g9 "And? And?"
        call her_main("And a moment later they began to...","open","closed") from _call_her_main_2584
        call her_main("They began to...","open","worriedCl",cheeks="blush") from _call_her_main_2585
        call her_main("They began to touch their breasts!","scream","wide",cheeks="blush") from _call_her_main_2586
        m "They were naked, I hope?"
        call her_main("What?","open","squint",cheeks="blush") from _call_her_main_2587
        her "No, fortunately they were dressed."
        call her_main("How can such a thing happen in our beloved school!","angry","angry",cheeks="blush") from _call_her_main_2588
        m "But you kept watching, didn't you?"
        call her_main("Only for educational purposes.","annoyed","angryL",cheeks="blush") from _call_her_main_2589
        g9 "{size=-2}(\"Educational purposes\"... ha-ha, I've never heard a worse excuse!){/size}"
        m "And during all this time you didn't feel a certain need?"
        call her_main("To my shame, yes. Like I said before, I felt kind of warm inside.","annoyed","angryL",cheeks="blush") from _call_her_main_2590
        call her_main("Like when I have to pee but... different. Better.","disgust","down_raised",cheeks="blush") from _call_her_main_2591
        m "This good sensation... next time you experience it, let it come."
        call her_main("But...","open","base",cheeks="blush") from _call_her_main_2592
        m "It's the only way to get better, Miss Granger."
        m "If you suppress it, it won't work."
        call her_main("Ok...{w=0.3} I'll try my best.","annoyed","angryL",cheeks="blush") from _call_her_main_2593
        her "But to be honest, sir, I thought you were going to punish those two sluts."
        m "Can you provide proof of their crime? No?"
        m "Even I can't punish students without proof of any wrongdoing."
        g11 "{size=-2}(With the possible exception of you!){/size}"
        m "Anyway, you've done well. I think it will be enough for this lesson."
        m "Remember what I've told you, and good night!"
        call her_main("Good night, professor.","base","base") from _call_her_main_2594
        hide screen hermione_main
        call nar("You dismiss Hermione.") from _call_nar_405
        
        call her_walk("mid","door",2) from _call_her_walk_76
        
        call her_head("{size=-4}(Well, I'll try to investigate those two girls again.){/size}","disgust","down_raised",cheeks="blush") from _call_her_head_904
        call her_head("{size=-4}(Like a real anthropologist!){/size}","base","glance",cheeks="blush") from _call_her_head_905
        call her_head("{size=-4}(Yes, that's right. Hermione the anthropologist!){/size}","base","worriedCl",cheeks="blush") from _call_her_head_906
        call her_chibi("leave") from _call_her_chibi_115
        
        $ v_tutoring = 4
        $ aftercum = False
        jump day_start

    elif v_tutoring == 4:   # Whoring lvl 5
        m "So, any luck with your \"studies\"?"
        call her_main("Yes! When you hear the results of my hunt, you'll be proud of me!","base","happyCl") from _call_her_main_2595
        m "{size=-2}(\"Hunt\"?){/size}"
        m "Your \"hunt\", Miss Granger?"
        call her_main("Yes, professor!","smile","happyCl") from _call_her_main_2596
        call her_main("Like an explorer in the wild jungle, I tracked those two filthy animals.","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2597
        call her_main("With success, sir!","smile","happyCl",cheeks="blush",emote="06") from _call_her_main_2598
        call her_main("Hogwarts has so many dark and discreet corners...","annoyed","base") from _call_her_main_2599
        call her_main("Believe me, it wasn't easy, professor.","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2600
        m "I'm sure you gave it your best."
        m "But right now I await your report."
        call her_main("Yes, but before that I want to clarify that my report is purely for scientific purposes.","base","ahegao_raised",cheeks="blush") from _call_her_main_2601
        m "{size=-2}(Sure...){/size}"
        call her_main("So I tracked down those two tarts to an area in the attic.","open","closed") from _call_her_main_2602
        call her_main("Which, by the way, seems to be the meeting place for girls of this... sort.","annoyed","suspicious") from _call_her_main_2603
        m "And what is your opinion on them?"
        call her_main("At least they don't sleep with professors in exchange for house points.","open","suspicious") from _call_her_main_2604
        call her_main("","annoyed","suspicious") from _call_her_main_2605
        m "And that's it? No \"this behavior must be severely punished\"?"
        m "Are you attracted to girls of this sort, Miss Granger?"
        call her_main("What? Lesbians? I'm not... I... No way, I...","open","base",cheeks="blush") from _call_her_main_2606
        m "Alright, alright, back to your report, if you please."
        call her_main("{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}","disgust","down_raised",cheeks="blush") from _call_her_main_2607
        call her_main("{size=-2}(Hermione, girl, pull yourself together! You're not a harlot!){/size}","mad","wide",cheeks="blush") from _call_her_main_2608
        call her_main("No, I'm not!","annoyed","closed",cheeks="blush") from _call_her_main_2609
        m "Excuse me?"
        call her_main("Uh... Yes, my report. My {b}scientific{/b} report.","open","base",cheeks="blush") from _call_her_main_2610
        m "{size=-2}(Yeah, we get it...){/size}"
        call her_main("So, like before, they started by kissing passionately.","open","worriedCl",cheeks="blush") from _call_her_main_2611
        call her_main("With the tongue and everything!","open","baseL",cheeks="blush") from _call_her_main_2612
        menu:
            "-Start to jerk off while she is talking-":
                $ d_flag_01 = True
                hide screen hermione_main
                hide screen blktone
                call nar(">You reach under the desk and grab your cock...") from _call_nar_406
                hide screen genie
                show screen genie_jerking_off
                with d3
                call ctc from _call_ctc_228
            "Do nothing.":
                pass
        call her_main("","open","base",cheeks="blush") from _call_her_main_2613
        g9 "And? And?"
        call her_main("They pulled up their shirts and caressed each others breasts.","open","worriedCl",cheeks="blush") from _call_her_main_2614
        call her_main("{size=-2}(Their beautiful and tempting breasts...){/size}","open","ahegao_raised",cheeks="blush") from _call_her_main_2615
        call her_main("Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2616
        $ b_her_tears = True
        call her_main("{size=-2}(I can't believe I said that!){/size}","base","ahegao_raised",cheeks="blush",tears="sweat") from _call_her_main_2617
        call her_main("They were very excited, and I could see their panties become wet.","open","ahegao_raised",cheeks="blush") from _call_her_main_2618
        call her_main("Disgusting.","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2619
        if d_flag_01:
            g9 "{size=-2}(Yes... yes...){/size}"
        $ b_her_tears = False
        call her_main("One of the girls went crazy and inserted her fingers into the other's \"thing\" and worked them furiously.","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2620
        call her_main("Soon imitated by her girlfriend.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2621
        call her_main("Those whores came so hard I'm sure they heard the screams on the other side of the grounds!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2622
        if d_flag_01:
            her "{size=-2}(And I had to bite my lip, or else they would've heard me too...){/size}"
            hide screen hermione_main
            with d3
            
            call cum_block from _call_cum_block_44
            
            g11 "Yes! That's the stuff!"
            hide screen bld1
            with d1
            show screen genie_jerking_sperm
            call cum_block from _call_cum_block_45
            call ctc from _call_ctc_229
            
            call gen_chibi("cum_on_desk") from _call_gen_chibi_59
            with d3
            
            call her_main("Professor!","angry","angry",cheeks="blush") from _call_her_main_2623
            
            m "You enjoyed it too, so don't act all innocent."
            
            $ mad = +7
            $ d_flag_01 = False
        else:
            m "You enjoyed it too."
        call her_main("Maybe...","annoyed","angryL",cheeks="blush") from _call_her_main_2624
        m "Anyway, I hope it was revealing."
        call her_main("\"Revealing\"? I'm not sure what you mean by that.","open","suspicious") from _call_her_main_2625
        call her_main("You're the headmaster, act as such!","open","base") from _call_her_main_2626
        call her_main("Do all you can to stop those acts of debauchery!") from _call_her_main_2627
        call her_main("","annoyed","angryL") from _call_her_main_2628
        m "Yes, of course."
        m "{size=-2}(Hypocrite...){/size}"
        her "{size=-2}(Old pervert...){/size}"
        m "You said that those girls became wet."
        g9 "Weren't you a little too?"
        call her_main("When I went to bed I noticed it, yes.","disgust","down_raised",cheeks="blush") from _call_her_main_2629
        call her_main("Apparently bad fluids are released from your body when you have faced such acts.","mad","wide",cheeks="blush") from _call_her_main_2630
        m "No, they aren't bad. It happens when you're excited."
        $ b_her_tears = True
        call her_main("No way! I can control myself!","scream","worriedCl",cheeks="blush",tears="soft_blink") from _call_her_main_2631
        $ b_her_tears = False
        call her_main("","angry","angry",cheeks="blush") from _call_her_main_2632
        m "No one can control their base desires."
        m "Consider this well, and enjoy your night, Miss Granger."
        call her_main("Good night, professor.","annoyed","worriedL") from _call_her_main_2633
        hide screen hermione_main
        call nar("You dismiss Hermione.") from _call_nar_407
        
        call her_walk("mid","door",2) from _call_her_walk_77
        
        call her_head("{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_907
        call her_head("{size=-4}(I lost control, it won't happen again!){/size}","shock","down_raised",cheeks="blush") from _call_her_head_908
        call her_head("{size=-4}(Good thing I'm not a degenerate like those filthy girls!){/size}","base","glance",cheeks="blush") from _call_her_head_909
        call her_chibi("leave") from _call_her_chibi_116

        $ v_tutoring = 5
        $ aftercum = False
        jump day_start

    elif v_tutoring == 5:   # Whoring lvl 8
        m "Bravo, last time you experienced your first \"emotion\"."
        call her_main("Yes, I remember but I still don't see the link with magic.","open","suspicious") from _call_her_main_2634
        m "{size=-2}(Me neither...){/size}"
        m "If you want to progress, you have to go a little further than a simple observation."
        m "You'll need to participate."
        call her_main("What! No way I'll participate in such debauchery!","scream","closed",cheeks="blush") from _call_her_main_2635
        call her_main("How can you even suggest such a thing!","angry","angry") from _call_her_main_2636
        m "Oh you don't have to go that far in one go."
        call her_main("I'm not sure I want to go there at all.","open","closed") from _call_her_main_2637
        m "How many times do I have to remind you why you're doing this?"
        call her_main("Yes but...","open","base") from _call_her_main_2638
        m "But what?"
        call her_main("A girl like me shouldn't stoop to such practices.","annoyed","suspicious") from _call_her_main_2639
        m "A girl like you should use all means at their disposal in order to excel."
        her "..........."
        call her_main("Alright, but this must remain between us.","annoyed","angryL",cheeks="blush") from _call_her_main_2640
        call her_main("You cannot disclose this to other professors, especially professor Snape!","annoyed","down") from _call_her_main_2641
        m "Oh, I have no intention of shar.. speaking of you with professor Snape."
        g9 "{size=-2}(You're mine.){/size}"
        call her_main("Well, what must I do now?","open","closed") from _call_her_main_2642
        m "Come here."
        hide screen hermione_main
        hide screen bld1
        with d3
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_9
        
        hide screen genie
        show screen no_groping_01
        call hide_blkfade from _call_hide_blkfade_71
        call ctc from _call_ctc_230
        
        call bld from _call_bld_76
        m "Have you ever touched yourself?"
        call her_main("Professor!","base","concerned",cheeks="blush",tears="soft",xpos="mid",ypos="base") from _call_her_main_2643
        show screen groping_01
        with d7
        call nar(">You touch her leg with your hands.") from _call_nar_408
        m "Please answer the question, Miss Granger. Have you ever touched yourself?"
        call her_main("No, it's... it's wrong!","annoyed","angryL",cheeks="blush") from _call_her_main_2644
        m "But when you looked at these girls, you felt certain emotions."
        call her_main("Yes and ?","grin","wink",cheeks="blush") from _call_her_main_2645
        m "You didn't feel the need to touch yourself?"
        call her_main("Yes... but I resisted.","base","ahegao_raised",cheeks="blush") from _call_her_main_2646
        call nar(">You start to caress her thigh.") from _call_nar_409
        call her_main("Professor...","open","worriedCl",cheeks="blush") from _call_her_main_2647
        m "And you felt those emotions without even touching yourself."
        call her_main("Yes...","open","base",cheeks="blush") from _call_her_main_2648
        g9 "{size=-2}(What a slut!){/size}"
        if whoring <= 12 or custom_bra >0:
            call nar(">You move forward to her panties.") from _call_nar_410
        else:
            call nar(">You move forward to her pussy.") from _call_nar_411
        call her_main("","open","worriedCl",cheeks="blush") from _call_her_main_2649
        m "Good."
        hide screen groping_01
        show screen no_groping_01
        with d3
        call nar(">You stop caressing her.") from _call_nar_412
        call her_main("Why... why did you stop?","mad","wide",cheeks="blush") from _call_her_main_2650
        m "Oh, because I need you to think about all this before we meet again."
        call her_main("But...","mad","wide",cheeks="blush") from _call_her_main_2651
        m "Good night, my dear."
        call her_main("Good night, professor.","annoyed","worriedL") from _call_her_main_2652
        
        hide screen hermione_main
        call blkfade from _call_blkfade_115
        
        hide screen no_groping_01
        "You dismiss Hermione."
        call her_chibi("stand","desk","base") from _call_her_chibi_117
        show screen genie
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_72
        
        call her_walk("desk","door",3) from _call_her_walk_78
        
        call her_head("{size=-4}(This is wrong...){/size}","disgust","down_raised",cheeks="blush") from _call_her_head_910
        call her_head("{size=-4}(I shouldn't listen to him.){/size}","angry","worriedCl",cheeks="blush") from _call_her_head_911
        call her_head("{size=-4}(And yet...){/size}","base","down_raised",cheeks="blush") from _call_her_head_912
        call her_chibi("leave") from _call_her_chibi_118

        $ v_tutoring = 6
        $ aftercum = False
        jump day_start

    elif v_tutoring == 6:   # Whoring lvl 11
        m "So, have you started practicing my teachings?"
        call her_main("I don't even know where to start.","open","suspicious") from _call_her_main_2653
        m "You see, the secret is to stimulate appropriate areas."
        m "Areas which are more sensitive than others."
        call her_main("You mean my intimate areas, sir?!","annoyed","angryL",cheeks="blush") from _call_her_main_2654
        m "Well, they're called intimate for a reason."
        m "You said you've never touched yourself because it was wrong."
        m "But it's never wrong to exercise ones body in order to reach a new level of consciousness."
        g4 "{size=-2}(The things I have to make up...){/size}"
        m "You can begin with your breasts, for example."
        m "But you shouldn't only caress your nipples but also grab your tits and squeeze them."
        m "And in the meanwhile, you can think of those two girls."
        g9 "Or what you want to do with those girls."
        call her_main("What makes you think... No, I don't want...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2655
        call her_main("I definitely don't want to have {b}anything{/b} to do with those harlots!","scream","worriedCl",cheeks="blush") from _call_her_main_2656
        m "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls."
        call her_main("I...{w=0.3} I honestly don't know what to think anymore.","mad","angry",cheeks="blush") from _call_her_main_2657
        her "At the moment my feelings are so confusing..."
        g9 "{size=-2}(Exactly what I was hoping!){/size}"
        call her_main("I'm happy to earn points for my house and at the same time I feel so ashamed.","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_2658
        her "And the same goes for your lessons."
        m "Yet you can't deny your progress in the practice of magic."
        call her_main("...{w=0.2} Yes...{w=0.2} perhaps you're right.","base","concerned",cheeks="blush",tears="soft",tears="sweat") from _call_her_main_2659
        m "You have to let it go, Miss Granger, follow your instincts!"
        g9 "{size=-2}(Grab my cock and wank it savagely!){/size}"
        $ b_her_tears = False
        call her_main("I'm not sure if...","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2660
        m "Enough procrastination, time for practice!"
        m "Come here."
        hide screen hermione_main
        hide screen bld1
        with d3
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_10

        ">Hermione walks towards your desk."
        ">You grab her tits and massage them softly."
        pause.5
        
        hide screen genie
        show screen groping_03
        with d1
        hide screen blkfade
        call her_main("","open","worriedCl",cheeks="blush",xpos="mid",ypos="base") from _call_her_main_2661
        call ctc from _call_ctc_231
        
        call bld from _call_bld_77
        m "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas."
        m "It's not enough if I do it myself, you need to practice when you're alone."
        call her_main("","upset","worriedCl",cheeks="blush") from _call_her_main_2662
        m "Like in your bed or in the shower, for example."
        call nar(">You keep massaging her tits...") from _call_nar_413
        call her_main("","open","worriedCl",cheeks="blush") from _call_her_main_2663
        call nar(">You feel her nipples becoming hard.") from _call_nar_414
        call her_main("Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!","open","base",cheeks="blush") from _call_her_main_2664
        m "Don't let old prejudices weigh you down. You're a girl with great potential."
        call nar(">You gently squeeze her nipples through the fabric.") from _call_nar_415
        call her_main("Ah, thank you professor.","open","ahegao_raised",cheeks="blush") from _call_her_main_2665
        m "A girl with a brilliant mind."
        call nar(">You increase your grip on her nipples.") from _call_nar_416
        m "A girl who will become a woman of exception."
        call her_main("Ahh yes... I'm already a woman of exception you fool.","grin","angry",cheeks="blush") from _call_her_main_2666
        m "Fool?"
        call nar(">You firmly pinch her nipples.") from _call_nar_417
        call her_main("Ahhh yesss, not that hard, yesss...","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2667
        call nar(">You abruptly stop.") from _call_nar_418

        call blkfade from _call_blkfade_116
        pause.5
        
        call her_head("Don't stop, you idiot!","scream","angry",cheeks="blush",emote="01") from _call_her_head_913
        
        hide screen hermione_main
        hide screen groping_03
        show screen genie_and_hermione
        hide screen genie_and_hermione
        show screen genie
        show screen hermione_blink
        call hide_blkfade from _call_hide_blkfade_73
        
        call her_head("...........","mad","wide",cheeks="blush") from _call_her_head_914
        
        call her_chibi("stand","desk","base") from _call_her_chibi_119
        show screen genie
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_74
        
        show screen bld1
        call her_head("Sorry, professor.","angry","angry",cheeks="blush") from _call_her_head_915
        m "Lesson is over. Time to practice by yourself."
        m "Good night my little witch."
        call her_main("Good night, professor, and thank you for this lesson.","base","happyCl") from _call_her_main_2668
        call her_main("{size=-2}(I just wish it had lasted longer...){/size}","annoyed","suspicious") from _call_her_main_2669
        hide screen bld1
        hide screen hermione_main
        with d3
        
        call her_walk("desk","door",3) from _call_her_walk_79
        
        show screen hermione_stand_f
        call her_head("{size=-4}(\"My little witch?\"){/size}","annoyed","angryL",cheeks="blush") from _call_her_head_916
        call her_head("{size=-4}(Why not, after all...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_917
        call her_chibi("leave") from _call_her_chibi_120

        $ v_tutoring = 7
        $ aftercum = False
        jump day_start

    elif v_tutoring == 7:   # Whoring lvl 14
        m "So, Miss Granger, have you practiced my teachings?"
        call her_main("Yes...{w=0.2} a little.","annoyed","angryL",cheeks="blush") from _call_her_main_2670
        m "And?"
        call her_main("It feels even better when I'm naked.","smile","happyCl",cheeks="blush",emote="06") from _call_her_main_2671
        call her_main("{size=-2}(Oh no, I shouldn't have said that...){/size}","mad","wide",cheeks="blush") from _call_her_main_2672
        m "Well come here and undress, we'll practice."
        call her_main("Completely?!","mad","angry",cheeks="blush") from _call_her_main_2673
        m "No, only the top will suffice."
        g9 "{size=-2}(For the moment...){/size}"
        call her_main("I'll be showing you my breasts without even earning any points?","open","suspicious") from _call_her_main_2674
        m "You can't have both points and lessons."
        call her_main("Ok...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2675
        
        hide screen hermione_main
        call her_chibi("lift_top") from _call_her_chibi_121
        
        call h_action("lift_top") from _call_h_action_49
        
        call her_main("Like that?","annoyed","angryL",cheeks="blush") from _call_her_main_2676
        
        if custom_bra >=1 and badges and custom_outfit_old <= 0:
            m "Without your bra Miss Granger... and come here."
        else:
            m "Yes and now come here."
            
        call her_main("........","annoyed","closed",cheeks="blush") from _call_her_main_2677
        call her_main("","base","closed") from _call_her_main_2678
        m "Now."
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_11
        
        ">Hermione slowly walks towards your desk."
        ">She tries not to bounce her tits without much success..."
        call her_chibi("hide") from _call_her_chibi_122
        hide screen genie
        show screen genie_and_tits_01
        with d1
        
        hide screen blkfade
        call her_main("","base","closed",xpos="mid",ypos="base") from _call_her_main_2679
        call ctc from _call_ctc_232
        
        call bld from _call_bld_78
        m "Now let's get serious if you want to."
        g9 "{size=-2}(Well, even if you don't...){/size}"

        hide screen hermione_main
        call blkfade from _call_blkfade_117
        
        ">You grab her tits and squeeze them gently."
        
        show screen chair_left
        hide screen genie_and_tits_01
        show screen groping_naked_tits
        call hide_blkfade from _call_hide_blkfade_75
        call ctc from _call_ctc_233

        call her_main("Professor, what are you doing?","disgust","down_raised",cheeks="blush") from _call_her_main_2680
        g9 "Teaching you, dear, teaching you."
        m "Doesn't it feel good?"
        call her_main("A little...","base","closed") from _call_her_main_2681
        m "Your hard nipples say the contrary."
        m "I can stop if you want."
        call her_main("Yeah sure!","grin","angry",cheeks="blush") from _call_her_main_2682
        call her_main("Suck them professor.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2683
        g9 "As you wish, princess."
        call her_main("","silly","ahegao_raised",cheeks="blush") from _call_her_main_2684
        call nar(">You suck her nipples with devotion.") from _call_nar_419
        $ b_her_tears = True
        call her_main("Yes {image=textheart} like that.","silly","ahegao_raised",cheeks="blush",tears="sweat") from _call_her_main_2685
        call nar(">You start to chew on her nipples.") from _call_nar_420
        call her_main("Ah, noo, don't...","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2686
        call nar(">You chew on them even harder.") from _call_nar_421
        call her_main("Not that hard, I will...","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2687
        g9 "{size=-2}(Time for the grand finale!){/size}"
        
        if hermione_wear_panties:
            ">You quickly slip your hand into her panties and rub her pussy furiously."
        else:
            ">You quickly move your hand toward her pussy and rub it furiously."
            
        $ b_her_tears = False
        call her_main("Yes! {image=textheart}","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2688
        her "I... I..."
        g9 "Came, my dear."
        
        hide screen hermione_main
        call blkfade from _call_blkfade_118
        call ctc from _call_ctc_234
        
        call h_action("none") from _call_h_action_50
        
        hide screen chair_left
        hide screen groping_naked_tits
        hide screen genie
        show screen genie_and_hermione
        call hide_blkfade from _call_hide_blkfade_76
        
        call her_main("Is the lesson over professor?","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2689
        m "Not if you don't want it to be."
        her "Maybe it's enough for tonight."
        call her_main("After all, you have a lot of work to do.","grin","concerned",cheeks="blush",tears="mascara") from _call_her_main_2690
        m "Sure."
        m "But before that I have a little present for you."
        
        call give_reward(">You give an assortment of adult magazines to Hermione.","images/store/gifts/7.png") from _call_give_reward_14
        
        m "I hope this will help you in your studies."
        call her_main("Yes, certainly.","grin","closed",cheeks="blush",tears="mascara") from _call_her_main_2691
        her "Thank you and good night professor."
        m "Good night dear child."
        
        hide screen hermione_main
        call blkfade from _call_blkfade_119
        
        hide screen genie_and_hermione
        "You dismiss Hermione."
        call her_chibi("stand","desk","base") from _call_her_chibi_123
        show screen genie
        call hide_blkfade from _call_hide_blkfade_77
        
        call her_walk("desk","door",2.5) from _call_her_walk_80
        
        call her_head("{size=-4}(I'm such a slut...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_918
        call her_head("{size=-4}(Cumming in front of my professor...){/size}","base","down_raised",cheeks="blush") from _call_her_head_919
        call her_head("{size=-4}(I definitely need to do that again!){/size}","base","glance",cheeks="blush") from _call_her_head_920
        call her_chibi("leave") from _call_her_chibi_124
        
        $ v_tutoring = 8
        $ aftercum = False
        jump day_start

    elif v_tutoring == 8:   # Whoring lvl 17
        m "So tell me, were your readings enlightening?"
        call her_main("I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too.","angry","worriedCl",cheeks="blush") from _call_her_main_2692
        m "Maybe it's time to discover new areas to stimulate."
        call her_main("You mean my pussy, right?","open","suspicious") from _call_her_main_2693
        call her_main("I'm not an idiot, professor.","annoyed","angryL") from _call_her_main_2694
        m "If it doesn't suit you, we can stop here."
        call her_main("And if I said stop?","annoyed","suspicious") from _call_her_main_2695
        g4 ".........."
        call her_main("Haha, you should have seen your face!","smile","angry",cheeks="blush") from _call_her_main_2696
        call her_main("With all your recent lessons you can imagine that this area isn't a *no man's land* any more.","smile","baseL") from _call_her_main_2697
        g4 "Have you slept..."
        call her_main("No I haven't! I'm not a harlot who offers her pussy to every boy around.","scream","closed",cheeks="blush") from _call_her_main_2698
        m "{size=-2}(Good, your pussy is mine alone!){/size}"
        call her_main("","annoyed","ahegao") from _call_her_main_2699
        g9 "{size=-2}(Although I may agree to share it with other girls...){/size}"
        m "I'm happy you're behaving honorably, Miss Granger."
        call her_main("Ha, who'd have guessed!","annoyed","angryL",cheeks="blush") from _call_her_main_2700
        m "Yes, I'm glad that my favorite student is not wasting her precious time with boys."
        her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
        m "Enough of this! Now take off your shirt and come here."
        call her_main("Here we go for another \"lesson\".","open","suspicious") from _call_her_main_2701
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_12
        
        $ hermione_wear_top = False
        call h_update_body from _call_h_update_body_2   
        
        if hermione_wear_bra:
            call her_head("...",xpos="base",ypos="high") from _call_her_head_921
            m "And your bra..."
            
            $ hermione_wear_bra = False
            call h_update_body from _call_h_update_body_3    
        
        call her_head("........","annoyed","closed",cheeks="blush",xpos="base",ypos="high") from _call_her_head_922
        
        call her_chibi("hide") from _call_her_chibi_125
        hide screen genie
        show screen no_groping_06
        call hide_blkfade from _call_hide_blkfade_78
        call ctc from _call_ctc_235
        
        call bld from _call_bld_79
        call her_main("And free tits again, enjoy!","grin","angry",cheeks="blush",xpos="mid",ypos="base") from _call_her_main_2702
        m "I definitely intend to."
        g9 "Now take off your skirt."
        pause.8
        
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_84
        pause.5
        
        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_85
        pause.5
        
        call her_main("","base","baseL",cheeks="blush") from _call_her_main_2703
        call ctc from _call_ctc_236
        
        if hermione_wear_panties:
            call her_main("You love my pussy don't you?","base","ahegao_raised",cheeks="blush") from _call_her_main_2704
            g9 "Oh yes, I love your smell, especially when you're wet."
            call her_main("Professor...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2705
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">You caress her clit.") from _call_nar_422
            call her_main("Professor!","mad","wide",cheeks="blush") from _call_her_main_2706
        else:
            call her_main("You love my panties don't you?","base","ahegao_raised",cheeks="blush") from _call_her_main_2707
            g9 "Oh yes, I love their smell, especially when you're wet."
            call her_main("Professor...","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2708
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">You caress her clit through the fabric.") from _call_nar_423
            call her_main("Professor!","mad","wide",cheeks="blush") from _call_her_main_2709
            m "Now take them off."
            
            $ hermione_wear_panties = False
            call set_hermione_action("pinch") from _call_set_hermione_action_86
            
            call nar(">She slowly lowers her panties.") from _call_nar_424
            
            call set_hermione_action("none","skip_update") from _call_set_hermione_action_87
            
            hide screen groping_06
            show screen no_groping_06
            $ b_her_panties_off = True
            call her_main("","base","closed") from _call_her_main_2710
            call ctc from _call_ctc_237
            
        m "What's great, you see, is that I have two hands."
        m "One can caress your clit while the other can play with your pussy."
        call nar(">You move from words to deeds and penetrate her already wet pussy with ease.") from _call_nar_425
        
        hide screen no_groping_06
        show screen groping_06
        with d3
        
        call her_main("Yes, you're probably right.","grin","angry",cheeks="blush") from _call_her_main_2711
        m "Probably?!"
        call nar(">While you're moving your finger in her pussy, you take over her clit with your thumb.") from _call_nar_426
        call her_main("Haa {image=textheart}, I'm only your humble student, I wouldn't know such naughty things.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2712
        m "One finger is rarely enough even with a tight pussy like yours."
        call nar(">You insert a second finger in her tight and warm pussy...") from _call_nar_427
        call her_main("Yesss {image=textheart}, I'll try to remember your teachings.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2713
        call nar(">You increase the pace and feel her pussy tighten on your fingers.") from _call_nar_428
        m "Maybe a third finger?"
        $ b_her_tears = True
        call her_main("Don't be so bold.","grin","angry",cheeks="blush",tears="soft") from _call_her_main_2714
        call nar(">Her whole body starts shaking as you increase your ramming.") from _call_nar_429
        
        hide screen groping_06
        show screen groping_06b
        with d3
        
        call her_main("Noo {image=textheart}{w=0.2} not so fast I will...","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2715
        call nar(">You increase your pace even more.") from _call_nar_430
        call her_main("I will I will...","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2716
        g9 "Time to get serious."
        call nar(">You force your soaked thumb into her butthole.") from _call_nar_431
        $ b_her_tears = False
        call her_main("Haaaaa {image=textheart} yesss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2717
        g9 "Lucky girl."
        
        call blkfade from _call_blkfade_120
        
        hide screen hermione_main
        hide screen groping_06b
        hide screen genie
        show screen no_groping_01
        call hide_blkfade from _call_hide_blkfade_79
        
        call her_main("I'm sure this lesson will be of great help tonight.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2718
        call her_main("And the other nights {image=textheart}.","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2719
        m "Always glad to help my little witch in her studies."
        call her_main("\"Studies\", yes, that's right.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2720
        m "And to aid your studies I have even more scientific materials."

        call give_reward(">You give an assortment of porn magazines to Hermione.","images/store/gifts/8.png") from _call_give_reward_15

        call her_main("I promise to study them every night until I commit their lessons to memory!","grin","closed",cheeks="blush",tears="mascara") from _call_her_main_2721
        call her_main("Thank you and good night professor.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2722
        m "Good night, my favorite little witch."
        
        hide screen hermione_main
        call blkfade from _call_blkfade_121
        
        hide screen no_groping_01
        "You dismiss Hermione."
        
        call h_action("none") from _call_h_action_51 #Resets clothes.
        
        call her_chibi("stand","desk","base") from _call_her_chibi_126
        show screen genie
        call hide_blkfade from _call_hide_blkfade_80
        
        call her_walk("desk","door",2.5) from _call_her_walk_81
        
        call her_head("{size=-4}(Favorite...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_923
        call her_head("{size=-4}(There's another one?){/size}","mad","wide",cheeks="blush") from _call_her_head_924
        call her_head("{size=-4}(I'll do my best to remain his favorite!){/size}","base","worriedCl",cheeks="blush") from _call_her_head_925
        call her_chibi("leave") from _call_her_chibi_127
        
        $ v_tutoring = 9
        $ aftercum = False
        jump day_start

    elif v_tutoring == 9:   # Whoring lvl 20
        m "So, Miss Granger, have you had an enjoyable night?"
        call her_main("You shouldn't ask such things, Professor.","open","closed") from _call_her_main_2723
        m "I have to make sure my students have a pleasant nights rest."
        call her_main("With your teachings and your \"scientific\" literature, indeed.","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2724
        call her_main("I'll become proficient in human anatomy with all this documentation.","angry","worriedCl",cheeks="blush") from _call_her_main_2725
        m "Do you need some scientific instruments for your research?"
        call her_main("They could come in handy.","grin","wink",cheeks="blush") from _call_her_main_2726
        call her_main("As long as it's not your dick.","annoyed","angryL",cheeks="blush") from _call_her_main_2727
        call her_main("{size=-2}(Not that I don't appreciate it but no points no cock!){/size}","smile","angry",cheeks="blush") from _call_her_main_2728
        m "Miss Granger! This is a serious matter!"
        call her_main("Sure...","annoyed","suspicious") from _call_her_main_2729
        m ".........."
        call her_main("So what's my gift this time?","open","suspicious") from _call_her_main_2730

        call give_reward(">You give the vibrator to Hermione","images/store/gifts/12.png") from _call_give_reward_16

        call her_main("And I suppose you want me to test this in front of you?","open","closed") from _call_her_main_2731
        g9 "Of course."
        call her_main("Where is the educational purpose in all of this?","annoyed","suspicious") from _call_her_main_2732
        m "Good question. Improving your skills?"
        call her_main("At what? Magic?","mad","angry",cheeks="blush") from _call_her_main_2733
        m "Certainly."
        her "........."
        call her_main("I have one request though.","open","baseL",cheeks="blush") from _call_her_main_2734
        call her_main("If I'm going to masturbate I don't want to be the only one. So enjoy the free show.","open","worriedCl",cheeks="blush") from _call_her_main_2735
        g9 "With pleasure!"
        call nar(">You reach under the desk and grab your cock.") from _call_nar_432
        
        hide screen hermione_main
        call blkfade from _call_blkfade_122

        hide screen genie
        show screen genie_jerking_off
        with d3
        
        call hide_blkfade from _call_hide_blkfade_81
        
        call her_main("{size=-2}(Thinking of the headmaster masturbating makes me wet already {image=textheart}){/size}",xpos="mid",ypos="base") from _call_her_main_2736
        call her_main("{size=-2}(I've become such a whore. Not that I don't enjoy it...){/size}","smile","angry",cheeks="blush") from _call_her_main_2737
        call her_main("So... where do we start?","open","squint",cheeks="blush") from _call_her_main_2738
        
        if hermione_wear_bra:
            m "Take off your shirt and bra, I want to see your tits."
            pause.5
            
            call set_hermione_action("lift_top") from _call_set_hermione_action_88
            pause.5
            
            $ hermione_wear_top = False
            $ hermione_wear_bra = False
            call set_hermione_action("none","skip_update") from _call_set_hermione_action_89
            pause.5
            
        else:
            m "Take off your shirt, I want to see your tits."
            pause.5
            
            call set_hermione_action("lift_top") from _call_set_hermione_action_90
            pause.5
            
            $ hermione_wear_top = False
            call set_hermione_action("none","skip_update") from _call_set_hermione_action_91
            pause.5

        her "You love them don't you?"
        g9 "Oh yes..."
        her "Having watched the other girls I now know why."
        her "Those breasts are so tempting."
        call her_main("Big or small, I want to hold them in my hands and suck the nipples.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2739
        g9 "Me too, me too!"
        m "Now remove your skirt!"
        pause.5
        
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_92
        pause.5
        
        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_93
        pause.5
        
        $ b_her_tears = True
        
        call ctc from _call_ctc_238
        
        her "Good idea."
        call her_main("Sometimes I wish I could do this with others girls.","open","squint",cheeks="blush") from _call_her_main_2740
        call her_main("Masturbate naked in front of each other.","open","ahegao_raised",cheeks="blush") from _call_her_main_2741
        if hermione_wear_panties:
            g9 "Yes go on, take off your panties!"
            her "Your wish is my command."
            pause.5
            
            call set_hermione_action("pinch") from _call_set_hermione_action_94
            pause.5
            
            $ hermione_wear_panties = False
            call set_hermione_action("none","skip_update") from _call_set_hermione_action_95
            pause.5
            
            $ u_tears_pic = "characters/hermione/face/e_her_tears_02b.png"
            call ctc from _call_ctc_239
            
            call her_main("And mine is to touch another girl's pussy.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2742
        else:
            call her_main("Touch her pussy like I'm touching mine now.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2743
            
        call set_hermione_action("pinch") from _call_set_hermione_action_96
        pause.5
        
        call her_main("Caress it.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2744
        
        call set_hermione_action("fingering") from _call_set_hermione_action_97
        pause.2
        
        call her_main("Insert my fingers into her wet pussy.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2745
        g11 "Yes, yes! Now the vibrator!"
        
        hide screen hermione_main
        call blkfade from _call_blkfade_123
        
        ##call her_pose("vibrator")
        $ vibrator = True
        show screen hermione_main
        
        call hide_blkfade from _call_hide_blkfade_82
        call ctc from _call_ctc_240
        
        her "Oh I had forgotten about it already."
        call her_main("I want to hear her moan as I work my fingers.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2746
        her "Hear her cum!"
        call her_main("Like me! Aaah yesssss! {image=textheart} {image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2747
        #$ b_her_squirt = True # the squirting needs some work. Graphically, I mean.
        call ctc from _call_ctc_241
        g11 "Ahh! You little whore!!!"
        show screen genie_jerking_sperm
        her "The vibrator... aaah I'm still cumming!!"
        show screen genie_jerking_sperm_02
        g11 "Take this!"

        hide screen hermione_main
        call blkfade from _call_blkfade_124
        
        ">Hermione catches her breath and puts her clothes back on."

        call h_action("none") from _call_h_action_52 #Resets clothes.
        
        hide screen her_naked
        call her_chibi("stand","desk","base") from _call_her_chibi_128
        call gen_chibi("cum_on_desk") from _call_gen_chibi_60
        call hide_blkfade from _call_hide_blkfade_83
        
        $ b_her_tears = False
        #$ aftercum = True   # the aftercum skirt is a bit overkill IMO. Maybe reduce the height of the stains and add some dripping down the legs.
        
        call her_main("I hope you enjoyed it as much I did.","open","concerned",cheeks="blush",tears="mascara",xpos="right",ypos="base") from _call_her_main_2748
        m "Oh fuck yes, you're doing great, my little witch!"
        g9 "Very good!"
        call her_main("Thank you, professor.","grin","concerned",cheeks="blush",tears="mascara") from _call_her_main_2749
        m "After all this, you need to rest."
        call her_main("Oh yes. Good night professor.","grin","closed",cheeks="blush",tears="mascara") from _call_her_main_2750
        m "Good night, my dirty little slut."
        call nar("You dismiss Hermione.") from _call_nar_433
        
        call her_walk("desk","door",2.5) from _call_her_walk_82
        
        call her_head("{size=-4}(Rest...){/size}","base","down_raised",cheeks="blush") from _call_her_head_926
        call her_head("{size=-4}(Not before I've played with this marvelous toy again){/size}","base","glance",cheeks="blush") from _call_her_head_927
        call her_head("{size=-4}(And again){/size}","silly","glance",cheeks="blush") from _call_her_head_928
        call her_chibi("leave") from _call_her_chibi_129
        
        $ v_tutoring = 10
        $ aftercum = False
        jump day_start

    elif v_tutoring == 10:   # Whoring lvl 23
        m "So... I hope my lessons are paying off."
        call her_main("You mean, by making me more \"open\" to the wonders of adulthood?","open","suspicious") from _call_her_main_2751
        m "Among other things..."
        call her_main("That's what I thought.","annoyed","suspicious") from _call_her_main_2752
        call her_main("But to be honest, I was looking forward to this lesson.","open","closed") from _call_her_main_2753
        call her_main("{size=-2}(Maybe, I shouldn't have said that){/size}","angry","wide") from _call_her_main_2754
        her "{size=-2}(This will drive him crazy and he'll rape me savagely on his desk){/size}"
        call her_main("{size=-2}(Not that I would mind...){/size}","angry","worriedCl",cheeks="blush") from _call_her_main_2755
        call her_main("{size=-2}(And I could ask him for points afterwards){/size}","smile","baseL") from _call_her_main_2756
        m "Miss Granger? Are you alright?"
        call her_main("Yes professor! Sorry, I was thinking of my next exam.","grin","wink",cheeks="blush") from _call_her_main_2757
        m "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise."
        call her_main("I would love that!","open","worriedCl",cheeks="blush") from _call_her_main_2758
        m "So, anal stimulation..."
        call her_main("Ah! I knew you would say that.","smile","angry",cheeks="blush") from _call_her_main_2759
        her "{size=-2}(Once again, not that I mind...){/size}"
        call her_main("{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_main_2760
        m "Come again, Miss Granger?"
        call her_main("In this school nobody can compete with me, right professor?","smile","happyCl",cheeks="blush",emote="06") from _call_her_main_2761
        call her_main("In any field!","smile","angry",cheeks="blush") from _call_her_main_2762
        m "In any field? I'm not sure."
        m "You still have things to learn..."
        call her_main("What?! What are we waiting for then?","scream","closed",cheeks="blush") from _call_her_main_2763
        
        call set_hermione_action("lift_top") from _call_set_hermione_action_98
        pause.2
        
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_99
        
        ">She rips off her shirt and rushes to your desk."
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_13

        hide screen genie
        show screen groping_05
        call hide_blkfade from _call_hide_blkfade_84
        call ctc from _call_ctc_242
        
        call bld from _call_bld_80
        m "We haven't even started yet and you're already wet, my adorable slut."
        
        show screen blktone
        call her_main("It's you and your dirty talk!","annoyed","angryL",cheeks="blush",xpos="mid",ypos="base") from _call_her_main_2764
        her "Talking about anal insertions, asshole licking and... and..."
        call her_main("Fisting!","open","ahegao_raised",cheeks="blush") from _call_her_main_2765
        m "I never mentioned any of that."
        call her_main("Oh. You didn't?","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2766
        call her_main("Well maybe you didn't but you {b}were{/b} thinking about it!","base","ahegao_raised",cheeks="blush") from _call_her_main_2767
        g9 "Maybe."
        g9 "Your ass is so luscious I could eat it."
        call her_main("My point exactly!","angry","worriedCl",cheeks="blush") from _call_her_main_2768
        call her_main("Enough talking, old man. Get to work!","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2769
        m "I haven't even given you your gift yet!"
        m "I'll just put it where you'll be sure to find it."
        m "So, can we start the lesson?"
        call her_main("Yes for Merlin's sake!","open","base",cheeks="blush") from _call_her_main_2770
        m "But before that..."
        call her_main("If you say another word I swear I will go back to my dorm right now!","scream","angry",cheeks="blush",emote="01") from _call_her_main_2771
        call nar(">You suddenly insert the anal plug.") from _call_nar_434
        call her_main("Yesss {image=textheart} like that!","silly","ahegao_raised",cheeks="blush") from _call_her_main_2772
        call nar(">You remove it just as quickly while giving her butt a loud slap.") from _call_nar_435
        
        play sound sd_boing1
        with flashbulb
        play sound sd_slap
        with hpunch
        
        call her_main("Yessss more {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2773
        g9 "As you wish, princess."
        call nar(">You promptly insert and remove it.") from _call_nar_436
        
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        $ b_her_tears = True
        call her_main("More!!","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2774
        
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.png"
        call her_main("Aaaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2775
        
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        
        m "You can touch yourself too, you know."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        call her_main("I can't.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2776
        her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
        call her_main("{size=-2}(But tonight...){/size}","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2777
        m "I'll handle it then."
        call nar(">You finger both her butthole and her pussy.") from _call_nar_437
        call her_main("Nooo it's too much {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2778
        g9 "Faster? No problem!"
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        call her_main("Aaah, you're killing me {image=textheart}.","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2779
        call her_main("{size=-2}(And I love it){/size}","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2780
        m "More fingers?"
        call her_main("No more pleassse.","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2781
        m "Actually, it wasn't a question."
        call her_main("If you keep this pace I will...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2782
        call nar(">You feel her muscles tighten on your fingers.") from _call_nar_438
        call her_main("Come!!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2783
        g9 "Good girl."
        her "Keep it up, I..."
        call her_main("Yessss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2784
        m "I can keep this up as long as you please."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Yesss {image=textheart}, nooo I will die!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2785
        g9 "In ecstasy."
        call her_main("Aahh not again {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2786
        hide screen groping_05b
        show screen no_groping_05
        m "I think you've had enough for one night."
        call her_main("Yes I... I better go.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2787
        m "You forgot your gift."
        call nar(">You promptly insert the butt plug.") from _call_nar_439
        with hpunch
        call her_main("Aaaaaaah.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2788
        
        hide screen hermione_main
        call blkfade from _call_blkfade_125
        
        hide screen no_groping_05
        show screen no_groping_05_desk

        ">She collapses panting on the desk."
        g9 "Best view in the world."

        ">After a while, she puts her shirt back on."

        call h_action("none") from _call_h_action_53 #Resets clothes.
        
        hide screen no_groping_05_desk
        show screen genie
        call her_chibi("stand","desk","base") from _call_her_chibi_130
        call hide_blkfade from _call_hide_blkfade_85
        pause.5

        call her_main("Thank you for everything, professor.",tears="mascara",xpos="right",ypos="base") from _call_her_main_2789
        call her_main("It was very...{w=0.5} enlightening.","grin","concerned",cheeks="blush",tears="mascara") from _call_her_main_2790
        call her_main("But please, try to go easy on me next time.","grin","closed",cheeks="blush",tears="mascara") from _call_her_main_2791
        g9 "I have absolutely no idea what you mean by that."
        call her_main("Good night professor.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2792
        m "Good night, my dear anal whore."
        call her_main("Professor...","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2793
        
        call nar("You dismiss Hermione.") from _call_nar_440
        
        call her_walk("desk","door",2.5) from _call_her_walk_83
        
        call her_head("{size=-4}(Finally tonight I'll just go to bed){/size}","base","worriedCl",cheeks="blush") from _call_her_head_929
        call her_head("{size=-4}(That was a little too intense){/size}","angry","worriedCl",cheeks="blush") from _call_her_head_930
        call her_head("{size=-4}(Not that I'm complaining...){/size}","silly","glance",cheeks="blush") from _call_her_head_931
        call her_chibi("leave") from _call_her_chibi_131
        
        $ v_tutoring = 11
        $ aftercum = False
        jump day_start

    elif v_tutoring == 11:
        m "[hermione_name], I have something for you."
        call her_main("Another gift for me?","base","ahegao_raised",cheeks="blush") from _call_her_main_2794
        call her_main("Please, please.","open","worriedCl",cheeks="blush") from _call_her_main_2795
        m "You weren't this excited last time when I gave you a present..."
        call her_main("Oh don't worry, it was just a moment of weakness.","smile","angry",cheeks="blush") from _call_her_main_2796
        her "I'm ready now!"
        call her_main("{size=-2}(My body perhaps not...){/size}","annoyed","down") from _call_her_main_2797
        m "Did you have fun with your anal plug?"
        call her_main("Y-yes... I wear it sometimes...","base","ahegao_raised",cheeks="blush") from _call_her_main_2798
        call her_main("But I cut the tail!","annoyed","angryL",cheeks="blush") from _call_her_main_2799
        her "{size=-2}(No way I could walk around like that...){/size}"
        m "And you like it?"
        call her_main("It's very...{w=0.5} stimulating. It helps me whenever I cast a spell.","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2800
        m "Tell me the truth Miss Granger, you wear it all the time, don't you?"
        call her_main("Nooo...","annoyed","angryL",cheeks="blush") from _call_her_main_2801
        call her_main("Maybe...","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2802
        her "........"
        m "Don't be ashamed, it's alright my little whore."
        call her_main("I wear it all the time and...{w=0.3} I love it!","smile","happyCl",cheeks="blush",emote="06") from _call_her_main_2803
        g9 "{size=-2}(Marvelous){/size}"
        m "I've taught you good."
        call her_main("To be a slut? Yes you have...","open","closed") from _call_her_main_2804
        call her_main("And now I want more so where is my gift?!","annoyed","suspicious") from _call_her_main_2805
        m "There, there."

        call give_reward(">You give the anal beads to Hermione","images/store/gift_anal_beads.png") from _call_give_reward_17

        call her_main("Oh! That's even better than a butt plug.","shock","wide",cheeks="blush") from _call_her_main_2806
        g9 "And they can be useful for your pussy too."
        call her_main("So many possibilities...","smile","angry",cheeks="blush") from _call_her_main_2807
        her "...so little time."
        call her_main("I suppose you want me to try them out?","smile","happyCl") from _call_her_main_2808
        her "Or would you rather try them out on me yourself?"
        g9 "Oh yes."
        call her_main("I don't even know why I'm asking...","annoyed","ahegao") from _call_her_main_2809
        her "{size=-2}(Old pervert...){/size}"
        call her_main("{size=-2}({b}My{/b} old pervert){/size}","open","worriedCl",cheeks="blush") from _call_her_main_2810
        
        call set_hermione_action("lift_top") from _call_set_hermione_action_100
        pause.5
        
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_101
        pause.5
        
        call her_main("My tits are the best in all of Hogwarts!","silly","ahegao_raised",cheeks="blush") from _call_her_main_2811
        m "Have you been with many girls to say that?"
        call her_main("I wish...","grin","ahegao_mad",cheeks="blush") from _call_her_main_2812
        g9 "I can tutor you on that too."
        call her_main("Maybe we should finish this lesson first.","base","ahegao_raised",cheeks="blush") from _call_her_main_2813
        m "Oh, we have time."
        call her_main("Speaking of that...","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2814
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_14
        
        hide screen genie
        show screen no_groping_05
        with d1
        call hide_blkfade from _call_hide_blkfade_86
        call ctc from _call_ctc_243
        
        call bld from _call_bld_81
        g9 "As always, it's a delightful view."
        call blktone from _call_blktone_21
        call her_main("I'm glad you love it.","angry","worriedCl",cheeks="blush",xpos="mid",ypos="base") from _call_her_main_2815
        
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_102
        pause.5
        
        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_103
        pause.5
        
        call her_main("Can we start now?","grin","angry",cheeks="blush") from _call_her_main_2816
        g9 "I suppose you want them in your ass?"
        call her_main("Naturally.","base","ahegao_raised",cheeks="blush") from _call_her_main_2817
        call her_main("{size=-2}(I'll try them in my pussy later tonight){/size}","base","closed") from _call_her_main_2818
        hide screen no_groping_05
        show screen groping_05
        call nar(">You push the first bead in with ease.") from _call_nar_441
        her "Hmmm {image=textheart}"
        m "How many do you think you can take, my dear?"
        call her_main("How many have you got?","base","ahegao_raised",cheeks="blush") from _call_her_main_2819
        g9 "That's the spirit!"
        call nar(">You push another one inside with little resistance.") from _call_nar_442
        call her_main("Yess {image=textheart}, one more please.","open","ahegao_raised",cheeks="blush") from _call_her_main_2820
        call nar(">You feel the beads sink deeper when you push the third one inside.") from _call_nar_443
        $ u_tears_pic = "characters/hermione/face/e_her_tears_01.png"
        $ b_her_tears = True
        call her_main("Ohhh, they're... they're moving {image=textheart}.","grin","ahegao_mad",cheeks="blush") from _call_her_main_2821
        call nar(">The fourth takes some work before it pops in.") from _call_nar_444
        $ b_her_tears = False
        call her_main("Ah {image=textheart} ah {image=textheart}.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2822
        call nar(">You push the last one forcefully inside.") from _call_nar_445
        call her_main("Ahhhhh {image=textheart}, delightful.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2823
        her "They're so deep in my ass... almost like your cock."
        g9 "I can..."
        call her_main("No you can't! My butthole is too tight for both.","annoyed","closed",cheeks="blush") from _call_her_main_2824
        call her_main("{size=-2}(But it's such a good idea){/size}","grin","ahegao_mad",cheeks="blush") from _call_her_main_2825
        m "I'm sure there's still room for at least one finger."
        call nar(">You finger her butthole gently.") from _call_nar_446
        call her_main("Ahh... {image=textheart}{w=0.5} aah...{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_2826
        call her_main("W-What did I say...","grin","ahegao_mad",cheeks="blush") from _call_her_main_2827
        call nar(">You wiggle the finger inside.") from _call_nar_447
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.png"
        $ b_her_tears = True
        call her_main("You never listen, old pervert.","grin","ahegao_mad",cheeks="blush") from _call_her_main_2828
        m "What can I say, I just know what's best for you, my little witch."
        call nar(">You pick up the pace.") from _call_nar_448
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        $ b_her_tears = True
        call her_main("Yesss {image=textheart}.","grin","ahegao_mad",cheeks="blush") from _call_her_main_2829
        m "I thought you didn't want the finger?"
        g9 "In that case, one more finger."
        call nar(">She shivers when you insert a second finger.") from _call_nar_449
        call her_main("Ahh noo... no more please.","grin","angry",cheeks="blush") from _call_her_main_2830
        call her_main("My butthole is stretched so wide!","open","ahegao_raised",cheeks="blush") from _call_her_main_2831
        g9 "Your butthole is doing great."
        call nar(">You finger her butthole fiercely.") from _call_nar_450
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        call her_main("Nooo... aahh {image=textheart}.","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2832
        m "Your pussy is getting neglected. We need to fix that!"
        call nar(">You start fingering her pussy with your other hand. She is panting heavily.") from _call_nar_451
        call her_main("Ah... ah... like that yesss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2833
        call nar(">You suddenly pull out all the beads.") from _call_nar_452
        call her_main("Ahhhhhh!!","grin","dead",cheeks="blush",tears="messy") from _call_her_main_2834
        call nar(">And insert four fingers in her ass.") from _call_nar_453
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("I'm cumming old bastard, I cumming!","silly","ahegao_raised",cheeks="blush") from _call_her_main_2835
        m "If you must..."
        call nar(">You continue to work her ass while you finger her pussy.") from _call_nar_454
        her "No don't I..."
        call her_main("Cummm {image=textheart}{image=textheart}.","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2836
        call her_main("Agaaain aaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2837
        g11 "Sorry my little anal whore but I'm starting to get tired."
        $ b_her_tears = False
        call her_main("Don't you dare stop now!","scream","angry",cheeks="blush",tears="messy") from _call_her_main_2838
        call her_main("Just a little more pleassse {image=textheart}.","grin","dead",cheeks="blush",tears="messy") from _call_her_main_2839
        call her_main("Because I will...","grin","dead",cheeks="blush",tears="messy") from _call_her_main_2840
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("Come again!!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2841
        hide screen hermione_main
        call blkfade from _call_blkfade_126
        
        ">There's a small puddle on your desk from her juices. You slowly remove your fingers."
        
        hide screen groping_05b
        show screen no_groping_05_desk
        call hide_blkfade from _call_hide_blkfade_87
        pause.5
        
        $ b_her_tears = False
        call her_main("*Pant* *pant*","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2842
        call her_main("I feel completely ravaged but happy.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2843
        call her_main("Thank you professor, for letting me discover such great sensations.","grin","glance",cheeks="blush",tears="mascara") from _call_her_main_2844
        call her_main("But I'm exhausted so good night.","grin","closed",cheeks="blush",tears="mascara") from _call_her_main_2845
        hide screen hermione_main
        call blkfade from _call_blkfade_127
        
        ">She puts her shirt back on and rushes to the door."
        
        call h_action("none") from _call_h_action_54 #Resets clothes.
        
        hide screen no_groping_05_desk
        call her_chibi("stand","door","base",flip=True) from _call_her_chibi_132
        show screen genie
        call hide_blkfade from _call_hide_blkfade_88
        
        m "Come back here, girl."
        g11 "I need your mouth, I can't hold it anymore."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03.png"
        $ b_her_tears = True
        pause.5
        
        call her_chibi("stand","door","base") from _call_her_chibi_133
        pause.5
        
        call her_main("Professor!","open","squint",cheeks="blush") from _call_her_main_2846
        call her_main(".........","base","ahegao_raised",cheeks="blush") from _call_her_main_2847
        call her_main("Can I have points for this?","mad","wide",cheeks="blush") from _call_her_main_2848
        g11 "Now!"
        hide screen hermione_main
        call blkfade from _call_blkfade_128
        
        ">She comes back and does not seem particularly upset."
        
        call her_chibi("hide") from _call_her_chibi_134
        hide screen genie
        $ genie_chibi_xpos = -10
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_left
        show screen g_c_u
        call hide_blkfade from _call_hide_blkfade_89
        call ctc from _call_ctc_244
        
        call her_head("*Slurp!* *Slurp!* *Gulp!*",xpos="base",ypos="base") from _call_her_head_932
        g9 "Yes, like that..."
        call nar(">Hermione eagerly sucks your dick.") from _call_nar_455
        m "You seem to be in a hurry. Is it because you're not getting points for this?"
        m "Consider it a payment for your private lessons."
        her "Mmmh..."
        m "Next time, come with your robe and your robe only."
        call nar(">She briefly nods.") from _call_nar_456
        her "*Slurp!* *Gulp!* *Slurp!*"
        g9 "You're doing great my little whore, I will..."
        g11 "Yes!"

        call cum_block from _call_cum_block_46
        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u
        hide screen bld1
        with d3
        
        her "*Gobble!* *Gobble!* *Gobble!*"
        call ctc from _call_ctc_245
        
        g9 "Good girl, you swallowed it all!"
        call blkfade from _call_blkfade_129

        ">She wipes her mouth."
        hide screen g_c_u
        hide screen chair_left
        show screen genie
        call her_chibi("stand","desk","base") from _call_her_chibi_135
        call hide_blkfade from _call_hide_blkfade_90
        call ctc from _call_ctc_246

        call her_main("Sir, I still think I deserve some...","annoyed","angryL",cheeks="blush") from _call_her_main_2849
        m "Good night, my dear child."
        call her_main(".........","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2850
        call her_main("Good night, professor.","annoyed","closed",cheeks="blush") from _call_her_main_2851
        call nar("You dismiss Hermione.") from _call_nar_457

        $ b_her_tears = False
        
        call her_walk("desk","door",2.5) from _call_her_walk_84
        
        call her_head("{size=-4}(Sucking his cock without getting any points!){/size}","annoyed","angryL",cheeks="blush") from _call_her_head_933
        call her_head("{size=-4}(If he hadn't made me come so hard...){/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_934
        call her_head("{size=-4}(*sigh* Although I guess it's not that high a price...){/size}","base","down_raised",cheeks="blush") from _call_her_head_935
        call her_chibi("leave") from _call_her_chibi_136
        
        $ v_tutoring = 12
        $ aftercum = False
        jump day_start

    elif v_tutoring == 12:
        call her_main("Oh! I can't believe I forgot! Stay where you are, I'll be right back!","mad","wide",cheeks="blush") from _call_her_main_2852
        hide screen hermione_main
        play sound sd_door
        call blkfade from _call_blkfade_130
        
        play sound sd_door
        pause.3
        
        ###MAKE HER WEAR JUST A ROBE
        $ h_robe = "gryff_robe_gap"
        $ hermione_robe = "characters/hermione/clothes/robe/"+str(h_robe)+".png"
        call h_action("naked") from _call_h_action_55 #Removes all clothes.
        $ hermione_wear_robe = True
        call update_chibi_uniform from _call_update_chibi_uniform_2
        
        call her_chibi("stand","door","base") from _call_her_chibi_137
        call hide_blkfade from _call_hide_blkfade_91
        
        call her_walk("door","mid",3) from _call_her_walk_85
        
        call her_main("{size=-4}*panting*{/size} Oh good, you're still here.","open","base",cheeks="blush",xpos="right",ypos="base") from _call_her_main_2853
        m "Is it safe to assume you have honored my request this time?"
        call her_main("I thought it was obvious.","open","squint",cheeks="blush") from _call_her_main_2854
        call her_main("I even had to hide in an alcove to avoid getting noticed on my way here!","open","base",cheeks="blush") from _call_her_main_2855
        call her_main("It was so embarrassing!","open","worriedCl",cheeks="blush") from _call_her_main_2856
        call her_main("{size=-2}(And exciting!){/size}","open","worriedCl",cheeks="blush") from _call_her_main_2857
        m "Are you sure you're not wearing anything underneath?"
        call nar(">Hermione opens up her cloak a little.") from _call_nar_458
        pause.2
        
        hide screen hermione_main
        $ h_robe = "gryff_robe_gap_wide"
        $ hermione_robe = "characters/hermione/clothes/robe/"+str(h_robe)+".png"
        call her_main("","open","squint",cheeks="blush") from _call_her_main_2858
        call ctc from _call_ctc_247
        
        call her_main("Does this answer your question?","open","squint",cheeks="blush") from _call_her_main_2859
        m "Not really. It's hard to tell from this distance. I mean, it's so dark..."
        call her_main("...","annoyed","ahegao_raised") from _call_her_main_2860
        pause.2
        
        hide screen hermione_main
        $ h_robe = "gryff_robe_off"
        $ hermione_robe = "characters/hermione/clothes/robe/"+str(h_robe)+".png"
        call her_main("","base","closed",cheeks="blush",trans="d5") from _call_her_main_2861
        call ctc from _call_ctc_248
        
        call her_main("Is that better?","base","glance",cheeks="blush") from _call_her_main_2862
        g9 "Oh yes, definitely. Well done, my girl."

        hide screen hermione_main
        $ h_robe = "gryff_robe_gap_wide"
        $ hermione_robe = "characters/hermione/clothes/robe/"+str(h_robe)+".png"

        call her_main("Alright then, can we start the lesson now?","smile","angry",cheeks="blush") from _call_her_main_2863
        m "Maybe, I don't know... do you like butterbeer?"
        call her_main("You know I do. What's that got to do with...","soft","baseL",cheeks="blush") from _call_her_main_2864
        g9 "......."
        call her_main("Do you mean...{w=0.3} no, no way professor!","scream","wide",cheeks="blush") from _call_her_main_2865
        m "Oh, rest assured, we won't start with the bottom end."
        call her_main("Still, professor, this is so dirty...","silly","ahegao_raised",cheeks="blush") from _call_her_main_2866
        call her_main("{size=-2}(And exciting){/size}","silly","ahegao_raised",cheeks="blush") from _call_her_main_2867
        call her_main("Moreover, my butthole isn't stretched enough.","annoyed","closed",cheeks="blush") from _call_her_main_2868
        g4 "Are you kidding me, with all your training!"
        call her_main("And what a training!","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2869
        call her_main("{size=-2}(Good thing I practiced by myself, otherwise...){/size}","angry","worriedCl",cheeks="blush") from _call_her_main_2870
        g4 "Now stop making up excuses!"
        m "I can see you rubbing your thighs from excitement!"
        call her_main("I thought it was so dark in here...","open","squint",cheeks="blush") from _call_her_main_2871
        call her_main("Humm, okay, but you better start out easy on me.","annoyed","suspicious") from _call_her_main_2872
        g9 "I'm always gentle with you my dear child."
        call her_main("Yeah, obviously...","annoyed","ahegao") from _call_her_main_2873
        m "{size=-2}(It's not as if you don't like it rough){/size}"
        m "Alright, my desk, you, naked, now!"

        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_15

        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause.5
        
        ">Hermione slowly slides down her robe and climbs up your desk."
        
        $ hermione_wear_robe = False
        
        call her_chibi("dance","on_desk","on_desk") from _call_her_chibi_138

        call hide_blkfade from _call_hide_blkfade_92
        pause 1

        call blktone from _call_blktone_22
        call her_main("You're crazy for my body, aren't you?",xpos="mid",ypos="base") from _call_her_main_2874
        m "Why do you ask..."
        call her_main("Because a girl likes to be complimented, professor!","annoyed","suspicious") from _call_her_main_2875
        call her_main("Especially when she's about to do these kinds of things!","annoyed","ahegao") from _call_her_main_2876
        m "I meant, of course you have a amazing body! That's not up to question."
        call her_main("Best in the school?","base","ahegao_raised",cheeks="blush") from _call_her_main_2877
        m "......{w=0.3} Yeah, yeah, best in the school."
        call her_main("I can tell you're lying!","mad","angry",cheeks="blush") from _call_her_main_2878
        m "Miss Granger, I've lived for a very long time and believe me, I have seen few women with a body like yours."
        m "And definitely none in this school."
        m "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}"
        m "{size=-2}(I wonder if I can fire him for that...){/size}"
        call her_main("Thank you, professor.","open","worriedCl",cheeks="blush") from _call_her_main_2879
        call her_main("Feel free to do use my body as you please.","angry","worriedCl",cheeks="blush") from _call_her_main_2880
        m "{size=-2}(*sigh* women...){/size}"
        m "Bend over the desk my dear little witch."
        call her_main("{size=-2}(It starts with my dear little witch and ends up with my dear anal whore...){/size}","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2881
        call her_main("{size=-2}(*sigh* men...){/size}","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2882
        call her_main("As you wish my dear {b}old{/b} headmaster.","open","squint",cheeks="blush") from _call_her_main_2883
        m "{size=-2}(If you knew how old I actually am...){/size}"
        hide screen hermione_main
        call blkfade from _call_blkfade_131
        
        ">Hermione languorously climbs down your desk and bends over it."
        
        call her_chibi("hide") from _call_her_chibi_139
        hide screen genie
        
        show screen no_groping_laying_02

        call her_head("I'm ready, [genie_name].",xpos="base",ypos="base") from _call_her_head_936
        ">You take an empty butterbeer bottle, spit on the neck and push it inside her butthole."
        
        hide screen no_groping_laying_02
        show screen scr_her_fingering_naked("slow")
        hide screen bld1
        hide screen blktone
        call hide_blkfade from _call_hide_blkfade_93
        call ctc from _call_ctc_249
        
        call her_main("Hmmm, yes like that.","base","ahegao_raised",cheeks="blush") from _call_her_main_2884
        call her_main("My pussy feels lonely without your care.","grin","wink",cheeks="blush") from _call_her_main_2885
        call nar(">You start to finger her pussy too.") from _call_nar_459
        m "Poor little thing."
        call her_main("What's better in life than this professor?","open","ahegao_raised",cheeks="blush") from _call_her_main_2886
        m "Oh, I don't know."
        call her_main("Thank you for letting me discover such pleasures.","open","worriedCl",cheeks="blush") from _call_her_main_2887
        g9 "{b}My{/b} pleasure."
        call her_main("It's even better when it's mutual, isn't it?","open","squint",cheeks="blush") from _call_her_main_2888
        m "Hmm, yes you're right. I'm glad you feel that way."
        call her_main("Now a little deeper please.","soft","baseL",cheeks="blush") from _call_her_main_2889
        call nar(">You push the whole bottle neck up inside her asshole.") from _call_nar_460
        call her_main("Ohhh, yesss! {image=textheart}","open","ahegao_raised",cheeks="blush") from _call_her_main_2890
        call her_main("More, faster!","open","ahegao_raised",cheeks="blush") from _call_her_main_2891
        show screen scr_her_fingering_naked()
        call nar(">You rotate the bottle while going back and forth deeper and deeper.") from _call_nar_461
        call her_main("Yessss, don't forget my pussy {image=textheart}.","grin","ahegao_mad",cheeks="blush") from _call_her_main_2892
        g9 "Oh, your pussy better be ready for what's coming!"
        call nar(">You insert all four fingers in her sopping wet pussy.") from _call_nar_462
        call her_main("Sweet Circe, aah, aah, that's too much! {image=textheart}","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2893
        m "Nothing is too much for my little whore."
        call nar(">You increase the pace of both hands.") from _call_nar_463
        call her_main("No, no, yes, yessss! {image=textheart}","grin","dead",cheeks="blush",tears="messy") from _call_her_main_2894
        call nar(">Most of the bottle is inside her now, leaving just enough to get a good grip.") from _call_nar_464
        m "Push the bottle, push it!"
        call nar(">Whenever she pushes it back you do the same in the other direction.") from _call_nar_465
        $ u_tears_pic = "characters/hermione/face/e_her_tears_04.png"
        $ b_her_tears = True
        call her_main("This is, this is, aaaah!!! {image=textheart}{image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2895
        call nar(">Her whole body convulses as she comes hard.") from _call_nar_466
        hide screen hermione_main
        call blkfade from _call_blkfade_132
        
        $ b_her_tears = False
        hide screen scr_her_fingering_naked
        show screen no_groping_laying_02
        pause.3
        call hide_blkfade from _call_hide_blkfade_94
        call ctc from _call_ctc_250
        
        call her_main("*Panting* *panting*","grin","dead",cheeks="blush",tears="messy") from _call_her_main_2896
        call her_main("P-professor...{w=0.3} I'm so happy right now.","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2897
        g9 "Glad to hear it."
        hide screen hermione_main
        call blkfade from _call_blkfade_133
        
        ">After a while, she makes herself somewhat presentable."
        
        $ hermione_wear_robe = True
        
        hide screen no_groping_laying_02
        show screen genie
        call her_chibi("stand","desk","base") from _call_her_chibi_140
        call hide_blkfade from _call_hide_blkfade_95
        
        call bld from _call_bld_82
        m "Sweet dreams my little princess."
        call her_main("You too, professor.","open","base",cheeks="blush",xpos="right",ypos="base") from _call_her_main_2898
        g9 "They are always sweet with you around."
        call her_main("Thank you.","base","ahegao_raised",cheeks="blush") from _call_her_main_2899
        m "And next time bring your books, I'll help you with your revisions."
        call nar("You dismiss Hermione.") from _call_nar_467
        
        $ b_her_tears = False
        
        call her_walk("desk","door",2.5) from _call_her_walk_86
        
        call her_head("{size=-4}(Yes, sweet dreams...){/size}","base","worriedCl",cheeks="blush") from _call_her_head_937
        call her_head("{size=-4}(Sweet and wet!){/size}","silly","glance",cheeks="blush") from _call_her_head_938
        call her_chibi("leave") from _call_her_chibi_141
        
        $ v_tutoring = 13
        
        call h_action("none") from _call_h_action_56 #Resets clothes.
        
        $ aftercum = False
        jump day_start

    elif v_tutoring == 13:
        call her_main("I'll go get my books right away, sir!","soft","baseL") from _call_her_main_2900
        hide screen hermione_main
        play sound sd_door
        call blkfade from _call_blkfade_134
        pause 1
        
        call h_action("hold_book") from _call_h_action_57
        
        play sound sd_door
        pause.3

        call hide_blkfade from _call_hide_blkfade_96
        call ctc from _call_ctc_251
        
        call her_main("Revisions are a serious matter, [genie_name]!","open","worried") from _call_her_main_2901
        m "{size=-2}(My cock in your ass is a serious matter...){/size}"
        m "In this regard, I kinda lied, it's more of a mock exam than revisions."
        call her_main("What a surprise!","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2902
        m "I need to make sure you've been working out your butthole."
        call her_main("........","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2903
        g9 "With my cock."
        call her_main("I see...","annoyed","baseL") from _call_her_main_2904
        call her_main("I'm not against that but I bet I'll gain no points for this?","annoyed","angryL",cheeks="blush") from _call_her_main_2905
        m "I'm helping you with your revisions, why should you be getting points for that?"
        call her_main("And what revisions...","annoyed","closed",cheeks="blush") from _call_her_main_2906
        call her_main("Alright, since you have helped me a lot, I'm in.","base","baseL",cheeks="blush") from _call_her_main_2907
        call her_main("{size=-2}(I give myself away for free now, what a bad whore I make){/size}","base","concerned",cheeks="blush",tears="soft") from _call_her_main_2908
        m "Come here and strip."
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_16
        
        hide screen hermione_main
        with d3

        call h_action("naked") from _call_h_action_58
        call h_action("hold_book") from _call_h_action_59
        
        call blktone from _call_blktone_23
        hide screen blkfade
        call her_main(xpos="mid",ypos="base") from _call_her_main_2909
        call ctc from _call_ctc_252
        
        m "Ok now, put your books down and bend over the desk, my little whore."
        pause.5
        
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_104
        pause.5
        
        hide screen hermione_main
        call blkfade from _call_blkfade_135
        
        call her_chibi("hide") from _call_her_chibi_142
        hide screen genie
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade from _call_hide_blkfade_97
        call ctc from _call_ctc_253
        
        call bld from _call_bld_83
        g9 "You can open a book if you want."

        call her_main("I should read about this spell called \"the Clap\"!","annoyed","closed",cheeks="blush") from _call_her_main_2910
        
        hide screen hermione_main
        call nar(">You take advantage of her moment of distraction to force you cock into her butthole.") from _call_nar_468

        hide screen no_groping_laying_02
        show screen chair_left
        show screen scr_her_sex("slow")
        hide screen bld1
        with d1
        with hpunch
        pause.8
        
        call her_main("Ah, you brute {image=textheart}.","grin","ahegao_mad",cheeks="blush") from _call_her_main_2911
        m "Your butthole is the perfect fit, not too tight and not too stretched!"
        call her_main("You've trained me well...","silly","ahegao_raised",cheeks="blush") from _call_her_main_2912
        call nar(">You caress her clit while fucking her.") from _call_nar_469
        call her_main("Mmmh, yes {image=textheart}.","open","ahegao_raised",cheeks="blush") from _call_her_main_2913
        g9 "You love it don't you?"
        call her_main("Your cock in my ass, oh yes.","base","ahegao_raised",cheeks="blush") from _call_her_main_2914
        m "Even without points?"
        call her_main("Don't make me regret agreeing to this.","upset","worriedCl",cheeks="blush") from _call_her_main_2915
        m "Say you love it even without points."
        show screen scr_her_sex()
        call nar(">You increase the pace.") from _call_nar_470
        call her_main("Ahh yesss {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2916
        call her_main("I'm such a whore, I love sex even for free.","mad","wide",cheeks="blush") from _call_her_main_2917
        g9 "You know it!"
        call her_main("Don't make it a habit.","open","squint",cheeks="blush") from _call_her_main_2918
        m "......"
        call nar(">You pull out your cock and roughly shove it back inside.") from _call_nar_471
        $ u_tears_pic = "characters/hermione/face/e_her_tears_01.png"
        $ b_her_tears = True
        with hpunch
        call her_main("Aaaaah {image=textheart}.","open","ahegao",cheeks="blush") from _call_her_main_2919
        call her_main("I love being sodomized savagely by my headmaster.","silly","ahegao_raised",cheeks="blush") from _call_her_main_2920
        call nar(">And again.") from _call_nar_472
        with hpunch
        her "Yessss {image=textheart}."
        call her_main("I love his big cock in my ass.","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2921
        call nar(">You slap her buttcheek.") from _call_nar_473
        play sound sd_slap
        with hpunch
        $ b_her_tears = False
        call her_main("And being punished for my sluttiness.","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2922
        play sound sd_slap
        with hpunch
        call her_main("Aah, like this, punish me more master {image=textheart}.","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2923
        play sound sd_slap 
        with hpunch
        call her_main("Yess!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2924
        play sound sd_slap 
        with hpunch
        call her_main("Mooore!","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2925
        play sound sd_slap 
        with hpunch
        call her_main("I'm about to...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2926
        play sound sd_slap 
        with hpunch
        pause.1
        play sound sd_slap
        with hpunch
        pause.1
        call her_main("Cuuuum {image=textheart}{image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2927
        show screen scr_her_sex("fast")
        call nar(">You fuck her butthole fiercely.") from _call_nar_474
        call her_main("Yes, yes, again, aaaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush") from _call_her_main_2928
        g11 "Yes, my little whore, yes!"
        hide screen scr_her_sex
        show screen scr_her_sex_cum_outside()
        call her_main("*Panting* *panting*","open","concerned",cheeks="blush",tears="mascara") from _call_her_main_2929
        show screen scr_her_sex_cum_outside(1)
        g11 "*Panting* *panting*"
        
        hide screen hermione_main
        call blkfade from _call_blkfade_136
        
        hide screen chair_left
        hide screen hermione_main
        hide screen scr_her_sex_cum_outside
        pause 1
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade from _call_hide_blkfade_98
        pause.8
        
        call bld from _call_bld_84
        m "*sigh* that was, that was..."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03.png"
        $ b_her_tears = True
        call her_main("Marvellous {image=textheart}.","smile","baseL") from _call_her_main_2930
        call her_main("I'm so glad you agreed to tutor me, professor...","silly","ahegao_raised",cheeks="blush") from _call_her_main_2931
        call her_main("Your lessons have changed my life so much!","smile","angry",cheeks="blush") from _call_her_main_2932
        g9 "{size=-2}(Victory!){/size}"
        call her_main("But if you think you can fuck me all the time without giving me points...","annoyed","angryL",cheeks="blush") from _call_her_main_2933
        call her_main("You're dreaming!","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2934
        m "{size=-2}(Ohhh...){/size}"
        m "Even occasionally?"
        her "......."
        call her_main("Only if you are well-behaved...","soft","baseL",cheeks="blush") from _call_her_main_2935
        g9 "I'm the most well-behaved professor in the whole school!"
        call her_main("Sure.","annoyed","angryL",cheeks="blush") from _call_her_main_2936
        call her_main("{size=-2}(At least, you're not the worst...){/size}","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_2937
        m "Good night my, [hermione_name]."
        call her_main("Good night my, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_2938
        
        hide screen hermione_main
        call blkfade from _call_blkfade_137
        
        ">You dismiss Hermione."
        ">She puts her clothes back on without haste."
        
        call h_action("none") from _call_h_action_60 #Resets clothes.
        
        hide screen no_groping_laying_02
        pause 1

        $ b_her_tears = False
        
        show screen genie
        call her_chibi("stand","desk","base") from _call_her_chibi_143
        call hide_blkfade from _call_hide_blkfade_99
        
        call her_walk("desk","door",2.5) from _call_her_walk_87
        
        call her_head("{size=-4}(\"my beloved prince\"...){/size}","base","down_raised",cheeks="blush") from _call_her_head_939
        call her_head("{size=-4}(He's hardly Prince Charming but...){/size}","base","glance",cheeks="blush") from _call_her_head_940
        call her_head("{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}","grin","ahegao_raised",cheeks="blush") from _call_her_head_941
        call her_chibi("leave") from _call_her_chibi_144
        
        $ v_tutoring = 14
        $ aftercum = False
        jump day_start




###UE CUSTOM THINGS
# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"
# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"
# Screens
screen genie_and_hermione: #Genie sitting, Hermione stands right in front of him (behind the desk even).
    tag favor
    add "images/main_room/genie_and_hermione_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05:
    tag favor
    add "groping_05" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05b:
    tag favor
    add "groping_05b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05:
    tag favor
    add "images/animation/grope_d_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05_desk:
    tag favor
    add "images/animation/grope_d_06.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_06: #Facing Genie.
    tag favor
    add "images/animation/grope_e_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06:
    tag favor
    add "groping_06" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06b:
    tag favor
    add "groping_06b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_01:
    tag favor
    add "images/animation/grope_laying_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_02:
    tag favor
    add "images/animation/grope_laying_b_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_fingering_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    else:
        add "ani_her_fingering_naked" at Position(xpos = table_position_x -84, ypos = 10)
    add "ani_her_fingering_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_sex_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "normal":
        add "ani_her_sex_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "fast":
        add "ani_her_sex_fast_naked" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "ani_her_sex_cum_outside_naked" at Position(xpos = table_position_x -84, ypos = 10)

image groping_06: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_e_01.png"
    pause.2
    "images/animation/grope_e_02.png"
    pause.2
    "images/animation/grope_e_03.png"
    pause.5
    "images/animation/grope_e_02.png"
    pause.2
    "images/animation/grope_e_01.png"
    pause.2
    repeat

image groping_06b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_e_01.png"
    pause.1
    "images/animation/grope_e_02.png"
    pause.1
    "images/animation/grope_e_03.png"
    pause.2
    "images/animation/grope_e_02.png"
    pause.1
    "images/animation/grope_e_01.png"
    pause.1
    repeat

image groping_06_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image groping_05: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_d_01.png"
    pause.2
    "images/animation/grope_d_02.png"
    pause.2
    "images/animation/grope_d_03.png"
    pause.5
    "images/animation/grope_d_02.png"
    pause.2
    "images/animation/grope_d_01.png"
    pause.2
    repeat

image groping_05b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "images/animation/grope_d_01.png"
    pause.1
    "images/animation/grope_d_02.png"
    pause.1
    "images/animation/grope_d_03.png"
    pause.2
    "images/animation/grope_d_02.png"
    pause.1
    "images/animation/grope_d_01.png"
    pause.1
    repeat

image groping_05_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "images/animation/grope_fingering_blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_slow_naked:
    "images/animation/grope_fingering_n_01.png"
    pause.3
    "images/animation/grope_fingering_n_02.png"
    pause.3
    "images/animation/grope_fingering_n_03.png"
    pause.3
    "images/animation/grope_fingering_n_04.png"
    pause.3
    repeat

image ani_her_fingering_naked:
    "images/animation/grope_fingering_n_01.png"
    pause.2
    "images/animation/grope_fingering_n_02.png"
    pause.2
    "images/animation/grope_fingering_n_03.png"
    pause.2
    "images/animation/grope_fingering_n_04.png"
    pause.2
    repeat

image ani_her_sex_slow_naked:
    "images/animation/21_sex_n_01.png"
    pause.15
    "images/animation/21_sex_n_02.png"
    pause.15
    "images/animation/21_sex_n_03.png"
    pause.15
    "images/animation/21_sex_n_04.png"
    pause.15
    "images/animation/21_sex_n_05.png"
    pause.15
    "images/animation/21_sex_n_06.png"
    pause.15
    "images/animation/21_sex_n_07.png"
    pause.15
    repeat

image ani_her_sex_naked:
    "images/animation/21_sex_n_01.png"
    pause.1
    "images/animation/21_sex_n_02.png"
    pause.1
    "images/animation/21_sex_n_03.png"
    pause.1
    "images/animation/21_sex_n_04.png"
    pause.1
    "images/animation/21_sex_n_05.png"
    pause.1
    "images/animation/21_sex_n_06.png"
    pause.1
    "images/animation/21_sex_n_07.png"
    pause.1
    repeat

image ani_her_sex_fast_naked:
    "images/animation/21_sex_n_01.png"
    pause.05
    "images/animation/21_sex_n_02.png"
    pause.05
    "images/animation/21_sex_n_03.png"
    pause.05
    "images/animation/21_sex_n_04.png"
    pause.05
    "images/animation/21_sex_n_05.png"
    pause.05
    "images/animation/21_sex_n_06.png"
    pause.05
    "images/animation/21_sex_n_07.png"
    pause.05
    repeat

image ani_her_sex_cum_outside_naked:
    "images/animation/22_cum_n_01.png"
    pause.1
    "images/animation/22_cum_n_02.png"
    pause.1
    "images/animation/22_cum_n_03.png"
    pause.1
    "images/animation/22_cum_n_04.png"
    pause.1
    "images/animation/22_cum_n_05.png"
    pause.1
    "images/animation/22_cum_n_06.png"
    pause.1
    "images/animation/22_cum_n_07.png"
    pause.1
    "images/animation/22_cum_n_08.png"
    pause.1
    "images/animation/22_cum_n_09.png"
    pause.1
    "images/animation/22_cum_n_10.png"
    pause.1
    "images/animation/22_cum_n_11.png"
    pause.1
    "images/animation/22_cum_n_12.png"
    pause.1
    "images/animation/22_cum_n_13.png"
    pause.1
    "images/animation/22_cum_n_14.png"
    pause.1
    "images/animation/22_cum_n_15.png"
    pause.1
    "images/animation/22_cum_n_16.png"
    pause.1
    "images/animation/22_cum_n_17.png"
    pause.1
    "images/animation/22_cum_n_18.png"
    pause.1
    "images/animation/22_cum_n_19.png"
    pause 2
    "images/animation/22_cum_n_20.png"
    pause.1
    "images/animation/22_cum_n_21.png"
    pause.1
    "images/animation/22_cum_n_22.png"
    pause.1
    "images/animation/22_cum_n_23.png"
    pause.1
    repeat
