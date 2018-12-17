

### Have Sex With A Classmate ###

##(Level 08) (75 pt.) (FUCK A CLASSMATE). (Available during daytime only).
label hg_pr_SexWithClassmate: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_SexWithClassmate_OBJ.points < 1:
        m "{size=-4}(Tell her to fuck one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_requests_menu

    call bld

    #Intro.
    if hg_pr_SexWithClassmate_OBJ.points == 0:
        m "[hermione_name]..."
        m "Today I need you to have sex with a classmate of your choice."

        if her_whoring < 21 or hg_pr_BlowjobClassmate_OBJ.points < 2:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("..............","angry","angry",xpos="right",ypos="base")
        call her_main("I had the feeling that we would get to this sooner or later...","disgust","glance")
        call her_main("But...","annoyed","angryL")
        her "..................."
        m "If you do this, \"Gryffindor\" will be getting seventy five points tonight."
        call her_main("Well, then I will do it, [genie_name].","annoyed","annoyed")
        m "Great. See you after your classes then."
        call her_main(".............","upset","closed")

    #Secont time event.
    else:
        m "[hermione_name]..."
        m "I need you to go have sex with another classmate of yours."
        call her_main("Again, [genie_name]?","angry","base",xpos="right",ypos="base")
        m "Yes. And you will get 75 points again as well."
        call her_main("Well, alright...","annoyed","annoyed")

    $ hg_pr_SexWithClassmate_OBJ.inProgress = True

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.


label hg_pr_SexWithClassmate_complete:

    #Event A
    if hg_pr_SexWithClassmate_OBJ.points <= 0 or one_out_of_three == 1: ### EVENT (A)

        if fucked_ron_and_har:
            jump returns_next_morning
        else:
            $ fucked_ron_and_har = True #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        m "....."
        m ".........."
        m "She was supposed to be here, by now..."
        m "Hm..."
        $ hg_pr_SexWithClassmate_OBJ.points += 1
        $ hg_pr_SexWithClassmate_OBJ.inProgress = False
        $ hermione_busy = True
        $ hg_pr_SexWithClassmate_AltFlag = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.

        jump day_start
        # NEXT MORNING

    #Event B
    elif one_out_of_three == 2: ### EVENT (B)

        call play_sound("door") #Sound of a door opening.
        call her_walk("door","mid",2)
        call bld

        m "[hermione_name], did you complete your task?"
        show screen blktone
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Yes I did, [genie_name].","upset","closed",xpos="right",ypos="base")
        call her_main("And in the school library of all places...","open","annoyed",cheeks="blush")
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

    #Event C
    elif one_out_of_three == 3:
        label returns_next_morning:
            pass

        call play_sound("door") #Sound of a door opening.
        call her_walk("door","mid",2)
        call bld

        m "[hermione_name], did you complete your task?"
        call play_music("playful_tension") # SEX THEME.
        call her_main("I did, [genie_name].","upset","closed",xpos="right",ypos="base")
        call her_main("I took one of the \"Ravenclaw\" boys to the girl's restroom...","base","down")
        her "...and let him have his way with me in one of the stalls."
        m "Well done, [hermione_name]."
        call her_main(".....................","annoyed","angryL")
        m "I said you did great. What's the matter?"
        call her_main("Ehm... well...","open","baseL",cheeks="blush")
        her "I am getting paid well for performing such tasks..."
        her "So I have no right to complain, but..."
        m "Hm...?"
        call her_main("My reputation is starting to suffer and it troubles me, [genie_name]...","open","base",cheeks="blush")
        m "Your reputation?"
        call her_main("Well, yes... ehm...","open","baseL",cheeks="blush")
        m ".............."
        call her_main("No, sorry, please disregard what I just said, [genie_name].","upset","closed")
        m "Hm..."

    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, [genie_name]."

    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False

    jump hg_pr_transition_block

    return



label hg_pr_SexWithClassmate_Alt: #Hermione does not show up. This is label where she shows up next morning.
    $ hg_pr_SexWithClassmate_AltFlag = False #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "[hermione_name], you missed your debriefing yesterday."
    call her_main("Yes, [genie_name], I apologize... *yawn*...","open","closed",xpos="right",ypos="base")
    m "Care to explain yourself?"
    call her_main("Of course, [genie_name].","open","squint",cheeks="blush")
    call her_main("It is sort of embarrassing, though...","base","baseL",cheeks="blush")
    call her_main("I spent the last night with two of my friends...","open","squint",cheeks="blush")
    m "A slumber party with some girlfriends, huh?"
    call her_main("Girlfriends?","angry","wink")
    call her_main("No, [genie_name]. Harry and Ron are boys...","open","baseL",cheeks="blush")
    m "Hm..."
    call her_main("Yes, we were best friends for such a long time...","base","baseL",cheeks="blush")
    call play_music("playful_tension") # SEX THEME.
    call her_main("But last night the boys made me their little plaything...","base","glance")
    call her_main("And I did not mind it one bit...","grin","dead")
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    call her_main(".................","soft","ahegao")
    call her_main("Will I get paid for this, [genie_name]?","angry","wink")

    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, [genie_name]."

    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False

    if her_reputation <= 23:
        $ her_reputation +=1

    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
