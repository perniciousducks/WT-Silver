

### Let Classmate Molest Her ###

##(Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label hg_pr_ClassmateTouchYou:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_ClassmateTouchYou_OBJ.points < 1:
        m "{size=-4}(Tell her to go get touched by one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    call bld from _call_bld_14
    
    #Intro.
    if hg_pr_ClassmateTouchYou_OBJ.points == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="right",ypos="base") from _call_her_main
        m "You do like boys your age, don't you?"
        call her_main("...?","normal","base") from _call_her_main_1
        m "one of your classmates maybe?"
        call her_main("Well...","open","worriedL") from _call_her_main_2
        her "Must I really discuss things like this with you, [genie_name]?"
        call her_main("It's a bit embarrassing...","annoyed","worriedL") from _call_her_main_3
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, [hermione_name]."
        m "Go confront that boy you fancy. The one you think is \"just so dreamy\"..."
        call her_main(".......?","open","base") from _call_her_main_4
        m "And let him touch you..."

        if whoring < 6 or hg_pr_FlirtTeacher_OBJ.points < 2: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much

        call her_main("Let him... touch me, [genie_name]?","open","base") from _call_her_main_5
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, [hermione_name]? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        call her_main("\"The talk\", [genie_name]?","angry","worriedCl",emote="05") from _call_her_main_6
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that  \"pee-pee\" in their mouths?"
        call her_main("!!!","normal","base") from _call_her_main_7
        call her_main("What kind of demented parent would have such a talk with their child?","angry","angry") from _call_her_main_8
        m "I bet Akabur would."
        call her_main("I beg your parodon, [genie_name]?","annoyed","suspicious") from _call_her_main_9
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, [hermione_name]."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        call her_main("..........","annoyed","angryL") from _call_her_main_10
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        call her_main("How many points would I receive after completing such a task, [genie_name]?","disgust","glance") from _call_her_main_11
        m "Hm... Twenty five should do..."
        call her_main("Twenty five house points...","annoyed","angryL") from _call_her_main_12
        her "...."
        call her_main("Well, so be it then...","disgust","glance") from _call_her_main_13
        m "Great..."
        call her_main("I'd better go now. The classes are about to start...","angry","angry") from _call_her_main_14

    #Second time event.
    else:
        if whoring >= 6 and whoring < 9: # LEVEL 03 
            m "[hermione_name]?"
            call her_main("[genie_name]?","base","base",xpos="right",ypos="base") from _call_her_main_15
            m "How about you go let one of your classmates molest you a little again?"
            call her_main("........","upset","closed") from _call_her_main_16
            m "Twenty five house points, [hermione_name]."
            call her_main("[genie_name], it's just...","annoyed","angryL") from _call_her_main_17
            call her_main("I do not understand why I must do things like that...","annoyed","annoyed") from _call_her_main_18
            m "To help out your house?"
            call her_main("That's not what I meant...","disgust","glance") from _call_her_main_19
            call her_main("Oh, never mind...","annoyed","angryL") from _call_her_main_20
            her "The classes are about to start, I'd better go..."
            m "Will you do it?"
            call her_main("I don't know... Maybe...","disgust","glance") from _call_her_main_21

        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "[hermione_name], I need you to go out there, and make one of your classmates molest you a little."
            call her_main("I understand, [genie_name]...","base","base",xpos="right",ypos="base") from _call_her_main_22
            m "Off you go then."
            her "..........."

        elif whoring >= 12: # LEVEL 05+
            m "[hermione_name], I need you to go out there..."
            m "Find a handsome guy and force yourself on him!"
            call her_main("You mean like...","base","base",xpos="right",ypos="base") from _call_her_main_23
            call her_main("In a sexual way, [genie_name]?","angry","wink") from _call_her_main_24
            m "What? No, I mean just let him get under your uniform that's all..."
            call her_main("Oh, I see...","grin","worriedCl",emote="05") from _call_her_main_25
            call her_main("I wonder who it should be this time...","grin","baseL") from _call_her_main_26
            call her_main("More than one boy, is not a problem, is it, [genie_name]?","angry","base") from _call_her_main_27
            m "A problem? Of course not!"
            m "If anything - it is encouraged." 
            call her_main("Great. I will see you after the classes then, [genie_name]. As usual.","angry","wink") from _call_her_main_28
            m "Yes. Good luck."
    
    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
    

label hg_pr_ClassmateTouchYou_complete:

    call play_sound("door") from _call_play_sound #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk
    call bld from _call_bld_15
    

    #First time event.
    call her_main("Good evening, [genie_name].","base","base",xpos="right",ypos="base") from _call_her_main_29
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "Give me the details."
            show screen blktone
            
            if whoring >= 6 and whoring < 9: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                call her_main("......","annoyed","angryL") from _call_her_main_30
                call her_main("Well... Em...","soft","baseL") from _call_her_main_31
                m "Speak up, [hermione_name]."
                m "Did you let some lucky guy feel you up or what?"
                    
                #Event A
                if one_out_of_three == 1:
                    her "I did, [genie_name]..."
                    m "So? Tell me more."
                    her "Well, there is not much to tell..."
                    call her_main("I told that one guy I know that he could touch me a little if he wants...","open","base") from _call_her_main_32
                    call her_main("He thought I was joking at first...","annoyed","worriedL") from _call_her_main_33
                    call her_main("So embarrassing...","normal","worriedCl") from _call_her_main_34
                    m "So, did he cop a feel or not?"
                    call play_music("playful_tension") from _call_play_music# SEX THEME.
                    call her_main("He did...","normal","worriedCl") from _call_her_main_35
                    m "Well, where did he touch you, [hermione_name]?"
                    call her_main("Ehm... My legs...","annoyed","worriedL") from _call_her_main_36
                    her "And my breasts a little I suppose..."
                    m "That's all?"
                    call her_main("Yes, [genie_name]...","open","base") from _call_her_main_37
                    call her_main("It's getting late... I think I'd better leave now...","normal","worriedCl") from _call_her_main_38
                    call her_main("I'm sorry, [genie_name]...","angry","worriedCl",emote="05") from _call_her_main_39
                    m "Nothing to be sorry about, [hermione_name]."
                    m "You did good. This will do for now."
                    
                #Event B
                elif one_out_of_three == 2:
                    stop music fadeout 3.0
                    call her_main("I did, [genie_name].","annoyed","angryL") from _call_her_main_40
                    her "But it was all very awkward and embarrassing..."
                    m "That's the whole point of it, [hermione_name]."
                    m "Tell me where you were touched today..."
                    call play_music("playful_tension") from _call_play_music_1# SEX THEME.
                    her "Ehm..."
                    call her_main("Well he touched me under my skirt a little...","angry","base") from _call_her_main_41
                    her "Then I let him rub my..."
                    call her_main("...my pussy through the panties, [genie_name].","angry","down_raised") from _call_her_main_42
                    m "Very good. Then what happened?"
                    call her_main("Then he sort of started to touch himself [genie_name]...","open","worriedCl") from _call_her_main_43
                    her "So, I decided to leave..."
                    m "I see..."
                    call her_main(".............","normal","worriedCl") from _call_her_main_44
                    
                #Event C
                elif one_out_of_three == 3:
                    her "I did, [genie_name]..."
                    call play_music("playful_tension") from _call_play_music_2# SEX THEME.
                    call her_main("I led this one guy from \"Hufflepuff\" to an empty classroom and I told him that he can touch me if he wants.","open","base") from _call_her_main_45
                    her "That I don't mind..."
                    call her_main("...........","annoyed","worriedL") from _call_her_main_46
                    m "And?"
                    call her_main("Well, he did touch me a little at first...","open","base") from _call_her_main_47
                    call her_main("......","normal","worriedCl") from _call_her_main_48
                    m "Don't make me pull every word out of you, [hermione_name]!"
                    m "Then what happened?"
                    call her_main("Well...","open","down") from _call_her_main_49
                    stop music fadeout 1.0
                    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
                    call her_main("He asked me to call him a \"sissy boy\"...","upset","wink") from _call_her_main_50
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("And he kept on reassuring me that he has a very small penis...","open","base") from _call_her_main_51
                    call her_main("He just kept repeating that *sob!*...","angry","base",tears="soft") from _call_her_main_52
                    call her_main("Why would anyone be like this?","angry","base",tears="soft") from _call_her_main_53
                    her "*Sob!* I Could not stay in his company a moment longer, so I just ran."
                    m "I'm sorry to hear this..."
                    call her_main("It was truly awful, [genie_name]...","angry","base",tears="soft") from _call_her_main_54
                    m "There, there..."
                    call her_main("*Sob!*","normal","baseL",tears="soft") from _call_her_main_55
                    m "Will ten extra points make you feel better?"
                    call her_main("Huh? That would be very sweet of you [genie_name].","soft","base",tears="soft") from _call_her_main_56
                    m "Of course... Ten extra points to \"Gryffindor\"."
                    call her_main("Thank you [genie_name]...","clench","worried",cheeks="blush",tears="soft") from _call_her_main_57
                    m "And the rest of your payment..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                    
                #Event A
                if one_out_of_three == 1:
                    call her_main("Well... There is not much to tell...","open","closed") from _call_her_main_58
                    her "I found this one boy from \"Ravenclaw\"..."
                    her "Led him to one of the empty classrooms in the eastern wing..."
                    her "He thought I wanted to make out with him..."
                    her "But I told him that I just want him to touch me..."
                    call her_main("...so he did.","normal","worriedCl") from _call_her_main_59
                    m "I see..."
                    m "Well done, [hermione_name]."
                    call her_main("Will I be getting my points now?","upset","wink") from _call_her_main_60
                    m "In a minute, [hermione_name]. I have a question I would like to ask you before that."
                    call her_main("???","open","base") from _call_her_main_61
                    m "Did you enjoy it?"
                    m "Did it feel good to be touched by that boy?"
                    call her_main("Oh...","open","closed") from _call_her_main_62
                    her "Well, he was rather handsome I suppose..."
                    call her_main("I didn't hate it, if that's what you mean, [genie_name]...","upset","closed") from _call_her_main_63
                    m "I see..."
                    
                #Event B
                elif one_out_of_three == 2:
                    call her_main("Well...","open","closed") from _call_her_main_64
                    her "I'm not sure whether or not this counts, but..."
                    her "During the herbology class today..."
                    call her_main("I let this one boy slide his hand under my skirt...","upset","wink") from _call_her_main_65
                    her "So while Professor Sprout explained the differences between \"mandrake\" and \"mandragore\"..."
                    call her_main("Something I already knew of course...","open","suspicious") from _call_her_main_66
                    call her_main("I let my lab partner massage my buttocks...","upset","wink") from _call_her_main_67
                    her "And that is all..."
                    m "Hm..."
                    menu:
                        "\"You can do better than that, [hermione_name].\"":
                            call her_main("Yes, I know, [genie_name]. I am sorry.","open","base") from _call_her_main_68
                            m "Just make sure you try harder next time."
                            her "I will, [genie_name]."
                        "\"Kudos on doing this during class.\"":
                            call her_main("Thank you, [genie_name].","base","happyCl") from _call_her_main_69
                            m "I say you deserve to get paid."
                    
                #Event C
                elif one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main(".................","annoyed","angryL") from _call_her_main_70
                    m "???"
                    call play_music("playful_tension") from _call_play_music_3# SEX THEME.
                    call her_main("I don't want to talk about it, [genie_name]...","annoyed","angryL") from _call_her_main_71
                    m "What happened, [hermione_name]. Spit it out."
                    call her_main(".................","annoyed","annoyed") from _call_her_main_72
                    call her_main("But... it's so embarrassing...","open","base") from _call_her_main_73
                    call her_main("Do I really have to, [genie_name]?","normal","worriedCl") from _call_her_main_74
                    m "Yes, I happen to love embarrassing things!"
                    call her_main(".................","annoyed","angryL") from _call_her_main_75
                    her "Well, alright..."
                    her "I approached this one guy that I always found attractive..."
                    her "Managed to muster up enough courage to ask him to follow me..."
                    call her_main("Normally I wouldn't dare...","open","base") from _call_her_main_76
                    her "But the fact that I was doing this as a task entrusted to me by someone else..."
                    her "made it easier somehow..."
                    m "Happy to help, [hermione_name]."
                    call her_main("I led him to the library...","open","down") from _call_her_main_77
                    her "We found a secluded spot behind one of the book shelves..."
                    her "And I told him that he can touch me wherever he wants..."                 
                    her "And...."
                    call her_main("..........","clench","down_raised") from _call_her_main_78
                    m "What?"
                    call her_main(".....................","normal","worriedCl") from _call_her_main_79
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("He started to touch my... feet, [genie_name].","scream","worriedCl") from _call_her_main_80
                    m "Huh?"
                    m "Your \"Feet\"? Is that what kids call tits these days?"
                    call her_main("I'd wish, [genie_name]...","disgust","glance") from _call_her_main_81
                    her "He asked me to take off my shoes..."
                    her "Then he..."
                    call her_main("He started to smell my toes, [genie_name]!","angry","base",tears="soft") from _call_her_main_82
                    call her_main("I felt so... violated!","angry","base",tears="soft") from _call_her_main_83
                    m "So he didn't touch your tits, or your butt?"
                    call her_main("No, [genie_name]... *sob!*","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_84
                    m "Alright, then what happened?"
                    call her_main("Nothing! I couldn't bear the humiliation... I just ran...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_85
                    her "I even left my shoes behind and had to come back later to pick them up..."
                    call her_main("*Sob!*............","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_86
                    m "Hm..."
                    m "Well, you did get molested..."
                    m "Although in a rather unconventional manner..."
                    call her_main("*Sob!* I wish he would have just touched my breasts like a descent boy would, [genie_name]... *Sob!*","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_87
                    m "There, there..."
                    m "You earned you pay today..."
            
            elif whoring >= 12: # LEVEL 05+
                    
                #Event A
                if one_out_of_three == 1:
                    stop music fadeout 1.0
                    call her_main("......","annoyed","worriedL") from _call_her_main_88
                    call her_main("Well...","open","base") from _call_her_main_89
                    her "During the potions class today..."
                    her "I wrote a note on a piece of paper..."
                    her "I was about to slide it to my lab partner when..."
                    call play_music("chipper_doodle") from _call_play_music_4 # HERMIONE'S THEME.
                    call her_main("Professor Snape snatched it right out of my hand...","annoyed","angryL") from _call_her_main_90
                    call her_main("He then read it out loud before the entire class...","annoyed","annoyed") from _call_her_main_91
                    m "What did the note say?"
                    call her_main("Well...","open","down") from _call_her_main_92
                    her "It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\""
                    call her_main("Everyone was laughing...","angry","down_raised") from _call_her_main_93
                    her "It was so embarrassing I wanted to die..."
                    call her_main("I really hate professor Snape, [genie_name]...","angry","angry") from _call_her_main_94
                    m "What happened then?"
                    call her_main("Nothing...","open","down") from _call_her_main_95
                    
                    call play_music("playful_tension") from _call_play_music_5# SEX THEME.
                    hide screen hermione_main
                    with d3
                    $ sc34CG(2, 19, 6, 5)
                    
                    call her_main("But when the class was over...",xpos="base",ypos="base") from _call_her_main_96
                    call her_main("These two nasty-looking boys from \"Slytherin\" cornered me...") from _call_her_main_97
                    call her_main("Actually they weren't mean to me or anything...") from _call_her_main_98
                    call her_main("So we just waited for everyone to leave the classroom...") from _call_her_main_99
                    $ sc34CG(2, 16, 6, 9)
                    call ctc from _call_ctc
                    
                    call her_main("And then I let them touch me...","angry","base") from _call_her_main_100
                    $ sc34CG(2, 17, 6, 9)
                    call her_main("They touched me everywhere, [genie_name]...") from _call_her_main_101
                    m "\"Everywhere\", huh?"
                    call her_main("Yes... Everywhere, [genie_name]...","soft","ahegao") from _call_her_main_102
                    call her_main("There were hands under my skirt, under my shirt...","base","glance") from _call_her_main_103
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("And then I started to breathe heavily...") from _call_her_main_104
                    call her_main("So one of them just put his hand over my mouth...","soft","ahegao") from _call_her_main_105
                    her "And their hands were so... thorough..." 
                    $ sc34CG(2, 17, 6, 9)
                    call her_main("My head started to spin...") from _call_her_main_106
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("It was most exhilarating, [genie_name].","base","glance") from _call_her_main_107
                    m "Very good, [hermione_name]. Very good indeed."
                    
                    hide screen sccg
                    call her_main(xpos="right",ypos="base",trans="fade") from _call_her_main_108
                    
                #Event B
                if one_out_of_three == 2:
                    call her_main("Actually something quite unexpected happened to me today, [genie_name]...","base","base") from _call_her_main_109
                    her "Right after the Defence Against the Dark Arts class..."
                    her "This stocky \"Hufflepuff \" boy came up to me..."
                    call play_music("playful_tension") from _call_play_music_6# SEX THEME.
                    call her_main("He said someone told him that I let boys touch me...","angry","wink") from _call_her_main_110
                    call her_main("Normally I would deny everything...","base","glance") from _call_her_main_111
                    her "But I decided not to waste the opportunity..."
                    call her_main("I took the boy to a quiet spot and let him touch me...","base","ahegao_raised") from _call_her_main_112
                    her "I let him run his hands up and down my thighs..."
                    her "I let him fondle my breasts..."
                    call her_main("All the usual things...","base","glance") from _call_her_main_113
                    m "Well done, [hermione_name]."
                    
                #Event C
                if one_out_of_three == 3:
                    stop music fadeout 1.0
                    call her_main("Well...","upset","wink") from _call_her_main_114
                    her "I did what you told me to do, [genie_name]..."
                    her "But... it sort of... ehm..."
                    call her_main("Well, it sort of escalated into something else...","base","ahegao_raised") from _call_her_main_115
                    call play_music("playful_tension") from _call_play_music_7# SEX THEME.
                    m "Hm?"
                    call her_main("uhm...","upset","wink") from _call_her_main_116
                    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
                    m "You got caught? By one of the teachers?"
                    call her_main("No, [genie_name]...","base","base") from _call_her_main_117
                    call her_main("By the boy's girlfriend...","smile","baseL") from _call_her_main_118
                    m "Interesting..."
                    call her_main("She was furious with him at first...","angry","base") from _call_her_main_119
                    call her_main("But then...","angry","wink") from _call_her_main_120
                    call her_main("Ehm... She started to touch my breasts as well...","base","down") from _call_her_main_121
                    call her_main("Almost the same way her boyfriend did just a moment ago...","smile","angry") from _call_her_main_122
                    her "Then she turned to him and she said..."
                    call her_main("\"I love you baby, and I want to share everything with you...\"","open","closed") from _call_her_main_123
                    her "\"...And that includes your whores.\""
                    call her_main("I did not appreciate being called a whore of course...","angry","base") from _call_her_main_124
                    call her_main("But that was such a sweet and romantic gesture...","base","base") from _call_her_main_125
                    her "Wouldn't you agree, [genie_name]?"
                    m "Totally..."
                    m "Seems that true love {size=+5}does{/size} exist after all."
                    m "Then what happened?"
                    call her_main("Ehm... Well, they kissed of course...","grin","worriedCl",emote="05") from _call_her_main_126
                    call her_main("And then they both started to touch me again...","upset","wink") from _call_her_main_127
                    call her_main("And then he was kind of only touching her and she was only touching him...","annoyed","worriedL") from _call_her_main_128
                    her "And they kissed..."
                    her "I suddenly felt like the third wheel in that situation, so I just slipped away quietly..."
                    m "I see..."
    
    $ gryffindor +=25
    m "The \"Gryffindor\" house gets 25 points!"
    her "Thank you, [genie_name]."
    
    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    $ hg_pr_ClassmateTouchYou_OBJ.points += 1
    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = False
    
    if hg_pr_ClassmateTouchYou_OBJ.points >= 2:
        $ hg_pr_ClassmateTouchYou_OBJ.complete = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
    
