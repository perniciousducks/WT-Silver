

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

    her "I disapprove of such behaviour, of course."
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
        her "There is a rumour that they are actually sleeping with professor snape..."
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
        her "We need to put an end to this behaviour, [genie_name]!"
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
# She tells you true stories that happened at Hogwarts.
# Favours can revolve around Cho, Luna, Tonks

label hg_pf_talk_T3_intro_E1:
    m "Let's have another chat, [hermione_name]."
    call her_main("Okay...","annoyed","worried")
    m "I'd like you to tell me a bit about your day."
    call her_main("Are you going to...{w=0.8} touch yourself again sir?","open","suspicious")
    m "I can't guarantee I won't...."
    m "You will be awarded with house points - as usual."
    call her_main("...","mad","down", cheeks="blush") #mad Blush
    m "You've not walked out the door so please, tell me about your day."

    call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_intro_E2:
    m "Let's have another chat [hermione_name]."
    call her_main("Okay...","base","base")

    call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_repeat:
    m "{size=-4}(Should I spice things up a bit?){/size}"
    menu:
        #"-Suggest inviting Snape-":
        #    pass
        #    #To be added
        #    #$ hg_pf_talk_snape.start()
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ hg_pf_talk_tonks.start()
        "-Decide against it-":

            m "Tell me about your day [hermione_name]."
            her "Okay..."

            m "Tell me about your day, [hermione_name]."
            call her_main("Okay...","base","base")

            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3:
    call her_main("","base","base", xpos="mid", ypos="base", trans="fade")
    pause.8

    menu:
        "-Start jerking off-":
            $ her_jerk_off_counter += 1
            $ masturbating = True

            hide screen hermione_main
            call nar(">You reach under the desk and grab your cock...")
            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8
            call her_main("[genie_name], I hoped we wouldn't do this again...","open","suspicious")
            call her_main(" Are you actually... Masturbating again?","disgust","suspicious")
            m "Me? I'd never do such a thing. Ever..."
            m "Anyhow... Don't forget why you're here, [hermione_name]. To earn some points..."

        "-Participate in the conversation-":
            $ masturbating = False
            m "Time to earn those points."

    call her_main("Well...","open","closed")
    her "Today started off fairly normal..."
    call her_main("We had muggle studies.","base","base")
    call her_main("Professor Burbage babbled on about things she doesn't understand as usual.","open","baseL")
    call her_main("As I'm a muggle born I've been considering dropping the subject. It's a waste of time.","base","base")
    call her_main("Although since I failed that test I feel like I need all the extra points I can get...","open","down")
    call her_main("Her views on muggle and wizarding relations and the fact that we're not that different is also quite refreshing...","base","happy")
    call her_main("Not that the Slytherins aren't constantly trying to disrupt her classes...","annoyed","happyCl")
    if masturbating:
        m "*Hmm* I bet they were...."
        call her_main("*UGH* Do you have to keep touching yourself professor?","disgust","down", cheeks="blush")
        m "Just keep talking [hermione_name]..."
        call her_main("Fine...","annoyed","angryL", cheeks="blush")
    else:
        m "Is that so?"
        m "So, what were they doing exactly?"
        call her_main("Well, her room is filled with a bunch of muggle toys, instruments and trinkets...","open","base")
        call her_main("Her collection would even bring Mr Weasley's to shame.","base","base")
    if masturbating:
        m "(I bet she has a bunch of sex toys in there...)"
    else:
        m "Maybe I should have a look at her collection myself."
    call her_main("There's obviously nothing that stands out as odd to me in any way.","open","base", cheeks="blush")
    call her_main("But since most of the Slytherins are pure-blood they were handling her items with little to no care.","mad","baseL")
    call her_main("So when they weren't silently insulting her about her views they were constantly making suggestive remarks about the objects asking where she'd insert that one...","annoyed","worriedL")
    call her_main("She's quite oblivious to it most of the time but the constant giggling from the Slytherin girls is very distracting and annoying.","open","down", cheeks="blush")
    call her_main("It didn't help when they discovered what professor Burbage actually believed to be a back massager...","angry","happyCl", cheeks="blush")
    m "I mean, that's what it says on the box..."
    g4 "Wait, how do you know what people usually use them for?"
    call her_main("...","disgust","shocked", cheeks="blush")
    g9 "Well?"
    call her_main("I...","annoyed","worriedCl", cheeks="blush")
    call her_main("Well, it's obvious to anyone with common sense isn't it!","open","angryL", cheeks="blush")
    call her_main("Even those Slytherin girls quickly realised what people use it for... and they're thicker than polyjuice potion!","mad","angryCl", cheeks="blush")
    if masturbating:
        m "(I bet you wouldn't mind nicking it for yourself...)"
    else:
        m "(Poly... what?)"
    g9 "Why don't {size=+4}you{/size} tell me since you seem so knowledgeable about the subject..."
    call her_main("Sorry?","mad","worried", cheeks="blush")
    m "What {size=+4}would{/size}{w=0.6} they use those massagers for?"
    call her_main("Well, you know...","open","down", cheeks="blush")
    m "Pretend that I don't."
    call her_main("...","normal","down_raised", cheeks="blush")

    if masturbating:
        call her_main("They'd use it for what you're doing...","open","worriedCl")
        m "Which is..."
        call her_main("Well, you'd insert it...{w=0.5} and use it to...","normal","down", cheeks="blush")
        m "To what?"
        her "To pleasure yourself..."
        m "And are you using one of these devices?"
        call her_main("Of...{w=0.5} of course I'm not!{w=0.5} Muggle electronics don't work at Hogwarts!","base","happyCl", cheeks="blush")
        g9 "So you have one at home then?"
        call her_main("I...","normal","down", cheeks="blush")
        g9 "(I knew it, you dirty slut!)"
        call her_main("I don't have to talk about my personal health to you!","open","angryL", cheeks="blush")
        g9 "I bet you use it any chance you get when nobody is around!"
        call her_main("I do not!","angry","angry", cheeks="blush")
        g9 "{size=-4}So you do it even when your parents are at home?{/size}"
        g4 "{size=-4}You dirty...{w=0.5}*HNGH*...{w=0.5} whore! *Argh!*{/size}"
        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call cum_block
        g4 "*Argh!* YES!"

        $ her_mood = +7
        call her_main("[genie_name]...{w} did you just..?","disgust","down_raised")
        call hide_characters
        call gen_chibi("came_on_desk")
        call her_main("*Yuck!*...","annoyed","glance")

        m "That felt amazing..."
        her "..."
        g9 "You shouldn't hold it in, [hermione_name]... It could help you relax a bit."
        m "All great wizards do it..."
        call her_main("(.........)","annoyed","angryL")
        m "I could even go fetch that massager for you if you'd like."
        her "No!"
        m "Oh yeah, you said they don't work at the school..."
        call her_main("That's not what I meant...","annoyed","worriedCl")
        m "Loosen up a bit won't you, I'll figure something out don't you worry..."
        call her_main("{size=-4}I am not-{/size}","annoyed","worriedCl")

        call her_main("(...................)","disgust","worried")
        m "You've done well today [hermione_name]..."
        call her_main("You've soiled your entire desk!","mad","wide")
        m "I'm sure it will be cleaned at one point or another..."
        call her_main("Gross...","normal","worriedCl", cheeks="blush")
        call her_main("May I have my points now?","open","down", cheeks="blush")
        m "Of course..."
    else:
        m "Yes?"
        call her_main("They're...{w=0.5} they're back massagers, it says so on the box... you said so yourself.","open","worriedL", cheeks="blush")
        m "Then what's the problem with the Slytherin girls having a go with it?"
        call her_main("Nothing! I'm sure they found it very educational!","angry","worriedCl", cheeks="blush")
        call her_main("I had never seen them more interested in muggle studies in fact!","disgust","angryL", cheeks="blush")
        m "I bet..."
        m "So, since you're muggle born and all..."
        call her_main("Yes?","open","happy")
        m "I hope you properly demonstrated how to use it to them."
        call her_main("What? Why on earth do you think I would do that?","shock","wide", cheeks="blush")
        call her_main("Do you take me for some sort of exhibitionist?","mad","wide", cheeks="blush")
        m "Sorry?"
        call her_main("Don't you sorry me...{w=0.5} you expect me to get my fanny out and casually just shove it in there for the whole class to see?","angry","angry", cheeks="blush")
        call her_main("I'm sure they would love that and find it more than educational...","base","angryCl", cheeks="blush")
        with hpunch
        call her_main("How{w=0.8} {size=+6}dare{/size} you suggest-","open","angry", cheeks="blush")
        m "What are you talking about? Weren't we talking about back massagers?"
        call her_main("-I'd just tear my clothes off and...","open","angryCl", cheeks="blush")
        $ renpy.sound.play("sounds/glass_shatter.mp3")
        call her_main("...","mad","wide", cheeks="blush")
        her "I...{w} I'm sorry professor!"
        g9 "I didn't take you for such a naughty girl [hermione_name]!"
        g9 "Here we were having an innocent conversation about back massagers and you spring all this on me."
        call her_main("Professor... I didn't mean.","soft","worriedCl", cheeks="blush")
        g9 "Don't you 'Professor' me..."
        call her_main("But please, I assure you...","open","worried", cheeks="blush")
        m "That will be all for today Miss Granger."
        m "You've surely opened my eyes..."
        call her_main("...","annoyed","base")
    return

label hg_pf_talk_tonks_T3_intro_E1:

    m "[hermione_name], for todays favour I'd like to bring in a guest to join us."
    call her_main("What? Didn't we decide it was going to be between just you and I?", mouth="open", eye="frown")
    m "Well, why only the two of us when there was the option to bring another person in?"
    call her_main("The option to?", mouth="normal", eye="frown")
    call her_main("Sorry, I'm not following...", mouth="normal", eye="suspicious")
    m "[hermione_name], what is your opinion of Miss Tonks?"
    call her_main("Well, she's a very talented witch... You'd have to be to become an auror.", mouth="open", eye="closed")
    m "Wouldn't it be great if we could have another chat with each other?"
    m "I heard you already had a bit of a talk previously."
    call her_main("You knew about that?", mouth="angry", eye="worried", cheeks="blush")
    m "I'm the headmaster [hermione_name]...{w} It's my job to know what goes on within the castle."
    m "She was the one that suggested you try selling some favours yourself was it not?"
    call her_main("Well...", mouth="disgust", eye="down_raised")
    m "I think it could be quite nice to have a little conversation all of us together."
    call her_main("Just a conversation then?", mouth="open", eye="baseL")
    m "Yes, just a conversation..."
    m "And you'd be awarded points of course."
    call her_main("...", mouth="annoyed", eye="baseL")
    call her_main("Would I be getting any extra points for this?", mouth="open", eye="base")
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    call her_main("Okay...", mouth="base", eye="base")
    m "Great, I'll call for her then..."

    call blkfade
    call hg_pf_talk_tonks

    jump end_hg_pf_talk

label hg_pf_talk_tonks_T3_E1:

    m "Let's call Miss Tonks up for this one shall we."
    call her_main("For what?", mouth="open", eye="squint")
    m "For today's favour of course!"
    call her_main("...", mouth="annoyed", eye="glance")
    call her_main("Will I get any extra points for this?", mouth="open", eye="base")
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    call her_main("Fine..", mouth="base", eye="worriedL")

    call blkfade
    call hg_pf_talk_tonks

    jump end_hg_pf_talk

label hg_pf_talk_tonks:
    call play_sound("door")
    call ton_chibi("stand","500","base")
    call her_chibi("stand","desk","base")
    pause 1.0
    hide screen blkfade

    call her_main("Hello, Professor Tonks.", xpos="right", mouth="open", eye="closed")
    call her_main("", mouth="base", eye="base")
    if daytime:
        m "Good day, Miss Tonks."
        call ton_main("Good day, Professor.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic", xpos="600")
    else:
        m "Good evening, Miss Tonks."
        call ton_main("Good evening, Professor.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic", xpos="600")
    call ton_main("Hermione...", mouth="horny", eyes="base", pupils="wide", eyebrows="base", hair="horny")
    call ton_main("Is there some sort of special circumstance as to why the two of you summoned me here?", mouth="open", eyes="base", pupils="L", eyebrows="base", hair="basic")
    m "More or less."
    m "I think the three of us should have a bit of a chat..."
    call ton_main("Miss Granger, you didn't cause any trouble I hope?", mouth="base", eyes="base", pupils="wide", eyebrows="base", hair="basic")
    call her_main("Me? Of course not!", mouth="open", eye="closed")
    m "Now, I thought we could have a chat about these favour trading allegations that you most kindly brought to Miss Tonks' attention." #changed 'think' to 'thought'
    call her_main("Oh, those...", mouth="open", eye="down")
    m "Unless you've suddenly changed your mind on that sort of thing?"
    call her_main("...", mouth="normal", eye="baseL")
    call her_main("No, I'll talk about it if you like...", mouth="open", eye="down_raised", cheeks="blush")
    call ton_main("...", mouth="base", eyes="base", pupils="wide", eyebrows="base", hair="basic")
    m "Why don't we start with..."
    menu:
        "\"Those pesky Slytherin Sluts!\"":
            call ton_main("Yes, I've heard those Slytherin girls are up to no good...", mouth="open", eyes="base", pupils="wide", eyebrows="base", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("They are! Where do I begin?", mouth="open", eye="angryCl", cheeks="blush")
            menu:
                "-Start jerking off-":
                    $ her_jerk_off_counter += 1
                    $ masturbating = True

                    call nar(">You reach under the desk and grab your cock...")
                    call gen_chibi("jerking_behind_desk")
                    with d3
                    pause.8

                "-Participate in the conversation-":
                    $ masturbating = False

            call her_main("There's the time Tracey Davis gave Slughorn a lapdance, in the middle of class!", mouth="annoyed", eye="angryL", cheeks="blush")
            call ton_main("In the middle of class?", mouth="open", eyes="wide", pupils="wide", eyebrows="base", hair="basic")
            call her_main("Yes, she was just sitting on his lap while he taught from his desk...", mouth="open", eye="baseL", cheeks="blush")
            call her_main("But we could all see her moving her hips!", mouth="annoyed", eye="baseL", cheeks="blush")
            call ton_main("Interesting...", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="horny")
            call ton_main("Any other incidents?", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("More than I could count!", mouth="open", eye="angryCl")
            call her_main("I'm almost certain one of the girls wasn't wearing any underwear in class which is completely unhygienic.", mouth="angry", eye="concerned")
            call her_main("It was if a snail had dragged themselves across one of the seats.", mouth="annoyed", eye="baseL", cheeks="blush")
            call her_main("I had to insist on staying after class and I spent a good 10 minutes scourgifying everything.", mouth="disgust", eye="down", cheeks="blush")
            call ton_main("Why bother, the elves would've done it anyway.", mouth="open", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
            call her_main("About tha...{w=0.4}{nw}", mouth="open", eye="frown")
            call ton_main("Actually, let's save that topic for another time...", mouth="open", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
            call ton_main("Is there anything else you could tell me about these... naughty Slytherin girls?", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("", mouth="normal", eye="annoyed")
            g9 "..."
            call her_main("I could go on for hours about the vile things they've been up to...", mouth="open", eye="annoyed")
            call ton_main("I'm not in a rush... even if I was it can wait until later.", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("Well, that girl...{w=0.3} Pansy Parkinson... She just lets Snape grab her ass whenever he wants for 5 points each time!", mouth="annoyed", eye="angryCl")
            call ton_main("Only 5 meagre points?", mouth="open", eyes="base", pupils="R", eyebrows="sad", hair="basic")
            call ton_main("Now we can't have that can we...", mouth="base", eyes="base", pupils="mid", eyebrows="sad", hair="basic")
            call her_main("I know... It angers me to the core...", mouth="annoyed", eye="worried")
            call her_main("Everyone has been working so hard towards winning the cup... I have been working so hard...", mouth="open", eye="worried", cheeks="blush")
            call her_main("The way it is right now doesn't promote fairness at all.", mouth="annoyed", eye="down")
            call ton_main("I can see how that could be a problem...", mouth="open", eyes="closed", pupils="mid", eyebrows="base", hair="basic")
            call her_main("It's a huge problem!", mouth="open", eye="angryCl")
            call ton_main("", mouth="base", eyes="closed", pupils="mid", eyebrows="base", hair="basic")

        "\"Yourself, Miss Granger!\"":
            call her_main("What?!", mouth="angry", eye="wide_stare")
            call ton_main("Yes, I would love to hear a bit more about what's going on with you Miss Granger... once I took the teaching position you and I had a bit of a discussion didn't we?", mouth="smile", eyes="base", pupils="wide", eyebrows="base", hair="basic")
            call ton_main("From what I've been hearing on the Portrait vine you have been selling a few favours yourself to professor Dumbledore here...", mouth="smile", eyes="base", pupils="L", eyebrows="raised", hair="basic")
            call her_main("I have not!", mouth="shock", eye="frown", cheeks="blush")
            menu:
                "-Start jerking off-":
                    $ her_jerk_off_counter += 1
                    $ masturbating = True

                    call nar(">You reach under the desk and grab your cock...")
                    call gen_chibi("jerking_behind_desk")
                    with d3
                    pause.8

                "-Participate in the conversation-":
                    $ masturbating = False

            if masturbating:
                g9 "(Oh yes you have, you naughty slut...)"
            else:
                $ tmp_val = her_jerk_off_counter+hg_pf_admire_panties.counter+hg_pf_admire_breasts.counter+hg_pf_grope.counter+hg_pf_strip.counter+hg_pf_handjob.counter+hg_pf_blowjob.counter+hg_pf_titjob.counter+hg_pf_sex.counter
                $ tmp_word = num_to_word(tmp_val) # Sum up all favour counters and turn them into a word.
                
                m "{size=-4}...[tmp_word]...{/size}"
                call her_main("huh?", mouth="open", eye="frown", cheeks="blush")
                m "You sold me exactly [tmp_word] favours."
                call her_main("B-but that's...{w=0.4}{nw}", mouth="angry", eye="happy", cheeks="blush")
                if tmp_val < 10:
                    call ton_main("Dissapointing but it's a start.", mouth="open", eyes="closed", pupils="R", eyebrows="base", hair="basic")
                    call her_main("...", mouth="annoyed", eye="glanceL", cheeks="blush")
                elif tmp_val >= 10 and tmp_val < 20:
                    call ton_main("Not bad, but I expected better from one of the top students in entire school.", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                elif tmp_val >= 20 and tmp_val < 30:
                    call her_main("", mouth="angry", eye="glanceL", cheeks="blush")
                    call ton_main("You go girl! I expected as much from one of my students.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    m "..."
                    call ton_main("\"I meant to say, one of {i}your{/i} students of course.", mouth="open", eyes="base", pupils="R", eyebrows="base", hair="basic")
                elif tmp_val >= 30 and tmp_val < 40:
                    call ton_main("Aren't you a sneaky one huh? Almost tricked me with those doe-like eyes of yours that you're an innocent girl.", mouth="smile", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                    call ton_main("But it turns out you're actually quite high on the list.", mouth="smile", eyes="happyCl", pupils="mid", eyebrows="raised", hair="basic")
                    call her_main("(...there's a list...?)", mouth="open", eye="surprised", cheeks="blush")
                    call ton_main("But it turns out you're actually quite high on the list.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("...", mouth="angry", eye="base", cheeks="blush")
                else:
                    call ton_main("Wow! Who would have thought you're the girl from top of the list.", mouth="smile", eyes="happyCl", pupils="wide", eyebrows="base", hair="basic")
                    call ton_main("Colour me surprised, looks like they were talking the truth afterall.", mouth="base", eyes="happyCl", pupils="wide", eyebrows="base", hair="basic")
                    call her_main("(...a list ... what list...?)", mouth="open", eye="surprised", cheeks="blush")
                    call ton_main("Congratulations for being a \"top\" student.", mouth="horny", eyes="base", pupils="L", eyebrows="base", hair="horny")
                    call her_main("...", mouth="disgust", eye="glanceL", cheeks="blush")
            call ton_main("Don't be so shy girl, I'm happy that you took my advice to heart... it's also thanks to you that the ministry sent me here.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("I guess...", mouth="disgust", eye="down_raised", cheeks="blush")
            call her_main("I assure you that I was actually against the practice during the time of sending the letter...", mouth="annoyed", eye="down", cheeks="blush")
            call her_main("At least until we had our talk about me trying it out for myself...", mouth="soft", eye="baseL", cheeks="blush")
            if masturbating:
                m "(And we've only just started...)"
            call her_main("To help my house catch up in points. Doing it to help Gryffindor...", mouth="soft", eye="down", cheeks="blush")
            if masturbating:
                g9 "(And because you love it...)"
            call ton_main("Well if you can't beat them....", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call ton_main("So how has that been working for you so far?", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call ton_main("How is morale amongst the Gryffindors, now?", mouth="open", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("It's great! Although I still believe that it isn't fair...", mouth="base", eye="happyCl", cheeks="blush")
            call her_main("That is why I created the \"M.R.M\"!", mouth="open", eye="happy")
            call ton_main("Yes. The \"Men's Reign Movement\"...", mouth="open", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
            call ton_main("", mouth="upset", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
            call her_main("But- that's not what \"M.R.M\" stands for!", mouth="annoyed", eye="base")
            call her_main("It's the \"Men's Rights Movement\"!", mouth="open", eye="base")
            call her_main("I've told you both about it... In detail!", mouth="annoyed", eye="down")
            call ton_main("I see, I probably wrote it down and put it somewhere in my... extensive notes folder...", mouth="open", eyes="base", pupils="R", eyebrows="sad", hair="basic")
            call ton_main("", mouth="upset", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            m "{size=-5}*Heh!* It's like looking at myself in a mirror...{/size}" # Small text
            call her_main("(...)", mouth="annoyed", eye="baseL")
            call her_main("The \"M.R.M\" is there to provide male students with the same fairness, righteousness, and just benefits that girls are receiving at the school.", mouth="open", eye="base")
            call her_main("I felt its creation was necessary...", mouth="open", eye="closed")

    call her_main("All this favour trading has been completely unfair to the boys!", mouth="open", eye="annoyed")
    call ton_main("Ah, yes... yes.", mouth="open", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
    call ton_main("...{w=0.1}What?", mouth="open", eyes="shocked", pupils="wide", eyebrows="wide", hair="basic")
    g9 "..."
    call ton_main("", mouth="upset", eyes="wide", pupils="wide", eyebrows="upset", hair="basic")
    call her_main("Ugh... I assumed you read through the initial letter more thoroughly...", mouth="open", eye="concerned")
    if masturbating:
        m "(And yet you're still quick to whore yourself out to your headmaster...)"
    else:
        m "Now, now Miss Granger... Tonks was very quick to get here when she heard about your accusations."
        call her_main("I suppose...", mouth="annoyed", eye="glanceL")
    call ton_main("Wait... So your problem was never that the girls of this school are engaging in illicit, sexual favours with their teachers...", mouth="open", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
    call ton_main("It's that the boys aren't able to do the same?", mouth="open", eyes="base", pupils="mid", eyebrows="upset", hair="basic")
    call her_main("Exactly!", mouth="open", eye="angryCl")
    call ton_main("Why didn't you say so during our talk earlier Miss Granger?", mouth="open", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
    call ton_main("I can easily sort out that problem!", mouth="base", eyes="base", pupils="mid", eyebrows="worried", hair="basic")
    call her_main("I did mention it!", mouth="annoyed", eye="worried")
    call ton_main("Oh...", mouth="upset", eyes="base", pupils="R", eyebrows="base", hair="basic")
    call ton_main("Hold on...", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
    call ton_main("That doesn't explain as to why you decided to contribute to this problem and do favours for your teachers as well.", mouth="open", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
    call her_main("Well...", mouth="disgust", eye="baseL")
    call ton_main("There is no need for you to keep up an act if you changed your mind on it.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
    call ton_main("You can tell us. I most certainly won't judge you...", mouth="horny", eyes="base", pupils="mid", eyebrows="base", cheeks="cheeks_blush", hair="horny")
    call her_main("I just...{w} Sometimes Gryffindor is just so far behind in points, I also only asked Professor Dumbledore for a favour once or twice...", mouth="soft", eye="down_raised")
    call ton_main("Oh, I see... and I suppose you're against the idea of doing favours for another teacher?", mouth="base", eyes="base", pupils="mid", eyebrows="upset", hair="horny")
    call her_main("I...", mouth="angry", eye="base")
    call her_main("Ummm... maybe?", mouth="soft", eye="baseL", cheeks="blush")
    call her_main("I haven't actively considered it...", mouth="soft", eye="glance", cheeks="blush")
    call ton_main("Don't think I'm judging you Miss Granger. I'm sure your house has been ecstatic about the sudden spike in house points.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")

    m "I think we've been trailing a bit off topic here..."
    call ton_main("Oh yes, perhaps...", mouth="base", eyes="base", pupils="L", eyebrows="base", hair="basic")
    m "Miss granger, why don't you tell us more about..."
    menu:
        "\"Those pesky Slytherin Sluts!\"":
            call her_main("What else would you like to know?", mouth="open", eye="base")
            m "What other classes do you have here?"
            call her_main("I'm not sure what you mean professor...", mouth="annoyed", eye="base")
            call ton_main("I think what your headmaster is getting at...", mouth="open", eyes="closed", pupils="L", eyebrows="base", hair="basic")
            call ton_main("Is there any other... uncouth behaviour going on outside of the dungeons? You've only mentioned potions and alchemy class thus far.", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            if masturbating:
                g9 "(Where did those bad teachers touch you?)"
            else:
                m "Yes, that!"
            call her_main("Well of course there is... Even if they might not be as successful with all the teachers there are plenty of filthy tactics being used all over the school...", mouth="open", eye="glance")
            if masturbating:
                m "(Filthy...)"
            else:
                m "Such...{w=0.1}{nw}"
            call ton_main("Such as?", mouth="open", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")

            if slyth_matches_won < huffl_matches_won > 0:
                call her_main("It's not even just the Slytherins doing it!", mouth="open", eye="angryCl")
                call ton_main("Oh really?", mouth="base", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                call her_main("Yes, that girl from Ravenclaw... Cho Chang, she was using some pretty dirty tactics during the first Quidditch match of the season!", mouth="open", eye="angry")
                if masturbating:
                    m "(And I bet you couldn't help enjoying it...)"
                call her_main("You could clearly see her panties at one point and she was surely dressed that way to distract the other team...", mouth="annoyed", eye="angryL")
                if masturbating:
                    m "(I'm sure it distracted the commentator as well...)"
                else:
                    m "You were looking?"
                    call her_main("...", mouth="annoyed", eyes="glanceL", cheeks="blush")
                call ton_main("Hmm... sounds like watching Quidditch has gotten a lot more interesting since I was in school.", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="horny")
                call her_main("I wouldn't use the word interesting to describe it...", mouth="annoyed", eye="worried", cheeks="blush")
                call ton_main("I'll make sure to show up to the next match to see what's going on for myself.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="horny")
                call her_main("Thank you professor...", mouth="open", eye="closed")
            elif slyth_matches_won >= huffl_matches_won > 0: #This event will be pretty rare since most people would get Hermione to strip before the Slytherin match
                call her_main("You're well aware that it's not just Slytherins that has been doing stuff like this...", mouth="open", eye="angryCl")
                call ton_main("If you'd like to give an example...", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                call her_main("I'm talking about Cho Chang!", mouth="open", eye="angry")
                call ton_main("Ah yes, the Ravenclaw seeker... she's a feisty one isn't she!", mouth="smile", eyes="closed", pupils="mid", eyebrows="base", hair="basic")
                call her_main("...", mouth="annoyed", eye="angry")
                call her_main("Yes, I can't believe I chose to commentate those matches...", mouth="open", eye="closed")
                call ton_main("If you're having such a problem I'm sure I could step in...", mouth="base", eyes="base", pupils="mid", eyebrows="upset", hair="basic")
                call her_main("...", mouth="annoyed", eye="base")
            elif ag_se_imperio_sb.counter > 0:
                call her_main("That Astoria girl, casting imperio on a student making her lift her top...", mouth="shock", eye="angryL")
                call ton_main("Ah, yes that was unfortunate...", mouth="open", eyes="base", pupils="R", eyebrows="sad", hair="basic")
                if masturbating:
                    m "(And hot...)"
                call her_main("I take it that has been dealt with?", mouth="normal", eye="frown")
                call ton_main("Yes, there's no need for you to worry about it miss Granger...", mouth="open", eyes="closed", pupils="R", eyebrows="upset", hair="basic")
                call ton_main("She has been properly reprimanded and both professor Dumbledore and I have taken it upon ourselves to work on her behaviour.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                #if first training done:
                if masturbating:
                    g9 "(If only there was a reason to give you some punishment...)"
                else:
                    m "Yes, it's been quite an experience for both Tonks and I that's for certain..."
                call her_main("I see...", mouth="normal", eye="base")
                call her_main("Well, that's good to hear...", mouth="open", eye="closed")
                call her_main("I would have just handed over her to the authorities if it was me...", mouth="open", eye="annoyed")
                call her_main("Anyway..", mouth="open", eyes="baseL")

            call her_main("It is quite astonishing to what level those Slytherins would go to get the teachers going...", mouth="open", eye="closed")
            call her_main("Especially that one time during care for magical creatures...", mouth="open", eye="base")
            call ton_main("Oh? You weren't studying centaurs were you?", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="horny")
            call her_main("No? Why would you assume that?", mouth="normal", eye="suspicious")
            call ton_main("No reason... please continue...", mouth="open", eyes="base", pupils="R", eyebrows="raised", cheeks="cheeks_blush", hair="basic")
            call ton_main("", mouth="base", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
            call her_main("Well, I do hope that Hagrid is above this favour trading business. He sure seems like it during my classes with him.", mouth="open", eye="closed")
            call her_main("One of those Slytherin students was being quite rough with a blast ended skrewt making it go off on purpose...", mouth="annoyed", eye="baseL")
            if masturbating:
                call her_main("She was slowly moving it up and down only agitating it a bit initially...", mouth="annoyed", eye="base")
                g9 "(Yes I bet you'd love to do that with my cock.)"
                call her_main("But once she got going you could really see how it could just go off any minute...", mouth="open", eye="base")
                m "(Yes, any minute now...)"
                call her_main("I was just about to call her out on it as it started shaking violently.", mouth="open", eye="baseL")
                g4 "(Yes, any second now...)"
                call ton_main("Then what happened?", mouth="base", eyes="base", pupils="mid", eyebrows="base", cheeks="cheeks_blush", hair="basic")
                call her_main("I could momentarily see the concerned look on her face as the skrewt exploded right into it...", mouth="open", eye="down", cheeks="blush")
                g4 "(Yes, take it right on your face you slut!)"
                call cum_block
                call gen_chibi("cumming_behind_desk")
                with d3
                pause.8

                call cum_block
                g4 "{size=-5}*Argh!* YES!{/size}"

                call ton_main("Are you okay professor? You're awfully quiet...", mouth="smile", eyes="base", pupils="mid", eyebrows="raised", cheeks="cheeks_blush", hair="basic")
                call her_main("(.............)", mouth="soft", eye="base")
                call hide_characters
                call gen_chibi("came_on_desk")

                m "Oh... yes, I was just so engaged in the conversation."
                call ton_main("Oh really?", mouth="open", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                call ton_main("What were we talking about then?", mouth="open", eyes="base", pupils="wide", eyebrows="raised", hair="basic")
                call ton_main("", mouth="base", eyes="base", pupils="wide", eyebrows="sad", hair="basic")
                m "Fast...{w=0.4} blended...{w=0.4} fruits?"
                call ton_main("Right...", mouth="open", eyes="closed", pupils="wide", eyebrows="sad", hair="basic")
                call ton_main("Well, then.... I think we're{w=0.4} done here...", mouth="open", eyes="base", pupils="wide", eyebrows="base", hair="basic")
                call her_main("...", mouth="normal", eye="baseL", cheeks="cheeks_blush")
                if daytime:
                    call ton_main("I'll leave you two to it, have a good day Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Good day, professor Tonks.", mouth="open", eye="base")
                else:
                    call ton_main("I'll leave you two to it, have a good night Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Good night, professor Tonks.", mouth="open", eye="base")
                call ton_main("Professor...", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                m "Miss Tonks..."
                call ton_walk(action="leave", speed=2.5)

            else:
                call ton_main("Now that's fucked up!", mouth="open", eyes="base", pupils="mid", eyebrows="angry", hair="basic")
                call her_main("I know! Finally!", mouth="open", eye="angryCl")
                call ton_main("That's not how you're supposed to care for a blast ended skrewt...", mouth="open", eyes="closed", pupils="mid", eyebrows="angry", hair="basic")
                call ton_main("Wait, what is a blast ended skrewt actually?", mouth="open", eyes="base", pupils="mid", eyebrows="sad", hair="basic")
                call her_main("It's some crossbreed that Hagrid made... I don't know exactly how he managed it...", mouth="open", eye="base")
                call ton_main("Sounds to me that this Hagrid fellow has been doing some illegal breeding...", mouth="upset", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                m "*Ahem*"
                call ton_main("Although all things considered!", mouth="open", eyes="closed", pupils="mid", eyebrows="base", hair="basic")
                call ton_main("It's probably nothing too bad.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                ton "Well then, I think we're done here."
                if daytime:
                    call ton_main("I'll leave you two to it, have a good day Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Good day, professor Tonks.", mouth="open", eye="base")
                else:
                    call ton_main("I'll leave you two to it, have a good night Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Good night, professor Tonks.", mouth="open", eye="base")
                call ton_main("Professor...", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                m "Miss Tonks..."
                call ton_walk(action="leave", speed=2.5)
        "\"Yourself.\"":
            call her_main("Well...", mouth="angry", eye="down")
            call ton_main("Yes...", mouth="smile", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
            call ton_main("What does our Headmaster ask of you? To earn those house points.", mouth="smile", eyes="base", pupils="R", eyebrows="upset", hair="basic")
            g4 "..."
            if masturbating:
                call gen_chibi("sit_behind_desk")
            call ton_main("...", mouth="smile", eyes="wink", pupils="mid", eyebrows="upset", cheeks="cheeks_blush", hair="basic")
            call her_main("I...", mouth="angry", eye="happyCl")
            call ton_main("Go on, I'm sure the Headmaster doesn't mind. My lips are sealed.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
            call her_main("Professor...", mouth="disgust", eye="down_raised")
            m "Miss Granger, your professor asked you a question..."
            call her_main("But I thought it was supposed to stay between just you and I...", mouth="disgust", eye="glance")
            menu:
                "\"That's true\"":
                    m "Then let's end it here for today..."
                    call ton_main("But sir...", mouth="open", eyes="base", pupils="mid", eyebrows="sad", hair="basic")
                    m "Tonks..."
                    call ton_main("Fine...", mouth="upset", eyes="closed", pupils="mid", eyebrows="sad", hair="basic")
                    call ton_main("I've thoroughly enjoyed it in any case.", mouth="smile", eyes="base", pupils="mid", eyebrows="sad", hair="basic")
                    g9 "Good to hear."
                    if daytime:
                        call ton_main("I'll leave you two to it, have a good day Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                        call her_main("Good day, professor Tonks.", mouth="open", eye="base")
                    else:
                        call ton_main("I'll leave you two to it, have a good night Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                        call her_main("Good night, professor Tonks.", mouth="open", eye="base")
                    call ton_walk(action="leave", speed=2.5)
                    m "(She ignored me...?)"
                    $ masturbating = False
                "\"Tonks isn't some kind of snitch\"":
                    m "I'm sure we can take Miss Tonks by her word."
                    call her_main("But...", mouth="disgust", eye="concerned")
                    m "I'm sure Miss Tonks would be happy to provide additional points as you'd basically be providing a favour for us both."
                    call ton_main("*Hmmm* Oh yes, I'd love to be of help for the Gryffindor house.", mouth="horny", eyes="base", pupils="mid", eyebrows="upset", hair="basic")
                    call her_main("Okay then, I want an additional 5 points in that case.", mouth="annoyed", eye="concerned")
                    m "That can be arran...{w=0.8}{nw}"
                    call ton_main("Done!", mouth="smile", eyes="base", pupils="mid", eyebrows="upset", hair="basic")
                    $ current_payout = 10
                    if masturbating:
                        call gen_chibi("jerk_off_behind_desk")
                        m "(This should be good...)"
                    call her_main("W...What would you like to know about then?", mouth="open", eye="baseL", cheeks="blush")
                    call ton_main("I'd be happy with anything you'd like to tell me...", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Well... it's quite embarrassing.", mouth="open", eye="down", cheeks="blush")
                    call ton_main("Yes?", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="horny")
                    call her_main("Well, he made me dance for him...", mouth="open", eye="glanceL", cheeks="blush")
                    call ton_main("Yes... dance...", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    if masturbating:
                        m "(And you loved every second of it, that butt bouncing around...)"
                    else:
                        pass
                    call ton_main("And how did that make you feel?", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("Humiliated!", mouth="annoyed", eye="glanceL", cheeks="blush")
                    call ton_main("And your headmaster, did he enjoy it?", mouth="smile", eyes="base", pupils="L", eyebrows="base", hair="basic")
                    if masturbating:
                        g9 "(And soon your butt will be bouncing on my dick...)"
                        call her_main("He did seem to enjoy it.", mouth="open", eye="closed", cheeks="blush")
                        g4 "(And once we're done you wont be able to dance again!)"
                        call cum_block
                        call gen_chibi("cumming_behind_desk")
                        with d3
                        pause.8

                        call cum_block
                        g4 "{size=-5}*Argh!* YES!{/size}"

                        call ton_main("Seems like the headmaster enjoyed our little discussion...", mouth="smile", eyes="base", pupils="mid", eyebrows="raised", cheeks="cheeks_blush", hair="basic")
                        call her_main("(.............)", mouth="soft", eye="base")
                        call hide_characters
                        call gen_chibi("came_on_desk")

                        m "*Ah-Ah*"
                        call ton_main("What have you been doing back there?", mouth="open", eyes="base", pupils="wide", eyebrows="raised", hair="basic")
                        m "I-{w=0.5}{nw}"
                        call her_main("H-he isn't doing anything! Isn't that right, Professor?", mouth="angry", eye="base", cheeks="blush")
                        call her_main("Just uhm...stretching your leg, as always.", mouth="crooked_smile", eye="happyCl", cheeks="cheeks_blush")
                        call ton_main("Right...", mouth="open", eyes="base", pupils="R", eyebrows="base", hair="basic")
                        call ton_main("Well then, since my work here is done... I need to go back to my regular duties.", mouth="open", eyes="closed", pupils="R", eyebrows="base", hair="basic")
                        if daytime:
                            call ton_main("I'll leave you two to it, have a good day Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                            call her_main("Good day, professor Tonks.", mouth="open", eye="base")
                        else:
                            call ton_main("I'll leave you two to it, have a good night Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                            call her_main("Good night, professor Tonks.", mouth="open", eye="base")
                        call ton_main("Professor...", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                        g9 "Miss Tonks..."
                        call ton_walk(action="leave", speed=2.5)
                    else:
                        m "I sure wa...{nw}"
                        call ton_main("I'm asking miss Granger.", mouth="upset", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                        m "Oh, of course!"
                    call her_main("He did seem to enjoy it.", mouth="open", eye="closed", cheeks="blush")
                    call her_main("Maybe a bit too much even...", mouth="angry", eye="glanceL", cheeks="blush")
                    call ton_main("That just means you did a great job Miss Granger.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call ton_main("Your house surely benefited even more from it.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    call her_main("True...", mouth="soft", eye="baseL", cheeks="blush")
                    call ton_main("Well, I do believe we're done here...", mouth="open", eyes="closed", pupils="mid", eyebrows="base", hair="basic")
                    call ton_main("You've done a great job Miss Granger, Gryffindor should be proud.", mouth="smile", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                    #call ton_main("35 points to Gryffindor...", mouth="smile", eyes="base", pupils="L", eyebrows="base", hair="basic")
                    #call her_main("Thank you.", mouth="base", eye="base", cheeks="blush")
                    m "Yes..."
                    m "That surely was something Miss Granger..."
                    call ton_main("It was... I'm glad you two called me...", mouth="base", eyes="happyCl", pupils="mid", eyebrows="base", hair="basic")
                    call ton_main("This conversation has been very enlightening.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")

                    if daytime:
                        call ton_main("I'll leave you two to it, have a good day Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                        call her_main("Good day, professor Tonks.", mouth="open", eye="base")
                    else:
                        call ton_main("I'll leave you two to it, have a good night Miss Granger.", mouth="base", eyes="base", pupils="mid", eyebrows="base", hair="basic")
                        call her_main("Good night, professor Tonks.", mouth="open", eye="base")
                    call ton_main("Professor...", mouth="horny", eyes="base", pupils="mid", eyebrows="raised", hair="basic")
                    g9 "Miss Tonks..."
                    call ton_walk(action="leave", speed=2.5)

    return