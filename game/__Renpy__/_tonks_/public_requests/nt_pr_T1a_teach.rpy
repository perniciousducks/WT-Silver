

### Tonks Teaching ###

# Detention with Tonks
# (Tonks gives students detention or lets them stay after class)
# (Gets to see the boy's dicks, the girl's panties, punishs them,...)
# (Gives hours points to each of the students)

label nt_pr_teach_start:

    if ton_tier == 1:

        if nt_pr_teach.points == 0:
            ton "So, what's the plan?"
            m "The plan?"
            ton "You know, how does this go down?"
            ton "I'm hardly a regular when it comes to this stuff."
            m "Let's start small. We'll need to build up a bit of a reputation for you before you start trying anything crazy."
            ton "A reputation?"
            ton "Think I'll get a nickname? Maybe they'll call me touchy tonks?"
            m "Maybe..."
            ton "So what did you buy off of Hermione on your first favour?"
            m "Ugh... I think I got her to make a silly face or something..."
            m "That and getting her to talk to me."
            ton "Talk to you? You paid her for that? You can get that for free!"
            m "In that case, the first \"real\" favour I bought was getting her to lift her skirt."
            ton "That's more like it!"
            ton "But even though we're in Scotland-"
            m "(we are?)"
            ton "None of the boys are wearing skirts..."
            m "Just get them to show you their dicks then."
            # Note: Mabye ad a section here in which Tonks is a bit more surprised about this suggestion, but ok with it in the end.
            ton "Show me their dicks... That's good... {p}Can I touch them?"
            m "Let's just look for now..."
            ton "Fine... So how many am I allowed to look at?"
            m "As many as you want..."
            ton "And how many points am I allowed to give out?"
            m "Look, I'm not really convinced these points are real..."
            ton "(what? Can't he see the scoreboard at the top of the screen?)" # Note: only Genie can break the 4th wall.
            m "I just say \"Ten points to gryffindor!\" to get these girls to show me their tits..."
            $ gryffindor += 10
            m "So as far as I'm concerned, hand out as many as you like."
            ton "Alright... Well, I better get to class. I've got some boys to {b}teach{/b}..."
            m "Don't forget to come back here after classes to fill me in."
            ton "Will do..."
            #send tonks off

        else:
            m "Ready to help the boys earn some points?"
            ton "You mean am I ready to see some dick?"
            m "Is there a difference?"
            ton "There {b}should{/b} be."
            ton "Lucky for you, I'm happy to do both."
            m "See you after classes then."
            ton "Mhmmm... Don't worry if I'm a little late though..."
            ">With that, Tonks strolls out of your office with a hungry look in her eyes..." # Note, we can just replace sentences like that with the chibi walking out.

    elif ton_tier >= 2:

        if nt_pr_teach.points == 0: # Tell her to be even lewder for the next level of favors.

            "Dev Note" "Write 2nd intro."

        else: # Repeat
            m "Would you like to give some boys detention again?"
            ton "And make them show me their dicks, Sir?"
            m "If that's what you fancy..."
            ton "Hmm...Yes. I wouldn't mind seeing the \"hard cocks\" of some of my \"favorites\"..."
            m "And make sure they remember it."
            ton "Yes, [ton_genie_name]. Don't wait for me, though..."

    # Tonks leaves

    return



### Tier 1 ###

label nt_pr_teach_T1_E1: #Tier 1 - Event 1 - Slytherin boy
    m "How were your extra curricular activities today?"
    ton "Ah! It's such a rush!"
    ton "I can't believe how naughty I feel!"
    m "So I take it you managed to sneak a peek?"
    ton "Sort of... I didn't really see it."
    ton "But it was still incredible..."
    ton "Ugh... that look on his face..."
    m "What did you see then?"
    ton "Well, this sweet little Slytherin kid had been staring at my boobs all lesson."
    ton "So, naturally, I get him to stay behind after class."
    ton "I couldn't tell if he was angrier than he was scared..."
    ton "But, as his teacher, I insisted that he write out some lines to correct his behavior."
    m "Do I need to ask what he had to write?"
    ton "\"I will not stare at my teacher's big, beautiful breasts\"..."
    m "Was the big and beautiful part really necessary?"
    ton "Oh, that's not the best bit..."
    ton "I went on to tell him how {b}naughty{/b} it was for him to peek at me..."
    ton "Then I made him pull down his trousers before he wrote his lines."
    m "So you did see it!"
    ton "He still had his underwear on. I think if I pushed him much further he would have snapped."
    ton "Besides, I could still see how hard he was..."
    ton "Ugh... It was crazy..."
    ton "I might have teased him a little more while he wrote them out as well..."
    m "The lines weren't enough?"
    ton "Don't worry, I just whispered in his ear a little..."
    ton "Told him what a naughty boy he'd been..."
    ton "Let him know he'd earn some points for Slytherin..."
    ton "If my boobs happened to rub into his back a little while it happened I don't see how that's my fault." # This sentense is a bit convoluted.
    m "Ugh... that poor kid."
    ton "Pfft... He was having the time of his life..."
    ton "His underwear was practically {b}soaked{/b} in precum."
    m "Well, do you think he'll spread the word about the favour trading?"
    ton "I'm not sure... Maybe..."
    ton "All I know is that he won't be able to keep his eyes off of me next lesson."
    m "Very good. That'll be all."
    ton "Thank you, [ton_genie_name]."

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    return


label nt_pr_teach_T1_E2: # Tier 1 - Event 2 - Racenclaw boy
    m "How were your classes today?"
    ton "Mmmm... Long and hard... Just how I like them..."
    m "I take it you were able to steal a few glances?"
    ton "Mmmm, it was even better than I thought it'd be!"
    ton "Who knew they'd be so nervous!"
    m "What happened?"
    ton "Well, I figured I'd have to be alone with a student to manage to convince them to whip it out..."
    ton "So I gave the cutest little thing I could find detention..."
    ton "Poor boy, I'm not sure he'd ever even been in trouble before."
    ton "So when the bell rang he immediately went on babbling about how sorry he was for speaking in class and how he'd never do it again..."
    ton "Ugh... I had to hold myself back from jumping him right then and there..."
    ton "Anyway, I eventually managed to calm him down and tell him it'll be alright..."
    ton "I even let him know that if he was a good boy he could earn some points for his house."
    m "Did he like the sound of that?"
    ton "You should have seen his eyes light up! He thought it was Christmas!"
    ton "After that it was child's play..."
    ton "Not that he looked like a kid down there... Mmmm, I even had him play with himself for a little bit..."
    ton "Ugh... Fuck, he looked tasty..."
    m "Ahem... So did you pay him his points or just tease him?"
    ton "Don't worry, I made sure \"Ravenclaw\" was paid."
    m "And did he look like the kind to talk?"
    ton "Probably not..."
    m "Well try and get a talker next time. We're trying to build your reputation, remember?"
    ton "I'll try..."
    ton "(Although I might have to play with this one a few more times...)"
    m "That will be all for now, [tonks_name]."
    ton "Thanks, [ton_genie_name]."

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    return


label nt_pr_teach_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys. Guess who...
    m "How'd it go?"
    ton "Great! I even managed to convince two boys to show me their dicks at the same time!"
    m "Two at once? Nice."
    ton "Yep. To be honest, they probably would have done it for free."
    ton "Not that they turned down the offer of points though..."
    m "Care to elaborate?"
    ton "Alright then you old perv..."
    ton "Normally I'd just keep the cutest thing that takes my eye back after class for a little one-on-one time..."
    ton "But I actually had to punish these two idiots for real."
    m "What did they do?"
    ton "Ugh... they wouldn't shut up, they kept trying to lift girl's skirts with \"wingardium leviosa\"..."
    ton "They reminded me of my younger self... Which probably meant they were going too far."
    ton "So I kept them after class, gave them the whole lecture about responsibility and respect..."
    m "..."
    # m "With their pants down?"
    # ton "With their pants down!..."
    # ton "I told them I'd pay them both ten points to show me their cocks as well."
    ton "Then I told them I'd pay them both ten points to show me their cocks..."
    m "Just like that?"
    ton "Well, there's a lot more subtlety to it in practice..."
    ton "Not that I think I needed it given how horny they were."
    ton "I think the poor buggers actually thought I was going to jerk them both off..."
    ton "Still, I think they had a fun time."
    m "Any chance they'll tell their friends about it?"
    ton "Are you kidding me? The \"Gryffindor\" common room is probably a buzz already!"
    ton "It wouldn't surprise me if I start getting asked to give boys detention."
    m "Great work."
    ton "Thank you, [ton_genie_name]. That means a lot coming from you."
    m "Even if it is encouragement for seducing your students?"
    ton "Even then."
    ton "Well, I better get back to work, these halls aren't safe unless there's a teacher on patrol."
    m "(I'm not sure they're safe with her on patrol...)"

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    return


label nt_pr_teach_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    m "Manage to sneak a peek today?"
    ton "Um... Afraid not..."
    m "Oh."
    ton "But I do have a story for you!"
    m "Well why didn't you just start with that? You had me worried for a moment there!"
    ton "Are you that desperate to hear about me fooling around with my students?"
    m "I'm desperate to hear {b}anything{/b}, this office isn't exactly riveting to listen to..."
    ton "In that case, I'll try and add some flair to it."
    ton "Once upon a time-"
    m "Ahem..."
    ton "Too much?"
    m "Just a tad."
    ton "So, I know my job is to try and balance out the favour trading a little..."
    ton "But I just couldn't help myself today..."
    m "Help yourself? You mean..."
    ton "Ugh, I don't normally mess around with girls..."
    ton "(Not since I left here anyway...)"
    ton "But there was the tastiest morsel I have ever seen in class."
    m "..."
    ton "Now, I know when I'm being checked out, I can feel someones eyes on me..."
    ">You nod, unconsciously gazing directly at her tits."
    ton "And most of the time I don't mind... I might even encourage it from time to time..."
    ">Tonks gives her boobs a subtle little shake. "
    ton "So when I felt a pair of cute little eyes struggling they're hardest not to stare at me."
    ton "I {b}had{/b} to play with her."
    m "Mmmm... what happened?"
    ton "Nothing much... I'm pretty sure she would have freaked if I tried anything..."
    ton "So I just asked her to stay after class for a little... {b}chat{/b}."
    m "What did that chat involve?"
    ton "Not much..."
    ton "I just sat directly in front of her desk..."
    ton "Asked her how she felt she was doing in class..."
    ton "I made sure to ask her if she was feeling distracted..."
    ton "All the while, playing with the buttons on my shirt..."
    ton "Ugh... I've never seen someone so flustered..."
    ton "Eventually, it got too much for her so she just yelled that I was wasting her time and ran off in typical \"Slytherin\" fashion."
    m "Do you really think she was looking at you?"
    ton "After that? There's no doubt... she's hooked."
    ton "Now I've just got to reel her in."
    ton "If that's alright with you, sir!"
    m "You're asking my permission?"
    ton "Well, I was only supposed to buy favours from the boys..."
    m "Eat your heart out. Just make sure you keep me in the loop."
    ton "Thanks, [ton_genie_name]."
    ton "I can't believe how much you've mellowed out since I was a student."
    m "Oh, um... time can do that..."
    m "Speaking of, it's getting a bit late..."
    ton "So it is... Night, sir."
    m "Goodnight, [ton_name]."

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    return



### Tier 2 ###

label nt_pr_teach_T2_E1: # Tier 2 - Event 1 - Hufflepuff girl
    ton "Guess what happened, [ton_genie_name]!"
    m "Um... You found the golden ticket?"
    ton "Better! I had a student come to me to sell a favour!"
    m "And you haven't bought a favour from them before?"
    ton "Not one! They're not even in any of my classes!"
    m "Very good! Word must be getting around that you're... \"purchasing\"."
    m "So what house is he in?"
    ton "Oh... um... it wasn't a he..."
    ton "I hope that's alright... I know I'm supposed to be balancing out the favours for the boys..."
    m "Right...(I'd forgotten about Miss Grangers dumb M.R.M. thing...)"
    m "(Does she even still run that?)"
    m "I wouldn't worry about that too much... so long as you're still buying from the boys I don't think it should matter."
    ton "Good... Because there was no way I could turn down this cute little \"Hufflepuff\"..."
    ton "Poor thing must have spent hours building up the courage..."
    m "So what did you buy from her?"
    ton "Well... I asked her what sort of favour she wanted to sell me..."
    ton "Poor thing was so flustered... She probably didn't plan this far ahead..."
    ton "She started babbling on so I just calmed her down by letting her know what favour I wanted..."
    ton "While she just sort of stood there stunned for a little bit I went and locked the door."
    ton "After that I sat down in the front row of the class and told her to sit on my desk..."
    m "Mmm, now that's a front row seat to die for."
    ton "All that was missing was a bucket of popcorn..."
    ton "Eventually she was able to muster up enough courage to pull up her skirt..."
    ton "Poor thing only thought to ask how many points she'd be paid after she lifted her skirt though."
    ton "I told her five for showing me her panties..."
    m "Only five?"
    ton "She said the same. I explained that showing her plain white panties only gets five points."
    ton "If she were to take those panties off though... Then that might get \"Hufflepuff\" an extra twenty..."
    m "Did she say yes?"
    ton "She didn't say anything... but she pulled them down all the same..."
    m "Nice! Getting a student to strip on the first favour is hard work!"
    ton "Oh, we're not done yet... After soaking in the view for a while I started to notice she was soaking as well..."
    ton "So... I offered her fifty extra points to play with herself for me..."
    m "Mmmm, go on..."
    ton "Ugh... it was amazing... she was so nervous... it looked incredible on her face..."
    ton "That and the soft mewling she made while she did it..."
    ton "It was that perfect combination of slutty need and statuesque beauty..."
    ton "Argh... I wanted to taste her so badly..."
    ton "But instead, I held back... I don't think she's ready for that..."
    ton "I'm not sure she was ready for this... She sure as hell wasn't ready for the orgasm she had..."
    ton "Ugh... I had to spend ten minutes scourgifying the desk..."
    m "Ah... very good... but I think that should be all for now..."
    m "Much more of this and I'll need to \"scour-ify\" my own desk..."
    ton "Mmm, alright then, [ton_genie_name]. I better be on my way as well."
    ton "(Fuck knows I could use a bit of \"alone\" time myself...)"

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    return


label nt_pr_teach_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy
    #Have a few drops of cum on her clothes when she comes in
    m "How'd your day go?"
    ton "The teaching was a little boring... Simple wards, hex-detection, basic stuff..."
    ton "Not that you'd know it was basic with how much they all struggled with it!"
    m "I was sort of referring to your... \"extra-curricular\" activities."
    ton "I know, I just wanted to get that off my chest. I'd complain to someone else but I'm not that fond of the other teachers..."
    m "Oh?"
    ton "Well McGonagall is as stuck up as ever, Snapes a gross weirdo, Hooch keeps trying to hit on me..."
    ton "Anyway, let's get onto the story, shall we?"
    menu:
        "-Let her know about the cum-":
            $ choice_flag=True
            m "Sure... But, you know you've got cum on you, right?"
            ton "Cum?"
            ">Tonks looks down at her clothes, noticing the cum streaked along it."
            ton "That cheeky bugger! I can't believe he actually shot it that far..."
            m "..."
            ton "I'll start from the beginning."
        "-Ignore it-":
            $ choice_flag=False
            pass
    ton "So, I spent a little time with my favourite \"Ravenclaw\" student today..."
    m "Another detention session after class?"
    ton "I don't need to resort to detention anymore, he's learned what a wink in class means..."
    ton "Plus, I think a few of the other students have worked out what it means as well."
    ton "There were a few whispers today... Hopefully that helps get the word out..."
    m "I bet."
    ton "So after class, I locked the door like normal and went over to him and let him know that I wanted another favour..."
    ton "He wanted to sell me a kiss today... I almost took him up on it honestly..."
    ton "But I told him I wanted something else... I wanted another look..."
    ton "I think he was a little disappointed... So I told him I didn't {b}just{/b} want to look at it..."
    ton "I wanted to see him play with it..."
    ton "His eyes lit up after that..."
    ton "He just started staring at me while he stroked it..."
    ton "Getting it hard for his teacher..."
    ton "Mmmm, the way he was staring at my tits... that hunger..."
    ton "I had to get them out for him."
    ton "That really got him excited... He even started to speak after that..."
    m "What did he say?"
    ton "The usual stuff; how pretty I was, how nice my tits looked..."
    ton "You know how guys are..."
    ton "What was weird was when he started to call me mommy again..."
    m "Did you tell him to stop?"
    ton "What? Why? It's just a little dirty talk... I might have even joined in."
    m "Really?"
    ton "What do you think made him fire his load across the room?"
    ton "All I said was \"cum for Mommy\" and he was blowing the biggest load I've seen."
    # ton "(From a human...)"
    m "Fuck. That's pretty hot..."
    ton "I know... Ugh... I need to go rub one out after it..."
    ton "See you, sir."
    m "Goodbye [ton_name]."
    if choice_flag:
        m "Are you going to do anything about the cum?"
        ton "Oh... Eh, why bother?"
        ton "I already had it on the way here. Besides, it'll be good for spreading the word."
        m "Whatever you say..."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    return


label nt_pr_teach_T2_E3: # Tier 2 - Event 3 - Slytherin boy
    m "How'd your favour go today?"
    ton "It was alright, I was able to kill two birds with one stone though."
    m "I'm intrigued."
    ton "So, I had some cocky little \"Slytherin\" brat causing trouble in class."
    ton "Talking, letting a chocolate frog loose, not locking his monster book of monsters."
    ton "Just being a general pain in the ass."
    m "Sounds like a hassle."
    ton "\"Slytherins\" always are."
    ton "Anyway, I let him know he'd earned himself detention after class."
    ton "Little bastard cursed me out for that..."
    ton "Once the class had emptied out I proceeded to lock the door to scare him a little..."
    ton "After that I let him know his Punishment was going to be selling me a favour."
    ton "At first the idiot thought I was going to jerk him off..."
    ton "I might have, if he'd played his cards right..."
    ton "Instead, his favour wouldn't be nearly as fun."
    ton "I made him pull down his pants and whip his cock out..."
    ton "He was so keen I bet he thought a blowjob was on the table..."
    ton "Eventually, I convinced him to start jacking it..."
    ton "Ugh... It was actually pretty cute at first..."
    ton "Then just as he was about to blow his load..."
    ton "Boom! Petrficus totalus!"
    m "Petrifi-{w} Petrifico-?"
    g4 "(What does she even mean by that?)"
    ton "I petrified him!"
    m "*Ahh*..."
    ton "Hahaha that look on his face!"
    ton "That's what he gets, the little shit. Not only did I leave him blueballed, I left him pants down in the class."
    m "Forever?"
    ton "What? Just until the spell wears off."
    ton "In an hour or so..."
    ton "That or someone else finds him..."
    ton "Either way, he's learned his lesson about screwing around in my class."
    m "Very good..."
    m "(This bitch might be crazier than I thought...)"
    ton "Thank you, Sir..."
    ton "See you..."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    return


label nt_pr_teach_T2_E4: # Tier 2 - Event 4 - Slytherin girl
    m "Anything interesting happen today, [ton_name]?"
    ton "Did it ever... I broke new ground today..."
    m "That's what I like to hear... So what happened?"
    ton "Remember that cute little \"Slytherin\" that's still coming to grips with her budding sexuality?"
    m "The girl you're turning into a lesbian, got it."
    ton "Well, I had her stay back after class today..."
    ton "For someone who supposedly hates selling favours, she was surprisingly keen today..."
    m "Maybe she's finally coming around..."
    ton "Maybe... Anyway, we agreed on me getting a little peek under her skirt for 15 points..."
    ton "After she'd pulled up I did the old offer more points for her to drop her panties."
    ton "I was expecting her to at least argue for more points but she dropped them in an instant."
    ton "Next, she just looked at me as if to ask, \"what next?\""
    ton "Ugh... it was so fucking hot..."
    ton "So I was going to have her play with herself..."
    ton "But that cute face of hers... and all the teasing..."
    ton "I decided to take matters into my own hands... specifically her matter..."
    m "You couldn't help yourself, could you?"
    ton "Ugh... You wouldn't blame me for fingering her if you saw how cute she was."
    ton "And that look on her face... that perfect mix of lust and need..."
    ton "Fucking. incredible. "
    m "What did she have to say about the whole thing?"
    ton "Not much... She just looked up at me with those puppy-dog eyes whispering \"wow\" and \"don't stop\"..."
    ton "To think she tried to pretend she wasn't into me before..."
    m "Good work, [ton_name]. Think she'll start talking now?"
    ton "Not unless she's ready to out herself as bi..."
    ton "But I think there are some whispers..."
    m "Very good. That'll be all then."
    ton "Thank you, sir... See you..."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    return
