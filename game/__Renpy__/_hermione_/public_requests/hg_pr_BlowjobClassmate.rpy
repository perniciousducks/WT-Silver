

### Give Classmate A Blowjob ###

##(Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label hg_pr_BlowjobClassmate: #LV.7 (Whoring = 18 - 20)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_BlowjobClassmate_OBJ.points < 1:
        m "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                call nar("!!! Attention !!!","start") from _call_nar_552
                ">Continuing on this path will lock your game to a specific ending."
                call nar(">You might want to save you game here.","end") from _call_nar_553

                menu:
                    "Do you wish to continue?"
                    "\"(Yes, continue!)\"":
                        pass
                    "\"(No, return.)\"":
                        jump silver_requests

            "\"(Not right now.)\"":
                jump silver_requests

    call bld from _call_bld_103
    
    #Intro.
    if hg_pr_BlowjobClassmate_OBJ.points == 0:
        m "[hermione_name], I will be buying another favour from you today."
        call her_main("Thank you, [genie_name]. I really appreciate it.","open","closed",xpos="right",ypos="base") from _call_her_main_5090
        m "Sure, Happy to help."
        m "I need you to go give a blowjob to one of your classmates."
        stop music fadeout 1.0
        call her_main("!!!","shock","wide") from _call_her_main_5091
        her "...with my mouth?"

        if whoring < 18 or hg_pr_HandjobClassmate_OBJ.points < 2:
            jump too_much

        call play_music("chipper_doodle") from _call_play_music_191 # HERMIONE'S THEME.
        m "Yes, that's how it's usually done..."
        call her_main("[genie_name], I...","upset","closed") from _call_her_main_5092
        call her_main("I refuse to sell you a depraved favour like that, [genie_name].","open","annoyed",cheeks="blush") from _call_her_main_5093
        call her_main("Can't I just kiss another girl instead?","open","worriedCl") from _call_her_main_5094
        her "I do not mind that..." 
        m "[hermione_name], please stop wasting my time..."
        m "If you are not in the mood to sell favours today..."
        m "Then there is the door."
        call her_main("But I need the points, [genie_name]. You know that.","upset","closed") from _call_her_main_5095
        m "It's as the saying goes, [hermione_name]..."
        m "\"If you won't suck a dick for it - you don't need it.\""
        call her_main("Tch...","angry","angry",cheeks="blush") from _call_her_main_5096
        her "............................"
        m ".........................................."
        call her_main("...alright.","annoyed","angryL") from _call_her_main_5097
        her "I'll do it..."
        m "Go do it, then!"
        m "Report back to me after your classes."
        call her_main("...","angry","angry",cheeks="blush") from _call_her_main_5098
        her "....."
        her "......."
        m "You may leave, [hermione_name]."
        her "..."
    
    #First and second time event.
    else:

        #First time event.
        if whoring >= 18 and whoring < 21:
            m "Go give some lucky boy another blowjob, [hermione_name]."
            call her_main("......Again?","disgust","glance",xpos="right",ypos="base") from _call_her_main_5099
            m "Yes, again."
            call her_main("..........","annoyed","annoyed") from _call_her_main_5100

        #Second time event.
        elif whoring >= 21:
            call play_music("chipper_doodle") from _call_play_music_192 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Do you believe in horoscopes?"
            call her_main("Not even a little bit, [genie_name]...","annoyed","angryL",xpos="right",ypos="base") from _call_her_main_5101
            m "Well, maybe you should..."
            call her_main("...?","open","base") from _call_her_main_5102
            m "Because I got yours right here and it says..."
            m "\"Dedicate today to something you do well\"..."
            call her_main("Something I do well...?","soft","baseL") from _call_her_main_5103
            m "Go suck on some cocks, [hermione_name]."
            call her_main(".....................","annoyed","annoyed") from _call_her_main_5104 # :(
            m "Report back to me after your classes as usual..."
            call her_main("Of course...","annoyed","angryL") from _call_her_main_5105
    
    $ hg_pr_BlowjobClassmate_OBJ.inProgress = True
    
    jump hg_pr_transition_block

    
label hg_pr_BlowjobClassmate_complete:

    call play_sound("door") from _call_play_sound_183 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_110
    call bld from _call_bld_104
    

    #First time event.
    if whoring >= 18 and whoring < 21: 

        #Event A
        if one_out_of_three == 1: ### EVENT (A)
            call play_music("chipper_doodle") from _call_play_music_193 # HERMIONE'S THEME.
            m "You know the drill, [hermione_name]. Start talking."
            show screen blktone
            call her_main("I have completed your task, [genie_name].","disgust","glance",xpos="right",ypos="base") from _call_her_main_5106
            m "Good. Tell me more."
            call her_main("What is there to tell, [genie_name]?","annoyed","angryL") from _call_her_main_5107
            her "I sucked off one of my classmates today..."
            her "And that's it..."
            m "Hm... I see..."
            m "..............."
            call her_main("....................................","angry","down_raised") from _call_her_main_5108
            m "Did you swallow?"
            call her_main("...........................","annoyed","annoyed") from _call_her_main_5109
            m "[hermione_name], did you swallow the load properly?"
            call her_main("Yes I did, [genie_name].","angry","angry") from _call_her_main_5110
            m "Well, I suppose that will do for now..."
        
        #Event B
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            call her_main("[genie_name], I...","angry","down_raised",xpos="right",ypos="base") from _call_her_main_5111
            her "I tried, but..."
            call her_main("The boy turned me down, [genie_name]...","mad","worried",tears="soft") from _call_her_main_5112
            call her_main("I cannot believe that actually happened...","angry","base",tears="soft") from _call_her_main_5113
            her "I am one of the top students in this school!"
            her "One of the most popular ones too..."
            call her_main("And he turns me down?","angry","angry",tears="soft") from _call_her_main_5114
            her "Why would he insult me like that?!"
            m "So you're insulted because that boy refused to put his cock in your mouth?"
            call her_main("Wouldn't you be, [genie_name]?","angry","angry",tears="crying") from _call_her_main_5115
            m "I think I would get over it rather quickly..."
            call her_main("He rejected me [genie_name]...","angry","angry",cheeks="blush") from _call_her_main_5116
            her "Who does he think he is?!"
            call her_main("With all due respect, [genie_name], you wouldn't understand...","open","annoyed",cheeks="blush") from _call_her_main_5117
            m "Well, in any case. I can't pay you for this."
            call her_main("Of course... I would not expect you to, [genie_name].","annoyed","annoyed",tears="soft") from _call_her_main_5118
            her "I failed to complete my task and deserve no praise of any kind..."
            her "And should you pay me out of pity..."
            call her_main("Then That would only worsen the insult...","annoyed","angryL") from _call_her_main_5119
            m "Hm... In that case, maybe I should pay you anyway..."
            call her_main("No, [genie_name]. I would not accept it...","annoyed","annoyed") from _call_her_main_5120
            m "Hm... Well, this will be all then."
            her "Have a good night, [genie_name]."
            hide screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3 

            $ display_h_tears = False
            
            $ hg_pr_BlowjobClassmate_OBJ.inProgress = False
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
        
        #Event C
        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("I still find the idea of selling a favour like this appalling, [genie_name].","annoyed","angryL",xpos="right",ypos="base") from _call_her_main_5121
            call her_main("But other than that it well surprising well...","annoyed","annoyed") from _call_her_main_5122
            call play_music("playful_tension") from _call_play_music_194# SEX THEME.
            her "I gave a proper blowjob to this handsome boy from \"Ravenclaw\"..."
            call her_main("And he was such a gentleman about it...","open","down") from _call_her_main_5123
            call her_main("He even warned me when he was about to cum.","angry","down_raised") from _call_her_main_5124
            m "A true gentleman indeed."
            m "Did you swallow?"
            call her_main("Of course I did, [genie_name].","upset","closed") from _call_her_main_5125
            her "I told you - I gave the boy a proper blowjob."
            call her_main("The least I could do for someone who treated me with respect for a change...","angry","down_raised") from _call_her_main_5126
            m "Well, in that case."
            
    #Second Event.
    if whoring >= 21: # LEVEL 08 =+               
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            $ u_tears_pic = "characters/hermione/face/tears_03.png"
            $ display_h_tears = True
            $ aftersperm = True
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"

            show screen blktone
            call her_main("","angry","angry",xpos="right",ypos="base") from _call_her_main_5127
            call ctc from _call_ctc_306

            m "[hermione_name]..."
            m "You look like hell..."
            call play_music("chipper_doodle") from _call_play_music_195 # HERMIONE'S THEME.
            call her_main("[genie_name], I have been raped.","scream","angryCl") from _call_her_main_5128
            m "Seriously?"
            call her_main("Yes, [genie_name].","annoyed","annoyed") from _call_her_main_5129
            her "That nasty boy from \"Slytherin\" raped me..."
            call her_main("Or raped my face rather I suppose...","open","down") from _call_her_main_5130
            her "And--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","shock","worriedCl") from _call_her_main_5131
            call her_main("Excuse me.","angry","down_raised") from _call_her_main_5132
            call her_main("He came so much I was barely able to swallow it all...","scream","angry",emote="01") from _call_her_main_5133
            her "Bloody bastard!"
            call her_main("You think I could file a complaint, [genie_name]?","angry","angry",cheeks="blush") from _call_her_main_5134
            m "Hm... I suppose..."
            m "But keep in mind that the moment we bring the ministry into this..."
            m "All this \"favour selling business\" will have to stop immediately."
            call her_main("Oh...?","open","baseL",cheeks="blush") from _call_her_main_5135
            her ".................."
            call her_main("Please, never mind what I just said then...","base","happyCl") from _call_her_main_5136
            m "Are you sure? You look pretty messed up."
            her "No, no. It's nothing really..."
            her "After all I was the one who offered him a free blowjob..."
            her "He just got a bit rough with me closer to the end, that's all..."
            her "I think I am just overreacting..."
            m "I see..."
            her "Can I just--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","shock","wide") from _call_her_main_5137
            call her_main("Excuse me, [genie_name].","angry","down_raised") from _call_her_main_5138
            call her_main("{size=-3}(He just kept on cumming... My stomach feels so full...){/size}","angry","worriedCl",emote="05") from _call_her_main_5139
            call her_main("Can I get my payment now, please?","open","base") from _call_her_main_5140
        
        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass

            stop music fadeout 1.0
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_10.png"

            show screen blktone
            call her_main("","base","ahegao_raised",xpos="right",ypos="base") from _call_her_main_5141
            call ctc from _call_ctc_307

            her "Good evening, [genie_name]..."
            g4 "[hermione_name]?!"
            g4 "What happened to you, [hermione_name]?"
            g4 "All I asked you to do was to give a blowjob to one of your classmates."
            call play_music("playful_tension") from _call_play_music_196# SEX THEME.
            call her_main("That... that was exactly what I did, [genie_name].","angry","down_raised") from _call_her_main_5142
            m "[hermione_name], you are covered in cum head to toe."
            call her_main("I am?","soft","ahegao") from _call_her_main_5143
            her "Oh... Did I forget to clean myself up?"
            call her_main("How embarrassing...","base","glance") from _call_her_main_5144
            her "That thing at the boy's restroom sort of escalated I suppose..."
            her "Before I knew what happened I was surrounded with hard throbbing cocks..."
            call her_main("Oh... Just talking about it makes me shiver with excitement... err..","silly","dead") from _call_her_main_5145
            call her_main("...I mean, with fear... no, not fear...","grin","ahegao") from _call_her_main_5146
            call her_main("Embarrassment?","base","baseL",cheeks="blush") from _call_her_main_5147
            m "Are you asking me?"
            call her_main("Oh, excuse me, [genie_name]... I feel a little lightheaded...","grin","dead") from _call_her_main_5148
            her "I think I need to go lie down for a while..."
            m "Don't forget to take a shower first."
            call her_main("A shower? Why?","base","glance") from _call_her_main_5149
            m "Never mind..."
            show screen ctc
            pause
            hide screen ctc
        
        #Event C
        elif one_out_of_three == 3:
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.

            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("Splendid, [genie_name]. Simply splendid.","base","happyCl",xpos="right",ypos="base") from _call_her_main_5150
            m "Really? Do tell."
            call play_music("playful_tension") from _call_play_music_197# SEX THEME.
            call her_main("Today I did something I wanted to do for such a long time now...","base","ahegao_raised") from _call_her_main_5151
            her "But never could muster up enough courage for..."
            m "Hm..?"
            call her_main("Today I sucked off my two best friends in the entire world!","soft","ahegao") from _call_her_main_5152
            call her_main("And it was every bit as exciting as I thought it would be.","base","down") from _call_her_main_5153
            call her_main("I made their cocks all sloppy with saliva...","grin","dead") from _call_her_main_5154
            her "I sucked on their balls too..."
            call her_main("But the best part was to see their faces...","silly","ahegao") from _call_her_main_5155
            her "The boys could not believe it was actually happening..."
            call her_main("To be honest, neither could I...","silly","dead") from _call_her_main_5156
            her "I, Hermione granger - the girl they knew for years..."
            call her_main("Sucking on their cocks...","open_wide_tongue","ahegao") from _call_her_main_5157
            call her_main("Like some nasty little slut...","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_5158
            m "Are you in love with those boys, [hermione_name]?"
            call her_main("I don't know, [genie_name]... Maybe...","base","happyCl") from _call_her_main_5159
            her "Could I get paid now please?"
            m "Sure..."
    
    $ gryffindor += 65 #65

    m "The \"Gryffindor\" house gets 65 points!"
    her "Thank you, [genie_name]."
    
    $ display_h_tears = False
    $ aftersperm = False
    $ uni_sperm = False
    
    $ public_whore_ending = True #Activates "Public Whore" ending.
    
    $ hg_pr_BlowjobClassmate_OBJ.points += 1
    $ hg_pr_BlowjobClassmate_OBJ.inProgress = False
    
    if hg_pr_BlowjobClassmate_OBJ.points >= 2:
        $ hg_pr_BlowjobClassmate_OBJ.complete = True
    
    jump hg_pr_transition_block

    return
    