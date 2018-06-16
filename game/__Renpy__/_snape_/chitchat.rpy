

### Snape Chitchat ###

label snape_chitchat:
 
#    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.

    ### WHORING LEVEL 01 ###
    if whoring >= 0 and whoring <= 2:
        if one_of_ten == 1:
            call sna_main("Do You really think you can do this?","snape_24") from _call_sna_main_277
            call sna_main("Do You think you can break the girl?","snape_25") from _call_sna_main_278
        
        elif one_of_ten == 2:
            call sna_main("Don't you just hate this wretched sunny weather?","snape_01") from _call_sna_main_279
            call sna_main("I wish it would rain every day.","snape_06") from _call_sna_main_280 
            
        elif one_of_ten == 3:
            call sna_main("I am feeling rather doubtful about our whole plan again...","snape_06") from _call_sna_main_281
            
        elif one_of_ten == 4:
            call sna_main("Are you sure that you are not Albus Dumbledore?","snape_05") from _call_sna_main_282
            sna "I'm still having a hard time believing this whole thing sometimes..."
  
        elif one_of_ten == 5:
            call sna_main("I killed a pupil once.","snape_01") from _call_sna_main_283
            call sna_main("Yes... I strangled the maggot with my bare hands.","snape_02") from _call_sna_main_284
            call sna_main("........*low growl*.","snape_03") from _call_sna_main_285
            call sna_main("Did that sound believable?","snape_05") from _call_sna_main_286
            call sna_main("The moment those animals stop fearing me, I'm done for.","snape_06") from _call_sna_main_287
            call sna_main("Cultivating fear in the hearts of your students is the most important task for every teacher.","snape_26") from _call_sna_main_288

        elif one_of_ten == 6:
            call sna_main("Those Weasley maggots...","snape_04") from _call_sna_main_289
            call sna_main("One of these days I'll just snap, I swear.","snape_07") from _call_sna_main_290

        elif one_of_ten == 7:
            call sna_main("Don't you think that owl post is a bit ridiculous?","snape_05") from _call_sna_main_291
            sna "I'd much rather use ravens."
            
        elif one_of_ten == 8:
            call sna_main("I'm having the worst day of my life...","snape_06") from _call_sna_main_292
            sna "So I'm really Not in the mood for chit-chats..."
            
        elif one_of_ten == 9:
            call sna_main("Being a wizard is a 24 hours a day...","snape_04") from _call_sna_main_293
            call sna_main("7 days a week...","snape_03") from _call_sna_main_294
            call sna_main("365 days a year job.","snape_04") from _call_sna_main_295
            sna "We get no vacation days..."
            
        elif one_of_ten == 10:
            call sna_main("Quidditch...","snape_04") from _call_sna_main_296
            call sna_main("What a waste of time and ressources!","snape_10") from _call_sna_main_297
            call sna_main("","snape_04") from _call_sna_main_298
        
    
    ### WHORING LEVEL 02 ###
    if whoring >= 3 and whoring <= 5:
        if one_of_ten == 1:
            call sna_main("I have yet to notice any changes in miss Granger's behavior...","snape_24") from _call_sna_main_299
            call sna_main("Are you sure that you know what you're doing?","snape_05") from _call_sna_main_300
            call sna_main("","snape_09") from _call_sna_main_301
        
        elif one_of_ten == 2:
            call sna_main("It sure feels good to be able to grant house points or take them away whenever I feel like it.","snape_24") from _call_sna_main_302
            sna "My authority among the students is growing every day..."
            call sna_main("And when I say \"authority\" I mean \"fear\".","snape_02") from _call_sna_main_303

        elif one_of_ten == 3:
            call sna_main("Did you know that the full moon is known to boost male potency?","snape_24") from _call_sna_main_304
            sna "It also makes it easier to focus at a task at hand, making you more proactive."
            call sna_main("But who gives a damn about that, am I right?","snape_28") from _call_sna_main_305
            call sna_main("","snape_29") from _call_sna_main_306

        elif one_of_ten == 4:
            call sna_main("My precious Slytherins make all of this torment worth while...","snape_06") from _call_sna_main_307
            call sna_main("Their skirts are getting shorter every week, I swear.","snape_19") from _call_sna_main_308
  
        elif one_of_ten == 5:
            call sna_main("There was a time when I was young and full of hope...","snape_06") from _call_sna_main_309
            call sna_main("Ha-ha... I'm pulling your leg, mate.","snape_28") from _call_sna_main_310
            call sna_main("I was never full of hope...","snape_29") from _call_sna_main_311

        elif one_of_ten == 6:
            call sna_main("Someone broke into my personal storage...","snape_16") from _call_sna_main_312
            call sna_main("Only took some gillyweed... lucky they didn't take any of my amorentia.","snape_29") from _call_sna_main_313
            call sna_main("Not that I need or use such things.","snape_09") from _call_sna_main_314

        elif one_of_ten == 7:
            call sna_main("A \"Men's rights movement\"...?","snape_05") from _call_sna_main_315
            call sna_main("What's next? A house elves' rights movement?","snape_04") from _call_sna_main_316
            call sna_main("How could a top student could be that dumb?","snape_06") from _call_sna_main_317
            
        elif one_of_ten == 8:
            call sna_main("I don't play favourites with my students.","snape_05") from _call_sna_main_318
            call sna_main("I merely tolerate some of them and hate the rest.","snape_04") from _call_sna_main_319
  
        elif one_of_ten == 9:
            call sna_main("There are four student houses at Hogwarts...","snape_24") from _call_sna_main_320
            sna "Slytherin, Ravenclaw, Gryffindor and..."
            call sna_main("...and Huff-something...","snape_05") from _call_sna_main_321
            call sna_main("No one really cares.","snape_29") from _call_sna_main_322
            call sna_main("","snape_09") from _call_sna_main_323
 
        elif one_of_ten == 10:
            call sna_main("Brooms are for kids and witches.","snape_24") from _call_sna_main_324
            call sna_main("You'll never see a self-respecting wizard prancing around on a broomstick.","snape_05") from _call_sna_main_325
            call sna_main("","snape_09") from _call_sna_main_326
        

    ### WHORING LEVEL 03 ###
    if whoring >= 6 and whoring <= 8:
        if one_of_ten == 1:
            call sna_main("Any progress on breaking our little ms. know-it-all?","snape_24") from _call_sna_main_327
            call sna_main("","snape_09") from _call_sna_main_328
        
        elif one_of_ten == 2:
            call sna_main("The other day this one girl sold me her panties for five house points.","snape_24") from _call_sna_main_329
            call sna_main("And man, was she excited about that...","snape_14") from _call_sna_main_330
            call sna_main("I think she would've given them away for free just to please me.","snape_19") from _call_sna_main_331
            call sna_main("","snape_09") from _call_sna_main_332

        elif one_of_ten == 3:
            call sna_main("I'm having a rather pleasant day so far...","snape_23") from _call_sna_main_333
            call sna_main("Bet you didn't expect to hear me saying that?","snape_02") from _call_sna_main_334

        elif one_of_ten == 4:
            call sna_main("Quidditch seems to steadily gain more and more popularity over the years...","snape_24") from _call_sna_main_335
            call sna_main("How disappointing...","snape_04") from _call_sna_main_336

        elif one_of_ten == 5:
            call sna_main("My life was incredibly dull before your arrival...","snape_24") from _call_sna_main_337
            call sna_main("Nowadays it's...","snape_05") from _call_sna_main_338
            call sna_main("...less dull.","snape_02") from _call_sna_main_339

        elif one_of_ten == 6:
            call sna_main("Regrets? I don't know the meaning of the word!","snape_05") from _call_sna_main_340
            call sna_main("I live a very fulfilling life.","snape_06") from _call_sna_main_341
            call sna_main("Ha-ha-ha! I'm sorry, I just can't say such nonsense with a straight face.","snape_28") from _call_sna_main_342
            call sna_main("","snape_26") from _call_sna_main_343

        elif one_of_ten == 7:
            call sna_main("There is no room for mistakes during class.","snape_24") from _call_sna_main_344
            call sna_main("One slip-up and the bloody bastards will tear you to shreds.","snape_04") from _call_sna_main_345

        elif one_of_ten == 8:
            call sna_main("You are the only person I have to answer to...","snape_04") from _call_sna_main_346
            call sna_main("So I can almost literally do whatever the bloody hell I want these days...","snape_05") from _call_sna_main_347
            call sna_main("...............","snape_09") from _call_sna_main_348
            call sna_main("So that's what freedom feels like, huh?","snape_06") from _call_sna_main_349

        elif one_of_ten == 9:
            call sna_main("Autumn... the most depressing time of the year...","snape_06") from _call_sna_main_350
            call sna_main("I Love it!","snape_02") from _call_sna_main_351
            call sna_main("","snape_23") from _call_sna_main_352

        elif one_of_ten == 10:
            call sna_main("I have a magical portrait of a stripper hanging in my room.","snape_24") from _call_sna_main_353
            call sna_main("One of my most precious possessions.","snape_22") from _call_sna_main_354
            call sna_main("","snape_09") from _call_sna_main_355
        

    ### WHORING LEVEL 04 ###
    if whoring >= 9 and whoring <= 11:
        if one_of_ten == 1:
            call sna_main("Lately miss Granger has gotten aggressive almost to the point of open hostility...","snape_24") from _call_sna_main_356
            call sna_main("I hope you know what you're doing...","snape_05") from _call_sna_main_357
            call sna_main("","snape_09") from _call_sna_main_358

        elif one_of_ten == 2:
            call sna_main("I shouldn't feel bad about having sex with my students, right?","snape_26") from _call_sna_main_359
            call sna_main("I mean, you should see the way some of those girls wear their uniforms...","snape_05") from _call_sna_main_360
            call sna_main("They're practically asking for it.","snape_13") from _call_sna_main_361
            call sna_main("","snape_12") from _call_sna_main_362

        elif one_of_ten == 3:
            call sna_main("It's been raining a lot lately...","snape_23") from _call_sna_main_363
            call sna_main("I wonder if I enjoy rainy weather so much simply because it makes most people miserable...","snape_02") from _call_sna_main_364
            call sna_main("","snape_23") from _call_sna_main_365

        elif one_of_ten == 4:
            call sna_main("According to a recent study 9 out of 10 girls secretly fantasize about being abused by their teacher.","snape_24") from _call_sna_main_366
            call sna_main("I bet that 10th girl was Hermione Granger.","snape_03") from _call_sna_main_367
            call sna_main("","snape_01") from _call_sna_main_368

        elif one_of_ten == 5:
            call sna_main("These days I have to actually make an effort to maintain my usual bad mood.","snape_24") from _call_sna_main_369
            call sna_main("","snape_23") from _call_sna_main_370

        elif one_of_ten == 6:
            call sna_main("Do You have a few condoms to spare?","snape_24") from _call_sna_main_371
            call sna_main("I have a whole pack but...","snape_25") from _call_sna_main_372
            call sna_main("...they've expired years ago...","snape_06") from _call_sna_main_373
            call sna_main("The changes you brought into my life, mate.","snape_02") from _call_sna_main_374
            call sna_main("","snape_23") from _call_sna_main_375

        elif one_of_ten == 7:
            call sna_main("You think we could turn Hogwarts into a \"girls only\" school?","snape_24") from _call_sna_main_376
            call sna_main("Hogwarts Girls Academy!","snape_23") from _call_sna_main_377
            call sna_main("Now that would be bloody perfect... except for Lockhart maybe.","snape_13") from _call_sna_main_378

        elif one_of_ten == 8:
            call sna_main("Why did the teacher cross the road?","snape_24") from _call_sna_main_379
            call sna_main("To get away from his students!","snape_25") from _call_sna_main_380
            call sna_main("Ha-ha-ha! Gets me every time!","snape_28") from _call_sna_main_381
            call sna_main("","snape_25") from _call_sna_main_382

        elif one_of_ten == 9:
            call sna_main("Want to hear a funny story?","snape_24") from _call_sna_main_383
            call sna_main("Well, I don't know any...","snape_06") from _call_sna_main_384

        elif one_of_ten == 10:
            call sna_main("Do you know what a \"royal goblet\" is?","snape_05") from _call_sna_main_385
            call sna_main("You do, don't you?","snape_13") from _call_sna_main_386
            call sna_main("","snape_23") from _call_sna_main_387

        
    ### WHORING LEVEL 05 ###
    if whoring >= 12 and whoring <= 14:
        if one_of_ten == 1:
            call sna_main("15 points for a blowjob is a fair price, right?","snape_24") from _call_sna_main_388
            call sna_main("","snape_23") from _call_sna_main_389

        elif one_of_ten == 2:
            call sna_main("Have you ever been in love, mate?","snape_24") from _call_sna_main_390
            call sna_main("Have you ever been in love with a schoolgirl?","snape_02") from _call_sna_main_391
            call sna_main("What about half a dozen of them at once?","snape_22") from _call_sna_main_392
            call sna_main("","snape_20") from _call_sna_main_393

        elif one_of_ten == 3:
            call sna_main("Something rather brilliant happened last night between me and this Slytherin mynx.","snape_20") from _call_sna_main_394
            call sna_main("Long story short, all of my muscles ache and I still feel rather dehydrated...","snape_22") from _call_sna_main_395
            call sna_main("","snape_13") from _call_sna_main_396

        elif one_of_ten == 4:
            call sna_main("It's getting colder lately...","snape_24") from _call_sna_main_397
            call sna_main("Winter is coming...","snape_23") from _call_sna_main_398
         
        elif one_of_ten == 5:
            call sna_main("Have you ever seen muggle women dressed as witches?","snape_24") from _call_sna_main_399
            call sna_main("So adorable.","snape_19") from _call_sna_main_400

        elif one_of_ten == 6:
            call sna_main("Do you know what an \"Internet\" is?","snape_24") from _call_sna_main_401
            call sna_main("Apparently it allows you to go \"on the line\" and see magical photographs of naked muggle women.","snape_02") from _call_sna_main_402 # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            call sna_main("Kind of makes me wish we had one here in Hogwarts.","snape_26") from _call_sna_main_403
            call sna_main("","snape_09") from _call_sna_main_404

        elif one_of_ten == 7:
            call sna_main("I have two major passions in life...","snape_24") from _call_sna_main_405
            sna "Dark arts..."
            call sna_main("......","snape_12") from _call_sna_main_406
            call sna_main("...and sluts.","snape_13") from _call_sna_main_407

        elif one_of_ten == 8:
            call sna_main("You think I ought to cut down on my drinking?","snape_24") from _call_sna_main_408
            call sna_main("But my life is so stressful...","snape_06") from _call_sna_main_409
            call sna_main("Hm...","snape_09") from _call_sna_main_410
            call sna_main("I'll try and cut down on the liquor...","snape_06") from _call_sna_main_411
            call sna_main("In favour of sweaty monkey-sex with my students!","snape_21") from _call_sna_main_412
            call sna_main("","snape_19") from _call_sna_main_413

        elif one_of_ten == 9:
            call sna_main("Miss Granger has been suspiciously quiet lately...","snape_24") from _call_sna_main_414
            call sna_main("I bet she is scheming something...","snape_03") from _call_sna_main_415
            call sna_main("","snape_01") from _call_sna_main_416

        elif one_of_ten == 10:
            call sna_main("It's quite easy to write a book and kill off half of the main characters for the sake of dramatic impact...","snape_24") from _call_sna_main_417
            sna "To put your characters against impossible odds and let them make it out alive in a believable manner..."
            call sna_main("Now {size=+7}that{/size} requires skill.","snape_02") from _call_sna_main_418
            call sna_main("","snape_23") from _call_sna_main_419
        
        
    ### WHORING LEVEL 06 ###
    if whoring >= 15 and whoring <= 17:
        if one_of_ten == 1:
            call sna_main("What if the girl is not our pet, but we are hers?","snape_11") from _call_sna_main_420
            call sna_main("","snape_26") from _call_sna_main_421

        elif one_of_ten == 2:
            call sna_main("Have you heard of the \"Slug club\"?","snape_24") from _call_sna_main_422
            sna "What if I start a club of my own?"
            call sna_main("I would call it the \"Snape Club\"!","snape_23") from _call_sna_main_423
            sna "I would invite girls over, offer them some tea and muffins..."
            call sna_main("Feel them up a little...","snape_13") from _call_sna_main_424
            call sna_main("Bloody brilliant!","snape_22") from _call_sna_main_425
            call sna_main("","snape_02") from _call_sna_main_426

        elif one_of_ten == 3:
            call sna_main("Tell me Genie... Have you ever had your asshole licked clean by a young witch?","snape_02") from _call_sna_main_427
            call sna_main("A life changing experience, neither less nor more...","snape_21") from _call_sna_main_428
            call sna_main("","snape_02") from _call_sna_main_429

        elif one_of_ten == 4:
            call sna_main("So, how is the training going?","snape_24") from _call_sna_main_430
            sna "All according to plan I hope?"
            call sna_main("","snape_05") from _call_sna_main_431

        elif one_of_ten == 5:
            call sna_main("I can see Thestrals, you know...","snape_06") from _call_sna_main_432
            call sna_main("","snape_09") from _call_sna_main_433

        elif one_of_ten == 6:
            call sna_main("You know what I like about Quidditch?","snape_24") from _call_sna_main_434
            call sna_main("Nothing! Not a single bloody thing!","snape_15") from _call_sna_main_435
            call sna_main("","snape_16") from _call_sna_main_436

        elif one_of_ten == 7:
            call sna_main("Hogwarts benefited greatly from your arrival.","snape_24") from _call_sna_main_437
            call sna_main("And when I say \"Hogwarts\" I mean \"me\".","snape_02") from _call_sna_main_438
            call sna_main("","snape_23") from _call_sna_main_439

        elif one_of_ten == 8:
            call sna_main("Real wizards wear black.","snape_24") from _call_sna_main_440
            call sna_main("Am I right?","snape_02") from _call_sna_main_441
            call sna_main("","snape_23") from _call_sna_main_442

        elif one_of_ten == 9:
            call sna_main("Some of those Slytherin girls simply adore me these days...","snape_24") from _call_sna_main_443
            call sna_main("Personally I'd much rather be feared...","snape_05") from _call_sna_main_444
            call sna_main("But I am willing to settle for mindless adoration...","snape_23") from _call_sna_main_445

        elif one_of_ten == 10:
            call sna_main("You are being way too generous with those Gryffindor points, mate.","snape_24") from _call_sna_main_446
            call sna_main("Lately I can barely keep up with you...","snape_25") from _call_sna_main_447
            call sna_main("","snape_29") from _call_sna_main_448
        
   
    ### WHORING LEVEL 07 ###
    if whoring >= 18 and whoring <= 20:
        if one_of_ten == 1:
            call sna_main("Miss Granger really is changing. I can see it clearly now...","snape_24") from _call_sna_main_449
            sna "Her grades went down and even her attendance is far from perfect now..."
            call sna_main("But despite that she continues to excel at being a pain in my arse!","snape_10") from _call_sna_main_450
            call sna_main("","snape_01") from _call_sna_main_451

        elif one_of_ten == 2:
            call sna_main("My least favourite colour?","snape_05") from _call_sna_main_452
            call sna_main("Let me give you two: red and gold.","snape_07") from _call_sna_main_453
            call sna_main("","snape_04") from _call_sna_main_454

        elif one_of_ten == 3:
            call sna_main("I hear the vampire-theme is quite popular among the girls lately.","snape_24") from _call_sna_main_455
            call sna_main("I would make a great vampire, don't you think?","snape_05") from _call_sna_main_456
            sna "Maybe I should buy a couple of those fake fangs..."
            call sna_main("Just to drive the horny, little sluts completely crazy.","snape_21") from _call_sna_main_457
            call sna_main("","snape_02") from _call_sna_main_458

        elif one_of_ten == 4:
            call sna_main("I ...hate my life.","snape_24") from _call_sna_main_459
            call sna_main("No, wait, let me try this again...","snape_16") from _call_sna_main_460
            call sna_main("I ...hate my life.","snape_17") from _call_sna_main_461
            call sna_main("Dammit! I'm trying to say \"love\" but it just won't come out...","snape_25") from _call_sna_main_462
            call sna_main("I don't think I've ever used the words \"love\" and \"life\" in one sentence before.","snape_29") from _call_sna_main_463
            call sna_main("Let me try this again...","snape_06") from _call_sna_main_464
            call sna_main("I ha...{w} lo... {w}love my life!","snape_10") from _call_sna_main_465
            call sna_main("There you go, I love my life...","snape_23") from _call_sna_main_466

        elif one_of_ten == 5:
            call sna_main("Sunlight, chocolate, Quidditch, cats and orange juice...","snape_01") from _call_sna_main_467
            sna "That's a list of things I don't care for..."
            call sna_main("Here is a short list of things I do care for a great deal...","snape_02") from _call_sna_main_468
            call sna_main("The dark arts, wine and pussy.","snape_23") from _call_sna_main_469

        elif one_of_ten == 6:
            call sna_main("have You ever seen two wizards in a fistfight?","snape_02") from _call_sna_main_470
            call sna_main("Bloody hilarious!","snape_28") from _call_sna_main_471
            call sna_main("","snape_23") from _call_sna_main_472

        elif one_of_ten == 7:
            call sna_main("You know that feeling when you just came in a girl's mouth and she swallows it all and says: \"Thank you, professor\"?","snape_14") from _call_sna_main_473
            call sna_main("Isn't that the best?","snape_13") from _call_sna_main_474
            call sna_main("","snape_23") from _call_sna_main_475

        elif one_of_ten == 8:
            call sna_main("do You think the Hogwarts ghosts sometimes spy on girls taking when they a shower and such?","snape_24") from _call_sna_main_476
            call sna_main("If I were a ghost I know I would.","snape_13") from _call_sna_main_477
            call sna_main("","snape_23") from _call_sna_main_478

        elif one_of_ten == 9:
            call sna_main("This one girl confessed to me that she has frequent fantasizes about being abused by that squib mr.Filch.","snape_19") from _call_sna_main_479
            call sna_main("I think I could arrange that. Should I?","snape_14") from _call_sna_main_480
            call sna_main("","snape_02") from _call_sna_main_481

        elif one_of_ten == 10:
            call sna_main("I used to hate my job so much...","snape_24") from _call_sna_main_482
            call sna_main("Hate is clean, simple and certain...","snape_06") from _call_sna_main_483
            call sna_main("Now, don't get me wrong - I still hate it.","snape_0") from _call_sna_main_484
            call sna_main("But I also sort of love it now...","snape_05") from _call_sna_main_485
            sna "How could I not? With all that has been happening lately?"
            call sna_main("To both cherish and hate something to an equal degree...","snape_06") from _call_sna_main_486
            call sna_main("It's like being in love again...","snape_19") from _call_sna_main_487
            call sna_main("","snape_06") from _call_sna_main_488
        
        
    ### WHORING LEVEL 08+ ###
    if whoring >= 21:
        if one_of_ten == 1:
            call sna_main("Do you know what a \"bukkake\" is?","snape_24") from _call_sna_main_489
            sna "What about \"deepthroating\"?"
            sna "And then there is also \"hate-sex\"."
            call sna_main("Kids these days, mate...","snape_05") from _call_sna_main_490
            sna "They have a special name for everything."
            call sna_main("Although \"hate-sex\" has always been around...","snape_06") from _call_sna_main_491
            call sna_main("Back in my days we just called it \"sex\".","snape_02") from _call_sna_main_492

        elif one_of_ten == 2:
            call sna_main("I heard a mysterious ticking noise today...","snape_04") from _call_sna_main_493
            call sna_main("It was kind of catchy...","snape_28") from _call_sna_main_494

        elif one_of_ten == 3:
            call sna_main("I organized a small party the other day...","snape_24") from _call_sna_main_495
            sna "One girl and three boys..."
            call sna_main("They fucked her and I watched...","snape_13") from _call_sna_main_496
            call sna_main(".........................","snape_29") from _call_sna_main_497
            call sna_main("You think I've been exercising my dark side a bit too often lately?","snape_05") from _call_sna_main_498
            call sna_main("","snape_06") from _call_sna_main_499

        elif one_of_ten == 4:
            call sna_main("I'm all out of condoms, mate.","snape_24") from _call_sna_main_500
            call sna_main("You think you could hook me up?","snape_02") from _call_sna_main_501
            call sna_main("","snape_01") from _call_sna_main_502

        elif one_of_ten == 5:
            call sna_main("I am secretly making this special herbal brew that should make her tits lactate...","snape_24") from _call_sna_main_503
            call sna_main("Pretty brilliant, huh?","snape_13") from _call_sna_main_504
            call sna_main("","snape_23") from _call_sna_main_505

        elif one_of_ten == 6:
            call sna_main("So, this witch has my cock in her mouth, right?","snape_24") from _call_sna_main_506
            call sna_main("Her hot girlfriend is cleaning my asshole with her tongue...","snape_02") from _call_sna_main_507
            sna "Meanwhile this third girl is on her knees with her mouth open, waiting for me to spit in it..."
            sna "And every time I spit, she says: \"Thank you, professor Snape\"."
            call sna_main("That was a bloody surreal evening...","snape_22") from _call_sna_main_508
            call sna_main("","snape_02") from _call_sna_main_509

        elif one_of_ten == 7:
            call sna_main("This one girl has been begging me to urinate in her mouth for days, now...","snape_06") from _call_sna_main_510
            sna "Persistent little minx..."
            call sna_main("Should I give in?","snape_05") from _call_sna_main_511
            call sna_main("","snape_23") from _call_sna_main_512

        elif one_of_ten == 8:
            call sna_main("I mercilessly dominate both male and female students...","snape_04") from _call_sna_main_513
            call sna_main("But in very different ways.","snape_22") from _call_sna_main_514
            call sna_main("","snape_23") from _call_sna_main_515

        elif one_of_ten == 9:
            call sna_main("I love my life!","snape_23") from _call_sna_main_516
            call sna_main("Still hate my job though...","snape_16") from _call_sna_main_517
            call sna_main("I wish I could skip all the teaching, but keep all the fucking.","snape_14") from _call_sna_main_518
            call sna_main("","snape_23") from _call_sna_main_519

        elif one_of_ten == 10:
            call sna_main("I almost feel bad for having all the fun.","snape_24") from _call_sna_main_520
            call sna_main("do You want me to send you up some young slut?","snape_14") from _call_sna_main_521
            call sna_main("","snape_23") from _call_sna_main_522
    

    return
    
