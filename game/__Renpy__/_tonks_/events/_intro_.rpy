

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
        m "(They must’ve found out I’m not actually Dumbywho!)"
        ton "Sir?"
        m "Governments are all the same with their bloody rules...{w=2.0}{nw}"
        ton "Sir, I’m here to discuss an important matter with you regarding your students."
        m "Oh... is that all?"
        m "I mean, of course. do come in!"
    else:
        m "(Another female?)"
        m "(She sounds a bit too old to be a student...)"
        g9 "(Better to just let my charm play...)"
        m "Yes... come in."

    #*Tonks walks in*

    call ton_main(face="neutral", xpos="right", ypos="base")

    ton "Thank you, I do apologize for arriving unannounced."
    m "(Oh shit, she’s hot...)"
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
            m "Shit..."

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
    ton "Don’t worry, I’ve already gotten a room down in Hogsmeade, I’ll be staying there so no worries about accommodations."
    m "Great..."
    ton "And you are not to speak to any of the other professors and students about our meeting. I’d like to keep my presence unknown."
    m "(...)"
    ton "Good day to you sir."

    # Tonks leaves.
    call hide_characters

    call bld
    m "Shit..."
    m "I better talk to Snape about this..."

    $ tonks_intro.E1_complete = True
    $ nt_event_pause += 1

    jump main_room


label tonks_intro_E2:

    "Dev Note" "Add knocking interaction."

    call ton_main(face="neutral", xpos="right", ypos="base")

    m "Tonks... Have you found any evidence yet?"
    ton "Sadly no, Professor."
    ton "I haven't gotten a chance to investigate properly."
    ton "I was rather occupied listening to Miss Granger's own investigations first."
    ton "That girl sure is something, isn't she?"
    ton "Not that I minded listening to her."
    ton "(With her cute little accent...)"
    ton "I offered her to stay over the evening and tell me everything, while I enjoyed a glass of firewhiskey..."
    ton "She was very thorough in writing down the happenings she's witnessed."

    # Tonks could tell you about some of Hermione's

    ton "Anyhow, she had no proof of any such activities. It's all just accusations."
    ton "As much as I wish they were true..."
    m "(Huh?)"
    ton "So I could conclude my investigations early, of course."
    ton "And bring this favour trading business to an end, once and for all."

    # Tonks leaves.
    call hide_characters

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

    ton "Professor Dumbledore, I know you’re in there..."
    m "Who is it?"
    ton "Tonks!"
    m "Who?"
    ton "..."
    ton "Nymphadora Tonks...{w=1.0} Ministry of Magic, Auror division."
    m "I see..."
    m "Do you mind coming another time, I’m very busy...{w} watering the bird."
    ton "..."
    ton "I’m coming in."

    #*Tonks enters the office*
    call ton_main(face="angry", xpos="right", ypos="base")

    m "Oh, that Tonks, my apologies. I thought you might have been someone else."
    m "How’s the investigation going? Nothing to report I gather?"
    ton "On the contrary..."
    m "(Darn...)"
    ton "In fact I caught one of your teachers engaged in rather...{w=0.3} adulterous activities with a couple of students."
    m "A couple...{w} Like, at the same time?"
    ton "Indeed, and could you guess who this teacher might be?"
    m "Probably Sn-"
    ton "Severus Snape!"
    m "Oh, no! How could this have happened in my school!"
    ton "Cut the bullshit, I know you’re in on it!"
    g4 "What, how... I mean, of course I’m not. What are these accusations?"
    ton "Surely these kinds of activities is not the proper way for a headmaster to behave."
    g4 "But I didn’t..."
    ton "Well, I got proof confirming the opposite."
    g4 "I never even got to..."
    ton "You’ll surely end up in azkaban prison for letting this go on under your supervision."
    g4 "No, I hate confined spaces!"
    ton "..."
    ton "And I can’t believe things had gone this far already without my involvement."
    g4 "Please don’t put me in...{w=0.4} Wait,{w=0.2} already?"
    ton "I assumed it would’ve taken at least another year before things reached anywhere close to this stage, at first I thought it was just pure ignorance from your part."
    ton "But if you’re also in on it, it makes a lot more sense..."
    m "Wait... hold on a minute."
    m "The ministry is in on this too?"
    ton "Oh, by Merlins left testicle..."
    ton "Of course they’re not, I am!"
    m "Why would you..."
    ton "Who do you think kept things quiet with the ministry and intercepted any correspondence to begin with."
    ton "Well, until miss Granger had hers sent directly to one of the other departments..."
    m "But this doesn’t make any sense, why would a ministry worker. That doesn’t even work here be in on any illicit goings on confined within the school."
    ton "Panty pictures!"
    m "What!"
    ton "Well, I’m fine with any photographs really, ankles, butts, underwear..."
    m "I see..."
    ton "Feet!"
    g4 "Feet?"
    ton "Well, anything I can get really."
    m "(This lady’s a pervert...)"
    ton "There seems to be a great opportunity here..."
    m "I’d rather keep my shoes on thank you!"
    ton "Not that, silly."
    ton "It appears that there’s finally an opening for me."
    ton "The ministry sent me to check out what they assumed to be a rumour."
    ton "And whilst I could just squash the rumour and go back to a dull office job, I know for a fact that they’ve been looking at any excuse to have an adversary here at Hogwarts."
    m "Then what are you suggesting?"
    ton "Well, I’m suggesting I continue keeping my own motives to myself, squash the rumour but suggest to the ministry that I could take a position here in the guise of continuing the investigation."
    m "So, you’re going to pretend that you’re doing them a favour and continuing your diligent allegiance with the ministry?"
    m "Whilst taking a normal teaching position here with the purpose to get closer to the students?"
    ton "Exactly!"
    m "(I think I might’ve come across this universe’s version of me...)"
    ton "So what do you say, Dumbledore? Any vacancies you need filled?"
    ton "Oh, who am I kidding. I already know you’re always in the need of a Defence against the Dark arts teacher."
    m "Are you sure it’s such a good idea..."
    ton "The alternative would be me bringing this to the ministry’s attention."
    g9 "Welcome aboard!"
    m "You can take whatever position is vacant."
    ton "Great, I already brought my things with me!"
    m "Of course you did..."
    ton "I’ll make sure to keep you updated."
    m "Marvelous..."

    #*Tonks leaves*
    call hide_characters

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
