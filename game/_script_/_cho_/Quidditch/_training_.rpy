
### Cho Quidditch Tactics ###

label cho_training:

    # Automatic-Events

    # Quiz.
    if not cho_quiz.complete:
        jump cho_quiz

    # Training Intro 1.
    # Event fails. Cho will get mad and leaves.
    if not cho_quid.E1_complete:
        jump cho_quid_E1

    # Training Intro 2.
    if not cho_quid.E2_complete:
        $ cho_training_unlocked = True
        $ cho_favors_unlocked = True
        jump cho_quid_E2

    # Slytherin Intro.
    if cho_tier == 2 and not cc_st.intro:
        $ cho_favors_unlocked = True
        jump cc_st_intro

    # Setup

    show screen blkfade
    call hide_characters
    with d5

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    call cho_chibi("stand", "right", "base")

    show screen chair_left
    show screen desk
    call gen_chibi("stand", "desk", "base")

    hide screen bld1
    hide screen blkfade
    with d5
    pause .8

    # Menu
    label .choices:

    menu:
        "-Discuss Quidditch Training-":
            if cho_tier == 1:
                # Hufflepuff
                call cc_ht_talk
            elif cho_tier == 2:
                # Slytherin
                call cc_st_talk
            #elif cho_tier == 3:
                # Gryffindor
                #call cc_gt_talk

            hide screen cho_main
            with fade

            jump cho_training.choices

        "-Discuss Tactics-" if cc_pf_talk.is_tier_complete() and not cho_quid.lock_tactic:
            if cho_tier == 1:
                # Hufflepuff
                # Clothes:  Skirt, Robes
                if not hufflepuff_match == "intro_done":
                    $ hufflepuff_match = "intro_done"

                    m "I got it!"
                    cho "Got what?"
                    m "I know how to get you that win against against those Badgers!"
                    cho "Really? How?"
                    m "You told me how, yourself."
                    m "Panties are the key!"
                    call cho_main("Panties? Why would panties have anything to do with Quidditch?", "soft", "wide", "raised", "mid")
                    m "Everything, girl!{w} For some they are the meaning of life!"
                    cho "What are you suggesting exactly?"
                    m "My plan is that we use Cedric's obsession of panties to distract him during the game."
                    cho "I don't really see how that would be-"
                    m "You'll have to wear a skirt of course."
                    cho "A skirt?" #shocked
                    g9 "Of course!"
                    g9 "If he's too focused on your panties there's no way he'll catch that snatch!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 3:
                        # Fail
                        cho "Got a better plan? One that doesn't involve showing off my panties?"
                        m "..."
                        cho "Didn't think so..."
                        m "(Damn... maybe I need to work on her confidence a bit...)"
                        g9 "(Some more favours should surely do it...)"

                        jump cho_training.choices

                if cho_whoring >= 3:
                    $ cho_quid.lock_practice = False

                    cho "..."
                    cho "You actually think that will work?"
                    m "If what you're telling me about him is true I'm sure of it."
                    cho "..."
                    cho "But what if it doesn't?"
                    cho "I need to win the game to make it to the finals!"
                    m "Then let's put this theory into practice..."
                    cho "You want me to try it out during next practice against them?"
                    m "You do practice matches against the other...{w=0.5} actually, that's a great idea!"
                    m "That way we'll know it works for sure!"
                    cho "..."
                    cho "Fine, but I'm not changing any of my other clothes, I'd rather not have anyone else staring at my panties..."
                    m "Okay then..."
                    m "Get your broom and Quidditch-gear... and put that skirt on!"
                    cho "Alright..."

                    #Cho returns with the Hufflepuff clothing combination
                    $ cho.equip(cho_outfit_quidditch_hufflepuff)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, now what?", "base", "base", "base", "mid", trans=fade)

                    m "Now let's try some flying positions..."
                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Excellent..."

                    jump cho_tactics
                else:
                    # Fail

                    cho "I will do nothing of the sort!"
                    m "Sorry?"
                    cho "You want me to wear a skirt during quidditch?"
                    cho "The whole school will be there!"
                    m "Don't focus on them, Cedric is your target!"
                    cho "But they'll see my panties!"
                    cho "No, I will not be going through with this plan of yours..."
                    cho "You better come up with something else!"

                    # Cho gets upset and leaves
                    $ cho_mood += 6
                    call cho_walk(action="leave")

                    m "(Damn... maybe I need to work on her confidence a bit...)"
                    g9 "(Some more favours should surely do it...)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

            elif cho_tier == 2:
                # Slytherin
                # Clothes: Trousers, Pullover
                if not slytherin_match = "intro_done":
                    $ slytherin_match = "intro_done"

                    m "I got it!"
                    m "I've got the perfect idea on how to beat those snakes!"
                    cho "..."
                    m "Do we say phrasing anymore?"
                    cho "Just tell me your plan."
                    m "It's all about the ass!"
                    cho "The ass?" #shocked
                    m "Yes, you told me how those brutes love a good ass spanking, now that's an ass fetish if I ever heard one!"
                    m "So this time we'll have those Slytherins get a good look of your ass!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 9:
                        # Fail
                        cho "Got a better plan? One that doesn't involve flaunting my ass to those Slytherins?"
                        m "..."
                        cho "Didn't think so..."
                        m "(Damn...)"
                        m "(Looks like she isn't confident enough yet...)"
                        m "(Some more favours should do the trick.)"

                        jump cho_training.choices

                if cho_whoring >= 9:
                    $ cho_quid.lock_practice = False

                    cho "..."
                    m "And yes, before you ask, I'm sure this will ensure the win."
                    cho "Fine..."
                    cho "I can't believe I'm saying this..." #disgust
                    cho "I'll flaunt my ass... to those Slytherins."
                    m "Excellent, then let's discuss some tactics..."
                    m "I'd like you to put on some trousers this time."
                    m "And get rid of your robes, they'll cover it too much."
                    cho "Get rid of my-" #Shocked
                    m "You can put on something else, just something that doesn't cover the goods."
                    cho "Alright... give me a minute to fetch my gear..."

                    #Cho returns with the Slytherin clothing combination
                    $ cho.equip(cho_outfit_quidditch_slytherin)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, tell me what to do.", "base", "base", "base", "mid", trans=fade)

                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Great."

                    jump cho_tactics

                else:
                    # Fail

                    cho "But, they're Slytherins!"
                    m "And?"
                    cho "You expect me to flaunt my ass to those brutes?"
                    m "Are you telling me you don't think it will work?"
                    cho "Of course it will work, they're dumb as hell."
                    cho "But I wont be doing... this..."
                    m "Well, that's your loss I guess..."
                    cho "..."
                    cho "If that's all you have then I think I'm done here."

                    # Cho gets upset and leaves
                    $ cho_mood += 3
                    call cho_walk(action="leave")

                    m "(Damn...)"
                    m "(Looks like she isn't confident enough yet...)"
                    m "(Some more favours should do the trick.)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

            elif cho_tier == 3:
                # Gryffindor:
                # Clothes: No clothes decided on yet
                if not gryffindor_match == "intro_done":
                    $ gryffindor_match = "intro_done"

                    m "I got it!"
                    cho "Finally..."
                    cho "So, what's the plan?"
                    m "It's time to get intimate!"
                    cho "Intimate?"
                    m "Yes, touchy touchy!"
                else:
                    # Repeated intro
                    m "So about that tactic..."
                    if cho_whoring < 12:
                        # Fail
                        cho "Got a better plan? One that doesn't involve me getting felt up?"
                        m "..."
                        cho "Didn't think so..."
                        m "(She doesn't seem fully convinced...)"
                        m "(But after some more favours... Surely she'll be more keen with the idea.)"

                        jump cho_training.choices

                if cho_whoring >= 12:
                    $ cho_quid.lock_practice = False

                    cho "And what are you basing this plan on?"

                    if cc_pr_manipulate_girls.is_complete(): # has completed "Manipulate the girls!" public request?
                        m "Those girls sure are fond of you by now. If you could get close to them they'll surely lose focus on the game."
                        cho "Although that doesn't solve an important issue..."
                    else:
                        m "It's obvious isn't it..."
                        cho "No?"
                        m "Those girls doing naughty things together."
                        m "If you get close to them they'll lose focus on the game!"
                        cho "..." #worried
                        cho "And what about the boys?"
                        m "What about them?"

                    cho "Shouldn't their seeker... Harry, be our priority?" #annoyed
                    m "The same tactic is sure to work for him."
                    m "I'm sure Hermione will go mental and make him lose focus if you get close to him seeing that they're friend."
                    cho "Now that's a plan!"
                    m "Great, it's settled then!"
                    # TODO: Add clothing writing if any
                    cho "Let me fetch my gear and you can show me how you want me to fly."

                    #Cho returns with the Gryffindor clothing combination
                    $ cho.equip(cho_outfit_quidditch_gryffindor)
                    $ cho_outfit_quidditch.save()
                    call cho_main("Okay then, tell me what to do.", "base", "base", "base", "mid", trans=fade)

                    m "Get on that broom, [cho_name]."

                    call cho_chibi("fly", "mid", "base")
                    hide screen cho_main
                    with fade

                    m "Great."

                    jump cho_tactics
                else:
                    # Fail

                    cho "You want me to let them feel me up by their team?"
                    m "Absolutely!"
                    m "And you should touch them a bit as well while you're at it!"
                    cho "No way!"
                    g4 "Why not?"
                    cho "Teasing them is one thing but touching as well?"
                    cho "With everyone watching" #blushes but imagining it
                    m "..."
                    cho "No, I wont do it..."
                    m "But what if-"

                    # Cho gets upset and leaves
                    $ cho_mood += 3
                    call cho_walk(action="leave")

                    m "(She doesn't seem fully convinced...)"
                    m "(But after some more favours... Surely she'll be more keen with the idea.)"

                    $ cho.equip(cho_outfit_last)

                    jump end_cho_event

        "{color=[menu_disabled]}-Discuss tactics-{/color}" if not cc_pf_talk.is_tier_complete() or cho_quid.lock_tactic:
            if cho_quid.lock_tactic:
                m "(We've already established a tactic for the next match)"
            else:
                m "(I don't know enough about the enemy team.)"
                m "(Cho and I should have a talk first.)"

            jump cho_training.choices

        "-Start Practice Match-" if daytime and not cho_quid.lock_practice:
            if cho_tier == 1:
                # Hufflepuff
                jump cc_ht_start
            elif cho_tier == 2:
                # Slytherin
                jump cc_st_start
            #elif cho_tier == 3:
                # Gryffindor
                #jump cc_gt_start

        "{color=[menu_disabled]}-Start Practice Match-{/color}" if not daytime or cho_quid.lock_practice:
            if cho_quid.lock_practice:
                call nar(">Cho isn't ready for practice yet.")
            else:
                call nar(">You can only do that during the day.")

            jump cho_training.choices

        "-Back-":
            call cho_main("Very well, [cho_genie_name].", "open", "base", "base", "mid", xpos="base", ypos="head")

            hide screen cho_main
            show screen blkfade
            with d3

            $ cho.equip(cho_outfit_last)

            call cho_chibi("stand", "mid", "base")
            call gen_chibi("sit_behind_desk")

            call reset_menu_position

            hide screen blkfade
            call cho_main(face="happy", xpos="base", ypos="base", trans=fade)
            jump cho_requests

### Quidditch Tactics ###

label cho_tactics:

    # Menu
    label .choices:

    call hide_characters
    call bld

    $ menu_y = 0.8

    menu:
        m "(What directions should I give her?)"
        "\"Fly in front of me.\"" if cho_quid.position != "front":
            call cho_tactics.change("front")
        "\"Fly in front of me.\" {size=-6}(selected){/size}" if cho_quid.position == "front":
            pass

        "\"Fly above me.\"" if cho_quid.position != "above":
            call cho_tactics.change("above")
        "\"Fly above me.\" {size=-6}(selected){/size}" if cho_quid.position == "above":
            pass

        "\"Fly close to me.\"" if cho_quid.position != "close":
            call cho_tactics.change("close")
        "\"Fly close to me.\" {size=-6}(selected){/size}" if cho_quid.position == "close":
            pass

    jump cho_tactics.choices

    #
    # Change Tactic
    #

    label .change(position=""):

    $ cho_quid.position = position
    #TODO This plays once cho has agreed to the tactic/clothing and during the first intro
    # Once you pick the right option the practice match option unlocks (Maybe we should have it say Try out tactic?)
    # The various options should go away once you've tried it once

    # TODO: add expressions

    if position == "front":
        # The *ASS* position!

        if cho_tier == 1:
            # Hufflepuff

            call cho_walk(600, 150+180)

            cho "Is this good?"
            m "Hmm... No, that robe is in the way... I can't seem to get a good view from this angle..."
            cho "Good! Then the crowd shouldn't either!"
            m "Yes, probably..."
            m "How about instead you..."

        elif cho_tier == 2:
            # Slytherin

            call cho_walk(600, 150+180)

            cho "How's this?"
            m "Excellent, I told you getting rid of that coat would do it!"
            m "And those trousers sure emphasise the shape of your-"

            # Cho turns towards you

            cho "Good, then it's settled!"
            m "But I didn't get a proper look yet!"
            cho "..."
            m "Alright, you can come down then..."

            #Cho flies down
            #Black screen

            m "We'll test the tactics during the next practice like usual."
            cho "Do we have to? I'm sure it will work even without trying it."
            m "Of course we do! You're the one that was so adamant last time..."
            m "So let's see those results!"
            cho "Yeah... great, just let me know when..."
            g9 "I certainly shall."
            m "But this will do for today, [cho_name]."

            if daytime:
                cho "I'll head back to class then."
            else:
                cho "I'll head back to my dorm then."

            g9 "Until next time."

            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/head_cho_2.png")

            jump end_cho_event

        elif cho_tier == 3:
            # Gryffindor

            call cho_walk(600, 150+180)

            m "No, this won't do, you're way to far away from me."
            cho "Then where do you want me?"
            m "Let's see..."

    elif position == "above":
        # The ~Panties~ position!

        if cho_tier == 1:
            # Hufflepuff

            m "Now move a bit higher."

            call cho_walk(550, 200+180)

            call cho_main("Like this?", "soft", "base", "base", "downR", xpos="base", ypos="head")
            with hpunch
            g4 "Higher!"
            cho "Is this not high enough to see my-"
            g4 "Fly right above my head!"
            g4 "Show me those panties!"
            call cho_main("Of course, [cho_genie_name]...", "base", "base", "base", "downR", xpos="base", ypos="head")

            call cho_walk(500, 100+180)

            call cho_main("How is this?", "open", "base", "base", "down", xpos="base", ypos="head")

            # TODO: Panty shot CG?

            # Genie looks up.
            call gen_chibi("stand_alt", "desk", "base")
            show screen bld1
            with d3

            g4 "Yes, fantastic!"
            g9 "You have very cute panties, girl!"
            call cho_main("*Uhm*...{w=0.5} Thank you, [cho_genie_name].", "annoyed", "base", "base", "down", xpos="base", ypos="head")
            m "(I have created the ultimate up-skirt!)"
            m "(Nothing can stop us now...)"
            cho "Can I come down now?"
            g9 "Give me another minute."
            cho "*Tsk*"
            m "Okay, you can come down now."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide screen cho_main
            with fade

            cho "Enjoyed the view?" #angry/annoyed
            m "Very much so."
            cho "Good!"
            cho "Then I'm sure Cedric will like it too..."
            m "Who?"
            m "Oh yeah, that guy!"
            m "Yes, we should definitely try this during your next practice against them."
            cho "..." #annoyed
            m "When is that again?"
            cho "*Sigh* Just let me know when and I'll set one up with their captain."
            m "Excellent."

            if daytime:
                cho "If that is all, I'll head back to class."
                m "Yes, that shall do for today."
                call cho_main("Good day then, Sir...", "soft", "narrow", "angry", "mid")
            else:
                cho "If that is all, I'll head back to my dorm."
                m "Yes, that shall do for today."
                call cho_main("Good night then, Sir...", "soft", "narrow", "angry", "mid")

            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho_quid.hufflepuff_prepared = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/head_cho_2.png")

            jump end_cho_event

        elif cho_tier == 2:
            # Slytherin

            cho "Above you, [cho_genie_name]?"
            m "Yes, above..."
            cho "Okay..."

            call cho_walk(500, 100+180)

            m "Hold on, that's a bit too high I think..."
            cho "You think?" #annoyed
            m "Yeah, how about instead you..."

        elif cho_tier == 3:
            cho "You want me to fly... above you?"
            m "You heard what I said..."
            cho "Okay then..."

            call cho_walk(500, 100+180)

            g4 "Hey, how am I supposed to reach you from up there?"
            m "That's not how you get intimate!"
            cho "Why did you tell me to fly above you then?"
            m "..."
            m "Sorry, I can't hear you from all the way up there."
            m "I think it might be better if you..."

    elif position == "close":
        # The ~intimate~ position!

        if cho_tier == 1:
            # Hufflepuff

            cho "Close? How would you be able to see my-"
            m "Come closer!"

            call cho_walk(450, 240+180)

            m "Wait a second, I can't see your panties at all from this angle..."
            cho "No shi-"
            m "Let's try this instead..."

        elif cho_tier == 2:
            # Slytherin

            cho "Close?"
            m "Yes close... did I stutter?"

            call cho_walk(450, 240+180)

            m "You smell nice..."
            cho "Yeah, this is not going to work..."
            m "Fine, let's have you..."

        elif cho_tier == 3:
            # Gryffindor

            m "Come as close to me as you can..."
            call cho_main("Yes, [cho_genie_name].", "soft", "base", "base", "R", xpos="base", ypos="head")

            call cho_walk(450, 240+180)

            call cho_main("How's this? Too close?", "soft", "wink", "raised", "mid", xpos="base", ypos="head")
            m "No! It's the perfect distance!"
            m "They should even be able to smell you if you are this close!"
            call cho_main("I hope not!", "quiver", "closed", "worried", "mid", xpos="base", ypos="head")
            g9 "Why? You smell lovely, girl!"
            call cho_main("*Uhm*...{w} Thank you, Sir.", "soft", "base", "worried", "mid", xpos="base", ypos="head")

            cho "Can I come down now?"
            m "Of course."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide screen cho_main
            with fade

            m "You'll definitely distract those girls with this kind of move!"
            cho "And boys..."
            m "Oh yeah, them to!"
            cho "Just let me know when to try it out against them."
            m "Certainly... Oh, and keep wearing that scent, whatever it is."
            cho "It's just deodorant..."
            m "Yes, that! Keep wearing it!"
            if daytime:
                cho "If that is all, I'll head back to class."
                m "Yes, that shall do for today."
                call cho_main("Good day then, Sir...", "soft", "narrow", "angry", "mid")
            else:
                cho "If that is all, I'll head back to my dorm."
                m "Yes, that shall do for today."
                call cho_main("Good night then, Sir...", "soft", "narrow", "angry", "mid")


            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/head_cho_2.png")

            jump end_cho_event

    return
