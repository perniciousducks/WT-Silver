

### Masturbate ###

label hg_pf_strip_fingering_intro:

    # Intro
    if not hg_fingering_trigger:
        $ hg_fingering_trigger = True
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?","base","base", xpos="mid", ypos="base")
        m "Do you ever touch yourself?"
        call her_main("What? why?","upset","wink")
        m "Do you?"
        call her_main("[genie_name]!","scream","worriedCl")
        m "It's a simple question [hermione_name]..."
        call her_main("......","normal","worriedCl")
        call her_main("{size=-5}I do...{/size}","angry","worriedCl", emote="05")
        m "Huh? What was that?"
        call her_main("I said that I do alright!!!","scream","worriedCl")
        m "Hmmmm, I'm not sure I believe you..."
        call her_main("What? why would I lie?","annoyed","worriedL")
        m "I'm not sure..."
        m "But don't worry, I'm sure a quick little demonstration will erase any doubts..."
        call her_main("......","annoyed","angryL")
        call her_main("well I suppose I could.","open","down")
        call her_main("But you better keep your hands to yourself...","open","down")
        m "Witcher's promise."
        call her_main("...","annoyed","suspicious")

    # Repeat
    else:
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?","base","base", xpos="mid", ypos="base")
        m "Are you feeling horny?"
        call her_main("maybe A little, [genie_name].","base","glance")
        m "Ah, well perhaps we can fix that..."
        call her_main("[genie_name]...","open","worriedCl")

        g9 "Why don't you play with that slutty little pussy of yours!"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
        call her_main(".............","soft","ahegao")
        call her_main("Alright...","base","down")

        call her_main("(I can't believe I'm going to do this... again...)","angry","down_raised")

    return



### Tier 2 ###

label hg_pf_strip_T2_fingering:

    call hg_pf_strip_fingering_intro

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........","upset","base")
    call her_main("Do you want me to... start?","soft","wink")
    m "Yes, my dear."
    call her_main("...........","disgust","down_raised")
    call her_main("(I can't believe I'm going to do this...)","normal","worriedCl")

    call set_her_action("covering_top")
    call ctc

    g9 "Nice..."
    call her_main("........","upset","wink")
    m "............."
    call her_main(".............","normal","worriedCl")
    call her_main("umm... [genie_name]?")
    m "Yes, what is it?"
    call her_main("How long do I have to keep doing this?","open","base")
    m "Until you finish [hermione_name]..."

    if daytime:
        call her_main("But my classes are about to start, [genie_name]...","soft","base")
    else:
        call her_main("But it's getting late, [genie_name]...","soft","base")

    call her_main("I'm not sure if I'll be able to finish... in time.","disgust","down_raised")
    m "Do you need the points or not?"
    call her_main("I do, [genie_name]! I'm sorry...","open","down")
    call her_main("I'll just keep ...going...","disgust","down_raised")
    m "(Hmmm, I might have to give her a little encouragement.)"

    menu:
        m "..."
        "\"That's it slut, keep going.\"":
            call her_main("[genie_name]!!!","angry","angry")
            call her_main("How dare you!")
            m "what?"
            call her_main("I hardly think that language is appropriate.","upset","wink")
            m "And masturbating in front of your headmaster is?"
            call her_main("Well... this is different.","open","down")
            call her_main("I'm doing this for the honor of \"gryffindor\"...")
            call her_main("To help my--")
            call nar(">You notice how she's starting to grind her hips a little faster.")
            $ hermione_dribble = True
            call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            call her_main("My classmates win the house cup...","angry","wink")
            m "Are you sure that's the only reason slut?"
            call her_main("I don't know--","normal","worriedCl")
            call her_main("ah-a{image=textheart}...","open","worriedCl")
            call her_main("I don't know what you mean, [genie_name]...","angry","down_raised")
            m "It seems to me that you might be enjoying this a little too much..."
            call her_main("I am not, [genie_name]!","open","worriedCl")
            m "Really?"
            call her_main("......................","normal","worriedCl")
            m "Then why is your pussy so wet slut?"
            call ctc

            call her_main("ah...{image=textheart}","open","worriedCl")
            m "ha! just Admit it, you enjoy being called a slut!"
            call her_main("I do not!","normal","worriedCl")
            call her_main("Aha...{image=textheart}","open","worriedCl")
            call her_main("I'm just thinking about how happy everyone will be when we win!","shock","worriedCl")
            m "and what if they find out how you earned the points?"
            call her_main("what?!","shock","wide")
            m "then it wouldn't just be me degrading you..."
            call her_main("...","soft","squintL")
            m "It would be the whole school."
            call her_main("ah...{image=textheart}","silly","dead")
            m "Little. miss. slut."
            call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
            call her_main("[genie_name], please... don't tell anyone...","angry","wink")
            call nar(">Hermione keeps on grinding her hips against her hand...")
            call her_main("they can't find out...","angry","base")
            call her_main("if harry and ron knew...","angry","down_raised")
            call her_main("i'd... ah...{image=textheart}","soft","ahegao")
            m "You'd what [hermione_name]?"
            call her_main("I'd...","open","worriedCl")
            call her_main("I'd...{image=textheart}","shock","worriedCl")
            call her_main("I...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")

        "\"Play with your breasts\"":
            call her_main("my breasts...","open","down")
            call set_her_action("covering_top")

            call her_main("I'm not sure if I should--","clench","down_raised")
            m "There's another 10 points for \"gryffindor\" in it for you..."
            $ current_payout += 10
            call her_main("...","soft","squintL")
            call her_main("......","soft","squintL")
            call set_her_action("lift_breasts")

            call her_main("ah...{image=textheart}","open","baseL")
            m "There... Isn't that better?"
            $ hermione_dribble = True
            call her_main("Ah... y-yes...{image=textheart}","grin","ahegao")
            call set_her_action("covering_top")
            call her_main("Mmmm...","smile","happyCl")
            m "That's it..."
            call set_her_action("lift_breasts")
            call her_main("[genie_name], do you mind...","base","ahegao_raised")
            m "What [hermione_name]?"
            call her_main("Could you... Call me names...","open","ahegao_raised", cheeks="blush")
            m "Such as?"
            call set_her_action("covering_top")

            call her_main("...{p}{size=-5}Slut...{/size}{p}Only if it's not too much...","base","ahegao_raised", cheeks="blush")
            m "You little whore..."
            call her_main("Ah...{image=textheart}{image=textheart}","grin","ahegao")
            m "What would your parents think if they saw this?"
            call her_main("i-{image=textheart}","base","ahegao_raised", cheeks="blush")
            call set_her_action("lift_breasts")

            call her_main("Ah...{image=textheart} I don't know...","base","ahegao_raised", cheeks="blush")
            call her_main("To be perfectly honest [genie_name]... I don't think I care...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised", cheeks="blush")
            m "Really?"
            call set_her_action("covering_top")

            call her_main("Really...{image=textheart}","silly","ahegao_raised", cheeks="blush")
            m "Would you at least stop?"
            call her_main("Ah...{image=textheart}","open_tongue","ahegao_raised", cheeks="blush")
            call set_her_action("lift_breasts")

            call her_main("Maybe....","open_tongue","ahegao_raised", cheeks="blush")
            call her_main("I'm not sure...","open","baseL", cheeks="blush")
            call set_her_action("covering_top")

            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised", cheeks="blush")

        "\"Dig deeper!\"":

            call set_her_action("covering")

            m "Good... Just keep playing with that slutty little pussy of yours!"
            call her_main("[genie_name]!","mad","angry", cheeks="blush")
            m "What?"
            $ hermione_dribble = True
            call her_main("It's not {size=-5}slutty...{/size}","annoyed","angryL", cheeks="blush")
            m "Are you sure? Because from where I'm sitting it looks nice and wet."
            call her_main("Ah...{image=textheart}","base","ahegao_raised", cheeks="blush")
            call her_main("It's just sweat, [genie_name]...","open","baseL", cheeks="blush")
            m "Whatever you say..."
            call her_main("...............","base","ahegao_raised", cheeks="blush")
            m "{size=-5}Slut.{/size}"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised", cheeks="blush")
            call her_main("Sir... please...","open","baseL", cheeks="blush")
            call set_her_action("pinch")

            call nar(">Hermione starts gently fingering herself.")
            m "Very good..."
            call her_main("...{image=textheart}","silly","ahegao_raised", cheeks="blush")
            call her_main("Ah...{image=textheart}","open_tongue","ahegao_raised", cheeks="blush")
            m "That's it slut. Try going a little deeper...."
            call her_main("...","open_tongue","ahegao_raised", cheeks="blush")
            call set_her_action("covering")

            call her_main("Mmmm...{image=textheart}","scream","worriedCl", cheeks="blush")


    call her_main("Ah...","shock","baseL", cheeks="blush", tears="soft")
    m "almost there [hermione_name]?"
    call her_main("a-almost...","clench","worried", cheeks="blush", tears="soft")
    call her_main("I just need a bit longer...")
    m "well you better hurry..."
    call her_main("Ah... i know, [genie_name].","mad","worriedCl", tears="soft_blink")
    call her_main("...........","shock","baseL", cheeks="blush", tears="soft")
    m "is everything alright?"
    call her_main("................","shock","down_raised", cheeks="blush", tears="crying")
    m "Why are you being so quiet [hermione_name]?"
    call her_main("......","clench","worried", cheeks="blush", tears="soft")
    call her_main("[genie_name]... I don't think I can...")
    m "what?"
    call her_main("...finish...","angry","dead", cheeks="blush", tears="crying")

    menu:
        "-Chastise her-":
            m "Well then I guess \"Slytherin\" will have to win the house cup this year."
            call her_main("B-but--","scream","wide")
            m "now, now [hermione_name], a deals a deal."
            call her_main("Really?","open","worriedCl")
            call her_main("but I'm trying [genie_name]...","shock","worriedCl")
            m "try harder..."
            call nar(">Hermione starts grinding furiously against hand")
            call her_main("*SOB!* i can't...","shock","down_raised", cheeks="blush", tears="crying")
            m "well then, 0 points to \"Gryffindor\"..."
            call her_main("{size=-5}After all...{/size} Really [genie_name]?","clench","worried", cheeks="blush", tears="soft")
            call her_main("After I stood here and...","scream","angry", cheeks="blush", tears="messy")
            call her_main("..........","angry","suspicious", cheeks="blush", tears="messy")
            call nar(">Hermione wipes the tears from her eyes.")
            call her_main("I am not going to sell you a single favour anymore, [genie_name]!","angry","angry", cheeks="blush")

            $ her_mood += 15

            jump end_hg_pf_strip

        "-Forgive her-":
            m "It's alright, [hermione_name]."
            call her_main("Really?","open","surprised", cheeks="blush", tears="messy")
            m "I'm sure you're just a little nervous."
            call her_main("Thank you [genie_name].","clench","worried", cheeks="blush", tears="soft")
            call her_main("I promise to try harder next time.","scream","worriedCl", cheeks="blush", tears="messy")

            jump end_hg_pf_strip



### Tier 3 ###

label hg_pf_strip_T3_fingering:

    call hg_pf_strip_fingering_intro

    call set_her_action("covering_top")
    call ctc

    call play_music("playful_tension") # SEX THEME.
    g9 "Nice..."
    call her_main("........","grin","ahegao")

    call her_main("A-ha... {image=textheart}ah...","open","worriedCl")
    call her_main("Ah... {image=textheart}-aha...","open","worriedCl")
    m "..."
    call her_main("Ah-ah...","open","worriedCl")
    m "......................"
    call her_main("Ah... ah...{image=textheart}","open","worriedCl")
    call her_main("Ah... [genie_name]?","soft","squintL")
    m "What is it?"
    call her_main("Ah... Do you.... like this?","open","worriedCl")
    m "Do I like watching \"you\" finger your slutty little pussy?"
    m "Very much so, [hermione_name]. Why?"
    call her_main("{image=textheart}{image=textheart}{image=textheart}","normal","worriedCl")
    call her_main("Ah... You're just so quiet...","open","worriedCl")
    m "Do you need a little more encouragement?"
    call her_main("Ah... yes... please....{image=textheart}","open","worriedCl")
    m "Tch... You nasty whore!"
    call her_main("yes [genie_name], ah...{image=textheart}","grin","ahegao_mad", cheeks="blush")
    call her_main("please... ah... more...{image=textheart}","grin","angry", cheeks="blush")
    g4 "You need to be punished for being such a slut!"
    call her_main("yes, [genie_name]... punish me...","open","ahegao_raised", cheeks="blush")
    call her_main("make me your little slut....","open","ahegao_raised", cheeks="blush")
    call her_main("I will... ah... {image=textheart}do anything... ah...{image=textheart}","silly","dead")
    m "Anything [hermione_name]?"
    call her_main("Ah-a...{image=textheart} yessss...","silly","ahegao_raised", cheeks="blush")
    m "Cum."
    $ hermione_squirt = True
    call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","silly","dead", cheeks="blush")
    call cum_block

    $ hermione_squirt = False
    call her_main("Ah...{image=textheart}...{image=textheart}","grin","ahegao")
    call her_main("Ah... ah...{image=textheart}","silly","ahegao")
    call her_main("...{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
    call her_main("*heavy panting*","open_wide_tongue","ahegao")
    call her_main("[genie_name]...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
    call her_main(".............","soft","ahegao")
    call nar(">Hermione takes a minute to collect herself.")
    m "You feeling alright?"
    call her_main("Yes, [genie_name]... I just need a little longer...","shock","baseL", cheeks="blush", tears="soft")
    m "take your time."
    call her_main("ah... {image=textheart}","silly","worried", cheeks="blush", tears="soft")

    jump end_hg_pf_strip



### Tier 4 ###

label hg_pf_strip_T4_fingering:
    $ hg_fingering_trigger = True

    m "[hermione_name]?"
    call her_main("[genie_name]?","base","base")
    m "You don't mind pleasuring yourself in front of me, do you?"
    if her_whoring <= 16:
        call her_main("As long as I am being paid...","grin","baseL")
        m "That's the spirit!"
    else:
        call her_main("I mean I have done it once today already...","grin","baseL")
        m "Once more for good luck then!"
        call her_main("If you insist...{image=textheart}","open","baseL", cheeks="blush")

        call hg_masturbate_3
        call hg_masturbate_3_cumming

    call her_main("...","base","glance")
    call set_her_action("covering")

    stop music fadeout 3.0
    call her_main("Do you like it when I do it like this, [genie_name]?","grin","baseL")
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    m "Yes, yes, like that..."
    m "Try going a little deeper with your fingers."
    call her_main("Alright [genie_name]...","base","happyCl")
    $ hermione_dribble = True
    call her_main("Ah... ah...{image=textheart}","open","worriedCl")
    call her_main("Ah... [genie_name]...{image=textheart}","open","worriedCl")

    menu:
        m "..."
        "\"What are you thinking about?\"":
            call her_main("Huh?","open","worriedCl", cheeks="blush")
            call her_main("Oh, um... nothing...","upset","worriedCl", cheeks="blush")
            m "[hermione_name]..."
            call her_main("[genie_name], please, it's too embarrassing...","disgust","down_raised", cheeks="blush")
            g4 "Well now I have to hear it."
            call her_main("OK... but you have to promise not to tell anyone!","open","baseL", cheeks="blush")
            m "Witcher's honor."
            call her_main("......","annoyed","annoyed")
            m "[hermione_name]..."
            call her_main("Alright. If you must know... I'm remembering the time I corrected professor Snape about the ingredients of a Hiccoughing potion.","open","down")
            m "....."
            call her_main("ah...{image=textheart}","soft","ahegao")
            call set_her_action("pinch")

            call her_main("It was ah... {image=textheart} in front of the entire class as well.")
            call set_her_action("covering")

            call her_main("He refused to let me answer any questions for a week after that.","base","down")
            call her_main("But it was worth it...","soft","squintL")
            call her_main("The look on his face when he realised he was wrong...{image=textheart}","soft","ahegao")
            call set_her_action("pinch")

            call her_main("a-ah...{image=textheart}")
            call set_her_action("covering")

            call her_main("It just felt so good!{image=textheart}","grin","dead")
            m "OK, I think that's enough..."
            call her_main("Was it too much?","angry","wink")
            m "Let's just get back to business shall we?"
            call her_main(".................","soft","ahegao")
            call nar(">Hermione keeps on plunging her fingers into herself.","start")
            call nar(">She is doing a great job of it too.","end")
            m "Yes, yes... Like that."

        "\"You really are a shameless slut, aren't you?\"":
            call her_main("Yes...","soft","ahegao")
            call set_her_action("pinch")

            call her_main("ah... {image=textheart}","silly","dead")
            call her_main("I don't know if it's the time I'm spending with you...{image=textheart}","angry","wink")
            call her_main("Or if i've always been this way...{image=textheart}","angry","down_raised")
            call her_main("But... {image=textheart} ah... {image=textheart} I'm a slut [genie_name]...{image=textheart}","soft","ahegao")
            call her_main("A shameless slut...","grin","dead")
            call her_main("That pleasures herself...{image=textheart} ah...","soft","ahegao")
            call her_main("Just to make her headmaster happy...","grin","dead")
            m "Oh, yes..."
            call her_main("That's it [genie_name]...","base","down")
            call her_main("Enjoy yourself while I stand here...","silly","dead")
            call her_main("Ah...{image=textheart}","open_wide_tongue","ahegao")
            call her_main("Fingering my pussy...","silly","ahegao")
            call her_main("Ah... ah...{image=textheart}","grin","ahegao")
            call her_main("Ah... Do you.... like this [genie_name]?","shock","worriedCl")
            call her_main("Watching me Ah...{image=textheart} degrade myself?","silly","dead")
            m "Very much, [hermione_name]. Just keep going..."
            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","dead")

        "\"Play with your tits some more!\"":
            call her_main("Hm?","soft","ahegao")
            call her_main("alright... if you insist...","open","baseL", cheeks="blush")
            call set_her_action("pinch")

            call her_main("ah...{image=textheart}","angry","wink")
            m "Now lift them up."
            call her_main("[genie_name]...","open","squint", cheeks="blush")
            m "do it, [hermione_name]."
            call her_main("...","open","baseL", cheeks="blush")
            call set_her_action("lift_breasts_naked")

            call her_main("Mmmm...","grin","ahegao_mad", cheeks="blush")
            m "That's it..."
            call nar(">You stare at Hermione's breasts with hunger...")
            call her_main("ah...","silly","dead")
            m "So do you like playing with those tits of yours, [hermione_name]?"
            call her_main("I do, [genie_name]... ah...{image=textheart}","soft","ahegao")
            call her_main("I don't know why...","base","baseL", cheeks="blush")
            call set_her_action("pinch")

            call her_main("But I love it...{image=textheart}{image=textheart}","base","down")
            m "You nasty slut!"
            call her_main("Ah...{image=textheart} ah-a...{image=textheart}","open_wide_tongue","ahegao")
            call her_main("I am...")
            call her_main("A nasty slut... Ah...{image=textheart}","silly","dead")
            m "You are a disgrace, [hermione_name]!"
            call her_main("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")


    m "Why don't you come down and I'll help you with it?"
    call her_main("...","base","down")



    # Hermione climbs off your desk.
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    pause 2

    ">Hermione slowly climbs down desk and stands in front of you."
    pause.5

    call hg_chibi_transition("admire_breasts") # Replace with naked chibi

    #show screen desk
    #show screen chair_left
    hide screen genie
    $ gen_chibi_xpos = -77
    $ gen_chibi_ypos = 13
    $ g_c_u_pic = "characters/hermione/chibis/grope_ass/front_e_01.png"
    show screen g_c_u

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call set_her_action("lift_breasts_naked")
    call her_main("..............","base","ahegao_raised", cheeks="blush")

    menu:
        m "..."
        "-Grab her tits-":
            call nar(">You reach forward and grab a hold of her supple breasts.")
            $ g_c_u_pic = "groping_naked_tits_ani"
            call set_her_action("fingering")

            call her_main("[genie_name]!","shock","worriedCl")
            call her_main("This wasn't part of the deal!","open","worriedCl")
            call her_main("I don't think we should...","annoyed","angryL", cheeks="blush")
            m "Don't worry [hermione_name], You can keep playing with yourself."
            m "This is just to hurry things along."
            call her_main("Ah...{image=textheart} Well, as long as it's just to make this end faster...","open","ahegao_raised", cheeks="blush")
            call her_main("I suppose I can... ah{image=textheart} allow it...","base","baseL", cheeks="blush")
            call nar(">You give her tits a couple of firm squeezes...")
            m "Just admit that you love it."
            call her_main("Ah... fine...{image=textheart}","open","worriedCl", cheeks="blush")
            call her_main("{size=-5}I like it...{/size}","soft","ahegao")
            m "What was that [hermione_name]?"
            call her_main(".......")
            call her_main("I love this...","grin","dead")
            call her_main("Standing here... playing with myself...","base","down")
            call her_main("Ah... while you play with me...{image=textheart}","grin","ahegao_mad", cheeks="blush")
            m "Heh... Nice."
            call her_main("Ah...{image=textheart}","open","ahegao_raised", cheeks="blush")
            call her_main("I sometimes wish I could spend all day in here...","grin","angry", cheeks="blush")
            m "Mmmm"
            call nar(">You keep on massaging the girl's breasts...")
            call her_main(".......")
            call her_main("[genie_name]... I know it's greedy of me...","base","baseL", cheeks="blush")
            call her_main("ah...{image=textheart}","base","down")
            call her_main("but could you touch me... down there...","open","squint", cheeks="blush")
            m "What's was that [hermione_name]? You'll have to speak up."
            call her_main("Please finger me...","open","ahegao_raised", cheeks="blush")
            m "Once more, a little louder this time."
            call her_main("Ah...{image=textheart} {size=+5}please finger my cunt!{/size}","grin","ahegao_mad", cheeks="blush")
            $ g_c_u_pic = "groping_06"
            call nar(">You swiftly plunge two fingers into her dripping pussy.")
            call set_her_action("lift_breasts_naked")
            call her_main("{image=textheart}{image=textheart}{size=+5}!!!{/size}{image=textheart}{image=textheart}","silly","ahegao")

        "-Finger her-":
            $ g_c_u_pic = "groping_06"
            call nar(">You run your hands up and down Hermione's legs...")
            call her_main("!!!","open","worriedCl")
            call nar(">And slowly move your hands towards her pussy...")
            call her_main(".................","silly","dead")
            m "That's it [hermione_name]..."
            call her_main("{size=-7}[genie_name]...{/size}","soft","ahegao")
            m "Shhh. Just play with your tits."
            call her_main("...fine, [genie_name]...","base","ahegao_raised", cheeks="blush")
            m "Good girl."
            call her_main("....................","base","closed")
            m "Just be quiet..."
            call nar(">you enjoy the sensation of gently stroking the inside of her thighs...")
            m "as my hands explore you"
            m "your thighs..."
            call nar(">your start kneading the flesh of her thighs, moving ever closer to her dripping cunt")
            m "your big, firm ass"
            call nar(">You move around and squeeze her ass gently...")
            call her_main(".....................","grin","ahegao")
            m "your loins..."
            call nar(">You move one hand back around, and start circling just above her clit.")
            call her_main(".....................{size=-8}[genie_name]...{/size}","silly","dead")
            m "What was that, [hermione_name]?"
            call her_main(".....................","annoyed","wink", cheeks="blush")
            call her_main("...i... {size=-5}...i need you... inside of me...{/size}","disgust","down_raised", cheeks="blush")
            m "You'll have to speak up if you expect me to hear you..."
            call her_main("I... ah...{image=textheart} need...","open","ahegao_raised", cheeks="blush")
            call nar(">You swiftly plunge two fingers into her drenched snatch.")
            call her_main("!!!{image=textheart}{image=textheart}","grin","ahegao")
            call nar(">you start to pump your fingers inside her before she can do more than gasp")
            call her_main("{size=+10}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}","silly","dead")
            m "That's it [hermione_name]. Just enjoy yourself."
            call her_main("..................................................","base","ahegao_raised", cheeks="blush")
            m "do you like this?"
            m "you like it when i finger your cunt?"
            call her_main("i love it!{image=textheart} i love your fingers in my tight, wet pussy!!{image=textheart}","silly","ahegao")
            m "well, i think we can do better."
            call nar(">with your other hand, you start rubbing the base of your palm against her clit.")
            call her_main("{size=+10}!!!{/size}","open","ahegao_raised", cheeks="blush")


    call nar(">you don't even need to move as she pounds herself against your fingers.")
    call her_main("ah...{image=textheart} please...{image=textheart} keep...{image=textheart}","silly","dead","blush")
    call her_main("fingering my cunt!{image=textheart}{image=textheart}","silly","ahegao","blush")
    g9 "As you command!"
    call nar(">you force another finger into her pussy!")
    call her_main("ah yes... {image=textheart}iloveitiloveitiloveit","grin","ahegao","blush")
    m "what do you love, [hermione_name]?"
    call her_main("ah!!{image=textheart} I love your fingers in my pussy [genie_name]!{image=textheart}","open_wide_tongue","ahegao","blush")
    call nar(">her movements are becoming more frantic")
    m "are you cumming, [hermione_name]?"
    call her_main("ah...{image=textheart} yes!!","grin","ahegao")
    call her_main("I'm cumming [genie_name]!!{image=textheart}","grin","dead")
    call her_main("I'm cumming from being fucked with your fingers!!{image=textheart}{image=textheart}","grin","ahegao_mad", cheeks="blush")
    m "show me your tits [hermione_name]!"
    m "I want to see you cum while you play with them."
    $ hermione_squirt = True
    call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}","silly","dead", cheeks="blush")
    call cum_block

    $ hermione_squirt = False
    call her_main("Ah...{image=textheart}...{image=textheart}","grin","ahegao")
    call her_main("Ah... ah...{image=textheart}","silly","ahegao")
    call her_main("...........","silly","ahegao")
    call her_main("........................","silly","ahegao")

    call nar(">You release her...")
    $ g_c_u_pic = "characters/hermione/chibis/grope_ass/front_e_01.png"
    m "This will do for now [hermione_name]."

    jump end_hg_pf_strip
