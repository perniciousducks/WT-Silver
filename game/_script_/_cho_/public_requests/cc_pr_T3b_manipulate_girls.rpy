

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_manipulate_girls_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_manipulate_girls.is_event_complete(1, 1): # Completed Alicia Spinnet?
        # Alicia Spinnet

        if not cc_pr_spy_girls.is_event_complete(1, 2):
            # Return if player has not spied on Alicia just yet.
            m "Let’s try and manipulate the girls on the enemy team!"
            cho "You’re expecting me to just jump in blind?"
            cho "I don’t know any of these girls, how do you expect me to manipulate them in any way without knowing what I’m dealing with?"
            m "Good point, perhaps we should consider spying on them a bit beforehand."

            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "I think it’s time to manipulate the female members of the enemy team a bit to see if we can find a way to distract them during the game."
        cho "And how do you suggest we do that?"
        m "Well, the Slytherin \"brutes\" seemed to think they had a pretty good chance to get with you during the last game."
        cho "They’re idiots though, I barely had to do anything."
        m "Which means it’s even more important to try and entice those girls before the match itself..."
        cho "..."
        m "It’s all about throwing them off their game, like you said... if the girls won’t get thrown off by you wearing some outfit then maybe an emotional... bond... would be more appropriate."
        cho "Don’t you think we’d have an easier time focusing on the boys?"
        m "Sometimes the hard route is the right one to take... you shouldn’t dismiss it."
        g9 "(Since those girls sound freaky...)"
        cho "But Harry is the seeker and Ron is the keeper... wouldn’t it be more useful if-"
        m "I’m certain my reasoning is correct here, are you questioning your trainer?"
        cho "..."
        cho "No..."
        g9 "Great, then off you go..."
        g9 "Time to make your team proud!"
        g9 "Pride is important!"
        cho "..."
        cho "I suppose, wish me luck..."
        g9 "Good luck..."

    elif not cc_pr_manipulate_girls.is_event_complete(1, 2): # Completed Katie Bell - Part 1?
        # Katie Bell - Part 1

        if not cc_pr_spy_girls.is_event_complete(1, 3):
            # Return if player has not spied on Katie just yet.
            m "Let’s try and manipulate-"
            cho "I’m going to stop you right there..."
            m "Yes?"
            cho "There’s no way I’ll try this again before I know more about the girls."
            m "Why? I thought it went great with the Spinnet girl!"
            cho "She cornered me!"
            m "And?"
            cho "I’m not going to attempt the other two unless I know a bit more about them..."
            m "Fine..."


            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "One down, two to go..."
        m "I think it’s time to manipulate one of the other Gryffindor girls."
        cho "Who do you want me to target this time?"
        m "Katie Bell!"
        cho "So, we’re still set on targeting the girls?"
        g9 "Of course, I’m sure we got but a taste last time...{w=0.4} No pun intended."
        cho "..."
        m "I hope you’ve  remembered what you learned from her. This girl likes being treated rough so show some assertiveness with her and I’m sure she’ll fall for you."
        cho "Okay..." #looking down a bit worried
        g9 "Assertiveness!"
        cho "..." #Changes from worried looking down to looking at genie
        cho "Yes, I will!"
        g9 "Great, off you go!"

    elif not cc_pr_manipulate_girls.is_event_complete(1, 3): # Completed Katie Bell - Part 2?
        # Katie Bell - Part 2

        # No return here since it's just a continuation of previous Katie event.

        m "Follow that girl again!"
        cho "Sir?"
        m "I mean... Today’s mission is to follow that Bell girl again..."
        cho "But... isn’t one time enough?"
        cho "My butt is still sore from last time..."
        m "There can never be too much of a good thing."
        cho "Fine..."
        m "Excellent, make sure to come back with an extensive report as usual B."
        cho "Got it..."

    elif not cc_pr_manipulate_girls.is_event_complete(1, 4): # Completed Angelina Johnson?
        # Angelina Johnson

        if not cc_pr_spy_girls.is_event_complete(1, 4):
            # Return if player has not spied on Angelina just yet.
            m "Let’s try and manipulate-"
            cho "I’m going to stop you right there..."
            m "Yes?"
            cho "There’s no way I’ll try this again before I know more about the girls."
            m "Fine..."

            call cho_main(xpos="base", ypos="base", trans=fade)

            jump cho_requests_menu

        m "You seem to have gotten to know the Gryffindor girls quite well by now [cho_name]."
        g9 "If you’re not careful you might turn into one yourself."
        cho "As if, Ravenclaw always comes first!"
        g9 "You do? No shame in that!"
        m "So...{w=0.4} Today we’re up against their team Captain, Angelina Johnson."
        m "Once you’ve managed to bond with her you’ll have no problem winning the cup."
        cho "Yes!"
        cho "We’re so close I could almost taste it!"
        g9 "I’m sure you will!"
        g9 "Now go get her..."
        cho "Yes [cho_genie_name]!"
    else:
        # Repeatable events.

        m "Let’s manipulate those girls some more!"
        cho "More? Haven’t I done it enough already?"
        m "There’s always room for more bonding."
        cho "Okay then..."
        m "Make sure to bring me your report as usual B."
        cho "Yes [cho_genie_name]!"

    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_manipulate_girls.inProgress = True

    jump end_cho_event

### Return Events ###

### Tier 3 (pre Gryffindor) ###

label cc_pr_manipulate_girls_T3_alicia_intro:
    # Alicia Spinnet

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Back so soon? I wasn’t expecting you for another hour."
    cho "..." #Blushing
    m "Are you alright? How did it go with the girls?"
    cho "Fine..." #Blush
    m "So, did you manage to connect with them in an emotional way?"
    cho "..."
    m "[cho_name]?"
    cho "You could say that."
    m "Tell me what happened."
    cho "Well..."
    cho "My plan was to try and approach Alicia Spinnet without the other two around."
    cho "So, I gestured her to come over to me as the other two entered the changing room..."
    m "Nicely done. Splitting up the group makes it less likely they’ll gang up on you."
    cho "That’s what I thought... and I felt pretty confident in my plan as she approached me."
    cho "But before I even got a word out she had come up and kissed me on the lips!"
    g4 "Whoa, wait what?"
    g4 "I thought the plan was for you to make the advances here..."
    cho "You and me both!"
    m "Do you know why she just came up and kissed you like that?"
    cho "Well, apparently she saw me when I entered the girls bathroom..."
    cho "And assumed I had followed her in there because I wanted to get in on the action..."
    g9 "Smart girl. She figured out you were perving on her!"
    cho "I'm not perving on anybody! I only followed her into that bathroom to gather information!"
    g9 "But I'm sure you liked sneaking a peek at her moist muff regardless."
    cho "How was I to know she wasn’t wearing any panties..." # annoyed
    m "Be that as it may, this Alicia girl seems to be one step ahead of us..."
    m "So, what happened next B?"
    cho "She started kissing me again, and placed a hand on one of my butt cheeks..."
    m "Correction, she's two steps ahead of us..."
    m "Sounds to me like you got a fan on the Gryffindor team..."
    g9 "That girl has the hots for you, that's for sure!"
    cho "*Tzzs!*... Those sluts would probably make out with anybody..."
    m "Tongue or no tongue?"
    cho "Sorry?" #Blush, shocked
    m "Did she slip you any tongue or what?"
    cho "How is that relevant to anything?"
    m "Did she though?"
    cho "..." #blush
    m "I knew it!"
    m "I hope you were at least courteous enough to return the favour..."
    g9 "Tongue kissing and a butt squeeze... Not that's what I'd call a true challenger!"
    cho "..." #Glaring
    m "What happened next?"
    cho "She broke off the kiss and slapped my butt cheek, before running off to the changing rooms."
    m "Sounds to me like a job well done, [cho_name]."
    cho "But I didn’t even do anything!"
    m "Yet you achieved exactly what I asked of you, you formed an emotional bond with her."
    m "Now we only have to do the same with the other two..."
    cho "So that's what this emotional bonding is all about? Getting them to kiss me?"
    m "Not kissing specifically..."
    cho "..."
    m "And now I'd like you to entice the other two as well."
    cho "Sure, no problem... I’ll just walk up to one of them and they’d throw themselves at me, just like Spinnet did!" #Sarcastic
    m "Great plan!"
    m "But for now you better get some rest and ready yourself to take on the other two."
    cho "..."
    m "Don’t look so dejected, [cho_name]. You had a beautiful girl kiss you today... surely you can’t be disappointed by that?"
    cho "It’s...{w=0.4} it’s not that...{w=0.4} I’m just used to it being me who..."
    cho "..." #Blush
    cho "Nevermind, good night then."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_intro_part1:
    # Katie Bell - Part 1

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    #Cho returns blushing with a vacant expression on her face
    cho "..."
    m "[cho_name]?"
    cho "..."
    m "Hello?"
    cho "Oh... Sorry [cho_genie_name]!" #face more focused still blushing
    m "What’s the report. Did you manage to bond with the girl?"
    cho "Of course..."
    m "Then how did it go? Tell me all the-"
    cho "All the details... Of course."
    cho "So...{w=0.4} My plan was to follow Katie again."
    cho "And to no surprise... She was once again making her way towards the lake."
    cho "This time I ran up to ask where she was going, and her response was that she was just going for a walk to clear her head."
    m "Yeah right..."
    cho "That's what I thought..."
    cho "So... I bluntly asked her if she was heading to the lake to enchant those seaweeds again..."
    m "Whoa, right to the point!"
    cho "Yes, I thought I’d catch her off guard..."
    cho "But she didn’t respond to me at all and just started walking again..."
    cho "So I tried pushing her more by asking her what Gryffindor house would think if they knew..."
    cho "But she just kept walking, completely ignoring me."
    cho "And it continued like that until finally I said that I would tell her captain unless she did something for me."
    cho "That’s when she stopped walking to eye me up and down, and ask what her punishment was going to be."
    g9 "Such a naughty girl!"
    cho "I know! That’s not at all where I was going with the conversation."
    cho "And what I hadn’t realized was that during my failed attempts at confronting her she had lead me off the path."
    cho "Because just as I was about to answer her, I felt something tighten around my waist and suddenly I found myself dangling several feet off the ground!"
    cho "Katie had not just wandering aimlessly... she had led me all the way to to the whomping willow!"
    m "The whomping what?"
    cho "That darn tree students are told to stay away from..."
    cho "It had grabbed both Katie and I, lifting us into air... I thought we were done for."
    cho "And for a couple of second we just dangled there until I heard a loud snapping sound and a yell."
    g4 "Terrifying!"
    cho "It was! But that was before I realised the tree wasn’t trying to kill us..."
    cho "It had started lashing its branches about, smacking Katie...{w} and she was thoroughly enjoying the whole thing." #Blushing
    g9 "A spanking tree? Seriously?"
    cho "Yeah...{w=0.4} this wasn’t her first time doing this, that's for sure..."
    cho "I couldn’t believe what I was seeing... I just stared at her in disbelief..."
    cho "And that's when the tree..."
    cho "Smacked one of its branches against my breasts and stomach..."
    m "But of course a bit of spanking wouldn't bother a girl as tough as you, would it?"
    cho "Of course! I’ve taken plenty of bruises playing Quidditch, so this is nothing in comparison..."
    cho "Once I got over the initial shock I realised that the tree had moved me so I was now right next to Katie."
    cho "And it was pretty hard to not stare at her body being smacked by those branches..."
    m "So did she-"
    cho "Of course she noticed me looking at her... and there was no doubt she enjoyed it even more than the spanking..."
    cho "So...{w=0.4} I had no choice other than going back to the original plan..."
    m "Yes?"
    cho "To form an emotional bond with her instead..." #blush
    m "Finally took that stick out of your butt, did you?"
    cho "What? There was no stick up my butt!" #angry
    m "Figuratively speaking... all that matters is that you're starting to enjoy yourself."
    m "To cherish the time you share with Katie... and that spanking willow."
    cho "Whomping, Sir."
    cho "I took it for what it was... Endurance training! There's nothing wrong with that..."

    cho "A couple of minutes later, the tree stopped smacking us, and I was able to catch my breath..."
    m "What a great workout. Maybe we can incorporate that tree into your training..."
    cho "But Sir, the whomping willow is extremely dangerous!"
    cho "Everybody knows to stay as far away from it as possible!"
    m "Because of a little ass spanking? Don't be silly..."
    m "That Katie girl sure took it like a champ... you need to be fearless as well, next time that tree spanks you red!"
    cho "Next time?"
    m "Just agree on a safe-word, if it gets too much."
    cho "It's a tree! It's not going to agree to anything!"
    cho "She tricked me into this!"
    cho "Once the tree lowered us onto the ground again, Katie immediately rushed off!"
    cho "So I had no oportunity to try and speak to her!"
    g9 "You kidding me? Talking would’ve just ruined it at that point!"
    g9 "You just had an amazing experience together, and didn’t exchange a word throughout the entire thing. There’s no better emotional bonding than that..."
    cho "..." #Blushing
    m "Well, I'd say we're one step closer to taking on the Lions for the finals."
    m "I'm confident you’ll be able to tame those lionesses by then."
    cho "I...{w=0.4} of course..." #Smiles and blushes
    m "You should take some rest now..."
    g9 "You look beat."
    cho "Very well... Good night then."
    m "Until next time."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_katie_intro_part2:
    # Katie Bell - Part 2

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Welcome back, any progress?"
    cho "If your goal was to get my ass red raw again then sure, plenty of progress..."
    m "Progress is progress... So, what went down today?"
    cho "I followed Katie... just as you wanted..."
    cho "This time I asked her directly if she intended to trick me again."
    cho "But she simply said she was going to the whomping willow, and that if I wanted to join I should just be quiet and follow her..."
    g9 "And, did you?"
    cho "Well, yes..."
    cho "Since she put it like that, how could I refuse? I'd look like a total wimp!"
    cho "I mean... It's only a giant, half-conscious, murderous tree... What's the worst that could happen?"
    cho "And let me tell you... it was even more intense than last time!"
    cho "Maybe Katie jinxed it this time around... or she forgot to jinx it... who knows."
    cho "It janked us into the air with such speed even I wasn’t ready for it!"
    cho "I had to fight its grip, to at least get some form of control back..."
    cho "But that was easier said than done as the tree had already snaked some of its branches underneath my clothes... sliding them right off my body."
    g9 "Nice! Just like that?"
    cho "Well I tried to grab them... but it had already moved its branches away from me..."
    m "What happened to your reflexes... Are you being bested by a tree now?"
    cho "No. I simply let it do its thing to... impress Katie..."
    cho "She for sure didn't mind that her clothing got taken off as well... that slut."
    m "(As well?)"
    cho "Just eyeing me up and down like a piece of meat... right up until..."
    g9 "Yes?"
    cho "The tree threw one of its branches about and swung it at us, smacking our butts..."
    g9 "Got to bless nature!"
    cho "And It just kept doing it, over and over, until our cheeks turned all red, a tingling sensation spreading across my butt..."
    cho "As it continued, Katie reached out to me to grab my hand..."
    cho "And as she did, the tree smacked us hard one last time."
    cho "And with the pain came a sudden sudden rush of relief as Katie tightened her hand around mine."
    g9 "An orgasm, Miss Chang?"
    cho "It...{w=0.4} yes, I think she might’ve."
    m "Still too early to admit it?"
    cho "Too early to admit what?"
    m "Never mind... did anything else happen after that?"
    cho "Not much, as far as I recall..."
    cho "All I remember is the tree lowering us to the ground and the sound of Katie’s breathing..."
    cho "I just laid there for a while catching my breath, until the only thing I could hear was the sound of the forest around me..."
    cho "Once I recovered, I turned to face Katie but again she was already gone..."
    m "Now that’s how it’s done!"
    cho "Thank you!"
    m "That shall be all for today..."
    m "You may leave now. Dismissed."
    cho "Good night then."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_angelina:

    # Since this is the last event in Tier 3, it will handle repeatables.
    if cc_pr_manipulate_girls.is_complete():
        $ renpy.jump(renpy.random.choice(("cc_pr_manipulate_girls_T3_repeat1", "cc_pr_manipulate_girls_T3_repeat2", "cc_pr_manipulate_girls_T3_repeat3")))

    # Angelina Johnson

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    if weather == "rain":
        g4 "Whoa, you’re soaking!"
        cho "Oh, yes... I guess my clothes ended up a little wet..." #Blushing
    else:
        g9 "Welcome back..."
        cho "..."
        g4 "You look soaked."
        cho "Oh, yes... I guess my clothes ended up a little wet..." #Blushing
        m "How? It's not even raining!"
        cho "*Uhm*...."

    m "So, do you have that report for me?"
    cho "I...{w=0.3} yes..."
    m "I’m waiting [cho_name]..."
    cho "Of course!"
    cho "So...{w=0.4} I went to see if I could catch Angelina talking to Madame Hooch again."
    cho "Determined to get the full context of what was going on this time!"
    cho "I immediately went and hid in the boys changing room as soon as they had gone for lunch to listen in."
    m "On Angelina talking to the Hooch lady?"
    cho "Yes, although I got there a bit early and they were still in the showers."
    cho "Doing my best to eavesdrop on their conversation, I went up to the hole I told you about."
    cho "To my luck, Angelina soon mentioned the spying to the other two, and Alicia piped up saying that she already knew about it."
    cho "Angelina sounded quite surprised that she knew about it but hadn’t told her."
    cho "That’s when Katie also joined in and said she knew about it as well but she had already worked out a plan on how to deal with it."
    m "Very perceptive of those girls..."
    cho "Quite..."
    cho "I waited to find out what her plan was, but then they suddenly went quiet, and I couldn't hear any of them."
    m "Left for the changing room?"
    cho "That’s what I thought, until I removed my ear from the hole to have a look..."
    cho "No, they hadn’t left... when I took a peek through the hole I found all three of them staring back at me.."
    g9 "Busted!"
    g9 "So what did you do, run away?"
    cho "At first I just sort of stood there in shock, not knowing what to do..."
    cho "Until Angelina angrily beckoned me to get in there."

    g4 "There goes our plan to separate them from each other..."
    cho "Let me finish!"
    cho "Once I got in there and before Angelina got a chance to anything, Spinnet came up to me..."
    cho "And just leaned in and kissed me again!"
    m "Nice, and you kissed her back?"
    cho "Of course! I wasn’t about to blow the cover, was I!"
    g9 "Of course..."
    cho "So, as she kissed me, Angelina shouted at her asking what the hell she was doing."
    cho "Alicia stopped and turned her head towards her asking what the problem was..."
    cho "And Angelina just sort of stared dumbfoundedly at her until she shouted that I’m the seeker of an enemy team."
    g4 "..."
    cho "I honestly thought it was over at that point but that’s when Katie joined in..."
    cho "Telling Angelina off for being mean, saying how it’s unfair that I don’t have a group of girls to play with after practice like she does."
    g9 "Nice... you got both Spinnet and Bell on your side! Told you that bonding with them would do it!"
    cho "I...{w=0.3} I suppose so." #Smiles
    cho "Angelina still didn’t look convinced though and just stood there with her arms crossed staring at me..."
    cho "So as an attempt at convincing her... I grabbed Alicia's head and pressed her lips against mine..."
    cho "Which was enough to grab Katies attention as she then moved up behind me to try and pull my top off."
    m "Nice..."
    cho "Of course I didn’t let her..."
    g4 "Why not! What about your cover!"
    cho "Because... I... Well, I didn’t blow it okay!"
    cho "I wasn’t going to let her undress me like that... so instead I grabbed her hands and put them under my bra to let her play with my breasts."
    cho "Luckily she didn’t seem to think much of it and began massaging them."
    cho "Angelina on the other hand was not convinced... telling the other girls to step aside..."
    cho "Which they did...{w=0.4} both Alicia and Katie jumped back as Angelina walked up, staring me down."
    m "Scary..."
    cho "I don’t think I’ve ever had a girl scrutinize me like that..."
    m "Especially a naked one..."
    cho "She then broke the silence to say I must truly be something special if her girls would just throw themselves at me as eagerly as they did."
    cho "I didn’t really know what to respond so I instinctively took a step back against the wall just as she leaned in and pressed her lips against mine which made me trip and slide down onto the wet floor."
    m "Ouch..."
    g9 "(Those Lionesses are animals!)"
    cho "She didn’t even apologize and just looked down at me, telling me I kiss like a highschooler..."
    cho "That said... didn’t stop her from crouching down for another... although this time she put her tongue in there."
    g9 "Straight in there!"
    g9 "I hope you returned the favour!"
    cho "I tried to... but as I started making any attempts towards doing so she stopped to stand back up."
    cho "And as I steadied myself against the wall to get up as well she put her foot beneath my skirt, pressing it against my panties which made me slide back down onto the floor."
    g9 "..."
    cho "Then turning back to the others she started chastising them even further, saying she was still mad about what they did..."
    cho "But when doing so, she also started rubbing her foot up and down against my panties."
    cho "Both Katie and Alicia didn’t seem to notice as they had turned towards Angelina to defend themselves as she kept rubbing me."
    cho "I don’t remember exactly what they were saying at that point..."
    m "(not surprising...)"
    cho "She just kept rubbing me more and more as they were arguing and..."
    cho "I just...{w} couldn’t...{w} hold it in at that point!" #ahegao?
    m "She made you-"
    cho "She made me orgasm as I lay there on the ground!"
    cho "Which they all realised as they stopped arguing to look at me..."
    cho "Angelina’s expression quickly changed into a smile and she pressed her foot down even harder, telling me I’ve been such a naughty girl..."
    cho "And that the other two shouldn't have been so selfish to keep me all for themselves."
    cho "She then stepped off me and made her way out of the showers, beckoning the other two to come with her."
    cho "And they just looked at me, giggled, then proceeded to follow her."
    m "Nice..."
    cho "What do you mean nice!"  #large text
    cho "She humiliated me!"  #large text
    m "She was testing you..."
    cho "She was..."
    g9 "Yes...{w=0.4} Not only that...{w=0.4} I think you passed!"
    m "Maybe I underestimated those girls... they aren’t easy to boss around that’s for sure..."
    m "But no matter..."
    cho "..." #pout
    m "We shall see soon enough what comes from this..."
    m "In any case, what has happened has happened."
    cho "You recon I ruined it?" #worried
    m "Of course not, you did great!"
    m "But you can’t let them take charge like that during the game."
    m "Maybe it’s best to let them get a look at you... at arm's length."
    cho "Yes [cho_genie_name]."
    m "Good!"
    m "One step closer towards sipping at the fizzy cup!"
    cho "You don’t drink from-"
    m "Better ready yourself [cho_name]. The finals are looming ever so closer."
    m "You got this."
    cho "Thanks..." #smiles
    m "Now, time for some rest."
    cho "Yes, good night then [cho_genie_name]."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

# Repeatable events

label cc_pr_manipulate_girls_T3_repeat1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you manage to seduce any of them?"

    cho "Katie caught me looking at her during the history of magic..."
    cho "Binns was droning on as usual and most of the other students were either sleeping or not paying attention."
    cho "Katie on the other hand found this a great opportunity to move her hand in a spanking motion at the sleeping student next to her."
    cho "No doubt trying to remind me of the Whomping Willow..."
    m "Ah... the tree..."
    m "Yeah... that was a good episode... I liked that one."

    m "Anything else to report?"
    cho "No, that’s about it..."
    g9 "Then mission success!"
    g9 "Good work B!"
    cho "Then if that’s all... I’ll head off for today."
    m "Yes, that will be all."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_repeat2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you manage to seduce any of them?"

    cho "Kind of... I was scouting them out during dinner over at the Gryffindor table where all three of them were sitting together."
    cho "Alicia saw me looking and leaned in and kissed Katie on the cheek."
    cho "Katies face turned red so I assume they don’t usually do stuff like that in public."
    cho "Angelina appeared to find her embarrassment pretty funny though."
    g9 "Nice..."

    m "Anything else to report?"
    cho "No, that’s about it..."
    g9 "Then mission success!"
    g9 "Good work B!"
    cho "Then if that’s all... I’ll head off for today."
    m "Yes, that will be all."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_manipulate_girls_T3_repeat3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you manage to seduce any of them?"

    cho "No, but they sure had a good laugh embarrassing me during practice."
    cho "They were somehow able to temporarily dispel the cushioning charm from my broom because that handle felt pretty hard between my legs..."
    cho "Angelina kept laughing as I flinched with every sharp turn whilst chasing the snitch..."
    m "Did it hurt that much?"
    cho "Oh... no it didn’t really hurt at all really..." #blush
    m "But you just sai-"
    m "(Oh, I see...)"
    m "Well then..."

    m "Anything else to report?"
    cho "No, that’s about it..."
    g9 "Then mission success!"
    g9 "Good work B!"
    cho "Then if that’s all... I’ll head off for today."
    m "Yes, that will be all."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event
