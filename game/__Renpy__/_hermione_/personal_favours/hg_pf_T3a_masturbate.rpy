

### Masturbate ###

label hg_pf_strip_fingering_intro:

    # Intro
    if hg_masturbated.trigger == False:
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "base", "base", "base", "mid", xpos="mid", ypos="base")
        m "Do you ever touch yourself?"
        call her_main("What? why?", "upset", "wink", "base", "mid")
        m "Do you?"
        call her_main("[genie_name]!", "scream", "worriedCl", "worried", "mid")
        m "It's a simple question [hermione_name]..."
        call her_main("......", "normal", "worriedCl", "worried", "mid")
        call her_main("{size=-5}I do...{/size}", "angry", "worriedCl", "worried", "mid", emote="05")
        m "Huh? What was that?"
        call her_main("I said that I do alright!!!", "scream", "worriedCl", "worried", "mid")
        m "Hmmmm, I'm not sure I believe you..."
        call her_main("What? why would I lie?", "annoyed", "base", "worried", "R")
        m "I'm not sure..."
        m "But don't worry, I'm sure a quick little demonstration will erase any doubts..."
        call her_main("......", "annoyed", "narrow", "angry", "R")
        call her_main("well I suppose I could.", "open", "narrow", "worried", "down")
        call her_main("But you better keep your hands to yourself...", "open", "narrow", "worried", "down")
        m "Witcher's promise."
        call her_main("...", "annoyed", "squint", "base", "mid")

    # Repeat
    else:
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", "base", "base", "base", "mid", xpos="mid", ypos="base")
        m "Are you feeling horny?"
        call her_main("maybe A little, [genie_name].", "base", "narrow", "base", "mid_soft")
        m "Ah, well perhaps we can fix that..."
        call her_main("[genie_name]...", "open", "worriedCl", "worried", "mid")

        g9 "Why don't you play with that slutty little pussy of yours!"
        call her_main("{image=textheart}{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")
        call her_main(".............", "soft", "narrow", "annoyed", "up")
        call her_main("Alright...", "base", "narrow", "worried", "down")

        call her_main("(I can't believe I'm going to do this... again...)", "angry", "narrow", "base", "down")

    return



### Tier 2 ###

label hg_pf_strip_T2_fingering:

    call hg_pf_strip_fingering_intro

    call play_music("playful_tension") # SEX THEME.
    call her_main("...........", "upset", "base", "base", "mid")
    call her_main("Do you want me to... start?", "soft", "wink", "base", "mid")
    m "Yes, my dear."
    call her_main("...........", "disgust", "narrow", "base", "down")
    call her_main("(I can't believe I'm going to do this...)", "normal", "worriedCl", "worried", "mid")

    call set_her_action("covering_top")
    #if hg_masturbated.trigger == False:
        #$ achievement.unlock("hg_masturbated") # TODO: Add achievement
    $ hg_masturbated.triggered() # .trigger = True, .counter += 1
    call ctc

    g9 "Nice..."
    call her_main("........", "upset", "wink", "base", "mid")
    m "............."
    call her_main(".............", "normal", "worriedCl", "worried", "mid")
    call her_main("umm... [genie_name]?")
    m "Yes, what is it?"
    call her_main("How long do I have to keep doing this?", "open", "base", "base", "mid")
    m "Until you finish [hermione_name]..."

    if daytime:
        call her_main("But my classes are about to start, [genie_name]...", "soft", "base", "base", "mid")
    else:
        call her_main("But it's getting late, [genie_name]...", "soft", "base", "base", "mid")

    call her_main("I'm not sure if I'll be able to finish... in time.", "disgust", "narrow", "base", "down")
    m "Do you need the points or not?"
    call her_main("I do, [genie_name]! I'm sorry...", "open", "narrow", "worried", "down")
    call her_main("I'll just keep ...going...", "disgust", "narrow", "base", "down")
    m "(Hmmm, I might have to give her a little encouragement.)"

    menu:
        m "..."
        "\"That's it slut, keep going.\"":
            call her_main("[genie_name]!!!", "angry", "base", "angry", "mid")
            call her_main("How dare you!")
            m "what?"
            call her_main("I hardly think that language is appropriate.", "upset", "wink", "base", "mid")
            m "And masturbating in front of your headmaster is?"
            call her_main("Well... this is different.", "open", "narrow", "worried", "down")
            call her_main("I'm doing this for the honour of gryffindor...")
            call her_main("To help my--")
            call nar(">You notice how she's starting to grind her hips a little faster.")
            $ hermione_dribble = True
            call her_main("ah...{image=textheart}{image=textheart}{image=textheart}", "soft", "narrow", "annoyed", "up")
            call her_main("My classmates win the house cup...", "angry", "wink", "base", "mid")
            m "Are you sure that's the only reason slut?"
            call her_main("I don't know--", "normal", "worriedCl", "worried", "mid")
            call her_main("ah-a{image=textheart}...", "open", "worriedCl", "worried", "mid")
            call her_main("I don't know what you mean, [genie_name]...", "angry", "narrow", "base", "down")
            m "It seems to me that you might be enjoying this a little too much..."
            call her_main("I am not, [genie_name]!", "open", "worriedCl", "worried", "mid")
            m "Really?"
            call her_main("......................", "normal", "worriedCl", "worried", "mid")
            m "Then why is your pussy so wet slut?"
            call ctc

            call her_main("ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
            m "ha! just Admit it, you enjoy being called a slut!"
            call her_main("I do not!", "normal", "worriedCl", "worried", "mid")
            call her_main("Aha...{image=textheart}", "open", "worriedCl", "worried", "mid")
            call her_main("I'm just thinking about how happy everyone will be when we win!", "shock", "worriedCl", "worried", "mid")
            m "and what if they find out how you earned the points?"
            call her_main("what?!", "shock", "wide", "base", "stare")
            m "then it wouldn't just be me degrading you..."
            call her_main("...", "soft", "happy", "base", "R")
            m "It would be the whole school."
            call her_main("ah...{image=textheart}", "silly", "narrow", "base", "dead")
            m "Little. miss. slut."
            call her_main("ah...{image=textheart}{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")
            call her_main("[genie_name], please... don't tell anyone...", "angry", "wink", "base", "mid")
            call nar(">Hermione keeps on grinding her hips against her hand...")
            call her_main("they can't find out...", "angry", "base", "base", "mid")
            call her_main("if harry and ron knew...", "angry", "narrow", "base", "down")
            call her_main("i'd... ah...{image=textheart}", "soft", "narrow", "annoyed", "up")
            m "You'd what [hermione_name]?"
            call her_main("I'd...", "open", "worriedCl", "worried", "mid")
            call her_main("I'd...{image=textheart}", "shock", "worriedCl", "worried", "mid")
            call her_main("I...{image=textheart}{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")

        "\"Play with your breasts\"":
            call her_main("my breasts...", "open", "narrow", "worried", "down")
            call set_her_action("covering_top")

            call her_main("I'm not sure if I should--", "clench", "narrow", "base", "down")
            m "There's another 10 points for gryffindor in it for you..."
            $ current_payout += 10
            call her_main("...", "soft", "happy", "base", "R")
            call her_main("......", "soft", "happy", "base", "R")
            call set_her_action("lift_breasts")

            call her_main("ah...{image=textheart}", "open", "base", "base", "R")
            m "There... Isn't that better?"
            $ hermione_dribble = True
            call her_main("Ah... y-yes...{image=textheart}", "grin", "narrow", "annoyed", "up")
            call set_her_action("covering_top")
            call her_main("Mmmm...", "smile", "happyCl", "base", "mid")
            m "That's it..."
            call set_her_action("lift_breasts")
            call her_main("[genie_name], do you mind...", "base", "narrow", "base", "up")
            m "What [hermione_name]?"
            call her_main("Could you... Call me names...", "open", "narrow", "base", "up", cheeks="blush")
            m "Such as?"
            call set_her_action("covering_top")

            call her_main("...{p}{size=-5}Slut...{/size}{p}Only if it's not too much...", "base", "narrow", "base", "up", cheeks="blush")
            m "You little whore..."
            call her_main("Ah...{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")
            m "What would your parents think if they saw this?"
            call her_main("i-{image=textheart}", "base", "narrow", "base", "up", cheeks="blush")
            call set_her_action("lift_breasts")

            call her_main("Ah...{image=textheart} I don't know...", "base", "narrow", "base", "up", cheeks="blush")
            call her_main("To be perfectly honest [genie_name]... I don't think I care...{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "up", cheeks="blush")
            m "Really?"
            call set_her_action("covering_top")

            call her_main("Really...{image=textheart}", "silly", "narrow", "base", "up", cheeks="blush")
            m "Would you at least stop?"
            call her_main("Ah...{image=textheart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call set_her_action("lift_breasts")

            call her_main("Maybe....", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call her_main("I'm not sure...", "open", "base", "base", "R", cheeks="blush")
            call set_her_action("covering_top")

            call her_main("{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "up", cheeks="blush")

        "\"Dig deeper!\"":

            call set_her_action("covering")

            m "Good... Just keep playing with that slutty little pussy of yours!"
            call her_main("[genie_name]!", "mad", "base", "angry", "mid", cheeks="blush")
            m "What?"
            $ hermione_dribble = True
            call her_main("It's not {size=-5}slutty...{/size}", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "Are you sure? Because from where I'm sitting it looks nice and wet."
            call her_main("Ah...{image=textheart}", "base", "narrow", "base", "up", cheeks="blush")
            call her_main("It's just sweat, [genie_name]...", "open", "base", "base", "R", cheeks="blush")
            m "Whatever you say..."
            call her_main("...............", "base", "narrow", "base", "up", cheeks="blush")
            m "{size=-5}Slut.{/size}"
            call her_main("{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "up", cheeks="blush")
            call her_main("Sir... please...", "open", "base", "base", "R", cheeks="blush")
            call set_her_action("pinch")

            call nar(">Hermione starts gently fingering herself.")
            m "Very good..."
            call her_main("...{image=textheart}", "silly", "narrow", "base", "up", cheeks="blush")
            call her_main("Ah...{image=textheart}", "open_tongue", "narrow", "base", "up", cheeks="blush")
            m "That's it slut. Try going a little deeper...."
            call her_main("...", "open_tongue", "narrow", "base", "up", cheeks="blush")
            call set_her_action("covering")

            call her_main("Mmmm...{image=textheart}", "scream", "worriedCl", "worried", "mid", cheeks="blush")


    call her_main("Ah...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "almost there [hermione_name]?"
    call her_main("a-almost...", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("I just need a bit longer...")
    m "well you better hurry..."
    call her_main("Ah... i know, [genie_name].", "mad", "worriedCl", "worried", "mid", tears="soft_blink")
    call her_main("...........", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "is everything alright?"
    call her_main("................", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
    m "Why are you being so quiet [hermione_name]?"
    call her_main("......", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
    call her_main("[genie_name]... I don't think I can...")
    m "what?"
    call her_main("...finish...", "angry", "narrow", "base", "dead", cheeks="blush", tears="crying")

    menu:
        "-Chastise her-":
            m "Well then I guess Slytherin will have to win the house cup this year."
            call her_main("B-but--", "scream", "wide", "base", "stare")
            m "now, now [hermione_name], a deals a deal."
            call her_main("Really?", "open", "worriedCl", "worried", "mid")
            call her_main("but I'm trying [genie_name]...", "shock", "worriedCl", "worried", "mid")
            m "try harder..."
            call nar(">Hermione starts grinding furiously against hand")
            call her_main("*SOB!* i can't...", "shock", "narrow", "base", "down", cheeks="blush", tears="crying")
            m "well then, 0 points to Gryffindor..."
            call her_main("{size=-5}After all...{/size} Really [genie_name]?", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
            call her_main("After I stood here and...", "scream", "base", "angry", "mid", cheeks="blush", tears="messy")
            call her_main("..........", "angry", "squint", "base", "mid", cheeks="blush", tears="messy")
            call nar(">Hermione wipes the tears from her eyes.")
            call her_main("I am not going to sell you a single favour anymore, [genie_name]!", "angry", "base", "angry", "mid", cheeks="blush")

            $ her_mood += 15

            jump end_hg_pf_strip

        "-Forgive her-":
            m "It's alright, [hermione_name]."
            call her_main("Really?", "open", "wide", "worried", "stare", cheeks="blush", tears="messy")
            m "I'm sure you're just a little nervous."
            call her_main("Thank you [genie_name].", "clench", "base", "worried", "mid", cheeks="blush", tears="soft")
            call her_main("I promise to try harder next time.", "scream", "worriedCl", "worried", "mid", cheeks="blush", tears="messy")

            jump end_hg_pf_strip



### Tier 3 ###

label hg_pf_strip_T3_fingering:

    call hg_pf_strip_fingering_intro

    call set_her_action("covering_top")
    #if hg_masturbated.trigger == False:
        #$ achievement.unlock("hg_masturbated") # TODO: Add achievement
    $ hg_masturbated.triggered() # .trigger = True, .counter += 1
    call ctc

    call play_music("playful_tension") # SEX THEME.
    g9 "Nice..."
    call her_main("........", "grin", "narrow", "annoyed", "up")

    call her_main("A-ha... {image=textheart}ah...", "open", "worriedCl", "worried", "mid")
    call her_main("Ah... {image=textheart}-aha...", "open", "worriedCl", "worried", "mid")
    m "..."
    call her_main("Ah-ah...", "open", "worriedCl", "worried", "mid")
    m "......................"
    call her_main("Ah... ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    call her_main("Ah... [genie_name]?", "soft", "happy", "base", "R")
    m "What is it?"
    call her_main("Ah... Do you.... like this?", "open", "worriedCl", "worried", "mid")
    m "Do I like watching \"you\" finger your slutty little pussy?"
    m "Very much so, [hermione_name]. Why?"
    call her_main("{image=textheart}{image=textheart}{image=textheart}", "normal", "worriedCl", "worried", "mid")
    call her_main("Ah... You're just so quiet...", "open", "worriedCl", "worried", "mid")
    m "Do you need a little more encouragement?"
    call her_main("Ah... yes... please....{image=textheart}", "open", "worriedCl", "worried", "mid")
    m "Tch... You nasty whore!"
    call her_main("yes [genie_name], ah...{image=textheart}", "grin", "narrow", "base", "up", cheeks="blush")
    call her_main("please... ah... more...{image=textheart}", "grin", "base", "angry", "mid", cheeks="blush")
    g4 "You need to be punished for being such a slut!"
    call her_main("yes, [genie_name]... punish me...", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("make me your little slut....", "open", "narrow", "base", "up", cheeks="blush")
    call her_main("I will... ah... {image=textheart}do anything... ah...{image=textheart}", "silly", "narrow", "base", "dead")
    m "Anything [hermione_name]?"
    call her_main("Ah-a...{image=textheart} yessss...", "silly", "narrow", "base", "up", cheeks="blush")
    m "Cum."
    $ hermione_squirt = True
    call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead", cheeks="blush")
    call cum_block

    $ hermione_squirt = False
    call her_main("Ah...{image=textheart}...{image=textheart}", "grin", "narrow", "annoyed", "up")
    call her_main("Ah... ah...{image=textheart}", "silly", "narrow", "annoyed", "up")
    call her_main("...{image=textheart}{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")
    call her_main("*heavy panting*", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_main("[genie_name]...{image=textheart}{image=textheart}{image=textheart}", "open_wide_tongue", "narrow", "annoyed", "up")
    call her_main(".............", "soft", "narrow", "annoyed", "up")
    call nar(">Hermione takes a minute to collect herself.")
    m "You feeling alright?"
    call her_main("Yes, [genie_name]... I just need a little longer...", "shock", "base", "base", "R", cheeks="blush", tears="soft")
    m "take your time."
    call her_main("ah... {image=textheart}", "silly", "base", "worried", "mid", cheeks="blush", tears="soft")

    jump end_hg_pf_strip



### Tier 4 ###

label hg_pf_strip_T4_fingering:
    m "[hermione_name]?"
    call her_main("[genie_name]?", "base", "base", "base", "mid")
    m "You don't mind pleasuring yourself in front of me, do you?"
    if her_whoring <= 16:
        call her_main("As long as I am being paid...", "grin", "base", "base", "R")
        m "That's the spirit!"
    else:
        call her_main("I mean I have done it once today already...", "grin", "base", "base", "R")
        m "Once more for good luck then!"
        call her_main("If you insist...{image=textheart}", "open", "base", "base", "R", cheeks="blush")

    call her_main("...", "base", "narrow", "base", "mid_soft")
    call set_her_action("covering")

    #if hg_masturbated.trigger == False:
        #$ achievement.unlock("hg_masturbated") # TODO: Add achievement
    $ hg_masturbated.triggered() # .trigger = True, .counter += 1

    stop music fadeout 3.0
    call her_main("Do you like it when I do it like this, [genie_name]?", "grin", "base", "base", "R")
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    m "Yes, yes, like that..."
    m "Try going a little deeper with your fingers."
    call her_main("Alright [genie_name]...", "base", "happyCl", "base", "mid")
    $ hermione_dribble = True
    call her_main("Ah... ah...{image=textheart}", "open", "worriedCl", "worried", "mid")
    call her_main("Ah... [genie_name]...{image=textheart}", "open", "worriedCl", "worried", "mid")

    menu:
        m "..."
        "\"What are you thinking about?\"":
            call her_main("Huh?", "open", "worriedCl", "worried", "mid", cheeks="blush")
            call her_main("Oh, um... nothing...", "upset", "worriedCl", "worried", "mid", cheeks="blush")
            m "[hermione_name]..."
            call her_main("[genie_name], please, it's too embarrassing...", "disgust", "narrow", "base", "down", cheeks="blush")
            g4 "Well now I have to hear it."
            call her_main("OK... but you have to promise not to tell anyone!", "open", "base", "base", "R", cheeks="blush")
            m "Witcher's honour."
            call her_main("......", "annoyed", "narrow", "annoyed", "mid")
            m "[hermione_name]..."
            call her_main("Alright. If you must know... I'm remembering the time I corrected professor Snape about the ingredients of a Hiccoughing potion.", "open", "narrow", "worried", "down")
            m "....."
            call her_main("ah...{image=textheart}", "soft", "narrow", "annoyed", "up")
            call set_her_action("pinch")

            call her_main("It was ah... {image=textheart} in front of the entire class as well.")
            call set_her_action("covering")

            call her_main("He refused to let me answer any questions for a week after that.", "base", "narrow", "worried", "down")
            call her_main("But it was worth it...", "soft", "happy", "base", "R")
            call her_main("The look on his face when he realised he was wrong...{image=textheart}", "soft", "narrow", "annoyed", "up")
            call set_her_action("pinch")

            call her_main("a-ah...{image=textheart}")
            call set_her_action("covering")

            call her_main("It just felt so good!{image=textheart}", "grin", "narrow", "base", "dead")
            m "OK, I think that's enough..."
            call her_main("Was it too much?", "angry", "wink", "base", "mid")
            m "Let's just get back to business shall we?"
            call her_main(".................", "soft", "narrow", "annoyed", "up")
            call nar(">Hermione keeps on plunging her fingers into herself.","start")
            call nar(">She is doing a great job of it too.","end")
            m "Yes, yes... Like that."

        "\"You really are a shameless slut, aren't you?\"":
            call her_main("Yes...", "soft", "narrow", "annoyed", "up")
            call set_her_action("pinch")

            call her_main("ah... {image=textheart}", "silly", "narrow", "base", "dead")
            call her_main("I don't know if it's the time I'm spending with you...{image=textheart}", "angry", "wink", "base", "mid")
            call her_main("Or if i've always been this way...{image=textheart}", "angry", "narrow", "base", "down")
            call her_main("But... {image=textheart} ah... {image=textheart} I'm a slut [genie_name]...{image=textheart}", "soft", "narrow", "annoyed", "up")
            call her_main("A shameless slut...", "grin", "narrow", "base", "dead")
            call her_main("That pleasures herself...{image=textheart} ah...", "soft", "narrow", "annoyed", "up")
            call her_main("Just to make her headmaster happy...", "grin", "narrow", "base", "dead")
            m "Oh, yes..."
            call her_main("That's it [genie_name]...", "base", "narrow", "worried", "down")
            call her_main("Enjoy yourself while I stand here...", "silly", "narrow", "base", "dead")
            call her_main("Ah...{image=textheart}", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("Fingering my pussy...", "silly", "narrow", "annoyed", "up")
            call her_main("Ah... ah...{image=textheart}", "grin", "narrow", "annoyed", "up")
            call her_main("Ah... Do you.... like this [genie_name]?", "shock", "worriedCl", "worried", "mid")
            call her_main("Watching me Ah...{image=textheart} degrade myself?", "silly", "narrow", "base", "dead")
            m "Very much, [hermione_name]. Just keep going..."
            call her_main("{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead")

        "\"Play with your tits some more!\"":
            call her_main("Hm?", "soft", "narrow", "annoyed", "up")
            call her_main("alright... if you insist...", "open", "base", "base", "R", cheeks="blush")
            call set_her_action("pinch")

            call her_main("ah...{image=textheart}", "angry", "wink", "base", "mid")
            m "Now lift them up."
            call her_main("[genie_name]...", "open", "happy", "base", "mid", cheeks="blush")
            m "do it, [hermione_name]."
            call her_main("...", "open", "base", "base", "R", cheeks="blush")
            call set_her_action("lift_breasts_naked")

            call her_main("Mmmm...", "grin", "narrow", "base", "up", cheeks="blush")
            m "That's it..."
            call nar(">You stare at Hermione's breasts with hunger...")
            call her_main("ah...", "silly", "narrow", "base", "dead")
            m "So do you like playing with those tits of yours, [hermione_name]?"
            call her_main("I do, [genie_name]... ah...{image=textheart}", "soft", "narrow", "annoyed", "up")
            call her_main("I don't know why...", "base", "base", "base", "R", cheeks="blush")
            call set_her_action("pinch")

            call her_main("But I love it...{image=textheart}{image=textheart}", "base", "narrow", "worried", "down")
            m "You nasty slut!"
            call her_main("Ah...{image=textheart} ah-a...{image=textheart}", "open_wide_tongue", "narrow", "annoyed", "up")
            call her_main("I am...")
            call her_main("A nasty slut... Ah...{image=textheart}", "silly", "narrow", "base", "dead")
            m "You are a disgrace, [hermione_name]!"
            call her_main("Ah-ah...{image=textheart}{image=textheart}{image=textheart}", "open_wide_tongue", "narrow", "annoyed", "up")


    m "Why don't you come down and I'll help you with it?"
    call her_main("...", "base", "narrow", "worried", "down")



    # Hermione climbs off your desk.
    show screen blkfade
    with d5

    call play_sound("climb_desk")
    pause 2

    ">Hermione slowly climbs down from the desk and stands in front of you."
    pause.5

    call her_chibi_scene("behind_desk_show_tits") #TODO Replace with naked chibi

    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    call set_her_action("lift_breasts_naked")
    call her_main("..............", "base", "narrow", "base", "up", cheeks="blush")

    menu:
        m "..."
        "-Grab her tits-":
            call nar(">You reach forward and grab a hold of her supple breasts.")
            call her_chibi_scene("grope_tits")
            call set_her_action("fingering")

            call her_main("[genie_name]!", "shock", "worriedCl", "worried", "mid")
            call her_main("This wasn't part of the deal!", "open", "worriedCl", "worried", "mid")
            call her_main("I don't think we should...", "annoyed", "narrow", "angry", "R", cheeks="blush")
            m "Don't worry [hermione_name], You can keep playing with yourself."
            m "This is just to hurry things along."
            call her_main("Ah...{image=textheart} Well, as long as it's just to make this end faster...", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I suppose I can... ah{image=textheart} allow it...", "base", "base", "base", "R", cheeks="blush")
            call nar(">You give her tits a couple of firm squeezes...")
            m "Just admit that you love it."
            call her_main("Ah... fine...{image=textheart}", "open", "worriedCl", "worried", "mid", cheeks="blush")
            call her_main("{size=-5}I like it...{/size}", "soft", "narrow", "annoyed", "up")
            m "What was that [hermione_name]?"
            call her_main(".......")
            call her_main("I love this...", "grin", "narrow", "base", "dead")
            call her_main("Standing here... playing with myself...", "base", "narrow", "worried", "down")
            call her_main("Ah... while you play with me...{image=textheart}", "grin", "narrow", "base", "up", cheeks="blush")
            m "Heh... Nice."
            call her_main("Ah...{image=textheart}", "open", "narrow", "base", "up", cheeks="blush")
            call her_main("I sometimes wish I could spend all day in here...", "grin", "base", "angry", "mid", cheeks="blush")
            m "Mmmm"
            call nar(">You keep on massaging the girl's breasts...")
            call her_main(".......")
            call her_main("[genie_name]... I know it's greedy of me...", "base", "base", "base", "R", cheeks="blush")
            call her_main("ah...{image=textheart}", "base", "narrow", "worried", "down")
            call her_main("but could you touch me... down there...", "open", "happy", "base", "mid", cheeks="blush")
            m "What's was that [hermione_name]? You'll have to speak up."
            call her_main("Please finger me...", "open", "narrow", "base", "up", cheeks="blush")
            m "Once more, a little louder this time."
            call her_main("Ah...{image=textheart} {size=+5}please finger my cunt!{/size}", "grin", "narrow", "base", "up", cheeks="blush")
            call her_chibi_scene("grope_ass_front")
            call nar(">You swiftly plunge two fingers into her dripping pussy.")
            call set_her_action("lift_breasts_naked")
            call her_main("{image=textheart}{image=textheart}{size=+5}!!!{/size}{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up")

        "-Finger her-":
            call her_chibi_scene("grope_ass_front")
            call nar(">You run your hands up and down Hermione's legs...")
            call her_main("!!!", "open", "worriedCl", "worried", "mid")
            call nar(">And slowly move your hands towards her pussy...")
            call her_main(".................", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]..."
            call her_main("{size=-7}[genie_name]...{/size}", "soft", "narrow", "annoyed", "up")
            m "Shhh. Just play with your tits."
            call her_main("...fine, [genie_name]...", "base", "narrow", "base", "up", cheeks="blush")
            m "Good girl."
            call her_main("....................", "base", "closed", "base", "mid")
            m "Just be quiet..."
            call nar(">you enjoy the sensation of gently stroking the inside of her thighs...")
            m "as my hands explore you"
            m "your thighs..."
            call nar(">your start kneading the flesh of her thighs, moving ever closer to her dripping cunt")
            m "your big, firm ass"
            call nar(">You move around and squeeze her ass gently...")
            call her_main(".....................", "grin", "narrow", "annoyed", "up")
            m "your loins..."
            call nar(">You move one hand back around, and start circling just above her clit.")
            call her_main(".....................{size=-8}[genie_name]...{/size}", "silly", "narrow", "base", "dead")
            m "What was that, [hermione_name]?"
            call her_main(".....................", "annoyed", "wink", "base", "mid", cheeks="blush")
            call her_main("...i... {size=-5}...i need you... inside of me...{/size}", "disgust", "narrow", "base", "down", cheeks="blush")
            m "You'll have to speak up if you expect me to hear you..."
            call her_main("I... ah...{image=textheart} need...", "open", "narrow", "base", "up", cheeks="blush")
            call nar(">You swiftly plunge two fingers into her drenched snatch.")
            call her_main("!!!{image=textheart}{image=textheart}", "grin", "narrow", "annoyed", "up")
            call nar(">you start to pump your fingers inside her before she can do more than gasp")
            call her_main("{size=+10}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}", "silly", "narrow", "base", "dead")
            m "That's it [hermione_name]. Just enjoy yourself."
            call her_main("..................................................", "base", "narrow", "base", "up", cheeks="blush")
            m "do you like this?"
            m "you like it when i finger your cunt?"
            call her_main("i love it!{image=textheart} i love your fingers in my tight, wet pussy!!{image=textheart}", "silly", "narrow", "annoyed", "up")
            m "well, i think we can do better."
            call nar(">with your other hand, you start rubbing the base of your palm against her clit.")
            call her_main("{size=+10}!!!{/size}", "open", "narrow", "base", "up", cheeks="blush")


    call nar(">you don't even need to move as she pounds herself against your fingers.")
    call her_main("ah...{image=textheart} please...{image=textheart} keep...{image=textheart}", "silly", "narrow", "base", "dead","blush")
    call her_main("fingering my cunt!{image=textheart}{image=textheart}", "silly", "narrow", "annoyed", "up","blush")
    g9 "As you command!"
    call nar(">you force another finger into her pussy!")
    call her_main("ah yes... {image=textheart}iloveitiloveitiloveit", "grin", "narrow", "annoyed", "up","blush")
    m "what do you love, [hermione_name]?"
    call her_main("ah!!{image=textheart} I love your fingers in my pussy [genie_name]!{image=textheart}", "open_wide_tongue", "narrow", "annoyed", "up","blush")
    call nar(">her movements are becoming more frantic")
    m "are you cumming, [hermione_name]?"
    call her_main("ah...{image=textheart} yes!!", "grin", "narrow", "annoyed", "up")
    call her_main("I'm cumming [genie_name]!!{image=textheart}", "grin", "narrow", "base", "dead")
    call her_main("I'm cumming from being fucked with your fingers!!{image=textheart}{image=textheart}", "grin", "narrow", "base", "up", cheeks="blush")
    m "show me your tits [hermione_name]!"
    m "I want to see you cum while you play with them."
    $ hermione_squirt = True
    call her_main("{image=textheart}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{image=textheart}", "silly", "narrow", "base", "dead", cheeks="blush")
    call cum_block

    $ hermione_squirt = False
    call her_main("Ah...{image=textheart}...{image=textheart}", "grin", "narrow", "annoyed", "up")
    call her_main("Ah... ah...{image=textheart}", "silly", "narrow", "annoyed", "up")
    call her_main("...........", "silly", "narrow", "annoyed", "up")
    call her_main("........................", "silly", "narrow", "annoyed", "up")

    call nar(">You release her...")
    call her_chibi_scene("behind_desk_show_tits")
    m "This will do for now [hermione_name]."

    jump end_hg_pf_strip
