

label hg_pf_TouchMe: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_TouchMe_OBJ.points == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(I feel like getting another handjob!){/size}"

    if hg_pf_TouchMe_OBJ.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    $ current_payout = 45 #Used when haggling about price of th favor.

    call bld

    #First Event.
    if hg_pf_TouchMe_OBJ.points == 0:

        m "[hermione_name]."
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "Do you know what a \"handjob\" is?"

        if her_whoring < 12:
            jump too_much

        call her_main("Why?","annoyed","annoyed")
        m "I feel like getting one..."
        call her_main("[genie_name]!","angry","angry")
        m "Just another favour. No big deal, right?"
        call her_main("......","disgust","glance")
        call her_main("{size=-7}I want 100 house points for this...{/size}","angry","worriedCl",emote="05")
        m "Huh? What was that?"
        call her_main("I want 100 house points for this!!!","scream","worriedCl")
        m "100 house points, huh?"
        m "And you will stroke my cock and everything?"
        call her_main("{size=-7}Yes...{/size}","disgust","glance")
        m "Sorry, I couldn't hear you..."
        call her_main("Yes, I said yes! I will stroke your cock, [genie_name]!","scream","worriedCl")


        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        label back_to_handjob_choices:

        menu:
            m "..."
            "\"You will get 15 house points.\"":
                $ mad +=7
                call her_main("For 15 house points I suppose I could let you molest me a little, but that is all you'll be getting, [genie_name].","annoyed","angryL")
                her "I will not stoop as low as to sell handjobs for 15 house points."
                her "That is just insulting, [genie_name]."
                jump back_to_handjob_choices

            "\"you will get 45 house points.\"":
                if mad > 7: #You could spam points into infinity with the choice above.
                    $ mad = 7
                call her_main(".....","annoyed","angryL")
                call her_main("45 house points...?","open","down")
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                call her_main("Yes, it is a yes, [genie_name].","annoyed","annoyed")
                m "Great!"

            "\"you will get 100 house points.\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 house points?!","scream","wide_stare")
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "Is that a \"yes\" then?"
                call her_main("Of course!","smile","happyCl")
                call her_main("If it will bring \"Gryffindor\" 100 house points, I don't mind touching your... thing a little.","smile","happyCl",emote="06")


        call play_music("playful_tension") # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        show screen chair_left
        hide screen desk
        show screen desk
        call gen_chibi("jerking_off","on_girl","base")

        hide screen bld1
        hide screen blktone
        with fade
        call ctc

        show screen bld1
        call her_main("...........","open","base",xpos="right",ypos="base")
        m "Whenever you're ready, [hermione_name]."
        pause.5

        label event_01_round_02:
        hide screen hermione_main
        call blkfade

        ">Hermione puts her slender hands on your cock..."
        m "Good. Now stroke it."
        call her_main("Right...","angry","worriedCl",emote="05",ypos="head")
        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide")
        call gen_chibi("handjob","desk","base")
        hide screen bld1
        call hide_blkfade
        call ctc

        call play_music("playful_tension") # SEX THEME.
        call blktone
        g9 "Nice..."

        if hg_pf_TouchMe_OBJ.points == 0:
            call her_main("!!!","shock","wide",xpos="right",ypos="base")
            call her_main("Are you about to finish, [genie_name]?!")
            m "About to finish?"
            m "Don't be ridiculous [hermione_name], we are just getting started."
            call her_main("Oh...","angry","worriedCl",emote="05")
            call her_main("......")
            call her_main("You will give me a warning though, won't you, [genie_name]?","upset","wink")
        else:
            call her_main("[genie_name]...?","angry","worriedCl",emote="05",xpos="right",ypos="base")
            m "What is it?"
            call her_main("Will you warn me before... uhm... you now...","angry","worriedCl",emote="05")

        $ d_flag_01 = False #If TRUE Genie promised to warn her.

        menu:
            m "..."
            "\"Of course I'll let you know when it's time.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                call her_main("Thank you, [genie_name].","normal","worriedCl")
            "\"I myself don't always know when...\"":
                call her_main("Really? But I thought...","open","base")
                call her_main("Well, never mind then...","normal","worriedCl")

        call her_main("........","open","base")
        m "............."
        call her_main(".............","normal","worriedCl")
        call her_main("Err... [genie_name]?")
        m "Yes, what is it?"
        call her_main("How long do you think this will take?","open","base")
        m "Why?"

        if daytime:
            call her_main("Well, it's just that my classes are about to start...","upset","wink")
        else:
            call her_main("Well, it's just that I have this paper that I need to finish...","upset","wink")
            call her_main("It's due tomorrow, and it's getting pretty late...")

        m "Do you need the points or not?"
        call her_main("I do, [genie_name]! I'm sorry...","base","happyCl")
        call her_main("I will just keep on stroking it then...")
        m "Well, there is something you could do to speed up the process..."
        call her_main("Really? What is it [genie_name]?","base","base")

        menu:
            m "..."
            "\"Tell me how much of a whore you are!\"":
                call her_main("What?","angry","angry")
                call her_main("But I'm not...")
                m "No need to be honest, [hermione_name]."
                m "Just make things up."
                call her_main("Really?","upset","wink")
                m "Sure. Just have fun with it."
                call her_main("Well, in that case...","open","down")
                call her_main("I am a... whore.")
                m "Heh... good. Go on."
                call her_main("I am a big whore...","open","down")
                m "Yes, you are."
                call her_main("I am the biggest whore in England!","annoyed","annoyed")
                call her_main("I try to act innocent, but in truth all I think about is cock!")
                m "Yes, you little slut!"
                call her_main("Yes! I am a slut!","annoyed","angryL")
                call her_main("I crave cock all the time.")
                m "Very nice!"
                m "But, like I said, you don't have to be honest."
                call her_main("What?","shock","wide")
                call her_main("[genie_name], those things I say are not true!","upset","wink")
                g9 "Heh... I know. I'm just messing with you."
                call her_main("[genie_name]!","disgust","glance")
                m "You are doing a great job, though. Keep at it!"
                call her_main(".....","open","down")
                call her_main("I love cock...")
                call her_main("And I love... spunk...","clench","down_raised")
                call her_main("And semen... and sperm...")
                call her_main("I love to drink sperm...")
                call her_main("I want you to feed me your sperm, [genie_name]!","open_tongue","glance")
                g4 "!!!"
                call her_main("Or better yet, pump me full of it, [genie_name]!","smile","glance")
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

            "\"Stick your tongue out and look at me!\"":
                call her_main("What?","base","base")
                m "Just do it, slut."
                call her_main("Like this?","open_wide_tongue","squintL")
                m "Yes, good. Keep looking into my eyes and stroke my cock."
                call her_main(".....................","open_wide_tongue","base")
                m "Yes... Good..."
                call her_main("...........","open_wide_tongue","base")
                call her_main("...........")
                call her_main("I can't keep my mouth open for so long, [genie_name]. I will start to drool...","open","base")
                m "But I want you to drool..."
                call her_main("What? But I will look silly!","open","base")
                m "That's the point, [hermione_name]!"
                call her_main(".......","annoyed","worriedL")
                m "Don't you want to be done with this as soon as possible?"
                call her_main("............","normal","worriedCl")
                call her_main("A-ha.....","open_wide_tongue","base")
                m "Good, [hermione_name]."
                call her_main("..............","open_wide_tongue","base")
                m "Yes, keep on stroking my cock."
                call her_main("..................","open_wide_tongue","base")
                g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
                call her_main(".................","open_wide_tongue","angryCl")
                m "No, keep on looking at me!"
                call her_main(".....................","open_wide_tongue","base")
                m "Yes, you little slut!"
                call her_main("......................","open_wide_tongue","angry")
                m "I want to cum in that mouth, yes..."
                call her_main("................","open_wide_tongue","angry")
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"

            "\"Give my cock a kiss!\"":
                call her_main("Excuse me?","angry","angry")
                m "You know, just a little kiss, right on the tip."
                call her_main(".............","angry","angry")
                call her_main("...with my lips?","shock","wide")
                m "Sure... That will speed things up, I'm telling you."
                call her_main("*sigh!*..............","open","down")
                call her_main("Well, I might as well, I suppose...")
                call nar(">Hermione gives the tip of your engorged cock a tender kiss.")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                pause 2

                call gen_chibi("handjob","desk","base")
                pause.5

                show screen blktone
                call her_main("Like this?","open","down")
                m "Wasn't that bad, was it?"
                call her_main("No, I suppose not...","upset","wink")
                m "Can you do it again, then?"
                call her_main("I could...","normal","worriedCl")
                m "Do it!"
                call her_main("Well, alright...","open","base")
                call nar(">Hermione gives your cock another kiss...")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                pause 3

                call nar(">This time she lingers a moment longer...")
                pause.8

                call blkfade
                call gen_chibi("handjob","desk","base")
                call hide_blkfade
                pause.5

                call blktone
                m "Good... Now do it again and just stay there for a while."
                call her_main("You mean with my lips touching your... cock, [genie_name]?","open","base")
                call her_main("No, I will look stupid...","annoyed","worriedL")
                m "Don't be silly, [hermione_name]. Nobody is watching."
                call her_main("You are, [genie_name].","open","down")
                m "But that's the whole point!"
                call her_main("......","annoyed","annoyed")
                m "It will make me cum in no time!"
                call her_main("...............","annoyed","angryL")
                m "And then you can just get out and and take care of your business today."
                call her_main(".............","disgust","glance")
                call her_main("Well, alright then....","open","down")
                call nar(">Hermione reaches down with her lips again...","start")
                call nar(">She touches the tip of your cock with her lips and keeps them there...","end")

                hide screen hermione_main
                hide screen blktone
                call blkfade

                call gen_chibi("handjob_kiss","desk","base")
                $ renpy.play('sounds/kiss.mp3')
                with kissiris
                call hide_blkfade
                call ctc

                call blktone
                m "Very good..."
                m "Now touch it with your tongue."
                call her_main("??!","open_tongue","closed")
                m "That's the last thing I will be asking of you today."
                her "............"
                call nar(">You feel the tip of Hermione's tongue warily rubbing against the head of your cock...")
                m "Yes, like this..."
                call nar(">Hermione wiggles her tongue a little....")
                m "Yes... Good..."

                call blkfade
                hide screen hermione_main
                call gen_chibi("handjob","desk","base")
                hide screen blktone
                call hide_blkfade
                pause.8

                show screen blktone
                call her_main("So, did it work? Are you ready to... finish, [genie_name]?","open","down")
                g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"

        menu:
            m "..."
            "-Give her a warning-":
                g4 "Here it comes, [hermione_name]! You better be ready!"
                call her_main("What? So soon?!","shock","wide")
                g4 "{size=+5}Yeah, you did a great job!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen hermione_main
                call blkfade

                call her_main("No, [genie_name], wait, I--","angry","base",ypos="head")
                g4 "{size=+5}Too late for that, slut!{/size}"
                call her_main("*whimper*","angry","down_raised",ypos="head")
                ">Hermione suddenly slides your already dripping cock under her shirt..."
                g4 "?!!"
                ">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man."

                call cum_block

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_main("!!!!!!!!!!!","shock","wide",ypos="head")

                call gen_chibi("cumming_under_shirt","desk","base")
                hide screen blktone
                call hide_blkfade
                stop music fadeout 1.0
                call ctc

                $ aftersperm = True
                call her_main(".......................","angry","wide",xpos="right",ypos="base")
                m "..........................."
                call her_main(".......................","angry","wide")
                m "....................?"
                call her_main(".......................","angry","down_raised")
                m "...What the fuck just happened?"

                call play_music("chipper_doodle") # HERMIONE'S THEME.

                call her_main("I don't know... I suppose I just panicked...","angry","worriedCl",emote="05")

                if daytime:
                    call her_main("My classes are about to start and I didn't want you to ruin my uniform, [genie_name]...","angry","worriedCl",emote="05")
                    m "So you'll go to classes like this now?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_main("What choice do I have?","angry","down_raised")
                    call her_main("I can't just skip a class...")
                else:
                    call her_main("At this hour The \"Gryffindor\" common room will be full of people...","angry","worriedCl",emote="05")
                    call her_main("I didn't want to have to return there all covered in your... spunk, [genie_name].")
                    call her_main("Oh, it's getting pretty late...","angry","base")
                    m "So you will go like this, instead?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_main("What choice do I have?","angry","down_raised")

                call ctc
                call blkfade

                ">Hermione releases your still pulsating cock."

                call her_chibi("stand","mid","base")
                call gen_chibi("stand","desk","base")
                hide screen bld1
                call hide_blkfade
                pause.5

                call her_main("Ew... Your sperm, [genie_name]...","angry","down_raised")
                call her_main("It's everywhere under my uniform...","angry","base")
                m "Just put it in your mouth next time."
                call her_main("I... don't think so, [genie_name].","annoyed","annoyed")
                call her_main("I really need to go. Can I just get paid now?")


            "-Just start cumming-":

                with hpunch
                g4 "ARGH!"
                call blkfade

                call her_main("WHAT?!","shock","wide",ypos="head")
                g4 "Take this!"

                call cum_block

                g4 "{size=+5}ARGH! YES!!!{/size}"
                call her_main("!!!!!!!!!!!","shock","wide",ypos="head")

                call gen_chibi("cumming_on_shirt","desk","base")
                hide screen blktone
                call hide_blkfade
                call ctc

                $ aftersperm = True

                call her_main(".......................","angry","wide",xpos="right",ypos="base")
                call gen_chibi("cumming_on_shirt_pause")
                m "Yes... I Feel so much better now..."
                pause.5

                $ g_c_u_pic = "images/animation/15_cum_21.png"
                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                call her_main("","soft","base",tears="soft")
                pause.5
                her ".........."
                m "Well, I think that's about it..."
                pause.2

                hide screen hermione_main
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide")
                call her_chibi("stand","desk","base")
                show screen genie
                hide screen bld1
                with fade
                pause.8

                show screen bld1
                call her_main("[genie_name]! What have you done?!","scream","worriedCl")
                m "What?"

                if d_flag_01: #If TRUE Genie promised to warn her.
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    $ mad += 11
                    call her_main("You promised to give me a warning, [genie_name]!","angry","angry")
                    m "Oh, that's right... My bad."
                    call her_main("My uniform is ruined...","annoyed","angryL")
                    her "...I would like to get paid now."

                else:

                    if daytime:
                        call her_main("My uniform is ruined now!","annoyed","angryL")
                        call her_main("My classes are about to start and I can't go looking like this!","open","down")
                        m "Of course you can, just wipe it off or something..."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","annoyed","annoyed")
                    else:
                        call her_main("My uniform is ruined!","annoyed","angryL")
                        her "Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                        m "Why not? You look hot, [hermione_name]!"
                        call her_main("[genie_name]!!!","annoyed","annoyed")
                        m "Alright, alright. Just wipe it off or something."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","annoyed","annoyed")


    #Second Event.
    elif hg_pf_TouchMe_OBJ.points == 1:
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="mid",ypos="base")
        m "Do you know what a \"handjob\" is?"
        call her_main("You have asked me that already, [genie_name].","disgust","glance")
        m "Ah, that's right."
        m "Well, I want you to play with my cock again."
        call her_main("[genie_name], you are being vulgar again...","upset","closed")
        m "Fine, fine."
        m "[hermione_name], I would like to buy another favour from you today."
        call her_main("Of course, [genie_name].","annoyed","angryL")
        g9 "The favour being you playing with my cock!"
        call her_main("..............","disgust","glance")
        m "Oh, come on. For the honour of the \"Gryffindors\"?"
        call her_main(".............","angry","angry")
        g9 "Play with my cock for the honour of the \"Gryffindors\", [hermione_name]!"
        call her_main("Stop saying that, [genie_name]...","scream","angry",emote="01")
        m "Come on [hermione_name], it's not like I'm asking you to do this for free."
        call her_main(".......","annoyed","angryL")
        stop music fadeout 4.0

        jump event_01_round_02 #Sets up handjob.


    #Third Event.
    elif hg_pf_TouchMe_OBJ.points >= 2:
        $ hg_pf_TouchMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="mid",ypos="base")
        m "You don't mind giving me another handjob, do you?"

        if her_whoring <= 16:
            call her_main("As long as I am getting paid...","grin","baseL")
            m "Well, come here then. Time to earn those points."
        else:
            call her_main("Of course not [genie_name]...","grin","baseL")
            m "Well, come here then."


        hide screen hermione_main
        hide screen bld1
        call blkfade

        stop music fadeout 3.0
        call her_main("Do you like it when I do it like this, [genie_name]?","grin","baseL",ypos="head")
        g9 "Actually, yes! Very nice!"
        call play_music("chipper_doodle") # HERMIONE'S THEME.

        show screen chair_left
        hide screen desk
        show screen desk
        call her_chibi("hide")
        call gen_chibi("handjob","desk","base")

        hide screen bld1
        call hide_blkfade
        call ctc

        call blktone
        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        call her_main("Thank you, [genie_name].","base","happyCl",xpos="right",ypos="base")
        call her_main("I figured the better I do this, the sooner it'll be over.")
        m "Hm..."

        menu:
            m "..."
            "\"What do you think of my cock?\"":
                call her_main("Huh?","open","base")
                call her_main("Oh, that's right...")
                call her_main("I need to compliment your penis! I completely forgot about that!","angry","worriedCl",emote="05")
                m "Well, you don't have to--"
                call her_main("[genie_name], let me be honest with you...","upset","closed")
                m "Yes?"
                call her_main("You have the biggest penis I have ever seen!","smile","angry")
                m "Well I suppo--"
                call her_main("Not done yet!","scream","angryCl")
                m "Apologies."
                call her_main("Your penis is so big it almost scares me!","angry","down_raised")
                g9 "You little mynx. You know exactly what to say..."
                call her_main("And yet I lust for it...","soft","ahegao")
                call her_main("Any woman would be happy to have your huge penis inside of her!")
                m "...you're good!"
                call her_main("There is more!","scream","angryCl")
                m "By all means..."
                call her_main("I think your magnificent cock is a blessing to this world!","scream","angryCl")
                m "Well, I wouldn't go that far--"
                call her_main("Listen to me, [genie_name]!","scream","angryCl")
                call her_main("I think a statue dedicated to your magnificent penis shall be erected in every city!")
                call her_main("So that people of the world could worship your phallus freely!")
                m "OK, I think I've heard enough."
                call her_main("Too much?","angry","wink")
                m "Yeah, just a bit."
                call her_main("Sorry...","angry","worriedCl",emote="05")
                m "No biggie. Just keep on stroking it."
                call her_main(".................","soft","ahegao")
                call nar(">Hermione keeps on stroking your cock.","start")
                call nar(">She is doing a great job of it too.","end")
                m "Yes, yes... Like that."

            "\"Call yourself a whore!\"":
                call her_main("Excuse me?","open","base")
                call her_main("Oh, that's right! I'm supposed to degrade myself, right?","annoyed","suspicious")
                m "Well, you don't have to, but..."
                call her_main("That's alright, I don't mind.","upset","closed")
                call her_main("Alright then! I am a whore!","base","base")
                m "Good. Glad we established that."
                m "Now I want you to say..."

                menu:
                    m "..."
                    "\"I am a worthless slut!\"":
                        call her_main("Of course.","angry","wink")
                        call her_main("I am a worthless slut.","soft","ahegao")
                        call her_main("A dirty little slut, that's what I am.")
                        m "Yes! Good!"
                    "\"I live to suck cock!\"":
                        call her_main("Em...","angry","wink")
                        call her_main("I live to suck penis, er... I mean cock...","base","base")
                        m "Really? Well why don't you suck on this one then?"
                        call her_main("[genie_name], I am just repeating after you...","smile","angry")
                        m "Really? Could've fooled me...."
                        call her_main("....................","angry","wink")
                        m ".................."
                    "\"I love to swallow cum!\"":
                        call her_main("I love to... ehm... swallow cum.","angry","wink")
                        m "You hesitated there for a moment."
                        call her_main("Yes, I know....","angry","wink")
                        call her_main("Let me try again...")
                        call her_main("I love to swallow cum!","soft","ahegao")
                        call her_main("It is truly the best to swallow cum!")
                        call her_main("I love it!")
                        call her_main("...................................","grin","dead")
                        call her_main("How was that, [genie_name]?","angry","wink")
                        m "Perfect."

            "\"This is really good. Did you practice?\"":
                call her_main("Hm?","base","happyCl")
                call her_main("Sort of... Well not really...")
                call her_main("I had a talk with the girls, and...","angry","wink")
                m "About handjobs?"
                call her_main("Among other things...","smile","happyCl",emote="06")
                m "So those girls of yours, they know a lot about such things?"
                call her_main("Actually, yes. I was surprised myself.","shock","wide")
                call her_main("All sorts of weird sexual things seem to be happening lately in our school...","grin","baseL")
                call her_main("Can't say I approve of that...")
                call her_main("But they did teach me quite a few... tricks.","base","happyCl")
                m "Really? Like what?"
                call her_main("Well, let's see...","base","down")
                call her_main("If I put one of my hands here...")
                call her_main("And another one here...")
                m "Oh, I see... Yes, this feels quite good."
                call her_main("Does it?","angry","wink")
                call her_main("So Ginny was right about this one...","grin","baseL")
                g4 "What did you just say?"
                call her_main("Ginny Weasley, she taught me this one.","base","happyCl")
                m "Oh, right..."
                call her_main("She said any boy would fall in love with me if I did this to him...","base","down")
                call her_main("There is also this thing when I form a ring with my fingers...")
                call her_main("And then I put one finger here...")
                m "Hm... I don't feel anything..."
                call her_main("Really?","angry","down_raised")
                call her_main("Hm...")
                call her_main("Oh! That's right!","base","down")
                call her_main("The finger goes here! Silly me!")
                with hpunch
                with kissiris
                g4 "Oh!!! By the great desert sands, yes!"
                call her_main("Really? That good?","smile","happyCl",emote="06")
                call her_main("What if I keep doing this but stick my finger here and press a little...","base","down")
                g4 "[hermione_name], you are killing me!"
                call her_main("Really? Really?!","smile","happyCl",emote="06")
                call her_main("This is actually quite fun!")
                call her_main("Err... I mean...","angry","wink")
                call her_main("I am only doing this to help my house of course...")
                m "Yes, yes... The \"Gryffindor\" honour and all that."
                m "You just keep massaging that spot..."
                m "Oh, yes..."
                call her_main("...............","base","down")

        m "Yes... Keep stroking it."
        call her_main("..............","angry","wink")
        m "Now I want you to say..."

        menu:
            m "..."
            "{size=-4}\"I fantasize about being raped by my father.\"{/size}":
                $ mad += 11
                call her_main("I do not!","angry","angry")
                m "I know. Just say it."
                call her_main("My father? That's disgusting, [genie_name]!","angry","angry",emote="01")
                m "Humour me."
                call her_main("...........","annoyed","annoyed")
                call her_main("Well...","open","down")
                call her_main("Sometimes I fantasize about being raped...")
                call her_main(".......")
                m "I see. And in those fantasies of yours..."
                m "Who is doing the raping?"
                call her_main("My father...?","angry","base")
                m "Do you enjoy it?"
                call her_main("No. I cry and beg for him to stop!","angry","down_raised")
                m "Heh... Nice."
                call her_main(".......","angry","down_raised")
                m "Well, this wasn't that hard, was--"
                call her_main("I scream for my Mommy but she is still at work...","mad","worried",tears="soft")
                m "Huh?"
                call her_main("My daddy takes me to my room...","normal","worriedCl")
                call her_main("He throws me on my bed!")
                call her_main("I cry \"No, daddy, please, I'm still a virgin!\"","scream","worriedCl")
                call gen_chibi("handjob_pause")
                call her_main("But He doesn't listen! He rips my panties off!","grin","dead")
                call her_main("I beg him to stop! I scream and I scream!","angry","base",tears="soft")
                m "Uhm, [hermione_name]?"
                call her_main("Yes?","angry","base",tears="soft")
                m "You are not stroking my cock anymore..."
                call her_main("Oh, I am sorry, [genie_name].","grin","worriedCl",emote="05")
                call her_main("I got lost in thought...")
                call gen_chibi("handjob")
                call her_main("But everything I just said is not true of course!","open","base")
                call her_main("I never have fantasies like that!")
                m "Right."

            "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
                call her_main("What?!","angry","wide")
                call her_main("That's disgusting.","annoyed","suspicious")
                call her_main("Dogs carry {size=+5}STD{/size}s, [genie_name].","open","closed")
                m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
                m "Means that they can only be spread to the same species."
                call her_main("............","open","suspicious")
                m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
                call her_main("What does getting \"knotted\" mean?","normal","frown")
                m "Ehm... Well..."
                m "Ah, it doesn't matter."
                m "Just say the thing!"
                call her_main("Fine!","normal","base")
                call her_main("Sometimes I get lonely and let my dog mount me.","open","suspicious")
                m "That sounded so fake..."
                call her_main("Because we don't even own a dog!","normal","frown")
                m "Fine, whatever, let's just move on then..."

            "{size=-4}\"-Manual user input-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt
                # the player to enter the name they've chosen.

                $ tmp_name = renpy.input("(Use keyboard to enter the phrase.)")

                $ tmp_name = tmp_name.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if tmp_name == "":
                    $ tmp_name="I'm a whore."
                    call her_main("Hm...?","annoyed","worriedL")
                    call her_main("Should I just say \"I'm a whore\" as usual?")
                if one_out_of_three == 1:
                    call her_main("I don't want to say that...","annoyed","worriedL")
                    m "Oh, just do it, [hermione_name]."
                    call her_main("...........","annoyed","worriedL")
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "He-he..."
                elif one_out_of_three == 2:
                    call her_main("Huh?","annoyed","worriedL")
                    call her_main("What does That have to do with anything?")
                    m "Just say it."
                    call her_main("......","annoyed","worriedL")
                    m "Come on, humour me."
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "He-he..."
                elif one_out_of_three == 3:
                    call her_main("...........","annoyed","worriedL")
                    call her_main("Do I really have to?")
                    m "Just say it."
                    call her_main("[tmp_name]","scream","angryCl")
                    g9 "He-he..."

        #CUMMING
        m "Hm..."
        m "I love that thing you do with the palm of your hand!"
        call her_main("You noticed...?","angry","wink")
        call her_main("Shall I do it some more then?")
        call blkfade

        ">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(I think this is it! Should I give her a waring?){/size}"

        menu:
            m "..."
            "\"(Yes, I must warn her).\"":
                g4 "I think I'm about to--"
                if her_whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                ">Hermione swiftly pulls her shirt up..."
                ">She then pushes your already dribbling cock against her belly and covers it up again..."
                ">The sensation of her skin under your engorged cock almost makes you lightheaded..."
                ">Hermione placed your cock a bit higher than you would expect..."
                ">You can feel her incredibly soft tits rubbing against the tip of your cock..."

                call cum_block

                g4 "{size=+5}ARGH! YES!!!{/size}"


                call play_music("chipper_doodle") # HERMIONE'S THEME.

                call her_main("!!!!!!!!!!!","shock","wide",ypos="head")

                call gen_chibi("cumming_under_shirt")
                hide screen blktone
                call hide_blkfade
                call ctc

                $ aftersperm = True

                g4 "Argh! You whore!"
                show screen blktone
                call her_main("Yes, [genie_name]! Just let it out!","base","down",xpos="right",ypos="base")
                g4 "Argh! Fucking slut!"
                call her_main("Ah!! It's so hot!","smile","glance")
                call her_main("And it's getting everywhere! So much of it!","soft","ahegao")
                call her_main("...[genie_name].")
                g4 "Argh!!!"
                m "............"
                m "I think I am done..."
                call her_main("Ah, alright...","angry","wink")
                call her_main("..............","base","down")
                call her_main("You came so much this time, [genie_name]...","soft","ahegao")
                call ctc
                call blkfade

                ">Hermione releases your still pulsating cock."

                hide screen chair_left
                hide screen desk
                call her_chibi("stand","desk","base")
                call gen_chibi("hide")
                show screen genie
                show screen bld1
                hide screen blkfade

                if daytime:
                    call her_main("Well, I think I'd better go now... my Classes are about to start.","base","base",xpos="right",ypos="base")
                else:
                    call her_main("Well, I think I'd better go now...  It's getting late.","base","base",xpos="right",ypos="base")

                m "Will you be alright in those clothes?"
                call her_main("What?","open","down")
                call her_main("Oh. Yes, I will be fine...","grin","baseL")
                call her_main("It may soak through a little here and there, but I doubt that anyone will notice.","base","happyCl")
                m "Hm... You could just put it in your mouth next time, and avoid the trouble..."
                call her_main("And swallow your hot spunk like that, [genie_name]?","angry","wink")
                m "Would keep your clothes clean."

                if her_whoring <= 15:
                    call her_main("With all due respect [genie_name]...","upset","closed")
                    call her_main("Not for the meagre 45 points...","angry","wink")
                    call her_main("Speaking of which. Can I get may payment now please?")
                else:
                    call her_main("Maybe next time...","angry","wink")
                    call her_main("Can I get may payment now please?","angry","wink")

            "\"(Nah... no need).\"":
                g4 "Here! Take this, whore!"
                if her_whoring >= 18: # LEVEL 07
                    jump hg_pf_TouchMe_KissSuck
                else:
                    pass
                with hpunch
                g4 "ARGH!"
                call blkfade

                call her_main("WHAT?!","shock","wide",ypos="head")
                g4 "Take this!"

                call cum_block

                g4 "{size=+5}ARGH! YES!!!{/size}"

                call her_main("!!!!!!!!!!!","shock","wide",ypos="head")

                call gen_chibi("cumming_under_shirt")

                hide screen bld1
                call hide_blkfade
                call ctc

                $ aftersperm = True
                call her_main(".......................","angry","wide",ypos="head")
                call gen_chibi("cumming_on_shirt_pause")
                m "Yes... I Feel so much better now..."
                call ctc

                hide screen hermione_main
                with d3

                $ u_sperm = "characters/hermione/face/auto_06.png"
                $ uni_sperm = True

                call her_main("","soft","base",tears="soft",xpos="right",ypos="base")
                call ctc
                her ".........."
                m "Well, I think that's about it..."
                call blkfade

                call her_chibi("stand","desk","base")
                hide screen chair_left
                hide screen desk
                call gen_chibi("hide")
                show screen genie
                call play_music("chipper_doodle") # HERMIONE'S THEME.

                hide screen blkfade
                call her_main("[genie_name]! What have you done?","scream","worriedCl")

                m "What?"
                call her_main("You came all over me, [genie_name]...","scream","worriedCl")
                call her_main("What a mess...","angry","down_raised")
                call her_main("[genie_name], you should have warned me.","upset","closed")
                m "It's your fault, [hermione_name]!"
                call her_main("My fault?","angry","base")
                m "Yes! You got me going too well..."
                m "I forgot about everything else..."
                call her_main("Oh...","angry","wink")
                her "Well, what's done is done..."
                call her_main("I will just wipe it off and hope that nobody will notice...","grin","dead")
                call her_main("Can I get my payment now?","angry","wink")

    label done_with_handjob:

    call blkfade

    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35

    call h_action("none","update") #Resets clothing.

    hide screen hermione_main
    hide screen hermione_ass
    hide screen jerking_off_01
    hide screen groping_01
    hide screen groping_02
    hide screen groping_naked_tits

    call her_chibi("stand","desk","base")

    hide screen chair_left
    show screen genie
    show screen hermione_main
    hide screen blktone
    hide screen blkfade
    show screen bld1
    call her_main(trans="fade",xpos="right",ypos="base")

    m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"."
    $ gryffindor +=current_payout

    call her_main("Thank you, [genie_name]...","soft","baseL")

    $ hg_pf_TouchMe_OBJ.points += 1

    if her_whoring < 15:
        $ her_whoring +=1

    if her_whoring >= 12 and her_whoring < 15:
        $ hg_pf_TouchMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

    if her_whoring >= 15 and her_whoring < 18:
        $ hg_pf_TouchMe_OBJ.hearts_level = 2 #Event hearts level (0-3)

    jump end_hg_pf


label hg_pf_TouchMe_KissSuck: #Jumps here after event #03 and if WHORING >= LEVEL 07 ### KISS SUCK! ###
    ">Hermione swiftly puts the tip of your cock on her lips, as if to give it a kiss..."
    ">The simple gesture makes your dick practically explode with pleasure and waves of cum."

    call cum_block

    g4 "{size=+5}ARGH! YES!!!{/size}"
    call gen_chibi("handjob_kiss","desk","base")

    hide screen hermione_main
    hide screen bld1
    call hide_blkfade
    call ctc

    call her_main("*Gulp!-Gulp!-Gulp!*",ypos="head")
    g4 "Argh! You little whore!"
    g4 "Yes, you slut! Drink my cum! Drink all of it!"
    call her_main("*Gulp!-Gulp!-Gulp!*",ypos="head")
    g4 "Argh... Yes!"
    call nar(">You notice that Hermione is barely able to keep up with the amount of hot cum your cock is pumping into her mouth.")
    call her_main("*Gulp!-Gulp!-Gulp!*",ypos="head")
    g4 "Ah..."
    g4 "This feels great..."
    call her_main("*Gulp!* *Gulp!* *Gulp!*",ypos="head")
    m "I think that's it, [hermione_name]..."
    m "You can let go now..."
    call blkfade

    hide screen chair_left
    hide screen desk
    call her_chibi("stand","desk","base")
    call gen_chibi("hide")
    show screen genie
    with d3

    call her_main("","full_cum","dead",xpos="mid",xpos="base")
    call ctc
    her "........................................."
    call her_main("GULP!!!","cum","worriedCl")
    call her_main("Gu-ah-a...","open_wide_tongue","down_raised")

    hide screen blkfade
    call her_main(trans="fade",xpos="right",xpos="base")
    pause.5

    show screen bld1
    call her_main("I swallowed it all, [genie_name]!","grin","dead")
    m "Good girl..."
    call her_main("At one point I thought I was going to choke...","grin","dead")
    her "There was so much of it..."
    m "Well, the deed is done, and your uniform is perfectly clean."
    call her_main("Yes! I know! It's So much easier this way!","base","down")

    if daytime:
        call her_main("I can just go to classes now as if nothing ever happened.","angry","wink")
    else:
        call her_main("I can just go and spend some time with the guys in the common room now and nobody will know...","base","down")

    m "Yes... With your belly full of semen..."
    call her_main("[genie_name]!","angry","base")
    her "...Can I just get paid now, please, [genie_name]?"

    jump done_with_handjob
