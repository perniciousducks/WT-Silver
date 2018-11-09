

### FAVOUR 1 - Cho Strips Naked ###
label cho_favor_1:
    $ current_payout = 20

    if cho_whoring <= 0:
        m "{size=-4}(All I'll do is admire her body a bit...){/size}"
        menu:
            "\"(Yes, let's do that.)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_requests

    hide screen cho_chang
    call blkfade
    pause.2
    hide screen blkfade
    call cho_main(xpos="mid",ypos="base",trans="d5")

    if cho_whoring <= 0:
        jump cho_favor_1_1 #First time event.
    elif cho_whoring <= 1:
        jump cho_favor_1_2 #Second time event.
    else:
        jump cho_favor_1_3 #Third time event.



# Favour 1 - First time event.
label cho_favor_1_1:
    menu:
        "\"Take off your top\"":
            m "[cho_name], why don't you take off your top?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Miss Granger is more than happy to show me her-"
            call cho_main("Fine...","pout","base","angry","R")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")
            $ cho_wear_top = False
            call cho_main("Sorry, about that.","open","base","sad","mid")
            g9 "Don't worry, girl. You're doing great!"
            call cho_main("Thanks.","angry","base","sad","R")
            m "Now take off your skirt..."
            call cho_main("O-okay...","horny","base","sad","down")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")
            $ cho_wear_bottom = False
            call ctc
            jump let_cho_strip

        "\"Take off your skirt\"":
            m "[cho_name], why don't you take off your skirt?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Just thinking about Miss Granger's ass makes me-"
            call cho_main("Fine, I'll do it...","pout","base","angry","R")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")
            $ cho_wear_bottom = False
            call cho_main("There, my skirt is gone!","angry","base","sad","down")
            g9 "I can see that, Miss Chang!"
            m "Now take off your shirt..."
            call cho_main("O-okay...","open","base","sad","mid")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")
            $ cho_wear_top = False
            call ctc
            jump let_cho_strip

        "\"Come here and suck my cock!\"":
            m "{size=-5}(Too early for this... It's always too early for this...){/size}"
            jump cho_favor_1_1

        "\"Do you eat ass, Miss Chong?\"":
            call cho_main("Miss... Chong?","open","wide","raised","mid")
            call cho_main("My name Is Chang, [cho_genie_name],... Cho Chang!","open","angry","angry","mid")
            call cho_main("...","pout","suspicious","angry","R")
            m "..."
            m "(She didn't answer my question...)"
            $ cho_mad += 5
            jump cho_favor_1_1


    label let_cho_strip:
        call cho_main("Um, I forgot to ask, but how many points do I get for this?","open","base","sad","mid")
        m "You're a terrible negotiator."
        call cho_main("I know.","smile","base","sad","R")
        call cho_main("What do you pay Hermione?","soft","base","raised","mid")
        m "(Too much if you ask me...)"
        m "A couple of points, maybe..."

        call cho_main("I bet my body is worth more than hers!","open","base","base","mid")
        call cho_main("Does Hermione have abs like this? Of course she doesn't!","horny","base","raised","down")
        if her_whoring < 17:
            call cho_main("That boring book glutton is sitting at the library all day as if it's her home...","open","angry","angry","mid")
        else:
            call cho_main("That stupid slut can't spend even a single day without flirting with somebody that has legs attached...","open","angry","angry","mid")

        call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","angry","suspicious","angry","mid")
        call cho_main("My body's at the absolute peak of human and wizard conditioning!","open","angry","angry","mid")
        g4 "It is quite impressive, I've got to say!"
        call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
        call cho_main("Now... How badly do you want me to take off the rest?","soft","angry","base","mid")

        m "(...)"
        m "I will give you..."

        menu:
            "-10 points-":
                call cho_main("(10 points... I hope that's a good price.)","horny","suspicious","sad","downR")
                call cho_main("I guess that's ok, [cho_genie_name].","angry","suspicious","sad","down")
                call blktone
                m "(Really? She'd strip down for barely anything?)"
                m "(Even Hermione gets more points for just her mindless talking...)"
                g4 "(Now she made me feel bad... I should probably pay her a little more.)"
                call hide_blktone
                m "Only the first time, Miss Chang. I will pay you 20 regularily."
                call cho_main("Ok! Thank you, [cho_genie_name].","smile","base","sad","mid")
                $ current_payout = 10
            "-20 points-":
                call cho_main("20 sounds reasonable.","soft","base","base","R")
                m "It sure does..."
                call cho_main("(...)","angry","base","base","R")
                m "(Is it just me, or is the middle choice always the boring one...?)"
                m "Anyway..."
                $ current_payout = 20
            "-100 points-":
                call cho_main("100?","scream","wide","raised","mid")
                call cho_main("Wow, that's a lot!","open","base","raised","L")
                m "(Yeah, it's way too much... what was I thinking?)"
                m "Just today, Miss Chang. I will pay you 20 after this time."
                call cho_main("Thank you so much, [cho_genie_name].","smile","base","base","mid")
                $ current_payout = 100

        g9 "Why don't you thank me by taking off that bra?"
        call cho_main("Of course, sir.","horny","base","sad","down")
        pause.5
        $ cho_wear_bra = False
        call ctc
        call cho_main("I bet my tight body looks way better than Hermione's...","soft","base","raised","mid")

        menu:
            "-Yeah, she's gross-":
                m  "Miss Granger's body is nothing compared to yours."
                call cho_main("Really?","open","wide","raised","mid")
                m  "Her tits sag too much, and her fat hips are disgusting..."
                call blktone
                g4 "(I think something inside me just died saying this.)"
                call hide_blktone
                call cho_main("She really is a...","open","closed","raised","mid")
                call cho_main("...stupid...","angry","closed","angry","mid")
                call cho_main("...fat...","angry","suspicious","angry","mid")
                call cho_main("...cow, isn't she?","quiver","suspicious","angry","mid")
                $ cho_mad = 0
            "-I can't choose-":
                m  "You're both hot."
                call cho_main("I guess.","pout","suspicious","angry","downR")
            "-Nope, you lose-":
                m "I'm afraid, Miss Granger is simply... how shall I put it... sexier!"
                call cho_main("What?","scream","wide","angry","mid")
                m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
                call cho_main("But she doesn't even do work-outs, [cho_genie_name]!","angry","suspicious","angry","downR")
                $ cho_mad +=5

        jump jerk_off_to_cho



# Favour 1 - Second time event.
label cho_favor_1_2:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","suspicious","sad","down")
    m "I want to see your body!"
    call cho_main("You want me to get naked, sir?","open","base","sad","R")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","pout","wide","sad","mid",trans="hpunch")
    call cho_main("I'll do it.","horny","base","sad","R")
    $ cho_wear_top = False
    call cho_main("There! How is that?","horny","base","sad","R")

    menu:
        "-Be aggressive-":
            g9 "Nice!"
            m "Now the bottom."
            call cho_main("Yes, uhm... [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            call cho_main("(House points...loads of house points...)","horny","closed","sad","mid")
            $ cho_wear_bra = False
            call cho_main("(Am I really doing this?)","angry","base","sad","down")
            $ cho_wear_panties = False
            call cho_main("(Too late now...)","angry","closed","sad","mid")
            call ctc

            m "Very good."
            call cho_main("(...)","upset","closed","sad","mid")
            call cho_main("Uhm... is that enough?","annoyed","wink","sad","mid")

        "-Be nice-":
            m "Go on, girl."
            call cho_main("Yes, sir!","smile","base","sad","R")
            call nar("Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips.")
            $ cho_wear_bottom = False
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            call nar("Her hands nervously move to her bra.")
            call cho_main("Is this okay?","pout","base","sad","mid")
            $ cho_wear_bra = False
            call cho_main("What do you think?","horny","angry","sad","R")
            m "Simply gorgeous."
            call nar("Finally, she pushes her panties down.")
            $ cho_wear_panties = False
            call cho_main("...","upset","closed","sad","mid")
            g4 "Very nice."
            call cho_main("(...)","pout","base","sad","mid")
            call cho_main("Um...","base","base","sad","R")
            call cho_main("Can I put my clothes back on now?","open","suspicious","sad","down")

    jump jerk_off_to_cho



# Favour 1 - Third time event.
label cho_favor_1_3:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","angry","sad","mid")
    m "I want to see your body again."
    call cho_main("You want me to get naked, sir?","horny","suspicious","sad","down")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","scream","wide","sad","mid")
    call cho_main("I'll do it.","smile","base","base","R")
    call cho_main("Only...","open","angry","sad","mid")
    call cho_main("You're not going to...you know...again, are you sir?","horny","angry","sad","mid")
    m "And what would that be, girl?"
    "Cho shifts uncomfortably on her feet."
    call cho_main("Don't make me say it, Professor.","open","angry","sad","R")
    m "Say what, girl?"
    call cho_main("....masturbate.","horny","angry","sad","mid")
    m "What was that?"
    call cho_main("You're not going to jerk off again, are you?","open","base","angry","mid")

    label cho_wants_you_to_jerk_off:
    menu:
        "-Be Aggressive-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Get on with it, girl."
            call cho_main("Yes, [cho_genie_name]!","base","base","sad","R")
            $ cho_wear_top = False
            "Cho grits her teeth and removes her top in one swift motion."
            m "That's better. Now the bottoms."
            call cho_main("Yes, [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("(house points...loads of house points....)","smile","base","base","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very good."
            call cho_main("........","smile","base","base","mid")

        "-Be Nice-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Go on, girl."
            call cho_main("Yes, [cho_genie_name]!","smile","base","sad","R")
            $ cho_wear_top = False
            "Cho flashes a subdued smile and removes her top in one swift motion."
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("is this okay?","pout","base","sad","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            call cho_main("what do you think?","horny","angry","sad","R")
            m "Simply. gorgeous."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very nice."
            call cho_main("........","upset","closed","sad","mid")

        "-I hadn't planned on it-":
            m "I hadn't planned on it."
            call cho_main("Oh.","pout","base","sad","R")
            call cho_main("Okay then.","base","base","base","mid")
            jump cho_wants_you_to_jerk_off

    jump jerk_off_to_cho



### Jerking off to naked Cho ###
label jerk_off_to_cho:
    menu:
        "-Start jerking off-":
            hide screen cho_chang
            hide screen bld1
            with d3
            pause.2
            call gen_chibi("jerking_off_behind_desk")
            pause.8

            if cho_mad <= 0: #OK with it.
                if cho_whoring in [0]:
                    call cho_main("(!!!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], are you...","horny","suspicious","sad","R")
                    call nar(">Cho's voice is soft and slightly husky. She almost sounds...aroused.")
                    call cho_main("Touching yourself?","quiver","suspicious","angry","down")
                    call cho_main("[cho_genie_name], I didn't agree to this...","angry","suspicious","sad","down")
                elif cho_whoring in [1]:
                    call cho_main("[cho_genie_name]...","horny","suspicious","raised","mid")
                    call cho_main("You are touching yourself.","quiver","suspicious","raised","down")
                else:
                    call cho_main("I knew you would do that...","smile","angry","angry","mid")

                label keep_jerking_off_to_cho:
                menu:
                    "-Keep jerking off-":
                        if cho_whoring in [0]:
                            call nar(">Your eyes continue to drift over the young Quidditch players tight, athletic body.","start")
                            call nar(">You lean back in your chair and begin stroking in earnest.","end")
                        call cho_main("...","quiver","suspicious","raised","downR")
                        call nar(">The young seeker looks mesmerized by your actions.")
                        call cho_main("...","quiver","suspicious","base","down")
                        call nar(">Her eyes glued to your thick cock.")

                        if cho_whoring in [0]: #Not really ok with it.
                            call cho_main("I-I've never seen one before.","open","suspicious","sad","down")
                            call cho_main("Are they always so... BIG?","smile","suspicious","raised","down")
                            m "(Look at the body on that slut!)"
                            call cho_main("(...)","horny","suspicious","sad","downR")
                            call ctc

                            call cho_main("[cho_genie_name], how much longer are you going to-","horny","suspicious","sad","downR")
                            g4 "Here is comes!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cum_block
                            call cho_main("(...)","horny","wide","sad","L")
                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "I think that was it..."
                            call cho_main("Can I have my points now, [cho_genie_name]?","smile","base","base","R")
                            m "Sure..."

                            if cho_whoring <= 0:
                                $ cho_whoring = 1

                            jump end_cho_favor


                        if cho_whoring >= 1: #Very OK with it!
                            if cho_whoring in [1]:
                                call cho_main("It's so big...","horny","suspicious","raised","down")
                                call cho_main("Does it always get like this??","soft","base","raised","mid")
                            else:
                                call cho_main("Keep stroking your cock, [cho_genie_name].","open","angry","angry","down")

                            menu:
                                "-Tell her to shut up-":
                                    if cho_whoring <= 1:
                                        m "Quiet, girl! Don't ruin this for me."
                                        call cho_main("...","annoyed","angry","angry","mid")
                                        call cho_main("","base","closed","base","mid")
                                        call ctc
                                        g4 "(Is she flexing her muscles?!)"
                                    else:
                                        m "Shut up, [cho_name],... and start flexing those muscles!"
                                        call cho_main("Of course, [cho_genie_name].","horny","base","raised","downR")
                                        call ctc
                                    call nar(">You pump your cock faster and faster...")
                                    g4 "(Look at those fucking abs on that girl!)"
                                    call nar("Cho's athletic, young body has you hard as stone.")
                                    g4 "(I want to play xylophone on it...)"

                                "-Play along-":
                                    if cho_whoring <= 1:
                                        m  "Only when I'm around athletic students like you, Miss Chang."
                                        call cho_main("...","horny","base","raised","R")
                                        call cho_main("I'm glad to hear that, [cho_genie_name].","soft","base","base","mid")
                                        m "Such a nice body you have there..."
                                    else:
                                        m "I can't help it, [cho_name]."
                                        m "When I get to see young girls, with bodies like yours..."
                                        g4 "I always get hard!"
                                    if cho_whoring <= 1:
                                        call cho_main("[cho_genie_name], does Hermione let you grope her?","horny","wink","raised","mid")
                                        g9 "She does!"
                                        call cho_main("Maybe next time, [cho_genie_name], I'll give you something that feels a lot nicer than her disgusting tits!","soft","closed","raised","mid")
                                        call ctc
                                    else:
                                        call cho_main("Is my body that good?","quiver","suspicious","raised","mid")
                                        call ctc
                                        call cho_main("You're' dripping everywhere, professor","horny","suspicious","sad","downR")
                                        call cho_main("oh god...your balls looks so full. There's so much.","horny","base","raised","down")
                                        call nar("The perverse wonder in Cho's voice pushes you over the edge.")
                                    call cho_main("Wouldn't you just love to touch every muscle on my bod-","soft","base","raised","R")

                            g4 "Fuck, here it comes!!!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cho_main("[cho_genie_name]?!","soft","wide","raised","down")
                            call cum_block

                            if cho_whoring <= 1:
                                call cho_main("(Wow. He's cumming so much...)","horny","base","raised","downR")
                                call cho_main("(Just from looking at my body...)","base","base","base","down")
                            else:
                                call cho_main("(Look at all that cum!)","horny","wide","raised","down")
                                call cho_main("......","horny","base","base","downR")
                                call cho_main("(I wonder what it tastes like...)","quiver","suspicious","raised","L")

                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "Girl, that was amazing!"
                            call cho_main("...","horny","base","raised","mid")

                            if cho_whoring <= 1:
                                call cho_main("(I can't believe I agreed to that...)","horny","suspicious","sad","down")
                                call cho_main("Can I have my points now, [cho_genie_name]?","soft","base","base","mid")
                            else:
                                call cho_main("I'd like to get my points now, [cho_genie_name].","soft","base","base","mid")
                            m "Of course..."

                            if cho_whoring < 2:
                                $ cho_whoring += 1

                            jump end_cho_favor


            else: #Cho is mad! Not OK with it!!!
                if cho_whoring in [0]:
                    call cho_main("(Is he?!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], stop!","scream","closed","angry","mid")
                    call cho_main("I won't let you do that!","open","angry","angry","mid")
                    m "Do what? I'm just scratching my leg..."
                    call cho_main("Don't take me for a fool! I know exactly what you are doing!","angry","closed","angry","mid")
                    call cho_main("Stop!","open","closed","angry","mid",trans="hpunch")
                    call cho_main("Touching!","scream","angry","angry","mid",trans="hpunch")
                    call cho_main("Yourself!!!","angry","angry","angry","mid",trans="hpunch")
                    g4 "Jeeze..., no need to scream like that..."
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("sit_behind_desk")
                    pause.8
                    call bld
                    m "I will stop..."
                    m "scratching..."
                    m "my leg..."

                elif cho_whoring in [1]:
                    call cho_main("No,[cho_genie_name]! Stop doing that!","horny","wide","sad","L")
                    m "Doing what?"
                    call cho_main("Stop touching yourself!","horny","wide","sad","L")
                    m "Whatever... You ruined the mood anyway..."
                    call gen_chibi("sit_behind_desk")
                    m "Better?"

                else: #OK again!
                    call cho_main("[cho_genie_name]! You are touching yourself again!","horny","wide","sad","L")
                    m "What? Don't you like it?"
                    call cho_main("(...)","horny","wide","sad","L")
                    jump keep_jerking_off_to_cho

                call cho_main("Thank you, [cho_genie_name].","annoyed","angry","angry","R")
                call cho_main("Can I have my points now?","open","closed","raised","mid")
                m "Sure..."
                jump end_cho_favor

        "-Better not-":
            call nar(">You decide not to indulge your baser instincts.")
            m "Alright, Miss [cho_name]."

            if cho_whoring <= 0:
                $ cho_whoring = 1

            else:
                call cho_main("[cho_genie_name], are we done, already?","horny","base","sad","R")
                call cho_main("(I thought he would maybe...)","smile","base","base","R")
                m "Yes. We are done for today."
            jump end_cho_favor



label end_cho_favor:
    if not first_cho_favor_done:
        $ first_cho_favor_done = True

        m "[current_payout] points to Gryffindor!"
        $ gryffindor += current_payout
        call cho_main("[cho_genie_name], I'm from Ravenclaw!","open","wide","raised","mid")
        m "Right, what did I say?"
        $ gryffindor -= current_payout

    m "[current_payout] points to Ravenclaw!"
    $ ravenclaw += current_payout
    $ cho_mad -= 10

    call cho_main("Thank you.","soft","base","base","mid")

    call nar(">Cho quickly puts her clothes on before leaving.")
    call load_cho_clothing_saves
    if daytime:
        call cho_main("Good day, [cho_genie_name].","smile","base","base","mid")
    else:
        call cho_main("Good night, [cho_genie_name].","smile","base","base","mid")
    call play_sound("door")

    jump end_cho_event








### FAVOUR 2 - Cho's ass gets fondled! ###
label cho_favor_2:
    m "(Right, then I'll just fondle Cho's ass a little.)"
    menu:
        "-Touch her ass-":
            if chof2_first: #have to include new boolean chof2_first=False
                $ chof2_first = False
                g9 "Miss Chang, I'd like to touch your ass."
                call cho_main("My...ass?","smile","suspicious","sad","downR")
                m "Yes. I'd like to touch it."
                call cho_main("I knew you liked my ass.","horny","shocked","base","mid")
                call cho_main("{size=-4}(i knew he couldn't resist for long.){/size}","quiver","shocked","base","R")
                call cho_main("if you want to touch my firm ass, it's going to cost you.","scream","closed","base","mid")
                call cho_main("I'll do it for 40 house points.","open","base","base","R")
                m "That's a lot just to grab a students ass."
                ">Cho twists her petite, muscular body."
                ">You can see the firm lines of her ass under her uniform."
                call cho_main("come on, Professor... isn't it worth it?","smile","base","base","mid")
                m "That is a nice ass..."
                m "But I could get Hermione to do it for..."
                menu:
                    "-25 points-":
                        m "I could get Hermione to do it for only 25 points."
                        call cho_main("25?","scream","wide","angry","mid")
                        call cho_main("25? What cheap slag.","upset","shocked","angry","R")
                        call cho_main("I'll do it for 40.","open","base","angry","mid")
                        m "Alright, 40. But it better be worth it."
                        jump chofbm
                    "-35 points-":
                        m "I could get Hermione to do it for 35 points."
                        call cho_main("{size=-2}35? Really?....{/size}","pout","suspicious","angry","down")
                        call cho_main("{size=+2}If her fat ass is worth 35 then mine must be worth 40.{/size}","open","closed","angry","mid")
                        m "Fine."
                        jump chofbm
                    "-50 points-":
                        m "I could get Hermione to do it for 50 points."
                        call cho_main("50!","open","wide","angry","mid")
                        call cho_main("50! are you serious! No way.","smile","suspicious","angry","down")
                        call cho_main("but, she doesn't even work out...","pout","suspicious","sad","downR")
                        m "I suppose you're ass will do for now, but I'm only paying you 40 house points."
                        call cho_main("my ass will do?!","scream","suspicious","angry","down")
                        call cho_main("i'll show you whose ass is better!","smile","suspicious","angry","down")
                        $ cho_mad +5 #new variable cho_mad
                        jump chofbm
                    "-Nothing-":
                        m "I could get Hermione to do it for absolutely nothing."
                        call cho_main("Nothing?","open","wide","angry","mid")
                        call cho_main("what a little slut.","horny","suspicious","base","downR")
                        call cho_main("you'll still haVE to pay me, of course.","soft","closed","angry","mid")
                        call cho_main("40 house Points.","open","suspicious","angry","down")
                        m "Very Well, Miss Chang."
                        jump chofbm
            else:
                    m "Miss Chang. I'd like to touch your butt again."
                    if cho_whoring  == 1: #new variable cho_whoring
                        call cho_main("well...okay. but it'll cost you 40 house points","open","angry","sad","R")
                        m "Very well. Now come over here, girl."
                        jump chofbm
                    if cho_whoring  == 2:
                        call cho_main("alright, professor.","horny","base","sad","R")
                        call cho_main("40 house points, right?","soft","angry","base","mid")
                        m "Of course, Miss Chang."
                        jump chofbm
                    if cho_whoring  == 3:
                        call cho_main("You do?","horny","base","base","mid")
                        call cho_main("are you going to wank off?","quiver","suspicious","sad","down")
                        menu:
                            "Of course.":
                                m "Of course."
                                call cho_main("i guess I'd better take off my panties.","quiver","suspicious","sad","downR")
                            "No Way.":
                                m "Of course not. What do you take me for, a pervert?"
                                call cho_main("Well...","smile","suspicious","base","R")
                        jump chofbm

label chofbm:
#Cho chibi walks over to Dumbledore's desk and turns around.
    if cho_whoring  == 1:
        if not chof2_first:
            call cho_main("AlrighT...{w=2} you can touch me a little.","horny","base","sad","R")
            ">Cho is standing just inches in front of you, the firm globes of her ass-"
            stop music
            $ renpy.play('sounds/scratch.wav')
            call cho_main("Hey! Hogwarts, like most respectable institutions for magical learning, is located in the UK.","scream","closed","angry","mid")
            call cho_main("Please, stick to the metric system.","upset","closed","angry","mid")
            ">Ah, yes...well..."
            #play music fadein 1.5
        else:
            call cho_main("Alright...","horny","base","sad","R")
            call cho_main("Alright...you can touch me a little.","quiver","base","sad","R")
        ">Cho is standing mere centimeters in front of you, the firm globes of her ass barely visible under her skirt."
        ">Cho's hands remain firmly planted on the edge of your desk."
        ">You feel her quiver as the tips of your fingers touch her warm thighs."
        ">Cho's hands grip the desk firmly as your hands begin to slide up her legs."
        ">You reach her panties, and after feeling the contrast between flesh and soft fabric, you guide your palms over both cheeks."
        ">You give both a series of firm squeezes, appreciating the thick tight muscles underneath."
        call cho_main("prof-Professor...","horny","closed","sad","mid")
        ">You hear Cho stiffle a nervous cry. Her ass squeezes tight under your palms."
        call cho_main("That's enough, right Professor?","pout","base","sad","R")
        menu:
            "\"Yes\"":
                m "Yes. I think that did the trick."
                call cho_main("THank you, Professor.","smile","base","base","R")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "\"Absolutely not!\"":
                m "Absolutely not. I'm paying you 40 house points for this, girl."
                call cho_main("But, [cho_genie_name], I-","soft","wide","sad","mid")
                ">You give Cho's ass an aggressive squeeze."
                m "I'll tell you when it's enough."
                call cho_main("Fine.","pout","shocked","angry","R")
                $ cho_mad += 2
                ">Cho's ass feels smooth and warm under your touch. Nevertheless, you begin to savage the poor girls ass."
                call cho_main("Ow.","upset","shocked","angry","mid")
                call cho_main("Ow. ow. That hurts!","open","shocked","angry","mid")
                call cho_main("Professor!","scream","shocked","angry","mid")
                call cho_main("Professor! Professor, please stop.","open","shocked","angry","mid")
                menu:
                    "-Do as she asks-":
                        ">You come to your senses and let the poor girl's ass be."
                        ">Cho quickly pulls her skirt back down, rubbing her tender asscheeks."
                        call cho_main("Thank you, [cho_genie_name].","upset","closed","base","mid")
                        call cho_main("Can I have my house points now?","soft","angry","sad","mid")
                        m "Of course, Miss Chang. You've earned them."
                        m "40 points to Ravenclaw."
                        $ ravenclaw += 40
                        jump chof2end
                    "-Keep going-":
                        ">You ignore the foolish girl's cries and continue to abuse her ass, sliding your hands under her panties."
                        call cho_main("Stop!","scream","wide","angry","mid")
                        ">You grab Cho's ass tightly and squeeze with all your might."
                        ">The star Quidditch player falls forward over your desk."
                        call cho_main("It hurts!","scream","wide","sad","mid")
                        ">You roll your hands over her ass and begin to guide your thumbs to her tight, little, brown hole."
                        ">You can feel her starting to fight, as you squeeze tightly and pull her cheeks apart."
                        call cho_main("Professor Dumbledore!","scream","closed","angry","mid")
                        ">You suddenly release her ass and rain your firm hands across her cheeks."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("...","upset","closed","sad","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("ockk!","upset","suspicious","sad","downR")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("(it hurts so bad!)","smile","wide","sad","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        ">Cho's breathing is heavy and her legs shake under your assault."
                        ">A thick, red outline of your hand is bruising on her buttcheeks."
                        call cho_main("Ack!","scream","wide","sad","mid")
                        call cho_main("Ack!...","horny","wide","angry","mid")
                        call cho_main("Ack!...Professor!","scream","wide","angry","mid")
                        ">Cho finally gains enough control to wriggle free of your grasp, and quickly moves away."
                        #Cho chibi walks to the middle of the room.
                        call cho_main("That's too far!","scream","closed","angry","mid")
                        call cho_main("I never agreed to any of that.","scream","shocked","angry","mid")
                        call cho_main(".......i want 60 points.","scream","closed","angry","mid")
                        menu:
                            "-She earned 60-":
                                m "Very well. That was more than we agreed to. 60 points to Ravenclaw."
                                call cho_main("Thank you, sir.","upset","shocked","base","R")
                                $ cho_mad += 5
                                $ ravenclaw += 60
                                jump chof2end
                            "\"That was a bit much. 80 points\"":
                                m "I think I got a little carried away."
                                call cho_main("...","upset","suspicious","angry","downR")
                                m "80 points to Ravenclaw."
                                call cho_main("Really?","soft","suspicious","angry","down")
                                call cho_main("Well, I suppose it wasn't that bad...","pout","suspicious","sad","downR")
                                $ cho_mad +1
                                $ ravenclaw += 80
                                jump chof2end
                            "\"(How dare she!) 0 points!\"":
                                m "How dare you defy your headmaster, Rumbledwarf!"
                                m "If you don't come back here, you'll get nothing."
                                call cho_main("What!","scream","wide","sad","mid")
                                call cho_main("That's not fair!","scream","wide","angry","mid")
                                m "Well?"
                                call cho_main("Fine!","upset","suspicious","angry","down")
                                $ cho_mad +15
                                #Cho chibi returns to Dumbledore's desk.
                                ">Cho returns to your desk."
                                ">You catch a glimpse of her furious tears as she presents you her tender ass."
                                ">Wasting no time, you quickly tear the poor girls panties down and plant your hands on her firm flesh."
                                call cho_main("...","horny","wide","angry","R")
                                pause
                                ">Pulling her cheeks apart, you begin to rub your thumbs across the tight ring of her virgin asshole."
                                call cho_main("...","horny","suspicious","sad","downR")
                                call cho_main("......","quiver","suspicious","sad","down")
                                ">You can feel Cho's body tensing up."
                                ">You wet a finger with your saliva and begin to prod her asshole."
                                call cho_main(".........","horny","wide","sad","L")
                                m "Just relax."
                                ">Finally, you feel it give and your thick digit begins to slowly slide in."
                                call cho_main("Profes-....","quiver","suspicious","sad","downR")
                                ">Cho fights the urge to cry out. Letting you continue."
                                ">It's clear she wants her points more than anything."
                                m "{size=-2}(Don't you worry girl. You'll get your points.){/size}"
                                ">Once your finger is completely buried you begin to pull it back."
                                ">The muscle clings to your finger as it slides out."
                                call cho_main("...","horny","base","sad","R")
                                ">You can feel Cho tensing up again."
                                ">Your finger slides in and out of her tight asshole."
                                ">Cho falls forward onto the desk. Her breathing is getting faster, more ragged."
                                call cho_main("...","horny","closed","sad","mid")
                                ">Suddenly, you feel her muscular ring pulse, squeezing your finger with unbearable tightness."
                                call cho_main("Professor!","quiver","wide","sad","L")
                                ">Cho cums hard on your finger, before completely collapsing."
                                m "40 points to Ravenclaw."
                                call cho_main("{size=-2}.....yay.{/size}","horny","suspicious","sad","down")
                                $ ravenclaw += 40
                                jump chof2end
    if cho_whoring  == 2:
        call cho_main("...","smile","base","base","mid")
        call cho_main("......","smile","base","base","mid")
        call cho_main("......Aren't you going to touch me?","smile","base","base","mid")
        ">Cho pulls up the bottom of her skirt, revealing her ass, then bends forward over your desk."
        call cho_main("Well?","smile","base","base","mid")
        ">Cho wiggles her ass at you."
        m "By the sands...."
        ">Your hands fly toward Cho's tight cheeks and grip them firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Prof-Professor..."
        ">You hear Cho stiffle a cry. Her ass squeezes tight under your palms."
        call cho_main("That's not enougH, is it, Professor?","smile","base","base","mid")
        menu:
            "No, that's quite enough.":
                m "No, no. That's quite enough. Thank you, Miss Chang."
                call cho_main("....uh. Yes. Thank you, Professor.","smile","base","base","mid")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "Not Enough.":
                m "You're right. After all, I'm paying you 40 house points for this, girl."
                call cho_main("Yes, sir. But...","smile","base","base","mid")
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">She hooks her thumbs in the waist of her panties and pulls them outward."
                cho_sexy "Well, sir. I suppose for 60 points I could take these ANNOYING panties off."
                call cho_main("And let you feel me, sir...","smile","base","base","mid")
                menu:
                    "60 it is.":
                        m "Well then, 60 it is."
                        $ ravenclaw += 60
                        call cho_main("{size=-4}(Wow, that was easy.){/size}","smile","base","base","mid")
                        call cho_main("{size=-4}(I bet his nasty, old cock is going crazy...){/size}","smile","base","base","mid")
                        ">Cho slowly pushes her panties down past her hips, until they finally fall to her feet."
                        ">She steps out of them and spreads her feet wide before putting her hands on your desk."
                        ">The young Quidditch star arches her back, thrusting her firm ass toward you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        jump chof2wl2
                    "50 seems more fair.":
                        m "I think 50 points seems more fair. Don't you?"
                        call cho_main("50?","smile","base","base","mid")
                        ">Cho begins to wiggle her panties around her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...","smile","base","base","mid")
                        menu:
                            "50 points.":
                                m "50 points."
                                call cho_main("Well, okay.","smile","base","base","mid")
                                call cho_main("{size=-4}(60 points was high anyway.){/size}","smile","base","base","mid")
                                $ ravenclaw += 50
                                ">Cho pushes her panties down and puts her hands on your desk."
                                jump chof2wl2
                            "Fine. 55 points.":
                                m "Very well, Miss Chang. I'll give you 55 points."
                                call cho_main("hm. 55 points seems fair.","smile","base","base","mid")
                                $ ravenclaw += 55
                                ">Cho moves her ass seductively, releasing her panties and placing her hands flat on your desk."
                                call cho_main("but, Professor...","smile","base","base","mid")
                                m "Yes?"
                                cho_sexy "I don't think I can reach. Will you help me?"
                                m "Of course, Miss Chang. It's important for the headmaster to take a hands on approach."
                                ">You lean forward and slowly slide Cho's panties down, revealing the girls perfect ass."
                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                jump chof2wl2
                            "No.":
                                ">You give Cho's ass an aggressive squeeze."
                                m "No. I don't think so."
                                call cho_main("What?","smile","base","base","mid")
                                call cho_main("well...i guess I could do it for 50.","smile","base","base","mid")
                                menu:
                                    "Yes.":
                                        m "Very well. 50 house points. You drive a hard bargain, Miss Chong."
                                        call cho_main("MY name Is Chang. And yes, I do.","smile","base","base","mid")
                                        $ ravenclaw += 50
                                        $ cho_mad +1
                                        ">Cho quickly pushes her panties off her hips, letting them fall to the ground before bending over your desk."
                                        jump chof2wl2
                                    "No.":
                                        m "No."
                                        call cho_main("Oh, okay.","smile","base","base","mid")
                                        ">Cho lets her panties snap back into place. Nevertheless, you begin to gently squeeze the girls firm ass."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("......","smile","base","base","mid")
                                        call cho_main(".........","smile","base","base","mid")
                                        call cho_main("is that enough, sir?","smile","base","base","mid")
                                        menu:
                                            "Yes. That's enough.":
                                                ">You nod."
                                                m "Yes. That was fine, Miss Chang."
                                                ">Cho quickly pulls her skirt back down, smoothing her panties."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                m "40 points to Ravenclaw."
                                                $ ravenclaw += 40
                                                jump chof2end
                                            "Keep going.":
                                                ">You ignore the girl's question and continue to molest her ass, sliding your hands under her panties."
                                                call cho_main("I knew you couldn't resist.","smile","base","base","mid")
                                                ">You grab Cho's bare ass tightly and give it a quick squeeze."
                                                m "40 points to Ravenclaw."
                                                call cho_main("THank you, Professor.","smile","base","base","mid")
                                                $ ravenclaw += 40
                                                jump chof2end

        label chof2wl2:
        ">You stare at Cho's tight, young ass, drinking it in."
        ">It looks like all of her Squidstitching has paid off."
        ">The asian girls ass looks incredible."
        cho_seductive "Well?"
        ">You grab Cho's firm ass in booth hands and squeeze tightly."
        ">Your thick cock strains against your robes."
        menu:
            "-Jerk off-":
                ">You stare at the girl's ass, mezmerized."
                ">You continue to molest her firm ass with one hand, while the other pulls your cock out of your wizard robes."
                call cho_main("what are you doing?","smile","base","base","mid")
                ">You begin to pump your cock, squeezing her ass."
                cho_seductive "A-alright, but I want an extra five... {w=.5} no TEN points."
                menu:
                    "Fine.":
                        ">You give your throbbing cock three quick pumps before nodding."
                        m "Fine. You'll get your points, girl."
                        call cho_main("okay, professor. but you'd better stop before...you know.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side."
                        ">You give it a light smack as it comes back, stroking your cock."
                        cho_sexy_surprise "..."
                        ">Cho bounces her ass up and down a few times. You slap it hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=-4}(It hurts...but it also feels good.){/size}","smile","base","base","mid")
                        call cho_main("Professor Dumbl-{nw}","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=-4}(OH blimey. that's starting to feel really good.){/size}","smile","base","base","mid")
                        ">Every slap brings your cock closer, until you feel a familiar pressure in your magic balls."
                        menu:
                            "-Cum-":
                                ">Finally, it's too much for you, and with one final smack-"
                                $ renpy.play('sounds/slap_02.mp3')
                                show screen white
                                "{size=+4}SLAP!{/size}"
                                #Shake the screen
                                hide screen white
                                ">Finally, it's too much for you, and with one final smack, your cock erupts all over Cho's ass."
                                m "Arg, you fucking slut!"
                                #Genie cums. - I'd need to know which screen to put here
                                cho_wideEyes "What is {size=+2}that?{/size}"
                                cho_wideEyesLookingBack "{size=+4}Are you cumming?{/size}"
                                ">Your cum splatters across the young girl's ass in thick, messy spurts."
                                call cho_main("Oh, my God...","smile","base","base","mid")
                                ">Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                call cho_main("You {size=+2}completely{/size} covered me in your {size=+2}nasty{/size} {size=+3}old{/size} {size=+4}wizard cum!{/size}","smile","base","base","mid")
                                call cho_main("i'm a complete mess, you jerk!","smile","base","base","mid")
                                call cho_main("You owe me an extra 10 points!","smile","base","base","mid")
                                $ cho_mad +=1
                                menu:
                                    "Yes.":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!","smile","base","base","mid")
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.","smile","base","base","mid")
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault you made me cum."
                                        call cho_main("!!","smile","base","base","mid")
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!","smile","base","base","mid")
                                        call cho_main("your smelly cum is all oveR my ass! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mad +5
                                        jump chof2end
                            "Better not.":
                                ">You stop at the last moment and put your cock away."
                                ">Your swollen balls throb with pressure."
                                call cho_main("are you okay?","smile","base","base","mid")
                                m "I'm a wizard, girl."
                                jump chof2end
                    "I'll give you 15.":
                        ">You give your throbbing cock a few quick pumps before rubbing the head across her ass cheek."
                        m "I'll give you 15."
                        call cho_main("15?...okay, Professor.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side, lightly dragging her ass across the tip of your cock."
                        ">You give you cock a quick stroke before guiding it back against Cho's ass."
                        cho_sexy_surprise "What are doing back there..."
                        ">Cho bounces her ass up and down a few times. You slap your cock head against it."
                        call cho_main("{size=-4}(Oh my god...i can't believe i'm letting an old man rub his cock on my ass.){/size}","smile","base","base","mid")
                        call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.5}{nw}","smile","base","base","mid")
                        ">You give your cock several good pumps and bring your free hand down across Cho's firm ass."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!","smile","base","base","mid")
                        call cho_main("(Oh blimey!)","smile","base","base","mid")
                        ">Then you rub your tip across her warm, naked ass flesh, dragging a trail of precum."
                        call cho_main("Professor...","smile","base","base","mid")
                        ">You slap your bulging cock against her ass again and bury the head between her cheeks."
                        ">You pump your cock like a madman, until you feel a familar pressure in your magic balls."
                        menu:
                            "Cum.":
                                ">Finally, it's too much for you, and with one final pump, your cock erupts between Cho's ass cheeks."
                                m "By Grabthar's Hammer!"
                                #Genie cums. - Find chibi
                                cho_wideEyes "Oh my God...What is that?"
                                cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                                ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                                call cho_main("Oh, my God...","smile","base","base","mid")
                                ">You pump your cock a few more times and dump the last of your cum in a fat, messy glob right against her asshole."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("my ass feels so gross!","smile","base","base","mid")
                                call cho_main("it's sO sticky. You owe me an extra 10 points!","smile","base","base","mid")
                                menu:
                                    "Why not?":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!","smile","base","base","mid")
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.","smile","base","base","mid")
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault your ass made me cum."
                                        call cho_main("!!!","smile","base","base","mid")
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!","smile","base","base","mid")
                                        call cho_main("your smelly cum is all iN my ass! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mad +5
                                        jump chof2end
                            "Warn Her.":
                                m "I'm almost there!"
                                call cho_main("Really?","smile","base","base","mid")
                                ">Suddenly, you feel Cho push back against you."
                                ">Your cock is wrapped tightly within her warm, muscular ass cheecks."
                                cho_sexy "Cum, Professor!"
                                ">Cho's ass rubs up and down, her ass tightly gripping your cock."
                                ">Finally, it's too much for you and with a grunt you bury your cock between her cheeks and cum violently."
                                m "Support Aka-{nw}"
                                cho_sexy "Shut up and cum, you dirty old man!"
                                m "Support Aka-gaaahhhh! You whore!"
                                #Genie cums. - find chibi
                                ">Spurt after nasty spurt of your cum shoots between the young girls ass, bubbling out over the top of her cheeks."
                                call cho_main("my ass feels so dirty!","smile","base","base","mid")
                                ">Completely spent, your fall back in your chair."
                                m "Well done girl."
                                call cho_main("thank you professor.","smile","base","base","mid")
                                ">Cho slips her panties back on, pulling them up over her cum filled crack."
                                ">Then she lightly pats her sticky ass."
                                call cho_main("Can't make a mess in the Hall, can I?","smile","base","base","mid")
                                jump chof2end
    if cho_whoring  ==3:
        ">Cho pulls up the bottom of her skirt, revealing her bare ass, then bends forward over your desk."
        call cho_main("Well?","smile","base","base","mid")
        ">Cho wiggles her naked ass at you."
        m "By the sands....you naughty girl."
        ">Your hands fly toward Cho's firm flesh and you grip her bare cheeks firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Dumbledore..."
        ">You hear Cho attempt to stiffle a moan. Her muscualar ass squeezes tight."
        call cho_main("You a want little more, don't you sir?","smile","base","base","mid")
        call cho_main("You...{w=1.5} you want to cum, don't you?","smile","base","base","mid")
        menu:
            "No, I want to preserve my essence.":
                m "No, Miss Chang. I'm on to you, you succubus!"
                call cho_main("....uh. What?","smile","base","base","mid")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                call cho_main("....thank you?","smile","base","base","mid")
                jump chof2end
            "Of course!":
                m "{size=-4}(I understand. You nasty little girl.){/size}"
                m "You'd better earn these 40 points girl."
                call cho_main("Yes, sir. But...","smile","base","base","mid")
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">Every so often you get a glimpse of her cute, little asshole."
                ">Cho leans forward, pulling her ass cheeks apart."
                call cho_main("Well, sir. i suppose for just 65 points I could","smile","base","base","mid")
                cho_sexy "Well, sir. I suppose for just 65 points I could put your big, strong cock between these."
                cho_sexy "And rub you up and down until you cum."
                menu: #[No.]
                    "65 it is.":
                        m "Well then, 65 it is."
                        call cho_main("{size=-4}(wow, that was easy.){/size}","smile","base","base","mid")
                        call cho_main("{size=-4}(I bet his nasty, old wizard balls are completely full of cum.){/size}","smile","base","base","mid")
                        ">Cho arches her back, thusting her firm ass toward you."
                        ">Then the young Quidditch star slowly backs into your cock, before wrapping her ass tightly around you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        jump chof2hd
                    "55 feels more right.":
                        m "I think 55 points is much more appropriate. Don't you?"
                        call cho_main("55?","smile","base","base","mid")
                        ">Cho begins to bounce and jiggle her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...","smile","base","base","mid")
                        cho_seductively "{size=-4}To cum...{/size}"
                        cho_seductively "{size=-2}To cum right...{/size}"
                        cho_seductively "{size=-1}To cum right{/size}...{w} here."
                        menu:
                            "55 points.":
                                m "55 points."
                                call cho_main("Well, okay.","smile","base","base","mid")
                                call cho_main("{size=-4}(60 points was high anyway.){/size}","smile","base","base","mid")
                                ">Cho pushes her ass back against you."
                                jump chof2hd
                            "Fine. 60 points.":
                                m "Very well, Miss Chang. I'll give you 60 points."
                                call cho_main("hm. 60 points isn't too bad.","smile","base","base","mid")
                                ">Cho moves her ass seductively, pulling her cheeks open wide before settling back against your cock."
                                call cho_main("Professor Dumbledore...","smile","base","base","mid")
                                m "Yes?"
                                call cho_main("your cock feels so...","smile","base","base","mid")
                                cho_sexy "So thick."
                                ">You lean forward and slowly slide your cock up and down Cho's valley."
                                call cho_main("Mmm. Thank you, sir.","smile","base","base","mid")
                                jump chof2hd
                    "No.":
                        ">You slap your stone hard cock against Cho's ass aggressively."
                        m "No. I don't think so."
                        call cho_main("What?","smile","base","base","mid")
                        call cho_main("well...i guess I could do it for 50.","smile","base","base","mid")
                        menu:
                            "Yes":
                                m "Very well. 50 house points. You drive a hard bargin, Miss Chong."
                                call cho_main("MY name Is Chang. And yes, I do.","smile","base","base","mid")
                                $ ravenclaw += 50
                                $ cho_mad +1
                                ">Cho quickly pushes her ass against you."
                                jump chof2hd
                            "No.":
                                m "No."
                                call cho_main("Oh, okay.","smile","base","base","mid")
                                ">Cho releases her cheeks, letting her ass clap together."
                                ">She bends over your desk and you begin to gently squeeze the girls firm, naked ass."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("......","smile","base","base","mid")
                                call cho_main(".........","smile","base","base","mid")
                                call cho_main("is that enough, sir?","smile","base","base","mid")
                                menu:
                                    "Yes. That's enough.":
                                        ">You nod."
                                        m "Yes. That was fine, Miss Chang."
                                        ">Cho quickly pulls her skirt back down, smoothing the fabric over her ass."
                                        call cho_main("Thank you, sir.","smile","base","base","mid")
                                        m "40 points to Ravenclaw."
                                        $ ravenclaw += 40
                                        jump chof2end
                                    "Keep going.":
                                        ">You ignore the girl's question and continue to molest her ass, sliding your hands deep between her ass cheeks."
                                        call cho_main("I knew you couldn't resist.","smile","base","base","mid")
                                        ">You lean forward and give Cho's ass a quick bite before leaning back."
                                        m "40 points to Ravenclaw."
                                        call cho_main("Thank you, Professor.","smile","base","base","mid")
                                        $ ravenclaw += 40
                                        jump chof2end

        label chof2hd:
        ">You can feel Cho's warmth spreading out over your body from her ass."
        ">You give her firm cheeks a quick slap."
        $ renpy.play('sounds/slap_02.mp3')
        show screen white
        "{size=+4}SLAP!{/size}"
        #Shake the screen
        hide screen white
        cho_seductive "Professor!"
        ">You grab Cho's firm ass in booth hands and squeeze it tightly around your cock."
        ">Your thick cock strains and throbs."
        call cho_main("let me do all the work.","smile","base","base","mid")
        menu:
            "Fuck her ass cheeks.":
                ">You stare at the girl's ass, mezmerized."
                ">Finally, you stand up and push Cho down over your desk."
                call cho_main("sir, what are you doing?","smile","base","base","mid")
                ">You squeeze her cheeks tight and begin to pump your cock through the tunnel."
                cho_seductive "A-alright, you can do that, but I want an extra five points."
                menu: #[I'll give you 15] [No more points]
                    "Fine.":
                        ">You give the girl's ass several quick pumps before answering."
                        m "Very well, girl."
                        call cho_main("okay, Professor, but...but warn me before you cum.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side, causing your slimy cock to pop free."
                        ">You give Cho's ass a light smack, squeezing your cock with her cheeks."
                        cho_sexySurprise "..."
                        ">You thrust forward enjoying the sensation on your head, then slap Cho hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=+4}(Oh my god!){/size}","smile","base","base","mid")
                        ">You feel Cho's thighs tighten with her ass."
                        call cho_main("{size=+4}(why does it feel so good?){/size}","smile","base","base","mid")
                        cho_sexy "{size=+4}(My pussy is tingling with every thrust of his nasty, old cock...){/size}"
                        call cho_main("Professor Dumbl-{w=.5}{nw}","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{sizE=+4}(oh! Oh, blimey!){/size}","smile","base","base","mid")
                        ">You feel Cho shifting her weight, and then notice her hand squeezed tight between her legs."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        m "You're enjoying this aren't you?"
                        call cho_main("no! no, I'm not!","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        m "Liar!"
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        ">Suddenly, you feel Cho's body start to convulse and her legs begin to shake uncontrollably."
                        call cho_main("proF {w}prof-PRofessor! I'm.{w=.75}{nw}","smile","base","base","mid")
                        call cho_main("PRofeSsor! I'm-I'm.{w=.75}{nw}","smile","base","base","mid")
                        call cho_main("I'm{W=.5}-I'm CUMMING!","smile","base","base","mid")
                        ">Cho's orgasm pushes you over the edge and you feel a familar twitch your wizard balls."
                        menu:
                            "Cum on her cheeks.":
                                "Finally, it's too much for you, and with one final thrust, your cock erupts all over Cho's ass."
                                m "Take it, you whore!"
                                #Genie cums.
                                cho_stupid"..."
                                cho_stupid"......"
                                "Your cum splatters between the young girl's ass cheeks in thick, messy spurts."
                                cho_stupid"........."
                                "Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                m "(Points) to Ravenclaw."
                                cho_stupid"........yessh."
                            "Cum in her ass.":
                                ">As you thrust forward you feel your head rub against the girls tight ring."
                                ">At the very brink you pull her cheeks open and press your cockhead against the tight entrance."
                                cho_stupid "...ahhh"
                                ">You push forward, fighting against the muscles."
                                cho_stupid "...ahhh....Ohhhh"
                                ">Finally, the ring gives way and your cock *pops* into her ass."
                                cho_stupid "...ahhh....ohhhh...Oomph!"
                                ">The pressure is too much and your cock explodes, dumping your cum safely in Cho's asshole."
                                #Genie cums - find sprite
                                m "Arg! You fucking cum dumpster!"
                                ">Load after load pumps into the girls tight, little hole until you feel her stomach bloat under you."
                                cho_stupid "Gack!"
                                cho_stupid "ooomph!"
                                $ renpy.play('sounds/pop02.mp3')
                                "Your cock pops out of the poor girls ass and you fall back in your chair, exhausted."
                                show screen blktone
                                #Cho chibi is standing in the middle of the room.
                                call cho_main("i don't feel So good...what happened?","smile","base","base","mid")
                                menu:
                                    "I filled your ass with cum.":
                                        m "You came so hard you passed out and I filled your ass with cum."
                                        cho _Shocked "..."
                                        cho _Shocked "......"
                                        cho _Shocked "........."
                                        cho_mouthfull "...."
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i need to go!","smile","base","base","mid")
                                        jump chof2end
                                    "I don't know. That was weird.":
                                        m "I don't know. That was weird."
                                        m "But you got your points."
                                        call cho_main("THank you, Prof...","smile","base","base","mid")
                                        cho_mouthfull "Prof-"
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i think i need To go seE moaning Myrtel!","smile","base","base","mid")
                                        $ renpy.play('sounds/run.mp3')
                                        jump chof2end
            "Let her.":
                m "As you wish, Miss Chang."
                ">You sit back in your chair and let Cho settle down against your lap."
                call cho_main("does this feel good?","smile","base","base","mid")
                ">Cho slowly drags her ass up and down over your cock."
                m "Fantastic, girl."
                ">Cho squeezes her ass around your dripping cock."
                ">The athletic, young Quidditch star arches her back and bounces her ass up a down, teasing the tip of your cock."
                m "You tease!"
                ">You suddenly bring your palm down across her meaty cheek."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}SLAP!{/size}"
                #Shake the screen
                hide screen white
                cho_sexySurprise "Professor!"
                ">Cho bounces her ass up and down a few more times, before  settling down on your lap."
                call cho_main("{size=-4}(Oh my god...i can't believe i'm rubbing my ass over an old wizard's cock.){/size}","smile","base","base","mid")
                call cho_main("{size=-4}(My ass is so slimy...the smell is so thick...){/size}","smile","base","base","mid")
                call cho_main("Professor Dumbledore, m-make sure you tell me before you-","smile","base","base","mid")
                ">You can already feel the beginning of your orgasm."
                ">You give the girls tight ass several slaps..."
                call slap_her

                call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.75}{nw}","smile","base","base","mid")
                call slap_her

                call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!","smile","base","base","mid")
                call cho_main("{size=+4}(Oh blimey!){/size}","smile","base","base","mid")
                ">Cho slides back against your lap and begins to grind against you as you pump your cock between her cheeks."
                cho_arounsed "Professor..."
                ">You can see the top of your cock popping in and out of her ass cleavage, leaving a puddle of slime in the valley."
                ">After several more pumps you feel a familar pressure building..."
                menu:
                    "Cum.":
                        ">Finally, it's too much for you, and with one final thrust, your cock erupts between Cho's ass cheeks."
                        m "Cor' blimey, you bloody wanker!"
                        #Genie cums. - find chibi
                        cho_wideEyes "Oh my God...What is that?"
                        cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                        ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                        call cho_main("Oh, my God...","smile","base","base","mid")
                        ">You pump your cock a few more times and dump the last of your cum at the top of her ass."
                        call cho_main("...","smile","base","base","mid")
                        call cho_main("my ass feels so gross!","smile","base","base","mid")
                        call cho_main("it's so sticky.","smile","base","base","mid")
                        cho_sexy "It's so sticky. You owe me an extra 10 points!"
                        menu:
                            "Yes.":
                                m "Yeah, sure. 10 more points to Ravenclaw."
                                $ ravenclaw += 10
                                call cho_main("look at this mess!","smile","base","base","mid")
                                call cho_main("I'll never get this cleaned up...","smile","base","base","mid")
                                call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                ">Cho stands up. Cum dripping down her firm ass, running in long, slimy rivulets down her thighs."
                                call cho_main("{size=-4}(He came so much...){/size}","smile","base","base","mid")
                                cho_happy "{size=-4}(I bet Hermione never makes him cum like this.){/size}"
                                ">Cho pulls her skirt back over her sticky ass and smoothes the fabric. Dark stains appear as the cum soaks through."
                                call cho_main("this should be okay.","smile","base","base","mid")
                                m "Yes, of course. Though, just to be safe you'd better try to avoid the prefects..."
                                jump chof2end
                            "Too bad.":
                                m "You're the one who made me cum."
                                call cho_main("!!!","smile","base","base","mid")
                                m "You should be more careful."
                                call cho_main("you can't be serious!","smile","base","base","mid")
                                call cho_main("your smelly cum is all over my arse! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                m "Too bad."
                                call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                "Cho pulls her skirt down and storms off, leaving a trail of cum dripping to your door."
                                $ cho_mad +5
                                jump chof2end
                    "Warn Her.":
                        m "I'm going to cum!"
                        call cho_main("Really?","smile","base","base","mid")
                        ">Suddenly, you feel Cho move forward, and her hands quickly pull your cock down between her thighs before pushing back against you."
                        ">Your cock is wrapped tightly within her warm, muscular thighs, pressed tightly against her virgin pussy."
                        ">Cho rocks her hips back and forth, thrusting you through her slippery thighs."
                        cho_sexy "Cum, Professor!"
                        ">You can feel the heat and juice dripping from Cho's pussy, clinging to your cock."
                        ">Finally, it's too much for you and with a grunt you grab the girl's hips and cum violently."
                        m "Arg, you whor-{w=.75}{nw}"
                        cho_sexy "Shut up and cum, you nasty, old wizard!"
                        m "Arg, you whor-errrrrr!"
                        #Genie cums. - find chibi
                        ">Spurt after nasty spurt of your cum shoots between the young girls thight thighs, drenching your desk."
                        cho_sexy "So much cum!"
                        ">Completely spent, your fall back in your chair."
                        m "Good job Ms Chang."
                        call cho_main("thank you professor.","smile","base","base","mid")
                        ">Cho carefully straightens her skirt."
                        ">Then she leans back over your desk and runs her finger through your warm, dripping cum."
                        call cho_main("i think you made a bit of a mess...","smile","base","base","mid")
                        ">Then, bringing the slimy mess to her soft lips she sucks her finger clean."
                        call cho_main("Oops...","smile","base","base","mid")
                        jump chof2end

    label chof2end:
    #cho walking out
    call play_sound("door")
    hide screen cho_chang
    with d3
    jump day_main_menu



label cho_favor_3:

        m "Miss Chang, do you know what a blowjob is?"
        call cho_main("?","smile","base","base","mid")
        call cho_main("you want me to put my mouth on your...","smile","base","base","mid")
        call cho_main("you want me to put my mouth on your...penis?","smile","base","base","mid")
        m "I just thought you'd like the chance to keep up with Miss Granger."
        call cho_main("you don't mean she's been-","smile","base","base","mid")
        menu:
            "-Absolutely-":
                m "I suppose Miss Granger is just more competitive than you."
                call cho_main("...","smile","base","base","mid")
                call cho_main("(i can't believe it.)","smile","base","base","mid")
                call cho_main("(What a...)","smile","base","base","mid")
                call cho_main("(what a...stupid whore.)","smile","base","base","mid")
                call cho_main("i can do it too!","smile","base","base","mid")
                call cho_main("i'll only charge you 60 points.","smile","base","base","mid")
                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?","smile","base","base","mid")
                        call cho_main("Really? 70 points?","smile","base","base","mid")
                        call cho_main("Okay.","smile","base","base","mid")
                        $ cho_mad -= 1
                        $ current_payout = 70
                        jump cho_favor_3_1

                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.","smile","base","base","mid")
                        $ current_payout = 60
                        jump cho_favor_3_1

                    "-Mrs. Granger only charges 55...-":
                        m "Ms. Granger only charges 55..."
                        call cho_main("55?...","smile","base","base","mid")
                        call cho_main("55?...why would she-","smile","base","base","mid")
                        call cho_main("I'll do it for 50!","smile","base","base","mid")
                        $ current_payout = 50
                        jump cho_favor_3_1

            "-Of course not-":
                m "Don't be crazy. Of course, not."
                m "Ms. Granger has standards."
                call cho_main("...","smile","base","base","mid")
                m "She's just been earning a lot of points lately."
                call cho_main("She is?","smile","base","base","mid")
                m "Well, she is the school's top student..."
                call cho_main("I'll do it for 60 points.","smile","base","base","mid")

                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?","smile","base","base","mid")
                        call cho_main("Really? 70 points?","smile","base","base","mid")
                        call cho_main("Okay.","smile","base","base","mid")
                        $ cho_mad -= 1
                        $ current_payout = 70
                        jump cho_favor_3_1

                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.","smile","base","base","mid")
                        $ current_payout = 60
                        jump cho_favor_3_1

                    "-You'll get 40-":
                        m "I'll give you 40 points."
                        call cho_main("40! I get more than that for...well, the other things you make me do.","smile","base","base","mid")
                        call cho_main("I'll do it for 50.","smile","base","base","mid")

                        menu:
                            "-Okay-":
                                m "Deal."
                                $ current_payout = 50
                                jump cho_favor_3_1

                            "-No way-":
                                m "No way, girl. You're not worth more than 40."
                                call cho_main("Fine!","smile","base","base","mid")
                                $ cho_mad += 10
                                m "And try not to look so miserable about it."
                                $ cho_mad += 10
                                call cho_main("(Asshole.)","smile","base","base","mid")
                                call cho_main("(how am i even supposed to do this?)","smile","base","base","mid")
                                $ current_payout = 40
                                jump cho_favor_3_1

        m "I assume you're familar with the ancient Chinese art of 'SukiSuki'."
        call cho_main("What?","smile","base","base","mid")
        m "I want a blowjob."
        if cho_mad >= 6:
            jump cho_mad_blowjob
        call cho_main("Okay. but i'm only doing this to help my House.","smile","base","base","mid")
        call cho_main("And i want [current_payout] points.","smile","base","base","mid")
        m "Yes, yes. Now get sucking."
        jump cho_favor_3_1

label cho_favor_3_1:

    call cho_main("Um...","smile","base","base","mid")
    call cho_main("um...What do I...","smile","base","base","mid")

    menu:
        "-Are you serious?-":
            m "Are you serious?"
            call cho_main("Of course I'm serious! I'm not a whore like Hermione.","smile","base","base","mid")
            m "You just suck my cock in your mouth like a lollipop."
            call cho_main("(Like candy? ew... No way, that's nasty. Old...worm tasting like candy...)","smile","base","base","mid")
            call cho_main("([current_payout]! [current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("hoh's hhisss hHohessor?(How's this professor?)","smile","base","base","mid")
            "You feel your cock twitch under your robes at the sight of your student crouched down on her knees like a whore."
            m "Yes...that will do nicely."
            "You pull your throbbing cock out of your wizard's robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your meaty wand."
            "Cho flinches as your cock bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "The head of your cock briefly touches the very tip of Cho's pointed nose, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide it into her mouth."
            call cho_main("(eww. it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!","smile","base","base","mid")
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*","smile","base","base","mid")
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!","smile","base","base","mid")
            call cho_main("Bleh!...","smile","base","base","mid")
            call cho_main("Oh my god!","smile","base","base","mid")
            call cho_main("I'm sorry, Professor!","smile","base","base","mid")

            menu:
                "-15 points-":
                    m "Fine! Just do it!"
                    call cho_main("Okay.","smile","base","base","mid")
                    "Cho leans forward and begins to quickly bob her head over your cock."
                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                    m "You fucking whore!"
                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!","smile","base","base","mid")
                    "Cho looks around for a place to spit it out."

                "-5 points-":
                    m "I'll give you 5 points."
                    call cho_main("...deal.","smile","base","base","mid")
                    "Cho leans forward and begins to quickly bob her head over your cock."
                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                    m "Yes, take it!"
                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!","smile","base","base","mid")
                    "Cho looks around for a place to spit it out."

                    menu:
                        "-Give her an empty wine glass-":
                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                            "You pass Ms. Chang the glass just as a little stream of cum dribbles over her lip."
                            call cho_main("Blehgff...","smile","base","base","mid")
                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                            "After a few moments it's completely full."
                            call cho_main("Thank you, sir.","smile","base","base","mid")
                            "#gain item [Cum Goblet]"
                            m "Yes...well, [current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Make her swallow it.-":
                            m "Hey, I'm paying extra so you'd better swallow it."
                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                            m "You want your points, don't you?"
                            call cho_main("(no way, you gross, old pervert!)","smile","base","base","mid")
                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                            $ renpy.play('sounds/gulp.mp3')
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("Blahg...","smile","base","base","mid")
                            call cho_main("Is...","smile","base","base","mid")
                            call cho_main("is...is that okay?","smile","base","base","mid")
                            m "Very good. [current_payout] to Ravenclaw."
                            call cho_main("Thank you, Profe-","smile","base","base","mid")
                            $ renpy.play('sounds/burp.mp3')
                            call cho_main("...","smile","base","base","mid")
                            jump end_cho_event
                "-Fuck you!-":
                    m "(What a bitch!)"
                    m "You greedy whore!"
                    "You grab your cock and quickly stroke it."
                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                    call cho_main("W-what?...","smile","base","base","mid")
                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                    call cho_main("But I can't go out like this!","smile","base","base","mid")
                    m "Get out."
                    call cho_main("...","smile","base","base","mid")
                    call cho_main("...Fine!","smile","base","base","mid")
                    $ cho_mad += 10
                    #Cho storms out.
                    m "Bitches..."
                    jump end_cho_event

        "-Put my cock in your mouth.-":
            m "You just have to put my cock in your mouth."
            call cho_main("I know that!","smile","base","base","mid")
            call cho_main("I know that! But after that...","smile","base","base","mid")
            m "Just suck on it and tease it with your tongue."
            call cho_main("(Tease it with my tongue? ew. that sounds gross...)","smile","base","base","mid")
            call cho_main("([current_payout]! [current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("'oo cahn puh i' In 'ow...(you can put it in now...)","smile","base","base","mid")
            "You feel your cock thicken under your robes."
            m "Don't mind if I do..."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "pre-cum oozes from the tip of your thick cock."
            "Cho flinches as your head bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "You slimy pre-cum touches the very tip of Cho's pointed nose, leaving a dangling line of slime stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide your cock into her mouth."
            call cho_main("(eww. it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!","smile","base","base","mid")
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*","smile","base","base","mid")
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!","smile","base","base","mid")
            call cho_main("Bleh!...","smile","base","base","mid")
            call cho_main("Oh my god!","smile","base","base","mid")
            call cho_main("I'm sorry, Professor!","smile","base","base","mid")

            menu:
                "-That's probably enough-":
                    m "Maybe, I went a little too far."
                    jump end_cho_event

                "-Keep going-":
                    m "You don't get your points if you didn't finish."
                    call cho_main("I'm sorry, Professor!","smile","base","base","mid")
                    m "That's quite all right, girl."
                    "You shove your cock back in her mouth, this time careful not to go too deep."
                    "Cho's tongue rolls around your cock with amateurish effort, getting in the way more than helping."
                    "To your surprise the thought of her inexperience brings you to the edge."

                    menu:
                        "-Cum-":
                            "#Genie cums in Cho's mouth."
                            call cho_main("Hmmmmm!","smile","base","base","mid")
                            m "By the profits of Disney..."
                            call cho_main("Hmmmm!...","smile","base","base","mid")
                            call cho_main("hmmmm!...Mmmmm!","smile","base","base","mid")
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!","smile","base","base","mid")
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...that was so nasty..)","smile","base","base","mid")
                            call cho_main("Gross! You owe me extra for that!","smile","base","base","mid")

                            menu:
                                "-Fine 5 extra points-":
                                    m "Very well, Ms. Chang. [current_payout] to Ravenclaw."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    $ current_payout += 5
                                    jump end_cho_event

                                "-What? Absolutely not.-":
                                    m "What? Absolutely not."
                                    call cho_main("That's not fair!","smile","base","base","mid")
                                    m "Take it or leave it, Ms. Chong."
                                    call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                    m "Do you want your points or not?"
                                    call cho_main("yes, please.","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event
                        "-Warn Her-":
                            m "I'm going to cum!"
                            call cho_main("Hm!","smile","base","base","mid")
                            call cho_main("hm!...Blehrg!","smile","base","base","mid")
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she crosses her arms."
                            call cho_main("i want 15 more points.","smile","base","base","mid")
                            m "What?!"
                            call cho_main("You only said I had to suck your cock. If you wanted to cum, I'd like another 15 points.","smile","base","base","mid")

                            menu:
                                "-15 points-":
                                    m "Fine! Just do it!"
                                    call cho_main("Okay.","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bob her head over your cock."
                                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                                    m "You fucking whore!"
                                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over, your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                "-5 points-":
                                    m "I'll give you 5 points."
                                    call cho_main("...deal.","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bobs her head over your cock."
                                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                                    m "Yes, take it!"
                                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass, left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            "#gain item [Cum Goblet]"
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("Is...","smile","base","base","mid")
                                            call cho_main("is...is that okay?","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-Fuck you!-":
                                    m "(What a bitch!)"
                                    m "You greedy whore!"
                                    "You grab your cock and quickly stroke it."
                                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                    call cho_main("W-what?...","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                                    call cho_main("But I can't go out like this!","smile","base","base","mid")
                                    m "Get out."
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Fine!","smile","base","base","mid")
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump end_cho_event
        "-Let's go slow-":
            m "Let's just go slow."
            call cho_main("Thank you, Professor Dumbledore.","smile","base","base","mid")
            call cho_main("Do i just...you know, suck on it?","smile","base","base","mid")
            m "Yes. Think of it like a lollipop."
            call cho_main("(Like a lollipop? That might be okay...)","smile","base","base","mid")
            call cho_main("(Just ignore the fact that that the wrinkly, old cock in my mouth belongs to a crusty, old wizard...)","smile","base","base","mid")
            call cho_main("([current_payout]! current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("I' I' 'ood 'o'esser?(is this good, professor?)","smile","base","base","mid")
            "You gently carress Cho's warm cheek with the back of your hand."
            call cho_main("(Wow...that was nice.)","smile","base","base","mid")
            $ cho_mad -= 1
            m "Yes, girl...that will do nicely."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your cock."
            "Cho's eyes flinch as your cock bobs above her face."
            "Her long Asian lashes blink fast as she fight the reflex to pull away."
            "A slimy stream of pre-cum drips down onto her face."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "The tip of your cock briefly touches Cho's tongue, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and slowly rub your cock across it."
            call cho_main("(it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's good."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's breath and the soft, slipperiness of her tongue."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Shhh. It's okay, girl."
            "You slowly slide your cock into the young girls mouth."
            call cho_main("Hmmmm....","smile","base","base","mid")
            "The sensations are incredible, and soon your head is wrapped in warm, slippery wetness."
            "You leave it there for a moment."
            call cho_main("(This isn't bad...)","smile","base","base","mid")
            "You pull your cock back, out of Cho's mouth."
            call cho_main("Mmm.","smile","base","base","mid")
            call cho_main("Mmm....","smile","base","base","mid")
            "Cho opens her mouth wide, letting spit drip from her tongue."

            menu:
                "-That's probably enough-":
                    m "That's probably enough for now."
                    m "[current_payout] to Ravenclaw."
                    jump end_cho_event

                "-Keep going-":
                    m "We're almost done, girl."
                    call cho_main("(this is definitely worth [current_payout]...)","smile","base","base","mid")
                    "You gently guide your cock back into her mouth, careful not to go too deep."
                    "Cho's tongue rolls around your cock with sweet effort, slipping around your head."
                    "To your surprise her tongue finds your hole, and the assault brings you to the edge."

                    menu:
                        "-Cum-":
                            #Genie cums in Cho's mouth.
                            call cho_main("Hmmmmm!","smile","base","base","mid")
                            m "G-good...girl..."
                            call cho_main("Hmmmm!...","smile","base","base","mid")
                            call cho_main("hmmmm!...Mmmmm!","smile","base","base","mid")
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!","smile","base","base","mid")
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...there was so much..)","smile","base","base","mid")
                            call cho_main("Gross!","smile","base","base","mid")
                            call cho_main("gross! warn me next time, okay?","smile","base","base","mid")
                            m "That was great. [current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Warn Her-":
                            m "I'm getting close!"
                            call cho_main("Hm?","smile","base","base","mid")
                            call cho_main("hm?...Blehrg!","smile","base","base","mid")
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she looks up at you with a smile."
                            call cho_main("if you give me 5 extRa points i'll eat it.","smile","base","base","mid")
                            m "You'll eat it?"
                            call cho_main("Well, yeah. I mean, it's gross, but I need the points...","smile","base","base","mid")

                            menu:
                                "-15 points-":
                                    m "I'll give you 15 points."
                                    call cho_main("what? Really?","smile","base","base","mid")
                                    call cho_main("Okay.","smile","base","base","mid")
                                    "Cho dives forward and guides your cock into her mouth."
                                    "Her tongue wraps around your bulbous head, and twists back and forth."
                                    call cho_main("(Mmm. It is like candy!)","smile","base","base","mid")
                                    m "By the power of GreySkull!"
                                    #Genie cums in Cho's mouth.
                                    "Your balls pull tight against your body and your cock begins to twitch."
                                    "Suddenly, you grab Cho's head and drive deeper between her soft lips, dumping your cum at the back of her mouth."
                                    "You feel her trying to swallow, but her cheeks start to bulge from the heavy load."
                                    "When it's over, your cock pops out of the smiling girl's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it all."
                                            call cho_main("fmMmhm mt?!(Swallow it all?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(I'm seriously going to throw up...)","smile","base","base","mid")
                                            call cho_main("Mm hhmm!","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("...","smile","base","base","mid")
                                            call cho_main("...All gone.","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-5 points-":
                                    m "Sure, I'll give you 5 points."
                                    call cho_main("You will?","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bob her head over your cock."
                                    "Her inexperienced mouth enthusiastically work your shaft."
                                    "Before long, you can feel the cum churning in your enchanted nut sack."
                                    m "It's magically delicious!"
                                    #Genie cums in Cho's mouth.
                                    Cho_WideEyes"!..."
                                    Cho_WideEyes"(What?)"
                                    "Cho's cheeks begin to bulge with the heavy load, causing her to forget your mad outburst."
                                    "When it's over, your cock slips out from between Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("Is...","smile","base","base","mid")
                                            call cho_main("is...is that okay?","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-Fuck you!-":
                                    m "(I didn't know Chong was a Jewish name?!)"
                                    m "You greedy whore!"
                                    "You grab your cock and pound it like Anne Frank."
                                    m "After a few fast pumps your cock explodes."
                                    #Genie cums.
                                    "After a few fast pumps your cock explodes, coating Cho in your non-kosher cum."
                                    call cho_main("W-what?...","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                                    call cho_main("but I can't go out like this!","smile","base","base","mid")
                                    m "Get out."
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Fine!","smile","base","base","mid")
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump end_cho_event

label cho_favor_3_2:

        m "Ms. Chang, I'd like you to give me another blowjob."
        if cho_mad > 10:
            jump cho_mad_blowjob

        call cho_main("[current_payout] points.","smile","base","base","mid")
        m "Of course."
        "Cho drops to her knees and waits patiently."
        call cho_main("whenever you're ready.","smile","base","base","mid")
        m "Open your mouth."
        "Cho obeys, opening her mouth and thusting her tongue out."
        call cho_main("On 'ea'y...(I'm ready...)","smile","base","base","mid")
        "Your cock throbs under your robes."
        m "This is why I got into teaching..."
        "You pull your throbbing cock out of your robes and stand over Cho."
        "Cho's mouth drips with with saliva."
        "You slap your cock against her tongue a few times before guiding it into her mouth."
        call cho_main("(What's he doing...)","smile","base","base","mid")
        m "Yessss....that's better."
        "You let your cock rest there for a moment. Basking in the warmth of Cho's mouth."
        call cho_main("Hmmm.","smile","base","base","mid")
        m "Hold on."
        "You slowly push your cock deeper into the young girls mouth."
        call cho_main("Hmmmm!","smile","base","base","mid")
        "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
        "Suddenly your cock bottoms out at the back of Cho's throat."
        call cho_main("*cough* *ack!*","smile","base","base","mid")
        "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
        call cho_main("Bleh!","smile","base","base","mid")
        call cho_main("Bleh!...","smile","base","base","mid")
        call cho_main("Oh my god!","smile","base","base","mid")
        call cho_main("I'm sorry, Professor!","smile","base","base","mid")
        menu:
                    "-Be Nice-":
                        m "That's perfectly alright, Ms. Chang."
                        m "We'll just consider this part of your education."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        "Cho gently wraps her mouth around your cock."
                        "Then, flattening her tongue, she guides your cock to the back of her mouth."
                        "You can feel the entrance to her throat tickle the tip of your head."
                        m "Very good. Now, just relax."
                        call cho_main("Mmhm.","smile","base","base","mid")
                        "Cho's tongue twitches under your cock as she tries her best to relax her throat."
                        m "Mmm. Good. Now, try to swallow."
                        call cho_main("*GuL* *Gul* *Glug*","smile","base","base","mid")
                        "Finally, you feel the head of your cock pop into her throat."
                        "The sensation of her tight flesh squeezing around your length is incredible."
                        call cho_main("...","smile","base","base","mid")
                        call cho_main("......","smile","base","base","mid")
                        call cho_main("..........","smile","base","base","mid")
                        call cho_main("*cough* *splutter* ack! i almost had it.","smile","base","base","mid")
                        call cho_main("Let me try again.","smile","base","base","mid")
                        "Cho takes you back into her mouth."
                        "There's a determined look in her eyes."
                        call cho_main("*Gul* *gulp* *Gluck*","smile","base","base","mid")
                        "Your cock pop's back into her throat."
                        "You can feel Cho struggling to hold herself down."
                        "Her throat is fighting around you, squeezing in violent pulses."
                        "The sensations are too much."

                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Gluuuuuuh!*","smile","base","base","mid")
                                m "Yessss..."
                                call cho_main("*Glurck!*...","smile","base","base","mid")
                                call cho_main("*GlUrck!*...*gluglugulgh...*","smile","base","base","mid")
                                "Cho struggles to swallow as your cum pumps down her throat, but she gags, vomiting your slimy cum."
                                call cho_main("Blehg!","smile","base","base","mid")
                                "A torrent of slime spews out of Cho's mouth and drips down her chin splattering her uniform."
                                call cho_main("(oh god...that was so nasty..)","smile","base","base","mid")
                                call cho_main("gross! My uniform! You owe me extra, you jerk!","smile","base","base","mid")

                                menu:

                                    "-Fine 5 extra points-":
                                        m "Fine, Ms. Chang. [current_payout] to Ravenclaw."
                                        call cho_main("Thank you, sir.","smile","base","base","mid")
                                        jump end_cho_event

                                    "-What? Absolutely not.-":
                                        m "Absolutely not."
                                        call cho_main("but! That's not fair!","smile","base","base","mid")
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                        Cho_Sad"It's not even a hard name..."
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw."
                                        jump end_cho_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!","smile","base","base","mid")
                                call cho_main("hm!...Blehrg!","smile","base","base","mid")
                                "Cho pulls back, dragging your slippery cock out of her throat."
                                "You catch your breath and wait patiently for her to finish you off."
                                "But instead she crosses her arms. and smirks cleverly."
                                call cho_main("15 points.","smile","base","base","mid")
                                m "What?!"
                                call cho_main("The original deal was just for a blowjob. if you want to cum, I want another 15 points.","smile","base","base","mid")

                                menu:

                                    "-15 points-":
                                        m "Whatever, girl! Just do it!"
                                        call cho_main("Okay.","smile","base","base","mid")
                                        "Cho leans forward and guides your cock back into her mouth."
                                        "Unexpectedly, she drives forward, roughly shoving your cock back down her throat."
                                        "The sudden stimulation coupled with her slutty expression drives you over the edge."
                                        m "Take it your plebeian whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches and your balls pull tight as you begin to dump your cum down Cho's throat."
                                        "The poor girl tries to swallow, but can't take it all. She pulls back collecting the rest in her mouth."
                                        "Her cheeks bulge with the heavy load."
                                        "When it's over your cock pops out from between the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it all."
                                                call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(Of course, I do.)","smile","base","base","mid")
                                                call cho_main("(just pretend it's pudding.)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                call cho_main("(salty, slimy pudding....)","smile","base","base","mid")
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Was...","smile","base","base","mid")
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Was...that what you wanted?","smile","base","base","mid")
                                                m "Yes. [current_payout] to Ravenclaw."
                                                call cho_main("THank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.","smile","base","base","mid")
                                        "Cho leans forward and begins to quickly bobs her head over your cock."
                                        "Her mouth fumbles quickly around your head."
                                        "Suddenly, she wraps her hands around your balls and tugs down gently."
                                        "The sensation is suprisingly pleasant."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out"

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Professor Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                                call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("Is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("THank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-Fuck you!-":
                                        m "(What a bitch!)"
                                        m "You greedy whore!"
                                        "You grab your cock and quickly stroke it."
                                        "After a few fast pumps your cock explodes."
                                        #Genie cums.
                                        "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                        call cho_main("W-what?...","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw. Now, get out of my office."
                                        call cho_main("but I can't go out like this!","smile","base","base","mid")
                                        m "Get out."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("...Fine!","smile","base","base","mid")
                                        $ cho_mad += 10
                                        #Cho storms out.
                                        m "Bitches..."
                                        jump end_cho_event


                        jump end_cho_event

                    "-Be mean-":
                        m "You talk too much."
                        call cho_main("I'm sor-MMPH","smile","base","base","mid")
                        "You shove your cock back in her mouth, enjoying the sputtering tightness."
                        m "That's quite all right, girl."
                        "Cho's tongue thrashes violently around your cock, getting in the way more than helping."
                        "You hold Cho's head and forcefully push your cock towards the back of her throat."
                        call cho_main("mmmph! Mmmm!","smile","base","base","mid")
                        "To your surprise the frantic writhing of her tongue feels incredible."
                        "Your cock finally pops into her tight oesophagus, and you hold it there, enjoying the warm tightness."
                        m "That's the spot..."
                        "You feel Cho pushing you back, but you're close to cumming."

                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Glllll!* *Glp!*","smile","base","base","mid")
                                m "By the profits of Disney..."
                                call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                                call cho_main("Hmmmm!","smile","base","base","mid")
                                "Cho's hands pull tight on your robes as she tries desperately to swallow your load, but your thick cum catches at the back of her throat"
                                call cho_main("Blehg!","smile","base","base","mid")
                                "Your cum spews out of Cho's mouth."
                                "The thick slime drips down her chin, soaking her uniform."
                                call cho_main("(oh god...he almost killed me...)","smile","base","base","mid")
                                call cho_main("You-you...asshole! You almost made Me drown! You better pay extra!","smile","base","base","mid")

                                menu:

                                    "-I was pretty rough. 10 extra points.-":
                                        m "Alright, Ms. Chang. [current_payout] to Ravenclaw."
                                        call cho_main("That's all? I want more next time.","smile","base","base","mid")
                                        jump end_cho_event

                                    "-What? Absolutely not.-":
                                        m "What? Absolutely not."
                                        call cho_main("But you almost killed me!","smile","base","base","mid")
                                        call cho_main("I couldn't breathe!","smile","base","base","mid")
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw."
                                        jump end_cho_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!","smile","base","base","mid")
                                call cho_main("Hm!...Blehrg!","smile","base","base","mid")
                                "Cho wrestles free of your grasp and spits your slippery cock out of her mouth."
                                "Your slimy cock slaps against her face, leaving a line of spit and cockslime across her nose."
                                call cho_main("i want 15 more points.","smile","base","base","mid")
                                m "What?!"
                                call cho_main("I only agreed to a blowjob. Cumming Is extra. I want another 15 points.","smile","base","base","mid")

                                menu:

                                    "-15 points-":
                                        m "It's a deal, now finish it!"
                                        call cho_main("Okay.","smile","base","base","mid")
                                        "Cho leans forward and gives your cock a few quick strokes before guiding the head into her mouth."
                                        "She continues to pump your cock while her tongue swirls around your head."
                                        "Soon, the constant stimulation drives you over the edge."
                                        m "You whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock pops out between the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                                call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("Thank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.","smile","base","base","mid")
                                        "Cho leans forward and begins to stroke your cock."
                                        "Then, pumping your cock with her fist, she leans forwards and plants a sloppy kiss on your head."
                                        "Her lips linger on your slit and she teases it with her tongue."
                                        "The intense stimulation finally pushes you over the edge."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's hand, and you begin to cum."
                                        "Cho purses her lips, letting your load fill her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock slips away from Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(Yes.)","smile","base","base","mid")
                                                call cho_main("(This is so gross...)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("Thank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-Fuck you!-":
                                        m "(Just who's in charge here?!)"
                                        m "You greedy bitch!"
                                        "You grab your cock and force it into Cho's mouth."
                                        call cho_main("Hmm!*Gluck!*","smile","base","base","mid")
                                        "You drive cruelly deep, bursting into her throat, and being to pump hard."
                                        call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                        "After a few fast pumps you feel your balls pull tight."
                                        m "You fucking whore!"
                                        "With a cruel smile, you pull your cock out of Cho's abused throat."
                                        #Genie cums.
                                        "Your cock explodes, coating the defiant girl in your smelly cum."
                                        call cho_main("...","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw. Now, get out of my office."
                                        call cho_main("......","smile","base","base","mid")
                                        m "Get out."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("...O-okay...","smile","base","base","mid")
                                        $ cho_mad += 10
                                        #Cho shuffles out.
                                        m "Bitches..."
                                        jump end_cho_event


label cho_favor_3_3:
    m "Suck my cock."

    if cho_mad > 10:
        jump cho_mad_blowjob

    call cho_main("Okay!","smile","base","base","mid")
    m "Don't you want some points or something?"
    call cho_main("What?","smile","base","base","mid")
    call cho_main("Oh, yeah.","smile","base","base","mid")
    call cho_main("That'll be [current_payout] points.","smile","base","base","mid")

    menu:

        "-Let's do this-":

            m "Get on your knees and open your mouth."
            "Cho slides down to her knees and opens her mouth, sticking out her tongue."
            "The sigh of your student on her knees with her young mouth open, her soft tongue drooling over her chin is enough to drive you wild."
            "Your cock strains against your robes, leaking pre-cum all over the inside."
            call cho_main("RIke 'ish?(Like this?)","smile","base","base","mid")
            m "Very good, Ms. Chang."
            call cho_main("Honk 'ou.(Thank you.)","smile","base","base","mid")
            "You pull your rigid cock out of your robes, letting it bob just centimetres from Cho's mouth."
            "You rock your hips back and forth, teasing her."
            call cho_main("...","smile","base","base","mid")
            call cho_main("......","smile","base","base","mid")
            call cho_main("......'ey! 'Ut it in!(hey! Put it in!)","smile","base","base","mid")
            m "Beg."
            call cho_main("What?","smile","base","base","mid")
            m "Beg me for it."
            call cho_main("OkAy. um... g-give it to me.","smile","base","base","mid")
            call cho_main("please. put your cock in my...mouth?","smile","base","base","mid")

            menu:

                "-You call that begging?-":
                    m "You call that begging?"
                    call cho_main("...","smile","base","base","mid")
                    m "Come on. You can do better than that."
                    call cho_main("please. let me suck your cock.","smile","base","base","mid")
                    "You lean forward, letting your slit touch her nose."
                    "Your pre-cum leaves a slimy strand tangling between you."
                    m "You can do better than that."
                    call cho_main("...","smile","base","base","mid")
                    call cho_main("......","smile","base","base","mid")
                    call cho_main(".........","smile","base","base","mid")
                    call cho_main("............please, fuck my mouth!","smile","base","base","mid")
                    call cho_main("treat my slutty little mouth like a pussy.","smile","base","base","mid")
                    call cho_main("please, please, please let me suck your perfect, old man cock!","smile","base","base","mid")
                    call cho_main("i'll lick your balls and slurp up every drop of your slimy stuff.","smile","base","base","mid")
                    call cho_main("please, let me be your little cock sucking whore.","smile","base","base","mid")
                    m "That was...good."
                    pass

                "-Very good.-":
                    m "Very good, girl."
                    call cho_main("Thank you.","smile","base","base","mid")
                    pass

            "You finally lean forward, letting Cho take your cock in her mouth."
            call cho_main("*chomp* *ommph* *Sluuurp*","smile","base","base","mid")
            "Cho begins to worship your throbbing flesh wand, bobbing her head savagely."
            "You can feel her uvula tickling your head as she pushes herself down your cock."
            call cho_main("*oomph* *Gluck*","smile","base","base","mid")
            "Your cock prods the back of her throat, and Cho's movements suddenly stop as she fights her gag reflex."
            call cho_main("*gack!* *Cough*","smile","base","base","mid")
            "A mouthful of slime and spit spills out around your cock."
            call cho_main("Oh my god...i almost had it that time.","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You slap your cock against her tongue a few times before guiding it back into her slippery fuck hole."
            call cho_main("(Cheeky old man...)","smile","base","base","mid")
            m "Practice makes perfect."
            "Cho sinks down, pushing your cock deeper into her mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "Cho ignores you. Pushing herself down. Your cock presses against her throat."
            call cho_main("hmmmm!*Gluck!*","smile","base","base","mid")
            "Suddenly, your cock pops into her throat."
            call cho_main("Mmmm!","smile","base","base","mid")
            "The sensations are incredible. Tightness squeezes all around your cock. It's almost too much."
            "Cho begins to bob quickly up and down, dragging your sensative head through her throat."
            call cho_main("*UgG* *Gug* *Gug!*","smile","base","base","mid")
            "The girl's efforts begin to pay off and you feel yourself getting close."

            menu:

                "-Cum-":
                    ##Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!","smile","base","base","mid")
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, smacking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.","smile","base","base","mid")
                    call cho_main("well, for A geezer, I mean.","smile","base","base","mid")
                    m "Thank you?"
                    call cho_main("i'll take my points now.","smile","base","base","mid")
                    m "..."
                    m "...Yes, of course. [current_payout] to Ravenclaw."
                    jump end_cho_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?","smile","base","base","mid")
                    call cho_main("hm!...Blehrg!","smile","base","base","mid")
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out of her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("do you want me to eat it?","smile","base","base","mid")
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("i'll swallow all of that tasty cum if you want.","smile","base","base","mid")
                    call cho_main("and i won't even charge extra...","smile","base","base","mid")

                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.","smile","base","base","mid")
                            "Cho leans forward and gives your cock a few quick strokes before sucking the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Soon the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....","smile","base","base","mid")
                            call cho_main("(Holy shit!)","smile","base","base","mid")
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lips."
                            "Cho looks up into your eyes, pleadingly."

                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                    "You pass Ms. Chang the glass just as she dribbles another little stream of cum over her lip."
                                    call cho_main("Blehgff...","smile","base","base","mid")
                                    "Your cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "After a few moments it's completely full."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)","smile","base","base","mid")
                                    call cho_main("(mmmm...it's so thick and slimy.)","smile","base","base","mid")
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...","smile","base","base","mid")
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Yummy.","smile","base","base","mid")
                                    m "You whore. [current_payout] to Ravenclaw."
                                    call cho_main("THank you, Profe-","smile","base","base","mid")
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...","smile","base","base","mid")
                                    jump end_cho_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?","smile","base","base","mid")
                            "Cho leans forward swallowing your cock."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to violently fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*","smile","base","base","mid")
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*","smile","base","base","mid")
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)","smile","base","base","mid")
                            "When it's over your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("THank you, Dumblesir...","smile","base","base","mid")
                            m "[current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?","smile","base","base","mid")
                                call cho_main("Okay.","smile","base","base","mid")
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*","smile","base","base","mid")
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke it."
                                call cho_main("Cum for me, Professor!","smile","base","base","mid")
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...","smile","base","base","mid")
                                call cho_main("Oh my god...","smile","base","base","mid")
                                call cho_main("that was amazing.","smile","base","base","mid")
                                m "[current_payout] to Ravenclaw."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("...i'm completely covered, aren't I?","smile","base","base","mid")
                                m "Get out."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("okay, Professor.","smile","base","base","mid")
                                jump end_cho_event


        "-I want to fuck your face.-":
            m "I want to fuck your face."
            call cho_main("What?...","smile","base","base","mid")
            m "I want to use your mouth like a pussy."
            call cho_main("Professor!","smile","base","base","mid")
            call cho_main("Professor! that sounds so dirty.","smile","base","base","mid")
            m "Get on your knees and open your mouth."
            call cho_main("Well...","smile","base","base","mid")
            call cho_main("Well...I am getting [current_payout] house Points...","smile","base","base","mid")
            "Cho slides down to her knees and opens her mouth, sticking her tounge out."
            call cho_main("ah Oo 'ea'y?(are you Ready?)","smile","base","base","mid")
            "Your cock throbs against your heavy robes."
            m "That's good, girl."
            "You pull out your thick wizard dick and slap it threateningly against your palm."
            call cho_main("(So scary...)","smile","base","base","mid")
            "You carefully guide your cock into Cho's soft, wet mouth."
            call cho_main("Hmmm...","smile","base","base","mid")
            call cho_main("Hmmm...(it's so thick!)","smile","base","base","mid")
            "The young witch's mouth is warm and surprisingly accommodating."
            "You push your cock deeper into her mouth."
            "You stop when you feel your thick head rest against the entrance to her throat."
            call cho_main("*Hrk!*","smile","base","base","mid")
            call cho_main("*Hrk!* *Ack!*","smile","base","base","mid")
            call cho_main("*Hrk!* *Ack!* *Glg*...","smile","base","base","mid")
            m "By the sands!"
            "To your surprise Cho forces her head forward, choking herself on your wizard dick."
            "It takes you a moment to catch your breath."
            "Then you grab Cho's head in your hands and hold tightly."
            m "There's a good witch..."
            "You drag your cock back, out of the slippery tightness of Cho's throat, stopping at the entrance."
            "Then you thrust deep, driving your it all the way to the hilt."
            call cho_main("AALG! HHHGGGGG!","smile","base","base","mid")
            call cho_main("AALG! HHhgGggG! (god he's choking me!)","smile","base","base","mid")
            "The young witch's throat feels too good, and you begin to fuck it in earnest."
            call cho_main("*glug* *GluG* *glg* *Gluck*","smile","base","base","mid")
            call cho_main("(Oh my god....)","smile","base","base","mid")
            call cho_main("*GlG* *Glg* *Glg*","smile","base","base","mid")
            call cho_main("(My throat...)","smile","base","base","mid")
            call cho_main("(My throat...feels...so good...)","smile","base","base","mid")

            menu:

                "-Cum-":
                    #Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!","smile","base","base","mid")
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, licking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.","smile","base","base","mid")
                    call cho_main("Well, for a geezer, I mean.","smile","base","base","mid")
                    m "Thank you?"
                    call cho_main("I'll take my points now.","smile","base","base","mid")
                    m "..."
                    m "...Yes, of course. [current_payout] to Ravenclaw."
                    jump end_cho_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?","smile","base","base","mid")
                    call cho_main("Hm!...Blehrg!","smile","base","base","mid")
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out between her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("Do you want me to drink it?","smile","base","base","mid")
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("I'll swallow all of that tasty cum if you want.","smile","base","base","mid")
                    call cho_main("And i won't even charge extra...","smile","base","base","mid")

                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.","smile","base","base","mid")
                            "Cho leans forward and gives your cock a few quick strokes before guiding the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Rapidly, the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....","smile","base","base","mid")
                            call cho_main("(Holy shit!)","smile","base","base","mid")
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lip."
                            "Cho looks up into your eyes, pleadingly."

                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                    "You pass Ms. Chang the glass just as she dribbles another little stream of cum over her lip."
                                    call cho_main("Blehgff...","smile","base","base","mid")
                                    "Your cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "After a few moments it's completely full."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)","smile","base","base","mid")
                                    call cho_main("(mmmm...it's so thick and slimy.)","smile","base","base","mid")
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...","smile","base","base","mid")
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Yummy.","smile","base","base","mid")
                                    m "You whore. [current_payout] to Ravenclaw."
                                    call cho_main("Thank you, Profe-","smile","base","base","mid")
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...","smile","base","base","mid")
                                    jump end_cho_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?","smile","base","base","mid")
                            "Cho leans forward swallowing your cock to the hilt."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to volently fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*","smile","base","base","mid")
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*","smile","base","base","mid")
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)","smile","base","base","mid")
                            "When it's over, your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("Thank","smile","base","base","mid")
                            call cho_main("Thank you","smile","base","base","mid")
                            call cho_main("Thank you, Dumbledore sir...","smile","base","base","mid")
                            m "[current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?","smile","base","base","mid")
                                call cho_main("Okay.","smile","base","base","mid")
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*","smile","base","base","mid")
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke it."
                                call cho_main("Cum for me, Professor!","smile","base","base","mid")
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...","smile","base","base","mid")
                                call cho_main("Oh my god...","smile","base","base","mid")
                                call cho_main("That was amazing.","smile","base","base","mid")
                                m "[current_payout] to Ravenclaw."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("...I'm completely covered, aren't I?","smile","base","base","mid")
                                m "Get out."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("okay, Professor.","smile","base","base","mid")
                                jump end_cho_event


        "-Ms. Chong, do you eat ass?-":
            m "Ms. Chong, do you eat ass?"
            call cho_main("Are you asking or telling?","smile","base","base","mid")
            m "Get over here."
            "Cho playfully hops over to you, stopping just in front of your desk."
            call cho_main("Well?","smile","base","base","mid")
            m "(What's she doing?)"
            m "(Maybe she's trying to tell me something...)"

            menu:

                "-Treat her like a slut.-":
                    "Words are for Socialists and pussies."
                    "You suddenly grab Cho by the hair and drag her down to her knees."
                    call cho_main("!","smile","base","base","mid")
                    call cho_main("Profes-","smile","base","base","mid")
                    "Before she can say another word you pull your wizard robes open and jam your cock in her mouth."
                    call cho_main("(Yessss...)","smile","base","base","mid")
                    call cho_main("*Hrk!*","smile","base","base","mid")
                    call cho_main("*Hrk!* *Ack!*","smile","base","base","mid")
                    call cho_main("*Hrk!* *Ack!* *Glg*...","smile","base","base","mid")
                    "You can feel Cho's tongue thrashing violently around your head as she fights your hands."
                    call cho_main("*oomph* *Gluck*","smile","base","base","mid")
                    "Your cock prods the back of her throat, and Cho's movements suddenly stop as she focuses on fighting her gag reflex."
                    call cho_main("*gack!* *Cough*","smile","base","base","mid")
                    "A mouthful of slime and spit shoots out around your cock as she chokes on it."
                    call cho_main("(I'm going to die...)","smile","base","base","mid")
                    call cho_main("(You nasty, old man...)","smile","base","base","mid")
                    "Cho's chin drips with tangled cords of slime."
                    "Your balls slap against her face as you pound her slippery fuck hole."
                    call cho_main("(I'm such a whore...)","smile","base","base","mid")
                    m "That's good, you fucking whore."
                    call cho_main("(Yes!)","smile","base","base","mid")
                    "Suddenly, you feel Cho's hands tightly grip your ass, and you realize that you haven't had to hold her down."
                    "The crazed young witch desperately fucks her face against your cock."
                    "Your cock feels amazing, but you have other plans."
                    "You grab Cho's hands and push her down."
                    $ renpy.play('sounds/pop.mp3')
                    "Your cock pops out of her throat, and she falls back on her haunches."
                    m "Get over here and lick my ass."
                    call cho_main("yes, Professor!","smile","base","base","mid")
                    "Cho crawls under your robes and leans back."
                    "Suddenly, you feel a slimy, wet sensation as Cho tongue probes your hairy asshole."
                    m "That's it."
                    m "That's it. That's it..."
                    "While Cho's tongue twists and tickles your asshole you pump your thick meat wand."
                    "Cho's hands push your own away and she begins to pound your cock while tongueing your ass."
                    m "By the Jews of Akabur..."
                    "Cho's hands work in concert with her tongue and it's not long before you find yourself on the edge."
                    #Genie Cums.
                    "Your cock explodes in Cho's soft, slippery hands as her tongue presses deep into your ass."
                    "Thick, heavy ropes of your cum shoot across the room, coating the floor at your feet."
                    call cho_main("Wow!","smile","base","base","mid")
                    call cho_main("Wow! that was intense...","smile","base","base","mid")
                    m "Good work, Ms. Chang. [current_payout] to Ravenclaw..."
                    call cho_main("Thank you, Professor Dumbledore.","smile","base","base","mid")
                    jump end_cho_event


label cho_mad_blowjob:
    call cho_main("I can't believe you, you old pervert.","smile","base","base","mid")
    call cho_main("Fine.","smile","base","base","mid")
    call cho_main("Fine. I'll do it.","smile","base","base","mid")
    "Cho drops to her knees and reaches into your robes grabbing your semi-hard cock."
    call cho_main("You're not even hard yet.","smile","base","base","mid")
    "Cho leans forward and after gathering saliva in her mouth she spits a messy dollop across your cockhead."
    "The angry young witch begins to roughly pump your hardening cock."
    m "Take it easy."
    call cho_main("Take it easy?","smile","base","base","mid")
    "Cho leans forward and guides your cock into her mouth."
    "Her tongue assaults your sensitive head, writhing against your glans."
    "Then she begins to bob her head back and forth, sucking hard."
    m "That's good."
    "Cho spits your cock out and pumps it with fast, rough strokes."
    call cho_main("Are you going to cum yet, you old jerk?","smile","base","base","mid")
    m "I'm almost there."
    "Cho takes your cock back into her mouth, sucking and bobbing."
    "Soon, you reach your limit, but before you can cum Cho feels your shaft twitch and pulls back."
    call cho_main("Cumming so soon?","smile","base","base","mid")
    "Cho squeezes your cock uncomfortably hard and pumps your shaft so fast that your mind reals from the twin sensations of pleasure and pain."
    ##Genie cums
    "Suddenly, your cock throbs and just as you begin to cum Cho bends your twitching cock down, forcing you to cum on the floow at your feet."
    m "Ah! Cho, you Teenage Bitch!"
    "As the last few drops of your cum splatter against the floor of your office, Cho releases your abused cock."
    "She shakes the spit and pre-cum off her hand before glaring daggers at you."
    call cho_main("well? my house Points?","smile","base","base","mid")
    m "Fine. But you're only getting [points-5], you little bitch..."
    $ cho_mad += 5
    m "[points-5] to Ravenclaw."
    call cho_main("Jerk.","smile","base","base","mid")
    jump end_cho_event
