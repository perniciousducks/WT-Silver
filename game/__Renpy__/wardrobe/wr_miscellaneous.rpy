

#Needs to be updated

label equip_misc_item:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_misc_item
    #Luna
    if active_girl == "luna":
        jump equip_lun_misc_item
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_misc_item

label equip_her_misc_item:

    if mad >= 1:
        jump equipping_failed

    else:
        if misc_item_choice == "transparency":
            if whoring <= 11:
                jump too_much

            $ wardrobe_active = 0 #activates dissolve in her_main

            if transparency == 1:
                call her_main("You want me to make my clothes see through?","normal","worriedCl")
                call her_main("Really, [genie_name]!","scream","angryCl")
                m "Just a little bit."
                call her_main("Fine...","open","suspicious")
                call her_main("How much should I drink...","annoyed","worriedL")

                menu:
                    "-A little bit-":
                        $ transparency_amount = 0.8
                        call her_main("(at least This shouldn't be too noticable.","normal","worriedCl")
                    "-A fair bit-" if whoring >= 20:
                        $ transparency_amount = 0.5
                        call her_main("(Hopefully it's not too bad","annoyed","worriedL")
                    "-A lot-" if whoring >= 23:
                        $ transparency_amount = 0.3
                        call her_main("(...)","base","down")
                    "-All of it-" if whoring == 24:
                        $ transparency_amount = 0.1
                        call her_main("...","grin","baseL")

                call her_main("Alright then...","annoyed","down")
                hide screen hermione_main
                with d5
                $ transparency = transparency_amount

                call update_her_uniform #Updates clothing and body.

            else:
                call her_main("You want me to wear new clothes?","annoyed","ahegao")
                call her_main("Oh... alright then, [genie_name].","annoyed","down")
                hide screen hermione_main
                with d5
                $ transparency = 1

                call update_her_uniform #Updates clothing and body.

            jump return_to_wardrobe

        #Buttplugs
        if misc_item_choice in ["buttplug_small","buttplug_medium","buttplug_large"]:
            if misc_item_choice == "buttplug_small" and not h_request_wear_buttplug:

                $ wardrobe_active = 0 #activates dissolve in her_main

                call her_main("You want me to use a buttplug? Again?","angry","wink")
                call her_main("(...)","annoyed","ahegao")
                call her_main("(It's small enough. Shouldn't be too bad...)","disgust","down_raised")
                call her_main("Alright,... Let me put it in real quick...","base","base")
                hide screen hermione_main
                with d5
                pause.2

                call set_h_buttplug("plug_a_on") #Updates clothing and body.

                jump return_to_wardrobe

            elif misc_item_choice == "buttplug_medium" and not h_request_wear_buttplug:

                $ wardrobe_active = 0 #activates dissolve in her_main

                call her_main("Are you sure this is the medium size one?","soft","wink")
                call her_main("(It still looks so big.)","angry","worriedCl")
                call her_main("Fine, I'll wear it... Just give me a second...","disgust","down")
                hide screen hermione_main
                with d5
                pause.2

                call set_h_buttplug("plug_b_on") #Updates clothing and body.

                jump return_to_wardrobe

            elif misc_item_choice == "buttplug_large" and not h_request_wear_buttplug:

                $ wardrobe_active = 0 #activates dissolve in her_main

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

                call set_h_buttplug("plug_c_on") #Updates clothing and body.

                jump return_to_wardrobe

            else: #Remove

                $ wardrobe_active = 0 #activates dissolve in her_main

                call her_main("You want me to take the buttplug out?","angry","wink")
                call her_main("(I was just getting used to it...)","annoyed","ahegao")
                call her_main("Well alright then...","base","base")
                hide screen hermione_main
                with d5
                call play_sound("pop")
                pause.2

                call set_h_buttplug("remove") #Updates clothing and body.

                jump return_to_wardrobe
