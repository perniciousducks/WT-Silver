

### Grope me ###

# (Tonks lets her students play with her tits, ass,...)

label nt_pr_grope_start:

    if ton_tier == 2:

        if nt_pr_grope.points == 0:
            m "Ready for the next step?"
            ton "Mmmm, you make it sound so ominous."
            ton "So where do we go from here?"
            ton "Should I start making out with them?"
            m "Pfft, may as well start holding hands."
            m "I was thinking you could take a few of these boys to second base."
            ton "Second base?! Already?"
            m "Obviously. We're trying to earn you a reputation as a favour trader."
            m "Making your students write lines in their underwear isn't going to cut it."
            ton "I suppose you might be right..."
            ton "I'm not sure if the students will be ready for it though..."
            m "Please, you sound like you're talking about a pop-quiz."
            m "All you have to do is follow the damn train-ahem"
            m "All you have to do is get them to grope your chest a little..."
            m "I can't imagine any of them saying no to that."
            m "Goodness knows I wouldn't..."
            ton "Mmm, well if you say so... You are the expert."
            m "That I am. Now get out there and buy some favours!"
            ton "Yes, sir!"
            ton "(This is way better than being an auror!)"

        else:
            m "Think you're up for messing around with your students again?"
            ton "Mmm, you bet!"
            m "Why don't you let them cop a feel then?"
            ton "Consider it done."
            m "Good to hear. I'll see you after class."
            ton "(I still can't believe Dumbledore is telling me to go molest my students...)"
            ton "Yes, sir!"

    elif ton_tier >= 3:

        if nt_pr_grope.points == 0: # Tell her to be even lewder for the next level of favors.

            "Dev Note" "Write 2nd intro."

        else: # Repeat
            m "Would you like to mess around with your students again?"
            ton "And let them grope their teacher?"
            g9 "Anyway they like!"
            ton "That sounds perfect!"
            m "I'll see you after class..."
            ton "Yes, [ton_genie_name]...{image=textheart}"

    # Tonks leaves

    $ nt_pr_grope.inProgress = True

    jump end_tonks_event



### Tier 1 ###

label nt_pr_grope_T1_E1: # Tier 1 - Event 1 - Slytherin boy
    m "How were classes today, [tonks_name]?"
    m "Taught your students some valuable lessons?"
    ton "I'm not sure about valuable... But I do know that he isn't going to forget it anytime soon!"
    m "That's what I like to hear! Go on."
    ton "Remember that \"Slytherin\" cutie I held back to write lines?"
    m "Vaguely."
    ton "Well, I decided to hold him back after class again."
    ton "He tried to put on a proud \"Slytherin\" facade, claiming that I had no right to hold him back."
    ton "Saying he's lucky he didn't \"report me\" for making him pull down his pants the first time."
    ton "It was all empty talk though... I could tell by the bulge in those pants he wanted to be there more than anything."
    ton "Still, I let him act tough... just so he wouldn't run away..."
    m "How did you manage to get him to grab a handful then."
    ton "I let him know today wasn't a punishment. I just wanted to talk about him being so distracted in class."
    ton "I sat down next to him and asked what was distracting him...{w} what he couldn't stop staring at..."
    ton "He didn't want to say at first, so I leaned in so close my breathe was on his neck..."
    ton "And then whispered in his ear that he was a dirty little tit addict."
    ton "Ugh... he went redder than a tomato when I said that."
    m "No wonder."
    ton "We're not done yet either!"
    ton "Next I told him there was only one cure, grabbed his wrist and forced it up to my chest."
    m "Just like that?"
    ton "He was hardly going to grab them himself!"
    ton "Besides, grabbing them is the only way to get them off his mind..."
    ton "Or at least that's what I told him..."
    m "And he believed you?"
    ton "Maybe... Maybe not..."
    ton "All I know is that he wasn't afraid to give it a go."
    m "He enjoyed himself then?"
    ton "Like you wouldn't believe. It was like a kid playing with lego for the first time." # Lego are muggle toys! No idea what wizards do  "It was like a kid playing with some bludgers..."
    ton "He just sat there silently groping them for ten minutes straight..."
    ton "Ughh... It took everything I had not to hold him down and jump his bones..."
    m "[tonks_name]..."
    ton "Right, well after letting him have a play in Disneyland for a little while I sent him back to class." # Disneyland?
    m "Just like that?"
    ton "There may have been a little more dirty talk... but that was just for me."
    m "Very well... Think you'll gain any rep from this encounter then?"
    ton "Hmmm, I'm not sure if he'll talk... But the fact I keep holding boys behind should start to spread some rumours by itself."
    m "Good to hear. That'll be all then, [tonks_name]."
    ton "Thank you, [ton_genie_name]."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E2: # Tier 1 - Event 2 - Ravenclaw boy
    m "So, how are you finding the education industry?"
    ton "Fun! I never though making lesson plans and marking tests would actually be enjoyable, but there's something rather cathartic to it..."
    ton "Plus, being allowed to mess around with your students is a nice bonus."
    m "Speaking of..."
    ton "Don't worry, I've got a story for you old man."
    ton "Remember that shy \"Ravenclaw\" boy I had touch himself for me the other day?"
    m "Maybe, but go on."
    ton "Well, he remembered me."
    ton "I didn't even have to ask him to stay behind after class this time!"
    m "You mean he started coming onto you?"
    ton "I wouldn't say that... He just sort of stayed in his seat after class while looking down at his desk."
    ton "So I waited until every other student had left before I locked the door..."
    m "Keeping him locked in with you. Nice..."
    ton "It's more to keep the other students out. But that doesn't mean he didn't gasp a little when I did it."
    ton "So after that I walked over and asked him if there was anything wrong."
    ton "He started mumbling about being sorry I had to give him detention, how he promised he'd never do anything bad in class again."
    ton "Mmmm, those poor \"Ravenclaws\" sure do care about school."
    ton "I let him know that I forgave him... But he didn't try and get up from his seat."
    ton "So, I figured he wanted to fool around again..."
    ton "And boy was I right. You should have seen his face light up when I asked him about buying another favour!"
    ton "You'd think it was Christmas!"
    m "Pfft, fooling around with you would be better than Christmas!"
    ton "Mmmm, thanks [ton_genie_name]... I think he thought the same."
    m "So did you go straight for the kill?"
    ton "No... I wanted to play with my food first."
    ton "That look of nervous awe as he gazed up at me after I asked him if he wanted to touch his teachers boobs."
    ton "It made it impossible for me to tell what he was going to do next, cheeky bugger."
    m "Which was?"
    ton "He went straight in for the motorboat!"
    m "Good on him! Did he do the noise as well?"
    ton "No... it was more like a hug if I'm being honest."
    ton "He just went in, face first into my cleavage while his hands locked together behind my back."
    ton "I thought he was going to require much more coaxing into it."
    m "So where'd he go from there?"
    ton "No where really, he just stared nuzzling his face into my cleavage, grinding himself against my thigh while giving me the tightest hug of his life."
    m "Sound's like he went to heaven then."
    ton "Maybe... It was pretty cute if I'm being honest."
    m "How long did this \"hug\" go on for?"
    ton "About five or ten minutes."
    ton "Eventually it all got too much for him and he just broke of the hug, said thanks and ran off."
    m "Very good. Did you make sure to pay him his points?"
    ton "I did, even if he wasn't there to hear it..."
    m "That'll be all then."
    ton "See ya, [ton_genie_name]."

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys
    m "I think I noticed a few extra points for \"Gryffindor\" today."
    m "Does that mean what I think it does?"
    ton "Maybe..."
    m "So you let a boy cop a feel?"
    ton "Sort of..."
    ton "It might have been two boys..."
    m "Nice, selling two favours in one day should get the word around."
    ton "Well... it wasn't exactly two favours..."
    m "You don't mean... Both at once?"
    ton "They're such good friends! I don't think I could manage to split them apart..."
    ton "Besides, I've already fooled around a little with them so they were easy to rope in."
    m "I'm sure they were... so how was it?"
    ton "Honestly? Pretty fucking hot..."
    ton "Having four hands clawing at you at once is {b}intense{/b}..."
    m "I bet... So they just played with your tits?"
    ton "At first... they were quick to start moving around though..."
    ton "They both had a cheek in each hand pretty soon after that... "
    ton "Ugh... I had to draw the line once they tried taking my bra off though."
    m "Mmmm, did you?"
    ton "If I didn't draw it there I don't think I would have been able to stop them at all..."
    ton "Not that it would be the worst thing in the world to let them..."
    ton "Ugh..."
    ton "Anyway, I paid \"Gryffindor\" handsomely for their work and sent them on their way..."
    m "Think they'll spread the word this time?"
    ton "Who knows... The tent they were both pitching when they left class will probably send the message though."
    m "Mmmm, very good, [tonks_name], very good..."
    ton "Thank you, sir. Now if you don't mind, I think I need to go to my room to \"unwind\"..."
    m "Goodnight."
    ton "Night."
    ton "(Mmmm, who knows, I might even come across {i}Harry{/i} and {i}Ron{/i} on my walk back...)" #Italics to draw attention to the name reveal # Note: Would change it to "Potter" and "Weasley"

    # Tonks leaves

    if ton_reputation < 9: # Points til 9.
        $ ton_reputation += 1

    jump end_tonks_event


label nt_pr_grope_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    m "How's my favorite teacher doing today?"
    ton "Never better!"
    m "I take it you were able to buy a favour then?"
    ton "You bet! Even if she might not have wanted to sell it at first..."
    m "She?"
    ton "Remember that naive \"slytherin\" that couldn't keep her eyes off of me?"
    m "I think so..."
    ton "Well, I held her back after class again."
    ton "Mmmm, she really didn't like that... Not that she tried to leave."
    ton "So I sat her down and had a little conversation with her."
    ton "About how it's alright to be a little confused sometimes..."
    ton "And that maybe she just needed to get it all out of her system."
    m "How did she take that?"
    ton "She kept insisting that she didn't have any idea what I was talking about."
    ton "Even though her eyes were still glued to my chest."
    ton "Eventually I just walked over to her, grabbed her wrist and pulled it up to my chest."
    m "Just like that?"
    ton "Mhmm... Ugh, it was fantastic!"
    ton "You should have seen the war of emotions taking place behind her eyes!"
    ton "It was incredible! I love seeing \"Slytherins\" get all flustered like that."
    m "What happened after the shock wore off?"
    ton "She tried to pull away at first..."
    ton "But I was able to calm her down by telling her I just needed to buy a favour from her."
    m "That calmed her down?"
    ton "Apparently it's not the first that she's sold."
    m "So she started to play around then?"
    ton "Not really, she just sat there with a bright red face while she let me hold her hand against my boob."
    ton "I let her go about ten seconds after that."
    m "Do you think she'll spread that you're buying favours?"
    ton "I can't say... I think she's still pretty conflicted about the whole thing..."
    m "Do you really think she's a lesbian?"
    ton "A lesbian? Probably not, I just think she's a little {b}curious{/b}..."
    ton "Couple that with her being a stubborn \"slytherin\" and you get a whole confusing mix of emotions..."
    ton "It's perfect."
    m "Well keep me informed. That will be all for now..."
    ton "Yes, sir!"
    ton "(I still can't believe that Dumbledore is having me fool around with my students...)"
    ton "(Best. job. ever.)"

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
