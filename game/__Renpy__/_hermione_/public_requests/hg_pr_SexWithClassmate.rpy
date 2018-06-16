

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
                jump silver_requests

    call bld from _call_bld_92
    
    #Intro.
    if hg_pr_SexWithClassmate_OBJ.points == 0:
        m "[hermione_name]..."
        m "Today I need you to have sex with a classmate of your choice."

        if whoring < 21 or hg_pr_BlowjobClassmate_OBJ.points < 2:
            jump too_much

        call play_music("chipper_doodle") from _call_play_music_151 # HERMIONE'S THEME.
        call her_main("..............","angry","angry",xpos="right",ypos="base") from _call_her_main_4033
        call her_main("I had the feeling that we would get to this sooner or later...","disgust","glance") from _call_her_main_4034
        call her_main("But...","annoyed","angryL") from _call_her_main_4035
        her "..................."
        m "If you do this, \"Gryffindor\" will be getting seventy five points tonight."
        call her_main("Well, then I will do it, [genie_name].","annoyed","annoyed") from _call_her_main_4036
        m "Great. See you after your classes then."
        call her_main(".............","upset","closed") from _call_her_main_4037

    #Secont time event.
    else:
        m "[hermione_name]..."
        m "I need you to go have sex with another classmate of yours."
        call her_main("Again, [genie_name]?","angry","base",xpos="right",ypos="base") from _call_her_main_4038
        m "Yes. And you will get 75 points again as well."
        call her_main("Well, alright...","annoyed","annoyed") from _call_her_main_4039
    
    $ hg_pr_SexWithClassmate_OBJ.inProgress = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
    

label hg_pr_SexWithClassmate_complete:

    #Event A
    if one_out_of_three == 1: ### EVENT (A)

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
        $ hermione_sleeping = True
        $ hg_pr_SexWithClassmate_AltFlag = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.

        return
        # NEXT MORNING
    
    #Event B
    elif one_out_of_three == 2: ### EVENT (B)

        call play_sound("door") from _call_play_sound_171 #Sound of a door opening.
        call her_walk("door","mid",2) from _call_her_walk_100
        call bld from _call_bld_93

        m "[hermione_name], did you complete your task?"
        show screen blktone
        call play_music("chipper_doodle") from _call_play_music_152 # HERMIONE'S THEME.
        call her_main("Yes I did, [genie_name].","upset","closed",xpos="right",ypos="base") from _call_her_main_4040
        call her_main("And in the school library of all places...","open","annoyed",cheeks="blush") from _call_her_main_4041
        her "At first I was kind of worried that we would make too much noise..."
        her "But the boy literally lasted only one minute, [genie_name]."
        m "Don't hold it against him, [hermione_name]."
        m "You are quite attractive, he probably got too excited..."
        call her_main("Nevertheless...","upset","closed") from _call_her_main_4042
        her "A dozen or so of rather gingerly thrusts and he is cumming already?"
        her "As a girl I cannot help but feel disappointed..."
        m "I see..."
        m "What did you do afterwards?"
        m "Pulled up your panties and went about your business as if nothing happened?"
        call her_main("My panties?","open","down") from _call_her_main_4043
        call her_main("I rarely bother to wear them anymore, [genie_name].","annoyed","angryL") from _call_her_main_4044
        m "Oh really?"
        call her_main("Yes... I find not wearing any underwear very empowering.","annoyed","annoyed") from _call_her_main_4045
        m "Good for you, [hermione_name]."
    
    #Event C
    elif one_out_of_three == 3:
        label returns_next_morning:
            pass

        call play_sound("door") from _call_play_sound_172 #Sound of a door opening.
        call her_walk("door","mid",2) from _call_her_walk_101
        call bld from _call_bld_94

        m "[hermione_name], did you complete your task?"
        call play_music("playful_tension") from _call_play_music_153# SEX THEME.
        call her_main("I did, [genie_name].","upset","closed",xpos="right",ypos="base") from _call_her_main_4046
        call her_main("I took one of the \"Ravenclaw\" boys to the girl's restroom...","base","down") from _call_her_main_4047
        her "...and let him have his way with me in one of the stalls."
        m "Well done, [hermione_name]."
        call her_main(".....................","annoyed","angryL") from _call_her_main_4048
        m "I said you did great. What's the matter?"
        call her_main("Ehm... well...","open","baseL",cheeks="blush") from _call_her_main_4049
        her "I am getting paid well for performing such tasks..."
        her "So I have no right to complain, but..."
        m "Hm...?"
        call her_main("My reputation is starting to suffer and it troubles me, [genie_name]...","open","base",cheeks="blush") from _call_her_main_4050
        m "Your reputation?"
        call her_main("Well, yes... ehm...","open","baseL",cheeks="blush") from _call_her_main_4051
        m ".............."
        call her_main("No, sorry, please disregard what I just said, [genie_name].","upset","closed") from _call_her_main_4052
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
    
    call play_sound("door") from _call_play_sound_173 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_102
    call bld from _call_bld_95
    
    call play_music("chipper_doodle") from _call_play_music_154 # HERMIONE'S THEME.
    m "[hermione_name], you missed your debriefing yesterday."
    call her_main("Yes, [genie_name], I apologize... *yawn*...","open","closed",xpos="right",ypos="base") from _call_her_main_4053
    m "Care to explain yourself?"
    call her_main("Of course, [genie_name].","open","squint",cheeks="blush") from _call_her_main_4054
    call her_main("It is sort of embarrassing, though...","base","baseL",cheeks="blush") from _call_her_main_4055
    call her_main("I spent the last night with two of my friends...","open","squint",cheeks="blush") from _call_her_main_4056
    m "A slumber party with some girlfriends, huh?"
    call her_main("Girlfriends?","angry","wink") from _call_her_main_4057
    call her_main("No, [genie_name]. Harry and Ron are boys...","open","baseL",cheeks="blush") from _call_her_main_4058
    m "Hm..."
    call her_main("Yes, we were best friends for such a long time...","base","baseL",cheeks="blush") from _call_her_main_4059
    call play_music("playful_tension") from _call_play_music_155# SEX THEME.
    call her_main("But last night the boys made me their little plaything...","base","glance") from _call_her_main_4060
    call her_main("And I did not mind it one bit...","grin","dead") from _call_her_main_4061
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    call her_main(".................","soft","ahegao") from _call_her_main_4062
    call her_main("Will I get paid for this, [genie_name]?","angry","wink") from _call_her_main_4063
    
    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
    
