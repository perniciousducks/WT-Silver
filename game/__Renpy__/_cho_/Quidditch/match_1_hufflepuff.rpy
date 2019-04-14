

### Ravenclaw vs. Hufflepuff ###

label start_hufflepuff_match:
    call cho_main(xpos="mid",ypos="base",trans="fade")
    m "[cho_name], what do you say... ready for your first game of the season?"
    call cho_main("To be honest, [cho_genie_name], I'm feeling quite nervouse.","soft","base","sad","R")
    m "Don't worry. I believe you are ready..."
    m "When are you going to play against Hufflepuff?"
    call cho_main("That's up to you, [cho_genie_name]. As headmaster you decide when the games will be held...","open","base","base","mid")
    m "So if I were to say tomorrow, it will happen tomorrow?"
    call cho_main("Yes, [cho_genie_name].","base","base","base","mid")
    g9 "Well then, tomorrow it is!"

    if weather_gen in [5,6]: # Bad weather.
        call cho_main("Sounds great, [cho_genie_name]. I just hope it stops raining until then.","soft","base","base","R")
    else:
        call cho_main("Sounds great, [cho_genie_name]. I hope the weather stays like this until tomorrw.","soft","base","base","R")

    m "With our tactics, this will be a piece of cake!"
    call cho_main("I hope you are right, [cho_genie_name].","base","base","base","mid")
    call cho_main("Anyhow, I need to prepare for the game.","soft","base","base","R")
    call cho_main("See you then, [cho_genie_name]!","smile","base","base","mid")
    m "Good luck!"

    # Cho leaves.
    call cho_walk(speed=1.6, action="leave")

    jump end_cho_event



### Main Match Against Hufflepuff ###

label hufflepuff_match:

    # Scene before Match agains Hufflepuff
    call play_sound("door")

    call sna_walk("door","mid",2)
    pause.5

    call sna_main("Are you ready to go?","snape_03",xpos="base",ypos="base")
    g4 "Can't you bloody knock?!"
    call sna_main("Should I?{w} I was sure you were already waiting for me...","snape_05")
    m "To do what?"
    call sna_main("We have to head out for the pitch. The whole school is waiting on you.","snape_24")
    m "Didn't you berate me about not to leaving this room unless absolutely necessary?"
    call sna_main("A rule which I’m sure you have disregarded a great many times already...","snape_29")
    call sna_main("You'll have to join me on this one. As headmaster, you are expected to attend the Quidditch matches.","snape_06")
    m "And that’s today?"
    call sna_main("Indeed.","snape_03")
    m "(...)"
    m "Wouldn’t the other teacher see me if I went?"
    call sna_main("Don't worry. I’ve arranged to have us moved from the teachers' seats to the commentator both.","snape_24")
    call sna_main("Just the two of us...","snape_23")
    m "And Miss Granger?"
    call sna_main("Granger...","snape_08")
    call sna_main("Well, that’s very displeasing to say the least...","snape_07")
    call sna_main("In any case, you won't be seen up close by any of the other teachers.","snape_09")
    m "Sounds like a snore. Can't I stay here and you’ll tell them I'm ill or something?"
    call sna_main("No.","snape_04")
    call sna_main("That would just prompt the nurse to examine you closely...","snape_03")
    m "Well... I wouldn’t mind that."
    call sna_main("I’m sure you wouldn’t...","snape_06")
    call sna_main("Good thing though is that we’ll be able to bring a little something to keep us preoccupied.","snape_20")
    call hide_characters
    with d3

    # Show wine
    call give_reward(text=">Not grape-juice.",gift="interface/icons/item_wine.png")

    m "That's all the persuasion I needed my friend!"

    # Teleport
    call play_sound("door")
    show screen chair_left
    show screen desk
    call gen_chibi("hide")
    with d3

    call gen_chibi("stand","door","base",flip=False)
    call teleport(position="genie",effect=False)
    pause.5

    call gen_chibi("stand","door","base",flip=True)
    with d3
    pause.2
    m "What are we waiting for. Let's go!"

    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_main("(When did he?...)","snape_05",ypos="head")
    call sna_main("After you...","snape_09",ypos="head")
    pause.8

    m "Actually, I have no idea where we're going."

    call gen_chibi("stand","door","base",flip=False)
    with d3
    pause.2

    m "You should lead the way..."
    call sna_main("Right you are. Time to get smashed!","snape_02",ypos="head")

    call sna_walk("mid","700",1.6)

    # Blackfade
    call play_sound("door")
    call blkfade
    pause 2

    centered "{size=+7}{color=#cbcbcb}At the Quidditch pitch...{/color}{/size}"

    pause 1
    call hide_blkfade



    ### Main Match Starts ###

    # Hermione’s Intro
    # open shot of Quidditch pitch
    # fade to hermione CG with eyes closed
    her "Good Morning everyone, and welcome to the i-inaugural-"
    call sna_main("Speak up girl! And would it kill you to enunciate?!","snape_03",ypos="head")
    her "*Grrr*"
    her "Welcome to the first quidditch game of the season!"
    call sna_main("Better... You’ve advanced from Troll to Dreadful....","snape_09",ypos="head")
    m "{size=-4}Troll?{/size}" # Small text.
    call sna_main("{size=-4}Those are grades we give out to our students, for decidedly poor performances, like Granger’s...{/size}","snape_01",ypos="head")
    her "..."
    her "Hufflepuff versus Ravenclaw!"
    ">A loud cheer roars from the grandstands."


    # Speech
    her "And now, to say a few words and declare the games open, Professor Dumbledore!"
    m "{size=-4}What? Isn’t that me?{/size}"  # Small text.
    call sna_main("It is.","snape_02",ypos="head")
    m "Why did no one warn me about this?"
    call sna_main("I’ve been looking forward to watching you bumble your way through this...","snape_22",ypos="head")
    call sna_main("Besides, you only have to give some trivial speech about team spirit, gesticulate wildly and say \"let the games begin\". A child could manage it.","snape_24",ypos="head")
    call sna_main("Now get up there!","snape_10",ypos="head")
    ">With that, Snape shoves you out of your chair, in front of the podium."

    menu:
        "\"Miracle on ice speech\"":
            m "Great moments are born from great opportunity."
            ">A reverent hush falls over the crowd..."
            m "And that’s what we have here tonight-"
            #Fade to black
            m "Tonight, WE are the greatest hockey team in the world!"
            #Fade to black
            m "Their time is done, it’s over! I’m sick and tired about hearing what a great hockey team the soviets have!"
            mal "I think Dumbledore has finally started to lose his marbles..."
            mal2 "I think you might be right."
            m "Screw it! This is our time, now let the games begin!"
        "\"Good Morning, Vietnam!\"":
            ">A confused murmur falls over the crowd."
            m "Ugh..."
            m "Go team!"
            ">The sound of confused murmuring increases even further..."
            mal "Fire’s lit but the cauldron’s empty..."
            mal2 "Looks like it..."
            m "Tough crowd... Anyway, let the games begin!"
    ">The crowd cheers excitedly, desperate to see the match kickoff."
    her "Ugh... thank you for that, professor Dumbledore..."
    her "Now, to get this game underway!"


    # Player Introduction
    her "First, let’s welcome everyone’s favourite underdogs, Ravenclaw!"
    ">The blue grandstand shakes violently with enthusiasm."
    call sna_main("At least try to sound like you’re awake, Miss Granger.","snape_03",ypos="head")
    her "..."
    her "And coming onto the field to face them are the equally impressive, Hufflepuff!"
    call sna_main("Back down to Troll...","snape_09",ypos="head")
    her "*grrrrr*"
    her "It appears we’ve got an interesting game ahead of us. If I’m not mistaken, there’s some history between our seekers, Cho Chang and Cedric Diggory..."
    ">Even though they are far down below on the pitch, you can clearly see Cho and Cedric glaring up at Hermione."
    her "Given how essential the seekers role are in Quidditch, their complex past might cost one of them the game..."
    call sna_main("Complex past...","snape_01",ypos="head")
    call sna_main("I practically caught them chew each other’s tongues off at one point.","snape_02",ypos="head")
    her "Speaking of important, I just realised that as the inaugural game, I should cover the rules of the game for any first-years watching."
    ">Hermione heaves a heavy rule book from under the table and begins to monotonously recite it to the crowd."
    her "The capturing of the snitch is worth 150 points-"
    her "The game may not conclude until it has been caught, or an agreement is made between both capt-"
    mal "Just get on with it already you big titted slag!"
    mal2 "Yeh! Start the game!"
    qcr "START THE GAME! START THE GAME!"
    ">Hermione’s voice eventually gets drowned out by the growing restlessness of the crowd."
    her "Ugh, fine. If everyone wants us to begin play without knowing a SINGLE thing... then that’s OK! A good commentator knows when to accommodate for a crowd’s impatience!"
    call sna_main("{size=-4}This should be good{/size}","snape_02",ypos="head") # Small text.
    ">With that, the snitch and bludgers are released and fly off into the air."
    her "Now then..."
    her "Let’s begin!"


    # Start of the Game
    ">A Grey haired woman then throws the quaffle into the air which signals the start of the match and the players quickly takes off!"

    her "Oh, wow... They’re going quite f-fast..."
    call sna_main("Great commentary there girl... You might want to let them know the colour of the grass next...","snape_10",ypos="head")
    her "Um, I’m not sure if anyone’s scored yet... Wait, that guy has the quaffle... I think..."
    her "Scratch that last bit, he has a stick so he must be a beater!"



    # Cho’s Skirt gets addressed
    her "Higher up, Cho seems to have caught an eye on the snitch and is chasing after it, directly followed by Cedric who..."
    her "Hold on a minute... Is Cho wearing a skirt?"
    qcr "!!!" # [screenshake?]
    mal "She totally is!"
    mal2 "What a slut!"
    her "Professor, why won’t you say something? She’s clearly breaking the very basics of Quidditch rules!"
    m "I fail to see anything wrong with the way she’s dressed."
    her "But... she’s wearing a skirt!"
    her "Surely that must be against some kind of regulation..."
    m "You tell me Miss Granger, you’ve got the rulebook right there..."
    call sna_main("...","snape_13",ypos="head") # [Smirk]
    her "Perhaps I could get Madame Hooch to pause the game..."
    call sna_main("Knowing her, she’s probably enjoying the sight of the Ravenclaw seeker rushing past her.","snape_20",ypos="head")
    call sna_main("{size=-4}Odds are she’s already tried to take a peek.{/size}","snape_20",ypos="head")  # Small text.
    m "{size=-4}Who’s Madame Hooch?{/size}"  # Small text.
    call sna_main("{size=-4}It’s that grey haired lady on the pitch that is seemingly unable to take her eyes off the underside of Cho’s... undergarments.{/size}","snape_09",ypos="head") # [Smirk]
    call sna_main("{size=-4}Great idea with the skirt, if I might add.{/size}","snape_13",ypos="head")  # Small text.
    m "{size=-4}You’re welcome, by the way.{/size}"  # Small text.
    call sna_main("...","snape_12",ypos="head")
    call sna_main("{size=-4}She is wearing something underneath I assume?{/size}","snape_13",ypos="head") # Small text.
    m "For now..."
    call sna_main("Excellent...","snape_22",ypos="head")

    mal "Cho show us your panties!"
    mal2 "We want to see them!"

    her "Oh, apparently Ravenclaw scored during that... \"captivating\" bit of distraction..."
    g9 "Sarcasm much?"
    call sna_main("...","snape_13",ypos="head") # [Smirk]
    her "I think it’s 10-20!"
    her "Or is that 20-10... I’m not sure, aren’t they both home teams..."
    call sna_main("Surely you must have learnt how to read by now, Miss Granger?","snape_03",ypos="head")
    her "Hey! I have excellent reading skills I’ll have you know..."
    her "Wait, now it’s... 20-30... I think..."
    mal "Has this girl ever commentated even once in her life?"
    mal2 "She can’t help herself answering questions in class...."
    mal2 "I suppose the rule book was more for her benefit than ours."
    mal "Then how’d she get the role over Lee Jordan?"
    mal2 "Affirmative action at it again if you ask me!"
    mal "..."
    her "Wow... that snitch is darting around like nobody’s business-"


    # Genie and Snape get Drunk
    # Cut to genie and snape
    call sna_main("Fancy a glass of wine then?","snape_02",ypos="head")
    m "Don’t mind if I do... Something to distract me from this... bizzare game..."
    pause.5
    call play_sound("bottle")
    pause.8

    call sna_main("{size=-4}I don’t care much for the game myself...{/size}","snape_09",ypos="head")
    call sna_main("{size=-4}Although, there is a special place in my heart for watching the bludgers catch a student...{/size}","snape_02",ypos="head")
    m "{size=-4}Blubbers?{/size}"
    call sna_main("{size=-4}Bludgers... See those cannonball looking things whizzing around?{/size}","snape_03",ypos="head")
    m "{size=-4}Oh... The ones those boys are whacking at?{/size}"
    call sna_main("{size=-4}Right... Well, we enchant them to go after the students while they play.{/size}","snape_23",ypos="head")
    m "{size=-4}Really? Why?{/size}"
    call sna_main("{size=-4}Makes things more interesting doesn’t it!{/size}","snape_02",ypos="head")
    m "{size=-4}So what happens when they hit their target?{/size}"
    call sna_main("{size=-4}Generally it’s just a concussion... Though sometimes they fall pretty far, that’s always entertaining.{/size}","snape_20",ypos="head")

    # hpunch
    with hpunch
    her "Oh no!"
    call sna_main("{size=+4}HAHAHAHA!!{/size}","snape_28",ypos="head")
    her "Somebody on the Ravenclaw team just got hit by a bludger!"
    g9 "That was awesome!"
    call sna_main("See, I told you!","snape_22",ypos="head")
    her "Professors, could you please keep it down a little?"
    call sna_main("Why? It’s not like we’re interrupting anything important.","snape_18",ypos="head")
    her "I’m trying to commentate the game!"
    call sna_main("Yes, and I was starting to enjoy it, you are missing most of it by the way...","snape_20",ypos="head")
    her "As a result of your yelling!"
    call sna_main("Eyes forward... girl.","snape_13",ypos="head")
    her "*Grrrrr*"
    ">Hermione’s eyes briefly meets with yours as if she can’t believe you’re letting Snape talk to her that way."

    call sna_main("{size=-4}As I was saying... They’re the only reason I watch the bloody thing. Now, mind if I top that one off for you?{/size}","snape_20",ypos="head")
    ">You and Snape lean back and watch the game, frequently shifting your focus to Cho, as she darts past the stands, only occasionally pausing for more wine or for Snape to ridicule Hermione’s commentating."

    # Fade to black

    her "So, I think... that Hufflepuff just scored another goal? They might even be unstoppable at this point!"


    # End of game
    # Hooch should blow the whistle here.

    her "What was that? Did somebody do a foul?"
    "You see Cho flying over to the commentator booth glaring at Hermione with a look of pure hatred."

    # Transition to Cho on her broom.
    cho "Hey, Granger!"
    her "What do you want? Shouldn’t you be busy with, I don’t know... playing the game?"
    cho "The game is over, you dipstick!"
    her "What? Already?"
    her "But who caught the Snitch?"
    ">Cho waves the snitch in front of her."
    cho "My first ever win this season and you didn’t even notice it! No one did thanks to your dreadful commentating!"
    her "Oh..."
    her "So should I announce it now?"
    call sna_main("Obviousl-","snape_12",ypos="head")
    cho "{size=+10}YES!{/size}"
    cho "{size=+6}WHAT ARE YOU EVEN WAITING FOR?{/size}" # Large text.
    her "Don’t scream at me like that, slut!"
    cho "{size=+6}WHAT DID YOU JUST CALL ME?!!!{/size}" # Large text.
    her "Everyone, Ravenclaw wins!"
    her "Cho Chang managed to catch it, the snitch that is..."
    her "With the help of her ridiculously short skirt!"
    cho "{size=+10}!!!{/size}"
    ">Hermione’s commentating is drowned out by the sound of the Ravenclaw grandstand cheering."
    cho "{size=+6}You are done, Granger!{/size}"
    pause.8

    # Outro
    m "This isn’t such a bad game after all."
    call sna_main("I *hick* told you... so...","snape_22",ypos="head")
    m "Just bring more wine next time!"
    call sna_main("M-More?!","snape_20",ypos="head")
    m "Or at least share more of it with me!"
    call sna_main("Get your own, magic man!","snape_21",ypos="head")
    m "..."
    ">Snape wanders off in a drunken rage..."

    # Blackfade

    "> You hurry back to your office before giving anyone a chance to talk to you."

    # Skip to evening.

    jump night_start







# Return Response
label hufflepuff_match_return:
    # Cho returns after winning the Quidditch match.
    # She's outraged about Hermione.
    # Demands that you will find somebody to replace her.
    pause.8

    call cho_walk("mid", "base", 1.6, action="enter")

    call cho_main("We beat \"Hufflepuff\"!!!","scream","shocked","base","mid",trans="hpunch")
    call cho_main("I can't believe that we've broken our 6 year dry streak and won a real game!","smile","base","base","mid")
    call cho_main("We could actually win the cup!","open","shocked","angry","L")
    m "And you weren't embarrassed?"
    call cho_main("I was a little at the start of the game...","quiver","suspicious","sad","downR")
    call cho_main("But once I realized how much it was affecting those slack-jawed \"Hufflepuffs\"s...","smile","angry","angry","R")
    call cho_main("It was like having my own personal weapon of mass distraction!","smile","shocked","angry","mid")
    call cho_main("I don't think Cedric even knew where the snitch was most of the time!","horny","base","base","downR")
    call cho_main("All he seemed to do was follow me around...","horny","suspicious","sad","down")
    call cho_main("{size=-2}Him {size=-2}and {size=-2}half {size=-2}the {size=-2}team...{/size}","quiver","suspicious","sad","downR")
    call cho_main("This might be the first real chance \"Ravenclaw\" has ever had to win the cup.","open","closed","sad","mid")
    m "I'm sure this must mean a lot to you..."
    call cho_main("It does... I might even get picked up by a pro team!","smile","base","base","R")
    m "..."
    call cho_main("Agh, I can't wait!","scream","closed","base","mid")
    call cho_main("I better go celebrate with the team now!","open","base","base","R")
    m "Well, off you go then."
    call cho_main("Thank you Professor...","smile","wink","base","mid")

    # Cho leaves.
    call cho_walk(speed=1.6, action="leave")

    stop music fadeout 1.0
    call give_reward(">New favours for Cho have been unlocked!","interface/icons/head/head_cho_2.png")

    $ cho_busy      = True
    $ hermione_busy = True
    $ snape_busy    = True

    $ cho_content_complete = True # Temporary to hide the Practice Match option in the menu.

    jump end_cho_event
