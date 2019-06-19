

### Tonks Hangout Event ###

label tonks_hangout:

    call setup_fireplace_hangout(char="tonks")

    $ nt_he_drink_responses.start()

    label tonks_hangout_continue:
        with fade

    # High Priority Events First!

    # Events.
    if hermione_intro.E5_complete and not hang_with_tonks.E1_complete:
        jump hang_with_tonks_E1

    if hermione_intro.E6_complete and not tonks_requests_unlocked:
        jump hang_with_tonks_E2

    # Tonks Auror Stories.
    $ nt_he_auror_story.start()

    label end_tonks_hangout:

        call bld
        if ton_friendship < 100:
            $ renpy.play('sounds/win_04.mp3')
            show screen notes
            ">You spend the evening hanging out with Tonks.\n>Your relationship with her has improved."
            hide screen notes
        else:
            ">You spend the evening hanging out with Tonks."
        call bld("hide")

    if ton_friendship < 100: #max
        if game_difficulty < 2:      #Easy difficulty
            $ ton_friendship += 4
        elif game_difficulty == 2:   #Normal
            $ ton_friendship += 3
        else:                        #Hardcore, larger wine bonus.
            $ ton_friendship += 2

    if ton_friendship > 100:
        $ ton_friendship = 100

    if daytime:
        jump night_start
    else:
        jump day_start



label nt_he_wine_intro:
    call bld
    m "Care for a drink?"
    ton "Of course, Professor."
    ton "Hit me!"
    pause.1

    # Show wine
    call give_reward(text=">You hand over a bottle you found in the cupboard to Tonks...", gift="interface/icons/item_wine.png", sound=False)

    ton "Wine?"
    ton "Don't you have anything stronger?"
    m "Like what?"
    ton "How about \"firewhiskey\"? Got any of those?"
    m "I fear not..."
    ton "What a bummer. I guess wine will do for the day."
    m "(Maybe there is some firewhiskey stored in that cupboard somewhere...)"
    # From now on you can find firewhiskey in there too.
    # End of event.

    jump tonks_hangout_continue


label nt_he_firewhiskey_intro:
    g9 "Look what I've got!"
    pause.1

    # Show firewhiskey
    call give_reward(text=">You hand over a bottle of firewhiskey to Tonks...", gift="interface/icons/item_wine.png", sound=False)

    ton "I'm glad you brought the firewhisky out... I'm not that fond of wine."
    ton "Wine makes me giggly and lowers my sense of judgment."
    m "..."
    ton "Got a frog in your throat?"
    m "No, I was just waiting for an opening."
    ton "Sorry, I guess I talk a lot once I get going..."
    ton "Bottoms up."
    ton "*Gulp*" #Gulp sound
    ton "*Cough* *Cough*"
    ton "Yeah, that was a mistake."
    m "I don’t drink  firewhiskey that often but even I know not to down it in one..." #[smirk]
    ton "Mmm, that's the stuff."
    m "Are you even listening?"

    jump tonks_hangout_continue


label nt_he_firewhiskey_E1:
    m "Another glass of firewhisky?"
    ton "Fill er up."
    ton "..."
    ton "A little bit more..."
    ton "A bit more..."
    ton "That's it, thanks."
    if daytime:
        m "Boring lessons ahead?"
        ton "Not in particular, why?"
        m "You might regret going back to classes after drinking this much."
        ton "Oh don't you worry, Professor."
        ton "I can drink an entire bottle before it can be noticed on me."
        m "You are one glass in and it's already noticeable..."
        ton "*Hick* Oh well-... No risk, no fun!"
    else:
        m "Long day?"
        ton "Not in particular, why?"
        m "..."
        m "No reason..."

    jump tonks_hangout_continue


label nt_he_firewhiskey_E2:
    m "More firewhiskey?"
    ton "Thought you’d never ask..."

    jump tonks_hangout_continue


label nt_he_firewhiskey_E3:
    m "Want to get drunk?"
    if daytime:
        ton "I'm going to regret this, won't I?"
        ton "I hope my students won't notice."
    else:
        ton "I'd never say no to that!"

    jump tonks_hangout_continue

label nt_he_firewhiskey_E4:
    ton "Bottoms up."
    ton "*Gulp* *Gulp* *Gulp*"

    jump tonks_hangout_continue



### Events ###

label hang_with_tonks_E1:
    ton "So that Granger girl is causing you two trouble?"
    m "Quite a bit. She's not too thrilled on the idea of favour trading."
    ton "Maybe I can be of help with her?"
    ton "I can be very convincing."
    m "What are you going to do?"
    ton "Persuade her to try it herself, for a start. Convince her that trading favours isn't all bad."
    m "That would indeed be very helpful. She's stubborn in that regard."
    ton "You don't have to tell me. She's been lecturing me about those sexual favours every day since I got here."
    ton "But I can't complain. Seeing her gorgeous lips move, while those naughty words are coming out of her mouth when she's describing those filthy Slytherin girls and what they do..."
    ton "I could never get tired of that."
    m "Yes it's quite something."
    ton "I'm very glad that I've decided to join you two."
    call ton_main("As an Auror It's just constant busy work...","open","base","angry","mid")
    call ton_main("Not to mention the hours.","open","base","base","up")
    call ton_main("And the mortality rate...","open","base","worried","down")
    call ton_main("If I'd realized the benefits of being a teacher at Hogwarts, I would have signed up straight away!","open","base","angry","mid")

    ">You spend the evening by conspiring against Hermione with Tonks..."
    ">You feel a faint bond forming between you two..."

    $ hang_with_tonks.E1_complete = True

    if daytime:
        jump night_start
    else:
        jump day_start


label hang_with_tonks_E2:
    call ton_main("So what's the going rate around here then?","open","base","base","mid")
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?","base","base","base","mid")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?","horny","base","raised","mid")
    m "Again, it depends on the student."
    call ton_main("...","base","base","base","mid")
    m "But if I had to guess, I'd say about 25 points."
    call ton_main("Wait...","open","wide","wide","wide")
    call ton_main("You pay them in points?","open","base","raised","mid")
    m "Most of them."
    call ton_main("So you've managed to convince these girls to offer themselves up for a bunch of imaginary points that don't mean anything?","open","base","angry","mid")
    m "Works for the internet..."
    #Achievement Unlock (A sense of pride and accomplishment)
    call ton_main("What?","base","base","angry","mid")
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("How so?","base","base","raised","mid")
    m "Well most of them aren't going to just do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("Awww really... Can't I just cheat a bit?","open","base","worried","L")
    m "..."
    m "Just take it slow all right, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("...And what if I want a girl?","horny","base","raised","mid")
    g4 "(...!)"
    m "Whatever floats your boat."

    $ tonks_requests_unlocked = True
    call popup("You can now ask Tonks to sell \"Public Requests\" to her students!", "Congratulations!", "interface/icons/head/head_tonks_1.png")

    $ hang_with_tonks.E2_complete = True

    if daytime:
        jump night_start
    else:
        jump day_start



### Tonks Auror Stories ###

label nt_he_auror_story_intro_E1:
    ton "Thanks for accepting my job application by the way."
    m "I didn't really have that much choice in the matter."
    ton "Oh, yeah..."
    ton "..."
    ton "I'll do well, you'll see."
    ton "I was taught by one of the best aurors there is. Teaching a class of beginners should be a breeze."
    m "I never said I doubted your abilities."
    ton "..."
    ton "Anyway, I think I'm gonna go hit the sack."
    m "There's more firewhiskey where this came from so feel free to stop by any time to talk about your progress."
    ton "I'll never say no to a free drink."
    ton "And I'll keep you updated on the academics as usual."
    m "(That's not the kind of progress I meant...)"

    jump end_tonks_hangout


label nt_he_auror_story_intro_E2:
    m "You mentioned an auror last time if I'm not mistaken."
    ton "Moody?"
    m "Not in particular."
    ton "What?"
    m "..."
    ton "You talking about Madeye?"
    m "I can see perfectly fine, dear."
    ton "Madeye Moody is the auror that taught me."
    m "Oh, of course."
    m "(What's wrong with a normal name... like Will Smith, or Robin Williams?)"
    m "Yes, tell me some more about him."
    ton "Well, he's a bit of a weirdo honestly but he knows his stuff."
    ton "I guess if you're as paranoid as him you'll end up knowing everything about defence against the dark arts."
    m "Then why isn't he teaching at Hogwarts? Doesn't the school have defences and all that?"
    ton "Oh, he's old... I was more of an apprentice of his, I think he just wants to retire to be honest."
    ton "Most of the people that have anything against him are in Azkaban anyway..."
    m "Most?"
    ton "Not every bad wizard goes to Prison you know..."
    m "They don't?"
    ton "Of course not."
    ton "Did you already start drinking before I got here?"
    m "I never stop..."
    ton "..."

    jump end_tonks_hangout


label nt_he_auror_story_intro_E3:
    ton "I've been so busy lately... The days here fly by faster than a Firebolt."
    m "I'm not sure I know that spell."
    ton "It's a broom..."
    m "I see..."
    ton "I should just go to the Hogshead next time I want a drink..."
    m "Why go anywhere when you got a magic cupboard that fills itself with alcohol."
    m "At least I think that’s how it works... I'm not Jesus, I can't just turn water into wine."
    ton "Yeah, that would be impressive, I haven't found a single wizard that could create food or drinks out of  nothing."
    m "Are all of the wizards that can do that already taken?"
    ton "Single as in... no one can do it."
    m "(What kind of shit wizard can't even make food...)"
    m "What about water though, doesn't that count as a drink?"
    ton "..."
    ton "You know what, I never thought of that."
    m "What even counts as food or drink... sound pretty arbitrary to me."
    ton "I don't think we're supposed to think about it too hard."
    m "Less obvious plot holes that way I suppose..."
    ton "Less what, sorry?"
    m "No matter, just thinking out loud is all."

    jump end_tonks_hangout


label nt_he_auror_story_intro_E4:
    m "You still haven't told me anything about your time as an auror."
    ton "Well, what would you like to know?"
    m "That moody guy taught you, you said. You could start there."
    ton "Well, the job of an auror is a bit different now than how it was ten or so years ago."
    ton "I studied to become an auror with the hopes of taking down evil wizards."
    m "Sounds like a 90s B movie to me."
    ton "Tell me about it,..."
    ton "But that's not at all how the job is anymore."
    m "Was it ever?"
    ton "That's what they tell me. But right now, it's mostly droves of paperwork as they didn't keep up with any of that at the time..."
    m "Don’t you have people for that sort of thing?"
    ton "We're our own division and are supposed to follow strict guidelines set by the ministry..."
    ton "There was too much bad stuff happening for anyone to lecture the aurors though..."
    m "Then why did you stay?"
    ton "I'm here aren't I. Why do you think I jumped on the opportunity to teach here?"
    m "(You kind of created that opportunity yourself...)"
    ton "I learned a lot though, I always wanted to use that knowledge to teach others..."
    ton "I just didn't think I was going to be up for it until I was actually back in the school again."
    ton "It made me realise how much I've missed being here."

    jump end_tonks_hangout


label nt_he_auror_story_E5:
    ton "Did I ever tell you about the time we arrested a vampire?"
    m "You've not even told me about your defence against the dark arts training yet but go ahead."
    ton "Right.... well, there was this vampire guy."
    ton "We spent ages looking for him and found that he had been disguising himself as a headmaster of a muggle school."
    m "..."
    ton "It was quite disgusting what he was doing to the students actually..."
    ton "He even brought over some of the teachers... they're never going to be the same..."
    m "..."
    ton "Corrupted... forever."
    m "(Not sure if I should feel bad at this point...)"
    ton "Kind of hot though, don't you think?"
    m "(Nevermind...)"
    ton "The power vampires have over their prey."
    ton "It's a shame that they're slaves to their own urges."
    m "(Well... there's that bad feeling I felt before.)"
    ton "I get it though. Some aspects of it..."

    jump end_tonks_hangout


label nt_he_auror_story_intro_E6:
    m "Now, I'm starting to feel like you've been avoiding the subject of your auror training."
    ton "Is it that obvious?"
    m "You brought up vampires last time without even saying hello."
    ton "Vampires are interesting..."
    m "..."
    ton "Fine, I didn't want to talk about some of Moody’s teaching methods, because they were quite..."
    ton "Unconventional."
    m "What does that mean?"
    ton "Well..."
    ton "Moody very much believed in learning by doing."
    m "Sounds reasonable enough..."
    ton "This is defence against dark magic we're speaking of."
    ton "Some of the spells and situations he put me in are borderline if not completely illegal."
    m "Surely in a controlled environment where there's no harm to both parties..."
    ton "Right, I'm glad you see it that way."
    ton "In that case I'll elaborate..."
    ton "I can't believe I'm talking about this... The ministry would have Moody kicked out faster than a blastended newt going off..."

    jump end_tonks_hangout


label nt_he_auror_story_E7:
    ton "I'll tell you about this one time where Moody went a bit too far."
    m "Where did this sudden urge of sharing come from?"
    ton "Oh, I've been wanting to spill the beans about this for ages. I just didn't want to get anyone in trouble at the ministry..."
    m "What is there to say I won't get you into trouble?"
    ton "You won't..."
    ton "Would you?"
    m "No..."
    ton "Right..."
    ton "Anyway, he once brought in this werewolf that we had put in custody."
    m "He did what?!?"
    ton "See, I knew you'd react like that."
    m "No, I was just taken by surprise..."
    m "(There's fucking werewolves in this world?)"
    ton "He brought in this werewolf... apparently quite harmless comparatively."
    m "Compared to what? A dog?"
    ton "Compared to werewolves like Fenrir Greyback..."
    m "Oh yeah..."
    m "(Who?)"
    m "That..."
    m "Guy."
    ton "He had worked out a deal with this... guy."
    ton "To see how I would react in a real life situation where he would turn."
    m "Turn where?"
    ton "Into a werewolf."
    ton "Well... lets just say he hadn't taken into account that it was mating season."
    ton "The guy wasn't that interested in biting me that's for sure."
    ton "So you can see why I wasn't so keen on reporting it. More of an embarrassing situation sort of thing than anything else."
    ton "And it was totally our fault, I should’ve recognized the signs straight away... when they’re turned they’re largely driven by their instincts."
    m "I see."
    ton "Dated him for a while."
    m "You did what?"
    ton "Saturated my need for a dominant male relationship for a couple of months, that's for sure..."
    m "(That explains a few things...)"

    jump end_tonks_hangout


label nt_he_auror_story_intro_E8:
    ton "Being an auror was quite a stressful job you know."
    m "I..."
    ton "It did have it's privileges..."
    ton "The ministry was mostly concerned about the criminals making up for their crimes."
    ton "Not necessarily putting them in prison. I had quite a few... more or less successful techniques."
    m "Such as?"
    ton "Well, there was this one guy using a love potion..."
    m "A love potion, too bad they aren’t real..."
    ton "Of course they’re real, and quite effective as well."
    ton "Also... highly illegal."
    m "Oh, of course..."
    ton "Anyway..."
    ton "He could've ended up in prison at some point... but law isn't black and white like that."
    m "So you're saying that his intentions were good?"
    m "When is using a love potion ever okay?"
    ton "In this instance the woman in question was in an abusive relationship."
    ton "And the man in question knew that the boyfriend was quite jealous."
    m "I see, so he fed her the potion to get her out of it."
    ton "Right, I mean jealousy isn't that bad in a playful relationship. But it wasn't like that."
    m "How do you know that he was telling the truth?"
    ton "Truth serum."
    m "And those aren't illegal or regulated?"
    ton "I did say that I had my own techniques..."
    ton "And as I said... Law is more complicated than that, and in certain instances using a truth serum would be the right thing to do."
    ton "And to be honest, who was he going to tell... It's not like he had the moral high ground."
    m "I see, how did the situation end up?"
    ton "The girl got out of the abusive relationship and requested to have her memory adjusted."
    m "And that's..."
    ton "That's fine if the person in question is okay with it."
    ton "They have to sign a form and all that..."
    m "Obviously..."
    m "(Where do these people draw the line... making someone fall in love with you just like that?)"
    m "(...)"

    jump end_tonks_hangout


label nt_he_auror_story_intro_E9:
    m "Settled in okay?"
    ton "Yes, I finally feel like I've found some sort of daily routine."
    ton "This school brings up so many memories. I feel like every time I turn a corner I expect to see one of my fellow classmates."
    m "So, good memories?"
    ton "Mostly, it's a bit different now."
    m "In what way?"
    ton "We had to redo tasks constantly instead of actually learning new things. I think I brew the same potion a million times."
    ton "And it was tied to this weird energy system."
    m "What's that?"
    ton "The teachers wanted to restrict the amount of enjoyment and fun we had so they gave us a set amount of energy points each day."
    ton "So if you ran out of energy points during potions, for example, you couldn't finish the lesson."
    m "That doesn't make any sense."
    ton "I know right... I'm glad they got rid of it."

    jump end_tonks_hangout


label nt_he_auror_story_E10:
    m "Tell me more about your time at Hogwarts as a student."
    ton "Sure, well. As you may or may not know. I'm an metamorphmagi."
    ton "It means I can change my physical appearance at will."
    m "Sounds useful."
    ton "It can be."
    ton "Since you can't reprimand me about it I might as well tell you a bit about it."
    m "I'm still your boss."
    ton "You gonna put me in detention?"
    ton "Or spank me across your knee?"
    m "Don’t tempt me."
    ton "Anyway, there was this time where I changed my appearance into professor Snape."
    m "Why Snape?"
    ton "Well, he was the most likely not to be in the staff room. Which is where I wanted to get in."
    m "Why's that?"
    ton "Never leaves the dungeon does he? Just need to take one look of his pasty face and you'll know that...."
    ton "Don't tell him I said that..."
    m "..." #[Smirk]
    ton "So, I changed my appearance to professor Snape. And I went towards the staff room."
    m "And why were you trying to get in there? Isn't it just full of boring old teachers."
    ton "Have you used a mirror lately?"
    ton "I wasn't going there to talk to the teachers. I was trying to get a key to the prefects bathroom."
    m "Why not turn into a prefect to get into it?"
    ton "Well, that would’ve been the clever thing to do, although like everything else in this school the bathroom has a password and not a key..."
    ton "Of course I didn't know that... I had just heard rumours about the bathroom."
    m "Did you manage to get in there in the end?"
    ton "Oh yeah, easy. Once I knew about the password I just had to pretend to be one of the prefects and ask for it."

    jump end_tonks_hangout

label nt_he_auror_story_E11:
    m "Tell me more about that shape shifting ability of yours."
    ton "Well..."
    ton "Most of my escapades were kind of one trick ponies."
    m "Sounds pretty foolproof to me. How many other students could change their appearance?"
    ton "None, that's why. Process of elimination."
    m "So you got punished without any sort of proof?"
    ton "No, but they set up countermeasures after the time when..."
    ton "I shouldn't really talk about it. They never confronted me about it so fessing up now isn't going to do me any good."
    m "Not a word leaves this office."
    ton "Do you think I'm weird?"
    m "Everyone is a bit weird..."
    ton "Fine, I'll tell you."
    ton "You might have noticed but I'm a bit more comfortable with my sexuality than most people."
    m "(Oh, here we go.)"
    ton "I already told you about the whole werewolf thing and the power play fantasies with the vampire."
    m "Well, you didn't phrase it that bluntly before but I got the gist."
    ton "Well, just like many weird or odd sexual preferences they're often deeply embedded with experiences from your youth."
    ton "So for me, there was this one time where I pretended to be a teacher. As in, I literally took over their lesson when they were ill."
    m "How did you manage that. Weren't the students notified of their leave beforehand?"
    ton "No? There was just a note on their door and I ripped it off before the class got there."
    m "Seems like a flawed system..."
    ton "Yeah, some of the teachers to this day changed the way they do it because of this reason. Not the new ones though..."
    m "You didn't tell me what class this was, did you turn into snape and teach potions?"
    ton "Of course not, I wasn't going to make someone hurt themselves... and Snape would've made my life hell."
    ton "It was charms..."
    m "Right..."
    ton "I had been practicing some charms on my own and taught myself the invisibility charm on my own."
    m "Impressive..."
    ton "Thanks... Normally you wouldn't learn it until much later so you'd easily be able to dispel it."
    m "But you decided it was a good idea to teach it anyway?"
    ton "I didn't say it was a good idea."
    ton "It ended up not working anyway. Instead of the clothes making the students whole body go see through, it just made their clothes vanish!"
    ton "Whilst it wasn't intentional, the memory of it still excites me a bit."
    ton "And that's where that particular fetish came from."
    m "Hold on, there's a spell to make only the clothes invisible?"
    ton "That's what you focus on?"
    m "Well, yeah. A new spell that no one has ever heard off. And it hasn't been used since then?"
    ton "It's not a new spell... it was just novice wizards and witches not being powerful enough to cast it properly."
    ton "Similarly to splinching."
    m "(The fuck is that, sounds disgusting.)"
    ton "Anyway, the teachers played it off as an accident... though poor Flitwick had his magical abilities questioned by the students for a while."
    ton "And they tried to set up some more countermeasures towards my abilities at that point."
    ton "Not that they worked that well... I was a bit more selective of my usage though and actually thought about the consequences a bit before using it."
    m "Well, you do start thinking more about others as you get older."
    ton "Yeah well, my sexual drive started deciding more for me than before so it evened out."

    jump end_tonks_hangout
