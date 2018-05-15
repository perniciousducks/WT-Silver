

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
                call her_main("As what?","open","worriedL")
                m "Ms Marvel."
                if whoring >= 7:
                    m "It's not that bad. It's empowering."
                    call her_main("...","angry","worriedCl",emote="05")
                    call her_main("Fine, let me go change.","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_msMarvel_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass            
    
    if whoring < 3: #Hermione refuses.
        m "[hermione_name], would you mind if I play with your tits a little?"
        call her_main("Play with...?","shock","wide")
        call her_main("My tits?!","angry","wide_stare")
        jump too_much
    
    #First time event
    elif whoring >= 3 and whoring <= 5:

        $ new_request_04_heart = 1 #Event hearts level (0-3)
        $ hg_pf_BreastMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Come closer, [hermione_name]..."        
        call her_head("Ehm... alright...","annoyed","angryL",xpos="base",ypos="base")
        hide screen bld1
        hide screen hermione_blink
        with d3
        
        call her_walk_desk_blkfade
        
        call her_head("[genie_name].....?","annoyed","angryL")

        menu: 
            m "..."
            "\"I'm gonna molest your tits now.\"":
                call her_head("What? What do you mean, [genie_name]--?","soft","wide")
                ">Hermione takes a hesitant step back..."
                ">You reach out swiftly and grab both of her tits through her uniform..."
            "-Just reach out and grab her tits.-":
                ">You reach out with both of your hands and grab the [hermione_name]'s tits!"

        stop music fadeout 1.0
        with hpunch
        call her_head("!!!?","mad","wide",cheeks="blush")
        call her_head("[genie_name]?!","base","ahegao_raised",cheeks="blush")

        ">Hermione tries to pull away from you, but you hold her firmly by her breasts..."
        call play_music("playful_tension") #SEX THEME.

        call her_head("[genie_name], what are you--?","angry","worriedCl",cheeks="blush",emote="05")
        ">She tries to pull away again."
        ">You squeeze her tits like a vice."

        call her_head("[genie_name], you're hurting me!","angry","suspicious",cheeks="blush")
        g4 "Then stand still, [hermione_name]!"
        call her_head("B-but...","soft","wide")
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        call her_head("B-but... this is...","disgust","down_raised",cheeks="blush")
        m "Just stand still..."
        m "go to your happy place or something..."
        call her_head("M-my happy place...?","angry","wink")
        ">You feel the girl's shapely breasts in your palms..."

        hide screen genie
        call her_chibi("hide")
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen bld1
        call hide_blkfade
        call ctc

        call bld
        call her_head("............................","shock","worriedCl")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "-Squeeze her tits with all of your strength-":
                call nar(">You put strength into your hold...")
                call her_head("my...........","disgust","down_raised",cheeks="blush")
                call nar(">You squeeze her tits even harder...")
                call her_head("[genie_name], you're hurting them...","shock","worriedCl")
                m "Be quiet [hermione_name]..."
                call her_head("aw..............","disgust","down_raised",cheeks="blush")
                call nar(">You squeeze her ample tits with all your strength.")
                call her_head("Ah! It hurts!","angry","suspicious",cheeks="blush")
                call her_head("They're gonna burst! Please stop it!","angry","suspicious",cheeks="blush")
                m "They are not going to burst, you silly girl..."
                call nar(">You losen your grip a little...")
                call her_head("It hurts...","shock","worriedCl")
                m "You will be fine..."
                call her_head(".........","annoyed","angryL",cheeks="blush")

            "-Give her tits a tender massage-":
                call nar(">You start massaging Hermione's beasts through her uniform...")
                call her_head("[genie_name]...?","shock","worriedCl")
                m "The points, [hermione_name]... You need the points. Concentrate on that."
                call her_head("Yes...","annoyed","angryL",cheeks="blush")
                call her_head("Yes, for the honour of the \"gryffindor\" house...","angry","worriedCl",cheeks="blush")
                "*Squeeze-squeeze!*"
                call nar(">You keep massaging her tits...","start")
                call nar(">You give one of her breasts a few pinches trying to locate the nipple...","end")
                call her_head("[genie_name]... you're pinching me...?","shock","worriedCl")
                call nar(">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick...")
                call her_head("\"gryffindor\" ............","angry","worriedCl",cheeks="blush")

            "-Let her go and give her the points-":
                m "Well if you gonna make a drama out of this, you might as well leave..."
                call nar(">You unhand the girl's breasts...")
                call her_head("Really?","base","baseL",cheeks="blush")
                m "Yes, yes... I will even give you your points..."
                call her_head("Err... thank you, [genie_name]...","base","baseL",cheeks="blush")
                m "But you didn't earn them today..."
                call her_head("Aw.........","disgust","down_raised",cheeks="blush")

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
        call her_main("As you say, [genie_name]...","base","baseL",cheeks="blush")
        
        hide screen bld1 
        hide screen hermione_main
        with d3

        call her_walk_desk_blkfade

        call play_music("playful_tension")# SEX THEME.
        ">Hermione is starting to pull her uniform up..."

        m "No, leave it on. I want to massage them while you are fully dressed..."
        call her_head("Oh, I see...","base","baseL",cheeks="blush",xpos="base",ypos="base")
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen genie
        call her_chibi("hide")
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        
        hide screen bld1
        call hide_blkfade
        call ctc

        "*squeeze-squeeze-squeeze*"
        call bld
        call her_head("................","base","ahegao_raised",cheeks="blush")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "\"Do you enjoy this, [hermione_name]?\"":
                call her_head("What...?","base","baseL",cheeks="blush")
                call her_head("Oh, I don't mind it...","base","baseL",cheeks="blush")
                "*squeeze-squeeze-squeeze*"
                call nar(">You keep massaging her soft tits...")

                if whoring <= 12:
                    call her_head("I mean, this isn't a big deal, as long as I am getting paid...","base","ahegao_raised",cheeks="blush")
                    call nar(">You keep on massaging her tits through her uniform...")
                    call her_head("A small price to pay for the honour of my house, really......{image=textheart}","soft","baseL",cheeks="blush")
                else:
                    m "Really? It seems to me as if you love it"
                    call her_head("I wouldn't say that I love it","base","ahegao_raised",cheeks="blush")
                    call nar(">You keep on massaging her tits through her uniform...")
                    m "What would you say then [hermione_name]?"
                    call her_head("I just like it, {size=-4}a lot{image=textheart}{/size}","base","ahegao_raised",cheeks="blush")

            "-Pull on them abruptly with force-":
                call nar(">You give Hermione's tits a sudden but firm pull...","start")
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ouch....","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">You pull on her tits again. This time much stronger.","start")
                with vpunch
                hide screen blktone8
                with d3
                call her_head("Ouch! [genie_name], what are you trying to do...?","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">You jerk the girl down by her tits with all your strength...","start")
                with vpunch
                with vpunch
                call nar(">Hermione almost loses balance...","end")
                call her_head("*Panting* What are you doing, [genie_name]...?","open","baseL",cheeks="blush")
                call her_head("You don't need to be so rough with me....{image=textheart}","base","baseL",cheeks="blush")
    
    call blkfade
    
    hide screen ctc
    hide screen bld1
    hide screen blktone
    hide screen blktone8
    hide screen hermione_blink
    hide screen hermione_main
    hide screen groping_03
    hide screen chair_02 #Genie's chair.
    show screen genie
    call her_chibi("stand","desk","base")

    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    call her_head("................","annoyed","angryL",cheeks="blush")
    
    call hide_blkfade
    

    if whoring < 6: #Adds points till 6.
        $ whoring +=1

    if whoring <= 12:
        $ gryffindor +=15
        m "The \"Gryffindor\" house gets 15 points!"
    else:
        m "you may leave now [hermione_name]"
   
    call bld
    call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."
    
    hide screen bld1
    hide screen hermione_main
    with d3
    
    if whoring >= 13:

        call her_walk("desk","door",3)

        call her_head("(What about my points?)","disgust","down_raised",cheeks="blush")
        if whoring >= 20:
            call her_head("(Eh, who cares)","base","ahegao_raised",cheeks="blush")
        else:
            call her_head("(I'll just ask him about it next time)","annoyed","angryL")

        pause.5
        call her_chibi("leave","door","base")

    else:
        call her_walk("desk","leave",3)

    $ hg_pf_BreastMolester_OBJ.points += 1
    
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
    








