
# Astoria chitchats

label astoria_chit_chat:
    $ chitchated_with_astoria = True

    $ renpy.dynamic("chitchat_choices", "chitchat_number")
    $ chitchat_choices = set(range(1, 15))
    $ chitchat_number = None

    # Prioritise chitchats tied to current story progression

    if ag_st_imperio.counter == 1:
        $ chitchat_choices.add(16)
        $ chitchat_number = 16

    if ag_st_imperio.counter == 2:
        $ chitchat_choices.add(17)
        $ chitchat_number = 17

    if ag_st_imperio.counter == 3:
        $ chitchat_choices.add(18)
        $ chitchat_number = 18

    if ag_st_imperio.counter == 4:
        $ chitchat_choices.add(19)
        $ chitchat_number = 19
    
    if ag_se_imperio_sb.counter >= 1:
        $ chitchat_choices.add(20)
        $ chitchat_number = 20

    # Select random chitchat unless one has been prioritised
    if chitchat_number is None or chitchat_number in astoria_chitchats_seen:
        $ chitchat_number = renpy.random.choice(list(chitchat_choices))

    $ astoria_chitchats_seen.add(chitchat_number)

    if chitchat_number == 1:
        ast "Why do we have to do potions with the Gryffindors?"
        ast "They have no talent whatsoever, they might as well be Hufflepuffs."
        ast "You can clearly tell none of them has brewed a Draught of Living Death before."

    elif chitchat_number == 2:
        ast "Why do we even have muggle studies at Hogwarts?"
        ast "One of my classmates was forced to take it by her parents, and she's one of the few Slytherins in our year taking it."
        ast "It's one of the few classes my parents aren't making me take."

    elif chitchat_number == 3:
        ast "Divination is one of the worst subjects at this school."
        ast "We literally sat the entire lesson yesterday staring a tea leaves."
        ast "Although that wasn't the worst bit. It was that I had to drink the tea without any sugar whatsoever."

    elif chitchat_number == 4:
        ast "Why can't we learn something more useful, like how to make stink pellets or Dung bombs?"
        ast "When am I ever going to use something as stupid as a Hiccoughing Potion!?"
        ast "*Hick*...{w=0.8}...{w=0.8} *Hick!*{w=0.6} Damnit..."

    elif chitchat_number == 5:
        ast "I found the perfect use for the Wingardium leviosa charm today..."
        ast "Granger was being especially annoying, prancing around one of the corridors, so I used it to lift her skirt up!"
        ast "But she didn't even see that I did it! she just punched that Weasley boy on the arm."
        ast "Snap-.. {i}Professor{/i} Snape saw it though. I thought I was in trouble for a moment, but he just corrected me on my pronunciation."

    elif chitchat_number == 6:
        ast "I've still not been able to cast spells properly without saying the words."
        ast "Some bullshit about focus..."

    elif chitchat_number == 7:
        ast "When are we going to learn the Serpensortia spell?"
        ast "I already asked Professor McGonagall, but she didn't want to teach it to us for some reason..."

    elif chitchat_number == 8:
        ast "I used a switching spell to swap one of the female Hufflepuff student clothes with one of the Gryffindor boys."
        ast "You should've seen the confusion and horror on their faces..."

    elif chitchat_number == 9:
        ast "I just came back with a great haul from the last Hogsmeade trip."
        ast "My best purchase was probably the nose biting tea-cup I bought at Zonko's."

    elif chitchat_number == 10:
        ast "Could you give me access to the restricted section of the library?"
        ast "Miss Pince says I need a note from a teacher to have her fetch a book and that I'm not allowed to actually go in there..."

    elif chitchat_number == 11:
        ast "Rules are meant to be broken. We break the laws of physics all the time so how come most teachers are so strict?"

    elif chitchat_number == 12:
        ast "I was bored during class and doodled a bit on one of the books I brought from the library and it started smacking me on the head."
        ast "Why is Miss Pince allowed to jinx books when I get in trouble for making somebody's quill to turn onto a worm when touched?"

    elif chitchat_number == 13:
        ast "Flying is probably one of my favourite subjects..."
        ast "But some of the fun was taken out of it once the other students stopped smashing into things."

    elif chitchat_number == 14:
        ast "History of magic is so dull. Who wants to sit in front of a literal ghost and listen to boring facts for hours on end?"
        ast "I can't wait to drop the subject once I finish my {i}O.W.L.{/i}s."

    elif chitchat_number == 15:
        ast "Professor Snape always seem to look at me whenever something goes wrong during his class... as if it's always going to be me who did it."
        ast "I mean, I might have but you can't prove anything..."

    # Chit-chats tied story progression

    elif chitchat_number == 16:
        ast "Tonks keeps telling me these stupid things about temper and focus."
        ast "Why can't this stupid curse just work like it should!?"
        ast "Stupid...{w=0.5} Cursed...{w=0.5} {size=+5}CURSE!{/size}"

    elif chitchat_number == 17:
        ast "I've heard about some students having private tutoring from other teachers..."
        ast "When Professor Tonks asked me to let her tutor me I didn't think it was going to be so...{w=0.5} hands on..."

    elif chitchat_number == 18:
        ast "This spell training thing is so easy, Tonks doesn't seem to be able to resist me at all."
        ast "I can't wait for another go at it!"

    elif chitchat_number == 19:
        ast "How come you constantly have me use imperio to make Tonks take her clothes off?"
        ast "Let's have her do something more fun like...{w=0.4} Uhm...{w=0.4} bark like a dog or...{w=0.4} step on a lego brick."

    elif chitchat_number == 20:
        ast "Susan is such a dumb cow."
        ast "I can't believe that she's as gullible as she is."
        ast "Well, I guess that's what you'd expect from a Hufflepuff."

    return
