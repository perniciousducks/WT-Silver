

### HERMIONE PERSONAL FAVOUR 4 ###

### BUTT MOLESTER ###

label hg_pf_ButtMolester:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(I'll just molest her butt a little.){/size}"

    if hg_pf_ButtMolester_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    if hg_maid_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL")
                m "A maid."
                if whoring >= 5:
                    call her_main("A maid?","base","squint")
                    m "A french maid."
                    call her_main("...","base","baseL")
                    call her_main("Well, if you insist...","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_maid_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass         
    
    hide screen hermione_main
    with d3

    if whoring > 8 and not cho_known:
        jump cho_intro
    
    #First time event
    if whoring >= 0 and whoring <= 5:

        $ new_request_05_heart = 1
        $ hg_pf_ButtMolester_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Come closer, child. Let me molest your butt a little."
        if whoring < 3:
            call her_main("My--","soft","surprised")
            call her_main("My butt?!","shock","shocked")
            jump too_much

        if hg_pf_ButtMolester_OBJ.points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            call her_head("[genie_name]!?","mad","wide",cheeks="blush",xpos="base",ypos="base")
            m "Relax, [hermione_name]. It will be the easiest 15 points you've ever made, I promise."
            call her_head("But....","angry","angry")
            m "All I am going to do is squeeze your little butt a couple of times..."
            call her_head("This is inappropriate, [genie_name]................","annoyed","angryL",cheeks="blush")
            m "Nobody needs to know how exactly you got the points..."
            call her_head("(These 15 points could really make a difference...)","disgust","down_raised",cheeks="blush")
            call her_head("(Darn it.....!)","angry","worriedCl",cheeks="blush")
        else:
            call her_head("Again.....?","annoyed","angryL",cheeks="blush",xpos="base",ypos="base")

        call her_walk_desk_blkfade
        hide screen genie

        call her_head("..................","annoyed","angryL",cheeks="blush")
        call her_head("Do you want me to turn around then, [genie_name]?","annoyed","angryL",cheeks="blush")
        call play_music("playful_tension")# SEX THEME.

        menu:
            m "Hm..."

            #Event A
            "\"Yes. Turn around, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head(".............","annoyed","angryL",cheeks="blush")
                call her_head("...........................","annoyed","angryL",cheeks="blush")
                call her_head("[genie_name], I would like to be done with this sooner rather then later...","annoyed","angryL",cheeks="blush")
                m "Don't rush me [hermione_name]... Let me savour the moment..."
                call her_head(".............................","annoyed","angryL",cheeks="blush")

                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        call slap_her #Calls slapping sound and visual.

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]!!?","scream","wide",cheeks="blush")

                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                call her_head(".......................","annoyed","angryL",cheeks="blush")
                                pass
                            "-Give her butt another slap-":
                                call slap_her #Calls slapping sound and visual.

                                call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                                call her_head("[genie_name], what are you doing!?","angry","worriedCl",cheeks="blush")
                                call her_head("You said all you were going to do is touch!","angry","worriedCl",cheeks="blush")

                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        call her_head(".......................","annoyed","angryL",cheeks="blush")
                                        pass
                                    "-Give her butt another slap-":
                                        call slap_her #Calls slapping sound and visual.

                                        call her_head("Ouch! It hurts!","angry","worriedCl",cheeks="blush")
                                        call her_head("This is so demeaning!","angry","angry",cheeks="blush")
                                        call her_head("You said all you were going to do is touch...","angry","angry",cheeks="blush")
                                        g4 "Just stand still, [hermione_name]!"
                                        call her_head("I don't think so, [genie_name]!","angry","worriedCl",cheeks="blush")
                                        call her_head("No amount of points are worth this humiliation!","scream","angry",cheeks="blush",emote="01")
                                        call her_head("You are abusing your power, [genie_name]!","scream","angry",cheeks="blush",emote="01")
                                        g4 "What?"
                                        call her_head("I'm leaving!","angry","worriedCl",cheeks="blush")

                                        menu:
                                            g4 "Tsk..."
                                            "\"I... I apologize...\"":
                                                call her_head("Just don't do this anymore, [genie_name]...","annoyed","angryL",cheeks="blush")
                                                #pass
                                            "\"You are not getting any points for this!\"":
                                                $ mad += 20
                                                call her_head("Ha! See if I care, [genie_name]!","angry","angry",cheeks="blush")
                                                ### Takes place aftre you refuse to pay her the points.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                with d3

                                                call her_walk("desk","leave",3,redux_pause=1)

                                                g4 "Tsk! (You little brat!)"

                                                $ hg_pf_ButtMolester_OBJ.points += 1

                                                if daytime:
                                                    call play_music("day_theme")
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    call play_music("night_theme")
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu

                                            "\"I'm subtracting points from you then!\"":
                                                $ mad += 30
                                                call her_head("You can't be serious!?","scream","wide",cheeks="blush")
                                                $ gryffindor -=10
                                                g4 "The \"Gryffindor\" house, minus 10 points!"
                                                g4 "There! It's done!"
                                                call her_head("Gr...........","angry","angry",cheeks="blush")
                                                call her_head("........................","angry","angry",cheeks="blush")
                                                call her_head("This is not fair...","angry","suspicious",cheeks="blush",tears="messy")
                                                m "What? Hey, wait, don't you start crying on me..."
                                                call her_head("I hate you, [genie_name]! I hate you!","scream","worriedCl",cheeks="blush",tears="messy")
                                                
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie

                                                call her_walk("desk","leave",2,action="run")

                                                m ".............."
                                                menu:
                                                    "\"Dammit. Now I feel like crap...\"":
                                                        m "Dammit... Now I feel like crap..."
                                                        g9 "But who could resist slapping that little behind of her's?"
                                                    "\"She made me do this, that brat!\"":
                                                        g4 "She made me do this, that brat!"
                                                        m "Acting all wounded now..."
                                                        g9 "I bet she actually enjoyed the slapping and just won't admit it..."

                                                $ hg_pf_ButtMolester_OBJ.points += 1

                                                if daytime:
                                                    call play_music("day_theme")
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    call play_music("night_theme")
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                #You apologized.
                call ctc
                show screen groping_02
                with d7
                call her_head("!!!!!!?","mad","wide",cheeks="blush")
                m "What is it, [hermione_name]?"
                call her_head("It's nothing [genie_name]...","angry","worriedCl",cheeks="blush")
                call her_head("It's just... ","angry","worriedCl",cheeks="blush")
                call her_head("I can't believe this is really happening...","angry","worriedCl",cheeks="blush")
                call her_head("This is so... inappropriate...","angry","worriedCl",cheeks="blush")
                m "Relax, [hermione_name]. It's not like you are enjoying this..."
                call her_head("What? Of course not! This is depraved...","angry","worriedCl",cheeks="blush")
                call her_head("I am making this sacrifice for the the honour of my house...","angry","worriedCl",cheeks="blush")
                m "Yes, concentrate on that..."
                call her_head("....................","angry","angry",cheeks="blush")
                call bld
                call ctc
                call her_head("But, [genie_name]...","open","baseL",cheeks="blush")
                call her_head("Why are {size=+7}you{/size} doing this?","open","baseL",cheeks="blush")

                menu: 
                    m "Hm..."
                    "\"I have my reasons...\"":
                        call her_head("Oh...","disgust","down_raised",cheeks="blush")
                        call her_head("Hm...","annoyed","angryL",cheeks="blush")
                    "\"In the name of science of course!\"":
                        call her_head("Really?!","soft","wide")
                        call her_head("Is this research of some kind?","soft","wide")
                        m "Yeah, sure, I'm researching ehm... er..."
                        m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
                        call her_head("I see...","soft","wide")
                        call her_head("Well, if it is for research then I am glad to be of help...","annoyed","angryL")
                    "-Just squeeze her butt cheeks tighter-":
                        show screen blktone8
                        with d3
                        ">You give Hermione's butt cheeks a couple of extra firm squeezes."
                        hide screen blktone8
                        with d3

                        call her_head("....................","open","baseL",cheeks="blush")
                        call her_head("(Shall I just be quiet, then.....?)","disgust","down_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">You keep on playing with Hermione's buttocks..."
                ">You slide your hands up and down her inner tighs..."
                hide screen blktone8
                with d3

                call her_head("................","angry","worriedCl",cheeks="blush")

                label connection_of_rapes:
                menu:
                    "-Slide your hands under her panties-":
                        show screen blktone8
                        with d3
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... What are you...?","mad","wide",cheeks="blush")
                        m "That's alright, just think about those 15 points your house is about to receive..."
                        call her_head(".............","disgust","down_raised",cheeks="blush")

                        menu:
                            "-Prod her pussy with one of your fingers-":
                                call blkfade
                                
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                call her_head("[genie_name]? No! What are you...?","mad","wide",cheeks="blush")
                                ">Hermione tries to pull away from you..."

                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">Also it is relatively dry... Doesn't look like Hermione's taking any pleasure in this..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass

                            "-Prod her butt-hole instead-":
                                call blkfade
                                
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                call her_head("[genie_name]? No! What are you doing!?","mad","wide",cheeks="blush")
                                ">Hermione tries to pull away from you..."

                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        call her_head("!!?","angry","wide")
                                        ">It's very tight and warm inside..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass

                            "-Stop pushing your luck. Dismiss the girl-":
                                pass

                    "-No. That's enough for today. Dismiss her-":
                        pass

            #Event B
            "\"No. Just stand still, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], please hurry up, before someone discovers us like this...","soft","baseL",cheeks="blush")
                m "What is the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                call her_head("I do know.","annoyed","angryL",cheeks="blush")
                call her_head("But not everyone would see it that way...","annoyed","angryL",cheeks="blush")
                call her_head("So let us be done with this as quick as possible...","annoyed","angryL",cheeks="blush")
                call her_head("Please...","open","baseL",cheeks="blush")
                m "Well, if you insist..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "What is it?"
                call her_head("It's nothing, [genie_name]. Your hands are cold, that's all...","open","baseL",cheeks="blush")
                call bld

                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                hide screen blktone8
                with d3

                call her_head(".........................","annoyed","angryL",cheeks="blush")

                show screen blktone8
                with d3
                ">You give her buttocks a good squeeze..."
                hide screen blktone8
                with d3

                call her_head(".................","angry","worriedCl",cheeks="blush")
                m "Don't look away, [hermione_name]. I want you to look into my eyes."
                call her_head("I would rather not, [genie_name]...","angry","worriedCl",cheeks="blush")

                menu:
                    m "..."
                    "\"Fine. Just keep standing still then.\"":
                        call her_head("Thank you [genie_name]...","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">You massage her buttocks lightly..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">And keep enjoying the sensation of her ass under your hands..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">Then you give Hermione's butt one last squeeze."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                    "\"Open your eyes, or lose the points!\"":
                        $ mad += 7
                        call her_head("Tsk! {size=-5}(You perverted old--{/size}","angry","worriedCl",cheeks="blush")
                        m "Did you say something, [hermione_name]?"
                        call her_head("It's nothing, [genie_name].","angry","angry")

                        show screen blktone8
                        with d3
                        ">You massage her buttocks lightly..."
                        ">Hermione maintains the eye contact as she's been told..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","angry")
                        call her_head("...............................","annoyed","angryL",cheeks="blush")
                        m "What did I tell you about looking away?"
                        call her_head("Yes, I remember...","angry","worriedCl",cheeks="blush")
                        call her_head(".................................","angry","angry")
                        call her_head("...................................","annoyed","angryL",cheeks="blush")
                        call her_head("..................................................","annoyed","angryL",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">You keep on enjoying the sensation of her soft ass-cheeks under your fingertips..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","angry")
                        jump connection_of_rapes

    #Second Event
    elif whoring >= 6 and whoring <= 15:

        $ new_request_05_heart = 2
        $ hg_pf_ButtMolester_OBJ.hearts_level = 2 #Event hearts level (0-3)

        m "Come closer, [hermione_name]. Let me molest your butt a little."
        call her_head("If I must...","open","baseL",cheeks="blush",xpos="base",ypos="base")
        
        call her_walk_desk_blkfade
        hide screen genie

        call her_head("Do you want me to turn around then, [genie_name]?","base","baseL",cheeks="blush")
        call play_music("playful_tension")# SEX THEME.

        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","base","baseL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head(".............","base","ahegao_raised",cheeks="blush")

                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]....?","base","baseL",cheeks="blush")

                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                call her_head("It's Ok...","base","baseL",cheeks="blush")
                                #pass
                            "-Give her butt another slap-":
                                call slap_her

                                call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                                call her_head("[genie_name], what are you doing!?","base","baseL",cheeks="blush")
                                call her_head("You said all you are going to do is touch!","base","baseL",cheeks="blush")

                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        call her_head("It's not a big deal...","base","baseL",cheeks="blush")
                                        #pass
                                    "-Give her butt another slap-":
                                        call slap_her

                                        call her_head("[genie_name], not so loud, please...","silly","ahegao_raised",cheeks="blush")
                                        call her_head("What if somebody hears us?","silly","ahegao_raised",cheeks="blush")
                                        m "Alright, alright... proceeding with groping then..."
                                        call her_head("................","base","baseL",cheeks="blush")

                call ctc
                show screen groping_02
                with d7

                call her_head("...................","base","baseL",cheeks="blush")
                m "You are being awfully quiet today, [hermione_name]."
                call her_head("Am I...?","base","baseL",cheeks="blush")

                if whoring <= 13:
                    call her_head("Well, you know me, [genie_name]...","base","ahegao_raised",cheeks="blush")
                    call her_head("I'm just happy to be able to do my part for the \"Gryffindor\" house....","base","ahegao_raised",cheeks="blush")

                call her_head("Please don't mind it and continue...","base","ahegao_raised",cheeks="blush")
                call her_head("(...to grope me...)","base","glance",cheeks="blush")

                show screen blktone8
                with d3
                ">You keep on playing with Hermione's ass..."
                ">And continue sliding your hands up and down her inner tighs..."
                hide screen blktone8
                with d3

                call her_head("................","base","baseL",cheeks="blush")

                label connection_of_rapes_02:
                menu:
                    "-Slide your hands under her panties-":
                        show screen blktone8
                        with d3
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... What are you...?","open","baseL",cheeks="blush")

                        if whoring <= 13:
                            m "It's alright, just think about those 15 points your house is about to receive..."
                        else:
                            m "It's alright, just try to relax and enjoy yourself"

                        call her_head("As you say...","open","baseL",cheeks="blush")

                        menu:
                            "-Prod her pussy with one of your fingers-":
                                call blkfade
                                
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                call her_head("[genie_name]?","base","baseL",cheeks="blush")

                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass

                            "-Prod her butt-hole instead-":
                                call blkfade
                                
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                call her_head("[genie_name]? What are planning on doing?","base","baseL",cheeks="blush")

                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        call her_head("ah... your finger is up my...","silly","worried",cheeks="blush",tears="soft")
                                        ">It's very tight and warm inside..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass

                            "-Stop pushing your luck. Dismiss the girl-":
                                pass

                    "-No. That's enough for today. Dismiss her-":
                        pass

            "\"No. Just stand still, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","annoyed","angryL",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], please hurry up, before someone discovers us like this...","soft","baseL",cheeks="blush")
                m "What's the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                call her_head("I do know.","annoyed","angryL",cheeks="blush")
                call her_head("But not everyone would see it that way...","annoyed","angryL",cheeks="blush")
                call her_head("So let us be done with this as quick as possible...","annoyed","angryL",cheeks="blush")
                call her_head("Please...","open","baseL",cheeks="blush")
                m "Well, if you insist..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "What is it?"
                call her_head("nothing, [genie_name]. Your hands are cold, that's all...","open","baseL",cheeks="blush")
                call bld

                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                hide screen blktone8
                with d3

                call her_head(".........................","annoyed","angryL",cheeks="blush")

                show screen blktone8
                with d3
                ">And give her Ass a good squeeze..."
                hide screen blktone8
                with d3

                call her_head(".................","angry","worriedCl",cheeks="blush")
                m "Don't look away, girl. I want you to look into my eyes."
                call her_head("I would rather not, [genie_name]...","angry","worriedCl",cheeks="blush")

                menu:
                    m "..."
                    "\"Fine. Just keep on standing still then.\"":
                        call her_head("Thank you [genie_name]...","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">You massage her ass-cheeks lightly..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","worriedCl",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">And keep enjoying the sensation of her butt under your hands..."
                        hide screen blktone8
                        with d3

                        show screen blktone8
                        with d3
                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                        ">Then You give Hermione's butt one last squeeze."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","worriedCl",cheeks="blush")
                    "\"Open your eyes, or you'll lose the points!\"":
                        $ mad += 20
                        call her_head("Tsk! {size=-5}(You perverted old--{/size}","angry","worriedCl",cheeks="blush")
                        m "Did you say something, [hermione_name]?"
                        call her_head("It's nothing, [genie_name].","angry","angry")

                        show screen blktone8
                        with d3
                        ">You massage her ass-cheeks lightly..."
                        ">Hermione maintains eye contact as she's been told..."
                        hide screen blktone8
                        with d3

                        call her_head("....................","angry","angry")
                        call her_head("...............................","annoyed","angryL",cheeks="blush")
                        m "What did I tell you about looking away?"
                        call her_head("Yes, I remember...","angry","worriedCl",cheeks="blush")
                        call her_head(".................................","angry","angry")
                        call her_head("...................................","annoyed","angryL",cheeks="blush")
                        call her_head("..................................................","annoyed","angryL",cheeks="blush")

                        show screen blktone8
                        with d3
                        ">You keep enjoying the sensation of her soft buttocks under your fingertips..."
                        hide screen blktone8
                        with d3

                        call her_head(".....................","angry","angry")
                        jump connection_of_rapes_02  
    

    #Third Event
    elif whoring >= 16:

        $ new_request_05_heart = 3
        $ hg_pf_ButtMolester_OBJ.hearts_level = 3 #Event hearts level (0-3)

        hide screen bld1
        m "Come closer, [hermione_name]. Let me molest your butt a little."
        call her_head("If I must...","open","baseL",cheeks="blush",xpos="base",ypos="base")
        
        call her_walk_desk_blkfade
        hide screen genie

        call her_head("Do you want me to turn around then, [genie_name]?","base","baseL",cheeks="blush")
        call play_music("playful_tension")# SEX THEME.

        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","base","baseL",cheeks="blush")
                show screen no_groping_02
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc
                call her_head(".............","base","ahegao_raised",cheeks="blush")

                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name]....?","base","baseL",cheeks="blush")

                        call slap_her

                        call her_head("!!!!!!!!!!!!!","scream","wide",cheeks="blush")
                        call her_head("[genie_name], what are you doing!?","silly","worried",cheeks="blush",tears="soft")
                        call her_head("You said all you are going to do is touch!","silly","worried",cheeks="blush",tears="soft")
                        m "do you want me to stop, [hermione_name]?"

                        call slap_her

                        call her_head("ahh!!","silly","ahegao_raised",cheeks="blush")
                        call her_head("...I-","disgust","down_raised",cheeks="blush")

                        call slap_her

                        call her_head("no!!","scream","wide")
                        m "then what do you want me to do?"

                        call slap_her

                        call her_head("to keep slapping me!!","silly","ahegao_raised",cheeks="blush")
                        m "and what do you want me to slap?"

                        call slap_her

                        call her_head("my ass!!","silly","ahegao")
                        call her_head("slap my slutty ass!!","open_tongue","ahegao_raised",cheeks="blush")
                        m "you'll have to speak up. I couldn't quite hear you."

                        call slap_her

                        call her_head("slap my slutty ass harder!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                        m "you're being rather loud today."

                        call slap_her

                        call her_head("yess!!","open_tongue","ahegao_raised",cheeks="blush")
                        call her_head("harder!!","silly","ahegao")
                        m "what if someone hears?"

                        call slap_her

                        call her_head("I don't care!!","shock","wide",cheeks="blush")

                        call slap_her

                        call her_head("yes!!!","silly","ahegao_raised",cheeks="blush")

                        call slap_her

                        call her_head("just a little-","grin","ahegao")

                        call slap_her

                        call her_head("I'm gunna","silly","dead")

                        call slap_her

                        call her_head("cumcumcummingcumming","silly","ahegao")
                        call her_head("I'm cumming!!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                        ">you take a moment watch her spasms"
                        m "well, then... proceeding with groping..."
                        call her_head("................","base","ahegao_raised")

                call ctc
                show screen groping_02
                with d7

                call her_head("-wait I juuuus-!!!","base","baseL",cheeks="blush")
                ">Her voice trails off to a squeak as you start to knead her big, round ass"
                m "Hm? what's that? i couldn't hear you, [hermione_name]."
                call her_head("You bastard{image=textheart}","grin","ahegao_mad",cheeks="blush")
                ">Hermione's body quivers as her hips roll"
                m "Well, someone's enjoying herself."
                call her_head("Well, you know me, [genie_name]...","base","ahegao_raised",cheeks="blush")
                call her_head("I'm just happy to be able to do my part","base","ahegao_raised",cheeks="blush")
                call her_head("Please don't mind it and continue...","base","ahegao_raised",cheeks="blush")
                call her_head("(...to grope me...)","silly","dead")

                show screen blktone8
                with d3
                ">You keep on playing with Hermione's ass..."
                ">And continue sliding your hands up and down her inner thighs..."
                hide screen blktone8
                with d3

                call her_head("................","base","baseL",cheeks="blush")

                menu:
                    "-Slide your hands between her legs-":
                        show screen blktone8
                        with d3
                        ">You slowly slide one of your hands towards her crotch..."
                        hide screen blktone8
                        with d3

                        call her_head("[genie_name]... What are you...?","base","ahegao_raised",cheeks="blush")
                        m "something you'll enjoy."
                        m "just relax and leave everything to me."
                        call her_head("As you say...","base","ahegao_raised",cheeks="blush")

                        menu:
                            "-Prod her pussy with one of your fingers-":
                                call blkfade
                                
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                call her_head("[genie_name]?","base","ahegao_raised",cheeks="blush") 

                                ">You force one of your fingers into her little pussy..."
                                ">It's very tight and warm..."
                                ">It is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                call her_head("Ah... your finger is in my...","silly","ahegao")
                                call her_head("Ah... wait--","angry","dead",cheeks="blush",tears="crying")
                                ">you slowly start to pump your fingers..."
                                call her_head("-Only fifteen poin-","shock","down_raised",cheeks="blush",tears="crying")
                                ">you speed up slightly..."
                                call her_head("{image=textheart}-My duty-{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                                ">you start rubbing her clit..."
                                call her_head("!!{image=textheart}-Gryffindor-{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                                m "we can, of course, stop right here, unfulfilled. If that's what you really want."
                                call her_head("...","angry","dead",cheeks="blush",tears="crying")
                                m "well?"
                                call her_head("...Keep going...","shock","down_raised",cheeks="blush",tears="crying")
                                m "hm?"
                                call her_head("Keep fingering my pussy!!","scream","angry",cheeks="blush",tears="messy")
                                m "You want me to keep fingering your cunt? is that what your saying?"
                                call her_head("Yes, [genie_name]! {image=textheart} Fuck my cunt with your fingers!{image=textheart}","open_wide_tongue","ahegao",tears="messy")
                                ">Her hips roll and slam into your fingers."
                                call her_head("Shove them deep in my slutty fuckhole!!{image=textheart}","silly","dead",tears="messy")
                                m "Hm... I don't think my fingers are up to this task after all..."
                                ">You take your fingers out of the girl's gushing cunt."
                                call her_head("what!!? no, don't st-","scream","worriedCl",cheeks="blush",tears="crying")
                                ">...so you can take the dildo out of your desk."
                                call her_head("oh, god yes!!","grin","dead",cheeks="blush",tears="messy")
                                m "this is a much better fit isn't it?"
                                call her_head("aah!{image=textheart}","silly","dead",tears="messy")
                                m "you're far too much of slut to be satisfied by fingers, aren't you?"
                                call her_head("yesfinewhatever!","scream","angry",cheeks="blush",tears="messy")
                                call her_head("i don't care!","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("just don't stop!","silly","ahegao",tears="messy")
                                ">her hips meet your every thrust, nearly tearing the toy from your grip."
                                call her_head("donstopdonstopdonstop-","grin","dead",cheeks="blush",tears="messy")
                                call her_head("pleasepleasepleaseplease-","scream","worriedCl",cheeks="blush",tears="messy")
                                m "are you enjoying yourself, [hermione_name]?"
                                call her_head("yes! I love how you spank me!","grin","dead",cheeks="blush",tears="messy")
                                call her_head("I love how you grope me!","scream","worriedCl",cheeks="blush",tears="crying")
                                call her_head("I love how you play with my little fuckholes!","grin","ahegao_mad",cheeks="blush",tears="messy")
                                call her_head("ohgodohgodohgod","scream","surprised",cheeks="blush",tears="messy")
                                ">Hermione tries to scream as her body bucks and the orgasm takes her, but can't get enough air to do more then moan."
                                call her_head("oooooooh...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                                jump ending_of_screams_of_pleasure

                            "-Prod her butt-hole instead-":
                                call blkfade
                                
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                call her_head("[genie_name]? you're not planning t-","open","baseL",cheeks="blush")

                                ">You force one of your thumbs into her little butt-hole..."
                                with hpunch
                                call her_head("ah... your finger is up my...","silly","ahegao")
                                ">It's very tight and warm inside..."
                                call her_head("ah... wait-","angry","dead",cheeks="blush",tears="crying")
                                ">you slowly start to pump your thumb"
                                call her_head("-only fifteen poin-","shock","down_raised",cheeks="blush",tears="crying")
                                ">you speed up slightly"
                                call her_head("{image=textheart}-my duty-{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                                ">you rotate thumb as you go"
                                call her_head("!!{image=textheart}-gryffindor-{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                                m "we can, of course, stop right here, unfulfilled. if that's what you really want."
                                call her_head("...","angry","dead",cheeks="blush",tears="crying")
                                m "well?"
                                call her_head("...keep going...","shock","down_raised",cheeks="blush",tears="crying")
                                m "hm?"
                                call her_head("keep fingering my ass!!","scream","angry",cheeks="blush",tears="messy")
                                ">you pull your thumb out of her tight little asshole..."
                                call her_head("w-what!?","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("why w-","scream","angry",cheeks="blush",tears="messy")
                                ">...and replace it with two fingers"
                                call her_head("Aaah!","scream","surprised",cheeks="blush",tears="messy")
                                call her_head("B-Bastard!{image=textheart}","scream","worriedCl",cheeks="blush",tears="messy")
                                call her_head("Y-you teasing b-bastard!{image=textheart}{image=textheart}","grin","dead",cheeks="blush",tears="messy")
                                m "do you like this, [hermione_name]?"
                                call her_head("yes!!!","angry","dead",cheeks="blush",tears="crying")
                                m "do you love it?"
                                call her_head("oh, god, yes!!!","silly","ahegao",tears="messy")
                                m "tell me what you love!"

                                call slap_her

                                call her_head("aaah!!{image=textheart}{image=textheart}{image=textheart}","scream","surprised",cheeks="blush",tears="messy")
                                m "I asked you a question."

                                call slap_her

                                call her_head("when you finger my ass!","scream","worriedCl",cheeks="blush",tears="messy")
                                call her_head("i love it when you fuck my ass with your fingers!","grin","dead",cheeks="blush",tears="messy")
                                m "what else do you love?"

                                call slap_her

                                call her_head("when you slap my slutty ass!","scream","worriedCl",cheeks="blush",tears="messy")

                                call slap_her

                                call her_head("a-again! i'm c-c","scream","surprised",cheeks="blush",tears="messy")
                                m "you're cumming again?"

                                call slap_her

                                call her_head("yes!","scream","suspicious",cheeks="blush",tears="messy")
                                m "you're cumming from being spanked again?"

                                call slap_her

                                call her_head("yes!!","scream","worriedCl",cheeks="blush",tears="messy")
                                m "you're cumming from having your headmaster's fingers shoved up your tight little asshole?"

                                call slap_her

                                call her_head("yes!!!{image=textheart}","scream","surprised",cheeks="blush",tears="messy")
                                ">Hermione's body starts to buck wildly."
                                ">you grab herby the hair with your free hand to keep her on the desk even as you frantically pump your fingers into her big, tight ass"
                                call her_head("ohgodohgodohgod","scream","surprised",cheeks="blush",tears="messy")
                                m "what are you cumming from, little whore?"
                                call her_head("!!!!","mad","wide",cheeks="blush",tears="messy")
                                m "where's all this pleasure coming from?!"
                                call her_head("my aaaaaaaass!{image=textheart}","open_wide_tongue","ahegao",tears="messy")
                                ">with one last spasm,hermione collapses to the desk. even after fainting, her Body still twitches, and her hips keep rolling."
                                jump ending_of_screams_of_pleasure

                    "-No. That's enough for today. Dismiss her-":
                        pass

            "\"No. Just stand still, [hermione_name].\"":
                call her_head("As you say, [genie_name]...","soft","base",cheeks="blush")
                show screen no_groping_01
                with d1

                $ menu_x = 0.5 #Menu is moved to the left side.
                $ menu_y = 0.3 #Menu is moved to the left side.

                call hide_blkfade
                call ctc

                call her_head("[genie_name], please hurry...","soft","baseL",cheeks="blush")
                m "What's the problem, [hermione_name]?"

                if daytime:
                    call her_head("I don't have long before class.","annoyed","angryL",cheeks="blush")
                else:
                    call her_head("I don't have long before others notice im missing.","annoyed","angryL",cheeks="blush")

                m "do you enjoy this so much?"
                call her_head("I wouldn't phrase it like that...","annoyed","wink",cheeks="blush")

                call her_head("Can we just start, please...?","angry","worriedCl",cheeks="blush",emote="05")
                m "Well, since you asked so nicely..."
                show screen groping_01
                with d7

                call her_head("!!!","mad","wide",cheeks="blush")
                m "What is it?"
                call her_head("nothing, [genie_name].","base","ahegao_raised",cheeks="blush")
                m "it didn't sound like nothing."
                call her_head("...","base","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                hide screen blktone8
                with d3

                call her_head(".........................","base","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">And give her Ass a good squeeze..."
                hide screen blktone8
                with d3

                call her_head(".................","base","glance")
                m "Don't look away, girl. I want you to look into my eyes."
                call her_head("but its embarrassing, [genie_name]...","angry","down_raised")
                m "..."
                call her_head("...fine, [genie_name]...","base","ahegao_raised",cheeks="blush")
                m "you're being so quiet."
                call her_head("....................","base","closed")
                m "not even a word..."

                show screen blktone8
                with d3
                ">you  enjoy the sensation of her butt under your hands..."
                hide screen blktone8
                with d3

                m "as my hands explore you..."
                m "your thighs..."

                show screen blktone8
                with d3
                ">your hands rub in circles from the sides of her legs to her inner thighs"
                hide screen blktone8
                with d3

                m "your big, firm ass..."

                show screen blktone8
                with d3
                ">You massage her ass-cheeks lightly..."
                hide screen blktone8
                with d3

                call her_head(".....................","grin","ahegao")
                m "your loins..."

                show screen blktone8
                with d3
                ">one hand circling just above her clit."
                hide screen blktone8
                with d3

                call her_head(".....................","silly","dead")
                m "is there something you want?"
                call her_head(".....................","annoyed","wink",cheeks="blush")
                call her_head("...i... {size=-5}...i want you to finger me...{/size}","disgust","down_raised",cheeks="blush")
                m "Did you say something, [hermione_name]?"
                call her_head("...it's nothing, [genie_name]...","open","ahegao_raised",cheeks="blush")

                show screen blktone8
                with d3
                ">You massage her ass-cheeks lightly with one hand as the other continues to circle above her cunt, fingers brushing against her clit..."
                ">Hermione maintains eye contact as she's been told..."
                hide screen blktone8
                with d3

                m "you're lying."
                call her_head("I... i said i want you to finger me!","shock","worriedCl")

                show screen blktone8
                with d3
                ">You swiftly plunge two fingers into her drenched snatch."
                hide screen blktone8
                with d3

                call her_head("!!!{image=textheart}{image=textheart}","grin","ahegao")

                show screen blktone8
                with d3
                ">you start to pump your fingers inside her before she can do more than gasp."
                hide screen blktone8
                with d3

                call her_head("...................................","disgust","down_raised",cheeks="blush")
                m "did i say you could look away?"
                call her_head("..................................................","base","ahegao_raised",cheeks="blush",tears="soft")
                m "good girl"

                show screen blktone8
                with d3
                ">her hips roll in rhythm as you fuck her with your fingers"
                hide screen blktone8
                with d3

                m "do you like this?"
                m "you like it when i finger your cunt?"
                call her_head("i love it!{image=textheart} i love your long fingers in my tight, wet cunt!!{image=textheart}","silly","ahegao",tears="crying")
                m "well, i think we can do better."

                show screen blktone8
                with d3
                ">with your other hand, you force a finger up her tight asshole."
                hide screen blktone8
                with d3

                call her_head("!!!","scream","surprised",cheeks="blush",tears="messy")
                call her_head("my cunt and my ass!","grin","dead",cheeks="blush",tears="messy")

                show screen blktone8
                with d3
                ">you don't even need to move as she pounds herself against your fingers."
                hide screen blktone8
                with d3

                call her_head("fingering my cunt and ass!{image=textheart}{image=textheart}","silly","dead",tears="messy")
                m "no, we can still do better."

                show screen blktone8
                with d3
                ">you force another finger up her ass."
                hide screen blktone8
                with d3

                call her_head("iloveitiloveitiloveit","grin","ahegao",tears="messy")
                m "what do you love, [hermione_name]?"
                call her_head("ah!!{image=textheart} i love your fingers in my ass and cunt!{image=textheart}","shock","wide",tears="messy")

                show screen blktone8
                with d3
                ">her movements have become more frantic."
                hide screen blktone8
                with d3

                m "are you cumming, [hermione_name]?"
                call her_head("yes!!","scream","surprised",cheeks="blush",tears="messy")
                call her_head("i'm cumming!!","scream","worriedCl",cheeks="blush",tears="messy")
                call her_head("i'm cumming from being fucked with your fingers!!","grin","dead",cheeks="blush",tears="messy")
                m "look at me!"
                m "show me your fuck-face!"
                m "i want to see you cum from whoring yourself for fifteen points."
                call her_head("aaaaaaaaah!!!","scream","surprised",cheeks="blush",tears="messy")
                jump ending_of_screams_of_pleasure  
    
    label ending_of_screams_of_pleasure:
    call blkfade
    
    stop music fadeout 1.0
    ">You release her..."
    m "This will do for now."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    call her_chibi("stand","mid","base")
    show screen genie

    $ menu_x = 0.5 #Menu is moved to the left side.
    $ menu_y = 0.5 #Menu is moved to the left side.
    
    call hide_blkfade

    if whoring <= 13:
        $ gryffindor +=15
        m "The \"Gryffindors\" get 15 points!"
    else:
        m "well done, [hermione_name]."

    call her_main("..................","grin","glance",cheeks="blush",tears="mascara",xpos="base",ypos="base")
    her "Thank you [genie_name]..."

    if daytime:
        her "Now if you don't mind I'd better go. My classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."

    hide screen bld1
    hide screen hermione_main
    with d3
    
    if whoring >= 3 and whoring <= 5: #First level. Not happy.

        call her_walk("mid","door",2)

        call her_head("...........................","disgust","down_raised",cheeks="blush")

        pause.5
        call her_chibi("leave","door","base")

    else:

        call her_walk("mid","leave",2)
    
    if whoring < 6: #Adds points till 6.
        $ whoring +=1

    $ hg_pf_ButtMolester_OBJ.points += 1
    
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
    











