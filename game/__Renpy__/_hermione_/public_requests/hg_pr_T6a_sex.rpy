

### Have Sex With A Classmate ###

label hg_pr_sex:

    if hg_pr_sex.counter < 1:
        m "{size=-4}(Tell her to fuck one of her classmates?){/size}"
        if her_tier < 6 or hg_T6_sex_trigger == False or her_reputation < 18:
            menu:
                "\"(Yes, let's do it!)\"":
                    pass
                "\"(Not right now.)\"":
                    jump hermione_favor_menu

        else: # Succeeds
            menu:
                "\"(Yes, let's do it!)\"":
                    call nar("!!! Attention !!!","start")
                    ">Continuing on this path will lock your game to a specific ending."
                    call nar(">You might want to save your game here.","end")

                    menu:
                        "Do you wish to continue?"
                        "\"(Yes, continue!)\"":
                            pass
                        "\"(No, return.)\"":
                            jump hermione_favor_menu

                "\"(Not right now.)\"":
                    jump hermione_favor_menu

    call her_main(face="happy", xpos="right", ypos="base")

    #Intro.
    if hg_pr_sex.counter == 0:
        m "[hermione_name]..."
        m "Today I need you to have sex with a classmate of your choice."

        if her_tier < 6 or hg_T6_sex_trigger == False or her_reputation < 18:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("..............","angry","angry")
        call her_main("I had the feeling that we would get to this sooner or later...","disgust","glance")
        call her_main("But...","annoyed","angryL")
        her "..................."
        m "If you do this, \"Gryffindor\" will be getting seventy five points tonight."
        call her_main("Well, then I will do it, [genie_name].","annoyed","annoyed")
        m "Great. See you after your classes then."
        call her_main(".............","upset","closed")

    else:
        m "[hermione_name]..."
        m "I need you to go have sex with another classmate of yours."
        call her_main("Again, [genie_name]?","angry","base")
        m "Yes. And you will get 75 points again as well."
        call her_main("Well, alright...","annoyed","annoyed")

    call her_walk(action="leave", speed=2.5)

    $ current_payout = 75
    $ hg_pr_sex.inProgress = True

    jump end_hermione_event


label end_hg_pr_sex:
    $ gryffindor += current_payout
    m "\"Gryffindor\" gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ public_whore_ending = True

    $ hg_pr_sex.inProgress = False

    # Increase Points
    if her_reputation < 24: # Points til 24
        $ her_reputation += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pr_sex_T1_intro_E1:

    call bld
    m "....."
    m ".........."
    m "She was supposed to be here, by now..."
    m "Hm..."

    $ hg_pr_sex.inProgress = False
    $ hermione_busy = True
    $ hg_pr_sex_skip = True

    # Next Morning.
    jump day_start


label hg_pr_sex_T1_intro_E2:
    $ hg_pr_sex_skip = False

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "[hermione_name], you missed your debriefing yesterday."
    call her_main("Yes, [genie_name], I apologize... *yawn*...","open","closed")
    m "Care to explain yourself?"
    call her_main("Of course, [genie_name].","open","squint", cheeks="blush")
    call her_main("It is sort of embarrassing, though...","base","baseL", cheeks="blush")
    call her_main("I spent the last night with two of my friends...","open","squint", cheeks="blush")
    m "A slumber party with some girlfriends, huh?"
    call her_main("Girlfriends?","angry","wink")
    call her_main("No, [genie_name]. Harry and Ron are boys...","open","baseL", cheeks="blush")
    m "Hm..."
    call her_main("Yes, we were best friends for such a long time...","base","baseL", cheeks="blush")
    call play_music("playful_tension") # SEX THEME.
    call her_main("But last night the boys made me their little plaything...","base","glance")
    call her_main("And I did not mind it one bit...","grin","dead")
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    call her_main(".................","soft","ahegao")
    call her_main("Will I get paid for this, [genie_name]?","angry","wink")

    jump end_hg_pr_sex


label hg_pr_sex_T1_E3:
    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="happy", xpos="right", ypos="base")

    m "[hermione_name], did you complete your task?"
    show screen blktone
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Yes I did, [genie_name].","upset","closed")
    call her_main("And in the school library of all places...","open","annoyed", cheeks="blush")
    her "At first I was kind of worried that we would make too much noise..."
    her "But the boy literally lasted only one minute, [genie_name]."
    m "Don't hold it against him, [hermione_name]."
    m "You are quite attractive, he probably got too excited..."
    call her_main("Nevertheless...","upset","closed")
    her "A dozen or so of rather gingerly thrusts and he is cumming already?"
    her "As a girl I cannot help but feel disappointed..."
    m "I see..."
    m "What did you do afterwards?"
    m "Pulled up your panties and went about your business as if nothing happened?"
    call her_main("My panties?","open","down")
    call her_main("I rarely bother to wear them anymore, [genie_name].","annoyed","angryL")
    m "Oh really?"
    call her_main("Yes... I find not wearing any underwear very empowering.","annoyed","annoyed")
    m "Good for you, [hermione_name]."

    jump end_hg_pr_sex


label hg_pr_sex_T1_E4:
    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="happy", xpos="right", ypos="base")

    m "[hermione_name], did you complete your task?"
    call play_music("playful_tension") # SEX THEME.
    call her_main("I did, [genie_name].","upset","closed")
    call her_main("I took one of the \"Ravenclaw\" boys to the girl's restroom...","base","down")
    her "...and let him have his way with me in one of the stalls."
    m "Well done, [hermione_name]."
    call her_main(".....................","annoyed","angryL")
    m "I said you did great. What's the matter?"
    call her_main("Ehm... well...","open","baseL", cheeks="blush")
    her "I am getting paid well for performing such tasks..."
    her "So I have no right to complain, but..."
    m "Hm...?"
    call her_main("My reputation is starting to suffer and it troubles me, [genie_name]...","open","base", cheeks="blush")
    m "Your reputation?"
    call her_main("Well, yes... ehm...","open","baseL", cheeks="blush")
    m ".............."
    call her_main("No, sorry, please disregard what I just said, [genie_name].","upset","closed")
    m "Hm..."

    jump end_hg_pr_sex
