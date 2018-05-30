

label hg_pf_LetMeTouchThem: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_LetMeTouchThem_OBJ.points == 0:
        m "{size=-4}(I feel like playing with those titties.){/size}"
    else:
        m "{size=-4}(I feel like playing with those titties again.){/size}"

    if hg_pf_LetMeTouchThem_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    if hg_christmas_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL")
                m "My christmas present."
                if whoring >= 14:
                    call her_main("Your present?","grin","baseL")
                    m "Yes, I've been a very good boy this year."
                    call her_main("...","base","glance")
                    call her_main("Fine, let me go wrap myself.","base","down")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_christmas_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
    
    $ current_payout = 35 #Used when haggling about price of th favor.

    if hg_pf_LetMeTouchThem_OBJ.points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.

        call bld
        m "[hermione_name]."
        call her_main("Yes, [genie_name]?","base","base",xpos="base",ypos="base")

        if whoring < 9:
            m "Come here and let me touch your titties!" #Bit of flavour text, lol.
            jump too_much

        m "How about selling me another favour today?"
        call her_main("Uhm... Alright...","open","base")
        her "What will it be, [genie_name]?"
        m "Well, how about you come closer and bare your tits for me...?"
        call her_main("!!!","open","base")
        m "I want to give them a good squeeze."
        call her_main("[genie_name]! Don't you think this is too much?","disgust","glance")
        m "You think?"
        her "I am not one of those harlots from \"Slytherin\", you know..."
        m "I know... You are from \"Gryfonmon\"... or something..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        call her_main("And if I don't feel like it I don't have to sell you a single favour, [genie_name]!","annoyed","worriedL")
        m "Of course..."
        call her_main("...................","annoyed","angryL")
        m "I'll give you 35 house points for this."
        call her_main(".......................","disgust","glance")
        her "All you are going to do is watch, [genie_name]?"
        m "Well, I feel more like touching, actually..."
        her "...................................."


    else: #Not first time.

        if whoring >= 9 and whoring < 15: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.

            call bld
            m "[hermione_name]..."
            call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
            m "I feel like playing with your tits a little..."
            call her_main("[genie_name]... I'd prefer it if you wouldn't make me such offers...","annoyed","annoyed")
            m "Why? Too hard to resist?"
            her "Nothing like that, [genie_name]."
            m "I'll give you 35 house points for this..."
            call her_main("..................","annoyed","angryL")
            her "Well, alright... You can touch them a little..."

        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.

            call bld
            m "[hermione_name]..."
            call her_main("[genie_name]?","base","base",xpos="base",ypos="base")
            m "I feel like playing with your tits a little..."
            call her_main("Of course [genie_name]...","base","ahegao_raised")
    
    call her_walk_desk_blkfade
    hide screen genie
    
    show screen genie_and_tits_01
    with d1
    call hide_blkfade
    stop music fadeout 1.0
    call ctc

    call play_music("playful_tension")# SEX THEME.

    $ hermione_wear_bra = False
    show screen blktone
    call h_action("lift_top")
    call her_main("","","",xpos="mid",ypos="base")
    call ctc
    
    menu:
        m "..."
        "-Grab them-":

            label no_smacking_tits:
                pass
            hide screen hermione_main
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            hide screen bld1
            hide screen blktone
            with fade
            call ctc
            

            #First event. (HERMIONE IS UNWILLING).
            if whoring >= 9 and whoring < 15:

                show screen blktone
                call her_main("..............................","angry","down_raised")    
                m "You have great tits, [hermione_name]..."
                call her_main("....................................","angry","down_raised") 
                m "You like it when I squeeze them like this?"
                call her_main("Excuse me, [genie_name], but you are confusing me with one of those lowly harlots again...","upset","closed")
                call her_main("I am only letting you fondle me because I am getting paid for it...","upset","closed")
                call her_main("Not because I enjoy it...","upset","closed")
                m "I see..."
                m "So, you're more like a prostitute then..."
                call her_main("[genie_name]!","angry","wide")
                call her_main("Prostitutes are getting paid to have sex with men...","angry","wide")
                call her_main("I'd never do something like that!","upset","closed") 
                
                call nar(">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs.")
                
                call her_main("Ah...","open","worriedCl") 
                m "Enjoying yourself, [hermione_name]?"

                if whoring >= 9 and whoring < 12:
                    call her_main("[genie_name], I am only doing this--","upset","closed") 
                    
                    call nar(">You squeeze both of her tits with force...")
                    
                    call her_main("ah...","shock","worriedCl") 
                    m "Tell me you like this, [hermione_name]!"
                    call her_main("[genie_name], I am only letting you do this to me because--","open","worriedCl") 
                    m "I know, know..."
                    m "You are starting to sound like a broken record."
                    call her_main("....","annoyed","annoyed") 
                    call blkfade

                    ">You let go of the girl's breasts..."

                else: #12+
                    call her_main("Ah...","open","down")
                    
                    call nar(">You squeeze her tits a few more times, then give them a firm tug...")
                    
                    call her_main("Ah... [genie_name]...","open","base")
                    m "What? You do enjoy this, don't you?"
                    call her_main("No... I...","open","base")
                    m "Don't you lie to your headmaster, [hermione_name]!"
                    
                    call nar(">You squeeze her tits again...")
                    
                    call her_main("Ah...","open","down")
                    call her_main("I am not lying, [genie_name]...","open","down")
                    call her_main("Why would I enjoy this?","open","base")
                    m "I don't know [hermione_name]. You tell me."
                    
                    call nar(">You keep massaging her breasts...")
                    
                    call her_main("Ah... I...","open","base")
                    m "Yes, what is it?"
                    call her_main("It's... It's nothing, [genie_name]...","angry","base")
                    m "Oh, I think it's something."
                    m "I think you like me squeezing your tits like this."
                    call her_main("[genie_name], please...","angry","down_raised")

                    if daytime:
                        call her_main("Classes are about to start...","angry","down_raised")
                    else: 
                        call her_main("It's getting late...","angry","down_raised")

                    call her_main("Can I go now, [genie_name]? Please?","angry","base")

                    m "Sure, go ahead..."
                    pause 2
                    call her_main("...............","angry","down_raised")
                    pause.2

                    call her_main("[genie_name], your are still... Holding me...","angry","base")
                    m "Oh, right... my bad...."
                    call blkfade
                    
                    ">You let go of Hermione's breasts..."

            #Third Event.
            elif whoring >= 15:

                show screen blktone
                call her_main("Ah...","soft","ahegao")
                m "A bit sensitive today, aren't you?"
                call her_main("I suppose...","base","glance")
                call her_main("Ah...","open","worriedCl")
                m "You like it when I squeeze them like this?"
                call her_main("I do, [genie_name]... Ah...","base","glance")
                m "Heh..."
                m "What if I pinch your nipples?"
                call her_main("!!!","angry","base")
                call her_main("Ah! [genie_name]...","open","worriedCl")
                m "And what if I do this?"
                call nar(">You grab the girl by her hard nipples and start pulling...")
                call her_main("Ah... Ah... Ah... [genie_name]...","shock","worriedCl")
                m "What if I pull even harder?"
                with hpunch

                call her_main("Ah... [genie_name], please...","scream","wide")
                call nar(">Hermione clutches the edge of your desk to keep herself from taking a step towards you...")
                m "Good girl..."
                call her_main("*Panting heavily*","grin","dead")
                m "Do you enjoy this?"
                call her_main("You are hurting me, [genie_name]...","shock","baseL",cheeks="blush",tears="soft")
                m "But do you enjoy it?"

                if whoring < 18:
                    call her_main("Ah... Yes, [genie_name]... I don't know why, but I do...","clench","worried",cheeks="blush",tears="soft")
                else:
                    call her_main("Ah... Yes, [genie_name]... I love it...","silly","worried",cheeks="blush",tears="soft")

                m "Good girl..."
                call nar(">You let go of her nipples...")
                call her_main("Ah...","silly","worried",cheeks="blush",tears="soft")

                show screen bld1
                call hide_blktone

                m "This will be all for today, [hermione_name]..."
                call her_main("Oh...?","shock","baseL",cheeks="blush",tears="soft")
                m "What is it? You look disappointed."
                m "I will pay you of course..."
                call her_main("That's not it, [genie_name]...","angry","suspicious",cheeks="blush")
                call her_main("It's...","angry","suspicious",cheeks="blush")

                if daytime:
                    call her_main("It's just that I still have some time left before I have to leave for the classes and...","shock","baseL",cheeks="blush",tears="soft")
                else:
                    call her_main("It's not really that late yet, is it?","shock","baseL",cheeks="blush",tears="soft")

                call her_main("uhm...","angry","suspicious",cheeks="blush")
                call her_main("...................","angry","suspicious",cheeks="blush")
                m "You want me to hurt you some more, don't you?"

                if whoring < 18:
                    call her_main("I don't \"want to\"... ","shock","baseL",cheeks="blush",tears="soft")
                    call her_main("But if you insist [genie_name]...","silly","worried",cheeks="blush",tears="soft")
                    m "Well, I do insist... apparently."
                else:
                    call her_main("Yes please, [genie_name]!","shock","baseL",cheeks="blush",tears="soft")
                    call her_main("I'll even let you do it for free...","shock","baseL",cheeks="blush",tears="soft")
                    m "Well, in that case..."

                call her_main("Ah...","silly","worried",cheeks="blush",tears="soft")
                call ctc
                call blkfade

                ">You spend some more time with Hermione's breasts..."

        "-Slap them-":

            show screen blktone
            call nar(">You give Hermione's tits a loud slap!")
            call slap_her

            #First Event (HERMIONE IS UNWILLING).
            if whoring >= 9 and whoring <= 11:

                $ mad += 20
                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch! It hurts! *SOB!*","angry","worried",cheeks="blush")
                m "Did you like it though?"
                call her_main("Did I... \"like it\, [genie_name]..?","annoyed","annoyed")
                call her_main("What girl in her right mind would like to be treated this way?")
                stop music fadeout 1.0

                hide screen blktone
                show screen bld1
                call set_hermione_action("none")
                pause.5
    
                call her_main("You are a mean and demented old man!","angry","worried",cheeks="blush",tears="soft")
                hide screen hermione_main 
                call blkfade 
                
                m "............"
                call play_sound("door")
                m "Well, no points for \"Gryffindor\" then..."
                
                jump could_not_flirt #Favor failed! #Needs Blkfade!
                
            #Second Event.        
            elif whoring >= 12 and whoring < 15:

                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch!","angry","worried",cheeks="blush")
                call her_main("[genie_name], what did you do this for?")
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_main("...Of course, not, [genie_name].","annoyed","closed")
                m "Let's try this again, then."
                call her_main("What?","annoyed","base")
                  
                call slap_her

                call her_main("!!!","scream","wide",cheeks="blush")
                call her_main("Ouch! Stop hurting me!")
                m "Admit that you enjoy it and I will."
                call her_main("But I don't...","disgust","down_raised")
                call her_main("And if you plan to keep on doing this to me, [genie_name]...")
                call her_main("...then I think I should leave.","annoyed","annoyed")
                m "Fine, fine..."

                jump no_smacking_tits #Jumps to usual tits molesting scene.

            #Third Event.
            elif whoring >= 15:

                call her_main("Ah!!!","scream","wide",cheeks="blush")
                call her_main("[genie_name], why did you do that?","grin","glance",cheeks="blush")
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_main("..........","annoyed","base")
                call her_main("I am not a pervert...")
                call nar(">You give Hermione's tits another loud smack!")

                call slap_her

                call her_main("A-ah!!!","silly","down",cheeks="blush")
                m "Tell me you like it!"
                her "[genie_name]... I..."
                call nar(">You unleash a whole series of slaps!")
                
                call slap_her

                call slap_her
                
                call slap_her

                call nar(">Hermione's tits bounce allover the place, completely out of control")
                call her_main("A-ah!!! Ah!!! A-a-aha!!!","silly","ahegao",cheeks="blush",tears="soft")
                m "You enjoy this. Admit it."
                call her_main("...........","base","dead",cheeks="blush",tears="soft")
                call nar(">You smack her tits again.")
                
                call slap_her
                
                call slap_her

                call slap_her

                call her_main("A-ah! Yes! I do, I do! A-ah...","silly","ahegao",cheeks="blush",tears="soft")
                call her_main("...does this mean I'm a pervert, [genie_name]?","angry","worried",cheeks="blush",tears="soft")
                m "What?"
                m "Stop being silly, [hermione_name]."
                m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
                her "......"
                her "Are you sure about that, [genie_name]?"
                m "Yes. Believe me, I know."
                call nar(">You give her tits one more slap!")
                
                call slap_her

                call her_main("A-ah... Yes... Thank you, [genie_name].","silly","ahegao",cheeks="blush",tears="soft")
                m "Well... Enough with the slapping for now..."

                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    call h_action("none") #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01  
    hide screen groping_01
    hide screen groping_02
    hide screen groping_naked_tits

    call her_chibi("stand","desk","base")

    hide screen chair_left
    show screen genie 
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main("","","",trans="fade",xpos="mid",ypos="base")
    
    stop music fadeout 1.0

    if whoring <= 17:
        m "Yes, [hermione_name].  35 points to \"Gryffindor\"." 
        $ gryffindor +=35
    
    call her_main("Thank you, [genie_name]...","soft","baseL")
    
    if whoring < 12:
        $ whoring +=1
    
    $ hg_pf_LetMeTouchThem_OBJ.points +=1

    if whoring >= 9 and whoring < 12:
        $ new_request_12_heart = 1
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if whoring >= 12 and whoring < 15:
        $ new_request_12_heart = 2
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if whoring >= 15:
        $ new_request_12_heart = 3
        $ hg_pf_LetMeTouchThem_OBJ.hearts_level = 3 #Event hearts level (0-3)


    hide screen bld1
    hide screen hermione_main
    with d3
    pause.2
    
    call her_walk("desk","leave",2.5)

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    $ custom_outfit_old = temp_outfit
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    if daytime:
        call play_music("day_theme")
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme")
        $ hermione_sleeping = True
        jump night_main_menu     
    







