

### Grope me ###

# (Tonks lets her students play with her tits, ass,...)

label nt_pr_grope_start:

    if ton_tier == 2:

        if nt_pr_grope.points == 0:
            m "Ready for the next step?"
            call ton_main("Mmmm, you make it sound so ominous.","base","base","base","mid")
            call ton_main("So where do we go from here?","base","base","base","mid")
            call ton_main("Should I start making out with them?","base","base","base","mid")
            m "Pfft, may as well start holding hands."
            m "I was thinking you could take a few of these boys to second base."
            call ton_main("Second base?! Already?","base","base","base","mid")
            m "Obviously. We're trying to earn you a reputation as a favour trader."
            m "Making your students write lines in their underwear isn't going to cut it."
            call ton_main("I suppose you might be right...","base","base","base","mid")
            call ton_main("I'm not sure if the students will be ready for it though...","base","base","base","mid")
            m "Please, you sound like you're talking about a pop-quiz."
            m "All you have to do is get them to grope your chest a little..."
            m "I can't imagine any of them saying no to that."
            call ton_main("Mmm, well if you say so... You are the expert.","base","base","base","mid")
            m "That I am. Now get out there and buy some favours!"
            call ton_main("Yes, sir!","base","base","base","mid")
            call ton_main("(This is way better than being an auror!)","base","base","base","mid")

        else:
            m "Think you're up for messing around with your students again?"
            call ton_main("Mmm, you bet!","base","base","base","mid")
            m "Why don't you let them cop a feel then?"
            call ton_main("Consider it done.","base","base","base","mid")
            m "Good to hear. I'll see you after class."
            call ton_main("(I still can't believe Dumbledore is telling me to go molest my students...)","base","base","base","mid")
            call ton_main("Yes, sir!","base","base","base","mid")

    elif ton_tier >= 3:

        if nt_pr_grope.points == 0: # Tell her to be even lewder for the next level of favors.

            "Dev Note" "Write 2nd intro."

        else: # Repeat
            m "Would you like to mess around with your students again?"
            call ton_main("And let them grope their teacher?","base","base","base","mid")
            g9 "Anyway they like!"
            call ton_main("That sounds perfect!","base","base","base","mid")
            m "I'll see you after class..."
            call ton_main("Yes, [ton_genie_name]...{image=textheart}","base","base","base","mid")

    # Tonks leaves

    $ nt_pr_grope.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_grope_T1_E1: # Tier 1 - Event 1 - Slytherin boy
    m "How were classes today, [tonks_name]?"
    m "Taught your students some valuable lessons?"
    call ton_main("I'm not sure about valuable... But I do know that he isn't going to forget it anytime soon!","base","base","base","mid")
    m "That's what I like to hear! Go on."
    call ton_main("Remember that \"Slytherin\" cutie I held back to write lines?","base","base","base","mid")
    m "Vaguely."
    call ton_main("Well, I decided to hold him back after class again.","base","base","base","mid")
    call ton_main("He tried to put on a proud \"Slytherin\" facade, claiming that I had no right to hold him back.","base","base","base","mid")
    call ton_main("Saying he's lucky he didn't \"report me\" for making him pull down his pants the first time.","base","base","base","mid")
    call ton_main("It was all empty talk though... I could tell by the bulge in those pants he wanted to be there more than anything.","base","base","base","mid")
    call ton_main("Still, I let him act tough... just so he wouldn't run away...","base","base","base","mid")
    m "How did you manage to get him to grab a handful then."
    call ton_main("I let him know today wasn't a punishment. I just wanted to talk about him being so distracted in class.","base","base","base","mid")
    call ton_main("I sat down next to him and asked what was distracting him...{w} what he couldn't stop staring at...","base","base","base","mid")
    call ton_main("He didn't want to say at first, so I leaned in so close my breathe was on his neck...","base","base","base","mid")
    call ton_main("And then whispered in his ear that he was a dirty little tit addict.","base","base","base","mid")
    call ton_main("Ugh... he went redder than a tomato when I said that.","base","base","base","mid")
    m "No wonder."
    call ton_main("We're not done yet either!","base","base","base","mid")
    call ton_main("Next I told him there was only one cure, grabbed his wrist and forced it up to my chest.","base","base","base","mid")
    m "Just like that?"
    call ton_main("He was hardly going to grab them himself!","base","base","base","mid")
    call ton_main("Besides, grabbing them is the only way to get them off his mind...","base","base","base","mid")
    call ton_main("Or at least that's what I told him...","base","base","base","mid")
    m "And he believed you?"
    call ton_main("Maybe... Maybe not...","base","base","base","mid")
    call ton_main("All I know is that he wasn't afraid to give it a go.","base","base","base","mid")
    m "He enjoyed himself then?"
    call ton_main("Like you wouldn't believe. It was like a kid playing with lego for the first time.","base","base","base","mid") # Lego are muggle toys! No idea what wizards do  "It was like a kid playing with some bludgers..."
    call ton_main("He just sat there silently groping them for ten minutes straight...","base","base","base","mid")
    call ton_main("Ughh... It took everything I had not to hold him down and jump his bones...","base","base","base","mid")
    m "[tonks_name]..."
    call ton_main("Right, well after letting him have a play in Disneyland for a little while I sent him back to class.","base","base","base","mid") # Disneyland?
    m "Just like that?"
    call ton_main("There may have been a little more dirty talk... but that was just for me.","base","base","base","mid")
    m "Very well... Think you'll gain any rep from this encounter then?"
    call ton_main("Hmmm, I'm not sure if he'll talk... But the fact I keep holding boys behind should start to spread some rumours by itself.","base","base","base","mid")
    m "Good to hear. That'll be all then, [tonks_name]."
    call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    m "So, how are you finding the education industry?"
    call ton_main("Fun! I never though making lesson plans and marking tests would actually be enjoyable, but there's something rather cathartic to it...","base","base","base","mid")
    call ton_main("Plus, being allowed to mess around with your students is a nice bonus.","base","base","base","mid")
    m "Speaking of..."
    call ton_main("Don't worry, I've got a story for you old man.","base","base","base","mid")
    call ton_main("Remember that shy \"Ravenclaw\" boy I had touch himself for me the other day?","base","base","base","mid")
    m "Maybe, but go on."
    call ton_main("Well, he remembered me.","base","base","base","mid")
    call ton_main("I didn't even have to ask him to stay behind after class this time!","base","base","base","mid")
    m "You mean he started coming onto you?"
    call ton_main("I wouldn't say that... He just sort of stayed in his seat after class while looking down at his desk.","base","base","base","mid")
    call ton_main("So I waited until every other student had left before I locked the door...","base","base","base","mid")
    m "Keeping him locked in with you. Nice..."
    call ton_main("It's more to keep the other students out. But that doesn't mean he didn't gasp a little when I did it.","base","base","base","mid")
    call ton_main("So after that I walked over and asked him if there was anything wrong.","base","base","base","mid")
    call ton_main("He started mumbling about being sorry I had to give him detention, how he promised he'd never do anything bad in class again.","base","base","base","mid")
    call ton_main("Mmmm, those poor \"Ravenclaws\" sure do care about school.","base","base","base","mid")
    call ton_main("I let him know that I forgave him... But he didn't try and get up from his seat.","base","base","base","mid")
    call ton_main("So, I figured he wanted to fool around again...","base","base","base","mid")
    call ton_main("And boy was I right. You should have seen his face light up when I asked him about buying another favour!","base","base","base","mid")
    call ton_main("You'd think it was Christmas!","base","base","base","mid")
    m "Pfft, fooling around with you would be better than Christmas!"
    call ton_main("Mmmm, thanks [ton_genie_name]... I think he thought the same.","base","base","base","mid")
    m "So did you go straight for the kill?"
    call ton_main("No... I wanted to play with my food first.","base","base","base","mid")
    call ton_main("That look of nervous awe as he gazed up at me after I asked him if he wanted to touch his teachers boobs.","base","base","base","mid")
    call ton_main("It made it impossible for me to tell what he was going to do next, cheeky bugger.","base","base","base","mid")
    m "Which was?"
    call ton_main("He went straight in for the motorboat!","base","base","base","mid")
    m "Good on him! Did he do the noise as well?"
    call ton_main("No... it was more like a hug if I'm being honest.","base","base","base","mid")
    call ton_main("He just went in, face first into my cleavage while his hands locked together behind my back.","base","base","base","mid")
    call ton_main("I thought he was going to require much more coaxing into it.","base","base","base","mid")
    m "So where'd he go from there?"
    call ton_main("No where really, he just stared nuzzling his face into my cleavage, grinding himself against my thigh while giving me the tightest hug of his life.","base","base","base","mid")
    m "Sound's like he went to heaven then."
    call ton_main("Maybe... It was pretty cute if I'm being honest.","base","base","base","mid")
    m "How long did this \"hug\" go on for?"
    call ton_main("About five or ten minutes.","base","base","base","mid")
    call ton_main("Eventually it all got too much for him and he just broke of the hug, said thanks and ran off.","base","base","base","mid")
    m "Very good. Did you make sure to pay him his points?"
    call ton_main("I did, even if he wasn't there to hear it...","base","base","base","mid")
    m "That'll be all then."
    call ton_main("See ya, [ton_genie_name].","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys
    m "I think I noticed a few extra points for \"Gryffindor\" today."
    m "Does that mean what I think it does?"
    call ton_main("Maybe...","base","base","base","mid")
    m "So you let a boy cop a feel?"
    call ton_main("Sort of...","base","base","base","mid")
    call ton_main("It might have been two boys...","base","base","base","mid")
    m "Nice, selling two favours in one day should get the word around."
    call ton_main("Well... it wasn't exactly two favours...","base","base","base","mid")
    m "You don't mean... Both at once?"
    call ton_main("They're such good friends! I don't think I could manage to split them apart...","base","base","base","mid")
    call ton_main("Besides, I've already fooled around a little with them so they were easy to rope in.","base","base","base","mid")
    m "I'm sure they were... so how was it?"
    call ton_main("Honestly? Pretty fucking hot...","base","base","base","mid")
    call ton_main("Having four hands clawing at you at once is {b}intense{/b}...","base","base","base","mid")
    m "I bet... So they just played with your tits?"
    call ton_main("At first... they were quick to start moving around though...","base","base","base","mid")
    call ton_main("They both had a cheek in each hand pretty soon after that... ","base","base","base","mid")
    call ton_main("Ugh... I had to draw the line once they tried taking my bra off though.","base","base","base","mid")
    m "Mmmm, did you?"
    call ton_main("If I didn't draw it there I don't think I would have been able to stop them at all...","base","base","base","mid")
    call ton_main("Not that it would be the worst thing in the world to let them...","base","base","base","mid")
    call ton_main("Ugh...","base","base","base","mid")
    call ton_main("Anyway, I paid \"Gryffindor\" handsomely for their work and sent them on their way...","base","base","base","mid")
    m "Think they'll spread the word this time?"
    call ton_main("Who knows... The tent they were both pitching when they left class will probably send the message though.","base","base","base","mid")
    m "Mmmm, very good, [tonks_name], very good..."
    call ton_main("Thank you, sir. Now if you don't mind, I think I need to go to my room to \"unwind\"...","base","base","base","mid")
    m "Goodnight."
    call ton_main("Night.","base","base","base","mid")
    call ton_main("(Mmmm, who knows, I might even come across {i}Potter{/i} and {i}Weasley{/i} on my walk back...)","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    m "How's my favorite teacher doing today?"
    call ton_main("Never better!","base","base","base","mid")
    m "I take it you were able to buy a favour then?"
    call ton_main("You bet! Even if she might not have wanted to sell it at first...","base","base","base","mid")
    m "She?"
    call ton_main("Remember that naive \"Slytherin\" that couldn't keep her eyes off of me?","base","base","base","mid")
    m "I think so..."
    call ton_main("Well, I held her back after class again.","base","base","base","mid")
    call ton_main("Mmmm, she really didn't like that... Not that she tried to leave.","base","base","base","mid")
    call ton_main("So I sat her down and had a little conversation with her.","base","base","base","mid")
    call ton_main("About how it's alright to be a little confused sometimes...","base","base","base","mid")
    call ton_main("And that maybe she just needed to get it all out of her system.","base","base","base","mid")
    m "How did she take that?"
    call ton_main("She kept insisting that she didn't have any idea what I was talking about.","base","base","base","mid")
    call ton_main("Even though her eyes were still glued to my chest.","base","base","base","mid")
    call ton_main("Eventually I just walked over to her, grabbed her wrist and pulled it up to my chest.","base","base","base","mid")
    m "Just like that?"
    call ton_main("Mhmm... Ugh, it was fantastic!","base","base","base","mid")
    call ton_main("You should have seen the war of emotions taking place behind her eyes!","base","base","base","mid")
    call ton_main("It was incredible! I love seeing \"Slytherins\" get all flustered like that.","base","base","base","mid")
    m "What happened after the shock wore off?"
    call ton_main("She tried to pull away at first...","base","base","base","mid")
    call ton_main("But I was able to calm her down by telling her I just needed to buy a favour from her.","base","base","base","mid")
    m "That calmed her down?"
    call ton_main("Apparently it's not the first that she's sold.","base","base","base","mid")
    m "So she started to play around then?"
    call ton_main("Not really, she just sat there with a bright red face while she let me hold her hand against my boob.","base","base","base","mid")
    call ton_main("I let her go about ten seconds after that.","base","base","base","mid")
    m "Do you think she'll spread that you're buying favours?"
    call ton_main("I can't say... I think she's still pretty conflicted about the whole thing...","base","base","base","mid")
    m "Do you really think she's a lesbian?"
    call ton_main("A lesbian? Probably not, I just think she's a little {b}curious{/b}...","base","base","base","mid")
    call ton_main("Couple that with her being a stubborn \"slytherin\" and you get a whole confusing mix of emotions...","base","base","base","mid")
    call ton_main("It's perfect.","base","base","base","mid")
    m "Well keep me informed. That will be all for now..."
    call ton_main("Yes, sir!","base","base","base","mid")
    call ton_main("(I still can't believe that I get to fool around with those students...)","base","base","base","mid")
    call ton_main("(Best. job. ever.)","base","base","base","mid")

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event



### Tier 2 ###

label nt_pr_grope_T2_E1: # Tier 2 - Event 1
    #Begrudgingly talks about how pretty tonks is


label nt_pr_grope_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy again
    #breastfeeding and mommy play



label nt_pr_grope_T2_E3: # Tier 2 - Event 3
    #hufflepuff girl comes in asking for another favour
    #ends up sucking tonks boobs



label nt_pr_grope_T2_E4: # Tier 2 - Event 4 -
    #Tonks has her a slyhterin girl sit there and do work while she has no top on
