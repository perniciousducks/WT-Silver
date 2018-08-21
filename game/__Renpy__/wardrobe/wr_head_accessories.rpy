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

    if makeup_choice in ["red_lipstick","pink_lipstick","turquoise_lipstick"]:
        hide screen wardrobe
        call her_main(xpos="right",ypos="base",trans="fade")

        if makeup_choice != h_lipstick:
            $ wardrobe_active = 0 #activates dissolve in her_main

            call her_main("You want me to put on lipstick?","normal","worriedCl")
            call her_main("Really, [genie_name]!","scream","angryCl")
            m "Just a little bit."

            call her_main("Alright then...","base","glance")
            hide screen hermione_main
            with d5

            $ h_lipstick = makeup_choice

            call update_her_uniform #Updates clothing and body.

        else: #Nude
            call her_main("You want me to take the lipstick off?","annoyed","ahegao")
            call her_main("Alright then...","annoyed","down")
            hide screen hermione_main
            with d5

            $ h_lipstick = "nude"

            call update_her_uniform #Updates clothing and body.

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
                    call her_main("Sure, [genie_name].","soft","base")
                    call her_main("Let me just put on a few dots on...","base","glance")
                else:
                    call her_main("Hmm","normal","frown")
                    call her_main("I suppose I can put an few dots...","annoyed","frown")

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Would you cover yourself with this? It's fake--uuuh... fake cum..."

                if whoring >= 20:
                    if whoring < 24:
                        call her_main("Fake cum...?","soft","base")
                        call her_main("...","annoyed","suspicious")
                        call her_main("well as long as it's not real...","base","glance")
                    else: #24
                        call her_main("Hm...?","soft","base")
                        call her_main("Do you want me to cover myself in fake cum, [genie_name]?","annoyed","suspicious")
                        call her_main("Or just my face?","annoyed","suspicious")
                        menu:
                            "-Covered-":
                                $ makeup_choice = "fake_cum_2"
                                call her_main("Mmmm, thank you [genie_name]...","grin","ahegao")
                            "-Face-":
                                $ makeup_choice = "fake_cum_3"
                                call her_main("Oh. Alright then [genie_name]...","upset","concerned")

                        call her_main("{size=-5}(It's a shame this isn't real...){/size}","base","down")
                        call her_main("Fine, I'll do it [genie_name].","base","glance")
                else:
                    if whoring < 8:
                        jump too_much
                    else: #8-19
                        call her_main("Fake cum...?","open","worried")
                        call her_main("You cannot be serious, [genie_name]!","open","base")
                        m "What's wrong? It's not real..."
                        call her_main("[genie_name] I am not going to smear myself with cum, real or not, and then parade around the school!","normal","frown")
                        call her_main("I absolutely refuse!","annoyed","frown")
                    ">She won't cover herself in cum just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice)

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice)
            call her_main("","","",xpos="wardrobe")
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
                call her_main("Alright. Let me just wipe it off.","base","base")

            #Fake Cum
            if makeup_choice == "fake_cum":
                m "Could you take that cum off your head again?"
                call her_main("Alright. Let me wipe it off.","base","base")

            hide screen hermione_main
            with d3

            pause.5

            call set_h_makeup(makeup_choice) #Removes Item

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_makeup(makeup_choice) #Removes Item
            call her_main("","","",xpos="wardrobe")
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
        jump equip_ast_hat

    #Susan
    if active_girl == "astoria":
        jump equip_sus_hat

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
                    call her_main("Reading glasses...?","open","worried")
                    call her_main("But I can see just fine, [genie_name].","normal","frown")
                    m "Don't worry, they have fake lenses."
                    call her_main("I suppose I could wear them...","annoyed","frown")
                    call her_main("Let me put them on real quick.","base","base")
                else:
                    call her_main("Sure, [genie_name].","soft","base")
                    call her_main("I will wear them for you.","base","glance")

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Could you wear these vintage glasses for me?"

                if whoring < 11:
                    call her_main("Vintage glasses...?","open","worried")
                    call her_main("I don't need to wear glasses, [genie_name]. I can see just fine!","open","closed")
                    m "They aren't real glasses. These lenses are fake."
                    call her_main("I see... I suppose I could wear them...","annoyed","frown")
                    call her_main("Let me put them on real quick.","base","base")
                else:
                    call her_main("Sure, [genie_name].","soft","base")
                    call her_main("I don't mind looking a bit nerdy...","open","baseL")
                    call her_main("Let me put them on for you.","base","glance")

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Could you wear these cat-ears for me?"

                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Cat-ears, [genie_name]?","open","worried")
                        call her_main("(They do look cute...)","base","glance")
                        call her_main("...","annoyed","down") #annoyed, down
                        m "So, are you going to wear them or not?"
                        call her_main("Fine, [genie_name]. Let me just put them on real quick.","soft","baseL")
                    else:
                        call her_main("They do look cute...","base","glance")
                        call her_main("(And they even match my hair!)","base","down")
                        call her_main("Let me put them on for you.","base","glance")
                else:
                    call her_main("Cat-ears...?","open","worried")
                    call her_main("Really, [genie_name]?!","open","base")
                    m "What's wrong? They're cute..."
                    call her_main("I'm not going to wear cat ears, [genie_name]!","annoyed","angryL")
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
                        call her_main("Elf-ears...?","soft","base")
                        call her_main("You wouldn't even be able to see them beneath all my hair...","open","closed")
                        m "You are right..."
                        m "Could you change your hair too then? Show off your cute little ears?"

                    if whoring < 17:
                        call her_main("...","annoyed","suspicious")
                        call her_main("I suppose they're not too noticeable...","base","glance")
                        call her_main("Alright. I will wear them.","soft","base")
                        call her_main("Let me put them on real quick.","soft","baseL")
                    else:
                        call her_main("...","annoyed","down")
                        call her_main("They do look cute...","base","down")
                        call her_main("Alright, [genie_name]. I will wear them for you.","base","glance")
                else:
                    call her_main("elf-ears...?","open","worried")
                    call her_main("I refuse, [genie_name]!","open","base")
                    m "Why not? Don't you support the house elves or something..."
                    call her_main("It's not about...","annoyed","angryL")
                    call her_main("I'm not going to wear these ridiculous ears for you, [genie_name]!","annoyed","angryL")
                    call her_main("...","annoyed","baseL")

                    ">She won't wear cat-ears just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            #Tiara
            if head_accessory_choice == "tiara":

                call her_main("A tiara...?","open","worried")
                call her_main("I suppose I can wear it...","annoyed","frown")
                call her_main("let me just go put it on.","base","glance")

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice)
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice)
            if head_accessory_choice in ["maid_hat","witch_hat","tiara"]:
                call set_h_hat(head_accessory_choice)

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice)
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                if whoring >= 11:
                    call set_h_ears(head_accessory_choice)
                else:
                    ">She won't wear those ears just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            if head_accessory_choice in ["maid_hat","witch_hat","tiara"]:
                call set_h_hat(head_accessory_choice)

            call her_main("","","",xpos="wardrobe")
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
                call her_main("Sure. Let me take them off.","base","base")

            #Vintage Glasses
            if head_accessory_choice == "vintage_glasses":
                m "Could you take off those glasses again?"
                call her_main("Alright. I will take them off.","base","base")

            #Cat Ears
            if head_accessory_choice == "cat_ears":
                m "Could you take off those cat-ears again?"
                call her_main("Sure. Let me take them off.","base","base")

            #Elf Ears
            if head_accessory_choice == "elf_ears":
                m "Could you take those ears off again?"
                call her_main("Alright. Let take them off.","base","base")

            #Tiara
            if head_accessory_choice == "tiara":
                m "Could you take off that tiara?"
                call her_main("Sure. I will take it off.","base","base")

            hide screen hermione_main
            with d3

            pause.5

            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice)
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice)
            if head_accessory_choice in ["maid_hat","witch_hat","tiara"]:
                call set_h_hat(head_accessory_choice)

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            if head_accessory_choice == "reading_glasses" or head_accessory_choice == "vintage_glasses":
                call set_h_glasses(head_accessory_choice, glasses_color_choice)
            if head_accessory_choice == "cat_ears" or head_accessory_choice == "elf_ears":
                call set_h_ears(head_accessory_choice)
            if head_accessory_choice in ["maid_hat","witch_hat","tiara"]:
                call set_h_hat(head_accessory_choice)

            call her_main("","","",xpos="wardrobe")
            call screen wardrobe

#

### Equip Astoria's Hat ###
label equip_ast_hat:
    call set_ast_hat(head_accessory_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Hat ###
label equip_sus_hat:
    call set_sus_hat(head_accessory_choice)

    hide screen wardrobe
    call screen wardrobe
