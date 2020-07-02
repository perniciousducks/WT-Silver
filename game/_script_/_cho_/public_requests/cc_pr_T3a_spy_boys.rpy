
### Manipulate the enemy male Quidditch players ###

# TODO: Entire file needs posing

### Start ###
label cc_pr_spy_boys_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_spy_boys.is_event_complete(1, 1): # Completed spying on the Weasley Twins?
        # Weasley Twins - handing over candies that turn people into blueberries

        if not cc_pr_spy_girls.is_event_complete(1, 1):
            # Player has not spied on girls just yet.

            m "Time to target the boys for a classic espionage mission C."
            cho "C? Is that some sort of spy name?"
            m "Yep! C is the perfect spy name for you."
            cho "Where do you get all these ideas from... seriously."
            m "That's your cup-size is it not?"
            cho "..." #Blushes
            cho "You're such an old pervert, you know that right?"
            cho "And it's B cup actually..." #Blushes and glances to the side
            g9 "Noted..."
            cho "..." #pondering
            m "Yes?"

        else:
            # Player has spied on the girls

            m "Let's target the boys this time for some good ole espionage B."

        cho "Where does this obsession with nicknames come from?"
        m "Where does it come from....?"
        cho "Where does this obsession with nicknames come from... [cho_genie_name]?"
        m "No no no... you don't get it, we use code words here..."
        m "This is a secret operation!"
        cho "You want me to give you a nickname?"
        m "I think codename would be the appropriate term."
        m "How about..."

        menu:
            "\"Jason Porn\"":
                g9 "Explosive truth seeker."
            "\"Agent 69\"":
                g9 "Licence to frisk."
            "\"Cody Spanks\"":
                g9 "No ass left untouched!"

        cho "Merlin's beard..." # Facepalm
        g9 "Merlin's beard.... that's a pretty good codename, I like it!"
        cho "But I was..."
        g9 "..."
        cho "Yes... Merlin's beard."
        cho "What is today's assig-...{w=0.4} mission then?"
        m "Today's mission, if you choose to accept it..."
        m "And by choose I mean there's not really much choice in the matter."
        cho "..." #rolls eyes, bit pissed off
        m "I'd like you to spy on the beaters.... those {i}Weasel{/i} twins."
        cho "Weasley..."
        m "Yeah, that!"
        m "I'd like you to follow them and see what they are doing, find out if there's anything we could use against them during the match."
        cho "You want me to follow them around the entire day?"
        m "Of course, that's what a spy does isn't it?"
        cho "..."
        cho "Yeah it's not like I have school or anything important to do."
        g9 "Great!"
        g9 "Report back to me this evening as usual B!"
        cho "Fine..."

    elif not cc_pr_spy_boys.is_event_complete(1, 2): # Completed Ron Weasley?
        # Spy on Ron Weasley

        m "Ready for some more espionage B?"
        cho "Of course!"
        cho "Who are we targeting today?"
        m "The keeper... Tom or whatever his name was."
        cho "Ron..."
        m "Oh, yes. That guy!"
        cho "And what would you have me do?"
        m "Spy on him of course!"
        m "See if there's anything we can use against him during the match."
        cho "Fine... I'll do my best, but don't get your hopes up..."
        m "You'll do excellent B, now make haste!"
        m "Quietly, make haste... quietly..."
        cho "..."

    elif not cc_pr_spy_boys.is_event_complete(1, 3): # Completed Harry Potter?
        # Spy on Harry Potter

        m "Ready for some more espionage B?"
        cho "Of course!"
        cho "Who are we targeting today?"
        m "The seeker... that Potter Boy"
        cho "Why do you say his name with such an odd tone?"
        m "Am I? That’s how Snape says it..."
        cho "So... what do you want me to do with him?"
        m "From my experience you shouldn’t share your wine with him or he’ll drink it all..."
        cho "Harry drinks your wine?"
        cho "This isn’t one of your weird euphemisms again is it?"
        m "I was talking about Snape."
        cho "I see..."
        m "Anyhow..."
        m "The Potter boy!"
        m "I want you to follow him around, see what he’s up to!"
        cho "But what about Hermione?"
        m "What about her?"
        cho "Harry usually hangs around her at all time, how am I supposed to spy on him if she’s around?"
        m "I’m sure you’ll figure it out..."
        cho "..."
        cho "Fine, I’ll see what I can do..."
        m "That’s the spirit."

    else:
        m "Let's spy on those boys some more!"
        call cho_main("Again? I've already spied on them all...", "soft", "base", "raised", "mid")
        m "You can never have enough intel."
        cho "Okay then..."
        m "Make sure to bring me your report as usual B."
        call cho_main("Of course.", "base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cc_pr_spy_boys.inProgress = True

    jump end_cho_event



### Return Events ###


### Tier 3 (pre Gryffindor) ###

label cc_pr_spy_boys_T3_twins:
    ## Weasley Twins - Blueberry candies ##

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    m "Mission successful?"
    cho "Well, in terms of not getting caught I suppose so."
    m "Then spill those beans B, what did you manage to learn about them?"
    cho "Well, they're pigs. I'll tell you that much."
    m "Really?"
    cho "Well, I guess calling them pigs is a bit uncalled for. They're a pair of pranksters that's for sure."
    cho "They'll do anything for a laugh...."
    m "Such as?"
    cho "They tricked some poor girls by handing out these weird sweets to them."
    cho "They all had different effects with the purpose to embarrass the consumer."
    cho "When one girl ate it and she turned blue and began swelling at a rapid pace, ending up looking like a giant blueberry."
    m "That's pretty funny..."
    cho "No it's not, why would anyone do that to someone..."
    m "What if the girl was Hermione?"
    cho "I..."
    cho "I suppose...{w=0.4} no...{w=0.4} no it's still..."
    m "She'd look like a blueberry with a huge wig draped on top of it."
    cho "*Giggles*"
    cho "Anyhow... it completely ruined her clothes and as she deflated she quickly ran off stark naked and crying to her dormitory."
    m "Wait, so the clothes didn't expand as well?"
    cho "It's not a spell... she ate it so why would her clothes be affected?"
    m "Sounds like amateurish magic to me, if they just imbued those sweets with some sort of effect which allows the consumers sweat to permeate their clothes then..."
    cho "..."
    m "Oh yes...{w=0.4} very bad, I'll have a word with those two..."
    cho "Please do..."

    m "Anyhow, I'm sure we'll find something we can use against some of the other players."
    cho "I hope so..."
    m "Anything else to report?"
    cho "No, that's all."
    m "Then that will be it for today."
    cho "Okay then."
    cho "Good night."
    m "Good night miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points till 12.
        $ cho_reputation += 1

    jump end_cho_event

label cc_pr_spy_boys_T3_ron:
    ## Ron Weasley ##

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    cho "..." #Annoyed
    m "Mission successful?"
    cho "No, of course it wasn't..."
    cho "Granger seems to be able to smell me if I get anywhere near her friend group."
    m "So you didn't manage to glean any sort of information?"
    cho "Well, one thing's for sure. That boy is a perv..."
    cho "Even before I was caught I could tell he was checking Hermione out any time he could."
    cho "It's quite sad really, you could tell from a mile off that she has no interest in him whatsoever."
    m "Maybe he's not mature enough for his age but once his character develops then love and attraction could unexpectedly come into fruition."
    cho "*Pfff* What kind of soppy romance novels have you been reading?"
    cho "In any case, he come off as the clingy type... If anything ever happened between them it'd probably be out of pity on Hermione's part..."
    m "And here I thought you'd make the assumption Miss Granger is sleeping with her friends."
    cho "..." #Blushing
    cho "Why would you think that?"
    m "No reason..."
    m "Well then, we'll find our way in at some point I'm sure."
    cho "..." #Blushing
    m "Our mission continues..."
    cho "Right..."
    cho "I'll be going then... Good night."
    m "Good night Miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points till 12.
        $ cho_reputation += 1

    jump end_cho_event

## Harry Potter ##
label cc_pr_spy_boys_T3_harry:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    call cho_main("", "annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)

    m "B, you return..."
    m "Was your mission successful?"
    cho "..."
    cho "This is such a waste of time..."
    m "I gather you didn’t get any useful information?"
    cho "No..."
    cho "I’ve been hiding in the boys bathroom trying to listen in on Harry and Ron."
    m "Why in the boys bathroom?"
    cho "That’s the only time Hermione isn’t around..."
    m "I see, then what were they talking about?"
    cho "Ron was going on about wizard’s chess."
    m "Wizard’s chess?"
    cho "Yes, wizard’s...{w=0.4}Surely you know about wizard’s chess..."
    cho "It’s like regular chess except the pieces move on their own."
    m "Sounds as dull as regular chess."
    m "Anything else?"
    cho "Harry was talking a bit about quidditch but it was mostly bragging about some previous win of his."
    cho "Honestly, that boy could learn to be a bit more humble, I don’t know why Hermione hangs around with him. Quidditch seems to be the only thing that he has going for him."
    m "Looks like you two have a lot in-"
    cho "Those three seem to constantly have some sort of dick measuring contest in terms of who is best at something. Harry goes on about Quidditch, Ron about Chess and Hermione..."
    cho "Well, Hermione seems to be the best at pretty much any other subject at this school..."
    m "I’m sure she’ll be very impressed if you manage to win the quidditch cup."
    cho "I don’t care about her approval... I’m only doing this for me and my house..."
    m "You tell yourself that..."
    m "Well, I’m sure we’ll find a good tactic against them eventually. There’s plenty of other members on their team we can focus on."
    cho "I hope so..."

    cho "So, are we done here?"
    m "Yes, that will be all."
    cho "Good..."
    cho "Good night then..."
    m "Good night Miss Chang"

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points till 12.
        $ cho_reputation += 1

    jump end_cho_event
