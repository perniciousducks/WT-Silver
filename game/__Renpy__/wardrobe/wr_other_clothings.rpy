#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\"

### Equip Neckwear ### MISSING TEXTS
### Equip Body Accessories ###
### Equip Gloves ### MISSING TEXTS
### Equip Stockings ### MISSING TEXTS
### Equip Robe ### MISSING TEXTS



### Neckwear Equip ###
label equip_neckwear:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_neckwear
    #Luna
    if active_girl == "luna":
        jump equip_lun_neckwear
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_neckwear
    #Susan
    if active_girl == "susan":
        jump equip_sus_neckwear

### Equip Hermione's Neckwear ###
label equip_her_neckwear:
    call set_h_neckwear(neckwear_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Neckwear ###
label equip_ast_neckwear:
    call set_ast_neckwear(neckwear_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Neckwear ###
label equip_sus_neckwear:
    call set_sus_neckwear(neckwear_choice)

    hide screen wardrobe
    call screen wardrobe



### Gloves Equip ###
label equip_gloves:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_gloves
    #Luna
    if active_girl == "luna":
        jump equip_lun_gloves
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_gloves
    #Susan
    if active_girl == "susan":
        jump equip_ast_gloves

### Equip Hermione's Gloves ###
label equip_her_gloves:
    call set_h_gloves(gloves_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Gloves ###
label equip_ast_gloves:
    call set_ast_gloves(gloves_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Gloves ###
label equip_sus_gloves:
    call set_sus_gloves(gloves_choice)

    hide screen wardrobe
    call screen wardrobe



### Body Accs Equip ###
label equip_body_accessory:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_body_accessory
    #Luna
    if active_girl == "luna":
        jump equip_lun_body_accessory
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_body_accessory
    #Susan
    if active_girl == "susan":
        jump equip_sus_body_accessory

### Equip Hermione's Body Accessory ###
label equip_her_body_accessory:

    if mad >= 1:
        jump equipping_failed

    if body_accessory_choice not in hermione_body_accs_list:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main

            m "[hermione_name]..."

            #S.P.E.W Badge
            if body_accessory_choice == "badge_SPEW":
                m "Would you wear this badge for me?"
                if whoring >= 0:
                    call her_main("A S.P.E.W. badge?","base","base")
                    call her_main("I'll wear this with pride [genie_name].","open","closed")

            #I <3 Cum Badge
            if body_accessory_choice == "badge_I_love_cum":
                m "Would you wear this badge for me?"

                if whoring >= 20:
                    if whoring < 24:
                        call her_main("Hm...?","soft","base")
                        call her_main("An \"I love cum\" badge?","annoyed","suspicious")
                        call her_main("{size=-5}(I suppose that it's not a complete lie...){/size}","base","down")
                        call her_main("Alright, I'll wear it.","base","glance")
                    else: #24
                        call her_main("An \"I love cum\" badge?","annoyed","suspicious")
                        call her_main("Sure, [genie_name]!","soft","base")
                        call her_main("Let me put it on for you.","base","glance")
                else:
                    if whoring < 8:
                        jump too_much
                    else: #8-19
                        call her_main("An I love cum badge...?","open","worried")
                        call her_main("You cannot be serious, [genie_name]!","open","base")
                        m "What's wrong?"
                        call her_main("I am not going to wear a badge that says that{w=0.5} {b}I{/b}{w=0.5} {b}love{/b}{w=0.5} {b}cum!{/b}","normal","frown")
                        call her_main("I absolutely refuse!","annoyed","frown")
                    ">She won't cover herself in cum just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_body_accessory(body_accessory_choice)

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_body_accessory(body_accessory_choice)
            call her_main("","","",xpos="wardrobe")
            call screen wardrobe


    else: #Remove makeup

        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ wardrobe_active = 0 #activates dissolve in her_main
            $ hermione_xpos = 665

            m "[hermione_name]..."

            #S.P.E.W Basge
            if body_accessory_choice == "badge_SPEW":
                m "Could you remove that Spew badge again?"
                call her_main("Alright. Let me take it off.","annoyed","down")

            #I <3 Cum Badge
            if body_accessory_choice == "badge_I_love_cum":
                m "Could you remove that Cum badge again?"
                call her_main("Alright. Let me take it off.","annoyed","down")

            hide screen hermione_main
            with d3

            pause.5

            call set_h_body_accessory(body_accessory_choice) #Removes Item

            call her_main("","","",xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:

            $ wardrobe_active = 1
            call set_h_body_accessory(body_accessory_choice) #Removes Item
            call her_main("",xpos="wardrobe")
            call screen wardrobe
#

#Add Luna Body Accessory Texts
#Add Astoria Body Accessory Texts

### Stockings Equip ###
label equip_stockings:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_stockings
    #Luna
    if active_girl == "luna":
        jump equip_lun_stockings
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_stockings
    #Susan
    if active_girl == "susan":
        jump equip_sus_stockings

### Equip Hermione's Stockings ###
label equip_her_stockings:
    if whoring < 11 and h_skirt in ["skirt_belted_mini","skirt_belted_micro"]:
        call nar(">You can't remove her pantyhose while wearing that skirt!")
    else:
        call set_h_stockings(stockings_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Stockings ###
label equip_ast_stockings:
    call set_ast_stockings(stockings_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Stockings ###
label equip_sus_stockings:
    call set_sus_stockings(stockings_choice)

    hide screen wardrobe
    call screen wardrobe



### Robe Equip ###
label equip_robe:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_robe
    #Luna
    if active_girl == "luna":
        jump equip_lun_robe
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_robe
    #Susan
    if active_girl == "susan":
        jump equip_sus_robe


### Equip Hermione's Robe ###
label equip_her_robe:
    call set_h_robe(robe_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Robe ###
label equip_ast_robe:
    call set_ast_robe(robe_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Robe ###
label equip_sus_robe:
    call set_sus_robe(robe_choice)

    hide screen wardrobe
    call screen wardrobe
