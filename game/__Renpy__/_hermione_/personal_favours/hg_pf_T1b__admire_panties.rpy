

### Admire Panties ###

label hg_pf_admire_panties:

    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"

    if hg_pf_admire_panties.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu


    # Start Event
    $ current_payout = 10
    $ hg_pf_admire_panties.start()


    # End Event
    label end_hg_pf_admire_panties:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call set_her_action(None)
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_tier <= 2:
        call her_main("..................","base","baseL", xpos="mid", ypos="base", trans="fade")
    elif her_tier <= 5:
        call her_main("","base","base", xpos="mid", ypos="base", trans="fade")
    else:
        call her_main("","smile","glance", xpos="mid", ypos="base", trans="fade")


    # Points
    if her_tier <= 3:
        $ gryffindor += current_payout
        m "[current_payout] points to \"Gryffindor\", [hermione_name]. Well done."

    if hg_pf_admire_panties.counter == 1: #First time.
        call her_main("Another [current_payout] points...","smile","baseL")
        her "Can't wait to tell the guys!"
        call her_main("Only that I can't actually tell them about any of this...","annoyed","angryL")

    call her_main("Will this be all then?","open","base")
    m "Yes, you can go now."

    if daytime:
        her "Well, my classes are about to start..."
    else:
        her "It's getting pretty late, [genie_name]... I should go..."


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    if her_tier > 3:
        her "What about my points?"
        her "Eh, Who cares. It's only [current_payout] points..."

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 1:
        if her_whoring < 3: # Points til 3
            $ her_whoring += 1

    elif her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    elif her_tier == 3: # No panties!
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    jump end_hermione_event



### Tier 1 ###

# Hermione reluctantly lifts her skirt for you.
# Event 1 (i) - Hermione is shocked about your suggestion.
# Event 2 (r) - Hermione still can't believe what you ask her to do.

label hg_pf_admire_panties_T1_intro_E1:
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."
    call her_main("My... panties...?","open","base")
    call her_main("[genie_name]!","angry","angry")
    m "I know, I know, this a little weird..."
    call her_main("{size=+7}A little !?{/size}","shock","wide")
    her "This is completely inappropriate!"
    m "Listen, we need to go through this phase before we get to the good stuff, alright?"
    call her_main("The \"good stuff\"? [genie_name], I don't understand...","open","base")
    m "What don't you understand, [hermione_name]?"
    m "Do you need these points or not?"
    call her_main("I do...","open","base")
    m "Lift up your skirt then..."
    call her_main(".............","angry","angry")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1_E1:
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."
    call her_main("This again?","angry","angry")
    m "Yes. Now lift up your skirt..."
    call her_main(".............","angry","angry")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1: # Call label
    call hide_characters
    hide screen bld1
    with d3

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")

    call her_chibi("lift_skirt","mid","base")
    with d3
    call ctc

    call play_music("playful_tension")
    show screen blktone
    call her_main(".....................","angry","angry", xpos="mid", ypos="base")
    call ctc

    menu:
        "-Stare at her face-":
            ">You study Hermione's face..."
            call ctc
            ">You wonder what's going through her mind right now."
            call her_main(".......................","angry","annoyed",emote="01")
            call ctc

            return

        "-Stare at her panties-":
            ">That's a plain girlish underwear..."
            call her_main(".......................","angry","annoyed",emote="01")
            call ctc

            return





### Tier 2 ###

# Hermione lifts her skirt for you.
# Event 1 (i) - Hermione is embarrassed about what she's about to do.
# Event 2 (r) - Hermione is still not happy.

label hg_pf_admire_panties_T2_intro_E1:
    call her_main("So, what will it be, [genie_name]?")
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."
    call her_main("Oh... again?","annoyed","worriedL")
    m "Just do it..."
    call her_main("..................","annoyed","worriedL")

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T2_E1:
    "Dev Note" "Add repeatable intro here."

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T2: # Call label

    call hide_characters
    hide screen bld1
    with d3

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")

    call her_chibi("lift_skirt","mid","base")
    with d3

    call play_music("playful_tension")
    show screen blktone
    call her_main("Here, [genie_name]...","base","base", xpos="mid", ypos="base")
    call ctc

    menu:
        "\"You don't look too embarrassed...\"":
            call her_main("That's not true...","base","squint")
            call her_main("But this is a small price to pay if the \"Gryffindors\" keep the cup this year.","base","baseL")
            her "I know everyone will be so happy..."
            call ctc

            return

        "\"I like your panties...\"":
            call her_main("Thank you, [genie_name]...","base","squint")
            call ctc

            return

        "-Keep looking into her eyes-":
            call her_main("..............................","soft","base")
            her "...........................?"
            call her_main("................................","grin","baseL")
            call her_main("[genie_name], please... You are embarrassing me.","grin","worriedCl",emote="05")
            call ctc

            return






### Tier 3 ###

# Event 1 (i) - Hermione is not wearing her panties.
# Event 2 (r) - No panties. You get to call her a slut.
# Event 3 (r) - Panties may or may not be equipped. Hermione asks to remove them or keep them on.

label hg_pf_admire_panties_T3_intro_E1:
    m "[hermione_name], would you like to show me your panties?"
    call her_main("Again?","annoyed","worriedL")
    m "If it's not too much trouble..."
    call her_main("..................","annoyed","worriedL")

    call hide_characters
    hide screen bld1
    with d3

    $ hermione_wear_panties = False
    call set_her_action("lift_skirt")

    call her_chibi("lift_skirt","mid","base")
    with d3
    pause.8

    call her_main("..........................","base","baseL", cheeks="blush", ypos="head")
    g4 "!!?"

    show screen blktone
    call her_main("","base","glance", xpos="mid", ypos="base", trans="fade")
    call ctc

    # No Panties!
    g4 "Where are your panties, [hermione_name]?"
    call her_main("Oh, lately I just don't feel like wearing them...","base","down", cheeks="blush")

    menu:
        "\"You little slut!\"":
            her "Hm..."
            call her_main("I suppose I am...","base","glance")
            her "Do I get extra points for that?"

            menu:
                "\"Absolutely!\"":
                    m "Absolutely!"
                    $ current_payout +=10
                    m "Ten additional points to \"Gryffindor\"!"
                    call her_main("Thank you, [genie_name]!","base","worriedCl")
                    call ctc

                "\"Absolutely not!\"":
                    $ her_mood +=5
                    call her_main("Why not!?","scream","angryCl")
                    m "Sluts aren't paid"
                    m "That's what makes them sluts"
                    call her_main("well are you even going to pay me [current_payout] points?","annoyed","angry")
                    m "Are you a slut or are you a prostitute?"
                    her "{size=-4}...a slut {/size}"
                    m "Good girl"
                    call ctc

        "\"Good! [current_payout] points!\"":
            pass

    jump end_hg_pf_admire_panties



label hg_pf_admire_panties_T3_E1:
    "Dev Note" "Add repeatable intro here."

    call hide_characters
    hide screen bld1
    with d3

    $ hermione_wear_panties = False
    call set_her_action("lift_skirt")

    call her_chibi("lift_skirt","mid","base")
    with d3
    pause.8

    show screen blktone
    call her_main("","base","glance", xpos="mid", ypos="base")
    call ctc

    # No Panties!
    g9 "Where are your panties, [hermione_name]?"
    call her_main("Oh, lately I just don't feel like wearing them...","base","down", cheeks="blush")

    menu:
        "\"You little slut!\"":
            her "Hm..."
            call her_main("I suppose I am...","base","glance")
            her "Do I get extra points for that?"

            menu:
                "\"Absolutely!\"":
                    m "Absolutely!"
                    $ current_payout +=10
                    m "Ten additional points to \"Gryffindor\"!"
                    call her_main("Thank you, [genie_name]!","base","worriedCl")
                    call ctc

                "\"Absolutely not!\"":
                    $ her_mood +=5
                    call her_main("Why not!?","scream","angryCl")
                    m "Sluts aren't paid"
                    m "That's what makes them sluts"
                    call her_main("well are you even going to pay me [current_payout] points?","annoyed","angry")
                    m "Are you a slut or are you a prostitute?"
                    her "{size=-4}...a slut {/size}"
                    m "Good girl"
                    call ctc

        "\"Good! [current_payout] points!\"":
            pass


    call her_main("I could put my panties back on for you, if you'd like that, Sir?","open","baseL")

    menu:
        "\"Yes, put them back on!\"":
            call her_main("Alright, [genie_name].","base","glance")
            hide screen hermione_main
            with d3
            ">Hermione puts on her panties."

            $ h_request_wear_panties = True
            $ hermione_wear_panties = True

            call update_her_uniform
            call update_chibi_uniform
            call her_chibi("lift_skirt")
            call set_her_action("lift_skirt")

            call her_main("","base","glance")
            call ctc

            call her_main("I hope you like them...","soft","baseL")

        "\"No, keep them off!\"":
            call her_main("Of course, [genie_name].","soft","ahegao")
            call ctc

            $ h_request_wear_panties = False

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T3_E2:

    "Dev Note" "Add repeatable intro here."

    call hide_characters
    hide screen bld1
    with d3

    if h_request_wear_panties:
        $ hermione_wear_panties = True
    else:
        $ hermione_wear_panties = False

    call set_her_action("lift_skirt")

    call her_chibi("lift_skirt","mid","base")
    with d3
    pause.8

    show screen blktone
    call her_main("","base","glance", xpos="mid", ypos="base")
    call ctc

    # No Panties.
    if not hermione_wear_panties:
        g9 "Where are your panties, [hermione_name]?"
        call her_main("I have them here in my pocket...","open","baseL")
        call her_main("Most of the time I just leave them in the \"Gryffindor\" common room...","open","baseL")
        call her_main("But I got them with me this time.","open","baseL")
        call ctc

        call her_main("If you'd like, Sir, I could put my panties back on for you.","soft","glance")

        menu:
            "\"Yes, put them back on!\"":
                call her_main("Alright, [genie_name].","base","glance")
                hide screen hermione_main
                with d3
                ">Hermione puts on her panties."

                $ h_request_wear_panties = True
                $ hermione_wear_panties = True

                call update_her_uniform
                call update_chibi_uniform
                call her_chibi("lift_skirt")
                call set_her_action("lift_skirt")

                call her_main("","base","glance")
                call ctc

                call her_main("I hope you like them...","soft","baseL")

            "\"No, keep them off!\"":
                call her_main("Of course, [genie_name].","soft","ahegao")
                call ctc

                $ h_request_wear_panties = False

    else:
        call her_main("Do you like them, [genie_name]?","base","glance")
        m "Indeed I do, [hermione_name]..."
        call ctc

        call her_main("I could take them off, if you'd like that, [genie_name].","open","baseL")

        menu:
            "\"Yes, Take them off!\"":
                call her_main("Alright, [genie_name].","soft","ahegao")
                m "And keep them off from now on!"
                call her_main("Whatever you want, [genie_name].","base","glance")
                hide screen hermione_main
                with d3
                call nar(">Hermione takes off her panties.")

                $ h_request_wear_panties = False
                $ hermione_wear_panties = False

                call update_her_uniform
                hide screen hermione_chibi_lift_skirt
                call update_chibi_uniform

                call her_chibi("lift_skirt")
                call set_her_action("lift_skirt")

                call her_main("","base","glance")
                call ctc

                call her_main("I hope you like it, [genie_name]...","angry","wink")

            "\"No, keep them on!\"":
                call her_main("Sure, [genie_name].","base","glance")
                call ctc

                $ h_request_wear_panties = True

    jump end_hg_pf_admire_panties
