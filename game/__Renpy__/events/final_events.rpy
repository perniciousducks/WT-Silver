
#hermione asks genie about who will be in-charge of the ball
label want_to_rule:
    
    $ event_chairman_happened = True #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    
    call hg_event_EnterRoom_block from _call_hg_event_EnterRoom_block #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") from _call_play_music_28 # HERMIONE'S THEME.
    
    #her "Professor Dumbledore?"
    call her_main("[genie_name]?","soft","base",xpos="right",ypos="base") from _call_her_main_410
    m "Miss Granger, how can I help you?"
    call her_main("Sir, have you made your decision yet on who will be in charge of the \"ABOC\" this year?","open","base") from _call_her_main_411
    m "\"ABOC\"?"
    call her_main("The \"Autumn Ball Organization Committee\", sir...","open","closed") from _call_her_main_412
    m "Ehm... Sure..."
    call her_main("Please excuse me if I am being too direct with this, sir...","normal","frown") from _call_her_main_413
    call her_main("But I think you should put me in charge.","open","angryCl") from _call_her_main_414
    her "I did it last year and it was the best organized \"autumn ball\" Hogwarts has had in years."
    call her_main("You said so yourself, sir. Do you remember?","normal","base") from _call_her_main_415
    m "Right, of course..."
    call her_main("So, is this a yes?","base","base") from _call_her_main_416
    her "Does this mean I will be in charge again this year?"

    menu:
        m "..."
        "\"You shall be in charge, miss Granger.\"":
            jump one_thing

        "\"No. Professor Snape shall be in charge!\"":
            call her_main("Professor Snape, sir?","normal","frown") from _call_her_main_417
            her "But, traditionally organizing and hosting the ball is the responsibility of the students..."
            her "Teachers are only present as the guests of honour..."
            m "Well of course... I was just kidding."
            m "You shall be in charge, [hermione_name]..."
            label one_thing:
                call her_main("Thank you, [genie_name].","base","base") from _call_her_main_418
            m "There is one condition, though..."
            call her_main("A conditions, [genie_name]?","normal","frown") from _call_her_main_419
            
            $ d_flag_04 = False
            label no_sleeping_with_professor:
                pass
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            menu:  
                m "..."
                "\"Show me your tits first.\"":
                    $ mad += 9
                    $ d_flag_01 = True
                    pass
                "\"Show me your pussy first.\"":
                    $ mad += 9
                    $ d_flag_02 = True
                    pass
                "\"Strip naked for me first.\"":
                    $ mad += 17
                    $ d_flag_03 = True
                    pass
                "\"You will have to sleep with me.\"" if not d_flag_04:
                    $ mad += 17
                    $ d_flag_04 = True
                    call her_main("I will have to... sleep...?","angry","wide") from _call_her_main_420
                    call her_main("...................","angry","angry",cheeks="blush") from _call_her_main_421
                    call play_music("chipper_doodle") from _call_play_music_29 # HERMIONE'S THEME.
                    her "I am not stupid, sir... Quite the opposite in fact."
                    her "And I understand that the nature of the favours I have been selling you lately..."
                    her "...Might have led you to believe that I would be willing to..."
                    her "...To let you have your way with me eventually, sir..."
                    m "Wha-a-a...? I would never--"
                    call her_main("Please, let me finish, sir.","scream","angry",emote="01") from _call_her_main_422
                    m "Right..."
                    call her_main("I know that you are a rather wise man yourself, sir.","angry","angry") from _call_her_main_423
                    call her_main("So, please... understand this...","disgust","glance") from _call_her_main_424
                    her "I may be willing to sacrifice my pride and even my dignity for the sake of my house..."
                    her "But sleeping with my headmaster?"
                    call her_main("That is where I draw the line, sir.","angry","angry",cheeks="blush") from _call_her_main_425
                    m "Got it. Let's just forget I said anything."
                    call her_main("{size=-5}(I wish I could...){/size}","angry","suspicious",cheeks="blush") from _call_her_main_426
                    jump no_sleeping_with_professor 
       
                "\"Never mind. the Position is yours.\"":
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    call blkfade from _call_blkfade
                    pass
    

            if d_flag_01 or d_flag_02 or d_flag_03:
                call her_main("What?!","open","base") from _call_her_main_427
                m "What?"
                #her "Professor!"
                call her_main("[genie_name]!","angry","angry") from _call_her_main_428
                m "What?"
                call her_main("You are abusing your power, sir. Again!","disgust","glance") from _call_her_main_429
                m "Seriously? After all those favours you sold me?"
                call her_main("Those were for the sake of my house, sir.","annoyed","annoyed") from _call_her_main_430
                m "Well this one is for the sake of the \"Autumn prom\"."
                call her_main("It's the \"Autumn Ball\", sir...","upset","closed") from _call_her_main_431
                m "Oh, come on..."
                m "Entrusting the thing to somebody else would be a crime, you know that."
                call her_main("..........","annoyed","angryL") from _call_her_main_432
                m "Don't you care about your classmates at all?"
                call her_main("What?","open","base") from _call_her_main_433
                m "Put your selfishness aside for once, would you?"
                call her_main("My... selfishness?","annoyed","worriedL") from _call_her_main_434
                m "Your classmates deserve the best organized ball possible!"
                m "And only {size=+5}YOU{/size} can give them that!"
                call her_main("...that is true actually.","angry","down_raised") from _call_her_main_435
                m "People depend on you, girl!"

                if d_flag_01:
                    m "So I suggest that you stop being selfish and show me your tits!"
                elif d_flag_02:
                    m "So I suggest that you stop being selfish and show me your pussy!"
                elif d_flag_03:
                    m "So I suggest that you stop being selfish and get naked for me!"

                #her "You are completely right, professor!"
                call her_main("You are completely right, [genie_name]!","open","down") from _call_her_main_436
                call her_main("I must do this. Everyone depends on me.","upset","closed") from _call_her_main_437
                call her_main("Just give me a second please...","base","glance") from _call_her_main_438
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d5   
                m "............"

                if d_flag_01: # SHOW ME TITS
                    call play_music("playful_tension") from _call_play_music_30# SEX THEME.
                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    pause.3
                    call her_chibi("lift_top","mid","base") from _call_her_chibi_2
                    with fade
                    pause.8
                    
                    $ hermione_wear_bra = False
                    call h_action("lift_top") from _call_h_action
                    pause.5
                    
                    show screen blktone
                    call her_main("","annoyed","base") from _call_her_main_439
                    call ctc from _call_ctc_13

                    m "Very good miss Granger..."
                    m "Your ample tits are always a welcome sight..."
                    call her_main("....................","disgust","down_raised") from _call_her_main_440
                    call ctc from _call_ctc_14

                    hide screen hermione_main
                    hide screen blktone
                    call blkfade from _call_blkfade_1
                    call reset_hermione_main from _call_reset_hermione_main

                elif d_flag_02: # SHOW ME PUSSY
                    call play_music("playful_tension") from _call_play_music_31# SEX THEME.
                    
                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    call ctc from _call_ctc_15

                    $ hermione_wear_panties = False
                    call her_chibi("lift_skirt","mid","base") from _call_her_chibi_3
                    with fade
                    call ctc from _call_ctc_16
            
                    call h_action("lift_skirt") from _call_h_action_1
                    pause.5
                    
                    show screen blktone
                    call her_main("","annoyed","base") from _call_her_main_441
                    call ctc from _call_ctc_17
                    
                    call her_main("","base","worriedCl") from _call_her_main_442
                    call ctc from _call_ctc_18
                    
                    her ".............................."
                    with hpunch
                    g4 "What are you doing, girl?!"
                    g4 "I am your headmaster! Do you have no shame?!"
                    call her_main("What?! But--","angry","angry",cheeks="blush") from _call_her_main_443
                    g9 "He-he... Relax, girl. I'm just kidding."
                    call her_main("[genie_name], that was just mean.","scream","angryCl") from _call_her_main_444
                    g9 "He-he..."
                    call her_main(".....................................","annoyed","angry") from _call_her_main_445
                    m "I do like your shaved little pussy though..."
                    call her_main(".....thank you, sir.","annoyed","angry") from _call_her_main_446
                    call ctc from _call_ctc_19

                    hide screen hermione_main   
                    hide screen blktone   
                    call blkfade from _call_blkfade_2

                    call reset_hermione_main from _call_reset_hermione_main_1
                
                elif d_flag_03: # STRIP NAKED
                    call play_music("playful_tension") from _call_play_music_32# SEX THEME.

                    hide screen blkfade
                    hide screen bld1
                    hide screen hermione_main
                    with d5
                    
                    
                    #Walks to the door
                    call her_walk("mid","door",2) from _call_her_walk_16
                    
                    #Locks the door
                    pause.5
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    call her_chibi("stand","door","base") from _call_her_chibi_4
                    pause.5
                    
                    #Returns from the door
                    m "??!"
                    call her_walk("door","mid",3) from _call_her_walk_17
                    pause.2
                    show screen bld1
                    with d3
                    
                    call her_main("Just in case...","annoyed","angryL") from _call_her_main_447
                    call ctc from _call_ctc_20
                    m ".........................."

                    show screen blktone
                    call nar(">Hermione is taking her clothes off...") from _call_nar_8
                    pause.2
                    
                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top") from _call_set_hermione_action
                    pause.5
                
                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update") from _call_set_hermione_action_1
                    pause.5

                    call nar(">One piece after another...") from _call_nar_9

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt") from _call_set_hermione_action_2
                    pause.5
                
                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update") from _call_set_hermione_action_3
                    pause.5

                    call nar(">Vest, shirt, her skirt, and finally...") from _call_nar_10
                    
                    $ hermione_wear_panties = False
                    call set_hermione_action("covering") from _call_set_hermione_action_4
                    pause.5

                    call nar(">The panties.") from _call_nar_11
                    call ctc from _call_ctc_21
                    
                    g9 "Ni-i-i-ce!"
                    call her_main("","soft","squintL") from _call_her_main_448
                    call ctc from _call_ctc_22
                    her "*Sob!*"
                    m "Huh?"
                    
                    $ display_h_tears = True
                    $ u_tears_pic = "characters/hermione/face/tears_01.png"
                    
                    call her_main("Oh, please, don't mind me, sir.","open","baseL",) from _call_her_main_449
                    call her_main("Just enjoy the... {w}the... {w}the view...","soft","squintL") from _call_her_main_450
                    m "Are you... crying?"
                    call her_main("*Sob!* No, not really, sir... *sob!*...","angry","worriedCl") from _call_her_main_451
                    her "It is just that I am standing here before my headmaster completely naked... *SOB!*"
                    call her_main("These are the tears of shame, sir.","shock","angryL",tears="messy") from _call_her_main_452
                    her "I can't help it! *Sob!*"
                    m "Are you sure that you are ok with this?"
                    call her_main("Yes, yes, sir, please.... *Sob!*","soft","angry",tears="messy") from _call_her_main_453
                    call her_main("Please keep on looking at my naked body... *Sob!*","shock","wide",tears="messy") from _call_her_main_454
                    
                    call her_main("","angry","angry",cheeks="blush",tears="messy") from _call_her_main_455
                    call set_hermione_action("lift_breasts") from _call_set_hermione_action_5
                    pause.2
                    
                    g4 "(What the...?)"
                    call her_main("Sir, I am begging you!","angry","angry",cheeks="blush",tears="messy") from _call_her_main_456
                    m "Kind of sounds like an order--"       
                    call her_main("I need it!","angry","dead_mad",cheeks="blush",tears="messy") from _call_her_main_457
                    her "...I need to shamelessly present my naked body before you like this!"
                    m ".............?"
                    call her_main("I need to feel this embarrassment and humiliation! *SOB!*","upset","dead_mad",cheeks="blush",tears="messy") from _call_her_main_458
                    call her_main("The fate of the \"Autumn ball\" depends on this...","grin","ahegao_mad",cheeks="blush",tears="messy") from _call_her_main_459
                    her "So, sir, please..."
                    call her_main("Keep looking at my naked breasts, and my pussy...","grin","angry",cheeks="blush",tears="messy") from _call_her_main_460
                    call ctc from _call_ctc_23

                    call her_main("Yes! Make my skin burn with shame, sir... *Sob!*","open","ahegao_raised",cheeks="blush",tears="messy") from _call_her_main_461
                    m "Ehm... right... Ok..."
                    m "Listen, I think this will do..."
                    call set_hermione_action("pinch") from _call_set_hermione_action_6
                    call her_main("Are you sure, sir?","angry","angry",cheeks="blush",tears="messy") from _call_her_main_462
                    her "Are you sure that you humiliated me enough, sir?"
                    m "...................."
                    m "(Is she getting off on this? Is she being sarcastic? I don't get it...)"
                    her ".........................."
                    call ctc from _call_ctc_24

                    m "Just put your clothes back on, Miss Granger. You're making me feel uncomfortable."
                    call her_main("As you wish, sir...","annoyed","angryL",tears="messy") from _call_her_main_463
                    
                    call ctc from _call_ctc_25
                    
                    hide screen hermione_main  
                    hide screen blktone
                    call blkfade from _call_blkfade_3

                    $  u_tears_pic = "characters/hermione/face/tears_03.png"

                    call reset_hermione_main from _call_reset_hermione_main_2

                
                    
                    
                    
    call play_music("chipper_doodle") from _call_play_music_33 # HERMIONE'S THEME.             
                    
    call her_chibi("stand","mid","base") from _call_her_chibi_5
    call hide_blkfade from _call_hide_blkfade_1
    call ctc from _call_ctc_26

    show screen bld1
    call her_main("So I am officially in charge of this year's \"Autumn Ball Organization Committee\" now?","base","happyCl",xpos="right",ypos="base") from _call_her_main_464
    m "That you are."
    her "Thank you sir! You will not regret this, I promise!"
    m "{size=-4}(Why would I?){/size}"
    m "{size=-4}(I couldn't care less about the whole thing...){/size}"
    call her_main("Well, I'd better go now. I have so many arrangements to make!","grin","baseL") from _call_her_main_465
    m "By all means, Miss Granger. Have a nice day."
    hide screen hermione_main
    hide screen bld1
    with d3 
    pause.2
    
    call her_walk("mid","leave",2) from _call_her_walk_18

    pause.5
    call bld from _call_bld_33
    m "........................................"
    m "A ball, huh?"
    m "I wonder if I will have to show up for that..."
    hide screen bld1
    with d3

    $ hermione_takes_classes = True
    $ days_without_an_event = 0

    $ display_h_tears = False
    
    call music_block from _call_music_block
    
    return
    
#==========================

#Snape confronts genie about his ABOC decision

label against_the_rule:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    $ snape_against_chairman_hap = True # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ days_without_an_event = 0
    
    call play_sound("door") from _call_play_sound_31 #Sound of a door opening.
    call sna_walk("door","mid",3) from _call_sna_walk_8
    pause.2

    show screen bld1
    call sna_main("Are you bloody insane?!","snape_01",xpos="base",ypos="base") from _call_sna_main_83
    m "You know, sometimes I think I may be..."
 
    call sna_main("You appointed the girl as the head of the \"Autumn Ball Organization Committee\"?!!","snape_01") from _call_sna_main_84
    m "I'm guessing that's bad?"
    call sna_main("Bad?{w} {size=+5}BAD?!{/size}","snape_10") from _call_sna_main_85
    call sna_main("{size=+5}That's a catastrophe!{/size}","snape_15") from _call_sna_main_86
    call sna_main("last year's ball was completely horrible!","snape_16") from _call_sna_main_87
    m "Was it? I heard differently..."
    call sna_main("Oh really? And who told you that?","snape_10") from _call_sna_main_88
    m "not a very reliable source apparently..."
    call sna_main("Dammit... Dammit all to hell...","snape_08") from _call_sna_main_89
    call sna_main("I had big plans for the thing...","snape_07") from _call_sna_main_90
    m "Really? Like what?"
    call sna_main("Oh, that doesn't matter now...","snape_06") from _call_sna_main_91
    #sna "The girl is a complete control freak..."
    sna "Now the girl will use prefects or the ghosts to keep an eye on me throughout entire thing..."
    m "Right, that reminds me..."
    m "Am I supposed to show up as well?"
    call sna_main("Show up?","snape_03") from _call_sna_main_92
    sna "You are expected to host the bloody thing!"
    call sna_main("But don't you worry! I'll figure something out!","snape_09") from _call_sna_main_93
    call sna_main("Hm... I'll Probably have to host the ball instead...","snape_06") from _call_sna_main_94
    m "............"
    call sna_main("Well, the Autumn ball is about to happen and Hermione Granger is in charge...","snape_09") from _call_sna_main_95
    sna "There is no changing it now..."
    call sna_main("Sorry for the outburst...","snape_05") from _call_sna_main_96
    call sna_main("That girl brings out the worst in me...","snape_16") from _call_sna_main_97
    m "Don't sweat it..."
    call sna_main("You know what...?","snape_06") from _call_sna_main_98
    sna "I don't feel like working today..."
    call sna_main("Do we still have any of Dumbledore's wine left?","snape_05") from _call_sna_main_99
    m "I believe so..."
    call sna_main("Great! Pour me some...","snape_02") from _call_sna_main_100
    m "Seriously? You're just gonna bail on your class like that?"
    call sna_main("Yeah, big news - I hate my job.","snape_03") from _call_sna_main_101
    sna "And since you are my boss..."
    call sna_main("I don't know why I even bother teaching those so-called students...","snape_06") from _call_sna_main_102
    m "To maintain the charade?"
    m "for the Same reason why I never leave this room...?"
    call sna_main("Right...","snape_05") from _call_sna_main_103
    sna "But you know what else could endanger out little enterprise?"
    call sna_main("Me losing it during class and strangling a couple of \"Gryffindor\" maggots with my bare hands...","snape_07") from _call_sna_main_104
    m "Hm... I see your point..."
    call sna_main("Seriously, man... I need a drink...","snape_06") from _call_sna_main_105

    hide screen snape_main
    call blkfade from _call_blkfade_4
    
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk
    
    $ fire_in_fireplace = True
    call sna_chibi("hide") from _call_sna_chibi_1
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_2
    
    call bld from _call_bld_34
    call nar("Professor Snape spends the day in your chamber, drinking the stress away.") from _call_nar_12
    
    if not sfmax:# Turns TRUE when friendship with Snape been maxed out.
        call nar(">Your relationship with him has improved.") from _call_nar_13
        $ snape_friendship +=1
   
    call blkfade from _call_blkfade_5
    
    hide screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    hide screen fireplace_fire
    show screen genie
    show screen chair_right
    show screen desk
    hide screen desk
    
    hide screen bld1

    stop bg_sounds #Stops playing the fire SFX.
   
    jump night_start
         
    
#============================

label crying_about_dress:
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    call hg_event_EnterRoom_block from _call_hg_event_EnterRoom_block_1 #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") from _call_play_music_34 # HERMIONE'S THEME.
    
    call her_main("My parents sent me the wrong dress!","angry","base",tears="soft",xpos="right",ypos="base") from _call_her_main_466
    m "are You kidding me!?"
    call her_main("They sent me the dress I wore to the ball last year...","angry","base",tears="soft") from _call_her_main_467
    m "Those inconsiderate bastards!"
    call her_main("Are you making fun of me sir?","mad","worried",tears="soft") from _call_her_main_468
    m "Can you blame me?"
    call her_main("I will become the laughingstock of Hogwarts! *Sob!*","clench","worried",cheeks="blush",tears="soft") from _call_her_main_469
    call her_main("My reputation is as good as ruined! *Sob!*","angry","dead",cheeks="blush",tears="crying") from _call_her_main_470
    m "Seriously? After all the favours you sold me you care about a thing like this?"
    call her_main("Wearing the same dress to the \"Autumn Ball\" for two years in a row would be more humiliating than any favour I sold you so far, sir.","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_471
    with hpunch
    g4 "You've gotta be kidding me..."
    call her_main("Oh, you wouldn't understand...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_472
    call her_main("You're just like my father!","scream","angry",cheeks="blush",tears="messy") from _call_her_main_473
    m "I beg your pardon?"
    call her_main("I mean... ehm...","open","surprised",cheeks="blush",tears="messy") from _call_her_main_474
    her "Forgive me sir..."
    call her_main("I don't know why I am telling you all of this...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_475
    m "................"
    call her_main("......................*sob!*","angry","dead",cheeks="blush",tears="crying") from _call_her_main_476
    call her_main("I think I'd better go now...*sob*","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_477
    m "Well, don't let me keep you a moment longer, miss Granger...."
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3
    
    call her_walk("mid","door",2) from _call_her_walk_19
    pause.3 

    show screen bld1
    call her_head("(My life is ruined...)","angry","suspicious",cheeks="blush",tears="messy",xpos="base",ypos="base") from _call_her_head_6
    pause.1
    call her_chibi("leave","door","base") from _call_her_chibi_6
 
    m "Hm... I don't remember ever seeing the girl this desperate..."
    m "And that says a lot, all things considered..."
    m "I suppose whoring herself out for house points is a significantly smaller problem than not having a proper prom dress..."
    m ".............."
    m "Schoolgirls..."
       
    hide screen bld1
    with d3
    
    $ hermione_takes_classes = True
    
    call music_block from _call_music_block_1
    
    return 
    
#===========================

label sorry_about_hesterics:
    $ sorry_for_hesterics = True # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    $ days_without_an_event = 0
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    call hg_event_EnterRoom_block from _call_hg_event_EnterRoom_block_2 #Chibi stands mid. bld1 active.
    
    call play_music("chipper_doodle") from _call_play_music_35 # HERMIONE'S THEME.
    
    m "Miss Granger?"
    call her_main("Sorry to disturb you sir...","open","worried",xpos="right",ypos="base") from _call_her_main_478
    call her_main("I came to apologize for my...","open","worriedL") from _call_her_main_479
    her "...my hysterical behaviour yesterday."
    m "Sure thing, don't worry about it."
    call her_main("Thank you, sir.","open","base") from _call_her_main_480
    call her_main("Still, I cannot help but feel awful for causing a scene...","open","angryCl") from _call_her_main_481
    m "So the issue has been resolved then?"
    call her_main("Not really...","open","worried") from _call_her_main_482
    call her_main("Not at all actually...","annoyed","angryL") from _call_her_main_483
    m "Hm..?"
    call her_main("But that is not a big deal...","annoyed","down") from _call_her_main_484
    her "I'm just overreacting..."
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("I woN't be able to attend the ball this year... so what?","annoyed","down") from _call_her_main_485
    call her_main("I spent countless hours with organizing the event...","normal","worriedCl") from _call_her_main_486
    call her_main("I worked so hard... and...","open","worried",tears="soft") from _call_her_main_487
    call her_main("And now I will not even be able to... to... *Sob!*","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_488
    call her_main("To... *SOB!*","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_489
    call her_main("Excuse me sir!","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_490
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    hide screen no_groping_02
    hide screen bld1
    show screen genie
    with d1
    
    call her_walk("mid","leave",2,action="run") from _call_her_walk_20
    pause.5
    
    call bld from _call_bld_35
    m "......................................."
    m "Hm..."

    $ hermione_takes_classes = True

    hide screen bld1
    with d3
    
    call music_block from _call_music_block_2
    
    return
    
    
#=========================

label giving_the_dress:
    hide screen wardrobe_gifts
    "Are you sure you wish to start this event?"

    menu: 
        "Yes!":
            jump giving_thre_dress
        "No.":
            pass

    call screen wardrobe_gifts

label giving_thre_dress:
    $ gave_the_dress = True #Turns True when Hermione has the dress.
    $ days_without_an_event = 0

    hide screen hermione_main
    with d5
    
    $ mad = 0
    stop music fadeout 1.0
    m "Here... This is for you..."
    $ the_gift = "images/store/01.png" # DRESS.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the ball gown to Hermione..."
    hide screen gift
    with d3
    call her_main("Hm...? What is this?","base","base") from _call_her_main_491
    call her_main("{size=+7}A DRESS?!{/size}","angry","wide") from _call_her_main_492
    with hpunch
    m "I thought that you--"
    call play_music("chipper_doodle") from _call_play_music_36 # HERMIONE'S THEME.
    call her_main("[genie_name]!","angry","base",tears="soft") from _call_her_main_493
    g4 "What? What happened? Don't tell me it's the wrong color or something!"
    call her_main("It's perfect, sir...*sob!*","angry","base",tears="soft") from _call_her_main_494
    her "It's perfect... *sob!* ...I love it."
    m "You sure don't look like it..."
    her "I am sorry, sir... *Sob!*"
    call her_main("I... I am just...","clench","worried",cheeks="blush",tears="soft") from _call_her_main_495
    call her_main("I am so happy...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_496
    her "Thank you, sir. Thank you so much."
    call her_main("I cannot believe that you would do something like that for me...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_497
    m "Well, I did. Now stop crying."
    call her_main("I can't, sir. I am so happy and so grateful...","scream","worriedCl",cheeks="blush",tears="messy") from _call_her_main_498
    call her_main("Do you want me to suck your cock, sir?","open","surprised",cheeks="blush",tears="messy") from _call_her_main_499
    m "What?"
    call her_main("Because I will do it!","open","surprised",cheeks="blush",tears="messy") from _call_her_main_500
    her "And I will swallow and everything!"
    call her_main("And you wouldn't have to pay me a single house point!","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_501
    m "uhm... Maybe some other time..."
    m "This is not the type of crying I find arousing..."
    call her_main("I'm sorry, sir. I'm such a mess...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_502
    call her_main("But this is so unexpected...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_503
    her "You made me so happy, sir...*sob!*"
    call her_main("Thank you sir! *SOB!* Thank you! *SOB!*","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_504
    m "Well... err... there, there..."
    m "Better stop crying before you stain that new dress of yours with those tears..."
    call her_main("My new dress! *SOB!*","scream","worriedCl",cheeks="blush",tears="messy") from _call_her_main_505
    m "Alright, you know what? Just get out of my office."
    m "Just take your dress and leave."
    call her_main("Of course... I am sorry, sir!","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_506
    hide screen hermione_main  
    hide screen bld1                                                                                                                                                                               #HERMIONE
    with d3          
    pause.1
    
    call her_chibi("stand","mid","base") from _call_her_chibi_7
    pause.3
    call her_chibi("stand","mid","base",flip="True") from _call_her_chibi_8
    pause.2
    
    call her_walk("mid","leave",2) from _call_her_walk_21
    
    call bld from _call_bld_36
    m "......................"
    m "Women..."
    hide screen bld1
    with d3

    call music_block from _call_music_block_3
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
    
    
    
###======================================================================
    
    
label good_bye_snape:

    $ days_without_an_event = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    call play_sound("door") from _call_play_sound_32 #Sound of a door opening.
    call sna_walk("door","desk",2.5) from _call_sna_walk_9 
    pause 1.5

    show screen bld1
    call sna_main("Genie...","snape_01",xpos="base",ypos="base") from _call_sna_main_106
    m "Severus?"
    call sna_main("I think I may have figured out why your magic does not work the way it should...","snape_05") from _call_sna_main_107
    g4 "Seriously?!"
    call sna_main("Yes...","snape_23") from _call_sna_main_108
    sna "It's quite obvious actually... I'm surprised that it didn't cross my mind before."
    call sna_main("You see, the thing is that every building in \"Hogwarts\" is enchanted with all kinds of protection spells...","snape_24") from _call_sna_main_109
    m "Protection spells, huh?"
    call sna_main("Yes...","snape_23") from _call_sna_main_110
    sna "Very powerful, old and nasty magic..."
    call sna_main("Even the land itself is heavily enchanted for kilometers in every direction...","snape_24") from _call_sna_main_111
    m "Hm..."
    call sna_main("Basically, any number of spells could be interfering with your powers around here...","snape_25") from _call_sna_main_112
    m "Wait, then how come that you have no problems with casting your spells?"
    call sna_main("My magic is \"Hogwarts\" magic, friend...","snape_05") from _call_sna_main_113
    sna "But I bet your powers are alien enough to be perceived as a threat."
    m "Interesting..."
    call sna_main("I think if you manage to get far enough from the school grounds...","snape_24") from _call_sna_main_114
    m "I will be able to go home... finally..."
    call sna_main("Yes, and the best time to do that would be tonight...","snape_02") from _call_sna_main_115
    call sna_main("While everyone is preoccupied with that bloody \"Autumn ball\" you could sneak out unnoticed...","snape_23") from _call_sna_main_116
    
    ### SHAKE HANDS WITH SNAPE ###
    hide screen snape_main
    call blkfade from _call_blkfade_6
    
    hide screen genie
    hide screen bld1
    call sna_chibi("hide") from _call_sna_chibi_2
    show screen chair_left
    show screen g_c_u
    $ genie_chibi_xpos = 220
    $ genie_chibi_ypos = 205
    $ g_c_u_pic = "images/main_room/hand_00.png"
    play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 # EPIC THEME.
    pause 1
    
    m "Right, tonight is the night of the \"Autumn ball\"..."
    m "So it ends tonight then..."
    call sna_head("Seems like it...","snape_09") from _call_sna_head_122
    call hide_blkfade from _call_hide_blkfade_3
    pause.5

    call sna_head("In case I'm right and will never see you again...","snape_05") from _call_sna_head_123
    m "Right..."
    call blkfade from _call_blkfade_7

    $ g_c_u_pic = "images/main_room/hand_01.png"
    call hide_blkfade from _call_hide_blkfade_4
    pause 2

    call bld from _call_bld_37
    call sna_head("The past several month were the best months of my life, Genie...","snape_26") from _call_sna_head_124
    call sna_head("Thank you for that, you incredible traveler from another world...") from _call_sna_head_125
    call sna_head("Thank you, my friend...") from _call_sna_head_126
    m "I don't know what to say, Severus..."
    call sna_head("Then don't say anything...","snape_06") from _call_sna_head_127
    call sna_head("Just move on to your next adventure...") from _call_sna_head_128
    call sna_head("Our world has stalled you long enough...") from _call_sna_head_129
    m "Thank you for keeping me company and being my only friend here, Severus."
    call sna_head("Thank you for being mine...","snape_27") from _call_sna_head_130 #TEARS?
    call sna_head("I'd better go now...","snape_06") from _call_sna_head_131
    #Goes to the door, stops and turns around.
    
    hide screen s_head2
    call blkfade from _call_blkfade_8

    hide screen chair_left
    hide screen g_c_u
    show screen genie
    pause.5

    call sna_chibi("stand","desk","base") from _call_sna_chibi_3
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_5
    pause.5
    
    call sna_walk("desk","door",3) from _call_sna_walk_10
    pause.5

    call sna_chibi("stand","door","base") from _call_sna_chibi_4
    pause.5

    call bld from _call_bld_38
    call sna_head("One more thing though...","snape_01") from _call_sna_head_132
    m "Yes?"
    call sna_head("If it all goes well...","snape_24") from _call_sna_head_133
    call sna_head("Will I find the real Albus Dumbledore in that chair tomorrow?") from _call_sna_head_134
    m "I believe so..."
    call sna_head("Hm...","snape_04") from _call_sna_head_135
    call sna_head("Albus can't know that I was aware of his absence...","snape_03") from _call_sna_head_136
    call sna_head("Is there a way to tell you guys apart?","snape_01") from _call_sna_head_137
    m ".............."
    m "How about a secret password?"
    call sna_head("A password?","snape_05") from _call_sna_head_138
    m "Yes... just ask me tomorrow: \"Who rules?\"."
    call sna_head("\"Who rules?\"","snape_01") from _call_sna_head_139
    g9 "\"Akabur rules!\""
    call sna_head("Akuba... ehm... What does it mean?","snape_05") from _call_sna_head_140
    m "Just a phrase that you will only be able to hear from the real me..."
    call sna_head("I understand...","snape_02") from _call_sna_head_141
    call sna_head("Alright then...","snape_06") from _call_sna_head_142
    call sna_head("Have a save trip home...") from _call_sna_head_143
    hide screen s_head2
    m "Thank you. Have fun with hosting the ball..."
    call sna_head("*Sigh*","snape_06") from _call_sna_head_144
    pause.3

    hide screen bld1
    with d3
    pause.3
    
    stop music fadeout 1.0

    call sna_chibi("stand","door","base",flip=True) from _call_sna_chibi_5
    pause.3

    call sna_chibi("leave","door","base") from _call_sna_chibi_6
    pause.8
    
    m "............................"
    m "So this is it then...?"
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    m "Seems like my time in this world has come to an end..."
    m "......................."

    if not public_whore_ending: #YOUR PERSONAL WHORE ENDING. WRITING A LETTER.
        m "That Means I'll probably never see the girl again..."
        m "..........."
        m "When I first met her she was so annoying..."
        m "to be honest, all the training I put her through changed very little in that regard..."
        m "But we did have a few special moments together..."
        m ".............."
        m "......................"
        m "I doesn't feel right to leave her without saying goodbye properly..."
        m "And yet I don't want to miss my chance to sneak out unnoticed..."
        m "I don't like long goodbyes..."
        m "Hm..."
        m "I suppose I could leave her a note or something..."
        
        m "Let's see..."
        call bld from _call_bld_39
        hide screen genie
        show screen paperwork
        with d3
        m "\"Dear...\""
        show screen genie
        hide screen paperwork
        with d3
        m "Hm... How shoud I adress her?"

        menu:
            m "Dear..."
            "\"Miss Granger\"":
                 $ word_01 = "Hermione Granger" 
            "\"Nasty whore\"":
                $ word_01 = "Nasty whore"
            "\"Slut\"":
                $ word_01 = "Slut"
            "\"Cumbucket\"":
                $ word_01 = "Cumbucket"
            "\"Human female\"":
                $ word_01 = "Human female"
            "\"friend\"":
                $ word_01 = "Friend"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"Dear [word_01]\" fits perfectly..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...it is time for me to go back...\""
        show screen genie
        hide screen paperwork
        with d3
        m "What should I write now?"

        menu:
            m "...time to go back..."
            "\"home\"":
                $ word_02 = "home"
            "\"to the mothership\"":
                $ word_02 = "to the mothership"
            "\"to Dimension \"X\"":
                $ word_02 = "to Dimension \"X\""
            "\"to my world\"":
                $ word_02 = "to my world"
            "\"To my Home Planet - Krypton\"":
                $ word_02 = "to my Home Planet - Krypton"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"Time to go back [word_02]\" that will do..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...farewell my little...\""
        show screen genie
        hide screen paperwork
        with d3
        m "What should I write now?"

        menu:
            m "...farewell my little... "
            "\"cock-hungry slut\"":
                $ word_03 = "cock-hungry slut"
            "\"cum receptacle\"":
                $ word_03 = "cum receptacle"
            "\"Girl\"":
                $ word_03 = "girl"
            "\"Witch\"":
                $ word_03 = "witch"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"farewell my little [word_03]\" sounds about right..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        show screen genie
        hide screen paperwork
        with d3
        m "And now to sign it as..."

        label stupid_kent:
            pass

        menu:
            m "..."
            "\"Genie\"":
                $ word_04 = "Genie"
            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                hide screen genie
                show screen paperwork
                with d3
                m "Yes, \"sincerely yours, [word_04]\"..."
                show screen genie
                hide screen paperwork
                with d3
                m "..........."
                m "No, that doesn't make any sense..."
                jump stupid_kent
            "\"Lord Voldemort\"":
                $ word_04 = "Lord Voldemort"
            "\"Traveler\"":
                $ word_04 = "Traveler"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"[word_04]\"..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "........................"
        m "Yes, this should do..."

    hide screen bld1
    with d3
    m "Well, off I go then..."
    
    call blkfade from _call_blkfade_9

    hide screen genie
    show screen chair_left
    hide screen desk
    show screen desk
    call gen_chibi("stand","desk","base") from _call_gen_chibi_4
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_6
    
    m "........."

    call gen_walk("desk","door",3) from _call_gen_walk
    pause 1

    m "...................."
    m "Agrabah... here I come..."
    call ctc from _call_ctc_27
    
    call gen_chibi("leave","door","base") from _call_gen_chibi_5
    pause.3
    ">.......................{w}............................{w}.....................{w}......................"
    pause.7
    call blkfade from _call_blkfade_10
    
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen blkback # Hide room

    $ end_u_1_pic =  "images/yule_ball/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    call hide_blkfade from _call_hide_blkfade_7
    call ctc from _call_ctc_28
    
    m "Severus was right..."
    pause.5
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "images/yule_ball/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7      
    
    m "The farther away I get from the school grounds..."
    m "The more powerful I'm starting to feel..."
    
    $ end_u_4_pic =  "images/yule_ball/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    m "I think  this is far enough..."
    m "Time to undo the spell and go back home..."
    m ".........."
    m "...................."
    m "Agrabah, here I come..."

    if not persistent.game_complete: # FIRST PLAYTHOURGH. 
        call ctc from _call_ctc_29
        
        show screen blkfade 
        with d9
        pause .5
        
        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.
        
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}This is ending \"00\" out of \"02\".{/color}{/size}"
        
        centered "{size=+7}{color=#cbcbcb}Thank you for playing!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}AKABUR 2014{/color}{/size}"
        
        
        #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
        #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
        #scene image "08_ending/e05.png" with Dissolve(2)
        # show akaani with d5

        
        centered "{cps=20}{size=+5}{color=#ea91b0}-Hermione Trainer-{/color}{/size}\n\n
        {size=+5}{color=#e5e297}-Producer-{/color}{/size}\n{color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Head programmer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Writer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Artwork-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Additional Artwork-{/color}{/size}\n     {color=#cbcbcb}DAHR{/color}\n\n
        {size=+5}{color=#e5e297}-Sound Effects-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n"
    #    {size=+5}{color=#e5e297}-MUSIC-{/color}{/size}\n\n

    #    {color=#e5e297}(From \"NEWGROUNDS\")\n
    #    {color=#e5e297}\"Eastern Journey\" {/color}{color=#cbcbcb}by Pike270.{/color}\n
    #    {color=#e5e297}\"Grape Soda Is Fucking Raw\"{/color} {color=#cbcbcb}by jrayteam6.{/color}\n
    #    {color=#e5e297}\"The Eastern Wind\"{/color} {color=#cbcbcb}by roensb.{/color}\n
    #    {color=#e5e297}\"Silly Cat\" {/color}{color=#cbcbcb}by Maverlyn.{/color}\n
    #    {color=#e5e297}\"Kabul Flight\" {/color}{color=#cbcbcb}by Jumpstart.{/color}\n
    #    {color=#e5e297}\"Sleep Walking\" {/color}{color=#cbcbcb}by hektikmusic.{/color}{/cps}"
        #nvl clear
    #    hide akaani
        
        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Wait, I'm still here!"
        centered "{size=+7}{color=#cbcbcb}WHAT?!{/color}{/size}"
        g4 "I said I am still here, dammit!"
        centered "{size=+7}{color=#cbcbcb}Oh... :({/color}{/size}"
        
        
        
        hide screen end_u_4
        with d1
        hide screen blkfade 
        with d9
        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
        
    m "....................."
    if persistent.game_complete:
        m "No, I can't just leave like this!"
    else:
        m "I can't just leave like this!"
    
    m "I must see the girl one last time..."
    
    call ctc from _call_ctc_30
    
    show screen blkfade
    with d7
    
    stop music fadeout 1.0
    
    if not persistent.game_complete: # FIRST PLAY THROUGH.
        centered "{size=+7}{color=#cbcbcb}Fine whatever...{/color}{/size}"
    play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
    centered "{size=+7}{color=#cbcbcb}\"The Annual Hogwarts Autumn Ball\"{/color}{/size}"

    hide screen end_u_4
    jump your_whore
    
    return
    
    
    
    
    

label hg_event_EnterRoom_block: #Chibi stands mid. bld1 active.
    call play_sound("door") from _call_play_sound_33 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_22
    pause.5
    call bld from _call_bld_40
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
