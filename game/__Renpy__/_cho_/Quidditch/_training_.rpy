

### Cho Quidditch Training ###

label cho_training_menu:

    # Quiz.
    if not cho_training_unlocked:
        jump cho_quiz_1

    # Training Intro.
    if cho_training_unlocked and not cho_training_intro_complete:
        $ cho_training_intro_complete = True
        call quidditch_training_intro

    menu:
        "-Change Tactics-":
            jump change_quidditch_tactics

        "-Change outfit-":
            jump change_quidditch_outfit

        "-Quidditch Commentator-" if quidditch_commentator == "Hermione would like to":
            $ lock_cho_practice = False
            $ quidditch_commentator = "Hermione"
            jump quidditch_commentator_event_3

        "-Go back-":
            jump cho_requests


label quidditch_training_intro:
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

    cho "Yes, Sir."
    g4 "Let's start with your \"Quiddesh\" training!"
    cho "\"Quidditch\", Sir."
    g4 "Let's start with your \"Quidditch\" training, [cho_name]."
    cho "!!!" # Happy

    return



### Quidditch Tactics ###

label change_quidditch_tactics:

    # Intro
    if not cho_tactics_intro_done:
        m "How about we discuss some tactics."
        cho "That sounds grat, [cho_genie_name]! Shall I call the rest of my team up here?"
        m "What? Why?"
        cho "So they can hear your expertise as well, of course."
        m "I don't think that will be necessary."


    else:
        pass


    menu:
        "-Fly in front the enemy seeker-":
            $ quidditch_position = "front"
        "-Fly above the enemy seeker-":
            $ quidditch_position = "above"
        "-Fly close to the enemy seeker-":
            $ quidditch_position = "close"
        "-Go back-":
            jump cho_training_menu

    jump cho_training_menu

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
