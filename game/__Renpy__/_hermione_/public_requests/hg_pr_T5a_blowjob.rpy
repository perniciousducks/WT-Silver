

### Give Classmate A Blowjob ###

label hg_pr_blowjob:

    if hg_pr_blowjob.counter < 1:
        m "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}"
        if her_tier < 5 or hg_T5_blowjob_trigger == False or her_reputation < 15:
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
    if hg_pr_blowjob.counter == 0:
        m "[hermione_name], I will be buying another favour from you today."
        call her_main("Thank you, [genie_name]. I really appreciate it.","open","closed")
        m "Sure, Happy to help."
        m "I need you to go give a blowjob to one of your classmates."
        stop music fadeout 1.0
        call her_main("!!!","shock","wide")
        her "...with my mouth?"

        if her_tier < 5 or hg_T5_blowjob_trigger == False or her_reputation < 15:
            jump too_much

        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "Yes, that's how it's usually done..."
        call her_main("[genie_name], I...","upset","closed")
        call her_main("I refuse to sell you a depraved favour like that, [genie_name].","open","annoyed", cheeks="blush")
        call her_main("Can't I just kiss another girl instead?","open","worriedCl")
        her "I do not mind that..."
        m "[hermione_name], please stop wasting my time..."
        m "If you are not in the mood to sell favours today..."
        m "Then there is the door."
        call her_main("But I need the points, [genie_name]. You know that.","upset","closed")
        m "It's as the saying goes, [hermione_name]..."
        m "\"If you won't suck a dick for it - you don't need it.\""
        call her_main("Tch...","angry","angry", cheeks="blush")
        her "............................"
        m ".........................................."
        call her_main("...alright.","annoyed","angryL")
        her "I'll do it..."
        m "Go do it, then!"
        m "Report back to me after your classes."
        call her_main("...","angry","angry", cheeks="blush")
        her "....."
        her "......."
        m "You may leave, [hermione_name]."
        her "..."

    elif her_tier < 6:
        m "Go give some lucky boy another blowjob, [hermione_name]."
        call her_main("......Again?","disgust","glance")
        m "Yes, again."
        call her_main("..........","annoyed","annoyed")

    else:
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "[hermione_name]..."
        m "Do you believe in horoscopes?"
        call her_main("Not even a little bit, [genie_name]...","annoyed","angryL")
        m "Well, maybe you should..."
        call her_main("...?","open","base")
        m "Because I got yours right here and it says..."
        m "\"Dedicate today to something you do well\"..."
        call her_main("Something I do well...?","soft","baseL")
        m "Go suck on some cocks, [hermione_name]."
        call her_main(".....................","annoyed","annoyed") # :(
        m "Report back to me after your classes as usual..."
        call her_main("Of course...","annoyed","angryL")

    call her_walk(action="leave", speed=2.5)

    $ current_payout = 65
    $ hg_pr_blowjob.inProgress = True

    jump end_hermione_event


label end_hg_pr_blowjob:
    $ gryffindor += current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ aftersperm = False
    $ uni_sperm = False

    $ public_whore_ending = True

    $ hg_pr_blowjob.inProgress = False

    # Increase Points
    if her_tier == 5:
        if her_whoring < 21: # Points til 21
            $ her_whoring += 1

    if her_reputation < 21: # Points til 21
        $ her_reputation += 1

    jump end_hermione_event


### Tier 1 ###

label hg_pr_blowjob_T1_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="annoyed", xpos="right", ypos="base")

    #if her_whoring >= 18 and her_whoring < 21:

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "You know the drill, [hermione_name]. Start talking."
    show screen blktone
    call her_main("I have completed your task, [genie_name].","disgust","glance",xpos="right",ypos="base")
    m "Good. Tell me more."
    call her_main("What is there to tell, [genie_name]?","annoyed","angryL")
    her "I sucked off one of my classmates today..."
    her "And that's it..."
    m "Hm... I see..."
    m "..............."
    call her_main("....................................","angry","down_raised")
    m "Did you swallow?"
    call her_main("...........................","annoyed","annoyed")
    m "[hermione_name], did you swallow the load properly?"
    call her_main("Yes I did, [genie_name].","angry","angry")
    m "Well, I suppose that will do for now..."

    jump end_hg_pr_blowjob


label hg_pr_blowjob_T1_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="annoyed", xpos="right", ypos="base")

    m "[hermione_name], did you complete your task?"
    show screen blktone
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("[genie_name], I...","angry","down_raised")
    her "I tried, but..."
    call her_main("The boy turned me down, [genie_name]...","mad","worried", tears="soft")
    call her_main("I cannot believe that actually happened...","angry","base", tears="soft")
    her "I am one of the top students in this school!"
    her "One of the most popular ones too..."
    call her_main("And he turns me down?","angry","angry", tears="soft")
    her "Why would he insult me like that?!"
    m "So you're insulted because that boy refused to put his cock in your mouth?"
    call her_main("Wouldn't you be, [genie_name]?","angry","angry", tears="crying")
    m "I think I would get over it rather quickly..."
    call her_main("He rejected me [genie_name]...","angry","angry", cheeks="blush")
    her "Who does he think he is?!"
    call her_main("With all due respect, [genie_name], you wouldn't understand...","open","annoyed", cheeks="blush")
    m "Well, in any case. I can't pay you for this."
    call her_main("Of course... I would not expect you to, [genie_name].","annoyed","annoyed", tears="soft")
    her "I failed to complete my task and deserve no praise of any kind..."
    her "And should you pay me out of pity..."
    call her_main("Then That would only worsen the insult...","annoyed","angryL")
    m "Hm... In that case, maybe I should pay you anyway..."
    call her_main("No, [genie_name]. I would not accept it...","annoyed","annoyed")
    m "Hm... Well, this will be all then."
    her "Have a good night, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ hg_pr_blowjob.inProgress = False

    jump end_hermione_event


label hg_pr_blowjob_T1_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="annoyed", xpos="right", ypos="base")

    m "[hermione_name], how did it go?"
    show screen blktone
    call her_main("I still find the idea of selling a favour like this appalling, [genie_name].","annoyed","angryL",xpos="right",ypos="base")
    call her_main("But other than that it well surprising well...","annoyed","annoyed")
    call play_music("playful_tension") # SEX THEME.
    her "I gave a proper blowjob to this handsome boy from \"Ravenclaw\"..."
    call her_main("And he was such a gentleman about it...","open","down")
    call her_main("He even warned me when he was about to cum.","angry","down_raised")
    m "A true gentleman indeed."
    m "Did you swallow?"
    call her_main("Of course I did, [genie_name].","upset","closed")
    her "I told you - I gave the boy a proper blowjob."
    call her_main("The least I could do for someone who treated me with respect for a change...","angry","down_raised")
    m "Well, in that case."

    jump end_hg_pr_blowjob



### Tier 2 ###

label hg_pr_blowjob_T2_intro_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="annoyed", xpos="right", ypos="base")

    m "[hermione_name], how did it go?"
    show screen blktone
    call her_main("Splendid, [genie_name]. Simply splendid.","base","happyCl")
    m "Really? Do tell."
    call play_music("playful_tension") # SEX THEME.
    call her_main("Today I did something I wanted to do for such a long time now...","base","ahegao_raised")
    her "But never could muster up enough courage for..."
    m "Hm..?"
    call her_main("Today I sucked off my two best friends in the entire world!","soft","ahegao")
    call her_main("And it was every bit as exciting as I thought it would be.","base","down")
    call her_main("I made their cocks all sloppy with saliva...","grin","dead")
    her "I sucked on their balls too..."
    call her_main("But the best part was to see their faces...","silly","ahegao")
    her "The boys could not believe it was actually happening..."
    call her_main("To be honest, neither could I...","silly","dead")
    her "I, Hermione granger - the girl they knew for years..."
    call her_main("Sucking on their cocks...","open_wide_tongue","ahegao")
    call her_main("Like some nasty little slut...","shock","baseL", cheeks="blush", tears="soft")
    m "Are you in love with those boys, [hermione_name]?"
    call her_main("I don't know, [genie_name]... Maybe...","base","happyCl")
    her "Could I get paid now please?"
    m "Sure..."

    jump end_hg_pr_blowjob


label hg_pr_blowjob_T2_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #if her_whoring >= 21: # LEVEL 08 =+

    stop music fadeout 1.0
    # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
    $ u_tears_pic = "characters/hermione/face/tears_03.png"
    $ aftersperm = True
    $ uni_sperm = True
    $ u_sperm = "characters/hermione/face/auto_08.png"

    show screen blktone
    call her_main("","angry","angry",xpos="right",ypos="base")
    call ctc

    m "[hermione_name]..."
    m "You look like hell..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("[genie_name], I have been raped.","scream","angryCl")
    m "Seriously?"
    call her_main("Yes, [genie_name].","annoyed","annoyed")
    her "That nasty boy from \"Slytherin\" raped me..."
    call her_main("Or raped my face rather I suppose...","open","down")
    her "And--"
    play sound "sounds/burp.mp3"
    call her_main("*Burp!*...","shock","worriedCl")
    call her_main("Excuse me.","angry","down_raised")
    call her_main("He came so much I was barely able to swallow it all...","scream","angry", emote="01")
    her "Bloody bastard!"
    call her_main("You think I could file a complaint, [genie_name]?","angry","angry", cheeks="blush")
    m "Hm... I suppose..."
    m "But keep in mind that the moment we bring the ministry into this..."
    m "All this \"favour selling business\" will have to stop immediately."
    call her_main("Oh...?","open","baseL", cheeks="blush")
    her ".................."
    call her_main("Please, never mind what I just said then...","base","happyCl")
    m "Are you sure? You look pretty messed up."
    her "No, no. It's nothing really..."
    her "After all I was the one who offered him a free blowjob..."
    her "He just got a bit rough with me closer to the end, that's all..."
    her "I think I am just overreacting..."
    m "I see..."
    her "Can I just--"
    play sound "sounds/burp.mp3"
    call her_main("*Burp!*...","shock","wide")
    call her_main("Excuse me, [genie_name].","angry","down_raised")
    call her_main("{size=-3}(He just kept on cumming... My stomach feels so full...){/size}","angry","worriedCl", emote="05")
    call her_main("Can I get my payment now, please?","open","base")

    jump end_hg_pr_blowjob


label hg_pr_blowjob_T2_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    stop music fadeout 1.0
    $ uni_sperm = True
    $ u_sperm = "characters/hermione/face/auto_10.png"

    show screen blktone
    call her_main("","base","ahegao_raised",xpos="right",ypos="base")
    call ctc

    her "Good evening, [genie_name]..."
    g4 "[hermione_name]?!"
    g4 "What happened to you, [hermione_name]?"
    g4 "All I asked you to do was to give a blowjob to one of your classmates."
    call play_music("playful_tension") # SEX THEME.
    call her_main("That... that was exactly what I did, [genie_name].","angry","down_raised")
    m "[hermione_name], you are covered in cum head to toe."
    call her_main("I am?","soft","ahegao")
    her "Oh... Did I forget to clean myself up?"
    call her_main("How embarrassing...","base","glance")
    her "That thing at the boy's restroom sort of escalated I suppose..."
    her "Before I knew what happened I was surrounded with hard throbbing cocks..."
    call her_main("Oh... Just talking about it makes me shiver with excitement... err..","silly","dead")
    call her_main("...I mean, with fear... no, not fear...","grin","ahegao")
    call her_main("Embarrassment?","base","baseL", cheeks="blush")
    m "Are you asking me?"
    call her_main("Oh, excuse me, [genie_name]... I feel a little lightheaded...","grin","dead")
    her "I think I need to go lie down for a while..."
    m "Don't forget to take a shower first."
    call her_main("A shower? Why?","base","glance")
    m "Never mind..."
    call ctc

    jump end_hg_pr_blowjob
