

### Cho Quidditch Training ###

label cho_training_menu:

    # Quiz.
    if cho_training_state in ["quiz_start","quiz_part_1","quiz_part_2"]:
        # Gets changed to "intro_1" once the quiz is beaten.
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
        call quidditch_training_intro_2

    jump change_quidditch_tactics



# Training Intro 1.
label quidditch_training_intro_1:
    # Genie should get into a drill sargeant mood here.
    call cho_main(xpos="mid",ypos="base",trans="fade")

    m "Are you ready for your first training session?"
    cho "Of course, Professor!"
    g4 "Professor? Who are you calling Professor, girl?"
    cho "I'm sorry?"
    m "From now on you will address me only as Sir, or..."

    menu:
        "\"Coach\"":
            $ cho_genie_name = "Coach"
        "\"Sergeant\"":
            $ cho_genie_name = "Sergeant"
        "\"Captain\"":
            $ cho_genie_name = "Captain"

    cho "Yes, [cho_genie_name]."
    m "And you I will call..."

    menu:
        "\"Cadet\"":
            $ cho_name = "Cadet"
        "\"Pilot\"":
            $ cho_name = "Pilot"
        "\"Maggot\"":
            $ cho_name = "Maggot"
            cho "(...)" # Annoyed look to the left.
        "\"Eagle #1\"":
            $ cho_name = "Eagle #1"
        "\"Eagle #2\"":
            $ cho_name = "Eagle #2"

    cho "Yes, Sir."
    g4 "Let's start with your \"Quiddesh\" training!"
    cho "\"Quidditch\", Sir."
    g4 "Let's start with your \"Quidditch\" training, [cho_name]."
    cho "!!!" # Happy
    cho "Shall I call the rest of my team up here?"
    m "What? Why?"
    cho "So they can hear your expertise as well, of course."
    m "I don't think that will be necessary."
    m "Let's focus on you, for the moment..."
    cho "Very well, [cho_genie_name]."
    m "How did you usually play? Why were you always losing?"
    cho "Well, Hufflepuff has a really good seeker."
    cho "He's always catching the snitch before me."
    cho "I don't know how he does it, to be honest. It always happens so quick..."
    m "And you are both looking for that thing? At the same time?"
    cho "Yes, [cho_genie_name]."
    cho "I do my best flying around the pitch searching for it. But it's just so small and really tricky to see."
    m "Why don't you look for it together? After all there is only one."
    m "You just need to grab that Snatch before he does."
    cho "[cho_genie_name]! It's \"Snitch\"!"
    m "Potato potato..."
    cho "You just said the same thing twice..."
    m "Exactly..."
    cho "..."
    cho "But what am I supposed to do once he catches sight of it?"
    m "catches the sight of what?"
    cho "The snitch!"
    m "Oh, I see..."
    cho "There wouldn't be a way for me to stop him. With how determined he is,... and how fast he can be..."
    g9 "Well, lucky for you, you have me!"
    m "And you just gave me a great idea."
    m "We'll need to distract him. So you can get a hold of that Snatch before he does!"
    cho "Please stop saying that, [cho_genie_name]!"
    m "Saying what?"
    cho "(...)"
    cho "\"Snatch\"." # Small text
    g9 "Hehehe- Now you've said it!"
    cho "Could we please just talk about your plan, [cho_genie_name]?"
    m "Patience, Miss Chang."
    cho "Tell me!"
    g9 "May I present to you{w}, the goal to our victory!"

    menu:
        "\"It's all about the ass!\"":
            $ quidditch_position = "front"
            cho "Who- What?! Whose ass?"
            m "Yours, of course."
            cho "M-my... my ass?"
            g4 "Yes! With an ass as great as yours, Miss Chang, we'd be foolish not to make use of it!"
            cho "Sir, please. You can't be serious!"
            m "Oh I'm dead serious! I never belittle a great ass should I see one."

        "\"Panties are Key!\"":
            $ quidditch_position = "above"
            cho "Panties? What does panties have to do with Quidditch?"
            m "Everything, girl! For some they are the meaning of life!"
            cho "What? Are you seriously suggesting \"this\"? To win? Panties?"
            m "I was never more sure about anything in my life..."

        "\"Get intimate!\"":
            $ quidditch_position = "close"
            cho "[cho_genie_name]?"
            m "Get close. Show him your goods. Give him a peek..."
            m "You know, basic stuff..."
            cho "Give him a peek? Of what?!"
            m "Your goods..."
            m "Am I not clear enough with how I word things?"
            m "You can also let him feel you up if you have to."

    cho "Sir, this is just ridiculous!"
    cho "I thought a hightly regarded wizard of your stature would know at least something that could help us at Quidditch."
    cho "I didn't hold it against you that you seemingly know very little about the sport."
    m "Which I proved you wrong, but who cares..."
    cho "Even with my limited time I thought it was at least worth a try. But hearing your suggestions now..."
    m "You will learn soon enough, girl."
    m "It’s very clear that to win we’ll have to go beyond normal conventional methods."
    g4 "The only way you can keep a man from fulfilling his seeked out purpose, is by confronting him with his most primal instinct!"
    cho "Which would be?"
    g9 "The act of procreation!"
    cho "Sir, are you suggesting I should have \"sex\" with him?!" # Shocked
    m "What? I never said that..."
    g9 "You have a really dirty mind, girl!"
    cho "But you just said-"
    m "I merely want you to distract him with your body, during the match."
    g9 "And then, when he can't keep his eyes off you, you grab that Snatch!"
    cho "(...)"
    cho "I'm sorry Sir, but I feel methods like those would get us nowhere!"
    cho "And it's very improper for a teacher to suggest such things! Not to mention right out vulgar!"
    cho "I'll be leaving now. Please only call me once you've decided to take things seriously!"
    g9 "And you, think about using that adrett body of yours to win your dream!"
    cho "*Tzzzz*"

    if daytime:
        cho "Good day, Sir..."
    else:
        cho "Good night, Sir..."

    # Cho leaves.
    call cho_walk(speed=1.6, action="leave") # Updated

    $ cho_training_state = "intro_2"
    call give_reward(">You've lost the ability to train Cho in Quidditch.","interface/icons/head/head_cho_1.png")

    m "She'll get over it..."

    $ cho_mood += 9
    $ cho_busy = True

    jump main_room



# Training Intro 2.
label quidditch_training_intro_2:
    call cho_main(xpos="mid",ypos="base",trans="fade")
    m "Let's start by discussing tactics."
    m "(...)"
    m "What did I suggest last time again?"

    if quidditch_position == "front":
        cho "You were raving about my bottom, Sir."

    elif quidditch_position == "above":
        cho "It had something to do with panties."
        cho "However, I have no clue why you would include panties in our training..."
        m "Ah yes. How could I forget."

    elif quidditch_position == "close":
        pass

    m "I will show you."
    m "First, get on your flying thing..."
    cho "My broom?"

    call give_reward(">You've re-gained the ability to train Cho in Quidditch!","interface/icons/head/head_cho_1.png")

    return



### Quidditch Tactics ###

label change_quidditch_tactics:
    $ cho_flying = False
    call hide_characters
    hide screen bld1
    call cho_chibi("stand","mid","base")
    show screen chair_left
    show screen desk
    call update_gen_chibi # Reset Chibi.
    call gen_chibi("stand","desk","base")
    with fade

    $ cho_outift_last.save() # Temporarily save last worn clothes

    $ cho_class.equip(cho_outfit_quidditch) # Equip quidditch set

    label demonstrate_quidditch_tactics:

    menu:
        "\"It's all about the ass!\"":
            call demonstrate_tactic("front")

        "\"Panties are Key!\"":
            call demonstrate_tactic("above")

        "\"Get intimate!\"":
            call demonstrate_tactic("close")

        "\"Come back down.\"" if cho_flying == True:
            $ cho_flying = False
            call cho_walk("mid", "base", 1.2)
            call cho_chibi("hide")
            call flying_cho_chibi(flying=False) # Reset chibi images.
            call cho_chibi("stand","mid","base")
            with d3

            jump cho_training_menu

        "\"Customize quidditch outfit.\"" if cho_flying == False:
            call cho_main(xpos="mid",ypos="base", face="neutral")
            call t_wardrobe_quidditch() # Open quidditch wardrobe
            $ cho_class.equip(cho_outfit_quidditch)
            call cho_main(xpos="wardrobe",ypos="base", face="neutral")

        "\"That's enough.\"" if cho_flying == False:
            cho "Very well, [cho_genie_name]."
            $ cho_class.equip(cho_outift_last) # Equip last worn clothes
            call cho_chibi("stand","mid","base")
            call gen_chibi("sit_behind_desk")
            call cho_main(face="happy",xpos="base",ypos="base",trans="fade")
            jump cho_requests

    jump demonstrate_quidditch_tactics



label demonstrate_tactic(position=""):

    if not cho_flying:
        $ cho_flying = True # Demonstrating

        m "Start flying, [cho_name]."
        cho "Yes, Sir!"

        call cho_chibi("hide")
        call flying_cho_chibi(flying=True) # Change chibi images to flying.
        call cho_walk("mid", "200", 0.3)
        with d3

    # The *ASS* position!
    if position == "front":
        m "Now turn away from me."
        call cho_walk("580","200", 0.5)

        cho "Like this?"
        m "A bit higher maybe..."

        call cho_walk("600", "150", 0.3)

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

        call cho_walk("mid", "180", 0.3)

        cho "Like this?"
        with hpunch
        g4 "Higher!"
        g4 "Fly right above my head!"

        if cho_quidditch_bottom in ["skirt_short","skirt_long"]:
            cho "But then you could see under my skirt, [cho_genie_name]!"
            g4 "Which is what we are going for, [cho_name]!"
            g4 "Maximum distraction!{w} Now show me those panties!"
            cho "(...)"
        else:
            cho "Of course, [cho_genie_name]..."

        call cho_walk("mid", "100", 0.5)

        cho "How is this?"
        call gen_chibi("hide")
        $ genie_chibi_stand = "characters/genie/chibis/standing.png"
        call gen_chibi("stand","desk","base")
        with d3

        if cho_quidditch_bottom in ["skirt_short","skirt_long"]:
            g4 "Yes, fantastic!"
            g9 "You have very cure panties, girl!"
            cho "Uhm-...{w} Thank you, [cho_genie_name]."
            m "(I have created the ultimate upskirt!)"
            m "(Nothing can stop us now...)"
        else:
            m "(...)"
            g4 "(What a tragedy!{w} No matter how high up she flies, you won't be able to see them while she's wearing those...)"

    # The [intimate] position!
    elif position == "close":
        m "Come as close to me as you can..."
        cho "Yes, [cho_genie_name]."
        call cho_walk("desk", "220", 0.5)


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
