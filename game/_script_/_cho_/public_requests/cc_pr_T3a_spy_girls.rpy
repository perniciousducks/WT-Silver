

### Manipulate the enemy female Quidditch players ###

### Start ###
label cc_pr_spy_girls_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_spy_girls.is_event_complete(1, 1): # Completed shower event?
        # Shower event - looking through the glory hole

        if True or cc_pr_spy_boys.is_event_complete(1, 1): # TODO: Remove `True` when `cc_pr_spy_boys` object exists.
            # Player has not spied on boys just yet.

            m "Time for some good old espionage!"
            cho "Finally, a plan that makes sense!"
            m "You say that like my plans haven't worked thus far..."
            m "For this mission I'd like you to spy on the girls of the Gryffindor team. When they're alone..."
            cho "When they're alone? I can't get into their common room... you should know that."
            m "And as you should know, there's plenty of other places where girls hang out and gossip."
            cho "..." #Blushes
            m "That's right, the women's changing room!"
            cho "Fine... I'll see what I can do."
            m "Excellent, report back to me as usual C."
            cho "C? Is that some sort of spy name?"
            m "Yep! C is the perfect spy name for you."
            cho "Where do you get all these ideas from... seriously."
            m "That’s your cup-size is it not?"
            cho "..." #Blushes
            cho "You're such an old pervert, you know that right?"
            cho "And it's B cup actually..." #Blushes and glances to the side
            g9 "Noted..."
        else:
            # Player has spied on the boys

            m "Time for some more espionage, and this time we’ll be targeting the girls!"
            cho "Okay then, so you want me to spy on anyone in particular?"
            m "Why one of them when you could do all at once?"
            cho "All at once? "
            m "That’s what I said!"
            m "Their changing room should be a good place to start."
            cho "Sir!"
            g9 "I know! I surprise myself with how good my plans are sometimes..."
            cho "..."
            cho "Okay then then, I’ll see what I can do..."
            g9 "Excellent."

        g9 "Now, to the gadgets... I’ve got this great new invention... It's a vibrating magical rod..."
        cho "A what?!"
        cho "Wouldn’t something like an extendable ear make more sense for eavesdropping?"
        m "Not unless it vibrates..."
        m "Anyway, you’d better get a move on..."
        m "I expect your report this evening B!"
        m "Good luck!"
        cho "Thanks..."

    elif not cc_pr_spy_girls.is_event_complete(1, 2): # Completed Alicia Spinnet?
        # Spy on Alicia Spinnet

        m "Ready for some more espionage B?"
        cho "Of course!"
        cho "Who’s the target?"
        m "Alicia Spinnet!"
        m "I suggest you try and spy on her when she’s not with the other two."
        cho "Why’s that?"
        m "It’s the best way to get to know a person for real, maybe she’s putting up a front with her friends."
        cho "Okay then..."
        m "Off you go!"
        m "Enj... I mean, good luck!"
        cho "Thanks..."

    elif not cc_pr_spy_girls.is_event_complete(1, 3): # Completed Katie Bell?
        # Spy on Katie Bell

        m "Ready for some more espionage B?"
        cho "Of course!"
        cho "Who are we targeting today?"
        m "Katie Bell!"
        cho "Okay then."
        m "Off you go."
        call cho_walk("door", "base")
        g4 "Oh, wait... I forgot about the gadgets!"
        call cho_walk(action="leave")
        m "(Damn, she must’ve not heard me...)"

        # End early, cho already left!
        $ cc_pr_spy_girls.inProgress = True

        jump end_cho_event

    elif not cc_pr_spy_girls.is_event_complete(1, 4): # Completed Angelina Johnson?
        # Spy on Angelina Johnson

        m "Ready for some more espionage B?"
        cho "Of course!"
        cho "Who are we targeting today?"
        m "Angelina Johnson!"
        cho "Their team captain?"
        m "Yes, and I can’t stress enough that today's performance is of the utmost importance."
        cho "Of course... So what-"
        m "Utmost!"
        cho "I unders-"
        m "Importance!"
        cho "..."
        m "So are you ready B?"
        cho "I am rea-"
        m "Don’t get spotted!"
        call cho_walk(action="leave")
        m "(Did she just...)"
        m "(Well, that’s just rude.)"

        # End early, cho already left!
        $ cc_pr_spy_girls.inProgress = True

        jump end_cho_event

    else:
        m "Let’s spy on those girls some more!"
        cho "Again? I’ve already spied on them all..."
        m "You can never get enough intel."
        cho "Okay then..."
        m "Make sure to bring me your report as usual B."
        cho "Of course."

    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_spy_girls.inProgress = True

    jump end_cho_event

### Return Events ###

### Tier 3 (pre Gryffindor) ###

label cc_pr_spy_girls_T3_showers_intro:
    # Showers - looking through the glory hole

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Welcome back, what's the report B?"
    cho "..." #Blushing looking away
    m "Did you get any juicy info that we could use against the Gryffindor girls?"
    cho "No juicy info per say..."
    m "Then how'd it go, anything you could tell me?"
    cho "Well, I went to spy on them in the showers as you asked me..."
    cho "I found a hole in one of the walls actually..."
    m "That's unfortunate, I'll have to look into filling that hole at some point..."
    m "So what were they talking about if it wasn’t Quidditch?"
    cho "There wasn’t much talking at all as they were too preoccupied with kissing and touching each other."
    g9 "I knew it!"
    cho "..." #annoyed
    g9 "Makes you wish you had those girls on your own team doesn't it?"
    cho "Yeah right..." #annoyed glancing to the right #blush
    m "What else did they do?"
    cho "Not a lot to be honest... I wasn't going to stay until they were done..."
    m "Why not? What's the worst that could happen? They’d catch you and ask for you to join in?"
    cho "*Pfff* Surely they'd never let one of their opponents in on anything they were doing."
    m "So you thought about it?"
    cho "I didn't say that..."
    cho "Anyhow..."
    cho "I had no idea they were so lewd..."
    cho "I'm worried that there's little I could do in terms of clothing that would distract them..."
    cho "Seeing how they were crawling over each other's naked bodies..."
    m "..."
    m "You should’ve stayed for longer miss Chang, perhaps you could’ve learned a thing or two."
    m "Anyway..."
    m "I’ll think of something... For now we'll just try some different clothing to see if anything works."
    cho "Okay..."
    cho "Good... Good night then."
    m "Good night miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_spy_girls_T3_alicia_intro:
    # Alicia Spinnet

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    #Cho returns blushing with a vacant expression on her face
    m "Ready for you report B... what’s the {i}sitch{/i}?"
    cho "The \"sitch\" sir?"
    m "What’s the situation."
    m "Did you manage to spy on miss Spinnet when she was alone?"
    cho "I did..."
    m "Great, tell me what happened."
    cho "That girl sure is something..."
    cho "She’s been assisting the twins by drawing in more customers to their shop."
    m "How kind."
    cho "I woulnd't call it that... Only reason she's assisting them is because they promised they'd behave during Quidditch."

    # Has player sent Hermione to work with the Twins, promoting the cardgame?
    if not first_time_cardgame_work:
        m "(I thought Hermione was helping them with that already...)"


    cho "And she sure doesn’t seem to have any problems enticing people."
    m "So, how does she do it?"
    cho "Well... If I didn’t know better I’d say she must be using some kind of hypnosis."
    m "Hypnosis? Now that sounds completely absurd."

    # Has player started imperius curse training?
    if ag_st_imperio.points > 0:
        m  "She’s not using that im-perv-ius curse is she?"
        cho "Imperius?"
        cho "No... I haven't seen her with a wand in hand..."
    else:
        cho "That's why I said, if I didn't know any better..."

    cho "I saw her whisper something into another student's ear and as if on command they immediately followed her into the girls toilets."
    m "Nice, a girl that takes what she wants..."
    m "So, what was she doing with them?"
    cho "Come on [cho_genie_name], surely you’re able to guess what she’s doing."
    g9 "I have no idea, that’s why you’re here...{w=0.4} to tell me..."
    cho "She’s doing lewd stuff with them obviously..."
    m "Such as?"
    cho "So predicatble...{w=0.4} Well, since I knew you’d ask... I did sneak in after her but I was only able to see part of her under the stall..."
    cho "She was on her knees and whoever was in there with her wasn’t being quiet that’s for sure."
    m "I should get her number."
    cho "Her what?"
    m "Nevermind... {w=0.4} So is that all you saw?"
    cho "*Uhm* As I said, I could only see her bottom from underneath that stall...{w=0.4} so yes..." #Blushing
    m "Your face says otherwise, is that really everything you saw?"
    cho "When I say bottom... She wasn’t wearing any panties [cho_genie_name]..."#Blushing
    cho "She was also..."#Blushing
    cho "She was also really wet down there..."#Blushing
    g9 "There it is..."
    cho "I just thought I’d tell you since she was making a huge mess on the floor!"
    m "Of course, thanks for letting me know."
    m "You’ve done a great job today B."
    m "Although I still think my gadgets... especially the magic rod would’ve been a great help for this mission."
    cho "..." #Blushing
    m "I could let you borrow it to figure out how it works. It’s very useful you know."
    cho "I’m good, thanks. I think I’ll just head straight to bed if you don’t mind."
    #Cho Heads to the door and stops TODO
    m "Changed your mind?"
    cho "N-...no, Good night!"

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_spy_girls_T3_katie_intro:
    # Katie Bell

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Mission successful?"
    m "What did you learn about Katie Bell?"
    cho "She’s a freak!" # angry
    m "Whoa, that’s a bit uncalled for don’t you think?"
    m "I’m sure she looks perfectly fine."
    cho "No, not her looks... what she’s been doing." # blush
    cho "I followed her all the way down to the lake today. And then hid behind a tree to observe her."
    m "Something wrong with a little swim?"
    cho "No, but... she went in there butt-naked!"
    g9 "Butt-naked? Did they open up a nude-beach without telling me?"
    cho "What? Of course they haven’t!"
    m "Shame..."
    cho "Once she had taken her clothes off she slowly walked into the water, and then just vanished beneath the surface..."
    m "That’s...{w=0.4} odd...{w=0.4} Perhaps she is a mermaid?"
    cho "I highly doubt that, seeing that she has legs..."
    cho "Although for a moment I did consider that the mermaids living there might have used their songs to charm her..."
    m "Well that's not concerning at all..."
    cho "She did resurface a couple of moments later... just as I began to worry..."
    cho "Although... not the way I expected."
    cho "After a huge splash I realised she had been lifted into the air by some giant tentacles!"
    g4 "Whoa, tentacles!"
    cho "Yes, gross slimy and green tentacles... It was if the seaweed had come to life!"
    m "So, what was it doing to her?"
    cho "*Ugh* Do I really have to tell you..."
    g9 "With as much detail as possible thank you."
    cho "Fine..."
    cho "They were holding her body stationary in the air, whilst more of its tentacles were working their way around, squeezing her breasts."
    g4 "Classic tentacle move!"
    cho "As it... {w=0.5} continued...{w=0.4} the tentacles grabbed her around the waist and began moving her body up and down, with another one wrapping itself around her legs."
    cho "She almost looked like a doll being puppeted around by those giant arms..."
    m "And she was letting it do this willingly?"
    cho "Yes, she seemed to thoroughly enjoy being its...{w=0.6} toy to play with."
    cho "And As the tentacles slid across her skin I could see her eyes roll back into her head."
    cho "As they did, another tentacle slipped through in between her legs from behind."
    cho "Which was enough to bring her over the edge I think."
    m "Impressive..."
    m "Now that’s quite a story, you’re not making this up are you?"
    cho "I wish..."
    g9 "Sounds to me like a mission accomplished!"
    cho "Mission... what?"
    m "I’m sure you’ve just learned more about her than even her closest friends."
    m "She’s a pervert who likes it rough, and enjoys being treated like an object."
    cho "If you say so, [cho_genie_name]..."
    g9 "And you definitely know not to entice her with any sort of seaweed."
    cho "..."
    cho "Can I go now?"
    m "Yes, you may leave... good job today [cho_name]."
    cho "Thanks..."
    cho "Good Night."
    m "Until next time."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_spy_girls_T3_angelina:

    # Since this is the last event in Tier 3, it will handle repeatables.
    if cc_pr_spy_girls.is_complete():
        $ renpy.jump(renpy.random.choice(("cc_pr_spy_girls_T3_repeat1", "cc_pr_spy_girls_T3_repeat2", "cc_pr_spy_girls_T3_repeat3")))

    # Angelina Johnson

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    g9 "Ready for your report B... lay on me!"
    cho "Don’t you mean lay \"it\" on me, [cho_genie_name]?"
    m "I’m pretty sure I’m right..."
    m "But before that, tell me how everything went with Miss Johnson!"
    cho "Well enough, I'd say..."
    cho "I stayed behind after practice, to see if I could follow her once they were done changing their clothes."
    cho "To my surprise, she didn't head back to the castle like the others, but went to the referee's office instead..."
    m "The Referee?"
    cho "Madam Hooch’s office, Sir."
    cho "I managed to eavesdrop on their conversation, although I only caught the tail end of their conversation..."
    cho "I suspect madame Hooch might know what they’ve been doing in the showers after the game..."
    cho "Angelina was talking about how she couldn’t believe that she and her friends were being spied on like that."
    cho "Madam Hooch just laughed it off and told her she should take it as a compliment."
    m "Good to know my staff knows how to diffuse a situation..."
    cho "Angelina sure didn’t see it that way as she then stormed out her office..."
    m "You sure she wasn’t talking about-"
    cho "Sir... If Madame Hooch is spying on them, then Angelina might get the idea to entice her into helping them during the finals!"
    m "Hmm... Not a bad idea now that I think about it. We should try that as well..."
    cho "[cho_genie_name]! I don’t want to win by cheating!"
    m "Yes, cause distracting hardly counts as cheating..."
    cho "Well of course it's not! It's within the rules!"
    m "..."
    cho "We need to do something about it before Angelina tries to take advantage of the situation..."
    m "I’ll... figure something out..."
    cho "You'd better!" #Angry
    cho "So... are we done here?" #smiles and focuses on genie
    g9 "Yes, mission successful, [cho_name]!"
    g9 "We’ll have that girl wrapped around our...{w=0.4} your finger soon enough..."
    cho "Good night, [cho_genie_name]."

    #cho leaves
    call cho_walk(action="leave")
    g9 "(Wrapped around your finger...{w} good one...)"

    if cho_reputation < 12: # Points til 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_spy_girls_T3_repeat1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you catch them doing anything interesting?"

    cho "I suppose... {w=0.5} I went to spy on them in the showers again."
    m "Go on..."
    cho "Angelina was slapping Katie on the butt with one of the beaters bats."
    cho "Her butt was bright red... I have no clue how she can even sit on a broom at this point..."
    cho "She must have some really potent cushioning charm on that thing..."
    m "That girl sure loves a spanking..."
    cho "Yes... and Angelina seems to thoroughly enjoy giving her one as well."
    m "Well then, anything else to report?"

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

label cc_pr_spy_girls_T3_repeat2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you catch them doing anything interesting?"
    cho "I was keeping an eye on Katie during Defence against the dark arts and caught her flashing her breasts towards another student."
    cho "I was quite shocked she’d dare do something like that in class to be honest."
    cho "I wasn’t going to say anything obviously but it would’ve been funny to see her get chastised by professor Tonks."
    m "(Yeah, as if that would ever happen...)"
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

label cc_pr_spy_girls_T3_repeat3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main(face="happy", xpos="mid", ypos="base", trans=fade)

    m "Ready for your report B..."
    m "Did you catch them doing anything interesting?"
    cho "Angelina pulled Katies panties down during practice to expose her red butt cheeks to the boys."
    cho "I heard her yelling at them to do better or she’d make their butts look like Katies."
    m "Such a bully..."
    cho "Yeah, Angelina is just looking to get a reaction from the boys..."
    cho "And Katie didn’t seem to mind the attention, that’s for sure..."
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
