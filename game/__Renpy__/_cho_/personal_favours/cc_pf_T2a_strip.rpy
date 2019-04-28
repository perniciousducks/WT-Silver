

# Favour tier 2 - Inspect her Body

label cc_pf_strip:

    # Tier 1
    if main_matches_won <= 1:

        # First time event.
        if cc_pf_strip_OBJ.points == 0:
            call cc_pf_strip_T1_E1

        # Second time event or repeat.
        else:
            call cc_pf_strip_T1_E1

        if cho_whoring < 8: # Points til 8
            $ cho_whoring += 1
        if cc_pf_strip_OBJ.level < 3: # Hearts 1+2
            $ cc_pf_strip_OBJ.level += 1

    # Stats
    $ cc_pf_strip_OBJ.points += 1

    jump end_cho_event



### Tier 1 ###

# Event 1, summary:
# Cho will remove her clothing for you. At first she only agreed to remove her top and skirt, but after you promise her that nobody will know, she strips down completely.

# Event 2, summary:
# After getting naked again, Cho asks you to summon Hermione into your room.
# While still concerned about her reputation, and Hermione's record of tarnishing it, she knows there is no thread from Hermione anymore, as she can blackmail Hermione with the knowledge about her favor trading.
# Cho wants to body shame Hermione. You summon her. She's in shock. Cho makes fun of her and Hermione gets angry at you.

label cc_pf_strip_T1_E1:
    m "It's time for your next favour, [cho_name]."
    cho "I uhm- I think I'm ready."
    cho "What would you like me to do, [cho_genie_name]?"
    m "How often do you typically exercise, Miss Chang?"
    cho "As often as I can, [cho_genie_name]!"
    m "Which is... how often? Twice a week?"
    cho "Three times a day, Sir!"
    m "What?!"
    g4 "(I don't even jerk off that often!)"
    m "You are clearly exaggerating..."
    cho "I am not! It's necessary for somebody in my position!"

    # Add section here.

    m "I need you to remove your clothes."
    cho "(!!!)"
    m "Go on, girl. Start with the top..."
    cho "No!"
    cho "Why are you even ask me of such a thing?!"
    m "I- uhm-..."

    menu:
        "\"I need to inspect your body!\"":
            m "You know, just making sure that you are even fitted for the job...{w} Literally..."
            cho "I am!"
            m "After all, you only work out three times a day."
            m "As your [cho_genie_name], I need to have a proper look at you..."
            m "Do you even keep your body in shape?"
            m "By the looks of it I'd say you are doing okay."
            cho "Only okay?!"
            m "I can only judge you probably once I get a better look at it..."
        "\"Hermione asked me to...\"":
            cho "Granger? And why would she do that?"
            g4 "(I'm running out of excuses!)"
            m "Because she believes you wouldn't be up for it?"
            cho "Did she?"
            g9 "And that I'd prefer the look of \"her\" body, over yours..."
            cho "That pretentious bitch!"
            cho "Her body is --- compared to mine!"

    call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","angry","narrow","angry","mid")
    call cho_main("My body's at the absolute peak of human and wizard condition!","open","angry","angry","mid")
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
            cho "Yeah she's been eyeing me a lot lately..."
            cho "Even more so after our recent game against Hufflepuff. I woder why..."
            g9 "And I wonder why you haven't taken off that skirt already!"

        "\"Would you look at those abs!\"":
            cho "Uhm-..." # Embarrassed
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
                "\"I can't choose\"":
                    m  "You're both hot."
                    call cho_main("In your dreams...","pout","narrow","angry","downR")
                    g9 "Not for much longer!"
                "\"Nope, you lose\"":
                    m "I'm afraid, Miss Granger is simply...{w} how shall I put it...{w} sexier!"
                    call cho_main("What?!","scream","wide","angry","mid",trans="hpunch")
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
    call cho_main("I'm sorry, who?","soft","wink","raised","mid")

    return


label cc_pf_strip_T1_E2:
    cho "[cho_genie_name], may I ask, does Hermione do these sorts of things for you?"
    g9 "She does a lot of things for me. You need to be more specific!"
    cho "I meant buying favours. Doing tasks that are, let's say, a little audacious..."
    m "Are you talking about stripping, girl?"
    cho "I am, Sir."

    #menu:
    #    "":

    cho "[cho_genie_name], could you please do me a huge, huge favour?"
    m "For you, anything my dear..."
    cho "Great! I'd like to to summon Hermione."
    with hpunch
    g4 "What?"
    cho "You've heard right."

    jump cc_pf_strip_T1_hermione

label cc_pf_strip_T1_E3:
    jump cc_pf_strip_T1_hermione

label cc_pf_strip_T1_hermione:

    cho "Tell me, Professor..."
    cho "Do you like my athletic, naked body, Sir? Is it better than Miss Granger's?"

    menu:
        "\"Definitely!\"":
            $ cho_mood += 10
        "\"Not even close!\"":
            $ cho_mood += 30
        "\"Ask Hermione.\"":
            che "Her?"
            her "I couldn't care less about the way she looks?"
            m "Are you sure about that?"
            m "Miss Granger, I'd like to you rate Miss Chang's figure, truthfully, and to the best of your ability."
            her "Do I really have to?"

            if her_whoring < 11:
                her "I refuse to give her a rating, Professor."
            elif whoring < 24:
                her "B+"
                cho "Only a B?"
                m "With a plus at the end, mind you..."
                cho "So in your opinion, Granger, my body has flaws?"
                her "Naturally..."
                cho "That's quite curious, don't you think so too? Professor?"
                m "Is a B+ not good enough for you?"
                cho "Are you kidding? Not even close!"
                cho "And I also know she isn't entirely truthfull!"
                her "But I am! And it's a C+ now!"
                cho "You area lying bitch, Granger!"
                her "Sir, you can't let her talk to me like that!"
                m "Bitch isn't even a proper curse word. You can say it on TV..."
                cho "Tell me Granger. If my body is so noticably flawd as you say, then it should be an easy task for you to define them to us."
                her "Of course. "
                her "Well, there is obviously"

            else:
                her "I uhm-..."
                her "I'm a bit ahamed to admit, in front of her, but..."
                cho "Yes, Granger..."
                her "I'd probably give it an...{w} \"A\"."
                g9 "Hear, hear!"
                her "Maybe even an \"A+\"..."
                cho "Thank you..." # Confident.
                her "(...)"
                cho "I ecpected nothing less."
                m "I'm surprised about that, Granger."
                her "I mean would you just look at it! It's utter ridiculous!"
                her "There isn't the tiniest flaw! Her body is so marvellous it almost drives me mad!!!"
                her "I wish I could find one but..."
                cho "Yours isn't too bad either, Granger."
                cho "If you were to start doing hourly exercises, you might even get close to where I'm at by the end of the year..."
                her "Hourly exercises?" # Shocked
                cho "And I do love your huge melons!"
                her "How dare you talk of them like that!"
                g9 "*Heh*... melons..."
    cho "I have to say, [cho_genie_name], doing those favours is fun!"
