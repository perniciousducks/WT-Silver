

### Hermione Masturbates ###

label hg_pf_TouchYourself: #LV.4 (Whoring = 8 - 10)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TouchYourself_OBJ.points == 0:
        m "{size=-4}(Should I ask her to masturbate?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    $ current_payout = 40 #Used when haggling about price of the favor.
    
    #First time event.
    if hg_pf_TouchYourself_OBJ.points == 0:
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?","base","base") from _call_her_main_4247
        m "Do you ever touch yourself?"
        if whoring < 8:
            jump too_much
            
        $ hg_pf_TouchYourself_OBJ.hearts_level = 1
        
        call her_main("What? why?","upset","wink") from _call_her_main_4248
        m "Do you?"
        call her_main("[genie_name]!","scream","worriedCl") from _call_her_main_4249
        m "It's a simple question [hermione_name]..."
        call her_main("......","normal","worriedCl") from _call_her_main_4250
        call her_main("{size=-5}I do...{/size}","angry","worriedCl",emote="05") from _call_her_main_4251
        m "Huh? What was that?"
        call her_main("I said that I do alright!!!","scream","worriedCl") from _call_her_main_4252
        m "Hmmmm, I'm not sure I believe you..."
        call her_main("What? why would I lie?","annoyed","worriedL") from _call_her_main_4253
        m "I'm not sure..."
        m "But don't worry, I'm sure a quick little demonstration will erase any doubts..."
        call her_main("...{p}And how much will this demonstration earn me?","annoyed","suspicious") from _call_her_main_4254
        
        menu:
            "\"You will get 20 house points.\"":
                $ current_payout = 20
                call her_main("......","annoyed","angryL") from _call_her_main_4255
                call her_main("well I suppose I could.","open","down") from _call_her_main_4256
                call her_main("But you better keep your hands to yourself...","open","down") from _call_her_main_4257
                m "Witcher's promise."
                call her_main("...","annoyed","suspicious") from _call_her_main_4258
            "\"you will get 40 house points.\"":
                $ current_payout = 40
                call her_main(".....","base","base") from _call_her_main_4259
                call her_main("40 house points...?","soft","baseL") from _call_her_main_4260
                her "That could put \"Gryffindor\" back on top..."
                m "so Is that a \"yes\"?"
                call her_main("Yes, it is, [genie_name].","base","squint") from _call_her_main_4261
                m "fantastic!"
            "\"you will get 80 house points!\"":
                call play_music("chipper_doodle") from _call_play_music_169 # HERMIONE'S THEME.
                $ current_payout = 80 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("80 house points?!","scream","wide_stare") from _call_her_main_4262
                m "Is that enough?"
                call her_main("Of course [genie_name]!","smile","happyCl") from _call_her_main_4263
                call her_main("If it's 80 points for Gryffindor then I don't mind giving you a little... show.","smile","happyCl",emote="06") from _call_her_main_4264
       
        call play_music("playful_tension") from _call_play_music_170# SEX THEME.
        call her_main("...........","upset","wink",xpos="mid",ypos="base",trans="fade") from _call_her_main_4265
        call her_main("Do you want me to... start?","upset","wink") from _call_her_main_4266
        m "Maybe take off your top first..."
        call her_main("...","angry","worriedCl",emote="05") from _call_her_main_4267
        call her_main("You want me to strip for you as well as...","angry","worriedCl",emote="05") from _call_her_main_4268
        m "There's an extra 10 points for \"gryffindor\" in it for you."
        $ current_payout += 10
        call her_main("alright... {p}but I'm leaving my skirt on...","upset","wink") from _call_her_main_4269
        hide screen bld1
        with d3
        
        call set_hermione_action("lift_top") from _call_set_hermione_action_108
        pause.5
        
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_109
        pause.5
        
        call her_main("...........","upset","wink") from _call_her_main_4270
        m "Mmmm, that's it, [hermione_name]..."
        
        call her_main("(I can't believe I'm going to do this...)","normal","worriedCl") from _call_her_main_4271 
        
        
        call set_hermione_action("covering_top") from _call_set_hermione_action_110
        call ctc from _call_ctc_262
        
        call play_music("playful_tension") from _call_play_music_171# SEX THEME.
        call nar(">Hermione slowly starts grinding her mound against her hand.") from _call_nar_497
        g9 "Nice..."
        call her_main("........","upset","wink") from _call_her_main_4272 
        m "............."
        call her_main(".............","normal","worriedCl") from _call_her_main_4273
        call her_main("umm... [genie_name]?") from _call_her_main_4274 
        m "Yes, what is it?"
        call her_main("How long do I have to keep doing this?","open","base") from _call_her_main_4275 
        m "Until you finish [hermione_name]..."
        
        if daytime:
            call her_main("What? my classes are about to start [genie_name]...","upset","wink") from _call_her_main_4276
        else: 
            call her_main("What? it's getting pretty late [genie_name]...","upset","wink") from _call_her_main_4277
            
        call her_main("I'm not sure if I'll be able to finish... in time.","upset","wink") from _call_her_main_4278
        m "Do you need the points or not?"
        call her_main("I do, [genie_name]! I'm sorry...","open","down") from _call_her_main_4279
        call her_main("I'll just keep ...going...","disgust","down_raised") from _call_her_main_4280
        m "(Hmmm, I might have to give her a little encouragement.)"
        
        #MAIN FAVOUR MENU
        label TouchYourself_menu:
        menu:
            m "..."
            "\"That's it slut, keep going.\"":
                call her_main("[genie_name]!!!","angry","angry") from _call_her_main_4281
                call her_main("How dare you!") from _call_her_main_4282
                m "what?"
                call her_main("I hardly think that language is appropriate.","upset","wink") from _call_her_main_4283 
                m "And masturbating in front of your headmaster is?"
                call her_main("Well... this is different.","open","down") from _call_her_main_4284
                call her_main("I'm doing this for the honor of \"gryffindor\"...") from _call_her_main_4285
                call her_main("To help my--") from _call_her_main_4286
                call nar(">You notice how she's starting to grind her hips a little faster.") from _call_nar_498
                $ hermione_dribble = True
                call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","soft","ahegao") from _call_her_main_4287
                call her_main("My classmates win the house cup...","angry","wink") from _call_her_main_4288
                m "Are you sure that's the only reason slut?"
                call her_main("I don't know--","normal","worriedCl") from _call_her_main_4289
                call her_main("ah-a{image=textheart}...","open","worriedCl") from _call_her_main_4290
                call her_main("I don't know what you mean, [genie_name]...","angry","down_raised") from _call_her_main_4291
                m "It seems to me that you might be enjoying this a little too much..."
                call her_main("I am not, [genie_name]!","open","worriedCl") from _call_her_main_4292
                m "Really?"
                call her_main("......................","normal","worriedCl") from _call_her_main_4293
                m "Then why is your pussy so wet slut?"
                call ctc from _call_ctc_263
                
                call her_main("ah...{image=textheart}","open","worriedCl") from _call_her_main_4294
                m "ha! just Admit it, you enjoy being called a slut!"
                call her_main("I do not!","normal","worriedCl") from _call_her_main_4295
                call her_main("Aha...{image=textheart}","open","worriedCl") from _call_her_main_4296 
                call her_main("I'm just thinking about how happy everyone will be when we win!","shock","worriedCl") from _call_her_main_4297
                m "and what if they find out how you earned the points?"
                call her_main("what?!","shock","wide") from _call_her_main_4298
                m "then it wouldn't just be me degrading you..."
                call her_main("...","soft","squintL") from _call_her_main_4299
                m "It would be the whole school."
                call her_main("ah...{image=textheart}","silly","dead") from _call_her_main_4300
                m "Little. miss. slut."
                call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4301
                call her_main("[genie_name], please... don't tell anyone...","angry","wink") from _call_her_main_4302 
                call nar(">Hermione keeps on grinding her hips against her hand...") from _call_nar_499
                call her_main("they can't find out...","angry","base") from _call_her_main_4303
                call her_main("if harry and ron knew...","angry","down_raised") from _call_her_main_4304
                call her_main("i'd... ah...{image=textheart}","soft","ahegao") from _call_her_main_4305
                m "You'd what [hermione_name]?"
                call her_main("I'd...","open","worriedCl") from _call_her_main_4306
                call her_main("I'd...{image=textheart}","shock","worriedCl") from _call_her_main_4307
                call her_main("I...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4308
            
            "\"Play with your breasts\"" if hg_pf_TouchYourself_OBJ.points > 0:
                call her_main("my breasts...","open","down") from _call_her_main_4309
                call set_hermione_action("covering_top") from _call_set_hermione_action_111
                
                call her_main("I'm not sure if I should--","clench","down_raised") from _call_her_main_4310
                m "There's another 10 points for \"gryffindor\" in it for you..."
                $ current_payout += 10
                call her_main("...","soft","squintL") from _call_her_main_4311
                call her_main("......","soft","squintL") from _call_her_main_4312
                call set_hermione_action("lift_breasts") from _call_set_hermione_action_112
                
                call her_main("ah...{image=textheart}","open","baseL") from _call_her_main_4313
                m "There... Isn't that better?"
                $ hermione_dribble = True
                call her_main("Ah... y-yes...{image=textheart}","grin","ahegao") from _call_her_main_4314
                call h_action("covering_top") from _call_h_action_71
                call her_main("Mmmm...","smile","happyCl") from _call_her_main_4315
                m "That's it..."
                call h_action("lift_breasts") from _call_h_action_72
                call her_main("[genie_name], do you mind...","base","ahegao_raised") from _call_her_main_4316
                m "What [hermione_name]?"
                call her_main("Could you... Call me names...","open","ahegao_raised",cheeks="blush") from _call_her_main_4317
                m "Such as?"
                call set_hermione_action("covering_top") from _call_set_hermione_action_113
                
                call her_main("...{p}{size=-5}Slut...{/size}{p}Only if it's not too much...","base","ahegao_raised",cheeks="blush") from _call_her_main_4318
                m "You little whore..."
                call her_main("Ah...{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4319
                m "What would your parents think if they saw this?"
                call her_main("i-{image=textheart}","base","ahegao_raised",cheeks="blush") from _call_her_main_4320
                call set_hermione_action("lift_breasts") from _call_set_hermione_action_114
                
                call her_main("Ah...{image=textheart} I don't know...","base","ahegao_raised",cheeks="blush") from _call_her_main_4321
                call her_main("To be perfectly honest [genie_name]... I don't think I care...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_4322
                m "Really?"
                call set_hermione_action("covering_top") from _call_set_hermione_action_115
                
                call her_main("Really...{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_4323
                m "Would you at least stop?"
                call her_main("Ah...{image=textheart}","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_4324
                call set_hermione_action("lift_breasts") from _call_set_hermione_action_116
                
                call her_main("Maybe....","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_4325
                call her_main("I'm not sure...","open","baseL",cheeks="blush") from _call_her_main_4326
                call set_hermione_action("covering_top") from _call_set_hermione_action_117
                
                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_4327

            "\"Take off your skirt\"" if hg_pf_TouchYourself_OBJ.points > 0:
                call her_main("Excuse me?","soft","wide") from _call_her_main_4328 
                m "You heard me, [hermione_name]..."
                call her_main("........","annoyed","angryL",cheeks="blush") from _call_her_main_4329
                call her_main("............","disgust","down_raised",cheeks="blush") from _call_her_main_4330 
                call her_main("*sigh!*..............","open","ahegao_raised",cheeks="blush") from _call_her_main_4331
                call her_main("Well, I might as well, I suppose...") from _call_her_main_4332
                call nar(">Hermione stops masturbating and slowly pulls down her skirt.") from _call_nar_500

                $ hermione_wear_bottom = False
                call set_hermione_action("covering") from _call_set_hermione_action_118
                
                call her_main("...","open","down") from _call_her_main_4333 
                m "That's not so bad now, is it?"
                call her_main("No, I suppose not...","upset","wink") from _call_her_main_4334 
                m "Well, back to work..."
                call her_main("...","normal","worriedCl") from _call_her_main_4335 
                call her_main("Well, alright...","base","ahegao_raised",cheeks="blush") from _call_her_main_4336
                m "Good... Just keep playing with that slutty little pussy of yours!"
                call her_main("[genie_name]!","mad","angry",cheeks="blush") from _call_her_main_4337
                m "What?"
                $ hermione_dribble = True
                call her_main("It's not {size=-5}slutty...{/size}","annoyed","angryL",cheeks="blush") from _call_her_main_4338 
                m "Are you sure? Because from where I'm sitting it looks nice and wet."
                call her_main("Ah...{image=textheart}","base","ahegao_raised",cheeks="blush") from _call_her_main_4339 
                call her_main("It's just sweat [genie_name]...","open","baseL",cheeks="blush") from _call_her_main_4340 
                m "Whatever you say..."
                call her_main("...............","base","ahegao_raised",cheeks="blush") from _call_her_main_4341 
                m "{size=-5}Slut.{/size}"
                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_4342
                call her_main("Sir... please...","open","baseL",cheeks="blush") from _call_her_main_4343
                call set_hermione_action("pinch") from _call_set_hermione_action_119
                
                call nar(">Hermione starts gently fingering herself.") from _call_nar_501
                m "Very good..."
                call her_main("...{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_4344
                call her_main("Ah...{image=textheart}","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_4345
                m "That's it slut. Try going a little deeper...."
                call her_main("...","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_4346
                call set_hermione_action("covering") from _call_set_hermione_action_120
                
                call her_main("Mmmm...{image=textheart}","scream","worriedCl",cheeks="blush") from _call_her_main_4347


        if hg_pf_TouchYourself_OBJ.points == 0: #HERMIONE DOESN'T CUM
                call her_main("Ah...","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_4348
                m "almost there [hermione_name]?"
                call her_main("a-almost...","clench","worried",cheeks="blush",tears="soft") from _call_her_main_4349
                call her_main("I just need a bit longer...") from _call_her_main_4350
                m "well you better hurry..."
                call her_main("Ah... i know, [genie_name].","mad","worriedCl",tears="soft_blink") from _call_her_main_4351
                call her_main("...........","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_4352
                m "is everything alright?"
                call her_main("................","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_4353
                m "Why are you being so quiet [hermione_name]?"
                call her_main("......","clench","worried",cheeks="blush",tears="soft") from _call_her_main_4354
                call her_main("[genie_name]... I don't think I can...") from _call_her_main_4355
                m "what?"
                call her_main("...finish...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_4356
                
                menu:
                    "-Chastise her-":
                        m "Well then I guess \"Slytherin\" will have to win the house cup this year."
                        call her_main("B-but--","scream","wide") from _call_her_main_4357
                        m "now, now [hermione_name], a deals a deal."
                        call her_main("Really?","open","worriedCl") from _call_her_main_4358
                        call her_main("but I'm trying [genie_name]...","shock","worriedCl") from _call_her_main_4359
                        m "try harder..."
                        call nar(">Hermione starts grinding furiously against hand") from _call_nar_502
                        call her_main("*SOB!* i can't...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_4360
                        m "well then, 0 points to \"Gryffindor\"..."
                        call her_main("{size=-5}After all...{/size} Really [genie_name]?","clench","worried",cheeks="blush",tears="soft") from _call_her_main_4361
                        call her_main("After I stood here and...","scream","angry",cheeks="blush",tears="messy") from _call_her_main_4362
                        call her_main("..........","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_4363
                        call nar(">Hermione wipes the tears from her eyes.") from _call_nar_503
                        call her_main("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry",cheeks="blush") from _call_her_main_4364
                        
                        $ mad += 15
                        jump end_touch_yourself
                        
                    "-Forgive her-":
                        m "It's alright, [hermione_name]."
                        call her_main("Really?","open","surprised",cheeks="blush",tears="messy") from _call_her_main_4365
                        m "I'm sure you're just a little nervous."
                        call her_main("Thank you [genie_name].","clench","worried",cheeks="blush",tears="soft") from _call_her_main_4366
                        call her_main("I promise to try harder next time.","scream","worriedCl",cheeks="blush",tears="messy") from _call_her_main_4367
                        
        else: #HERMIONE CUMS
            $ hg_pf_TouchYourself_OBJ.hearts_level = 2
            call her_main("A-ha... {image=textheart}ah...","open","worriedCl") from _call_her_main_4368
            call her_main("Ah... {image=textheart}-aha...","open","worriedCl") from _call_her_main_4369
            m "..."
            call her_main("Ah-ah...","open","worriedCl") from _call_her_main_4370
            m "......................"
            call her_main("Ah... ah...{image=textheart}","open","worriedCl") from _call_her_main_4371
            call her_main("Ah... [genie_name]?","soft","squintL") from _call_her_main_4372
            m "What is it?"
            call her_main("Ah... Do you.... like this?","open","worriedCl") from _call_her_main_4373
            m "Do I like watching you finger your slutty little pussy?"
            m "Very much so, [hermione_name]. Why?"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","normal","worriedCl") from _call_her_main_4374
            call her_main("Ah... You're just so quiet...","open","worriedCl") from _call_her_main_4375
            m "Do you need a little more encouragement?"
            call her_main("Ah... yes... please....{image=textheart}","open","worriedCl") from _call_her_main_4376
            m "Tch... You nasty whore!"
            call her_main("yes [genie_name], ah...{image=textheart}","grin","aheagao_mad",cheeks="blush") from _call_her_main_4377
            call her_main("please... ah... more...{image=textheart}","grin","angry",cheeks="blush") from _call_her_main_4378
            g4 "You need to be punished for being such a slut!"
            call her_main("yes, [genie_name]... punish me...","open","ahegao_raised",cheeks="blush") from _call_her_main_4379
            call her_main("make me your little slut....","open","ahegao_raised",cheeks="blush") from _call_her_main_4380
            call her_main("I will... ah... {image=textheart}do anything... ah...{image=textheart}","silly","dead") from _call_her_main_4381
            m "Anything [hermione_name]?"
            call her_main("Ah-a...{image=textheart} yessss...","silly","ahegao_raised",cheeks="blush") from _call_her_main_4382
            m "Cum."
            $ hermione_squirt = True
            call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","body_133b") from _call_her_main_4383
            
            call cum_block from _call_cum_block_47
            
            $ hermione_squirt = False
            call her_main("Ah...{image=textheart}...{image=textheart}","grin","ahegao") from _call_her_main_4384
            call her_main("Ah... ah...{image=textheart}","silly","ahegao") from _call_her_main_4385
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4386
            call her_main("*heavy panting*","open_wide_tongue","ahegao") from _call_her_main_4387
            call her_main("[genie_name]...{image=textheart}{image=textheart}{image=textheart}", "body_135") from _call_her_main_4388
            call her_main(".............","soft","ahegao") from _call_her_main_4389
            call nar(">Hermione takes a minute to collect herself.") from _call_nar_504
            m "You feeling alright?"
            call her_main("Yes, [genie_name]... I just need a little longer...","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_4390
            m "take your time."
            call her_main("ah... {image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_main_4391

    #Second time event.
    elif hg_pf_TouchYourself_OBJ.points == 1: # SECOND EVENT
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?","base","base") from _call_her_main_4392
        m "Are you feeling horny?"
        call her_main("maybe A little, [genie_name].","base","glance") from _call_her_main_4393
        m "Ah, well perhaps we can fix that..."
        call her_main("[genie_name]...","open","worriedCl") from _call_her_main_4394
        m "[hermione_name], I would like to buy yet another favour from you today."
        call her_main("Of course, [genie_name].","base","down") from _call_her_main_4395
        g9 "The favour being you playing with that slutty little pussy of yours!"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4396
        call her_main(".............","soft","ahegao") from _call_her_main_4397
        call her_main("Alright...","base","down") from _call_her_main_4398
        
        call her_main("","base","glance",xpos="mid",ypos="base",trans="fade") from _call_her_main_4399
        call set_hermione_action("lift_top") from _call_set_hermione_action_121
        pause.5
        
        call her_main("...........","upset","wink") from _call_her_main_4400
        m "Mmmm, that's it [hermione_name]..."
        
        call her_main("(I can't believe I'm going to do this... again...)","angry","down_raised") from _call_her_main_4401 
        call set_hermione_action("covering_top") from _call_set_hermione_action_122
        call ctc from _call_ctc_264
        
        call play_music("playful_tension") from _call_play_music_172# SEX THEME.
        call nar(">Hermione slowly starts grinding her mound against her hand.") from _call_nar_505
        g9 "Nice..."
        call her_main("........","grin","ahegao") from _call_her_main_4402 
        

        jump TouchYourself_menu


    #Third time event.
    elif hg_pf_TouchYourself_OBJ.points >= 2:
        $ hg_pf_TouchYourself_OBJ.hearts_level = 3 #Event hearts level (0-3)
        
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base") from _call_her_main_4403
        m "You don't mind pleasuring yourself in front of me, do you?"
        if whoring <= 16:
            call her_main("As long as I am being paid...","grin","baseL") from _call_her_main_4404
            m "Well, come on then. Time to earn those points."
        else:
            call her_main("I mean I have done it once today already...","grin","baseL") from _call_her_main_4405
            m "Once more for good luck then!"
            call her_main("If you insist...{image=textheart}","open","baseL",cheeks="blush") from _call_her_main_4406
        
        call her_main("","base","glance",xpos="mid",ypos="base",trans="fade") from _call_her_main_4407
        call set_hermione_action("lift_top") from _call_set_hermione_action_123
        pause.5
        
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_124
        pause.5
        
        call her_main("(I can't believe I'm doing this... again...)","base","baseL",cheeks="blush") from _call_her_main_4408 
        m "Now the skirt."
        
        call set_hermione_action("lift_skirt") from _call_set_hermione_action_125
        pause.5
        
        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_126
        pause.5
        
        call her_main("...","base","glance") from _call_her_main_4409 
        call set_hermione_action("covering") from _call_set_hermione_action_127
        
        stop music fadeout 3.0
        call her_main("Do you like it when I do it like this, [genie_name]?","grin","baseL") from _call_her_main_4410
        call play_music("chipper_doodle") from _call_play_music_173 # HERMIONE'S THEME.

        m "Yes, yes, like that..."
        m "Try going a little deeper with your fingers."
        call her_main("Alright [genie_name]...","base","happyCl") from _call_her_main_4411
        $ hermione_dribble = True
        call her_main("Ah... ah...{image=textheart}","open","worriedCl") from _call_her_main_4412
        call her_main("Ah... [genie_name]...{image=textheart}","open","worriedCl") from _call_her_main_4413
        
        menu:
            m "..."
            "\"What are you thinking about?\"":
                call her_main("Huh?","open","worriedCl",cheeks="blush") from _call_her_main_4414
                call her_main("Oh, um... nothing...","upset","worriedCl",cheeks="blush") from _call_her_main_4415      
                m "[hermione_name]..."
                call her_main("[genie_name], please, it's too embarrassing...","disgust","down_raised",cheeks="blush") from _call_her_main_4416         
                g4 "Well now I have to hear it."
                call her_main("OK... but you have to promise not to tell anyone!","open","baseL",cheeks="blush") from _call_her_main_4417         
                m "Witcher's honor."
                call her_main("......","annoyed","annoyed") from _call_her_main_4418         
                m "[hermione_name]..."
                call her_main("Alright. If you must know... I'm remembering the time I corrected professor Snape about the ingredients of a Hiccoughing potion.","open","down") from _call_her_main_4419      
                m "....."
                call her_main("ah...{image=textheart}","soft","ahegao") from _call_her_main_4420
                call set_hermione_action("pinch") from _call_set_hermione_action_128
                
                call her_main("It was ah... {image=textheart} in front of the entire class as well.") from _call_her_main_4421
                call set_hermione_action("covering") from _call_set_hermione_action_129
                
                call her_main("He refused to let me answer any questions for a week after that.","base","down") from _call_her_main_4422       
                call her_main("But it was worth it...","soft","squintL") from _call_her_main_4423      
                call her_main("The look on his face when he realised he was wrong...{image=textheart}","soft","ahegao") from _call_her_main_4424
                call set_hermione_action("pinch") from _call_set_hermione_action_130
                
                call her_main("a-ah...{image=textheart}") from _call_her_main_4425
                call set_hermione_action("covering") from _call_set_hermione_action_131
                
                call her_main("It just felt so good!{image=textheart}","grin","dead") from _call_her_main_4426 
                m "OK, I think that's enough..."
                call her_main("Was it too much?","angry","wink") from _call_her_main_4427            
                m "Let's just get back to business shall we?"
                call her_main(".................","soft","ahegao") from _call_her_main_4428  
                call nar(">Hermione keeps on plunging her fingers into herself.","start") from _call_nar_506
                call nar(">She is doing a great job of it too.","end") from _call_nar_507
                m "Yes, yes... Like that."
                
            "\"You really are a shameless slut, aren't you?\"":
                call her_main("Yes...","soft","ahegao") from _call_her_main_4429
                call set_hermione_action("pinch") from _call_set_hermione_action_132
                
                call her_main("ah... {image=textheart}","silly","dead") from _call_her_main_4430 
                call her_main("I don't know if it's the time I'm spending with you...{image=textheart}","angry","wink") from _call_her_main_4431
                call her_main("Or if i've always been this way...{image=textheart}","angry","down_raised") from _call_her_main_4432
                call her_main("But... {image=textheart} ah... {image=textheart} I'm a slut [genie_name]...{image=textheart}","soft","ahegao") from _call_her_main_4433 
                call her_main("A shameless slut...","grin","dead") from _call_her_main_4434
                call her_main("That pleasures herself...{image=textheart} ah...","soft","ahegao") from _call_her_main_4435
                call her_main("Just to make her headmaster happy...","grin","dead") from _call_her_main_4436
                m "Oh, yes..."
                call her_main("That's it [genie_name]...","base","down") from _call_her_main_4437
                call her_main("Enjoy yourself while I stand here...","silly","dead") from _call_her_main_4438
                call her_main("Ah...{image=textheart}","open_wide_tongue","ahegao") from _call_her_main_4439
                call her_main("Fingering my pussy...","silly","ahegao") from _call_her_main_4440
                call her_main("Ah... ah...{image=textheart}","grin","ahegao") from _call_her_main_4441
                call her_main("Ah... Do you.... like this [genie_name]?","shock","worriedCl") from _call_her_main_4442
                call her_main("Watching me Ah...{image=textheart} degrade myself?","silly","dead") from _call_her_main_4443
                m "Very much, [hermione_name]. Just keep going..."
                call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_main_4444
                
            "\"Play with your tits some more!\"":
                call her_main("Hm?","soft","ahegao") from _call_her_main_4445
                call her_main("alright... if you insist...","open","baseL",cheeks="blush") from _call_her_main_4446
                call set_hermione_action("pinch") from _call_set_hermione_action_133
                
                call her_main("ah...{image=textheart}","angry","wink") from _call_her_main_4447
                m "Now lift them up."
                call her_main("[genie_name]...","open","squint",cheeks="blush") from _call_her_main_4448    
                m "do it, [hermione_name]."
                call her_main("...","open","baseL",cheeks="blush") from _call_her_main_4449
                call set_hermione_action("lift_breasts_naked") from _call_set_hermione_action_134
                
                call her_main("Mmmm...","grin","aheagao_mad",cheeks="blush") from _call_her_main_4450
                m "That's it..."
                call nar(">You stare at Hermione's breasts with hunger...") from _call_nar_508
                call her_main("ah...","silly","dead") from _call_her_main_4451
                m "So do you like playing with those tits of yours, [hermione_name]?"
                call her_main("I do, [genie_name]... ah...{image=textheart}","soft","ahegao") from _call_her_main_4452
                call her_main("I don't know why...","base","baseL",cheeks="blush") from _call_her_main_4453
                call set_hermione_action("pinch") from _call_set_hermione_action_135
                
                call her_main("But I love it...{image=textheart}{image=textheart}","base","down") from _call_her_main_4454
                m "You nasty slut!"
                call her_main("Ah...{image=textheart} ah-a...{image=textheart}","open_wide_tongue","ahegao") from _call_her_main_4455
                call her_main("I am...") from _call_her_main_4456
                call her_main("A nasty slut... Ah...{image=textheart}", "body_133") from _call_her_main_4457
                m "You are a disgrace, [hermione_name]!"
                call her_main("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao") from _call_her_main_4458
                
        m "Why don't you come a little closer?"
        call her_main("...","base","down") from _call_her_main_4459
        
        call her_walk_desk_blkfade from _call_her_walk_desk_blkfade_18
        
        ">Hermione slowly walks towards your desk and stands in front of you."
        
        show screen desk
        show screen chair_left
        hide screen genie
        $ genie_chibi_xpos = -217
        $ genie_chibi_ypos = 13
        $ g_c_u_pic = "images/animation/grope_e_01.png"
        show screen g_c_u
        
        hide screen blktone
        hide screen bld1
        call hide_blkfade from _call_hide_blkfade_101
        call ctc from _call_ctc_265
        
        call set_hermione_action("lift_breasts_naked") from _call_set_hermione_action_136
        call her_main("..............","base","ahegao_raised",cheeks="blush") from _call_her_main_4460
        
        menu:
            m "..."
            "-Grab her tits-":
                call nar(">You reach forward and grab a hold of her supple breasts.") from _call_nar_509
                $ g_c_u_pic = "groping_naked_tits_ani"
                call set_hermione_action("fingering") from _call_set_hermione_action_137
                
                call her_main("[genie_name]!","shock","worriedCl") from _call_her_main_4461
                call her_main("This wasn't part of the deal!","open","worriedCl") from _call_her_main_4462
                call her_main("I don't think we should...","annoyed","angryL",cheeks="blush") from _call_her_main_4463
                m "Don't worry [hermione_name], You can keep playing with yourself."
                m "This is just to hurry things along."
                call her_main("Ah...{image=textheart} Well, as long as it's just to make this end faster...","open","ahegao_raised",cheeks="blush") from _call_her_main_4464
                call her_main("I suppose I can... ah{image=textheart} allow it...","base","baseL",cheeks="blush") from _call_her_main_4465
                call nar(">You give her tits a couple of firm squeezes...") from _call_nar_510
                m "Just admit that you love it."
                call her_main("Ah... fine...{image=textheart}","open","worriedCl",cheeks="blush") from _call_her_main_4466
                call her_main("{size=-5}I like it...{/size}","soft","ahegao") from _call_her_main_4467
                m "What was that [hermione_name]?"
                call her_main(".......") from _call_her_main_4468
                call her_main("I love this...","grin","dead") from _call_her_main_4469
                call her_main("Standing here... playing with myself...","base","down") from _call_her_main_4470
                call her_main("Ah... while you play with me...{image=textheart}","grin","aheagao_mad",cheeks="blush") from _call_her_main_4471
                m "Heh... Nice."
                call her_main("Ah...{image=textheart}","open","ahegao_raised",cheeks="blush") from _call_her_main_4472
                call her_main("I sometimes wish I could spend all day in here...","grin","angry",cheeks="blush") from _call_her_main_4473
                m "Mmmm"
                call nar(">You keep on massaging the girl's breasts...") from _call_nar_511
                call her_main(".......") from _call_her_main_4474
                call her_main("[genie_name]... I know it's greedy of me...","base","baseL",cheeks="blush") from _call_her_main_4475
                call her_main("ah...{image=textheart}","base","down") from _call_her_main_4476
                call her_main("but could you touch me... down there...","open","squint",cheeks="blush") from _call_her_main_4477
                m "What's was that [hermione_name]? You'll have to speak up."
                call her_main("Please finger me...","open","ahegao_raised",cheeks="blush") from _call_her_main_4478
                m "Once more, a little louder this time."
                call her_main("Ah...{image=textheart} {size=+5}please finger my cunt!{/size}","grin","aheagao_mad",cheeks="blush") from _call_her_main_4479
                $ g_c_u_pic = "groping_06"
                call nar(">You swiftly plunge two fingers into her dripping pussy.") from _call_nar_512
                call h_action("lift_breasts_naked") from _call_h_action_73
                call her_main("{image=textheart}{image=textheart}{size=+5}!!!{/size}{image=textheart}{image=textheart}","silly","ahegao") from _call_her_main_4480
                
            "-Finger her-":
                $ g_c_u_pic = "groping_06"
                call nar(">You run your hands up and down Hermione's legs...") from _call_nar_513
                call her_main("!!!","open","worriedCl") from _call_her_main_4481
                call nar(">And slowly move your hands towards her pussy...") from _call_nar_514
                call her_main(".................","silly","dead") from _call_her_main_4482
                m "That's it [hermione_name]..."
                call her_main("{size=-7}[genie_name]...{/size}","soft","ahegao") from _call_her_main_4483
                m "Shhh. Just play with your tits."
                call her_main("...fine, [genie_name]...","base","ahegao_raised",cheeks="blush") from _call_her_main_4484
                m "Good girl."
                call her_main("....................","base","closed") from _call_her_main_4485
                m "Just be quiet..."
                call nar(">you enjoy the sensation of gently stroking the inside of her thighs...") from _call_nar_515
                m "as my hands explore you"
                m "your thighs..."
                call nar(">your start kneading the flesh of her thighs, moving ever closer to her dripping cunt") from _call_nar_516
                m "your big, firm ass"
                call nar(">You move around and squeeze her ass gently...") from _call_nar_517
                call her_main(".....................","grin","ahegao") from _call_her_main_4486
                m "your loins..."
                call nar(">You move one hand back around, and start circling just above her clit.") from _call_nar_518
                call her_main(".....................{size=-8}[genie_name]...{/size}","silly","dead") from _call_her_main_4487
                m "What was that, [hermione_name]?"
                call her_main(".....................","annoyed","wink",cheeks="blush") from _call_her_main_4488
                call her_main("...i... {size=-5}...i need you... inside of me...{/size}","disgust","down_raised",cheeks="blush") from _call_her_main_4489
                m "You'll have to speak up if you expect me to hear you..."
                call her_main("I... ah...{image=textheart} need...","open","ahegao_raised",cheeks="blush") from _call_her_main_4490
                call nar(">You swiftly plunge two fingers into her drenched snatch.") from _call_nar_519
                call her_main("!!!{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_4491
                call nar(">you start to pump your fingers inside her before she can do more than gasp") from _call_nar_520
                call her_main("{size=+10}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}","silly","dead") from _call_her_main_4492
                m "That's it [hermione_name]. Just enjoy yourself."
                call her_main("..................................................","base","ahegao_raised",cheeks="blush") from _call_her_main_4493
                m "do you like this?"
                m "you like it when i finger your cunt?"
                call her_main("i love it!{image=textheart} i love your fingers in my tight, wet pussy!!{image=textheart}","silly","ahegao") from _call_her_main_4494
                m "well, i think we can do better."
                call nar(">with your other hand, you start rubbing the base of your palm against her clit.") from _call_nar_521
                call her_main("{size=+10}!!!{/size}","open","ahegao_raised",cheeks="blush") from _call_her_main_4495


        call nar(">you don't even need to move as she pounds herself against your fingers.") from _call_nar_522
        call her_main("ah...{image=textheart} please...{image=textheart} keep...{image=textheart}","silly","dead","blush") from _call_her_main_4496
        call her_main("fingering my cunt!{image=textheart}{image=textheart}","silly","ahegao","blush") from _call_her_main_4497
        g9 "As you command!"
        call nar(">you force another finger into her pussy!") from _call_nar_523
        call her_main("ah yes... {image=textheart}iloveitiloveitiloveit","grin","ahegao","blush") from _call_her_main_4498
        m "what do you love, [hermione_name]?"
        call her_main("ah!!{image=textheart} I love your fingers in my pussy [genie_name]!{image=textheart}","open_wide_tongue","ahegao","blush") from _call_her_main_4499
        call nar(">her movements are becoming more frantic") from _call_nar_524
        m "are you cumming, [hermione_name]?"
        call her_main("ah...{image=textheart} yes!!","grin","ahegao") from _call_her_main_4500
        call her_main("I'm cumming [genie_name]!!{image=textheart}","grin","dead") from _call_her_main_4501
        call her_main("I'm cumming from being fucked with your fingers!!{image=textheart}{image=textheart}","grin","aheagao_mad",cheeks="blush") from _call_her_main_4502
        m "show me your tits [hermione_name]!"
        m "I want to see you cum while you play with them."
        $ hermione_squirt = True
        call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","body_133b") from _call_her_main_4503
        
        call cum_block from _call_cum_block_48
        
        $ hermione_squirt = False
        call her_main("Ah...{image=textheart}...{image=textheart}","grin","ahegao") from _call_her_main_4504
        call her_main("Ah... ah...{image=textheart}","silly","ahegao") from _call_her_main_4505
        call her_main("...........","silly","ahegao") from _call_her_main_4506
        call her_main("........................","silly","ahegao") from _call_her_main_4507
        call nar(">You release her...") from _call_nar_525
        $ g_c_u_pic = "images/animation/grope_e_01.png"
        m "This will do for now [hermione_name]."
    
    
    label end_touch_yourself:
    hide screen hermione_main
    call blkfade from _call_blkfade_143
    ">Hermione quickly puts her clothes back on."
    
    call h_action("none") from _call_h_action_74 #Resets clothes.
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") from _call_her_chibi_146
    pause.1
    
    hide screen blktone
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_102
    pause.5

    if whoring < 19:
        call her_main("Now about my payment.","scream","surprised",cheeks="blush",tears="messy",xpos="right",ypos="base") from _call_her_main_4508
        m "Yes, yes, [hermione_name]. [current_payout] to \"Gryffindor\"." 
        $ gryffindor +=current_payout

    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base") from _call_her_main_4509
    
    if whoring < 14: #Adds points till 14.
        $ whoring +=1
    
    $ hg_pf_TouchYourself_OBJ.points += 1
    
    if hg_pf_TouchYourself_OBJ.points == 1:
        $ new_request_16_heart = 1
        $ hg_pf_TouchYourself_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_TouchYourself_OBJ.points == 2:
        $ new_request_16_heart = 2
        $ hg_pf_TouchYourself_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_TouchYourself_OBJ.points == 3:
        $ new_request_16_heart = 3
        $ hg_pf_TouchYourself_OBJ.hearts_level = 3 #Event hearts level (0-3)
    
    
    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
    
    

