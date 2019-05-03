

### Tier 2 (pre Slytherin) ###

label cho_panties_response_T2:
    $ has_cho_panties = False
    call cho_main("Hello, [cho_genie_name]", xpos="mid", ypos="base")
    m "Sup..."
    cho "*Uhm*..."
    cho "I forgot to take my underwear with me the last time I was here."

    if cho_panties_soaked:
        g9 "Your panties! Of course, [cho_name]!{w} I've got them right here..."
        call cho_walk("desk","base", speed=2)
        pause.8

        cho "(...)" # Evil stare.
        m "What?"
        cho "(...)"
        m "Anything wrong?"
        cho "They are covered in semen."
        m "What was that?"
        cho "Semen, Sir!" # Scream
        g4 "You are correct!{w} They are indeed covered in a thick load of filthy, nasty reeking semen!"
        g4 "Who could have done this?!"
        cho "I don't know... why don't we inquire how they got here in the first place..."
        cho "Didn't I take off my panties while I was stipping for you?"
        m "That is correct."
        cho "And you had my panties this whole time?"
        m "Yup."
        cho "And you just gave them back to me covered in cum..."
        m "That makes sense to me..."
        cho "So you admit that you did it?"
        m "It's not my cum..."
        cho "*Argh!*"
        cho "Well who's cum is it then? The house-elfes?"
        m "*Uhm*...{w} Yes?"
        cho "It's disgusting!"
        cho "I better get them cleaned immediately..."

        call cho_walk("door","base", speed=3)

        call bld
        m "Where are you going?"

        call cho_chibi(action="leave")

        call bld
        m "(...)"

        $ cho_mood += 6
        $ cho_busy = True

        $ cho_panties_soaked = False

        $ achievement.unlock("pantiesfapcho")

        jump main_room

    else:
        g9 "Your panties, that's right!{w} I've got them right here..."
        call nar(">You take the panties to your nose and give them one last sniff.")
        g4 "*Aaahhh!*{w} Wonderful!"
        cho "(...)"
        m "There, take them..."

        call cho_walk("desk","base", speed=2)
        pause.8

        call cho_walk("mid","base", speed=2)
        call cho_chibi("stand","mid","base")
        with d3
        pause.2

        cho "Thank you, Sir."
        m "You're welcome..."

        jump cho_requests
