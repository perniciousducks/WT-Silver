
### Manipulate the enemy male Quidditch players ###


### Start ###
label cc_pr_spy_boys_start:

    call cho_main(xpos="right", ypos="base", trans=fade)

    if not cc_pr_spy_boys.is_event_complete(1, 1): # Completed spying on the Weasley Twins?
        # Weasley Twins - handing over candies that turn people into blueberries

        if not cc_pr_spy_girls.is_event_complete(1, 1):
            # Player has not spied on girls just yet.

            m "Time to target the boys for a classic espionage mission C."
            call cho_main("C? Is that some sort of spy name?", "soft", "base", "base", "mid")
            m "Yep! C is the perfect spy name for you."
            call cho_main("Where do you get all these ideas from... seriously.", "annoyed", "base", "base", "mid")
            m "That's your cup-size is it not?"
            call cho_main("...", "disgust", "wide", "base", "mid") #Blushes
            call cho_main("You're such an old pervert, you know that right?", "soft", "base", "angry", "mid")
            call cho_main("And it's B cup actually...", "open", "base", "base", "downR") #Blushes and glances to the side
            g9 "Noted..."
            call cho_main("So...", "annoyed", "base", "base", "down") #pondering
            m "Yes?"

        else:
            # Player has spied on the girls

            m "Let's target the boys this time for some good ole espionage B."

        call cho_main("Where does this obsession with nicknames come from?", "open", "base", "raised", "mid")
        m "Where does it come from....?"
        call cho_main("Where does this obsession with nicknames come from... [cho_genie_name]?", "annoyed", "base", "raised", "mid")
        m "No no no... you don't get it, we use code words here..."
        m "This is a secret operation!"
        call cho_main("You want me to give you a nickname?", "annoyed", "narrow", "base", "mid")
        m "I think codename would be the appropriate term."
        m "How about..."

        menu:
            "\"Jason Porn\"":
                g9 "Explosive truth seeker."
            "\"Agent 69\"":
                g9 "Licence to frisk."
            "\"Cody Spanks\"":
                g9 "No ass left untouched!"

        call cho_main("Merlin's beard...", "angry", "narrow", "raised", "downR") # Facepalm
        g9 "Merlin's beard.... that's a pretty good codename, I like it!"
        call cho_main("But I was...", "mad", "base", "raised", "mid")
        g9 "..."
        call cho_main("Yes... Merlin's beard.", "soft", "narrow", "base", "downR")
        call cho_main("What is today's assig-...{w=0.4} mission then?", "open", "base", "base", "mid")
        m "Today's mission, if you choose to accept it..."
        m "And by choose I mean there's not really much choice in the matter."
        call cho_main("...", "normal", "narrow", "base", "mid") #rolls eyes, bit pissed off
        m "I'd like you to spy on the beaters.... those {i}Weasel{/i} twins."
        call cho_main("Weasley...", "soft", "narrow", "base", "mid")
        m "Yeah, that!"
        m "I'd like you to follow them and see what they are doing, find out if there's anything we could use against them during the match."
        call cho_main("You want me to follow them around the entire day?", "angry", "base", "base", "mid")
        m "Of course, that's what a spy does isn't it?"
        call cho_main("Yeah, it's not like I have school or anything important to do.", "upset", "base", "angry", "downR")
        g9 "Great!"
        g9 "Report back to me this evening as usual B!"
        call cho_main("Fine...", "angry", "narrow", "base", "mid")

    elif not cc_pr_spy_boys.is_event_complete(1, 2): # Completed Ron Weasley?
        # Spy on Ron Weasley

        m "Ready for some more espionage B?"
        call cho_main("Of course!", "open", "base", "base", "mid")
        call cho_main("Who are we targeting today?", "soft", "base", "raised", "mid")
        m "The keeper... Tom or whatever his name was."
        call cho_main("Ron...", "angry", "narrow", "base", "mid")
        m "Oh, yes. That guy!"
        call cho_main("And what would you have me do?", "open", "base", "raised", "mid")
        m "Spy on him of course!"
        m "See if there's anything we can use against him during the match."
        call cho_main("Fine... I'll do my best, but don't get your hopes up...", "soft", "base", "base", "downR")
        m "You'll do excellent B, now make haste!"
        m "Quietly, make haste... quietly..."
        call cho_main("As you wish...", "base", "narrow", "base", "downR")

    elif not cc_pr_spy_boys.is_event_complete(1, 3): # Completed Harry Potter?
        # Spy on Harry Potter

        m "Ready for some more espionage B?"
        call cho_main("Of course!", "open", "base", "base", "mid")
        call cho_main("Who are we targeting today?", "soft", "base", "raised", "mid")
        m "The seeker...{w=0.3} that Potter Boy."
        call cho_main("Why do you say his name with such an odd tone?", "angry", "narrow", "base", "mid")
        m "Am I? That's how Snape says it..."
        call cho_main("Right... So, what is it that you want me to do with him?", "open", "base", "raised", "downR")
        m "I'll tell you what you shouldn't do."
        m "Don't share your wine with him or he'll drink it all..."
        call cho_main("Harry drinks your wine?", "annoyed", "base", "raised", "mid")
        call cho_main("This isn't one of your weird euphemisms again is it?", "open", "narrow", "raised", "mid")
        m "I was talking about Snape."
        call cho_main("I see...", "soft", "base", "base", "mid")
        m "Anyhow..."
        m "The Potter boy!"
        m "I want you to follow him around, see what he's up to!"
        call cho_main("But what about Hermione?", "clench", "base", "base", "mid")
        m "What about her?"
        call cho_main("Harry usually hangs around her at all time, how am I supposed to spy on him if she's around?", "annoyed", "narrow", "base", "mid")
        m "I'm sure you'll figure it out..."
        call cho_main("...", "disgust", "closed", "base", "down")
        call cho_main("Fine, I'll see what I can do...", "open", "narrow", "base", "downR")
        m "That's the spirit."

    else:
        m "Let's spy on those boys some more!"
        call cho_main("Again? I've already spied on them all...", "angry", "base", "base", "mid")
        m "You can never have enough intel."
        call cho_main("Right...", "open", "narrow", "base", "R")
        m "Make sure to bring me your report as usual B."
        call cho_main("Of course.", "open", "base", "base", "mid")

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
    call cho_main("Well, in terms of not getting caught I suppose so.", "angry", "closed", "base", "down")
    m "Then spill those beans B, what did you manage to learn about them?"
    call cho_main("They're pigs. I'll tell you that much.", "annoyed", "base", "angry", "mid")
    m "Really?"
    call cho_main("Well, I guess calling them pigs is a bit uncalled for. They're a pair of pranksters that's for sure.", "open", "closed", "angry", "mid")
    call cho_main("Those two would do anything for a laugh...", "clench", "narrow", "angry", "mid")
    m "So, what did they do?"
    call cho_main("They tricked some poor Hufflepuff girls by giving them sweets that they had tampered with...", "angry", "base", "angry", "downR")
    call cho_main("All with various effects to embarrass whoever ate them...", "open", "narrow", "angry", "mid")
    call cho_main("As one girl ate one, she turned blue and began swelling until she ended up looking like a giant blueberry.", "clench", "base", "base", "mid")
    m "That's pretty funny..."
    call cho_main("How is that funny!?", "angry", "wide", "angry", "mid")
    m "What if the girl was Hermione?"
    call cho_main("I...", "angry", "base", "base", "mid")
    call cho_main("I suppose...{w=0.4} no...{w=0.4} no it's still...", "soft", "happyCl", "angry", "mid")
    m "She'd look like a blueberry with a huge wig draped on top of it."
    call cho_main("*Giggles*", "smile", "closed", "base", "mid", cheeks="blush")
    call cho_main("Anyhow... it completely ruined her clothes and as she deflated she quickly ran off stark naked and crying to her dormitory.", "annoyed", "closed", "base", "mid", cheeks="blush")
    m "Wait, so the clothes didn't expand as well?"
    call cho_main("It's not a spell... she ate it so why would her clothes be affected?", "clench", "base", "raised", "mid")
    m "Sounds like amateurish magic to me, if they just imbued those sweets with some sort of effect which allows the consumers sweat to permeate their clothes then..."
    call cho_main("...", "disgust", "wide", "angry", "mid")
    m "Oh yes...{w=0.4} very bad, I'll have a word with those two..."
    call cho_main("Please do...", "annoyed", "narrow", "angry", "mid")

    m "Anyhow, I'm sure we'll find something we can use against some of the other players."
    call cho_main("I hope so...", "upset", "base", "angry", "downR")
    m "Anything else to report?"
    call cho_main("No, that's all.", "angry", "base", "base", "mid")
    m "Then that will be it for today."
    call cho_main("Okay then.", "open", "base", "base", "R")
    call cho_main("Good night.", "soft", "base", "base", "mid")
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

    call cho_main("...", "annoyed", "base", "angry", "downR") #Annoyed
    m "Mission successful?"
    call cho_main("No, of course it wasn't...", "clench", "closed", "angry", "mid")
    call cho_main("It's as if Granger could smell me if I'm anywhere near her friend group.", "open", "narrow", "angry", "R")
    m "So, you didn't manage to glean any sort of information?"
    call cho_main("Well, I'm certain about one thing... That boy is a perv.", "upset", "narrow", "angry", "mid")
    call cho_main("Before Hermione caught me, I could tell he was checking her out any time he could.", "open", "base", "angry", "downR")
    call cho_main("It's quite sad really, you could tell from a mile off that she has no interest in him whatsoever.", "normal", "narrow", "angry", "R")
    m "Maybe he's not mature enough for his age but once his character develops then love and attraction could unexpectedly come into fruition."
    call cho_main("*Pfff* What kind of soppy romance novels have you been reading?", "soft", "closed", "angry", "mid")
    call cho_main("In any case, he come off as the clingy type... If anything ever happened between them it'd probably be out of pity on Hermione's part...", "soft", "closed", "angry", "mid")
    m "And here I thought you'd make the assumption Miss Granger is sleeping with her friends."
    call cho_main("...", "clench", "base", "base", "down") #Blushing
    call cho_main("Why would you think that?", "open", "narrow", "angry", "downR")
    m "No reason..."
    m "Anyhow... We'll find our way in at some point I'm sure."
    call cho_main("...", "annoyed", "base", "base", "downR") #Blushing
    m "Our mission continues..."
    call cho_main("Right...", "angry", "narrow", "base", "down")
    call cho_main("I'll be going then... Good night.", "open", "narrow", "base", "down")
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
    call cho_main("...", "disgust", "closed", "angry", "mid")
    call cho_main("This is such a waste of time...", "open", "base", "angry", "downR")
    m "I gather you didn't get any useful information?"
    call cho_main("No...", "annoyed", "base", "angry", "downR")
    call cho_main("I've been hiding in the boys bathroom trying to listen in on Harry and Ron.", "open", "closed", "angry", "mid")
    m "Why in the boys bathroom?"
    call cho_main("That's the only time Hermione isn't around...", "soft", "base", "angry", "downR")
    m "I see, then what were they talking about?"
    call cho_main("Ron was going on about wizard's chess.", "open", "closed", "angry", "mid")
    m "Wizard's chess?"
    call cho_main("Yes, wizard's...{w=0.4} Surely you know about wizard's chess...", "angry", "narrow", "raised", "mid")
    call cho_main("It's like regular chess except the pieces move on their own.", "soft", "narrow", "base", "mid")
    m "Sounds as dull as regular chess."
    m "Anything else?"
    call cho_main("Harry was talking a bit about quidditch but it was mostly bragging about some previous win of his.", "annoyed", "narrow", "base", "R")
    call cho_main("Honestly, that boy could learn to be a bit more humble, I don't know why Hermione hangs around with him.", "soft", "narrow", "angry", "downR")
    call cho_main("Quidditch seems to be the only thing that he has going for him...", "open", "narrow", "angry", "mid")
    m "Looks like you two have a lot in--"
    call cho_main("Those three seem to constantly have some sort of dick measuring contest in terms of who is best at something. Harry goes on about Quidditch, Ron about Chess and Hermione...", "open", "closed", "angry", "mid")
    call cho_main("Well, Hermione seems to be the best at pretty much any other subject at this school...", "annoyed", "base", "angry", "downR", cheeks="blush")
    m "I'm sure she'll be very impressed if you manage to win the quidditch cup."
    call cho_main("I don't care about her approval... I'm only doing this for me and my house...", "open", "happyCl", "angry", "mid", cheeks="blush")
    m "You tell yourself that..."
    m "Well, I'm sure we'll find a good tactic to use against them."
    call cho_main("I hope so...", "upset", "closed", "base", "mid", cheeks="blush")

    call cho_main("So, are we done here?", "angry", "base", "base", "down", cheeks="blush")
    m "Yes, that will be all."
    call cho_main("Good...", "upset", "base", "base", "R", cheeks="blush")
    call cho_main("Good night then...", "open", "base", "base", "mid", cheeks="blush")
    m "Good night Miss Chang."

    # Cho leaves.
    call cho_walk(action="leave")

    if cho_reputation < 12: # Points till 12.
        $ cho_reputation += 1

    jump end_cho_event
