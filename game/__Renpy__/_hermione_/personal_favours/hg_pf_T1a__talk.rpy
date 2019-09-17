

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
# 'hg_jerkoff.trigger' is required to advance into the next tier.
# Event 1 (i) - Hermione can spot you jerking off.
# Event 2 (r) - Slight dialogue variation if you've been busted jerking off before.

label hg_pf_talk_T2_intro_E1:

    call her_main("Very well, Sir.","base","base")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2_E1:

    if hg_jerkoff.trigger:
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
        if hg_jerkoff.trigger:
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

        if hg_jerkoff.trigger == False:
            $ achievement.unlock("busted")
        $ hg_jerkoff.triggered() # .trigger = True, .counter += 1


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

    "Dev Note" "Add long intro here."

    call hg_talk_3

    jump end_hg_pf_talk


label hg_pf_talk_T3_E1:

    "Dev Note" "Add short repeated intro here."

    call hg_talk_3

    jump end_hg_pf_talk


label hg_talk_3:


    menu:
        "-Start jerking off-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call her_main("[genie_name], don't tell me you are...","open","suspicious")
            call her_main("Masturbating again.....","disgust","suspicious")
            m "Me? I'd never do such a thing. Ever..."
            call her_main("I caught you before, remember?","annoyed","angry")
            m "Oh right..."
            m "Anyhow... Don't forget why you are here, [hermione_name]. To earn some points..."

        "-Participate in the conversation-":
            $ masturbating = False
            m "Don't mention it."

    call her_main("Well, as I was saying...","open","closed")
    her "Today started off fairly normal..."
    her "We had muggle studies."
    her "Professor Burbage babbled on about things she doesn't understand as usual."
    her " As I'm a muggle born I've been considering dropping the subject as it's a waste of time."
    her "Although since I failed that test I feel like I need all the extra points I can get..."
    her "Her views on muggle and wizarding relations and the fact that we're not that different is also quite refreshing..."
    her "Not that the Slytherins aren't constantly trying to disrupt her classes..."
    if masturbating:
        m "*Hmm* I bet they were...."
        her "*UGH* Do you have to keep touching yourself professor?"
        m "Just keep talking [hermione_name]..."
        her "Fine..."
    else:
        m "Is that so?"
    m "So, what were they doing exactly?"
    her "Well, her room is filled with a bunch of muggle toys, instruments and trinkets..."
    her "Her collection would even bring Mr Weasleys to shame."
    if masturbating:
        m "(I bet she has a bunch of sex toys in there...)"
    else:
        m "Maybe I should have a look at her collection myself."
    her "There's obviously nothing that stands out as odd to me in any way."
    her "But since most of the Slytherins are pure-blood they were handling her items with little to no care."
    her "So when they weren't silently insulting her about her views they were constantly making suggestive remarks about the objects asking where she'd insert that one..."
    her "She's quite oblivious to it most of the time but the constant giggling from the Slytherin girls is very distracting and annoying."
    her "It didn't help when they discovered what professor Burbage actually believed to be a back massager..."
    m "I mean, that's what it says on the box..."
    m "Wait, how do you know what people usually use them for?"
    her "..."#Blush
    m "Well?"
    her "Well, it's obvious to anyone with common sense isn't it!"
    her "Even those Slytherin girls quickly realised what people use it for... and they're thicker than polyjuice potion!"
    if masturbating:
        m "(I bet you wouldn't mind nicking it for yourself...)"
    else:
        m "(Poly... what?)"
    m "Why don't you tell me since you seem to knowledgeable about the subject..."
    her "Sorry?"
    m "What do{nw=0.2} people use those massagers for?"
    her "Well, you know..."
    m "Pretend that I don't."
    her "..."

    if masturbating:
        her "They use it for what you're doing..."
        m "Which is..."
        her "They insert it... and use it to..."
        m "To what?"
        her "To pleasure themselves..."
        m "And are you using one of these devices?"
        her "Of... of course I'm not! Muggle electronics doesn't work at Hogwarts!"
        g9 "So you have one at home then?"
        her "I..."
        g9 "(I knew it, you dirty slut!)"
        her "I don't have to talk about my personal health to you!"
        g9 "I bet you use it any chance you get when nobody is around!"
        her "I am not!"
        m "So you do it even when your parents is at home?"
        her "I don...{nw}"

        g4 "{size=-4}You dirty whore! *Argh!*{/size}"
        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call cum_block
        g4 "*Argh!* YES!"

        $ her_mood = +7
        call her_main("[genie_name] did you just..?","disgust","down_raised")
        call her_main("*Yuck!*...","disgust","glance")

        m "That felt amazing..."
        her "..."
        g9 "You shouldn't hold it in, [hermione_name]... It could help you relax a bit."
        m "All great wizards do it..."
        call her_main("(.........)","annoyed","angryL")
        m "I could even go fetch that massager for you if you'd like."
        her "No!"
        m "Oh yeah, you said they don't work at the school..."
        her "That's not what I meant..."
        m "Loosen up a bit wont you, I'll figure something out don't you worry..."
        her "{size=-4}I am not-{/size}"


        call hide_characters
        call gen_chibi("came_on_desk")
        with d3
        pause.8

        call her_main("(...................)","disgust","worried")
        m "You've done well today [hermione_name]..."
        her "You've soiled your entire desk!" #Shocked
        m "I'm sure it will be cleaned at one point or another..."
        her "Gross..."
        her "Can I have my points now?"
        m "Of course..."



        # VVV Remove this bit VVV
        m "[points] to gryffindor-"
        her "Thanks, [genie_name]..." #Still a bit mad
        m "-and an extra [points] for opening up to me."
        her "What?!" #Shocked can't believe it
        her "Really?" #hesitant smile
        m "Of course [hermione_name], you've deserved it."
        her "*Oh*... Okay then, thank you I suppose..."
        m "Don't mention it."
        if daytime:
            m "Now, back to class [hermione_name]."
            her "Of course!"
            her "Good day then [genie_name]."
            m "To you as well [hermine_name]..."
        else:
            m "Now, time for bed..."
            her "What are you..."
            m "Close the door on your way out wont you..."
            her "Oh... of course [genie_name]."
            her "Good night then."
            m "Good night [hermione_name]"

    else:
        m "Yes?"
        her "They're... they're back massagers, it says so on the box... you said so yourself."
        m "Then what's the problem with the Slytherin girls having a go with it?"
        her "Nothing! I'm sure they found it very educational!"
        her "I had never seen them more interested in muggle studies in fact!"
        m "I bet..."
        m "So, since you're muggle born and all..."
        her "Yes?"
        m "I hope you properly demonstrated for them on how to use it."
        her "What? Why on earth do you think I would do that?"
        her "You take me for some sort of exhibitionist?"
        m "Sorry?"
        her "Don't you sorry me... you expect me to get my fanny out and casually just shove it in there for the whole class to see?"
        her "I'm sure they would love that and find it more than educational..."
        her "How dare you suggest-"
        m "What are you talking about? Weren't we talking about back massagers?"
        her "-I'd just tear my clothes of and..." #Scraeming mouth
        her "..." #Wide eyes
        her "I...{w} I'm sorry professor!"
        g9 "I didn't take you for such a naughty girl [hermione_name]!"
        g9 "Here we were having an innocent conversation about back massagers and you spring all this on me."
        her "Professor... I didn't mean."
        g9 "Don't you professor me..."
        her "But please, I assure you..."
        m "That will be all for today Miss Granger."



        # VVV Remvoe this bit VVV
        m "[points] to Gryffindor."
        her "But...{w} okay then...{w} Thank you [genie_name]"
        if daytime:
            m "Now, back to class [hermione_name]."
            her "Of course!"
            her "Good day then [genie_name]."
            m "To you as well [hermine_name]..."
        else:
            m "Now, time for bed..."
            her "Oh... of course [genie_name]."
            her "Good night."
            m "Good night [hermione_name]"

    return
