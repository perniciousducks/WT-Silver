

### Hermione Talks ###

label hg_pf_talk:

    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"


    # Start Event
    $ current_payout = 5
    $ hg_pf_talk.start()


    # End Event
    label end_hg_pf_talk:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    call her_main(xpos="mid", ypos="base", trans="fade")


    # Points
    if her_tier <= 3:
        $ gryffindor += current_payout
        m "[current_payout] points to \"Gryffindor\" [hermione_name]. Well done."
    elif her_tier == 4 and hg_pf_talk.points == 1:
        m "[current_payout] points to \"Gryffindor\", [hermione_name]. Well done."
        her "Oh, don't worry about the points, [genie_name]. We were just having a nice talk."
        m "Really? What about \"Gryffindor\" winning the cup?"
        call her_main("It's only [current_payout] points...","soft","baseL")
        m "If you say so."

    if hg_pf_talk.counter == 1: #First time.
        call her_main("Another [current_payout] points... The Guys will be so happy!","base","happyCl")

    if her_mood != 0:
        call her_main("Will this be all then?","annoyed","angry")
    else:
        call her_main("Will this be all then?","soft","base")
    m "Yes, you can go now."
    her "Thank you, [genie_name]."


    # Hermione leaves
    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_chibi(action="leave")


    # Increase level
    if her_tier == 1:
        if her_whoring < 3: # Points til 3
            $ her_whoring += 1

    if her_tier == 2:
        if her_whoring < 9: # Points til 9
            $ her_whoring += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pf_talk_T1_intro_E1:
    call play_music("chipper_doodle")

    m "Alright then..."
    m "Just tell me some news about you."
    call her_main("Ehm... Alright...","open","suspicious")

    call her_walk(xpos="desk", ypos="base", speed=1)

    call her_main("I just stand here and talk then...? Like this?","open","suspicious", xpos="mid", ypos="base", trans="fade")
    call ctc

    m "Well?"

    call her_main("Em... very well...","open","worried")
    call nar(">Hermione is feeling confused...")
    call her_main("...................","annoyed","angryL")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1_E1:
    call play_music("chipper_doodle")

    m "Alright then..."
    m "Just tell me some news about you."

    call her_chibi("stand","desk","base")

    call her_main("Here in the middle, right? I remember...","open","suspicious", xpos="mid", ypos="base", trans="fade")
    call ctc

    m "Yes?"

    call her_main("Em... very well...","open","worried")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1: # Call label
    call her_main("My life has been quite uneventful lately, to be honest...","annoyed","angryL")
    her "Apart from the day when I failed that test..."
    her "I still can't believe it happened..."

    menu:
        "-Jerk off while she is talking-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call her_main("[genie_name], what are you doing?","open","base", xpos="mid")
            m "What? Oh, it's nothing. Just scratching my leg."
            m "You were saying?"
            call her_main("Yes... Well, that test I failed...","open","base")

        "-Participate in the conversation-":
            $ masturbating = False #NOT JERKING OFF.
            m "Yes, what a tragedy that was..."
            her "Exactly! I'm glad you understand, [genie_name]."

    her "Come to think of it, I don't feel like talking about it anymore..."
    m "Alright, what else has happened lately?"
    her "Em... Well, I'm doing pretty well at herbology..."
    her "I mean, I always score the top marks, but I have been studying really hard anyway..."
    her "And now I sort of feel like sometimes I know more than professor Sprout herself..."

    if masturbating:
        m "{size=-4}(Yes... ah...){/size}"
    else:
        m "(Professor Sprout... He-he, what a ridiculous name...)"

    call her_main("Did you say something, [genie_name]?","normal","frown")
    m "It's nothing, keep going..."
    call her_main("Well, some students are making fun of professor Quirell behind his back...","open","base")

    her "I disapprove of such behavior, of course."
    if masturbating:
        m "{size=-4}(Come on! Say something naughty!){/size}"
    else:
        m ".................."

    her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
    her "I'm very happy about that..."
    call her_main("I think, given time, we will be able to make a real difference...","open","closed")
    call her_main("It is so invigorating to know that you are doing the right thing!","base","base")
    her "Wouldn't you agree, professor?"

    if masturbating:
        $ masturbating = False
        m "{size=-4}(Dammit. Now she's killed the mood completely...){/size}"
        call gen_chibi("sit_behind_desk")
        with d3
        pause.8
    else:
        m "Zzzz........"

    call her_main("[genie_name]?","angry","angry")
    m "Yes, yes, I'm totally listening..."
    m "This is all very self-righteous, er..."
    m "I mean, very invigorating and stuff..."
    call her_main("..........................","normal","frown")

    return



### Tier 2 ###

# Hermione realizes you've been jerking off this whole time!
# 'hg_T2_jerk_off_trigger' is required to advance into the next tier.
# Event 1 (i) - Hermione can spot you jerking off.
# Event 2 (r) - Slight dialogue variation if you've been busted jerking off before.

label hg_pf_talk_T2_intro_E1:

    call her_main("Very well, Sir.","base","base")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2_E1:

    if hg_T2_jerk_off_trigger:
        call her_main("Another talk, [hermione_name]?","soft","base")
        call her_main("(I hope he doesn't do \"that\" again...)","disgust","down_raised")
    else:
        call her_main("Of course, Sir.","soft","baseL")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2:
    call her_main("","normal","base", xpos="mid", ypos="base", trans="fade")

    call her_main("My life has been quite uneventful lately, to be honest...","annoyed","angryL")
    her "Hm..."
    her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
    her "To be honest, [genie_name], there should be none..."
    her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
    her "The things I hear those girls do simply to get a few extra points..."
    call her_main("How despicable!","open","angryCl")
    m "What does this make you then, [hermione_name]?"
    call her_main("Exactly!","normal","base")
    m "Huh?"
    call her_main("I have to work even harder to compensate for the damage those nasty girls are doing...","open","angryCl")
    call her_main("Thank you for helping me out, [genie_name].","normal","base")

    menu:
        "-Start jerking off-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call her_main("[genie_name], what are you doing?","open","base")
            her "You are not.....?"
            call her_main("Are you...?","annoyed","worriedL")
            m "What? Oh, it's nothing. Keep going."
            call her_main("Hm...","normal","frown")
            m "{size=-4}(Is she onto me? Nah...){/size}"

        "-Participate in the conversation-":
            $ masturbating = False
            m "Don't mention it."

    call her_main("Well, like I was saying...","open","closed", xpos="mid")
    her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."

    if masturbating:
        m "{size=-4}(What a slut... ah... Yes...){/size}"
    else:
        m "Ten points, huh?"

    her "Yes..."

    if masturbating:
        call her_main("And these two other girls...","annoyed","worriedL")
        her "There is a rumor that they are actually sleeping with professor snape..."
        m "{size=-4}(Yes... Those nasty \"slytherin\" sluts!){/size}"
        call her_main("Also, there was this one girl who gave a teacher a handjob, right during class...","base","base")
        m "{size=-4}(Yes... This is good stuff, go on!){/size}"
        call her_main("And this other girl, she sucked off a teacher!","annoyed","worriedL")
        m "{size=-4}(Yes! Yes!){/size}"
        call her_main("And another girl let a teacher cum in her mouth...","smile","baseL")
        her "And she swallowed it all and loved it!"
        m "{size=-4}(Wait... Is she making this up?){/size}"
        call her_main("I'm a nasty girl too, you know...","smile","glance")
        g4 "What?!"
        call her_main("I just want to suck a cock...","open_tongue","glance")
        her "I want men to cum on my face like in those videos I saw!"
        g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"

        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call cum_block
        g4 "*Argh!* YES!"

        $ her_mood = +7
        if hg_T2_jerk_off_trigger:
            call her_main("I can't believe it, [genie_name]!","soft","angry")
            call her_main("You were touching yourself!{w} Again!","angry","angry")
        else:
            call her_main("You were touching yourself, [genie_name]!","angry","angry")

        g4 "What? No, I was just... ah, shit, this feels good..."

        call hide_characters
        call gen_chibi("came_on_desk")
        with d3
        pause.8

        call her_main("This is disgusting! How could you!?","scream","worriedCl")
        her "[genie_name], you are the headmaster! You are supposed to set a good example!"
        m "Hey, little missy, are you going to judge me or do you want your points?"
        call her_main("My points please, I believe I earned those.","angry","worriedCl",emote="05")
        m "Yes, you did."
        call her_main("Ew... I feel so dirty now...","angry","angry")

        $ hg_T2_jerk_off_trigger = True

    else:
        her "We need to put an end to this behavior, [genie_name]!"
        m "Yeah, sure..."
        her "So you agree with me then?"
        her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
        m "(All I heard was \"punish girls\"...)"
        her "This will also help the boys in our school to feel less discriminated against!"
        m "The boys?"
        m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
        her "I'm so glad that you understand my concerns, [genie_name]."
        m "Yes, yes, sure..."

    return



### Tier 3 ###

# Hermione knows by now that you like to jerk off while she talks.
# She tells you true stories that happened at Hogwards.
# Favors can revolve around Cho, Luna, Tonks

label hg_pf_talk_T3_intro_E1:

    # You summon Tonks or Snape
    m "I've just got an idea!"

    call hg_talk_3

    jump end_hg_pf_talk


label hg_pf_talk_T3_E1:

    # You summon Tonks or Snape

    call hg_talk_3

    jump end_hg_pf_talk


label hg_talk_3:

    "Dev Note" "Add Tier 3 favor here."

    jump end_hg_pf_talk
