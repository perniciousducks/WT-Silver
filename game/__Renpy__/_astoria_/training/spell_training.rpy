

### Spell Training ###

### Astoria Imperio Training ###

label ag_st_imperio:

    "Dev Note" "You send Astoria to Tonks"

    $ ag_st_imperio.inProgress = True

    jump main_room


label ag_se_imperio_sb: # Move label

    $ ag_se_imperio_sb.start()

    label end_ag_se_imperio_sb:

    jump main_room


label ag_st_imperio_E1:
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    # call ast_chibi("stand","desk","base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("playful")
    call ast_main("","annoyed","base","base","mid", xpos="right", ypos="base")
    call ton_main("Good evening, Professor.","base","happyCl","base","mid", xpos="base", ypos="base")
    m "You are back."
    call ton_main("Yes we are.","base","base","base","mid")
    call ast_main("......................","annoyed","narrow","base","L") # embarrassed
    g9 "Astoria!{w} How was your training?"
    call ast_main("................................","annoyed","narrow","base","R")
    call ton_main("It went very well, I'd say.","smile","happyCl","base","mid")
    call ton_main("I instructed her on how to cast the curse - properly.","base","base","base","mid")
    call ton_main("The right wand movement... The correct pronunciation...","open","base","base","R")
    call ton_main("There's a lot to it!","base","base","base","mid")
    call ton_main("One mishap with those - and the curse might backfire!","open","base","angry","mid")
    call ton_main("Sending you straight to St. Mungos hospital - quacking like a duck!","smile","happyCl","base","mid")
    m "..........."
    call ton_main("I'd say she was very lucky using it on Susan...","angry","base","base","mid")
    call ast_main("I knew exactly what I was doing...","clench","closed","angry","mid")
    call ast_main("","clench","narrow","base","mid")
    call ton_main("Of course you did, princess.","base","base","base","L") # Happy
    call ast_main(".................................","annoyed","narrow","angry","L") # annoyed

    call ton_main("Now, shall we get started?","smile","happyCl","base","mid")
    call ast_main("Get started - with what?","open","narrow","base","R")
    call ton_main("Continuing your training, of course!","open","base","base","L")
    call ton_main("I'd like you to cast the Imperius curse now... On another person.","base","base","angry","L")
    call ast_main("Wait- what?","angry","base","base","mid")
    call ast_main("I thought I wasn't allowed to ever use it again?","open","base","worried","R")
    call ton_main("You aren't... That is correct.","open","closed","sad","mid")
    call ton_main("However, you are hereby given special permission!","base","base","base","mid")
    call ast_main("Really?","smile","base","base","mid") # happy
    call ton_main("Yes, dear!","base","base","base","L")
    call ton_main("I believe our Professor would have no objection with that...","open","closed","base","mid")
    call ton_main("Would you, Professor?","base","base","angry","mid")
    call ast_main("Please, Professor!","smile","base","base","mid")
    m "*Uhm*...{w=0.4} Sure...{w=0.6} Go ahead."
    call ton_main("Splendid!","smile","happyCl","base","mid")
    call ast_main("Yes!","smile","base","angry","L")

    call ton_main("You can cast it, as long as it's under the surveillance of a teacher...","open","base","angry","mid")
    call ton_main("And only within the walls of this room!","open","base","base","L") # stern
    call ast_main("Right here? In front of Professor Dumbledore?","open","base","base","mid")
    call ton_main("Naturally!","smile","base","base","mid")
    call ast_main("But who do I I cast it on? Susan?","smile","base","base","R")
    call ton_main("Not this time, sweetheart.","upset","base","base","down")
    call ton_main("Today, I'd like you to cast it on me, if you don't mind...","open","closed","base","mid")
    call ast_main("Wicked!","grin","narrow","worried","down")
    call ton_main("Let's give this old man a quick demonstration of your talents, shall we...","base","base","angry","mid")
    call ast_main("","grin","narrow","base","mid")
    m ".............................."

    call ton_main("Just like we practiced...","open","closed","base","mid")
    call ton_main("Do the movement with your wand, and then you say-","open","base","base","R")
    call ast_main("Imperio!","scream","narrow","angry","mid") # angry scream
    call ast_main("","clench","narrow","angry","mid")
    call ton_main("Yes...","angry","base","sad","R")
    call ton_main("....................","upset","base","worried","up")
    call ton_main("You don't have to scream the words, darling.","open","base","raised","L")
    call ton_main("What's crucial is that your mind is focused and-","open","closed","base","mid")

    # Astoria casts imperio.
    hide screen tonks_main

    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch") # Screams it even louder

    call hide_characters
    with d3
    pause.2

    # chibi spell animation.
    with hpunch
    pause.8

    call ast_main("","clench","base","angry","L", xpos="base", ypos="base")
    call ton_main(".........................","angry","wide","wide","ahegao", xpos="right", ypos="base") # shock
    call ton_main("*Aaaaaah*...","horny","base","base","ahegao", hair="horny") # inhales
    call ast_main("......................","clench","base","worried","L") # clenched teeth
    m "What's happening to her?"
    call ast_main("I just cast the spell on her...","open","closed","base","mid")
    call ast_main("Now she should be under my command!","smile","base","base","mid")
    g9 "You don't say?"
    g9 "I love magic!"
    call ast_main("What shall I do, Professor?","clench","base","base","L")
    m "I don't know... Why are you asking me?"
    m "Did you not discuss this with her beforehand?"
    call ast_main("No. All we did was some theoretical practice of the spell...","open","base","base","down")
    call ast_main("I need to tell her to do something... or...","open","base","worried","mid")
    call ast_main("I don't know... Maybe say something?","clench","base","base","L")
    call ton_main("*Hmmm*... Something...","base","base","worried","ahegao")
    call ast_main("","smile","base","base","L")
    m "What?"
    call ast_main("She did it!","smile","base","base","L")
    g4 "Something what?"
    call ast_main("No, she just said what I asked her to say!","smile","base","base","mid")
    m "Oh..."
    call ast_main("I believe it's working!","smile","closed","base","mid")

    call ast_main("*Uhm*... Professor Tonks, you can now speak freely!","horny","base","base","L")
    call ton_main("............................","base","base","base","ahegao")
    call ton_main("Oh... can I?...","open","base","base","ahegao")
    call ton_main("Thank you...","smile","happyCl","base","mid")
    call ast_main("She can hear me!","smile","base","base","mid")
    call ton_main("You have a really cute voice...","horny","base","worried","R")
    call ast_main("................","annoyed","base","worried","R")
    m "Try something else now."
    call ast_main("","annoyed","base","base","L")
    call ton_main("I feel so good!","base","base","angry","ahegao")
    call ton_main("What is happening to me?","angry","base","angry","ahegao")
    call ton_main("Are you playing with me?","open","base","sad","ahegao")
    call ton_main("I want you to play with me!","open_wide_tongue","base","angry","ahegao") # horny
    m "I think she's tripping..."
    call ast_main("No!{w=0.6} Keep{w=0.4} - standing{w=0.4} - still!","clench","closed","worried","mid")
    call ton_main("Ok...................","smile","happyCl","base","mid")
    g9 "This is quite funny to watch!"
    g9 "Can you make her *oink?*"
    call ast_main("*oink?*","open","wink","base","mid")
    m "You know, like a pig..."
    call ast_main("Yes, we can try that!","clench","base","base","mid")
    call ast_main("Professor Tonks, I demand that you *oink!*","open","base","base","L")
    call ton_main("*Huh?*...","open","base","raised","ahegao")
    call ast_main("*oink!*","open","base","angry","L")
    call ton_main("...................","base","base","base","ahegao")
    call ast_main("Do it already!","angry","base","angry","L")
    call ast_main("*oink!*{w=0.8}-*oink!*{w=0.8}-*oink!*","clench","closed","angry","mid") # Angry
    g9 "*he-he-he!*"
    call ast_main("*oink*...{w=0.8} you pig!","scream","base","angry","L", trans="hpunch") # Screaming
    call ast_main("","clench","narrow","angry","L")
    m "I don't believe she's going to do it..."
    call ast_main("But!","clench","closed","base","mid")
    m "It's pointless, girl..."
    m "You can stop now..."
    call ast_main(".............................","annoyed","base","angry","down")

    # Tonks reverts back.
    pause.2
    call hide_characters
    hide screen bld1
    with fade
    pause.8

    call ast_main("","annoyed","base","angry","mid", xpos="right", ypos="base")
    call ton_main("Oh my...","upset","base","worried","down", xpos="base", ypos="base")
    call ton_main("Well that was fun!","smile","happyCl","base","mid") # Happy
    call ast_main("No it wasn't!","clench","narrow","angry","mid")
    call ast_main("Why weren't you doing pig noises!","scream","closed","angry","mid", trans="hpunch")
    call ast_main("You refused to do what I demanded!","annoyed","narrow","angry","R")
    call ton_main("Yes I did!","open","base","base","L")
    call ton_main("It was quite easy, actually.","base","base","raised","mid")
    call ast_main("*Hnghhh!*","clench","narrow","angry","down")
    call ton_main("Don't worry. You'll have better luck next time...","smile","happyCl","base","mid")
    call ton_main("Just try a bit harder.","base","happyCl","base","mid")
    call ast_main("...................................","annoyed","narrow","angry","down")
    call ton_main("Thank you for your assistance, Professor.","open","base","base","mid")
    call ton_main("You can have Astoria visit me again for our next training session...","base","base","base","mid")
    m "Very well."
    call ton_main("I can't wait!","base","happyCl","base","mid") # Happy
    call ast_main("........................","annoyed","base","angry","R")
    call ton_main("Have a good night, Professor.","base","base","base","mid")

    call ton_walk(xpos="door", ypos="base", speed=2)
    call ton_chibi("stand","door","base", flip=False)
    with d3
    pause.2

    call ton_main("Come on, Astoria. I shall escort you back to your dormitory...","horny","base","base","L", ypos="head")
    call ast_main(".................................................","annoyed","base","base","down", ypos="head")

    # They both leave.
    #call ast_walk(action="leave", speed=2.5)

    call play_sound("door")
    call ton_chibi("hide")
    with d3

    jump main_room


label ag_st_imperio_E2:
    call play_sound("door")
    call ton_chibi("stand","desk","base")
    # call ast_chibi("stand","desk","base") # Make sure it's slightly to the left of Tonks' chibi.
    with d3
    pause.8

    call play_music("playful")
    call ast_main("","upset","base","base","mid", xpos="right", ypos="base")
    call ton_main("Hello, Professor.","base","happyCl","base","mid", xpos="base", ypos="base")
    call ast_main(".........................","upset","base","base","L")
    m "Back already?"
    call ton_main("Yes, I gave Astoria a couple more pointers on how to improve the persuasiveness of the curse...","open","base","base","mid")
    call ton_main("The trick is to not lose your temper after casting it!","open","closed","base","mid")
    call ast_main(".........................","annoyed","base","base","down")
    call ton_main("This should be fun!","smile","happyCl","base","mid")
    m "Very good."

    call ton_main("Now, Astoria, just as last time - you will cast the Imperius curse on me...","open","base","base","L")
    call ton_main("And I'll do my best to resist-","open","closed","base","mid")

    # Astoria casts imperio.
    hide screen tonks_main

    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch") # Screams it even louder

    call hide_characters
    with d3
    pause.2

    # chibi spell animation.
    with hpunch
    pause.8

    call ast_main("","clench","base","angry","L", xpos="base", ypos="base")
    call ton_main(".........................","angry","wide","wide","ahegao", xpos="right", ypos="base") # shock

    g9 "Damnit, girl!"
    m "Give me a warning next time. You scared the crap out of me..."
    call ast_main("Sorry Professor!","smile","base","base","mid") # Cute face

    call ton_main("..........................","base","base","base","ahegao")
    call ton_main("*uhhhh*... I looooooove this!","horny","base","base","ahegao")
    call ton_main("It's like - I'm floating...","open","base","worried","ahegao")
    call ton_main("It feels...sooooooooooooo...goooooooooooood!","open_wide_tongue","base","base","ahegao")
    call ton_main("","angry","base","base","ahegao")
    m "(Is she getting off on this?)"

    call ast_main("What shall I have her do, Professor?","clench","wink","base","mid")

    m "..........."
    menu:
        "Have her turn around.":
            call ast_main("Yes, that's a good idea!","smile","base","base","mid")
            call ton_main("................................","base","base","base","ahegao")
            call ast_main("Professor Tonks, I command you to turn around.","open","base","base","L")
            call ton_main("*Huh?*","open","base","worried","ahegao")
            call ast_main("Turn around!","clench","base","angry","L")
            m "Remember what she said about your temper, Astoria..."
            call ast_main("Oh... yes Sir! Of course...","smile","closed","base","mid")
            call ast_main("Turn around.","open","narrow","base","L")
            call ton_main("......................","base","base","base","ahegao")

            # Tonks turns around. (mirror sprite)
            call ton_main("","base","base","base","ahegao", xpos="left", ypos="base",flip=True)
            pause.8

        "Ask her to remove her coat.":
            call ast_main("Yes, that should be easy.","smile","base","base","mid")
            call ton_main("................................","base","base","base","ahegao")
            call ast_main("Tonks, I command you to remove your coat.","open","closed","base","mid")
            call ton_main("*Huh?*","open","base","worried","ahegao")
            call ast_main("Come on, do it!","annoyed","base","angry","L")
            m "Try saying the magic word..."
            call ast_main("Imperio? But I already did-","open","wink","base","mid")
            m "No... Ask her politely..."
            call ast_main("Oh! I got it!","smile","closed","base","mid")
            call ast_main("Professor Tonks, please remove your coat for me...","open","base","base","L")
            call ton_main("*Hmmm*... okay...","base","base","base","ahegao")

            # Tonks removes her coat.
            call play_sound("equip")
            $ tonks_class.strip("robe")
            call ton_main("","base","base","base","ahegao", xpos="left", ypos="base",flip=True)
            pause.8


    call ast_main("Yes, she did it!","smile","base","base","L")
    call ast_main("What shall I have her do next?","base","base","base","mid")
    m "*hmmm*................."

    $ d_flag_01 = False

    label ag_st_imperio_E2_choices:

    menu:
        m "Make her..."
        "Do pig-noises again!" if d_flag_01 == False: # Jumps back to choices.
            $ d_flag_01 = True

            call ast_main("Do a pig-noise?","open","base","worried","mid")
            call ton_main("*oink!*","horny","base","base","ahegao")
            call ast_main("She did it!","smile","closed","base","mid")
            g9 "Well done!"
            call ast_main("Do it again!","smile","base","angry","L")
            call ton_main("*oink!*","open","base","worried","ahegao")
            call ast_main("*hi-hi-hi-hi!*","smile","closed","base","mid")
            m "I believe that's enough-"
            call ast_main("Do it again! Ten times!","clench","narrow","angry","L") # Angry
            call ton_main("*oink*{w=0.8}-*oink*{w=0.8}-*oink*{w=1.2}-*oink*{w=0.8}-*oink*{w=1.4}-*oink*{w=1.4}-*oink*{w=1.6}-*oink*{w=2.0}-*oink*{w}-*oink!*","open_wide_tongue","base","base","ahegao")
            m "......................."
            call ast_main("Agai-","scream","closed","angry","mid", trans="hpunch")
            g4 "That's enough, Astoria!"
            call ast_main("Fine...","annoyed","narrow","angry","R")

            # Tonks returns to normal
            with fade

            call ton_main("Oh wow...","angry","base","worried","down")
            call ton_main("You made me squeal like a pig!","smile","happyCl","base","mid")
            call ton_main("That was quite good!","base","base","base","mid")
            call ast_main("Thank you!","open","base","base","down")
            m "..."
            m "I have to say, I'm not that impressed..."
            call ton_main("You aren't?","open","base","raised","mid")
            call ast_main("But, Professor!","clench","base","worried","mid")
            m "Tonks, would you please do the noise again..."
            call ton_main("The noise, Professor?","angry","base","sad","mid")
            m "Yes. Squeal for me."
            call ton_main("Very well...","base","base","worried","down")
            call ton_main("*oink*-*oink!*","open","base","worried","mid")
            g9 "See, I don't even have to use magic to make her do it!"
            call ton_main("Very funny, Sir...","open","closed","base","mid")
            m "I'd like us to try this again..."
            call ton_main("Right now? Are you sure?","open","base","raised","mid")
            g4 "(I want to see some tits - damnit! Or hear her talk dirty...)"
            m "Yes, cast that spell again, Astoria..."
            call ast_main("Very well, Sir...","smile","closed","base","mid")

            # Astoria casts imperio.
            hide screen tonks_main

            call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch") # Screams it even louder

            call hide_characters
            with d3
            pause.2

            # chibi spell animation.
            with hpunch
            pause.8

            call ast_main("","clench","base","angry","L", xpos="base", ypos="base")
            call ton_main("*hmmm*.............","base","base","base","ahegao", xpos="right", ypos="base")
            call ast_main("And now?","open","base","base","mid")

            jump ag_st_imperio_E2_choices

        "Let her say something naughty!": # Fails
            call ast_main("*Huh?*...","open","base","worried","mid")
            g9 "Wouldn't you like to hear your teacher say something shameful?"
            call ast_main("Yes!","smile","base","angry","L")
            call ast_main("And what exactly?","clench","base","base","mid")
            m "I don't know... You should think of something..."
            m "You're the one with the magic-stick, after all..."
            call ton_main(".......................","base","base","base","ahegao")
            call ast_main("Okay... Professor Tonks...","open","base","worried","L")
            call ast_main("I want you to repeat after me...","open","closed","base","mid")
            call ton_main("...................................","horny","base","base","ahegao")
            call ast_main("I - am - a-","open","base","worried","L")
            call ton_main("I am a...","open","base","base","ahegao")
            call ast_main("dirty! - filthy! - pig!","open","narrow","base","L")
            call ton_main("...................................","base","base","base","ahegao")
            call ast_main("Go on, say it!","clench","narrow","base","L")
            call ast_main("I'm a dirty - filthy - pig!","open","closed","base","mid")
            call ton_main("*hi-hi!*...","angry","happyCl","base","mid")
            call ast_main("SAY IT!","scream","base","angry","L") # Scream
            g4 "Time-out!"
            call ast_main("No! She has to do what she's told!","clench","narrow","angry","mid")
            m "She clearly isn't going to..."
            m "We should take a break here..."
            call ast_main(".......................","annoyed","narrow","angry","mid")

            # Tonks returns to normal.
            pause.2
            call hide_characters
            hide screen bld1
            with fade
            pause.8

            call ast_main("","annoyed","base","angry","mid", xpos="right", ypos="base")
            call ton_main("*huh*...","open","base","worried","mid", xpos="base", ypos="base")
            call ton_main("Well that was something, wasn't it?","smile","happyCl","base","mid")
            call ast_main("..................................","annoyed","narrow","angry","L")
            m "You resisted her curse again."
            call ton_main("Yes...","upset","base","worried","L")
            call ton_main("I'm sorry, honey!","open","base","sad","L")
            call ast_main("..................................","annoyed","narrow","angry","down")
            call ton_main("You can't expect to succeed right away now, can you?","open","base","sad","L")
            call ton_main("To master a spell it takes time - and regular practicing...","open","closed","base","mid")
            call ton_main("Or else anyone could do it.","base","base","base","mid")
            call ton_main("We'll try again next time...","base","base","sad","L")
            call ast_main("............................","upset","narrow","base","down")
            call ton_main("Have a good night, Professor.","base","base","base","mid")

            call ton_walk(xpos="door", ypos="base", speed=2)
            call ton_chibi("stand","door","base", flip=False)
            with d3
            pause.2

            call ton_main("After you, Astoria.","open","base","base","L", ypos="head")
            call ast_main("...........................","upset","base","base","L", ypos="head")

            # They both leave
            #call ast_walk(action="leave", speed=2.5)

            call play_sound("door")
            call ton_chibi("hide")
            with d3

            $ ast_mood += 12

            # Event fails.
            $ ag_st_imperio.fail()

            call bld
            m "I don't think we made much progress here..."

            jump main_room

        "Make her show us those tits!": # Succeeds
            call ast_main("What?","clench","base","base","mid")
            g9 "Have her show us her breasts!"
            call ast_main("Professor?!","open","closed","worried","mid")
            m "You did the same to Susan, didn't you?"
            call ast_main("Yes, but...","open","narrow","worried","mid")
            call ast_main("I doubt Professor Tonks would be ok with that!","clench","narrow","base","L")
            m "Did you have those concerns with Susan as well?"
            m "Just try it."
            m "She can refuse to do it if she doesn't want to..."
            call ast_main("I suppose...","annoyed","base","base","L")
            call ast_main("Professor Tonks, I'd like you to show us your...","open","base","base","mid")
            call ast_main("*uhm*...","upset","base","base","down")
            call ast_main("Your breasts!","clench","closed","base","mid") # embarrassed
            call ton_main("Oh...","open","base","raised","ahegao")
            call ton_main("............................","angry","base","worried","ahegao")
            g4 "(Fingers crossed!)"
            call ton_main("............................","angry","wide","worried","ahegao_intense") # Clenched teeth
            call ast_main("I think she's struggling!","smile","base","base","L")
            g4 "Very good, girl!"
            g4 "Pressure her more! I want to see those puppies!"
            call ast_main("Professor Tonks, show us your breasts! Now!","open","base","angry","L")
            m "(It was easier for her to resist doing pig-noises...)"
            m "(Could it be that she {b}wants{/b} to show them to us?{w} And is resisting that inner urge?)"
            call ton_main("................................","angry","wide","sad","ahegao_intense") # Really struggling!
            g4 "(What a slut!)" # Small text
            call ast_main("Come on, do it!","clench","narrow","angry","L")
            call ton_main("*Hnnnngh!*...","angry","wide","sad","ahegao_intense")
            call cum_block
            call ton_main("*Aaaaahhh*...","open_wide_tongue","base","worried","ahegao") # Relieved
            g4 "(Did she just?!)"
            m "..."
            m "Girl, I think your teacher is done for..."
            call ast_main("What?","clench","base","worried","mid")
            m "She \"broke the curse.\" You can stop now..."
            call ast_main("*Aww*...","upset","narrow","base","down")
            call ast_main("If you say so, Professor...","annoyed","base","base","mid")

            # Tonks returns to normal.
            pause.2
            call hide_characters
            hide screen bld1
            with fade
            pause.8

            call ast_main("","annoyed","base","base","mid", xpos="right", ypos="base")
            call ton_main("Ouch... That was painful!","angry","closed","angry","mid", xpos="base", ypos="base")
            call ton_main("You nearly got me there.","smile","base","worried","mid")
            call ast_main("Did I really?","smile","base","base","mid")
            call ton_main("Yes, well done, Astoria!","base","base","base","L")
            call ast_main("Thank you!","smile","closed","base","mid")
            m "Was it really such a struggle for you to not get your breasts out?"
            call ton_main("*Uhm*...","angry","base","worried","down")
            call ton_main("Yes!","angry","closed","sad","mid") # Embarrassed
            g9 "*He-he-he!*"
            call ton_main("Shall we wrap it up for today?","open","base","worried","L")
            call ton_main("I'm sure next time you'll have better luck, Astoria.","base","base","base","mid")
            call ast_main("Okay...","annoyed","base","base","R")
            call ton_main("Have a good night, Professor!","smile","happyCl","base","mid")
            m "See ya..."

            # They both leave
            call play_sound("door")
            # Call ast_chibi("leave")
            call ton_chibi("leave")

            call bld
            m "And they say I'm the big, bad pervert..."

            jump main_room


label ag_st_imperio_E3:
    # Astoria is more confident this time.
    # Tonks sais that she almost want to do the command.
    # Atoria lightens up hearing that.
    # Tonks encourages her more, but to no success.
    # Next time it will be a success for sure!
    # Astoria leaves. After she's left, Tonks tells you how she barely felt anything...

    "Dev Note" "Add 3rd event here."

    jump main_room


label ag_st_imperio_E4:
    ton "Astoria, would you come in here please..."
    ast "Do I have to?"
    ton "Yes, we already talked about this..."
    ast "Fine, whatever..."

    #Astoria walks in

    ast "..."
    ton "Astoria... isn't there something you'd like to say to our Professor?"
    m "........................"
    ast "Yes..."
    ast "Sir, I'm sorry about my behaviour during our last training session."
    m "Sure, no big dea-"
    ast "It was wrong of me to scream at Professor Tonks like that, or scream at you..."
    m "Fine. Let's just get to-"
    ton "And what else?"
    ast "I was disrespectful, selfish, and mean, and I should be thankful that you are granting me this opportunity."
    m "......................."
    ast "I'm well aware of what is at stake here, and I shall follow the rules from now on."
    ast "....................." # Looks away
    m "*Ahem* Could we please just get started?"
    g4 "(I'm dying to see some tits!)"
    ast "........................"
    ton "Very good, Astoria."
    ton "I'm proud of you [textheart]."
    ast "........................." # embarrassed
    m "......................."

    ton "So, let’s begin... Astoria, try and focus on what we went through today..."
    ton "Keep good track of your emotions after channeling the spell..."
    ton "Anger and rage will cause you to lose control - and eventually break the connection with the target..."
    ton "Do your best to be as thoughtful, nice, and endearing as you possibly can towards your target..."
    ton "The stronger the emotional bond the better."
    ton "So try to charm them a bit while you're at it!"
    ton "It is called charms for a reason, after all!"
    ast "....................."
    m "...................."
    ton "Not a very good joke - I gather..."
    m "I'm sorry. I was only half paying attention..."
    ton "Very well..."

    ton "Now then, let's get on with it, shall we?"
    ast "..................."
    ton "Astoria, as soon as I'm ready - I'd like you to-"

    # Astoria casts the spell.
    ast "Imperio!"

    m "......................"
    ton "*Aaaaah*..."
    ast "I'm getting really good at this!"
    ton "......................."
    ast "What shall I have her do, Professor?"

    m "How about..."
    "Make her turn around!": # She's facing Astoria
    ast "Very well, Sir."
    ast "Professor, please turn around for me..."
    ton "*hmm*... Yes!"

    # Tonks turns around

    ton "........................"
    ast "*uhm*..." # Astoria is uncomfortable

    "Let her face me!":
    ast "Okay, Sir."

    ast "And now?"
    g9 "Her coat! Tell her to take it off!"
    ast "Professor Tonks, please remove your coat for me."
    ton "Of course, honey! [textheart]"

    # Tonks removes her coat.

    g9 "You're doing great, Astoria!"
    g9 "It's like watching you teach a puppy new tricks..."
    ton ".........................." # ahegao
    ast "If you say so, Sir."
    m "Let's move on to the next trick, shall we?"
    g9 "Ask her to get those tits out!"
    ast "Her what?!"
    m "Her breasts, girl..."
    m "Tell her to remove her top."
    ast "Right now?"
    ast "But..."

    if tonks_flip == 1: # Facing Astoria
        ast "Can I at least tell her to turn around again?"
        m "Why? Scared of your teacher's enormous rack?"
        ast "What?{w} As if!"
        g9 "I doubt she'd like to show them to you anyway..."
        ton "......................" # Ahegao
        ast "............"
        m "Go on...."

    else: # Facing Genie
        ast "I'm not sure if she'd be okay with that."
        m "This again?"
        ast "You'd have to close your eyes first, Professor!"
        m "What?"
        m "Are you giving orders to me now as well, girl?"
        ast "Close your eyes!"
        m "Not a chance!"
        ast "......................."
        ast "It won't be my fault if she gets mad at you later!"
        m "Sure, whatever..."
        m "Go on already!"

    g9 "Let's get those tits out!"
    ast "Professor Tonks, I need you to remove your-... your shirt..."
    ton "................"
    g9 "!!!"

    # Tonks removes her top.

    if tonks_flip == 1: # Facing Astoria
        ast "Is she-... is she doing it?" # closed eyes
        ton "............." # horny
        g9 "Why don't you see for yourself?"
        g9 "Open your eyes, girl!"
        ast "I don't want to..."
        m "How rude..."
        g9 "It seems to me like your teacher would really like to show you something!"
        ast "...................." # eyes still closed
        ast "*Eeeeehig*..." # Weird sound.
        ast "...................." # Looks away
        g9 "That wasn't too bad now, was it?
        ton "......................." # ahegao

    else:
        g9 "Now would you look at that!"
        ton "................" # horny
        m "Those are some great breasts your teacher has there!"
        ton "................" # ahegao
        ast "I asked you not to look, Professor!"
        g9 "I don't believe she minds, does she?"
        ton "................" # ahegao

    m "*hmm*..."
    m "We might be able to push her even further!"
    ast "Further, Sir? How?"
    g9 "By getting her to remove the rest of her clothing, naturally!"
    ton ".............." # angry/horny expression
    g9 "What do you think? Want to give it a try?"
    ast "Would that really be necessary, Sir?"
    m "Yes - it - would."
    ast "We-... we could try again next time, Professor..."
    m "Next time?"
    m "Where did your enthusiasm go all of a sudden?"
    m "Weren't you so eager to practice this spell?"
    ast "Yes, but..."
    m "Yes?"
    ast "I don’t have to explain myself to you!"
    ast "..."
    m "..."
    ast "I should go to bed..."
    m "Is that so..."
    ast "I- *uhm*... I'm tired, Sir."
    ast "*yaaaaawn!*... See?"
    m "...................."
    m "Very well..."
    m "You are dismissed."
    ast "........................................." #embarrased

    # Astoria leaves and spell fades

    ton "Well, that was interesting..."
    m "Do you have any idea why she wanted to leave so abruptly?"
    ton "I have a couple of theories, actually..."
    m "*Mhmm*.........................."
    ton ".................." # horny stare
    ton "Would you like me to put my clothes back on?"
    g9 "Don't feel pressured!"
    ton "Very well, then..."

    # screenshake
    call nar(">Tonks gives her breasts a quick shake for you.")

    g9 "Sweet!"
    ton "..............."
    ton "She made some good progress today, unlike last time..."
    ton "And she was very polite!"
    ton "But she isn't quite there yet..."

    m "Does she require more training?"
    ton "Yes, actually..."
    ton "She'll need a lot more training to pull off the Imperius curse properly..."
    ton "And, as you could see,...it doesn't have much of an effect on me."
    ton "I could have easily avoided doing everything she's told me today, if I wanted to..."
    g9 "But you didn't!"
    ton "It wasn't my intention to break her spirit again... She was really trying!"
    ton "Now, as you know, I'm a trained Auror..."
    g9 "A very \"talented\" one at that!"
    ton "Are you just praising my tits, Sir?"
    m " Every part of your body is worthy of praise!"
    ton "Well... thank you, [ton_genie_name]."

    # Screenshake
    call nar(">Tonks gives her breasts another quick shake for you.")

    ton "I suggest we do one more training session, and then call it from there..."
    m "Sounds good to me..."
    ton "Believe me, it's gonna be a great one!"
    g9 "Are we going to see more of your...talents?"
    ton "How would you like to see *all* this Auror has to offer?" # horny
    g9 "Looking forward to it!"
    ton "Have a good night, [ton_genie_name]!"

    # Tonks leaves.

    g9 "I hope she's planned something big!"


    jump main_room


label ag_st_imperio_E5:
    # She does it to make Astoria look good, even though she's still not good enough with the curse.
    # She starts stripping, and then climbs your desk.
    # You start jerking-off. And suggest to Astoria that Tonks should get under your desk...
    # Suddenly Snape enters again, and asks what the fuck is going on.
    # The curse interrupts. You tell Astoria to leave.
    # You and Tonks explain it to Snape.
    # Tonks will remain naked for the rest of the event.
    # Tonks is flirty with him, and Snape is enjoying himself.
    # Tonks tells you the do's and don't when cursing Susan.
    # Then they both leave...

    ton "Hi, Professor!"
    ast "Hello." # Happy
    m "All cheered up today, Astoria?"
    ast "Yes, Sir."
    ton "She should be. We made some real progress today."
    ton "I'm very impressed with her, I've got to say!"
    ton "She's very close to mastering it!"
    ast "Really?!"
    g9 "Is that so?"
    g9 "Care for a demonstration?"
    ton "Of course."
    ton "I’m confident you’ll be able to make me do *anything* you want today." # Horny stare
    g9 "Counting on it!"
    ton "Make sure to give her some good suggestions, Professor!"
    g9 "Absolutely!"
    ton "And Astoria..."
    ton "Today we are going to try to push me to the limit."
    ton "You will have me do whatever Professor Dumbledore commands, without question!"
    ast "I suppose..."
    ton "We will only stop with today's training once I'm able to...resist, am I clear?"
    ast "Okay, Professor..."

    ton "You may start now, Astoria..."
    ton "..................."
    ast "..................."
    ton "Astoria? Would you cast the curse - please?"
    ast "..................."

    # Astora casts the curse.
    ast "Imperio..."
    # screenshake

    ton "*hmmmm*............"
    g9 "(Here we go!)"
    ast ".............."
    ast "What should we start with, Professor?"
    m "Let's just try the same things as last time..."
    m "Ask her to take that coat off first."
    ast "Very well..."
    ast "Professor, would you please take off your coat?"
    ton "*hmm*... My coat?..."
    ton "..............."
    ton "Sure [textheart]"

    # Remove coat.

    ast "Yay!"
    ast "Her shirt was next, right?"
    m "That is correct."
    ast "Yes! Take off your shirt, Professor!" # menacing
    ton "*Ahhh*................"

    # Remove top.

    ast "She did it!"
    m "Well done!"
    m "Next, I'd like you to-"
    ast "Ask her to take off her TROUSERS!"
    g9 "Yes please!"
    ast "Professor, please take off your trousers..."
    ton "*hngh*..."

    # Removes trousers.

    ast "Oh wow..."
    ton "..................."
    ast "Professor, how can it be that you're not wearing any underwear?!" # angry embarrassed
    m "Yes, Miss Tonks."
    g9 "Explain yourself!"
    ton "*Hmmm*......."
    ast "Answer us!"
    ton "I don't like to wear them..."
    ast "Why?!" # angry
    ton "I feel so much better without a bra on...or panties..."
    ast "You're a teacher! This is disgusting!"
    g4 "Dis-{w=0.8}gusting!"
    ton "{image=textheart} {image=textheart} {image=textheart}"
    ast "I can't believe my teacher is such a slut!"
    g4 "Des-{w=0.8}picable!"
    ast "Are you a slut, Professor?"
    ton "..............." # ahegao
    ast "Are you?!"
    ton "I am! {image=textheart}"
    ast "I knew it!"
    ast "That's why she has such difficulty resisting our commands!"
    m "Yes. She’s clearly trying her hardest..."
    ast "Professor Dumbledore, you knew exactly what her weakness would be!"
    m "I did?"
    m "*ahem*... I mean-{w} of course I did!"
    ast "We're taking off her clothes, because that's what she enjoys! But could never do in school!"
    ast "Which makes it easier for me to channel the Imperius curse..."
    ast "Because she's nothing but a weak-minded slut!" # angry
    ton "................" # ahegao
    m "You're on point!"

    ast "Take off the rest of your clothes!" # angry
    g9 "Yes!"
    ast "Take them off, you slut!" # scream
    ton "........{image=textheart}"

    # Strip naked. Removes clothes and stockings.

    ast "Look, Professor!"
    ast "I got her to be completely naked!"
    m "Excellent work, [astoria_name]!"
    ast "Thank you, Sir!"
    ton "............."

    #screenshake
    call nar(">Tonks gives her tits a little sway...")

    g4 "*argh!* (I can't take it anymore!)"

    g4 "..."
    menu:
        "Start masturbating!":
            $ masturbating = True
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerk_off_behind_desk")
            with d5
            pause.8

            show screen bld1
            call nar(">You take out your cock and start jacking-off.")

    ast "What shall we do now?"
    "fap-fap-fap"
    ast "Professor?"
    m "What?"
    m "Oh..."
    g9 "Get her to climb my desk next!"
    g9 "Have her do a little dance for us."
    ast "Did you hear him, Professor?"
    ast "Get on that desk, and start dancing!"
    ton "..........."

    # Climb desk and dance.

    m "This is getting better and better..."
    "fap-fap-fap"
    ast "Move your hips!"
    ton "............"
    ast "She’s really doing everything I tell her!"
    ast "Look how easy it is, Professor!"

    call nar(">Astoria joyfully jumps up and down on the spot, making a happy squeal, while dropping her wand unknowingly...")

    m "*Uhm*..."
    ast "What's next, Professor?"
    m "Next?"
    ast "What else should we make her do?"
    ast "Can I walk her around school like this?"
    m "What?"
    m "Are you serious?"
    ast "Please!"
    ton ".............."
    m "(That might be a good idea for another time...)"
    m "Not today, I'm afraid..."
    ast "*Aww*..."
    g9 "Don't worry, I have an even better idea!"
    g9 "Could you ask her to get under my table?"
    ast "*Huh?*... To do what?"
    ton "To give him a blowjob..." # Tonks answers for Genie
    ast "Professor Tonks!{w} Are you serious?" # shocked
    ast "Why would she want to do that? That's disgusting!!!"
    m "That- *uhm*..."
    m "That wasn't what I would have suggested, but..."
    m "I'm willing to give her a chance to try..."
    m "Try to resist that urge, naturally..."
    ast "As long as I don't have to look at it..."
    ast "Professor Tonks, you can climb under Professor Dumbledore's desk...and..."
    ast "Do \"that\" thing..."
    ton "............."
    call nar(">Without hesitation, Tonks climbs down your desk to join you.")

    # Snape enters...
    sna "Genie, I was wondering if you could-"

    # Record Scratch
    sna "!!!"
    ast "*Huh?!*"
    ton "Shit!"
    ast "*Aaaaaaaaaah!!!*......................." # Screams
    m "What's going on?"
    sna "Yes! I'd like to know that as well!"

    if hg_strip.trigger == True: # Snape saw Hermione strip
        g4 "Damnit, not you again!"
        g4 "(You walking cock-block!)"

    else:
        g4 "Damnit, what are you doing here?"

    sna "You two better explain to me what I just witnessed!"
    sna "What on Earth is going on here?!"

    # Tonks climbs up the desk again.

    ton "Stop being such a wuss, Severus!"
    ton "We were just practicing some spells - with Miss Greengrass."
    sna "And that required you to be undressed? In front of a student?"
    ton "Well... she caused it..."
    sna "Caused you to strip? Which spells are you teaching that girl?!"
    sna "Don't tell me you-" # Shocked
    ton "The Imperius Curse."
    sna "I can't believe you two..."
    ast "Am I in trouble now, Professor?" # Asking Snape
    sna "Keep quiet, girl!"
    sna "............" # Snape sees the wand.

    sna "Is that your wand lying on the ground there?"
    ast "My wand?"
    ast "Oh no, I must have dropped it when you came in, Sir."
    sna "Well, pick it back up!"
    sna "A Slytherin takes better care of her equipment..."
    ast "Yes, I'm sorry, Professor."
    sna "You may leave, Astoria."
    ast "..."
    sna "Miss Greengrass..."
    ast "Yes sir."

    #astoria leaves

    # Tonks hops off your desk and stands closer to Snape.

    sna "........................."
    ton "Like what you see?" # Bit flirty, maybe just to calm Snape down.
    sna "............................." # blushing
    m "You couldn't have picked a worse time to burst in here..."
    sna "I can imagine that..."

    sna "So, Nymphadora..."
    ton "*Tzzzzs!*......"
    sna "Would you mind explaining to me why you were naked in the headmaster's office - with a student present?"
    sna "One of my students - at that."
    ton "Are you jealous?"
    sna "............"

    sna "The question..."
    ton "It’s this Astoria girl... there’s something wrong with her...."
    ton "She’s cursed you see!"
    ton "A blood curse... very unfortunate."
    sna "A blood curse you say?" #incredulous
    sna "Now that sounds serious..."
    ton "Yes, very serious!"
    ton "Been in her family for generations even."
    sna "And what are the effects of this \"Blood curse\" exactly?"
    ton "Well... I believe that this curse has rendered her practically asexual!"
    sna "What nonsense..."
    m "........................."
    ton "How dare you!"
    ton "I can recognize someone that's under a curse!"
    ton "I've been an auror for three years now, I’ll have you know!"
    sna "Working at that precious ministry of yours has really rubbed off on you, hasn't it?"
    m "That’s enough, Severus."
    sna "..."
    m "What business is conducted in this office is none of your concern."
    m "You’re excused..."
    sna ".................."
    sna "Very well..."
    sna "Genie...{w} Nymphadora..."
    ton ".................." # Angry stare

    #Snape leaves

    ton "Thank you..."
    m "..."
    m "Now..."
    menu:
        "-Prompt her to be honest with herself-":
        	m "I think it’s time for some honesty."
        	ton "Regarding?"
        	m "Everything that we’ve been doing with the Astoria girl."
        	ton "Oh..."
        	ton "Well, we’ve been helping her haven't we?"
        	ton "She’s such an uptight and oppressed little cut- girl."
        	ton "..."
        	ton "How can I not help her, even if she is a slyther...{w=0.5}{nw}"
        	m "Miss Tonks… You aren’t convincing anyone."
        	ton "To think such an innocent girl could be the victim of such an...{w=0.6}{nw}"
        	m "Tonks!"
        	ton "Alright..." #exasperated
        	ton "The blood curse may have been a little white lie on my part."
        	m "And?"
            ton "And the imperio training with Astoria may have been for my own benefit."
            m "..."
        	ton "Having her cast it on me was exclusively for my own personal enjoyment."
        	m "(What a surprise...)"
        	m "Why weren’t you honest with me?"
        	ton "*Sigh*"
        	ton "Perhaps I’ve been taking this favour business... thing a bit too lightly."
        	ton "I’ve been telling myself that it’s as much for the students benefit as it is my own."
            ton "\"I’ll help them explore their sexuallity, it’ll do them good.\""
        	m "We both know that is not the reason why we’re doing this."
        	ton "Yes..."
        	ton "A small voice in my head knows it...  and I can’t help that I’m just so god...{w=0.4] damn...{w=0.3} horny!"
            ton "All the bloody time!"
        	m "You should stop lying to yourself, it’s not healthy..."
            m "I’m immortal and even I know that!"
        	m "Embrace why you chose to be a part of this, you’ve got a pretty good gig here."
        	ton "Yes, you’re right."
        	m "You’re doing this for yourself, it’s okay to be selfish. Think about how much you’ve endured at that ministry."
        	ton "..."
        	g9 "Think of it as your reward, the students should be happy to have such a loving teacher as you."
        	ton "Thank you... sir."

        "-Call her out on her bullshit-":
            m "I think there’s someone who hasn’t been very honest here..."
            ton "Sorry?"

            #Music changes and darker overlay on screen
            m "You seem to think you’re above what we’re doing here. That you’re doing the students a favour rather than accepting it’s for your benefit."
            m "So, do know what I think?"
            ton "N-no..."
            m "I think that you’ve been fabricating this curse to get what you really wanted all along."
            m "Not for the good of Miss Greengrass..."
            ton "..."
            m "Someone’s been a naughty girl... acting all innocent with the ones that welcomed her into their scheme..."
            m "Or perhaps you’ve been trying to justify your actions... to yourself?"
            m "Is that right?"
            ton "That’s..."
            m "I think we both know what this means don’t we?"
            m "Miss Tonks..."
            m "What this means is that you’re no different than Snape and I."
            m "But you have yet to accept it.... and if you’re unable to, well in that case..."
            ton "I can! I have!"
            m "Are you sure? Because if you’re not in on this one hundred percent. Perhaps this may have been a mistake."
            ton "I..."
            g9 "Say it!"
            m "I’m in... One hundred percent..."
            g9 "..."
            m "Good, you’re doing this for yourself and nobody else...you’d do good to remember that."
            ton "Yes sir."

    #Overlay goes away and music returns to normal

    m "Now, with that out of the way..."
    m "Are you ready to take this to the next step?"
    m "Have you considered letting miss Greengrass cast the curse on a more susceptible subject?"
    ton "..."
    m "Miss Tonks..."
    ton "Fine, let’s do it!"
    g9 "Good."
    g9 "Do you have a student in mind... someone weak minded perhaps?"
    g9 "That Susan girl... How about her?"
    ton "Susan Bones?"

    # Tonks looks concerned (Blue)
    ton "But, she is a Hufflepuff... I used to be..."
    m "I don’t see how that makes any difference..."
    m "Remember why we’re doing this, you want Miss Greengrass to be able to curse you properly, correct?"
    ton "Yes..."
    m "Until then I will go ahead with the training... alone, any objections?"
    ton "No sir..."
    m "Make sure to obliterate her afterwards."
    ton "Erase her memory?"
    m "That’s what I said."
    m "Well then, I believe we’re done here..."
    ton "..."
    ton "Good luck with the training."
    m "Good night miss Tonks."

    call nar(">Astoria has \"mastered\" the imperio curse!")

    $ ag_st_imperio.complete = True

    jump main_room
