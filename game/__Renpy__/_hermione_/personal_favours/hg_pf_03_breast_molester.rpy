

### Hermione Breast Molester ###

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

    if her_whoring < 3: #Hermione refuses.
        m "[hermione_name], would you mind if I play with your tits a little?"
        call her_main("Play with...?","shock","wide")
        call her_main("My tits?!","angry","wide_stare")
        jump too_much

    #First time event
    elif her_whoring >= 3 and her_whoring <= 5:

        $ hg_pf_BreastMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Come closer, [hermione_name]..."
        call her_main("Ehm... alright...","annoyed","angryL")

        call her_walk_desk_blkfade

        call hg_breast_molester_1

        jump end_hg_breast_molester

    #Second Event
    if her_whoring >= 6:
        if her_whoring >= 6 and her_whoring <= 8:
            $ hg_pf_BreastMolester_OBJ.hearts_level = 2 #Event hearts level (0-3)
        else:
            $ hg_pf_BreastMolester_OBJ.hearts_level = 3 #Event hearts level (0-3)

        stop music fadeout 2.0
        m "Come closer [hermione_name]... I want to give your tits a massage..."
        call her_main("As you say, [genie_name]...","base","baseL",cheeks="blush")

        call her_walk_desk_blkfade

        call hg_breast_molester_2

        jump end_hg_breast_molester



### First Time Breast Molester ###

label hg_breast_molester_1:
        call blkfade

        call her_main("[genie_name].....?","annoyed","angryL",ypos="head")

        menu:
            m "..."
            "\"I'm gonna molest your tits now.\"":
                call her_main("What? What do you mean, [genie_name]--?","soft","wide")
                ">Hermione takes a hesitant step back..."
                ">You reach out swiftly and grab both of her tits through her uniform..."
            "-Just reach out and grab her tits.-":
                ">You reach out with both of your hands and grab the [hermione_name]'s tits!"

        stop music fadeout 1.0
        with hpunch
        call her_main("!!!?","mad","wide",cheeks="blush")

        hide screen genie
        call her_chibi("hide")
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1
        hide screen bld1
        call hide_blkfade
        call ctc

        call her_main("[genie_name]?!","base","ahegao_raised",cheeks="blush")

        call nar(">Hermione tries to pull away from you, but you hold her firmly by her breasts...")
        call play_music("playful_tension") #SEX THEME.

        call her_main("[genie_name], what are you--?","angry","worriedCl",cheeks="blush",emote="05")
        call nar(">She tries to pull away again.")
        call nar(">You squeeze her tits like a vice.")

        call her_main("[genie_name], you're hurting me!","angry","suspicious",cheeks="blush")
        g4 "Then stand still, [hermione_name]!"
        call her_main("B-but...","soft","wide")
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        call her_main("B-but... this is...","disgust","down_raised",cheeks="blush")
        m "Just stand still..."
        m "go to your happy place or something..."
        call her_main("M-my happy place...?","angry","wink")
        call nar(">You feel the girl's shapely breasts in your palms...")

        call her_main("............................","shock","worriedCl",ypos="head")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "-Squeeze her tits with all of your strength-":
                call nar(">You put strength into your hold...")
                call her_main("my...........","disgust","down_raised",cheeks="blush")
                call nar(">You squeeze her tits even harder...")
                call her_main("[genie_name], you're hurting them...","shock","worriedCl")
                m "Be quiet [hermione_name]..."
                call her_main("aw..............","disgust","down_raised",cheeks="blush")
                call nar(">You squeeze her ample tits with all your strength.")
                call her_main("Ah! It hurts!","angry","suspicious",cheeks="blush")
                call her_main("They're gonna burst! Please stop it!","angry","suspicious",cheeks="blush")
                m "They are not going to burst, you silly girl..."
                call nar(">You losen your grip a little...")
                call her_main("It hurts...","shock","worriedCl")
                m "You will be fine..."
                call her_main(".........","annoyed","angryL",cheeks="blush")

                return

            "-Give her tits a tender massage-":
                call nar(">You start massaging Hermione's beasts through her uniform...")
                call her_main("[genie_name]...?","shock","worriedCl")
                m "The points, [hermione_name]... You need the points. Concentrate on that."
                call her_main("Yes...","annoyed","angryL",cheeks="blush")
                call her_main("Yes, for the honour of the \"gryffindor\" house...","angry","worriedCl",cheeks="blush")
                "*Squeeze-squeeze!*"
                call nar(">You keep massaging her tits...","start")
                call nar(">You give one of her breasts a few pinches trying to locate the nipple...","end")
                call her_main("[genie_name]... you're pinching me...?","shock","worriedCl")
                call nar(">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick...")
                call her_main("\"gryffindor\" ............","angry","worriedCl",cheeks="blush")

                return

            "-Let her go and give her the points-":
                m "Well if you gonna make a drama out of this, you might as well leave..."
                call nar(">You unhand the girl's breasts...")
                call her_main("Really?","base","baseL",cheeks="blush")
                m "Yes, yes... I will even give you your points..."
                call her_main("Err... thank you, [genie_name]...","base","baseL",cheeks="blush")
                m "But you didn't earn them today..."
                call her_main("Aw.........","disgust","down_raised",cheeks="blush")

                return



### Third Time Breast Molester ###

label hg_breast_molester_2:
        call blkfade

        call play_music("playful_tension") # SEX THEME.
        ">Hermione is starting to pull her uniform up..."

        m "No, leave it on. I want to massage them while you are fully dressed..."
        call her_main("Oh, I see...","base","baseL",cheeks="blush",ypos="head")
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen genie
        call her_chibi("hide")
        show screen chair_left #Genie's chair.
        show screen groping_03
        with d1

        hide screen bld1
        call hide_blkfade
        call ctc

        "*squeeze-squeeze-squeeze*"
        call bld
        call her_main("................","base","ahegao_raised",cheeks="blush")

        $ menu_x = 0.5 #Menu is moved to the left side.
        $ menu_y = 0.3 #Menu is moved to the left side.

        menu:
            "\"Do you enjoy this, [hermione_name]?\"":
                call her_main("What...?","base","baseL",cheeks="blush")
                call her_main("Oh, I don't mind it...","base","baseL",cheeks="blush")
                "*squeeze-squeeze-squeeze*"
                call nar(">You keep massaging her soft tits...")

                if her_whoring <= 12:
                    call her_main("I mean, this isn't a big deal, as long as I am getting paid...","base","ahegao_raised",cheeks="blush")
                    call nar(">You keep on massaging her tits through her uniform...")
                    call her_main("A small price to pay for the honour of my house, really......{image=textheart}","soft","baseL",cheeks="blush")
                else:
                    m "Really? It seems to me as if you love it."
                    call her_main("I wouldn't say that I love it...","base","ahegao_raised",cheeks="blush")
                    call nar(">You keep on massaging her tits through her uniform...")
                    m "What would you say then, [hermione_name]?"
                    call her_main("I just like it, {size=-4}a lot{image=textheart}{/size}","base","ahegao_raised",cheeks="blush")

                return

            "-Pull on them abruptly with force-":
                call nar(">You give Hermione's tits a sudden but firm pull...","start")
                with vpunch
                call her_main("Ouch....","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">You pull on her tits again. This time much stronger.","start")
                with vpunch
                call her_main("Ouch! [genie_name], what are you trying to do...?","angry","worriedCl",cheeks="blush",emote="05")
                call nar(">You jerk the girl down by her tits with all your strength...","start")
                with vpunch
                with vpunch
                call nar(">Hermione almost loses balance...","end")
                call her_main("*Panting* What are you doing, [genie_name]...?","open","baseL",cheeks="blush")
                call her_main("You don't need to be so rough with me....{image=textheart}","base","baseL",cheeks="blush")

                return



### End Breasts Molester ###

label end_hg_breast_molester:
    hide screen hermione_main
    call blkfade

    hide screen blktone
    hide screen groping_03
    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")

    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    call her_main("................","annoyed","angryL",cheeks="blush",ypos="head")

    hide screen bld1
    call hide_blkfade

    if her_whoring < 6: #Adds points till 6.
        $ her_whoring +=1

    if her_whoring <= 12:
        $ gryffindor +=15
        m "The \"Gryffindor\" house gets 15 points!"
    else:
        m "you may leave now, [hermione_name]."

    call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."

    hide screen bld1
    hide screen hermione_main
    with d3

    if her_whoring >= 13:

        call her_walk("desk","door",3)

        call her_main("(What about my points?)","disgust","down_raised",cheeks="blush",ypos="head")
        if her_whoring >= 20:
            call her_main("(Eh, who cares)","base","ahegao_raised",cheeks="blush",ypos="head")
        else:
            call her_main("(I'll just ask him about it next time...)","annoyed","angryL",ypos="head")

    $ hg_pf_BreastMolester_OBJ.points += 1

    jump end_hg_pf
