

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

        $ hg_jerkoff.triggered()

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
# She tells you true stories that happened at Hogwards.
# Favors can revolve around Cho, Luna, Tonks

label hg_pf_talk_T3_intro_E1:

    m "Let's have another chat [hermione_name]."
    call her_main("Okay...","annoyed","worried")
    m "I'd like you to tell me a bit about your day."
    call her_main("Are you going to...{w=0.8} touch yourself again sir?","open","suspicious")
    m "I can't guarantee I won't...."
    m "You will be awarded your house points as usual."
    call her_main("...","mad","down", cheeks="blush") #mad Blush
    m "You've not walked out the door so please, tell me about your day."

    call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_E1:
    m "{size=-4}(Unless we spice things up a bit...){/size}"
    menu:
        "-Suggest inviting Snape-":
            pass
            #To be added
            # $ hg_pf_talk_snape.start()
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ hg_pf_talk_tonks.start()
        "-Decide against it-":
           
            m "Tell me about your day [hermione_name]."
            her "Okay..."

            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3:

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
    her "What? Didn't we decide it was going to be between just you and I?"
    m "Well, why only the two of us when there was the option to bring another person in?"
    her "The option to?"
    her "Sorry, I'm not following..."
    m "[hermione_name], what is your opinion of Miss Tonks?"
    her "Well, she's a very talented witch... You'd have to be to become an auror."
    m "Wouldn't it be great if we could have another chat with each other?"
    m "I heard you already had a bit of a talk previously."
    her "You knew about that?" #worried
    m "I'm the headmaster [hermione_name]...{w} It's my job to know what goes on within the castle."
    m "She was the one that suggested you try selling some favours yourself was it not?"
    her "Well..."
    m "I think it could be quite nice to have a little conversation all of us together."
    her "Just a conversation then?"
    m "Yes, just a conversation..."
    m "And you'd be awarded points of course."
    her "..." #Upset mouth #Worried eyes
    her "Would I be getting any extra points for this?"
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    her "Okay..."
    m "Great, I'll call for her then..."
    
    call hg_pf_talk_tonks
    
    jump end_hg_pf_talk
    
label hg_pf_talk_tonks_T3_E1:

    m "Let's call Miss Tonks up for this one shall we."
    her "For what?"
    m "For today's favour of course!"
    her "..."
    her "Will I get any extra points for this?"
    m "Well, that will be up to Miss Tonks, [hermione_name]."
    her "Fine.."
    
    call hg_pf_talk_tonks
    
    jump end_hg_pf_talk
    
label hg_pf_talk_tonks:
    
    her "Hello, Professor Tonks."
    if daytime:
        m "Good day, Miss Tonks."
    else:
        m "Good evening, Miss Tonks."
    if daytime:
        ton "Good day, Professor."
    else:
        ton "Good evening, Professor."
    ton "Hermione..." # Horny
    ton "Is there some sort of special circumstance as to why the two of you summoned me here?"
    m "More or less."
    m "I think the three of us should have a bit of a chat..."
    ton "Miss Granger, you didn't cause any trouble I hope?"
    her "Me? Of course not!"
    m "Now, I thought we could have a chat about these favour trading allegations that you most kindly brought to Miss Tonks' attention." #changed 'think' to 'thought'
    her "Oh, those..."
    m "Unless you've suddenly changed your mind on that sort of thing?"
    her "..."
    her "No, I'll talk about it if you like..." #Blush
    ton "..." #Smirk
    m "Why don't we start with..."
    menu:
        "\"Those pesky Slytherin Sluts!\"":
            ton "Yes, I've heard those Slytherin girls are up to no good..."
            her "They are! Where do I begin?"
            # Add option to jerk off here.
            her "There's the time Tracey Davis gave Slughorn a lapdance, in the middle of class!"
            ton "In the middle of class?"
            her "Yes, she was just sitting on his lap while he taught from his desk..."
            her "But we could all see her moving her hips!"
            ton "Interesting... Any other incidents?"
            her "More than I could count!"
            her "I'm almost certain one of the girls wasn't wearing any underwear in class which is completely unhygienic."
            her "It was if a snail had dragged themselves across one of the seats." #there was a missing speech mark here, fixed
            her "I had to insist on staying after class and I spent a good 10 minutes scourgifying everything."
            ton "Why bother, the elves would've done it anyway."
            her "About tha...{nw}"
            ton "Actually, let's save that topic for another time..."
            ton "Is there anything else you could tell me about these... naughty Slytherin girls?"
            g9 "..."
            her "I could go on for hours about the vile things they've been up to..."
            ton "I'm not in a rush... even if I was it can wait until later."
            her "Well, that girl...{w=0.3} Pansy Parkinson... She just lets Snape grab her ass whenever he wants for 5 points each time!"
            ton "Only 5 meagre points?"
            ton "Now we can't have that can we..."
            her "I know... It angers me to the core..."
            her "Everyone has been working so hard towards winning the cup... I have been working so hard..."
            her "The way it is right now doesn't promote fairness at all."
            ton "I can see how that could be a problem..."
            her "It's a huge problem!"

        "\"Yourself, Miss Granger!\"":
            her "What?!"
            ton "Yes, I would love to hear a bit more about what's going on with you Miss Granger... once I took the teaching position you and I had a bit of a discussion didn't we?"
            ton "From what I've been hearing on the Portrait vine you have been selling a few favours yourself to professor Dumbledore here..."
            her "I have not!"
            if masturbating:
                pass
                #Add writing
            else:
                m "She totally has."
                her "*hmpf!*" # Annoyed
            ton "Don't be so shy girl, I'm happy that you took my advice to heart... it's also thanks to you that the ministry sent me here."
            her "I guess..."
            her "I assure you that I was actually against the practice during the time of sending the letter..."
            her "At least I was until we had our talk about me trying it out for myself..."
            her "To help my house catch up in points. Doing it to help Gryffindor..."
            ton "Well if you can't beat them...."
            ton "So how has that been working for you so far?"
            ton "How is morale amongst the Gryffindors, now?"
            her "It's great! Although I still believe that it isn't fair..."
            her "That is why I created the \"M.R.M\"!"
            ton "Yes. The \"Men's Reign Movement\"..."
            her "But- that's not what \"M.R.M\" stands for!"
            her "It's the \"Men's Rights Movement\"!"
            her "I've told you both about it... In detail!"
            ton "I see, I probably wrote it down and put it somewhere in my... extensive notes folder..."
            m "*Heh!* It's like looking at myself in a mirror..." # Small text
            her "(...)" # Annoyed
            her "The \"M.R.M\" is there to provide male students with the same fairness, righteousness, and just benefits that girls are receiving at the school."
            her "I felt its creation was necessary..."


    her "All this favour trading has been completely unfair to the boys!"
    ton "Ah, yes... yes."
    ton "...{w}What?"
    g9 "..."
    her "Ugh... I assumed you read through the initial letter more thoroughly..."
    m "Now, now Miss Granger... Tonks was very quick to get here when she heard about your accusations."
    her "I suppose..."
    ton "Wait... So your problem was never that the girls of this school are engaging in illicit, sexual favours with their teachers..."
    ton "It's that the boys aren't able to do the same?"
    her "Exactly!"
    ton "Why didn't you say so during our talk earlier Miss Granger?"
    ton "I can easily sort out that problem!"
    her "I did mention it!"
    ton "Oh..."
    ton "Hold on..."
    ton "That doesn't explain as to why you decided to contribute to this problem and do favours for your teachers as well."
    her "Well..."
    ton "There is no need for you to keep up an act if you changed your mind on it."
    ton "You can tell us. I most certainly won't judge you..." # Horny
    her "I just...{w} Sometimes Gryffindor is just so far behind in points, I also only asked Professor Dumbledore for a favour once or twice..."
    ton "Oh, I see... and I suppose you're against the idea of doing favours for another teacher?"
    her "I..." #Hesitant Nervousness
    her "Ummm... maybe?"
    her "I haven't actively considered it..."
    ton "Don't think I'm judging you Miss Granger. I'm sure your house has been ecstatic about the sudden spike in house points."


    m "I think we've been trailing a bit off topic here..."
    ton "Oh yes, perhaps..."
    m "Miss granger, why don't you tell us more about..."
    menu:
        "\"Those pesky Slytherin Sluts!\"":
            her "What else would you like to know?"
            m "What other classes do you have here?"
            her "I'm not sure what you mean professor..."
            ton "I think what your headmaster is getting at..."
            ton "Is there any other... uncouth behaviour going on outside of the dungeons? You've only mentioned potions and alchemy class thus far."
            m "Yes, that!"
            her "Well of course there is... Even if they might not be as successful with all the teachers there are plenty of filthy tactics being used all over the school..." #replaced 'are' with 'is'
            m "Such...{w}"
            ton "Such as?"
            #You continue stroking cock
            if cho has had hufflepuff match with hermione commentating:
                her "It's not even just the Slytherins doing it!"
                ton "Oh really?"
                her "Yes, that girl from Ravenclaw... Cho Chang, she was using some pretty dirty tactics during the first Quidditch match of the season!"
                her "You could clearly see her panties at one point and she was surely dressed that way to distract the other team..."
                ton "Hmm... sounds like watching Quidditch has gotten a lot more interesting since I was in school."
                her "I wouldn't use the word interesting to describe it..."
                ton "I'll make sure to show up to the next match to see what's going on for myself."
                her "Thank you professor..."
            elif Slytherin match has happened:
                her "You're well aware that it's not just Slytherins that has been doing stuff like this..."
                ton "If you'd like to give an example..."
                her "I'm talking about Cho Chang!"
                ton "Ah yes, the Ravenclaw seeker... she's a feisty one isn't she!"
                her "..."
                her "Yes, I can't believe I chose to commentate those matches..."
                ton "If you're having such a problem I'm sure I could step in..."
                her "..."
            elif Astoria cast imperio on susan:
                her "That Astoria girl, casting imperio on a student making her lift her top..."
                ton "Ah, yes that was unfortunate..."
                her "I take it that has been dealt with?"
                ton "Yes, there's no need for you to worry about it miss Granger..."
                ton "She has been properly reprimanded and both professor Dumbledore and I have taken it upon ourselves to work on her behaviour."
                if first training done:
                    m "Yes, it's been quite an experience for both Tonks and I that's for certain..."
                else:
                    her "I see..."
                her "Well, that's good to hear..."
                her "I would have just handed over her to the authorities if it was me..."
            else:
                her "It is quite astonishing to what level those Slytherin would go to get the teachers going..."

            her "Especially that one time during care for magical creatures..."
            ton "Oh? You weren't studying centaurs were you?"
            her "No? Why would you assume that?"
            ton "No reason... please continue..."
            her "Well, I do hope that Hagrid is above this favour trading business. He sure seems like it during my classes with him."
            her "One of those Slytherin students was being quite rough with a blast ended skrewt making it go off on purpose..."
            if masturbating:
                her "She was slowly moving it up and down only agitating it a bit initially..."
                m "(Yes I bet you'd love to do that with my cock.)"
                her "But once she got going you could really see how it could just go off any minute..."
                m "(Yes, any minute now...)"
                her "I was just about to call her out on it as it started shaking violently."
                m "(Yes, any second now...)"
                ton "Then what happened?"
                her "I could momentarily see the concerned look on her face as the skrewt exploded right into it..."
                m "(Yes, take it right on your face you slut!)"
                # Genie cums
            else:
                ton "Now that's fucked up!"
                her "I know! Finally!"
                ton "That's not how you're supposed to care for a blast ended skrewt..."
                ton "Wait, what is a blast ended skrewt actually?"
                her "It's some crossbreed that Hagrid made... I don't know exactly how he managed it..."
                ton "Sounds to me that this Hagrid fellow has been doing some illegal breeding..."
                m "*Ahem*"
                ton "Although all things considered!"
                ton "It's probably nothing too bad."
        "\"Yourself.\"":
            her "Well..."
            ton "Yes..."
            ton "What does our Headmaster ask of you? To earn those house points."
            g4 "..."
            ton "..." #Winks
            her "I..."
            ton "Go on, I'm sure the Headmaster doesn't mind. My lips are sealed."
            her "Professor..."
            m "Miss Granger, your professor asked you a question..."
            her "But I thought it was supposed to stay between just you and I..."
            menu:
                "\"That's true\"":
                    m "Then let's end it here for today..."
                    ton "But sir..."
                    m "Tonks..."
                    ton "Fine..."
                    ton "I've thoroughly enjoyed it in any case."
                    m "Yes."
                "\"Tonks isn't some kind of snitch\"":
                    m "I'm sure we can take Miss Tonks by her word."
                    her "But..."
                    m "I'm sure Miss Tonks would be happy to provide an additional [points] as you'd basically be providing a favour for us both."
                    ton "*Hmmm* Oh yes, I'd love to be of help for the Gryffindor house."
                    her "Okay then, I want an additional [points] in that case."
                    m "That can be arran..."
                    ton "Done!"
                    her "W...What would you like to know about then?"
                    ton "I'd be happy with anything you'd like to tell me..."
                    her "Well... it's quite embarrassing."
                    ton "Yes?" #Horny
                    her "Well, he made me dance for him..."
                    ton "Yes... dance..."
                    ton "And how did that make you feel?"
                    her "Humiliated!"
                    ton "And your headmaster, did he enjoy it?"
                    m "I sure wa...{nw}"
                    ton "I'm asking miss Granger."
                    m "Oh, of course!"
                    her "He did seem to enjoy it."
                    her "Maybe a bit too much even..."
                    ton "That just means you did a great job Miss Granger."
                    ton "Your house surely benefited even more from it."
                    her "True..."
                    ton "Well, I do believe we're done here..."
                    ton "You've done a great job Miss Granger, Gryffindor should be proud."
                    ton "[Points] to Gryffindor..."
                    her "Thank you."
                    m "Yes..."

                #needs writing
    m "That surely was something Miss Granger..."
    ton "It was... I'm glad you two called me..." #removed 'on' think it's superfluous here
    ton "This conversation has been very enlightening."

    return
