label __init_variables:
    $ heretic = 0
    $ heretic_01 = False
    $ heretic_02 = False
    $ heretic_03 = False
    $ heretic_busy = False
    $ hermione_desperate_done = False
    return
    
label heritic_intro:
    $ ce_base = True
    $ ce_top = True
    $ ce_arms = True
    $ ce_head_ypos = 235
    return
    
label heritic_event:
    $ ce_base = False
    $ ce_top = False
    $ ce_arms = False
    return

    
label heretic:
    $ ce_name = "heretic"
    $ menu_x = 0.5
    call heritic_intro from _call_heritic_intro
    hide screen hermione_main
    hide screen custom_event_h
    with d3
    m "{size=-4}(Is she really going to let me do this?){/size}"
    menu:
        "\"(I've got her well trained.  Why not?)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    m "Alright then..."
    if heretic == 0: #First time this event taking place.
        m "Miss Granger, do you know what a dildo is?"
        call ce_her_head("I... I'm familiar with the concept.","c") from _call_ce_her_head
        m "Have you used one before?"
        call ce_her_head("Excuse me?","q") from _call_ce_her_head_1
        m "There's no need to be embarrassed, girl, just tell me if you've ever used a dildo before."
        if whoring >=16:
            call ce_her_head("...yes I have.","e") from _call_ce_her_head_2
            g9 "Excellent, well you'll be using one today."
        else:
            call ce_her_head("...Of course not professor.","e") from _call_ce_her_head_3
            m "Well you'll be using one today."
    else:
        if whoring >=18:
            call ce_her_head("Well... if it's for the good of Gryffindor.","na") from _call_ce_her_head_4
        else:
            call ce_her_head("This again?","e") from _call_ce_her_head_5
            #### CONTINUE ####

### FIRST QUEST DAY ###
    if whoring <= 14:
        jump too_much
    else:
        call ce_her_head("You want to watch me masturbate?","s") from _call_ce_her_head_6
        call ce_her_head("Er...I have class to get to.","h") from _call_ce_her_head_7
        g9 "Perfect, because you'll need this."
        call ce_her_head("Oh my god, it's as big as my forearm!","s") from _call_ce_her_head_8
        call ce_her_head("Do you expect me to use this for you?","h") from _call_ce_her_head_9
        m "In a way. Put it in, girl."
        call ce_her_head("How many house points is this worth, sir?","c") from _call_ce_her_head_10
        m "I'll give you 50."
        call ce_her_head("Only 50? What if I hurt myself?","q") from _call_ce_her_head_11
        m "It's magically enchanted, there's no risk of injury."
        call ce_her_head("Really? Where did you get this?") from _call_ce_her_head_12
        m "Do you plan on getting one for yourself?"
        call ce_her_head("If I told you yes...{p}Would you give me more house points?","c") from _call_ce_her_head_13
        g4 "Miss Granger, would you rather get to class, or sit here and haggle?"
        call ce_her_head("Fine.") from _call_ce_her_head_14
        ">Hermione slips the dildo under her skirt, struggling to insert the vibrator into herself."
        call ce_her_head("I think it's too big, sir","h") from _call_ce_her_head_15
        m "Nonsense, keep trying."
        ">Changing her strategy, Hermione drops to her knees and rests the base of the cock against the floor. She starts rocking back and forth to wiggle the dick deeper inside her."
        g9 "Lift your skirt, bitch, I want to watch."
        
        call heritic_event from _call_heritic_event
        show screen blktone
        call ce_her_main("","p_jt",140) from _call_ce_her_main_89
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro from _call_heritic_intro_1
        
        ">Complying, Hermione flips her skirt up to reveal her engorged snatch."
        call ce_her_head("Oh my god... mmmmhh","v") from _call_ce_her_head_16
        g9 "Enjoying yourself?"
        call ce_her_head("Of course not. This is all for the... ahn... glory of Gryffindor.","e") from _call_ce_her_head_17
        g4 "Looks like you're enjoying yourself now, slut."
        call ce_her_head("Please sir, don't call me a slut. It's so...{p}{size=-2}degrading.{/size}","v") from _call_ce_her_head_18
        call ce_her_head("{size=-4}(I am a slut.){/size}","e") from _call_ce_her_head_19
        call ce_her_head("{size=-4}(Look what I've become!!!){/size}") from _call_ce_her_head_20
        call ce_her_head("{size=-5}(Masturbating in front of Professor Dumbledore for house points.){/size}") from _call_ce_her_head_21
        call ce_her_head("{size=-4}(I'm nothing but a common whore.){/size}") from _call_ce_her_head_22
        call ce_her_head("{size=-4}(I wish it didn't feel so good.){/size}","v") from _call_ce_her_head_23
        m "I'm sure. You better hurry up if you want to get to class."
        ">With that, Hermione's motions become frantic. Bouncing up and down, tears of frustration well up in the corners of her eyes."
        call ce_her_head("I can't... it won't go any deeper.","e") from _call_ce_her_head_24
        m "Allow me."
        
        call heritic_event from _call_heritic_event_1
        show screen blktone
        call ce_her_main("","p_di",140) from _call_ce_her_main_90
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro from _call_heritic_intro_2
        
        ">With a few idle movements of your one free hand, you forces the dildo to shoot up inside of Hermione."
        call ce_her_head("AAAAHHH!","a") from _call_ce_her_head_25
        ">Hermione falls sideways onto the floor as a puddle of her fluids pools around her."
        m "Good girl. Now off you go."
        call ce_her_head("Can't I stay here for a bit?","v") from _call_ce_her_head_26
        call ce_her_head("{size=-4}(So you can cum on my...){/size}","a") from _call_ce_her_head_27
        call ce_her_head("{size=-4}(OH GOD! Get it together Hermione!){/size}","s") from _call_ce_her_head_28
        g9 "So you can keep fucking yourself while I watch?"
        call ce_her_head("Of course not. I just need a moment.","c") from _call_ce_her_head_29
        m  "What are you doing?"
        call ce_her_head("Taking this dildo out, sir.","n") from _call_ce_her_head_30
        menu:
            "\"(That gives me an idea.)\"":
                g4 "No, you leave that where it is."
                if whoring >= 16:
                    call ce_her_head("But sir, I have class.","c") from _call_ce_her_head_31
                    g9 "I know."
                    call ce_her_head("You mean...") from _call_ce_her_head_32
                    call ce_her_head("SIR!","s") from _call_ce_her_head_33
                    call ce_her_head("You expect me to walk around all day with this...{p}inside of me?","i") from _call_ce_her_head_34
                    m "That's exactly what I expect."
                    call ce_her_head("...","e") from _call_ce_her_head_35
                    g9 "You had better hurry. Wouldn't want to be late for class."
                    
                    call heritic_event from _call_heritic_event_2
                    show screen blktone
                    call ce_her_main("","p_us",140) from _call_ce_her_main_91
                    show screen ctc
                    pause
                    hide screen custom_event_h
                    with d3
                    call heritic_intro from _call_heritic_intro_3
                    
                    call ce_her_head("Sir, it's sticking out of the bottom of my skirt!","e") from _call_ce_her_head_36
                    g9 "I know. Off you go."
                    call ce_her_head("{size=-4}(Oh god... I can barely walk... What if somebody notices?){/size}","e") from _call_ce_her_head_37
                    $ heretic_busy = True
                else:
                    jump too_much
            "\"(That's enough.)\"":
                m "Alright, you can go. Fifty points to Gryffindor."
                $ gryffindor +=50
                call ce_her_head("Uh, sir... Could you help me?","e") from _call_ce_her_head_38
                
                call heritic_event from _call_heritic_event_3
                show screen blktone
                call ce_her_main("","p_jt",140) from _call_ce_her_main_92
                show screen ctc
                pause
                hide screen custom_event_h
                with d3
                call heritic_intro from _call_heritic_intro_4
                
                ">You wave your hand. The dildo erupts out of Hermione, who begins spasming in ecstacy again."
                m "Now say thank you."
                call ce_her_head("Th...thaan...thank you...siiir.","a") from _call_ce_her_head_39
                m "Hurry along Miss Granger, I haven't got all day."
                ">Hermione slowly rises off the floor and lurches out of the room on shaky legs."
                if whoring <= 16:
                    $ whoring +=1
        hide screen bld1
        hide screen custom_event_h
        hide screen blktone
        hide screen hermione_02
        hide screen ctc
        with d3
        
        call her_walk(400,610,2) from _call_her_walk_94
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        with Dissolve(.3)
        
        call music_block from _call_music_block_14
        $ hermione_takes_classes = True
        $ only_upper = False
        $ badges = True
        jump day_main_menu
        #### END THE SCENE ####
### First Quest Night ###
label heretic_night:
    $ menu_x = 0.5
    call her_walk(520,400,2) from _call_her_walk_95
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    show screen hermione_02
    pause 0.5
    show screen bld1
    with Dissolve(.3)
    $ exposure = renpy.random.randint(1, 10)
    
    if exposure <= 3: #Caught By Harry
        m "Good evening Miss Granger."
        
        call heritic_event from _call_heritic_event_4
        show screen blktone
        call ce_her_main("","p_nd",140) from _call_ce_her_main_93
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro from _call_heritic_intro_5
        
        call ce_her_head("Hello sir.","n") from _call_ce_her_head_40
        m "So I see you didn't live up to you end of the bargain."
        call ce_her_head("Sir! I would never cheat!","i") from _call_ce_her_head_41
        call ce_her_head("Especially when Gryffindor's honor is at stake!") from _call_ce_her_head_42
        g4 "Then where is the dildo, girl?!"
        call ce_her_head("It's... err...","n") from _call_ce_her_head_43
        
        call heritic_event from _call_heritic_event_5
        show screen blktone
        call ce_her_main("","p_dd",140) from _call_ce_her_main_94
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro from _call_heritic_intro_6
        
        ">Hermione pulls up her skirt to reveal the dildo lodged deeply in her cunt."
        g4 "Would you care to explain yourself, or are you ready to admit what a whore you are?"
        call ce_her_head("I had no choice, sir.","na") from _call_ce_her_head_44
        m "You could have taken it out."
        call ce_her_head("Err...","e") from _call_ce_her_head_45
        m "Well, did you enjoy yourself today Miss Granger?"
        call ce_her_head("It was...","na") from _call_ce_her_head_46
        call ce_her_head("It was terrible sir.","i") from _call_ce_her_head_47
        m "What was so terrible about it, girl?"
        call ce_her_head("...I can't","e") from _call_ce_her_head_48
        m "Do you want your points or not?"
        call ce_her_head("Please sir, it was mortifying.") from _call_ce_her_head_49
        m "I'm waiting."
        call ce_her_head("...") from _call_ce_her_head_50
        call ce_her_head("I... As soon as I left I ran into Harry. He could...{p}I mean he didn't say anything{p}but I saw him staring at it.") from _call_ce_her_head_51
        m "Well, what did you do?"
        call ce_her_head("I... I knew I couldn't leave it dangling out...{p}and... I mean he already saw it...") from _call_ce_her_head_52
        g4 "Spit it out girl!"
        call ce_her_head("Harry fucked me with the dildo!","v") from _call_ce_her_head_53
        g9 "Oh you filthy whore."
        call ce_her_head("I needed help,{p}and we've been through so much together...") from _call_ce_her_head_54
        call ce_her_head("He must think I'm such a whore.","e") from _call_ce_her_head_55
        g9 "Did you tell him why you had a massive magical cock sticking out of you?"
        call ce_her_head("No. It's better he thinks I'm a slut.{p}I can't imagine him knowing I'm a traitor.{p}to him, or the cause!") from _call_ce_her_head_56
        g9 "Did you enjoy yourself?"
        call ce_her_head("How could you ask me that sir? I was humiliated.","i") from _call_ce_her_head_57
        m "You didn't answer the question."
        call ce_her_head("...","e") from _call_ce_her_head_58
        m "Well?"
        call ce_her_head("Can I go now sir?") from _call_ce_her_head_59
        g4 "Once you answer the question."
        call ce_her_head("...It wasn't terrible...") from _call_ce_her_head_60
        g9 "Did you cum?"
        call ce_her_head("You said I could go, sir.","i") from _call_ce_her_head_61
        menu:
            "\"Press Her.\"":
                g4 "You can go when I tell you to leave. Tell me Miss Granger, did you cum when your friend played with your pussy?"
                if whoring <= 17:
                    call ce_her_head("Sir, you said I could leave! I don't mind being subjected to your sick perversions if order to help out my house, but I draw the line here!","f") from _call_ce_her_head_62
                    g4 "Miss Granger..."
                    call ce_her_head("I'm not finished! You forced me to humiliate myself, and what do I have to show for it?") from _call_ce_her_head_63
                    m "...Fifty point to gryffindor."
                    $ gryffindor +=50
                    call ce_her_head("Good night, Sir.","i") from _call_ce_her_head_64
                    $ mad += 10
                    jump q7y8f5
                else:
                    call ce_her_head("...yes.","e") from _call_ce_her_head_65
                    g4 "Speak up, girl."
                    call ce_her_head("YES!","sl") from _call_ce_her_head_66
                    m "Details, girl."
                    call ce_her_head("He... he pushed me up against a wall.{p}Then he ground the dildo into my pussy.") from _call_ce_her_head_67
                    show screen genie_jerking_off
                    ">You start stroking your cock under the desk."
                    call ce_her_head("He... he said he always thought I was a slut.{p}and then kissed me.","n") from _call_ce_her_head_68
                    call ce_her_head("Oh god, I can still feel his tongue down my throat...","a") from _call_ce_her_head_69
                    call ce_her_head("He forced the dildo all the way in with the his palm.{p}I came so much I stained his shirt sleeve.","sl") from _call_ce_her_head_70
                    g9 "Then what?"
                    call ce_her_head("...","e") from _call_ce_her_head_71
                    g4 "Come on, girl, out with it."
                    call ce_her_head("I sucked him off.","v") from _call_ce_her_head_72
                    g9 "Oh you little bitch."
                    call ce_her_head("I felt the massive bulge when we were pressed up{p}against the wall, and he had helped me... you know...","sl") from _call_ce_her_head_73
                    g9 "Cum your brains out?"
                    call ce_her_head("Yes... I... Can I be honest with you sir?","na") from _call_ce_her_head_74
                    m "I hope so."
                    call ce_her_head("I wanted so desperately to taste it.","v") from _call_ce_her_head_75
                    g11 "YES!"
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen genie_jerking_sperm
                    ">You finally cum from the excitement of knowing what she's done."
                    call ce_her_head("Did you enjoy that, sir?","p") from _call_ce_her_head_76
                    hide screen genie_jerking_sperm
                    show screen genie
                    hide screen genie_jerking_off
                    g9 "Absolutely."
                    call ce_her_head("Good. Can I get paid now?") from _call_ce_her_head_77
                    m "Fifty points to gryffindor."
                    call ce_her_head("And sir...","pr") from _call_ce_her_head_78
                    call ce_her_head("You know I only said those things{p}because you wanted me to.{p}right?") from _call_ce_her_head_79
                    m "Whatever you say, Miss Granger."
                    call ce_her_head("I'm not that kind of girl, sir.") from _call_ce_her_head_80
                    call ce_her_head("Harry didn't really use your dildo on me...{p}I went to the bathroom and did it myself.") from _call_ce_her_head_81
                    g9 "Whatever the case, it was a wonderful story."
                    jump q7y8f5
            "\"Let her leave.\"":
                label q7y8f5:
                m "Well done Miss Granger."
                call ce_her_head("Thank you sir.","p") from _call_ce_her_head_82
                m "Fifty points to Gryffindor."
                $ gryffindor +=50
                call ce_her_head("Thank you sir,{p}now if you'll excuse me I need to lay down.") from _call_ce_her_head_83
                if whoring >= 18:
                    m "Where are you going?"
                    call ce_her_head("Sir?","q") from _call_ce_her_head_84
                    g4 "The dildo, girl."
                    call ce_her_head("Oh, right. Err... You see sir, it's stuck.","e") from _call_ce_her_head_85
                    m "Well I can help with..."
                    call ce_her_head("No need, sir.","h") from _call_ce_her_head_86
                    m "Miss Granger, I can't let you leave with my dildo."
                    call ce_her_head("...Please?","q") from _call_ce_her_head_87
                    m "Please what?"
                    call ce_her_head("...Please may I keep the dildo, sir?","sl") from _call_ce_her_head_88
                    g9 "Hm... Very well slut, as long as you walk back to Gryffindor tower with it inside you."
                    call ce_her_head("I was plan...") from _call_ce_her_head_89
                    call ce_her_head("Err... If you say so, sir.","na") from _call_ce_her_head_90
                hide screen bld1
                hide screen custom_event_h
                hide screen blktone
                hide screen hermione_02
                hide screen ctc
                with d3
                
                call her_walk(400,610,2) from _call_her_walk_96
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                with Dissolve(.3)
                
                call music_block from _call_music_block_15
                $ heretic_busy = False
                $ hermione_sleeping = True
                jump night_main_menu
                
    elif exposure >= 4 and exposure <=9: #Accidental Exposure
        m "Hello, Miss Granger."
        call ce_her_head("Hello sir.","pe") from _call_ce_her_head_91
        call ce_her_head("...") from _call_ce_her_head_92
        m "Well?"
        call ce_her_head("There's nothing to talk about.","pr") from _call_ce_her_head_93
        m "So spending an entire day with a dildo inside you is a normal day for you?"
        call ce_her_head("What am I supposed to say?") from _call_ce_her_head_94
        call ce_her_head("I went to class,{p}I ate with friends,{p}I tried to hide the giant rod between my legs.","h") from _call_ce_her_head_95
        m "Welcome to my world."
        call ce_her_head("Are you making fun of me, sir?","i") from _call_ce_her_head_96
        m "Not at the moment. Tell me, girl, did anybody notice?"
        if whoring <=15:
            call ce_her_head("Of course not. As soon as I left I cast a disillusionment charm on it.","d") from _call_ce_her_head_97
            m "What?"
            call ce_her_head("Well, they can't see something that's invisible, sir.") from _call_ce_her_head_98
        else:
            call ce_her_head("...","h") from _call_ce_her_head_99
            m "So, yes. Who and when."
            call ce_her_head("...I don't know his name, sir.{p}He was a first year who was tying his shoe while I walked by.","e") from _call_ce_her_head_100
            call ce_her_head("He...well he saw it.") from _call_ce_her_head_101
            m "What did this boy do?"
            call ce_her_head("He ran off. I think he was embarrassed.","pe") from _call_ce_her_head_102
            m "Is that all?"
            call ce_her_head("Yes, sir.","pr") from _call_ce_her_head_103
            call ce_her_head("I can be quite subtle if I want to be.","d") from _call_ce_her_head_104
            m "Not to mention dull."
        m "Did anything interesting happen to you today?"
        call ce_her_head("I did...Err...No, not really.","h") from _call_ce_her_head_105
        menu:
            "\"Press Her.\"":
                m "Come now, girl,you want to earn these points, right?"
                if whoring <= 17:
                    call ce_her_head("I got a perfect score on a herbology exam today.","p") from _call_ce_her_head_106
                    call ce_her_head("Which, isn't that surprising, but I was a bit...distracted.","na") from _call_ce_her_head_107
                    call ce_her_head("Not that you would care about my test scores...","i") from _call_ce_her_head_108
                    m "{size=-4}*Snoring*{/size}"
                    call ce_her_head("Professor!","s") from _call_ce_her_head_109
                    m "Hm? Wha? Right, uh... 50 points to Gryffindor."
                    $ gryffindor +=50
                    call ce_her_head("Good night, sir.","i") from _call_ce_her_head_110
                    
                    hide screen bld1
                    hide screen custom_event_h
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    
                    call her_walk(400,610,2) from _call_her_walk_97
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    with Dissolve(.3)
                    
                    call music_block from _call_music_block_16
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
                else:
                    call ce_her_head("...Well...{p}I have divination today, and it's all so dull.{p}Not to mention Professor Trelawney is a fraud.","i") from _call_ce_her_head_111
                    m "Get on with it, girl!"
                    call ce_her_head("...") from _call_ce_her_head_112
                    call ce_her_head("As I was saying, I was in divination class.") from _call_ce_her_head_113
                    call ce_her_head("Professor Trelawney was droning on about something or other.") from _call_ce_her_head_114
                    call ce_her_head("You have to understand, that room is very comfortable, sir.{p}It's only lit by candle light, the room is heavily incenced...","na") from _call_ce_her_head_115
                    call ce_her_head("And I was lounging among all those very soft pillows.","sl") from _call_ce_her_head_116
                    m "You didn't."
                    call ce_her_head("I think I did, sir.","p") from _call_ce_her_head_117
                    m "Hermione Granger masturbated in class?"
                    call ce_her_head("Only a bit.","sl") from _call_ce_her_head_118
                    call ce_her_head("It was quite easy, I only really had to rock back and forth.{p}The toy did the rest.") from _call_ce_her_head_119
                    m "Miss Granger, you certainly have come a long way."
                    call ce_her_head("I came quite a bit there as well.") from _call_ce_her_head_120
                    m "You delightful little slut, did you enjoy yourself?"
                    call ce_her_head("Sir, you shouldn't call your students sluts...","na") from _call_ce_her_head_121
                    call ce_her_head("I did. More than I expected actually...{p}Especially since I was sitting between Ron and Harry.","sl") from _call_ce_her_head_122
                    m "Did they notice?"
                    call ce_her_head("I have no idea.","n") from _call_ce_her_head_123
                    m "You hope they did, don't you?"
                    call ce_her_head("Of course not!{p}Fantasy is one thing, but if they actually noticed I would be mortified.","e") from _call_ce_her_head_124
                    jump q7y8f5
            "\"Let her leave\"":
                jump q7y8f5
    else: #Caught By Draco
        m "Good evening, Miss Granger."
        
        call heritic_event from _call_heritic_event_6
        show screen blktone
        call ce_her_main("","p_m",140) from _call_ce_her_main_95
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro from _call_heritic_intro_7
        
        m "My goodness, interesting day?"
        call ce_her_head("Can I just get paid, sir?","mash") from _call_ce_her_head_125
        m "You're going to have to do better than that."
        call ce_her_head("...Draco Malfoy.") from _call_ce_her_head_126
        m "What about him?"
        call ce_her_head("He's a Slytherin cretin, a racist, he's...","ma") from _call_ce_her_head_127
        call ce_her_head("He's a monster, sir.") from _call_ce_her_head_128
        m "What makes you say this, girl?"
        call ce_her_head("...","me") from _call_ce_her_head_129
        call ce_her_head("Please... I just want to be done with this, sir...","mash") from _call_ce_her_head_130
        menu:
            "\"Press Her\"":
                m "Once you tell me what happened, girl."
                if whoring >=21:
                    call ce_her_head("He molested me, Sir.","mash") from _call_ce_her_head_131
                    m "Oh?"
                    call ce_her_head("Coming out of potions class. He saw the... he saw me and decided to...") from _call_ce_her_head_132
                    m "Go on."
                    call ce_her_head("He brought me over to a secluded part of the dungeons.{p}He threatened to tell the whole school about...","mm") from _call_ce_her_head_133
                    call ce_her_head("He pushed me up against a wall...{p}and fucked me with the toy until my legs gave out.") from _call_ce_her_head_134
                    call ce_her_head("Then he made me... I had to play with myself for him.") from _call_ce_her_head_135
                    m "That's a fantastic idea! Masturbate while you tell me."
                    call ce_her_head("What?","me") from _call_ce_her_head_136
                    m "You heard me, girl. You're already full, make use of it."
                    call ce_her_head("Yes sir...","mn") from _call_ce_her_head_137
                    show screen genie_jerking_off
                    show screen hermione_03_b
                    call ce_her_head("I had to lick his shoes till they shined.") from _call_ce_her_head_138
                    call ce_her_head("The whole time he was calling me a mudblood...{p}and Gryffinwhore...") from _call_ce_her_head_139
                    call ce_her_head("After I did that,{p}he pulled me up by my hair and started jerking off in my face.") from _call_ce_her_head_140
                    m "Why didn't you suck him off, girl?"
                    call ce_her_head("...","me") from _call_ce_her_head_141
                    call ce_her_head("I tried to at first...","mash") from _call_ce_her_head_142
                    m "As I suspected, Miss Granger, you are truly a filty bitch."
                    call ce_her_head("I really tried! I just wanted it to be over.","mf") from _call_ce_her_head_143
                    call ce_her_head("But he told me my filthy muggle tongue{p}wasn't worthy to touch his perfect pureblood prick.") from _call_ce_her_head_144
                    m "You have to respect a man that uses alliteration to describe his cock."
                    call ce_her_head("It wasn't lost on me, Sir.","mn") from _call_ce_her_head_145
                    m "What next, girl?"
                    call ce_her_head("He made me stick out my tongue.","mash") from _call_ce_her_head_146
                    m "Show me."
                    call ce_her_head("...","mo") from _call_ce_her_head_147
                    m "Did he make you drink his cum?"
                    call ce_her_head("*nods*") from _call_ce_her_head_148
                    menu:
                        "\"Let her continue.\"":
                            m "Continue."
                            call ce_her_head("It was so degrading...","mn") from _call_ce_her_head_149
                            call ce_her_head("I had to swish it in my mouth for five minutes before he let me swallow it.","mb") from _call_ce_her_head_150
                            jump g67x8a384
                        "\"Make her drink your cum.\"":
                            m "Come over here, Miss Granger."
                            call ce_her_head("Sir...{p}If you expect me to suck your cock after a day like this...{p}you'll need to pay me tripple!","mf") from _call_ce_her_head_151
                            m "What? That's absurd!"
                            call ce_her_head("You try being huminiated by Draco Malfoy for hours!{p}See if you're up for being facefucked!") from _call_ce_her_head_152
                            label g67x8a384:
                            m "That's enough for now, girl. Fifty points to Gryffindor."
                            $ gryffindor +=50
                            call ce_her_head("Thank you sir.","me") from _call_ce_her_head_153
                            hide screen genie_jerking_off
                            hide screen hermione_03_b
                            hide screen bld1
                            hide screen custom_event_h
                            hide screen blktone
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            
                            call her_walk(400,610,2) from _call_her_walk_98
                            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                            with Dissolve(.3)
                            
                            call music_block from _call_music_block_17
                            $ heretic_busy = False
                            $ hermione_sleeping = True
                            jump night_main_menu
                elif whoring >=18 and whoring <=20:
                    call ce_her_head("We were in potions class, and he must have noticed the dildo...","me") from _call_ce_her_head_154
                    call ce_her_head("All of a sudden it just starts vibrating.","mash") from _call_ce_her_head_155
                    call ce_her_head("I know that son of a deatheater was behind it.","mf") from _call_ce_her_head_156
                    m "What else, Miss Granger?"
                    call ce_her_head("Err...do I have to, sir.","me") from _call_ce_her_head_157
                    m "Yes."
                    call ce_her_head("...He started fucking me.","mm") from _call_ce_her_head_158
                    m "What?"
                    call ce_her_head("With the dildo. Right in the middle of class.") from _call_ce_her_head_159
                    call ce_her_head("I tried to stop him...but...","mn") from _call_ce_her_head_160
                    m "You must not have tried that hard."
                    call ce_her_head("I couldn't focus, sir. I would have stopped him if I could.","me") from _call_ce_her_head_161
                    m "What next, Miss Granger"
                    call ce_her_head("I was trying not to draw any attention to myself.","mm") from _call_ce_her_head_162
                    call ce_her_head("Professor Snape called on me though...{p}I had to try to recite the recepie for Wingot's Elixer while...") from _call_ce_her_head_163
                    m "While Mr. Malfoy was fucking you with a dildo."
                    call ce_her_head("...") from _call_ce_her_head_164
                    m "Well?"
                    call ce_her_head("...I came halfway through.","mn") from _call_ce_her_head_165
                    m "You're a nasty little slut, Miss Granger."
                    call ce_her_head("It wasn't... I couldn't help it!","me") from _call_ce_her_head_166
                    call ce_her_head("He was, err, I mean it was...","mn") from _call_ce_her_head_167
                    m "Just admit it Miss Granger, admit you liked it."
                    call ce_her_head("I'll never admit it!","me") from _call_ce_her_head_168
                    call ce_her_head("Err, I mean it was criminal! I want to press charges!","ma") from _call_ce_her_head_169
                    m "Do you mean that, Miss Granger?"
                    call ce_her_head("Sir, Draco Malfoy raped me in the middle of a classroom.","mf") from _call_ce_her_head_170
                    call ce_her_head("{size=+3}I demand justice!{/size}") from _call_ce_her_head_171
                    m "Well if you really feel that way I'll just call him up to the office and we'll sort this whole thing out."
                    call ce_her_head("Err... No, that's alright sir.","me") from _call_ce_her_head_172
                    m "Are you sure? You did just demand justice, Miss Granger."
                    call ce_her_head("Well... I'll get justice some other way.","ma") from _call_ce_her_head_173
                    m "Should we keep up this charade, or do you just want to get paid?"
                    call ce_her_head("...Just pay me, sir.","me") from _call_ce_her_head_174
                    jump q7y8f5
                else:
                    call ce_her_head("I just... I can't sir.","mm") from _call_ce_her_head_175
                    $ mad += 5
                    hide screen bld1
                    hide screen custom_event_h
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    
                    call her_walk(400,610,2) from _call_her_walk_99
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    with Dissolve(.3)
                    
                    call music_block from _call_music_block_18
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
            "\"Let her leave.\"":
                jump q7y8f5
