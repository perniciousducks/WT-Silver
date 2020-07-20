
# Susan chitchats

default chitchat_number = 1 # temp for posing

label susan_chit_chat:
    $ chitchated_with_susan = True

    $ renpy.dynamic("chitchat_choices")
    $ chitchat_choices = set(range(1, 15))

    # Locked chitchats can be removed from chitchat_choices

    # $ random_number = renpy.random.choice(list(chitchat_choices))
    $ random_number = chitchat_number

    if random_number == 1:
        sus "My favourite subject is Herbology..."
        sus "But we're often paired into groups and the other students often talk over me..."

    elif random_number == 2:
        sus "The Hufflepuff house entrance is hidden in the kitchen corridor."
        sus "Even though we're so close, I've only seen a house elf once."

    elif random_number == 3:
        sus "Care for magical creatures is a bit scary sometimes..."
        sus "When we were taught how to properly approach Hippogriffs, I was shaking the entire time."
        sus "After bowing and letting it approach me, I only pet it a couple of times. I wouldn't dare to ride the thing."

    elif random_number == 4:
        sus "Sir, could you... Could you please tell professor Snape not to..."
        sus "Never mind..."

    elif random_number == 5:
        sus "Does flying have to be mandatory?"
        sus "Surely only a piece of wood between you, and falling from the sky can't be safe..."

    elif random_number == 6:
        sus "Madame Hooch was keeping a close eye on me during the last flying lesson."
        sus "I hope I'm not disappointing her too much..."

    elif random_number == 7:
        sus "Madame Pomfrey once prescribed me a \"Draught of peace\" to drink the night before exams so I could get some sleep."
        sus "But even with her prescription, Snape wouldn't give one to me."

    elif random_number == 8:
        sus "Why does everyone assume I'm a Weasley just because I've got red hair?"
        sus "Some Slytherin boys keep mocking me about it... even though I wear Hufflepuff robes."

    elif random_number == 9:
        sus "I used to be scared of ghosts before I got to Hogwarts, but the \"Fat Friar\" is so nice it's hard to stay scared of them."
        sus "Poltergeists on the other hand..."

    elif random_number == 10:
        sus "The \"Defence against the dark arts\" lesson when had to confront a Boggart was one of my worst days here..."
        sus "Tonks did keep me for a little while after class to make sure I was okay."
        sus "Once I got back to my dorm, some of the other students were whistling at me for some reason..."

    elif random_number == 11:
        sus "Whilst most students go home during winter break, I usually stay at Hogwarts."
        sus "The castle is a lot quieter than usual, but I don't really mind."

    elif random_number == 12:
        sus "How come Snape is allowed to ask us to gather ingredients in the forbidden forest?"
        sus "The students that didn't go got a bad grade and the ones that did got detention..."
        sus "How is that fair?"

    elif random_number == 13:
        sus "I think my school robes must've shrunk in the wash."
        sus "They're a lot tighter than when I bought them..."

    elif random_number == 14:
        sus "Just because Hufflepuff house is next to the kitchen, doesn't mean we can get food whenever we like."
        sus "Some Slytherin students keeps asking me to show where I hide my melons..." # ;)

    elif random_number == 15:
        sus "Why do people seem to find my surname so funny?"
        sus "I mean, I guess it's a bit unusual..."

    return
