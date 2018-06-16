

label hg_pf_SuckIt: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"
    
    if hg_pf_TouchMe_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_slythCheer_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL",xpos=140) from _call_her_main_5381
                m "A Slytherin Cheerleader."
                if whoring >= 10:
                    call her_main("A Slytherin?","scream","angryCl") from _call_her_main_5382
                    m "Just for a minute."
                    call her_main("...","angry","worriedCl",emote="05") from _call_her_main_5383
                    call her_main("Fine, let me go change.","normal","worriedCl") from _call_her_main_5384
                    call play_sound("door") from _call_play_sound_187 #Sound of a door opening.
                    call set_hermione_outfit(hg_slythCheer_OBJ) from _call_set_hermione_outfit_15
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    call set_u_ani("blowjob_ani","hand_ani",0,10) from _call_set_u_ani_3
    $ mouth_full_of_cum = False
    
    call bld from _call_bld_108

    #Intro
    if hg_pf_SuckIt_OBJ.points == 0: #<=== EVENT 01   FIRST EVENT

        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base") from _call_her_main_5385
        m "I plan to grant \"Gryffindor\" 55 house points today..."
        m "If you suck me off..."

        if whoring < 15: # LEVEL 05
            jump too_much

        call her_main("Oh...","open","down") from _call_her_main_5386
        call her_main("Alright.","base","down") from _call_her_main_5387
        m "Really? Just like that?"
        call her_main("Yes. I know I'm supposed feel outraged...","angry","down_raised") from _call_her_main_5388
        call her_main("But somehow I do not...","angry","base") from _call_her_main_5389
        call her_main("I suppose I am just glad that I can help out my house...","base","down") from _call_her_main_5390
        call her_main("And if to do that I must put your penis in my mouth so be it...","upset","closed") from _call_her_main_5391
        m "Well, alright then."
        call her_main("Although, now when I say it out loud like this...","angry","down_raised") from _call_her_main_5392
        m "Too late! You already said \"yes\"!"
        call her_main("I know...","grin","worriedCl",emote="05") from _call_her_main_5393
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_22
        
        label blowjob_jumping:  # BLOWJOB
        call play_music("playful_tension") from _call_play_music_211# SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        call her_chibi("hide") from _call_her_chibi_169
        show screen chair_left
        call u_play_ani from _call_u_play_ani
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_318
        
        show screen bld1
        call her_head("*Slurp!* *Gulp!* *Slurp!*",xpos="base",ypos="base") from _call_her_head_1287
        m "Yes..."
        m "Try to take it deeper now..."
        her "*Gulp!* *Gobble!* *Gobble!*"
        m "Yes, like that. Good."
        her "*Slurp!* *Gltch!* *Gulp!*"
        m "Yes, that's a good girl."

        menu:
            m "Hm..."
            "\"Whatever happened to your \"MRM\" thing?\"":
                her "*Slurp?*"
                call u_pause_ani from _call_u_pause_ani
                call her_head("Oh, well...","angry","down_raised") from _call_her_head_1288
                call her_head("We are still active, but...") from _call_her_head_1289
                call u_play_ani from _call_u_play_ani_1
                her "*Slurp!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_1
                call her_head("But we are not getting as popular and as much support as I thought we would...","angry","wink") from _call_her_head_1290
                call u_play_ani from _call_u_play_ani_2
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
                call u_pause_ani from _call_u_pause_ani_2
                call her_head("That's not what we stand for, [genie_name].","angry","base") from _call_her_head_1291
                m "What do you mean?"
                call her_head("The \"MRM\" is about gender equality.","open","closed") from _call_her_head_1292
                call her_head("We are not as much against selling sexual favours to the teachers...") from _call_her_head_1293
                call her_head("As we are against the gender inequality that the selling of sexual favour creates...") from _call_her_head_1294
                m "Hm..."
                m "This conversation is starting to bore me..."
                m "Suck on my cock some more before we continue."
                call her_head("Of course, [genie_name].","soft","ahegao") from _call_her_head_1295
                call u_play_ani from _call_u_play_ani_3
                her "*Gobble!* *Slurp!* *Slurp!*"
                m "Yes, much better..."
                m "But you still disapprove of selling the favours, right?"
                her "*Slurp--"
                call u_pause_ani from _call_u_pause_ani_3
                call her_head("Yes, it is frowned upon...","upset","closed") from _call_her_head_1296
                m "And yet, you are the biggest offender by far."
                call her_head("But what choice do I have?","upset","closed") from _call_her_head_1297
                call her_head("I've been put in a very difficult position...") from _call_her_head_1298
                m "The cock, [hermione_name]."
                call her_head("Right, sorry...","upset","closed") from _call_her_head_1299
                call u_play_ani from _call_u_play_ani_4
                her "*Slurp!* *Gulp!* *Gltch!*"
                her "*Slurp--"
                call u_pause_ani from _call_u_pause_ani_4
                call her_head("This one time we had a meeting right after I sold you another favour, [genie_name].","angry","base") from _call_her_head_1300
                call her_head("I had to give a speech with my uniform all messy and stained.") from _call_her_head_1301
                call her_head("It felt awful that I had to do that...") from _call_her_head_1302
                m "You did enjoy it a little bit though..."
                call her_head("Well...","angry","down_raised") from _call_her_head_1303
                m "Just admit it."
                call her_head("...............","angry","base") from _call_her_head_1304
                m "Yes, I knew it. You took pleasure in it, you little perv."
                call her_head("I suppose it was embarrassing and exciting at the same time...","angry","down_raised") from _call_her_head_1305
                call her_head("And it made me feel even worse about myself.") from _call_her_head_1306
                m "You poor thing."
                m "Cock back in the mouth."
                call her_head("Yes, [genie_name].","angry","base") from _call_her_head_1307
                call u_play_ani from _call_u_play_ani_5
                
            "\"Your parents must be proud of you...\"":
                her "*Slurp--"
                call u_pause_ani from _call_u_pause_ani_5
                call her_head("Yes, I believe they are...","smile","happyCl") from _call_her_head_1308
                call her_head("With me being an excellent student despite being muggle-born and all...","base","happyCl") from _call_her_head_1309
                call her_head("Although at first they were against sending me to some \"Bogus boarding school\".","angry","base") from _call_her_head_1310
                call her_head("Took some effort to convince them that \"Hogwarts\" is a respectable institution.","base","happyCl") from _call_her_head_1311
                m "Yes, a respectable institution indeed."
                m "Cock back in your mouth [hermione_name]."
                call u_play_ani from _call_u_play_ani_6
                her "*Slurp!* *Gulp!* *Gobble!*"
                m "Yes, just keep at it for a while..."
                her "*Slurp!* *Gltch!* *Gulp!*"
                m "Good, good..."
                m "So, what would your folks say if they were to see you now, [hermione_name]?"
                her "*Slurp--"
                call u_pause_ani from _call_u_pause_ani_6
                call her_head("They would not understand of course...","open","down") from _call_her_head_1312
                call her_head("But I do not care.") from _call_her_head_1313
                call her_head("I am not afraid to \"get my hands dirty\" and do what needs to be done.","upset","closed") from _call_her_head_1314
                m "A bit rebellious, aren't you?"
                call her_head("Hm... I suppose I am.","angry","wink") from _call_her_head_1315
                m "Back to sucking then. Teach your folks a lesson."
                call u_play_ani from _call_u_play_ani_7
                her "*Slurp!* *Slurp!* *Slurp!*"
                
            "\"Tell me about the \"Gryffindor\" house.\"":
                her "*Slurp--"
                call u_pause_ani from _call_u_pause_ani_7
                call her_head("What can I say that you don't already know, [genie_name]?","soft","baseL") from _call_her_head_1316
                m "Yes... Ehm... I know everything of course."
                m "But I want to see how much you know."
                m "To test your knowledge on the subject."
                call nar(">As soon as you mention \"test\" Hermone's eyes light up with excitement.") from _call_nar_568
                call her_head("OK. But I need a moment gather my thoughts...","smile","happyCl",emote="06") from _call_her_head_1317
                call u_play_ani from _call_u_play_ani_8
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Oh, yes... Take as much time as you need, [hermione_name]."
                her "*Slurp!* *Gulp!* *Slurp!*"
                her "*Gulp--"
                call u_pause_ani from _call_u_pause_ani_8
                call her_head("The \"Gryffindor\" house was founded by Godric Gryffindor, thus the name.","open","down") from _call_her_head_1318
                call her_head("The heraldic animal of \"Gryffindor\" is the lion...") from _call_her_head_1319
                call her_head("And it's colors are red and gold.","open","closed") from _call_her_head_1320
                call u_play_ani from _call_u_play_ani_9
                her "*Gulp!* *Slurp!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_9
                call her_head("Professor Minerva McGonagall is the headmaster of our house.","open","closed") from _call_her_head_1321
                call her_head("The \"Gryffindor\" house emphasizes the traits of courage...") from _call_her_head_1322
                call her_head("As well as \"daring, nerve and chivalry\"...") from _call_her_head_1323
                call her_head("And thus its members are generally regarded as brave but reckless...") from _call_her_head_1324
                call u_play_ani from _call_u_play_ani_10
                her "*Slurp!* *Slurp!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_10
                call her_head("\"Gryffindor\" corresponds roughly to the element of fire...","open","closed") from _call_her_head_1325
                call her_head("And for that reason the colours of red and gold were chosen.") from _call_her_head_1326
                call u_play_ani from _call_u_play_ani_11
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Hm..."
                m "Well, I thought I could turn this around somehow to make fun of you..."
                her "*Slurp??*"
                m "Well, with your house representing courage and righteousness and such..."
                m "And you being a nasty slut..."
                call u_pause_ani from _call_u_pause_ani_11
                call her_head("[genie_name]!","scream","angry",emote="01") from _call_her_head_1327
                m "But to be honest..."
                m "\"Daring, nerve, fire, recklessness\"..."
                m "That sort of describes your personality quite well..."
                call her_head("[genie_name]...","base","base") from _call_her_head_1328
                call u_play_ani from _call_u_play_ani_12
                her "*Gobble!!* *Gltch!!* *Gobble!!!*"
                m "Good girl..."
        
        m "Good..."
        her "*Gobble!* *Slurp!* *Slurp!*"
        m "Good... Back and forth, back and forth... Good girl."
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        call u_pause_ani from _call_u_pause_ani_12
        call her_head("[genie_name]... I am a... whore.","open","down") from _call_her_head_1329
        m "What?"
        call u_play_ani from _call_u_play_ani_13
        her "*Slurp-Slurp-Slurp!*"
        call u_pause_ani from _call_u_pause_ani_13
        call her_head("I truly am a slut and deeply enjoy sucking your cock.","angry","base") from _call_her_head_1330
        m "Oh, yes, yes... Say more things like that."
        call u_play_ani from _call_u_play_ani_14
        her "*Slurp!* *Gulp!* *Slurp!*"
        call u_pause_ani from _call_u_pause_ani_14
        call her_head("Please, [genie_name]. Cum for me.","soft","ahegao") from _call_her_head_1331
        with hpunch
        g4 "Argh! You little...!!!"
        g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"

        menu:
            m "..."
            "-Warn her-":
                call her_head("Yes, I love to suck and --","soft","ahegao") from _call_her_head_1332
                g4 "Heads up, [hermione_name]! Here it comes!"
                call her_head("!!!","angry","wide") from _call_her_head_1333
                call ctc from _call_ctc_319
                hide screen bld1
                call blkfade from _call_blkfade_175

                call set_u_ani("cum_in_mouth_ani") from _call_set_u_ani_4
                call u_play_ani from _call_u_play_ani_15
                ">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."
                call cum_block from _call_cum_block_60
                g4 "{size=+7}ARGH!{/size}"
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "And some more!"
                her "*Gulp!* *Gulp!* *Gulp!*"
                call hide_blkfade from _call_hide_blkfade_131
                call ctc from _call_ctc_320

                call bld from _call_bld_109
                m "Well, I think that's it."
                call u_pause_ani from _call_u_pause_ani_15
                call her_head("..............","cum","worriedCl") from _call_her_head_1334
                m "Are you alright there, [hermione_name]?"
                call her_head("Yes, [genie_name]...","grin","dead") from _call_her_head_1335
                call her_head("You came so much...") from _call_her_head_1336
                m "You managed to swallow it all though."
                call her_head("Yes... I thought I would choke...","grin","dead") from _call_her_head_1337
                call her_head("But I made a promise to myself that I won't let go of your penis no matter what!") from _call_her_head_1338
                m "Good girl."
                call her_head("Thank you, [genie_name].","grin","dead") from _call_her_head_1339
                call her_head("But, still... You came so much...") from _call_her_head_1340
                call her_head("I almost feel as if I just got fed...","soft","ahegao") from _call_her_head_1341
                call her_head("My stomach is so full...") from _call_her_head_1342
                g9 "Yes, I fed you with my cum!"

                if daytime:
                    call her_head("I think I may skip the meal and go straight to class today.","soft","ahegao") from _call_her_head_1343
                else:
                    call her_head("Yes. I think I may skip supper tonight...","soft","ahegao") from _call_her_head_1344

                call her_head("Can I get paid now?","angry","wink") from _call_her_head_1345
                call ctc from _call_ctc_321
                call blkfade from _call_blkfade_176

            "-Don't bother-":
                call her_head("Yes, I love to suck and --","soft","ahegao") from _call_her_head_1346
                call cum_block from _call_cum_block_61
                g4 "{size=+7}Whore!{/size}"
                call her_head("!!?","shock","wide") from _call_her_head_1347
                hide screen bld1
                call set_u_ani("cum_on_face_ani") from _call_set_u_ani_5
                call u_play_ani from _call_u_play_ani_16

                call ctc from _call_ctc_322

                call bld from _call_bld_110
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_07.png"
                call her_head("[genie_name]...","shock","wide") from _call_her_head_1348
                g4 "Don't you move now, [hermione_name]."
                g4 "Yes, just be still and take it."
                g4 "Argh! You little slut! You make me cum hard, [hermione_name]!"
                call her_head("..............","angry","base",tears="soft") from _call_her_head_1349
                m "Whew..."
                call set_u_ani("cum_on_face_blink_ani") from _call_set_u_ani_6
                call her_head("..............","normal","worriedCl") from _call_her_head_1350
                m "Alright, I'm done..."
                call her_head(".................","open","base") from _call_her_head_1351

                if daytime:
                    her "My classes are about to start..."
                else:
                    pass

                m "Just wipe it off and you'll be alright."
                call her_head("............","open","base") from _call_her_head_1352
                m "Unless, you don't want to."
                call her_head("Huh?","angry","worriedCl",emote="05") from _call_her_head_1353
                m "And would rather go outside looking like this."
                m "Let everyone see what a nasty little slut you are."
                call her_head("Of course not, [genie_name]!","angry","worriedCl",emote="05") from _call_her_head_1354
                call ctc from _call_ctc_323
                call blkfade from _call_blkfade_177

                stop music fadeout 1.0

                if daytime:
                    m "You better go before you are late for your classes..."
                else:
                    m "It's getting late..."
                    call her_head("Yes...","angry","worriedCl",emote="05") from _call_her_head_1355

                call her_head("Can I get paid before I leave, [genie_name]?","upset","wink") from _call_her_head_1356
                call blkfade from _call_blkfade_178
                $ aftersperm = True

    #Second Event.
    elif hg_pf_SuckIt_OBJ.points == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base") from _call_her_main_5394
        m "How about another blowjob?"
        call play_music("playful_tension") from _call_play_music_212# SEX THEME.
        call her_main("[genie_name], how dare you propose such a thing to one of your pupils!","scream","angry",emote="01") from _call_her_main_5395
        m "Wha...?"
        call her_main("This is unbecoming of a man of your standing.","scream","angry",emote="01") from _call_her_main_5396
        call her_main("You should be ashamed of yourself [genie_name]!","angry","angry") from _call_her_main_5397

        menu:
            m "???"
            "\"Fine. No points to you then! Leave!\"":
                call play_music("chipper_doodle") from _call_play_music_213 # HERMIONE'S THEME.
                call her_main("[genie_name], calm down, please.","grin","worriedCl",emote="05") from _call_her_main_5398
                m "You are dismissed, [hermione_name]."
                call her_main("[genie_name], please, I didn't mean any of the things I said.","grin","worriedCl",emote="05") from _call_her_main_5399
                m "What?"

            "\"Ehm... I am sorry?\"":
                stop music fadeout 1.0
                call her_main("*Giggle*","base","base") from _call_her_main_5400
                m "Huh?"
                call play_music("chipper_doodle") from _call_play_music_214 # HERMIONE'S THEME.
                call her_main("I got you... [genie_name].","grin","worriedCl",emote="05") from _call_her_main_5401
                m "What?"

        call her_main("Well, so much has happened lately...","base","base") from _call_her_main_5402
        her "I had so many new experiences that kind of changed the way I look at things..."
        her "So I was just trying to imagine how the \"old me\" would've reacted to this."
        m "So..."
        g4 "You were messing with me then?"
        call her_main("uhm... I'm sorry [genie_name], I didn't mean to...","angry","worriedCl",emote="05") from _call_her_main_5403
        g4 "You nasty little girl! You must be punished!"
        g9 "I'll punish you with my cock!"
        call her_main("...............................","angry","worriedCl",emote="05") from _call_her_main_5404

        call blkfade from _call_blkfade_179 #Needs to be active first!
        jump blowjob_jumping

    #Third Event.
    elif hg_pf_SuckIt_OBJ.points >= 2 and whoring < 21:
        call play_music("playful_tension") from _call_play_music_215# SEX THEME.
        m "Suck my dick, [hermione_name]."
        call her_main("Of course...","base","base",xpos="mid",ypos="base") from _call_her_main_5405
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_23
        
        call play_music("playful_tension") from _call_play_music_216# SEX THEME.                                                                                                                                                                           #HERMIONE
        hide screen genie
        call her_chibi("hide") from _call_her_chibi_170
        show screen chair_left
        call u_play_ani from _call_u_play_ani_17
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_324
        
        show screen bld1
        call her_head("*Slurp!* *Slurp!* *Gulp!*","","",xpos="base",ypos="base") from _call_her_head_1357
        m "Yes, good girl..."
        her "*Slurp!* *Gobble!* *Slurp!*"
        
        call play_sound("knocking") from _call_play_sound_188 #Sound someone knocking on the door.
        call nar("> *Knock-knock-knock!*") from _call_nar_569
        her "{size=+7}!!!{/size}"
        m "Hm?"

        if daytime:
            m "Who could that be?"
        else:
            m "Who could that be at this hour?"

        call u_pause_ani from _call_u_pause_ani_16

        if not luna_known:
            call her_head("([genie_name], what should I do?)","shock","wide") from _call_her_head_1358
            m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
            sna "Albus? Are you there? I need to talk to you."
            call her_head("(It's professor Snape!)","angry","base") from _call_her_head_1359
            call her_head("([genie_name], please, send him away, I beg you!)") from _call_her_head_1360

            menu:
                m "..."
                "\"Please, come on in, Severus.\"":
                    $ mad = 30
                    stop music fadeout 1.0
                    call her_head("([genie_name], no!)","angry","angry",emote="01") from _call_her_head_1361
                    
                    call nar(">Hermione gives your balls a firm twist full of frustration.") from _call_nar_570
                    g4 "Ouch!"
                    hide screen bld1
                    # SNAPE COMES IN
                    call play_sound("door") from _call_play_sound_189 #Sound of a door opening.
                    call sna_chibi("stand","door","base") from _call_sna_chibi_19
                    pause.2
                    call sna_walk("door","mid",4) from _call_sna_walk_20
                    pause.2

                    call bld from _call_bld_111
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    
                    call sna_head("Good, you are here.","snape_01",xpos="base",ypos="base") from _call_sna_head_201
                    call u_play_ani from _call_u_play_ani_18
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("Listen, there is something I want to discuss...","snape_06") from _call_sna_head_202
                    call sna_head("Hm...?","snape_05") from _call_sna_head_203
                    call sna_head("Genie? Are you alright?") from _call_sna_head_204
                    her "{size=-4}(Ginny!!? Is she here as well?!){/size}"
                    her "{size=-4}(No, please! I will die of shame!){/size}"
                    m "Yes, Severus, I am fine..."
                    her "{size=-4}(What? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
                    call sna_head("What are you... looking at?","snape_05") from _call_sna_head_205
                    m "Ehm... Just admiring...{w} the cupboard."
                    m "Please, continue..."
                    call sna_head("...............","snape_05") from _call_sna_head_206
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    m "Did you want to discuss something?"
                    call sna_head("Yes. That Hermione girl.","snape_06") from _call_sna_head_207
                    her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                    m "Oh... What about her?"
                    call sna_head("You promised that you would take care of the little witch.","snape_04") from _call_sna_head_208
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("But she is still being a major pain in my arse!","snape_04") from _call_sna_head_209
                    call sna_head("Her tactics have changed...") from _call_sna_head_210
                    call sna_head("But the amount of grief she manages to bring me is the same...","snape_03") from _call_sna_head_211
                    m "I see... ah..."
                    call sna_head("I swear, that girl is driving me crazy!","snape_10") from _call_sna_head_212
                    g4 "Yeah, she is driving me crazy as well... ah..."
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    call sna_head("Will you take care of this then?","snape_04") from _call_sna_head_213
                    m "Yes. She'll get what she deserves."
                    call sna_head("Good. That is all I wanted to hear.","snape_06") from _call_sna_head_214

                    if daytime:
                        m "Well, have a good day, Severus."
                        call sna_head("Yes, thank you.","snape_06") from _call_sna_head_215
                    else:
                        m "Good night, Severus."
                        call sna_head("Right...","snape_06") from _call_sna_head_216

                    # SNAPE LEAVES
                    hide screen bld1
                    with d3

                    call sna_chibi("stand","mid","base",flip=True) from _call_sna_chibi_20
                    pause.2
                    call sna_walk("mid","leave",3) from _call_sna_walk_21
                    stop music fadeout 1.0
                    call ctc from _call_ctc_325
                    call blkfade from _call_blkfade_180
        
                    call play_music("playful_tension") from _call_play_music_217# SEX THEME.
                    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
                    ">Seeing her being so confused and vulnerable and yet continuing to perform her task diligently pushes you over the edge."
                    g4 "(Here it comes!)"
                    call hide_blkfade from _call_hide_blkfade_132
                    
                "\"I am busy right now, Severus.\"":
                    call her_head("(Thank you, [genie_name].)","angry","base") from _call_her_head_1362
                    sna "Busy? With what?"
                    sna "All you do is sit on you arse all day."
                    sna "I really need to talk to you about something."
                    m "I said I am busy, Severus."
                    m "Understood? I am \"busy\"!"
                    sna "Oh... You mean \"Busy\" busy? Gotcha!"
                    sna "Well, I'll talk to you later then."

        #Scene with Luna.
        else:
            call her_head("([genie_name], what should I do?)","shock","wide") from _call_her_head_1363
            m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
            lun "[l_genie_name]? Are you there? I need to talk to you."
            call her_head("(It's Luna!)","angry","base") from _call_her_head_1364
            call her_head("Please, [genie_name], send her away, I beg you!") from _call_her_head_1365

            menu:
                m "..."
                "\"Please, come on in, [luna_name].\"":
                    $ mad += 10
                    stop music fadeout 1.0
                    call her_head("([genie_name], no!)","angry","angry",emote="01") from _call_her_head_1366
                    hide screen bld1
                    with d3

                    #Luna comes in
                    call play_sound("door") from _call_play_sound_190 #Sound of a door opening.
                    $ luna_chibi("stand", 400, 250)
                    $ changeLuna(1, 1, 4, 1)
                    call bld from _call_bld_112
                    lun "Hello [l_genie_name]."
                    $ g_c_u_pic = "blowjob_ani" # sucking
                    call u_play_ani from _call_u_play_ani_19

                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ changeLuna(1, 2, 4, 1)
                    lun "Um, are you going to turn around sir..."
                    m "I'm afraid I'm a bit preoccupied at the moment."
                    $ changeLuna(1, 1, 5, 1)
                    lun "Doing what?."
                    her "{size=-4}(What? *Slurp...?* *Gulp...?*){/size}"

                    menu:
                        "-Tell the truth-":
                            if collar == 0:
                                $ collar = 5
                            m "Miss Granger is helping relieve me as we speak."
                            $ changeLuna(1, 2, 5, 4)
                            lun "You mean that Hermione is behind your desk..."
                            $ changeLuna(10, 1, 4, 9)
                            lun "Releiving you as we speak."
                            ">Hermione's face goes crimson with shame but she continues her efforts."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Yes, that's correct."
                            lun "Well in that case I think I best be off. It seems that you're busy tending to other students."
                            m "Thank you [luna_name]"

                            if daytime:
                                m "Well, have a good day.."
                                $ changeLuna(1, 1, 1, 5)                                                       # SNAPE
                                lun "Yes, thank you. I know that you will..."
                            else:
                                m "Good night, [luna_name]."
                                $ changeLuna(1, 1, 4, 1)
                                lun "Goodnight [l_genie_name].."
                                $ changeLuna(5, 2, 3, 1)   
                                lun "Goodnight hermione..."

                        "-Lie-":
                            m "Ehm... Just admiring...{w} the cupboard."
                            m "Please continue..."
                            lun "..............."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Did you want to discuss something?"
                            $ changeLuna(2, 1, 4, 1)   
                            lun "Yes. These wrackspurts."
                            her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                            m "Oh... What about them?"
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}" 
                            lun "No matter what I do I can't seem to be rid of them!"
                            $ changeLuna(1, 2, 4, 1) 
                            lun "They only seem to be getting worse!"
                            m "I see... ah..."
                            $ changeLuna(1, 1, 4, 1) 
                            lun "They're driving me crazy, I won't be able to cope much longer"
                            g4 "Yeah, they're driving me crazy as well... ah..."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            $ changeLuna(1, 1, 4, 1)                            # SNAPE
                            lun "Will you take care of them then?"
                            m "Yes. I'll find a way to deal with these rapers soon."
                            $ changeLuna(1, 2, 5, 1) 
                            lun "...Thank you [l_genie_name]."

                            if daytime:
                                m "Well, have a good day, [luna_name]."
                                $ changeLuna(1, 2, 1, 1)
                                lun "Yes, thank you."
                            else:
                                m "Good night, [luna_name]."
                                lun "Goodnight [l_genie_name]..."

                    #Luna leaves.
                    hide screen luna
                    hide screen bld1
                    with d3
                    call play_sound("door") from _call_play_sound_191 #Sound of a door opening.
                    hide screen luna_chibi
                    stop music fadeout 1.0
                    pause.5
                    call blkfade from _call_blkfade_181
                    
                    call play_music("playful_tension") from _call_play_music_218# SEX THEME.
                    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
                    
                "\"I am busy right now, [luna_name].\"":
                    call her_head("(Thank you, [genie_name].)","angry","base") from _call_her_head_1367
                    lun "Busy? How so?"
                    lun "Are you helping another student fight off the wrackspurts?"
                    m "Yes, that's exactly what I'm doing."
                    lun "Oh... well, I'll visit you later then."

            call blkfade from _call_blkfade_182
            her "*Slurp!* *Slurp!* *Gulp!*"
            ">Hermione keeps sucking on your cock with a rather fierce determination."
            ">Her technique is lacking but she makes up for it with the effort she puts it."
            hide screen bld1
            call hide_blktone from _call_hide_blktone_21
            call ctc from _call_ctc_326

            call bld from _call_bld_113
            m "Yes... I love your eager, little mouth girl..."
            her "*Gobble!* *Gobble!* *Gobble!*"
            call u_pause_ani from _call_u_pause_ani_17
            call her_head("[genie_name]?","soft","ahegao") from _call_her_head_1368
            m "Hm?"
            call her_head("Are you going to cum on my face today?","soft","ahegao") from _call_her_head_1369
            call her_head("Or do you plan to cum in my mouth?") from _call_her_head_1370

            menu:
                "\"I Plan to splatter your face with cum!\"":
                    call her_head("I see...","soft","ahegao") from _call_her_head_1371
                    m "Why do you ask?"
                    call her_head("Oh... I just read in a book that semen contains a lot of antioxidants...","grin","dead") from _call_her_head_1372
                    call her_head("It's good for the skin...") from _call_her_head_1373
                    m "Great. One facial coming up."
                    m "Back to work now."
                "\"I Plan to fill your mouth with cum!\"":
                    call her_head("I see...","grin","dead") from _call_her_head_1374
                    m "Why do you ask?"
                    call her_head("Well, I am trying to watch my calorie-intake...","soft","ahegao") from _call_her_head_1375
                    call her_head("I just wonder how much calories your load contains, [genie_name].") from _call_her_head_1376
                    call her_head("Maybe I should skip my next meal...") from _call_her_head_1377
                    m "[hermione_name]."
                    call her_head("Yes?","soft","ahegao") from _call_her_head_1378
                    m "Dick back in the mouth."
                "\"I don't plan so far ahead.\"":
                    call her_head("I see...","soft","ahegao") from _call_her_head_1379
                    m "Don't you like surprises?"
                    call her_head("Not really...","soft","ahegao") from _call_her_head_1380
                    call her_head("I rather enjoy planning ahead actually...") from _call_her_head_1381
                    m "Well some things in life are just unpredictable."
                    m "There is only one way to find out for sure."
                    
                "\"What would you like?\"":
                    call her_head("If it is all the same to you, [genie_name]...","soft","ahegao") from _call_her_head_1382
                    if generating_points == 1:
                        call her_head("I would like you to cum on my face, [genie_name].","grin","dead") from _call_her_head_1383
                        call her_head("I read that it's good for the skin.") from _call_her_head_1384
                    else:
                        call her_head("I would like you to cum in my mouth.","grin","dead") from _call_her_head_1385
                        call her_head("You usually cum so much so I think I will be able to just skip my next meal...") from _call_her_head_1386
                        call her_head("And do some homework instead.") from _call_her_head_1387
                    m "Well, we'll see about that."
                    m "Back to sucking now."
                    
        call u_play_ani from _call_u_play_ani_20
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Hm..."
        m "You are getting better at this [hermione_name]."
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Ok, say something nasty now..."
        her "*Slurp--?"
        call u_pause_ani from _call_u_pause_ani_18

        if whoring < 21:
            call her_head("uhm...","angry","down_raised") from _call_her_head_1388
            call her_head("I eat cockroaches?","angry","base") from _call_her_head_1389
            m "What the fuck?"
            call her_head("T-they are pretty nasty, [genie_name]...","angry","base") from _call_her_head_1390
            m "No, [hermione_name], I mean something dirty!"
            m "And don't you dare to say \"mud\"!"
            m "I mean dirty in a sexual way!"
            call her_head("Oh... Ehm...","angry","down_raised") from _call_her_head_1391
            m "Ah, never mind, the moment is gone..."
            call her_head("Ehm... I'm sorry, [genie_name].","angry","base") from _call_her_head_1392
            m "Yeah, whatever. Make it up to me by sucking my cock harder."
            call her_head("Of course, [genie_name].","upset","closed") from _call_her_head_1393

        else:
            call her_head("I'm a slut, [genie_name].","base","suspicious") from _call_her_head_1394
            call her_head("A slut for your cum.","base","glance") from _call_her_head_1395
            m "That's it, [hermione_name]."
            call her_head("It's all I can think about [genie_name].","base","down") from _call_her_head_1396
            call her_head("Sucking your dirty old cock...") from _call_her_head_1397
            m "Well you better get back to it then [hermione_name]"
            call her_head("Thank you, [genie_name].","grin","dead") from _call_her_head_1398
            m "You're welcome, cumslut."
            call her_head("...","base","ahegao_raised") from _call_her_head_1399

        call u_play_ani from _call_u_play_ani_21
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
                call ctc from _call_ctc_327
                call blkfade from _call_blkfade_183

                call set_u_ani("cum_in_mouth_ani") from _call_set_u_ani_7
                call u_play_ani from _call_u_play_ani_22
                call cum_block from _call_cum_block_62
                g4 "{size=+7}ARGH!{/size}"
                g4 "Eat my cum, slut!"
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Yes! Down your fucking throat!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_133
                stop music fadeout 1.0
                call ctc from _call_ctc_328

                call bld from _call_bld_114
                m "Well, I think that's it."
                m "You can let go now..."
                call u_pause_ani from _call_u_pause_ani_19

                call her_main("...........................","full_cum","dead",xpos="mid",ypos="base") from _call_her_main_5406
                call her_main("................") from _call_her_main_5407
                call her_main("........") from _call_her_main_5408
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_main("*GULP!*","cum","worriedCl") from _call_her_main_5409
                call her_main("Gua-ha...","open_wide_tongue","base") from _call_her_main_5410
                m "You alright?"
                call play_music("chipper_doodle") from _call_play_music_219 # HERMIONE'S THEME.
                call her_main("Yes, [genie_name]...","grin","dead") from _call_her_main_5411
                m "Going to skip your next meal?"
                call her_main("I think so...","grin","dead") from _call_her_main_5412
                call her_main("You always cum so much, [genie_name]...") from _call_her_main_5413
                m "Heh... And who's fault is that??"
                call her_main(".............","grin","dead") from _call_her_main_5414 #Smile.
                call her_main("Can I get paid now?") from _call_her_main_5415

                if whoring >= 21:
                    if daytime:
                        m "What, even after I just gave you lunch?"
                    else:
                        m "What, even after I fed you dinner"
                    call her_main(".............","annoyed","suspicious") from _call_her_main_5416 #Smile.
                    call her_main("Fine, I suppose this was worth a meal") from _call_her_main_5417

                call ctc from _call_ctc_329
                call blkfade from _call_blkfade_184
                
            "-Cum on her face-":
                call blkfade from _call_blkfade_185

                call u_pause_ani from _call_u_pause_ani_20
                g4 "Ready for your facial, [hermione_name]?"
                call her_head("Yes [genie_name]!","grin","dead") from _call_her_head_1400
                g4 "Here it comes then!"
                hide screen bld1
                call set_u_ani("cum_on_face_ani") from _call_set_u_ani_8
                call u_play_ani from _call_u_play_ani_23
                call hide_blkfade from _call_hide_blkfade_134
                call cum_block from _call_cum_block_63

                call bld from _call_bld_115
                g4 "{size=+7}Whore!{/size}"
                call her_head("!!?","shock","wide") from _call_her_head_1401
                hide screen bld1
                with d3
                call ctc from _call_ctc_330

                call bld from _call_bld_116
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_07.png"
                call her_head("[genie_name]...","shock","wide") from _call_her_head_1402
                g4 "All over your fucking face!"
                call her_head("Aaah!","grin","dead") from _call_her_head_1403
                call set_u_ani("cum_on_face_blink_ani") from _call_set_u_ani_9

                m "Well, I'm done."
                call her_head("....................................","grin","dead") from _call_her_head_1404
                m "I said it's over, [hermione_name]."
                call her_head("Yes, I heard you [genie_name]...","grin","dead") from _call_her_head_1405
                m "So... Aren't you going to clean up?"
                call her_head("In a moment...","grin","dead") from _call_her_head_1406
                call her_head("I'm giving my skin time to soak in the anti-oxidants...") from _call_her_head_1407 
                m "Hm... I find this quite hot..."
                m "Take your time, [hermione_name]..."

                call blkfade from _call_blkfade_186
                stop music fadeout 1.0 
                ">A while later."
                call u_pause_ani from _call_u_pause_ani_21
                $ uni_sperm = True
                $ aftersperm = True
                call her_chibi("stand","desk","base") from _call_her_chibi_171
                show screen genie
                hide screen bld1
                hide screen blktone
                call hide_blkfade from _call_hide_blkfade_135
                pause.5

                call her_main("I take it you enjoyed yourself, [genie_name]?","angry","wink",xpos="mid",ypos="base") from _call_her_main_5418
                call play_music("chipper_doodle") from _call_play_music_220 # HERMIONE'S THEME.
                m "Yes I did, [hermione_name]."
                call her_main("Good, so Can I get paid now?","grin","dead") from _call_her_main_5419

                if whoring >= 21:
                    m "What, even after I just gave you a salon treatment?"
                    m "Women pay a lot of money for a good facial."
                    call her_main(".............","annoyed","suspicious") from _call_her_main_5420 #Smile.
                    call her_main("Fine, but my skin better look better tomorrow.") from _call_her_main_5421

                call blkfade from _call_blkfade_187
    
    #Fourth Event
    elif hg_pf_SuckIt_OBJ.points >= 2 and whoring >= 21:
        call play_music("playful_tension") from _call_play_music_221# SEX THEME.
        m "Suck my dick, [hermione_name]."
        call her_main("Of course [genie_name]...","base","ahegao_raised",xpos="mid",ypos="base") from _call_her_main_5422
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_24
        
        call play_music("playful_tension") from _call_play_music_222# SEX THEME.                                                                                                                                                                       #HERMIONE
        hide screen genie
        call her_chibi("hide") from _call_her_chibi_172
        show screen chair_left
        call u_play_ani from _call_u_play_ani_24
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_331
        
        show screen bld1
        call her_head("*Slurp!* *Slurp!* *Gulp!*","","",xpos="base",ypos="base") from _call_her_head_1408
        m "Yes, good girl..."
        her "*Slurp!* *Gobble!* *Slurp!*"
        m "lick the shaft..."
        her "*lick!* *Slurp!* *lick!*"
        call nar(">Hermione keeps sucking on your cock like her life depends on it.","start") from _call_nar_571
        call nar(">Her technique is almost perfect and she is incredibly enthusiastic.","end") from _call_nar_572
        m "Yes... I love your eager, little mouth slut..."
        her "*Gobble!* *Gobble!* *Gobble!*"
        call u_pause_ani from _call_u_pause_ani_22
        call her_head("[genie_name]?","base","down") from _call_her_head_1409
        m "Hm?"
        call her_head("How would you like me to please you today?","soft","ahegao") from _call_her_head_1410

        menu:
            "\"Pretend I am your father.\"":
                call her_head("My father?","angry","wink") from _call_her_head_1411
                m "Anything wrong with that?"
                call her_head("I suppose not...","base","down") from _call_her_head_1412
                call her_head("I mean it's just pretending...","grin","dead") from _call_her_head_1413
                m "Great. Dick back in mouth then."
                call u_play_ani from _call_u_play_ani_25
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "That's it, princess. Suck daddy's dick."
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Tell me how much you want it."
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_23
                call her_head("So much daddy...","soft","ahegao") from _call_her_head_1414
                call u_play_ani from _call_u_play_ani_26
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_24
                call her_head("It's all I think about when we're together...","base","ahegao_raised") from _call_her_head_1415
                call u_play_ani from _call_u_play_ani_27
                her "*Gobble!* *Gulp!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_25
                call her_head("When we're sitting together on the couch watching T.V...","base","ahegao_raised") from _call_her_head_1416
                call her_head("I just imagine that I am sucking your cock instead...","base","ahegao_raised") from _call_her_head_1417
                call u_play_ani from _call_u_play_ani_28
                her "*lick!* *Slurp!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_26
                call her_head("I even wish that mum left you sometimes...","annoyed","down") from _call_her_head_1418
                call u_play_ani from _call_u_play_ani_29
                her "*Gobble!* *Slurp!* *lick!*"
                m "Why's that?"
                call u_pause_ani from _call_u_pause_ani_27
                call her_head("So that I'm the only one to get your dick...","soft","dead") from _call_her_head_1419
                call u_play_ani from _call_u_play_ani_30
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_28
                call her_head("You'll come home every day...","soft","dead") from _call_her_head_1420
                call u_play_ani from _call_u_play_ani_31
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_29
                call her_head("Throw me onto my bed...","grin","dead") from _call_her_head_1421
                call u_play_ani from _call_u_play_ani_32
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_30
                call her_head("and use me...","grin","dead") from _call_her_head_1422
                call u_play_ani from _call_u_play_ani_33
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_31
                call her_head("however you want...","grin","dead") from _call_her_head_1423
                call u_play_ani from _call_u_play_ani_34
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_32
                call her_head("for as long as you want...","grin","dead") from _call_her_head_1424
                call u_play_ani from _call_u_play_ani_35
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_33
                call her_head("you won't even ask...","grin","dead") from _call_her_head_1425
                call u_play_ani from _call_u_play_ani_36
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_34
                call her_head("you'll just take me...","grin","dead") from _call_her_head_1426
                call u_play_ani from _call_u_play_ani_37
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_35
                call her_head("even though I say no...","grin","dead") from _call_her_head_1427
                call u_play_ani from _call_u_play_ani_38
                her "*Gobble!* *lick!* *Gobble!*"
                m "That's it princess, Almost there..."
                call u_pause_ani from _call_u_pause_ani_36
                call her_head("Where do you want to cum today daddy?","soft","ahegao") from _call_her_head_1428
                call her_head("Are you going to cover my face?","soft","ahegao") from _call_her_head_1429
                call her_head("Or make me swallow your big load?","grin","dead") from _call_her_head_1430
                call her_head("{size=-4}Even if I don't want to...{/size}","grin","dead") from _call_her_head_1431
                m "Let's find out shall we?"
                call her_head("Yes daddy...","soft","ahegao") from _call_her_head_1432
                call u_play_ani from _call_u_play_ani_39
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
                        call hide_blkfade from _call_hide_blkfade_136
                        g4 "Here it comes, [hermione_name]! Here comes daddy!"
                        her "!!!"
                        call ctc from _call_ctc_332
                        call blkfade from _call_blkfade_188

                        call set_u_ani("cum_in_mouth_ani") from _call_set_u_ani_10
                        call u_play_ani from _call_u_play_ani_40
                        call cum_block from _call_cum_block_64
                        g4 "{size=+7}ARGH!{/size}"
                        g4 "Eat my cum, slut!"
                        #Cumming.
                        her "*Gulp!-Gulp!-Gulp!*"
                        with hpunch
                        g4 "Yes! Down your fucking slut throat!"
                        her "*Gulp-gulp-gulp-gulp-gulp!*"
                        hide screen bld1
                        call hide_blkfade from _call_hide_blkfade_137

                        stop music fadeout 1.0
                        call ctc from _call_ctc_333
                        show screen bld1
                        with d3
                        m "Well, I think that's it."
                        m "You can let go now..."
                        call u_pause_ani from _call_u_pause_ani_37
                        call her_head("...........................","full_cum","dead") from _call_her_head_1433
                        call her_head("................") from _call_her_head_1434
                        call her_head("........") from _call_her_head_1435
                        $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                        call her_head("*GULP!*","cum","worriedCl") from _call_her_head_1436
                        call her_head("Gua-ha...","open_wide_tongue","base") from _call_her_head_1437
                        m "How was that?"
                        call play_music("chipper_doodle") from _call_play_music_223 # HERMIONE'S THEME.
                        call her_head("So tasty...","grin","dead") from _call_her_head_1438
                        m "Really?"
                        call her_head("Yes daddy...","grin","dead") from _call_her_head_1439
                        call her_head("It's always tasty with you...") from _call_her_head_1440
                        m "Heh... is that so?"
                        call her_head(".............","grin","dead") from _call_her_head_1441 #Smile.
                        ">She leans forward and gives your wilting cock a small kiss."
                        call her_head("Thanks daddy.","base","baseL") from _call_her_head_1442 #Smile.
                        call ctc from _call_ctc_334
                        call blkfade from _call_blkfade_189
                        
                    "-Cum on her face-":
                        call hide_blkfade from _call_hide_blkfade_138
                        call u_pause_ani from _call_u_pause_ani_38
                        g4 "Ready for your cum-load, princess slut?"
                        call her_head("Yes daddy!","grin","dead") from _call_her_head_1443
                        g4 "Here it comes then!"
                        call cum_block from _call_cum_block_65
                        g4 "{size=+7}Slut!{/size}"
                        call her_head("!!?","shock","dead") from _call_her_head_1444
                        call set_u_ani("cum_on_face_ani") from _call_set_u_ani_11
                        call u_play_ani from _call_u_play_ani_41
                        hide screen bld1
                        with d3
                        call ctc from _call_ctc_335

                        call bld from _call_bld_117
                        $ uni_sperm = True
                        $ u_sperm = "characters/hermione/face/auto_07.png"
                        call her_head("Daddy...","shock","wide") from _call_her_head_1445
                        g4 "That's it, princess!"
                        call her_head("Aaah!","grin","dead") from _call_her_head_1446
                        call set_u_ani("cum_on_face_blink_ani") from _call_set_u_ani_12
                        m "Well, I'm done."
                        call her_head("....................................","grin","dead") from _call_her_head_1447
                        m "I said it's over, [hermione_name]."
                        call her_head("Yes, I heard you, daddy...","grin","dead") from _call_her_head_1448
                        m "So... Aren't you going to clean up?"
                        call her_head("In a minute...","grin","dead") from _call_her_head_1449
                        call her_head("I'm just savouring the moment...") from _call_her_head_1450 
                        m "Hm..."
                        m "Take your time, [hermione_name]..."
                        call blkfade from _call_blkfade_190

                        stop music fadeout 1.0 
                        ">A while later."
                        call u_pause_ani from _call_u_pause_ani_39
                        $ uni_sperm = False
                        $ aftersperm = True
                        call her_main("I take it you enjoyed yourself sir?","angry","wink") from _call_her_main_5423
                        call play_music("chipper_doodle") from _call_play_music_224 # HERMIONE'S THEME.
                        m "Yes I did princess."
                        $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

            "\"Worship my cock.\"": ###IN PROGRESS
                call her_head("Worship it?","angry","wink") from _call_her_head_1451
                m "Worship. My. Cock."
                call her_head("Well...","base","down") from _call_her_head_1452
                call her_head("ok...","soft","ahegao") from _call_her_head_1453
                m "Great. You can start by putting it back in your mouth."
                call u_play_ani from _call_u_play_ani_42
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Thats it.."
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Tell me how much you love my cock."
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_40
                call her_head("So much [genie_name]...","soft","ahegao") from _call_her_head_1454
                call u_play_ani from _call_u_play_ani_43
                her "*Slurp!* *Gobble!* *Slurp!*"
                call u_pause_ani from _call_u_pause_ani_41
                call her_head("It's all I think about when I'm in class...","base","ahegao_raised") from _call_her_head_1455
                call u_play_ani from _call_u_play_ani_44
                her "*Gobble!* *Gulp!* *Gobble!*"

                if lock_public_favors == True:
                    call u_pause_ani from _call_u_pause_ani_42
                    call her_head("Sucking your perfect dick.","base","ahegao_raised") from _call_her_head_1456
                    call her_head("No one elses...","base","ahegao_raised") from _call_her_head_1457
                    call u_play_ani from _call_u_play_ani_45
                    her "*lick!* *Slurp!* *Slurp!*"
                    call u_pause_ani from _call_u_pause_ani_43
                    call her_head("Just your {p}perfect, {p}beautiful {p}{size=-4}cock{/size}","grin","dead") from _call_her_head_1458
                    call u_play_ani from _call_u_play_ani_46
                    her "*Gobble!* *Slurp!* *lick!*"

                else:
                    call u_pause_ani from _call_u_pause_ani_44
                    call her_head("Even when you make me suck another boys dick...","base","ahegao_raised") from _call_her_head_1459
                    call her_head("I still imagine that it's yours...","base","ahegao_raised") from _call_her_head_1460
                    call u_play_ani from _call_u_play_ani_47
                    her "*lick!* *Slurp!* *Slurp!*"
                    call u_pause_ani from _call_u_pause_ani_45
                    call her_head("Imagine that it's your cum sliding down my throat...","soft","ahegao") from _call_her_head_1461
                    call u_play_ani from _call_u_play_ani_48
                    her "*Gobble!* *Slurp!* *lick!*"
                    call u_pause_ani from _call_u_pause_ani_46
                    call her_head("Imagine that it's your hot load shot across my face...","grin","dead") from _call_her_head_1462
                    call u_play_ani from _call_u_play_ani_49
                    her "*Gobble!* *Slurp!* *lick!*"

                m "Is that so?"
                call u_pause_ani from _call_u_pause_ani_47
                call her_head("Yes [genie_name]...","soft","dead") from _call_her_head_1463
                call u_play_ani from _call_u_play_ani_50
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_48
                call her_head("Sometimes...","soft","dead") from _call_her_head_1464
                call u_play_ani from _call_u_play_ani_51
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_49
                call her_head("After you make me suck your perfect cock...","grin","dead") from _call_her_head_1465
                call u_play_ani from _call_u_play_ani_52
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_50
                call her_head("I won't brush my teeth...","grin","dead") from _call_her_head_1466
                call u_play_ani from _call_u_play_ani_53
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_51
                call her_head("just so I can go to sleep...","grin","dead") from _call_her_head_1467
                call u_play_ani from _call_u_play_ani_54
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_52
                call her_head("with that perfect taste in my mouth...","grin","dead") from _call_her_head_1468
                call u_play_ani from _call_u_play_ani_55
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_53
                call her_head("and when I do brush my teeth...","grin","dead") from _call_her_head_1469
                call u_play_ani from _call_u_play_ani_56
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_54
                call her_head("Your beautiful cock is all I can think about...","grin","dead") from _call_her_head_1470
                call u_play_ani from _call_u_play_ani_57
                her "*Gobble!* *lick!* *Gobble!*"
                call u_pause_ani from _call_u_pause_ani_55
                call her_head("I even started to moan while brushing them...","grin","dead") from _call_her_head_1471
                call u_play_ani from _call_u_play_ani_58
                her "*Gobble!* *lick!* *Gobble!*"
                m "That's it cock slut, Almost there..."
                call u_pause_ani from _call_u_pause_ani_56
                call her_head("Where do you want to cum today [genie_name]?","soft","ahegao") from _call_her_head_1472
                call her_head("I know it's greedy of me to ask...","angry","down_raised") from _call_her_head_1473
                call her_head("But can you cum in my mouth?","angry","wink") from _call_her_head_1474
                call her_head("{size=-4}Please...{/size} I promise I won't waste a drop.","soft","ahegao") from _call_her_head_1475
                m "I think that can be arranged "
                call her_head("Thank you [genie_name]!","smile","happyCl",cheeks="blush",emote="06") from _call_her_head_1476
                call u_play_ani from _call_u_play_ani_59
                call nar(">Hermione devours your cock with renewed vigour.") from _call_nar_573
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
                hide screen blkfade
                with d3
                g4 "Here it comes, [hermione_name]! Here's you reward!"
                her "!!!"
                
                call ctc from _call_ctc_336
                call blkfade from _call_blkfade_191

                call set_u_ani("cum_in_mouth_ani") from _call_set_u_ani_13
                call u_play_ani from _call_u_play_ani_60
                call cum_block from _call_cum_block_66
                g4 "{size=+7}ARGH!{/size}"
                g4 "Eat my cum, slut!"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Yes! Down your fucking cumslut mouth!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen bld1
                call hide_blkfade from _call_hide_blkfade_139
                stop music fadeout 1.0
                call ctc from _call_ctc_337

                call bld from _call_bld_118
                m "Well, I think that's it."
                m "You can let go now..."
                call u_pause_ani from _call_u_pause_ani_57
                call her_main("...........................","full_cum","dead",tears="mascara",xpos="mid",ypos="base",trans="fade") from _call_her_main_5424
                call her_main("................","full_cum","dead",tears="mascara") from _call_her_main_5425
                call her_main("........","full_cum","dead",tears="mascara") from _call_her_main_5426
                m "How was that?"
                call her_main("...") from _call_her_main_5427
                call play_music("chipper_doodle") from _call_play_music_225 # HERMIONE'S THEME.
                m "Are you going to swallow?"
                call her_main("*Shakes her head side to side*","full_cum","dead",tears="mascara") from _call_her_main_5428

                if daytime:
                    m "So you're going to go to class with a mouth full of my cum?"
                else:
                    m "So you're going to go to sleep with a mouth full of my cum?"

                call her_main("*She nods her head up and down enthusiastically*","full_cum","ahegao",cheeks="blush",tears="mascara") from _call_her_main_5429 #Smile.
                m "Good girl."
                call ctc from _call_ctc_338

                call blkfade from _call_blkfade_192
                $ mouth_full_of_cum = True
                
    $ gryffindor += current_payout #35

    call blkfade from _call_blkfade_193
    hide screen hermione_main
    call u_end_ani from _call_u_end_ani
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") from _call_gen_chibi_112
    show screen genie
    call her_chibi("stand","desk","base") from _call_her_chibi_173
    hide screen bld1
    hide screen blktone
    call hide_blkfade from _call_hide_blkfade_140
    pause.5
    
    call bld from _call_bld_119
    if whoring < 21:
        m "Yes, [hermione_name]. 55 points to \"Gryffindor\"." 
        $ gryffindor +=55

    if mouth_full_of_cum:
        call her_main("...","full_cum","ahegao",cheeks="blush",tears="mascara",xpos="right",ypos="base") from _call_her_main_5430
    else:
        call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base") from _call_her_main_5431
    
    if whoring < 18:
        $ whoring +=1
        
    if hg_pf_SuckIt_OBJ.points == 0:
        $ new_request_22_heart = 1
        $ hg_pf_SuckIt_OBJ.hearts_level = 1 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points == 1:
        $ new_request_22_heart = 2
        $ hg_pf_SuckIt_OBJ.hearts_level = 2 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points >= 2:
        $ new_request_22_heart = 3
        $ hg_pf_SuckIt_OBJ.hearts_level = 3 #Event hearts level (0-4)
    if hg_pf_SuckIt_OBJ.points >= 2 and whoring > 21:
        $ hg_pf_SuckIt_OBJ.hearts_level = 4 #Event hearts level (0-4)
    
    $ hg_pf_SuckIt_OBJ.points += 1
    
    $ custom_outfit_old = temp_outfit
    
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.5

    jump end_hg_pf #Hides screens. Hermione walks out. Resets Hermione.
    





