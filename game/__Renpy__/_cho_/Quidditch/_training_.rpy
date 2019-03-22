

### Cho Quidditch Training ###

label quiz_intro:

    return



label quidditch_quiz:

    return

label quidditch_quiz_outro:
    call nar("You are supposed to do and beat a quiz about you Quidditch knowledge here. Not yet added if you see this message.")

    cho "I have to say Sir, I'm impressed!"
    cho "You have proven that you know a great deal about Quidditch."
    m "So you will let me train you?"
    cho "I suppose..."
    g9 "(Fuck yeah, here we go!)" # Small text.
    cho "And I will stay true to my word that I will sell you favours for...{w} Wins..."
    g4 "(Hell yes!)"
    cho "But keep it civil. I won't do anything those Slytherin skanks do!"
    m "(Aaaaaa-nd she's ruined the mood...)"
    cho "And should you not be able to help me and my team beat Hufflepuff, this will be over before you can even say Snitch!"
    m "..."

    cho "I got to go now, [cho_genie_name] or I'll be too late for classes."
    cho "Please ask me again about our training tomorrow morning. I'll be ready."
    m "Oh you have no idea, girl..." # Small text.
    cho "Until then, [cho_genie_name]."
    m "I'm looking forward to it."

    # Cho leaves
    call cho_walk("mid","leave",2.5)

    $ cho_busy = True

    jump main_room



### Quidditch Training ###

label cho_training_menu:

    # Quiz.
    # ADD Quiz here!
    if not cho_training_unlocked:
        $ cho_training_unlocked = True
        jump quidditch_quiz_outro

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
    # Replace this menu with a proper wardrobe panel.
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
