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
            if underwear_choice == "bra_1":
                pass
            call set_h_bra(underwear_choice, underwear_color_choice)

            hide screen wardrobe
            call screen wardrobe

        else:
            $ wardrobe_active = 1
            call set_h_bra(underwear_choice, underwear_color_choice)

            hide screen wardrobe
            call screen wardrobe


### Equip Astoria's Bra ###
label equip_ast_bra:

    if underwear_choice == ast_bra and underwear_color_choice == ast_bra_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    #elif mad >= 1:
    #    jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            pass
            #hide screen astoria_main
            #with d3

            #$ wardrobe_active = 0 #activates dissolve in her_main
            #$ astoria_xpos = 665

            #m "[astoria_name]..."

            #Panties
            if underwear_choice == "bra_1":
                m "Would you wear your school panties for me? The very long one."
        else:
            pass

        $ wardrobe_active = 1

        call set_ast_bra(underwear_choice)

        call ast_main(xpos="wardrobe")
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

    if underwear_choice == ast_panties and underwear_color_choice == ast_panties_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    #elif mad >= 1:
    #    jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            pass
            #hide screen astoria_main
            #with d3

            #$ wardrobe_active = 0 #activates dissolve in her_main
            #$ astoria_xpos = 665

            #m "[astoria_name]..."

            #Panties
            if underwear_choice == "panties_1":
                m "Would you wear your school panties for me? The very long one."
        else:
            pass

        $ wardrobe_active = 1

        call set_ast_panties(underwear_choice)

        call ast_main(xpos="wardrobe")
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
