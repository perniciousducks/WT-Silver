

### Manipulate the enemy Quidditch players ###

# Start
label cc_pr_manipulate_start: # Complete. Not posed.

    ### Tier 1 ###
    if main_matches_won == 0: # Pre Hufflepuff.

        # Intro
        if cc_pr_manipulate.points == 0:
            m "So what do we know about our opponents?"
            cho "Hufflepuff? Well their team isn't the best, but they have a really strong seeker."
            m "Right...{w} who was that again?"
            cho "Cedric Diggory. How often do I have to repeat myself, [cho_genie_name]?"
            m "You will know, once you get to be my age..."
            g4 "(Because then you stop giving a damn...)"
            cho "I'm so sorry Sir!{w} I'll be more respectful of your age from now on!"
            cho "Cedric is a bit of a block head, but he's quite a competent seeker."
            cho "And very popular with the girls..."
            m "Do I sense a little bit of something in your voice?"
            cho "Of course not! We stopped dating ages ago!"
            cho "I didn't want to be seen with an idiot like him anymore, not if I'm supposed to be a proper Ravenclaw..."
            cho "Even if he is cute..." # Small text.
            m "That's good. We can use this to our advantage."
            cho "We can? How?"
            m "You two having history! Which means he'll be much easier to distract during the game."
            m "All you have to do is make him believe something might actually happen."
            cho "What? I don't want to go out with Cedric again!"
            m "I know, I know, you just have to make him believe that you will."
            cho "Oh-... Well,... how do I do that?"
            m "It's a little something called seduction. It should be your genders bread and butter."
            cho "Isn't it a little mean?"
            m "Mean? You're not doing anything wrong are you? You're just talking to him."
            cho "So I'm just supposed to lead him down the garden path?"
            m "Only if you want Ravenclaw to have a chance at winning."
            cho "*Hmmm*..."
            m "And don't worry about him.{w} He's hardly going to complain about having a pretty little thing like you to talk to..."
            g9 "Not to mention look at..."
            cho "Hey!"
            m "I'm just saying, he's hasn't got anything to be whine about."
            m "And if you are worried about his feelings..."
            m "Maybe you can fool around a little... I'm sure that would make him forget all about the garden path..."
            cho "Sir!"
            m "I'm just telling you to use what the gods gave you to try and win a game."
            cho "Can't I use what they gave me to just catch the snitch?"
            m "And how's that plan been working out so far?"
            cho "*Ugh!* Fine...{w} Point taken..."
            cho "So I just have to make him think there's something between us again?"
            cho "I think I can do that...{w} For Ravenclaw..."
            m "Good, let me know how it goes later today."
            cho "Yes, [cho_genie_name]!"

        # Repeated
        else:
            m "Ready to mess with Hufflepuff again?"
            cho "I guess so..."
            g9 "Great! I'll see you later today for your report, [cho_name]!"
            cho "Yes, [cho_genie_name]!"


    ### Tier 2 ###
    else: # Pre Slytherin.

        # Intro
        if cc_pr_manipulate.points == 0:
            m "[cho_name], how well, in your opinion, did you do in your last match?"
            cho "I think I did quite well with distracting those Hufflepuffs..."
            m "Only one Hufflepuff! We were lucky you could secure that win even with such little effort..."
            cho "(...)"
            m "We have to up our game to win against the next house, don't you think?"
            m "Manipulating just one player won't be enough this time! We have to put our focus on their entire team!"
            cho "You might be right, [cho_genie_name]. Slytherin's team is quite good overall, and they have some of the best players at this school."
            cho "What do you suggest I should do?"
            m "Same as with that Diggory boy!"
            g4 "Go and talk to them, be affectionate and flirty, make out with them..."
            cho "Make out with? Those Slytherins-"
            cho "*guargh!*"
            ">You hear Cho make some inadvertent gag noises..."
            m "Is everything okay, girl?"
            cho "No! It's not ok! I'd never go and start snogging with those ugly, repulsive, Slytherin brutes!"
            cho "The thought alone is utterly disgusting, [cho_genie_name]!"
            cho "I'll do anything but that!"
            m "So no kissing?"
            cho "Absolutely not! Not even with Malfoy..."
            m "(...)
            cho "Besides, Sir. They're Slytherins! What if someone saw me with them?"
            m "Would that be an issue?"
            cho "If they are on the enemy team, yes! What if my team was to find out I hang around them?"
            m "So... just do it in secret, then."
            cho "That... might work."
            m "Don't you have any classes with them?"
            cho "I guess..."
            m "Then give them a note to meet you alone once the class is finished, easy..."
            m "They can read right?"
            cho "Yes, I do believe they can read..."

            m "You need to find a way to convince them to throw the game. It's our only chance..."
            m "Do you have any ideas?"
            cho "I- *uhm*..."
            cho "I could still try to flirt with them, I guess."
            m "I doubt that that will be enough..."
            m "But, let's just try it and see how it goes."
            m "If anything goes wrong... just improvise..."
            cho "Very well, Sir. I'll try my best!"
            m "Report back to me later today with your results."
            cho "Yes, Sir!"

        # Repeated
        else:
            pass








    call cho_walk(action="leave", speed=1.6)

    $ cc_pr_manipulate.inProgress = True

    # First Star
    if cc_pr_manipulate.points == 0:
        $ cc_pr_manipulate.level = 1
    # Second Star, gets added when you play the last event in the list.

    $ cc_pr_manipulate.points += 1 # Points get set to 0 when you beat Hufflepuff.

    # Stats
    $ cc_pr_manipulate.counter += 1

    jump end_cho_event



# Ideas

### Tier 1 ###

# Intro:
# Cedric tried to kiss her.

label cc_pr_manipulate_T1_intro:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    call cho_main(face="happy",xpos="mid",ypos="base",trans="fade")
    m "How did it go?"
    cho "It went...{w} well?"
    cho "Maybe a little too well... He tried to kiss me!"
    g9 "Really? Nice work!{w} Did you slip him a little tongue?"
    cho "[cho_genie_name]! Of course not!"
    m "Why not?"
    cho "Because I'm not some slut who gives it away for free!"
    m "It was only a kiss..."
    m "(Now I'm falling asleep)"
    cho "A kiss is very personal!"
    cho "Besides, he didn't even try to make it special!"
    cho "He just leaned in while I was in the middle of a conversation..."
    m "Sounds special enough to me."
    cho "Well it wasn't! I want a bit of romance..."
    m "At least it sounds like you're doing a good job distracting him."
    cho "If you say so..."
    m "Just keep in mind why we're doing this."
    g4 "You can't chicken out of something as small as a kiss if you want \"Ravenclaw\" to have a chance!"
    cho "Right, [cho_genie_name]!"
    m "That'll be all for now, you can go."
    cho "Thank you, [cho_genie_name]."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event



# Random/Repeatable:

label cc_pr_manipulate_T1_E1:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    call cho_main(face="happy",xpos="mid",ypos="base",trans="fade")
    m "What's my favourite Quidditch player been up to today?"
    cho "I think you'll be happy, [cho_genie_name]!"
    g9 "I like the sound of that! Tell me what happened."
    cho "Well, I thought about the best way to get to Cedric and I remembered how much he loved my bum!"
    m "Mmm, I can't say I blame him..."
    m "Let me guess, you tried the old \"drop your pencil trick\" on him?"
    cho "\"Pencil trick\"?"
    m "Yes. You \"accidentally\" drop your pencil, and then when you have the boy's attention, you bent down and-"
    cho "Sir, we're only allowed to use quills here."
    m "So just use quills instead?"
    cho "That would just get ink everywhere on the ground..."
    cho "But I \"did\" try something \"close\" to what you described..."
    g9 "You did?"
    cho "Yes, Sir. I pretended to drop my books, and when I bent down to pick them up, I gave Cedric a good view of my bum."
    m "So...{w} you did the \"pencil trick\"...{w} Just with books."
    cho "I've put my own spin on it. It's different enough..."
    m "No it isn't."
    cho "In any case, I think it worked."
    cho "He couldn't keep his eyes off my bum for the rest of classes!"
    g9 "Well done, [cho_name]! You may leave now."
    cho "Thank you, Sir."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event


label cc_pr_manipulate_T1_E2:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    call cho_main(face="annoyed",xpos="mid",ypos="base",trans="fade")
    g4 "[cho_name]! Do you have some good news for me?"
    cho "I'm afraid not this time, Sir."
    m "Why not? Tell me what happened..."
    cho "Well, today I saw Cedric again down in the dungeons."
    g9 "(The dungeons? I like where this is going already!)"
    cho "Before I approached him I removed my \"Ravenclaw\"tie, and unbuttoned the top of my blouse."
    m "A very well thought out strategy, girl!"
    cho "I thought it would be enough to get his attention."
    m "Which I assume you got straight away?"
    cho "No, Sir. But somebody elses..."
    g9 "Intriguing! Who else did you manage to snag?"
    cho "Professor Slughorn, Sir."
    g4 "Who?"
    cho "The Alchemy professor... also stand in for potions when Snape can't make it."
    m "Snape is missing his classes? How often has this been happening?"
    cho "Probably every other week or so."
    m "Slacker..."
    cho "..."
    cho "Anyway, Slughorn sort of crossed my path when I was on my way to Cedric, down the hallway..."
    cho "He came out of nowhere!"
    cho "And he stood so close, he could see right down my cleavage!"
    g4 "What a lucky git!"
    cho "I couldn't move a single muscle! It was like I was frozen in place!"
    cho "What if something like that would happen during the game?!"
    m "You are right. That could be an issue..."
    cho "And the worst thing is, he just kept staring!"
    m "And then? What happened?"
    cho "He commended me about how well I did in my last potion lesson with him, so he awarded \"Ravenclaw\" five house points for my efforts."
    m "Sounds like a nice guy..."
    cho "But Sir, I ruined my potion during the last lesson I had with him!"
    cho "The only reason he gave me those points, is because I let him stare down my shirt!"
    cho "I feel so dirty because of it..."
    m "You shouldn't feel dirty...{w} Maybe only feel a \"little\" dirty, if anything..."
    cho "I'm sorry, Sir. May I leave now?"
    m "Sure... But try to be more effective next time."
    cho "I will, Sir."
    cho "Have a nice day."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event


label cc_pr_manipulate_T1_E3:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    call cho_main(face="happy",xpos="mid",ypos="base",trans="fade")
    m "So? How did it go?"
    cho "Very well, Sir!"
    g9 "Yeah? Tell me about it!"
    cho "I ran into Cedric on my way to the library... Literally!"
    cho "I bumped into him and hit my head pretty hard..."
    m "You poor thing."
    cho "It's nothing. I'm used to pain by now."
    g4 "*gulp!*"
    cho "After all those years of playing Quidditch, I've grown pretty resistent to it..."
    m "A useful skill to have I suppose..."
    cho "Anyway, Cedric helped me back up on my feet, but before he could even apoligize, I kissed him!"
    cho "It just... happened..."
    m "Well done, girl!"
    cho "It was really nice, though. He still is a really good kisser!"
    cho "Compared to most of the others I had, at the very least..."
    g4 "!!!"
    cho "Anyhow, I should get going, Sir."
    cho "It's getting late..."
    m "Of course."
    cho "Good night, [cho_genie_name]."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    $ cc_pr_manipulate.level = 2

    jump end_cho_event



### Tier 2 ###

label cc_pr_manipulate_T2_intro:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    m "Good evening [cho_name], How did todays task go?"
    cho "I can't believe you convinced me to do this."
    m "So badly I take it?"
    cho "No, it went perfectly..."
    m "So why the face?"
    cho "Well, I did as you suggested, I left a note for them to meet me alone after class."
    m "Great, so did they show?"
    cho "Yes... apparently they could read and they met with me after the lesson."
    cho "Once everyone had left and we were alone in the corridor. I didn't really know how to go about it."
    cho "They must've felt how awkward I was as I approached them, or they had literally never had any woman approach them before."
    m "So they didn't get that you were coming onto them, sure they're not that thick..."
    cho "No sir, they got it alright... perhaps a little too well."
    cho "Or they're just used to treating those Slytherin skanks as their personal squeeze toys."
    m "So, what happened?"
    cho "I came onto them a little bit, since they're new on the Slytherin team I told them how impressed I was when watching their practice match against Gryffindor."
    cho "Told them that it must be lonely on the pitch with no girls on their team so fool around with in the showers."
    cho "I couldn't stand the idea of complimenting them on their looks so I told them how impressed I am with their pure strength... which technically isn't a lie,"
    m "Understandable... but what about getting them to take it a bit easier on you during the game itself?"
    cho "I'm getting to it..."
    cho "I was asking them how much the game meant to them and what I could do to persuade them to take it easy... They didn't really seem to know what I meant. They just do whatever Draco tells them to."
    m "Sounds like trying to make a cat understand how to bark."
    cho "Exactly..."
    cho "So I was a bit frustrated at that point and running out of options on how I could make my intentions even clear to them I lifted my skirt a bit to show them my panties."
    m "You go girl!"
    cho "Well, there's where I messed up... they took it as an invitation and squeezed my butt cheeks quite hard and painfully."
    m "Ouch, then what happened?"
    cho "Naturally I pushed their hands away... telling them if they're kind to me during the game they'll get rewarded at that point."
    cho "Not that I have any intentions to..."
    m "... obviously"
    m "And what about the butt squeeze?"
    cho "What about it, sir?"
    m "Did you like it?"
    cho "Sir! They're Slytherins!"
    m "That's not what I asked."
    cho "..."
    cho "Can I go now sir, I've done what you asked of me."
    m "Good job [cho_name], you've done a great job today getting closer to beating those pesky Slytherins."
    cho "Thank you sir..."
    m "Make sure they'll remember your meeting during the match and I'm sure any sort of desire to win will wash away."
    cho "*Hmph*..."
    cho "I'll do my best."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

# Random/Repeatable:
# Cho gets a polite kiss on her cheek by her team captain.

label cc_pr_manipulate_T2_E1:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    cho "I managed to corner their seeker when he came out of the boys bathroom. One of the only times those thugs weren't hanging around with him."
    m "Him?"
    cho "Malfoy..."
    cho "I cornered him and pushed him back into the bathroom."
    m "That's against the school rules miss Chang..."
    cho "But I thought."
    m "Then what happened..."
    cho "Oh, well... I asked him if he had ever touched a Quidditch players ass before."
    cho "And before he could answer I pushed him up onto the wall and put his hand around my waste and on my butt cheeks!"
    m "Impressive, and what was his reaction?"
    cho "At first he was mostly surprised by the circumstance but then I clenched my cheeks so he could get a good feel of what a real athlete feels like."
    cho "When that happened he went from surprised to shocked."
    cho "You should have seen it, I was actually not as repulsed as I thought I might be. It was quite thrilling actually."
    m "Why wouldn't you be, you've worked hard on your body. Now you're starting to see some of the benefits."
    cho "Yeah... yeah you're right!"
    m "And he's not going to forget it, I'm sure the snitch will be the last on his mind during the upcoming game."
    cho "You know..."
    cho "You're smarter than I gave you credit for, you've not been wrong so far..."
    m "That's why I'm the headmaster."
    cho "Will that be all?"
    m "Yes Miss Chang, good work today."
    cho "Thanks!"
    cho "Good night then."

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

label cc_pr_manipulate_T2_E2:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#e42e4e}second{/color} event in {color=#8000ff}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    $ cc_pr_manipulate.level = 2

    jump end_cho_event


### Tier 3 ###

# Intro:
# Cho meets Harry.
# Che meets Ginny. Ginny is teasing Cho actually and she's embarrassed about it.

# Random/Repeatable:
# Cho again tries to flaunt Harry. Maybe he could compliment her ass?
# Ginny watches her while doing squads.They have a little Chat. Ginny reveals that she likes Cho.
