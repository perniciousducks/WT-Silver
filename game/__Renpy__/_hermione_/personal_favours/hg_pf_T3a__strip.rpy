

### Hermione Dance ###

label hg_pf_strip:

    if hg_pf_strip.counter < 1:
        m "{size=-4}(Ask her to dance for me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu


    # Start Event
    $ temp_top = h_top # Save
    $ current_payout = 35
    $ hg_pf_strip.start()


    # End Event
    label end_hg_pf_strip:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ h_top = temp_top # Load
    $ temp_save = aftersperm # Save

    call reset_hermione
    $ aftersperm = temp_save # Load

    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen s_c_c_u # Snape's sperm. Universal.

    call sna_chibi("hide")
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans="fade")
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")


    # Points
    m "[current_payout] to the \"Gryffindor\" house."
    call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    if her_tier == 4:
        if her_whoring < 18: # Points til 18
            $ her_whoring += 1

    jump end_hermione_event



### Fail Events ###

label hg_pf_strip_fail:
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...", "soft", "wide", "base", "stare")

    call her_main("...dance for you, [genie_name]?", "open", "wide", "base", "stare")

    $ hg_pf_strip.counter -= 1

    jump too_much


label hg_pf_strip_T0_fail_intro: # Hermione starts dancing, but it will fail anyway.
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...","open","worried")
    call her_main("...dance for you, [genie_name]?", "open", "wink", "base", "mid")
    m "Yes... You think you could manage that?"
    call her_main("Ehm... I suppose so...", "soft", "base", "base", "R")
    her "Am I getting paid for this?"
    m "Of course, [hermione_name]!"
    call her_main("So... Just a little dancing then...","annoyed","worriedL")
    m "Whenever you're ready..."
    her "................."
    hide screen hermione_main
    with d3

    call nar(">Hermione starts dancing...")

    stop music fadeout 1.0
    hide screen bld1
    call her_chibi("dance","mid","base")
    with d3
    pause.2

    m "Hm..."
    call her_main("{size=-5}(...........................................){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    call her_main("{size=-5}(This is silly...){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call nar(">Hermione looks embarrassed but she keeps on \"dancing\"...")
    m "..................."
    call her_main("{size=-5}(...........................................){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Alright, you can start undressing now."

    call her_chibi("stand","mid","base") #Hermione stands still.
    with hpunch

    show screen blktone
    call her_main("??!", "mad", "wide", "base", "stare", cheeks="blush")
    m "Take off those clothes..."
    call her_main("You want me to...?", "disgust", "narrow", "base", "down", cheeks="blush")

    hide screen blktone
    call her_main("[genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")
    call her_main("This is ridiculous on a whole other level!", "angry", "closed", "angry", "mid", cheeks="blush")
    call her_main("I won't let myself be forced to become some cheap stripper!!!", "mad", "wide", "base", "stare", cheeks="blush")
    m "Nobody is forcing you to do this."
    m "If you don't need the points, please feel free to leave."
    call her_main("Yes. I believe you're right Sir.", "soft", "closed", "angry", "mid")
    call her_main("Stripping for you won't be worth \"any\" amount of points!", "angry", "base", "angry", "mid")
    call her_main("I will be leaving now!", "annoyed", "base", "angry", "mid")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 5
    $ hg_pf_strip.counter -= 1

    jump end_hermione_event


label hg_pf_strip_T0_fail_repeat:
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("And would you like me to take off my clothes as well?", "soft", "closed", "base", "mid")
    m "Yes?"
    call her_main("No! I will not!", "scream", "base", "angry", "mid")
    call her_main("And I'd appreciate it if you'd stop making such outrageous requests...", "annoyed", "base", "angry", "mid")
    m "You will get points for it..."
    call her_main("Shove those points up your-", "angry", "closed", "angry", "mid")
    call her_main("I will be leaving now...", "annoyed", "base", "angry", "mid")
    call her_main("Good day, Sir...", "annoyed", "narrow", "angry", "R")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 5
    $ hg_pf_strip.counter -= 1

    jump end_hermione_event



### Tier 1 ###

# Event 1 (i) - Hermione tries to stip for you but fails.
# Event 2 (i) - Hermione strips for you on your desk. Snape then enters.
# Event 3 (r) - Hermione strips for. You will get some event choices.

label hg_pf_strip_T1_intro_E1: # Complete
    call bld
    m "[hermione_name], I need you to dance for me a little."
    call her_main("You want me to...","open","worried")
    call her_main("...dance for you, [genie_name]?", "open", "wink", "base", "mid")
    m "Yes... You think you could manage that?"
    call her_main("Ehm... I suppose so...", "soft", "base", "base", "R")
    her "Am I getting paid for this?"
    m "Of course, [hermione_name]!"
    call her_main("So... Just a little dancing then...","annoyed","worriedL")
    m "Whenever you're ready..."
    her "................."
    hide screen hermione_main
    with d3

    call nar(">Hermione starts dancing...","start")

    stop music fadeout 1.0
    hide screen bld1
    call her_chibi("dance","mid","base")
    with d3
    pause.2

    m "Hm..."
    call her_main("{size=-5}(...........................................){/size}", "disgust", "narrow", "base", "down", cheeks="blush", ypos="head")
    call her_main("{size=-5}(This is silly...){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    call nar(">Hermione looks embarrassed but she keeps on \"dancing\"...")
    m "..................."
    call her_main("{size=-5}(...........................................){/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
    m "Alright, you can start undressing now."

    call her_chibi("stand","mid","base") #Hermione stands still.
    with hpunch

    call her_main("??!", "mad", "wide", "base", "stare", cheeks="blush")
    call her_main("I thought all I had to do was dance?", "angry", "base", "angry", "mid")
    call play_music("playful_tension") # SEX THEME.
    m "Really? That's adorable."
    m "Now start taking off those clothes."

    show screen blktone
    call her_main("You want me to... strip for you...?", "disgust", "narrow", "base", "down", cheeks="blush")
    m "Yes. And I expect you to do it today, [hermione_name]."
    call her_main("[genie_name]!","angry","worriedCl", cheeks="blush")
    m "Don't you raise your voice at me, [hermione_name]!"
    call her_main(".....!!?", "mad", "wide", "base", "stare", cheeks="blush")
    m "Nobody is forcing you to do this."
    m "I am doing you a favour!"
    m "If you don't need the points, please feel free to leave."
    call her_main(".....................", "angry", "base", "angry", "mid")
    call her_main(".......................................", "disgust", "narrow", "base", "down", cheeks="blush")

    hide screen blktone
    call nar(">Hermione is starting to dance again...")

    call her_chibi("dance","mid","base")
    with d5

    call her_main("{size=-5}(...........................................){/size}","angry","worriedCl", cheeks="blush")
    m "What are you waiting for then?"

    if hermione_wear_top and (h_top == "top_1" or h_top == "top_6"):
        m "Start with the vest."
        call her_main(".............................................................", "disgust", "narrow", "base", "down", cheeks="blush")
        call nar(">Hermione gives you a confused look and then takes off her vest...")
    else:
        call nar(">Hermione gives you a confused look...")


    if hermione_wear_top and (h_top == "top_1" or h_top == "top_6"):
        if h_top == "top_1":
            $ h_top = "top_2"
        else:
            $ h_top = "top_4"
        call update_her_uniform

    pause.5
    show screen blktone
    call her_main("{size=-5}(Am I really going to do this?){/size}","angry","worriedCl", cheeks="blush", xpos="base", ypos="base", trans="fade")
    hide screen blktone
    call ctc

    menu:
        m "......................."
        "\"Now get rid of your skirt!\"":
            call her_main(".................................","angry","worriedCl", cheeks="blush")
            call nar(">Hermione starts to unzip her skirt...","start")
            ">She seems very hesitant and takes her time..."
            call nar(">Finally the zipper is undone and she has no choice but to take the skirt off...","end")

            call her_main("{size=-5}(Here it comes then...){/size}","angry","worriedCl", cheeks="blush")
            call her_main("{size=-5}(For the honour of \"Gryffindor\"....){/size}","angry","worriedCl", cheeks="blush")

            call nar(">Hermione takes off her skirt...")
            pause.2

            $ hermione_wear_panties = True
            call set_her_action("lift_skirt")
            pause.5

            $ hermione_wear_bottom = False
            call set_her_action("None")
            pause.5

            m "..............."
            call her_main("{size=-5}(.........................................){/size}","angry","worriedCl", cheeks="blush")
            call nar(">Hermione keeps on dancing...")
            m "Alright, your shirt is next!"
            call her_main("My shirt....?", "disgust", "narrow", "worried", "down", cheeks="blush")
            hide screen hermione_main
            with d3

            call nar(">Hermione looks extremely embarrassed...","start")
            call nar(">She clumsily fumbles with the buttons of her shirt...","end")

        "\"Now take off your shirt!\"":
            call her_main(".................................","angry","worriedCl", cheeks="blush")
            call nar(">Hermione starts to unbutton her shirt...","start")
            ">She seems very hesitant and takes her time..."
            call nar(">Finally the last button is undone and she has no choice but to take the shirt off...","end")

            call her_main("{size=-5}(Alright, here it comes...){/size}","angry","worriedCl", cheeks="blush")
            call her_main("{size=-5}(For the honour of the \"Gryffindor\"!){/size}","angry","worriedCl", cheeks="blush")

            call nar(">Hermione takes off her shirt...")
            pause.2

            call set_her_action("lift_top")
            pause.5

            $ hermione_wear_top = False
            call set_her_action("None")
            pause.5

            call her_main("{size=-5}(I actually did it...){/size}","angry","worriedCl", cheeks="blush")
            call her_main("{size=-5}([genie_name] can see my breasts while I'm dancing for him...){/size}","angry","worriedCl", cheeks="blush")
            call her_main("{size=-5}(This is so demeaning...){/size}","angry","worriedCl", cheeks="blush")
            call her_main("{size=-5}(But I am doing this for my house...){/size}","angry","worriedCl", cheeks="blush")

            m "Not bad...."
            call her_main("{size=-5}(.........................................){/size}","angry","worriedCl", cheeks="blush")

            call nar(">Hermione is topless now...","start")
            ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
            call nar(">It seems like she's desperately trying to prevent her breasts from bouncing or swaying...","end")

            m "Alright, your skirt is next!"
            call her_main("....................","angry","worriedCl", cheeks="blush")
            hide screen hermione_main
            with d3

            call nar(">Hermione looks extremely embarrassed...","start")
            call nar(">She fumbles with the zipper of her skirt...","end")

    stop music fadeout 1.0
    m "What's the problem, [hermione_name]?"
    call play_music("sad") # HERMIONE'S THEME.

    call her_main("I'm sorry, [genie_name]...","angry","worriedCl", cheeks="blush")
    call her_main("It's stuck...","angry","worriedCl", cheeks="blush")
    call her_main("It won't budge...","angry","worriedCl", cheeks="blush")
    call her_main("Why won't it budge?! *sob*","angry","worriedCl", cheeks="blush")
    call her_main("No, I can't do this, [genie_name]! *sob*","open","surprised", cheeks="blush", tears="messy")
    m "What?"
    call her_main("I thought I could, but...","angry","suspicious", cheeks="blush", trans="fade")
    call her_main("Stripping for points, [genie_name]?","angry","suspicious", cheeks="blush")
    call her_main("People look up to me in this school!","angry","suspicious", cheeks="blush")
    call her_main("I have a reputation...*sob*","angry","suspicious", cheeks="blush")
    call her_main("And If I do this...", "scream", "base", "angry", "mid", cheeks="blush", tears="messy")
    show screen blkfade
    with d5

    ">Hermione quickly puts her uniform back on..."

    call set_her_action("None","update")
    call her_chibi("stand","desk","base")

    hide screen blkfade
    call her_main("[genie_name], I think I'd better go now... *Sob!*","angry","suspicious", cheeks="blush", tears="messy", trans="fade")

    menu:
        "\"Alright. I had fun. Here are your points.\"":
            call her_main("Really? I didn't ruin it completely then?", "soft", "base", "base", "R", tears="soft")

            jump end_hg_pf_strip

        "\"Sure. You will receive no points though.\"":
            call her_main("[genie_name]... I may not be very good at this...", "open", "base", "base", "mid", tears="mascara_crying")
            call her_main("But I did my best... I think I deserve some--", tears="mascara_crying")
            m "Just make sure you try harder next time, [hermione_name]."
            call her_main("Next time?!", "open", "base", "base", "mid", tears="mascara_crying")
            call her_main("I assure you, [genie_name], there will be no next time...", "angry", "base", "angry", "mid", cheeks="blush", tears="mascara")
            m "We'll see..."
            call her_main("Tsk!", "disgust", "narrow", "base", "mid_soft", tears="mascara")

            call her_walk(action="leave", speed=2.5)

            # Event does not fail. She jsut gets mad, but no whoring increase.
            $ her_mood += 25

            jump end_hermione_event



label hg_pf_strip_T1_intro_E2:
    call bld
    m "[hermione_name], I need you to dance for me."
    call her_main("That again, [genie_name]...?", "disgust", "narrow", "base", "mid_soft")
    m "You will get paid accordingly of course..."
    call her_main("............................", "annoyed", "narrow", "angry", "R")
    call her_main("And you expect me to... ehm...", "annoyed", "narrow", "angry", "R")
    m "Take your clothes off. Naturally."
    stop music fadeout 1.0

    show screen blktone
    call her_main("......................", "annoyed", "narrow", "angry", "R")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Well, why not?", "disgust", "narrow", "base", "mid_soft")
    call her_main("Yes, I don't see why not!", "scream", "base", "angry", "mid", emote="01")
    m "Hm...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
    call her_main("After all, as a pupil I am meant to obey your every order, isn't that right, [genie_name]?!", "scream", "closed", "angry", "mid")
    m "...................."
    call her_main("If the Headmaster tells me to strip for him, Then I shall strip!!!", "scream", "closed", "angry", "mid")
    call her_main("Do I find this extremely inappropriate, disgraceful and humiliating?", "angry", "base", "angry", "mid")
    call her_main("Of course not. What nonsense!", "scream", "closed", "angry", "mid")
    m ".............."
    call her_main("Ha! Might as well do this the proper way!", "angry", "base", "angry", "mid")

    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3
    pause.2

    m "??!"

    call chibi_walk_desk_blkfade("hermione")

    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
    pause 3
    g4 "!!!!!!"
    ">To your surprise Hermione just hops onto your desk and starts dancing franticly..."

    call her_chibi("dance","on_desk","on_desk")

    hide screen blkfade
    with fade
    pause.5

    call her_main("If I must degrade myself in order to protect the honour of my house...", "scream", "closed", "angry", "mid", xpos="mid", ypos="base")

    if hermione_wear_top and (h_top == "top_1" or h_top == "top_6"):
        call nar(">Hermione is starting to take off her vest...")
    elif hermione_wear_top:
        call nar(">Hermione is starting to take off her top...")

    call her_main("So be it then!", "scream", "base", "angry", "mid", emote="01")
    call her_main("Just...", "open", "narrow", "worried", "down")
    call her_main("*groan*", "clench", "narrow", "base", "down")

    if hermione_wear_top and (h_top == "top_1" or h_top == "top_6"):
        call nar(">Her vest seems to be stuck somehow, but the girl keeps pulling on at the fabric with anger...")
        call her_main("Why won't it....?!")
        call her_main("There!", "annoyed", "narrow", "annoyed", "mid")
        call nar(">Hermione finally manages to untangle herself and sends the vest flying to the other side of the room...")

        if h_top == "top_1":
            $ h_top = "top_2"
        else:
            $ h_top = "top_4"
        call update_her_uniform
        pause.2

        call her_main()
        pause.1

    else:
        call nar(">The girl seems to contemplate about which piece of clothing she should take off first...")
        pause.1

    call her_main("The skirt is next, right?", "scream", "closed", "angry", "mid")

    menu:
        m "..."
        "\"Yes, that's right. Take it off!\"":
            call her_main("Of course!")
            call her_main("Here it goes!", "open", "narrow", "worried", "down")
            pause.1
        "\"You need to calm down, [hermione_name]. \"":
            call her_main("Well, {size=+7}EXCUSE ME{/size}, [genie_name]!")
            call her_main("You told me to strip for you, but you never told me your preferences in regards to the pace!")
            m "Well, I'm telling you now, [hermione_name]!"
            call her_main("Too late!", "angry", "base", "angry", "mid")
            pause.1

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")
    pause.5

    $ hermione_wear_bottom = False
    call set_her_action("None")
    pause.2

    call nar(">Hermione sends her skirt flying across the room, just like she did with her vest a moment earlier...")

    m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
    m "{size=-4}(Maybe it was still too early to--{/size}"
    call her_main("My shirt?!!", "disgust", "narrow", "base", "mid_soft")

    $ hermione_wear_bra = True
    call set_her_action("lift_top")
    pause.2

    call her_main("{size=+9}I don't need it!{/size}", "scream", "base", "angry", "mid", emote="01")
    pause.2

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.2

    call nar(">Hermione's shirt suddenly hits the floor.")
    call her_main("", "angry", "base", "angry", "mid")
    pause.2
    g4 "{size=-4}(When did she??!){/size}"
    call ctc

    call her_main("Do you enjoy this, [genie_name]?")
    call her_main("", "angry", "base", "angry", "mid")

    call set_her_action("lift_breasts")

    call her_main("Shall I shake my breasts for you like one of those harlots?", "scream", "closed", "angry", "mid")
    m "Well---"
    call her_main("Of course! Why wouldn't I degrade myself for your pleasure?!")
    call her_main("This is completely {size=+7}acceptable!{/size}", "scream", "base", "angry", "mid", emote="01")
    call her_main("", "angry", "base", "angry", "mid")

    call set_her_action("None")
    pause.2

    call nar(">Hermione is starting to shake her naked breasts rather clumsily...","start")
    call nar(">As you watch the girl's tits sway right and left before your face you find yourself fighting the urge to...","end")

    menu:
        m "..."
        "-Grab them!-":
            g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
            g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "disgust", "wide", "base", "stare")
            pause.2
            call slap_her #Calls slapping sound and visual.
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

        "-Slap them!-":
            m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "disgust", "wide", "base", "stare")
            pause.2
            g9 "{size=-4}(Yes, just slap them around a little...){/size}"
            call slap_her #Calls slapping sound and visual.
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

        "-Bite on them!":
            m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
            m "{size=-4}(No, it's not weird!){/size}"
            m "{size=-4}(Just a couple of gentle love-bites!){/size}"
            call kiss_her
            call her_main("", "shock", "wide", "base", "stare", tears="soft")
            pause.2
            g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
            call her_main("","disgust","worriedCl", tears="soft_blink")
            pause.2
            call kiss_her
            call kiss_her
            pause.2

        "-Motorboat them!-":
            m "{size=-4}(I'm going to put my face right in between them!){/size}"
            call kiss_her
            call her_main("","shock","worriedCl")
            pause.2
            g9 "{size=-4}(Yes, motorboating these titties is be the best!){/size}"
            call her_main("", "shock", "wide", "worried", "shocked")
            pause.2

    call nar(">While you are having fun with her tits, Hermione keeps on dancing...","start")

    call her_main("(Dancing naked in front of the headmaster...)", "soft", "wide", "worried", "shocked")
    call her_main("(Letting him touch my breasts...)", "disgust", "wide", "worried", "shocked")
    call her_main("(If my parents knew about this they would lose their minds...)", "soft", "wide", "worried", "shocked")
    call her_main("(Especially my father...)", "annoyed", "closed", "base", "mid")
    ">Hermione is starting to shake her tits again..."
    call her_main("(Hermione Granger - the stripper...)")
    call her_main("(Forgive me father...)", "annoyed", "narrow", "base", "dead")

    ">Hermione puts her hands on her tits and starts squeezing them..."
    ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
    call her_main("(I used to be a top student... Used to have standards...)")
    ">Hermione clutches her tits even harder and then gives them a couple of twists..."
    ">It almost looks as if she is mad at her own breasts and trying to punish them..."

    call nar(">You find the thought strangely arousing...","end")

    call her_chibi("image","on_desk","on_desk","dance/05_panties_01")
    call ctc

    call her_main("Well, I hope you enjoyed yourself, [genie_name]!", "open", "narrow", "annoyed", "mid")
    m "What?"
    call her_main("I would like to get paid now...", "open", "closed", "angry", "mid")
    m "Aren't you forgetting something, [hermione_name]?"
    call her_main("[genie_name]...?", "open", "narrow", "annoyed", "mid")
    m "Your panties...?"
    call her_main("My panties?", "open", "wide", "base", "stare")
    call her_main("But, they always leave them on!")
    m "Who exactly are \"they\"?"
    m "Strippers in kid's cartoons?"
    m "Stripping is stripping, [hermione_name]!"
    m "Now take off your panties!"
    call her_main("................", "angry", "wide", "base", "stare")

    call nar(">Hermione looks horror-struck. All of her anger is gone...","start")
    call her_main(".................", "annoyed", "closed", "base", "mid")
    ">Without saying another word..."
    call nar(">She starts to pull down her panties...","end")

    $ hermione_wear_panties = False
    call update_her_uniform
    call her_chibi("image","on_desk","on_desk","dance/07_dance_01")
    call her_main("","annoyed","worriedCl", cheeks="blush")
    pause.2

    g9 "......................................."

    hide screen blktone
    hide screen bld1
    hide screen hermione_main
    with d1

    stop music

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call sna_main("Listen, Genie. I've been thinki-","snape_01", xpos="base", ypos="base")

    show screen hermione_main
    with d3

    $ renpy.play('sounds/scratch.wav')
    with hpunch

    call sna_main("............................................","snape_11")
    with hpunch

    call her_main("(Professor Snape???????!)", "angry", "wide", "base", "stare")
    call sna_main("Miss Granger?","snape_12")

    call set_her_action("covering")
    call her_main("(No, no... This is not happening. Please...)","shock","worriedCl", cheeks="blush", trans="d5")
    call play_music("playful_tension") # SEX THEME.
    m "...................................."

    menu:
        m "..."
        "\"Severus, I am busy right now.\"":
            call sna_main("Yes... I can see that...","snape_13")
            call her_main("{size=-7}(I want to die!){/size}","angry","worriedCl")

        "\"Severus! Please, come join us.\"":
            $ her_mood += 20
            call sna_main("Seriously?","snape_14")
            call her_main("([genie_name], no, please.............................)","angry","worriedCl")
            call sna_main("A very tempting offer indeed...","snape_13")
            call her_main("!!!!!!.......", "angry", "wide", "base", "stare")
            call sna_main("Well, maybe some other time...","snape_13")
            call her_main("{size=-5}(There will be no other time!){/size}","angry","worriedCl")
            call her_main("{size=-5}(I will stop selling favours from now on, I swear!){/size}")

    call sna_main("I shall postpone our conversation then, Geni-- *khem!* Albus.","snape_12")
    call sna_main("Miss Granger...","snape_13")
    call her_main(".................................","angry","worriedCl")

    call hide_characters
    hide screen bld1
    with fade
    pause.2

    call sna_walk(action="leave", speed=3)

    show screen blkfade
    with d5

    ">Hermione hastily hops off your desk."
    ">She starts putting her clothes back on rather frantically..."

    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d5

    call her_main("My shirt! Where is my shirt?!","scream","worriedCl", xpos="mid", ypos="base")
    m "It's over there, by the fireplace..."

    hide screen hermione_main
    with d3
    pause.2

    call her_walk(xpos="mid", ypos="base", speed=1.5)

    call her_main("................................", "disgust", "narrow", "base", "down", ypos="head")
    pause.2

    # Reset Hermione
    $ h_top = temp_top # Load
    call reset_hermione

    call her_chibi("stand","mid","base", flip=True)
    pause.2

    call her_walk(xpos="desk", ypos="base", speed=2)

    call her_main("........................","normal","worriedCl", xpos="base", ypos="base")
    stop music fadeout 2.0
    call her_main("Can I just get my points now, please?","angry","worriedCl", emote="05")
    pause.5

    if hg_strip.trigger == False:
        $ achievement.unlock("herstrip")
        $ hg_pf_strip.change_icon(a="heart_yellow", b="heart_red")
    $ hg_strip.triggered() # .trigger = True, .counter += 1
    $ hg_pf_strip.title = "Strip for Me!"

    jump end_hg_pf_strip



label hg_pf_strip_T1_E2:
    m "[hermione_name], how about another strip?"
    call her_main("..............", "disgust", "narrow", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [genie_name]..."
    m "Why? You are getting quite good at it."
    call her_main(".........................", "annoyed", "narrow", "annoyed", "mid")
    call her_main("Thirty five house points?", "open", "narrow", "worried", "down")
    m "Sure! The usual rate."
    call her_main("...................", "annoyed", "narrow", "angry", "R")

    if ss_he.hermione_strip: #Turns TRUE after Dance Event 2 and the next Date with Snape.
        m "(Hm... Should I invite Snape to watch as well?)"

        menu:
            "-\"Yes! Hermione needs an audience!\"-":
                jump hg_pf_strip_T1_Snape

            "-\"Nah... That's not a good idea...\"-":
                pass

    # Locks Door.
    call hide_characters
    hide screen bld1
    with d3
    pause.5

    call her_walk(xpos="door", ypos="base", speed=2)

    pause.2
    call chibi_effect("thought", "hermione")
    pause.5
    call play_sound("lock")
    call chibi_effect("hide")
    pause.2

    m "??!"
    pause.2


    # Walks back.
    call her_chibi("stand","door","base")
    pause.1

    call her_walk(xpos="mid", ypos="base", speed=3)
    pause.2

    call her_main("Just in case...", "annoyed", "narrow", "angry", "R", ypos="head")
    stop music fadeout 1.0

    call her_walk(xpos="desk", ypos="base", speed=3, redux_pause=2, loiter=False)

    show screen blkfade
    with d5
    pause.5

    call play_sound("climb_desk")
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    call her_main("Just for the record...", "open", "closed", "base", "mid", xpos="mid", ypos="base")
    call her_main("I still consider this a highly inappropriate favour to be buying from one of your students, [genie_name].","annoyed","suspicious")
    m "Right. And an equally inappropriate favour to be selling to your headmaster. Wouldn't you agree?"
    call her_main("..........", "annoyed", "narrow", "angry", "R")


    # Talk off top
    call nar(">Hermione undoes the last button of her shirt...")
    $ hermione_wear_bra = False
    call set_her_action("lift_top")
    pause.5

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.2

    call nar(">And takes it off somewhat clumsily...")
    call ctc

    g9 "Yes! The tits!"

    call play_music("playful_tension") # SEX THEME.
    call her_main("..............", "open", "narrow", "worried", "down")
    call her_main("What if my parents were to find out about this, [genie_name]?", "disgust", "narrow", "base", "down")
    call her_main("Mother would never understand...")
    call her_main("As for my father...", "upset", "wink", "base", "mid")

    menu:
        m "..."
        "{size=-3}\"Your father would be proud of you!\"{/size}":
            call her_main("I doubt it...")
            call her_main("Yes, I am doing this for the right reasons, but...")
            call her_main("He would never see it that way...", "annoyed", "base", "angry", "mid")
            call her_main("He must never know about this...")

        "{size=-3}\"Your father would spank you hard!\"{/size}":
            call her_main("He would not!", "shock", "wide", "base", "stare")
            call her_main("And I am too old for that any way...", "upset", "wink", "base", "mid")
            g9 "I would say that you are in the perfect age for that..."
            call her_main("Huh?")
            call her_main("I do not know what you mean, [genie_name].","grin","worriedCl", emote="05")

        "{size=-3}\"Your father would disown you!\"{/size}":
            call her_main("You are probably right, [genie_name]...","angry","worriedCl", emote="05")
            call her_main("(Oh father, I am so sorry...)", "angry", "base", "base", "mid", tears="soft")
            call her_main("he must never find out...", "angry", "base", "base", "mid", tears="soft")

        "{size=-3}\"Your father would love to watch you strip!\"{/size}":
            call her_main("He would not! He would be ashamed of me!","normal","worriedCl")
            m "Are you sure about that?"
            call her_main("absolutely! My father is a man of integrity!","scream","worriedCl")
            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
            call her_main(".....................", "annoyed", "narrow", "annoyed", "mid")
            call her_main("My father must never know about this...","annoyed","worriedL")


    # Take off skirt
    call nar(">Hermione is starting to sway her hips rather seductively...")

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")
    pause.5

    $ hermione_wear_bottom = False
    call set_her_action("None")
    pause.2

    call nar(">While she slides her skirt down...")
    call ctc

    menu:
        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T1_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T1_watch



label hg_pf_strip_T1_watch:
    call nar(">You watch Hermione Dance...")
    call her_main("(Time for the finishing act I suppose...)","angry","worriedCl", xpos="mid", ypos="base")

    if hermione_wear_panties:
        m "Yes, [hermione_name]! Take them off!"
        call her_main("........", "annoyed", "closed", "base", "mid")

        $ hermione_wear_panties = False
        call set_her_action("pinch")
        pause.5

        call set_her_action("None")
        pause.2

        call nar(">Hermione bends over slightly and slides her panties down...")

    call nar(">You can see that she is doing her best to not fall off the desk...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
    call ctc

    call her_main("..........","disgust","worriedCl")
    call nar(">Hermione performs another set of rather awkward movements...","start")
    call nar(">if not for her naked tits bouncing all over the place this would be quite embarrassing...","end")

    g9 "................."
    call nar(">A few more clumsy movements before Hermione slumps on her butt...")

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call her_main("I'm sorry, Sir. Was this good enough?...", "disgust", "narrow", "base", "down", emote="05", ypos="head")

    menu:
        m "..."
        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
            m "Good job [hermione_name]!"
            call her_main("..............", "disgust", "narrow", "worried", "down")
            m "You have a lot of talent for this!"
            call her_main("Thank you [genie_name].","soft","worriedL", emote="05")
        "{size=-3}\"Hm... This was quite awful...\"{/size}":
            $ her_mood += 4
            call her_main("............", "annoyed", "base", "angry", "mid")
            m "You just need to practice more..."
            call her_main("Whatever..........", "annoyed", "narrow", "angry", "R")
        "{size=-3}\".................................................\"{/size}":
            call her_main(".......................","silly","worriedCl", emote="05")
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

    hide screen bld1
    call ctc

    jump end_hg_pf_strip



label hg_pf_strip_T1_masturbate:
    show screen blkfade
    with d5

    call her_main("[genie_name]?!", "open", "wide", "base", "stare", ypos="head")
    m "It's alright, [hermione_name]. Don't mind me..."

    show screen chair_left
    call gen_chibi("jerking_off","behind_desk","behind_desk")
    show screen desk
    call her_chibi("dance","on_desk","on_desk")
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call bld
    call her_main("B-but...", "angry", "wide", "base", "stare", ypos="head")
    call her_main("Your...")
    m "Yes... Ah, yes, this is good..."
    call her_main("[genie_name]!!!","scream","worriedCl")
    call her_main("I must insist that you put away your...","angry","worriedCl")
    call her_main("...thing.")

    menu:
        m "..."
        "\"I said, keep on dancing, [hermione_name]!\"":
            stop music fadeout 1.0

            call her_main("No, [genie_name]!", "annoyed", "narrow", "angry", "R", ypos="head")
            m "Huh?"
            show screen blkfade
            with d5

            ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
            m "Oh, come on! Don't leave me like that!"

            call hg_chibi_transition("stand","desk","base", flip=False, trans="fade")

            call reset_hermione
            call her_main("The dance is over, [genie_name]!", "soft", "base", "angry", "mid")
            pause 1
            call her_main("I would like to get paid now!", "annoyed", "narrow", "annoyed", "mid")
            m "Stubborn [hermione_name]..."
            call nar(">You reluctantly put your cock away...")
            call her_main("I would like to get paid now.", "annoyed", "narrow", "annoyed", "mid")

            $ her_mood += 6

            jump end_hg_pf_strip

        "\"Fine. There is no need for drama!\"":
            call her_main("......................", "annoyed", "narrow", "angry", "R", ypos="head")
            pause.1

            hide screen chair_left
            hide screen g_c_u
            hide screen desk
            call gen_chibi("hide")
            show screen genie
            call her_chibi("dance","on_desk","on_desk")
            hide screen blktone
            hide screen bld1
            with fade
            pause.5

            jump hg_pf_strip_T1_watch



### Tier 2 ###


# Event 1 (i) - Hermione tries her best at stripping.
# Event 2 (i) -
# Event 3 (r) -

label hg_pf_strip_T2_intro_E1:
    m "[hermione_name], how about another strip?"
    call her_main("..............", "disgust", "narrow", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [genie_name]..."
    m "Why? You are getting quite good at it."
    call her_main(".........................", "annoyed", "narrow", "annoyed", "mid")
    call her_main("Thirty five house points?", "open", "base", "base", "mid")
    g9 "Sure!"
    call her_main("Very well, then...", "base", "base", "base", "R")

    jump hg_pf_strip_T2



label hg_pf_strip_T2_intro_E2:
    m "[hermione_name], would you like to provide me with about another strip show?"
    m "(I'm bored as fuck in here after all...)"
    call her_main("*Hmm*...", "annoyed", "base", "base", "R", xpos="base", ypos="base")
    call her_main("Sure! Why not...", "base", "happyCl", "base", "mid")
    g9 "Yes?"
    call her_main("I've been practising a bit more. Mainly just my dancing.", "soft", "narrow", "worried", "down")
    m "Very good. I'd love to see your progress."
    call her_main("Of course, [genie_name]...", "base", "narrow", "base", "mid_soft")

    jump hg_pf_strip_T2



label hg_pf_strip_T2_E2:
    m "[hermione_name], would you like to strip for me again?"
    if her_tier <= 5:
        call her_main("Of course, [genie_name]...", "base", "base", "base", "mid", xpos="base", ypos="base")
    else:
        call her_main("I'd love to, [genie_name]!", "open_tongue", "narrow", "annoyed", "up", xpos="base", ypos="base")

    jump hg_pf_strip_T2



label hg_pf_strip_T2:
    menu:
        m "(...)"
        "-Invite Snape to watch!-" if ss_he.hermione_strip:
            jump hg_pf_strip_T2_Snape

        "-Ask her to lock the door.-":
            $ lock_door = True
            pass

        "-Tell her to leave the door open...-":
            $ lock_door = False
            pass


    if lock_door: # Locks door.

        if her_tier <= 5:
            call her_main("Of course...", "base", "base", "base", "mid")
        else:
            call her_main("(How boring...)", "annoyed", "narrow", "annoyed", "up")

        call hide_characters
        hide screen bld1
        with d3
        pause.5

        call her_walk(xpos="door", ypos="base", speed=1.6)

        pause.5
        call play_sound("lock")

        # Walks back.
        call her_chibi("stand","door","base")
        pause.1

        call her_walk(xpos="mid", ypos="base", speed=2.5)
        pause.2

        call her_main("All done!", "smile", "closed", "base", "mid", ypos="head")

        pass

    else: # Leave door open.

        if her_tier <= 4:
            call her_main("But, what if somebody walks in again!", "shock", "wide", "base", "stare")
            m "Nonsense. No such thing will happen..."
            call her_main("It happened once already!", "angry", "base", "angry", "mid")
            m "Stop being such a fuzzy and get over here..."
            call her_main("..................", "annoyed", "narrow", "angry", "R")

            stop music fadeout 1.0
            call her_walk(xpos="desk", ypos="base", speed=2, redux_pause=1, loiter=False)

            $ her_mood += 4
            pass

        else:
            call her_main("Yes, [genie_name].", "base", "narrow", "base", "mid_soft")

            stop music fadeout 1.0
            pass


    # Climb desk
    show screen blkfade
    with d5
    pause.5

    call play_sound("climb_desk")
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call her_main("...", "base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")
    m "Yes, very nice."
    call her_main("...", "annoyed", "narrow", "worried", "down")
    call nar(">Hermione hastily starts pulling at her top...")
    m "Slowly, please..."
    m "There's no rush."
    call her_main("I'm not!", "open", "base", "angry", "mid")
    call her_main("It's just... it's stuck.", "disgust", "narrow", "base", "down")
    g9 "Would you like some help with it?"
    if her_tier <= 5:
        call her_main("No...", "annoyed", "base", "angry", "mid")
        call her_main("I can do it myself, [genie_name].", "open", "closed", "base", "mid")
    else:
        call her_main("No, [genie_name].", "base", "narrow", "base", "mid_soft")
        call her_main("Just enjoy the show...", "soft", "narrow", "base", "mid_soft")
        g9 "I will, [hermione_name]."
    call her_main("...", "base", "narrow", "worried", "down")
    call nar(">Hermione pulls her shirt over her head...")

    $ hermione_wear_bra = False
    call set_her_action("lift_top")
    pause.5

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.2

    call nar(">And takes it off somewhat gracefully...")
    call ctc

    g9 "Yes! The tits!"

    if her_tier <= 4:
        call her_main("Must you be so vulgar, [genie_name]?", "annoyed", "closed", "base", "mid")
        call her_main("..............", "annoyed", "narrow", "worried", "down")

        call her_main("[genie_name]?", "open", "base", "base", "mid")
        m "Huh?"
        call her_main("Can I ask you a question?", "upset", "wink", "base", "mid")
        m "Go ahead..."
        call her_main("...............","normal","worriedCl")
        call her_main("Have you ever been in love...?","grin","worriedCl", emote="05")

        menu:
            m "..."
            "\"Don't be ridiculous! Love is a lie!\"":
                call her_main("I am sorry you think that way, [genie_name]!","annoyed","worriedL")
                call her_main("But you couldn't be more wrong!", "annoyed", "narrow", "annoyed", "mid")
                call her_main("I believe that true love is what makes the earth turn!", "base", "base", "base", "R")
                m "Actually the conservation of angular momentum is responsible for that."
                call her_main("Huh?", "upset", "wink", "base", "mid")
                m "Never mind. Just take off your skirt already?"
                call her_main("............", "annoyed", "narrow", "annoyed", "mid")

            "\"Be quiet and keep on dancing!\"":
                call her_main("But you said I could ask you a question...", "annoyed", "narrow", "annoyed", "mid")
                m "And you did, didn't you?"
                call her_main("!!!............", "open", "base", "base", "mid")
                call her_main("....................................", "annoyed", "narrow", "annoyed", "mid")
                m "Now, hush and take your skirt off."
                call her_main("........", "annoyed", "narrow", "angry", "R")

            "\"Yes... a very long time ago...\"":
                m "Yes... a very long time ago..."
                call her_main("!!!!!??..............................", "open", "base", "base", "mid")
                m "Her name was Eden..."
                call her_main("Was she beautiful?", "base", "base", "base", "mid")
                m "She was so much more than that..."
                m "She was smart, green and perfect..."
                call her_main("She was... \"green\"...?", "open", "narrow", "worried", "down")
                call her_main("Are you making fun of me, [genie_name]?", "angry", "base", "angry", "mid")
                m "Oh, you humans know nothing of true love..."
                call her_main(".....................................?", "soft", "base", "base", "mid")
                m "Err... I mean, take off that skirt, [hermione_name]!"
                call her_main(".................", "annoyed", "narrow", "angry", "R")

            "\"I feel like I'm in love right now!\"":
                call her_main("You don't have to be vulgar, [genie_name].", "annoyed", "narrow", "angry", "R")
                m "Oh, but I mean it!"
                call her_main("[genie_name], please!", "disgust", "narrow", "base", "mid_soft")
                call her_main("I am one of your students!", "soft", "base", "base", "mid")
                call her_main("And you are older than my father!","grin","worriedCl", emote="05")
                m "{size=-4}(You have no idea, girl.){/size}"
                call her_main("Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction...", "soft", "base", "base", "mid")
                call her_main("And when a man is experiencing sexual arousal, the same type of hormones--", "open", "closed", "base", "mid")
                m "[hermione_name]!"
                call her_main("Yes, [genie_name]?", "soft", "base", "base", "mid")
                m "Did you forget where you are?"
                call her_main("Oh, my apologies, [genie_name]... I get distracted sometimes.","grin","worriedCl", emote="05")
                m "Take off your skirt already, would you?!"
                call her_main("Right...","annoyed","worriedL")


    # Take off skirt
    call nar(">Hermione is starting to sway her hips rather seductively...")

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")
    pause.5

    $ hermione_wear_bottom = False
    call set_her_action("None")
    pause.2

    call nar(">While she slides her skirt down...")
    call ctc

    menu:
        "-Ask her to masturbate-":
            if her_tier <= 4:
                jump hg_pf_strip_T2_fingering
            elif her_tier == 5:
                jump hg_pf_strip_T3_fingering
            else:
                jump hg_pf_strip_T4_fingering

        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T2_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T2_watch




label hg_pf_strip_T2_watch:
    call blktone
    call nar(">You watch Hermione Dance...")
    call her_main("(Time for the finishing act I suppose...)","angry","worriedCl", xpos="mid", ypos="base")

    if hermione_wear_panties:
        m "Yes, [hermione_name]! Take them off!"
        call her_main("........", "annoyed", "closed", "base", "mid")

        $ hermione_wear_panties = False
        call set_her_action("pinch")
        pause.5

        call set_her_action("None")
        pause.2

        call nar(">Hermione bends over slightly and slides her panties down...")

    call nar(">You can see that she is doing her best to be graceful...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
    call ctc

    call her_main("..........", "base", "narrow", "base", "mid_soft")

    call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes...")
    m "{size=-4}(This looks quite impressive actually...){/size}"

    call set_her_action("fingering")
    pause.5

    call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements...")
    call ctc

    m "{size=-4}(Did she practice this?){/size}"
    g9 "Oh, why would I care?"
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "open", "closed", "base", "mid")

    call set_her_action("None")
    pause.5

    call nar(">Hermione performs another set of movements that could be considered classy...","start")
    call nar(">if not for her naked tits bouncing all over the place...","end")

    g9 "Yes, yes, you little harlot!"

    call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    ">And then Hermione slumps on her butt, completely exhausted."

    call hide_characters
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("Whew... This was rather exciting...","silly","worriedCl", emote="05", ypos="head")

    menu:
        m "..."
        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
            m "Good job [hermione_name]!"
            call her_main("Really?", "base", "narrow", "base", "mid_soft")
            m "Yes! You have a lot of talent for this!"
            call her_main("Thank you [genie_name].","silly","worriedCl", emote="05")
        "{size=-3}\"Hm... This was quite awful...\"{/size}":
            call her_main("Oh... I'm sorry...", "soft", "happy", "base", "R")
            m "That's OK... You just need to practice more..."
            call her_main("Em... I will keep that in mind, [genie_name]...", "open", "base", "base", "R")
        "{size=-3}\".................................................\"{/size}":
            call her_main(".......................","silly","worriedCl", emote="05")
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

    hide screen bld1
    call ctc

    jump end_hg_pf_strip



label hg_pf_strip_T2_masturbate:
    show screen blkfade
    with d5

    show screen chair_left
    call gen_chibi("jerking_off","behind_desk","behind_desk")
    show screen desk
    hide screen blkfade
    with fade

    call her_main("But...","angry","worriedCl", xpos="mid", ypos="base")
    call her_main(".............................")
    call her_main("Well, alright, but only if you will promise me not to....finish, [genie_name].", "soft", "base", "angry", "mid")

    menu:
        m "..."
        "-Promise her to hold it-":
                $ d_flag_07 = True #Promised to hold it.
                call her_main("Well, alright then...", "open", "closed", "base", "mid")

        "-Give her no such promise-":
            $ d_flag_07 = False #Did not promise to hold it.
            m "\"Not to finish\"? That would be like torture!"
            m "Please keep your sadistic urges to yourself, [hermione_name]."
            call her_main("I don't have any... sadistic urges, [genie_name]!", "annoyed", "narrow", "angry", "R")
            call her_main("I just don't want to...")
            g9 "Yes... Those are some nice tits you have..."
            call her_main("............","angry","worriedCl")
            g9 "A-ah... Yes..."
            call her_main("..........","angry","worriedCl")
            call her_main("Fine! Have it your way, [genie_name]!","angry","worriedCl")
            call her_main("{size=-5}(As usual...){/size}", "annoyed", "narrow", "angry", "R")


    call nar(">You keep on wanking while you watch Hermione's dance...")
    show screen blktone
    call her_main("Time for the finishing act I suppose...", "annoyed", "closed", "base", "mid")
    m "Yes, [hermione_name]! Take them off!"
    call her_main("........", "annoyed", "narrow", "base", "dead")
    if h_request_wear_panties or hermione_wear_panties:
        call nar(">Hermione bends over slightly and slides her panties down...")

        $ hermione_wear_panties = False
        call set_her_action("pinch")
        pause.5

        call set_her_action("None")
        pause.2

    call nar(">You can see that she is doing her best to be graceful...","start")
    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
    call ctc

    call nar(">None the less you decide to show her some appreciation...","start")
    call nar(">By stroking your cock even faster!","end")
    call her_main("..........", "annoyed", "narrow", "base", "dead")
    call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes...")
    m "{size=-4}(This looks quite impressive actually...){/size}"

    call set_her_action("fingering")
    pause.5

    call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements...")
    call ctc

    m "{size=-4}(Did she practice this?){/size}"
    g9 "Oh, what do I care?"
    call nar(">You stroke your diamond-hard cock furiously.")
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}", "open", "closed", "base", "mid")

    call set_her_action("None")
    pause.5

    call nar(">Hermione performs another set of movements that could be considered classy...","start")
    call nar(">if not for her naked tits bouncing all over the place...","end")

    g9 "Yes, yes, you little whore!"
    call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")
    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    ">And then Hermione slumps on her butt, completely exhausted."

    hide screen hermione_main
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("Whew... This was--", "open", "closed", "base", "mid", ypos="head")
    with hpunch
    g4 "ARGH! YOU FUCKING CUNT!"

    call cum_block
    call gen_chibi("jerking_off","behind_desk","behind_desk")
    $ g_c_c_u_pic = "genie_cum_03"
    $ genie_cum_chibi_xpos = -65
    $ genie_cum_chibi_ypos = 5
    show screen g_c_c_u
    call ctc

    $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
    $ u_sperm = "characters/hermione/face/auto_04.png"

    call her_chibi("sit_naked_shocked","on_desk","on_desk")

    call her_main("??!!!", "shock", "wide", "base", "stare")
    call her_main("[genie_name]!!!","angry","worriedCl")

    call gen_chibi("hold_dick","behind_desk","behind_desk")

    $ g_c_c_u_pic = "characters/genie/chibis/masturbating/sperm_wide_18.png"

    if d_flag_07: #Promised to hold it.
        call her_main("No, [genie_name]! You promised!","angry","worriedCl", ypos="head")
        g4 "Oh, man... This was pretty intense..."
        call her_main("You went back on your word, [genie_name]!","scream","worriedCl")
        m "Huh? What are you talking about?"
        call her_main("How could you do this to me, [genie_name]?", "shock", "base", "angry", "mid", tears="crying_blink")
        m "Oh, calm down, [hermione_name]."
        m "You earned your points today."
        m "Now, just get dressed and leave before somebody discovers you like this."
        call her_main("*sob!*........................", "shock", "narrow", "angry", "R", tears="messy")
        show screen blkfade
        with d5

        $ uni_sperm = False #Sperm layer is not displayed.
        $ aftersperm = True #Aftersperm layer is displayed.
        stop music fadeout 5.0
        ">.................{w}.................{w}.................{w}................."
        call her_main("...Can I just get paid now, [genie_name]... please?", "annoyed", "narrow", "angry", "R")

        $ her_mood += 30

        jump end_hg_pf_strip

    else:
        call her_main("it's so hot...","angry","worriedCl", ypos="head")
        call gen_chibi("hold_dick","behind_desk","behind_desk")
        m "Aha... Yeah... This feels great..."
        call her_main("You came all over me...", "soft", "happy", "base", "R")
        call her_main("I am your pupil and...")
        call her_main("You just came on me...", "grin", "narrow", "annoyed", "up")
        g9 "I know! Pretty exciting stuff, huh?!"
        call her_main("Nothing of that sort!", "open", "base", "base", "R")
        call her_main("You should have restrained yourself like a proper headmaster would!")
        m "Really? What did you expect me to do?"
        m "Aim at the wall or just put it back in my trousers and start cumming?"
        call her_main("........", "soft", "happy", "base", "R")
        call her_main("Still, you should not have...", "soft", "base", "angry", "mid")
        call her_main("I agreed to perform a striptease for you...", "open", "closed", "base", "mid")
        call her_main("But I didn't agree to be defiled like this.")
        m "I think I know where this is going..."

    call her_main("I demand to be paid extra!", "base", "base", "angry", "mid")
    m "Of course you do..."

    menu:
        m "..."
        "\"You get 1 extra point.\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            call her_main("One extra point?", "soft", "base", "angry", "mid")
            call her_main("One meagre extra point for letting you do this to me?","scream","worriedCl")
            call her_main("Now, that is just insulting, [genie_name]!", "soft", "base", "angry", "mid")
            m "One extra point, [hermione_name]. Take it or leave it."
            hide screen g_c_c_u
            call her_chibi("sit_naked","on_desk","on_desk")
            show screen g_c_c_u

            call her_main(".............", "annoyed", "narrow", "angry", "R")
            call her_main("I'll take it.", "soft", "base", "angry", "mid")
            $ her_mood += 30
            $ current_payout = 36
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ aftersperm = True #Show cum stains on Hermione's uniform.
            jump end_hg_pf_strip

        "\"You get 10 extra points.\"":
            $ current_payout = 45
            call her_main("Ten extra points [genie_name]?", "soft", "base", "angry", "mid")
            call her_main("But that is not even nearly enough!")
            m "Ten extra points. Take 'em or leave 'em [hermione_name]."
            hide screen g_c_c_u
            call her_chibi("sit_naked","on_desk","on_desk")
            show screen g_c_c_u

            call her_main("...............", "annoyed", "narrow", "angry", "R")
            call her_main("Well, alright... Better than nothing I suppose...", "soft", "base", "angry", "mid")
            $ her_mood += 11
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ aftersperm = True #Show cum stains on Hermione's uniform.
            jump end_hg_pf_strip

        "\"You get 25 extra points.\"":
            $ current_payout = 60
            hide screen g_c_c_u
            call her_chibi("sit_naked","on_desk","on_desk")
            show screen g_c_c_u

            call her_main("Yes, I believe this would be an appropriate amount.", "open", "closed", "base", "mid")
            m "are we good then?"
            call her_main("Yes, [genie_name]. Thank you.", "open", "closed", "base", "mid")
            hide screen bld1
            with d3
            call ctc
            show screen blkfade
            with d7
            pause.5
            $ aftersperm = True #Show cum stains on Hermione's uniform.
            jump end_hg_pf_strip

        "\"You get 50 extra points.\"":
            $ current_payout = 85
            call her_main("Seriously?!", "angry", "wide", "base", "stare")
            hide screen g_c_c_u
            call her_chibi("sit_naked","on_desk","on_desk")
            show screen g_c_c_u

            call her_main("Oh, I don't know what to say...", "open", "wide", "base", "stare")
            m "I enjoyed your performance [hermione_name]."
            call her_main("Thank you [genie_name]...", "base", "narrow", "base", "mid_soft")
            m "I also enjoyed plastering your agile little body with cum..."
            call her_main("[genie_name]......","silly","worriedCl", emote="05")
            m "So, just allow me to show my appreciation."
            m "Fifty extra points. Well deserved, [hermione_name]."
            call her_main("Thank very much, [genie_name].","silly","worriedCl", emote="05")
            hide screen bld1
            call ctc

            show screen blkfade
            with d5
            $ aftersperm = True #Show cum stains on Hermione's uniform.
            jump end_hg_pf_strip

        "\"You're not getting shit!\"":
            stop music fadeout 1.0
            call her_main("What? Not even my usual pay?", "shock", "wide", "base", "stare")

            menu:
                m "..."
                "\"Oh, no, you are still getting that.\"":
                    $ her_mood += 30
                    call her_main("How generous of you, [genie_name].", "soft", "base", "angry", "mid")
                    hide screen bld1
                    call ctc

                    show screen blkfade
                    with d5
                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                    jump end_hg_pf_strip

                "\"No, not even that!\"":
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("!!!?", "shock", "wide", "base", "stare")
                    call her_main("I danced for you, [genie_name]...")
                    call her_main("I degraded myself for your amusement...", "soft", "happy", "base", "R")
                    call her_main("I let you cum on me...", "open", "base", "base", "R")
                    with hpunch
                    call her_main("And I get NOTHING?!", "clench", "base", "angry", "mid", emote="01")
                    m "You are dismissed, [hermione_name]!"
                    call her_main("Oh, this is a new low even for you, [genie_name]!", "soft", "base", "angry", "mid")
                    m "I said you are dismissed."
                    call her_main("*GROAN!*", "clench", "base", "angry", "mid", emote="01")
                    hide screen bld1
                    call ctc

                    show screen blkfade
                    with d5

                    hide screen g_c_c_u
                    call gen_chibi("sit_behind_desk")
                    call her_chibi("stand","desk","base")
                    hide screen blkfade
                    with d5

                    call her_walk(action="leave", speed=2.5)

                    $ her_mood += 50

                    jump end_hermione_event
