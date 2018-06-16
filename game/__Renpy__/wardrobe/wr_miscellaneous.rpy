

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
                call her_main("You want me to make my clothes see through?","normal","worriedCl") from _call_her_main_4510
                call her_main("Really, [genie_name]!","scream","angryCl") from _call_her_main_4511
                m "Just a little bit."
                call her_main("Fine...","open","suspicious") from _call_her_main_4512
                call her_main("How much should I drink...","annoyed","worriedL") from _call_her_main_4513
            
                menu: 
                    "-A little bit-":
                        $ transparency_amount = 0.8
                        call her_main("(at least This shouldn't be too noticable.","normal","worriedCl") from _call_her_main_4514
                    "-A fair bit-" if whoring >= 20:
                        $ transparency_amount = 0.5
                        call her_main("(Hopefully it's not too bad","annoyed","worriedL") from _call_her_main_4515
                    "-A lot-" if whoring >= 23:
                        $ transparency_amount = 0.3
                        call her_main("(...)","base","down") from _call_her_main_4516
                    "-All of it-" if whoring == 24:
                        $ transparency_amount = 0.1
                        call her_main("...","grin","baseL") from _call_her_main_4517

                call her_main("Alright then...","annoyed","down") from _call_her_main_4518
                hide screen hermione_main
                with d5
                $ transparency = transparency_amount
            
                call update_her_uniform from _call_update_her_uniform_90 #Updates clothing and body.
            
            else:
                call her_main("You want me to wear new clothes?","annoyed","ahegao") from _call_her_main_4519
                call her_main("Oh... alright then, [genie_name].","annoyed","down") from _call_her_main_4520
                hide screen hermione_main
                with d5
                $ transparency = 1
            
                call update_her_uniform from _call_update_her_uniform_91 #Updates clothing and body.
                
            jump return_to_wardrobe
            
        if misc_item_choice == "small_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("You want me to use a buttplug? Again?","angry","wink") from _call_her_main_4521
            call her_main("(...)","annoyed","ahegao") from _call_her_main_4522
            call her_main("(It's small enough. Shouldn't be too bad...)","disgust","down_raised") from _call_her_main_4523
            call her_main("Alright,... Let me put it in real quick...","base","base") from _call_her_main_4524
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_a_on") from _call_set_h_buttplug #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "medium_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("Are you sure this is the medium size one?","soft","wink") from _call_her_main_4525
            call her_main("(It still looks so big.)","angry","worriedCl") from _call_her_main_4526
            call her_main("Fine, I'll wear it... Just give me a second...","disgust","down") from _call_her_main_4527
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_1 #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "large_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("The big one?","soft","base") from _call_her_main_4528
            g9 "The giant one!"
            call her_main("...","annoyed","angry") from _call_her_main_4529
            call her_main("(Why am I not surprised...)","annoyed","angryL") from _call_her_main_4530
            call her_main("(This is going to hurt...)","angry","worriedCl",cheeks="blush") from _call_her_main_4531
            call her_main("Fine... Let me put it on.","base","baseL") from _call_her_main_4532
            g9 "Don't you mean... \"in\"?"
            call her_main("...","annoyed","frown") from _call_her_main_4533
            hide screen hermione_main
            with d5
            pause.2

            call set_h_buttplug("plug_c_on") from _call_set_h_buttplug_2 #Updates clothing and body.

            jump return_to_wardrobe
            
        if misc_item_choice == "remove_buttplug":
    
            $ wardrobe_active = 0 #activates dissolve in her_main 
        
            call her_main("You want me to take the buttplug out?","angry","wink") from _call_her_main_4534
            call her_main("(I was just getting used to it...)","annoyed","ahegao") from _call_her_main_4535
            call her_main("Well alright then...","base","base") from _call_her_main_4536
            hide screen hermione_main
            with d5
            call play_sound("pop") from _call_play_sound_175
            pause.2
                
            call set_h_buttplug("remove") from _call_set_h_buttplug_3 #Updates clothing and body.
            
            jump return_to_wardrobe
            
            
            
            
            
            