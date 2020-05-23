
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
        "-Discuss Quidditch Training-" if not cho_quid.lock_training:
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


# Training Intro 1. (Hufflepuff)
# TODO: we should put training intro on all tiers which gives you a short summary of what you're up against. Private favours unlock right after

label cho_quid_E1:
    # Genie should get into a drill sergeant mood here.
    call cho_main(xpos="mid", ypos="base", trans=fade)

    m "Are you ready for your first training session?"
    call cho_main("Of course, Professor!", "smile", "base", "base", "mid")
    g4 "Professor? Who are you calling Professor, girl?"
    call cho_main("I'm... sorry?", "soft", "base", "worried", "mid")
    m "From now on you will address me only as \"Sir\"!{w} Or..."

    menu:
        "\"Coach\"":
            $ cho_genie_name = "Coach"
        "\"Sergeant\"":
            $ cho_genie_name = "Sergeant"
        "\"Captain\"":
            $ cho_genie_name = "Captain"
        "\"Professor\"":
            $ cho_genie_name = "Professor"
            m "You know what, keep calling me Professor..."

    call cho_main("Yes, [cho_genie_name].", "base", "base", "angry", "mid")
    m "And you I will call..."

    menu:
        "\"Cadet\"":
            $ cho_name = "Cadet"
        "\"Pilot\"":
            $ cho_name = "Pilot"
        "\"Maggot\"":
            $ cho_name = "Maggot"
            call cho_main("(...)", "quiver", "base", "worried", "R")
        "\"Eagle #1\"":
            $ cho_name = "Eagle #1"
        "\"Eagle #2\"":
            $ cho_name = "Eagle #2"
        "\"Cho\"":
            $ cho_name = "Cho"

    call cho_main("Yes, Sir!", "soft", "closed", "angry", "mid")
    g4 "Let's start with your \"Quiddesh\" training!"
    call cho_main("\"Quidditch\", Sir.", "annoyed", "narrow", "angry", "mid")
    g4 "Let's start with your \"Quidditch\" training, [cho_name]."
    call cho_main("!!!", "smile", "happyCl", "base", "mid", cheeks="blush")
    call cho_main("Shall I call the rest of my team up here?", "open", "base", "base", "mid")
    m "What? Why?"
    call cho_main("So they can hear your expertise as well, of course.", "soft", "narrow", "base", "mid")
    m "I don't think that will be necessary."
    m "Let's focus on you, for the moment..."
    call cho_main("Very well, [cho_genie_name].", "soft", "base", "worried", "R")
    m "Tell me, how did you usually play?{w} Why were you always losing?"
    call cho_main("Well, Hufflepuff has a really good seeker!", "open", "base", "base", "mid")
    call cho_main("He's always catching the snitch before me.", "quiver", "narrow", "worried", "down")
    call cho_main("I don't know how he does it, to be honest. It always happens so quick...", "open", "narrow", "worried", "mid")
    m "And you are \"both\" looking for that thing? At the same time?"
    call cho_main("Yes, [cho_genie_name].", "soft", "base", "base", "mid")
    call cho_main("I do my best flying around the pitch searching for it. But it's just so small and really tricky to see...", "angry", "base", "worried", "down")
    m "Why don't you look for it together? After all there is only one."
    call cho_main("Hmmm?", "annoyed", "base", "base", "mid")
    g9 "You just need to grab that Snatch before he does."
    call cho_main("???", "annoyed", "wide", "raised", "mid")
    call cho_main("[cho_genie_name]! It's \"Snitch\"!", "angry", "closed", "angry", "mid")
    m "Potato {i}potato{/i}..."
    call cho_main("You just said the same thing twice...", "open", "base", "raised", "R")
    m "Exactly..."
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("But what am I supposed to do once he catches sight of it?", "open", "narrow", "base", "mid")
    m "Catches the sight of what?"
    call cho_main("The snitch!", "annoyed", "narrow", "base", "mid")
    m "Oh, I see..."
    call cho_main("There wouldn't be a way for me to stop him. With how determined he is... and how fast he can be...", "open", "base", "base", "R")
    g9 "Well, lucky for you, you have me!"
    call cho_main("", "annoyed", "base", "raised", "mid")
    g9 "I'm also very fast and determined!"
    m "And you just gave me a great idea."
    m "We'll need to distract him!"
    g4 "So you can get a hold of that Snatch before he does!"
    call cho_main("Please stop saying that, [cho_genie_name]!", "angry", "closed", "angry", "mid")
    m "Saying what?"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("{size=-4}\"Snatch.\"{/size}", "soft", "narrow", "angry", "mid")
    g9 "*Hehehehe*{w} Now you've said it!"
    call cho_main("Could we please just talk about your plan, [cho_genie_name]?", "open", "narrow", "angry", "R")
    m "Patience, Miss Chang."
    call cho_main("Tell me!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("", "annoyed", "narrow", "angry", "mid")

    # TODO: expressions
    m "We'll hit him where he least expects it!"
    cho "And that would be?"
    m "The balls!"
    cho "What?!?"
    cho "Sir, surely you can't be-"
    m "If we entice him during the game he'll lose focus..."
    cho "Entice... what are you..."

    call cho_main("Sir, this is just ridiculous!", "scream", "closed", "angry", "mid", trans=hpunch)
    call cho_main("I thought a highly regarded wizard of your stature would know at least something that could help us at Quidditch.", "open", "narrow", "angry", "mid")
    call cho_main("I didn't hold it against you that you seemingly know very little about the sport.", "open", "base", "angry", "R")
    m "Which I proved you wrong, but who cares..."
    call cho_main("Even with my limited time I thought it was at least worth a try.{w} But hearing your suggestions now...", "angry", "narrow", "angry", "mid")
    m "You will learn soon enough, girl."
    m "It’s very clear that to win we’ll have to go beyond normal conventional methods."
    g4 "The only way you can keep a man from fulfilling his sought-out purpose, is by confronting him with his most primal instinct!"
    call cho_main("Which would be?", "annoyed", "narrow", "angry", "mid")
    g9 "The act of procreation!"
    call cho_main("Sir, are you suggesting I should have \"sex\" with him?!", "soft", "wide", "base", "mid") # Shocked
    m "What? I never said that..."
    call cho_main("", "annoyed", "narrow", "angry", "mid")
    g9 "You have a really dirty mind, girl!"
    call cho_main("But you just said-", "angry", "closed", "angry", "mid")
    m "I merely want you to distract him with your body, during the match."
    g9 "And then, when he can't keep his eyes off you..."
    g9 "You grab that Snatch!"
    call cho_main("(...)", "annoyed", "narrow", "angry", "mid")
    call cho_main("I'm sorry Sir, but I feel methods like those would get us nowhere!", "open", "closed", "raised", "mid")
    call cho_main("And it's very improper for a teacher to suggest such things! Not to mention right out vulgar!", "open", "base", "angry", "R")
    call cho_main("I'll be leaving now.{p=0.8}Please only call me should you decide to finally take things seriously...", "soft", "narrow", "angry", "mid")
    g9 "And you, think about using that petite body of yours to get closer to your dreams!"
    call cho_main("*Tzzzz*", "angry", "closed", "angry", "mid")

    if daytime:
        call cho_main("Good day, Sir...", "soft", "narrow", "angry", "mid")
    else:
        call cho_main("Good night, Sir...", "soft", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call popup("You've lost the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/head_cho_2.png")

    call bld
    m "She'll get over it..."

    $ cho_mood += 9
    $ cho_busy = True

    $ cho_quid.E1_complete = True

    jump main_room

# Training Intro 2. (Hufflepuff)
label cho_quid_E2:
    call cho_main(xpos="mid",ypos="base", trans=fade)
    m "So, have you consider going with my training methods?"
    call cho_main("I... Yes...", "soft", "closed", "angry", "mid")
    call cho_main("I've simply run out of options.{p}If we want to win the cup this year, you're the only hope we have left...", "open", "narrow", "angry", "mid")
    call cho_main("I have no choice but to try your methods, Sir.", "annoyed", "narrow", "angry", "mid")
    g9 "I'm glad you've come to your senses."
    call cho_main("(...)", "annoyed", "narrow", "angry", "R")
    g9 "Let's get this ball rolling... flying then shall we!"
    call cho_main("(...)", "annoyed", "base", "base", "mid")

    m "I will show you."
    call cho_main("", "base", "base", "base", "mid")

    m "First, get your flying thing ready!"
    call cho_main("My broom?", "soft", "base", "raised", "mid")
    m "Broom... flying carpet... Whichever you prefer."
    call cho_main("Only brooms are allowed in Quidditch, Sir.", "annoyed", "base", "base", "mid")
    m "Good for you."
    m "And put on your Quidditch outfit while you're at it..."
    call cho_main("Yes, Sir.{w} Let me just go and get all of my equipment.", "smile", "base", "base", "mid")
    call cho_main("I'll be right back.", "base", "narrow", "base", "mid")

    call cho_walk(action="leave", speed=1.5) # Cho moves, excitedly.

    call blkfade
    pause .8

    # Scene Setup
    show screen chair_left
    show screen desk
    call gen_chibi("stand", "desk", "base")
    call cho_chibi("stand", "right", "base")

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    call hide_blkfade
    pause .8

    call cho_main("Ready when you are, [cho_genie_name]!", "smile", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    hide screen cho_main
    with d3

    # Tutorial menu
    $ _selected = [False, False, False]
    $ menu_y = 0.8

    label .choices:

    if not all(x == True for x in _selected): # Has selected every position once? Loop if the answer is no.
        call bld
        menu:
            m "Now..."
            "\"Fly in front of me.\"" if not _selected[0]:
                $ _selected[0] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                call cho_walk("mid", "base")
                if cho_chibi.flip == False:
                    m "Looking good, now turn away from me..."
                    call cho_chibi("fly", "mid", "base", flip=True)
                    with d5
                call cho_main("Like this?", "soft", "base", "base", "R", xpos="base", ypos="head")
                m "A bit higher maybe..."
                call cho_walk(600, 150+180)
                m "Excellent!"

                jump cho_quid_E2.choices

            "\"Fly above me.\"" if not _selected[1]:
                $ _selected[1] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                m "Move a bit higher."
                call cho_walk(550, 200+180)
                call cho_main("Like this?", "soft", "base", "base", "downR", xpos="base", ypos="head")
                m "Great, you've got some excellent control over that stick."

                jump cho_quid_E2.choices

            "\"Fly close to me.\"" if not _selected[2]:
                $ _selected[2] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                cho "How close?"
                m "As close as you can get..."
                call cho_walk(450, 240+180)
                m "Nice, and you could hold this position during movement?"
                cho "Of course..."
                m "Great!"

                jump cho_quid_E2.choices
    else:
        pass

    m "That should be enough..."
    m "You can come down now."
    cho "Okay."

    #Cho flies down
    call cho_walk("mid", "base")
    call cho_chibi("stand", "right", "base")
    with fade

    # TODO: Posing

    m "Great job, we should definitely use positioning to our advantage!"
    cho "Well, that much is true for any quidditch game..."
    cho "I don't really see what we've achieved here."
    m "All in due time, [cho_name]..."
    m "With my training methods you'll have the upper hand over those other teams, I'm sure of it."
    cho "Okay then." #cautious smile
    m "That's all for today."
    cho "Already? I usually train for a couple of hours!"
    m "Yes, I need to come up with a pl... prepare for our next session!"
    cho "Oh... okay."
    cho "Bye then."
    m "Bye, Miss Chang."

    call cho_walk(action="leave")

    m "(Now to find out what the boy's into and make sure she's prepared to do what it takes...)"
    call popup("You've unlocked Cho private favours!", "Congratulations!", "interface/icons/head/head_cho_1.png")

    # Unlock favours
    $ cho_quid.E2_complete = True
    $ cho_favors_unlocked = True

    # Reset
    $ cho.equip(cho_outfit_last)

    jump end_cho_event

label cho_quid_E3:
    # Commentator disaster, Lee Jordan is unable to commentate.

    call cho_walk(action="enter", "desk", "base", speed=1.5)

    call play_music("stop")

    call cho_main("[cho_genie_name], there's been a disaster!", "scream", "closed", "angry", "mid", xpos="mid", ypos="base", trans=hpunch)

    call play_music("cho")

    m "Off to a good start..."
    call cho_main("[cho_genie_name], something terrible happened to Lee Jordan!", "soft", "narrow", "worried", "mid")
    m "Lee Jordan?{w=0.5} Is that a famous basketball player I'm not aware of?"
    call cho_main("What?{w=0.5} No Sir, Lee is our quidditch commentator!", "soft", "narrow", "base", "mid")
    call cho_main("He got hit in the throat by a bludger!", "disgust", "base", "raised", "down")
    call cho_main("Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season.", "soft", "closed", "worried", "mid")
    call cho_main("What are we going to do! We can't have a \"W.S.C.\" without a commentator!", "soft", "base", "worried", "mid")
    m "Can't you play without one?"
    call cho_main("No. Someone has to announce the points after all.", "annoyed", "narrow", "base", "mid")
    m "I see..."

    $ _selected = [False, False]

    label .choices:
    menu:
        m "How about we ask..."
        "\"Hermione\"":
            pass

        "\"Astoria\"" if astoria_unlocked and not _selected[0]:
            $ _selected[0] = True

            call cho_main("That mischievous little...", "clench", "wide", "raised", "mid")
            call cho_main("Not a chance!", "open", "closed", "angry", "mid")
            call cho_main("Besides, [cho_genie_name]. Did you forget that she's a Slytherin?", "open", "narrow", "angry", "mid")
            m "Right. No Slytherins. Got it."
            m "How about..."

            jump cho_quid_E3.choices

        "\"Luna\"" if luna_unlocked and not _selected[1]:
            $ _selected[1] = True

            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?", "open", "narrow", "raised", "mid")
            m "Yes?"
            call cho_main("Surely{w=0.3}, nobody in their right mind would let Luna Lovegood commentate.", "grin", "happyCl", "base", "mid") # Book quote.
            #m "I am of right mind, Miss Chang...{w} and don't call me Shirley..."
            m "(...)"
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...", "open", "base", "base", "R")
            call cho_main("Trust me, [cho_genie_name]. Luna would be a terrible choice!", "soft", "narrow", "base", "mid")
            m "Fine. How about..."

            jump cho_quid_E3.choices

    call cho_main("Hermione Granger?", "scream", "wide", "raised", "mid")
    call cho_main("She wouldn't know the first thing about quidditch!", "clench", "narrow", "angry", "mid")
    call cho_main("You can't pick her!", "annoyed", "narrow", "angry", "mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    call cho_main("Absolutely not! I won't talk to that Gryffindor skunk ever again!", "scream", "closed", "angry", "mid")
    call cho_main("Didn't I make it clear that I don't want her to {b}ever{/b} be involved in Quidditch again?", "annoyed", "narrow", "angry", "mid")
    m "Alright... are there any other students who know Quidditch rules well enough to take this... Jordan boy's place?"
    call cho_main("...", "annoyed", "base", "base", "down")
    m "Well?"
    call cho_main("Well, most of them would be on one of the Quidditch teams...", "soft", "base", "raised", "R")
    call cho_main("But Granger wouldn't know anything about Quidditch either!", "annoyed", "narrow", "angry", "mid")
    m "Do you know anybody else suited for the job?"
    call cho_main("{size=-4}Probably anyone at this point...{/size}", "annoyed", "base", "raised", "R")
    call play_music("stop")
    call cho_main("(Wait a minute...)", "annoyed", "wide", "raised", "mid")
    play music "music/marty-gots-a-plan-by-kevin-macleod.mp3" fadein 1.0
    call cho_main("No...", "smile", "base", "base", "mid") #Mischievous smile
    g9 "I'll ask her... What's the worst that could happen..."
    call cho_main("Yeah, actually you're probably right...", "grin", "narrow", "angry", "mid")
    m "Don't worry she'll do a-{w=1.0}{nw}"
    g4 "Wait... what did you say?"
    call cho_main("I'm sure she'll do a heckin' good job!", "smile", "narrow", "angry", "mid")
    call cho_main("(She'll flub the whole thing and everyone will laugh at her.)", "smile", "narrow", "angry", "R") #Mischievous smile
    g9 "Well, great then. I'll ask her in that case!"
    call cho_main("(She'll be so humiliated! And no one will ever see her as anything but a show-off that knows nothing!)", "grin", "narrow", "angry", "down")
    call cho_main("(I can already picture it...{w=0.8} the whole school laughing...)", "silly", "base", "raised", "up")
    m "Miss Chang?"
    call cho_main("Oh, thank you for handling it professor!", "open", "base", "base", "mid")
    call cho_main("Boy, you took a load off my mind...", "silly", "happyCl", "base", "mid", trans=hpunch)
    m "(...)"
    call cho_main("I'll be heading back to class, if you don't mind.", "soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    m "(...)"

    $ cho_quid.E3_complete = True

    # Reset
    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    jump end_cho_event

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
            m "Give me another minute."
            cho "*Tsk*"
            m "Okay, you can come down now."

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            show screen bld1
            with d3

            # TODO: Write ending
            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
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

            # TODO: Write ending

            call cho_walk(action="leave")

            $ cho_quid.lock_practice = False
            $ cho_quid.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's sparring matches have been unlocked.", "Congratulations!", "interface/icons/head/head_cho_2.png")

            jump end_cho_event

    return
