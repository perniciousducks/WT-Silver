

### Hermione Blowjob ###

label hg_pf_SuckIt: #15+
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"

    if hg_pf_SuckIt_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_requests_menu

    call set_u_ani("blowjob_ani","hand_ani",0,10)
    $ mouth_full_of_cum = False

    call bld

    #Intro
    if hg_pf_SuckIt_OBJ.points == 0:

        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "I plan to grant \"Gryffindor\" 55 house points today..."
        m "If you suck me off..."

        if her_whoring < 15: # LEVEL 05
            jump too_much

        call her_main("Oh...","open","down")
        call her_main("Alright.","base","down")
        m "Really? Just like that?"
        call her_main("Yes. I know I'm supposed feel outraged...","angry","down_raised")
        call her_main("But somehow I do not...","angry","base")
        call her_main("I suppose I am just glad that I can help out my house...","base","down")
        call her_main("And if to do that I must put your penis in my mouth so be it...","upset","closed")
        m "Well, alright then."
        call her_main("Although, now when I say it out loud like this...","angry","down_raised")
        m "Too late! You already said \"yes\"!"
        call her_main("I know...","grin","worriedCl",emote="05")
        call her_walk_desk_blkfade

        call hg_blowjob_1 #First Blowjob.

        $ hg_pf_SuckIt_OBJ.level = 1
        jump end_hg_blowjob

    #Second Event.
    elif hg_pf_SuckIt_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base")
        m "How about another blowjob?"
        call play_music("playful_tension") # SEX THEME.
        call her_main("[genie_name], how dare you propose such a thing to one of your pupils!","scream","angry",emote="01")
        m "Wha...?"
        call her_main("This is unbecoming of a man of your standing.","scream","angry",emote="01")
        call her_main("You should be ashamed of yourself [genie_name]!","angry","angry")

        menu:
            m "???"
            "\"Fine. No points to you then! Leave!\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("[genie_name], calm down, please.","grin","worriedCl",emote="05")
                m "You are dismissed, [hermione_name]."
                call her_main("[genie_name], please, I didn't mean any of the things I said.","grin","worriedCl",emote="05")
                m "What?"

            "\"Ehm... I am sorry?\"":
                stop music fadeout 1.0
                call her_main("*Giggle*","base","base")
                m "Huh?"
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main("I got you... [genie_name].","grin","worriedCl",emote="05")
                m "What?"

        call her_main("Well, so much has happened lately...","base","base")
        her "I had so many new experiences that kind of changed the way I look at things..."
        her "So I was just trying to imagine how the \"old me\" would've reacted to this."
        m "So..."
        g4 "You were messing with me then?"
        call her_main("uhm... I'm sorry [genie_name], I didn't mean to...","angry","worriedCl",emote="05")
        g4 "You nasty little girl! You must be punished!"
        g9 "I'll punish you with my cock!"
        call her_main("...............................","angry","worriedCl",emote="05")
        call blkfade #Needs to be active first!

        call hg_blowjob_1 #Same as first. Change to second.

        $ hg_pf_SuckIt_OBJ.level = 2
        jump end_hg_blowjob


    #Third Event.
    elif hg_pf_SuckIt_OBJ.points >= 2 and her_whoring < 21:
        call play_music("playful_tension") # SEX THEME.
        m "Suck my dick, [hermione_name]."
        call her_main("Of course...","base","base",xpos="mid",ypos="base")
        call her_walk_desk_blkfade

        call update_hidden_bj_list

        call hg_hidden_blowjob #Hidden Blowjob with Snape, Luna;

        $ hg_pf_SuckIt_OBJ.level = 3
        jump end_hg_blowjob


    #Fourth Event
    elif hg_pf_SuckIt_OBJ.points >= 2 and her_whoring >= 21:
        call play_music("playful_tension") # SEX THEME.
        m "Suck my dick, [hermione_name]."
        call her_main("Of course [genie_name]...","base","ahegao_raised",xpos="mid",ypos="base")
        call her_walk_desk_blkfade

        call update_hidden_bj_list

        $ random_number = renpy.random.randint(1, 5)
        if hg_hidden_bj_list != hg_hidden_bj_seen_list:
            call hg_hidden_blowjob

        elif random_number in [1,2]:
            call hg_hidden_blowjob

        else:
            call hg_blowjob_4 #Daddy Roleplay, Worship Cock;
            $ hg_pf_SuckIt_OBJ.level = 4

        jump end_hg_blowjob





### First Blowjob ###

label hg_blowjob_1: #Call label. Returns.
    call play_music("playful_tension") # SEX THEME.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    call her_chibi("hide")
    show screen chair_left
    call u_play_ani
    hide screen bld1
    hide screen blkfade
    with fade
    call ctc

    call her_main("*Slurp!* *Gulp!* *Slurp!*",ypos="head")
    m "Yes..."
    m "Try to take it deeper now..."
    call her_main("*Gulp!* *Gobble!* *Gobble!*")
    m "Yes, like that. Good."
    call her_main("*Slurp!* *Gltch!* *Gulp!*")
    m "Yes, that's a good girl."

    menu:
        m "Hm..."
        "\"Whatever happened to your \"MRM\" thing?\"":
            call her_main("*Slurp?*",ypos="head")
            call u_pause_ani
            call her_main("Oh, well...","angry","down_raised")
            call her_main("We are still active, but...")
            call u_play_ani
            her "*Slurp!* *Gobble!*"
            call u_pause_ani
            call her_main("But we are not getting as popular and as much support as I thought we would...","angry","wink")
            call u_play_ani
            her "*Slurp!* *Gulp!* *Gulp!*"
            m "Oh... This is good..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Hm..."
            m "So you don't mind selling me sexual favours, letting me play with your tits and such..."
            her "*Gobble!* *Gltch!* *Slurp!*"
            m "And then condemn such behavior in front of the other students."
            her "*Slurp!* *Slurp!* *Gulp!*"
            m "You perverted, little hypocrite."
            her "*Gulp--"
            call u_pause_ani
            call her_main("That's not what we stand for, [genie_name].","angry","base")
            m "What do you mean?"
            call her_main("The \"MRM\" is about gender equality.","open","closed")
            call her_main("We are not as much against selling sexual favours to the teachers...")
            call her_main("As we are against the gender inequality that the selling of sexual favour creates...")
            m "Hm..."
            m "This conversation is starting to bore me..."
            m "Suck on my cock some more before we continue."
            call her_main("Of course, [genie_name].","soft","ahegao")
            call u_play_ani
            her "*Gobble!* *Slurp!* *Slurp!*"
            m "Yes, much better..."
            m "But you still disapprove of selling the favours, right?"
            her "*Slurp--"
            call u_pause_ani
            call her_main("Yes, it is frowned upon...","upset","closed")
            m "And yet, you are the biggest offender by far."
            call her_main("But what choice do I have?","upset","closed")
            call her_main("I've been put in a very difficult position...")
            m "The cock, [hermione_name]."
            call her_main("Right, sorry...","upset","closed")
            call u_play_ani
            her "*Slurp!* *Gulp!* *Gltch!*"
            her "*Slurp--"
            call u_pause_ani
            call her_main("This one time we had a meeting right after I sold you another favour, [genie_name].","angry","base")
            call her_main("I had to give a speech with my uniform all messy and stained.")
            call her_main("It felt awful that I had to do that...")
            m "You did enjoy it a little bit though..."
            call her_main("Well...","angry","down_raised")
            m "Just admit it."
            call her_main("...............","angry","base")
            m "Yes, I knew it. You took pleasure in it, you little perv."
            call her_main("I suppose it was embarrassing and exciting at the same time...","angry","down_raised")
            call her_main("And it made me feel even worse about myself.")
            m "You poor thing."
            m "Cock back in the mouth."
            call her_main("Yes, [genie_name].","angry","base")
            call u_play_ani

        "\"Your parents must be proud of you...\"":
            call her_main("*Slurp--",ypos="head")
            call u_pause_ani
            call her_main("Yes, I believe they are...","smile","happyCl")
            call her_main("With me being an excellent student despite being muggle-born and all...","base","happyCl")
            call her_main("Although at first they were against sending me to some \"Bogus boarding school\".","angry","base")
            call her_main("Took some effort to convince them that \"Hogwarts\" is a respectable institution.","base","happyCl")
            m "Yes, a respectable institution indeed."
            m "Cock back in your mouth [hermione_name]."
            call u_play_ani
            her "*Slurp!* *Gulp!* *Gobble!*"
            m "Yes, just keep at it for a while..."
            her "*Slurp!* *Gltch!* *Gulp!*"
            m "Good, good..."
            m "So, what would your folks say if they were to see you now, [hermione_name]?"
            her "*Slurp--"
            call u_pause_ani
            call her_main("They would not understand of course...","open","down")
            call her_main("But I do not care.")
            call her_main("I am not afraid to \"get my hands dirty\" and do what needs to be done.","upset","closed")
            m "A bit rebellious, aren't you?"
            call her_main("Hm... I suppose I am.","angry","wink")
            m "Back to sucking then. Teach your folks a lesson."
            call u_play_ani
            her "*Slurp!* *Slurp!* *Slurp!*"

        "\"Tell me about the \"Gryffindor\" house.\"":
            call her_main("*Slurp--",ypos="head")
            call u_pause_ani
            call her_main("What can I say that you don't already know, [genie_name]?","soft","baseL")
            m "Yes... Ehm... I know everything of course."
            m "But I want to see how much you know."
            m "To test your knowledge on the subject."
            call nar(">As soon as you mention \"test\" Hermone's eyes light up with excitement.")
            call her_main("OK. But I need a moment gather my thoughts...","smile","happyCl",emote="06")
            call u_play_ani
            her "*Slurp!* *Slurp!* *Gulp!*"
            m "Oh, yes... Take as much time as you need, [hermione_name]."
            her "*Slurp!* *Gulp!* *Slurp!*"
            her "*Gulp--"
            call u_pause_ani
            call her_main("The \"Gryffindor\" house was founded by Godric Gryffindor, thus the name.","open","down")
            call her_main("The heraldic animal of \"Gryffindor\" is the lion...")
            call her_main("And it's colors are red and gold.","open","closed")
            call u_play_ani
            her "*Gulp!* *Slurp!* *Slurp!*"
            call u_pause_ani
            call her_main("Professor Minerva McGonagall is the headmaster of our house.","open","closed")
            call her_main("The \"Gryffindor\" house emphasizes the traits of courage...")
            call her_main("As well as \"daring, nerve and chivalry\"...")
            call her_main("And thus its members are generally regarded as brave but reckless...")
            call u_play_ani
            her "*Slurp!* *Slurp!* *Slurp!*"
            call u_pause_ani
            call her_main("\"Gryffindor\" corresponds roughly to the element of fire...","open","closed")
            call her_main("And for that reason the colours of red and gold were chosen.")
            call u_play_ani
            her "*Slurp!* *Gulp!* *Slurp!*"
            m "Hm..."
            m "Well, I thought I could turn this around somehow to make fun of you..."
            her "*Slurp??*"
            m "Well, with your house representing courage and righteousness and such..."
            m "And you being a nasty slut..."
            call u_pause_ani
            call her_main("[genie_name]!","scream","angry",emote="01")
            m "But to be honest..."
            m "\"Daring, nerve, fire, recklessness\"..."
            m "That sort of describes your personality quite well..."
            call her_main("[genie_name]...","base","base")
            call u_play_ani
            her "*Gobble!!* *Gltch!!* *Gobble!!!*"
            m "Good girl..."

    m "Good..."
    call her_main("*Gobble!* *Slurp!* *Slurp!*",ypos="head")
    m "Good... Back and forth, back and forth... Good girl."
    her "*Slurp!* *Slurp!* *Slurp!*"
    her "*Slurp--"
    call u_pause_ani
    call her_main("[genie_name]... I am a... whore.","open","down")
    m "What?"
    call u_play_ani
    her "*Slurp-Slurp-Slurp!*"
    call u_pause_ani
    call her_main("I truly am a slut and deeply enjoy sucking your cock.","angry","base")
    m "Oh, yes, yes... Say more things like that."
    call u_play_ani
    her "*Slurp!* *Gulp!* *Slurp!*"
    call u_pause_ani
    call her_main("Please, [genie_name]. Cum for me.","soft","ahegao")
    with hpunch
    g4 "Argh! You little...!!!"
    g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"

    menu:
        m "..."
        "-Warn her-":
            call her_main("Yes, I love to suck and --","soft","ahegao",ypos="head")
            g4 "Heads up, [hermione_name]! Here it comes!"
            call her_main("!!!","angry","wide")
            call ctc
            hide screen bld1
            call blkfade

            call set_u_ani("cum_in_mouth_ani")
            call u_play_ani
            ">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."
            call cum_block
            g4 "{size=+7}ARGH!{/size}"
            her "*Gulp!-Gulp!-Gulp!*"
            with hpunch
            g4 "And some more!"
            her "*Gulp!* *Gulp!* *Gulp!*"
            call hide_blkfade
            call ctc

            call bld
            m "Well, I think that's it."
            call u_pause_ani
            call her_main("..............","cum","worriedCl")
            m "Are you alright there, [hermione_name]?"
            call her_main("Yes, [genie_name]...","grin","dead")
            call her_main("You came so much...")
            m "You managed to swallow it all though."
            call her_main("Yes... I thought I would choke...","grin","dead")
            call her_main("But I made a promise to myself that I won't let go of your penis no matter what!")
            m "Good girl."
            call her_main("Thank you, [genie_name].","grin","dead")
            call her_main("But, still... You came so much...")
            call her_main("I almost feel as if I just got fed...","soft","ahegao")
            call her_main("My stomach is so full...")
            g9 "Yes, I fed you with my cum!"

            if daytime:
                call her_main("I think I may skip the meal and go straight to class today.","soft","ahegao")
            else:
                call her_main("Yes. I think I may skip supper tonight...","soft","ahegao")

            call her_main("Can I get paid now?","angry","wink")
            hide screen hermione_main
            call blkfade

            return

        "-Don't bother-":
            call her_main("Yes, I love to suck and --","soft","ahegao",ypos="head")
            call cum_block
            g4 "{size=+7}Whore!{/size}"
            call her_main("!!?","shock","wide")
            hide screen bld1
            call set_u_ani("cum_on_face_ani")
            call u_play_ani

            call ctc

            call bld
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_07.png"
            call her_main("[genie_name]...","shock","wide")
            g4 "Don't you move now, [hermione_name]."
            g4 "Yes, just be still and take it."
            g4 "Argh! You little slut! You make me cum hard, [hermione_name]!"
            call her_main("..............","angry","base",tears="soft")
            m "Whew..."
            call set_u_ani("cum_on_face_blink_ani")
            call her_main("..............","normal","worriedCl")
            m "Alright, I'm done..."
            call her_main(".................","open","base")

            if daytime:
                her "My classes are about to start..."

            m "Just wipe it off and you'll be alright."
            call her_main("............","open","base")
            m "Unless, you don't want to."
            call her_main("Huh?","angry","worriedCl",emote="05")
            m "And would rather go outside looking like this."
            m "Let everyone see what a nasty little slut you are."
            call her_main("Of course not, [genie_name]!","angry","worriedCl",emote="05")
            call ctc
            call blkfade

            stop music fadeout 1.0

            if daytime:
                m "You better go before you are late for your classes..."
            else:
                m "It's getting late..."
                call her_main("Yes...","angry","worriedCl",emote="05")

            call her_main("Can I get paid before I leave, [genie_name]?","upset","wink")
            hide screen hermione_main
            call blkfade

            $ aftersperm = True

            return



### Hidden Blowjob ###

label hg_hidden_blowjob: #Call label. Returns.
    call play_music("playful_tension") #HERMIONE
    hide screen genie
    call her_chibi("hide")
    show screen chair_left
    call u_play_ani
    hide screen bld1
    hide screen blkfade
    with fade
    call ctc

    call her_main("*Slurp!* *Slurp!* *Gulp!*",ypos="head")
    m "Yes, good girl..."
    her "*Slurp!* *Gobble!* *Slurp!*"

    call play_sound("knocking") #Sound someone knocking on the door.
    call nar("> *Knock-knock-knock!*")
    her "{size=+7}!!!{/size}"
    m "Hm?"

    if daytime:
        m "Who could that be?"
    else:
        m "Who could that be at this hour?"

    call u_pause_ani


    #Priority.
    if "snape" in hg_hidden_bj_list and "snape" not in hg_hidden_bj_seen_list:
        $ character_choice = "snape"
    elif "luna" in hg_hidden_bj_list and "luna" not in hg_hidden_bj_seen_list:
        $ character_choice = "luna"
    elif "tonks" in hg_hidden_bj_list and "tonks" not in hg_hidden_bj_seen_list:
        $ character_choice = "tonks"

    #Random Pick.
    else:
        $ character_choice = renpy.random.choice(hg_hidden_bj_list)


    #Calls Scene.
    if character_choice == "snape":
        call hg_hidden_blowjob_snape

    if character_choice == "luna":
        call hg_hidden_blowjob_luna

    if character_choice == "tonks":
        call hg_hidden_blowjob_tonks

    #Genie Cums.
    call hg_hidden_blowjob_cumming

    return



label hg_hidden_blowjob_snape: #Call label. Returns.
    call her_main("([genie_name], what should I do?)","shock","wide",ypos="head")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    sna "Albus? Are you there? I need to talk to you."
    call her_main("(It's professor Snape!)","angry","base")
    call her_main("([genie_name], please, send him away, I beg you!)")

    menu:
        m "..."
        "\"Please, come on in, Severus.\"":
            if "snape" not in hg_hidden_bj_seen_list:
                $ hg_hidden_bj_seen_list.append("snape")
            $ her_mood = 30
            stop music fadeout 1.0
            call her_main("([genie_name], no!)","angry","angry",emote="01",ypos="head")

            call nar(">Hermione gives your balls a firm twist full of frustration.")
            g4 "Ouch!"

            call play_sound("door")
            call sna_chibi("stand","door","base")
            hide screen bld1
            with d3
            pause.8
            call sna_walk("door","mid",4)
            pause.2

            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME

            call sna_head("Good, you are here.","snape_01",xpos="base",ypos="base")
            call u_play_ani
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            call sna_head("Listen, there is something I want to discuss...","snape_06")
            call sna_head("Hm...?","snape_05")
            call sna_head("Genie? Are you alright?")
            her "{size=-4}(Ginny!!? Is she here as well?!){/size}"
            her "{size=-4}(No, please! I will die of shame!){/size}"
            m "Yes, Severus, I am fine..."
            her "{size=-4}(What? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
            call sna_head("What are you... looking at?","snape_05")
            m "Ehm... Just admiring...{w} the cupboard."
            m "Please, continue..."
            call sna_head("...............","snape_05")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            m "Did you want to discuss something?"
            call sna_head("Yes. That Hermione girl.","snape_06")
            her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
            m "Oh... What about her?"
            call sna_head("You promised that you would take care of the little witch.","snape_04")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            call sna_head("But she is still being a major pain in my arse!","snape_04")
            call sna_head("Her tactics have changed...")
            call sna_head("But the amount of grief she manages to bring me is the same...","snape_03")
            m "I see... ah..."
            call sna_head("I swear, that girl is driving me crazy!","snape_10")
            g4 "Yeah, she is driving me crazy as well... ah..."
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            call sna_head("Will you take care of this then?","snape_04")
            m "Yes. She'll get what she deserves."
            call sna_head("Good. That is all I wanted to hear.","snape_06")

            if daytime:
                m "Well, have a good day, Severus."
                call sna_head("Yes, thank you.","snape_06")
            else:
                m "Good night, Severus."
                call sna_head("Right...","snape_06")

            call sna_chibi("stand","mid","base",flip=True)
            hide screen bld1
            with d3
            pause.2
            call sna_walk("mid","leave",3)
            stop music fadeout 1.0
            call ctc
            call blkfade

            call play_music("playful_tension") # SEX THEME.
            ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
            ">Seeing her being so confused and vulnerable and yet continuing to perform her task diligently pushes you over the edge."
            g4 "(Here it comes!)"

            return

        "\"I am busy right now, Severus.\"":
            call her_main("(Thank you, [genie_name].)","angry","base",ypos="head")
            sna "Busy? With what?"
            sna "All you do is sit on you arse all day."
            sna "I really need to talk to you about something."
            m "I said I am busy, Severus."
            m "Understood? I am \"busy\"!"
            sna "Oh... You mean \"Busy\" busy? Gotcha!"
            sna "Well, I'll talk to you later then."

            return



label hg_hidden_blowjob_luna: #Call label. Returns.
    call her_main("([genie_name], what should I do?)","shock","wide",ypos="head")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    lun "[lun_genie_name]? Are you there? I need to talk to you."
    call her_main("(It's Luna!)","disgust","wide")
    call her_main("Please, [genie_name], send her away, I beg you!","shock","worriedCl")

    menu:
        m "..."
        "\"Please, come on in, [luna_name].\"":
            if "luna" not in hg_hidden_bj_seen_list:
                $ hg_hidden_bj_seen_list.append("luna")
            $ her_mood += 30
            stop music fadeout 1.0
            call her_main("[genie_name], no! Why would you let-","angry","angry",emote="01",ypos="head")
            m "Quiet, [hermione_name]! Unless you want to be noticed..."

            #Luna comes in
            call play_sound("door") #Sound of a door opening.

            call lun_walk("door","mid",3)

            call lun_main("Hello, [lun_genie_name].","soft","base","base","down")
            $ g_c_u_pic = "blowjob_ani" # sucking
            call u_play_ani

            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            g9 "Miss Lovegood! How can I help you?"
            call lun_main("I have a message for you, [lun_genie_name],... from Professor Sprout.","open","base","base","R")
            m "Professor Sprout?"
            m "(Who was that again?)"
            call lun_main("Yes, she's sent me to inform you about the school's latest yield of Venomous Tentacula.","open","base","raised","mid")
            m "(Venomous Tentacles?)"
            her "{size=-4}(Those things are nasty... *Slurp...* *Gulp...*){/size}"

            lun "Very feisty little plants, they are. And still quite young."
            lun "They'll wither if you don't take care of them properly..."
            m "So why tell me?"
            call lun_main("They have just started sucking!","smile_large","happyCl","raised","mid")
            with hpunch
            m "What?"
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            call lun_main("Sucking, [lun_genie_name]!","base","seductive","base","mid")
            call lun_main("It's so cute! They suck at each others tentacles with their little mouths!","soft","base","raised","up")
            m "(Plants with mouths?)"
            call lun_main("Normally they only do that shortly before they spread their spores.","open","base","base","R")
            call lun_main("Which means they are almost ready!","grin","happyCl","raised","mid")
            m "Ready? for what?"
            call lun_main("Pollination!","soft","seductive","base","mid")
            call lun_main("That's when they weave their tentacles into each other and shoot out their spores.","open_tongue","seductive","base","up")
            m "(How nasty!)"

            call lun_main("You won't believe how hard it is to get them to that stage...","pout","mad","mad","up")
            call lun_main("It's quite an achievement!","base","base","base","mid")

            m "I'm more than familiar with them!"
            call lun_main("You are?","soft","wink","raised","mid")
            g4 "Those young-{w=0.9} sucking- {w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} UGH! {w=0.2} Troublemakers!"
            g4 "Yes. I've got one right here!"
            call lun_main("Oh! can I see it, [lun_genie_name]?","grin","wide","raised","mid")
            m "I'm afraid not, [luna_name]."
            g9 "It's such a shy little thing. You'd better not get any closer!"
            call lun_main("Aww... ok.","pout","base","sad","down")
            m "I know everything about those little devils..."
            m "At first there was just bitching and moaning about every tiny little thing I wanted to do..."
            m "But now, straight down on the knees... right in front of me."
            g4 "Sucking like crazy!"
            call lun_main("(So they do not only have a head but also knees... I didn't even know that!)","soft","base","raised","up")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"

            call lun_main("Sprout told us to be careful, [lun_genie_name]. As you probably know, they like to spit... and bite...","soft","base","base","mid")
            m "Truly?"
            call lun_main("Yes. If you aren't careful, they'll hit you with their saliva, or bite at your limbs!","clench","annoyed","raised","down")
            call lun_main("Luckily, there is an easy way to make them stop such behavior!","base","seductive","base","mid")
            m "I'm all ears..."
            call lun_main("They hate being spat on just as much as you, [lun_genie_name]. Maybe even more so!","soft","seductive","base","L")
            m "(Those are some weird fucking plants...)"
            call lun_main("She said that if a Venomous Tentacula ever acts up-","open","closed","raised","mid")
            call lun_main("You should show dominance by spitting on it and put it in its place!","angry","angry","angry","down")
            call lun_main("Her words...","pout","base","raised","R")
            g9 "Like this?"
            call spit_on_her

            g4 "Take that, you nasty little slu-... Uhh, plant."
            her "{size=-4}(What the... *Slurp...* *Slurp...* *Gulp...*){/size}"
            call lun_main("That's right, [lun_genie_name]!","grin","happyCl","raised","mid")
            g4 "This one wants more spit!"
            call spit_on_her
            her "{size=-4}(Stop it! *Slurp...* *Slurp...* *Gulp...*){/size}"
            call lun_main("Professor Sprout said, sometimes, a bit of tough love is the only thing that can make them behave.","clench","angry","angry","down")
            m "She did?"
            g9 "Oh no, mine is fighting back!"
            call lun_main("Be careful, [lun_genie_name]! Or she'll bite you!","clench","closed","sad","mid")
            g4 "Don't worry, this one's getting a beating!"
            call slap_her
            her "{size=-4}(Ouch!... *Slurp...* *Slurp...* *Gulp...*){/size}"
            call slap_her
            call slap_her
            g4 "Had enough, you narsty little thing?"
            call slap_her
            g4 "Want some more?"
            call slap_her
            call slap_her

            call lun_main("You seem so well versed with plants!","grin","wide","raised","mid")
            call lun_main("I need to tell Professor Sprout, she'll be overjoyed to hear about your training methods!","grin","happyCl","raised","mid")
            m "Give her my thanks, [luna_name]. She's a smart lady, this Sprout!"
            g9 "Full of great ideas!"
            call lun_main("I will, [lun_genie_name].","smile","seductive","base","mid")

            if daytime:
                call lun_main("Have a nice day!","smile_large","happyCl","base","mid")
            else:
                call lun_main("Good night!","smile_large","happyCl","base","mid")

            #Luna leaves.
            hide screen luna_main
            hide screen bld1
            with d3

            stop music fadeout 1.0

            call lun_walk("mid","leave",3)
            pause.5

            m "Well that wasn't too bad, was it?"
            her "{size=-4}(............................. *Slurp...* *Slurp...* *Gulp...*){/size}"
            call blkfade

            call u_play_ani
            call play_music("playful_tension") # SEX THEME.
            ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."

            return

        "\"I am busy right now, [luna_name].\"":
            call her_main("(Thank you, [genie_name].)","angry","base",ypos="head")
            lun "Oh... well, I'll visit you later then, [lun_genie_name]."
            if daytime:
                lun "Have a good day!"
            else:
                lun "Have a good night!"
            m "I definitely will, Miss Lovegood!"

            return

#Add scene with Astoria here.
#Add scene with Susan here.
#Add scene with Cho here.

label hg_hidden_blowjob_tonks: #Call label. Returns.
    call her_main("([genie_name], what should I do?)","shock","wide",ypos="head")
    m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
    ton "[ton_genie_name]? Is it ok if I come in?"
    call her_main("(It's Professor Tonks!)","clench","worriedCl")
    call her_main("Please, [genie_name], don't let her in!","open","worried")
    call her_main("I don't want my teacher to see me like this!","shock","down")

    menu:
        m "..."
        "\"Please, come on in, [tonks_name].\"":
            if "tonks" not in hg_hidden_bj_seen_list:
                $ hg_hidden_bj_seen_list.append("tonks")
            $ her_mood += 10
            stop music fadeout 1.0
            call her_main("[genie_name], no! Please she will know that-","angry","angry",emote="01",ypos="head")
            m "Shhhhsh. Keep your voice down..."

            #Tonks comes in
            call play_sound("door") #Sound of a door opening.

            #call ton_walk("door","mid",3)

            if daytime:
                call ton_main("Hello, [ton_genie_name].","base","base","base","mid",xpos="right",ypos="base")
            else:
                call ton_main("Good evening, [ton_genie_name].","base","base","base","mid",xpos="right",ypos="base")

            $ g_c_u_pic = "blowjob_ani" # sucking
            call u_play_ani

            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            g9 "Tonks! What can I do for you?"
            call ton_main("[ton_genie_name], I was wondering if we could-","open","base","raised","R")
            call ton_main("(...)","base","base","base","mid")
            call ton_main("Am I interrupting something?","horny","base","raised","down")
            her "She's going to find out!!!"
            m "Nothing drastically..."

            menu:
                "-Tell the truth-":
                    m "Just stuffing Miss Granger's cute little mouth..."
                    g9 "With my cock!"
                    call u_pause_ani

                "-Lie-":
                    m "A... Just admiring...{w} the woodworks."
                    call ton_main("Like I'm going to believe that...","open","base","base","mid")
                    call ton_main("Are you masturbating, [ton_genie_name]?","horny","base","raised","mid")
                    call ton_main("Are you stroking your hard, {w}magnificent, {w}cock?","open_wide_tongue","base","base","ahegao")
                    with hpunch
                    her "{size=-4}(*Blergchhhgh...* *Caugh...* *Caugh...* *Caugh...*){/size}"
                    call u_pause_ani
                    her "{size=-4}What??{/size}"
                    call ton_main("who was that?","base","base","raised","mid")
                    call ton_main("[ton_genie_name]?!","open","base","angry","mid")
                    m "Uhm-{w} My belly?"
                    call ton_main("Sounded like somebody doesn't know how to throat a dick properly...","open","base","base","R")
                    her "(Excuse me?!)"
                    m "Don't be mean, she's doing her best..."
                    call ton_main("So there is a girl behind you!","horny","base","raised","down")
                    call ton_main("Who is it? Tell me!","base","base","base","mid")
                    m "(...)"
                    m "It's Miss Granger."

            call ton_main("Miss Granger?!","open","wide","wide","wide")

            if lock_public_favors:
                call ton_main("That cute little tease who always hangs out at the library, pretending to study?","open","base","raised","mid")
                her "(Pretending???)"
            else:
                call ton_main("That Gryffindor slut? The one who always hangs around flirting with some Slytherins?","open","base","raised","mid")
                her "(Gryffindor slut !!?)"
                with hpunch
                m "Ouch, I felt that..."

            call ton_main("And you are telling me, you are fucking her mouth? {w}Right now???","open","base","worried","mid")

            call ton_main("Oh I've got to see this...","horny","base","base","down")
            call ton_main("","horny","base","base","down",xpos="mid",ypos="base",trans="move")
            pause.2
            g4 "Wait!"
            call ton_main("Hmm?","horny","base","raised","mid")

            m "You better not come any closer..."
            m "Or I fear she will bite me..."
            g4 "Or worse,..."
            m "She'll stop with the sucking..."
            her "(Damn right I will...)"
            call u_play_ani
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"

            call ton_main("Very well...","base","base","raised","R",xpos="right",ypos="base")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"

            call ton_main("Is that really, {w}Miss Hermione Granger,{w} back there?","horny","base","base","mid")
            call ton_main("That's so hard to believe!","open","base","raised","L")
            call ton_main("Or perhaps, you are just fucking with me, [ton_genie_name]...","horny","base","angry","mid")
            m "No,... {w}it's her..."
            call ton_main("That's too good to be true!","base","base","base","ahegao")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"

            call ton_main("Miss Granger, If that's really you back there, why don't you say hi to your favourite teacher?","horny","base","raised","down")
            m "(...)"
            call ton_main("I will reward you with 50 house points if you show yourself!","base","base","raised","down")
            with hpunch
            g4 "What?!"
            call u_pause_ani
            her "(Oh wow, that's a lot of points!)"
            call u_play_ani
            g4 "You can't give her that many points, [tonks_name]! She's already getting [current_payout] from me!"
            m "Do you even realise how many days I'll have to spend with Snape, of all people, to get even with Slytherin again, after this?"
            call ton_main("So what? The girl has clearly earned it!","open","base","angry","mid")
            call ton_main("Sucking her headmasters cock...","horny","base","angry","down")
            call ton_main("50 points could be yours, Miss granger!","open","base","raised","down")
            call ton_main("You only have to stick your gorgeous head out and say hi to me, and of course...","open","base","base","R")
            call ton_main("I promise I won't tell anybody.","base","base","base","down")
            call ton_main("It will be our little secret.","horny","base","angry","down")
            her "(...)"
            m "Do what you must, girl..."
            her "(...............)"
            call u_pause_ani

            call ton_main("Oh my!","horny","base","base","down")

            $ hermione_flip = -1 #head will be on the left.
            call her_main("He- Hello, Miss Tonks.","clench","worriedCl",ypos="head")

            call ton_main("Miss Granger, what a plreasant surprise.","base","base","raised","mid")
            call ton_main("Are you having a good time back there?","open","base","base","down")
            call ton_main("You nasty little cock sucker.","horny","base","raised","mid")
            her "(........................)"
            call her_main("I suppose so...................","disgust","down")
            call ton_main("What a sight to see...","base","base","base","mid")
            call u_play_ani

            call ton_main("I'd love to join you back there, Miss Granger...","base","base","base","down")
            call ton_main("Suck your Headmaster's dick with you!","horny","base","angry","mid")
            her "{size=-4}(She'd do what?... *Slurp...* *Slurp...* *Gulp...*){/size}"
            g9 "You can both have it!"
            call ton_main("I'm sorry, [ton_genie_name]... I'm already pre-occupied with something...","open","base","worried","R")
            call ton_main("Teaching our second-years how to cast a simple deflection spell...","open","base","raised","down")
            call ton_main("We are already two sessions behind my planned class schedule.","open","base","worried","mid")
            call ton_main("I came to you to get consultation about some material I had prepared for them.","open","base","worried","down")
            call ton_main("But since you have to take care of Miss Granger right now,...","base","base","raised","down")
            call ton_main("I guess that can wait.","open","base","worried","R")
            call ton_main("Who said teaching would be easy, am I right?","base","base","worried","ahegao")
            m "It's quite easy, actually."
            call ton_main("As a headmaster maybe... All you do is molest any girl that finds her way in here, I reckon...","horny","base","raised","down")
            m "It can get quite hard, taking care of all those girls."
            call ton_main("I can certainly see that...","horny","base","angry","mid")
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"

            call ton_main("Anyway...","open","base","raised","R")
            call ton_main("Hermione, for your exceptional and benevolent effort of sucking your headmaster's cock, {w}I hereby reward the house Gryffindor...","open","base","base","down")
            call u_pause_ani

            call ton_main("69 points!","horny","base","base","mid")
            $ gryffindor += 69

            her "(69! That's even more than she agreed on!)"
            m "Didn't you say 50 earlier?"
            call ton_main("Yes, but 69 is so much better!","horny","base","raised","mid")
            call ton_main("Don't you think so too, Miss Granger?","base","base","angry","down")
            call her_main("Uhm... Yes. Thank you, Miss Tonks.","disgust","worriedCl")
            m "Less talking, more sucking, [hermione_name]!"
            call her_main("Sorry, [genie_name]...","soft","ahegao")
            call u_play_ani

            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            call ton_main("I'm going to have to go, [ton_genie_name].","open","base","worried","R")
            call ton_main("Wish I could watch you two a little longer...","base","base","worried","mid")
            call ton_main("But I have to head back to my office.","open","base","worried","L")
            m "What a shame."
            call ton_main("Make sure she swallows for me.","horny","base","base","mid")
            g9 "Every last drop!"

            if daytime:
                call ton_main("See you in class, you little cutie!","horny","base","angry","down")
            else:
                call ton_main("Good night... slut!","horny","base","angry","down")
            call her_main("..........","silly","worriedCl")

            #Tonks leaves.
            hide screen tonks_main
            hide screen bld1
            with d3

            stop music fadeout 1.0

            #call ton_walk("mid","leave",3)
            pause.5

            $ hermione_flip = 1 #Default

            call blkfade

            call play_music("playful_tension") # SEX THEME.
            ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."

            return

        "\"I am busy right now, [tonks_name].\"":
            call her_main("(Thank you, [genie_name].)","soft","base",ypos="head")
            ton "Busy?"
            ton "Could it be..."
            ton "Is Snape with you?"
            if daytime:
                ton "Are you two having one of your silly little duels again?"
            else:
                ton "Don't stay up drinking again..."
                ton "We wouldn't want him making a fool of himself. Not in front of the students."
                ton "He made such a mess last time..."
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            m "He isn't here, actually. But I will let him know..."
            ton "So, are you with a student then, hmm?"
            her "{size=-4}(.......... *Slurp...* *Slurp...* *Gulp...*){/size}"
            ton "Who is she? Is it the blonde? Or..."
            ton "You aren't shagging my little cousin, are you?"
            her "{size=-4}(Her cusin? *Slurp...* *Slurp...* *Gulp...*){/size}"
            her "{size=-4}(Is she talking about Susan? *Slurp...* *Slurp...* *Gulp...*){/size}"
            m "That's non of your concern, Tonks!"
            m "You may leave now..."
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            ton "I can help you jack off, if that's what you're-"
            g4 "I said, leave!"
            ton "Okay, [ton_genie_name]."
            ton "*Giggle...*"
            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
            m "I think she's gone..."

            return


label hg_hidden_blowjob_cumming: #Call label. Returns.
    call blkfade
    her "*Slurp!* *Slurp!* *Gulp!*"
    ">Hermione keeps sucking on your cock with a rather fierce determination."
    ">Her technique is lacking but she makes up for it with the effort she puts it."
    hide screen bld1
    call hide_blkfade
    call ctc

    call bld
    m "Yes... I love your eager, little mouth girl..."
    her "*Gobble!* *Gobble!* *Gobble!*"
    call u_pause_ani
    call her_main("[genie_name]?","soft","ahegao",ypos="head")
    m "Hm?"
    call her_main("Are you going to cum on my face today?","soft","ahegao")
    call her_main("Or do you plan to cum in my mouth?")

    menu:
        "\"I Plan to splatter your face with cum!\"":
            call her_main("I see...","soft","ahegao",ypos="head")
            m "Why do you ask?"
            call her_main("Oh... I just read in a book that semen contains a lot of antioxidants...","grin","dead")
            call her_main("It's good for the skin...")
            m "Great. One facial coming up."
            m "Back to work now."

        "\"I Plan to fill your mouth with cum!\"":
            call her_main("I see...","grin","dead",ypos="head")
            m "Why do you ask?"
            call her_main("Well, I am trying to watch my calorie-intake...","soft","ahegao")
            call her_main("I just wonder how much calories your load contains, [genie_name].")
            call her_main("Maybe I should skip my next meal...")
            m "[hermione_name]."
            call her_main("Yes?","soft","ahegao")
            m "Dick back in the mouth."

        "\"I don't plan so far ahead.\"":
            call her_main("I see...","soft","ahegao",ypos="head")
            m "Don't you like surprises?"
            call her_main("Not really...","soft","ahegao")
            call her_main("I rather enjoy planning ahead actually...")
            m "Well some things in life are just unpredictable."
            m "There is only one way to find out for sure."

        "\"What would you like?\"":
            call her_main("If it is all the same to you, [genie_name]...","soft","ahegao",ypos="head")
            if generating_points == 1:
                call her_main("I would like you to cum on my face, [genie_name].","grin","dead")
                call her_main("I read that it's good for the skin.")
            else:
                call her_main("I would like you to cum in my mouth.","grin","dead")
                call her_main("You usually cum so much so I think I will be able to just skip my next meal...")
                call her_main("And do some homework instead.")
            m "Well, we'll see about that."
            m "Back to sucking now."

    call u_play_ani
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "Hm..."
    m "You are getting better at this [hermione_name]."
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "Ok, say something nasty now..."
    her "*Slurp--?"
    call u_pause_ani

    if her_whoring < 21:
        call her_main("uhm...","angry","down_raised",ypos="head")
        call her_main("I eat cockroaches?","angry","base")
        m "What the fuck?"
        call her_main("T-they are pretty nasty, [genie_name]...","angry","base")
        m "No, [hermione_name], I mean something dirty!"
        m "And don't you dare to say \"mud\"!"
        m "I mean dirty in a sexual way!"
        call her_main("Oh... Ehm...","angry","down_raised")
        m "Ah, never mind, the moment is gone..."
        call her_main("Ehm... I'm sorry, [genie_name].","angry","base")
        m "Yeah, whatever. Make it up to me by sucking my cock harder."
        call her_main("Of course, [genie_name].","upset","closed")

    else:
        call her_main("I'm a slut, [genie_name].","base","suspicious",ypos="head")
        call her_main("A slut for your cum.","base","glance")
        m "That's it, [hermione_name]."
        call her_main("It's all I can think about [genie_name].","base","down")
        call her_main("Sucking your dirty old cock...")
        m "Well you better get back to it then [hermione_name]"
        call her_main("Thank you, [genie_name].","grin","dead")
        m "You're welcome, cumslut."
        call her_main("...","base","ahegao_raised")

    call u_play_ani
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Yes, like this... Good..."
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "You know what? I think we are almost there."
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "Yes, definitely."
    her "*Slurp!* *Gobble!* *Gobble!*"
    m "Alright, [hermione_name], this is the final stretch."
    g4 "Show me what you've got."
    her "!!! *Gobble-goble-slurp-goble!* !!!"
    g4 "Yes, like that!"
    her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    g4 "Ghr!!!"

    menu:
        g4 "!!!"
        "-Cum in her mouth-":
            g4 "Here it comes, [hermione_name]! get ready to swallow fast!"
            her "!!!"
            call ctc
            call blkfade

            call set_u_ani("cum_in_mouth_ani")
            call u_play_ani
            call cum_block
            g4 "{size=+7}ARGH!{/size}"
            g4 "Eat my cum, slut!"
            her "*Gulp!-Gulp!-Gulp!*"
            with hpunch
            g4 "Yes! Down your fucking throat!"
            her "*Gulp-gulp-gulp-gulp-gulp!*"
            hide screen bld1
            call hide_blkfade
            stop music fadeout 1.0
            call ctc

            call bld
            m "Well, I think that's it."
            m "You can let go now..."
            call u_pause_ani

            call her_main("...........................","full_cum","dead",xpos="mid",ypos="base")
            call her_main("................")
            call her_main("........")
            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            call her_main("*GULP!*","cum","worriedCl")
            call her_main("Gua-ha...","open_wide_tongue","base")
            m "You alright?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("Yes, [genie_name]...","grin","dead")
            m "Going to skip your next meal?"
            call her_main("I think so...","grin","dead")
            call her_main("You always cum so much, [genie_name]...")
            m "Heh... And who's fault is that??"
            call her_main(".............","grin","dead") #Smile.
            call her_main("Can I get paid now?")

            if her_whoring >= 21:
                if daytime:
                    m "What, even after I just gave you lunch?"
                else:
                    m "What, even after I fed you dinner"
                call her_main(".............","annoyed","suspicious") #Smile.
                call her_main("Fine, I suppose this was worth a meal")

            call ctc
            call blkfade

            return

        "-Cum on her face-":
            call blkfade

            call u_pause_ani
            g4 "Ready for your facial, [hermione_name]?"
            call her_main("Yes [genie_name]!","grin","dead",ypos="head")
            g4 "Here it comes then!"
            hide screen bld1
            call set_u_ani("cum_on_face_ani")
            call u_play_ani
            call hide_blkfade
            call cum_block

            call bld
            g4 "{size=+7}Whore!{/size}"
            call her_main("!!?","shock","wide",ypos="head")
            hide screen bld1
            with d1
            call ctc

            call bld
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_07.png"
            call her_main("[genie_name]...","shock","wide")
            g4 "All over your fucking face!"
            call her_main("Aaah!","grin","dead")
            call set_u_ani("cum_on_face_blink_ani")

            m "Well, I'm done."
            call her_main("....................................","grin","dead")
            m "I said it's over, [hermione_name]."
            call her_main("Yes, I heard you [genie_name]...","grin","dead")
            m "So... Aren't you going to clean up?"
            call her_main("In a moment...","grin","dead")
            call her_main("I'm giving my skin time to soak in the anti-oxidants...")
            m "Hm... I find this quite hot..."
            m "Take your time, [hermione_name]..."
            call blkfade

            stop music fadeout 1.0
            ">A while later."
            $ uni_sperm = True
            $ aftersperm = True

            call u_end_ani
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blktone
            call hide_blkfade
            pause.5

            call her_main("I take it you enjoyed yourself, [genie_name]?","angry","wink",xpos="mid",ypos="base")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Yes I did, [hermione_name]."
            call her_main("Good, so Can I get paid now?","grin","dead")

            if her_whoring >= 21:
                m "What, even after I just gave you a salon treatment?"
                m "Women pay a lot of money for a good facial."
                call her_main(".............","annoyed","suspicious") #Smile.
                call her_main("Fine, but my skin better look better tomorrow.")

            call blkfade

            return



### Fourth Blowjob ###

label hg_blowjob_4:
    call play_music("playful_tension") #HERMIONE
    hide screen genie
    call her_chibi("hide")
    show screen chair_left
    call u_play_ani
    hide screen bld1
    hide screen blkfade
    with fade
    call ctc

    call her_main("*Slurp!* *Slurp!* *Gulp!*",ypos="head")
    m "Yes, good girl..."
    her "*Slurp!* *Gobble!* *Slurp!*"
    m "lick the shaft..."
    her "*lick!* *Slurp!* *lick!*"
    call nar(">Hermione keeps sucking on your cock like her life depends on it.","start")
    call nar(">Her technique is almost perfect and she is incredibly enthusiastic.","end")
    m "Yes... I love your eager, little mouth slut..."
    her "*Gobble!* *Gobble!* *Gobble!*"
    call u_pause_ani
    call her_main("[genie_name]?","base","down")
    m "Hm?"
    call her_main("How would you like me to please you today?","soft","ahegao")

    menu:
        "\"Pretend I am your father.\"":
            call her_main("My father?","angry","wink",ypos="head")
            m "Anything wrong with that?"
            call her_main("I suppose not...","base","down")
            call her_main("I mean it's just pretending...","grin","dead")
            m "Great. Dick back in mouth then."
            call u_play_ani
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "That's it, princess. Suck daddy's dick."
            her "*Slurp!* *Gulp!* *Slurp!*"
            m "Tell me how much you want it."
            her "*Slurp!* *Gobble!* *Slurp!*"
            call u_pause_ani
            call her_main("So much daddy...","soft","ahegao")
            call u_play_ani
            her "*Slurp!* *Gobble!* *Slurp!*"
            call u_pause_ani
            call her_main("It's all I think about when we're together...","base","ahegao_raised")
            call u_play_ani
            her "*Gobble!* *Gulp!* *Gobble!*"
            call u_pause_ani
            call her_main("When we're sitting together on the couch watching T.V...","base","ahegao_raised")
            call her_main("I just imagine that I am sucking your cock instead...","base","ahegao_raised")
            call u_play_ani
            her "*lick!* *Slurp!* *Slurp!*"
            call u_pause_ani
            call her_main("I even wish that mum left you sometimes...","annoyed","down")
            call u_play_ani
            her "*Gobble!* *Slurp!* *lick!*"
            m "Why's that?"
            call u_pause_ani
            call her_main("So that I'm the only one to get your dick...","soft","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("You'll come home every day...","soft","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("Throw me onto my bed...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("and use me...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("however you want...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("for as long as you want...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("you won't even ask...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("you'll just take me...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("even though I say no...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            m "That's it princess, Almost there..."
            call u_pause_ani
            call her_main("Where do you want to cum today daddy?","soft","ahegao")
            call her_main("Are you going to cover my face?","soft","ahegao")
            call her_main("Or make me swallow your big load?","grin","dead")
            call her_main("{size=-4}Even if I don't want to...{/size}","grin","dead")
            m "Let's find out shall we?"
            call her_main("Yes daddy...","soft","ahegao")
            call u_play_ani
            her "*Slurp!* *Gulp!* *Slurp!*"
            m "Yes, like that... Good girl..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Do it for daddy."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Come on princess."
            her "*Slurp!* *Gobble!* *Gobble!*"
            m "Alright, [hermione_name], almost there."
            g4 "Make daddy proud!"
            her "!!! *Gobble-goble-slurp-goble!* !!!"
            g4 "Yes, like that!"
            her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
            g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
            g4 "Ghr!!!"

            menu:
                g4 "!!!"
                "-Cum in her mouth-":
                    call hide_blkfade
                    g4 "Here it comes, [hermione_name]! Here comes daddy!"
                    her "!!!"
                    call ctc
                    call blkfade

                    call set_u_ani("cum_in_mouth_ani")
                    call u_play_ani
                    call cum_block
                    g4 "{size=+7}ARGH!{/size}"
                    g4 "Eat my cum, slut!"
                    #Cumming.
                    her "*Gulp!-Gulp!-Gulp!*"
                    with hpunch
                    g4 "Yes! Down your fucking slut throat!"
                    her "*Gulp-gulp-gulp-gulp-gulp!*"
                    hide screen bld1
                    call hide_blkfade

                    stop music fadeout 1.0
                    call ctc
                    show screen bld1
                    with d1

                    m "Well, I think that's it."
                    m "You can let go now..."
                    call u_pause_ani
                    call her_main("...........................","full_cum","dead",ypos="head")
                    call her_main("................")
                    call her_main("........")
                    $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                    call her_main("*GULP!*","cum","worriedCl")
                    call her_main("Gua-ha...","open_wide_tongue","base")
                    m "How was that?"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("So tasty...","grin","dead")
                    m "Really?"
                    call her_main("Yes daddy...","grin","dead")
                    call her_main("It's always tasty with you...")
                    m "Heh... is that so?"
                    call her_main(".............","grin","dead")
                    call nar(">She leans forward and gives your wilting cock a small kiss.")
                    call her_main("Thanks daddy.","base","baseL")
                    call ctc
                    call blkfade

                    return

                "-Cum on her face-":
                    call hide_blkfade
                    call u_pause_ani
                    g4 "Ready for your cum-load, princess slut?"
                    call her_main("Yes daddy!","grin","dead",ypos="head")
                    g4 "Here it comes then!"
                    call cum_block
                    g4 "{size=+7}Slut!{/size}"
                    call her_main("!!?","shock","dead")
                    call set_u_ani("cum_on_face_ani")
                    call u_play_ani
                    hide screen bld1
                    with d3
                    call ctc

                    call bld
                    $ uni_sperm = True
                    $ u_sperm = "characters/hermione/face/auto_07.png"
                    call her_main("Daddy...","shock","wide")
                    g4 "That's it, princess!"
                    call her_main("Aaah!","grin","dead")
                    call set_u_ani("cum_on_face_blink_ani")
                    m "Well, I'm done."
                    call her_main("....................................","grin","dead")
                    m "I said it's over, [hermione_name]."
                    call her_main("Yes, I heard you, daddy...","grin","dead")
                    m "So... Aren't you going to clean up?"
                    call her_main("In a minute...","grin","dead")
                    call her_main("I'm just savouring the moment...")
                    m "Hm..."
                    m "Take your time, [hermione_name]..."
                    call blkfade

                    stop music fadeout 1.0
                    ">A while later."
                    $ uni_sperm = False
                    $ aftersperm = True

                    call u_end_ani
                    call her_chibi("stand","desk","base")
                    call gen_chibi("sit_behind_desk")
                    hide screen bld1
                    hide screen blktone
                    call hide_blkfade
                    pause.5

                    call her_main("I take it you enjoyed yourself sir?","angry","wink")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    m "Yes I did princess."
                    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

                    return

        "\"Worship my cock.\"":
            call her_main("Worship it?","angry","wink",ypos="head")
            m "Worship. My. Cock."
            call her_main("Well...","base","down")
            call her_main("ok...","soft","ahegao")
            m "Great. You can start by putting it back in your mouth."
            call u_play_ani
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Thats it.."
            her "*Slurp!* *Gulp!* *Slurp!*"
            m "Tell me how much you love my cock."
            her "*Slurp!* *Gobble!* *Slurp!*"
            call u_pause_ani
            call her_main("So much [genie_name]...","soft","ahegao")
            call u_play_ani
            her "*Slurp!* *Gobble!* *Slurp!*"
            call u_pause_ani
            call her_main("It's all I think about when I'm in class...","base","ahegao_raised")
            call u_play_ani
            her "*Gobble!* *Gulp!* *Gobble!*"

            if lock_public_favors == True:
                call u_pause_ani
                call her_main("Sucking your perfect dick.","base","ahegao_raised")
                call her_main("No one elses...","base","ahegao_raised")
                call u_play_ani
                her "*lick!* *Slurp!* *Slurp!*"
                call u_pause_ani
                call her_main("Just your {p}perfect, {p}beautiful {p}{size=-4}cock{/size}","grin","dead")
                call u_play_ani
                her "*Gobble!* *Slurp!* *lick!*"

            else:
                call u_pause_ani
                call her_main("Even when you make me suck another boys dick...","base","ahegao_raised")
                call her_main("I still imagine that it's yours...","base","ahegao_raised")
                call u_play_ani
                her "*lick!* *Slurp!* *Slurp!*"
                call u_pause_ani
                call her_main("Imagine that it's your cum sliding down my throat...","soft","ahegao")
                call u_play_ani
                her "*Gobble!* *Slurp!* *lick!*"
                call u_pause_ani
                call her_main("Imagine that it's your hot load shot across my face...","grin","dead")
                call u_play_ani
                her "*Gobble!* *Slurp!* *lick!*"

            m "Is that so?"
            call u_pause_ani
            call her_main("Yes [genie_name]...","soft","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("Sometimes...","soft","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("After you make me suck your perfect cock...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("I won't brush my teeth...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("just so I can go to sleep...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("with that perfect taste in my mouth...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("and when I do brush my teeth...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("Your beautiful cock is all I can think about...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            call u_pause_ani
            call her_main("I even started to moan while brushing them...","grin","dead")
            call u_play_ani
            her "*Gobble!* *lick!* *Gobble!*"
            m "That's it cock slut, Almost there..."
            call u_pause_ani
            call her_main("Where do you want to cum today [genie_name]?","soft","ahegao")
            call her_main("I know it's greedy of me to ask...","angry","down_raised")
            call her_main("But can you cum in my mouth?","angry","wink")
            call her_main("{size=-4}Please...{/size} I promise I won't waste a drop.","soft","ahegao")
            m "I think that can be arranged "
            call her_main("Thank you [genie_name]!","smile","happyCl",cheeks="blush",emote="06")
            call u_play_ani
            call nar(">Hermione devours your cock with renewed vigour.")
            her "*Slurp!* *Gulp!* *Slurp!*"
            m "Yes, like that... that's a good little slut..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Deeper now."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Come on cock-slut."
            her "*Slurp!* *Gobble!* *Gobble!*"
            m "Alright, [hermione_name], almost there."
            g4 "Deeper now!"
            her "!!! *Gobble-goble-slurp-goble!* !!!"
            g4 "Yes, like that!"
            her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
            g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
            g4 "Ghr!!!"
            g4 "Here it comes, [hermione_name]! Here's you reward!"
            her "!!!"

            call ctc
            call blkfade

            call set_u_ani("cum_in_mouth_ani")
            call u_play_ani
            hide screen bld1
            call hide_blkfade

            call cum_block
            g4 "{size=+7}ARGH!{/size}"
            g4 "Eat my cum, slut!"
            her "*Gulp!-Gulp!-Gulp!*"
            with hpunch
            g4 "Yes! Down your fucking cumslut mouth!"
            her "*Gulp-gulp-gulp-gulp-gulp!*"

            stop music fadeout 1.0
            call ctc

            call bld
            m "Well, I think that's it."
            m "You can let go now..."
            call u_pause_ani
            call her_main("...........................","full_cum","dead",tears="mascara",xpos="mid",ypos="base",trans="fade")
            call her_main("................","full_cum","dead",tears="mascara")
            call her_main("........","full_cum","dead",tears="mascara")
            m "How was that?"
            call her_main("...")
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "Are you going to swallow?"
            call her_main("*Shakes her head side to side*","full_cum","dead",tears="mascara")

            if daytime:
                m "So you're going to go to class with a mouth full of my cum?"
            else:
                m "So you're going to go to sleep with a mouth full of my cum?"

            call her_main("*She nods her head up and down enthusiastically*","full_cum","ahegao",cheeks="blush",tears="mascara") #Smile.
            m "Good girl."
            call ctc

            call blkfade
            $ mouth_full_of_cum = True

            return



### END BLOWJOB ###

label end_hg_blowjob:

    $ current_payout = 55

    hide screen hermione_main
    call blkfade

    call u_end_ani

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    pause.5

    call bld
    if her_whoring <= 24:
        m "Yes, [hermione_name]. [current_payout] points to \"Gryffindor\"."
        $ gryffindor += current_payout

    if mouth_full_of_cum:
        call her_main("...","full_cum","ahegao",cheeks="blush",tears="mascara",xpos="right",ypos="base")
    else:
        call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if her_whoring < 18:
        $ her_whoring +=1

    $ hg_pf_SuckIt_OBJ.points += 1

    jump end_hg_pf #Hides screens. Hermione walks out. Resets Hermione.




#Hidden Blowjob
label update_hidden_bj_list:
    $ hg_hidden_bj_list = ["snape"]
    if luna_unlocked and luna_reverted:
        $ hg_hidden_bj_list.append("luna")
    if tonks_unlocked:
        $ hg_hidden_bj_list.append("tonks")

    return
