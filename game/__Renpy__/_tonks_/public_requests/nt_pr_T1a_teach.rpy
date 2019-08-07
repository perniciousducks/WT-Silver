

### Tonks Teaching ###

# Detention with Tonks
# (Tonks gives students detention or lets them stay after class)
# (Gets to see the boy's dicks, the girl's panties, punishs them,...)
# (Gives hours points to each of the students)

label nt_pr_teach_start:

    if ton_tier == 1:

        if nt_pr_teach.points == 0:
            call ton_main("So, what's the plan?","base","base","base","mid")
            m "The plan?"
            call ton_main("You know, how does this go down?","base","base","base","mid")
            call ton_main("I'm hardly a regular when it comes to this stuff.","base","base","base","mid")
            m "Let's start small. We'll need to build up a bit of a reputation for you before you start trying anything crazy."
            call ton_main("A reputation?","base","base","base","mid")
            call ton_main("Think I'll get a nickname? Maybe they'll call me touchy tonks?","base","base","base","mid")
            m "Maybe..."
            call ton_main("So what did you buy off of Hermione on your first favour?","base","base","base","mid")
            m "Ugh... I think I got her to make a silly face or something..."
            m "That and getting her to talk to me."
            call ton_main("Talk to you? You paid her for that? You can get that for free!","base","base","base","mid")
            if hg_pf_admire_panties.counter != 0:
                m "In that case, the first \"real\" favour I bought was getting her to lift her skirt."
                call ton_main("That's more like it!","base","base","base","mid")
                call ton_main("But even though we're in Scotland-","base","base","base","mid")
                m "(we are?)"
                call ton_main("None of the boys are wearing skirts...","base","base","base","mid")
            elif hg_pf_admire_breasts.counter != 0:
                m "In that case, the first \"real\" favour I bought was getting her to show me her bra."
                call ton_main("That's more like it!","base","base","base","mid")
                call ton_main("But it's not a big deal for boys to show you their chests...","base","base","base","mid")
            else:
                m "Yes, Granger is greedy when it comes to points..."
                call ton_main("I'm not interested in just chatting with my Students! I get to do that all day...","base","base","base","mid")
            m "Just get them to show you their dicks then."
            call ton_main("Oh wow! Are you serious about that?","base","base","base","mid")
            m "Sure why the hell not. It's no big deal..."
            call ton_main("Show me their dicks... That's good... {p}Can I touch them?","base","base","base","mid")
            m "Let's just look for now..."
            call ton_main("Fine... So how many am I allowed to look at?","base","base","base","mid")
            m "As many as you want..."
            call ton_main("And how many points am I allowed to give out?","base","base","base","mid")
            m "Look, I'm not really convinced these points are real..."
            m "I just say \"Ten points to gryffindor!\" to get these girls to show me their tits..."
            $ gryffindor += 10
            m "So as far as I'm concerned, hand out as many as you like."
            call ton_main("Alright... Well, I better get to class. I've got some boys to {b}teach{/b}...","base","base","base","mid")
            m "Don't forget to come back here after classes to fill me in."
            call ton_main("Will do...","base","base","base","mid")

        else:
            m "Ready to help the boys earn some points?"
            call ton_main("You mean am I ready to see some dick?", face="horny")
            m "Is there a difference?"
            call ton_main("There {b}should{/b} be.","open","base","base","R")
            call ton_main("Lucky for you, I'm happy to do both.","base","base","base","mid")
            m "See you after classes then."
            call ton_main("Mhmmm... Don't worry if I'm a little late though...", face="horny")

    elif ton_tier >= 2:

        if nt_pr_teach.points == 0: # Tell her to be even lewder for the next level of favors.

            "Dev Note" "Write 2nd intro."

        else: # Repeat
            m "Would you like to give some boys detention again?"
            call ton_main("And make them show me their dicks, Sir?", face="horny")
            m "If that's what you fancy..."
            call ton_main("Hmm...Yes. I wouldn't mind seeing the \"hard cocks\" of some of my \"favorites\"...", face="horny")
            m "And make sure they remember it."
            call ton_main("Yes, [ton_genie_name]. Don't wait for me...","base","base","base","mid")

    # Tonks leaves

    $ nt_pr_teach.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_teach_T1_E1: #Tier 1 - Event 1 - Slytherin boy
    call ton_main("Hi, [ton_genie_name].","base","base","base","mid")
    m "How were your extra curricular activities today?"
    call ton_main("It's such a rush!","base","base","base","mid")
    call ton_main("I can't believe how naughty I feel!","base","base","base","mid")
    m "So I take it you managed to sneak a peek?"
    call ton_main("Sort of... I didn't really see it.","base","base","base","mid")
    call ton_main("But it was still incredible...","base","base","base","mid")
    call ton_main("*Ugh*... that look on his face...","base","base","base","mid")
    m "What did you see then?"
    call ton_main("Well, this sweet little Slytherin kid had been staring at my boobs all lesson.","base","base","base","mid")
    call ton_main("So, naturally, I get him to stay behind after class.","base","base","base","mid")
    call ton_main("I couldn't tell if he was angrier than he was scared...","base","base","base","mid")
    call ton_main("But, as his teacher, I insisted that he write out some lines to correct his behavior.","base","base","base","mid")
    m "Do I need to ask what he had to write?"
    call ton_main("\"I will not stare at my teacher's big, beautiful breasts\"...","base","base","base","mid")
    m "Was the big and beautiful part really necessary?"
    call ton_main("Oh, that's not the best bit...","base","base","base","mid")
    call ton_main("I went on to tell him how {b}naughty{/b} it was for him to peek at me...","base","base","base","mid")
    call ton_main("Then I made him pull down his trousers before he wrote his lines.","base","base","base","mid")
    m "So you did see it!"
    call ton_main("He still had his underwear on. I think if I pushed him much further he would have snapped.","base","base","base","mid")
    call ton_main("Besides, I could still see how hard he was...","base","base","base","mid")
    call ton_main("Ugh... It was crazy...","base","base","base","mid")
    call ton_main("I might have teased him a little more while he wrote them out as well...","base","base","base","mid")
    m "The lines weren't enough?"
    call ton_main("Don't worry, I just whispered in his ear a little...","base","base","base","mid")
    call ton_main("Told him what a naughty boy he'd been...","base","base","base","mid")
    call ton_main("Let him know he'd earn some points for Slytherin...","base","base","base","mid")
    call ton_main("If my boobs happened to rub into his back a little while it happened I don't see how that's my fault.","base","base","base","mid") # This sentense is a bit convoluted.
    m "Ugh... that poor kid."
    call ton_main("Pfft... He was having the time of his life...","base","base","base","mid")
    call ton_main("His underwear was practically {b}soaked{/b} in precum.","base","base","base","mid")
    m "Well, do you think he'll spread the word about the favour trading?"
    call ton_main("I'm not sure... Maybe...","base","base","base","mid")
    call ton_main("All I know is that he won't be able to keep his eyes off of me next lesson.","base","base","base","mid")
    m "Very good. That'll be all."
    call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T1_E2: # Tier 1 - Event 2 - Racenclaw boy
    m "How were your classes today?"
    call ton_main("Mmmm... Long and hard... Just how I like them...","base","base","base","mid")
    m "I take it you were able to steal a few glances?"
    call ton_main("Mmmm, it was even better than I thought it'd be!","base","base","base","mid")
    call ton_main("Who knew they'd be so nervous!","base","base","base","mid")
    m "What happened?"
    call ton_main("Well, I figured I'd have to be alone with a student to manage to convince them to whip it out...","base","base","base","mid")
    call ton_main("So I gave the cutest little thing I could find detention...","base","base","base","mid")
    call ton_main("Poor boy, I'm not sure he'd ever even been in trouble before.","base","base","base","mid")
    call ton_main("So when the bell rang he immediately went on babbling about how sorry he was for speaking in class and how he'd never do it again...","base","base","base","mid")
    call ton_main("Ugh... I had to hold myself back from jumping him right then and there...","base","base","base","mid")
    call ton_main("Anyway, I eventually managed to calm him down and tell him it'll be alright...","base","base","base","mid")
    call ton_main("I even let him know that if he was a good boy he could earn some points for his house.","base","base","base","mid")
    m "Did he like the sound of that?"
    call ton_main("You should have seen his eyes light up! He thought it was Christmas!","base","base","base","mid")
    call ton_main("After that it was child's play...","base","base","base","mid")
    call ton_main("Not that he looked like a kid down there... Mmmm, I even had him play with himself for a little bit...","base","base","base","mid")
    call ton_main("Ugh... Fuck, he looked tasty...","base","base","base","mid")
    m "Ahem... So did you pay him his points or just tease him?"
    call ton_main("Don't worry, I made sure \"Ravenclaw\" was paid.","base","base","base","mid")
    m "And did he look like the kind to talk?"
    call ton_main("Probably not...","base","base","base","mid")
    m "Well try and get a talker next time. We're trying to build your reputation, remember?"
    call ton_main("I'll try...","base","base","base","mid")
    call ton_main("(Although I might have to play with this one a few more times...)","base","base","base","mid")
    m "That will be all for now, [tonks_name]."
    call ton_main("Thanks, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys. Guess who...
    m "How'd it go?"
    call ton_main("Great! I even managed to convince two boys to show me their dicks at the same time!","base","base","base","mid")
    m "Two at once? Nice."
    call ton_main("Yep. To be honest, they probably would have done it for free.","base","base","base","mid")
    call ton_main("Not that they turned down the offer of points though...","base","base","base","mid")
    m "Care to elaborate?"
    call ton_main("Alright then you old perv...","base","base","base","mid")
    call ton_main("Normally I'd just keep the cutest thing that takes my eye back after class for a little one-on-one time...","base","base","base","mid")
    call ton_main("But I actually had to punish these two idiots for real.","base","base","base","mid")
    m "What did they do?"
    call ton_main("Ugh... they wouldn't shut up, they kept trying to lift girl's skirts with \"wingardium leviosa\"...","base","base","base","mid")
    call ton_main("They reminded me of my younger self... Which probably meant they were going too far.","base","base","base","mid")
    call ton_main("So I kept them after class, gave them the whole lecture about responsibility and respect...","base","base","base","mid")
    m "..."
    # m "With their pants down?"
    # call ton_main("With their pants down!..."
    # call ton_main("I told them I'd pay them both ten points to show me their cocks as well."
    call ton_main("Then I told them I'd pay them both ten points to show me their cocks...","base","base","base","mid")
    m "Just like that?"
    call ton_main("Well, there's a lot more subtlety to it in practice...","base","base","base","mid")
    call ton_main("Not that I think I needed it given how horny they were.","base","base","base","mid")
    call ton_main("I think the poor buggers actually thought I was going to jerk them both off...","base","base","base","mid")
    call ton_main("Still, I think they had a fun time.","base","base","base","mid")
    m "Any chance they'll tell their friends about it?"
    call ton_main("Are you kidding me? The \"Gryffindor\" common room is probably a buzz already!","base","base","base","mid")
    call ton_main("It wouldn't surprise me if I start getting asked to give boys detention.","base","base","base","mid")
    m "Great work."
    call ton_main("Thank you, [ton_genie_name]. That means a lot coming from you.","base","base","base","mid")
    m "Even if it is encouragement for seducing your students?"
    call ton_main("Even then.","base","base","base","mid")
    call ton_main("Well, I better get back to work, these halls aren't safe unless there's a teacher on patrol.","base","base","base","mid")
    m "(I'm not sure they're safe with her on patrol...)"

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    m "Manage to sneak a peek today?"
    call ton_main("Um... Afraid not...","base","base","base","mid")
    m "Oh."
    call ton_main("But I do have a story for you!","base","base","base","mid")
    m "Well why didn't you just start with that? You had me worried for a moment there!"
    call ton_main("Are you that desperate to hear about me fooling around with my students?","base","base","base","mid")
    m "I'm desperate to hear {b}anything{/b}, this office isn't exactly riveting to listen to..."
    call ton_main("In that case, I'll try and add some flair to it.","base","base","base","mid")
    call ton_main("Once upon a time-","base","base","base","mid")
    m "Ahem..."
    call ton_main("Too much?","base","base","base","mid")
    m "Just a tad."
    call ton_main("So, I know my job is to try and balance out the favour trading a little...","base","base","base","mid")
    call ton_main("But I just couldn't help myself today...","base","base","base","mid")
    m "Help yourself? You mean..."
    call ton_main("Ugh, I don't normally mess around with girls...","base","base","base","mid")
    call ton_main("(Not since I left here anyway...)","base","base","base","mid")
    call ton_main("But there was the tastiest morsel I have ever seen in class.","base","base","base","mid")
    m "..."
    call ton_main("Now, I know when I'm being checked out, I can feel someones eyes on me...","base","base","base","mid")
    ">You nod, unconsciously gazing directly at her tits."
    call ton_main("And most of the time I don't mind... I might even encourage it from time to time...","base","base","base","mid")
    ">Tonks gives her boobs a subtle little shake. "
    call ton_main("So when I felt a pair of cute little eyes struggling they're hardest not to stare at me.","base","base","base","mid")
    call ton_main("I {b}had{/b} to play with her.","base","base","base","mid")
    m "Mmmm... what happened?"
    call ton_main("Nothing much... I'm pretty sure she would have freaked if I tried anything...","base","base","base","mid")
    call ton_main("So I just asked her to stay after class for a little... {b}chat{/b}.","base","base","base","mid")
    m "What did that chat involve?"
    call ton_main("Not much...","base","base","base","mid")
    call ton_main("I just sat directly in front of her desk...","base","base","base","mid")
    call ton_main("Asked her how she felt she was doing in class...","base","base","base","mid")
    call ton_main("I made sure to ask her if she was feeling distracted...","base","base","base","mid")
    call ton_main("All the while, playing with the buttons on my shirt...","base","base","base","mid")
    call ton_main("Ugh... I've never seen someone so flustered...","base","base","base","mid")
    call ton_main("Eventually, it got too much for her so she just yelled that I was wasting her time and ran off in typical \"Slytherin\" fashion.","base","base","base","mid")
    m "Do you really think she was looking at you?"
    call ton_main("After that? There's no doubt... she's hooked.","base","base","base","mid")
    call ton_main("Now I've just got to reel her in.","base","base","base","mid")
    call ton_main("If that's alright with you, sir!","base","base","base","mid")
    m "You're asking my permission?"
    call ton_main("Well, I was only supposed to buy favours from the boys...","base","base","base","mid")
    m "Eat your heart out. Just make sure you keep me in the loop."
    call ton_main("Thanks, [ton_genie_name].","base","base","base","mid")
    call ton_main("I can't believe how much you've mellowed out since I was a student.","base","base","base","mid")
    m "Oh, um... time can do that..."
    m "Speaking of, it's getting a bit late..."
    call ton_main("So it is... Night, sir.","base","base","base","mid")
    m "Goodnight, [tonks_name]."

    # Tonks leaves

    if ton_reputation < 3: # Points til 3.
        $ ton_reputation += 1

    jump end_tonks_event



### Tier 2 ###

label nt_pr_teach_T2_E1: # Tier 2 - Event 1 - Hufflepuff girl
    call ton_main("Guess what happened, [ton_genie_name]!","base","base","base","mid")
    m "Um... You found the golden ticket?"
    call ton_main("Better! I had a student come to me to sell a favour!","base","base","base","mid")
    m "And you haven't bought a favour from them before?"
    call ton_main("Not one! They're not even in any of my classes!","base","base","base","mid")
    m "Very good! Word must be getting around that you're... \"purchasing\"."
    m "So what house is he in?"
    call ton_main("Oh... um... it wasn't a he...","base","base","base","mid")
    call ton_main("I hope that's alright... I know I'm supposed to be balancing out the favours for the boys...","base","base","base","mid")
    m "Right...(I'd forgotten about Miss Grangers dumb M.R.M. thing...)"
    m "(Does she even still run that?)"
    m "I wouldn't worry about that too much... so long as you're still buying from the boys I don't think it should matter."
    call ton_main("Good... Because there was no way I could turn down this cute little \"Hufflepuff\"...","base","base","base","mid")
    call ton_main("Poor thing must have spent hours building up the courage...","base","base","base","mid")
    m "So what did you buy from her?"
    call ton_main("Well... I asked her what sort of favour she wanted to sell me...","base","base","base","mid")
    call ton_main("Poor thing was so flustered... She probably didn't plan this far ahead...","base","base","base","mid")
    call ton_main("She started babbling on so I just calmed her down by letting her know what favour I wanted...","base","base","base","mid")
    call ton_main("While she just sort of stood there stunned for a little bit I went and locked the door.","base","base","base","mid")
    call ton_main("After that I sat down in the front row of the class and told her to sit on my desk...","base","base","base","mid")
    m "Mmm, now that's a front row seat to die for."
    call ton_main("All that was missing was a bucket of popcorn...","base","base","base","mid")
    call ton_main("Eventually she was able to muster up enough courage to pull up her skirt...","base","base","base","mid")
    call ton_main("Poor thing only thought to ask how many points she'd be paid after she lifted her skirt though.","base","base","base","mid")
    call ton_main("I told her five for showing me her panties...","base","base","base","mid")
    m "Only five?"
    call ton_main("She said the same. I explained that showing her plain white panties only gets five points.","base","base","base","mid")
    call ton_main("If she were to take those panties off though... Then that might get \"Hufflepuff\" an extra twenty...","base","base","base","mid")
    m "Did she say yes?"
    call ton_main("She didn't say anything... but she pulled them down all the same...","base","base","base","mid")
    m "Nice! Getting a student to strip on the first favour is hard work!"
    call ton_main("Oh, we're not done yet... After soaking in the view for a while I started to notice she was soaking as well...","base","base","base","mid")
    call ton_main("So... I offered her fifty extra points to play with herself for me...","base","base","base","mid")
    m "Mmmm, go on..."
    call ton_main("Ugh... it was amazing... she was so nervous... it looked incredible on her face...","base","base","base","mid")
    call ton_main("That and the soft mewling she made while she did it...","base","base","base","mid")
    call ton_main("It was that perfect combination of slutty need and statuesque beauty...","base","base","base","mid")
    call ton_main("Argh... I wanted to taste her so badly...","base","base","base","mid")
    call ton_main("But instead, I held back... I don't think she's ready for that...","base","base","base","mid")
    call ton_main("I'm not sure she was ready for this... She sure as hell wasn't ready for the orgasm she had...","base","base","base","mid")
    call ton_main("Ugh... I had to spend ten minutes scourgifying the desk...","base","base","base","mid")
    m "Ah... very good... but I think that should be all for now..."
    m "Much more of this and I'll need to \"scour-ify\" my own desk..."
    call ton_main("Mmm, alright then, [ton_genie_name]. I better be on my way as well.","base","base","base","mid")
    call ton_main("(Fuck knows I could use a bit of \"alone\" time myself...)","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy
    #Have a few drops of cum on her clothes when she comes in
    m "How'd your day go?"
    call ton_main("The teaching was a little boring... Simple wards, hex-detection, basic stuff...","base","base","base","mid")
    call ton_main("Not that you'd know it was basic with how much they all struggled with it!","base","base","base","mid")
    m "I was sort of referring to your... \"extra-curricular\" activities."
    call ton_main("I know, I just wanted to get that off my chest. I'd complain to someone else but I'm not that fond of the other teachers...","base","base","base","mid")
    m "Oh?"
    call ton_main("Well McGonagall is as stuck up as ever, Snapes a gross weirdo, Hooch keeps trying to hit on me...","base","base","base","mid")
    call ton_main("Anyway, let's get onto the story, shall we?","base","base","base","mid")
    menu:
        "-Let her know about the cum-":
            $ choice_flag=True
            m "Sure... But, you know you've got cum on you, right?"
            call ton_main("Cum?","base","base","base","mid")
            ">Tonks looks down at her clothes, noticing the cum streaked along it."
            call ton_main("That cheeky bugger! I can't believe he actually shot it that far...","base","base","base","mid")
            m "..."
            call ton_main("I'll start from the beginning.","base","base","base","mid")
        "-Ignore it-":
            $ choice_flag=False
            pass
    call ton_main("So, I spent a little time with my favourite \"Ravenclaw\" student today...","base","base","base","mid")
    m "Another detention session after class?"
    call ton_main("I don't need to resort to detention anymore, he's learned what a wink in class means...","base","base","base","mid")
    call ton_main("Plus, I think a few of the other students have worked out what it means as well.","base","base","base","mid")
    call ton_main("There were a few whispers today... Hopefully that helps get the word out...","base","base","base","mid")
    m "I bet."
    call ton_main("So after class, I locked the door like normal and went over to him and let him know that I wanted another favour...","base","base","base","mid")
    call ton_main("He wanted to sell me a kiss today... I almost took him up on it honestly...","base","base","base","mid")
    call ton_main("But I told him I wanted something else... I wanted another look...","base","base","base","mid")
    call ton_main("I think he was a little disappointed... So I told him I didn't {b}just{/b} want to look at it...","base","base","base","mid")
    call ton_main("I wanted to see him play with it...","base","base","base","mid")
    call ton_main("His eyes lit up after that...","base","base","base","mid")
    call ton_main("He just started staring at me while he stroked it...","base","base","base","mid")
    call ton_main("Getting it hard for his teacher...","base","base","base","mid")
    call ton_main("Mmmm, the way he was staring at my tits... that hunger...","base","base","base","mid")
    call ton_main("I had to get them out for him.","base","base","base","mid")
    call ton_main("That really got him excited... He even started to speak after that...","base","base","base","mid")
    m "What did he say?"
    call ton_main("The usual stuff; how pretty I was, how nice my tits looked...","base","base","base","mid")
    call ton_main("You know how guys are...","base","base","base","mid")
    call ton_main("What was weird was when he started to call me mommy again...","base","base","base","mid")
    m "Did you tell him to stop?"
    call ton_main("What? Why? It's just a little dirty talk... I might have even joined in.","base","base","base","mid")
    m "Really?"
    call ton_main("What do you think made him fire his load across the room?","base","base","base","mid")
    call ton_main("All I said was \"cum for Mommy\" and he was blowing the biggest load I've seen.","base","base","base","mid")
    # call ton_main("(From a human...)"
    m "Fuck. That's pretty hot..."
    call ton_main("I know... Ugh... I need to go rub one out after it...","base","base","base","mid")
    call ton_main("See you, sir.","base","base","base","mid")
    m "Goodbye [tonks_name]."
    if choice_flag:
        m "Are you going to do anything about the cum?"
        call ton_main("Oh... Eh, why bother?","base","base","base","mid")
        call ton_main("I already had it on the way here. Besides, it'll be good for spreading the word.","base","base","base","mid")
        m "Whatever you say..."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T2_E3: # Tier 2 - Event 3 - Slytherin boy
    m "How'd your favour go today?"
    call ton_main("It was alright, I was able to kill two birds with one stone though.","base","base","base","mid")
    m "I'm intrigued."
    call ton_main("So, I had some cocky little \"Slytherin\" brat causing trouble in class.","base","base","base","mid")
    call ton_main("Talking, letting a chocolate frog loose, not locking his monster book of monsters.","base","base","base","mid")
    call ton_main("Just being a general pain in the ass.","base","base","base","mid")
    m "Sounds like a hassle."
    call ton_main("\"Slytherins\" always are.","base","base","base","mid")
    call ton_main("Anyway, I let him know he'd earned himself detention after class.","base","base","base","mid")
    call ton_main("Little bastard cursed me out for that...","base","base","base","mid")
    call ton_main("Once the class had emptied out I proceeded to lock the door to scare him a little...","base","base","base","mid")
    call ton_main("After that I let him know his Punishment was going to be selling me a favour.","base","base","base","mid")
    call ton_main("At first the idiot thought I was going to jerk him off...","base","base","base","mid")
    call ton_main("I might have, if he'd played his cards right...","base","base","base","mid")
    call ton_main("Instead, his favour wouldn't be nearly as fun.","base","base","base","mid")
    call ton_main("I made him pull down his pants and whip his cock out...","base","base","base","mid")
    call ton_main("He was so keen I bet he thought a blowjob was on the table...","base","base","base","mid")
    call ton_main("Eventually, I convinced him to start jacking it...","base","base","base","mid")
    call ton_main("Ugh... It was actually pretty cute at first...","base","base","base","mid")
    call ton_main("Then just as he was about to blow his load...","base","base","base","mid")
    call ton_main("Boom! Petrficus totalus!","base","base","base","mid")
    m "Petrifi-{w} Petrifico-?"
    g4 "(What does she even mean by that?)"
    call ton_main("I petrified him!","base","base","base","mid")
    m "*Ahh*..."
    call ton_main("Hahaha that look on his face!","base","base","base","mid")
    call ton_main("That's what he gets, the little shit. Not only did I leave him blueballed, I left him pants down in the class.","base","base","base","mid")
    m "Forever?"
    call ton_main("What? Just until the spell wears off.","base","base","base","mid")
    call ton_main("In an hour or so...","base","base","base","mid")
    call ton_main("That or someone else finds him...","base","base","base","mid")
    call ton_main("Either way, he's learned his lesson about screwing around in my class.","base","base","base","mid")
    m "Very good..."
    m "(This bitch might be crazier than I thought...)"
    call ton_main("Thank you, Sir...","base","base","base","mid")
    call ton_main("See you...","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_teach_T2_E4: # Tier 2 - Event 4 - Slytherin girl
    m "Anything interesting happen today, [ton_name]?"
    call ton_main("Did it ever... I broke new ground today...","base","base","base","mid")
    m "That's what I like to hear... So what happened?"
    call ton_main("Remember that cute little \"Slytherin\" that's still coming to grips with her budding sexuality?","base","base","base","mid")
    m "The girl you're turning into a lesbian, got it."
    call ton_main("Well, I had her stay back after class today...","base","base","base","mid")
    call ton_main("For someone who supposedly hates selling favours, she was surprisingly keen today...","base","base","base","mid")
    m "Maybe she's finally coming around..."
    call ton_main("Maybe... Anyway, we agreed on me getting a little peek under her skirt for 15 points...","base","base","base","mid")
    call ton_main("After she'd pulled up I did the old offer more points for her to drop her panties.","base","base","base","mid")
    call ton_main("I was expecting her to at least argue for more points but she dropped them in an instant.","base","base","base","mid")
    call ton_main("Next, she just looked at me as if to ask, \"what next?\"","base","base","base","mid")
    call ton_main("Ugh... it was so fucking hot...","base","base","base","mid")
    call ton_main("So I was going to have her play with herself...","base","base","base","mid")
    call ton_main("But that cute face of hers... and all the teasing...","base","base","base","mid")
    call ton_main("I decided to take matters into my own hands... specifically her matter...","base","base","base","mid")
    m "You couldn't help yourself, could you?"
    call ton_main("Ugh... You wouldn't blame me for fingering her if you saw how cute she was.","base","base","base","mid")
    call ton_main("And that look on her face... that perfect mix of lust and need...","base","base","base","mid")
    call ton_main("Fucking. incredible.","base","base","base","mid")
    m "What did she have to say about the whole thing?"
    call ton_main("Not much... She just looked up at me with those puppy-dog eyes whispering \"wow\" and \"don't stop\"...","base","base","base","mid")
    call ton_main("To think she tried to pretend she wasn't into me before...","base","base","base","mid")
    m "Good work, [tonks_name]. Think she'll start talking now?"
    call ton_main("Not unless she's ready to out herself as bi...","base","base","base","mid")
    call ton_main("But I think there are some whispers...","base","base","base","mid")
    m "Very good. That'll be all then."
    call ton_main("Thank you, sir... See you...","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event
