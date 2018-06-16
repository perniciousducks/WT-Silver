





label susan_imperio:
    call ast_main("Alright, [ast_genie_name].","smile","base","base","mid") from _call_ast_main_278
    call ast_main("I will bring the [ast_susan_name]!","grin","angry","angry","mid") from _call_ast_main_279
    call blkfade from _call_blkfade_38
    
    call nar(">Astoria leaves to summon Susan.") from _call_nar_84
    pause.5
    call play_sound("door") from _call_play_sound_75
    hide screen blkfade
    call sus_main("Hello, Professor.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade") from _call_sus_main_13
    call sus_main("You wanted to see me?","upset","base","worried","down") from _call_sus_main_14
    
    m "Yes, Miss Bones, if you could just stand there in the middle while--"
    call ast_main("Wait a second, [ast_genie_name],...","scream","closed","base","mid",trans="hpunch") from _call_ast_main_280
    call ast_main("50 points, remember!","grin","angry","angry","mid") from _call_ast_main_281
    m "..."
    m "Right..."
    m "Alright... 50 points to \"Slytherin\"!"
    $ slytherin +=50
    call ast_main("Thank you!","grin","happyCl","base","mid") from _call_ast_main_282
    pause.5
    call blkfade from _call_blkfade_39
                    
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base") from _call_ast_main_283 #uses the fade from the next line.
    hide screen blkfade
    call sus_main("What are you--","open","wide","worried","R",xpos="mid",ypos="base",trans="fade") from _call_sus_main_15
                    
    call cast_spell("imperio") from _call_cast_spell_2
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry") from _call_ast_main_284
                    
    show screen blktone
    call ast_main("[ast_susan_name], I command you to do whatever the old man tells you to do!") from _call_ast_main_285
    call sus_main("Of course, I will do whatever the old man sa--","open","base","base","up") from _call_sus_main_16
                    
    hide screen blktone
    call ast_main("All done, [ast_genie_name]! This will probably last a couple of days...","smile","base","base","R") from _call_ast_main_286
    call ast_main("You may leave now, [ast_susan_name]!","grin","happyCl","base","mid") from _call_ast_main_287
    call sus_main("Ok","base","base","base","up") from _call_sus_main_17
    hide screen susan_main
    with d3
                    
    $ susan_imperio_counter += 20 #Lasts 20 days.
    $ susan_imperio_influence = True
    $ spells_locked = True
                    
    call nar(">Susan is now under the influence of imperio.\n>The effect will last for 20 days.") from _call_nar_85
    jump astoria_requests
    
    
    
    
label imperio_spell_1:
    call play_music("hermione_theme") from _call_play_music_73
    call blkfade from _call_blkfade_40
    
    call nar(">You summon Susan to your office.") from _call_nar_86
    pause.5
    call play_sound("door") from _call_play_sound_76
    hide screen blkfade
    call sus_main("Hello, [sus_genie_name]. You wanted to see me?.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade") from _call_sus_main_18
    call ast_main("Hey [ast_susan_name]!","grin","narrow","narrow","L",xpos="base",ypos="base") from _call_ast_main_288
    call sus_main("Astoria? What are you doing here?","open","base","worried","R") from _call_sus_main_19

    call ast_main("Oh, don't mind me...","pout","base","base","R") from _call_ast_main_289
    call ast_main("I'm only here to put a curse on you.","grin","angry","angry","mid") from _call_ast_main_290
    call sus_main("P-Put a curse on me?!!","open","wide","worried","wide") from _call_sus_main_20
    call sus_main("No! Professor, do someth--","scream","wide","worried","mid") from _call_sus_main_21
    
    call cast_spell("imperio") from _call_cast_spell_3
    call ast_main("{size=+10}{b}Imperio Cor Meum!{/b}{/size}","scream","angry","angry","angry") from _call_ast_main_291
    
    call sus_main("W-what are you--","open","wide","worried","wide") from _call_sus_main_22
    call nar("A puff of orange smoke appears from the end of Astoria's wand, working it's way up into Susan's nose.") from _call_nar_87
    call sus_main("--doing...","upset","base","base","up") from _call_sus_main_23
    call sus_main("...","upset","narrow","base","up") from _call_sus_main_24
    hide screen astoria_main
    with d3
    call ast_main("OK, so what should we do now?","grin","angry","angry","mid",xpos="close",ypos="base") from _call_ast_main_292
    m "You read the book as well didn't you?"
    call ast_main("That was just on how to cast it, [ast_genie_name]!","open","base","base","R") from _call_ast_main_293
    call ast_main("What should we make her want?","grin","angry","angry","L") from _call_ast_main_294
    m "Hmmm?"
    m "How about making her want to strip?"
    call ast_main("[ast_genie_name]!","disgust","closed","worried","mid") from _call_ast_main_295
    m "What? Didn't you already do that?"
    call ast_main("I only made her take her top off.","open","base","base","mid") from _call_ast_main_296
    m "Ugh, fine... let's just go with that again..."
    call ast_main("OK...","smile","base","base","L") from _call_ast_main_297
    call ast_main("Susy, are you listening?","open","closed","base","mid") from _call_ast_main_298
    call sus_main("yes...","upset","narrow","worried","up") from _call_sus_main_25
    call ast_main("Good, I want you to pay attention.","open","base","base","L") from _call_ast_main_299
    call sus_main("...","base","narrow","base","up") from _call_sus_main_26
    call ast_main("From now on you have an uncontrollable urge to show Dumby and I your boobs!","open","closed","base","mid") from _call_ast_main_300
    call sus_main("My boobs? Ok...","upset","narrow","worried","down") from _call_sus_main_27
    call ast_main("Alright, now wake up!","smile","base","base","L") from _call_ast_main_301
    call sus_main("I am awa--...","open","narrow","base","down") from _call_sus_main_28
    
    call nar(">Susan's body shifts a little as the life returns to her eyes.") from _call_nar_88
    call sus_main("W-w-what happened?","scream","wide","worried","wide",trans="hpunch") from _call_sus_main_29
    
    call sus_main("And why do I...","open","base","base","down") from _call_sus_main_30
    call sus_main("Oh no...","upset","narrow","worried","down") from _call_sus_main_31
    call ast_main("Is something wrong, Susy?","grin","narrow","narrow","L") from _call_ast_main_302
    call sus_main("*gulp*","upset","closed","worried","down") from _call_sus_main_32
    call sus_main("Sir, would it be alright if I showed you my... b-boobs?","open","closed","worried","mid") from _call_sus_main_33
    m "Your {b}boobs{/b}, Miss Bones?"
    call ast_main("(Hihihihihi--)","grin","angry","angry","L") from _call_ast_main_303
    call sus_main("I'm terribly sorry sir!","open","closed","base","mid") from _call_sus_main_34
    call sus_main("Please don't look!!!","upset","closed","worried","mid") from _call_sus_main_35
    
    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform from _call_update_sus_uniform_1
    with d3
    pause.5
    
    m "Oh no, Miss Bones!"
    m "What are you doing?!"
    hide screen bld1
    with d3
    pause.8
    
    call gen_chibi("jerking_off_behind_desk") from _call_gen_chibi_14
    pause.5
    
    call ast_main("(...)","pout","narrow","narrow","mid") from _call_ast_main_304
    call sus_main("I-I-I'm sorry, Professor Dumbledore, I don't know what's come over me...","open","narrow","worried","down") from _call_sus_main_36
    call sus_main("I'm Sorry you have to see this...","upset","closed","base","mid") from _call_sus_main_37
    call ast_main("See what Susy?","grin","angry","angry","mid") from _call_ast_main_305
    call sus_main("My gross boobs...","open","closed","worried","mid") from _call_sus_main_38
    call ast_main("(I knew they were gross!)","grin","angry","angry","L") from _call_ast_main_306
    call sus_main("Please Sir--","open","narrow","worried","mid") from _call_sus_main_39
    call sus_main("Don't think less of me...","upset","closed","worried","mid") from _call_sus_main_40
    
    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform from _call_update_sus_uniform_2
    with d3
    call ctc from _call_ctc_71
    
    g4 "{size=+10}Nice!{/size}"
    call ast_main("Dumby!","scream","wide","wide","mid") from _call_ast_main_307
    m "What? You can't blame me for this!"
    call ast_main("Not that! You're not supposed to think they're nice!","clench","angry","angry","mid") from _call_ast_main_308
    call ast_main("(And stop touching yourself... Gross...)","pout","angry","angry","R",cheeks="blush") from _call_ast_main_309
    m "Are they not?"
    call ast_main("{b}No!{/b} they're huge and soft and squishy and, and, and,... gross!","scream","closed","angry","mid") from _call_ast_main_310
    g9 "You're right about them looking huge and soft..."
    call ast_main("Dumby!","clench","angry","angry","mid") from _call_ast_main_311
    call sus_main("How can you two be so mean!","upset","narrow","worried","R") from _call_sus_main_41
    call ast_main("Oh calm down, [ast_susan_name]!","scream","angry","angry","L") from _call_ast_main_312
    call sus_main("[ast_susan_name]!? What's that supposed to mean?","open","wide","worried","wide") from _call_sus_main_42
    call ast_main("Pfft... you know...","pout","angry","angry","R") from _call_ast_main_313
    call sus_main("How dare you!","scream","closed","angry","mid") from _call_sus_main_43
    call sus_main("Are you just going to let her say that, sir?","scream","base","angry","mid") from _call_sus_main_44
    g4 "What's that? I was a little-- ugh... distracted..."
    
    call nar(">You keep stroking your rock-hard cock whilst marveling at Susan's heaving chest.") from _call_nar_89
    g4 "(So big...)"
    call sus_main("...","upset","base","worried","down") from _call_sus_main_45
    call ast_main("Alright, I think you're enjoying this a little too much, Dumby!","disgust","angry","angry","mid") from _call_ast_main_314
    m "Just a little longer..."
    
    call cast_spell("imperio") from _call_cast_spell_4
    call ast_main("{size=+10}{b}Imperio!{/b}{/size}","scream","angry","angry","angry") from _call_ast_main_315
    
    call sus_main("W-w-what...","open","base","base","up") from _call_sus_main_46
    call nar(">A soft line of yellow smoke puffs from astoria's wand and into Susan's nose.") from _call_nar_90
    
    call gen_chibi("hide") from _call_gen_chibi_15
    show screen genie
    with d3
    pause.1
    m "(Damn it! Not again...)"
    
    call sus_main("...","upset","base","worried","down") from _call_sus_main_47
    call ast_main("Get dressed, Susy.","smile","base","base","mid") from _call_ast_main_316
    call sus_main("Alright...","upset","narrow","worried","mid") from _call_sus_main_48
    
    hide screen susan_main
    $ susan_wear_bra = True
    call update_sus_uniform from _call_update_sus_uniform_3
    call sus_main("","upset","narrow","worried","mid") from _call_sus_main_49
    pause.5
    call nar("Susan mechanically puts her clothes back on...") from _call_nar_91
    
    hide screen susan_main
    $ susan_wear_top = True
    call update_sus_uniform from _call_update_sus_uniform_4
    call sus_main("","upset","narrow","base","mid") from _call_sus_main_50
    pause.5
    call nar("Her eyes staring blankly forward the entire time.") from _call_nar_92
    
    m "Aww... why'd you do that?"
    call ast_main("You were getting too excited, old man.","clench","angry","angry","mid") from _call_ast_main_317
    m "So what?"
    call ast_main("Well you can't go having too much fun, otherwise you'll never want to practice the new spells!","pout","angry","angry","R") from _call_ast_main_318
    m "You could have at least made her dance or something..."
    call ast_main("We could do that...","pout","base","base","L") from _call_ast_main_319
    m "Then why don't we?"
    call ast_main("Because it's boring!","disgust","ahegao","ahegao","ahegao") from _call_ast_main_320
    call ast_main("I wanna learn more spells!","open","closed","base","mid") from _call_ast_main_321
    m "Ugh... fine..."
    call ast_main("Good, I already read what the next one is called!","grin","angry","angry","mid") from _call_ast_main_322
    m "Really, what's that?"
    call ast_main("Imperio tempus...","open","closed","base","mid") from _call_ast_main_323
    call ast_main("I didn't see what it could do though...","upset","base","base","down") from _call_ast_main_324
    m "Wanna start reading it now?"
    call ast_main("It's a little late sir.","worried","base","base","mid") from _call_ast_main_325
    call ast_main("Besides, I better put bessy here back in her barn before people start to notice.","grin","angry","angry","L") from _call_ast_main_326
    call sus_main("(Bessy...?)","upset","wide","worried","wide") from _call_sus_main_51
    m "Alright..."
    call ast_main("Just let me know when you're ready to read the next chapter Dumby!","smile","narrow","narrow","mid") from _call_ast_main_327
    m "You got it."
    call ast_main("Night, Dumby!","grin","closed","base","mid") from _call_ast_main_328
    m "Good night..."
    call ast_main("Come on Susy, go back to your room and go to sleep.","open","base","base","L") from _call_ast_main_329
    call sus_main("yes...","upset","narrow","worried","down") from _call_sus_main_52
    hide screen susan_main
    with d3
    pause.5
    
    call ast_main("(This is so much fun!)","grin","closed","base","mid") from _call_ast_main_330
    hide screen astoria_main
    hide screen bld1
    with d3


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.
    
    if astoria_affection < 1:
        $ astoria_affection = 1
        $ astoria_spell_progress = 0
    
    jump day_main_menu



        
label imperio_spell_2: #second level imperio spell #needs posing
    call play_music("hermione_theme") from _call_play_music_74
    call ast_main("Are you finally ready to try out the new spell Dumby?","grin","narrow","narrow","mid",xpos="close",ypos="base",trans="fade") from _call_ast_main_331
    m "You bet!"
    call ast_main("Awesome, I can't wait to see the look on Susan's dumb face...","grin","closed","base","mid") from _call_ast_main_332
    m "Let me just bring her up here."
    call blkfade from _call_blkfade_41
    
    call nar(">You summon Susan up to your office.") from _call_nar_93
    pause.5
    call play_sound("door") from _call_play_sound_77
    hide screen blkfade
    call sus_main("You wanted to see me, [sus_genie_name]?","open","base","worried","mid",xpos="mid",ypos="base",trans="fade") from _call_sus_main_53
    call sus_main("Astoria? Why are you here again?","open","base","worried","R") from _call_sus_main_54
    call ast_main("Oh... no reason...","pout","base","base","down") from _call_ast_main_333
    call sus_main("Is there something wrong, Professor?","upset","base","worried","mid") from _call_sus_main_55
    m "As a matter of fact there is..."
    call sus_main("R-really? Is this about me returning my books to the library a day late?","open","wide","base","wide") from _call_sus_main_56
    call sus_main("I swear it won't happen again!","open","closed","worried","mid") from _call_sus_main_57
    m "What? No, I'm afraid there's an issue with your uniform..."
    call sus_main("Oh... Is it because I'm not wearing the school robe?","open","base","worried","down") from _call_sus_main_58
    call sus_main("I can wear it from now on if you like!","upset","base","base","mid") from _call_sus_main_59
    m "Actually, Wearing too many clothes is the problem."
    call sus_main("W-w-what???","scream","wide","base","wide") from _call_sus_main_60
    call sus_main("You can't be serious sir!","open","wide","base","mid") from _call_sus_main_61
    m "I am, Ms Bones..."
    g9 "Hiding away those glorious milk duds of yours is a serious offense!"
    call sus_main("","open","wide","base","wide") from _call_sus_main_62
    call ast_main("(Pffft, gloriously gross)","pout","angry","angry","R") from _call_ast_main_334
    call sus_main("Professor Dumbledore! How can you say something like that!","scream","base","angry","mid",trans="hpunch") from _call_sus_main_63
    call sus_main("I think I better go...","upset","closed","worried","mid") from _call_sus_main_64
    hide screen astoria_main
    with d3
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base") from _call_ast_main_335
    pause.5
    
    call cast_spell("imperio") from _call_cast_spell_5
    call ast_main("{size=+10}{b}Imperio Tempus{/b}{/size}","scream","angry","angry","angry") from _call_ast_main_336
    
    call nar("A flash of purple smoke erupts from Astoria's wand and flies towards Susan.") from _call_nar_94
    call sus_main("What is--","open","wide","base","wide") from _call_sus_main_65
    
    show screen blktone
    call sus_main("...","upset","narrow","base","mid") from _call_sus_main_66
    call ast_main("hahahaha","grin","happyCl","base","mid") from _call_ast_main_337
    call ast_main("Her face was priceless when you said milk duds...","grin","base","base","L") from _call_ast_main_338
    m "You liked that?"
    hide screen astoria_main
    with d3
    call ast_main("Of course! Anything to bring Bessy here down a peg.","smile","narrow","narrow","L",xpos="close",ypos="base") from _call_ast_main_339
    call ast_main("Although, you said that before I cast Imperio on her, so we might have to obliviate that if we want to keep this a secret.","upset","base","worried","L") from _call_ast_main_340
    m "Yeah sure..."
    m "(What in the hells is obliviate?)"
    call ast_main("So what should we make her do today, [ast_genie_name]?","smile","base","base","mid") from _call_ast_main_341
    m "Well, if the books to be believed, this spell should let us change something about her permanently."
    call ast_main("Hmmm...","pout","narrow","narrow","R") from _call_ast_main_342
    call ast_main("I know!","grin","angry","angry","mid") from _call_ast_main_343
    call ast_main("Lets make her forget everything that happens in this room as soon as she leaves!","open","angry","angry","L") from _call_ast_main_344
    call ast_main("That way we don't have to worry about her tattling on us.","open","angry","angry","mid") from _call_ast_main_345
    m "Good thinking boy wonder."
    call ast_main("...","pout","angry","angry","mid") from _call_ast_main_346
    m "But is that all we're going to change about her?"
    m "Can't we do something a little more... adventurous?"
    call ast_main("You mean like making her show you her milk duds?","pout","narrow","narrow","mid") from _call_ast_main_347
    m "Well if you insist..."
    call ast_main("ugh... you're such a filthy pervert!","clench","angry","angry","mid") from _call_ast_main_348
    m "We can do something else if you--"
    call ast_main("I didn't say no...","upset","closed","base","mid") from _call_ast_main_349
    m "Oh... well how about you make it so--"
    call ast_main("I get to choose, [ast_genie_name]!","scream","closed","angry","mid") from _call_ast_main_350
    m "What? Why?"
    call ast_main("Because it's my spell and my wand!","open","narrow","narrow","mid") from _call_ast_main_351
    call ast_main("Not to mention you'd probably do something over the top and gross...","open","narrow","narrow","R") from _call_ast_main_352
    m "Probably..."
    m "So what's your plan?"
    call ast_main("Just wait and see old man!","disgust","narrow","narrow","mid") from _call_ast_main_353
    call ast_main("Susan, listen up!","scream","closed","base","L") from _call_ast_main_354
    call sus_main("Yes...","upset","narrow","base","up") from _call_sus_main_67
    call ast_main("From now on, you'll no longer remember anything that happens in this office.","open","base","base","L") from _call_ast_main_355
    call sus_main("Ok...","upset","narrow","base","mid") from _call_sus_main_68
    m "Is that all?"
    call ast_main("Shush old man, I'm not done yet!","disgust","narrow","narrow","mid") from _call_ast_main_356
    call ast_main("You'll also get an uncontrollable urge to take your top off whenever you see Dumby and I together, OK?","open","closed","base","mid") from _call_ast_main_357
    call sus_main("yes...","upset","base","worried","down") from _call_sus_main_69
    m "Nice! But won't she just run away from now on?"
    call ast_main("Hmmm, you're probably right...","upset","base","worried","L") from _call_ast_main_358
    call ast_main("Last of all, you're not allowed to leave this office until I say so, OK, Susy?","open","narrow","narrow","L") from _call_ast_main_359
    call sus_main("Yes, Astoria...","upset","narrow","worried","mid") from _call_sus_main_70
    call ast_main("Awesome! Now wake up, [ast_susan_name]!","grin","angry","angry","L") from _call_ast_main_360
    call sus_main("...","upset","narrow","base","up") from _call_sus_main_71
    
    hide screen blktone
    call nar(">The colour slowly returns to Susan's eyes...") from _call_nar_95
    call sus_main("ugh...","upset","narrow","base","up") from _call_sus_main_72
    call sus_main("What happened?","open","narrow","worried","mid") from _call_sus_main_73
    call ast_main("Nothing Susy, Dumbledore was just explaining how your uniform wasn't up to scratch.","grin","base","base","mid") from _call_ast_main_361
    call sus_main("My uniform... You're right... Too many clothes...","open","narrow","worried","down") from _call_sus_main_74
    call sus_main("I need to take off my top...","open","base","worried","down") from _call_sus_main_75
    call ast_main("Mhmm, that's right, Susy... Why don't you show old Dumby here your gross boobs...","grin","angry","angry","mid") from _call_ast_main_362
    call sus_main("B-b-b-but,... he's so old.","upset","narrow","worried","L") from _call_sus_main_76
    call ast_main("That's right... Only a nasty slut would show their boobs to such a wrinkly old man...","grin","angry","angry","L") from _call_ast_main_363
    m "Hey!"
    call ast_main("Shhh, dumby,... don't ruin my fun!","clench","angry","angry","mid") from _call_ast_main_364
    m "Fine..."
    call sus_main("I-I'm not a slut...","upset","narrow","worried","down") from _call_sus_main_77
    call ast_main("Well I'm sure you'll be able to keep your top on then, [ast_susan_name].","open","closed","base","mid") from _call_ast_main_365
    call sus_main("I... There's something wrong sir!","open","base","worried","mid") from _call_sus_main_78
    call sus_main("I can't help it...","upset","narrow","worried","down") from _call_sus_main_79
    call ast_main("","grin","angry","angry","L") from _call_ast_main_366
    pause.2
    
    hide screen susan_main
    $ susan_wear_top = False
    $ susan_wear_bra = False
    call update_sus_uniform from _call_update_sus_uniform_5
    call sus_main("","upset","closed","worried","mid") from _call_sus_main_80
    call ctc from _call_ctc_72
    
    g4 "Nice!"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk") from _call_gen_chibi_16
    pause.8
    
    call ast_main("[ast_genie_name]! Are you touching yourself?","scream","wide","wide","mid") from _call_ast_main_367
    m "Ugh... I can't help it..."
    g4 "It's not everyday you get to see a rack like this..."
    call ast_main("Well stop it! It's gross!","clench","angry","angry","mid") from _call_ast_main_368
    m "Alri--"
    call sus_main("Please sir... it's too much!","open","closed","base","mid") from _call_sus_main_81
    call sus_main("It's bad enough that I have to show you my breasts...","open","closed","worried","mid") from _call_sus_main_82
    call ast_main("Wait...","open","wide","wide","wide") from _call_ast_main_369
    call ast_main("Keep going, dumby!","clench","angry","angry","mid") from _call_ast_main_370
    m "What?"
    call sus_main("What?","scream","wide","base","mid") from _call_sus_main_83
    call ast_main("Well if bessy here hates it... Then I love it!","clench","angry","angry","L") from _call_ast_main_371
    call ast_main("Besides, it's not like I can see anything under the desk.","open","closed","base","mid") from _call_ast_main_372
    call sus_main("(...)","upset","closed","worried","mid") from _call_sus_main_84
    m "So you're OK with this?"
    call ast_main("Mhmm, just don't expect me to touch it old man!","upset","angry","angry","mid") from _call_ast_main_373
    call sus_main("I'm not OK with this!","open","closed","base","mid") from _call_sus_main_85
    call ast_main("No one asked you, slut!","clench","angry","angry","L") from _call_ast_main_374
    call sus_main("I am not a slut!","scream","closed","angry","mid") from _call_sus_main_86
    call ast_main("Ha! You're standing here, letting old man dumbledore oggle your fat tits while he jerks his wrinkly old cock!","open","closed","base","mid") from _call_ast_main_375
    call ast_main("If that's not a slut then I don't know what is!","disgust","narrow","narrow","L") from _call_ast_main_376
    call sus_main("I-- don't know why I'm doing this...","upset","closed","worried","mid") from _call_sus_main_87
    call sus_main("You probably cursed me!","open","closed","angry","mid") from _call_sus_main_88
    call ast_main("Duh!","grin","angry","angry","L") from _call_ast_main_377
    call sus_main("well stop it!","open","base","angry","R") from _call_sus_main_89
    call ast_main("Nuh!","open","closed","base","mid") from _call_ast_main_378
    call sus_main("Please astoria...","upset","narrow","worried","down") from _call_sus_main_90
    
    call nar(">You start to zone out the two girls argument as you focus in on Susan's heaving boosom...") from _call_nar_96
    g4 "Ugh yeah... that's it..."
    call ast_main("You can leave once old dumby here's done.","open","closed","base","mid") from _call_ast_main_379
    call sus_main("What? you mean I have to wait until he...","open","base","worried","mid") from _call_sus_main_91
    call sus_main("This is unbelievable!","scream","base","angry","mid") from _call_sus_main_92
    call sus_main("I'm going to report both of you to the ministry of magic!","open","closed","angry","mid") from _call_sus_main_93
    call sus_main("My aunt is an auror you know!","open","base","angry","mid") from _call_sus_main_94
    call ast_main("yeah... I've met your creepy old aunt.","pout","narrow","narrow","R") from _call_ast_main_380
    call sus_main("What? Did you curse her too you evil little witch?","open","wide","base","R") from _call_sus_main_95
    call ast_main("I wish...","pout","narrow","base","R") from _call_ast_main_381
    call sus_main("Well she's going to lock both of you away in azkaban!","open","closed","angry","mid") from _call_sus_main_96
    call sus_main("You'll never see me or anyone else again...","scream","closed","angry","mid") from _call_sus_main_97
    call ast_main("Ha!","grin","angry","angry","L") from _call_ast_main_382
    call sus_main("And you, Dumbledore! I hope you enjoy wanking that nasty cock of yours because it'll be the last time you ever get to do that!","scream","narrow","angry","mid") from _call_sus_main_98
    g4 "Ugh yeah... say that again..."
    call sus_main("Ugh! You're both sick!","open","narrow","angry","mid") from _call_sus_main_99
    g4 "Mmmm, keep shaking those tits of yours..."
    g4 "I'm almost there {b}slut!{/b}"
    call sus_main("I am not a {size=+10}slut!{/size}","scream","closed","angry","mid",trans="vpunch") from _call_sus_main_100
    call nar(">As Susan yells at the top of her voice, the effort causes her gigantic tits to rise and slap back together.") from _call_nar_97
    
    g4 "{size=+10}HERE IT COMES!{/size}"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("cumming_behind_desk") from _call_gen_chibi_17
    call cum_block from _call_cum_block_20
    g4 "{size=+10}AHHH... YESS!!!!{/size}"
    call ast_main("Woah... I didn't think you'd have that much in you dumby...","worried","wide","wide","wide") from _call_ast_main_383
    
    hide screen susan_main
    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform from _call_update_sus_uniform_6
    call sus_main("{size=+10}Hmph! I hope you Enjoy azkaban perverts!{/size}","upset","narrow","angry","down") from _call_sus_main_101
    call play_sound("door") from _call_play_sound_78
    hide screen susan_main
    with d3
    call ast_main("","pout","narrow","narrow","R") from _call_ast_main_384
    call gen_chibi("cum_on_desk") from _call_gen_chibi_18
    pause.5
    
    call nar(">With Susan's curse broken by your colossal ejaculation, she turns and runs out of your office, her shirt in hand...") from _call_nar_98
    m "Ugh... should we stop her?"
    call ast_main("It's fine [ast_genie_name], I made it so she forgets everything that happens in here, remember?","open","closed","base","mid") from _call_ast_main_385
    m "Oh... yeah..."
    call ast_main("Well I'll let you clean up...","disgust","narrow","narrow","mid") from _call_ast_main_386
    m "(...)"
    call ast_main("See ya [ast_genie_name]! and don't forget that we've got a new spell to learn!","open","closed","base","mid") from _call_ast_main_387
    m "Can't we just do that one again?"
    call ast_main("NO!","clench","angry","angry","mid") from _call_ast_main_388
    m "Fine... See you later..."
    hide screen astoria_main
    with d3
    pause.5
    
    call nar(">Astoria turns to leave your office, skipping cheerfully as she goes...") from _call_nar_99


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.
    
    if astoria_affection < 2:
        $ astoria_affection = 2
        $ astoria_spell_progress = 0
    
    jump day_main_menu

    
label imperio_spell_3:
    call play_music("hermione_theme") from _call_play_music_75
    call ast_main("","smile","base","base","mid",xpos="close",ypos="base",trans="fade") from _call_ast_main_389
    m "Ready to try out the final imperio spell?"
    call ast_main("You bet [ast_genie_name]! I can't wait to see the look on Susy's stupid face this time!","grin","angry","angry","down") from _call_ast_main_390
    m "Shall I bring her up here?"
    call ast_main("Do you even need to ask old man?","smile","narrow","narrow","mid") from _call_ast_main_391
    m "I suppose not..."
    call blkfade from _call_blkfade_42
    
    call nar(">You summon Susan up to your office.") from _call_nar_100
    pause.5
    call play_sound("door") from _call_play_sound_79
    hide screen blkfade
    call sus_main("You wanted to see me sir?","open","base","worried","mid",xpos="mid",ypos="base",trans="fade") from _call_sus_main_102
    call sus_main("Astoria?...","upset","base","worried","R") from _call_sus_main_103
    call sus_main("You seem to be here quite often...","upset","narrow","worried","R") from _call_sus_main_104
    call ast_main("I'm surprised you have noticed that, Susy...","pout","base","base","R") from _call_ast_main_392
    call sus_main("Well I'm not sure why I was brought here...","open","base","worried","mid") from _call_sus_main_105
    
    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform from _call_update_sus_uniform_7
    call sus_main("","upset","base","worried","mid") from _call_sus_main_106
    pause.5
    
    call nar(">As susan begins to talk her arms seem to have a mind of their own, queitly removing her top as she speaks.") from _call_nar_101
    call sus_main("Was this about the library books that I returned a day late sir?","open","narrow","worried","down") from _call_sus_main_107
    call sus_main("I promise it won't happen again...","upset","closed","worried","mid") from _call_sus_main_108
    m "It's not about the damn books, Ms Bones!"
    call sus_main("Then what is it?","base","narrow","base","mid") from _call_sus_main_109
    
    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform from _call_update_sus_uniform_8
    call sus_main("","base","base","base","mid") from _call_sus_main_110
    pause.5
    
    g4 "(!!!)"
    call ast_main("Maybe it's because of you showing off your gross boobs?","pout","base","base","R") from _call_ast_main_393
    call sus_main("Astoria! How can you say something so rude! I'd never...","open","closed","angry","mid") from _call_sus_main_111
    call sus_main("","upset","wide","worried","down",trans="hpunch") from _call_sus_main_112
    pause.8
    call nar(">Susan's eyes drift down to her exposed chest.") from _call_nar_102
    call sus_main("WHAT?!?!?","scream","wide","worried","down") from _call_sus_main_113
    call sus_main("I'm so sorry, professor Dumbledore!","upset","closed","worried","mid") from _call_sus_main_114
    call sus_main("I Don't know what came over me!","open","closed","base","mid") from _call_sus_main_115
    call ast_main("Maybe it's just because you're a nasty slut!","pout","base","base","L") from _call_ast_main_394
    call sus_main("I am not a {size=+10}slut{/size}, Astoria!","scream","closed","angry","mid") from _call_sus_main_116
    call ast_main("Pfft... You must just like showing your headmaster your tits because your such a prude then...","pout","base","base","R") from _call_ast_main_395
    call sus_main("I-- don't know why this is happening...","open","wide","worried","wide") from _call_sus_main_117
    call sus_main("You must have cursed me!","scream","narrow","angry","R") from _call_sus_main_118
    call ast_main("Bingo!","grin","angry","angry","L") from _call_ast_main_396
    call sus_main("Professor! You have to stop her!","scream","wide","base","mid") from _call_sus_main_119
    hide screen astoria_main
    with d3
    m "Ugh... I'm afraid not Susan..."
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base") from _call_ast_main_397
    call sus_main("WHAT?!","scream","wide","base","wide") from _call_sus_main_120
    call sus_main("W-w-w-well my aunt will just send you--","upset","narrow","angry","mid") from _call_sus_main_121
    
    call cast_spell("imperio") from _call_cast_spell_6
    call ast_main("{size=+10}{b}IMPERIO MAXIMUS!{/b}{/size}","scream","angry","angry","angry") from _call_ast_main_398
    
    call nar(">A thick stream of golden smoke erupts out of astoria's wand and floats towards susan...") from _call_nar_103
    call sus_main("to azkaban...","open","narrow","base","up") from _call_sus_main_122
    
    show screen blktone
    call sus_main("...","upset","narrow","base","mid") from _call_sus_main_123
    hide screen astoria_main
    with d3
    call ast_main("Alright... so what should we make her do this time, [ast_genie_name]?","grin","base","base","mid",xpos="close",ypos="base") from _call_ast_main_399
    m "Hmmm... Are you actually going to let me choose this time or are you just asking to be annoying?"
    call ast_main("Hey! I am not annoying!","scream","closed","angry","mid",trans="hpunch") from _call_ast_main_400
    m "Well are you going to let me choose then?"
    call ast_main("Alright... Just don't be too gross dumby!","disgust","narrow","narrow","mid") from _call_ast_main_401
    call ast_main("Or boring... that'd be even worse!","upset","narrow","narrow","mid") from _call_ast_main_402
    
    m "Alright well, first things first..." #I'll add a menu here with more options once art assets are drawn for them
    
    hide screen blktone
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk") from _call_gen_chibi_19
    pause.8
    
    show screen bld1
    call nar(">Your hands sneak under your desk and around your engorged cock.") from _call_nar_104
    g9 "That's better..."
    call ast_main("(...)","pout","angry","angry","R") from _call_ast_main_403
    m "What?"
    call ast_main("I told you not to be boring! We already did this last time!","open","closed","base","mid") from _call_ast_main_404
    g9 "If this is too boring, why don't you get her to suck me off?"
    call ast_main("Dumby! That's too gross!","disgust","narrow","narrow","mid") from _call_ast_main_405
    call ast_main("I don't wanna have to see your nasty old cock!","clench","narrow","narrow","R") from _call_ast_main_406
    m "Ugh... Fine... What do you want to do then?"
    call ast_main("Well seeing as how you asked...","open","closed","base","mid") from _call_ast_main_407
    call ast_main("Susy, are you listening?","open","narrow","narrow","L") from _call_ast_main_408
    
    show screen blktone
    call sus_main("yes...","upset","narrow","base","up") from _call_sus_main_124
    call ast_main("I want you to crawl under Dumby's desk.","grin","base","base","L") from _call_ast_main_409
    m "I thought you didn't want her to suck me off?"
    call ast_main("Shut it, and stop being so gross, dumby!","scream","closed","angry","mid") from _call_ast_main_410
    call sus_main("...","upset","narrow","base","up") from _call_sus_main_125
    call ast_main("Now go, [ast_susan_name]!","grin","narrow","angry","mid") from _call_ast_main_411
    
    hide screen astoria_main
    hide screen susan_main
    hide screen blktone
    call blkfade from _call_blkfade_43
    
    call nar("Susan slowly starts walking around your desk before obediently crawling under.") from _call_nar_105
    pause.5
    hide screen blkfade
    call ast_main("","smile","base","base","down",xpos="mid",ypos="base",trans="fade") from _call_ast_main_412
    hide screen bld1
    call ctc from _call_ctc_73
    
    show screen blktone
    call ast_main("And you're not allowed to come out until dumby covers you in his nasty goop!","open","closed","base","mid") from _call_ast_main_413
    sus "yes..."
    call ast_main("And you have to love it down there!","disgust","narrow","base","down") from _call_ast_main_414
    sus "...Love it?"
    call ast_main("Yep! You have to love how it smells and how it looks and how gross it is!","open","closed","base","mid") from _call_ast_main_415
    sus "I'll love it..."
    call ast_main("Good!","clench","angry","angry","angry") from _call_ast_main_416
    m "Isn't that a little much?"
    call ast_main("Pfft! That's rich coming from you dumby!","pout","narrow","narrow","mid") from _call_ast_main_417
    call ast_main("If it was up to you she'd be touching your nasty old wrinkly thing!","pout","narrow","narrow","R") from _call_ast_main_418
    call ast_main("With her mouth!","disgust","narrow","narrow","down") from _call_ast_main_419
    m "I suppose you're right..."
    call ast_main("Of course I am!","pout","narrow","narrow","R") from _call_ast_main_420
    call ast_main("Now get back to stroking that gross cock of yours!","open","closed","angry","mid") from _call_ast_main_421
    m "You don't have to tell me twice!"
    call nar(">You renew your efforts, encouraged by the image of the well-endowed redhead hidden under your desk.") from _call_nar_106
    call ast_main("And susy...","open","narrow","narrow","down") from _call_ast_main_422
    sus "Yes..."
    call ast_main("Time for you to wake up...","grin","angry","angry","down") from _call_ast_main_423
    sus "..."
    
    call play_music("hermione_theme") from _call_play_music_76
    hide screen blktone
    hide screen bld1
    with d3
    pause.5
    show screen bld1
    with hpunch
    sus "W-w-what's happening?"
    call play_sound("kick") from _call_play_sound_80
    with vpunch
    pause.2
    sus "Ouch..."
    pause.5
    sus "Where am I?"
    call ast_main("Don't you remember crawling under your headmaster's desk, begging him to jerk his nasty old cock for you?","open","closed","base","mid") from _call_ast_main_424
    with hpunch
    sus "WHAT?"
    sus "I'd never do something like that!"
    call ast_main("Really? Because it sure looks like you did...","grin","base","base","R") from _call_ast_main_425
    sus "I--" 
    sus "I don't know why..."
    call ast_main("If you don't like it down there, why don't you just hop out then?","pout","base","base","R") from _call_ast_main_426
    sus "I can't!"
    call ast_main("Really? why's that susy?","grin","narrow","narrow","down") from _call_ast_main_427
    sus "I don't know... I just can't!"
    call ast_main("Hmmm... it must be because you're such a nasty little slut then...","open","closed","base","mid") from _call_ast_main_428
    with hpunch
    "I am not!"
    call ast_main("Are you sure?","grin","angry","angry","down") from _call_ast_main_429
    sus "Y-yes..."
    call ast_main("because it sure doesn't look like that...","open","narrow","narrow","down") from _call_ast_main_430
    call ast_main("In fact, it looks like you're the nastiest little slut this school has ever seen!","grin","closed","base","mid") from _call_ast_main_431
    g4 "That's it, Astoria..."
    sus "Professor... {b}please...{/b}"
    call ast_main("Please what, Susan?","open","closed","base","mid") from _call_ast_main_432
    call ast_main("Please stop?","open","narrow","narrow","down") from _call_ast_main_433
    call ast_main("Or please coat me in cum?","disgust","narrow","narrow","down") from _call_ast_main_434
    with hpunch
    sus "ASTORIA!"
    call ast_main("Answer the question, Susy...","open","base","base","mid") from _call_ast_main_435
    sus "..."
    sus "Please sir..."
    sus "{size=-3}Coat {size=-3}me {size=-3}in {size=-3}your {size=-3}cum...{/size}"
    call ast_main("I knew it!","scream","wide","wide","wide") from _call_ast_main_436
    call ast_main("You're a dirty little slut after all aren't you!","clench","angry","angry","down") from _call_ast_main_437
    sus "I am not! I don't know why I'm down here!"
    call ast_main("Alright then... if you're such a good girl...","open","closed","base","mid") from _call_ast_main_438
    call ast_main("Why don't you tell me what it's like down there?","smile","narrow","narrow","down") from _call_ast_main_439
    sus "Down here?"
    sus "Under professor dumbledore's desk?"
    call ast_main("Mhmm... I bet it's nasty down there...","clench","angry","angry","down") from _call_ast_main_440
    call ast_main("It probably smells gross with all the yucky cum he shoots against that desk of his...","open","base","base","R") from _call_ast_main_441
    call ast_main("Not to mention his smelly old cock...","disgust","ahegao","ahegao","ahegao") from _call_ast_main_442
    m "Ahem..."
    call ast_main("Shh, dumby!","pout","angry","angry","R") from _call_ast_main_443
    call ast_main("So go on, Susy... tell me what it's like...","open","closed","base","mid") from _call_ast_main_444
    
    sus "It... It's..."
    call nar(">you hear susan take a deep breath before she goes to speak.") from _call_nar_107
    sus "{size=+10}It's incredible!{/size}"
    call ast_main("","grin","angry","angry","mid") from _call_ast_main_445
    sus "Everything about it is fantastic!"
    call ast_main("","smile","base","base","mid") from _call_ast_main_446
    sus "The cum stains on the back of the desk..."
    call ast_main("","disgust","narrow","base","mid") from _call_ast_main_447
    sus "The thick smell of semen in the air..."
    call ast_main("","disgust","narrow","narrow","R") from _call_ast_main_448
    sus "The way Dumbledore's stroking his {b}cock{/b}..."
    call ast_main("","clench","narrow","narrow","R") from _call_ast_main_449
    sus "That cock... that's the best part..."
    sus "I just want to--"
    call ast_main("(Eeeegh--...)","tongue_disgust","closed","narrow","R",trans="hpunch") from _call_ast_main_450
    
    sus "..."
    call nar(">You hear susan's words trail off into nothingness as she takes another breath...") from _call_nar_108
    sus "I wish I could live down here! Is that what you wanted to hear you evil witch?!"
    call ast_main("Almost...","grin","narrow","narrow","down") from _call_ast_main_451
    call ast_main("I want you to say you're a slut...","grin","angry","angry","mid") from _call_ast_main_452
    call ast_main("Then I'll let you go...","open","closed","base","mid") from _call_ast_main_453
    sus "Really? You mean I won't have to..."
    sus "Alright..."
    sus "{size=-5}I'm a... {size=-3}slut...{/size}"
    call ast_main("Hmmm, I'm not sure I heard anything... What about you dumby?","pout","base","base","R") from _call_ast_main_454
    m "Ah... almost..."
    call ast_main("Go on susy... one more time...","smile","narrow","narrow","down") from _call_ast_main_455
    with hpunch
    sus "I'm a slut, OK!"
    g4 "Ah... YES..."
    sus "I'm a nasty slut who crawled under her headmasters desk and--"
    
    g4 "HERE IT COMES SLUT!"
    hide screen bld1
    call gen_chibi("cumming_behind_desk") from _call_gen_chibi_20
    call cum_block from _call_cum_block_21
    sus "No wait! Astoria, you said I could go--"
    call cum_block from _call_cum_block_22
    g4 "ARGHHHH!!!"
    call nar("Susan's desperate screams prove too much for you as your cock begins to fire off an immense load onto Susan's face...") from _call_nar_109
    g4 "HERE IT IS SLUT!!!"
    call cum_block from _call_cum_block_23
    sus "..."
    
    call ast_main("That's it, [ast_genie_name]! Make sure you get it all out...","grin","angry","angry","mid") from _call_ast_main_456
    g4 "Ahhh... don't worry about that..."
    call nar(">You give your cock a few final pumps, working out the last of your load onto Susan's waiting face...") from _call_nar_110
    
    call gen_chibi("cum_on_desk") from _call_gen_chibi_21
    pause.5
    g4 "There we go..."
    call ast_main("Nice work, [ast_genie_name]...","open","closed","base","mid") from _call_ast_main_457
    call ast_main("You can come out now, Susy...","smile","narrow","narrow","down") from _call_ast_main_458
    sus "..."
    hide screen astoria_main
    call blkfade from _call_blkfade_44
    
    call nar(">Susan slowly crawls out from under your desk...") from _call_nar_111
    
    $ susan_face_covered = True
    hide screen blkfade
    call sus_main("","upset","narrow","worried","L",xpos="mid",ypos="base",trans="fade") from _call_sus_main_126
    call ctc from _call_ctc_74
    
    call ast_main("Oh my god! He absolutely covered you!","scream","base","base","mid",xpos="close",ypos="base") from _call_ast_main_459
    call sus_main("...","upset","narrow","base","L") from _call_sus_main_127
    call ast_main("I didn't know you had it in you, dumby!","scream","wide","wide","wide") from _call_ast_main_460
    call ast_main("Nice work!","open","wide","wide","mid") from _call_ast_main_461
    m "Thanks..."
    call ast_main("And Susy... that look suits you.","grin","angry","angry","L") from _call_ast_main_462
    call sus_main("Are you done astoria?","open","narrow","base","L") from _call_sus_main_128
    call ast_main("Yeah... you can go now Susy...","smile","narrow","narrow","L") from _call_ast_main_463
    
    call nar(">Susan slowly wipes the cum from her face as she gets dressed.") from _call_nar_112
    
    hide screen susan_main
    $ susan_face_covered = False
    call sus_main("I hope you two are happy...","upset","narrow","base","down") from _call_sus_main_129
    
    call play_sound("door") from _call_play_sound_81
    hide screen susan_main
    with d3
    pause.5
    
    call nar(">She turns and runs out the door, tears streaming down her face.") from _call_nar_113
    call ast_main("ahahahahaha, that was incredible, dumby!","happy","wide","wide","mid") from _call_ast_main_464
    call ast_main("Did you see the look on that tramps face!","grin","ahegao","ahegao","ahegao") from _call_ast_main_465
    m "..."
    m "Yeah..."
    call ast_main("What's wrong, old man?","clench","angry","angry","mid") from _call_ast_main_466
    m "(I have created a monster...)" 
    m "Nothing... it's just... don't you think that was taking it a little far?"
    call ast_main("Pfft... it's nothing more than what that tramp deserves!","open","closed","angry","mid") from _call_ast_main_467
    call ast_main("She's just lucky I didn't make her touch your gross weiner!","clench","angry","angry","down") from _call_ast_main_468
    m "..."
    call ast_main("Don't tell me you've gotten soft, old man!","pout","narrow","narrow","mid") from _call_ast_main_469
    m "Well that's usually what happens after I--"
    call ast_main("That's not what I meant!","clench","closed","angry","mid") from _call_ast_main_470
    call ast_main("Besides, these spells were your idea in the first place!","open","closed","base","mid") from _call_ast_main_471
    m "I don't think that's--"
    call ast_main("Anyway, it's getting pretty late...","pout","narrow","narrow","R") from _call_ast_main_472
    call ast_main("I better go to bed.","open","closed","base","mid") from _call_ast_main_473
    m "Ugh... uhm... good night."
    call ast_main("Good night, [ast_genie_name]!","grin","happyCl","base","mid") from _call_ast_main_474
    
    call play_sound("door") from _call_play_sound_82
    hide screen astoria_main
    with d3
    pause.5
    
    call nar(">Astoria skips out of your room, humming all the way.") from _call_nar_114
    m "(That girl is even worse than me...)"

    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to Tonks.
    
    if astoria_affection < 3:
        $ astoria_affection = 3
        $ astoria_spell_progress = 0
    
    jump day_main_menu
    
    
    
    
    
#humiliate self for genie and astoria
#training labels are on the other page.

label hornify_spell_1: #first level hornify spell
    #Start grinding her hips in front of genie
label hornify_spell_2: #second level hornify spell
    #Takes her top of and starts shaking her boobs for genie
label hornify_spell_3: #third level hornify spell
    #Plays with herself in front of astoria and genie


label slutify_spell_1: #first level sluttify spell
    #Underwear becomes slutty
label slutify_spell_2: #second level sluttify spell
    #Skirt becomes short, vest only and slutty Underwear
label slutify_spell_3: #third level sluttify spell
    #Pink heart dress and no underwear


label orgasmio_spell_1: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times
    
    
    
    
    
    
    