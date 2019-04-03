

### Ravenclaw vs. Hufflepuff ###

label start_hufflepuff_match:
    m "Are you ready for your first official game of the season?"
    cho "To be honest, [cho_genie_name], I'm quite nervouse."
    m "You will do great."
    m "It's tomorrow isn't it?"

    if weather_gen in [5,6]: # Bad weather, no match today.
        cho "Yes, [cho_genie_name]. I just hope it stops raining until then."
    else:
        cho "Yes, [cho_genie_name]. I hope the weather stays like this until tomorrw."

    m "With our tactics, this will be a piece of cake!"
    cho "I hope you are right, [cho_genie_name]."
    cho "Anyhow, I need to prepare for the game tomorrow."
    cho "See you then, [cho_genie_name]!"
    m "Good luck!"

    # Cho leaves.
    jump end_cho_event



### Main Match Against Hufflepuff ###

label hufflepuff_match:

    # Scene before Match agains Hufflepuff

    # Summon Snape
    sna "Are you ready to go?"
    m "Go?- Go where?"
    m "Didn't you berate me about not to leaving this room unless absolutely necessary?"
    sna "A rule which I’m sure you have disregarded a great many times already..."
    sna "You'll have to join me on this one. As headmaster, you are expected to attend the Quidditch matches."
    m "And that’s today?"
    sna "Indeed."
    m "Wouldn’t the other teacher see me if I went?"
    sna "I’ve arranged to have us moved from the teachers' seats to the commentator both."
    sna "Just the two of us and-"
    m "And Miss granger!"
    sna "Granger..."
    sna "Well, that’s very displeasing to say the least..."
    sna "In any case, you won't be seen up close by any of the other teachers."
    m "Sounds like a snore. Can't I stay here and you’ll tell them I'm ill or something?"
    sna "No."
    sna "That would just prompt the nurse to examine you closely..."
    m "Well... I wouldn’t mind that."
    sna "I’m sure you wouldn’t..."
    sna "Good thing though is that we’ll be able to bring little something something to keep us preoccupied."

    # Show wine

    m "That's all the persuasion I needed my friend!"
    m "What are we waiting for. Let's go!"
    sna "After you..."
    m "Actually, I have no idea where we're going. You should lead the way..."
    sna "Right you are. Time to get smashed!"

    # Blackfade



    ### Main Match Starts ###

    # Hermione’s Intro
    # open shot of Quidditch pitch
    # fade to hermione CG with eyes closed
    her "Good Morning everyone, and welcome to the i-inaugural-"
    sna "Speak up girl! And would it kill you to enunciate?!"
    her "*Grrr*"
    her "Welcome to the first quidditch game of the season!"
    sna "Better... You’ve advanced from Troll to Dreadful...."
    m "Troll?" # Small text.
    sna "Those are grades we give out to our students, for decidedly poor performances, like Granger’s..."
    her "..."
    her "Hufflepuff versus Ravenclaw!"
    ">A loud cheer roars from the grandstands."


    # Speech
    her "And now, to say a few words and declare the games open, Professor Dumbledore!"
    m "What? Isn’t that me?"  # Small text.
    sna "It is."
    m "Why did no one warn me about this?"
    sna "I’ve been looking forward to watching you bumble your way through this..."
    sna "Besides, you only have to give some trivial speech about team spirit, gesticulate wildly and say \"let the games begin\". A child could manage it."
    sna "Now get up there!"
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
    sna "At least try to sound like you’re awake, Miss Granger."
    her "..."
    her "And coming onto the field to face them are the equally impressive, Hufflepuff!"
    sna "Back down to Troll..."
    her "*grrrrr*"
    her "It appears we’ve got an interesting game ahead of us. If I’m not mistaken, there’s some history between our seekers, Cho Chang and Cedric Diggory..."
    ">Even though they are far down below on the pitch, you can clearly see Cho and Cedric glaring up at Hermione."
    her "Given how essential the seekers role are in Quidditch, their complex past might cost one of them the game..."
    sna "Complex past..."
    sna "I practically caught them chew each other’s tongues off at one point."
    her "Speaking of important, I just realised that as the inaugural game, I should cover the rules of the game for any first-years watching."
    ">Hermione heaves a heavy rule book from under the table and begins to monotonously recite it to the crowd."
    her "The capturing of the snitch is worth 150 points-"
    her "The game may not conclude until it has been caught, or an agreement is made between both capt-"
    mal "Just get on with it already you big titted slag!"
    mal2 "Yeh! Start the game!"
    qcr "START THE GAME! START THE GAME!"
    ">Hermione’s voice eventually gets drowned out by the growing restlessness of the crowd."
    her "Ugh, fine. If everyone wants us to begin play without knowing a SINGLE thing... then that’s OK! A good commentator knows when to accommodate for a crowd’s impatience!"
    sna "This should be good" # Small text.
    ">With that, the snitch and bludgers are released and fly off into the air."
    her "Now then..."
    her "Let’s begin!"


    # Start of the Game
    ">A Grey haired woman then throws the quaffle into the air which signals the start of the match and the players quickly takes off!"

    her "Oh, wow... They’re going quite f-fast..."
    sna "Great commentary there girl... You might want to let them know the colour of the grass next..."
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
    m "You tell me miss granger, you’ve got the rulebook right there..." # Small text.
    sna "..." # [Smirk]
    her "Perhaps I could get Madame Hooch to pause the game..."
    sna "Knowing her, she’s probably enjoying the sight of the Ravenclaw seeker rushing past her."
    sna "Odds are she’s already tried to take a peek."  # Small text.
    m "Who’s Madame Hooch?"  # Small text.
    sna "It’s that grey haired lady on the pitch that is seemingly unable to take her eyes off the underside of Cho’s... undergarments." # [Smirk]
    sna "Great idea with the skirt, if I might add."  # Small text.
    m "You’re welcome, by the way."  # Small text.
    sna "..."
    sna "She is wearing something underneath I assume?" # Small text.
    m "For now..."
    sna "Excellent..."

    mal "Cho show us your panties!"
    mal2 "We want to see them!"

    her "Oh, apparently Ravenclaw scored during that... \"captivating\" bit of distraction..."
    g9 "Sarcasm much?"
    sna "..." # [Smirk]
    her "I think it’s 10-20!"
    her "Or is that 20-10... I’m not sure, aren’t they both home teams..."
    sna "Surely you must have learnt how to read by now, Miss Granger?"
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
    sna "Fancy a glass of wine then?"
    m "Don’t mind if I do... Something to distract me from this... bizzare game..."
    sna "I don’t care much for it myself..."
    sna "Although, there is a special place in my heart for watching the bludgers catch a student..."
    m "Blubbers?"
    sna "Bludgers... See those cannonball looking things whizzing around?"
    m "Oh... The ones those boys are whacking at?"
    sna "Right... Well, we enchant them to go after the students while they play."
    m "Really? Why?"
    sna "Makes things more interesting doesn’t it!"
    m "So what happens when they hit their target?"
    sna "Generally it’s just a concussion... Though sometimes they fall pretty far, that’s always entertaining."

    # hpunch
    her "Oh no!"
    sna "HAHAHAHA!!"
    her "Somebody on the Ravenclaw team just got hit by a bludger!"
    g9 "That was awesome!"
    sna "See, I told you!"
    her "Professors, could you please keep it down a little?"
    sna "Why? It’s not like we’re interrupting anything important."
    her "I’m trying to commentate the game!"
    sna "Yes, and I was starting to enjoy it, you are missing most of it by the way..."
    her "As a result of your yelling!"
    sna "Eyes forward... girl."
    her "Grrrrr!"
    ">Hermione’s eyes briefly meets with yours as if she can’t believe you’re letting Snape talk to her that way."

    sna "As I was saying... They’re the only reason I watch the bloody thing. Now, mind if I top that one off for you?"
    ">You and Snape lean back and watch the game, frequently shifting your focus to Cho, as she darts past the stands, only occasionally pausing for more wine or for Snape to ridicule Hermione’s commentating."

    # Fade to black

    her "So, I think... that Hufflepuff just scored another goal? They might even be unstoppable at this point!"


    # End of game
    # Hooch should blow the whistle here.

    her "What was that? Did somebody do a foul?"
    ">With that, Cho flies over to the commentator  booth glaring at Hermione with a look of pure hatred."

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
    sna "Obviousl-"
    cho "YES!"
    cho "WHAT ARE YOU EVEN WAITING FOR?" # Large text.
    her "Don’t scream at me like that, slut!"
    cho "WHAT DID YOU JUST CALL ME?!!!" # Large text.
    her "Everyone, Ravenclaw wins!"
    her "Cho Chang managed to catch it, the snitch that is..."
    her "With the help of her ridiculously short skirt!"
    cho "!!!"
    ">Hermione’s commentating is drowned out by the sound of the Ravenclaw grandstand cheering."
    cho "You are done, Granger!"


    # Outro
    m "This isn’t such a bad game after all."
    sna "I *hick* told you... so..."
    m "Just bring more wine next time!"
    sna "M-More?!"
    m "Or at least share more of it with me!"
    sna "Get your own, magic man!"
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
    call play_sound("door")

    call cho_walk("door","mid",1.6)

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

    call cho_walk("mid","leave",1.6)

    stop music fadeout 1.0
    call give_reward(">New favours for Cho have been unlocked!","interface/icons/head/head_cho_2.png")

    "Developer note:" ">This marks the end of Cho's current Quidditch story.\nThank you for playing."
    $ cho_content_complete = True # Temporary to hide the Practice Match option in the menu.

    jump end_cho_event
