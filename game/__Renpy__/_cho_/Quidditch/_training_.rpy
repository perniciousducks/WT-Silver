

### Cho Quidditch Training ###

label cho_training_menu:

    # Quiz.
    if not cho_quiz_complete:
        jump cho_quiz_1

    # Training Intro 1.
    # Event fails. Cho will get mad and leaves.
    if cho_training_state == "intro_1":
        $ cho_training_state = "intro_2"
        jump quidditch_training_intro_1

    # Training Intro 2.
    if cho_training_state == "intro_2":
        $ cho_training_state = "complete"
        $ cho_training_unlocked = True
        $ cho_favors_unlocked = True
        jump quidditch_training_intro_2

    jump change_quidditch_tactics



# Training Intro 1.
label quidditch_training_intro_1:
    # Genie should get into a drill sargeant mood here.
    call cho_main(xpos="mid",ypos="base",trans="fade")

    m "Are you ready for your first training session?"
    call cho_main("Of course, Professor!","base","base","base","mid")
    g4 "Professor? Who are you calling Professor, girl?"
    call cho_main("I'm... sorry?","soft","base","raised","mid")
    m "From now on you will address me only as \"Sir\"!{w} Or..."

    menu:
        "\"Coach\"":
            $ cho_genie_name = "Coach"
        "\"Sergeant\"":
            $ cho_genie_name = "Sergeant"
        "\"Captain\"":
            $ cho_genie_name = "Captain"

    call cho_main("Yes, [cho_genie_name].","smile","base","base","down")
    m "And you I will call..."

    menu:
        "\"Cadet\"":
            $ cho_name = "Cadet"
        "\"Pilot\"":
            $ cho_name = "Pilot"
        "\"Maggot\"":
            $ cho_name = "Maggot"
            call cho_main("(...)","quiver","base","sad","R")
        "\"Eagle #1\"":
            $ cho_name = "Eagle #1"
        "\"Eagle #2\"":
            $ cho_name = "Eagle #2"

    call cho_main("Yes, Sir!","soft","angry","angry","mid")
    g4 "Let's start with your \"Quiddesh\" training!"
    call cho_main("\"Quidditch\", Sir.","soft","narrow","base","mid")
    g4 "Let's start with your \"Quidditch\" training, [cho_name]."
    call cho_main("!!!","smile","base","base","downR") # Happy
    call cho_main("Shall I call the rest of my team up here?","open","base","base","mid")
    m "What? Why?"
    call cho_main("So they can hear your expertise as well, of course.","soft","narrow","base","mid")
    m "I don't think that will be necessary."
    m "Let's focus on you, for the moment..."
    call cho_main("Very well, [cho_genie_name].","soft","base","base","R")
    m "Tell me, how did you usually play?{w} Why were you always losing?"
    call cho_main("Well, Hufflepuff has a really good seeker!","open","base","base","mid")
    call cho_main("He's always catching the snitch before me.","quiver","narrow","sad","down")
    call cho_main("I don't know how he does it, to be honest. It always happens so quick...","open","narrow","sad","mid")
    m "And you are \"both\" looking for that thing? At the same time?"
    call cho_main("Yes, [cho_genie_name].","soft","base","base","mid")
    call cho_main("I do my best flying around the pitch searching for it. But it's just so small and really tricky to see...","angry","base","sad","down")
    m "Why don't you look for it together? After all there is only one."
    call cho_main("Hmmm?","annoyed","base","base","mid")
    g9 "You just need to grab that Snatch before he does."
    call cho_main("???","annoyed","wide","raised","mid")
    call cho_main("[cho_genie_name]! It's \"Snitch\"!","angry","closed","angry","mid")
    m "Potato potato..."
    call cho_main("You just said the same thing twice...","open","base","raised","R")
    m "Exactly..."
    call cho_main("(...)","annoyed","narrow","angry","mid")
    call cho_main("But what am I supposed to do once he catches sight of it?","open","narrow","base","mid")
    m "Catches the sight of what?"
    call cho_main("The snitch!","annoyed","narrow","base","mid")
    m "Oh, I see..."
    call cho_main("There wouldn't be a way for me to stop him. With how determined he is,... and how fast he can be...","open","base","base","R")
    g9 "Well, lucky for you, you have me!"
    call cho_main("","annoyed","base","base","mid")
    g9 "I'm also very fast and determined!"
    m "And you just gave me a great idea."
    call cho_main("","annoyed","base","raised","mid")
    m "We'll need to distract him!"
    g4 "So you can get a hold of that Snatch before he does!"
    call cho_main("Please stop saying that, [cho_genie_name]!","angry","closed","angry","mid")
    m "Saying what?"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    call cho_main("{size=-4}\"Snatch\".{/size}","soft","narrow","angry","mid") # Small text
    g9 "*Hehehehe*{w} Now you've said it!"
    call cho_main("Could we please just talk about your plan, [cho_genie_name]?","open","narrow","angry","R")
    m "Patience, Miss Chang."
    call cho_main("Tell me!","scream","closed","angry","mid",trans="hpunch")
    call cho_main("","annoyed","narrow","angry","mid")
    g9 "May I present to you{w}, the path to our victory!"

    menu:
        "\"It's all about the ass!\"":
            $ quidditch_position = "front"
            call cho_main("Who- What?!{w} Whose ass?","soft","wide","base","mid")
            m "Yours, of course."
            call cho_main("M-my... my ass?","open","wide","raised","mid")
            g4 "Yes! With an ass as great as yours, Miss Chang, we'd be foolish not to make use of it!"
            call cho_main("Sir, please. You can't be serious!","soft","narrow","angry","mid")
            m "Oh I'm dead serious! I never belittle a great ass should I see one."

        "\"Panties are Key!\"":
            $ quidditch_position = "above"
            call cho_main("Panties? What does panties have to do with Quidditch?","soft","wide","raised","mid")
            m "Everything, girl!{w} For some they are the meaning of life!"
            call cho_main("What?!{w} Are you seriously suggesting \"this\"?{w} To win?{w} Panties?","angry","narrow","angry","mid")
            m "I was never more sure about anything in my life..."

        "\"Get intimate!\"":
            $ quidditch_position = "close"
            call cho_main("[cho_genie_name]?","soft","wide","base","mid")
            m "Get close. Show him your goods. Give him a peek..."
            m "You know, basic stuff..."
            call cho_main("Give him a peek? Of what?!","annoyed","wide","raised","mid")
            m "Your goods..."
            m "Am I not clear enough with how I word things?"
            m "You can also let him feel you up if you have to."

    call cho_main("Sir, this is just ridiculous!","scream","closed","angry","mid",trans="hpunch")
    call cho_main("I thought a highly regarded wizard of your stature would know at least something that could help us at Quidditch.","open","narrow","angry","mid")
    call cho_main("I didn't hold it against you that you seemingly know very little about the sport.","open","base","angry","R")
    m "Which I proved you wrong, but who cares..."
    call cho_main("Even with my limited time I thought it was at least worth a try.{w} But hearing your suggestions now...","angry","narrow","angry","mid")
    m "You will learn soon enough, girl."
    m "It’s very clear that to win we’ll have to go beyond normal conventional methods."
    g4 "The only way you can keep a man from fulfilling his seeked out purpose, is by confronting him with his most primal instinct!"
    call cho_main("Which would be?","annoyed","narrow","angry","mid")
    g9 "The act of procreation!"
    call cho_main("Sir, are you suggesting I should have \"sex\" with him?!","soft","wide","base","mid") # Shocked
    m "What? I never said that..."
    call cho_main("","annoyed","narrow","angry","mid")
    g9 "You have a really dirty mind, girl!"
    call cho_main("But you just said-","angry","closed","angry","mid")
    m "I merely want you to distract him with your body, during the match."
    g9 "And then, when he can't keep his eyes off you..."
    g9 "You grab that Snatch!"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    call cho_main("I'm sorry Sir, but I feel methods like those would get us nowhere!","open","closed","raised","mid")
    call cho_main("And it's very improper for a teacher to suggest such things! Not to mention right out vulgar!","open","base","angry","R")
    call cho_main("I'll be leaving now.{p=0.8}Please only call me should you decide to finally take things seriously...","soft","narrow","angry","mid")
    g9 "And you, think about using that adrett body of yours to get closer to your dreams!"
    call cho_main("*Tzzzz*","angry","closed","angry","mid")

    if daytime:
        call cho_main("Good day, Sir...","soft","narrow","angry","mid")
    else:
        call cho_main("Good night, Sir...","soft","narrow","angry","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    $ cho_training_state = "intro_2"

    call popup("You've lost the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/head_cho_2.png")

    call bld
    m "She'll get over it..."

    $ cho_mood += 9
    $ cho_busy = True

    jump main_room



# Training Intro 2.
label quidditch_training_intro_2:
    call cho_main(xpos="mid",ypos="base",trans="fade")
    m "Did you finally come to terms with my training methods?"
    call cho_main("No, Sir.","soft","closed","angry","mid")
    call cho_main("But I've simply run out of options.{w} If we want to win the cup this year, you're the only hope we have left...","open","narrow","angry","mid")
    call cho_main("I have no choice but to try your methods, Sir.","annoyed","narrow","angry","mid")
    g9 "I'm glad you came to your senses."
    call cho_main("(...)","annoyed","narrow","angry","R")
    g9 "Let's discuss tactics then, shall we!"
    call cho_main("(...)","annoyed","base","base","mid")
    m "(...)"
    m "What did I suggest last time again?"

    if quidditch_position == "front":
        call cho_main("You were raving about my bum, Sir.","open","closed","base","mid")
        g9 "That's right! Your ass!{w} Now I remember!"
        call cho_main("(...)","annoyed","narrow","angry","mid")
        call cho_main("I'm not here to deny that my behind is in great shape.{w} And I'm very proud of it!","open","closed","base","mid")
        g9 "You should be!"
        call cho_main("But, May I ask, Sir...","open","base","base","R")
        call cho_main("How exactly did you picture my \"ass\" helping us win?","annoyed","narrow","angry","mid")

    elif quidditch_position == "above":
        call cho_main("It had something to do with panties.","open","narrow","angry","mid")
        call cho_main("However, I have no clue why you would include panties in our training...","soft","narrow","base","R")
        g9 "Ah yes. Panties!{w} Now I remember!"

    elif quidditch_position == "close":
        call cho_main("You wanted me to have sex with their seeker...","angry","closed","angry","mid")
        m "I did?"
        call cho_main("You did! You ask me to get intimate with him!","soft","narrow","angry","mid")
        g9 "Yes, now I remember!"
        m "I wanted you to stay close to him."
        m "Let him cup a feel once or twice..."
        call cho_main("And that's going to help us how exactly?","soft","narrow","raised","mid")

    m "I will show you."
    call cho_main("","base","base","base","mid")

    call popup("You've re-gained the ability to train Cho in Quidditch!", "Congratulations!", "interface/icons/head/head_cho_1.png")
    pause 1

    m "First, get your flying thing ready!"
    call cho_main("My broom?","soft","base","raised","mid")
    m "Broom,... flying carpet,... Whichever you prefer."
    call cho_main("Only brooms are allowed in Quidditch, sir.","annoyed","base","base","mid")
    m "Good for you."
    m "And put on your Quidditch outfit while you're at it..."
    m "I suspect we'll need to do some adjustments to it."
    call cho_main("Yes, Sir.{w} Let me just go and get all of my equipment.","smile","base","base","mid")
    call cho_main("I'll be right back.","base","narrow","base","mid")

    call cho_walk(action="leave", speed=2)

    call blkfade
    pause.8

    # Scene Setup
    show screen chair_left
    show screen desk
    call update_gen_chibi # Reset Chibi.
    call gen_chibi("stand","desk","base")

    $ cho_outfit_last.save()
    $ cho_class.equip(cho_outfit_quidditch) # Equip quidditch set

    call hide_blkfade
    pause.8

    call cho_walk(action="enter", xpos="mid", ypos="base", speed=2)
    pause.5

    call cho_main("Ready when you are, [cho_genie_name]!","smile","base","base","mid", xpos="right", ypos="base")
    m "(...)"

    jump demonstrate_quidditch_tactics




### Quidditch Tactics ###

label change_quidditch_tactics:
    show screen blkfade
    call hide_characters
    with d5

    $ cho_outfit_last.save()

    call cho_chibi("stand","mid","base")

    show screen chair_left
    show screen desk
    call update_gen_chibi # Reset Chibi.
    call gen_chibi("stand","desk","base")

    $ cho_class.equip(cho_outfit_quidditch) # Equip quidditch set

    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    label demonstrate_quidditch_tactics:
    call hide_characters
    call bld

    $ menu_y = 0.8

    if cho_chibi_animation == "fly":
        menu:
            m "(What directions should I give her?)"
            "\"It's all about the ass!\"" if quidditch_position != "front":
                call demonstrate_tactic("front")
            "\"It's all about the ass!\" {size=-6}(selected){/size}" if quidditch_position == "front":
                pass

            "\"Panties are Key!\"" if quidditch_position != "above":
                call demonstrate_tactic("above")
            "\"Panties are Key!\" {size=-6}(selected){/size}" if quidditch_position == "above":
                pass

            "\"Get intimate!\"" if quidditch_position != "close":
                call demonstrate_tactic("close")
            "\"Get intimate!\" {size=-6}(selected){/size}" if quidditch_position == "close":
                pass
            "":
                pass
            "\"Come back down.\"":
                call cho_walk("mid", "base", 1.2)
                pause.2

                call cho_chibi("reset","mid","base", flip=False)
                with d5

                jump demonstrate_quidditch_tactics

        jump demonstrate_quidditch_tactics

    else:
        menu:
            "-Change Tactic-":
                m "Start flying, [cho_name]."
                call cho_main("Yes, Sir!","open","closed","angry","mid", ypos="head")
                hide screen bld1
                with d3
                pause.2

                call cho_chibi(action="fly", xpos="550", ypos="260")
                with d5
                pause.8

            "-Customize quidditch outfit-":
                call cho_main(face="neutral", xpos="mid", ypos="base")
                call t_wardrobe_quidditch() # Open quidditch wardrobe
                $ cho_class.equip(cho_outfit_quidditch)
                call cho_main(face="neutral", xpos="mid", ypos="base")

            "-Start Practice Match-" if daytime and huffl_matches_won < 2 and not lock_cho_practice:
                # Cho continues to wear her Quidditch outfit.
                # No clothing reset until after the eventing.
                jump start_training_match

            "{color=#858585}-Start Practice Match-{/color}" if (not daytime or lock_cho_practice) and not cho_content_complete:
                if not daytime:
                    call nar(">You can only do that during the day.")
                else:
                    call nar(">You can't do that right now.")

            "-Go Back-":
                call cho_main("Very well, [cho_genie_name].","open","base","base","mid", ypos="head")

                hide screen cho_chang
                show screen blkfade
                with d3

                $ cho_class.equip(cho_outfit_last)

                call cho_chibi("stand","mid","base")
                call gen_chibi("sit_behind_desk")

                call reset_menu_position

                hide screen blkfade
                call cho_main(face="happy", xpos="base", ypos="base", trans="fade")
                jump cho_requests

        jump demonstrate_quidditch_tactics



label demonstrate_tactic(position=""):

    # The *ASS* position!
    if position == "front":
        m "Now turn away from me."
        call cho_walk(xpos=580, ypos=220, speed=0.5)

        call cho_main("Like this?","soft","base","base","R", ypos="head")
        m "A bit higher maybe..."

        call cho_walk(xpos=600, ypos=150, speed=0.3)

        call bld
        m "Yes, very good. Keep that position."

        if cho_quidditch_coat == True:
            m "(It's going to be problematic getting a good view of her ass while she has that coat on...)"
            m "(Maybe I can get her to remove it...)"
        elif cho_quidditch_bottom in ["skirt_short","skirt_long"]:
            m "(This might work!)"
            m "(Although, her skirt doesn't really emphasize her ass enough...)"
            m "(Maybe there is a better option for this position...)"
        else:
            m "(This might work!)"
            g4 "(Without the coat, and in those lovingly tight pants, her ass is right on display! Like a delicious piece of ham!)"
            m "(If she keeps this hight and position, there is no way their seeker can keep his eyes away from her...)"
            m "(Unless he isn't into asses...)"

    # The ~Panties~ position!
    elif position == "above":
        m "Now move a bit higher."

        call cho_walk(xpos=550, ypos=200, speed=0.3)

        call cho_main("Like this?","soft","base","base","downR", ypos="head")
        with hpunch
        g4 "Higher!"
        g4 "Fly right above my head!"

        if cho_quidditch_bottom in ["skirt_short","skirt_long"]:
            call cho_main("But then you could see under my skirt, [cho_genie_name]!","open","base","base","downR", ypos="head")
            g4 "Which is what we are going for, [cho_name]!"
            g4 "Maximum distraction!{w} Now show me those panties!"
            call cho_main("(...)","annoyed","narrow","angry","downR", ypos="head")
        else:
            call cho_main("Of course, [cho_genie_name]...","base","base","base","downR", ypos="head")

        call cho_walk(xpos=500, ypos=100, speed=0.5)

        call cho_main("How is this?","open","base","base","down", ypos="head")

        # Genie looks up.
        call gen_chibi("hide")
        $ gen_chibi_stand = "characters/genie/chibis/standing.png"
        call gen_chibi("stand","desk","base")
        show screen bld1
        with d3

        if cho_quidditch_bottom in ["skirt_short","skirt_long"]:
            g4 "Yes, fantastic!"
            g9 "You have very cute panties, girl!"
            call cho_main("*Uhm*...{w} Thank you, [cho_genie_name].","annoyed","base","base","down", ypos="head")
            m "(I have created the ultimate up-skirt!)"
            m "(Nothing can stop us now...)"
        else:
            m "(...)"
            g4 "(You would never be able to see her panties while she's wearing those pants... Such a tragedy!)"

        call update_gen_chibi
        call gen_chibi("stand","desk","base")
        show screen bld1
        with d3

    # The [intimate] position!
    elif position == "close":
        m "Come as close to me as you can..."
        call cho_main("Yes, [cho_genie_name].","soft","base","base","R", ypos="head")

        call cho_walk(xpos=450, ypos=240, speed=0.5)

        call cho_main("How's this? Too close?","soft","wink","raised","mid", ypos="head")
        m "No! It's the perfect distance!"
        m "He should even be able to smell you if you are this close!"
        call cho_main("I hope not!","quiver","closed","sad","mid", ypos="head")
        g9 "Why? You smell lovely, girl!"
        call cho_main("*Uhm*...{w} Thank you, Sir.","soft","base","sad","mid", ypos="head")


    $ quidditch_position = position

    return

    #m "I think we'll need to change our angle of attack..."
    #call cho_main("Our angle?","annoyed","wink","raised","mid")
    #m "At the moment panty shot that all the boys are hoping for can only be seen from underneath-"
    #m "-so as a result, most of the boys are hounding you to get a look."
    #m "But if we widen our angle of attack, they won't be forced to chase you to get a look..."
    #call cho_main("Widen our angle? What do you mean?","pout","wink","raised","mid")

    #m "Should we talk strategy for the next game?"
    #m "I can't help but notice your robe stayed on this game..."
    #call cho_main("I'm lucky I kept it on! Can you imagine what Hermione would have said otherwise?","open","closed","raised","mid")
    #g9 "Mmmm, I'm picturing it now..."
    #call cho_main("Professor!","quiver","shocked","raised","mid")
