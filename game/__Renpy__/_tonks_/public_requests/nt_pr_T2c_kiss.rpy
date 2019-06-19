

### Kissing ###

# ([tonks_name] makes out with her students...)


label nt_pr_kiss_start:

    if ton_tier == 2:

        if nt_pr_kiss.points == 0:
            m "Ready to try something a little different?"
            ton "Mmmm, you bet... This is the most fun I've had in years!"
            ton "What were you thinking we try out next?"
            m "What do you think?"
            ton "I know you shot it down earlier... but I think making-out with them would be really fucking hot..."
            m "Pfft, you're such a girl."
            m "You've already gotten to second base, let's not jump back to first!"
            ton "You don't understand... The way I make-out... It's way more intense than anything these kids will have ever experienced..."
            m "Hmmmm... So you're not just going to give them a peck on the cheek, are you?"
            ton "Oh no..."
            ton "They'll be lucky if they can talk straight after I'm done with them..."
            m "In that case, you have my permission..."
            m "Just don't disappoint me with the stories you bring back!"
            ton "I'll make sure you get your money's worth, don't worry."
            m "Just see me after class."
            ton "Yes, sir!"

        else:

            m "Fancy another student-snog-session?"
            ton "Mmmm, you bet... It's my job to teach these kids..."
            ton "Even if that lesson is French Kissing..."
            m "Well, don't let me stop you."
            ton "Thank you, sir..."

    elif ton_tier >= 3:

        if nt_pr_kiss.points == 0: # Tell her to be even lewder for the next level of favors.

            m "How would you feel about French kissing your students again?"
            ton "Mmmm... Pretty good if the last few times are anything to go by..."
            ton "I'll see you after class then."
            m "Very good..."

        else: # Repeat
            m "Would you like to help your students with their oral skills again?"
            ton "Mmmm, yes... Some of these kids are in dire need of some practice..."
            g9 "Then go and practice with them!"
            ton "I will, [ton_genie_name]..."

    # Tonks leaves

    $ nt_pr_kiss.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_kiss_T1_intro_E1: # Tier 1 - Event 1 - Slytherin boy
    #Gentle kissing
    m "Fun day?"
    ton "It was! I got to show the kids a Boggart for the first time, that was pretty entertaining!"
    ton "Not to mention I got to take a boys first kiss..."
    m "A day of firsts then..."
    ton "Mmmm, I know which one I preferred..."
    m "Care to fill me in?"
    ton "Alright..."
    ton "So, I had class with my favourite little \"slythinerin\" today."
    ton "I figured that I didn't really have much to do after classes so I may as well hold him back."
    ton "He was expecting me to buy a favour from him straight away, however, I was in the mood for a little conversation today..."
    ton "We talked about his performance in class... him being so distracted..."
    ton "Then I asked him if he had a girlfriend to help with his distractions..."
    ton "He answered no of course, so I pretend to sympathize, saying it must be hard for him to walk around school with all the pretty thing running around."
    ton "I then asked if he'd made out with any of the girls..."
    ton "He hadn't even kissed anyone before!"
    ton "So, obviously I had to buy a favour off of him..."
    ton "It's my duty as a teacher of this school to see to my students education."
    m "How noble."
    ton "Not to mention, he was so excited by the whole thing."
    ton "You should have seen his face light up... It was precious."
    m "Was it as intense as you promised?"
    ton "Not really... I wanted to take it slow for his first time..."
    ton "I just sat next to him and slowly peppered a few kisses on his lips at first..."
    ton "After the initial shock and nerves, we were Eventually able to settle into a nice rhythm of kissing and some light tongue play..."
    ton "He was still inexperienced, but definitely eager to learn."
    ton "Then, after five minutes I paid him his points and sent him on his way..."
    m "Just like that?"
    ton "I don't think it's the last I'll see of him, besides I don't want to push him too far."
    ton "This favour trading might actually be a good way to address student behavior!"
    m "Oh?"
    ton "His behavior has really started to improve after I've started buying favours from him."
    m "Maybe you should consider dealing with all your troublemakers this way?"
    ton "Hmmmm, don't tempt me..."
    m "That'll be all then."
    ton "See ya, [ton_genie_name]."

    jump end_tonks_event


label nt_pr_kiss_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    m "You're a bit late... Get caught up having fun with your students?"
    ton "Mmmm, and then some..."
    m "I like the sound of that!"
    m "Now, care to elaborate?"
    ton "Alright then, you old perv..."
    ton "Today was that shy, horny \"ravenclaw\" boy..."
    m "The one who stayed behind by himself?" # Note: If the favors don't reference each other in such a direct way, we could make both "touch" and "kiss" available at the same time, playable independently to each other.
    ton "Yep..."
    ton "Ugh... he made the classic school boy mistake today..."
    m "Which is?"
    ton "Calling your teacher \"Mommy\"."
    m "hahaha! Really?"
    m "I bet he copped it for that!"
    ton "Surprisingly not... Everyone just sort of went quiet."
    m "Hmmm. I know I would have given him hell for that..."
    ton "Anyway... I decided that was plenty of reason to hold him back..."
    ton "Not that I needed to... Cheeky bugger didn't even get out of his seat..."
    ton "He just sat there with his head down... waiting for me to come over..."
    ton "So, I figured I'd indulge him... I walked over and plonked myself onto his lap, facing towards him..."
    m "Mmmm, did he see that coming."
    ton "No, although it didn't seem to bother him..."
    ton "He just looked up at me with this look in his eyes..."
    ton "It was too much... I started kissing him just to break our gaze..."
    m "I assume he just sat there, taking it?"
    ton "Oh no... He may have seemed shy... but kissing awoke something in him..."
    ton "It was like he wanted to kiss me as much as he could... ugh..."
    ton "I've never had someone attack me with their tongue like that..."
    ton "He was intense... if a little inexperienced..."
    ton "But my god... the most fun I've had in years!" # They don't really say "my god" in HP or reference god. "Merlin" is their stand in for that.
    m "And what, you made out for a few minutes and sent him on his way?"
    ton "A few minutes? Why do you think I'm so late?"
    m "Wait... You mean to tell me you spent all afternoon, french kissing one of your students?"
    ton "I didn't think it'd-"
    m "I'm very proud. Good work, [ton_name]."
    ton "..."
    ton "Thank you, [ton_genie_name]."

    jump end_tonks_event


label nt_pr_kiss_T1_E3: # Tier 1 - Event 3 - Slytherin girls
    #Tonks pays two best friends to make-out
    m "How was your day?"
    ton "Better than most... You're going to love todays story!"
    m "Don't let me stop you then."
    ton "As always, there were a few \"slytherins\" messing around in class."
    ton "There was an especially annoying pair of girls that wouldn't shut up."
    ton "So, I pretty much had to give them detention, just to quiet down the class a little."
    ton "Normally, I only try and buy favours from one person at a time..."
    ton "But I figured, if what they say about \"slytherin\" sluts is true this should be worth a shot."
    m "Did you take turns kissing the girls?"
    ton "Better."
    ton "I gave them the option of staying behind for detention for a full hour..."
    ton "Or sell their teacher a favour and get out of here in ten minutes..."
    m "I take it they said yes?"
    ton "Only after they negotiated out a price."
    ton "But I tell you what, those hundred points were worth it."

    menu:
        "-start jerking off-":
            ">Your arm slips into your robe, grabbing a hold of your cock and gently stroking it back to life."
            ton "...*tsk*"
            ton "At least I know I have your attention..."
            m "Mmmm... undivided."
        "-Pay attention-":
            pass

    ton "I convinced the two of them to make out with each other for a full ten minutes..."
    ton "Ugh... It was quite possibly the hottest thing I've ever witnessed in my life."
    m "Mmmm, more..."
    ton "Well, the two of them are best friends, so naturally they were a bit hesitant to start..."
    ton "But I have a feeling that this wasn't their first time kissing girls..."
    ton "Maybe not even each other..."
    m "Ugh... that's it..."
    ton "I couldn't help myself... I had to play around while they did it..."
    m "Did they care?"
    ton "Big time... they whined about this not being included in the price..."
    ton "Not that it stopped them making out..."
    ton "They'd just take it in waves..."
    ton "Making out... calling me a pervert..."
    ton "Closing their mouths together only to break apart to call me a slut..."
    ton "Ugh... it was so {b}bloody{/b} {b}hot{/b}..."
    ton "Eventually they continued to call me a lesbo while saliva kept dripping down their faces..."
    ton "Fuck, I came so hard while they just sat there goading me on..."
    ton "Ugh... This really is the best job ever..."
    m "You're telling me... That'll be all for now then Tonks."
    ton "Yes, sir..."

    jump end_tonks_event


label nt_pr_kiss_T1_E4: #Level 1 Event 4
    #Tender make-out sesh with slytherin lesbian
    ton "Do I have a story for you today!"
    ton "This is so good I feel I should turn it into a feel-good, coming-of-age flick!"
    m "About a boy snogging his teacher?"
    ton "No! About a tender and confused young girl coming to terms with her sexuality thanks to her stunningly intelligent teacher."
    ton "Starring our favourite little repressed \"slytherin\"..."
    ton "Now, she's started coming around to me as of late..."
    ton "So, I figured now might be a good time to take it to the next level..."
    ton "Getting her to stay after class is easy enough now, I can just brush her hand as I walk around the class and throw her a subtle wink."
    m "You're getting brazen."
    ton "Wasn't that the idea? To spread rumours?"
    m "I never said it was a bad thing."
    ton "Good. Because I'm not planning on slowing down. Not after today."
    ton "She was so cute. Still nervous, but not nearly as cocky..."
    ton "Today, she just let her red cheeks do most of the talking as she hung her head towards her desk..."
    ton "All I had to do was ask to purchase another favour. It's not like she'd say no at this point."
    ton "I don't think she was expecting me to ask for a kiss though... It really threw her for a loop..."
    ton "She couldn't work out whether it was too extreme a favour or too mild..."
    m "Kissing can always be a bit weird at first..."
    ton "especially when you're as emotionally charged as a horny little schoolgirl..."
    ton "Mmm... She didn't let me down..."
    ton "At first she just gazed up at me like a stunned deer... lips quivering in either fear or anticipation... I couldn't tell..."
    ton "Of course, I had to make the first move. I just swept in and placed my lips on hers... Ugh... they were so soft..."
    ton "After waiting for a little bit of her shock to wear off, I started probing the front of her mouth with my tongue..."
    ton "I thought she was going to try and close her teeth and keep me out but she was Surprisingly quick to open wide for auntie Tonks..."
    ton "After that it was game over for her... I just softly cradled her head as I spent the next five minutes teaching her how to french..."
    ton "Ugh... That's not an experience you get to live very often..."
    m "Consider yourself lucky then."
    ton "Oh, I do, believe me."
    m "Very good. That'll be all for now then tonks."
    ton "Thank you, sir."

    jump end_tonks_event



label nt_pr_kiss_T2_E1: # Tier 2 Event 1
    m "How did your extra-curricular activities pan out today?"
    ton "Honestly? I don't think I've ever been as turned on in my life..."
    ton "Fuck... It was incredible... the power I felt over him... it was intoxicating..."
    m "Care to elaborate?"
    ton "Well, you know that stuck up little \"Slytherin\" I've been fooling around with?"
    m "The guy or the girl?"
    ton "The boy."
    m "Yep, I think I remember them..."
    ton "I asked them to stay back after classes again... Even if it was by staring at them during class..."
    ton "Either way... He knew he had to stay behind to play with \"auntie\" Tonks..."
    m "Kinky..."
    ton "Mmmm, I walked over to him slowly... Making sure I savored that frightened look on his face..."
    ton "Then, I got to his desk... I was half expecting him to blabber on about not deserving to be there..."
    ton "But today he just looked up at me with a delectable mix of fear and anticipation..."

    # Genie starts jerking off

    ">Unable to help yourself any longer, you start to inconspicuously stroke your cock under your desk."
    ton "*tsk* *tsk* *tsk*...{w} Couldn't help yourself, could you?"
    m "Can you blame me?"
    ton "I suppose not..."
    ton "Anyway, back to that cute little thing..."
    ton "Eventually I'd had enough of his eager expression..."
    ton "I pounced upon him... Sitting down on his lap, pinning him to his chair and forcing my chest into his..."
    ton "I could feel his heartbeat... It was so fast... Like a mouse..."
    ton "Whispering in his ear I asked if he wanted a little kiss..."
    ton "Making sure to let him know that I'd pay him plenty of points..."
    ton "Just for a kiss..."
    m "Mmmmm..."
    ton "Of course he said yes... Even if it was so faint I could barely hear it..."
    ton "But once he said it... I was on him..."
    ton "I pinned him down as I held his head in place..."
    ton "Ugh... My tongue was going crazy..."
    ton "I'm not sure if you remember this from school, sir, but I'm an Metamorphmagus..." # Note: I'd wait with adding Tonks' abilities and reserve them for the 2nd level of favors (longer tongue, bigger breasts,...)
    ton "Normally I just use that to blend in or for jokes..."
    ton "But sometimes I use it to... Play around..."
    ton "And all the excitement today may have caused me to lose control of my tongue..."
    m "Lose control of your tongue?"
    ton "Ugh... it was so long..."
    ton "It was like I was fucking that poor boys mouth with it..." # Note: This section is a bit too extreme for the first level.
    ton "I wrapped his tongue in mine... stuck it down his throat..."
    ton "Ugh... I even licked his face clean..."
    ton "By the time I was done there wasn't a dry spot on his face..."
    m "Argh..."
    ton "Poor thing... I think I broke him if I'm being honest..."
    m "That's it..."
    ton "I thought he'd like it... but there were so many tears-"
    g9 "UGH... THERE IT IS!!!"

    # Genie cums

    ">You begin firing a load of under your desk, making a dull thud with each blast hitting against the backboard..."
    ton "Mmmm, looks like you enjoyed our little lesson as well..."
    m "Ugh... can you blame me? That was... Ugh..."
    ton "I told you I knew how to kiss..."
    m "I believe you... that'll be all for now..."
    m "I need to clean up..."
    ton "Very well... Thank you, sir."

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
