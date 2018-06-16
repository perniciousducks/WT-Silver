

label hg_pf_LetsHaveSex: #LV.7 (Whoring = 18 - 20)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Should I ask her to have sex with me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_laraCroft_OBJ.purchased and hg_pf_SuckIt_OBJ.points >= 1:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL") from _call_her_main_946
                m "As who. I want you to dress up as Lara Croft"
                if whoring >= 22:
                    call her_main("Who?","open","base") from _call_her_main_947
                    m "She's a video game character."
                    call her_main("...","annoyed","down") from _call_her_main_948
                    call her_main("Whatever, let me go change.","annoyed","base") from _call_her_main_949
                    call play_sound("door") from _call_play_sound_42 #Sound of a door opening.
                    call set_hermione_outfit(hg_laraCroft_OBJ) from _call_set_hermione_outfit_8
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_ani"
    
    call bld from _call_bld_43
    
    if whoring < 18:
        m "[hermione_name]..."
        m "Why don't you come over here and I pound your pussy for a bit..."
        g9 "With my cock!"
        jump too_much
        
    #First Event.
    if hg_pf_LetsHaveSex_OBJ.points == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base") from _call_her_main_950
        m "The favour I will be buying from you today..."
        call her_main(".......?","base","base") from _call_her_main_951
        m "How should I put this delicately...?"
        call her_main("Is it sex, [genie_name]?","base","suspicious") from _call_her_main_952
        m "Well, yes. How did you...?"

        call her_main("Not a terribly difficult deduction all things considered...","base","glance") from _call_her_main_953
        m "You don't mind then?"
        call her_main("Of course, I mind, [genie_name]!","upset","closed") from _call_her_main_954
        her "I am not a prostitute!"
        m "But you'll do it anyway??"
        call her_main("\"Gryffindor\" is falling behind again...","open","closed") from _call_her_main_955
        her "What choice do I have...?"
        m "Great!"
        
        label your_ass:
        hide screen hermione_main
        call blkfade from _call_blkfade_27
        
        stop music fadeout 1.0
        call gen_chibi("hide") from _call_gen_chibi_8
        call her_chibi("hide") from _call_her_chibi_24
        
        call her_head(".............","upset","closed") from _call_her_head_184
        call her_head("!!!!!!!!!!!!!!!","angry","wide") from _call_her_head_185
        m "Relax, [hermione_name]. I'm Just gonna take off your panties."
        call her_head("..............","angry","angry") from _call_her_head_186
        m "Are you ready?"
        call her_head("No...","annoyed","annoyed") from _call_her_head_187
        m "Good girl."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide") from _call_her_head_188
        
        call gen_chibi("hide") from _call_gen_chibi_9
        call her_chibi("hide") from _call_her_chibi_25
        hide screen genie
        show screen chair_left
        show screen g_c_u
        
        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","normal","worriedCl") from _call_her_head_189
            show screen ccg
        
        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_47
        
           
        call play_music("playful_tension") from _call_play_music_50# SEX THEME.
        
        #FUCKING
        g4 "Your pussy... It's so tight."
        call her_head("................","normal","worriedCl") from _call_her_head_190
        m "You alright?"
        call her_head("A-ha... It's too big...","angry","base",tears="soft") from _call_her_head_191
        call her_head("You will rip me apart, [genie_name]!") from _call_her_head_192
        m "Nonsense! My cock is of a regular size."
        m "It's not my fault that you are so tiny."
        call her_head("......................","normal","worriedCl") from _call_her_head_193
        
        menu:
            "\"You should be ashamed of yourself!\"":
                #$ ccg2 = 20
                call her_head("I am not ashamed, [genie_name]!","normal","worriedCl") from _call_her_head_194
                call her_head("I am doing this for the sake my house!") from _call_her_head_195
                call her_head("To help my--") from _call_her_head_196
                call her_head("ah-ha-a...","open","worriedCl") from _call_her_head_197
                call her_head("My classmates depend on me... ah-a...") from _call_her_head_198
                m "Are you sure that's the only reason?"
                call her_head("I don't know--","normal","worriedCl") from _call_her_head_199
                call her_head("ah-a...","open","worriedCl") from _call_her_head_200
                call her_head("I don't know what you mean, [genie_name].","angry","down_raised") from _call_her_head_201
                m "It seems to me that you are enjoying this a little bit too much."
                #$ ccg2 = 21
                call her_head("I'm not, [genie_name]!","angry","down_raised") from _call_her_head_202
                m "Really?"
                call her_head("......................","normal","worriedCl") from _call_her_head_203
                m "Then why is your pussy so wet?"
                call her_head("....................a-ha.{image=textheart}","open","worriedCl") from _call_her_head_204
                m "Admit it, you enjoy getting fucked by your [genie_name]!"
                #$ ccg2 = 25
                call her_head("I do not!","normal","worriedCl") from _call_her_head_205
                m "Stubborn girl..."
                call her_head("Aha...{image=textheart}","open","worriedCl") from _call_her_head_206 
            "\"So... What's new in your life?\"":
                #$ ccg2 = 14
                call her_head("...[genie_name]?","open","base") from _call_her_head_207
                m "Just trying to have a polite conversation."
                #$ ccg2 = 17
                call her_head("Ah-ah... But... ah...","open","base") from _call_her_head_208
                m "Any news from your folks?"
                call her_head("My parents?","angry","worriedCl",emote="05") from _call_her_head_209
                call her_head("[genie_name], please, I cannot talk...","open","worriedCl") from _call_her_head_210
                m "Why not? Enjoying this too much?"
                call her_head("I am not... ah...{image=textheart}","open","worriedCl") from _call_her_head_211
                m "I think you are."
                call her_head("I am only doing this for the points, [genie_name]...","open","worriedCl") from _call_her_head_212
                m "Oh, I see..."
                m "So you are like a prostitute then."
                call her_head("What?","angry","base") from _call_her_head_213
                m "Well I pay you to have sex with me. How would you call that?"
                call her_head("...........","angry","down_raised") from _call_her_head_214
                #$ ccg2 = 19
                call her_head("I am not a prostitute...","open","worriedCl") from _call_her_head_215
                call her_head("Why are you being so mean to me, [genie_name]?","angry","base",tears="soft") from _call_her_head_216
                m "I think you like it when I'm mean."
                call her_head("I do not!","mad","worried",tears="soft") from _call_her_head_217
                m "Really? Then why is your pussy so wet?"
                call her_head("Not because of that!","angry","down_raised") from _call_her_head_218
                m "If you say so..."
                #$ ccg2 = 20
                call her_head("A-ah...{image=textheart}","open","worriedCl") from _call_her_head_219
                call her_head("I am... ah...{image=textheart} not a prostitute...","shock","worriedCl") from _call_her_head_220            
            "\"......................................................\"":
                #$ ccg2 = 14
                call her_head("A-ha... ah...","open","worriedCl") from _call_her_head_221
                m "*Panting!*"
                call her_head("Ah... ha-aha...","open","worriedCl") from _call_her_head_222
                m "Oh..."
                call her_head("Ah-ah...","open","worriedCl") from _call_her_head_223
                m "......................"
                call her_head("Ah... ah...","open","worriedCl") from _call_her_head_224
                call her_head("Ah... [genie_name]?","open","base") from _call_her_head_225
                m "What is it?"
                #$ ccg2 = 17
                call her_head("Ah... Do you.... like it?","open","worriedCl") from _call_her_head_226
                m "Do I like drilling your super-tight pussy?"
                m "Very much so, [hermione_name]. Why?"
                call her_head(".....................","normal","worriedCl") from _call_her_head_227
                call her_head("Ah... You just got so quiet...","open","worriedCl") from _call_her_head_228
                m "Just enjoying the moment, [hermione_name]."
                m "What about you? You alright?"
                call her_head("Ah... yes...","open","worriedCl") from _call_her_head_229
                call her_head("It hurts a little though, ah...","open","base") from _call_her_head_230
                call her_head("Your penis is too big... ah...","open","worriedCl") from _call_her_head_231
                m "Hm..."
                m "You need me to slow down or something?"
                #$ ccg2 = 20
                call her_head("No, [genie_name]... You don't have to...","open","base") from _call_her_head_232
                call her_head("Please, don't mind me... Enjoy your moment.","normal","worriedCl") from _call_her_head_233
                call her_head("I will... ah... Get used to it eventually... ah...") from _call_her_head_234
                m "As you say, [hermione_name]."
                #$ ccg2 = 21
                call her_head("Ah-a...{image=textheart}","open","worriedCl") from _call_her_head_235
                m "Yes, this is great!"
                
        call her_head("Ah-ah...{image=textheart}","open","worriedCl") from _call_her_head_236
        
        if daytime:
            m "Going to classes after this?"
        else:
            m "Going to bed after this?"
        #$ ccg2 = 22
            
        call her_head("Yes, ah...{image=textheart}","open","worriedCl") from _call_her_head_237
        call her_head("If I'll be able to walk...") from _call_her_head_238
        g4 "Ght! {image=textheart} Yes, you always say the right things, [hermione_name]!"
        call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}","shock","worriedCl") from _call_her_head_239
        with hpunch
        #$ ccg2 = 24
        call her_head("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}","scream","wide") from _call_her_head_240
        m "Huh? You alright?"
        call nar(">Hermione's legs are shaking...") from _call_nar_61
        m "[hermione_name]?"
        #$ ccg2 = 28
        call her_head("{image=textheart}{image=textheart}{image=textheart}I think I'm cumming, [genie_name]!{image=textheart}{image=textheart}{image=textheart}","scream","wide") from _call_her_head_241
        g9 "Tch... You nasty slut!"
        #$ ccg2 = 29
        call her_head("AAH! I can't hold it!","silly","dead") from _call_her_head_242
        g4 "You need to be punished for being such a slut!"
        call nar(">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!") from _call_nar_62
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        #$ ccg2 = 30
        call her_head("NO! STOP! PLEASE!","scream","wide") from _call_her_head_243
        g4 "Who told you you could cum, slut? This is your punishment!"
        call her_head("[genie_name], no, ah-a!{image=textheart}","open","worriedCl") from _call_her_head_244
        #$ ccg2 = 31
        call her_head("Ah-a...{image=textheart}I will go insane!{image=textheart}{image=textheart}{image=textheart}","silly","ahegao") from _call_her_head_245
        g4 "{size=+7}Grragh!{/size}"
        hide screen bld1
        with d3
        call ctc from _call_ctc_48
        
        #$ ccg2 = 32
        call her_head("No...{image=textheart} ah...{image=textheart}","silly","ahegao") from _call_her_head_246
        #$ ccg2 = 33
        call her_head("I think I will...{image=textheart} pass out...{image=textheart}") from _call_her_head_247
        g4 "ARGH! YOU WHORE!"
        
        menu:
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block from _call_cum_block_7
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_out_ani") from _call_set_u_ani
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"
                call cum_block from _call_cum_block_8
                call ctc from _call_ctc_49
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 42
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_248
                hide screen bld1
                call ctc from _call_ctc_50
                
                call set_u_ani("sex_cum_out_blink_ani") from _call_set_u_ani_1
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Well, that was rather intense..."
                #$ ccg2 = 28
                call her_head("*heavy panting*","open_wide_tongue","ahegao") from _call_her_head_249
                m "You alright?"
                call her_head("Ah... yes...","silly","dead") from _call_her_head_250
                #$ ccg2 = 29
                call her_head("My legs are still shaking...") from _call_her_head_251
                hide screen bld1
                with d3
                call ctc from _call_ctc_51
                call blkfade from _call_blkfade_28
                
                hide screen ccg
                $ face_on_cg = False
                call h_update_hair from _call_h_update_hair_4
                
                if daytime:
                    call her_head("But I think I will be able to make it to my classes...","silly","dead",xpos="base",ypos="base") from _call_her_head_252
                else:
                    call her_head("But I think I will be able to make it to the common room...","silly","dead",xpos="base",ypos="base") from _call_her_head_253
                    
                m "Good."
                m "Did you enjoy getting fucked by your [genie_name]?"
                call her_head("[genie_name], I am only doing this for my house.","grin","ahegao") from _call_her_head_254
                m "Seriously? Still?"
                call her_head("Could I just get paid now... please?","open","worriedCl") from _call_her_head_255
                
            "-Cum inside Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block from _call_cum_block_9
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_in_ani") from _call_set_u_ani_2
                $ g_c_u_pic = "sex_cum_in_ani"
                $ ccg3 = "s1"
                call cum_block from _call_cum_block_10
                call ctc from _call_ctc_52
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 41
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_256
                hide screen bld1
                with d3
                call ctc from _call_ctc_53
                $ g_c_u_pic = "images/animation/23_cum_19.png"
                #$ ccg2 = 40
                call her_head("You came inside of me...","silly","dead") from _call_her_head_257
                g9 "I sure did."
                hide screen bld1
                with d3
                call ctc from _call_ctc_54
                call blkfade from _call_blkfade_29
                
                hide screen ccg
                $ face_on_cg = False
                call h_update_hair from _call_h_update_hair_5
                
                call her_head("But...","silly","dead",xpos="base",ypos="base") from _call_her_head_258
                m "What?"
                call her_head("What if I get pregnant?","shock","worriedCl") from _call_her_head_259
                m "Nah, you will be alright..."
                call her_head("How do you know, [genie_name]?","shock","worriedCl") from _call_her_head_260
                m "We witchers are infertile."
                call her_head("Witchers?","open","worriedCl") from _call_her_head_261
                m "Sure... You are a witch, that make me a witcher, right?"
                m "And everyone knows that witchers are infertile..."
                call her_head("[genie_name], you make no sense...","angry","base") from _call_her_head_262
                call her_head("Can I please just get paid now...?") from _call_her_head_263
    
    #Second time event.
    elif hg_pf_LetsHaveSex_OBJ.points == 1:
        m "[hermione_name], are you keeping your pussy wet and ready for me?"
        call her_main("[genie_name]!","scream","angryCl") from _call_her_main_956
        m "Just say \"I do\" and come over here, [hermione_name]."
        call her_main("...........","open","base") from _call_her_main_957
        call her_main("I do....","angry","down_raised") from _call_her_main_958
        hide screen hermione_main    
        jump your_ass
    
    #Third time event.
    elif hg_pf_LetsHaveSex_OBJ.points >= 2:
        m "[hermione_name]..."
        m "Last night I had a dream..."
        g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
        if whoring >= 24:
            call her_main("In that dream, [genie_name]...","soft","ahegao",xpos="right",ypos="base") from _call_her_main_959
        else:
            call her_main("In that dream, [genie_name]...","upset","closed",xpos="right",ypos="base") from _call_her_main_960
        if whoring <= 23:
            call her_main("Did I happen to receive 65 house points afterwards?","angry","angry") from _call_her_main_961
            g9 "Why yes, you did, [hermione_name]."
        else:
            call her_main("Did you cum inside me or not?","smile","baseL") from _call_her_main_962
            g9 "I'm not sure [hermione_name], care to find out?"
        call her_main("...............................","disgust","glance") from _call_her_main_963
        her "Let me just take my panties off..."
        stop music fadeout 1.0
        hide screen hermione_main
        call blkfade from _call_blkfade_30
        
        # SEX
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide") from _call_her_head_264
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        
        call gen_chibi("hide") from _call_gen_chibi_10
        call her_chibi("hide") from _call_her_chibi_26
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u
        
        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","worriedCl") from _call_her_head_265
            show screen ccg
        
        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_55
        
        call play_music("playful_tension") from _call_play_music_51# SEX THEME.
        
          
        call her_head("Ah...{image=textheart}","open","worriedCl") from _call_her_head_266
        m "Your pussy feels a bit looser today..."
        #$ ccg2 = 4
        call her_head("Does it...{image=textheart} ah...?{image=textheart}","open","worriedCl") from _call_her_head_267
        #$ ccg2 = 5
        call her_head("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl") from _call_her_head_268
        #$ ccg2 = 6
        call her_head("You are ruining my little pussy with your monstrous penis...{image=textheart}","silly","ahegao") from _call_her_head_269
        g4 "Agh, you whore!"
        #$ ccg2 = 10
        call her_head("Ah...{image=textheart}{image=textheart}","silly","ahegao") from _call_her_head_270
        m "Yes! Do you like it when I fuck you like this?"
        call her_head("Yes, [genie_name]...","base","glance") from _call_her_head_271
        menu:
            g4 "..."
            "\"Be sweet but passionate.\"":
                m "Yes, you're liking this?"
                #$ ccg2 = 14
                call her_head("I do, [genie_name]... ah...{image=textheart}","open","closed") from _call_her_head_272
                m "Good girl!"
                m "Just relax and take my cock!"
                call her_head("Yes... ah...{image=textheart}","open","closed") from _call_her_head_273
                m "All the way in... all the way..."
                call her_head("Ah...{image=textheart}{image=textheart}","open","worriedCl") from _call_her_head_274
                m "Yes, my little princess..."
                #$ ccg2 = 15
                call her_head("What?","angry","wide") from _call_her_head_275
                call her_head("No, please don't call me that... ah...{image=textheart}","angry","down_raised") from _call_her_head_276
                call her_head("My daddy used to call me his little princess when I was little...") from _call_her_head_277
                m "Well, right now I am your daddy!"
                #$ ccg2 = 16
                call her_head("Ah...{image=textheart} ah-ah...{image=textheart}{image=textheart}","soft","ahegao") from _call_her_head_278
                m "And you are my little princess-slut!"
                #$ ccg2 = 17
                call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","grin","dead") from _call_her_head_279
            "\"Be mean to her!\"":
                m "Yes, you slut!"
                m "I bet you love every second of this!"
                call nar(">You pick up the pace.") from _call_nar_63
                #$ ccg2 = 17
                call her_head("Ah...{image=textheart} [genie_name]...","open","worriedCl") from _call_her_head_280
                m "You nasty slut!"
                call her_head("Ah...{image=textheart} ah-a...{image=textheart}","shock","worriedCl") from _call_her_head_281
                m "You are a disgrace, [hermione_name]!"
                #$ ccg2 = 18
                call her_head("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl") from _call_her_head_282
                m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
                #$ ccg2 = 19
                call her_head("Ah-a...{image=textheart} But I am only doing this--","shock","worriedCl") from _call_her_head_283
                m "Nobody cares why you are doing this, cocksucker!"
                m "Look at what you've become!"
                m "Butt-naked, on your professor's old cock, like a cheap whore!"
                #$ ccg2 = 20
                call her_head("Ah...{image=textheart} No...{image=textheart} stop saying...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao") from _call_her_head_284
                call nar(">You pick up the pace some more.","start") from _call_nar_64
                $ g_c_u_pic = "sex2_ani"
                call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...","end") from _call_nar_65
                m "You let me molest you... You suck my cock..."
                m "What are you after that I ask you!?"
                #$ ccg2 = 21
                call her_head("................","grin","dead") from _call_her_head_285
                call her_head("Ah...{image=textheart} ah....{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl") from _call_her_head_286
                call her_head(".......................","angry","down_raised") from _call_her_head_287
                call her_head("{size=-5}I am a whore...{/size}") from _call_her_head_288
                m "Yes! That's exactly what you are!"
                
        #$ ccg2 = 22
        call her_head("Ah... ah... ah...","angry","down_raised") from _call_her_head_289
        call her_head("[genie_name], you think you could... ah...") from _call_her_head_290
        m "What?"
        call her_head("Could you spank me a little... ah...?","silly","worried",cheeks="blush",tears="soft") from _call_her_head_291
        g4 "Gladly!"
        
        call slap_her from _call_slap_her

        #$ ccg2 = 24
        call her_head("Aa-a-ah!{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft") from _call_her_head_292
        m "You liked that one, huh?"
        
        call slap_her from _call_slap_her_1
        
        #$ ccg2 = 28
        call her_head("Ah..!{image=textheart} Yes!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_293
        m "And some more!"
        
        call slap_her from _call_slap_her_2
        
        #$ ccg2 = 29
        call her_head("Ahh! Yes!","silly","worried",cheeks="blush",tears="soft") from _call_her_head_294
        call nar(">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second...","start") from _call_nar_66
        ">You love the sensation..."
        ">You unleash another series of slaps on Hermione's ass-cheeks."
        call nar(">Every single one met with a gasp of excitement from the girl.","end") from _call_nar_67
        #$ ccg2 = 30
        
        call slap_her from _call_slap_her_3
        call slap_her from _call_slap_her_4
        call slap_her from _call_slap_her_5
        call slap_her from _call_slap_her_6
        call slap_her from _call_slap_her_7
        
        #$ ccg2 = 31
        call her_head("Aah!!!{image=textheart}{image=textheart}{image=textheart} IT HURTS!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_295
        #$ ccg2 = 32
        call her_head("It hurts...{image=textheart}{image=textheart}{image=textheart} It hurts...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao") from _call_her_head_296
        m "Hm?"
        m "Why your legs are shaking, [hermione_name]?"
        m "Are you cumming?"
        #$ ccg2 = 33
        call her_head("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_297
        m "Well, I think I will follow your example then."
        call her_head("..............","silly","dead") from _call_her_head_298
        call nar(">You start fucking Hermione with renewed determination!") from _call_nar_68
        #$ ccg2 = 34
        call her_head("Ah! No! I can't...{image=textheart} I...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft") from _call_her_head_299
        m "Shut it whore!"
        g4 "Argh!"
        
        menu:
            "-Cum inside of Hermione-":
                with hpunch
                g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
                call cum_block from _call_cum_block_11
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ ccg3 = "s1"
                $ g_c_u_pic = "sex_cum_in_ani"
                call cum_block from _call_cum_block_12
                call ctc from _call_ctc_56
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 33
                call her_head("!!!","silly","dead") from _call_her_head_300
                #$ ccg2 = 38
                call her_head("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}") from _call_her_head_301
                g4 "I'm Not done yet, bitch!"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call cum_block from _call_cum_block_13
                call her_head("AH! MY BELLY!","shock","baseL",cheeks="blush",tears="soft") from _call_her_head_302
                g4 "{size=+5}SLUT!{/size}"
                
                hide screen bld1
                with d3
                call ctc from _call_ctc_57
                
                
                
                $ g_c_u_pic = "images/animation/23_cum_19.png"
                
                #$ ccg2 = 40
                m "Well, this was pretty great..."
                call her_head("Ah...{image=textheart}","silly","dead") from _call_her_head_303
                m "You alright there, slut? Ehm, I mean, [hermione_name]."
                call her_head("Yes... I...","silly","dead") from _call_her_head_304
                #$ ccg2 = 41
                call her_head("I feel so full...","open_wide_tongue","ahegao") from _call_her_head_305
                call her_head("!!!","scream","wide") from _call_her_head_306
                call her_head("You came inside of me, [genie_name]!") from _call_her_head_307
                m "I sure did."
                call her_head("You shouldn't have...","open","worriedCl") from _call_her_head_308
                m "Didn't you enjoy it?"
                call her_head("....maybe.","grin","dead") from _call_her_head_309
                #$ ccg2 = 42
                call her_head("I think I came several times...","soft","ahegao") from _call_her_head_310
                call blkfade from _call_blkfade_31
                
                $ face_on_cg = False
                call h_update_hair from _call_h_update_hair_6
                
                call her_head("Maybe you are right, [genie_name], and I shouldn't worry so much.","angry","wink",xpos="base",ypos="base") from _call_her_head_311
                if whoring <= 23:
                    call her_head("Can I get my payment now?") from _call_her_head_312
                    
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block from _call_cum_block_14
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"
                
                call cum_block from _call_cum_block_15
                call ctc from _call_ctc_58
                
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 30
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_313
                g4 "{size=+5}You whore! Take this!{/size}"
                call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_314
                hide screen bld1
                with d3
                call ctc from _call_ctc_59
                
                
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Well, that was pretty great..."
                #$ ccg2 = 31
                call her_head("Ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_315
                m "You alright there, slut?"
                call her_head("Yes... I...","silly","dead") from _call_her_head_316
                m "Didn't you enjoy this?"
                #$ ccg2 = 29
                call her_head("....I think so...","grin","dead") from _call_her_head_317
                call ctc from _call_ctc_60
                call blkfade from _call_blkfade_32

                $ face_on_cg = False
                call h_update_hair from _call_h_update_hair_7
                
                call her_head("I think I came several times, [genie_name]...","soft","ahegao",xpos="base",ypos="base") from _call_her_head_318
                if whoring <= 23:
                    call her_head("Can I get my payment now?","angry","wink") from _call_her_head_319
                $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    #Fourth time event.
    elif hg_pf_LetsHaveSex_OBJ.points >= 3:
        m "[hermione_name]..."
        m "I have a favour to ask of you..."
        call her_main("Is it sex? {size=-2}Please let it be sex...{/size}","smile","baseL") from _call_her_main_964
        m "You certainly seem eager."
        call her_main(".......","base","glance") from _call_her_main_965
        call her_main("Well I may have made some plans...","base","down") from _call_her_main_966
        her "but I can't tell you what..."
        m "well as long as you bend over my desk I don't really care..."
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down") from _call_her_main_967
        stop music fadeout 1.0
        hide screen hermione_main
        call blkfade from _call_blkfade_33
        # SEX
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide") from _call_her_head_320                                                                                                                                                                                 #HERMIONE
        hide screen genie
        
        $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u
        
        call her_chibi("hide") from _call_her_chibi_27
        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc from _call_ctc_61
        
        call play_music("playful_tension") from _call_play_music_52# SEX THEME.
        show screen bld1
        with d3    
        
        call her_head("Ah...{image=textheart}","open","worriedCl") from _call_her_head_321
        m "Your pussy feels drenched today..."
        call her_head("Does it...{image=textheart} ah...{image=textheart}","open","worriedCl") from _call_her_head_322
        call her_head("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl") from _call_her_head_323
        
        if daytime:
            call her_head("I've been... looking forward to this all morning...{image=textheart}","silly","ahegao") from _call_her_head_324
        else:
            call her_head("I've been... looking forward to this all day...{image=textheart}","silly","ahegao") from _call_her_head_325
            
        g4 "Agh, you whore!"
        call her_head("Ah...{image=textheart}{image=textheart}","silly","ahegao") from _call_her_head_326
        m "Yes! Do you like it when I fuck you like this?"
        call her_head("Yes, [genie_name]...","base","glance") from _call_her_head_327
        
        call play_sound("knocking") from _call_play_sound_43
        call nar(">You hear a knock at the door.") from _call_nar_69
        
        menu:
            "\"Who is it?\"":
                m "(Who would be knocking at a time like this?)"
                lun "It's Luna Lovegood sir."
                m "{size=-3}Who's that again, [hermione_name]?{/size}"
                call her_head("the crazy blonde... ah...{image=textheart}... with the nice breasts...","open","closed") from _call_her_head_328
                m "Come in!"
            "-Tell them to go away.-":
                m "Go aw-!"
                call her_head("no [genie_name]... let them in...","open","worriedCl") from _call_her_head_329
                m "You want to get caught?!"
                call her_head("Ah...{image=textheart} yes...{image=textheart}","shock","worriedCl") from _call_her_head_330
                m "You are a such a little whore, [hermione_name]!"
                call her_head("Ah-ah...{image=textheart} let them in... please...","shock","worriedCl") from _call_her_head_331
                m "You asked for it!"
                call her_head("Ah-a...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl") from _call_her_head_332
                m "Come in!"
                
        ">The door opens as Luna Lovegood walks in."
        call play_sound("door") from _call_play_sound_44 #Sound of a door opening.
        call luna_init from _call_luna_init
        $ luna_chibi("stand", 540, 250)
        $ changeLuna(1, 1, 4, 1)
        lun "Hello Professor!"
        #Stop sex
        m "....."
        call her_head("......","shock","worriedCl") from _call_her_head_333

        lun "I wanted to talk to you about the school uniform."
        m "The uniform?"
        lun "Yes, I have some ideas about some necessary changes and I'd like you to listen."
        m "{size=-3}What's going on here, [hermione_name]?{/size}"

        call her_head("I may have given her a suggestibility serum...","silly","ahegao") from _call_her_head_334
        m "{size=-3}A suggestibility serum?{/size}"
        lun "Who are you talking to sir?"
        m "Oh, um.... no one, just ignore me..."
        lun "Ok then, I'll ignore you..."
        call her_head("I may have suggested that she come here...","silly","ahegao") from _call_her_head_335
        call her_head("And that she be unable to see me...","silly","ahegao") from _call_her_head_336
        lun "As I was saying sir, the school uniform simply cannot stay as it is."

        show screen blktone
        with d3
        ">You pick up the pace some more."
        $ g_c_u_pic = "sex2_ani"
        ">The room fills up with rhythmical sound of a flesh hitting flesh..."
        call her_head("Ah... ah... ah...","angry","down_raised") from _call_her_head_337
        m "{size=-3}So let me get this straight.{/size}"
        m "{size=-3}You drugged your class mate...{/size}"
        m "{size=-3}Just so she would come in here and watch you have sex with your headmaster.{/size}"
        call her_head("Ah... yes...{image=textheart}{image=textheart}{image=textheart}") from _call_her_head_338
        lun "The girls uniform is far too conservative!"
        m "conservative?"
        lun "Indeed! Ms Granger is the only student that is dressing appropriately."
        call her_head("ah...","silly","worried",cheeks="blush",tears="soft") from _call_her_head_339
        m "{size=-3}What else did you do to her?{/size}"
        call her_head("I may have told her to... ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_340
        call her_head("act like the biggest slut she knows...{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_341
        m "{size=-3}So you then?{/size}"
        call her_head("yessss...{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_342
        lun "Sir please, pay attention."
        m "Sorry Miss Lovesgood, go on."
        lun "Thank you. As I was saying I think you need to enact several new policies regarding the girls school uniform."
        lun "Everyone should strive to achieve the same level of perfection as Miss granger."
        call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_343
        lun "I've come up with several rules that will help with this and I'd like you to enforce them."
        m "alright..."
        lun "rule number one: shirts must reveal a minimum of 3 inches of cleavage."
        call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_344
        lun "Rule number two: No skirt over 5 inches in length my be worn."
        call her_head("{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_345
        lun "rule number three: No bras to be worn at anytime."
        call her_head("{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_346
        lun "And finally, rule number four: No panties to be worn at anytime."
        call her_head("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_347

        m "Why are your legs shaking, [hermione_name]?"
        m "Are you cumming? In front of your classmate?"
        call her_head("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_348
        m "Well, I think I will follow your example then."
        call her_head("..............","silly","dead") from _call_her_head_349
        call nar(">You start fucking Hermione with renewed determination!") from _call_nar_70
        call her_head("Ah! No! I can't...{image=textheart} not in front of...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft") from _call_her_head_350
        m "Shut it whore!"
        lun "Yes sir."
        g4 "Argh!"
        with hpunch
        g4 "{size=+7}Argh!!!{/size}"
        call cum_block from _call_cum_block_16
        g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_out_ani"
        call cum_block from _call_cum_block_17
        call ctc from _call_ctc_62
        
        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_08.png"
        call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_head_351
        g4 "{size=+5}You whore! Take this!{/size}"
        call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_352
        hide screen bld1
        with d3
        call ctc from _call_ctc_63
        
        
        $ g_c_u_pic = "sex_cum_out_blink_ani"
        m "Well, that was pretty great..."
        call her_head("Ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft") from _call_her_head_353
        m "You alright there, slut?"
        call her_head("Yes... I...","silly","dead") from _call_her_head_354
        m "Didn't you enjoy this?"
        call her_head("....I think so...","grin","dead") from _call_her_head_355
        call ctc from _call_ctc_64
        
        call blkfade from _call_blkfade_34
        call her_head("I think I came several times, [genie_name]...","soft","ahegao") from _call_her_head_356
        m "Well that'll do for now. You two best head to class."
        call her_head("yes sir...","grin","dead") from _call_her_head_357
        call her_head("Come on Luna let's go.","grin","dead") from _call_her_head_358
        lun "Hermione! WHen did you get here?"
        lun "And what are you covered in?"
        call her_head("It doesn't matter...","soft","ahegao") from _call_her_head_359
        call her_head("{size=-7}You can lick it off later...{/size}","soft","ahegao") from _call_her_head_360
    
    $ face_on_cg = False
    call h_update_hair from _call_h_update_hair_8
                
    hide screen ccg
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    if not daytime:
        show screen candlefire
        
    call her_chibi("stand","desk","base") from _call_her_chibi_28
    call gen_chibi("hide") from _call_gen_chibi_11
    show screen genie
    pause.1
    hide screen blktone
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_13
    pause.5
    
    call bld from _call_bld_44
    stop music fadeout 4.0
    if whoring < 24:
        m "Yes, [hermione_name]. 65 points to the \"Gryffindor\" house." 
        $ gryffindor +=65
    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base") from _call_her_main_968
    
    if whoring < 21: #Adds points till 21.
        $ whoring +=1
    
    if hg_pf_LetsHaveSex_OBJ.points == 0:
        $ new_request_29_heart = 1
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points == 1:
        $ new_request_29_heart = 2
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points >= 2:
        $ new_request_29_heart = 3
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 3 #Event hearts level (0-3)
    
    $ hg_pf_LetsHaveSex_OBJ.points += 1
   
    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
    





