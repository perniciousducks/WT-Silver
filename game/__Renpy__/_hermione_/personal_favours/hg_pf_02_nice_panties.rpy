

### HERMIONE PERSONAL FAVOUR 2 ###

### NICE PANTIES ###

label hg_pf_NicePanties:
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"
    if hg_pf_NicePanties_OBJ.points < 1:

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    $ menu_x = 0.2 #Menu is moved to the left side.

    call her_main("So, what will it be, [genie_name]?") from _call_her_main_5045
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."  

    #First Time Event.
    if hg_pf_NicePanties_OBJ.points == 0 and whoring <= 5:
        call her_main("My... panties...?","open","base") from _call_her_main_5046
        call her_main("[genie_name]!","angry","angry") from _call_her_main_5047
        m "I know, I know, this a little weird..."
        call her_main(" {size=+7}A little !?{/size}","shock","wide") from _call_her_main_5048
        her "This is completely inappropriate!"
        m "Listen, we need to go through this phase before we get to the good stuff, alright?"
        call her_main("The \"good stuff\"? [genie_name], I don't understand...","open","base") from _call_her_main_5049
        m "What don't you understand, [hermione_name]?"
        m "Do you need these points or not?"
        call her_main("I do...","open","base") from _call_her_main_5050
        m "Lift up your skirt then..."
        call her_main(".............","angry","angry") from _call_her_main_5051
    else:
        if hg_pf_NicePanties_OBJ.points >= 1: #Not the first time
            call her_main("Oh... again?","annoyed","worriedL") from _call_her_main_5052
            m "Just do it..."
        call her_main("..................","annoyed","worriedL") from _call_her_main_5053
    

    ### Setup ###

    hide screen bld1
    hide screen hermione_main
    with d3

    #First and Second Event
    if whoring < 9:
        $ hermione_wear_panties = True
        call h_action("lift_skirt") from _call_h_action_76

    #Third Event
    else:
        if hg_pf_NicePanties_OBJ.hearts_level == 2: #Before third event happens.
            $ h_request_wear_panties = False
            $ hermione_wear_panties = False

        elif hg_pf_NicePanties_OBJ.hearts_level == 3: #Third event.
            if h_request_wear_panties:
                $ hermione_wear_panties = True
            else:
                $ hermione_wear_panties = False
    
    call her_chibi("lift_skirt","mid","base") from _call_her_chibi_162
    with d3
    call play_music("playful_tension") from _call_play_music_190
     
    

    #Fist event.
    if whoring >= 0 and whoring <= 2:

        $ new_request_02_heart = 1 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 1 #Event hearts level (0-3)
        
        pause.8
        
        show screen blktone
        call her_main(".....................","angry","angry",trans="fade",xpos="mid",ypos="base") from _call_her_main_5054
        call ctc from _call_ctc_289
        
        menu:
            "-Stare at her face-":
                ">You study Hermione's face..."
                call ctc from _call_ctc_290
                ">You wonder what's going through her mind right now."
                call her_main(".......................","angry","annoyed",emote="01") from _call_her_main_5055
                call ctc from _call_ctc_291
            "-Stare at her panties-":
                ">That's a plain girlish underwear..."
                call her_main(".......................","angry","annoyed",emote="01") from _call_her_main_5056
                call ctc from _call_ctc_292
    
    #Second Event.
    elif whoring >= 3 and whoring < 9:

        $ new_request_02_heart = 2 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 2 #Event hearts level (0-3)
        
        pause.8
        
        show screen blktone
        call her_main("Here, [genie_name]...","base","base",trans="fade",xpos="mid",ypos="base") from _call_her_main_5057
        call ctc from _call_ctc_293

        menu:
            "\"You don't look too embarrassed...\"":
                call her_main("That's not true...","base","squint") from _call_her_main_5058
                call her_main("But this is a small price to pay if the \"Gryffindors\" keep the cup this year.","base","baseL") from _call_her_main_5059
                her "I know everyone will be so happy..."
                call ctc from _call_ctc_294
            "\"I like your panties...\"":
                call her_main("Thank you, [genie_name]...","base","squint") from _call_her_main_5060
                call ctc from _call_ctc_295
            "-Keep looking into her eyes-":
                call her_main("..............................","soft","base") from _call_her_main_5061
                her "...........................?"
                call her_main("................................","grin","baseL") from _call_her_main_5062
                call her_main("[genie_name], please... You are embarrassing me.","grin","worriedCl",emote="05") from _call_her_main_5063
                call ctc from _call_ctc_296
    
    #Third Event.
    elif whoring >= 9:

        $ new_request_02_heart = 3 #Event hearts level (0-3)
        $ hg_pf_NicePanties_OBJ.hearts_level = 3 #Event hearts level (0-3)
        
        call ctc from _call_ctc_297

        call her_head("..........................","base","baseL",cheeks="blush",xpos="base",ypos="base") from _call_her_head_1035

        if not hermione_wear_panties:
            g4 "!!?"

        call h_action("lift_skirt") from _call_h_action_77
        
        show screen blktone
        call her_main("","base","glance",trans="fade",xpos="mid",ypos="base") from _call_her_main_5064
        call ctc from _call_ctc_298

        #Event A (no panties)
        if not hermione_wear_panties:
            g4 "Where are your panties, [hermione_name]?"
            call her_main("Oh, lately I just don't feel like wearing them...","base","down",cheeks="blush") from _call_her_main_5065

            menu:
                "\"You little slut!\"":
                    her "Hm..."
                    call her_main("I suppose I am...","base","glance") from _call_her_main_5066
                    her "Do I get extra points for that?"

                    menu:
                        "\"Absolutely!\"":
                            m "Absolutely!"
                            $ gryffindor +=10
                            m "Ten additional points to \"Gryffindor\"!" 
                            call her_main("Thank you, [genie_name]!","base","worriedCl") from _call_her_main_5067
                            call ctc from _call_ctc_299
                        "\"Absolutely not!\"":
                            $ mad +=5
                            call her_main("Why not!?","scream","angryCl") from _call_her_main_5068
                            m "Sluts aren't paid"
                            m "That's what makes them sluts"
                            call her_main("well are you even going to pay me 5 points?","annoyed","angry") from _call_her_main_5069   
                            m "Are you a slut or are you a prostitute?"
                            her "{size=-4}...a slut {/size}"
                            m "Good girl"
                            call ctc from _call_ctc_300

                "\"Good! Five points!\"":
                    pass

        else: #Event B
            call her_main("Do you like them, [genie_name]?","base","glance") from _call_her_main_5070
            m "Indeed I do, [hermione_name]..."
            m "They look lovely on you!"
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_5071
            call ctc from _call_ctc_301


        #Hermione asks to put them back on/take them off.
        if not hermione_wear_panties:
            call her_main("If you want, [genie_name], I could put my panties back on for you.","open","baseL") from _call_her_main_5072

            menu:
                "\"Yes, put them back on!\"":
                    call her_main("Alright, [genie_name].","base","glance") from _call_her_main_5073
                    hide screen hermione_main
                    with d3
                    ">Hermione puts on her panties."

                    $ h_request_wear_panties = True
                    $ hermione_wear_panties = True

                    call update_her_uniform from _call_update_her_uniform_92
                    call update_chibi_uniform from _call_update_chibi_uniform_3
                    call her_chibi("lift_skirt") from _call_her_chibi_163
                    call set_hermione_action("lift_skirt") from _call_set_hermione_action_138

                    call her_main("","base","glance") from _call_her_main_5074
                    call ctc from _call_ctc_302

                    call her_main("I hope you like them...","soft","baseL") from _call_her_main_5075

                "\"No, keep them off!\"":
                    call her_main("Of course, [genie_name].","soft","ahegao") from _call_her_main_5076
                    call ctc from _call_ctc_303

                    $ h_request_wear_panties = False

        else:
            call her_main("I could take them off, if you'd like that, [genie_name].","open","baseL") from _call_her_main_5077

            menu:
                "\"Yes, Take them off!\"":
                    call her_main("Alright, [genie_name].","soft","ahegao") from _call_her_main_5078
                    m "And keep them off from now on!"
                    call her_main("Whatever you want, [genie_name].","base","glance") from _call_her_main_5079
                    hide screen hermione_main
                    with d3
                    ">Hermione takes off her panties."

                    $ h_request_wear_panties = False
                    $ hermione_wear_panties = False

                    call update_her_uniform from _call_update_her_uniform_93
                    hide screen hermione_chibi_lift_skirt
                    call update_chibi_uniform from _call_update_chibi_uniform_4

                    call her_chibi("lift_skirt") from _call_her_chibi_164
                    call set_hermione_action("lift_skirt") from _call_set_hermione_action_139

                    call her_main("","base","glance") from _call_her_main_5080
                    call ctc from _call_ctc_304

                    call her_main("I hope you like it, [genie_name]...","angry","wink") from _call_her_main_5081

                "\"No, keep them on!\"":
                    call her_main("Sure, [genie_name].","base","glance") from _call_her_main_5082
                    call ctc from _call_ctc_305

                    $ h_request_wear_panties = True


    stop music fadeout 4.0

    if whoring <= 8:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\", [hermione_name]. Well done." 

    call reset_hermione_main from _call_reset_hermione_main_6

    call her_chibi("stand","mid","base") from _call_her_chibi_165
    
    hide screen blktone
    call her_main("Will this be all then?","open","base",trans="fade",xpos="base",ypos="base") from _call_her_main_5083

    if whoring >= 13:
        menu:
            "-Let her go-":
                m "Yes, you can go now."

                if hg_pf_NicePanties_OBJ.points == 0: #First time.
                    call her_main("Another 5 points...","soft","baseL") from _call_her_main_5084
                    her "Can't wait to tell the guys!"
                    call her_main("Only that I can't actually tell them about any of this...","annoyed","angryL") from _call_her_main_5085
        
                if daytime:
                    her "Well, my classes are about to start..."
                else:
                    her "It's getting pretty late, [genie_name]... I should go..."
        
                if whoring <= 2:
                    $ whoring +=1
        
                $ hg_pf_NicePanties_OBJ.points += 1
        
                jump end_hg_pf
            "-Ask about more favours-":
                m "Are you interested in some additional points?"    
                her "Why not. What are you thinking about?"
                hide screen hermione_main
                with d3
                m "Hmmmm, I want..."

                if whoring <= 2:
                    $ whoring +=1
        
                if hg_pf_NicePanties_OBJ.points < 3:
                    $ hg_pf_NicePanties_OBJ.points += 1
    
                $ menu_x = 0.5 #Menu is moved to the middle.
                $ menu_y = 0.5 #Menu is moved to the middle.

                jump silver_requests_root

    else:
        m "Yes, you can go now."
        if hg_pf_NicePanties_OBJ.points == 0: #First time.
            call her_main("Another 5 points...","soft","baseL") from _call_her_main_5086
            her "Can't wait to tell the guys!"
            call her_main("Only that I can't actually tell them about any of this...","annoyed","angryL") from _call_her_main_5087

        if daytime:
            her "Well, my classes are about to start..."
        else:
            her "It's getting pretty late, [genie_name]... I should go..."

        if whoring < 3: #Adds points till 3.
            $ whoring +=1

        $ hg_pf_NicePanties_OBJ.points += 1
    
        jump end_hg_pf #Hides screens. Hermione walks out. Resets Hermione.







