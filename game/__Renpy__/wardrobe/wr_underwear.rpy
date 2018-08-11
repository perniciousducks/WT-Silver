#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

### Equip Bra ###
label equip_bra:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_bra
    #Luna
    if active_girl == "luna":
        jump equip_lun_bra
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_bra
    #Susan
    if active_girl == "susan":
        jump equip_sus_bra


### Equip Hermione's Bra ###
label equip_her_bra:
    if underwear_choice == h_bra and underwear_color_choice == h_bra_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ wardrobe_active = 0 #activates dissolve in her_main
            $ hermione_xpos = 665

            m "[hermione_name]..."

            #Bras
            if underwear_choice in ["bra_base"]:
                m "Would you wear this bra for me?"
                if whoring >= 11: #Success
                    if whoring < 17:
                        call her_main("That old thing?","disgust","down")
                        call her_main("It looks so boring...","annoyed","down")
                        call her_main("Do I really have to wear this?","soft","base")
                        m "Yep..."
                        call her_main("Fine... Let me put it on real quick.","base","baseL")
                    else:
                        call her_main("Of course, [genie_name].","base","glance")
                else: #Fail
                    call her_main("No, [genie_name]!","open","closed")
                    m "Why not?"
                    call her_main("Why not?!","shocked","wide")
                    call her_main("Why would you even requests something like that from one of your students?","angry","angry")
                    call her_main("I see no reason why I should ever change my bra for you...","open","closed_raised")
                    call her_main("(Disgusting...)","annoyed","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_lace"]:
                g9 "Do you like this bra I bought you?"
                if whoring >= 11: #Success
                    if whoring < 17:
                        call her_main("Hmm...","annoyed","down")
                        call her_main("It looks decent enough...","annoyed","down_raised")
                        call her_main("Alright, I'll wear it.","open","baseL")
                        call her_main("Give me a second to put it on.","base","base")
                    else:
                        call her_main("Of course, [genie_name]! I love that one!","grin","closed")
                        call her_main("It's so soft and comfy!","grin","base")
                        call her_main("Let me put it on for you.","base","glance")
                else: #Fail
                    if whoring < 5:
                        call her_main("A bra?","shocked","shocked")
                        call her_main("Why in the world would you buy me a bra, [genie_name]?","disgust","down")
                        m "So you can... uhm... wear it?"
                        call her_main("Wear it? Are you out of your mind?","angry","angry")
                        call her_main("I'm your student! Don't even request something like that again!","angry","angry")
                        m "Fine. Forget about it..."
                        call her_main("(Damn perv...)","annoyed","angry")
                    else:
                        call her_main("No, [genie_name]!","annoyed","closed")
                        m "Why not? It's a really nice one!"
                        m "And it's so soft..."
                        m "I'd wear it myself but I lack the tits..."
                        call her_main("","annoyed","closed")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_silk"]:
                g9 "I have bought you a new bra!"
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        call her_main("A... WHAT?","shocked","shocked")
                        call her_main("[genie_name], why would you buy me a bra?","disgust","down")
                        m "As a gift? Don't you like gifts?"
                        call her_main("It's a bra! You can't gift bras to your students, [genie_name]!","angry","angry")
                        m "Why not? This one is really sexy!"
                        call her_main("(Oh my bloody god! What the hell is wrong with him?!)","angry","angryCl")
                        call her_main("Keep it for yourself, [genie_name]! I don't want gifts like that.","annoyed","angryL")
                        m "Fine..."
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_bikini","bra_bikini_string"]:
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        pass
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_latex"]:
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        pass
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_french_maid"]:
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        pass
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_tape"]:
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        pass
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["top_fishnets"]:
                if whoring >= 11: #Success
                    if whoring < 17:
                        pass
                    else:
                        pass
                else: #Fail
                    if whoring < 5:
                        pass
                    #    m "[hermione_name], "
                    #    call her_main("What? What's this? ?","soft","base")
                    #    m "It's a fishnet t--"
                    #    call her_main("Oh, I get it!","grin","down")
                    #    call her_main("This isn't really a hobby I considered pursuing, [genie_name]...","open","baseL")
                    #    call her_main("But if you say it will help me with my grades then I'll try my best.","soft","down")
                    #    m "Wait what?"
                    #    call her_main("I will try it out later if that's alright with you.","base","glance")
                    #    m "(...)"
                    #    m "(Does she want to wear the top now or did she decide to go fishing with it...?)"
                    else:
                        pass
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe









            call set_h_bra(underwear_choice, underwear_color_choice)

            call her_main(xpos="wardrobe")
            hide screen wardrobe
            call screen wardrobe

        else:
            $ wardrobe_active = 1
            call set_h_bra(underwear_choice, underwear_color_choice)

            call her_main(xpos="wardrobe")
            hide screen wardrobe
            call screen wardrobe




### Equip Astoria's Bra ###
label equip_ast_bra:
    call set_ast_bra(underwear_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Bra ###
label equip_sus_bra:
    call set_sus_bra(underwear_choice)

    hide screen wardrobe
    call screen wardrobe



### Equip Onepiece ###
label equip_onepiece:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_onepiece
    #Luna
    if active_girl == "luna":
        jump equip_lun_onepiece
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_onepiece
    #Susan
    if active_girl == "susan":
        jump equip_sus_onepiece

### Equip Hermione's OnePiece/Nighty ###
label equip_her_onepiece:
    call set_h_onepiece(underwear_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's OnePiece/Nighty ###
label equip_ast_onepiece:
    call set_ast_onepiece(underwear_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's OnePiece/Nighty ###
label equip_sus_onepiece:
    call set_sus_onepiece(underwear_choice)

    hide screen wardrobe
    call screen wardrobe



### Equip Panties ###
label equip_panties:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_panties
    #Luna
    if active_girl == "luna":
        jump equip_lun_panties
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_panties
    #Susan
    if active_girl == "susan":
        jump equip_sus_panties

### Equip Hermione's Panties ###
label equip_her_panties:
    call set_h_panties(underwear_choice, underwear_color_choice)

    hide screen wardrobe
    call screen wardrobe


### Equip Astoria's Panties ###
label equip_ast_panties:
    call set_ast_panties(underwear_choice)

    hide screen wardrobe
    call screen wardrobe


### Equip Susan's Panties ###
label equip_sus_panties:
    call set_sus_panties(underwear_choice)

    hide screen wardrobe
    call screen wardrobe



### Equip Garterbelt ###
label equip_garterbelt:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_garterbelt
    #Luna
    if active_girl == "luna":
        jump equip_lun_garterbelt
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_garterbelt
    #Susan
    if active_girl == "susan":
        jump equip_sus_garterbelt

### Equip Hermione's Garterbelt ###
label equip_her_garterbelt:
    call set_h_garterbelt(underwear_choice, underwear_color_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Astoria's Garterbelt ###
label equip_ast_garterbelt:
    call set_ast_garterbelt(underwear_choice, underwear_color_choice)

    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Garterbelt ###
label equip_sus_garterbelt:
    call set_sus_garterbelt(underwear_choice, underwear_color_choice)

    hide screen wardrobe
    call screen wardrobe
