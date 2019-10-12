

### Hermione Titjob ###

label hg_pf_titjob:

    if hg_pf_titjob.counter == 0:
        m "{size=-4}(Should I ask her for a titjob?){/size}"
    else:
        g9 "{size=-4}(I feel like putting my cock between those tits again!){/size}"

    if hg_pf_titjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 45
    $ hg_pf_titjob.start()


    # End Event
    label end_hg_pf_titjob:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3
    
    $ face_on_cg = False
    hide screen ccg
    hide screen g_c_c_u

    # Update Hermione
    $ temp_save = aftersperm # Save
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    call set_her_action("none","update") #Resets clothing.
    $ aftersperm = temp_save # Load

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if her_mood != 0:
        call her_main("", "annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans="fade")
    else:
        call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")


    # Points
    if her_tier <= 5:
        m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"."
        $ gryffindor += current_payout
    else:
        m "You may leave now, [hermione_name]."

    call her_main("Thank you, [genie_name]...", "soft", "base", "base", "R")

    if daytime:
        her "Classes are about to start..."
    else:
        her "It's getting late..."
    her "I'd better go now..."


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 5:
        if her_whoring < 21: # Points til 21
            $ her_whoring +=1
    if her_tier == 6:
        if her_whoring < 24: # Points til 24
            $ her_whoring += 1

    jump end_hermione_event



### Fail Events ###

label hg_pf_titjob_fail:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "[hermione_name]..."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Have you ever given somebody a \"titjob\"?"

    $ hg_pf_titjob.counter -= 1

    jump too_much



### Tier 1 ###

# Event 1 (i) - Hermione wants 100 house points for it!
# Event 2 (r) - Reluctantly does it again.

label hg_pf_titjob_T1_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "Now, [hermione_name]..."
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "Have you ever given someone a \"titjob?\""
    call her_main("A \"titjob?\"", "annoyed", "narrow", "annoyed", "mid")
    m "It's where you wrap those \"fat tits\" of yours around a cock,..."
    g9 "And then shake them up and down, and up and...{w=0.5}{nw}"
    call her_main("[genie_name]!", "angry", "base", "angry", "mid")
    m "So have you ever given a boy a titjob?"
    call her_main("...............", "disgust", "narrow", "base", "mid_soft")
    call her_main("{size=-7}No...{/size}","angry","worriedCl", emote="05")
    m "*Hmmm?*... What was that?"
    call her_main("Of course I haven't...", "open", "narrow", "angry", "R")
    g9 "Well then, today is your lucky day!"
    call her_main("Lucky? In what way would you consider it lucky?", "disgust", "narrow", "base", "mid_soft")
    m "It's not every day that you learn something new."
    call her_main("I'm at a school... I get taught hundreds of things each day...", "annoyed", "base", "angry", "mid")
    call her_main("And giving \"titjobs\" isn't one of them...", "angry", "base", "angry", "mid")
    m "At least this is something you'll be able to use in the real world."
    call her_main("If you say so, [genie_name]...", "annoyed", "narrow", "angry", "R")
    call her_main("{size=-7}I want 100 points for this...{/size}","angry","worriedCl", emote="05")
    m "Speak up, [hermione_name]."
    call her_main("I want 100 points!","scream","worriedCl")
    call her_main("", "annoyed", "narrow", "angry", "R")

    label back_to_titjob_choices:
    menu:
        m "(...)"
        "\"You'll get 15 house points.\"" if her_mood == 0:
            $ her_mood += 7
            call her_main("[genie_name], are you seriously expecting me to give you a titjob...", "angry", "closed", "angry", "mid")
            call her_main("For 15 meagre points?!", "scream", "base", "angry", "mid")
            call her_main("", "clench", "base", "angry", "mid")
            m "How about 20? Does that sound fair?"
            call her_main("I don't know who you think I am, but I'm not doing something like this for only 15 points!", "open", "base", "angry", "mid")
            m "I promise I won't even cum on them..."
            call her_main("And you believe that \"that\" would change my mind?", "scream", "base", "angry", "mid")
            m "I had hoped so..."
            call her_main("No.{w} You need to make me a better offer...or I'll be leaving...", "annoyed", "narrow", "angry", "R")
            m "Fair enough..."
            jump back_to_titjob_choices

        "\"You'll get 45 house points.\"":
            call her_main("45 house points...?", "open", "wink", "base", "mid")
            call her_main("This could put \"Gryffindor\" back in the lead...", "annoyed", "narrow", "worried", "down")
            m "So,...is that a yes?"
            call her_main("That is a yes, [genie_name]...", "open", "closed", "base", "mid")
            call her_main("45 points seem like a fair amount for-...", "open", "base", "base", "R")
            g9 "For a titjob!"
            call her_main("(...)", "annoyed", "base", "angry", "mid")

        "\"You'll get 100 house points.\"":
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ current_payout = 100
            $ her_mood = 0
            call her_main("100 house points?!","scream","wide_stare")
            call her_main("This might be enough to put \"Gryffindor\" in the lead!", "smile", "wide", "base", "stare")
            m "So,...is that a yes?"
            call her_main("Yes, [genie_name]!", "smile", "happyCl", "base", "mid")
            call her_main("I shall do my best...", "soft", "narrow", "base", "mid_soft", emote="06")

    jump hg_pf_titjob_1


label hg_pf_titjob_T1_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "[hermione_name], would you like to earn some house points again?"
    call her_main("Of course, [genie_name]...", "base", "base", "base", "mid")
    call her_main("What would I have to do to earn them?", "open", "base", "base", "R")
    g9 "Nothing you aren't already experienced with!"
    m "I'm just going to rub my cock between those precious little tits of yours..."
    call her_main("This again...", "angry", "closed", "angry", "mid")
    call her_main("(...)", "annoyed", "narrow", "angry", "R")
    call her_main("For 45 house points?", "open", "base", "angry", "mid")
    m "45 house points, as always..."
    call her_main("(...)", "annoyed", "narrow", "angry", "R")
    call her_main("Very well, [genie_name]", "open", "closed", "base", "mid")
    call her_main("But you have to promise me that you'll make it quick...", "annoyed", "base", "angry", "mid")
    g9 "..............."

    jump hg_pf_titjob_1



### Tier 2 ###

# Event 1 (i) - Event with a couple of choices.
# Event 2 (i) - Some new interactions.
# Event 3 (r) - Repeat.

label hg_pf_titjob_T2_intro_E1:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "How do you feel about wrapping those nice tits of yours around my cock again?"
    call her_main("Only nice?", "upset", "closed", "base", "mid")
    m "Fine, fine."
    m "How do you feel about wrapping those perfect tits of yours around my cock again?"
    call her_main("Of course, [genie_name].", "base", "narrow", "base", "mid_soft")
    m "You like it when I call them perfect don't you?"
    call her_main(".............", "base", "narrow", "worried", "down")
    g9 "you don't have to say anything, just bring those perfect tits over here."
    call her_main("{image=textheart}{image=textheart}{image=textheart}","base","worriedCl")
    call her_main("yes, [genie_name]...", "grin", "base", "base", "R")

    jump hg_pf_titjob_2


label hg_pf_titjob_T2_intro_E2:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?", "base", "base", "base", "mid")
    m "I would very much like to see those perfect tits of yours again..."
    g9 "See them wrapped around my cock!"
    call her_main("Oh... Again?", "base", "narrow", "worried", "down")
    call her_main("For 45 house points?", "soft", "narrow", "base", "mid_soft")
    m "Yes, [hermione_name]."
    call her_main("(...)", "annoyed", "base", "base", "R")
    call her_main("Very well then...", "smile", "happyCl", "base", "mid")
    g9 "Splendid!"

    jump hg_pf_titjob_2


label hg_pf_titjob_T2_repeat:
    call her_main("", "base", "base", "base", "mid", xpos="mid", ypos="base", trans="fade")
    m "[hermione_name], how would you like wrapping those perfect tits of yours around my cock again?"
    call her_main("As long as I am getting paid...", "soft", "happy", "base", "R")
    g9 "Well, then... Time to earn those points!"
    call her_main("{image=textheart}{image=textheart}{image=textheart}", "base", "narrow", "base", "up")

    jump hg_pf_titjob_2



### First Tier Titjob ###

label hg_pf_titjob_1:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    show screen chair_left
    show screen desk
    call her_chibi("stand","560","base")
    call gen_chibi("jerking_off","450","base")

    hide screen blkfade
    with fade
    pause.8

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "disgust", "narrow", "worried", "down", ypos="head")
    if hg_pf_titjob.counter == 0:
        call her_main("(It's so big...)", "disgust", "narrow", "base", "down")
    m "Get to it, [hermione_name]..."
    call her_main("Right...","angry","worriedCl", emote="05")
    call her_main("", "annoyed", "narrow", "annoyed", "mid")
    pause.1

    # Hermione holds her Breasts.
    call set_her_action("lift_breasts")

    # Setup
    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 5
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with fade

    call hg_chibi_transition("tj_pause", trans="d9")
    call ctc
    #pause.8

    call nar(">Hermione clumsily wraps her tits around your cock...")
    call bld
    m "That's a start. Now, up and down..."
    call her_main("Alright...","angry","worriedCl", emote="05", ypos="head")

    call hg_chibi_transition("tj", trans="d9")
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call bld
    g9 "mmmm..."
    $ ccg1 = 6
    if hg_pf_titjob.counter == 1:
        call her_main("...", "base", "base", "base", "mid")
        call her_main("Does it... feel good?", "base", "happy", "base", "mid")
        m "Good?"
        m "It feels amazing."
        call her_main("Oh...", "base", "happy", "base", "mid")
        call her_main("......")
        call her_main("Thank you [genie_name].", "base", "base", "base", "R")

    call her_main("............", "annoyed", "narrow", "worried", "down")
    call her_main("[genie_name]...?", "soft", "base", "base", "mid")
    m "What is it?"
    $ ccg1 = 7
    call her_main("Promise me you won't cum on my...face...", "upset", "wink", "base", "mid")

    $ d_flag_01 = False #If TRUE Genie promised to warn her.
    menu:
        m "..."
        "\"I promise not to cover that sweet little face of yours...\"":
            $ d_flag_01 = True #If TRUE Genie promised to warn her.
            $ ccg1 = 6
            call her_main("Thank you, [genie_name].", "base", "happy", "base", "mid")
        "\"Hmmmm...{w=0.3} We'll see how I feel later...\"":
            $ ccg1 = 8
            call her_main("*Hmmmmph*...", "annoyed", "narrow", "annoyed", "mid")
            call her_main("At least avoid my hair...","normal","worriedCl")

    $ ccg1 = 5
    call her_main(".............", "disgust", "narrow", "worried", "down")
    m "............."
    call her_main(".............","normal","worriedCl")
    call her_main("Err... [genie_name]?")
    m "Yes, what is it?"
    call her_main("Are you almost...{w=0.3}there?", "open", "base", "base", "mid")
    m "Why?"
    $ ccg1 = 7
    if daytime:
        call her_main("Well, it's just that...{w=0.3}my classes are about to start...", "upset", "wink", "base", "mid")
    else:
        call her_main("Well, it's just that...{w=0.3}I promised Ginny that we'd hang out tonight...", "upset", "wink", "base", "mid")
        call her_main("She's pretty upset that I'm spending so much time in here...")
    m "Do you need the points or not?"
    $ ccg1 = 6
    call her_main("I do, [genie_name]! I'm sorry...","grin","worriedCl")
    call her_main("I'll just keep on stroking it then...")
    m "Well, you could make this finish up a little faster..."
    call her_main("Really? What can I do, [genie_name]?", "base", "base", "base", "R")

    menu:
        m "..."
        "\"Tell me how much you love your tits!\"":
            $ ccg1 = 5
            call her_main("What?", "upset", "wink", "base", "mid", ypos="head")
            $ ccg1 = 6
            call her_main("My breasts?", "disgust", "narrow", "worried", "down")
            m "You know,...how good they feel..."
            m "The looks you receive thanks to them..."
            call her_main("Oh,{w=0.3} okay then...", "base", "base", "base", "mid")
            call her_main("There was this one time in the library...", "smile", "base", "base", "R")
            call her_main("It was empty, apart from this first year boy sitting across from me...")
            m "*Heh*... good.{w=0.3} Go on..."
            call her_main("Well, it was quite hot that day, so I decided to take my vest off...", "base", "happy", "base", "mid")
            g4 "Yes! Very hot indeed..."
            call her_main("He was trying to act sly, but I could tell that he kept sneaking glances at them...", "base", "base", "base", "R")
            call her_main("So I began undoing the buttons... Slowly at first, not enough for him to suspect anything...", "base", "narrow", "base", "mid_soft")
            g9 "*hmmm*... you little slut..."
            $ ccg1 = 9
            call her_main("By the third button, he couldn't take his eyes off me...", "base", "narrow", "worried", "down")
            call her_main("And when I got to the fourth,...I saw him move his hands under the desk...")
            m "Really?"
            call her_main("Yes... I could almost hear him...{w=0.3}\"doing it\"...", "base", "narrow", "base", "up")
            $ ccg1 = 10
            call her_main("I even gave him a glimpse of my bra...", "open", "base", "base", "R")
            g9 "Do you have no shame?"
            $ ccg1 = 5
            call her_main("[genie_name]! I was just trying to cool down...", "base", "narrow", "worried", "down")
            m "I'm just kidding, keep going..."
            call her_main("..............", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 9
            call her_main("By the sixth button my entire bra was unveiled...")
            call her_main("He really must have had a good view of my cleavage...", "base", "base", "base", "mid")
            call her_main("And my...{w=0.3} tits...", "soft", "narrow", "base", "mid_soft")
            call her_main("He just kept staring at them...not even trying to hide what he was doing...")
            $ ccg1 = 10
            call her_main("He shot several ropes of cum under the table, even covering my legs and feet with it!", "open_tongue", "narrow", "annoyed", "up")
            g4 "!!!"
            call her_main("Come on, [genie_name]! Cover me as well! Cum all over my tits!", "grin", "base", "angry", "mid")

        "\"Stick out your tongue!\"":
            $ ccg1 = 5
            call her_main("[genie_name]?", "open", "wink", "base", "mid", ypos="head")
            g4 "Just do it, slut!"
            $ ccg1 = 11
            call her_main("*Uhm*... Like this?", "open_wide_tongue", "narrow", "worried", "down")
            m "Yes, good..."
            m "Now tilt your head down,...as far as it'll go."
            call her_main(".....................", "open_wide_tongue", "base", "base", "mid")
            m "Yes... Good..."
            call her_main("...........", "open_wide_tongue", "base", "base", "mid")
            call her_main("...........")
            $ ccg1 = 9
            call her_main("[genie_name], I can't keep my mouth open for so long...", "open_tongue", "base", "base", "mid")
            call her_main("I'm starting to drool...", "open_wide_tongue", "narrow", "worried", "down")
            g4 "Yes! Drool all over those perfect tits of yours!"
            call her_main("Perfect, you say?", "open_tongue", "base", "base", "mid")
            m "As perfect as any mortal, [hermione_name]!"
            $ ccg1 = 11
            call her_main(".......", "base", "narrow", "base", "up")
            m "Try to get it as close to the tip of my cock as you can..."
            call her_main("............","normal","worriedCl")
            call her_main("A-ha.....", "open_wide_tongue", "base", "base", "mid")
            m "Good, [hermione_name]."
            call her_main("..............", "open_wide_tongue", "base", "base", "mid")
            m "Yes, keep on stroking my cock."
            call nar(">You thrust up as she pushes her tits down causing the tip of your cock to touch her wet tongue.")
            call her_main("..................", "open_wide_tongue", "base", "base", "mid")
            g4 "That's good..."
            call her_main(".................", "open_wide_tongue", "base", "base", "mid")
            pause.2

            call hg_chibi_transition("tj_bj_pause", trans="d9")
            call ctc
            #pause.8

            call nar(">Your thrusts ends up going into her drooling mouth.")
            g4 "That's it, slut! Taste it!"
            call her_main(".....................", "open_wide_tongue", "closed", "angry", "mid")
            m "Yes, you big-titted whore!"
            call her_main("......................", "open_wide_tongue", "base", "angry", "mid")
            g4 "I want to cum in that little slutty mouth of yours..."
            call her_main("................", "open_wide_tongue", "base", "angry", "mid")

    with hpunch
    g4 "{size=-4}(Here it comes! Where should I aim for?){/size}"

    menu:
        m "..."
        "\"(Cum in her mouth!)\"":
            $ her_mood += 3
            call bld
            g4 "Here it comes, [hermione_name]! You better be ready!"
            $ ccg1 = 13

            call hg_chibi_transition("tj_pause", trans="d5")

            call her_main("What? already?!", "shock", "wide", "base", "stare", ypos="head")
            g4 "{size=+5}Yeah, your tits felt great!!!{/size}"
            g4 "{size=+5}You little whore!!!{/size}"
            call her_main("No, [genie_name], wait, not on my face!", "angry", "base", "base", "mid")
            g4 "{size=+5}Open wide, you slut!!{/size}"
            call her_main("Not in my mou-", "scream", "wide", "base", "stare")
            $ ccg1 = 12

            stop music fadeout 1.0
            call cum_block
            call hg_chibi_transition("tj_cumming_in", trans="d9")
            pause.8

            call nar(">You grab the back of Hermione's head and force your cock into her open mouth...")
            call her_main("!!!", "shock", "wide", "base", "stare")
            call cum_block

            g4 "{size=+5}ARGH! YES!!! Take it!{/size}"
            call her_main(".....................","shock","worriedCl")
            call bld("hide")
            call ctc

            call hg_chibi_transition("tj_cumming_in_pause", trans="d9")

            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "*Mmm*... That felt great...."
            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "How are you feeling?"
            call her_main(".......................", "full_cum", "narrow", "worried", "down",cheeks="blush")
            m "[hermione_name]?"
            pause.2

            call hg_chibi_transition("tj_pause", trans="d9")
            pause.5

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 15
            call her_main("*Ptui*...", "open_wide_tongue_cum", "base", "angry", "mid", trans="hpunch")

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True

            $ ccg1 = 16
            call her_main("Why on earth did you cum in my mouth?","angry","worriedCl", emote="05")
            m "well, you did say not to cum on your face..."
            pause.2

            $ ccg1 = 17

            call hg_chibi_transition("tj_cumming_on_pause", trans="d9")
            pause.5

            call nar(">Hermione lets go of your still pulsating cock...")
            call her_main("*Ugh*... You came so much!","angry","worriedCl", emote="05")
            call her_main("I had to swallow most of it...", "disgust", "narrow", "base", "down", emote="05")
            g9 "You did a great job, [hermione_name]!"
            call her_main("I don't want to hear it...", "angry", "narrow", "angry", "R", emote="05")
            if daytime:
                call her_main("I can't go to class like this...","angry","worriedCl", emote="05")
                call her_main("I'm covered in semen...", "disgust", "narrow", "base", "down", emote="05")
            else:
                call her_main("At this hour the \"Gryffindor common room\" will be full of students...","angry","worriedCl", emote="05")
                call her_main("And I'm smelling like spunk!","scream","worriedCl")
                call her_main("I hope I can just run past them without anybody noticing...", "disgust", "narrow", "worried", "down")

            m "You could have swallowed..."
            m "Then there wouldn't have been any clean up."
            call her_main("Swallow? All of that?", "angry", "narrow", "base", "down")
            call her_main("I don't think I have enough room in my stomach...")
            call her_main("Could I please have my points now, [genie_name]?", "soft", "base", "angry", "mid")
            $ aftersperm = True

        "\"(Cover her tits!)\"":
            with hpunch
            call bld
            g4 "ARGH!"
            $ ccg1 = 13

            call hg_chibi_transition("tj_pause", trans="d5")

            call her_main("WHAT?!", "shock", "wide", "base", "stare", ypos="head")
            g4 "Take this slut!"

            stop music fadeout 1.0
            call cum_block
            call hg_chibi_transition("tj_cumming_on", trans="d9")
            pause.8

            call bld
            g4 "{size=+5}ARGH! YES!!!{/size}"

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True
            call her_main("....................","shock","worriedCl")
            call cum_block
            $ ccg1 = 18
            call ctc

            call hg_chibi_transition("tj_cumming_on_pause", trans="d9")

            call her_main(".......................", "angry", "wide", "base", "stare")
            m "Well, I think that's about it..."
            call her_main("..........", "soft", "base", "base", "mid",tears="soft")

            $ ccg1 = 17
            call her_main("[genie_name]! How could you cum so much?!","scream","worriedCl")
            call her_main("(It's like he dumped a bucket load all over my chest...)", "disgust", "narrow", "base", "down")
            if daytime:
                call her_main("I can't attend class looking like this!","angry","worriedCl")
            else:
                call her_main("How am I supposed to go back to the \"Gryffindor common room\" like this?!","angry","worriedCl")
            m "Just wipe it off..."
            call her_main("...........................", "angry", "narrow", "worried", "down")
            call her_main("I would like to get paid now, [genie_name]...", "annoyed", "narrow", "angry", "R")

            $ aftersperm = True

    jump end_hg_pf_titjob



### Second Tier Titjob ###

label hg_pf_titjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    # Setup
    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 6
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with d3

    # Hermione holds her Breasts.
    call set_her_action("lift_breasts")

    $ ccg1 = 20
    call hg_chibi_transition("tj", trans="fade")
    call ctc

    call nar(">Hermione wraps her plump tits around your cock...")
    call her_main("Do you enjoy it when I do it like this, [genie_name]?", "grin", "base", "base", "R", ypos="head")
    call nar(">Hermione starts alternating her breasts as she titfucks you.")
    g9 "Actually...{w=0.3} yes! Very nice!"

    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("...", "base", "narrow", "base", "mid_soft")
    m "Yes, yes, like that..."
    m "*Hmm*... You are getting pretty good at this."
    $ ccg1 = 21
    call her_main("Thank you, [genie_name].", "base", "happyCl", "base", "mid")
    call her_main("I figured with how kind you've been it's the least I could do...")

    menu:
        m "..."
        "\"What do you think of my cock?\"":
            $ ccg1 = 22
            call her_main("Huh?", "open", "base", "base", "mid", ypos="head")
            call her_main("Your cock?","angry","worriedCl", emote="05")
            m "What do you think about-"
            $ ccg1 = 23
            call her_main("It's magnificent!", "upset", "closed", "base", "mid")
            m "go on..."
            call her_main("[genie_name], If you say that I have the perfect tits...", "soft", "narrow", "annoyed", "up")
            call nar(">She squeezes her tits around your cock.")
            $ ccg1 = 22
            call her_main("This, has to be the perfect cock!", "grin", "narrow", "base", "dead")
            g9 "Perfect you say?"
            call her_main("The size...", "soft", "narrow", "worried", "down")
            call her_main("The shape...", "base", "narrow", "worried", "down")
            call her_main("Everything about it...", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 24
            call nar("Hermione tilts her head down and licks the tip of your cock.")
            call her_main("...........", "open_tongue", "narrow", "annoyed", "up")
            $ ccg1 = 23
            call her_main("Perfect taste...", "soft", "narrow", "annoyed", "up")
            m "..."
            $ ccg1 = 25
            call her_main("I think your perfect cock should be shared around the school.", "scream", "closed", "angry", "mid")
            m "Well, I wouldn't go that far-"
            call her_main("Listen to me, [genie_name]!", "angry", "closed", "angry", "mid")
            call her_main("I think it should be worshipped as part of the school curriculum!", "soft", "narrow", "annoyed", "up")
            $ ccg1 = 24
            call her_main("Girls will be required to come in and bask in it's glory!", "open_tongue", "narrow", "annoyed", "up")
            m "OK, I think I've heard enough."
            $ ccg1 = 21

            call hg_chibi_transition("tj_pause", trans="d5")
            pause.8

            call her_main("Too much?", "angry", "wink", "base", "mid")
            m "Yeah, just a bit."
            call her_main("Sorry [genie_name], I got a bit carried away...","angry","worriedCl", emote="05")
            m "No worries. Just keep on massaging it with those big tits of yours."

            call hg_chibi_transition("tj", trans="d5")
            pause.8

            call her_main(".................", "soft", "narrow", "annoyed", "up")
            call nar(">Hermione keeps on stroking your cock.","start")
            $ ccg1 = 25
            call nar(">Letting some spit dribble down to help lubricate it.","end")
            $ ccg1 = 21
            m "Yes, yes...{w=0.3} That's it, slut!"

        "\"Call yourself a big-titted whore!\"":
            $ ccg1 = 22
            call her_main("Excuse me?", "open", "base", "base", "mid", ypos="head")
            $ ccg1 = 23
            call her_main("Oh...{w} I am a big-titted whore!", "soft", "narrow", "annoyed", "up")
            m "Good. Glad we established that."
            m "Now I want you to say..."

            menu:
                m "..."
                "\"I am a shameless cumslut!\"":
                    $ ccg1 = 22
                    call her_main("Of course.", "base", "narrow", "worried", "down", ypos="head")
                    $ ccg1 = 24
                    call her_main("I am a shameless cumslut.", "soft", "narrow", "annoyed", "up")
                    $ ccg1 = 21
                    call her_main("A dirty little slut who's addicted to the taste of my headmaster's cum...", "grin", "narrow", "base", "dead")
                    m "Yes! Good!"

                "\"I love being covered in cum!\"":
                    $ ccg1 = 24
                    call her_main("I love being covered in cum!", "soft", "narrow", "annoyed", "up", ypos="head")
                    call her_main("hot...")
                    call her_main("sticky...")
                    call her_main("smelly...")
                    call her_main("cum...")
                    $ ccg1 = 23
                    call her_main("...................................", "grin", "narrow", "base", "dead")
                    $ ccg1 = 21
                    call her_main("How was that, [genie_name]?", "angry", "wink", "base", "mid")
                    m "Perfect."

        "\"This is really good. Did you practice?\"":
            $ ccg1 = 22
            call her_main("*Hmm?*...", "base", "happyCl", "base", "mid", ypos="head")
            $ ccg1 = 21
            call her_main("Sort of...{w=0.3} Well not on another cock...", "angry", "wink", "base", "mid")
            m "On what then?"
            $ ccg1 = 22
            call her_main("Well, I spoke to Ginny...", "grin", "base", "base", "R")
            m "A friend of yours?"
            call her_main("yes. I asked if she had any tips for this sort of thing...", "base", "base", "base", "R")
            $ ccg1 = 21
            call her_main("She said the best way to improve was practice...", "base", "happy", "base", "mid")
            m "Practice on what?"
            $ ccg1 = 22
            call her_main("On Ginny", "smile", "base", "base", "R")
            $ ccg1 = 23
            call her_main("Well,...on her arm...", "angry", "wink", "base", "mid")
            m "You tit-fucked your friend's arm?"
            $ ccg1 = 25
            call her_main("Just as practice!","grin","worriedCl", emote="05")
            $ ccg1 = 22
            call her_main("She even gave me some tips...")
            $ ccg1 = 23
            call her_main("How does this feel?", "base", "narrow", "worried", "down")
            m "*Mmm*... Yes, this feels quite good."
            call her_main("Does it?", "angry", "wink", "base", "mid")
            $ ccg1 = 21
            call her_main("Ginny seemed to enjoy it a lot as well...", "base", "narrow", "base", "up")
            g4 "She enjoyed it?"
            $ ccg1 = 22
            call her_main("Of course she did!", "base", "happyCl", "base", "mid")
            $ ccg1 = 23
            call her_main("Who wouldn't love feeling my perfect tits...", "base", "closed", "base", "mid")
            call her_main("Although I think she might have enjoyed it...", "open", "narrow", "worried", "down")
            $ ccg1 = 22
            call her_main("A little too much...", "soft", "happy", "base", "R")
            m "How so?"
            call her_main("Well...", "soft", "happy", "base", "R")
            call her_main("She might have started...")
            $ ccg1 = 23
            call her_main("Playing with herself...", "grin", "narrow", "annoyed", "up")
            with hpunch
            with kissiris
            g4 "Yes, keep going slut"
            call her_main("As I was \"Practising\" on her arm she might have...", "open", "base", "base", "R")
            $ ccg1 = 24
            call her_main("cum...", "soft", "narrow", "annoyed", "up")
            g4 "[hermione_name], you little slut!"
            $ ccg1 = 23
            call her_main("It was just practice!","grin","worriedCl", emote="05")
            call her_main("Err... I mean...", "angry", "wink", "base", "mid")
            $ ccg1 = 21
            call her_main("It's not like I enjoyed it as well...", "angry", "narrow", "base", "down")
            m "Yes, yes... you're not a slut at all..."
            m "*Mmm*... Why don't you spit on it a little..."
            m "Oh, yes..."
            $ ccg1 = 24
            call her_main("...............", "base", "narrow", "worried", "down")

    if hg_pf_titjob.points == 1:
        jump hg_pf_titjob_2_cumming
    else: # Repeat
        jump hg_pf_titjob_2_continue


label hg_pf_titjob_2_continue:
    call hg_chibi_transition("tj", trans="d5")

    call bld
    m "Yes... Keep stroking it."
    $ ccg1 = 23
    call her_main("..............", "angry", "wink", "base", "mid", ypos="head")
    m "Now I want you to say..."

    menu:
        m "..."
        "{size=-4}\"I love teasing my father with my big tits.\"{/size}":
            $ ccg1 = 25
            call her_main("I do not!", "angry", "narrow", "base", "down", ypos="head")
            m "I know. Just say it."
            $ ccg1 = 22
            call her_main("My father? That's gross, [genie_name]! How could you suggest that I want to fu-", "soft", "narrow", "annoyed", "up")
            m "Come on... Just make something up."
            call her_main("...........", "angry", "wink", "base", "mid")
            call her_main("Well...", "open", "narrow", "worried", "down")
            $ ccg1 = 21
            call her_main("Sometimes when I hug him...")
            call her_main(".......")
            m "Go on [hermione_name]..."
            $ ccg1 = 22
            call her_main("I press my tits into him...", "soft", "narrow", "annoyed", "up")
            m "Do you think he enjoys it?"
            call her_main("I'm not sure...", "annoyed", "base", "base", "mid")
            call her_main("I think so...", "soft", "happy", "base", "R")
            $ ccg1 = 23
            call her_main("He always seems to cover his crotch afterwards...", "base", "closed", "base", "mid")
            call her_main("He even says I'm too old for hugs...", "annoyed", "closed", "base", "mid")
            call her_main("But I make sure to give him a big one every night before I go to bed...")
            call her_main("So that he'll think of me...", "base", "narrow", "worried", "down")
            call her_main("And how good I felt...", "grin", "narrow", "base", "dead")
            $ ccg1 = 24
            call her_main("Pressing into him...", "soft", "narrow", "annoyed", "up")
            m "That's it slut."
            $ ccg1 = 22
            call her_main("Then I give him a kiss on the forehead...", "soft", "happy", "base", "R")
            $ ccg1 = 23
            call her_main("Making sure that he can see down my blouse...","grin","worriedCl", emote="05")
            call her_main("{image=textheart}{image=textheart}{image=textheart}")
            $ ccg1 = 25
            call her_main("But all of that is not true of course!", "open", "base", "base", "mid")
            $ ccg1 = 22
            call her_main("None of that happens! It was just for you to imagine!")
            m "Right..."

        "{size=-4}\"I love teasing my schoolmates with my perfect tits.\"{/size}":
            $ ccg1 = 23
            call her_main("I love teasing my schoolmates with my perfect tits...", "soft", "narrow", "annoyed", "up", ypos="head")
            m "Of course you do..."
            call her_main("I love the jealous looks from the other girls...", "base", "narrow", "worried", "down")
            m "I bet they're jealous..."
            $ ccg1 = 21
            call her_main("I love teasing Ron and harry during breakfast...", "base", "narrow", "base", "mid_soft")
            $ ccg1 = 22
            call her_main("Sometimes I'll walk around with only one button done up...", "base", "squint", "base", "mid")
            $ ccg1 = 23
            call her_main("Other times I'll just wear my vest with nothing on underneath...")
            m "And how do you feel..."
            call her_main("So good...", "silly", "narrow", "base", "dead")
            call her_main("One time when I was walking back from your office at night I was barely covering them...", "angry", "wink", "base", "mid")
            call her_main("And as I rounded a corner...", "soft", "narrow", "annoyed", "up")
            $ ccg1 = 24
            call her_main("A second year boy ran head first into them...", "grin", "narrow", "annoyed", "up")
            m "Head first into your tits?"
            call her_main("All I could see was the top of his head...", "grin", "narrow", "base", "dead")
            m "What did he do?"
            call her_main("He tried to pull away...")
            m "Tried?"
            $ ccg1 = 22
            call her_main("Well I may have held him there...", "base", "narrow", "base", "mid_soft")
            call her_main("Just for a little bit...", "base", "narrow", "worried", "down")
            $ ccg1 = 23
            call her_main("Just to tell him it was okay...", "base", "squint", "base", "mid")
            m "You little slut."
            $ ccg1 = 22
            call her_main("I think I might have broken him though...", "base", "narrow", "worried", "down")
            $ ccg1 = 21
            call her_main("Because when I let him go he said nothing. He just stepped back slowly and walked away.", "soft", "narrow", "annoyed", "up")
            m "I bet I know where he went..."
            $ ccg1 = 23
            call her_main("so do i...", "soft", "narrow", "annoyed", "up")

    jump hg_pf_titjob_2_cumming


label hg_pf_titjob_2_cumming:
    call hg_chibi_transition("tj", trans="d5")

    call bld
    m "*Hmm*..."
    m "I love your slutty tits.!"
    $ ccg1 = 22
    call her_main("Thank you [genie_name].", "soft", "narrow", "annoyed", "up", ypos="head")
    $ ccg1 = 23
    call her_main("Shall I rub them some more then?")
    call nar(">Hermione presses her tits together against your cock and starts rubbing it very quickly...")
    m "Oh yes!!!"
    stop music fadeout 1.0
    g4 "{size=-5}(Almost there! where should I aim?){/size}"

    menu:
        m "..."
        "\"(In her mouth).\"":
            call bld
            g4 "Take this, whore!"
            $ ccg1 = 25
            call her_main("What are you-", "angry", "wink", "base", "mid", ypos="head")

            call hg_chibi_transition("tj_bj_pause", trans="d5")
            pause.8

            call bld
            call nar(">You thrust up into Hermione's wet mouth, the sensation of it driving you over the edge.")
            call cum_block
            g4 "{size=+5}ARGH! YES!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 26

            call hg_chibi_transition("tj_cumming_in", trans="d5")
            pause.8

            call her_main("!!!!!!!!!!!", "full", "wide", "base", "stare")
            g4 "Argh! You whore!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}", "full_cum", "narrow", "base", "dead")
            call cum_block

            g4 "Argh! you big-titted slut! Take it all!"
            call her_main("...............", "full_cum", "narrow", "base", "dead")
            m "............"

            call hg_chibi_transition("tj_cumming_in_pause", trans="d5")
            pause.8

            call bld
            m "Ok, I think I am done..."
            call her_main("..............", "full_cum", "narrow", "base", "dead")
            call her_main("........", "full_cum", "narrow", "base", "dead")
            call her_main("...", "full_cum", "narrow", "base", "dead")

            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            $ ccg1 = 27
            call her_main("*GULP*","cum","worriedCl") #play noise here

            call hg_chibi_transition("tj_idle", trans="d5")
            pause.8

            call bld
            call nar(">Hermione releases your cock from between her tits.")

            if daytime:
                call her_main("Well, I think I'd better go now... my Classes are about to begin.", "base", "base", "base", "mid")
            else:
                call her_main("Well, I think I'd better go now... It's getting late.", "base", "base", "base", "mid")
            m "So you're fine with swallowing now?"
            call her_main("What?", "open", "narrow", "worried", "down")
            call her_main("Oh. I suppose so...", "grin", "base", "base", "R")
            call her_main("I mean it doesn't taste that bad and it means that I don't have to clean up afterwards.", "base", "happyCl", "base", "mid")
            m "Hm... Are you sure you don't want people seeing your tits covered in cum..."
            call her_main("What? Walk around school covered in your cum, [genie_name]?", "angry", "wink", "base", "mid")

            if her_tier < 6:
                call her_main("With all due respect, [genie_name]...", "upset", "closed", "base", "mid")
                call her_main("I don't plan on getting a reputation as a cum-loving whore...", "angry", "wink", "base", "mid")
                call her_main("Not like those \"Slytherin\" girls...", "angry", "narrow", "angry", "R")
            else:
                call her_main("*Hmm*...", "soft", "happy", "base", "R")
                call her_main("Maybe if you ask nicely...", "soft", "narrow", "base", "mid_soft")
            call her_main("Will that be all, [genie_name]?", "base", "closed", "base", "mid")
            $ aftersperm = False

        "\"(On her tits).\"":
            call hg_chibi_transition("tj_pause", trans="d5")

            call bld
            g4 "Here! Take this you big-titted whore!"
            with hpunch
            g4 "ARGH!"
            $ ccg1 = 25
            call her_main("What? Already?!", "shock", "wide", "base", "stare", ypos="head")
            g4 "Yeah, your tits felt great slut!"
            call cum_block

            call hg_chibi_transition("tj_cumming_on", trans="d9")
            pause.8

            call bld
            g4 "{size=+5}ARGH! YES!!!{/size}"
            $ ccg1 = 30

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True
            call her_main("!!!!!!!!!!!", "shock", "wide", "base", "stare")

            $ ccg1 = 31
            call her_main(".......................", "angry", "wide", "base", "stare")

            $ ccg1 = 32
            call hg_chibi_transition("tj_cumming_on_pause", trans="d9")
            pause.8

            call bld
            m "*Aghhh*... I feel so much better now..."
            $ ccg1 = 33
            call her_main(".......................", "base", "narrow", "base", "down")

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 35
            call her_main("[genie_name]!","open","worriedCl")
            m "What?"
            call her_main("You covered my chest in cum...","angry","worriedCl")
            $ ccg1 = 34
            call her_main("There's so much...", "open", "base", "base", "R")
            m "It's your fault, [hermione_name]!"
            call her_main("My fault?", "angry", "base", "base", "mid")
            m "Yes! It's those perfect tits of yours..."
            m "They just felt too good..."
            $ ccg1 = 36
            call her_main("Oh...", "shock", "wide", "base", "stare")
            call her_main("Well, I suppose it's not too bad then...", "soft", "narrow", "base", "down")
            $ ccg1 = 37
            call her_main("I'll just wipe it off and hope that nobody will notice...", "upset", "closed", "base", "mid")
            m "You could lick them clean..."
            call her_main("You want me to lick your cum off my tits?", "soft", "narrow", "annoyed", "up")
            call her_main("I don't think so, [genie_name]...", "soft", "narrow", "annoyed", "up")
            call her_main("{size=-5}Maybe next time...{/size}", "soft", "base", "base", "R")
            call her_main("Will that be all, [genie_name]?", "base", "closed", "base", "mid")
            $ aftersperm = True

    jump end_hg_pf_titjob
