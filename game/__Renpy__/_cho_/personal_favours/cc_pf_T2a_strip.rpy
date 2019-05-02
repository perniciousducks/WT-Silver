

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
    cho "I- *uhm*...{w} I think I'm ready."
    cho "What would you like me to do, [cho_genie_name]?"
    m "How often do you typically exercise, Miss Chang?"
    cho "As often as I can, [cho_genie_name]!"
    m "Which is... how often? Twice a week?"
    cho "Three times a day, Sir!"
    with hpunch
    m "What?!"
    g4 "(I don't even jerk off that often!)"
    m "You are clearly exaggerating..."
    cho "I'm not! It's necessary for somebody in my position!"

    m "I assume you get complimented often?"
    cho "Occasionally..."
    g9 "You must have many admirers."

    # Add section here.

    m "I need you to remove your clothes."
    cho "(!!!)"
    m "Go on, girl. Start with the top..."
    cho "No!"
    cho "Why are you even asking me to do such a thing?!"
    m "I- uhm-..."

    menu:
        "\"I need to inspect your body!\"":
            m "You know, just making sure that you're fitted for that Quidditch job...{w} Literally..."
            cho "I am!"
            m "After all, you only work out three times a day."
            m "As your [cho_genie_name], I need to have a proper look at you..."
            m "Do you even keep your body in shape?"
            m "By the looks of it I'd say you are doing okay."
            cho "Only okay?!"
            m "I can only judge you probably once I've getten a better look at you..."
        "\"Hermione asked me to...\"":
            cho "Granger? And why'd she do that?"
            g4 "(I'm running out of excuses!)"
            m "Because she believes you wouldn't be up for it?"
            cho "Did she?"
            g9 "And that I'd prefer the look of \"her\" body, over yours..."
            cho "That pretentious bitch!"
            cho "Her body is --- compared to mine!"

    call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","angry","narrow","angry","mid")
    call cho_main("My body's at the absolute peak of human condition!","open","angry","angry","mid")
    g4 "It is quite impressive, I've got to say!"
    call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
    g9 "Now let me see it!"
    cho "I don't think that will be necessary, [cho_genie_name]."
    m "Have you already forgotten who helped you?"
    m "Your trusted mentor..."
    m "Your strong advisor."
    g9 "Your guardian angel!"
    cho "And I'm very thankful for that, Sir."
    g9 "Well, why don't you thank me by taking off your top?"
    cho "Is there no other way I could repay my favor?"
    m "Well yes- Several!{w} But we'll get to those later..."

    # Add section here

    call cho_main("(...)","horny","base","sad","down")
    call cho_main("Only my top?","soft","wink","base","mid")
    g9 "Would you like to take off \"more\"?"
    call cho_main("I didn't mean it like that!","angry","closed","angry","mid")
    m "[cho_name], it's only the two of us in here. Nobody will know."
    cho "And you better keep it that way, [cho_genie_name]!"
    g9 "Promise! Now take it off!"
    cho "(...)"
    m "*He-hem*{w} Slowly..."
    pause.5

    # Remove top.
    hide screen cho_chang
    $ cho_class.strip("robe","top")
    call cho_main("","base","base","base","mid")

    call ctc

    g4 "Magnificent."
    g4 "Simply...{w} magnificent..."
    cho "Thank you, Sir."

    menu:
        "\"Your posture is remarkable!\"":
            cho "Thank you, Sir!{w} I'm glad you noticed!" # Happy
            cho "It's a relief to see your interest in my body status!"
            m "(Oh- You have no idea, girl!)"
            cho "I thought you just wanted to gush at my body like all the other teachers..."
            m "Who?{w} Which other teachers are you talking about?"
            m "Snape?"
            cho "No, not him."
            cho "(...)"
            cho "Promise me you won't tell her!"
            m "Her?!"
            cho "Madame Hooch, Sir."
            m "Ah, the old, gray haired lady..."
            cho "Yeah, she's been eyeing me a lot lately..."
            cho "Even more so after our recent game against Hufflepuff. I woder why..."
            g9 "And I wonder why you haven't taken off that skirt already!"

        "\"Would you look at those abs!\"":
            cho "*Uhmm*..." # Embarrassed
            g9 "You didn't tell me you had such nice abs, girl!{w} Why were you hiding them from me?"
            cho "I wasn't hiding anything..."

            # Add section here.

            call cho_main("Are you surprised, Sir?{w} I bet you only get to see wrinkly Hermione...","soft","narrow","angry","mid")
            call cho_main("Does Hermione have abs like this? Of course she doesn't!","horny","base","raised","down")
            call cho_main("All she does is sit at the library all day stuffing her head with useless junk...","open","angry","angry","mid")
            m "(...)"
            call cho_main("I bet my \"tight\" body looks way better than hers!","soft","base","raised","mid")

            menu:
                "\"Yeah, she's gross.\"":
                    m  "Miss Granger's body is nothing compared to yours."
                    call cho_main("Really?","open","wide","raised","mid")
                    m  "Her tits sag too much, and her fat hips are disgusting..."
                    call blktone
                    g4 "(I think something inside me just died saying that.)"
                    call hide_blktone
                    call cho_main("She really is a...","open","closed","raised","mid")
                    call cho_main("...stupid...","angry","closed","angry","mid")
                    call cho_main("...fat...","angry","narrow","angry","mid")
                    call cho_main("...cow, isn't she?","quiver","narrow","angry","mid")

                "\"Nope, you lose\"":
                    call cho_main("What?!","scream","wide","angry","mid",trans="hpunch")
                    m "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!"
                    m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
                    call cho_main("But she doesn't even do work-outs!","angry","narrow","angry","downR")
                    $ cho_mood +=6

            m "Speaking of Hermione..."
            g9 "Why don't you show me \"your\"{w} very much \"superior\"{w} hips?"

            if cho_mood != 0:
                cho "I'm not sure if I want to after what you've just said..."
                m "Why? What did I say?"
                cho "That Granger's body is better?! We both know that isn't true."
                m "Do you expect me to apologize?"
                cho "Admit that mine is sexier!" # Snobby
                g9 "You are indeed, \"very sexy\", Miss Chang!"
                cho "Thank you, Sir."
            else:
                cho "Are you asking me to take off my skirt?"
                m "Yes, my dear."

    cho "Please don't tell anybody about what I'm doing in here, Sir."
    cho "It could really tarnish my reputation."
    m "I'd never think of it..."
    cho "I will take off my skirt now!" # Scream
    g9 "(!!!)"
    call cho_main("","horny","closed","angry","mid")
    pause.4

    # Remove skirt.
    hide screen cho_chang
    $ cho_class.strip("bottom")
    call cho_main("","horny","narrow","base","mid")

    call ctc

    g4 "YES!"
    g4 "Look at those thighs!"
    g4 "Those tree-trunks!"
    g9 "Even the great \"Chun Lee\" would be jealous of those!"
    call cho_main("I'm sorry Sir, who's that?","soft","wink","raised","mid")
    m "One of the best female street fighters, if you know how to play with her..."
    cho "(Play with her?!)"
    g9 "Speaking of which!{w} I don't believe we are done here just yet."
    cho "We aren't? But I did exactly what you wanted!"
    g9 "You've still got some clothes on..."
    cho "Sir is this why you are helping me?"
    cho "Is this all just part of a sick scheme to get to see me naked?"
    m "(...)"

    menu:
        "\"It absolutely is!\"":
            $ cho_mood += 20
            $ cho_mad_about_stripping = True # Flag that enables different dialogue that is a bit more "lewd" in the next favor repeat.
            g9 "Now take off that bra of yours and show me those titties!"
            cho "[cho_genie_name], how can you talk to me like that!"
            cho "I'm your student!"
            g9 "And a very pretty one at that!"
            cho "You disgust me, Professor..."

        "\"Of course not...\"":
            $ cho_mood += 6
            $ cho_mad_about_stripping = False
            cho "Aye right..." # Expression of disbelieve...
            cho "And I'm supposed to believe that."
            cho "You're practically foaming out of your mouth just looking at me..."
            g4 "I'm not...{w} that's just..."
            #if butterbeer_ITEM.number > 0:
            g4 "Butterbeer..."
            cho "This is as far as I will go, Sir!"

    cho "If you want a bimbo to strip for you, I suggest ye call Hermione instead..."

    hide screen cho_chang
    $ cho_class.wear("all")

    call cho_main("We are done here!","angry","angry","angry","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    return



label cc_pf_strip_T1_E2:
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","pout","wide","sad","mid",trans="hpunch")
    call cho_main("I'll do it.","horny","base","sad","R")

    menu:
        "\"Take off your top\"":
            m "[cho_name], why don't you take off your top?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Miss Granger is more than happy to show me her-"
            call cho_main("Fine...","pout","base","angry","R")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")
            $ cho_wear_top = False
            call cho_main("Sorry, about that.","open","base","sad","mid")
            g9 "Don't worry, girl. You're doing great!"
            call cho_main("Thanks.","angry","base","sad","R")
            m "Now take off your skirt..."
            call cho_main("O-okay...","horny","base","sad","down")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")

        "\"Take off your skirt\"":
            m "[cho_name], why don't you take off your skirt?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Just thinking about Miss Granger's ass makes me-"
            call cho_main("Fine, I'll do it...","pout","base","angry","R")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")
            $ cho_wear_bottom = False
            call cho_main("There, my skirt is gone!","angry","base","sad","down")
            g9 "I can see that, Miss Chang!"
            m "Now take off your shirt..."
            call cho_main("O-okay...","open","base","sad","mid")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")


        cho "[cho_genie_name], may I ask, does Granger do these sorts of things for you?"
        g9 "She does a lot of things for me. You need to be more specific!"
        cho "I meant buying sexual favours. Doing tasks that are, let's say, a little audacious..."
        m "Are you talking about stripping, girl?"
        cho "Yes, Sir."
        cho "Do you really pay Hermione house points for doing this sort of thing?"

        cho "Just out of curiosity, [cho_genie_name]. How much does she get for such a favour?"
        m "(What should I tell her? Should I exaggerate a bit to get her more motivated?)"

        menu:
            "\"Five points.\"":
                $ current_payout = 5
                call cho_main("Only five points? I expected more, Sir.","horny","narrow","sad","downR")
                call cho_main("I've gotten more points for answering Quidditch questions to Madam Hooch!","open","wide","raised","mid")
                m "I'm sure that wasn't the only reason she gave you those points..."
                call cho_main("Just to be clear... She completely undresses? For five mere points?","angry","narrow","sad","down")
                m "Yep"
                call cho_main("What a slut! I can't believe it!","angry","narrow","sad","down")
                m "Sometimes I only give her two if she doesn't sway her hips enough..."
                cho "You don't say!"
                m "Why were you asking?"

            "\"One-hundred points!\"":
                $ current_payout = 30
                $ cho_mood += 6
                call cho_main("So many? But...","soft","wide","base","mid")
                call cho_main("Sir, how can you agree to such a thing?","open","closed","angry","mid")
                call cho_main("People in house \"Ravenclaw\" work hard to earn that amount!","open","base","raised","L")
                call cho_main("And you're telling me that you give that cow \"one-hundred bloody points\"{w}, for showing you her tits?!","open","base","raised","L")
                m "(Well that clearly backfired...)"
                m "Not just her tits, [cho_name]."
                g4 "Everything!!!"
                call cho_main("Sir, how can you agree to such a thing?","open","closed","angry","mid")
                m "Calm down, would you. I was joking..."
                m "She doesn't get that many points from me. It's closer to thirty..."
                cho "That's still far too many points!"
                m "Why are you even so invested in this all of a sudden?"
                cho "(...)"


        cho "I thought,...{w} maybe...{w} just this once..."
        cho "You could give me house points as well?"
        m "Really? I thought you were so appalled by that though."
        cho "I still am, [cho_genie_name]!"
        cho "But if you want me to remove my clothes for you, Sir, I'll require some additional motivation!"
        m "What is your motivation I wonder..."
        cho "Sir?"
        m "Is it the noble deed of earning points for your house?..."
        g4 "Or the corruptive, dirty feeling you get from the way you acquired them?"
        cho "(...)" # Embarrassed
        g9 "Stripping down for points! Don't you know what that would make you?"
        cho "*Uhm*"
        m "You'd be just as cheap as Hermione..."
        cho "Don't compare me to that whore!"
        g9 "Yes, Miss Chang. A whore!"
        cho "That's not why-"
        cho "Please, Sir. Just this once!"
        cho "I won't ask for payment ever again!"
        cho "I'll strip naked for you, for... [current_payout] house points!" # Embarrassed

        menu:
            "\"Make your house proud, slut! Earn those points!\"":
                cho "Yes, Sir!"
                cho "Here goes my bra!"
            "\"No. You are better than that!\"":
                m ""


        g4 "It is quite impressive, I've got to say!"
        call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
        call cho_main("Now... How badly do you want me to take off the rest?","soft","angry","base","mid")

    return



label cc_pf_strip_T1_E3:

    # Intro for the first time you summon Hermione to watch Cho having fun, naked in your office…



    # Add section here.

    cho "[cho_genie_name], could you please do me a huge, huge favour?"
    m "Of course, anything my dear..."
    cho "Great! I'd like you to summon Granger."
    with hpunch
    g4 "What?"
    cho "You heard right."
    cho "It’s time someone throws \"high and mighty\" Granger from her high horse!"
    cho "She’s been a pain in my butt for years now…"
    cho "This is going to be my revenge!"

    # Check if Hermione is willing to strip for you.
    if hg_pf_dance_OBJ.points < 2:
        m "I don’t think it’s a good idea…"
        cho "Why not? I’m not scared of her!"
        m "Have you ever thought about what it could mean for me?"
        cho "What’s the worst that could happen?"
        m "She could report me, and I’d get kicked out of this school most likely."
        m "She’s reported me to that ministry before..."
        cho "The \"ministry of magic\"?!"
        cho "She's nuts! Isn’t she in on this too? All the favour trading?"
        m "Lets just say, she isn’t as progressive as you...{w} yet."
        cho "Wait, you haven’t even seen her naked?"
        cho "What favours are you even buying from her?"
        m "Just chit-chats, mostly…"
        cho "Make her strip too!"
        g4 "It’s not that easy, girl!"
        cho "Well then get on with it! I want to see her humiliated!"
        m "(...)"

        # Cho leaves.
        call cho_walk(action="leave", speed=2.5)

        jump end_cho_event

    else:
        pass

    m "Are you sure that’s a good idea? Aren’t you scared she’ll tattle about you?"
    cho "No. Granger is smarter than that..."
    cho "I’m not the only one stripping for you, ain’t I."
    m "I suppose not..."
    cho "I can’t believe how depraved Granger actually is..."

    # Cho removes her top.
    # Cho removes her robe.

    cho "Stripping for her headmaster. What a slut..."

    # Cho removed her bottom.

    m "Aren’t you doing exactly the same?"
    cho "Yes, but I’m doing it for a good cause.{w} Not because I’m a slut!"
    cho "I’m untouchable! I’ll show that bitch she can’t mess with me!"
    cho "This is gonna be so much fun!"
    cho "Don't ye think so too, [cho_genie_name]?"

    # Cho removes her bra.

    # Add writing. Hermione is shocked. Cho blackmails her...

    cho "Tell me, Professor..."
    cho "How do you like the athletic, immaculate body of your student?"
    cho "Isn't it so much better than Miss Granger's?"

    jump cc_pf_strip_T1_hermione



label cc_pf_strip_T1_E4:

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
    cho "Now, if ye don't mind, Sir..."
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



label cc_pf_strip_T1_hermione:

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
            her "Thank you for inviting me, Proffessor."
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
            call her_walk("mid","leave",2.5)

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
            cho "Don't worry, Granger.{w} Not all is lost.
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
            call her_walk("mid","leave",2.5)

            cho "I have to say, [cho_genie_name], doing these favours is fun!"
            m "I'm glad you're enjoying yourself."
            cho "Believe me, Sir. I am."

            # Cho puts her clothes back on.

            cho "Now, if ye excuse me..."

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
