

# Susan chitchats

label susan_chit_chat:
    $ chitchated_with_susan = True

    $ renpy.dynamic("chitchat_choices")
    $ chitchat_choices = set(range(1, 15))

    # Locked chitchats can be removed from chitchat_choices

    $ random_number = renpy.random.choice(list(chitchat_choices))

    if random_number == 1:
        call sus_main("My favourite subject is Herbology...","open", "base", "base", "mid")
        call sus_main("But when we're working in groups the other students usually talk over me...", "base", "closed", "worried", "mid")

    elif random_number == 2:
        call sus_main("The Hufflepuff house entrance is hidden in the kitchen corridor.", "open", "base", "base", "mid")
        call sus_main("Even though we're so close, I've only seen a house elf once.", "upset", "base", "base", "R")

    elif random_number == 3:
        call sus_main("Care for magical creatures is a bit scary sometimes...", "open", "base", "worried", "mid")
        call sus_main("When we were taught how to properly approach Hippogriffs, I was shaking the entire time.", "upset", "base", "worried", "R")
        call sus_main("After bowing and letting it approach me, I only pet it a couple of times. I wouldn't dare to ride the thing.", "open", "base", "worried", "mid")

    elif random_number == 4:
        call sus_main("Sir, could you... Could you please tell professor Snape not to...", "open", "base", "worried", "mid")
        call sus_main("Never mind...", "upset", "base", "worried", "down")

    elif random_number == 5:
        call sus_main("Does flying have to be mandatory?", "open", "base", "worried", "mid")
        call sus_main("Surely only a piece of wood between you, and falling from the sky can't be safe...", "upset", "base", "worried", "down")

    elif random_number == 6:
        call sus_main("Madame Hooch was keeping a close eye on me during the last flying lesson.", "open", "base", "base", "down")
        call sus_main("I hope I'm not disappointing her too much...", "upset", "base", "base", "R")

    elif random_number == 7:
        call sus_main("Madame Pomfrey once prescribed me a \"Draught of peace\" to drink the night before exams so I could get some sleep.", "open", "base", "base", "mid")
        call sus_main("But even with her prescription, Snape wouldn't give one to me.", "upset", "base", "base", "R")

    elif random_number == 8:
        call sus_main("Why does everyone assume I'm a Weasley just because I've got red hair?", "upset", "base", "base", "mid")
        call sus_main("Some Slytherin boys keep mocking... even though I'm clearly wearing Hufflepuff robes.", "open", "base", "worried", "down")

    elif random_number == 9:
        call sus_main("I used to be scared of ghosts before I got to Hogwarts, but the \"Fat Friar\" is so nice it's hard to stay scared of them.", "grin", "base", "base", "mid")
        call sus_main("Poltergeists on the other hand...", "open", "base", "angry", "mid")

    elif random_number == 10:
        call sus_main("The \"Defence against the dark arts\" lesson when we had to confront a Boggart was one of my worst days here...", "upset", "base", "worried", "down")
        call sus_main("Professor Tonks had me stay behind after class to make sure I was okay.", "base", "base", "worried", "R")
        call sus_main("Once I got back to my dorm, some of the other students were whistling at me for some reason...", "open", "base", "worried", "R")

    elif random_number == 11:
        call sus_main("Whilst most students go home during winter break, I usually stay at Hogwarts.", "open", "base", "base", "R")
        call sus_main("The castle is a lot quieter than usual, but I don't really mind.", "base", "base", "base", "mid")

    elif random_number == 12:
        call sus_main("How come Professor Snape is allowed to ask us to gather ingredients in the forbidden forest?", "upset", "base", "worried", "mid")
        call sus_main("The students that didn't go got a bad grade and the ones that did got detention...", "open", "base", "worried", "mid")
        call sus_main("How is that fair?", "upset", "base", "base", "down")

    elif random_number == 13:
        call sus_main("I think my school robes must've shrunk in the wash.", "upset", "base", "base", "down")
        call sus_main("They're a lot tighter than when I bought them...", "open", "base", "base", "down")

    elif random_number == 14:
        call sus_main("Just because the Hufflepuff house is next to the kitchen, doesn't mean we can get food whenever we like.", "open", "base", "base", "mid")
        call sus_main("So why does the Slytherin students keep asking me to show where I hide my melons?", "upset", "base", "base", "R")

    elif random_number == 15:
        call sus_main("Why do people seem to find my surname so funny?", "open", "base", "angry", "R")
        call sus_main("I mean, I guess it's a bit unusual...", "upset", "base", "base", "mid")

    return
