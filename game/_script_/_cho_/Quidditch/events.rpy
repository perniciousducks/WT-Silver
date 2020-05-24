
# Training Intro 1. (Hufflepuff)

label cho_quid_E1:
    # Genie should get into a drill sergeant mood here, but fails at the end.

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

    # Flags
    $ cho_mood += 9
    $ cho_quid.E1_complete = True

    jump end_cho_event

label cho_quid_E2:
    # Genie regains ability to train Cho

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
                call cho_walk(550, 200+180)

                m "Excellent!"

                jump cho_quid_E2.choices

            "\"Fly above me.\"" if not _selected[1]:
                $ _selected[1] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                m "Move a bit higher."
                call cho_walk(600, 150+180)
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

    # Flags
    $ cho.equip(cho_outfit_last)
    $ cho_quid.E2_complete = True
    $ cho_favors_unlocked = True

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

    # Reset
    $ cho.equip(cho_outfit_last) # Equip last worn clothes
    $ cho_quid.E3_complete = True
    $ cho_quid.lock_practice = True

    jump end_cho_event

label cho_quid_E4:
    # Genie asks Hermione if she would agree to commentate the game.

    call her_main(xpos="mid", ypos="base", trans=fade)
    m "[hermione_name], how much do you know about Quidditch?"
    call her_main("[genie_name], I mean, I've taken flying lessons... they're mandatory.", "open", "base", "base", "R")
    m "Ah, okay... and here I was hoping that you'd be able to commentate this years quidditch games..."
    call her_main("Me, wasting time on something as stupid as-", "base", "closed", "base", "mid")
    call her_main("Wait...{w=0.3} What did you say?", "open", "squint", "base", "mid")
    m "I was going to ask you if you'd commentate this years quidditch games..."
    call her_main("You want me... to commentate this years wizarding school cup?", "open", "wide", "base", "mid")
    call her_main("I'd be honoured, sir!", "scream", "closed", "base", "mid", trans=hpunch)
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...", "open", "base", "angry", "mid")
    call her_main("Not to mention getting to make all the announcements...", "smile", "base", "base", "R")
    call her_main("The speeches...", "grin", "happy", "base", "mid")

    if her_whoring < 18:
        call her_main("The paper...", "soft", "narrow", "annoyed", "up")
        call her_main("The {heart}{b}preparation{/b}{heart}...", "open_tongue", "narrow", "base", "up")
    else:
        call her_main("Everybody will be focused on me...", "soft", "narrow", "annoyed", "up")

    call her_main("I accept!", "scream", "closed", "angry", "mid", trans=hpunch)
    g4 "I thought you just said you didn't-"
    call her_main("Cho will be so mad!", "crooked_smile", "happy", "base", "mid")
    m "I see..."
    g9 "Congratulations then, [hermione_name]! You got the job."
    call her_main("Ah!!! I better start learning-...{w=0.8} I mean, preparing my opening speech!", "open", "wide", "base", "mid", trans=hpunch)

    call her_walk(action="leave", speed=1.5)

    call bld
    m "Aaaa-nd, she's gone..."
    m "I better tell Cho about the...{w=0.8} news."

    $ cho_quid.commentator = "hermione"
    $ cho_quid.E4_complete = True

    jump end_hermione_event # This is correct, it's Hermione talking!
