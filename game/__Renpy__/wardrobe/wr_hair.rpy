#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

### Change Hair Style ###
### Change Hair Color ###


label change_hair:

    #Hermione
    if active_girl == "hermione":
        jump change_her_hair
    #Luna
    if active_girl == "luna":
        jump change_lun_hair
    #Astoria
    if active_girl == "astoria":
        jump change_ast_hair
    #Susan
    if active_girl == "susan":
        jump change_sus_hair


### Change Hermione's Hair Color ###

label change_her_hair:

    #if hair_color_choice == h_hair_color:
    #    $ wardrobe_active = 1
    #    #">She's already wearing that!" #Remove line. Just for testing.
    #    jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 


            #Change Hair-Style
            if hair_style_choice == "A" and h_hair_style != "A":
                m "[hermione_name]..."
                m "Could you wear your hair normal for me?"
                call her_main("Of course, [genie_name].","soft","base") from _call_her_main_5432
                call her_main("Let me just change it.","base","base") from _call_her_main_5433

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) from _call_set_her_hair_style_1
                call compliment_her_hair_style from _call_compliment_her_hair_style

                if hair_color_choice != h_hair_color:
                    m "There is something else I would like you to do, [hermione_name]..."
                    call her_main("Of course, [genie_name].","base","base") from _call_her_main_5434

            if hair_style_choice == "B" and h_hair_style != "B":
                m "[hermione_name]..."
                m "Could you tie your hair up for me?"
                call her_main("Of course, [genie_name].","soft","base") from _call_her_main_5435
                call her_main("Let me just change it.","base","base") from _call_her_main_5436

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) from _call_set_her_hair_style_2
                call compliment_her_hair_style from _call_compliment_her_hair_style_1

                if hair_color_choice != h_hair_color:
                    m "There is something else I would like you to do, [hermione_name]..."
                    call her_main("Of course, [genie_name].","base","base") from _call_her_main_5437

            if hair_style_choice == "E" and h_hair_style != "E":
                m "[hermione_name]..."
                m "Could you wear your hair short for me?"
                call her_main("Of course, [genie_name].","soft","base") from _call_her_main_5438
                call her_main("Let me just change it.","base","base") from _call_her_main_5439

                hide screen hermione_main
                with d3

                pause.5

                call set_her_hair_style(hair_style_choice) from _call_set_her_hair_style_3

                if hair_color_choice != h_hair_color:
                    m "There is something else I would like you to do, [hermione_name]..."
                    call her_main("Of course, [genie_name].","base","base") from _call_her_main_5440

            #Change Hair-Color
            if hair_color_choice == h_hair_color:
                jump return_to_wardrobe
            else:
                if hair_style_choice != h_hair_style:
                    m "[hermione_name]..."

            #Brown #Done
            if hair_color_choice == "1":
                m "I want you to change your hair back to brown." 
                if whoring < 5:
                    call her_main("Gladly, [genie_name].","open","closed") from _call_her_main_5441
                    call her_main("(I hate having people stare at me...)","annoyed","ahegao") from _call_her_main_5442
                    call her_main("I will go and change it.","base","baseL") from _call_her_main_5443
                elif whoring < 11:
                    call her_main("Of course, [genie_name].","open","base") from _call_her_main_5444
                    call her_main("Let me go change it.","base","base") from _call_her_main_5445
                elif whoring < 20:
                    call her_main("Sure, [genie_name].","soft","baseL") from _call_her_main_5446
                    call her_main("Let me just change it.","base","glance") from _call_her_main_5447
                else: #20+
                    call her_main("Brown, [genie_name]?","upset","wink") from _call_her_main_5448
                    call her_main("(But I liked having my hair stand out...)","annoyed","down") from _call_her_main_5449
                    call her_main("Fine, [genie_name]... {w=0.9}let me go change it.","base","baseL") from _call_her_main_5450
                    
            #Blonde #Done
            elif hair_color_choice == "2":
                m "Would you dye your hair blonde for me?" 
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Blonde?...","upset","wink") from _call_her_main_5451
                        call her_main("(It looks decent enough... {w=0.9}maybe I should try something new once in a while...)","annoyed","down") from _call_her_main_5452
                        call her_main("Ok, [genie_name]... {w=0.9}Let me go change it.","base","base") from _call_her_main_5453
                    elif whoring < 20:
                        call her_main("Blonde?","base","base") from _call_her_main_5454
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_5455
                        call her_main("Let me just change it real quick.","base","glance") from _call_her_main_5456
                    else: #20+
                        call her_main("That barely even looks like blonde!","annoyed","down") from _call_her_main_5457
                        call her_main("Don't you have anything brighter?","angry","wink") from _call_her_main_5458
                        m "You going to wear it or not?"
                        call her_main("Fine,... Let me go change it.","annoyed","annoyed") from _call_her_main_5459
                else:
                    call her_main("No thank you, [genie_name].","open","closed") from _call_her_main_5460
                    call her_main("I like my hair how it is.","open","worriedL") from _call_her_main_5461
                    call her_main("I have to refuse!","normal","base") from _call_her_main_5462
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Red #Done
            elif hair_color_choice == "3":
                m "Would you dye your hair red for me?" 
                if whoring >= 5:
                    if whoring < 11:
                        
                        call her_main("Red, [genie_name]?","open","base") from _call_her_main_5463
                        call her_main("It looks a lot like Ginny's hair-colour...","base","down") from _call_her_main_5464
                        m "Genie?"
                        call her_main("Ginny Weasley, [genie_name].","open","closed") from _call_her_main_5465
                        m "..."
                        call her_main("(...?)","angry","wink") from _call_her_main_5466
                        m "Of course! That Weasely... uhh--sister...?"
                        call her_main("Yes, [genie_name].","open","suspicious") from _call_her_main_5467
                        m "(I wonder if she is hot...)"
                        m "(The girl says she is a redhead...)"
                        g9 "(She has to be!)"
                        #if not mentioned_ginnys_hair:
                        #    call nar(>Your curiosity about Ginny grows!)
                        call her_main("I will go and change my hair, [genie_name].","open","baseL") from _call_her_main_5468
                    elif whoring < 20:
                        call her_main("Oh wow, it looks pretty. I really like it!","soft","base") from _call_her_main_5469
                        call her_main("It will make me look just like Ginny!","smile","happyCl") from _call_her_main_5470
                        call her_main("(although she's a bit shorter than me,... and her hair isn't as curly.)","annoyed","base") from _call_her_main_5471
                        #if not mentioned_ginnys_hair:
                        #    call nar(>Your curiosity about Ginny grows!)
                        call her_main("(I wonder if the teachers will notice should we switch places in class...)","grin","ahegao") from _call_her_main_5472
                        call her_main("(Only one way to find out!)","smile","glance") from _call_her_main_5473
                        call her_main("Let me go change it!","base","glance") from _call_her_main_5474
                    else: #20+
                        call her_main("You want me to be a redhead, hmm...?","base","glance") from _call_her_main_5475
                        call her_main("You know what they say about redheads, [genie_name].","smile","glance") from _call_her_main_5476
                        call her_main("Let me go change it for you.","soft","base") from _call_her_main_5477
                        
                    #$ mentioned_ginnys_hair      = True
                    
                else:
                    call her_main("No thank you, [genie_name].","open","closed") from _call_her_main_5478
                    call her_main("I like my hair how it is.","open","worriedL") from _call_her_main_5479
                    call her_main("I have to refuse!","normal","base") from _call_her_main_5480
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Crimson #Done
            elif hair_color_choice == "4":
                m "Would you dye your hair crimson for me?" 
                if whoring >= 8:
                    call her_main("It is a really nice colour, [genie_name].","soft","base") from _call_her_main_5481
                    call her_main("Let me go change it real quick.","base","base") from _call_her_main_5482
                else:
                    call her_main("That's a bit much don't you think?","angry","worriedCl") from _call_her_main_5483
                    call her_main("(I'm not dying my hair red to look like some harlot.)","annoyed","baseL") from _call_her_main_5484
                    call her_main("I have to refuse, [genie_name]!","normal","base") from _call_her_main_5485
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Black #Done
            elif hair_color_choice == "5":
                m "Would you dye your hair black for me?" 
                if whoring >= 8:
                    if whoring < 17:
                        call her_main("Black, [genie_name]?","annoyed","down") from _call_her_main_5486
                        call her_main("(It does look nice.)","annoyed","baseL") from _call_her_main_5487
                        call her_main("I will try it! Let me go and change it.","soft","baseL") from _call_her_main_5488
                    else: #17+
                        call her_main("Sure, [genie_name]!","base","glance") from _call_her_main_5489
                        call her_main("I really like that colour!","smile","happyCl") from _call_her_main_5490
                        call her_main("Let me just change it.","base","glance") from _call_her_main_5491
                else:
                    call her_main("Black, [genie_name]?","open","suspicious") from _call_her_main_5492
                    call her_main("Black isn't really my colour.","soft","baseL") from _call_her_main_5493
                    call her_main("I don't think it will suit me, [genie_name].","open","closed") from _call_her_main_5494
                    call her_main("I have to refuse.","normal","base") from _call_her_main_5495
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Green #Done
            elif hair_color_choice == "6":
                m "Would you dye your hair for me again?"
                call her_main("Of course, [genie_name]. In which colour?","open","base") from _call_her_main_5496
                g9 "Slytherin Green!"
                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Sure, why not.","soft","baseL") from _call_her_main_5497 #soft, baseL
                        call her_main("Green is just a colour, [genie_name]!","open","base") from _call_her_main_5498
                        call her_main("Wear it on my head doesn't mean I support Slytherin!","open","closed") from _call_her_main_5499
                        call her_main("(It will look awfully suspicious for a Gryffindor though...)","annoyed","worriedL") from _call_her_main_5500
                        call her_main("Just let me go change it.","base","base") from _call_her_main_5501
                    else: #17+
                        call her_main("Yes, [genie_name].","base","base") from _call_her_main_5502
                        call her_main("To tell you a secret...","soft","baseL") from _call_her_main_5503
                        call her_main("Green is my favourite colour.","base","glance") from _call_her_main_5504
                        m "Really? what about red?"
                        call her_main("Hmm... no, [genie_name].","annoyed","baseL") from _call_her_main_5505
                        call her_main("Red is such an aggressive colour.","open","down") from _call_her_main_5506
                        call her_main("Green one the other hand is soft and sweet...","soft","baseL") from _call_her_main_5507
                        call her_main("It always reminds me of nature, grassy fields in the summer, the smell of flowers everywhere...","open","baseL") from _call_her_main_5508
                        call her_main("I really love it!","smile","happyCl") from _call_her_main_5509
                        call her_main("Let me go change it for you.","base","glance") from _call_her_main_5510
                else:
                    call her_main("What?!","angry","angry") from _call_her_main_5511
                    call her_main("I'm not going to walk around school parading as some Slytherin joke-mascot!","scream","angryCl") from _call_her_main_5512
                    call her_main("I definitely refuse!","annoyed","annoyed") from _call_her_main_5513
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Blue #Done
            elif hair_color_choice == "7":
                m "Would you dye your hair blue for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","soft","baseL") from _call_her_main_5514
                    call her_main("Let me go change.","base","glance") from _call_her_main_5515
                else:
                    if whoring < 5:
                        call her_main("I'm not going to dye my hair blue for you, [genie_name]!","open","angryCl") from _call_her_main_5516
                        call her_main("If you want your own parrot, then you should just buy one!","angry","angry") from _call_her_main_5517
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                    else: #5-10
                        call her_main("Really, [genie_name]?","annoyed","suspicious") from _call_her_main_5518
                        call her_main("You want me to look like a lesbian that bad?","open","annoyed",cheeks="blush") from _call_her_main_5519
                        call her_main("I'm going to refuse!","annoyed","baseL") from _call_her_main_5520
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                    
            #Purple #Done
            elif hair_color_choice == "8":
                m "Would you dye your hair purple for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","soft","baseL") from _call_her_main_5521
                    call her_main("Let me go change.","base","glance") from _call_her_main_5522
                else:
                    call her_main("Purple?","angry","wink") from _call_her_main_5523
                    call her_main("I do like the colour, but...","soft","baseL") from _call_her_main_5524
                    call her_main("I don't think I want to wear it on my head...","annoyed","ahegao") from _call_her_main_5525
                    call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_5526
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pink #Done
            elif hair_color_choice == "9":
                m "Would you dye your hair pink for me?" 
                if whoring >= 14:
                    call her_main("Of course, [genie_name]!","smile","glance") from _call_her_main_5527
                    call her_main("I love pink!!!","soft","baseL") from _call_her_main_5528
                    call her_main("Hi-hi--","smile","happyCl") from _call_her_main_5529
                    call her_main("Let me go change.","base","glance") from _call_her_main_5530
                else:
                    call her_main("Dye my hair...","angry","angry") from _call_her_main_5531 #mad, angry
                    call her_main("Dye my hair Pink?... {w=0.9}Pink?!","angry","angry",emote="01") from _call_her_main_5532
                    call her_main("I can't dye my hair pink, [genie_name]!","scream","worriedCl") from _call_her_main_5533
                    call her_main("(What does he think I am? Some cheap dressup-doll?)","annoyed","angryL") from _call_her_main_5534
                    call her_main("It's an ugly colour anyway.","open","closed") from _call_her_main_5535
                    call her_main("I definitely refuse!","annoyed","annoyed") from _call_her_main_5536
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #White #Done
            elif hair_color_choice == "10":
                m "Dye your hair white for me." 
                if whoring >= 17:
                    call her_main("Alright, [genie_name].","smile","baseL") from _call_her_main_5537
                    call her_main("Let me go change.","base","glance") from _call_her_main_5538
                else:
                    call her_main("No, [genie_name].","open","closed") from _call_her_main_5539
                    call her_main("I'm not going to run around school looking like some grandma!","annoyed","annoyed") from _call_her_main_5540
                    call her_main("I refuse!","annoyed","baseL") from _call_her_main_5541
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_her_hair_color(hair_color_choice) from _call_set_her_hair_color


            call her_main("","","",xpos="wardrobe") from _call_her_main_5542
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_her_hair_style(hair_style_choice) from _call_set_her_hair_style_4
            call her_main("","","",xpos="wardrobe") from _call_her_main_5543

            if hair_color_choice == h_hair_color:
                call screen wardrobe

            if hair_color_choice == "2" and whoring <= 5:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if hair_color_choice == "3" and whoring <= 5:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if hair_color_choice == "4" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if hair_color_choice == "5" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if hair_color_choice == "6" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if hair_color_choice == "7" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if hair_color_choice == "8" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if hair_color_choice == "9" and whoring <= 14:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if hair_color_choice == "10" and whoring <= 17:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_her_hair_color(hair_color_choice) from _call_set_her_hair_color_1
            call her_main("","","",xpos="wardrobe") from _call_her_main_5544
            call screen wardrobe
#


label compliment_her_hair_style:
    if whoring < 5:
        call her_main("Like this, [genie_name]?","soft","base") from _call_her_main_5545
        m "This look really suits you, [hermione_name]."
        call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_5546
    elif whoring < 11:
        call her_main("...","base","happyCl") from _call_her_main_5547
        call her_main("Do you like it, [genie_name]?","grin","wink",cheeks="blush") from _call_her_main_5548
        m "Indeed I do, [hermione_name]."
        call her_main("Thank you.","base","base") from _call_her_main_5549
    elif whoring < 20:
        call her_main("How do I look?","open","closed") from _call_her_main_5550
        m "You look very lovely, [hermione_name]!"
        call her_main("Glad to hear that, [genie_name].","base","glance") from _call_her_main_5551
    else: #20+
        if h_hair_style == "A":
            call her_main("Do you like my long hair, [genie_name]?","base","glance") from _call_her_main_5552
            m "I do, [hermione_name]"
            call her_main("I prefer wearing my hair open like this.","open","closed") from _call_her_main_5553
            call her_main("Makes it easier to grab and pull...","base","glance") from _call_her_main_5554
            call her_main("Like a leash!","smile","angry") from _call_her_main_5555
            g4 "You dirty slut!"
        else: 
            call her_main("Do you like it, [genie_name]?","base","glance") from _call_her_main_5556
            call her_main("Does this hair make me look...","base","base") from _call_her_main_5557
            call her_main("Slutty?","base","glance") from _call_her_main_5558
            g4 "Ugh!--You can bet your perfect ass on it!" 
            g9 "Why don't you come over here and I give your hair some lotion!" 
            call her_main("[genie_name] you should know that I already used some rather expensive lotion this morning and--","open","closed") from _call_her_main_5559
            m "I just want to shower them in my cum, girl..."  
            call her_main("Oh-","soft","base") from _call_her_main_5560
            call her_main("...","soft","baseL",cheeks="blush") from _call_her_main_5561
            call her_main("(What a great idea.)","base","happyCl") from _call_her_main_5562
            call her_main("Maybe next time, [genie_name].","smile","baseL") from _call_her_main_5563

    return


label change_ast_hair:
    call set_ast_hair(hair_style_choice, hair_color_choice) from _call_set_ast_hair

    hide screen wardrobe
    call screen wardrobe

label change_sus_hair:
    call set_sus_hair(hair_style_choice, hair_color_choice) from _call_set_sus_hair

    hide screen wardrobe
    call screen wardrobe

