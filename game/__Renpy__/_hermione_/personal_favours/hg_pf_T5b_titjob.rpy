

### Hermione Titjob ###

label hg_pf_titjob: #LV.6 (Whoring = 15 - 17)

    call reset_menu_position

    if hg_pf_titjob.points == 0:
        m "{size=-4}(Should I ask her for a titjob?){/size}"
    else:
        g9 "{size=-4}(I feel like putting my cock between those tits again!){/size}"

    if hg_pf_titjob.points < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    $ current_payout = 45

    call bld

    #First Event.
    if hg_pf_titjob.points == 0:
        m "Now [hermione_name]."
        call her_main("Yes, [genie_name]?","base","base",xpos="right",ypos="base")
        m "Have you ever given someone a titjob?"

        if her_whoring < 15:
            jump too_much

        call her_main("A titjob?","annoyed","annoyed")
        m "It's where you wrap those fat tits of your around a cock and then shake them up and down and up and..."
        call her_main("[genie_name]!","angry","angry")
        m "So have you ever given a boy a titjob?"
        call her_main("......","disgust","glance")
        call her_main("{size=-7}No...{/size}","angry","worriedCl",emote="05")
        m "Hmmm? What was that?"
        call her_main("No!!!","scream","worriedCl")
        m "Well today is your lucky day!"
        call her_main("Lucky? How would you call this lucky?","disgust","glance")
        m "it's not every day you learn something new."
        call her_main("I'm in school! It's my job to learn something new everyday!","scream","angryCl")
        m "At least this is something you'll be able to use in the real world."
        call her_main("......","disgust","glance")
        call her_main("{size=-7}I want 100 points...{/size}","angry","worriedCl",emote="05")
        m "Speak up [hermione_name]."
        call her_main("I want 100 points!","scream","worriedCl")

        label back_to_titjob_choices:
        menu:
            m "..."
            "\"You will get 15 house points and I promise not to cum on you.\"":
                $ her_mood +=7
                call her_main("You expect me to give you a titjob for 15 points!","annoyed","angryL")
                her "I don't know who you think I am but I am not going to do this for 15 measly points!"
                call her_main("(Besides, I don't really mind being covered in his sticky load...)","annoyed","angryL")
                jump back_to_titjob_choices
            "\"you will get 45 house points.\"":
                if her_mood > 7: #You could spam points into infinity with the choice above.
                    $ her_mood = 7
                call her_main(".....","annoyed","angryL")
                call her_main("45 house points...?","open","down")
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                call her_main("Yes, yes it is, [genie_name].","annoyed","annoyed")
                m "Great!"
            "\"you will get 100 house points.\"":
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                $ current_payout = 100
                $ her_mood = 0
                call her_main("100 house points?!","scream","wide_stare")
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "SO that's a yes?"
                call her_main("Of course!","smile","happyCl")
                call her_main("For 100 points I'll give you the best damn titjob of your life!","smile","happyCl",emote="06")

        hide screen hermione_main
        hide screen bld1
        call blkfade

        call play_music("playful_tension") #HERMIONE
        hide screen genie
        show screen chair_left
        show screen desk
        call her_chibi("stand","mid","base")
        call gen_chibi("hold_dick","desk","base")
        call hide_blkfade
        call ctc

        call her_main("...........","open","base")
        call her_main("(It's so big...)","base","down")
        m "Get to it [hermione_name]."
        call her_main("Right...","angry","worriedCl",emote="05")
        call her_main("","annoyed","annoyed")
        pause.2

        call hg_titjob_1
        call hg_titjob_1_cumming

        jump end_hg_titjob


    #Second Event.
    elif hg_pf_titjob.points == 1:
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","base","base",xpos="right",ypos="base")
        m "How do you feel about wrapping those nice tits of yours around my cock again?"
        call her_main("Only nice?","upset","closed")
        m "Fine, fine."
        m "How do you feel about wrapping those perfect tits of yours around my cock again?"
        call her_main("Of course, [genie_name].","base","glance")
        m "You like it when I call them perfect don't you?"
        call her_main(".............","base","down")
        g9 "you don't have to say anything, just bring those perfect tits over here."
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","worriedCl")
        call her_main("yes [genie_name]","grin","baseL")
        stop music fadeout 4.0

        call hg_titjob_1
        call hg_titjob_1_cumming

        jump end_hg_titjob


    #Third Event.
    elif hg_pf_titjob.points >= 2:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base",xpos="right",ypos="base")
        m "You don't mind wrapping those perfect tits of yours around my cock again, do you?"
        call her_main("{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised")
        if her_whoring < 21:
            call her_main("As long as I am getting paid...","soft","squintL")
            m "Well, come here then. Time to earn those points."
        else:
            call her_main("Of course not [genie_name]...","open","baseL")
            m "Well, come here then."
            call her_main("","base","glance")
            pause.1

        call hg_titjob_3
        call hg_titjob_3_cumming

        jump end_hg_titjob



### First Blowjob ###

label hg_titjob_1:

    #Hermione removes her top.
    $ hermione_wear_bra = False
    call set_her_action("lift_top")
    pause.5

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.5

    hide screen bld1
    call blkfade

    hide screen genie
    show screen chair_left
    hide screen desk
    show screen desk
    call her_chibi("hide")
    call gen_chibi("titjob","mid","base")

    if hermione_costume:
        call set_her_action("lift_top")
    else:
        call set_her_action("lift_breasts")

    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 5
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with d3

    call nar(">Hermione clumsily wraps her tits around your cock...")
    m "That's a start. Now, up and down..."
    call her_main("Alright...","angry","worriedCl",emote="05",ypos="head")
    hide screen bld1
    call hide_blkfade
    call ctc

    call play_music("playful_tension") # SEX THEME.
    call bld
    g9 "mmmm..."
    $ ccg1 = 6
    if hg_pf_titjob.points == 0:
        call her_main("...","base","base")
        call her_main("Does it... feel good?","base","squint")
        m "Good?"
        m "It feels amazing."
        call her_main("Oh...","base","squint")
        call her_main("......")
        call her_main("Thank you [genie_name]","base","baseL")

    call her_main("[genie_name]...?","soft","base")
    m "What is it?"
    $ ccg1 = 7
    call her_main("Promise me you won't cum on my... face...","upset","wink")

    $ d_flag_01 = False #If TRUE Genie promised to warn her.
    menu:
        m "..."
        "\"I promise not to cover that sweet little face of yours...\"":
            $ d_flag_01 = True #If TRUE Genie promised to warn her.
            $ ccg1 = 6
            call her_main("Thank you, [genie_name].","base","squint")
        "\"Hmmmm... We'll see how I feel later...\"":
            $ ccg1 = 8
            call her_main("Hmmmmph.","annoyed","annoyed")
            call her_main("At least avoid my hair...","normal","worriedCl")

    $ ccg1 = 5
    call her_main("........","open","base")
    m "............."
    call her_main(".............","normal","worriedCl")
    call her_main("Err... [genie_name]?")
    m "Yes, what is it?"
    call her_main("Are you almost there?","open","base")
    m "Why?"
    $ ccg1 = 7
    if daytime:
        call her_main("Well, it's just that my classes are about to start...","upset","wink")
    else:
        call her_main("Well, it's just that I promised Ginny that we'd hang out tonight...","upset","wink")
        call her_main("She's pretty upset that I'm spending so much time in here...")
    m "Do you need the points or not?"
    $ ccg1 = 6
    call her_main("I do, [genie_name]! I'm sorry...","grin","worriedCl")
    call her_main("I'll just keep on stroking it then...")
    m "Well, you could make this finish up a little faster..."
    call her_main("Really? What can I do [genie_name]?","base","baseL")

    menu:
        m "..."
        "\"Tell me how much you love your tits.\"":
            $ ccg1 = 5
            call her_main("What?","upset","wink",ypos="head")
            $ ccg1 = 6
            call her_main("My breasts?")
            m "you know, How good they feel..."
            m "The looks that you get because of them."
            call her_main("Oh, alright then...","base","base")
            call her_main("There was this one time in the library...","smile","baseL")
            call her_main("It was empty apart from this first year boy sitting across from me...")
            m "Heh... good. Go on."
            call her_main("Well it was so hot that I'd taken my vest off...","base","squint")
            m "I bet it was hot..."
            call her_main("He was trying to act sly but I could tell that he kept sneaking glances at them...","base","baseL")
            call her_main("So I started undoing the buttons... Slowly at first, not enough for him to suspect anything....","base","glance")
            m "mmmmm, you little slut."
            $ ccg1 = 9
            call her_main("By the third button he couldn't take his eyes off of me.","base","down")
            call her_main("As I slowly undid the fourth he moved his hands under the desk...")
            m "Really?"
            call her_main("Really... I could almost hear him stroking it...","base","ahegao_raised")
            $ ccg1 = 10
            call her_main("When I undid the fifth button he could almost see my nipples...","open","baseL")
            g9 "Do you have no shame?"
            $ ccg1 = 5
            call her_main("[genie_name]! I was just trying to cool down...","base","down")
            m "I'm just kidding, keep going."
            call her_main(".....","base","glance")
            $ ccg1 = 9
            call her_main("By the sixth button almost nothing was hidden...")
            call her_main("He could see my naked tits...","base","suspicious")
            call her_main("and he just stared at them... not even trying to hide what he was doing...")
            call her_main("when I undid the final button it was too much for him...")
            $ ccg1 = 10
            call her_main("He shot his cum under the table, covering my legs and feet in his hot cum!","silly","ahegao")
            g4 "!!!"
            call her_main("Come on [genie_name] cover me as well! Cum all over my tits!","grin","ahegao")

            return

        "\"Stick your tongue out tilt you head down!\"":
            $ ccg1 = 5
            call her_main("What?","base","base",ypos="head")
            m "Just do it, slut."
            $ ccg1 = 11
            call her_main("Like this?","open_wide_tongue","squintL")
            m "Yes, good. Tilt your head down as far as it'll go."
            call her_main(".....................","open_wide_tongue","base")
            m "Yes... Good..."
            call her_main("...........","open_wide_tongue","base")
            call her_main("...........")
            $ ccg1 = 9
            call her_main("I can't keep my mouth open for so long, [genie_name]. I will start to drool...","open","base")
            m "But I want you to drool... all over those perfect tits of yours"
            call her_main("What? You think they're perfect?","open","base")
            m "As perfect as any mortal, [hermione_name]!"
            $ ccg1 = 11
            call her_main(".......","base","ahegao_raised")
            m "Now stick it back out again and try to get it as close to the tip of my cock as you can"
            call her_main("............","normal","worriedCl")
            call her_main("A-ha.....","open_wide_tongue","base")
            m "Good, [hermione_name]."
            call her_main("..............","open_wide_tongue","base")
            m "Yes, keep on stroking my cock."
            ">You thrust up as she pushes her tits down causing the tip of your cock to touch her wet tongue."
            call her_main("..................","open_wide_tongue","base")
            g4 "Oh that's good..."
            call her_main(".................","open_wide_tongue","base")
            ">You thrust into her tongue again."
            m "That's it slut taste it!"
            call her_main(".....................","open_wide_tongue","angryCl")
            m "Yes, you big titted whore!"
            call her_main("......................","open_wide_tongue","angry")
            m "I want to cum in that little slutty mouth of yours..."
            call her_main("................","open_wide_tongue","angry")

            return


label hg_titjob_1_cumming:
    with hpunch
    g4 "{size=-4}(Here it comes! Where should I aim for?){/size}"

    menu:
        m "..."
        "-cum in her mouth-":
            $ her_mood += 3
            g4 "Here it comes, [hermione_name]! You better be ready!"
            $ ccg1 = 13
            call her_main("What? already?!","shock","wide",ypos="head")
            g4 "{size=+5}Yeah, your tits felt great!!!{/size}"
            g4 "{size=+5}You little whore!!!{/size}"
            hide screen bld1
            call blkfade

            call her_main("No, [genie_name], wait, not on my fa--","angry","base")
            g4 "{size=+5}Open wide slut!!{/size}"
            call her_main("Not in my mou-","scream","wide")
            $ ccg1 = 12
            ">You grab the back of Hermione's head and force your cock into her open mouth..."
            call her_main("!!!!!!!","shock","worriedCl")
            ">The sensation of her warm mouth and squirming tongue overwhelm you and you start cumming like crazy"
            call cum_block

            g4 "{size=+5}ARGH! YES!!! Take it, slut!{/size}"
            call her_main("!!!!!!!!!!!","shock","wide")

            call gen_chibi("titjob_cum_in_mouth","mid","base")
            hide screen bld1
            call hide_blkfade
            stop music fadeout 1.0
            call ctc

            call bld
            call her_main(".......................","full_cum","down",cheeks="blush")
            m "mmmmmm that felt great...."
            call her_main(".......................","full_cum","down",cheeks="blush")
            m "How are you feeling?"
            call her_main(".......................","full_cum","down",cheeks="blush")
            m "[hermione_name]?"

            call play_music("chipper_doodle") # HERMIONE'S THEME.

            hide screen bld1
            call gen_chibi("titjob_pause","mid","base")
            pause.5

            show screen bld1
            $ ccg1 = 15
            call nar(">Hermione opens her mouth, letting your cum fall out onto her tits.")
            call her_main("*ptui*","open_wide_tongue_cum","angry")

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True

            $ ccg1 = 16
            call her_main("Why on earth did you cum in my mouth!","angry","worriedCl",emote="05")
            m "well you did say not to cum on your face."
            pause.5
            hide screen bld1
            call blkfade
            $ ccg1 = 17
            ">Hermione releases your still pulsating cock."
            pause.5

            call gen_chibi("hold_dick","desk","base")
            call her_chibi("stand","mid","base")
            call hide_blkfade
            pause.5

            call her_main("Ughhh... you came so much! I had to swallow most of it!","angry","worriedCl",emote="05",xpos="right",ypos="base")
            m "That's your fault for doing such a great job..."
            call her_main("I don't want to hear it...","angry","worriedCl",emote="05")
            if daytime:
                call her_main("My classes are about to start and now I'm covered in your sperm...","angry","worriedCl",emote="05")
            else:
                call her_main("At this hour The \"Gryffindor\" common room will be full of people...","angry","worriedCl",emote="05")
                call her_main("And now I'm going to have to go there, smelling like... spunk...")
                call her_main("Maybe if I just run to bed no one will be able to tell...","angry","base")

            m "You could have swallowed..."
            m "Then there wouldn't have been any clean up."
            call her_main("Swallow all of that?","angry","down_raised")
            call her_main("I don't think I have enough room in my stomach...")
            call her_main("Is that all [genie_name]?","annoyed","closed")
            call blkfade
            hide screen ccg
            with d3
            $ aftersperm = True

            return

        "-cover her tits-":
            with hpunch
            g4 "ARGH!"
            call blkfade
            $ ccg1 = 13
            call her_main("WHAT?!","shock","wide",ypos="head")
            g4 "Take this slut!"

            call cum_block

            g4 "{size=+5}ARGH! YES!!!{/size}"
            call her_main("!!!!!!!!!!!","shock","wide")
            $ ccg1 = 18
            call gen_chibi("titjob_cum_on_tits","mid","base")
            hide screen bld1
            call hide_blkfade
            call ctc

            call bld
            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True
            call her_main(".......................","angry","wide")
            m "Yes... That's it..."
            call her_main("..........","soft","base",tears="soft")
            m "Well, I think that's about it..."
            her ".........."
            hide screen bld1
            call blkfade

            call gen_chibi("hold_dick","desk","base")
            call her_chibi("stand","mid","base")
            pause 1
            call hide_blkfade
            pause.5

            call her_main("","annoyed","baseL",xpos="right",ypos="base")
            call ctc
            $ ccg1 = 17
            if daytime:
                call her_main("[genie_name]! How could you cum so much?!","scream","worriedCl")
                call her_main("It's like you dumped a bucket of spunk over my chest!","annoyed","angryL")
                call her_main("My classes are about to start and I can't go looking like this!","open","down")
                m "Of course you can, just wipe it off or something..."
                m "Nobody will even notice... Except for the smell maybe..."
                call her_main("...I would like to get paid now.","annoyed","annoyed")
            else:
                call her_main("How can one person cum so much!","annoyed","angryL")
                her "how Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                m "Just wipe it off or something."
                m "It's not like it'll be the first time you've gone to bed smelling like cum."
                call her_main("...I would like to get paid now.","annoyed","annoyed")

            call blkfade
            hide screen ccg
            with d3
            $ uni_sperm = False
            $ aftersperm = True

            return



### Third Blowjob ###

label hg_titjob_3:

    #Hermione removes her top.
    $ hermione_wear_bra = False
    call set_her_action("lift_top","skip_update")
    pause.5

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.5

    hide screen bld1
    call blkfade
    pause.8

    hide screen genie
    show screen chair_left
    show screen desk
    call her_chibi("hide")
    call gen_chibi("titjob","mid","base")

    ">Hermione wraps her plump tits around your cock..."

    if use_cgs:
        $ ccg_folder = "herm_boob"
        $ ccg1 = 6
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        with d3

    call set_her_action("lift_breasts","skip_update")

    stop music fadeout 3.0
    $ ccg1 = 20
    call her_main("Do you like it when I do it like this, [genie_name]?","grin","baseL",ypos="head")
    ">Hermione starts alternating her breasts as she titfucks you."
    g9 "Actually, yes! Very nice!"
    call play_music("chipper_doodle") # HERMIONE'S THEME.

    call hide_blkfade
    call ctc

    show screen bld1
    call her_main("...","base","glance")
    m "Yes, yes, like that..."
    m "Hm... You are getting pretty good at this."
    $ ccg1 = 21
    call her_main("Thank you, [genie_name].","base","happyCl")
    call her_main("I figured with how nice you've been it's the least I could do...")
    m "Hm..."

    menu:
        m "..."
        "\"What do you think of my cock?\"":
            $ ccg1 = 22
            call her_main("Huh?","open","base",ypos="head")
            call her_main("Your cock?","angry","worriedCl",emote="05")
            m "What do you think abo-"
            $ ccg1 = 23
            call her_main("It's amazing....","upset","closed")
            m "go on..."
            call her_main("If I have the perfect tits then this...","soft","ahegao")
            call nar(">She squeezes her tits around your cock.")
            $ ccg1 = 22
            call her_main("This is the perfect cock","grin","dead")
            m "Perfect?"
            call her_main("Perfect.","base","down")
            call her_main("Perfect size...","soft","down")
            call her_main("Perfect shape...")
            $ ccg1 = 24
            call nar("Hermione tilts her head down and licks the tip of your cock.")
            call her_main("...","open_tongue","ahegao")
            $ ccg1 = 23
            call her_main("Perfect taste...","soft","ahegao")
            m "..."
            $ ccg1 = 25
            call her_main("I think your perfect cock should be shared around the school. ","scream","angryCl")
            m "Well, I wouldn't go that far--"
            call her_main("Listen to me, [genie_name]!","soft","ahegao")
            call her_main("I think your perfect cock should be worshipped as part of the school curriculem!")
            $ ccg1 = 24
            call her_main("Girls will be required to come in and bask in it's glory!")
            m "OK, I think I've heard enough."
            $ ccg1 = 21
            call her_main("Too much?","angry","wink")
            m "Yeah, just a bit."
            call her_main("Sorry [genie_name], I got a bit carried away...","angry","worriedCl",emote="05")
            m "No biggie. Just keep on massaging it with those big tits of yours."
            call her_main(".................","soft","ahegao")

            call nar(">Hermione keeps on stroking your cock.","start")
            $ ccg1 = 25
            call nar(">She spits on it to help lubricate it.","end")
            $ ccg1 = 21
            m "Yes, yes... That's it slut."

        "\"Call yourself a big titted whore!\"":
            $ ccg1 = 22
            call her_main("Excuse me?","open","base",ypos="head")
            $ ccg1 = 23
            call her_main("Oh... I am a big tittedwhore!","soft","ahegao")
            m "Good. Glad we established that."
            m "Now I want you to say..."

            menu:
                m "..."
                "\"I am a shameless cumslut!\"":
                    $ ccg1 = 22
                    call her_main("Of course.","base","down",ypos="head")
                    $ ccg1 = 24
                    call her_main("I am a shameless cumslut.","soft","ahegao")
                    $ ccg1 = 21
                    call her_main("A dirty little slut who's addicted to the the taste of my headmaster's cum...","grin","dead")
                    m "Yes! Good!"
                "\"I love being covered in cum!\"":
                    $ ccg1 = 24
                    call her_main("I love being covered in cum!","soft","ahegao",ypos="head")
                    call her_main("hot...")
                    call her_main("sticky...")
                    call her_main("smelly...")
                    call her_main("cum...")
                    $ ccg1 = 23
                    call her_main("...................................","grin","dead")
                    $ ccg1 = 21
                    call her_main("How was that, [genie_name]?","angry","wink")
                    m "Perfect."

        "\"This is really good. Did you practice?\"":
            $ ccg1 = 22
            call her_main("Hm?","base","happyCl",ypos="head")
            $ ccg1 = 21
            call her_main("Sort of... Well not on another cock...","angry","wink")
            m "On what then?"
            $ ccg1 = 22
            call her_main("Well I spoke to Ginny...","grin","baseL")
            m "A friend of yours?"
            call her_main("yes. I asked if she had any tips for this sort of thing...","base","baseL")
            $ ccg1 = 21
            call her_main("She said the best way to improve was practice...","base","squint")
            m "Practice on what?"
            $ ccg1 = 22
            call her_main("On Ginny","smile","baseL")
            $ ccg1 = 23
            call her_main("Well... on her... arm.","angry","wink")
            m "You titfucked your friends arm?"
            $ ccg1 = 25
            call her_main("Just as practice!","grin","worriedCl",emote="05")
            $ ccg1 = 22
            call her_main("She even game me some tips...")
            $ ccg1 = 23
            call her_main("How does this feel?","base","down")
            m "mmmmm... Yes, this feels quite good."
            call her_main("Does it?","angry","wink")
            $ ccg1 = 21
            call her_main("Ginny seemed to enjoy it a lot as well...","base","ahegao_raised")
            g4 "She enjoyed it?"
            $ ccg1 = 22
            call her_main("Of course she did!","base","happyCl")
            $ ccg1 = 23
            call her_main("Who wouldn't love feeling my perfect tits...","base","closed")
            call her_main("Although I think she might have enjoyed it...","open","down")
            $ ccg1 = 22
            call her_main("A little too much...","soft","squintL")
            m "How so?"
            call her_main("Well...","soft","squintL")
            call her_main("She might have started...")
            $ ccg1 = 23
            call her_main("Playing with herself...","grin","ahegao")
            with hpunch
            with kissiris
            g4 "Yes, keep going slut"
            call her_main("As I was \"Practicing\" on her arm she might have...","open","baseL")
            $ ccg1 = 24
            call her_main("cum...","soft","ahegao")
            g4 "[hermione_name], you little slut!"
            $ ccg1 = 23
            call her_main("It was just practice!","grin","worriedCl",emote="05")
            call her_main("Err... I mean...","angry","wink")
            $ ccg1 = 21
            call her_main("It's not like I enjoyed it as well...","angry","down_raised")
            m "Yes, yes... you're not a slut at all..."
            m "Mmmmm, why don't you spit on it a little..."
            m "Oh, yes..."
            $ ccg1 = 24
            call her_main("...............","base","down")

    m "Yes... Keep stroking it."
    $ ccg1 = 23
    call her_main("..............","angry","wink",ypos="head")
    m "Now I want you to say..."

    menu:
        m "..."
        "{size=-4}\"I love teasing my father with my big tits.\"{/size}":
            $ ccg1 = 25
            call her_main("I do not!","angry","down_raised",ypos="head")
            m "I know. Just say it."
            $ ccg1 = 22
            call her_main("My father? That's gross, [genie_name]! How could you suggest that I want to fu-","soft","ahegao")
            m "Come on... Just make something up."
            call her_main("...........","angry","wink")
            call her_main("Well...","open","down")
            $ ccg1 = 21
            call her_main("Sometimes when I hug him...")
            call her_main(".......")
            m "Go on [hermione_name]..."
            $ ccg1 = 22
            call her_main("I press my tits into him...","soft","ahegao")
            m "Do you think he enjoys it?"
            call her_main("I'm not sure...","annoyed","base")
            call her_main("I think so...","soft","squintL")
            $ ccg1 = 23
            call her_main("He always tries to cover his croutch afterwards...","base","closed")
            call her_main("He even says I'm too old for hugs...","annoyed","closed")
            call her_main("But I make sure to give him a big one every night before I go to bed...")
            call her_main("So that he'll think of me...","base","down")
            call her_main("And how good I felt...","grin","dead")
            $ ccg1 = 24
            call her_main("Pressing into him...","soft","ahegao")
            m "That's it slut."
            $ ccg1 = 22
            call her_main("Then I give him a kiss on the forehead...","soft","squintL")
            $ ccg1 = 23
            call her_main("Making sure that he can see down my blouse...","grin","worriedCl",emote="05")
            call her_main("{image=textheart}{image=textheart}{image=textheart}")
            $ ccg1 = 25
            call her_main("But all of that is not true of course!","open","base")
            $ ccg1 = 22
            call her_main("None of that happens! It was just for you to imagine!")
            m "Right..."

            return

        "{size=-4}\"I love teasing my schoolmates with my perfect tits.\"{/size}":
            $ ccg1 = 23
            call her_main("I love teasing my schoolmates with my perfect tits...","soft","ahegao",ypos="head")
            m "Of course you do..."
            call her_main("I love the jealous looks from the other girls...","base","down")
            m "I bet they're jealous..."
            $ ccg1 = 21
            call her_main("I love teasing ron and harry during breakfast...","base","glance")
            $ ccg1 = 22
            call her_main("Sometimes I'll walk around with only one button done up...","base","suspicious")
            $ ccg1 = 23
            call her_main("Other times I'll just wear my vest with nothing on underneath...")
            m "And how do you feel..."
            call her_main("So good...","silly","dead")
            call her_main("One time when I was walking back from your office at night I was barely covering them...","angry","wink")
            call her_main("And as I rounded a corner...","soft","ahegao")
            $ ccg1 = 24
            call her_main("A second year boy ran head first into them...","grin","ahegao")
            m "Head first into your tits?"
            call her_main("All I could see was the top of his head...","grin","dead")
            m "What did he do?"
            call her_main("He tried to pull away...")
            m "Tried?"
            $ ccg1 = 22
            call her_main("Well I may have held him there...","base","glance")
            call her_main("Just for a little bit...","base","down")
            $ ccg1 = 23
            call her_main("Just to tell him it was alright...","base","suspicious")
            m "You little slut."
            $ ccg1 = 22
            call her_main("I think I might have broken him though...","base","down")
            $ ccg1 = 21
            call her_main("Because when I let him go he said nothing. He just stepped back slowly and walked away.","soft","ahegao")
            m "I bet I know where he went..."
            $ ccg1 = 23
            call her_main("so do i...","soft","ahegao")

            return



label hg_titjob_3_cumming:
    m "Hm..."
    m "I love your slutty tits.!"
    $ ccg1 = 22
    call her_main("Thank you [genie_name].","soft","ahegao",ypos="head")
    $ ccg1 = 23
    call her_main("Shall I rub them some more then?")
    call nar(">Hermione presses her tits together against your cock and starts rubbing it very quickly...")
    m "Oh yes!!!"
    stop music fadeout 1.0
    g4 "{size=-5}(Almost there! where should I aim?){/size}"

    menu:
        m "..."
        "\"(In her mouth).\"":
            g4 "Take this whore"
            hide screen bld1
            call blkfade

            ">You grab Hermione by the back of her head, tilting it down "
            $ ccg1 = 25
            call her_main("What are you-","angry","wink",ypos="head")
            ">You thrust up into her wet mouth, the sensation of it driving you over the edge."
            call cum_block

            g4 "{size=+5}ARGH! YES!!!{/size}"

            call play_music("chipper_doodle") # HERMIONE'S THEME.

            $ ccg1 = 26
            call her_main("!!!!!!!!!!!","shock","wide")

            call gen_chibi("titjob_cum_in_mouth")
            call hide_blkfade
            call ctc

            call bld
            g4 "Argh! You whore!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","full_cum","dead")
            g4 "Argh! you big titted slut! Take it all!"
            call her_main("......","full_cum","dead")
            m "............"
            m "Ok, I think I am done..."
            call her_main("..............","full_cum","dead")
            call her_main("........","full_cum","dead")
            call her_main("...","full_cum","dead")
            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            $ ccg1 = 27
            call her_main("*GULP*","cum","worriedCl") #play noise here
            hide screen bld1
            call ctc

            call blkfade

            pause.5
            ">Hermione releases your cock from between her tits."
            pause 1

            call gen_chibi("stand","desk","base")
            call her_chibi("stand","mid","base")

            call set_her_action("None")

            hide screen ccg
            call hide_blkfade
            pause.5

            call her_main("","soft","glance",xpos="right",ypos="base")
            call ctc

            if daytime:
                call her_main("Well, I think I'd better go now... my Classes are about to start.","base","base")
            else:
                call her_main("Well, I think I'd better go now... It's getting late.","base","base")
            m "So you're alright with swallowing now?"
            call her_main("What?","open","down")
            call her_main("Oh. I suppose so...","grin","baseL")
            call her_main("I mean it doesn't taste that bad and it means that I don't have to clean up afterwards.","base","happyCl")
            m "Hm... Are you sure you don't want people seeing your tits covered in cum..."
            call her_main("What? walk around school covered in your cum [genie_name]?","angry","wink")

            if her_whoring < 21:
                call her_main("With all due respect [genie_name]...","upset","closed")
                call her_main("I don't plan on getting a reputation as a cum loving whore...","angry","wink")
                call her_main("Not like those \"Slytherin\" girls...")
            else:
                call her_main("Hmmmmm...","soft","squintL")
                call her_main("Maybe if you ask nicely...","soft","squintL")
            call her_main("Is that all [genie_name]?","annoyed","closed")

            call blkfade
            hide screen ccg

            return

        "\"(On her tits).\"":
            g4 "Here! Take this you bit titted whore!"
            with hpunch
            g4 "ARGH!"
            hide screen bld1
            call blkfade
            $ ccg1 = 25
            call her_main("What? Already?!","shock","wide",ypos="head")
            g4 "Yeah, you're tits felt great slut!"
            call cum_block

            g4 "{size=+5}ARGH! YES!!!{/size}"
            $ ccg1 = 30
            call her_main("!!!!!!!!!!!","shock","wide")

            call gen_chibi("titjob_cum_on_tits")
            call hide_blkfade
            call ctc

            $ u_sperm = "characters/hermione/face/auto_06.png"
            $ uni_sperm = True

            $ ccg1 = 31
            call her_main(".......................","angry","wide")
            m "Aghhh... I Feel so much better now..."
            hide screen bld1
            call ctc

            call blkfade
            $ ccg1 = 32
            call gen_chibi("stand","desk","base")
            call her_chibi("stand","mid","base")

            call set_her_action("None")

            call hide_blkfade
            pause.5

            call her_main("","upset","closed",xpos="right",ypos="base")
            call ctc
            $ ccg1 = 33
            her ".........."
            m "Well, I think that's about it..."

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            $ ccg1 = 35
            call her_main("[genie_name]!","annoyed","angryL")
            m "What?"
            call her_main("You covered my chest in cum, [genie_name]...","angry","worriedCl")
            $ ccg1 = 34
            call her_main("There's so much...","open","baseL")
            m "It's your fault, [hermione_name]!"
            call her_main("My fault?","angry","base")
            m "Yes! It's those perfect tits of yours..."
            m "They just felt too good..."
            $ ccg1 = 36
            call her_main("Oh...","shock","wide")
            her "Well, I suppose it's not too bad then..."
            $ ccg1 = 37
            call her_main("I'll just wipe it off and hope that nobody notices...","upset","closed")
            m "You could lick them clean."
            call her_main("You want me to lick your cum off of my tits?","soft","ahegao")
            call her_main("I don't think so, [genie_name]...","soft","ahegao")
            her "{size=-5}Maybe next time...{/size}"
            call her_main("Is that all [genie_name]?","angry","wink")

            call blkfade
            hide screen ccg
            $ aftersperm = True

            return



### END BLOWJOB ###

label end_hg_titjob:

    hide screen ccg
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    hide screen hermione_main

    call set_her_action("none","update")

    hide screen g_c_c_u # Genie's sperm. Universal.
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    call hide_blkfade
    pause.5

    call bld
    if her_whoring < 24:
        m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"."
        $ gryffindor += current_payout

    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    call her_walk(action="leave", speed=2.5)

    if her_whoring < 21:
        $ her_whoring +=1

    $ hg_pf_titjob.points += 1

    if hg_pf_titjob.points <= 3:
        $ hg_pf_titjob.level = hg_pf_titjob.points

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    # Stats
    $ hg_pf_titjob.counter += 1

    jump end_hermione_event
