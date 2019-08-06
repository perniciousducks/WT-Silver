

#Needs to be updated

label equip_misc_item:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_misc_item
    #Luna
    if active_girl == "luna":
        jump equip_lun_misc_item
    #Susan
    #if active_girl == "susan":
        #jump equip_sus_misc_item



### Hermione ###

label equip_her_misc_item:

    if her_mood >= 1:
        jump equipping_failed

    else:
        if misc_item_choice == "transparency":
            if her_whoring <= 11:
                jump too_much

            $ hide_transitions = False #activates dissolve in her_main

            call her_main("You want me to make my clothes see through?","normal","worriedCl")
            m "Just a little bit."
            call her_main("Fine...","open","suspicious")
            call her_main("How much should I drink?","annoyed","worriedL")

            label make_item_transparent:

            menu:
                "-Just a sip-":
                    $ transparency = 0.9
                    if wardrobe_chitchat_active:
                        call her_main("(at least This shouldn't be too noticable.)","normal","worriedCl")
                "-20 percent-" if her_whoring >= 15:
                    $ transparency = 0.8
                "-30 percent-" if her_whoring >= 15:
                    $ transparency = 0.7
                "-40 percent-" if her_whoring >= 15:
                    $ transparency = 0.6
                "-Half the bottle-" if her_whoring >= 18:
                    $ transparency = 0.5
                "-60 percent-" if her_whoring >= 21:
                    $ transparency = 0.4
                    if wardrobe_chitchat_active:
                        call her_main("(...)","base","down")
                "-70 percent-" if her_whoring >= 21:
                    $ transparency = 0.3
                    if wardrobe_chitchat_active:
                        call her_main("(...)","base","down")
                "-80 percent-" if her_whoring >= 21:
                    $ transparency = 0.2
                "-All of it-" if her_whoring >= 24:
                    $ transparency = 0.1
                    if wardrobe_chitchat_active:
                        call her_main("(...)","grin","baseL")
                "-remove it-":
                    $ transparency = 1
                "-That's enough-":
                    jump return_to_wardrobe

            if wardrobe_chitchat_active:
                if her_whoring < 18:
                    call her_main("What do you want to change?","disgust","down_raised")
                else:
                    call her_main("What would you like to change?","base","down")

            menu:
                ">Which item would you like to make transparent?\n>Only items she's currently wearing are listed here."
                "-top-" if hermione_wear_top:
                    call set_her_transparency(top=transparency)
                "-bottom" if hermione_wear_bottom:
                    call set_her_transparency(bottom=transparency)
                "-bra-" if hermione_wear_bra:
                    call set_her_transparency(bra=transparency)
                "-onepiece-" if hermione_wear_onepiece:
                    call set_her_transparency(onepiece=transparency)
                "-panties-" if hermione_wear_panties:
                    call set_her_transparency(panties=transparency)
                "-garterbelt-" if hermione_wear_garterbelt:
                    call set_her_transparency(garterbelt=transparency)
                "-gloves-" if hermione_wear_gloves:
                    call set_her_transparency(gloves=transparency)
                "-stockings-" if hermione_wear_stockings:
                    call set_her_transparency(stockings=transparency)
                "-robe-" if hermione_wear_robe:
                    call set_her_transparency(robe=transparency)
                "-outfit-" if hermione_wear_outfit:
                    call set_her_transparency(outfit=transparency)
                "-Never mind-":
                    jump return_to_wardrobe

            if wardrobe_chitchat_active:
                call her_main()
                pause.8
                call her_main("All done!",face="happy")
                call her_main("Would you like me to drink a bit more?","base","glance")
            else:
                call her_main(face="happy")

            jump make_item_transparent



        #Buttplugs
        if misc_item_choice in ["buttplug_small","buttplug_medium","buttplug_large"]:
            if misc_item_choice == "buttplug_small" and not h_request_wear_buttplug:

                $ hide_transitions = False #activates dissolve in her_main

                call her_main("You want me to use a buttplug? Again?","angry","wink")
                call her_main("(...)","annoyed","ahegao")
                call her_main("(It's small enough. Shouldn't be too bad...)","disgust","down_raised")
                call her_main("Alright,... Let me put it in real quick...","base","base")
                hide screen hermione_main
                with d5
                pause.2

                call set_her_buttplug("plug_a_on") #Updates clothing and body.

                jump return_to_wardrobe

            elif misc_item_choice == "buttplug_medium" and not h_request_wear_buttplug:

                $ hide_transitions = False #activates dissolve in her_main

                call her_main("Are you sure this is the medium size one?","soft","wink")
                call her_main("(It still looks so big.)","angry","worriedCl")
                call her_main("Fine, I'll wear it... Just give me a second...","disgust","down")
                hide screen hermione_main
                with d5
                pause.2

                call set_her_buttplug("plug_b_on") #Updates clothing and body.

                jump return_to_wardrobe

            elif misc_item_choice == "buttplug_large" and not h_request_wear_buttplug:

                $ hide_transitions = False #activates dissolve in her_main

                call her_main("The big one?","soft","base")
                g9 "The giant one!"
                call her_main("...","annoyed","angry")
                call her_main("(Why am I not surprised...)","annoyed","angryL")
                call her_main("(This is going to hurt...)","angry","worriedCl",cheeks="blush")
                call her_main("Fine... Let me put it on.","base","baseL")
                g9 "Don't you mean... \"in\"?"
                call her_main("...","annoyed","frown")
                hide screen hermione_main
                with d5
                pause.2

                call set_her_buttplug("plug_c_on") #Updates clothing and body.

                jump return_to_wardrobe

            else: #Remove

                $ hide_transitions = False #activates dissolve in her_main

                call her_main("You want me to take the buttplug out?","angry","wink")
                call her_main("(I was just getting used to it...)","annoyed","ahegao")
                call her_main("Well alright then...","base","base")
                hide screen hermione_main
                with d5
                call play_sound("pop")
                pause.2

                call set_her_buttplug("remove") #Updates clothing and body.

                jump return_to_wardrobe

        #Gags
        if misc_item_choice in ["item_ballgag_and_cuffs"]:
            menu:
                "Hardcore mode only" ">You can gag Hermione, but it won't prevent her from talking. There is no way around it."
                "-Use Ball Gag-":
                    $ item_choice = "gag"
                "-Mouthpiece-":
                    $ item_choice = "mouthpiece"
                "-Mouthpiece Drooling-":
                    $ item_choice = "mouthpiece_drool"
                "-Remove Gag-":
                    $ item_choice = "remove"

            call set_her_gag(item_choice)

            jump return_to_wardrobe



### Luna ###

label equip_lun_misc_item:

    if misc_item_choice == "transparency":

        $ hide_transitions = False #activates dissolve in her_main

        call lun_main("You want to make my clothes see through?",mouth="open",face="happy")
        m "Yes. Just drink this potion."
        call lun_main("Okay, [lun_genie_name].",face="happy")
        call lun_main("How much should I drink?",mouth="soft",face="neutral")

        label make_lunas_item_transparent:

        menu:
            "-Just a sip-":
                $ transparency = 0.9
                if wardrobe_chitchat_active:
                    call lun_main("Only so little?",mouth="upset",pupils="down",face="neutral")
            "-20 percent-":
                $ transparency = 0.8
            "-30 percent-":
                $ transparency = 0.7
            "-40 percent-":
                $ transparency = 0.6
            "-Half the bottle-":
                $ transparency = 0.5
            "-60 percent-":
                $ transparency = 0.4
            "-70 percent-":
                $ transparency = 0.3
            "-80 percent-":
                $ transparency = 0.2
            "-All of it-":
                $ transparency = 0.1
                if wardrobe_chitchat_active:
                    call lun_main("Sure, why not. This is fun!",mouth="grin",eye="closed",face="happy")
            "-remove it-":
                $ transparency = 1
            "-That's enough-":
                jump return_to_wardrobe

        if wardrobe_chitchat_active:
            call lun_main("What would you like to change?",face="happy")

        menu:
            ">Which item would you like to make transparent?\n>Only items she's currently wearing are listed here."
            "-top-" if luna_wear_top:
                call set_lun_transparency(top=transparency)
            "-bottom" if luna_wear_bottom:
                call set_lun_transparency(bottom=transparency)
            "-bra-" if luna_wear_bra:
                call set_lun_transparency(bra=transparency)
            "-onepiece-" if luna_wear_onepiece:
                call set_lun_transparency(onepiece=transparency)
            "-panties-" if luna_wear_panties:
                call set_lun_transparency(panties=transparency)
            "-garterbelt-" if luna_wear_garterbelt:
                call set_lun_transparency(garterbelt=transparency)
            "-gloves-" if luna_wear_gloves:
                call set_lun_transparency(gloves=transparency)
            "-stockings-" if luna_wear_stockings:
                call set_lun_transparency(stockings=transparency)
            "-robe-" if luna_wear_robe:
                call set_lun_transparency(robe=transparency)
            "-outfit-" if luna_wear_outfit:
                call set_lun_transparency(outfit=transparency)
            "-Never mind-":
                jump return_to_wardrobe

        if wardrobe_chitchat_active:
            call lun_main()
            pause.8
            call lun_main("All done!",mouth="grin",face="happy")
            call lun_main("Would you like me to a bit drink more?",mouth="soft",face="neutral")
        else:
            call lun_main(face="neutral")

        jump make_lunas_item_transparent