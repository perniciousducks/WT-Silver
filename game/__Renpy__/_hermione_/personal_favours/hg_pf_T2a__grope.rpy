

### Hermione Groping ###

label hg_pf_grope:

    m "{size=-4}(I will grope her a little. Pretty harmless stuff.){/size}"

    if hg_pf_grope.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 15
    $ hg_pf_grope.start()


    # End Event
    label end_hg_pf_grope:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    ">You let go of Hermione..."

    call set_her_action("none")
    call hg_chibi_transition("stand", xpos="desk", ypos="base", flip=False, trans="fade")

    m "This will do for now."
    if her_tier <= 3:
        call her_main("................","annoyed","angryL", cheeks="blush", xpos="mid", ypos="base")
    else:
        call her_main("................", face="horny", cheeks="blush", xpos="mid", ypos="base")


    # Points
    if her_tier <= 5:
        $ gryffindor += current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"
    else:
        m "You may leave now, [hermione_name]."

    if her_tier <= 2:
        call her_main("..................","annoyed","worriedL")
        her "Thank you, [genie_name]..."
    elif her_tier <= 4:
        call her_main("..................","base","baseL")
        call her_main("Thank you, [genie_name]...","soft","base")
    else:
        call her_main("..................","soft","ahegao")
        call her_main("Thank you, [genie_name]...","soft","glance")

    if daytime:
        her "Now if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    if her_tier > 5:
        call her_main("(What about my points?)","disgust","down_raised", cheeks="blush", ypos="head")
        if her_whoring < 24:
            call her_main("(I'll just ask him about it next time...)","annoyed","angryL", ypos="head")
        else:
            call her_main("(Eh, who cares...)","base","ahegao_raised", cheeks="blush", ypos="head")
        pause.5

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    jump end_hermione_event



### Tier 0 - Events Fail ###

# Those events still prgress, but Hermione will run off and get mad.
# The heart icons for these events are 'black'

label hg_pf_grope_T0_fail_intro:
    m "[hermione_name], would you mind if I play with your tits a little?"
    call her_main("Play with...?","shock","wide")
    call her_main("My tits?!","angry","wide_stare")
    g9 "Or your butt! I haven't fully decided yet!"

    $ hg_pf_grope.counter -= 1

    jump too_much


label hg_pf_grope_T0_fail_repeat:
    g9 "[hermione_name], I'd like to grope you a little!"
    call her_main("This again...?","angry","angry")
    call her_main("I've told you before, [genie_name], absolutely not!!","scream","angryCl")
    call her_main("Merlin's beard...","angry","angry")
    m "Please?"
    call her_main("I'm leaving! Good day, Sir!","soft","closed")

    call her_chibi(action="leave", speed=2.5)

    $ her_mood += 6

    $ hg_pf_grope.counter -= 1

    jump end_hermione_event



### Tier 2 ###

# Event 1 (i) - Hermione is shocked about you groping her.
# Event 2 (i) - Hermione is still shocked.

label hg_pf_grope_T1_intro_E1:
    stop music fadeout 2.0
    m "Come closer [hermione_name]... Hop around my desk..."
    call her_main("*Uhm*... very well, Sir.","disgust","down_raised")

    call her_walk_desk_blkfade

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")
    pause.5

    call her_main("[genie_name].....?","annoyed","worriedL", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("What? What do you mean, [genie_name]-","soft","wide")
            call nar(">You reach out swiftly and grab both of her tits through her uniform...")

            jump hg_pf_grope_breasts_T1

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand under her skirt...")

            jump hg_pf_grope_ass_T1



label hg_pf_grope_T1_E1:
    stop music fadeout 2.0
    m "Come closer [hermione_name]... Hop around my desk..."
    call her_main("...............","annoyed","angry")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("[genie_name].....?","annoyed","angryL", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("!!!","soft","shocked")
            call her_main("S-Sir?!","disgust","worriedCl")
            call nar(">You reach out swiftly and grab both of her tits through her uniform...")

            jump hg_pf_grope_breasts_T1

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand under her skirt...")

            jump hg_pf_grope_ass_T1



### Tier 3 ###

# Event 1 (i) - Hermione tries to talk you out of it.
# Event 2 (i) - Hermione is indignant.

label hg_pf_grope_T2_intro_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?","base","base")
    m "How would you like to earn some house-points today?"
    call her_main("And what would I need to do to earn them?","annoyed","annoyed")
    m "Oh nothing too out of the ordinary."
    m "You just stand here while I grope you for a bit..."
    call her_main("[genie_name]... I'd prefer it if you wouldn't make me such offers...","annoyed","annoyed")
    m "Why? Too hard to resist?"
    her "Nothing like that, [genie_name]."
    m "Well, how about you come closer and bare your tits for me...?"
    g9 "I feel like playing with them a little..."
    call her_main("!!!","open","base")
    m "Or your but..."
    g9 "I'd like to give it a good squeeze."

    call her_main("[genie_name]! Don't you think this is too much?","disgust","glance")
    m "You think?"
    her "I am not one of those harlots from \"Slytherin\", you know..."
    m "I know... You are from \"Gryfonmon\"... or something..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE
    call her_main("And if I don't feel like it I don't have to sell you a single favour, [genie_name]!","annoyed","worriedL")
    m "Of course..."
    call her_main("...................","annoyed","angryL")
    m "I'll give you 35 house points for this."
    call her_main(".......................","disgust","glance")
    her "All you are going to do is watch, [genie_name]?"
    m "Well, I feel more like touching, actually..."
    her "...................................."

    call her_walk_desk_blkfade

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("[genie_name].....?","annoyed","angryL", ypos="head")
    m "..."

    menu:
        "\"I'm gonna play with your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("[genie_name].....?","disgust","worriedCl")

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand under her skirt...")

            jump hg_pf_grope_ass_T2



label hg_pf_grope_T2_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?","base","base")
    m "How would you like to earn some house-points today?"
    call her_main("And what would I need to do to earn them?","annoyed","annoyed")
    g9 "Get squeezed!"
    call her_main("....................................","annoyed","angryL")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("[genie_name].....?","annoyed","angryL", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("[genie_name].....?","disgust","worriedCl")

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand under her skirt...")

            jump hg_pf_grope_ass_T2



### Tier 3 ###

# Event 1 (i) - Hermione ejoys it.
# Event 2 (i) - Hermione asks if you are going to grope her tits or her ass.
# Event 2 (i) - Hermione ejoys it.

label hg_pf_grope_T3_intro_E1:
    m "[hermione_name]..."
    call her_main("[genie_name]?","base","base")
    m "Would you like to join me again?"
    g9 "Behind my desk."
    call her_main("Are you going to grope me again, [genie_name]?","soft","glance")
    g9 "You just read my mind!"
    call her_main("...................","disgust","down_raised")

    call her_walk_desk_blkfade

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("[genie_name].....?","base","down", ypos="head")
    m "..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            #call nar(">You reach out swiftly and grab both of her tits through her uniform...")
            call her_main("..........","base","down")

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt a little.\"":
            call nar(">You reach out and place your hand under her skirt...")
            jump hg_pf_grope_ass_T3



label hg_pf_grope_T3_intro_E2:
    m "[hermione_name]. Come here and join me..."
    g9 "I feel like playing with you a little."
    call her_main("Yes, Sir...","soft","baseL")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("[genie_name].....?","soft","down", ypos="head")
    m "Yes?"
    call her_main("Are you going to grope my breasts again?","soft","base")
    call her_main("Or my bum?....","soft","glance")
    m "*Hmm*..."

    menu:
        "\"I'm gonna play with your tits today.\"":
            call her_main("Of course, Sir.","base","down")
            call nar(">You reach out swiftly and grab both of her tits through her uniform...")

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt today.\"":
            call her_main("Of course, Sir.","base","down")
            call nar(">You reach out and place your hand under her skirt...")
            jump hg_pf_grope_ass_T3



label hg_pf_grope_T3_E2:
    g9 "[hermione_name]. Come here and let me grope you!"
    call her_main("Of course, [genie_name]...","base","glance")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="fade")

    call her_main("Are you going to grope my breasts today, Sir?","soft","glanceL", ypos="head")
    call her_main("Or my bum?....","soft","glance")

    m "*Hmm*... What would you like?"
    if one_out_of_three == 1:
        call her_main("I wouldn't mind it if you massaged my breasts a little...","soft","glanceL")
    elif one_out_of_three == 2:
        call her_main("I wouldn't mind it if you carassed my bum a bit, Sir...","soft","down")
    else:
        call her_main("I wouldn't mind either today, Sir.","soft","glanceL")

    m "Very well then..."

    menu:
        "\"I'm gonna molest your tits now.\"":
            call her_main("Yes, Sir.","base","ahegao")
            call nar(">You reach out swiftly and grab both of her tits through her uniform...")

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt now.\"":
            call her_main("Yes, Sir.","soft","ahegao")
            call nar(">You reach out and place your hand under her skirt...")

            jump hg_pf_grope_ass_T3
