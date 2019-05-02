

### Manipulate the enemy Quidditch players ###

# Start
label cc_pr_manipulate_start: # Complete. Not posed.

    # Intro
    if cc_pr_manipulate_OBJ.points == 0:
        m "So what do we know about our opponents?"
        cho "Hufflepuff? Well their team isn't the best, but they have a really strong seeker."
        m "Right...{w} who was that again?"
        cho "Cedric Diggory. How often do I have to repeat myself, [cho_genie_name]?"
        m "You will know, once you get to be my age..."
        g4 "(Because then you stop giving a damn...)"
        cho "I'm so sorry Sir!{w} I'll be more respectful of your age from now on!"
        cho "Well Cedric is a bit of a block head, but he's quite a competent seeker."
        cho "And very popular with the girls..."
        m "Do I sense a little bit of something in your voice?"
        cho "Of course not! We stopped dating ages ago!"
        cho "I didn't want to be seen with an idiot like him anymore, not if I'm supposed to be a proper Ravenclaw..."
        cho "Even if he is cute..." # Small text.
        m "That's good. We can use this to our advantage."
        cho "We can? How?"
        m "You two having history! Which means he'll be much easier to dristract during the game."
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

    call cho_walk(action="leave", speed=1.6)

    $ cc_pr_manipulate_OBJ.inProgress = True

    $ cc_pr_manipulate_OBJ.points += 1

    jump end_cho_event



# Ideas

### Tier 1 ###

# Intro:
# Cedric tried to kiss her.

label cc_pr_manipulate_T1_intro:
    $ cc_pr_manipulate_OBJ.level = 1

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
    m "(♫Now I'm falling asleep♫)"
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
    cho "He sort of crossed my path when I on my way to Cedric, down the hallway..."
    cho "He came out of nowhere!"
    cho "And he stood so close, he could see right down my cleavage!"
    g4 "What a lucky git!"
    cho "I couldn't move a single muscle! It was like I was frozen in place!"
    cho "What if something like that will happen during the game?!"
    m "You are right. That could be an issue..."
    cho "And the worst thing is, he just kept stairing!"
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
    m "Well? How did it go?"
    cho "Very well, Sir!"
    g9 "Yeah? Tell me about it!"
    cho "I ran into Cedric on my way to library... Literally!"
    cho "I bumped into him and hit my head pretty hard..."
    m "You poor thing."
    cho "It's nothing. I'm used to pain by now."
    g4 "*gulp!*"
    cho "After all those years of playing Quidditch, I've grown pretty resistent to it..."
    m "A usefull skill to have I suppose..."
    cho "Anyways, Cedric helped me back up on my feet, but before he could even say how sorry he was, I kissed him!"
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

    jump end_cho_event



### Tier 2 ###

# Intro:


label cc_pr_manipulate_T2_intro:
    $ cc_pr_manipulate_OBJ.level = 2

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the intro {color=#80ff00}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

# Random/Repeatable:
# Cho gets a polite kiss on her cheek by her team captain.

label cc_pr_manipulate_T2_E1:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#ffae19}first{/color} event in {color=#8000ff}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

label cc_pr_manipulate_T2_E2:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#e42e4e}second{/color} event in {color=#8000ff}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event


### Tier 3 ###

# Intro:
# Cho meets Harry.
# Che meets Ginny. Ginny is teasing Cho actually and she's embarrassed about it.

# Random/Repeatable:
# Cho again tries to flaunt Harry. Maybe he could compliment her ass?
# Ginny watches her while doing squads.They have a little Chat. Ginny reveals that she likes Cho.
