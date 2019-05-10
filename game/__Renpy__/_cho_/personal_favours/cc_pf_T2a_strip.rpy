

# Favour tier 2 - Inspect her Body

label cc_pf_strip:

    # Tier 1
    if main_matches_won <= 1:

        if cc_pf_strip_OBJ.level == 0:   # 0 Hearts.
            # Cho strips to her underwear.
            call cc_pf_strip_T1_E1

        elif cc_pf_strip_OBJ.level == 1: # 1 Heart.
            # Cho strips naked.
            call cc_pf_strip_T1_E2

        elif cc_pf_strip_OBJ.level == 2: # 2 Hearts.
            # Cho wants you to summon Hermione.
            # Event fails when Hermione hasn't stripped for you yet.
            # Succeeds after Hermione's second dance favour.
            jump cc_pf_strip_T1_E3

        else:                            # 3+ Hearts.
            # Cho wants you to summon Hermione again.
            # Repeat of event 3 with different intro.
            jump cc_pf_strip_T1_E4


    # End event jump
    # (only used when the event isn't called.)
    label end_cho_strip_event:

        if cho_whoring < 8: # Points til 8
            $ cho_whoring += 1

        if cc_pf_strip_OBJ.level < 4:
            $ cc_pf_strip_OBJ.level += 1

    # Stats
    $ cc_pf_strip_OBJ.points += 1

    jump end_cho_event



### Tier 1 ###

label cc_pf_strip_T1_E1:
    m "It's time for your next favour, [cho_name]."
    call cho_main("I- *uhm*...{w} I think I'm ready.","horny","base","sad","downR")
    call cho_main("What would you like me to do, [cho_genie_name]?","soft","base","sad","mid")
    m "First, come a bit closed..."
    call cho_main("Very well, Sir.","base","base","base","mid")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main(xpos="mid", ypos="base", trans="fade")
    call ctc

    m "How often do you typically exercise, Miss Chang?"
    call cho_main("As often as I can, [cho_genie_name]!","soft","base","base","mid")
    m "Which is... how often? Twice a week?"
    call cho_main("Three times a day, Sir!","base","narrow","base","mid")
    with hpunch
    g4 "What?!"
    m "(I don't even jerk off that often!)"
    m "You are clearly exaggerating..."
    call cho_main("I'm not, Sir! It's necessary for somebody in my position!","open","closed","angry","mid")
    call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","open","narrow","angry","mid")
    call cho_main("My body's at the absolute peak of human condition!","open","narrow","angry","R")
    g4 "It is quite impressive, I've got to say!"
    call cho_main("Glad to hear it, [cho_genie_name].","base","closed","base","mid")
    m "I assume you get complimented often?"
    call cho_main("Occasionally...","soft","base","base","R")
    g9 "And I suspect you have many admirers?"
    call cho_main("A couple, maybe...","quiver","base","sad","down")
    call cho_main("But that's \"not\" why I take such great care of my body, Sir!","open","narrow","angry","mid")
    m "Of course not..."
    call cho_main("I simply have to be at the top of the game! Stay competitive, as best as I can!","open","closed","base","mid")
    m "That's very commendable of you..."
    call cho_main("Thank you, Sir.","base","base","base","mid")

    # Ask her to strip.
    g9 "Why don't you show me what you are made of?{w} Let me have a proper look at you!"
    call cho_main("Sir?","soft","wink","raised","mid")
    m "I need you to remove your clothes."
    call cho_main("!!!","soft","wide","base","mid")
    m "Go on, girl. Start with the top..."
    call cho_main("No!","scream","closed","angry","mid", trans="hpunch")
    call cho_main("Why are you even asking me to do such a thing?!","angry","narrow","angry","mid")
    m "Have you already forgotten that I help you?"
    call cho_main("And I'm very thankful for that, Sir, but...","open","closed","base","mid")
    m "Am I not your trusted mentor?"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    m "Your strong advisor..."
    g9 "Your guardian angel!"
    call cho_main("I don't think taking off my clothes will be necessary for our training, [cho_genie_name].","annoyed","narrow","angry","R")
    m "I'm very disappointed I've got to say..."
    m "You aren't this shy with undressing in front of your team, are you?"
    call cho_main("Sir, that's entirely different!","angry","closed","sad","mid")
    m "How so?"
    call cho_main("I'm just not comfortable doing this in front of you, Sir!","quiver","closed","sad","mid")
    call cho_main("You're really old...","soft","narrow","sad","downR")
    m "Pardon me?"
    call cho_main("I meant... you're our headmaster! It just feels wrong to me!","soft","narrow","sad","mid")
    m "Are you one of those shy girls, Miss Chang?"
    call cho_main("No, Sir. I wouldn't say I'm shy, but...","soft","narrow","sad","downR")
    m "Well then prove me you aren't, girl!"
    g9 "Let me see it!"

    # Cho stays reluctant.
    call cho_main("Is there no other way I could repay the favor?","annoyed","narrow","sad","mid")
    m "Well yes- Several.{w} But we'll get to those later..."
    call cho_main("Later, Sir?","soft","base","raised","mid")
    g4 "Girl, I wouldn't be asking you this if it wasn't absolutely necessary for your training!"
    call cho_main("Of course, [cho_genie_name].","annoyed","base","sad","down")
    m "All that's required of you is to cooperate..."
    call cho_main("(...)","annoyed","base","sad","mid")
    m "Now take of your top..."
    call cho_main("(...)","annoyed","narrow","angry","mid")
    call cho_main("Only my top?","soft","narrow","sad","mid")
    g9 "Would you like to take off \"more\"?"
    call cho_main("I didn't mean it like that!","angry","narrow","angry","mid")
    m "[cho_name], it's only the two of us in here. No need to worry."
    call cho_main("I'm not worried about others, [cho_genie_name]!","annoyed","narrow","angry","mid")
    call cho_main("For as long as nobody else will find out...{w} You have to promise me that, Sir!","soft","narrow","angry","R")
    g9 "Promised! Now take it off!"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    m "*He-hem*{w} Slowly..."
    pause.5
    call cho_main("","quiver","closed","sad","mid")
    pause.8

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","quiver","narrow","sad","mid")
    call ctc

    g4 "Magnificent."
    g4 "Simply...{w} magnificent..."
    call cho_main("Thank you, Sir.","soft","narrow","sad","R")

    menu:
        "\"Your posture is remarkable!\"":
            call cho_main("I'm glad you noticed!","base","base","sad","mid") # Happy
            call cho_main("I'm relieved you actually show interest in my body status, Sir!","smile","base","base","mid")
            m "(Oh- You have no idea, girl!)"
            call cho_main("I thought you just wanted to gush at my body like all the other teachers...","soft","narrow","sad","mid")
            m "Who?{w} Which other teachers are you talking about?{w} Snape?!"
            call cho_main("No, not Snape...","annoyed","narrow","angry","R")
            call cho_main("(...)","annoyed","base","sad","downR")
            call cho_main("Promise me you won't tell her!","quiver","narrow","sad","mid")
            m "Her?!"
            call cho_main("Madame Hooch, Sir.","soft","narrow","sad","mid")
            m "Ah, the old, gray haired lady..."
            call cho_main("Yes, she's been eying me a lot lately...","quiver","base","sad","downR")
            call cho_main("Even more so after our recent game against Hufflepuff. I wonder why...","horny","narrow","sad","R")
            g9 "I can't blame her... Your body is very pleasing to look at!"
            call cho_main("Thank you, Sir.","base","base","base","mid")

        "\"You have marvelous abs!\"":
            call cho_main("*Uhmm*...","quiver","narrow","sad","R") # Embarrassed
            g4 "As if Michelangelo himself carved them onto your flesh..."
            m "I must say I'm very impressed!"
            call cho_main("Thank you, Sir.","soft","narrow","sad","downR")

    m "Not every girl I get to see here has such fine...{w} contours..."
    call cho_main("Other girls?","soft","wide","base","mid")
    call cho_main("Sir, you aren't training anybody else in Quidditch besides me, are you?","soft","narrow","angry","mid")
    m "What? Of course not..."
    call cho_main("Then which other girls are you talking about?","annoyed","narrow","angry","mid")
    g4 "(Shit! I better just tell her the truth.)"
    m "Just...{w} Granger..."
    call cho_main("*Phewww*{w} You scared me there for a second, Sir...","smile","narrow","sad","mid")
    m "You... don't mind about it?"
    call cho_main("Please. Why should I care what Granger does for you in here?","soft","narrow","angry","R")
    call cho_main("I suspected she was one of those girls buying favours from her teachers!","soft","closed","angry","mid")
    call cho_main("With how many points she's earned for her house lately,... to win the house cup...","open","narrow","angry","R")
    call cho_main("But as long as you don't help any \"Gryffindor\" or \"Slytherins\" sluts win the Quidditch cup, everything will be fine.","base","narrow","base","mid")
    m "That's a relief..."

    call cho_main("Besides, she clearly doesn't hold a candle against me!","open","narrow","base","R")
    call cho_main("All she does is sit on her arse all day, studying in the library...","soft","narrow","angry","mid")
    m "(...)"
    call cho_main("You can't expect somebody who's as lazy as her to look as great as I do!","soft","closed","base","mid")

    menu:
        "\"Yeah, she's gross.\"":
            m  "Miss Granger's body is nothing compared to yours."
            call cho_main("I wholeheartedly agree, Sir!","base","narrow","angry","mid")
            m  "Her tits sag too much, and her fat hips are disgusting..."
            call blktone
            g4 "(Something deep inside me just died saying this...)"
            call hide_blktone
            call cho_main("She really is a...","open","closed","raised","mid")
            call cho_main("... stupid...","angry","closed","angry","mid")
            call cho_main("... fat...","angry","narrow","angry","mid")
            call cho_main("... cow, isn't she?","quiver","narrow","angry","mid")
            m "Speaking of Hermione..."
            g9 "Why don't you show me \"your\"{w} very much \"superior\"{w} hips?"
            call cho_main("Are you asking me to take off my skirt?","soft","wink","raised","mid")
            m "Yes, my dear."

        "\"Nope, you lose\"":
            $ cho_mood +=6

            call cho_main("What?!","scream","wide","angry","mid", trans="hpunch")
            call cho_main("","angry","narrow","angry","mid")
            m "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!"
            m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
            call cho_main("But she doesn't even do work-outs!","angry","narrow","angry","downR")
            m "Let's just forget about her, shall we?"
            m "And continute where we left off..."
            call cho_main("And where would that be?","annoyed","narrow","angry","mid")
            m "Your Quidditch training, Miss Chang."
            call cho_main("I'm not sure I want to after what you've just said...","annoyed","narrow","angry","R")
            m "Why? What did I say?"
            call cho_main("That Granger's body is better?! We both know that isn't true.","angry","narrow","angry","mid")
            m "Do you expect me to apologize?"
            call cho_main("Yes!{w} Admit that I'm sexier!","annoyed","closed","angry","mid") # Snobby
            g9 "You are indeed, \"very sexy\", Miss Chang!"
            call cho_main("Thank you, Sir.","base","narrow","base","mid")
            m "Now take of that skirt, would you..."
            call cho_main("(...)","annoyed","narrow","angry","mid")


    call cho_main("Please don't tell anybody about what I'm doing in here, Sir.","quiver","narrow","sad","mid")
    call cho_main("It could really tarnish my reputation.","soft","narrow","sad","R")
    m "I'd never think of it..."
    call cho_main("I will take off my skirt now!","scream","closed","angry","mid") # Scream
    call cho_main("","horny","narrow","sad","R")
    g9 "(!!!)"
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","base","mid")
    call ctc

    g4 "YES!"
    g4 "Look at those thighs!"
    g4 "Those tree-trunks!"
    g9 "Even the great \"Chun Lee\" would be jealous of those!"
    call cho_main("I'm sorry Sir, who's that?","soft","wink","raised","mid")
    m "One of the best female street fighters, if you know how to play with her..."
    call cho_main("(Play with her?!)","angry","wide","base","mid")
    g9 "Speaking of which!{w} I don't believe we are done here just yet."
    call cho_main("We aren't? But I did exactly what you wanted!","quiver","wide","sad","mid")
    g9 "You've still got some clothes on..."
    call cho_main("Sir, is this why you are helping me?","open","closed","angry","mid")
    call cho_main("Might this be all just part of a sick scheme to get to see me naked?","annoyed","narrow","angry","mid")
    m "(...)"

    menu:
        "\"It absolutely is!\"":
            $ cho_mood += 20
            $ cho_mad_about_stripping = True # Flag that enables different dialogue that is a bit more "lewd" in the next favor repeat.
            call cho_main("","angry","wide","base","mid") # Shock
            g9 "Now take off that bra of yours and show me those titties!"
            call cho_main("[cho_genie_name], how can you talk to me like that!","scream","closed","angry","mid", trans="hpunch")
            call cho_main("I'm your student!","open","narrow","angry","mid")
            g9 "And a very pretty one at that!"
            call cho_main("You disgust me, Professor...","angry","narrow","angry","mid")

        "\"Of course not...\"":
            $ cho_mood += 6
            $ cho_mad_about_stripping = False
            call cho_main("Aye right...","soft","narrow","raised","mid") # Expression of disbelieve...
            call cho_main("And I'm supposed to believe that.","open","narrow","base","R")
            call cho_main("You're practically foaming out of your mouth just looking at me, Sir...","soft","narrow","angry","mid")
            g4 "I'm not...{w} that's just..."
            #if butterbeer_ITEM.number > 0:
            g4 "Butterbeer..."
            call cho_main("This is as far as I will go, Sir!","annoyed","narrow","angry","mid")

    call cho_main("If you want a bimbo to strip for you, I suggest you call Hermione instead...","open","narrow","angry","mid")
    pause.5

    hide screen cho_chang
    $ cho_class.wear("all")
    call cho_main("","angry","angry","angry","mid")
    pause.8

    call cho_main("We are done here!","angry","angry","angry","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "She'll do it next time, I'm sure..."

    return



label cc_pf_strip_T1_E2: # Incomplete. Not posed.

    # Ask Cho to strip again.
    # This event is similar to Hermione's second strip favor.

    "Dev Note" ">This favour hasn't been written yet!"

    #call cho_main("Granger? And why'd she do that?","base","base","base","mid")
    #g4 "(I'm running out of excuses!)"
    #m "Because she believes you wouldn't be up for it?"
    #call cho_main("Did she?","base","base","base","mid")
    #g9 "And that I'd prefer the look of \"her\" body, over yours..."
    #call cho_main("That pretentious bitch!","base","base","base","mid")
    #call cho_main("Her body is --- compared to mine!","base","base","base","mid")



    $ cho_strip_complete = True # Unlocks Wardrobe on next summon.

    return



label cc_pf_strip_T1_E3:

    # Intro for the first time you summon Hermione to watch Cho having fun, naked in your office…

    # Cho starts to strip. Asks you some questions about Hermione.

    g9 "[cho_name], how would you like to do another strip-tease for me?"
    call cho_main("(...)","annoyed","narrow","angry","mid")
    g9 "You did such a phenomenal job last time!"
    call cho_main("Another strip show?","soft","narrow","angry","R")
    g9 "Yes Indeed! Come a bit closer..."
    call cho_main("(...)","angry","narrow","base","down")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("Sir, Those favours were never about my training, were they?","soft","narrow","angry","mid", xpos="mid", ypos="base", trans="fade")
    m "I never said they were!"
    call cho_main("","annoyed","narrow","angry","mid")
    pause.8
    m "You keep me happy by doing favours for me, and in return, I will train you..."
    m "That was the deal."
    call cho_main("I never expected that they would require me to do...{w} this!","annoyed","base","sad","down")
    g9 "But you did it anyway! Commendable!"
    call cho_main("Please stop it with your compliments, Sir!","open","closed","angry","mid")
    call cho_main("And explain to me why those favours have to be so...","annoyed","narrow","sad","downR")
    call cho_main("perverted?","soft","narrow","angry","R") # Small text
    m "You see,..."
    m "It can get pretty lonely in this room."
    m "There's not even a television set up here..."
    call cho_main("(...)","annoyed","narrow","angry","mid")
    pause.8

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    call update_cho_chibi_uniform
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","quiver","narrow","sad","R")
    call ctc

    call cho_main("Does Granger do these sorts of things for you too?","soft","base","sad","mid")
    g9 "She does a lot of things for me. You need to be more specific!"
    call cho_main("I meant buying \"sexual favours\".{w} Doing tasks that are, let's say, a little audacious...","soft","narrow","sad","downR")
    m "Are you talking about stripping, girl?"
    call cho_main("Yes, Sir.","quiver","narrow","sad","downR")
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    call update_cho_chibi_uniform
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","base","sad","mid")
    call ctc

    # Check if Hermione has already stripped for you.
    if hg_pf_dance_OBJ.points < 2:

        # Cho demands that you get Hermione to strip, so Cho has something to blackmail her should anything happen.
        # Cho gets dressed again and storms off.

        m "Actually, she doesn't..."
        call cho_main("What? But I thought she'd-","soft","wide","base","mid")
        call cho_main("Why do you ask me to do these favours, and not Granger?","open","angry","angry","mid", trans="hpunch")
        m "Lets just say, she isn’t as progressive as you...{w} yet."
        call cho_main("You haven’t even seen her naked?","angry","base","base","mid")
        call cho_main("What favours are you even buying from her?","open","base","angry","mid")
        m "Just chit-chats, mostly..."
        call cho_main("Make her strip too!","angry","narrow","angry","mid")
        g4 "It’s not that easy, girl!"
        call cho_main("Well then get on with it!","angry","closed","angry","mid")
        call cho_main("What’s the worst that could happen?","soft","narrow","angry","R")
        m "She could report me, and I’d get kicked out of this school most likely."
        m "She’s reported me to that ministry before..."
        call cho_main("The \"Ministry of Magic\"?!","open","base","raised","mid")
        call cho_main("If they were to regulate the school rules more strictly, my chance of winning the Quidditch cup would be back down to zero!","angry","wide","sad","mid")
        call cho_main("And if Granger ever was to find out about me stripping for our headmaster, it would mean the end of my Quidditch career for sure!","quiver","base","sad","downR")
        m "So? What do you suggest we do?"
        call cho_main("Isn't it obvious?! Ask her to do more advanced favours!","soft","narrow","angry","mid")
        call cho_main("If I could get a hold of something to blackmail her with, she'd never dare to report to the ministry!","quiver","narrow","angry","R")
        m "That doesn't sound too bad of an idea..."
        call cho_main("Until then, don't expect me to undress for you until you've solved this situation...","soft","narrow","angry","mid")
        m "(Bollocks...)"
        call cho_main("","annoyed","closed","angry","mid")
        pause.5

        hide screen cho_chang
        $ cho_class.wear("all")
        call update_cho_chibi_uniform
        call cho_main("","angry","closed","angry","mid")
        pause.8

        call cho_main("Good day, Sir!","soft","narrow","angry","mid")

        # Cho leaves.
        call cho_walk(action="leave", speed=2.5)

        jump end_cho_event


    # After you got Hermione to strip.
    m "She does indeed."
    call cho_main("Really?!{w} You got that cow to take off her clothes?","soft","wide","base","mid")
    call cho_main("Did you get any prove of it?","soft","base","sad","mid")
    m "What?{w} Why would I need to do that?"
    call cho_main("To blackmail her!{w} To prove that she's in on this whole \"favour trading\" business too...","open","narrow","angry","mid")
    m "We had an eye witness, for what it's worth..."
    call cho_main("Seriously?! Who was it?","smile","base","base","mid")
    m "Snape..."
    call cho_main("What?! Professor Snape?","scream","wide","base","mid", trans="hpunch")
    call cho_main("","smile","wide","base","mid")
    m "He sort of just walked in on the action.{w} After all, the door wasn't locked..."
    call cho_main("That's too funny! I wish I could have been there when that happened!","smile","base","base","R")
    g9 "She was dancing on my desk, right here, butt naked!"
    call cho_main("That sounds sooo embarrassing!","soft","narrow","sad","up")
    m "As far as I know, that door isn't locked right now either..."
    m "Aren't you scared that Snape might walk in on you too?"
    call cho_main("*Hmmmm*","annoyed","base","base","R")

    call hide_characters
    show screen blkfade
    with d3
    call play_sound("desk")
    pause 3

    ">You watch as Cho slowly climbs onto your desk..."

    call cho_chibi("stand","on_desk","on_desk")
    hide screen bld1
    hide screen blkfade
    with d3
    call ctc

    call cho_main("I'm not scared at all, Sir!","smile","narrow","angry","mid")
    call cho_main("","horny","narrow","angry","mid")
    pause.4

    # Remove bra.
    hide screen cho_chang
    $ cho_class.strip("bra")
    call update_cho_chibi_uniform
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","angry","mid")
    call ctc

    call cho_main("It's just Professor Snape, after all...","soft","narrow","base","R")
    call cho_main("Everybody knows that he's a creep! Nobody would believe a word he says.","horny","base","angry","down")
    m "So...{w} what if it's not Snape, but some other teacher that makes their way in here?"
    call cho_main("*Huh?*{w} Oh no!","soft","wide","base","mid")
    call cho_main("For a second I forgot we even had other teachers at this school!","open","wide","sad","L")
    call cho_main("What if Professor McGonagal stumbples in here while-{w} while I-...","angry","closed","sad","mid")

    call play_sound("desk")
    call hide_characters
    show screen blkfade
    with d3
    pause 1.0

    call cho_chibi("stand","desk","base", flip=True)
    hide screen bld1
    hide screen blkfade
    with d3
    call teleport(position="cho", effect=False)
    pause.5

    call bld
    m "Don't worry. That won't happen."
    call cho_chibi("stand","desk","base")
    with d3
    pause.5

    call cho_main("Are you sure, Sir?","soft","narrow","sad","mid")
    m "You have my word on it..."
    call cho_main("O-{w}okay...","soft","narrow","sad","R")
    m "Now then, Miss Chang!{w} It's time for the grand finale..."
    g9 "Take off your panties!"
    call cho_main("(...)","annoyed","base","sad","down")
    call cho_main("Very well, Sir.","base","base","base","mid")

    # Cho asks if you could give her house points for once.
    call cho_main("But, before that, may I ask you about something?","soft","base","sad","mid")
    m "Sure..."
    call cho_main("Does Granger only ask for house points? To do this sort of thing?","open","base","base","mid")
    m "She does."
    call cho_main("And, just out of curiosity, how much do you pay her for such a favour?","soft","base","base","R")
    call blktone
    m "(What should I tell her? Should I exaggerate a bit to get her more motivated?)"

    menu:
        "\"Five points.\"":
            $ current_payout = 5

            call hide_blktone
            call cho_main("Only five points? I expected more, Sir.","horny","narrow","sad","downR")
            call cho_main("I've gotten more points for answering Quidditch questions to Madam Hooch!","open","base","base","mid")
            m "I'm sure that wasn't the only reason she gave you those points..."
            call cho_main("Just to be clear... She completely undresses?{w} For five mere points?","soft","narrow","raised","mid")
            m "Yep."
            call cho_main("What a slut! I can't believe it!","smile","narrow","angry","R")
            g9 "Sometimes I only reward her with two points!{w} If she doesn't sway her hips enough..."
            call cho_main("You don't say!","smile","base","angry","mid")
            m "Why were you asking?"

        "\"One-hundred points!\"":
            $ current_payout = 30
            $ cho_mood += 6

            call hide_blktone
            call cho_main("So many? But...","soft","wide","base","mid")
            call cho_main("Sir, don't you think that's a bit outrageous?","open","closed","angry","mid")
            call cho_main("People in house \"Ravenclaw\" work hard to earn that amount of points!","open","base","raised","L")
            call cho_main("And you're telling me that you give that cow \"one-hundred bloody points\"{w}, for showing you her tits?!","angry","narrow","angry","mid")
            m "Not just her tits, [cho_name]."
            g4 "Everything!!!"
            call cho_main("Sir, how can you agree to such a thing?","angry","closed","angry","mid")
            m "Calm down, would you. I was joking..."
            m "She doesn't get that many points from me. It's closer to thirty..."
            call cho_main("That's still far too many points!","annoyed","narrow","angry","mid")
            m "Why are you even so invested in this all of a sudden?"
            call cho_main("(...)","annoyed","narrow","angry","R")

    call cho_main("I thought,...{w} maybe...{w} just this once...","angry","base","sad","down")
    call cho_main("You could give me house points as well?","soft","base","sad","mid")
    m "Really? I thought you didn't give a flying fuck about that house cup?"
    call cho_main("Sir?!","angry","wide","base","mid") # Shock
    m "Why do you want points all of a sudden?"
    call cho_main("I have my reasons....","annoyed","narrow","angry","mid")
    call cho_main("And, as I've said, this will be a one-time-only request of mine. I promise!","open","base","base","R")
    call cho_main("I'm a fair sportsman, [cho_genie_name]. You know that...","base","closed","base","mid")
    call cho_main("I'd never subject myself to earning house-points this way!","soft","narrow","angry","mid")
    call cho_main("Unlike a certain other student at this school...","angry","narrow","angry","R")
    m "And yet you asked me for that very thing?{w} I wonder why, Miss Chang..."
    call cho_main("Just as additional motivation, Sir!","angry","closed","sad","mid")
    m "Additional motivation, so so..."
    call cho_main("Yes.","soft","narrow","sad","mid")
    m "Does that motivation come from the noble deed of earning those points for your house?"
    g4 "Or getting that dirty, corruptive feeling from the way you acquired them?"
    call cho_main("(...)","angry","closed","sad","mid") # Embarrassed
    g9 "Stripping down for points! Don't you know what that would make you?"
    call cho_main("*Uhm*","soft","narrow","sad","mid")
    m "You'd be just as cheap as Hermione..."
    call cho_main("Please, Sir.{w} Don't compare me to that whore!","annoyed","narrow","angry","mid")
    g9 "Yes, Miss Chang. A whore!"
    call cho_main("That's not why-","angry","closed","sad","mid")
    call cho_main("Please, Sir. Just this once!","soft","narrow","sad","mid")
    call cho_main("I won't ask for payment ever again!","soft","base","sad","mid")
    call cho_main("I'll strip naked for you, for... [current_payout] house points!","angry","closed","sad","mid") # Embarrassed

    menu:
        "\"Yes! Make your house proud, you slut! Earn those points!\"":
            call cho_main("Yes, Sir!","base","narrow","angry","mid")
            g9 "Take of those panties!"

        "\"No. You are better than that...\"":
            $ cho_mood += 6
            call cho_main("But Sir! I asked for them!","soft","wide","sad","mid")
            m "And I'm sure you wouldn't want to sink as low as Miss Granger, would you?"
            call cho_main("Yes! I would!","angry","closed","angry","mid")
            call cho_main("That's the entire reason I want them!!!","open","narrow","angry","R")
            m "Seriously?"
            call cho_main("Give me those points, or I will walk right out of here!","open","narrow","angry","mid")
            m "Fine. If you're that insistent on [current_payout] meager points..."
            call cho_main("Thank you.","soft","closed","base","mid")

    call cho_main("","base","narrow","angry","mid")
    pause.4

    # Remove panties.
    hide screen cho_chang
    $ cho_class.strip("panties")
    call update_cho_chibi_uniform
    show screen cho_chang
    with d3
    pause.5

    call cho_main("","horny","narrow","angry","mid")
    call ctc

    g4 "I've got to say, once again I'm very impressed by you!"
    call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
    call cho_main("You can have those, by the way.","base","narrow","angry","mid")
    call nar(">Cho throws a pair of panties onto your desk.")
    call cho_main("You can keep them, for now...","soft","narrow","base","R")
    g9 "I appreciate the notion!"
    call cho_main("","base","narrow","base","mid")
    pause.8

    # Panties acquired message!
    $ has_cho_panties = True

    m "Well then..."
    m "[current_payout] points for \"Ravencla-\""
    call cho_main("Wait Sir!{w} Not yet!","open","wide","base","mid")
    m "What? Didn't you specifically ask me for it?"
    call cho_main("I did, Sir, but...{w} we aren't done here just yet...","angry","base","sad","R")
    g9 "We aren't?"
    call cho_main("Could you please wait just a tiny bit longer, until...","soft","narrow","base","mid")
    m "Until what?"
    call cho_main("May I ask another request of you, Sir?","soft","narrow","sad","mid")
    m "Yes?{w} What is it?"

    # Cho asks you to summon Hermione.
    call cho_main("Could you please...","soft","base","sad","downR")
    call cho_main("*Uhm*...","quiver","narrow","sad","downR")
    call cho_main("Could you please summon Hermione?","soft","narrow","sad","mid")

    with hpunch
    g4 "What?"
    call cho_main("It’s time someone throws \"high and mighty\" Granger off her high horse!","open","narrow","angry","mid")
    call cho_main("She’s been a pain in my butt for years now…","angry","angry","angry","downR")
    call cho_main("This is going to be my revenge!","soft","narrow","angry","mid")
    m "Are you sure that this is such a good idea? Aren’t you scared she’ll tattle about it?"
    call cho_main("No.{w} Granger is clever...","soft","closed","base","mid")
    call cho_main("She could destroy my reputation, sure,...","soft","base","base","R")
    call cho_main("But, should that happen, I now have the means to take her down with me!","base","narrow","angry","mid")
    call cho_main("I’m not the only one stripping for you, after all.","soft","narrow","base","mid")
    m "I suppose you're right..."
    call cho_main("I can’t believe how depraved Granger actually is...","horny","narrow","angry","down")
    call cho_main("Stripping for her headmaster. What a slut...","soft","narrow","angry","mid")
    m "Aren’t you doing exactly the same?"
    call cho_main("Yes, but I’m not a whore stripping for points, unlike her!","open","closed","base","mid")
    m "Still makes you a slut..."
    call cho_main("I’m untouchable! I’ll show that bitch she can’t mess with me!","angry","angry","angry","R")
    call cho_main("This is gonna be so much fun!","smile","narrow","angry","mid")

    call cho_walk(xpos="570",ypos="base", speed=1.5)
    pause 2.0

    call cho_main("Call her already!","annoyed","narrow","angry","R", ypos="head", flip=True)
    m "I'm on it..."

    hide screen bld1
    with d3
    pause 1.0

    # Summon Hermione.
    call play_sound("door")
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call her_main("You wanted to see me, Sir?","soft","closed", ypos="head")
    call her_main("Cho?","soft","shocked", ypos="head")
    call cho_main("Hey there, Granger!","horny","narrow","angry","mid", ypos="head", flip=True) # Grinning
    call her_main("What? Why are you-","disgust","shocked", ypos="head")

    call her_walk(xpos="660",ypos="base", speed=2)

    call cho_main("","smile","narrow","angry","mid", xpos="mid", ypos="base", flip=True)
    call her_main("What the bloody hell is going on here?!","scream","closed", xpos="base", ypos="base", trans="hpunch") # Scream
    call her_main("","angry","angry")

    call cho_main("You know, just the usual...","soft","base","base","L")
    call cho_main("Stripping for our dear headmaster!","smile","angry","angry","L")
    call cho_main("I trust that you're more than familiar with it...","soft","closed","base","L")
    call her_main("You've told her?","clench","angry")
    call cho_main("So you really \"did\" do it!","open","wide","base","L")
    call her_main("That's none of your business what I do at this school! You slut!","angry","angryL")
    call cho_main("Are you sure? I believe there are some people that would think otherwise...","angry","narrow","base","mid")
    call cho_main("Your friends...{w} the other students...{w} our teachers...","soft","narrow","angry","L")
    call cho_main("Maybe even the ministry?","smile","narrow","angry","L")
    call her_main("You wouldn't dare!!!","upset","squint")
    call cho_main("Indeed, I wouldn't.","soft","closed","base","mid")
    call cho_main("And neither would you!","smile","narrow","angry","L")
    call cho_main("Which is why we brought you here...","open","base","base","mid")
    call cho_main("To have some fun!","base","narrow","angry","mid")

    call her_main("Sir, I demand that you stop her nonsense!","open","angry")
    call cho_main("I don't think he will do that, Granger...","soft","narrow","angry","mid")
    call cho_main("We both know what he prefers...","soft","closed","base","mid")
    call cho_main("And who he prefers...","smile","angry","angry","mid")
    call her_main("And you think that's you?","soft","angryL")
    call cho_main("Why don't we just ask him?","base","narrow","base","mid")
    call cho_main("Tell us, Professor...","soft","narrow","base","R")
    call cho_main("How do you like the athletic, immaculate, nude body of your favourite student?","smile","narrow","angry","mid")
    call cho_main("How does it compare to Miss Granger's?","base","narrow","angry","mid")
    call ctc

    jump cc_pf_strip_T1_hermione



label cc_pf_strip_T1_E4: # Complete. Not posed.

    g9 "[cho_name], I’m in the mood for another strip-tease!"
    cho "Funny you should say that, [cho_genie_name]..."

    # Cho removes her top.
    # Cho removes her robe.

    cho "Because so am I!"

    # Cho removes her bottom.

    g4 "*Argh!* You little minx!"

    cho "Are we going to invite Granger again?"
    cho "I want to have some fun with her..."
    cho "Let her watch..."

    # Cho removes her bra.

    g9 "The more, the merrier!"
    cho "I agree."

    # Cho removes her panties.

    cho "Catch, [cho_genie_name]!"
    call nar("Cho throws her panties at you.")

    # Panties acquired message!
    $ has_cho_panties = True

    g9 "Nice!"
    cho "I'd like to have them back after this, mind you."
    m "Of course..."
    cho "Now, if you don't mind, Sir..."
    cho "I'd like you to call that Gryffindor slut to your office!"
    g9 "On it!"
    cho "(...)"
    m "(...)"

    # Hermione enters.
    call her_chibi("stand","door","base")
    with d3
    pause.2

    her "You wanted to see me, Professor?"
    g9 "Yes, but I wasn't the only one."
    her "(...)" # Annoyed look at Cho
    cho "Hi, Granger!" # Grinning
    her "Let me guess, we are here to marvel at your insecurity again?"
    cho "Why don't you join me, Granger? Strip down for your headmaster, like you usually do..."
    her "*glare*" # Hermione glares at you angrily.
    cho "Maybe then you'd have a chance to win against me! And earn some useless Gryffindor point while you're at it."
    her "I don't think that will even be necessary..."
    cho "Well, we all know how this is going to end, don't we, [cho_genie_name]?"
    cho "My body is still better than Miss Granger's, isn't it?"

    jump cc_pf_strip_T1_hermione



label cc_pf_strip_T1_hermione: # Almost complete. Missing 1 menu branch. Not posed.

    menu:
        "\"Definitely!\"":
            $ her_mood += 10

            # Hermione steals Cho's clothes and runs off.

            # Cho has to sneak out naked.

            jump end_cho_strip_event

        "\"Not even close.\"":
            $ cho_mood += 15
            cho "Thank you, Sir. Just what I thought you'd sa-"
            her "*Hihihi*"
            cho "What?!"
            cho "Professor, could you please repeat that for me?"
            m "Hermione's body is better."
            her "Thank you, Professor..." # Small text. Cute and shy
            cho "No!{w} It clearly isn't!" # Scream
            cho "You are mad, old man!"
            her "Don't talk like that to our headmaster..."
            her "After all, he's the smartest living wizard!{w} Surely he has to know what he's talking about."
            g9 "Miss Granger, why don't you show Miss Chang why I chose you..."
            g9 "Share with us your two most compelling arguments..."
            her "Sir?"
            cho "He's talking about your \"tits\", you dimwit!" # Angry
            her "(...)" # Embarrassed
            g9 "Yes Miss Granger!{w} Your very round{w}, handsomely sphered{w}, perfectly sized{w}, very voluptuous and-"
            her "I got it, Professor!"
            cho "(Cow tits...)"
            her "Here..."

            # Hermione lifts her top

            her "Have a good look."
            cho "(...)" # Tries to look away.
            her "You can have a peek too, slut."
            cho "I'd rather not, or I might have to vomit..." #
            g9 "Very nice, Miss Granger!"

            menu:
                "\"Ten points to Gryffindor!\"":
                    cho "(...)"

                "\"Fifty points to Gryffindor!\"":
                    $ cho_mood += 10
                    cho "(Fifty?!)" # Shocked

            her "Thank you."
            g9 "For exposing those magnificent breasts to us."
            her "Any time, Professor."
            cho "(I bloody hate her!)"

            her "If you don't mind, Sir."
            her "I'd like to leave now."
            cho "By all means, just go already."
            her "Is somebody mad? Did something not go as you expected?"
            her "Even exposing yourself wasn't in your favour..."
            her "Thank you for inviting me, Professor."
            her "I \"did\" enjoy watching this little, obscene freak-show you've arranged for me..."
            cho "You'll regret this, Granger!"
            her "Oh, will I?{w} I bet it's just another empty threat of yours."
            her "You don't have the balls..."
            cho "(...)"

            if daytime:
                her "Have a nice day, Professor."
            else:
                her "Have a good night, Professor."

            m "(...)"
            her "See you in school, slut!"
            cho "*Tzzzz!*"
            cho "Cow..."

            # Hermione leaves.
            call her_walk(action="leave", speed=2.5)

            cho "I thought you were on my side, Sir..."
            m "I'm on nobody's side, because nobody is on my side..."
            cho "You're supposed to have my back! Not Granger's!"
            cho "That \"whore\" doesn't deserve your praise!"
            m "She made some good arguments..."
            g9 "\"Two\" good arguments, to be precise!"
            cho "They're barely larger than mine!"
            cho "You'll see, Sir. I'm better than her. I'll prove it to you..."
            g9 "I'm looking forward to it!"

            # Cho puts her clothes back on.

            # Cho walks closer to your desk.

            cho "Sir, my *uhm*... my panties..."
            m "Oh, Right...{w} one second."
            call nar("You give them one last sniff before handing them back to the girl.")
            g4 "There."
            cho "(Pervert...)"
            cho "I have to go now."
            cho "Until next time, [cho_genie_name]."

            # Cho leaves.
            call cho_walk(action="leave", speed=2.5)

            call bld
            g4 "Damn!"
            g9 "For somebody that does a lot of sport, she smells really nice!"
            m "Maybe I should be a bit nicer to her next time..."

            $ has_cho_panties = False

            jump end_cho_strip_event


        "\"Ask Hermione.\"":
            $ her_mood += 6
            cho "Her?"
            her "I couldn't care less about the way she looks!"
            m "Are you sure about that? I've seen you staring..."
            her "Because she just so happens to be standing there, butt naked! In your own office!"
            her "What other choice to I have than to look at the obscenity of this slut!"
            m "I'd like to you rate Miss Chang's figure, truthfully, and to the best of your ability."
            her "Do I really have to?"
            g9 "You do! And I'd really like to hear your opinion about Miss Chang's shamelessly exposed body!"
            cho "*Hmmmpf*" # Self assured.
            her "Fine..."
            her "\"Poor\", I'd say..."
            cho "How dare you! You snobby skunk!"
            m "(Is that better or worse than \"troll\"?)" # Snape explained school ratings during the match.
            cho "Our Professor asked you to rate my body truthfully!"
            her "Which I did!{w} And it's at \"dreadful\" now!"
            cho "\"Dreadful\"?!"
            cho "You're a lying bitch, Granger!"
            her "Sir, you can't let her talk to me like that!"
            m "Bitch isn't even a proper curse word. You can even say that on TV..."
            cho "Tell me Granger. If my body is so noticeably flawed as you say, then it shouldn't be too difficult for you to define those flaws for us."
            her "Very well…"
            her "For one, you are one huge narcissistic bitch!{w} That likes to think her body is superior to others..."
            cho "Because it is." # Grinning
            her "Not to mention that you have even fever curves than some of the boys I know..."
            her "Maybe once your Quidditch endeavors all fail, you can apply for a profession to model male underwear..."
            cho "Nice one, Granger."
            cho "I wonder where you're getting \"your\" undergarments from..."
            cho "Stealing them from Madam Pomfrey, are ye?"
            her "I do not!!!"
            m "Girls, we all know that what really counts is how we look on the inside."
            cho "Oh- Shut up!" # Annoyed
            her "Professor, you are the one who continuously asks us to expose ourselves for you..." # Angry
            m "Well yes. I also never claimed that \"I\" was pretty on the inside."
            m "I'm a guy, Miss Granger. You of all people should know better..."
            her "Despicable..."
            cho "If you're to start doing hourly exercises, our Professor might even be attracted to you by the end of the year..."
            her "Hourly exercises?" # Shocked
            cho "Don't worry, Granger.{w} Not all is lost."
            cho "While your figure might be a bit repulsive on the eyes..."
            cho "I don't mind looking at those huge melons of yours."
            her "How dare you talk of them like that!"
            g9 "*Heh*... melons..."
            her "Sir, I’d like to leave now."

            cho "Already missing your books?"
            her "I am not. And I don't appreciate being made fun of!"

            if daytime:
                her "Good day, Sir."
                cho "See ya around, Granger..."
                her "*Hmpf*"

            else:
                her "Good night, Sir."
                cho "Nighty-night, Granger..."
                her "*Tzzzzzh!*"

            # Hermione leaves.
            call her_walk(action="leave", speed=2.5)

            cho "I have to say, [cho_genie_name], doing these favours is fun!"
            m "I'm glad you're enjoying yourself."
            cho "Believe me, Sir. I am."

            # Cho puts her clothes back on.

            cho "Now, if you excuse me..."

            if daytime:
                cho "I have to head back to classes."
                m "I still got your-"
                cho "See ya next time, [cho_genie_name]!"
            else:
                cho "I have to head back to our dorms."
                m "Don't you want your-"
                cho "Sweet dreams, [cho_genie_name]!"

            g9 "Nice, her panties!"

            $ has_cho_panties = True

            jump end_cho_strip_event
