

### Kissing ###

# ([tonks_name] makes out with her students...)


label nt_pr_kiss_start:

    if ton_tier == 2:

        if nt_pr_kiss.points == 0:
            m "Ready to try something a little different?"
            call ton_main("Mmmm, you bet... This is the most fun I've had in years!","base","base","base","mid")
            call ton_main("What were you thinking we try out next?","base","base","base","mid")
            m "What do you think?"
            call ton_main("I know you shot it down earlier... but I think making-out with them would be really fucking hot...","base","base","base","mid")
            m "Pfft, you're such a girl."
            m "You've already gotten to second base, let's not jump back to first!"
            call ton_main("You don't understand... The way I make-out... It's way more intense than anything these kids will have ever experienced...","base","base","base","mid")
            m "Hmmmm... So you're not just going to give them a peck on the cheek, are you?"
            call ton_main("Oh no...","base","base","base","mid")
            call ton_main("They'll be lucky if they can talk straight after I'm done with them...","base","base","base","mid")
            m "In that case, you have my permission..."
            m "Just don't disappoint me with the stories you bring back!"
            call ton_main("I'll make sure you get your money's worth, don't worry.","base","base","base","mid")
            m "Just see me after class."
            call ton_main("Yes, sir!","base","base","base","mid")

        else:

            m "Fancy another student-snog-session?"
            call ton_main("Mmmm, you bet... It's my job to teach these kids...","base","base","base","mid")
            call ton_main("Even if that lesson is French Kissing...","base","base","base","mid")
            m "Well, don't let me stop you."
            call ton_main("Thank you, sir...","base","base","base","mid")

    elif ton_tier >= 3:

        if nt_pr_kiss.points == 0: # Tell her to be even lewder for the next level of favors.

            m "How would you feel about French kissing your students again?"
            call ton_main("Mmmm... Pretty good if the last few times are anything to go by...","base","base","base","mid")
            call ton_main("I'll see you after class then.","base","base","base","mid")
            m "Very good..."

        else: # Repeat
            m "Would you like to help your students with their oral skills again?"
            call ton_main("Mmmm, yes... Some of these kids are in dire need of some practice...","base","base","base","mid")
            g9 "Then go and practice with them!"
            call ton_main("I will, [ton_genie_name]...","base","base","base","mid")

    # Tonks leaves

    $ nt_pr_kiss.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_kiss_T1_intro_E1: # Tier 1 - Event 1 - Slytherin boy
    #Gentle kissing
    m "Fun day?"
    call ton_main("It was! I got to show the kids a Boggart for the first time, that was pretty entertaining!","base","base","base","mid")
    call ton_main("Not to mention I got to take a boys first kiss...","base","base","base","mid")
    m "A day of firsts then..."
    call ton_main("Mmmm, I know which one I preferred...","base","base","base","mid")
    m "Care to fill me in?"
    call ton_main("Alright...","base","base","base","mid")
    call ton_main("So, I had class with my favourite little \"Slythinerin\" today.","base","base","base","mid")
    call ton_main("I figured that I didn't really have much to do after classes so I may as well hold him back.","base","base","base","mid")
    call ton_main("He was expecting me to buy a favour from him straight away, however, I was in the mood for a little conversation today...","base","base","base","mid")
    call ton_main("We talked about his performance in class... him being so distracted...","base","base","base","mid")
    call ton_main("Then I asked him if he had a girlfriend to help with his distractions...","base","base","base","mid")
    call ton_main("He answered no of course, so I pretend to sympathize, saying it must be hard for him to walk around school with all the pretty thing running around.","base","base","base","mid")
    call ton_main("I then asked if he'd made out with any of the girls...","base","base","base","mid")
    call ton_main("He hadn't even kissed anyone before!","base","base","base","mid")
    call ton_main("So, obviously I had to buy a favour off of him...","base","base","base","mid")
    call ton_main("It's my duty as a teacher of this school to see to my students education.","base","base","base","mid")
    m "How noble."
    call ton_main("Not to mention, he was so excited by the whole thing.","base","base","base","mid")
    call ton_main("You should have seen his face light up... It was precious.","base","base","base","mid")
    m "Was it as intense as you promised?"
    call ton_main("Not really... I wanted to take it slow for his first time...","base","base","base","mid")
    call ton_main("I just sat next to him and slowly peppered a few kisses on his lips at first...","base","base","base","mid")
    call ton_main("After the initial shock and nerves, we were Eventually able to settle into a nice rhythm of kissing and some light tongue play...","base","base","base","mid")
    call ton_main("He was still inexperienced, but definitely eager to learn.","base","base","base","mid")
    call ton_main("Then, after five minutes I paid him his points and sent him on his way...","base","base","base","mid")
    m "Just like that?"
    call ton_main("I don't think it's the last I'll see of him, besides I don't want to push him too far.","base","base","base","mid")
    call ton_main("This favour trading might actually be a good way to address student behavior!","base","base","base","mid")
    m "Oh?"
    call ton_main("His behavior has really started to improve after I've started buying favours from him.","base","base","base","mid")
    m "Maybe you should consider dealing with all your troublemakers this way?"
    call ton_main("Hmmmm, don't tempt me...","base","base","base","mid")
    m "That'll be all then."
    call ton_main("See ya, [ton_genie_name].","base","base","base","mid")

    jump end_tonks_event


label nt_pr_kiss_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    m "You're a bit late... Get caught up having fun with your students?"
    call ton_main("Mmmm, and then some...","base","base","base","mid")
    m "I like the sound of that!"
    m "Now, care to elaborate?"
    call ton_main("Alright then, you old perv...","base","base","base","mid")
    call ton_main("Today was that shy, horny \"ravenclaw\" boy...","base","base","base","mid")
    m "The one who stayed behind by himself?" # Note: If the favors don't reference each other in such a direct way, we could make both "touch" and "kiss" available at the same time, playable independently to each other.
    call ton_main("Yep...","base","base","base","mid")
    call ton_main("Ugh... he made the classic school boy mistake today...","base","base","base","mid")
    m "Which is?"
    call ton_main("Calling your teacher \"Mommy\".","base","base","base","mid")
    m "hahaha! Really?"
    m "I bet he copped it for that!"
    call ton_main("Surprisingly not... Everyone just sort of went quiet.","base","base","base","mid")
    m "Hmmm. I know I would have given him hell for that..."
    call ton_main("Anyway... I decided that was plenty of reason to hold him back...","base","base","base","mid")
    call ton_main("Not that I needed to... Cheeky bugger didn't even get out of his seat...","base","base","base","mid")
    call ton_main("He just sat there with his head down... waiting for me to come over...","base","base","base","mid")
    call ton_main("So, I figured I'd indulge him... I walked over and plonked myself onto his lap, facing towards him...","base","base","base","mid")
    m "Mmmm, did he see that coming."
    call ton_main("No, although it didn't seem to bother him...","base","base","base","mid")
    call ton_main("He just looked up at me with this look in his eyes...","base","base","base","mid")
    call ton_main("It was too much... I started kissing him just to break our gaze...","base","base","base","mid")
    m "I assume he just sat there, taking it?"
    call ton_main("Oh no... He may have seemed shy... but kissing awoke something in him...","base","base","base","mid")
    call ton_main("It was like he wanted to kiss me as much as he could... ugh...","base","base","base","mid")
    call ton_main("I've never had someone attack me with their tongue like that...","base","base","base","mid")
    call ton_main("He was intense... if a little inexperienced...","base","base","base","mid")
    m "And what, you made out for a few minutes and sent him on his way?"
    call ton_main("A few minutes? Why do you think I'm so late?","base","base","base","mid")
    m "Wait... You mean to tell me you spent all afternoon, french kissing one of your students?"
    call ton_main("I didn't think it'd-","base","base","base","mid")
    m "I'm very proud. Good work, [ton_name]."
    call ton_main("...","base","base","base","mid")
    call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")

    jump end_tonks_event


label nt_pr_kiss_T1_E3: # Tier 1 - Event 3 - Slytherin girls
    #Tonks pays two best friends to make-out
    m "How was your day?"
    call ton_main("Better than most... You're going to love todays story!","base","base","base","mid")
    m "Don't let me stop you then."
    call ton_main("As always, there were a few \"slytherins\" messing around in class.","base","base","base","mid")
    call ton_main("There was an especially annoying pair of girls that wouldn't shut up.","base","base","base","mid")
    call ton_main("So, I pretty much had to give them detention, just to quiet down the class a little.","base","base","base","mid")
    call ton_main("Normally, I only try and buy favours from one person at a time...","base","base","base","mid")
    call ton_main("But I figured, if what they say about \"slytherin\" sluts is true this should be worth a shot.","base","base","base","mid")
    m "Did you take turns kissing the girls?"
    call ton_main("Better.","base","base","base","mid")
    call ton_main("I gave them the option of staying behind for detention for a full hour...","base","base","base","mid")
    call ton_main("Or sell their teacher a favour and get out of here in ten minutes...","base","base","base","mid")
    m "I take it they said yes?"
    call ton_main("Only after they negotiated out a price.","base","base","base","mid")
    call ton_main("But I tell you what, those hundred points were worth it.","base","base","base","mid")

    call ton_main("I convinced the two of them to make out with each other for a full ten minutes...","base","base","base","mid")
    call ton_main("Ugh... It was quite possibly the hottest thing I've ever witnessed in my life.","base","base","base","mid")
    m "Mmmm, more..."
    call ton_main("Well, the two of them are best friends, so naturally they were a bit hesitant to start...","base","base","base","mid")
    call ton_main("But I have a feeling that this wasn't their first time kissing girls...","base","base","base","mid")
    call ton_main("Maybe not even each other...","base","base","base","mid")
    m "Ugh... that's it..."
    call ton_main("I couldn't help myself... I had to play around while they did it...","base","base","base","mid")
    m "Did they care?"
    call ton_main("Big time... they whined about this not being included in the price...","base","base","base","mid")
    call ton_main("Not that it stopped them making out...","base","base","base","mid")
    call ton_main("They'd just take it in waves...","base","base","base","mid")
    call ton_main("Making out... calling me a pervert...","base","base","base","mid")
    call ton_main("Closing their mouths together only to break apart to call me a slut...","base","base","base","mid")
    call ton_main("Ugh... it was so {b}bloody{/b} {b}hot{/b}...","base","base","base","mid")
    call ton_main("Eventually they continued to call me a lesbo while saliva kept dripping down their faces...","base","base","base","mid")
    call ton_main("Fuck, I came so hard while they just sat there goading me on...","base","base","base","mid")
    call ton_main("Ugh... This really is the best job ever...","base","base","base","mid")
    m "You're telling me... That'll be all for now then Tonks."
    call ton_main("Yes, sir...","base","base","base","mid")

    jump end_tonks_event


label nt_pr_kiss_T1_E4: #Level 1 Event 4
    #Tender make-out sesh with slytherin lesbian
    call ton_main("Do I have a story for you today!","base","base","base","mid")
    call ton_main("This is so good I feel I should turn it into a feel-good, coming-of-age flick!","base","base","base","mid")
    m "About a boy snogging his teacher?"
    call ton_main("No! About a tender and confused young girl coming to terms with her sexuality thanks to her stunningly intelligent teacher.","base","base","base","mid")
    call ton_main("Starring our favourite little repressed \"Slytherin\"...","base","base","base","mid")
    call ton_main("Now, she's started coming around to me as of late...","base","base","base","mid")
    call ton_main("So, I figured now might be a good time to take it to the next level...","base","base","base","mid")
    call ton_main("Getting her to stay after class is easy enough now, I can just brush her hand as I walk around the class and throw her a subtle wink.","base","base","base","mid")
    m "You're getting brazen."
    call ton_main("Wasn't that the idea? To spread rumours?","base","base","base","mid")
    m "I never said it was a bad thing."
    call ton_main("Good. Because I'm not planning on slowing down. Not after today.","base","base","base","mid")
    call ton_main("She was so cute. Still nervous, but not nearly as cocky...","base","base","base","mid")
    call ton_main("Today, she just let her red cheeks do most of the talking as she hung her head towards her desk...","base","base","base","mid")
    call ton_main("All I had to do was ask to purchase another favour. It's not like she'd say no at this point.","base","base","base","mid")
    call ton_main("I don't think she was expecting me to ask for a kiss though... It really threw her for a loop...","base","base","base","mid")
    call ton_main("She couldn't work out whether it was too extreme a favour or too mild...","base","base","base","mid")
    m "Kissing can always be a bit weird at first..."
    call ton_main("especially when you're as emotionally charged as a horny little schoolgirl...","base","base","base","mid")
    call ton_main("Mmm... She didn't let me down...","base","base","base","mid")
    call ton_main("At first she just gazed up at me like a stunned deer... lips quivering in either fear or anticipation... I couldn't tell...","base","base","base","mid")
    call ton_main("Of course, I had to make the first move. I just swept in and placed my lips on hers... Ugh... they were so soft...","base","base","base","mid")
    call ton_main("After waiting for a little bit of her shock to wear off, I started probing the front of her mouth with my tongue...","base","base","base","mid")
    call ton_main("I thought she was going to try and close her teeth and keep me out but she was Surprisingly quick to open wide for auntie Tonks...","base","base","base","mid")
    call ton_main("After that it was game over for her... I just softly cradled her head as I spent the next five minutes teaching her how to french...","base","base","base","mid")
    call ton_main("Ugh... That's not an experience you get to live very often...","base","base","base","mid")
    m "Consider yourself lucky then."
    call ton_main("Oh, I do, believe me.","base","base","base","mid")
    m "Very good. That'll be all for now then tonks."
    call ton_main("Thank you, sir.","base","base","base","mid")

    jump end_tonks_event



label nt_pr_kiss_T2_E1: # Tier 2 Event 1 # Not in use.
    m "How did your extra-curricular activities pan out today?"
    call ton_main("Honestly? I don't think I've ever been as turned on in my life...","base","base","base","mid")
    call ton_main("Fuck... It was incredible... the power I felt over him... it was intoxicating...","base","base","base","mid")
    m "Care to elaborate?"
    call ton_main("Well, you know that stuck up little \"Slytherin\" I've been fooling around with?","base","base","base","mid")
    m "The guy or the girl?"
    call ton_main("The boy.","base","base","base","mid")
    m "Yep, I think I remember them..."
    call ton_main("I asked them to stay back after classes again... Even if it was by staring at them during class...","base","base","base","mid")
    call ton_main("Either way... He knew he had to stay behind to play with \"auntie\" Tonks...","base","base","base","mid")
    m "Kinky..."
    call ton_main("Mmmm, I walked over to him slowly... Making sure I savored that frightened look on his face...","base","base","base","mid")
    call ton_main("Then, I got to his desk... I was half expecting him to blabber on about not deserving to be there...","base","base","base","mid")
    call ton_main("But today he just looked up at me with a delectable mix of fear and anticipation...","base","base","base","mid")

    # Genie starts jerking off

    #">Unable to help yourself any longer, you start to inconspicuously stroke your cock under your desk."
    #call ton_main("*tsk* *tsk* *tsk*...{w} Couldn't help yourself, could you?"
    #m "Can you blame me?"
    #call ton_main("I suppose not..."
    #call ton_main("Anyway, back to that cute little thing..."

    call ton_main("Eventually I'd had enough of his eager expression...","base","base","base","mid")
    call ton_main("I pounced upon him... Sitting down on his lap, pinning him to his chair and forcing my chest into his...","base","base","base","mid")
    call ton_main("I could feel his heartbeat... It was so fast... Like a mouse...","base","base","base","mid")
    call ton_main("Whispering in his ear I asked if he wanted a little kiss...","base","base","base","mid")
    call ton_main("Making sure to let him know that I'd pay him plenty of points...","base","base","base","mid")
    call ton_main("Just for a kiss...","base","base","base","mid")
    m "Mmmmm..."
    call ton_main("Of course he said yes... Even if it was so faint I could barely hear it...","base","base","base","mid")
    call ton_main("But once he said it... I was on him...","base","base","base","mid")
    call ton_main("I pinned him down as I held his head in place...","base","base","base","mid")
    call ton_main("Ugh... My tongue was going crazy...","base","base","base","mid")
    call ton_main("I'm not sure if you remember this from school, sir, but I'm an Metamorphmagus...","base","base","base","mid") # Note: I'd wait with adding Tonks' abilities and reserve them for the 2nd level of favors (longer tongue, bigger breasts,...)
    call ton_main("Normally I just use that to blend in or for jokes...","base","base","base","mid")
    call ton_main("But sometimes I use it to... Play around...","base","base","base","mid")
    call ton_main("And all the excitement today may have caused me to lose control of my tongue...","base","base","base","mid")
    m "Lose control of your tongue?"
    call ton_main("Ugh... it was so long...","base","base","base","mid")
    call ton_main("It was like I was fucking that poor boys mouth with it...","base","base","base","mid") # Note: This section is a bit too extreme for the first level.
    call ton_main("I wrapped his tongue in mine... stuck it down his throat...","base","base","base","mid")
    call ton_main("Ugh... I even licked his face clean...","base","base","base","mid")
    call ton_main("By the time I was done there wasn't a dry spot on his face...","base","base","base","mid")
    m "Argh..."
    call ton_main("Poor thing... I think I broke him if I'm being honest...","base","base","base","mid")
    m "That's it..."
    call ton_main("I thought he'd like it... but there were so many tears-","base","base","base","mid")

    #g9 "UGH... THERE IT IS!!!"
    # Genie cums
    #">You begin firing a load of under your desk, making a dull thud with each blast hitting against the backboard..."

    call ton_main("Mmmm, looks like you enjoyed our little lesson as well...","base","base","base","mid")
    m "Ugh... can you blame me? That was... Ugh..."
    call ton_main("I told you I knew how to kiss...","base","base","base","mid")
    m "I believe you... that'll be all for now..."
    m "I need to clean up..."
    call ton_main("Very well... Thank you, sir.","base","base","base","mid")

    jump end_tonks_event

label tonks_teacher_event_3_6: #Level 2 Event 2
    #Spends afternoon making out with ravenclaw, topless

    return

label tonks_teacher_event_3_7: #Level 2 Event 3
    #Tonks has two best friends make out while she plays with herself

    return

label tonks_teacher_event_3_8: #Level 2 Event 4
    #Another make out sesh with slytherin involving tonks fingering the student

    jump end_tonks_event
