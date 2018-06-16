#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

### Equip Makeup ###
### Equip Glasses ###
### Equip Ears ###
### Equip Hat ###

label equip_makeup:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_makeup
    #Luna
    if active_girl == "luna":
        jump equip_lun_makeup
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_makeup


### Equip Hermione's Makeup ###

label equip_her_makeup:

    if mad >= 1:
        jump equipping_failed

    if makeup_choice == "lipstick":
        hide screen wardrobe
        call her_main(xpos="right",ypos="base",trans="fade") from _call_her_main_294
        
        menu:
            "-Change Lipstick Colour-"
            "-Red Lipstick-" if reward_her_red_lipstick and not h_lipstick == "red": #Hypno potion event.
                $ makeup_choice = "red_lipstick"
                jump equi_her_makeup_lipstick
            "-Remove Red Lipstick-" if h_lipstick == "red": #Unequip
                $ makeup_choice = "nude"
                jump equi_her_makeup_lipstick
            "-Never mind-":
                jump return_to_wardrobe
        
        label equi_her_makeup_lipstick:
        
            if makeup_choice == "red_lipstick":
           
                $ wardrobe_active = 0 #activates dissolve in her_main 

                if h_lipstick == "nude":
                    call her_main("You want me to put on lipstick?","normal","worriedCl") from _call_her_main_295
                    call her_main("Really, [genie_name]!","scream","angryCl") from _call_her_main_296
                    m "Just a little bit."
            
                    call her_main("Alright then...","base","glance") from _call_her_main_297
                    hide screen hermione_main
                    with d5
                
                    $ h_lipstick = "red"
            
                    call update_her_uniform from _call_update_her_uniform_1 #Updates clothing and body.
            
            else: #Nude
                call her_main("You want me to take the lipstick off?","annoyed","ahegao") from _call_her_main_298
                call her_main("Alright then...","annoyed","down") from _call_her_main_299
                hide screen hermione_main
                with d5
                
                $ h_lipstick = "nude"
            
                call update_her_uniform from _call_update_her_uniform_2 #Updates clothing and body.
                
            jump return_to_wardrobe
            
    if makeup_choice not in hermione_makeup_list:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Freckles
            if makeup_choice == "freckles":
                m "Would you apply some makeup for me? I think freckles would look cute on you."
                if whoring >= 14:
                    call her_main("Sure, [genie_name].","soft","base") from _call_her_main_300
                    call her_main("Let me just put on a few dots on...","base","glance") from _call_her_main_301
                else:
                    call her_main("Hmm","normal","frown") from _call_her_main_302
                    call her_main("I suppose I can put an few dots...","annoyed","frown") from _call_her_main_303

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Would you cover yourself with this? It's fake--uuuh... fake cum..."

                if whoring >= 20:
                    if whoring < 24:
                        call her_main("Fake cum...?","soft","base") from _call_her_main_304
                        call her_main("...","annoyed","suspicious") from _call_her_main_305
                        call her_main("well as long as it's not real...","base","glance") from _call_her_main_306
                    else: #24
                        call her_main("Hm...?","soft","base") from _call_her_main_307
                        call her_main("You want me to cover myself in fake cum?","annoyed","suspicious") from _call_her_main_308
                        call her_main("{size=-5}(It's a shame it's not real...){/size}","base","down") from _call_her_main_309
                        call her_main("Fine, I'll do it [genie_name].","base","glance") from _call_her_main_310
                else:
                    if whoring < 8:
                        jump too_much
                    else: #8-19
                        call her_main("Fake cum...?","open","worried") from _call_her_main_311
                        call her_main("You cannot be serious, [genie_name]!","open","base") from _call_her_main_312
                        m "What's wrong? It's not real..."
                        call her_main("[genie_name] I am not going to smear myself with cum, real or not, and then parade around the school!","normal","frown") from _call_her_main_313
                        call her_main("I absolutely refuse!","annoyed","frown") from _call_her_main_314
                    ">She won't cover herself in cum just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice) from _call_set_h_makeup

            call her_main("","","",xpos="wardrobe") from _call_her_main_315
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice) from _call_set_h_makeup_1
            call her_main("","","",xpos="wardrobe") from _call_her_main_316
            call screen wardrobe


    else: #Remove makeup

        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Freckles
            if makeup_choice == "freckles":
                m "Could you remove those freckles again?"
                call her_main("Alright. Let me just wipe it off.","base","base") from _call_her_main_317

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Could you take that cum off your head again?"
                call her_main("Alright. Let me wipe it off.","base","base") from _call_her_main_318

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice) from _call_set_h_makeup_2 #Removes Item

            call her_main("","","",xpos="wardrobe") from _call_her_main_319
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice) from _call_set_h_makeup_3 #Removes Item
            call her_main("","","",xpos="wardrobe") from _call_her_main_320
            call screen wardrobe
#

#Add Luna Makeup Texts
#Add Astoria Makeup Texts





label equip_head_accessory:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_head_accessory

    #Luna
    if active_girl == "luna":
        jump equip_lun_head_accessory

    #Astoria
    if active_girl == "astoria":
        jump equip_ast_head_accessory


### Equip Hermione's Head Accessory ###

label equip_her_head_accessory:

    if head_accessory_choice == h_glasses and glasses_color_choice == h_glasses_color or head_accessory_choice == h_ears or head_accessory_choice == h_hat:
        jump remove_head_accessory

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Reading Glasses
            if head_accessory_choice == "reading_glasses":
                m "Could you wear those reading glasses for me?"

                if whoring < 11:
                    call her_main("Reading glasses...?","open","worried") from _call_her_main_321
                    call her_main("But I can see just fine, [genie_name].","normal","frown") from _call_her_main_322
                    m "Don't worry, they have fake lenses."
                    call her_main("I suppose I could wear them...","annoyed","frown") from _call_her_main_323
                    call her_main("Let me put them on real quick.","base","base") from _call_her_main_324
                else:
                    call her_main("Sure, [genie_name].","soft","base") from _call_her_main_325
                    call her_main("I will wear them for you.","base","glance") from _call_her_main_326

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Could you wear these vintage glasses for me?"

                if whoring < 11:
                    call her_main("Vintage glasses...?","open","worried") from _call_her_main_327
                    call her_main("I don't need to wear glasses, [genie_name]. I can see just fine!","open","closed") from _call_her_main_328
                    m "They aren't real glasses. These lenses are fake."
                    call her_main("I see... I suppose I could wear them...","annoyed","frown") from _call_her_main_329
                    call her_main("Let me put them on real quick.","base","base") from _call_her_main_330
                else:
                    call her_main("Sure, [genie_name].","soft","base") from _call_her_main_331
                    call her_main("I don't mind looking a bit nerdy...","open","baseL") from _call_her_main_332
                    call her_main("Let me put them on for you.","base","glance") from _call_her_main_333

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Could you wear these cat-ears for me?"

                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Cat-ears, [genie_name]?","open","worried") from _call_her_main_334
                        call her_main("(They do look cute...)","base","glance") from _call_her_main_335
                        call her_main("...","annoyed","down") from _call_her_main_336 #annoyed, down
                        m "So, are you going to wear them or not?"
                        call her_main("Fine, [genie_name]. Let me just put them on real quick.","soft","baseL") from _call_her_main_337
                    else:
                        call her_main("They do look cute...","base","glance") from _call_her_main_338
                        call her_main("(And they even match my hair!)","base","down") from _call_her_main_339
                        call her_main("Let me put them on for you.","base","glance") from _call_her_main_340
                else:
                    call her_main("Cat-ears...?","open","worried") from _call_her_main_341
                    call her_main("Really, [genie_name]?!","open","base") from _call_her_main_342
                    m "What's wrong? They're cute..."
                    call her_main("I'm not going to wear cat ears, [genie_name]!","annoyed","angryL") from _call_her_main_343
                    m "Fine. Forget it..."

                    ">She won't wear cat-ears just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            #Elf Ears
            if head_accessory_choice == "elf_ears":
                m "Could you wear these elf-ears for me?"

                if whoring >= 11:
                    if h_hair_style != "B":
                        call her_main("Elf-ears...?","soft","base") from _call_her_main_344
                        call her_main("You wouldn't even be able to see them beneath all my hair...","open","closed") from _call_her_main_345
                        m "You are right..."
                        m "Could you change your hair too then? Show off your cute little ears?"

                    if whoring < 17:
                        call her_main("...","annoyed","suspicious") from _call_her_main_346
                        call her_main("I suppose they're not too noticeable...","base","glance") from _call_her_main_347
                        call her_main("Alright. I will wear them.","soft","base") from _call_her_main_348
                        call her_main("Let me put them on real quick.","soft","baseL") from _call_her_main_349
                    else:
                        call her_main("...","annoyed","down") from _call_her_main_350
                        call her_main("They do look cute...","base","down") from _call_her_main_351
                        call her_main("Alright, [genie_name]. I will wear them for you.","base","glance") from _call_her_main_352
                else:
                    call her_main("elf-ears...?","open","worried") from _call_her_main_353
                    call her_main("I refuse, [genie_name]!","open","base") from _call_her_main_354
                    m "Why not? Don't you support the house elves or something..."
                    call her_main("It's not about...","annoyed","angryL") from _call_her_main_355
                    call her_main("I'm not going to wear these ridiculous ears for you, [genie_name]!","annoyed","angryL") from _call_her_main_356
                    call her_main("...","annoyed","baseL") from _call_her_main_357

                    ">She won't wear cat-ears just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            #Tiara
            if head_accessory_choice == "tiara":

                call her_main("A tiara...?","open","worried") from _call_her_main_358
                call her_main("I suppose I can wear it...","annoyed","frown") from _call_her_main_359
                call her_main("let me just go put it on.","base","glance") from _call_her_main_360

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) from _call_set_h_glasses
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) from _call_set_h_ears
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) from _call_set_h_hat

            call her_main("","","",xpos="wardrobe") from _call_her_main_361
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) from _call_set_h_glasses_1
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                if whoring >= 11:
                    call set_h_ears(head_accessory_choice) from _call_set_h_ears_1
                else:
                    ">She won't wear those ears just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) from _call_set_h_hat_1

            call her_main("","","",xpos="wardrobe") from _call_her_main_362
            call screen wardrobe


label remove_head_accessory: #Remove/Toggle off

        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            #Reading Glasses
            if head_accessory_choice == "reading_glasses":
                m "Could you take off those reading glasses?"
                call her_main("Sure. Let me take them off.","base","base") from _call_her_main_363

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Could you take off those glasses again?"
                call her_main("Alright. I will take them off.","base","base") from _call_her_main_364

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Could you take off those cat-ears again?"
                call her_main("Sure. Let me take them off.","base","base") from _call_her_main_365

            #Elf Ears
            if head_accessory_choice == "elf_ears":
                m "Could you take those ears off again?"
                call her_main("Alright. Let take them off.","base","base") from _call_her_main_366

            #Tiara
            if head_accessory_choice == "tiara":
                m "Could you take off that tiara?"
                call her_main("Sure. I will take it off.","base","base") from _call_her_main_367

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) from _call_set_h_glasses_2
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) from _call_set_h_ears_2
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) from _call_set_h_hat_2

            call her_main("","","",xpos="wardrobe") from _call_her_main_368
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice) from _call_set_h_glasses_3
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice) from _call_set_h_ears_3
            if head_accessory_choice == "tiara":
                call set_h_hat(head_accessory_choice) from _call_set_h_hat_3

            call her_main("","","",xpos="wardrobe") from _call_her_main_369
            call screen wardrobe

#

#Add Luna's Head Accessory Texts
#Add Astoria's Head Accessory Texts