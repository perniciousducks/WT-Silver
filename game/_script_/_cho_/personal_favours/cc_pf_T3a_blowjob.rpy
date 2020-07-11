

### Cho Blowjob ###

label cc_pf_blowjob:

    if cc_pf_blowjob.counter == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"

    if cc_pf_blowjob.counter < 1:
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_favor_menu.personal

    # Setup
    $ warned_her = False

    $ cc_pf_blowjob.start()

    # End Event Jump
    label end_cc_pf_blowjob:

    if cho_tier == 3:
        if cho_whoring < 12: # Points til 16
            $ cho_whoring += 1

    jump end_cho_event

label cc_pf_blowjob_T3_intro_E1:

    if cho_bj_choice == None:
        m "[cho_name], ready to reward your coach for a job well done?"
        cho "Of course... a deal's a deal."
        m "Great, in that case I think a blowjob is in order!"
        cho "A blowjob?!!"
        m "And some hand action as well of course!"
        cho "Sir, I didn't think it'd come to this... I already showed you my naked body and everything..."
        m "There are other tactics you could use that aren't just about showing off your body in public you know..."
        cho "Oh, yeah? Like what?"
        m "Your dream is to become a professional is it not?"
        cho "I... yes... I suppose it is."
        m "Then we should do our best to prepare you for what's out there!"
        m "I won't be your coach forever... Once you're looking for a proper team, you'll be in fierce competition with the other women athletes."
        m "Women that will stop for nothing to get where they want."
        m "So, as your coach, it's my responsibility to prepare you!"
        cho "And a blowjob is necessary for this?"

        if 1 > 0: # TODO: add a check if Cho has spied on the enemy before.
            m "You've seen the girls on the Gryffindor team... you think they would hesitate with something as simple as a blowjob?"
            cho "..." #Pout
            m "I see how it is..."
            m "I sure didn't think a simple blowjob would dissuade you from pursuing your dreams."
        else:
            m "Well... I can tell you this much. A woman looking to make it professionally should have enough confidence not to get stopped by something as simple as a blowjob."

        cho "..." # angry
        cho "Alright, I'll do it..."
        g9 "That's more like it!"
        cho "Don't get me wrong sir... I don't believe a word of what you just said is even remotely true."
        cho "But you've helped me get this far..."
        cho "So if a blowjob is what it takes, then so be it..."
        g9 "That's the kind of determination I've been looking for..."
        g9 "Let's find out how a skilled Quidditch player handles this type of wood..."
        cho "..." #smile #looks away
        cho "Okay, then... I'm ready."
        g4 "(At last!)"

        call gen_chibi("jerk_off_behind_desk")
        with d5

        pause 0.5
        #Genie takes out cock
        $ renpy.sound.play("sounds/zipper.mp3")

        hide screen cho_main
        with d3

        call cho_walk("desk_close", "base")
        pause 1.0

        # TODO: CG behind desk
        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_shock")
        if daytime:
            $ camera.set_overlay("day_overlay")
        else:
            $ camera.set_overlay("night_overlay")
        $ camera.set(zoom=1.0, pos=(950, -750), initialize=True)
        show screen animatedCG
        with fade

        call gen_chibi("sit_behind_desk") # reset

        # Start CG with Cho kneeling in front of Genie.
        # Cho is dressed.

        # Note: Cho does not require posing here because it happens during the CG scene.
        $ renpy.checkpoint()

        pause 1.0
        $ camera.set(pos=(0, -750), t=3.5, pause=True)
        $ camera.set(pos=(150, 400), t=2)
        cho "By Merlin's beard!" #Wide eyed looking at dick #open mouth
        gen "Something wrong?"
        $ camera.set_image("mid_surprised")
        cho "N-No...{w=0.4} It's just...{w=0.4} this close...{w=0.4} it's so much larger than--" #Looking at dick
        gen "Good, then stop staring and put your hand on it..."
        $ camera.set_image("mid_surprised_blush")
        cho "Okay..." #Blush #Normal mouth
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("up_worried")

        pause 0.6

        $ camera.set(zoom=0.39, pos=(0, 0), t=3.0)
        #Cho puts her hand on genies dick and looks up at him

        cho "..." #worried eyes
        gen "What? Don't tell me this is the first time you've done this..."
        $ camera.set_image("away_blush")
        cho "O-... of course I've done it before!"
        gen "Then get going, move those muscles!"
        $ camera.set_image("up")
        cho "..." # annoyed

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "That's it... stroke that cock you little Ravenclaw slut..."

        $ camera.set_image("up_annoyed")

        cho "[cho_genie_name]!"# Stops moving hand #Annoyed #Looks up at genie
        gen "What?"
        gen "You're doing a great job [cho_name], keep it going just like that..."

        $ camera.set_image("mid_annoyed")

        cho "..." #annoyed

        $ camera.set_image("away_blush")

        cho "Fine...."

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Such a firm grip..."
        gen "Must be from riding that broom so much..."
        gen "Although your rhythm could do with some work..."

        $ camera.set_image("cho_hj mid annoyed")

        cho "*tsk*..." #Annoyed

        call ctc

        gen "That's better..."
        gen "Now then... Let's find out what you can do with that mouth of yours, shall we?"

        $ camera.set_image("up_wide")

        cho "Already?" #Wide eyed
        $ camera.set_image("up_worried")
        cho "Can't I just keep jerking you off?"
        gen "You agreed to a blowjob did you not?."
        $ camera.set_image("mid_worried")
        cho "I...{w=0.4} well that was before you showed me your..." #Looks back down
        $ camera.set_image("away_blush")
        cho "How is this even..." #Cuts to dialog Menu choice
    else: # Alternate intro if first event has failed
        m "Ready to continue with your training?"
        cho "Of course!"
        m "Then you know what is required..."
        cho "You want me to touch your..."
        cho "..."
        cho "Fine... I'll do it."

        hide screen cho_main
        with d3

        call cho_walk("desk_close", "base")
        pause 1.0

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_surprised")
        $ camera.set(zoom=1.0, pos=(0, -750), initialize=True)
        show screen animatedCG
        with fade

        $ camera.set(pos=(150, 400), t=2.0, pause=True)

        $ camera.set(zoom=0.39, pos=(0, 0), t=3.0)
        cho "Okay, then... I'm ready."
        $ camera.set_image("mid_surprised_blush")
        cho "..." #blush
        gen "Go on then, I don't have all day..."
        $ camera.set_image("mid_blush")
        cho "..." #Pout
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("mid_annoyed")
        cho "..." #annoyed
        gen "There you go... much easier the second time, isn't it?"
        gen "Now, get those muscles moving..."

        $ camera.set_image("cho_hj mid")
        call ctc

        gen "That's it... you keep stroking, slut..."

        $ camera.set_image("cho_hj mid annoyed")
        cho "..." #Annoyed

        call ctc

        gen "Good..."
        gen "You're doing way better than last time... looks like you had some time to think things over..."

        $ camera.set_image("cho_hj up blush")

        cho "..." #looks up

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Now let's put that mouth to good use..."

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("up_shock")

        cho "Already?"
        gen "No, tomorrow... yes of course now!"
        $ camera.set_image("mid_worried")
        cho "Can't I just keep jerking you off?" #pout
        gen "This again..."

    jump cc_pf_blowjob_1

label cc_pf_blowjob_1:
    menu:
        "-A deal's a deal...-": # FAIL
            gen "That's not what we agreed on."
            gen "Get those lips on there..."

            if cho_bj_choice == None:
                $ camera.set_image("up_wide")
            else:
                $ camera.set_image("up_worried")

            cho "[cho_genie_name]!" #shocked
            gen "It's time to push those limits [cho_name]... we've been over this."
            gen "Open up..."

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            cho "But... it's... how is it even going to fit?!"
            $ camera.set_image("mid")
            gen "It will fit, you're the most flexible girl in the castle. If anyone could do it it's you..."
            cho "..."
            gen "Now, put your hand back..."
            $ camera.set_image("mid_worried")
            cho "..."
            cho "Al- Alright...!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("up_worried")
            #Cho puts her hand back on
            gen "Good... now put your lips around the tip..."

            $ camera.set_image("away_blush")
            cho "Oh-okay...{w=0.4} Here I go..."

            #Cho opens her mouth and moves in towards genies cock #Genie cock twitches
            #She moves in closer and closes her eyes with her mouth wide open and just as she barely touches it she jumps back
            $ camera.set_image("cho_bj lick fail")
            pause 1 # Pauses at last frame.
            cho "No, I can't!"

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            if cho_bj_choice == "failed":
                cho "It still won't fit!"
                gen "[cho_name]... You're here to push your limits, stop with the whining!"
                $ camera.set_image("up_worried")
                cho "I- I'm sorry [cho_genie_name]..."
                cho "I... just can't do this, it all happens too fast!"
                gen "[cho_name]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away
                $ cho_mood += 3 # Annoyed that you failed it again, sucker
            else:
                cho "It won't fit!"
                gen "[cho_name]... You're here to push your limits."
                $ camera.set_image("up_worried")
                cho "I- I'm sorry [cho_genie_name]..."
                cho "I... need some time to think..."
                gen "[cho_name]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away

            # Genie standing with his dick out, all alone, blue balled, all aloooooooone
            call gen_chibi("dick_out", 230, "base")
            show screen chair_left
            show screen desk

            hide screen animatedCG
            with fade

            #Cuts to Office and Cho walks quickly out of the room
            call cho_walk(action="leave")

            m "(Damn...{w=0.4} I'm that type of coach that keep pushing their pupils too hard...)"
            m "(Speaking of, I should jerk off or something, it kinda hurts...)"
            if cho_bj_choice == "failed":
                m "(Again... Perhaps I should ease up on her training a bit.)"

            $ cc_pf_blowjob.fail()
            $ cho_bj_choice = "failed"

            call gen_chibi("sit_behind_desk")
            hide screen chair_left
            hide screen desk
            with fade

            jump end_cho_event

        "-Take it slow...-": #Cho strokes and licks genie then goes back to stroking until climax
            gen "Okay... just keep stroking it for now..."

            if cho_bj_choice == None:
                $ camera.set_imagepath("cho_bj/hj/")
                $ camera.set_image("up_wide")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it!"
                $ camera.set_image("mid")
            else:
                $ camera.set_imagepath("cho_bj/kneel/")
                $ camera.set_image("up")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it!"
                $ camera.set_image("mid")

            cho "Of course!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("mid_blush")
            cho "..." #Blushing

            $ camera.set_image("cho_hj mid")

            call ctc

            gen "That's it, you're finally getting the hang of this..."
            gen "Who knew quidditch players were so good at handjobs..."

            $ camera.set_image("cho_hj up blush")
            cho "...." #Looks up at genie #Blushes

            call ctc

            gen "Such a good slut... stroking your coach's cock..."

            $ camera.set_image("cho_hj mid")

            cho "..."#Looks back down at cock #still stroking

            call ctc

            gen "Willing to do anything to win that cup..."

            $ camera.set_image("cho_hj mid blush")

            gen "Ready to receive her coach's cum."
            gen "Now, put your mouth on it [cho_name]..."
            $ camera.set_image("up_wide")
            #Cho stops handjob
            cho "But I thought..."
            gen "If you want to outdo your competition you need to push through your limits [cho_name]..."
            $ camera.set_image("up_worried")
            gen "Give it a little lick, I promise it won't bite."
            cho "..." #Annoyed
            $ camera.set_image("away_blush")
            cho "Fine..." #Blushes #Annoyed
            $ camera.set_image("cho_bj lick success")
            "...."
            gen "See? That wasn't bad, was it?"
            $ camera.set_image("up_annoyed")
            cho "..." # Grim look at Genie
            $ camera.set_image("mid")
            cho "..." #Looks back on cock
            gen "Go on..."
            $ camera.set_image("mid_annoyed")
            cho "..." #annoyed
            $ camera.set_image("mid_worried")
            cho "..." #Worried
            $ camera.set_image("cho_bj lick start")
            pause .7
            $ camera.set_image("cho_bj lick")
            cho "*lick-slurp-lick*"

            call ctc

            gen "Good job [cho_name]..."
            gen "I suppose that will be enough for..."
            $ camera.set_image("up_annoyed")
            cho "No! I want--"
            $ camera.set_image("away_blush")
            cho "I mean... {w=0.5} you deserve your reward [cho_genie_name]."
            cho "At least let me finish you off with my hand..."
            $ camera.set_image("mid_blush")
            gen "That's what I wanted to hear [cho_name], you're learning..."
            gen "Get going then..."

            $ camera.set_image("cho_hj mid blush")

            call ctc

            gen "That's it, grip it firmly just like that..."

            call ctc

            gen "Not bad... Not bad at all..."
            gen "I think someone deserves a reward..."
            gen "Now... a little bit faster [cho_name]..."

            $ camera.set_image("cho_hj mid blush fast")

            cho "Okay..." #Blush

            $ camera.set(zoom=0.55, pos=(0, 145), t=5.0, pause=True)

            $ camera.set_image("cho_hj up blush")
            cho "[cho_genie_name]... Will you tell me when--"
            gen "Faster [cho_name]!"
            cho "Oh... of course!"

            $ camera.set_image("cho_hj mid blush fast")
            call ctc

            gen "(Now that's my [cho_name]!)"
            gen "(I'm at my limit, should I warn her?)"

            menu:
                "-Warn her-":
                    $ warned_her = True

                    gen "That's it, almost there...!"

                    call ctc

                    gen "Get ready for your reward [cho_name]!"
                    menu:
                        "-Cum on her face-":
                            cho "..." #Eyes and mouth closed
                            gen "*ARGH*!"
                            $ renpy.play("sounds/burp.mp3") # lol
                            $ camera.set_image("cho_hj cum face")
                            pause 1.42
                            $ camera.set_image("cum") # Still image
                            gen "*Ah*..."
                            cho "Is...{w=0.5} are you done?"
                            gen "*Ah*...{w=0.4} yes, you can open your eyes now..."
                            $ camera.set_image("cum_eye")
                            cho "..." #Opens eyes
                            $ camera.set_image("cum_eye_blush")
                            cho "So... much..." #blush
                            $ camera.set_imagepath("cho_bj/kneel/")
                            $ camera.set_image("cum_eye")
                            #Cho takes hand off penis and puts to her side
                            cho "It's so sticky..." #blush
                            "{cps=3}.....{/cps}{nw}"
                            #Adds cum on cho's Doll face when CG ends

                        "-Cum on her tits (No animation yet)-":
                            cho "..." #Eyes and mouth closed
                            gen "*ARGH!*"
                            "....." #Cum stage 1
                            "....."#Cum stage 2
                            "....." #Cum stage 3
                            gen "*Ah*..."
                            cho "..." # Wide eyed
                            cho "You..." #Looks down on breasts
                            #Cho takes hand off penis and puts to her side
                            cho "My breasts..."
                            cho "So much..." #blush
                            #Adds cum on cho's Doll tits when CG ends
                            gen "That...{w=0.4} was...{w=0.4} amazing!"
                            gen "That is some talent you have there [cho_name]..."
                            cho "..." #blush #looking at penis
                            gen "[cho_name]?"
                            cho "Oh... Thank you [cho_genie_name]." #looks up at genie
                            gen "Now, get on your feet and let me have a proper look at you..."
                            #Cuts back to office screen  (sound of cloth etc as genie puts dick away and Cho moves)

                "-Don't- (Incomplete)":
                    $ warned_her = False

                    gen "(You better be ready slut...)"
                    "....."
                    "....."
                    "....."
                    gen "(!!!)"
                    cho "[cho_genie_name], are you about to--"
                    gen "*ARGH*!"
                    cho "[cho_genie_name]!" #Wide eyed
                    "....." #Cum stage 1 #closes eyes #Genie cums on face
                    "....."#Cum stage 2 #Cho moves back and Genie cums rest on tits
                    "....." #Cum stage 3 #Even more cum on tits
                    gen "*Ah*..."
                    cho "..." # Wide eyed
                    cho "M-... my face!" #Angry
                    cho "You just came on my face!"
                    gen "*Ah*..."
                    cho "..." #Angry
                    cho "Why didn't you warn me?!"
                    cho "My clothes are all ruined now..."
                    cho "There's cum all over them!"
                    gen "That...{w=0.4} was...{w=0.4} amazing!"
                    cho "Are you even liste--" #annoyed
                    gen "That is some talent you have there [cho_name]..."
                    cho "What?!"
                    gen "Get on your feet and let me have a proper look at you..."
                    cho "Fine..."

                    $ cho_mood += 4
                    #Adds cum on cho's Doll face and tits when CG ends
                    #Cuts back to office screen (sound of cloth etc as genie puts dick away and Cho moves)

    hide screen animatedCG
    with fade

    # After CG, in the office.
    # TODO: Posing, cum layers

    if warned_her:
        m "You've got a little something right there..."
        cho "Very funny [cho_genie_name]..."
        m "You finally got it, you've started pushing those limits on your own."
        m "Your confidence is showing itself more and more every day."
        cho "I... {w=0.5} You deserved it [cho_genie_name]...{w=0.5} for helping me this far..."
        cho "For teaching me... all this stuff...." #Blush
        m "(I'm a bloody saint I've waited that long...)"
        m "You're very welcome."
    else:
        cho "I can't believe you just came all over me like that..." #pout
        m "Should've put it in your mouth then..."
        cho "..." #pout

    cho "Is this what you do to Hermione as well?"

    if hg_kiss.trigger:
        m "Maybe."
        cho "I knew it..."
        m "Miss Granger knows how to properly dispose--"
        cho "She swallows?!?" #Shocked #Big text
        cho "I mean..."
        cho "Of course she does...." #small text #Blush
    else:
        m "Of course not..."
        cho "I knew--"
        cho "Wait, she doesn't do stuff like that?"
        m "No."
        cho "So I am your first?" # blush
        m "In one way or the other."
        cho "What's that supposed to mean?!" # angry
        cho "Whatever.." # pout

    cho "Are we done?" #Blush
    m "Yes, for now..."

    if daytime:
        cho "Good... I better head back to class then."
    else:
        cho "Good... I better head off to bed then."
    m "Until next time..."

    call cho_walk(action="leave")

    m "[cho_name]!"
    m "......"
    m "(Probably should've asked her to clean herself first...)"
    m "(Oh well, what's done is done.)"

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E2:
    m "Ready for an oral exam [cho_name]?"
    cho "A what?"
    m "Time to put that mouth to good use..."
    cho "My mouth to--" #Blush
    m "Any problems?"
    cho "No... of course not [cho_genie_name]..."
    m "Excellent!"
    cho "Just...{w=0.4} tell me what to do [cho_genie_name]..."

    hide screen cho_main
    with d3

    call cho_walk("desk_close", "base")
    pause 1.0

    # TODO: CG behind desk
    show screen placeholder
    with fade

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    # Note: Cho does not require posing here because it happens during the CG scene.

    gen "..."
    cho "..." #looking at dick
    gen "Go on then..."
    cho "Of course..." #Blush
    #Cho puts hand on genies dick
    gen "Just start with some stroking like you did before..."
    cho "Yes, [cho_genie_name]..."
    "....." #Cho strokes genies dick #looks at dick
    "....."
    "....."
    gen "That's it... stroke your coach's cock..."
    gen "Good...{w=0.} back and forth...{w=0.} just like I taught you..."
    cho "..." #Blushes
    "....."
    "....."
    "....."
    gen "Very good... Now take that shirt off for me will you..."
    cho "..." #Blushes #moves back to base position
    #Shirt fades away
    $ cho.strip("top")
    gen "Excellent... Now continue stroking, [cho_name]."
    cho "..."
    #Resumes handjob
    "....."
    "....."
    "....."
    "....."
    gen "You're being awfully quiet [cho_name]... it's very unlike you..."
    cho "Sorry [cho_genie_name]..."
    cho "It's just...{w=0.4} I just keep thinking...{w=0.4} how without your help I would've been out of the competition by now..."
    gen "(And without your help I'd be sitting here with a limp dick right about now.)"
    cho "I...{w=0.4} I'm sorry I doubted your methods at first [cho_genie_name]..."
    gen "I knew you'd come around..."
    cho "I'm just glad that there was some small way for me to repay you..." #looks at genies dick
    "....."
    "....."
    "....."
    gen "*Ah*... yes of course... It's nothing really."
    "....." #Cho strokes genies dick #smiles
    "....."
    "....."
    "....."
    cho "Oh please..."
    cho "Pleasuring you is little to nothing compared to what you've done for me so far..."
    cho "Giving you a bit of a reward is the least I could do..." #Blush
    "....." #Cho strokes genies dick a little faster  #Looks at dick
    "....."
    "....."
    gen "Now you're getting into it... {w=0.5} Speaking of--"
    gen "Time to put that mouth to work..."
    #Cho stops stroking
    cho "Already?"
    gen "Not again--"
    cho "Yes, [cho_genie_name]... Of course."
    #Cho moves in so her head is closer to genies penis #Still looking at penis #Penis twitches
    gen "[cho_name]?"
    cho "Just...{w=0.4} Tell me what to do..." #blush
    gen "I want you to start by putting those lips around the tip, then slowly work your mouth further down the shaft..."
    cho "I...{w=0.4} Yes, [cho_genie_name]..." #Looks at genie
    #Cho Looks back down at penis as it twitches
    cho "..." #blush
    cho "Here it goes..."

    #Cho closes her eyes as she moves in, her mouth spreading open as she works it around the tip of genies penis
    #Once her mouth worked past the tip she pulls out and open her eyes, looking up at genie

    cho "How...{w=0.4} how was that [cho_genie_name]?"
    gen "Good start, but you shouldn't close your eyes... And keep going until you find your limit, then hold it there for a bit..."
    gen "The further down the better..."
    cho "Okay..."
    #Cho closes her eyes again
    gen "[cho_name]..."
    cho "Oh!{w=0.4} Sorry [cho_genie_name]!"
    #Cho opens her eyes and looks at Genies penis."
    cho "Further down the better..." #small text

    #Cho goes in again with her eyes open this time, her mouth spreading open as it slowly goes over the tip."
    #As her mouth continues past the tip she stops and looks up at genie for some approval but he stays silent, her eyes closes slightly as she resumes by slowly going down further
    gen "*Ah*... That's... it..." #This line should auto play as she goes further down
    #As she continues further down, her pupils move up a bit more until she hits her gag reflex (slow zoom in effect)
    #Quickly retracting she moves her head back and her eyes open again (Loop going backwards fast if animated, zoom effect quickly goes back to normal)

    cho "*Gah*...{w=0.4}*Cough*,{w=0.2} *Cough*"
    #Genies dick twitches
    cho "*ah*...{w=0.4}*ah*...{w=0.4}*ah*..."
    gen "Easy there girl..."
    cho "How...{w=0.4} how did I do this time, [cho_genie_name]?" #Cho looks up at genie
    gen "Excellent!... Although... maybe a bit too far. You barely held it there for a second..."
    cho "Oh... I suspected that..."
    gen "(This girl is like a on and off switch...)"
    gen "In any case... I think you got it..."
    gen "Time to get to head bobbing [cho_name]."
    #Cho looks back down at dick
    cho "Are...{w=0.4} are you going to cum on me again [cho_genie_name]?"
    gen "I wouldn't worry about that yet... just focus on your task..."
    cho "... {w=0.5}Okay then..."
    #Cho starts jerking genie off again
    "....."
    "....."
    "....."
    gen "You'll have to do more than just--"
    #Cho moves in and starts sucking genie off properly (Not as deep as she attempted)
    cho "..."
    "....."
    "....."
    "....."
    gen "That's more like it... work that tongue..."
    #Cho look up at genie and starts going faster
    "....."
    "....."
    "....."
    gen "Fuck yes... you naughty girl..."
    #Cho pulls out and starts jerking genie off slowly
    "...."
    "...."
    cho "Am I doing good [cho_genie_name]?"
    gen "It feels great--"
    #Cho starts licking the tip a couple of times #looking at dick
    gen "*Whoa*!"
    cho "...." #looks up at genie still licking
    #Cho pulls back and smiles
    cho "Good."
    #Blowjob starts again
    gen "You...{w=0.4} you're a fast learner [cho_name]..."
    #Faster Blowjob
    "....."
    "....."
    gen "That's it..."

    # TODO: shenanigans here, needs to be reviewed
    # Player gets control here (Only options that she has already done) When you click ejaculate button it goes back to her sucking

    gen "(Time to fill this slut up... Should I warn her?)"
    menu:
        "-Warn her-":
            gen "[cho_name]... I think..."
            "....."
            "....."
            gen "There's....{w=0.5} one more thing...{w=0.5} I could teach you today..."
            #Cho looks up at genie
            gen "Time to make your coach proud... Get ready!"
            "....."
            "....."

            menu:
                "\"I'll even give you some house points!\"":
                    $ cho_bj_choice = "points"
                    #Cho pulls back
                    cho "House points!?" # angry #Wide eyed #Big text
                    gen "Fuuuuuuuuuuuuuuuuuuuck!" #Big text #Auto forwards #Text appears slowly and it cuts to next scene before it finishes
                    #Genie cums on Cho's face and tits
                    cho "Ah!" #Cum stage 1 #face #Cho pulls back
                    "....."#Cum stage 2 #tits
                    "....." #Cum stage 3 #tits

                    show screen blkfade
                    with d3

                    cho "My eye!" #Big text
                    cho "I think I got some in my eye!" #Big text
                    gen "*Ah*...{w=0.4} Why'd you pull back!"

                    # TODO: Hide CG
                    hide screen placeholder
                    hide screen blkfade
                    with d3

                    #Office screen (Cho has cum on her face and tits)
                    cho "House points!"
                    cho "You want me to swallow your semen for house points?!"
                    m "The points were just going to be a bonus."
                    cho "A bonus on top of?"
                    m "Not having to clean up..."
                    m "Although I guess you didn't see it that way since you--"
                    cho "..." #Angry
                    m "Pulled...{w=0.5} back..."
                    cho "I'm not selling my body for points!"
                    m "Of course..."
                    cho "I can't believe you..." #Small text

                    call cho_walk("door", "base")

                    cho "Who does he think I am?{w=0.4} I'm not Hermione, that slut!" #Small text
                    m "[cho_name]."

                    call cho_chibi("stand", "door", flip=False)
                    with d5
                    cho "I don't want to hear any of your excuses [cho_genie_name]!"
                    call cho_chibi("stand", "door", flip=True)
                    with d5
                    m "At least let m--"

                    $ renpy.play('sounds/door_down.mp3')
                    with hpunch
                    call cho_walk(action="leave")

                    pause 1.0
                    m "..."
                    pause 0.5

                    call cho_walk(action="enter")
                    with d5

                    pause 1.0

                    m "Don't say I didn't try to--"
                    cho "Shut... up!"
                    $ renpy.sound.play("sounds/cloth_sound2.mp3")
                    $ cho.wear("top")

                    pause 1.0
                    call cho_walk("door", "base")
                    $ renpy.play('sounds/door_down.mp3')
                    with hpunch
                    call cho_walk(action="leave")

                    m "..."
                    m "(She'll get over it...)"
                    m "(I think.)"

                    $ cho_mood += 12

                "\"Taste that cum in your mouth!\"":
                    $ cho_bj_choice = "taste"
                    #Cho stops for a second to consider and then starts going again
                    gen "That's it [cho_name]!"
                    cho "..." #blush
                    "...."
                    "...."
                    gen "Here it comes!"
                    gen "*ARGH!*" #Big text screen shake
                    cho "!!!" #Cum stage 1  #cho's eye expression wide
                    "..." #Cum stage 2 #Cum splatters from the side of her mouth #Cheeks bulge slightly
                    "...." #Cum stage 3 #Cho pulls away and genie cums some on her face
                    #Cho opens her mouth and lets the cum dribble out
                    cho "*Ah*...{w=0.4}*Ah*....{w=0.4}*Ah*..." #blush
                    cho "So...{w=0.4} so much...." #blush
                    cho "But my skirt...{w=0.4} it's ruined again..."
                    gen "Nicely done [cho_name], I knew you'd have it in you!"
                    gen "Now, get on your feet so I can have a look at you..."
                    cho "..." #Blush

                    # TODO: hide CG screen
                    hide screen placeholder
                    with fade

                    # TODO: Posing, cum layers
                    #Cho has no shirt, cum on her skirt and down her tits

                    m "Although can't say the same for--"
                    cho "My clothes are all sticky..."
                    m "If you don't want your clothes dirty you'd better swallow next time..."
                    cho "Swallow [cho_genie_name]'s..." #Blush
                    cho "I don't know..." #Blush
                    m "In any case, you've excelled today [cho_name]."
                    cho "Thank...{w=0.4} Thank you...{w=0.4} I think I need to lie down for a bit..."
                    cho "It was exhausting..."
                    if hg_kiss.trigger:
                        cho "I don't know how Granger can keep doing this for this long."
                        g9 "(Heh, you have no idea girl...)"

                    m "Of course..."
                    m "Off you go."
                    cho "Thank you [cho_genie_name]..."

                    if daytime:
                        cho "Good day..."
                    else:
                        cho "Good night..."

                    call cho_walk("mid", "base")
                    m "[cho_name]!"

                    call cho_chibi("stand", "mid", "base", flip=False)
                    with d5

                    cho "Yes [cho_genie_name]?"
                    m "Your top..."
                    cho "Oh... Of course!" #Blush

                    $ cho.wear("top")
                    $ renpy.sound.play("sounds/cloth_sound2.mp3")

                    cho "..." #Cho puts on top
                    cho "Thank you [cho_genie_name]..."

                    call cho_walk(action="leave")

                    m "...{w=0.5}Silly girl."
                    #Cho leaves
                    #End Scene #Marks at completed


                "\"Swallow that cum!\"":
                    $ cho_bj_choice = "swallow"
                    #Cho's eyes goes wide and pulls out
                    cho "But [cho_genie_name]--" #Big text
                    gen "[cho_name]!" #Big text #Screenshake?
                    cho "!!!" #wide eyed
                    #Cho quickly goes back in as genie releases in her mouth
                    "....." #Cum stage 1 #cho's eye expression wide
                    gen "That's it [cho_name], take it all!"
                    "....."#Cum stage 2 #cum starts coming out on side of mouth
                    cho "*Mmmmf*"
                    "....." #Cum stage 3 #More cum coming out and some out of nose, she has some around her cheeks and a bit on her breasts
                    #Genie cock now out of her mouth and slightly dripping cho's looks a bit worried as she's standing there with cum still in her mouth.
                    #Cho then swallows what's still in her mouth
                    cho "*ah*...{w=0.4}*ah*...{w=0.4}*ah*...!"
                    cho "I... I just swallowed my coach's cum..."
                    gen "Nicely done [cho_name]."

                    # TODO: hide CG screen
                    hide screen placeholder
                    with fade

                    # TODO: Posing, cum layers
                    #Cho still has some cum on her cheeks and tits but not a lot

                    m "Now this is the kind of initiative I'm talking about!"
                    cho "..." #blank stare
                    m "[cho_name]?"
                    cho "Yes...{w=0.5} sorry...{w=0.5} thank you [cho_genie_name]."
                    cho "Is that all?"
                    if daytime:
                        m "That will be all for today..."
                    else:
                        m "That will be all for tonight..."
                    cho "Okay, good..."
                    #Cho walks out of door still without shirt on
                    call cho_walk(action="leave")
                    m "[cho_name]!"
                    #Cho comes back through the door
                    call cho_walk(action="enter")
                    with d5

                    cho "Yes [cho_genie_name]?"
                    m "..."
                    cho "Oh, of course!" #Wide eyed
                    #Cho puts on her shirt
                    $ cho.wear("top")
                    $ renpy.sound.play("sounds/cloth_sound2.mp3")

                    if daytime:
                        cho "Bye then!"
                    else:
                        cho "Good night then!"

                    call cho_walk(action="leave")

                    m "(Heh. She's silly, but adorable.)"
                    m "(Not the worst of the combinations.)"
                    #Cho leaves
                    #End Scene #Marks at completed

        "-Just cum down her throat-":
            $ cho_bj_choice = "throat"
            gen "[cho_name]..."
            gen "I was wrong...{w=0.4} earlier...{w=0.4} there's one more thing for you to learn today..." #Genie puts hand on cho's head
            cho "*Hmmf*?" #looks at genie
            gen "How to--"
            gen "Swallow coach's cum!" #big text #Cum stage 1 #Genie pushes cho's head forward a bit
            cho "*Mff*!!!" #Cum stage 1 #Cho's mouth  #cho's eye expression wide
            gen "That's it slut!" #Cum stage 2 #Cum splatters from the side of her mouth #Cheeks bulge slightly #cho's pupils on dick
            cho "*Gah*!" #Cum stage 3 #Genie lets go  #Cho pulls away and genie cums on her face
            gen "..."
            cho "*Cough*-*Cough*-...*Ah*...{w=0.4}*Ah*..."
            gen "That was awesome... great job--"
            cho "What...{w=0.4}the hell...{w=0.4} is wrong with you?!?!" #screen shake
            gen "What do you--"
            cho "Why didn't you warn me! I almost choked!"
            cho "I never agreed to--"
            gen "It's sort of expected with a blowjob..."
            cho "..." #Wide eyed

            show screen blkfade
            with d3

            cho "For a first blowjob?! It is not!"
            gen "I mean...{w=0.4} wait did you say first... does that mean you still want to do--"
            $ cho.wear("all")
            $ renpy.sound.play("sounds/cloth_sound2.mp3")
            cho "I can't believe you..."

            # TODO: Hide CG
            hide screen placeholder
            hide screen blkfade
            with d3

            # TODO: Posing, cum layers

            #Cut to office screen #Cho has put on her top
            m "As I said, it's kind of expected from the whole blowjob thing..."
            cho "You...{w=0.4} you're joking right?"
            m "Deadly serious..."
            m "Unless I fancy covering your face that is..."
            cho "Unless you--" #disgust
            cho "*Humph*!"

            # Gets upset
            $ cho_mood += 12

            cho "I'm going to go take a shower now if you don't mind!"
            m "You're dismissed [cho_name]."
            cho "Good!"
            call cho_walk("door", "base")
            cho "Seriously... just ask first..." #Small text #Pout #Blush

            call cho_walk(action="leave")

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E3:
    m "Let's see what that mouth can do."
    cho "You want to...{w=0.4} use my mouth again [cho_genie_name]?"
    cho "I guess I could..." #Blush #Horny

    if cho_bj_choice == "points":
        m "And this time I won't make the mistake of offering house points..."
        cho "You better not."
        m "But my expectations are still the same..."
        m "For you to push your limits on your own..."
        cho "So you want me to..."
    elif cho_bj_choice == "taste":
        m "And if you don't want those clothes dirty you better swallow this time..."
        cho "..." #blush
    elif cho_bj_choice == "swallow":
        cho "You expect me to swallow again?"
        m "Of course, that's part of the deal..."
    else: # cho_bj_choice == throat - Using `else` as a fallback for degenerates that use cheats
        cho "Will you warn me this time?"
        m "Of course..."

    cho "Fine..."
    m "Good! And one more thing..."
    m "I expect some dirty talk this time."
    cho "Dirty talk, [cho_genie_name]?" #pout
    cho "I... If that's what you want..." #Blush
    m "Good, then get over here..."

    hide screen cho_main
    with d3

    call cho_walk("desk_close", "base")
    pause 1.0

    # TODO: cg
    show screen placeholder
    with fade

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    cho "Do you want me to take my top off again [cho_genie_name]?"
    gen "Initiative..."
    cho "..." #Cho takes top off
    gen "..." #Genie takes out cock
    cho "..."
    cho "In that case...{w=0.4} Just...{w=0.4} just relax [cho_genie_name] and I'll take care of you..."
    #Cho moves up closer
    cho "..."
    cho "You-... your cock is so big [cho_genie_name]!"
    gen "What?"
    cho "I'm... this is what you asked for isn't it?"
    gen "Oh, yes... keep on going then, [cho_name]."
    #Cho grabs genies dick
    cho "..."
    #Cho starts jacking genie off #Looking at dick
    "....."
    "....."
    "....."
    cho "You... do you like it when I stroke it like this?" #Looks at genie
    gen "..."
    cho "..." #Annoyed #Looks at dick
    "...."
    "...."
    "...."
    cho "Want me to go faster?"#Looks at genie
    gen "..."
    cho "...." #Worried #Looks at dick
    "...."
    cho "I love the feeling of your cock in my hand!"
    gen "That's more like it [cho_name]..."
    "...."
    "...."
    cho "And the taste of your..." #Looks at dick
    #Cho goes in and either licks or kisses genies dick
    "...."
    gen "Continue..."
    cho "..." #blushes #Looks up at genie
    #Cho continues stroking genie
    "...."
    "...."
    "...."
    cho "Will you let me put my lips around it [cho_genie_name]?" #Looks at genie
    gen "Perhaps..."
    cho "..." #blush #Looks at dick
    "...."
    "...."
    "...."
    cho "What do you--"  #Looks at genie
    gen "Tell me you want it..."
    cho "[cho_genie_name]?"
    gen "Tell me how much you want my cock in your mouth."
    cho "..."
    #Cho stops stroking but still holding genies cock #looking at cock
    cho "I...{w=0.4} I want...{w=0.4} I need your cock in my mouth!"
    gen "..." #genie dick twitches in cho's hand (if possible)
    cho "..." #Wide eyed looking at genies cock
    cho "I need..."
    cho "I..."
    gen "Go on..."
    cho "I need to feel your cum going down my throat..."
    gen "That's it [cho_name]... Now work that mouth of yours for your reward..."
    cho "..." #Blushes
    #Cho puts her mouth against genies penis
    #Cho slowly goes half way down his shaft
    gen "That's it..."
    #Cho removes her mouth from genies dick again and looks up at him
    cho "Sir... How am I supposed to talk dirty--"
    gen "Your reward [cho_name]!"
    cho "Yes, [cho_genie_name]!"
    #Cho looks back down on dick
    #Cho puts her mouth against it and then starts sucking it slowly
    "...."
    "...."
    "...."
    gen "Good... Suck that cock like it's the only thing between you and winning that cup..."
    #Cho looks up at genie as she's sucking and starts going faster.
    "..."
    "..."
    "..."
    gen "That's it [cho_name], coach will soon reward you for all of your efforts..."
    cho "..." #Looks back down on cock
    "..."
    "..."
    "..."
    gen "Good... keep going just like that..."
    "..."
    "..."
    #Cho suddenly pulls out
    gen "I didn't say you could--"
    #Cho starts jerking genie off and looks up at him
    cho "Cum for me [cho_genie_name]!"
    cho "I need to taste your delicious cum down my throat!"
    cho "I need to swallow it all!"
    gen "Then work for it!"

    # TODO:
    #Player gets control here and when they click on ejaculate it goes back to her sucking

    #
    # Discuss this part if we prefer more writing or player control.
    #

    cho "That's it [cho_name], get ready for your reward."
    #Cho starts sucking fast again if she's not already
    "..."
    "..."
    "..."
    gen "Open up [cho_name], here it comes!" #large text
    gen "*ARGH!*"
    "....." #Cum stage 1 #Down her throat #Cho eyes wide
    "....."#Cum stage 2 #Some cum comes out on side of mouth
    "....." #Cum stage 3 More cum
    gen "*Ah*..." #Genie pulls out
    cho "..." #Mouth full
    #Gulp sound
    cho "..." #swallows
    cho "*Gah*..."
    gen "That's more like it!"
    gen "Now... On your feet [cho_name]."
    cho "*Ah*...{w=0.4}Ah*...{w=0.4}Yes [cho_genie_name]..."

    # TODO: hide cg
    hide screen placeholder
    with fade

    if cho_bj_choice in ("taste", "points"):
        cho "I...{w=0.4} I did it...{w=0.4} I swallowed your cum [cho_genie_name]."
        m "As expected."
        m "But an improvement from last time nevertheless..."
        cho "Thank you [cho_genie_name]..."
    elif cho_bj_choice == "swallow":
        cho "I...{w=0.4} I hope you liked it [cho_genie_name]."
    else: # cho_bj_choice == throat - Using `else` as a fallback for degenerates that use cheats
        cho "I...{w=0.4} I did it..."
        m "And without my help this time."

    cho "Your...{w=0.4} Your cum...{w=0.4} was delicious [cho_genie_name]..."
    g9 "That's right [cho_name]... and if you keep doing such a good job there's even more where that came from..."
    m "You can stop talking dirty now."
    cho "I wasn-... Yes [cho_genie_name]..." #blush, looking right
    cho "So... Is that all?"
    m "For now..."
    cho "Okay then..."
    if daytime:
        cho "In that case I'll head back to class."
    else:
        cho "I'll head back to my dorms then..."
    m "Of course...{w=0.4} you better be ready for next time..."
    cho "Next...{w=0.4} yes [cho_genie_name]..."
    call cho_walk("door", "base")
    cho "(He's so commanding...)" # horny
    cho "(And he has such a big stick too!)"
    cho "(No wonder Hermione enjoys it so much...)"
    m "[cho_name]."

    call cho_chibi("stand", "door", "base", flip=False)
    with d5

    cho "Yes... sorry!" #Blush
    cho "Bye then!" #Blush

    call cho_walk(action="leave")

    jump end_cc_pf_blowjob
