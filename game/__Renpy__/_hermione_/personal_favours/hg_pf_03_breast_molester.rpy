

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
                jump hermione_requests_menu

    if her_whoring < 3: #Hermione refuses.
        m "[hermione_name], would you mind if I play with your tits a little?"
        call her_main("Play with...?","shock","wide")
        call her_main("My tits?!","angry","wide_stare")
        jump too_much

    #First Event
    if her_whoring >= 3 and her_whoring < 6:
        m "Come closer, [hermione_name]..."
        call her_main("Ehm... alright...","annoyed","angryL")
        call her_walk_desk_blkfade
        $ current_payout = 15

        call hg_breast_molester_1

        $ hg_pf_BreastMolester_OBJ.level = 1
        jump end_hg_breast_molester

    #Second Event
    if her_whoring >= 6 and her_whoring < 9:
        stop music fadeout 2.0
        m "Come closer [hermione_name]... I want to give your tits a massage..."
        call her_main("As you say, [genie_name]...","base","baseL",cheeks="blush")
        call her_walk_desk_blkfade
        $ current_payout = 15

        call hg_breast_molester_2

        $ hg_pf_BreastMolester_OBJ.level = 2
        jump end_hg_breast_molester

    #Third Event
    if her_whoring >= 9 and her_whoring < 15:
        m "[hermione_name]..."
        call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
        m "I feel like playing with your tits a little..."
        call her_main("[genie_name]... I'd prefer it if you wouldn't make me such offers...","annoyed","annoyed")
        m "Why? Too hard to resist?"
        her "Nothing like that, [genie_name]."
        m "Well, how about you come closer and bare your tits for me...?"
        call her_main("!!!","open","base")
        m "I want to give them a good squeeze."
        call her_main("[genie_name]! Don't you think this is too much?","disgust","glance")
        m "You think?"
        her "I am not one of those harlots from \"Slytherin\", you know..."
        m "I know... You are from \"Gryfonmon\"... or something..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        call her_main("And if I don't feel like it I don't have to sell you a single favour, [genie_name]!","annoyed","worriedL")
        m "Of course..."
        call her_main("...................","annoyed","angryL")
        m "I'll give you 35 house points for this."
        call her_main(".......................","disgust","glance")
        her "All you are going to do is watch, [genie_name]?"
        m "Well, I feel more like touching, actually..."
        her "...................................."
        her "Well, alright... You can touch them a little..."
        call her_walk_desk_blkfade
        $ current_payout = 35
        $ favor_failed = False #Not yet failed.

        call hg_breast_molester_3

        if favor_failed: #fails when you slap her tits and her_whoring < 12
            $ favor_failed = False #Reset
            jump could_not_flirt

        call hg_breast_molester_3_grabbing

        $ hg_pf_BreastMolester_OBJ.level = 3
        jump end_hg_breast_molester

    if her_whoring >= 15:
        m "[hermione_name]..."
        call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
        m "I feel like playing with your tits a little..."
        call her_main("Of course [genie_name]...","base","ahegao_raised")
        call her_walk_desk_blkfade
        $ current_payout = 35

        call hg_breast_molester_3
        call hg_breast_molester_3_grabbing

        $ hg_pf_BreastMolester_OBJ.level = 4
        jump end_hg_breast_molester




### First Time Breast Molester ###

label hg_breast_molester_1:
    call blkfade

    call her_main("[genie_name].....?","annoyed","angryL",ypos="head")
    m "..."
    
    menu:
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


label hg_breast_molester_3:
    call blkfade

    hide screen genie
    show screen genie_and_tits_01
    with d1

    call hide_blkfade
    stop music fadeout 1.0
    call ctc

    call play_music("playful_tension") # SEX THEME.

    hide screen hermione_main
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    show screen blktone
    call set_her_action("lift_top")
    call her_main(xpos="mid",ypos="base")
    call ctc

    menu:
        m "..."
        "-Grab them-":
            return

        "-Slap them-":
            show screen blktone
            call nar(">You give Hermione's tits a loud slap!")
            call slap_her

            if her_whoring >= 9 and her_whoring < 12:

                $ her_mood += 20
                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch! It hurts! *SOB!*","angry","worried",cheeks="blush")
                m "Did you like it though?"
                call her_main("Did I... \"like it\, [genie_name]..?","annoyed","annoyed")
                call her_main("What girl in her right mind would like to be treated this way?")
                stop music fadeout 1.0

                hide screen blktone
                show screen bld1
                call set_her_action("none")
                pause.5

                call her_main("You are a mean and demented old man!","angry","worried",cheeks="blush",tears="soft")
                hide screen hermione_main
                call blkfade

                m "............"
                call play_sound("door")
                m "Well, no points for \"Gryffindor\" then..."
                $ favor_failed = True #Jumps to favor fail label after return.

                return

            #Second Event.
            elif her_whoring >= 12 and her_whoring < 15:
                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch!","angry","worried",cheeks="blush")
                call her_main("[genie_name], what did you do this for?")
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_main("...Of course, not, [genie_name].","annoyed","closed")
                m "Let's try this again, then."
                call her_main("What?","annoyed","base")
                call slap_her

                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch! Stop hurting me!")
                m "Admit that you enjoy it and I will."
                call her_main("But I don't...","disgust","down_raised")
                call her_main("And if you plan to keep on doing this to me, [genie_name]...")
                call her_main("...then I think I should leave.","annoyed","annoyed")
                m "Fine, fine..."

                return

            #Third Event.
            elif her_whoring >= 15:
                call her_main("Ah!!!","scream","wide",cheeks="blush")
                call her_main("[genie_name], why did you do that?","grin","glance",cheeks="blush")
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_main("..........","annoyed","base")
                call her_main("I am not a pervert...")
                call nar(">You give Hermione's tits another loud smack!")
                call slap_her

                call her_main("A-ah!!!","silly","down",cheeks="blush")
                m "Tell me you like it!"
                her "[genie_name]... I..."
                call nar(">You unleash a whole series of slaps!")

                call slap_her
                call slap_her
                call slap_her

                call nar(">Hermione's tits bounce allover the place, completely out of control")
                call her_main("A-ah!!! Ah!!! A-a-aha!!!","silly","ahegao",cheeks="blush",tears="soft")
                m "You enjoy this. Admit it."
                call her_main("...........","base","dead",cheeks="blush",tears="soft")
                call nar(">You smack her tits again.")

                call slap_her
                call slap_her
                call slap_her

                call her_main("A-ah! Yes! I do, I do! A-ah...","silly","ahegao",cheeks="blush",tears="soft")
                call her_main("...does this mean I'm a pervert, [genie_name]?","angry","worried",cheeks="blush",tears="soft")
                m "What?"
                m "Stop being silly, [hermione_name]."
                m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
                her "......"
                her "Are you sure about that, [genie_name]?"
                m "Yes. Believe me, I know."
                call nar(">You give her tits one more slap!")
                call slap_her

                call her_main("A-ah... Yes... Thank you, [genie_name].","silly","ahegao",cheeks="blush",tears="soft")
                m "Well... Enough with the slapping for now..."

                return


label hg_breast_molester_3_grabbing:
    hide screen hermione_main
    hide screen genie
    show screen groping_naked_tits
    hide screen bld1
    with fade
    call ctc

    if her_whoring >= 9 and her_whoring < 15:
        show screen blktone
        call her_main("..............................","angry","down_raised")
        m "You have great tits, [hermione_name]..."
        call her_main("....................................","angry","down_raised")
        m "You like it when I squeeze them like this?"
        call her_main("Excuse me, [genie_name], but you are confusing me with one of those lowly harlots again...","upset","closed")
        call her_main("I am only letting you fondle me because I am getting paid for it...","upset","closed")
        call her_main("Not because I enjoy it...","upset","closed")
        m "I see..."
        m "So, you're more like a prostitute then..."
        call her_main("[genie_name]!","angry","wide")
        call her_main("Prostitutes are paid to have sex with men...","angry","wide")
        call her_main("I'd never do something like that!","upset","closed")

        call nar(">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs.")

        call her_main("Ah...","open","worriedCl")
        m "Enjoying yourself, [hermione_name]?"

        if her_whoring >= 9 and her_whoring < 12:
            call her_main("[genie_name], I am only doing this--","upset","closed")

            call nar(">You squeeze both of her tits with force...")

            call her_main("ah...","shock","worriedCl")
            m "Tell me you like this, [hermione_name]!"
            call her_main("[genie_name], I am only letting you do this to me because--","open","worriedCl")
            m "I know, know..."
            m "You are starting to sound like a broken record."
            call her_main("....","annoyed","annoyed")
            call blkfade

            ">You let go of the girl's breasts..."

            return

        else: #12+
            call her_main("Ah...","open","down")

            call nar(">You squeeze her tits a few more times, then give them a firm tug...")

            call her_main("Ah... [genie_name]...","open","base")
            m "What? You do enjoy this, don't you?"
            call her_main("No... I...","open","base")
            m "Don't you lie to your headmaster, [hermione_name]!"

            call nar(">You squeeze her tits again...")

            call her_main("Ah...","open","down")
            call her_main("I am not lying, [genie_name]...","open","down")
            call her_main("Why would I enjoy this?","open","base")
            m "I don't know [hermione_name]. You tell me."

            call nar(">You keep massaging her breasts...")

            call her_main("Ah... I...","open","base")
            m "Yes, what is it?"
            call her_main("It's... It's nothing, [genie_name]...","angry","base")
            m "Oh, I think it's something."
            m "I think you like me squeezing your tits like this."
            call her_main("[genie_name], please...","angry","down_raised")

            if daytime:
                call her_main("Classes are about to start...","angry","down_raised")
            else:
                call her_main("It's getting late...","angry","down_raised")

            call her_main("Can I go now, [genie_name]? Please?","angry","base")

            m "Sure, go ahead..."
            pause 2
            call her_main("...............","angry","down_raised")
            pause.2

            call her_main("[genie_name], your are still... Holding me...","angry","base")
            m "Oh, right... my bad...."
            call blkfade

            ">You let go of Hermione's breasts..."

            return

    elif her_whoring >= 15:
        show screen blktone
        call her_main("Ah...","soft","ahegao")
        m "A bit sensitive today, aren't you?"
        call her_main("I suppose...","base","glance")
        call her_main("Ah...","open","worriedCl")
        m "You like it when I squeeze them like this?"
        call her_main("I do, [genie_name]... Ah...","base","glance")
        m "Heh..."
        m "What if I pinch your nipples?"
        call her_main("!!!","angry","base")
        call her_main("Ah! [genie_name]...","open","worriedCl")
        m "And what if I do this?"
        call nar(">You grab the girl by her hard nipples and start pulling...")
        call her_main("Ah... Ah... Ah... [genie_name]...","shock","worriedCl")
        m "What if I pull even harder?"
        with hpunch

        call her_main("Ah... [genie_name], please...","scream","wide")
        call nar(">Hermione clutches the edge of your desk to keep herself from taking a step towards you...")
        m "Good girl..."
        call her_main("*Panting heavily*","grin","dead")
        m "Do you enjoy this?"
        call her_main("You are hurting me, [genie_name]...","shock","baseL",cheeks="blush",tears="soft")
        m "But do you enjoy it?"

        if her_whoring < 18:
            call her_main("Ah... Yes, [genie_name]... I don't know why, but I do...","clench","worried",cheeks="blush",tears="soft")
        else:
            call her_main("Ah... Yes, [genie_name]... I love it...","silly","worried",cheeks="blush",tears="soft")

        m "Good girl..."
        call nar(">You let go of her nipples...")
        call her_main("Ah...","silly","worried",cheeks="blush",tears="soft")

        show screen bld1
        call hide_blktone

        m "This will be all for today, [hermione_name]..."
        call her_main("Oh...?","shock","baseL",cheeks="blush",tears="soft")
        m "What is it? You look disappointed."
        m "I will pay you of course..."
        call her_main("That's not it, [genie_name]...","angry","suspicious",cheeks="blush")
        call her_main("It's...","angry","suspicious",cheeks="blush")

        if daytime:
            call her_main("It's just that I still have some time left before I have to leave for the classes and...","shock","baseL",cheeks="blush",tears="soft")
        else:
            call her_main("It's not really that late yet, is it?","shock","baseL",cheeks="blush",tears="soft")

        call her_main("uhm...","angry","suspicious",cheeks="blush")
        call her_main("...................","angry","suspicious",cheeks="blush")
        m "You want me to hurt you some more, don't you?"

        if her_whoring < 18:
            call her_main("I don't \"want to\"... ","shock","baseL",cheeks="blush",tears="soft")
            call her_main("But if you insist [genie_name]...","silly","worried",cheeks="blush",tears="soft")
            m "Well, I do insist... apparently."
        else:
            call her_main("Yes please, [genie_name]!","shock","baseL",cheeks="blush",tears="soft")
            call her_main("I'll even let you do it for free...","shock","baseL",cheeks="blush",tears="soft")
            m "Well, in that case..."

        call her_main("Ah...","silly","worried",cheeks="blush",tears="soft")
        call ctc
        call blkfade

        ">You spend some more time with Hermione's breasts..."

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

    if her_whoring < 21:
        $ gryffindor += current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"
    else:
        m "You may leave now, [hermione_name]."

    call her_main("..................","annoyed","worriedL",xpos="base",ypos="base")
    her "Thank you, [genie_name]..."

    if daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."

    hide screen bld1
    hide screen hermione_main
    with d3

    if her_whoring >= 21:

        call her_walk("desk","door",3)

        call her_main("(What about my points?)","disgust","down_raised",cheeks="blush",ypos="head")
        if her_whoring < 24:
            call her_main("(I'll just ask him about it next time...)","annoyed","angryL",ypos="head")
        else:
            call her_main("(Eh, who cares)","base","ahegao_raised",cheeks="blush",ypos="head")

    if her_whoring < 6: #Adds points till 6.
        $ her_whoring +=1

    $ hg_pf_BreastMolester_OBJ.points += 1

    jump end_hg_pf
