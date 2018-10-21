

#Event 1 - Cho Intro
label cho_intro:
    $ cho_known = True

    call bld
    m "Miss Granger. How would you like to earn some points today?"
    call her_main("What do I have to do?","soft","baseL",cheeks="blush")
    m "Nothing. Just stand there."
    call her_main("I don't believe you.","annoyed","angryL",cheeks="blush")
    m "Well, of course, there's more to it than that. I'm going to molest your butt a little bit as well."
    call her_main("You're not going to spank me again, are you?","annoyed","frown",cheeks="blush")
    m "You don't like it when I slap your butt?"
    call her_main("It's...it's not that. It's just that you're too loud.","annoyed","baseL")
    call her_main("What would you do if someone walked by while you...while I was 'just standing here'? They might hear.","annoyed","angryL",cheeks="blush")
    m "What? Nonsense. These walls are solid unobtanium. They'd have to be some kind of a wizard to notice anything."
    call her_main("That doesn't make any sense!","soft","wide")
    m "Do you want those points or not?"
    call her_main("Yes, please.","angry","worriedCl",cheeks="blush")

    hide screen bld1
    call her_walk("mid","desk",3, redux_pause = 2)
    call blkfade

    call her_chibi("hide")
    hide screen genie
    show screen groping_02
    pause.5

    call hide_blkfade
    call ctc

    show screen blktone
    call her_main("...","annoyed","baseL", xpos="mid",ypos="base")

    menu:
        "-Give her butt a slap-":
            pass
        "-Who are you kidding, slap that ass!-":
            pass

    call slap_her

    call her_main("[genie_name]!","open","wide")

    menu:
        "-Give her butt another slap!-":
            call slap_her

            call her_main("[genie_name]!","angry","angry",cheeks="blush")

            call slap_her

            call her_main("Not-","angry","angry",cheeks="blush")

            call slap_her

            call her_main("So-","angry","worriedCl",cheeks="blush")

            call slap_her

            call her_main("Hard!","angry","worriedCl",cheeks="blush")
            m "Did you say something, miss granger?"
            call her_main("I said, not so hard.","angry","angry",cheeks="blush",tears="down")
            call her_main("Someone might hear!","scream","angry",cheeks="blush",tears="down")
            m "Miss Granger, please. There's no need to shout."

            menu:
                "-Keep Slapping her Butt-":

                    call slap_her
                    call slap_her
                    call slap_her
                    call her_main("Professor!","scream","worriedCl",cheeks="blush",tears="messy")
                "-Soothe her tender cheeks-":
                    "You gently slide your hands up Hermione's legs, slipping your hands under her skirt."
                    call her_main("...........","angry","worried",cheeks="blush",tears="down")
                    "Your hands softly carress her skin. You can feel the heat rising from her abused cheeks."
                    call her_main("......","angry","worriedCl",cheeks="blush",tears="crying_blink")
                    "You can feel the soft goosebumps forming on the inflamed skin."
                    call her_main("Professor?","angry","worried",cheeks="blush",tears="down")
                    "You notice her breathing becoming more shallow."
                    call her_main("Can we please stop, now?","disgust","down_raised",cheeks="blush")
                    m "Doesn't that feel better?"
                    call her_main(".......Yes.","angry","worriedCl",cheeks="blush",tears="soft_blink")
                    call her_main("I mean, no.","disgust","wink",cheeks="blush",tears="soft_blink")

                    menu:
                        "-Listen to the Girl-":
                            pass
                        "-Play with Her Asshole-":
                            "You ignore Hermione and gently slide your hands under her panties."
                            "Your left hand gently pulls her cheek back, exposing the smooth, muscular ring of her asshole."
                            "You extend your middle finger, and gingerly touch the soft, smooth skin."
                            call her_main("!","scream","wide",cheeks="blush")
                            call her_main("Prof-","scream","wideL",cheeks="blush")
                            m "Shhh. Not too loud, girl. Wouldn't want to alarm anyone out in the hall."
                            "Your finger presses against the firm muscle and you begin to trace a slow circle around the ring."
                            call her_main("......","mad","wide",cheeks="blush")
                            call her_main("...","disgust","wink",cheeks="blush",tears="soft_blink")
                            "You can feel Hermione's ass start to twitch."
                            call her_main("I-I think I'm going to-","angry","worriedCl",cheeks="blush")
                            "Hermione's tight asshole opens just enough for your finger to pop inside."

        "-Give her butt a squeeze-":
            pass

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with fade
    pause.5

    $ days_since_cho = 0
    call play_sound("door")

    call update_cho_uniform

    call cho_main("Professor Dumbledore! I'm sorry for rushing in without knocking, but I finally-","upset","closed","angry","mid",xpos="base",ypos="base")

    call play_sound("scratch")
    call cho_main("","scream","wide","angry","L",trans="hpunch")
    pause.2

    hide screen groping_02
    show screen no_groping_02

    call her_main("...","angry","wide",cheeks="blush",xpos="mid",ypos="base")
    call her_main(".............","soft","ahegao",cheeks="blush")
    call cho_main("Uhm...","annoyed","wide","angry","L")

    call her_main("It's not what it looks like!","shock","worriedCl",cheeks="blush")
    call cho_main("You lying bitch!","scream","angry","angry","mid")
    call cho_main("Men's rights movement my ass!","upset","angry","angry","R")
    call her_main("...","shock","worriedCl",cheeks="blush",emote="01")
    call her_main("{size=-7}(I want to die!){/size}","disgust","down_raised",cheeks="blush")
    call her_main("He was merely massaging a pulled muscle in my...in my...leg!","open","worriedCl",cheeks="blush")
    call cho_main("Liar!","annoyed","base","angry","mid")
    call her_main("You... you...","annoyed","frown",cheeks="blush")
    call her_main("You flat-chested skank!","scream","angryL",cheeks="blush")
    call cho_main("Two-faced cow!","scream","shocked","angry","mid")
    call her_main("C student!","scream","angryL",cheeks="blush")

    menu:
        "-Tell them to shut up-":
            m "Students! By the sands! Calm yourselves! There is a perfectly reasonable explanation!"
            call her_main("...","annoyed","frown",cheeks="blush")
            call cho_main("...","annoyed","angry","angry","mid")
            call cho_main("....well?","scream","angry","angry","mid")
            m "Miss Granger was simply helping me clean my office when she pulled a muscle in her leg. It's quite painful. That's why she's so flustered."
            call cho_main("...","annoyed","shocked","angry","R")
            call cho_main("i can't believe this!","scream","shocked","angry","R")
            call play_sound("door")
            hide screen cho_chang
            with d3
            pause.5

            call her_main("You dirty old man!","scream","angryL",cheeks="blush")
            m "Now see here, young lady. Do not mistake me for some conjurer of cheap tr-"
            call slap_her

            m "Calm yourself, gir-"
            call slap_her
            call slap_her
            call slap_her

            call her_main("I'm never selling you another favor again!","angry","angry",cheeks="blush",tears="down")
            $ mad += 15

        "-Stay out of it-":
            call her_main("Nothing! Get out!","angry","worriedCl",cheeks="blush")
            call cho_main("Slut!","scream","shocked","angry","mid")
            call play_sound("door")
            hide screen cho_chang
            with d3
            pause.5

            call her_main("I can't believe that just happened.","angry","worriedCl",cheeks="blush")
            call her_main("What kind of a person just barges into the headmaster's office with out knocking!","angry","angryCl",cheeks="blush")
            call her_main("This was all your fault!","annoyed","frown",cheeks="blush")
            $ mad += 5

    show screen blkfade
    hide screen hermione_main
    hide screen bld1
    hide screen blktone
    hide screen no_groping_02
    show screen genie
    call her_chibi("stand","desk","base")
    hide screen blkfade
    with fade

    call her_walk("desk","leave",1.5,action="run")

    m "Bitches..."

    jump main_room



#Event 2 - Hermione apologizes
label hermione_cho:
    call play_sound("knocking")
    "*Knock-knock-knock!*"

    menu:
        "-Come in-":
            call play_sound("door")
            call her_chibi("stand","desk","base")
            pause.2

            call her_main("Sir, I just wanted to...","annoyed","baseL",xpos="mid",ypos="base")
            call her_main("...to...","annoyed","angryL",cheeks="blush")
            m "By the great desert sands, girl! What?!"
            call her_main("I wanted to apologize for what happened.","open","baseL",cheeks="blush")
            m "You mean with that girl earlier?"

            menu:
                "-Miss Chang-":
                    m "Miss Chang. Yes?"
                    call her_main("Yes, sir.","annoyed","baseL")
                    call her_main("She's always trying to compete with me.","open","baseL",cheeks="blush")
                    m "Well, girls being girls, you know."
                    call her_main("Yes, sir. But she takes things too far.","annoyed","baseL")
                "-Miss Chong-":
                    m "Miss Chong, was it?"
                    call her_main("Chang, sir.","annoyed","baseL")
                    m "Of course."

            call her_main("I just wanted to tell you that I...","open","baseL",cheeks="blush")
            call her_main("I explained everything to Cho.","angry","worriedCl",cheeks="blush",tears="soft_blink")
            call her_main("It was so embarassing.","angry","worriedCl",cheeks="blush")
            m "And?"
            call her_main("So everything is okay.","base","base",cheeks="blush")
            call her_main("I told her that you trading me points for cleaning your office.","base","worriedCl",cheeks="blush")
            call her_main("Pretty clever, huh?","base","glance",cheeks="blush")
            m "Yes. Very good, Miss Granger. I assume Miss..."

            menu:
                "-Miss Chang-":
                    m "I assume Miss Chang won't be any trouble, then?"
                    call her_main("Nope!","base","worriedCl",cheeks="blush")
                    m "Splendid."
                    call her_main("Well, I've got to get to class. Bye, sir.","annoyed","baseL")
                    m "Of course, Miss Granger."

                "-Miss Ching-":
                    m "I assume she won't be any trouble, then?"
                    m "Miss Ching?"
                    call her_main("Chang","open","baseL",cheeks="blush")
                    m "Chong?"
                    call her_main("Her name is Cho Chang!","annoyed","angryL",cheeks="blush")
                    m "Ching, Chong, Cho Chang?!"
                    m "That's racist!"
                    call her_main("What?","mad","wide",cheeks="blush")
                    m "Don't you have class or something?"

            hide screen hermione_main
            with d3

            #$ days_since_cho = 3
            call her_walk("desk","leave",2.5)
            $ hermione_busy = True

            jump main_room

        "-Not Now, I'm busy-":
            her "Ok, [genie_name]. I will leave you alone then..."
            $ days_without_an_event = 0
            jump main_room



#Event 3 - Cho asks for favours.
label cho_intro_2:
    call play_sound("knocking")
    "*Knock-knock-knock!*"

    menu:
        "Is that you, Miss Granger?":
            "No, it's me. Cho Chang?"
            m "Ah, Miss Chong."
            cho "Chang!"
            m "What?"
            cho "MY name is Chang, sir!"
            m "Ah, well, come in already, Miss Ching."
        "Come in.":
            pass
        "Not now, I'm busy.":
            cho "Ok, [cho_genie_name]. I will ask you again later."
            $ days_without_an_event = 0

            jump main_room

    #Cho enters the room.
    call play_sound("door")

    call cho_main("...","upset","closed","sad","L",xpos="mid",ypos="base")
    m "Miss [cho_name], what was it you needed?"
    call cho_main("I... um...","annoyed","base","sad","R")
    call cho_main("[cho_genie_name], I know you're buying favors from Hermione!","annoyed","angry","sad","mid")
    g4 "*Gasps* Me? I'd never-"
    call cho_main("I saw you!","open","base","angry","mid")
    m "Oh,... right..."
    call cho_main("[cho_genie_name], I want you to buy favors from me!","smile","angry","sad","mid")
    m "What? Last time you went on and on about being above all of this 'nasty' favor business,..."
    m "Not needing to 'dirty' yourself to win the cup, and bla, bla, bla..."
    call cho_main("[cho_genie_name], The Slytherin team is cheating!","pout","suspicious","angry","down")
    call cho_main("It doesn't matter how hard I try or how good I am!","open","suspicious","angry","down")
    call cho_main("They leave me no choice, [cho_genie_name]...","annoyed","suspicious","angry","downR")
    call cho_main("Please, we just can't beat them any other way!","angry","angry","angry","mid")
    m "(...)"
    g4 "(How could I even say no when a damsel like her is in... such distress.)"
    g9 "(One with such a nice body, on top of that!)"

    label cho_insists_on_favours:
    menu:
        ">Buy favours from Cho?"
        "-Better not-":
            m "I don't think that's a good idea..."
            call cho_main("What?!","open","wide","angry","L")
            m "Can't you ask any of the other teachers to buy favours from?"
            call cho_main("The only other teacher trading favors is Snape.","pout","suspicious","sad","downR")
            g9 "Problem solv-"
            call cho_main("And I will never trade that corrupt, stinking, slytherin scum a single favor!", "scream", "closed","angry","mid",trans="hpunch")
            m "(...)"
            call cho_main("I can't believe you let that stupid Gryffindor slut buy favours from you...","open","angry","angry","mid")
            call cho_main("But not me?","scream","closed","angry","mid",trans="hpunch")
            call cho_main("What is it that makes her so much better?","upset","angry","angry","R")
            m "Well, for one."
            g9 "She has tits!"
            call cho_main("I have tits too, [cho_genie_name]!!!","scream","angry","angry","mid",trans="hpunch")
            $ cho_wear_top = False
            call cho_main("","angry","angry","angry","mid",trans="fade")
            call ctc
            call cho_main("Here!","open","angry","angry","mid")
            call cho_main("","angry","closed","angry","mid")
            call ctc

            g9 "You are right... They are quite nice."
            $ cho_wear_top = True
            call cho_main("Wouldn't you like to see them more often, [cho_genie_name]? You'd just need to buy favours from me...","pout","angry","angry","R",trans="fade")
            jump cho_insists_on_favours

        "-Sure, why not-":
            m "Alright, Miss Chang. I'll let you sell me favors."
            call cho_main("Yes. We can finally win this!","smile","base","base","mid")
            g9 "Such motivation!"
            call cho_main("Just know, [cho_genie_name]...","open","base","sad","mid")
            call cho_main("I'll do anything to win that Quidditch cup!","horny","base","sad","mid")
            m "Quit-it... quit what?"
            call cho_main("The Quidditch cup, [cho_genie_name]!","open","base","sad","mid")
            call cho_main("Ravenclaw is losing against Slytherin.","soft","base","sad","R")
            call cho_main("And Gryffindor...","annoyed","base","sad","down")
            call cho_main("(And Hufflepuff........)","angry","closed","sad","mid")
            m "Can't I just give you some house-points and we're good?"
            call cho_main("Well of course you can, but... I thought you could maybe... help us out with that too?","soft","base","raised","mid")
            call cho_main("Quidditch means everything to me, [cho_genie_name]...","open","suspicious","sad","R")
            call cho_main("I'm only really good at sports, and Quidditch is the only sport-subject we have at this school...","soft","suspicious","sad","down")
            m "(A school sport, hmm...)"
            g9 "(I've got an idea!)"
            m "So what you are saying is, you want me to help you cheat?"
            call cho_main("Uhm... Yes...","open","base","sad","mid")
            m "Very well then. I'll help you with your silly Cup, but in return, you won't get as many house-points!"
            call cho_main("Thank you, [cho_genie_name]! Thank you so much!","smile","base","raised","mid")
            m "Don't mention it."

    hide screen cho_chang
    with d3
    pause.2

    $ cho_whoring = 0
    $ cho_mad = 0
    $ cho_unlocked = True
    call give_reward(">You've unlocked the ability to summon Cho Chang to your office, and buy favours from her.","interface/icons/head/cho_unlock_01.png")

    pause.5
    call cho_main(xpos="base",ypos="base")

    jump cho_requests
