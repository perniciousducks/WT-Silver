

### HERMIONE PERSONAL FAVOUR 3 ###

### BREAST MOLESTER (while wearing clothes!) ###

label hg_pf_BreastMolester:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(I will molest her tits a little. Won't even ask her to bare them for me. Pretty harmless stuff.){/size}"

    if hg_pf_BreastMolester_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    if hg_msMarvel_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL") from _call_her_main_2501
                m "Ms Marvel."
                if whoring >= 7:
                    m "It's not that bad. It's empowering."
                    call her_main("...","angry","worriedCl",emote="05") from _call_her_main_2502
                    call her_main("Fine, let me go change.","normal","worriedCl") from _call_her_main_2503
                    call play_sound("door") from _call_play_sound_98 #Sound of a door opening.
                    call set_hermione_outfit(hg_msMarvel_OBJ) from _call_set_hermione_outfit_11
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass            
    
    if whoring < 3: #Hermione refuses.
        m "[hermione_name], would you mind if I play with your tits a little?"
        call her_main("Play with...?","shock","wide") from _call_her_main_2504
        call her_main("My tits?!","angry","wide_stare") from _call_her_main_2505
        jump too_much
    
    #First time event
    elif whoring >= 3 and whoring <= 5:

        $ new_request_04_heart = 1 #Event hearts level (0-3)
        $ hg_pf_BreastMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Come closer, [hermione_name]..."        
        call her_head("Ehm... alright...","annoyed","angryL",xpos="base",ypos="base") from _call_her_head_855
        hide screen bld1
        hide screen hermione_blink
        with d3
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_7
        
        call her_head("[genie_name].....?","annoyed","angryL") from _call_her_head_856

        menu: 
            m "..."
            "\"I'm gonna molest your tits now.\"":
                call her_head("What? What do you mean, [genie_name]--?","soft","wide") from _call_her_head_857
                ">Hermione takes a hesitant step back..."
                ">You reach out swiftly and grab both of her tits through her uniform..."
            "-Just reach out and grab her tits.-":
                ">You reach out with both of your hands and grab the [hermione_name]'s tits!"

        stop music fadeout 1.0
        with hpunch
        call her_head("!!!?","mad","wide",cheeks="blush") from _call_her_head_858
        call her_head("[genie_name]?!","base","ahegao_raised",cheeks="blush") from _call_her_head_859

        ">Hermione tries to pull away from you, but you hold her firmly by her breasts..."
        call play_music("playful_tension") from _call_play_music_114 #SEX THEME.

        call her_head("[genie_name], what are you--?","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_860
        ">She tries to pull away again."
        ">You squeeze her tits like a vice."

        call her_head("[genie_name], you're hurting me!","angry","suspicious",cheeks="blush") from _call_her_head_861
        g4 "Then stand still, [hermione_name]!"
        call her_head("B-but...","soft","wide") from _call_her_head_862
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        call her_head("B-but... this is...","disgust","down_raised",cheeks="blush") from _call_her_head_863
        m "Just stand still..."
        m "go to your happy place or something..."
        call her_head("M-my happy place...?","angry","wink") from _call_her_head_864
        ">You feel the girl's shapely breasts in your palms..."

        hide screen genie
        call her_chibi("hide") from _call_her_chibi_108
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_67
        call ctc from _call_ctc_225

        call bld from _call_bld_73
        call her_head("............................","shock","worriedCl") from _call_her_head_865

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "-Squeeze her tits with all of your strength-":
                call nar(">You put strength into your hold...") from _call_nar_386
                call her_head("my...........","disgust","down_raised",cheeks="blush") from _call_her_head_866
                call nar(">You squeeze her tits even harder...") from _call_nar_387
                call her_head("[genie_name], you're hurting them...","shock","worriedCl") from _call_her_head_867
                m "Be quiet [hermione_name]..."
                call her_head("aw..............","disgust","down_raised",cheeks="blush") from _call_her_head_868
                call nar(">You squeeze her ample tits with all your strength.") from _call_nar_388
                call her_head("Ah! It hurts!","angry","suspicious",cheeks="blush") from _call_her_head_869
                call her_head("They're gonna burst! Please stop it!","angry","suspicious",cheeks="blush") from _call_her_head_870
                m "They are not going to burst, you silly girl..."
                call nar(">You losen your grip a little...") from _call_nar_389
                call her_head("It hurts...","shock","worriedCl") from _call_her_head_871
                m "You will be fine..."
                call her_head(".........","annoyed","angryL",cheeks="blush") from _call_her_head_872

            "-Give her tits a tender massage-":
                call nar(">You start massaging Hermione's beasts through her uniform...") from _call_nar_390
                call her_head("[genie_name]...?","shock","worriedCl") from _call_her_head_873
                m "The points, [hermione_name]... You need the points. Concentrate on that."
                call her_head("Yes...","annoyed","angryL",cheeks="blush") from _call_her_head_874
                call her_head("Yes, for the honour of the \"gryffindor\" house...","angry","worriedCl",cheeks="blush") from _call_her_head_875
                "*Squeeze-squeeze!*"
                call nar(">You keep massaging her tits...","start") from _call_nar_391
                call nar(">You give one of her breasts a few pinches trying to locate the nipple...","end") from _call_nar_392
                call her_head("[genie_name]... you're pinching me...?","shock","worriedCl") from _call_her_head_876
                call nar(">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick...") from _call_nar_393
                call her_head("\"gryffindor\" ............","angry","worriedCl",cheeks="blush") from _call_her_head_877

            "-Let her go and give her the points-":
                m "Well if you gonna make a drama out of this, you might as well leave..."
                call nar(">You unhand the girl's breasts...") from _call_nar_394
                call her_head("Really?","base","baseL",cheeks="blush") from _call_her_head_878
                m "Yes, yes... I will even give you your points..."
                call her_head("Err... thank you, [genie_name]...","base","baseL",cheeks="blush") from _call_her_head_879
                m "But you didn't earn them today..."
                call her_head("Aw.........","disgust","down_raised",cheeks="blush") from _call_her_head_880

    #Second Event
    if whoring >= 6:
        if whoring >= 6 and whoring <= 8:
            $ new_request_04_heart = 2
            $ hg_pf_BreastMolester_OBJ.hearts_level = 2 #Event hearts level (0-3)
        else:
            $ new_request_04_heart = 3
            $ hg_pf_BreastMolester_OBJ.hearts_level = 3 #Event hearts level (0-3)

        stop music fadeout 2.0
        m "Come closer [hermione_name]... I want to give your tits a massage..."
        call her_main("As you say, [genie_name]...","base","baseL",cheeks="blush") from _call_her_main_2506
        
        hide screen bld1 
        hide screen hermione_main
        with d3

        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_8

        call play_music("playful_tension") from _call_play_music_115# SEX THEME.
        ">Hermione is starting to pull her uniform up..."

        m "No, leave it on. I want to massage them while you are fully dressed..."
        call her_head("Oh, I see...","base","baseL",cheeks="blush",xpos="base",ypos="base") from _call_her_head_881
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen genie
        call her_chibi("hide") from _call_her_chibi_109
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1
        
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_68
        call ctc from _call_ctc_226

        "*squeeze-squeeze-squeeze*"
        call bld from _call_bld_74
        call her_head("................","base","ahegao_raised",cheeks="blush") from _call_her_head_882

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "\"Do you enjoy this, [hermione_name]?\"":
                call her_head("What...?","base","baseL",cheeks="blush") from _call_her_head_883
                call her_head("Oh, I don't mind it...","base","baseL",cheeks="blush") from _call_her_head_884
                "*squeeze-squeeze-squeeze*"
                call nar(">You keep massaging her soft tits...") from _call_nar_395

                if whoring <= 12:
                    call her_head("I mean, this isn't a big deal, as long as I am getting paid...","base","ahegao_raised",cheeks="blush") from _call_her_head_885
                    call nar(">You keep on massaging her tits through her uniform...") from _call_nar_396
                    call her_head("A small price to pay for the honour of my house, really......{image=textheart}","soft","baseL",cheeks="blush") from _call_her_head_886
                else:
                    m "Really? It seems to me as if you love it."
                    call her_head("I wouldn't say that I love it...","base","ahegao_raised",cheeks="blush") from _call_her_head_887
                    call nar(">You keep on massaging her tits through her uniform...") from _call_nar_397
                    m "What would you say then, [hermione_name]?"
                    call her_head("I just like it, {size=-4}a lot{image=textheart}{/size}","base","ahegao_raised",cheeks="blush") from _call_her_head_888

            "-Pull on them abruptly with force-":
                call nar(">You give Hermione's tits a sudden but firm pull...","start") from _call_nar_398
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ouch....","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_889
                call nar(">You pull on her tits again. This time much stronger.","start") from _call_nar_399
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ouch! [genie_name], what are you trying to do...?","angry","worriedCl",cheeks="blush",emote="05") from _call_her_head_890
                call nar(">You jerk the girl down by her tits with all your strength...","start") from _call_nar_400
                with vpunch
                with vpunch
                call nar(">Hermione almost loses balance...","end") from _call_nar_401
                call her_head("*Panting* What are you doing, [genie_name]...?","open","baseL",cheeks="blush") from _call_her_head_891
                call her_head("You don't need to be so rough with me....{image=textheart}","base","baseL",cheeks="blush") from _call_her_head_892
    
    call blkfade from _call_blkfade_113
    
    hide screen ctc
    hide screen bld1
    hide screen blktone
    hide screen blktone8
    hide screen hermione_blink
    hide screen hermione_main
    hide screen groping_03
    hide screen chair_left #Genie's chair.
    show screen genie
    call her_chibi("stand","desk","base") from _call_her_chibi_110

    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    call her_head("................","annoyed","angryL",cheeks="blush") from _call_her_head_893
    
    call hide_blkfade from _call_hide_blkfade_69
    

    if whoring < 6: #Adds points till 6.
        $ whoring +=1

    if whoring <= 12:
        $ gryffindor +=15
        m "The \"Gryffindor\" house gets 15 points!"
    else:
        m "you may leave now, [hermione_name]."
   
    call bld from _call_bld_75
    call her_main("..................","annoyed","worriedL",xpos="base",ypos="base") from _call_her_main_2507
    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."
    
    hide screen bld1
    hide screen hermione_main
    with d3
    
    if whoring >= 13:

        call her_walk("desk","door",3) from _call_her_walk_69

        call her_head("(What about my points?)","disgust","down_raised",cheeks="blush") from _call_her_head_894
        if whoring >= 20:
            call her_head("(Eh, who cares)","base","ahegao_raised",cheeks="blush") from _call_her_head_895
        else:
            call her_head("(I'll just ask him about it next time...)","annoyed","angryL") from _call_her_head_896

        pause.5
        call her_chibi("leave","door","base") from _call_her_chibi_111

    else:
        call her_walk("desk","leave",3) from _call_her_walk_70

    $ hg_pf_BreastMolester_OBJ.points += 1
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme") from _call_play_music_116
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme") from _call_play_music_117
        $ hermione_sleeping = True
        jump night_main_menu
    








