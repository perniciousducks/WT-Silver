
#hermione asks genie about who will be in-charge of the ball
label ball_quest_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]?","soft","base", xpos="right", ypos="base")
    m "Miss Granger, how can I help you?"
    call her_main("Sir, have you made your decision yet on who will be in charge of the \"ABOC\" this year?","open","base")
    m "\"ABOC\"?"
    call her_main("The \"Autumn Ball Organization Committee\", sir...","open","closed")
    m "Ehm... Sure..."
    call her_main("Please excuse me if I am being too direct with this, sir...","normal","frown")
    call her_main("But I think you should put me in charge.","open","angryCl")
    her "I did it last year and it was the best organized \"autumn ball\" Hogwarts has had in years."
    call her_main("You said so yourself, sir. Do you remember?","normal","base")
    m "Right, of course..."
    call her_main("So, is this a yes?","base","base")
    her "Does this mean I will be in charge again this year?"

    menu:
        m "..."
        "\"You shall be in charge, miss Granger.\"":
            jump one_thing

        "\"No. Professor Snape shall be in charge!\"":
            call her_main("Professor Snape, sir?","normal","frown")
            her "But, traditionally organizing and hosting the ball is the responsibility of the students..."
            her "Teachers are only present as the guests of honour..."
            m "Well of course... I was just kidding."
            m "You shall be in charge, [hermione_name]..."
            label one_thing:
                call her_main("Thank you, [genie_name].","base","base")
            m "There is one condition, though..."
            call her_main("A conditions, [genie_name]?","normal","frown")

            $ d_flag_04 = False
            label no_sleeping_with_professor:
                pass
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            menu:
                m "..."
                "\"Show me your tits first.\"":
                    $ her_mood += 9
                    $ d_flag_01 = True
                    pass
                "\"Show me your pussy first.\"":
                    $ her_mood += 9
                    $ d_flag_02 = True
                    pass
                "\"Strip naked for me first.\"":
                    $ her_mood += 17
                    $ d_flag_03 = True
                    pass
                "\"You will have to sleep with me.\"" if not d_flag_04:
                    $ her_mood += 17
                    $ d_flag_04 = True
                    call her_main("I will have to... sleep...?","angry","wide")
                    call her_main("...................","angry","angry", cheeks="blush")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    her "I am not stupid, sir... Quite the opposite in fact."
                    her "And I understand that the nature of the favours I have been selling you lately..."
                    her "...Might have led you to believe that I would be willing to..."
                    her "...To let you have your way with me eventually, sir..."
                    m "Wha-a-a...? I would never--"
                    call her_main("Please, let me finish, sir.","scream","angry",emote="01")
                    m "Right..."
                    call her_main("I know that you are a rather wise man yourself, sir.","angry","angry")
                    call her_main("So, please... understand this...","disgust","glance")
                    her "I may be willing to sacrifice my pride and even my dignity for the sake of my house..."
                    her "But sleeping with my headmaster?"
                    call her_main("That is where I draw the line, sir.","angry","angry", cheeks="blush")
                    m "Got it. Let's just forget I said anything."
                    call her_main("{size=-5}(I wish I could...){/size}","angry","suspicious", cheeks="blush")
                    jump no_sleeping_with_professor

                "\"Never mind. the Position is yours.\"":
                    hide screen hermione_main
                    with d3
                    call blkfade
                    pass


            if d_flag_01 or d_flag_02 or d_flag_03:
                call her_main("What?!","open","base")
                m "What?"
                call her_main("[genie_name]!","angry","angry")
                m "What?"
                call her_main("You are abusing your power, sir. Again!","disgust","glance")
                m "Seriously? After all those favours you sold me?"
                call her_main("Those were for the sake of my house, sir.","annoyed","annoyed")
                m "Well this one is for the sake of the \"Autumn prom\"."
                call her_main("It's the \"Autumn Ball\", sir...","upset","closed")
                m "Oh, come on..."
                m "Entrusting the thing to somebody else would be a crime, you know that."
                call her_main("..........","annoyed","angryL")
                m "Don't you care about your classmates at all?"
                call her_main("What?","open","base")
                m "Put your selfishness aside for once, would you?"
                call her_main("My... selfishness?","annoyed","worriedL")
                m "Your classmates deserve the best organized ball possible!"
                m "And only {size=+5}YOU{/size} can give them that!"
                call her_main("...that is true actually.","angry","down_raised")
                m "People depend on you, girl!"

                if d_flag_01:
                    m "So I suggest that you stop being selfish and show me your tits!"
                elif d_flag_02:
                    m "So I suggest that you stop being selfish and show me your pussy!"
                elif d_flag_03:
                    m "So I suggest that you stop being selfish and get naked for me!"

                call her_main("You are completely right, [genie_name]!","open","down")
                call her_main("I must do this. Everyone depends on me.","upset","closed")
                call her_main("Just give me a second please...","base","glance")
                hide screen hermione_main
                with d5
                m "............"

                if d_flag_01: # SHOW ME TITS
                    call play_music("playful_tension") # SEX THEME.
                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    pause.3
                    call her_chibi("lift_top","mid","base")
                    with fade
                    pause.8

                    $ hermione_wear_bra = False
                    call set_her_action("lift_top")
                    pause.5

                    show screen blktone
                    call her_main("","annoyed","base")
                    call ctc

                    m "Very good miss Granger..."
                    m "Your ample tits are always a welcome sight..."
                    call her_main("....................","disgust","down_raised")
                    call ctc

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade
                    call reset_hermione

                elif d_flag_02: # SHOW ME PUSSY
                    call play_music("playful_tension") # SEX THEME.

                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    call ctc

                    $ hermione_wear_panties = False
                    call her_chibi("lift_skirt","mid","base")
                    with fade
                    call ctc

                    call set_her_action("lift_skirt")
                    pause.5

                    show screen blktone
                    call her_main("","annoyed","base")
                    call ctc

                    call her_main("","base","worriedCl")
                    call ctc

                    her ".............................."
                    with hpunch
                    g4 "What are you doing, girl?!"
                    g4 "I am your headmaster! Do you have no shame?!"
                    call her_main("What?! But--","angry","angry", cheeks="blush")
                    g9 "He-he... Relax, girl. I'm just kidding."
                    call her_main("[genie_name], that was just mean.","scream","angryCl")
                    g9 "He-he..."
                    call her_main(".....................................","annoyed","angry")
                    m "I do like your shaved little pussy though..."
                    call her_main(".....thank you, sir.","annoyed","angry")
                    call ctc

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade

                    call reset_hermione

                elif d_flag_03: # STRIP NAKED
                    call play_music("playful_tension") # SEX THEME.

                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5

                    #Walks to the door
                    call her_walk(xpos="door", ypos="base", speed=2)

                    #Locks the door
                    pause.5
                    call chibi_effect("thought","hermione")
                    pause.5

                    call chibi_effect("hide")
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4

                    call her_chibi("stand","door","base")
                    pause.5

                    #Returns from the door
                    m "??!"

                    call her_walk(xpos="mid", ypos="base", speed=3)
                    pause.2

                    call her_main("Just in case...","annoyed","angryL")
                    call ctc

                    m ".........................."

                    show screen blktone
                    call nar(">Hermione is taking her clothes off...")
                    pause.2

                    $ hermione_wear_bra = False
                    call set_her_action("lift_top")
                    pause.5

                    $ hermione_wear_top = False
                    call set_her_action("None")
                    pause.5

                    call nar(">One piece after another...")

                    $ hermione_wear_panties = True
                    call set_her_action("lift_skirt")
                    pause.5

                    $ hermione_wear_bottom = False
                    call set_her_action("None")
                    pause.5

                    call nar(">Vest, shirt, her skirt, and finally...")

                    $ hermione_wear_panties = False
                    call set_her_action("covering")
                    pause.5

                    call nar(">The panties.")
                    call ctc

                    g9 "Ni-i-i-ce!"
                    call her_main("","soft","squintL")
                    call ctc
                    her "*Sob!*"
                    m "Huh?"

                    call her_main("Oh, please, don't mind me, sir.","open","baseL",)
                    call her_main("Just enjoy the... {w}the... {w}the view...","soft","squintL")
                    m "Are you... crying?"
                    call her_main("*Sob!* No, not really, sir... *sob!*...","angry","worriedCl")
                    her "It is just that I am standing here before my headmaster completely naked... *SOB!*"
                    call her_main("These are the tears of shame, sir.","shock","angryL", tears="messy")
                    her "I can't help it! *Sob!*"
                    m "Are you sure that you are ok with this?"
                    call her_main("Yes, yes, sir, please.... *Sob!*","soft","angry", tears="messy")
                    call her_main("Please keep on looking at my naked body... *Sob!*","shock","wide", tears="messy")

                    call her_main("","angry","angry", cheeks="blush", tears="messy")
                    call set_her_action("lift_breasts")
                    pause.2

                    g4 "(What the...?)"
                    call her_main("Sir, I am begging you!","angry","angry", cheeks="blush", tears="messy")
                    m "Kind of sounds like an order--"
                    call her_main("I need it!","angry","dead_mad", cheeks="blush", tears="messy")
                    her "...I need to shamelessly present my naked body before you like this!"
                    m ".............?"
                    call her_main("I need to feel this embarrassment and humiliation! *SOB!*","upset","dead_mad", cheeks="blush", tears="messy")
                    call her_main("The fate of the \"Autumn ball\" depends on this...","grin","ahegao_mad", cheeks="blush", tears="messy")
                    her "So, sir, please..."
                    call her_main("Keep looking at my naked breasts, and my pussy...","grin","angry", cheeks="blush", tears="messy")
                    call ctc

                    call her_main("Yes! Make my skin burn with shame, sir... *Sob!*","open","ahegao_raised", cheeks="blush", tears="messy")
                    m "Ehm... right... Ok..."
                    m "Listen, I think this will do..."
                    call set_her_action("pinch")
                    call her_main("Are you sure, sir?","angry","angry", cheeks="blush", tears="messy")
                    her "Are you sure that you humiliated me enough, sir?"
                    m "...................."
                    m "(Is she getting off on this? Is she being sarcastic? I don't get it...)"
                    her ".........................."
                    call ctc

                    m "Just put your clothes back on, Miss Granger. You're making me feel uncomfortable."
                    call her_main("As you wish, sir...","annoyed","angryL", tears="messy")

                    call ctc

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade

                    $  u_tears_pic = "characters/hermione/face/tears_03.png"

                    call reset_hermione





    call play_music("chipper_doodle") # HERMIONE'S THEME.

    call her_chibi("stand","mid","base")
    call hide_blkfade
    with d5
    call ctc

    call her_main("So I am officially in charge of this year's \"Autumn Ball Organization Committee\" now?","base","happyCl", xpos="right", ypos="base")
    m "That you are."
    her "Thank you sir! You will not regret this, I promise!"
    m "{size=-4}(Why would I?){/size}"
    m "{size=-4}(I couldn't care less about the whole thing...){/size}"
    call her_main("Well, I'd better go now. I have so many arrangements to make!","grin","baseL")
    m "By all means, Miss Granger. Have a nice day."

    call her_walk(action="leave", speed=2)
    pause.5

    call bld
    m "........................................"
    m "A ball, huh?"
    m "I wonder if I will have to show up for that..."

    $ event_chairman_happened = True
    #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    $ hermione_busy = True
    $ hg_event_pause += 2 # Event happens in 2 days.

    jump main_room


#Snape confronts genie about his ABOC decision

label ball_quest_E2:

    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    call sna_walk(action="enter", xpos="mid", ypos="base", speed=3)
    pause.2

    call sna_main("Are you bloody insane?!","snape_01", xpos="base", ypos="base")
    m "You know, sometimes I think I may be..."

    call sna_main("You appointed the girl as the head of the \"Autumn Ball Organization Committee\"?!!","snape_01")
    m "I'm guessing that's bad?"
    call sna_main("Bad?{w} {size=+5}BAD?!{/size}","snape_10")
    call sna_main("{size=+5}That's a catastrophe!{/size}","snape_15")
    call sna_main("last year's ball was completely horrible!","snape_16")
    m "Was it? I heard differently..."
    call sna_main("Oh really? And who told you that?","snape_10")
    m "not a very reliable source apparently..."
    call sna_main("Dammit... Dammit all to hell...","snape_08")
    call sna_main("I had big plans for the thing...","snape_07")
    m "Really? Like what?"
    call sna_main("Oh, that doesn't matter now...","snape_06")
    #sna "The girl is a complete control freak..."
    sna "Now the girl will use prefects or the ghosts to keep an eye on me throughout entire thing..."
    m "Right, that reminds me..."
    m "Am I supposed to show up as well?"
    call sna_main("Show up?","snape_03")
    sna "You are expected to host the bloody thing!"
    call sna_main("But don't you worry! I'll figure something out!","snape_09")
    call sna_main("Hm... I'll Probably have to host the ball instead...","snape_06")
    m "............"
    call sna_main("Well, the Autumn ball is about to happen and Hermione Granger is in charge...","snape_09")
    sna "There is no changing it now..."
    call sna_main("Sorry for the outburst...","snape_05")
    call sna_main("That girl brings out the worst in me...","snape_16")
    m "Don't sweat it..."
    call sna_main("You know what...?","snape_06")
    sna "I don't feel like working today..."
    call sna_main("Do we still have any of Dumbledore's wine left?","snape_05")
    m "I believe so..."
    call sna_main("Great! Pour me some...","snape_02")
    m "Seriously? You're just gonna bail on your class like that?"
    call sna_main("Yeah, big news - I hate my job.","snape_03")
    sna "And since you are my boss..."
    call sna_main("I don't know why I even bother teaching those so-called students...","snape_06")
    m "To maintain the charade?"
    m "for the Same reason why I never leave this room...?"
    call sna_main("Right...","snape_05")
    sna "But you know what else could endanger out little enterprise?"
    call sna_main("Me losing it during class and strangling a couple of \"Gryffindor\" maggots with my bare hands...","snape_07")
    m "Hm... I see your point..."
    call sna_main("Seriously, man... I need a drink...","snape_06")

    hide screen snape_main
    call blkfade

    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk

    $ fire_in_fireplace = True
    show screen fireplace_fire
    call sna_chibi("hide")
    hide screen bld1
    call hide_blkfade

    call bld
    call nar("Professor Snape spends the day in your chamber, drinking the stress away.")

    if sna_friendship < 100:
        call nar(">Your relationship with him has improved.")
        $ sna_friendship +=1

    $ snape_against_chairman_hap = True
    # Turns TRUE after Snape comes and complains
    # that appointing Hermione in the Autumn Ball committee was a mistake.
    $ ss_event_pause += 5
    $ hg_event_pause += 5

    jump night_start


label ball_quest_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("My parents sent me the wrong dress!","angry","base", tears="soft", xpos="right", ypos="base")
    m "are You kidding me!?"
    call her_main("They sent me the dress I wore to the ball last year...","angry","base", tears="soft")
    m "Those inconsiderate bastards!"
    call her_main("Are you making fun of me sir?","mad","worried", tears="soft")
    m "Can you blame me?"
    call her_main("I will become the laughingstock of Hogwarts! *Sob!*","clench","worried", cheeks="blush", tears="soft")
    call her_main("My reputation is as good as ruined! *Sob!*","angry","dead", cheeks="blush", tears="crying")
    m "Seriously? After all the favours you sold me you care about a thing like this?"
    call her_main("Wearing the same dress to the \"Autumn Ball\" for two years in a row would be more humiliating than any favour I sold you so far, sir.","shock","down_raised", cheeks="blush", tears="crying")
    with hpunch
    g4 "You've gotta be kidding me..."
    call her_main("Oh, you wouldn't understand...","angry","suspicious", cheeks="blush", tears="messy")
    call her_main("You're just like my father!","scream","angry", cheeks="blush", tears="messy")
    m "I beg your pardon?"
    call her_main("I mean... ehm...","open","surprised", cheeks="blush", tears="messy")
    her "Forgive me sir..."
    call her_main("I don't know why I am telling you all of this...","shock","down_raised", cheeks="blush", tears="crying")
    m "................"
    call her_main("......................*sob!*","angry","dead", cheeks="blush", tears="crying")
    call her_main("I think I'd better go now...*sob*","angry","suspicious", cheeks="blush", tears="messy")
    m "Well, don't let me keep you a moment longer, miss Granger...."

    call her_walk(xpos="door", ypos="base", speed=2)
    pause.3

    call her_main("(My life is ruined...)","angry","suspicious", cheeks="blush", tears="messy", ypos="head")
    pause.1

    call her_chibi(action="leave")

    call bld
    m "Hm... I don't remember ever seeing the girl this desperate..."
    m "And that says a lot, all things considered..."
    m "I suppose Whoring herself out for house points is a significantly smaller problem than not having a proper prom dress..."
    m ".............."
    m "Schoolgirls..."

    $ hermione_busy = True
    $ have_no_dress_hap = True
    # Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ hg_event_pause += 1

    jump main_room


label ball_quest_E4:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call bld
    m "Miss Granger?"
    call her_main("Sorry to disturb you sir...","open","worried", xpos="right", ypos="base")
    call her_main("I came to apologize for my...","open","worriedL")
    her "...my hysterical behaviour yesterday."
    m "Sure thing, don't worry about it."
    call her_main("Thank you, sir.","open","base")
    call her_main("Still, I cannot help but feel awful for causing a scene...","open","angryCl")
    m "So the issue has been resolved then?"
    call her_main("Not really...","open","worried")
    call her_main("Not at all actually...","annoyed","angryL")
    m "Hm..?"
    call her_main("But that is not a big deal...","annoyed","down")
    her "I'm just overreacting..."
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("I woN't be able to attend the ball this year... so what?","annoyed","down")
    call her_main("I spent countless hours with organizing the event...","normal","worriedCl")
    call her_main("I worked so hard... and...","open","worried", tears="soft")
    call her_main("And now I will not even be able to... to... *Sob!*","shock","baseL", cheeks="blush", tears="soft")
    call her_main("To... *SOB!*","shock","down_raised", cheeks="blush", tears="crying")
    call her_main("Excuse me sir!","angry","suspicious", cheeks="blush", tears="messy")
    hide screen hermione_main
    hide screen bld1
    with d3
    hide screen no_groping_02
    show screen genie
    with d1

    call her_walk(action="run", xpos="door", ypos="base", speed=1, loiter=False)
    call play_sound("door")
    pause.5

    call bld
    m "......................................."
    m "Hm..."

    $ sorry_for_hesterics = True
    # Turns TRUE after Hermione comes and apologizes for the day (event) before.

    $ have_no_dress_hap = True
    #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.

    $ hermione_busy = True
    $ hg_event_pause += 1

    jump main_room


label ball_quest_E5:
    hide screen hermione_main
    with d5

    stop music fadeout 1.0
    m "Here... This is for you..."

    call give_reward(">You give the ball gown to Hermione...","interface/icons/box_red_1.png")

    call her_main("Hm...? What is this?","base","base")
    call her_main("{size=+7}A DRESS?!{/size}","angry","wide")
    with hpunch
    m "I thought that you--"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name]!","angry","base", tears="soft")
    g4 "What? What happened? Don't tell me it's the wrong color or something!"
    call her_main("It's perfect, sir...*sob!*","angry","base", tears="soft")
    her "It's perfect... *sob!* ...I love it."
    m "You sure don't look like it..."
    her "I am sorry, sir... *Sob!*"
    call her_main("I... I am just...","clench","worried", cheeks="blush", tears="soft")
    call her_main("I am so happy...","shock","down_raised", cheeks="blush", tears="crying")
    her "Thank you, sir. Thank you so much."
    call her_main("I cannot believe that you would do something like that for me...","angry","suspicious", cheeks="blush", tears="messy")
    m "Well, I did. Now stop crying."
    call her_main("I can't, sir. I am so happy and so grateful...","scream","worriedCl", cheeks="blush", tears="messy")
    call her_main("Do you want me to suck your cock, sir?","open","surprised", cheeks="blush", tears="messy")
    m "What?"
    call her_main("Because I will do it!","open","surprised", cheeks="blush", tears="messy")
    her "And I will swallow and everything!"
    call her_main("And you wouldn't have to pay me a single house point!","shock","down_raised", cheeks="blush", tears="crying")
    m "uhm... Maybe some other time..."
    m "This is not the type of crying I find arousing..."
    call her_main("I'm sorry, sir. I'm such a mess...","angry","suspicious", cheeks="blush", tears="messy")
    call her_main("But this is so unexpected...","shock","down_raised", cheeks="blush", tears="crying")
    her "You made me so happy, sir...*sob!*"
    call her_main("Thank you sir! *SOB!* Thank you! *SOB!*","angry","suspicious", cheeks="blush", tears="messy")
    m "Well... err... there, there..."
    m "Better stop crying before you stain that new dress of yours with those tears..."
    call her_main("My new dress! *SOB!*","scream","worriedCl", cheeks="blush", tears="messy")
    m "Alright, you know what? Just get out of my office."
    m "Just take your dress and leave."
    call her_main("Of course... I am sorry, sir!","angry","suspicious", cheeks="blush", tears="messy")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand","mid","base")
    pause.3
    call her_chibi("stand","mid","base",flip="True")
    pause.2

    call her_walk(action="leave", speed=2)

    call bld
    m "......................"
    m "Women..."

    $ her_dress_wearable = True
    #Unlocks the dress in the wardrobe. Makes it wearable.
    #$ gave_the_dress = True # Removed. Starts in "label ball_ending_start" now.
    $ hg_event_pause += 2

    jump main_room
