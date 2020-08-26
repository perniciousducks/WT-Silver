
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
        call ast_main("Why do we have to do potions with the Gryffindors?", "base", "narrow", "worried", "R")
        call ast_main("They have no talent whatsoever, they might as well be Hufflepuffs.", "annoyed", "narrow", "base", "mid")
        call ast_main("You can clearly tell none of them has brewed a Draught of Living Death before.", "annoyed", "base", "base", "mid")

    elif chitchat_number == 2:
        call ast_main("Why do we even have muggle studies at Hogwarts?", "open", "narrow", "angry", "L")
        call ast_main("One of my classmates was forced to take it by her parents, and she's one of the few Slytherins in our year taking it.", "annoyed", "base", "base", "L")
        call ast_main("It's one of the few classes my parents aren't making me take.", "open", "closed", "base", "mid")

    elif chitchat_number == 3:
        call ast_main("Divination is one of the worst subjects at this school.", "open", "narrow", "base", "mid")
        call ast_main("We literally sat the entire lesson yesterday staring a tea leaves.", "base", "base", "angry", "R")
        call ast_main("Although that wasn't the worst bit. It was that I had to drink the tea without any sugar whatsoever.", "clench", "base", "base", "mid")

    elif chitchat_number == 4:
        call ast_main("Why can't we learn something more useful, like how to make stink pellets or Dung bombs?", "upset", "narrow", "base", "R")
        call ast_main("When am I ever going to use something as stupid as a Hiccoughing Potion!?", "annoyed", "base", "base", "mid")
        call ast_main("*Hick*...{w=0.8}...{w=0.8} *Hick!*{w=0.6} Damnit...", "open", "narrow", "worried", "down")

    elif chitchat_number == 5:
        call ast_main("I found the perfect use for the Wingardium leviosa charm today...", "smile", "base", "base", "mid")
        call ast_main("Granger was being especially annoying, prancing around one of the corridors, so I used it to lift her skirt up!", "open", "base", "angry", "down")
        call ast_main("But she didn't even see that I did it! she just punched that Weasley boy on the arm.", "angry", "narrow", "base", "down", cheeks="blush")
        call ast_main("Snap-- {i}Professor{/i} Snape saw it though. I thought I was in trouble for a moment, but he just corrected me on my pronunciation.", "grin", "narrow", "base", "mid")

    elif chitchat_number == 6:
        call ast_main("I've still not been able to cast spells properly without saying the words.", "open", "base", "base", "mid")
        call ast_main("Some bullshit about focus...", "base", "base", "angry", "mid")

    elif chitchat_number == 7:
        call ast_main("When are we going to learn the Serpensortia spell?", "open", "base", "worried", "mid")
        call ast_main("I already asked Professor McGonagall, but she didn't want to teach it to us for some reason...", "annoyed", "narrow", "angry", "mid")

    elif chitchat_number == 8:
        call ast_main("I used a switching spell to swap one of the female Hufflepuff student clothes with one of the Gryffindor boys.", "smile", "base", "angry", "mid")
        call ast_main("You should've seen the confusion and horror on their faces...", "grin", "narrow", "base", "L")

    elif chitchat_number == 9:
        call ast_main("I just came back with a great haul from the last Hogsmeade trip.", "smile", "narrow", "base", "mid")
        call ast_main("My best purchase was probably the nose biting tea-cup I bought at Zonko's.", "smile", "base", "base", "mid")

    elif chitchat_number == 10:
        call ast_main("Could you give me access to the restricted section of the library?", "open", "base", "base", "mid")
        call ast_main("Miss Pince says I need a note from a teacher to have her fetch a book and that I'm not allowed to actually go in there...", "annoyed", "base", "base", "mid")

    elif chitchat_number == 11:
        call ast_main("Rules are meant to be broken. We break the laws of physics all the time so how come most teachers are so strict?", "annoyed", "base", "angry", "mid")

    elif chitchat_number == 12:
        call ast_main("I was bored during class and doodled a bit on one of the books I brought from the library and it started smacking me on the head.", "upset", "narrow", "angry", "mid")
        call ast_main("Why is Miss Pince allowed to jinx books when I get in trouble for making somebody's quill turn into a worm when touched?","base","base","base","mid")

    elif chitchat_number == 13:
        call ast_main("Flying is probably one of my favourite subjects...", "open", "base", "base", "mid")
        call ast_main("But some of the fun was taken out of it once the other students stopped smashing into things.", "annoyed", "base", "base", "R")

    elif chitchat_number == 14:
        call ast_main("History of magic is so dull. Who wants to sit in front of a literal ghost and listen to boring facts for hours on end?", "clench", "closed", "base", "mid")
        call ast_main("I can't wait to drop the subject once I finish my {i}O.W.L.{/i}s.", "base", "narrow", "base", "down")

    elif chitchat_number == 15:
        call ast_main("Professor Snape always seem to look at me whenever something goes wrong during his class... as if it's always going to be me who did it.", "annoyed", "narrow", "angry", "R")
        call ast_main("I mean, I might have but you can't prove anything...", "upset", "narrow", "base", "down")

    # Chit-chats tied story progression

    elif chitchat_number == 16:
        call ast_main("Tonks keeps telling me these stupid things about temper and focus.", "clench", "base", "base", "down")
        call ast_main("Why can't this stupid curse just work like it should!?", "open", "base", "angry", "mid")
        call ast_main("Stupid...{w=0.5} Cursed...{w=0.5} {size=+5}CURSE!{/size}", "angry", "narrow", "angry", "down")

    elif chitchat_number == 17:
        call ast_main("I've heard about some students taking private tutoring from other teachers...", "open", "base", "base", "mid")
        call ast_main("When Professor Tonks asked me to let her tutor me I didn't think it was going to be so...{w=0.5} hands on...", "annoyed", "narrow", "angry", "R")

    elif chitchat_number == 18:
        call ast_main("This spell training thing is so easy, Tonks doesn't seem to be able to resist me at all.", "smile", "narrow", "base", "R")
        call ast_main("I can't wait for another go at it!", "open", "narrow", "base", "down")

    elif chitchat_number == 19:
        call ast_main("How come you constantly have me use imperio to make Tonks take her clothes off?", "annoyed", "narrow", "worried", "mid")
        call ast_main("Let's have her do something more fun like...{w=0.4} *uhm*...{w=0.4} bark like a dog or...{w=0.4} step on a lego brick.", "horny", "base", "base", "down")

    elif chitchat_number == 20:
        call ast_main("Susan is such a dumb cow.", "clench", "base", "base", "mid")
        call ast_main("I can't believe that she's as gullible as she is.", "angry", "closed", "base", "mid")
        call ast_main("Well, I guess that's what you'd expect from a Hufflepuff.", "base", "base", "base", "down")

    return
