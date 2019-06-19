

label tonks_intro_E1:

    pause.5
    call bld
    call play_sound("knocking")
    "*Knock on door*"
    m "Who is it?"
    ton "It’s Tonks-"
    ton "*Ugh*..."
    ton "(...)"
    ton "Nymphadora Tonks, Sir."
    ton "Ministry of Magic, Auror division."


    if letter_favor_complaint_OBJ.read:
        g4 "(Oh shit, the fuzz...)"
        m "(I thought they would have forgotten about those damn letters by now...)"
        ton "Sir, I’m here to discuss an important matter with you regarding your students."
        m "(Governments are all the same with their bloody rules.)"
        ton "Sir?"
        m "(...)"
        m "Of course. Do come in..."

    else:
        m "(Another female?)"
        m "(She sounds a bit too old to be a student...)"
        g9 "(Better to just let my charm play...)"
        m "Yes... come in."

    #*Tonks walks in*

    call ton_main(face="neutral", xpos="right", ypos="base")

    ton "Thank you, Professor."
    m "(Oh shit, she’s hot...)"
    ton "I apologize for arriving unannounced... And a couple of days late..."
    ton "I had quite the *pleasant* encounter with a group of centaurs that moved too far out of their assigned territory."
    ton "I had to *convince* them to move back into the area that was given to them by the Ministry."
    m "(...)"
    ton "You'd never be able to guess how I did it... It's quite the story."
    m "(I bet she gave them all a blowjob...)"
    ton "Okay then, let’s get this over with."
    ton "So... Professor Dumbledore, are you aware of why the Ministry sent me here?"

    if letter_favor_complaint_OBJ.read:
        m "More or less..."
        ton "We have received a letter by a certain \"Hermione Granger\", about ongoing favour tradings here at this school."
        m "Yes she likes to do that..."
        ton "Trading favors?"
        m "(I wished...)"
        m "No. She likes to write letters... lots of 'em..."
    else:
        m "I can’t say that I do."
        ton "So you haven't had any complaints from students in regards to \"favour trading\"?"
        g4 "(Oh, fuck...)"
        g9 "That depends...{w=0.3} What sort of favours are you referring to?"
        ton "..."
        ton "Well, we’ve received a letter from Miss Hermione Granger."
        m "Oh, good..."
        g4 "..."

    ton "I take it you’re acquainted with Miss Granger?"
    m "Quite..."
    ton "Fantastic. So, the reason I’m here is because of said letter."
    ton "And to address the concerns this student has presented to the ministry."
    m "I see..."

    menu:
        "-You don't have any proof!-":
            m "We aren't selling sexual favours to our students."
            ton "Who said anything about sexual favours?"
            m "Shit..."
            ton "Go on..."

        "-What was mentioned in the letter?-":
            ton "Miss Granger wrote about several Slytherin girls that inquire to do favours for their male     teachers."
            m "So what?"
            ton "Those favours tend to be very \"sexual\" in nature."
            m "(Shit...)"

    m "Well, I can’t say I’m very well versed in these... very,{w=0.4} very rare occurrences."
    m "I was actually just about to begin my own investigation in the matter."
    ton "Don't worry about it, Professor."
    ton "The Ministry has sent me specifically to investigate in case there is any truth to Miss Granger's concerns."
    ton "I’ll be happy to look into this for you."
    m "Now, now. That shouldn’t be-"
    ton "Investigating is in my job description, after all..."
    ton "I’ll just stay for a little while to investigate the claims and question the students."
    m "But you can’t-"
    ton "Do have some confidence in me, Professor. This is what I was trained for..."
    m "Well, wait just one minute..."
    ton "Don’t worry, I’ve already gotten a room down in Hogsmeade."
    ton "I’ll be staying there so no worries about accommodations."
    m "Great..."
    ton "And you are not to speak to any of the other professors and students about our meeting. I’d like to keep my presence unknown."
    m "(...)"
    ton "Good day to you sir."

    # Tonks leaves.
    call hide_characters

    $ tonks_intro.E1_complete = True
    # Don't add event pause here!

    jump main_room


label tonks_intro_E2:

    "Dev Note" "Add knocking interaction."

    call ton_main(face="neutral", xpos="right", ypos="base")

    m "Hey! It's...{w} you again..."
    m "Found any evidence yet?"
    ton "Sadly no, Professor."
    ton "I haven't gotten a chance to investigate properly."
    ton "I’ve been rather occupied listening to Miss Granger's own investigations first."
    ton "That girl sure is something, isn't she?"
    ton "Not that I mind listening to her."
    ton "She gave me a very long report that went well into the evening, whilst I enjoyed a glass of firewhisky..."
    ton "She’s sure been very thorough in documenting the happenings she's witnessed..."
    ton "Anyhow, other than her documentation she had no proof of any illicit activities. It's all just accusations."
    ton "As much as I wish they were true..."
    m "Huh?"
    ton "So I could conclude my investigations early, of course."
    ton "And bring this favour trading business to an end, once and for all."

    # Tonks leaves.
    call hide_characters

    call bld
    m "Shit..."
    m "I better talk to Snape about this..."

    $ tonks_intro.E2_complete = True
    $ nt_event_pause += 1

    jump main_room


label tonks_intro_E3:

    call bld
    call play_sound("knocking")
    "*Loud kocking*"

    call play_sound("knocking")
    "*Knock on door*"

    m "............"
    call play_sound("knocking")

    ton "Professor Dumbledore, may I come in?"
    m "(It's that hot Ministry chick again...)"

    menu:
        "Yes, please come on in.":
            pass
        "Not right now.":
            ton "But it's urgent, Sir. I need to talk to you about Miss Granger's favour trading accusations..."
            g4 "(Shit. That can't be good.)"
            m "Do you mind coming another time, I’m very busy...{w} watering the bird."
            ton "Watering what?"
            ton "Sir, I’m coming in."
        "Who is it?":
            ton "It's Tonks."
            m "Who?"
            ton "..."
            ton "Nymphadora Tonks...{w=1.0} Ministry of Magic, Auror division."
            m "(Nympho-what?)"
            ton "Sir, I’m coming in."
            g4 "(Shit!)"


    #*Tonks enters the office*
    call ton_main(face="angry", xpos="right", ypos="base")

    ton "Thank you, Professor."
    m "How’s the investigation going? Nothing to report I gather?"
    ton "On the contrary..."
    ton "This school has changed since the last time I was here."
    ton "And I wouldn't say for the better..."
    ton "Teachers taking advantage of their students, selling them favours..."
    ton "While they abuse their authority and power to do the most despicable things to them..."
    ton "The Dumbledore I know would never agree to such debauchery..."
    m "(...)"
    ton "I had this suspicion... Since the very day I got here..."
    # Tonks threatens Genie.
    # Maybe have her chibi point her wand at him?

    ton "Now tell me, who are you? And you better tell the truth!"
    g4 "(Shit, how often is this going to happen to me?)"

    menu:
        g4 "I'm..."
        "Albus Dumbledore!":
            ton "You are most certainly *not* Albus Dumbledore!"
            g4 "No wait, it was Albertus Dumblerdore! That's it!"
            m "(Yes, that was probably it...)"
        "You know who!":
            ton "What?"
            m "You... know... who..."
            ton "That can't be true!"
            m "You know who I am. You said it yourself earlier."
            m "(If only I could remember what she called me...)"

    ton "I've had enough of this!"
    ton "Reveal who you are, dark wizard!"
    g4 "I'm not a dark wizard, you racist twat!"
    ton "What? How dare you call me a racist!"
    g4 "I'm not afraid of you! Bring it! Do your worst, witch!"
    call hide_characters
    hide screen bld1
    with d3

    # Glass break animation.
    # Duel won't happen and Tonks just casts a spell.

    call play_music("boss_theme")
    call play_sound("glass_break")
    pause.1

    show screen snape_glass
    pause 3
    show screen blkfade
    with d5

    hide screen snape_glass
    hide screen blkfade
    with d5
    pause.1

    call gen_chibi("hide")
    show screen dumbledore
    call cast_spell("revelio")
    call ton_main("Revelio!","open","base","angry","mid", hair="angry", ypos="head")
    call bld("hide")
    pause.6

    call gen_chibi("sit_behind_desk")
    hide screen dumbledore
    with d9
    pause.6

    call ton_main("","open","wide","wide","mid", xpos="right", ypos="base")
    m "(...)"
    call ton_main("No way!","open","base","base","mid")
    m "What just happened?"
    ton "What... are you...?"
    m "(Can she see through the illusion?)"
    ton "Wait a minute... Are you...{w} a Genie?"
    g4 "(This witch knows her shit...)"
    m "..."
    call play_music("playful")
    g9 "Some people would say I'm *the* Genie, actually!"
    m "The most powerful being in the entire universe... Multiple universes even.... Glad my reputation precedes me..."
    ton "How curious. I've never had one before..." # Tonks looks horny.
    m "What?"
    ton "I meant, I've never had the pleasure of meeting a Genie before. This is brilliant!"
    m "I'm flattered... But how were you able to tell?"
    ton "I'm an Auror. It's my job to identify and catch magical beings..."
    ton "But, if you are here, what happened to Professor Dumbledore? Did he use one of your wishes and wished himself away?"
    m "No... I don't do that anymore."
    m "I'm what you would call a *free* Genie..."
    ton "So? What happened to him?"
    m "I believe we traded places when one of my magical inventions went wrong..."
    ton "You don't say?! Is he all right?"
    m "I think so.{w} He traveled to my universe, and I’m stuck in this dull place..."
    m "Believe me, there are a lot more brothels in Agrabah.{w} I bet he's having the time of his life..."
    ton "So, you just poofed in here and decided to turn this school into your own private brothel..."
    ton "Because you were bored?!"
    m "Hey! I'm an immortal being... boredom is my worst enemy."
    m "And I didn’t do much, just a nudge in the right direction at the very best."
    ton "You need to bring him back, the real Dumbledore, immediately!"
    m "I don't know how,... yet.{w} We’re still working on it..."
    ton "We? Who else knows about this?"
    m "That Snape guy."
    ton "But of course!{w} After all... Professor Snape was mentioned in Miss Granger's letter as one of the offenders."
    ton "That sleazy, vile snake... Naturally he'd be all over an opportunity such as this."
    m "(Snake? Have I been saying his name wrong this entire time... I hate when that happens.)"
    ton "And to think I got fooled by that creep when I questioned him about it."
    m "(...)"
    ton "He's a very skilled liar, I'll give him that."
    m "Are you going to lock us up now?"
    ton "I very well should! It would be the moral thing to do."
    m "(Shit...)"
    ton "But that won't bring back Professor Dumbledore..."
    call ton_main("You and Professor Snape should be locked up in the tiniest cell in Azkaban for what you’ve done...","open","base","angry","mid")
    g4 "No, I hate confined spaces!"
    ton "And stay there for the rest of your life..."
    g4 "You can't do that to me, I'm immortal! I'd go insane!"
    ton "You should have thought about that before deciding to fuck your own students!"
    g4 "But I haven't even gotten to that part yet!"
    call ton_main("And you never will! Unless...","open","base","raised","R")
    m "Unless?"
    ton "It's simple..."
    call ton_main("You let me join in on the fun.",face="horny")
    m "..."
    m "What?" #screenshake
    ton "The ministry sent me to investigate what they assumed to be a rumour."
    ton "And whilst I could just squash the rumour and go back to a dull desk job."
    ton "Keeping quiet would be far more beneficial to me..."
    ton "I know for a fact that the Ministry has been looking at any excuse to have an adversary here at Hogwarts."
    m "Then what are you suggesting?"
    ton "Hire me as a teacher."
    ton "I could teach the students a thing or two about the *Defence against the Dark Arts*..."
    m "(...)"
    ton "And if you and Snape want this favour trading to continue, you'll need somebody who can keep things quiet with the ministry."
    m "Do I even have a choice?"
    ton "The alternative would be me bringing this to the ministry’s attention."
    g9 "Welcome aboard!"
    ton "Don't worry. I'm not here to spoil the fun."
    m "That's a relief..."
    ton "I'll inform the other teachers about my stay."
    ton "And the Ministry too of course. I know they'd love to have a ministry person teaching at Hogwarts, at the request of Professor Dumbledore himself, no less."
    ton "If only they knew..."
    ton "In any case, Profess-"
    ton "Or is it Genie now? What would you like me to call you?"
    m "You can call me whatever you want, hon."
    ton "Very well. Call me to your office whenever you need my help, Sir."
    m "I most certainly will..."

    #*Tonks leaves*
    call hide_characters

    call bld
    m "What an interesting turn of events..."
    g9 "Who could have guessed that she's a pervert as well?!"

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton")
    $ tonks_busy = True

    $ tonks_intro.E3_complete = True
    $ nt_event_pause += 1

    jump main_room



label new_tonks_intro:
    #knock on the office door
    #option to ask who it is
    #bla bla bla, intro stuff
    ton "So, Professor Dumbledore, are you aware why I have been sent here be the Ministry of Magic?"
    m "None at all."
    ton "You haven't had any complaints from students regarding any \"favour trading\"?"
    m "What sort of favours are you talking about?"
    ton "..."
    ton "In any case, I think it would be best that we bring the student in question up here to answer a few questions and hopefully clear everything up."
    ton "Are you acquainted with a Hermione Granger."
    m "We've met."
    ton "Fantastic. Would you mind summoning up here for me?"
    m "Certainly."
    ">With that, you summon the trouble making Miss Granger up to your office."
    her "Oh, hello Tonks! What are you doing here?"
    m "You two know each other?"
    her "Of course! We're all members of the order of the phoenix!."
    ton "Don't talk about that!"
    her "What? Why? Are you worried about he-who-must-not-be-named?"
    ton "Worse... continuity..."
    her "?"
    ton "Anyway, I'm here today to address some concerns students brought to the ministry."
    ton "Specifically, you're letter describing an \"unjust\" favour trading ring taking place at Hogwarts."
    her "Oh! The letter!"
    her "I didn't actually think anyone would read it..."
    ton "Now, now, have some faith in the ministry Miss Granger."
    her "You're right."
    ton "Now, would you be able to tell me a little about the sort of favours that are happening?"
    her "Oh... of course! What would you like to hear first?"
    ton "In your mention, you mentioned the slytherin house were the main offenders..."
    her "The slytherin sluts! Where do I begin?"
    her "There's the time Tracey Davis gave slughorn a lapdance in the middle of class."
    ton "In the middle of class?"
    her "Well, she was just sitting on his lap while he taught from his desk..."
    her "But we could all see her shaking her hips!"
    ton "Interesting... Any other incidents?"
    her "More than I can count!"
    her "Pansy Parkinson will let Snape grab her ass whenever he wants for 5 points a pop!"
    ton "Points? Is that how every one is being paid?"
    her "Of course! I've even heard that Slughorn will hold makeout competitions in his office after dark where the winner gets a hundred!"
    ton "So there's no gold involved?"
    her "I don't think so..."
    ton "Interesting... Please, go on. You mentioned something about girls making out?"
    her "I wish that was the worst of it!"
    ton "Ugh... go on..."
    her "I think a few girls might even be going all the way..."
    ton "really? Just for a few points?"
    her "Yep! From what I heard, Viola Richmond has sex with any teacher she can!"
    her "There are rumors that she's even done it with some of the female teachers..."
    ton "Wow... That's... pretty crazy..."
    ton "So... What's the problem?"
    her "What's the {b}problem{/b}?!"
    her "The {b}problem{/b} is that it's unfair to the boys!"
    ton "...{w}What?"
    her "Ugh... I knew you ministry goons wouldn't bother reading my letter properly!"
    her "Did you even read about the plights of the M.R.M., the \"men's rights movement\"?"
    ton "Wait... You're problem isn't that the girls of this school are engaging in illicit, sexual favours with their teachers..."
    ton "It's that the boys aren't able to do the same?"
    her "Exactly!"
    her "I don't um... necessarily want to stop the favour trading..."
    her "(I don't think gryffindor could win if we did that.)"
    her "I just want to make it fair, so that everyone can participate."
    ton "You want to make sex favours... fair..."
    her "Of course! They're so much fun, I don't think it makes sense to stop them..."
    ton "Wait... are you trading favours?"
    her "Oh... umm... I wasn't when I sent the letter, I promise!"
    ton "But you are now?"
    her "Ummm... maybe?"
    her "That's not a problem is it?"
    ton "Not if you're happy to do it... I'm hardly the moral police."
    m "Aren't you the magic police though?"
    ton "It's a bit of a grey area. I don't think this really counts as a magical crime..."
    ton "But I was assigned to investigate and resolve this issue..."
    her "Oh... so you are going to shut it down?"
    her "Well, if you do, make sure you take aways all the dirty points that slytherin managed to get their grimy hands on!"
    ton "Now, now, now... I never said I'd shut down your naughty little favour trading game..."
    ton "From what I can tell, all you need is another player."
    her "Another player?"
    ton "From what you were saying, apparently the problem is that the boys don't have anyone to sell favours to..."
    ton "But if a new teacher should come along... One that's happy to purchase favours from all her willing students..."
    ton "Well, I think that solves everyone's problems... Don't you?"
    her "You mean... You'd start buying favours from the boys?"
    m "I'm not so sure-"
    her "It's perfect! I hadn't even considered this solution to the M.R.M.s problems!"
    ton "You think so?"
    her "Of course! This way it's finally an even playing field for everyone!"
    her "So long as you don't buy too many points from those dirty slytherins!"
    ton "I still have to become a teacher first..."
    ton "So what do you say, Dumbledore? Any vacancies you need filled?"
    m "Hold on a second... Aren't you here to investigate the school? Why are you suddenly asking for a job?"
    ton "Well, I've only just started this job but my new title is technically \"Auror in charge of Hogwarts protection and oversight\"..."
    ton "So I think I'm allowed to stay on as a teacher while I work. At least that's how Mad Eye Moody did it when he was overseeing the goblet of fire."
    ton "Or was that the death-eater, Barty Crouch Jr in disguise?..."
    ton "Either way, there's a precedent for it."
    m "(I have no idea who or what she was just talking about.)"
    ton "Or, I could just bring this whole thing to the attention of the ministry and let them deal with it."
    ton "I'm sure that they'll love to hear you've all been shagging your students senseless..."
    m "Welcome aboard Miss- um..."
    ton "It's Miss Nymphadora Tonks, Dumbledore. Surely you remember me from when I was a student?"
    ton "God knows I was sent to this office often enough."
    m "Of course, I was just unsure of your title these days... You know how people with colored hair are."
    ton "(What?)"
    m "You can take whatever position is vacant."
    #Have her become a teacher, send Hermione off and discuss how she's going to start seducing her students with Dumbledore
