

label luna_favour_4: ###Luna handjob #DONE

    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if lun_whoring > 13:
        jump luna_handjob_hermione_call
    if luna_addicted:
        if lun_whoring <= 11:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "[lun_name]?"
        call lun_main("yes, [lun_genie_name]...","normal","base","angry","R")
        m "Would it be possible for me to buy another favour..."
        call lun_main("Does it involve me cranking out that delicous cum from your wrinkly old balls?","base","angry","angry","R")
        call lun_main("Hmmmm?","base","seductive","base","mid")
        m "Possibly..."
        call lun_main("mmmm... good boy...","base","mad","mad","mid")
        call lun_main("well...","base","mad","mad","mid")
        call lun_main("stand up [lun_genie_name]...","base","mad","mad","mid")

        show screen blkfade
        ">You stand up and walk around your desk, standing in front of Luna."
        ">You open your cloak and pull out your cock."
        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ gen_chibi_xpos = -20
        $ gen_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen g_c_u
        with fade
        hide screen blktone
        hide screen blkfade
        with d5
        call ctc

        m "Well..."
        call lun_main("...","upset","angry","angry","mid")
        ">Luna looks down at your cock."
        call lun_main("Mmmm, to think something so disgusting could be so tasty...","base","suspicious","mad","mid")
        ">She takes a firm hold of it with her right hand"
        $ luna_r_arm = 3
        $ genie_xpos = 300
        $ genie_ypos = 0
        $ luna_xpos = 390
        $ genie_base = "characters/genie/base/open.png"
        call gen_main("!!!","grin")
        call lun_main("*Hmmph*","base","seductive","angry","mid")
        call lun_main("(It's so warm...)","base","seductive","mad","down")
        ">Luna slowly starts stroking your cock with her hand, her movements are fast yet stiff."
        m "Why don't you try grabbing it with both hands, [lun_name]..."
        call lun_main("Hmph... I don't think so [lun_genie_name]!","base","mad","angry","mid")
        m "..."
        ">Luna starts moving her hand back and forth along the length of your cock."
        m "ugh... Yes, that's it..."
        call lun_main("See, one hand's all you need.","upset","suspicious","mad","down")
        m "Mmmm, yes... just like that, [lun_name]..."
        call lun_main("Is this good, [lun_genie_name]?","soft","annoyed","sad","mid")
        m "yes, yes, this is amazing..."
        call lun_main("good...","base","suspicious","sad","mid")
        call lun_main("but...","normal","suspicious","sad","R")
        call lun_main("I think you need a little more encouragement...","base","mad","sad","mid")
        m "What are you thinking?"
        call lun_main("well...","base","suspicious","mad","mid")

        hide screen luna_main
        $ luna_wear_bottom = False
        $ luna_wear_bra = False
        $ luna_wear_panties = False
        $ luna_wear_top = False
        show screen luna_main
        with d3
        call ctc

        ">Luna casually strips, all while keeping a firm grip of your cock."
        g4 "Now that's some encouragement!"
        call lun_main("That's not all sir...","base","suspicious","mad","mid")
        $ genie_base = "characters/genie/base/hard.png"
        $ luna_r_arm = 1

        menu:
            "-Luna teases you with her butt-":
                $ luna_flip = -1
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ luna_xpos = 500
                ">Luna slowly turns around, giving a nice view of her pale white cheeks."
                m "Mmmm"
                ">She slowly rolls her hips side to side."
                call lun_main("Enjoying the view...","base","mad","sad","R")
                m "Very nice, [lun_name]!"
                call lun_main("...","normal","angry","sad","mid")
                call lun_main("Thank you sir...","base","angry","sad","R")
                $ luna_xpos = 390
                call ctc

                ">She quietly backs into you, just letting the tip of your cock touch her ass, a drop of precum sticks to her cheek."
                call lun_main("Mmm, that's much better...","base","seductive","angry","R")
                m "Gods yes."
                call lun_main("...","base","happyCl","angry","R")
                call ctc

                $ luna_xpos = 390
                call lun_main("well, I suppose I better get back to work...","base","mad","angry","mid")
                ">Luna slowly turns back around before placing her hand back on your cock."
                $ luna_r_arm = 3
                $ luna_flip = 1
                $ genie_base = "characters/genie/base/open.png"
                ">Luna starts pumping your cock a little faster."

            "-Luna teases you with her thighs-":
                $ luna_choice = 2
                call lun_main("Come on Professor...","base","mad","sad","R")
                $ luna_xpos = 350
                ">Luna steps towards you."
                m "mmmm..."
                call lun_main("Get a nice big, tasty load ready for me...","normal","angry","sad","mid")
                m "Ah yes..."
                call lun_main("get ready to cum all for your student.","base","angry","sad","mid")
                $ luna_xpos = 280
                $ luna_ypos = -40
                ">She steps even closer, forcing your cock in between her soft thighs."
                m "Ah..."
                call lun_main("so that I can eat it...","base","angry","angry","down")
                m "yes..."
                call lun_main("Mmmm, you like that don't you...","base","mad","angry","R")
                ">Luna starts rolling her thighs around your cock. You can even feel her wet mound grinding against the top of your shaft."
                g4 "Ah! yes!"
                call lun_main("...","base","suspicious","mad","mid")
                g4 "[lun_name]..."
                call lun_main("Hmmm, are you feeling alright now, [lun_genie_name]?","base","seductive","raised","R")
                g4 "yes... thank you, [lun_name]..."
                call lun_main("Good boy.","base","angry","angry","down")
                $ luna_xpos = 390
                $ luna_ypos = 0
                call lun_main("*Ptew*","open_tongue","seductive","angry","downL")
                $ luna_r_arm = 3
                $ luna_flip = 1
                $ genie_base = "characters/genie/base/open.png"
                ">Luna spits into her hand before placing it back on your cock."

        g4 "Mmmm, yes that's it, [lun_name]..."
        call lun_main("...","base","angry","angry","mid")
        g4 "Just keep pumping that hand up and down."
        call lun_main("......","base","mad","mad","mid")
        if luna_choice == 1:
            ">Luna gently starts shaking her boobs as she jerks you off."
        else:
            call lun_main("*Ptew*","open_tongue","angry","mad","downL")
            ">Luna spits into her hand again and places it back on your cock."
        ">She then starts pumping your cock even faster."
        g4 "Gods yes..."
        g4 "(This is it, where should I cum?)"

        menu:
            "-On her cunt!-":
                ">You place your hand on Luna's cheek, trying to hold her in position."

            "-On her tits!-":
                ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

        call lun_main("[lun_genie_name]!!!","clench","angry","mad","mid")
        call lun_main("You're not trying to cum on me are you?","upset","mad","mad","mid")
        g4 "Ah, [lun_name], I'm almost there!"
        $ genie_base = "characters/genie/base/hard.png"
        $ luna_ypos = 220
        $ luna_xpos = 350
        $ luna_r_arm = 1
        ">Luna gets on her knees before you."
        ">She takes her hand off your cock, leaving you high and dry."
        call lun_main("from now on, the only place you'll be coming is here...","upset","suspicious","mad","mid")
        g4 "Mmmm yes!"
        call lun_main("...","silly","seductive","angry","down")
        $ luna_xpos = 310
        ">She leans forward, giving your cock a tentative lick."
        call lun_main("...","silly","suspicious","sad","downL")
        call lun_main("(This doesn't taste nearly as good...)","silly","suspicious","mad","R")
        call lun_main("(although it's not the worst...)","silly","seductive","sad","down")
        g4 "Almost there slut!"
        $ luna_xpos = 350
        ">She moves back slightly from your cock."
        call lun_main("then cum for me...","base","angry","mad","down")
        call lun_main("cum...","base","seductive","sad","empty")
        call ctc
        g4 "Ah{size=+2} here{/size} {size=+4}it{/size} {size=+6}is!{/size}"

        menu:
            "Where should you cum?"
            "-Face-":
                $ luna_choice = 1
                $ luna_cum = 11
                $ luna_wear_cum = True
                call cum_block

                call lun_main("{image=textheart}{image=textheart}{image=textheart}","silly","happyCl","sad","down")
                call ctc

                ">You start shooting your load across her face, coating her in your sticky cum."
                hide screen g_c_c_u
                $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ genie_base = "characters/genie/base/open.png"
                hide screen genie_main
                with d3

                $ luna_xpos = 390
                $ luna_ypos = 0
                ">Luna hops to her feet."
                $ luna_cum = 12
                ">Luna then collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","angry","angry","mid")
                call lun_main("Just give me a moment to clean up sir...","base","seductive","angry","mid")
                m "Sure..."
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
                call ctc

                $ luna_cum = 14
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
                $ luna_cum = 15
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
                $ luna_wear_cum = False
                call lun_main("...","full","seductive","sad","empty")
                call lun_main("*gulp*","base","happyCl","sad","mid")
                call lun_main("ah...","base","happyCl","sad","mid")
                call lun_main("amazing...","base","seductive","sad","mid")

            "-Mouth-":
                $ luna_choice = 2
                call cum_block

                call lun_main("{image=textheart}{image=textheart}{image=textheart}","full","happyCl","sad","down")
                call ctc

                ">You start firing your load directly into her open mouth. Her eyes glaze over as she struggles to fit it all in."
                g4 "Argh! by the gods {size=+10}YES!{/size}"
                call lun_main("!!!","full","seductive","sad","empty")
                call ctc

                call lun_main("(It's so good...)","full","seductive","sad","R")
                call lun_main("...","full","seductive","down","sad")
                g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
                g4 "mmmm....."
                hide screen g_c_c_u
                $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ genie_base = "characters/genie/base/open.png"
                hide screen genie_main
                with d3

                m "That hit the spot..."
                call lun_main("*gulp*","base","happyCl","sad","mid")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","empty")
                m "Ahh... that was fantastic slut..."
                call lun_main("[lun_genie_name]...","base","suspicious","angry","R")

        $ g_c_u_pic = "characters/genie/chibis/masturbating/b_01.png"
        $ luna_xpos = 390
        $ luna_ypos = 0
        m "well then, Here's your payment, [lun_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        call lun_main("Oh um... yes, Thank you, [lun_genie_name].","base","seductive","base","R", cheeks="blush")
        call lun_main("let me just get dressed...","base","seductive","base","R", cheeks="blush")
        hide screen luna_main
        with d3

        call load_luna_clothing_saves

        ">Luna quickly gets dressed before leaving your office, a streak of embarrassment across her face."
        $ luna_wear_cum = False
        $ luna_wear_cum_under = False
        m "Weird..."

        hide screen g_c_u
        show screen genie
        hide screen chair_left
        hide screen desk

        jump luna_away


    else:
        if lun_whoring <= 10: #FIRST TIME - Change this to 10 when part 2 added
            if lun_whoring <= 10:
                $ lun_whoring += 1
            call play_music("chipper_doodle")
            m "[lun_name]?"
            call lun_main("yes, [lun_genie_name]...","normal","base","angry","R")
            m "Would it be possible for me to buy another favour..."
            call lun_main("...","normal","angry","angry","R")
            call lun_main("Go on...","normal","angry","angry","R")

            menu:
                "-Ask for a handjob politely-" if lun_sub < lun_dom:
                    $ current_payout = 160
                    if lun_dom <= 8:
                        $ lun_dom += 1
                    $ luna_choice = 3
                    m "Well seeing as how you're so skilled at everything you turn your hand towards..."
                    call lun_main("Mhmmm...","upset","suspicious","angry","R")
                    m "I was hoping you could turn your hand towards my cock."
                    call lun_main("...","normal","mad","base","R")
                    m "please..."
                    call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
                    call lun_main("Isn't it enough that I let you touch yourself...","upset","suspicious","mad","R")
                    m "There'll be a hefty reward..."
                    call lun_main("...","upset","mad","mad","R")
                    call lun_main("......","normal","mad","angry","mid")
                    call lun_main("Well seeing as how you asked so nicely...","base","mad","base","mid")
                    m "..."
                    call lun_main("Get over here...","base","angry","mad","mid")
                    m "Fantastic! Let me just stand up."
                    call lun_main("(This couldn't get any easier)","base","mad","angry","R")

                "-Beg for a handjob-" if lun_dom >= 7:
                    $ current_payout = 200
                    if lun_dom <= 8:
                        $ lun_dom += 1
                    $ luna_choice = 4
                    m "Well if it's not too much trouble..."
                    call lun_main("Mhmmm...","upset","suspicious","angry","R")
                    m "I was hoping you could..."
                    call lun_main("...","normal","mad","base","R")
                    m "give me a handjob..."
                    call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
                    m "If it's not too much trouble..."
                    call lun_main("Well I suppose I probably should.","base","seductive","base","R")
                    call lun_main("Who knows who you'll call up here if I don't...","base","mad","mad","mid")
                    m "Thank you..."
                    call lun_main("...","upset","mad","mad","R")
                    call lun_main("......","normal","mad","angry","mid")
                    call lun_main("However I do expect to be fairly compensated...","base","mad","base","mid")
                    m "Of course."
                    call lun_main("Good. Now Get over here...","base","angry","mad","mid")
                    m "Fantastic! Let me just stand up."
                    call lun_main("(This couldn't get any easier...)","base","mad","angry","R")
                    call lun_main("(I'll be the only person in his will by the end of the month at this rate...)","base","suspicious","mad","mid")

            show screen blkfade

            ">You stand up and walk around your desk, standing in front of Luna."
            ">You open your cloak and pull out your cock."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ gen_chibi_xpos = -20
            $ gen_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            call ctc

            m "Well..."
            call lun_main("...","upset","angry","angry","mid")
            ">Luna looks down at your cock."
            call lun_main("Disgusting...","base","suspicious","mad","mid")
            ">She takes a firm hold of it with her right hand"
            $ luna_r_arm = 3
            $ genie_xpos = 300
            $ genie_ypos = 0
            $ luna_xpos = 390
            $ genie_base = "characters/genie/base/hard.png"
            call gen_main("!!!","grin")
            call lun_main("*Hmmph* At least it isn't small...","base","seductive","angry","mid")
            call lun_main("(I can't even fit my hand around it.)","base","seductive","mad","down")
            ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
            m "Why don't you try grabbing it with both hands, [lun_name]..."
            call lun_main("Hmph... you wish!","base","mad","angry","mid")
            m "..."
            ">Luna starts moving her hand back and forth along the length of your cock."
            m "ugh... Yes, that's it..."
            call lun_main("(Men really are the worst)","upset","suspicious","mad","down")
            m "Mmmm, yes... just like that, [lun_name]..."
            call lun_main("Is this good, [lun_genie_name]?","soft","annoyed","sad","mid")
            m "yes, yes, this is amazing..."
            call lun_main("good...","base","suspicious","sad","mid")
            call lun_main("but...","normal","suspicious","sad","R")
            call lun_main("Do you need a little more encouragement?","base","mad","sad","mid")
            m "What are you thinking?"
            call lun_main("......","base","suspicious","mad","mid")

            menu:
                "-Luna takes her top off-":
                    ">Luna slowly removes her vest and starts to unbutton her top."
                    m "Mmmm"
                    hide screen luna_main
                    $ luna_wear_top = False
                    $ luna_choice = 1
                    $ luna_r_arm = 2
                    show screen luna_main
                    with d3

                    ">She takes her shirt off and places it onto the floor."
                    call lun_main("There...","base","mad","sad","R")
                    m "Very nice, [lun_name]!"
                    call lun_main("...","normal","angry","sad","mid")
                    call lun_main("Thank you sir...","base","angry","sad","mid")
                    $ luna_r_arm = 3
                    ">She places her hands back around your cock."
                    call lun_main("Mmm, much better...","base","seductive","angry","mid")
                    m "Gods yes."
                    call lun_main("...","base","seductive","angry","mid")
                    call lun_main("I'd take my bra off as well...","normal","seductive","sad","R")
                    call lun_main("But I don't think you'd be able to stop yourself from cumming on the spot, would you?","base","mad","mad","mid")
                    g4 "probably not!"
                    call lun_main("...","base","suspicious","angry","mid")
                    ">Luna starts pumping your cock a little faster."

                "-Luna teases you-":
                    $ luna_choice = 2
                    call lun_main("Come on Professor...","base","mad","sad","R")
                    ">Luna starts moving her hands up and down your cock a little faster."
                    m "mmmm..."
                    call lun_main("Get a nice big load ready for me...","normal","angry","sad","mid")
                    m "Ah yes..."
                    call lun_main("get ready to cum all over your student.","base","angry","sad","mid")
                    ">She speeds up the pace."
                    m "Ah..."
                    call lun_main("What's wrong?","normal","angry","raised","mid")
                    m "Well if you go that fast the friction's a little painful."
                    call lun_main("Really?...","base","mad","angry","mid")
                    ">Luna doesn't slow down. If anything she speeds up slightly."
                    g9 "Ah!"
                    call lun_main("...","base","suspicious","mad","mid")
                    g9 "[lun_name]..."
                    call lun_main("Hmmm, do You want me to spit on your cock then?","base","seductive","raised","mid")
                    g9 "Just a little bit..."
                    call lun_main("...","base","seductive","angry","mid")
                    call lun_main("......","base","seductive","mad","mid")
                    g9 "Please..."
                    call lun_main("Good boy.","base","angry","angry","mid")
                    call lun_main("*Ptew*","open_tongue","seductive","angry","downL")
                    ">Luna spits into her hand before placing it back on your cock."

            g4 "Mmmm, yes that's it, [lun_name]..."
            call lun_main("...","base","angry","angry","mid")
            g4 "Just keep pumping those hands up and down."
            call lun_main("......","base","mad","mad","mid")
            if luna_choice == 1:
                ">Luna gently starts shaking her boobs as she jerks you off."
            else:
                call lun_main("*Ptew*","open_tongue","angry","mad","downL")
                ">Luna spits into her hand again and places it back on your cock."
            ">She then starts pumping your cock even faster."
            g4 "Gods yes..."
            g4 "(This is it, where should I cum?)"

            menu:
                "-On her face-":
                    ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

                "-On her tits-":
                    ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

            call lun_main("[lun_genie_name]!!!","clench","angry","mad","mid")
            call lun_main("You're not trying to cum on me are you?","upset","mad","mad","mid")
            g4 "Ah, [lun_name], I'm almost there."
            call lun_main("Well...","upset","suspicious","mad","mid")
            $ luna_wear_bottom = False
            ">Luna quickly pulls down her skirt."
            g4 "!!!"
            call lun_main("You cum...","upset","mad","mad","mid")
            g4 "Ah..."
            ">Luna slowly pulls her panties forward, exposing her pussy to the air."
            ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
            call lun_main("Where I tell you...","upset","suspicious","mad","mid")
            g4 "mmmm"
            call lun_main("Now...","normal","mad","mad","mid")
            call lun_main("Cum.","base","seductive","angry","mid")
            $ g_c_c_u_pic = "jerking_off_cum_ani"
            $ genie_cum_chibi_xpos = -45
            $ genie_cum_chibi_ypos = 5
            show screen g_c_c_u
            $ luna_wear_cum_under = True
            $ luna_cum = 10
            call cum_block

            ">You start shooting your load directly into Luna's panties, coating her pussy in cum."
            g4 "Argh! by the gods {size=+10}YES!{/size}"
            call lun_main("...","base","seductive","base","down")
            call lun_main("(It's so warm...)","base","seductive","sad","R")
            g4 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
            g4 "mmmm....."
            hide screen g_c_c_u
            $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
            $ luna_r_arm = 2
            hide screen genie_main
            with d3

            m "That hit the spot..."
            call lun_main("({image=textheart}{image=textheart}{image=textheart})","base","seductive","sad","mid")
            call lun_main("[lun_genie_name]!","base","mad","mad","mid")
            call lun_main("How could you! Cumming on your students {size=-10}pussy{/size}...","base","angry","angry","mid")
            m "Ahh... that was fantastic slut..."
            $ g_c_u_pic = "characters/genie/chibis/masturbating/b_01.png"
            call lun_main("[lun_genie_name]...","base","suspicious","angry","R")

        else: #last time event is run before cum addict variant
            if lun_whoring <= 11:
                $ lun_whoring += 1
            call play_music("chipper_doodle")
            m "[lun_name]?"
            call lun_main("yes, [lun_genie_name]...","normal","base","angry","R")
            m "Would it be possible for me to buy another favour..."
            call lun_main("I think I know what you want...","base","angry","angry","R")
            call lun_main("but why don't you ask me anyway...","base","seductive","base","mid")
            call lun_main("you know I like to hear you beg.","base","mad","mad","mid")

            menu:
                "-Ask for a handjob politely-" if lun_sub < lun_dom:
                    $ current_payout = 160
                    if lun_dom <= 8:
                        $ lun_dom += 1
                    $ luna_choice = 3
                    m "Well seeing as how you're so skilled at everything you turn your hand towards..."
                    call lun_main("Mhmmm...","upset","suspicious","angry","R")
                    m "I was hoping you could turn your hand towards my cock."
                    call lun_main("...","normal","mad","base","R")
                    m "please..."
                    call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
                    call lun_main("Isn't it enough that I let you touch yourself...","upset","suspicious","mad","R")
                    m "There'll be a hefty reward..."
                    call lun_main("...","upset","mad","mad","R")
                    call lun_main("......","normal","mad","angry","mid")
                    call lun_main("Well seeing as how you asked so nicely...","base","mad","base","mid")
                    m "..."
                    call lun_main("Get over here...","base","angry","mad","mid")
                    m "Fantastic! Let me just stand up."
                    call lun_main("(This couldn't get any easier)","base","mad","angry","R")

                "-Beg for a handjob-" if lun_dom >= 7:
                    $ current_payout = 200
                    if lun_dom <= 8:
                        $ lun_dom += 1
                    $ luna_choice = 4
                    m "Well if it's not too much trouble..."
                    call lun_main("Mhmmm...","upset","suspicious","angry","R")
                    m "I was hoping you could..."
                    call lun_main("...","normal","mad","base","R")
                    m "give me a handjob..."
                    call lun_main("Really? You want me to stroke that filthy cock of yours?","upset","mad","angry","mid")
                    m "If it's not too much trouble..."
                    call lun_main("Well I suppose I probably should.","base","seductive","base","R")
                    call lun_main("Who knows who you'll call up here if I don't...","base","mad","mad","mid")
                    m "Thank you..."
                    call lun_main("...","upset","mad","mad","R")
                    call lun_main("......","normal","mad","angry","mid")
                    call lun_main("However I do expect to be fairly compensated...","base","mad","base","mid")
                    m "Of course."
                    call lun_main("Good. Now Get over here...","base","angry","mad","mid")
                    m "Fantastic! Let me just stand up."
                    call lun_main("(This couldn't get any easier...)","base","mad","angry","R")
                    call lun_main("(I'll be the only person in his will by the end of the month at this rate...)","base","suspicious","mad","mid")

            show screen blkfade
            ">You stand up and walk around your desk, standing in front of Luna."
            ">You open your cloak and pull out your cock."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ gen_chibi_xpos = -20
            $ gen_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            call ctc

            m "Well..."
            call lun_main("...","upset","angry","angry","mid")
            ">Luna looks down at your cock."
            call lun_main("Disgusting...","base","suspicious","mad","mid")
            ">She takes a firm hold of it with her right hand"
            $ luna_r_arm = 3
            $ genie_xpos = 300
            $ genie_ypos = 0
            $ luna_xpos = 390
            $ genie_base = "characters/genie/base/hard.png"
            call gen_main("!!!","grin")
            call lun_main("*Hmmph* At least it isn't small...","base","seductive","angry","mid")
            call lun_main("(I can't even fit my hand around it.)","base","seductive","mad","down")
            ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
            m "Why don't you try grabbing it with both hands, [lun_name]..."
            call lun_main("Hmph... you wish [lun_genie_name]!","normal","mad","angry","mid")
            m "..."
            ">Luna starts moving her hand back and forth along the length of your cock."
            m "ugh... Yes, that's it..."
            call lun_main("(He loves this...)","base","suspicious","mad","down")
            m "Mmmm, yes... just like that, [lun_name]..."
            call lun_main("Is this good [lun_genie_name]?","soft","annoyed","sad","mid")
            m "yes, yes, this is amazing..."
            call lun_main("good...","base","suspicious","sad","mid")
            call lun_main("but...","normal","suspicious","sad","R")
            call lun_main("Do you need a little more encouragement?","base","mad","sad","mid")
            m "What are you thinking?"
            call lun_main("......","base","suspicious","mad","mid")

            menu:
                "-Luna takes her top off-":
                    ">Luna slowly removes her vest and starts to unbutton her top."
                    m "Mmmm"
                    hide screen luna_main
                    $ luna_wear_top = False
                    $ luna_choice = 1
                    show screen luna_main
                    with d3

                    ">She takes her shirt off and places it onto the floor."
                    call lun_main("There...","base","mad","sad","R")
                    $ luna_r_arm = 2
                    m "Very nice, [lun_name]!"
                    call lun_main("...","normal","angry","sad","mid")
                    call lun_main("Thank you sir...","base","angry","sad","mid")
                    $ luna_r_arm = 3
                    ">She places her hands back around your cock."
                    call lun_main("Mmm, much better...","base","seductive","angry","mid")
                    m "Gods yes."
                    call lun_main("...","base","seductive","angry","mid")
                    call lun_main("well, seeing as how you're being such a good boy...","base","mad","angry","down")
                    hide screen luna_main
                    $ luna_wear_bra = False
                    $ luna_r_arm = 2
                    $ luna_l_arm = 2
                    show screen luna_main
                    with d3

                    ">Luna slowly removes her bra before placing her hand back on your cock."
                    hide screen luna_main
                    $ luna_r_arm = 3
                    $ luna_l_arm = 1
                    show screen luna_main
                    with d3

                    ">Luna starts pumping your cock a little faster."

                "-Luna teases you-":
                    $ luna_choice = 2
                    call lun_main("Come on Professor...","base","mad","sad","R")
                    ">Luna starts moving her hands up and down your cock a little faster."
                    m "mmmm..."
                    call lun_main("Get a nice big load ready for me...","normal","angry","sad","mid")
                    m "Ah yes..."
                    call lun_main("get ready to cum all over your student.","base","angry","sad","mid")
                    ">She speeds up the pace."
                    m "Ah..."
                    call lun_main("mmmm, hurts doesn't it.","base","angry","angry","down")
                    m "yes..."
                    call lun_main("Really?...","base","mad","angry","mid")
                    ">Luna doesn't slow down. If anything she speeds up slightly."
                    g9 "Ah! yes!"
                    call lun_main("...","base","suspicious","mad","mid")
                    g9 "[lun_name]..."
                    call lun_main("Hmmm, do You want me to spit on your cock then?","base","seductive","raised","mid")
                    g9 "yes... please, [lun_name]..."
                    call lun_main("Good boy.","base","angry","angry","mid")
                    call lun_main("*Ptew*","open_tongue","seductive","angry","downL")
                    ">Luna spits into her hand before placing it back on your cock."

            g4 "Mmmm, yes that's it, [lun_name]..."
            call lun_main("...","base","angry","angry","mid")
            g4 "Just keep pumping those hands up and down."
            call lun_main("......","base","mad","mad","mid")
            if luna_choice == 1:
                ">Luna gently starts shaking her boobs as she jerks you off."
                call lun_main("......","base","seductive","angry","mid")
            else:
                call lun_main("*Ptew*","open_tongue","angry","mad","downL")
                ">Luna spits into her hand again and places it back on your cock."
            ">She then starts pumping your cock even faster."
            g4 "Gods yes..."
            g4 "(This is it, where should I cum?)"

            menu:
                "-On her face-":
                    ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

                "-On her tits-":
                    ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

            call lun_main("[lun_genie_name]!!!","clench","angry","mad","mid")
            call lun_main("You're not trying to cum on me are you?","upset","mad","mad","mid")
            g4 "Ah [lun_name], I'm almost there!"
            call lun_main("hmmm... (Might as well make some more money from the, [lun_genie_name]...)","upset","suspicious","mad","mid")

            hide screen luna_main
            $ luna_wear_bottom = False
            $ luna_wear_bra = False
            $ luna_wear_panties = False
            $ luna_wear_top = False
            show screen luna_main
            with d3

            ">Luna quickly strips, all while keeping a firm grip of your cock.."
            g4 "hurry up! You'll ruin the damn moment!"
            call lun_main("well then, pick...","normal","seductive","sad","mid")
            g4 "you mean..."
            ">Leans forward slowly while ever so slightly jiggling her milky boobs."
            ">Her right hand is still wrapped around your cock as she pumps slowly, keeping you at firmly at the edge."
            call lun_main("pick where you want to cum...","base","seductive","mad","mid")
            g4 "Ah yes!"
            call lun_main("you can pick my boobs...","normal","mad","sad","R")
            ">She gives them another shake."
            call lun_main("or my thighs...","base","seductive","angry","mid")
            ">She rubs them together as she rotates on the balls of her feet."
            call lun_main("boobs are an extra 100...","base","angry","mad","mid")
            call lun_main("thighs are 50...","normal","angry","angry","R")
            g4 "Ah{size=+2} here{/size} {size=+4}it{/size} {size=+6}is!{/size}"

            menu:
                "-boobs-":
                    $ current_payout += 100
                    show screen g_c_c_u
                    $ luna_cum = 5
                    $ luna_wear_cum = True
                    call cum_block

                    ">You start shooting your load across her chest, coating her tits in cum."

                "-thighs-":
                    $ current_payout += 50
                    show screen g_c_c_u
                    $ luna_cum = 10
                    $ luna_wear_cum = True
                    call cum_block

                    ">You start spurting over Luna's soft thighs, coating her pussy in cum."

                "-{size=+10}FACE!{/size}-":
                    jump luna_cum_addict_event

            g4 "Argh! by the gods {size=+10}YES!{/size}"
            call lun_main("...","base","seductive","base","down")
            call lun_main("(It's so warm...)","base","seductive","sad","R")
            g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
            g4 "mmmm....."
            hide screen g_c_c_u
            $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
            $ luna_r_arm = 2
            hide screen genie_main
            with d3

            m "That hit the spot..."
            call lun_main("({image=textheart}{image=textheart}{image=textheart})","base","seductive","sad","mid")
            if luna_choice == 1:
                $ luna_cum = 12
                ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","mid")
                call lun_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}","base","seductive","sad","mid")
                call lun_main("but please just shoot it into my mouth next time?","base","seductive","sad","mid")
                m "Sure..."
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call lun_main("...","base","seductive","sad","mid")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","mid")
                call ctc

                $ luna_cum = 14
                call lun_main("...","base","seductive","sad","mid")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","mid")
                $ luna_cum = 15
                call lun_main("...","base","seductive","sad","mid")
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","mid")
                $ luna_wear_cum = False
                call lun_main("ah...","base","seductive","sad","mid")
                call lun_main("amazing...","base","seductive","sad","mid")

            m "Ahh... that was fantastic slut..."
            $ g_c_u_pic = "characters/genie/chibis/masturbating/b_01.png"
            call lun_main("[lun_genie_name]...","base","suspicious","angry","R")

    hide screen luna_main
    call load_luna_clothing_saves
    $ luna_wear_cum = False
    show screen luna_main
    hide screen bld1
    with d3

    m "well then, Here's your payment, [lun_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
    ">Luna leaves your office."
    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    hide screen g_c_u
    show screen genie
    hide screen chair_left
    hide screen desk

    jump luna_away


label luna_cum_addict_event:
    $ luna_addicted = True #luna is now a cum addict. I'm a bit undecided about the whole thing tbh, might ruin the dom path but idk, we can work it in, make her a dommy cumslut or whatever........
    ">You put your arms on Luna's shoulders forcing her to her knees."
    $ luna_l_arm = 2
    $ luna_r_arm = 2
    $ genie_base = "characters/genie/base/hard.png"
    call gen_main("Down we go!","grin")
    $ luna_ypos = 225
    $ luna_xpos = 350
    call lun_main("Stop right now! This wasn't an option [lun_genie_name]!","open","wide","mad","mid")
    g4 "Argh, too late slut!"
    call lun_main("!!!","upset","closed","mad","mid")
    $ luna_cum = 11
    call cum_block

    $ luna_wear_cum = True
    ">You coat Luna's furious expression in a wave of hot cum!"
    pause
    g4 "Argh! by the gods {size=+10}YES!{/size}"
    call lun_main("...","normal","seductive","base","crossed")
    call lun_main("(What's this smell?)","pout","seductive","sad","downL")
    g4 "{size=+10}TAKE IT ALL YOU big titted SLUT!{/size}"
    g4 "mmmm....."
    hide screen g_c_c_u
    $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
    $ luna_r_arm = 2
    hide screen genie_main
    $ genie_base = "characters/genie/base/open.png"
    with d3
    m "That hit the spot..."
    call lun_main("...","pout","mad","mad","L")
    call lun_main("......","normal","angry","angry","downL")
    call lun_main(".........","base","seductive","sad","empty")
    m "Ahh... that was fantastic slut..."
    $ g_c_u_pic = "characters/genie/chibis/masturbating/b_01.png"
    call lun_main("What {size=+4}is {size=+4}this {size=+4}smell?{/size}","base","wide","sad","mid")
    m "Cum?"
    ">Luna gets up from her knees"
    $ luna_ypos = 0
    call lun_main("{size=+4}it{/size}","upset","suspicious","mad","L")
    call lun_main("{size=+8}smells{/size}","normal","mad","angry","downL")
    call lun_main("{size=+12}incredible!!!{/size}","base","wide","sad","empty")
    m "..."
    m "What?"
    call lun_main("My god!!! there's so much magical energy in it!","base","wide","sad","mid")
    call lun_main("I've never sensed anything this powerful before!","base","wide","sad","down")
    m "Ah yes, well I am the great fumblemore!"
    call lun_main("...","pout","angry","angry","mid")
    call lun_main("This smell... it's too much for any mortal to make...","base","angry","base","mid")
    m "(Shit...)"
    call lun_main("Can I...","normal","base","sad","mid")
    call lun_main("Taste it?","normal","seductive","sad","R")
    m "What sort of question is that?"
    call lun_main("If it's too much...","normal","wide","sad","mid")
    g9 "Of course you can taste my cum girl!"
    call lun_main("Thank you, sir...","base","wide","sad","mid")
    m "(She seems different...)"
    $ luna_cum = 12
    ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","full","seductive","sad","empty")
    call lun_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}","base","happyCl","sad","mid")
    call lun_main("Can I have the rest? Please sir?","base","wide","sad","mid")
    m "Sure..."
    ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
    $ luna_cum = 13
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    pause
    $ luna_cum = 14
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    $ luna_cum = 15
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    $ luna_wear_cum = False
    call lun_main("Ah...","base","happyCl","sad","mid")
    call lun_main("Amazing...","base","seductive","sad","mid")
    m "Enjoyed yourself did we?"
    call lun_main("How could I not?","pout","angry","angry","R")
    m "(What is going on here? She seems all bitchy again...)"
    call lun_main("You have to tell me how you did that!","normal","mad","angry","mid")
    m "Cum? I'm pretty sure you've got that all worked out..."
    call lun_main("Not that, idiot!","normal","suspicious","mad","mid")
    call lun_main("Why did it contain so much magical energy?","normal","angry","angry","mid")
    call lun_main("We lovegoods are sensitive to magic, but the only thing I've ever experienced like this was when I was allowed in the same room as some essence of Djinn...","pout","angry","mad","R")
    call lun_main("But everyone knows the Djinn were hunted to extinction millenia ago...","normal","mad","angry","mid")
    g4 "(!!!)"
    m "Oh,{w=0.3} um..."
    m "Trade secret..."
    call lun_main("Fine! Be that way then [lun_genie_name]...","pout","suspicious","angry","R")
    ">Luna gets dressed in front of you in a huff."

    call load_luna_clothing_saves

    call lun_main("Just don't expect me to let you get away with wasting that spunk anymore [lun_genie_name]!","normal","mad","angry","mid")

    m "Anyway, here's your payment, [lun_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")

    jump luna_away #DONE
