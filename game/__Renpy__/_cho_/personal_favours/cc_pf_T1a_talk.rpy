

### Talk with Cho ###

label cc_pf_talk:

    ### Tier 1 (pre Hufflepuff) ###
    if cho_tier == 1:

        if cc_pf_talk.points == 0:
            # Talk about her boyfriends.
            call cc_pf_talk_T1_E1

        elif cc_pf_talk.points == 1:
            # Talk about her Quidditch team.
            # Unlocks public requests favours.
            $ cho_requests_unlocked = True
            call cc_pf_talk_T1_E2

        else:
            # Talk about Cedric some more.
            call cc_pf_talk_T1_E3

    ### Tier 2 (pre Slytherin) ###
    elif cho_tier == 2:

        if cc_pf_talk.points == 0:
            # Talk about Malfoy and his team.
            # Talk about getting bullied by Slytherin.
            call cc_pf_talk_T2_E1

        elif cc_pf_talk.points == 1:
            # Talk about becoming more popular.
            call cc_pf_talk_T2_E2

        else:
            call cc_pf_talk_T2_E3

    # End event jump
    # (only used when the event isn't called.)
    label end_cho_talk_event:

        if cho_tier == 1:
            if cho_whoring < 3: # Points til 3
                $ cho_whoring += 1

        elif cho_tier == 2:
            if cho_whoring < 9: # Points til 9
                $ cho_whoring += 1

        if cc_pf_talk.level < 4:
            $ cc_pf_talk.level += 1

    $ cc_pf_talk.points += 1

    # Stats
    $ cc_pf_talk.counter += 1

    jump end_cho_event



### Tier 1 (pre Hufflepuff) ###

label cc_pf_talk_T1_E1: # Complete
    m "Let’s have a little chat shall we."
    g9 "Just to get to know each other a little bit better."
    call cho_main("Of course, Sir.","smile","base","base","mid")
    m "First, I'd like you to come a bit closer."
    call cho_main("Very well, [cho_genie_name]...","soft","base","base","R")

    call cho_walk("desk", "base", speed=1.6)

    call play_music("chipper_doodle")
    call cho_main(face="happy",xpos="mid",ypos="base",trans="fade")
    call ctc

    call cho_main("What would you like to talk about?","soft","base","base","mid")
    m "Do you have a boyfriend, Miss Chang?"
    call cho_main("Excuse me?","open","wide","base","mid",trans="hpunch") # Shocked
    m "I asked if you have boyfriend. Anybody you fool around with?"
    call cho_main("Me? Professor? He-{w=0.8} hav-{w=0.5} a boyfrind?","open","wide","base","R") # Reluctant, Embarassed
    g9 "Or a girlfriend! That would be even better, now that I think about it!"
    call cho_main("Sir that's-{w} that's not something a headmaster should be concerned about.","open","base","sad","L")
    call cho_main("And I don’t see how this information would be of importance for my training.","open","wide","raised","downR")
    call cho_main("Why would it matter if- {w}Even if I did I'd-","soft","wide","base","down")
    g9 "So you don't have one?"
    call cho_main("You're making me nervous, [cho_genie_name]. {image=textheart}","horny","narrow","sad","R")
    m "(So cute.{w=0.5} Perhaps this is something I could push her further on...)"

    call cho_main("Sir, I do not have a boyfriend at the moment.{w} I hope that answers your question.","soft","closed","angry","mid")
    g9 "So, a girlfriend then?"
    call cho_main("!!!","angry","wide","raised","mid",trans="hpunch")
    call cho_main("No!","scream","closed","angry","mid",trans="hpunch")
    call cho_main("","annoyed","narrow","angry","mid")
    m "(She doesn’t seem that keen on the subject, perhaps I could tell her...)"

    label get_cho_to_talk:

    menu:
        "\"It's important to open up to your headmaster.\"":
            m "Emphasis on \"opening up\"..."
            call cho_main("I don't think that will be necessary, [cho_genie_name].","annoyed","narrow","angry","mid")
            m "There's a lot more to gather from discussing previous life choices than you might think."
            m "You get to learn a lot about the way someone has matured by previous experiences..."
            m "Like a first kiss, who it was with, and so on..."
            call cho_main("You think I'm mature?","soft","base","base","mid")
            g4 "(That's what she's focusing on?)"
            m "*Ahem*, yes.{w=0.5} Of course you are, don't you think so?"
            call cho_main("Well, my previous boyfriend didn't seem to think so...","open","base","raised","R")
            m "So you did have one?"
            call cho_main("*Ugh*{w=0.8} Fine...{w=0.8} I'll tell you about him...","soft","narrow","base","down")

            pass

        "\"It's okay if you like girls...\"":
            m "Swinging the other way, you know..."
            call cho_main("What?","angry","wide","base","mid")
            m "Some people like flicking the bean rather than rubbing a wand..."
            call cho_main("*Uhmm*, I never said I minded either way...","quiver","narrow","sad","R")
            m "So you have had a girlfriend?"
            call cho_main("I'd rather not talk about it right now...","soft","narrow","sad","mid")
            m "(Damn, maybe that's not the way to go about this, maybe instead I could tell her...)"

            jump get_cho_to_talk

        "\"Let me tell you something about my own previous relationships...\"":
            call cho_main("Sir, I'd rather not hear a boring old tale about any of your old flames...","open","narrow","base","R")
            g9 "Oh they weren't boring at all!"
            call cho_main("Hmm?","annoyed","narrow","base","mid")
            g9 "They were very intimate..."
            call cho_main("???","annoyed","base","raised","mid")
            g4 "Very sexual!"
            call cho_main("!!!","annoyed","wide","base","mid")
            g9 "Lots of acrobatic stuff!"
            call cho_main("NO Sir, please!{w=0.5} I don't want to know any of that!","scream","closed","angry","mid",trans="hpunch")
            call cho_main("(Gross!{w=0.5} Keep it to yourself...)","angry","narrow","sad","R")
            m "I just wanted to expand my backstory a little bit...{w=0.5} What's so wrong with that..."

            jump get_cho_to_talk

    # Cedric Diggory
    call cho_main("Cedric was my boyfriend during the time Hogwarts was hosting the \"triwizards tournament\".","soft","base","base","R")
    m "(They host tournaments here? Interesting...)"
    call cho_main("That year was the most fun I've ever had!","smile","base","base","mid")
    m "Was he that good?"
    call cho_main("What?{w=0.5} No, Sir, not because of him!{w} The tourney, [cho_genie_name]!","soft","narrow","base","mid")
    m "Sure..."
    call cho_main("We should have it every year if you were to ask me!","open","closed","base","mid")
    g9 "(A cosplay tournament is what this school needs...)"
    call cho_main("Sir that would be great!","smile","narrow","base","mid")
    g4 "(Wait, wait!{w=0.8} A \"nude\" cosplay tournament!{w=0.6} Even better!)"
    g4 "(Is it even cosplay if they're naked?)"
    call cho_main("And with new contestants every month! You've got to do this, Sir!","smile","base","base","mid")
    m "I'll think about it..."

    m "Now tell me, how come you two ended up together?"
    call cho_main("Oh. Well...","soft","base","base","down")
    call cho_main("I have this thing for...{w=0.5} athletes.","horny","base","base","down")
    call cho_main("Cedric was the representative champion of our school, so of course I had to date him.","horny","base","sad","down")
    m "Of course..."
    m "(She's into athletes, so so...)"
    g4 "(You should see me, girl. I'm shredded!)"
    m "(Too bad you can only see the body of that wrinkly old geezer...)"
    m "(Maybe there's like a steroid spell...)"
    g4 "{size=-4}Plexus maximus!{/size}"
    call cho_main("Did you say something?","soft","base","raised","mid")
    m "Oh, it was nothing... go on."

    call cho_main("Anyway, Cedric even put his life at risk during the whole thing.","open","base","base","R")
    m "Oh you poor, poor thing..."
    m "I can see why you didn't want to mention him before then..."
    call cho_main("Why?","soft","narrow","raised","mid")
    m "He surely will be missed."
    call cho_main("Sir?","angry","narrow","base","mid")
    m "Died just the way he lived,...{w} as a plot device."
    call cho_main("Sir, Cedric isn't dead.","open","angry","angry","mid")
    m "Oh...{w} he's not?"
    call cho_main("No!","annoyed","narrow","angry","mid")
    m "I could've sworn I read that somewhere..."
    m "Are you sure he's still around?{w} What if he \"did\" die, but then he returned from the dead?"
    g4 "For all you know he could be a vampire!"
    call cho_main("Sir, you're talking nonsense...","annoyed","angry","angry","R")
    call cho_main("Please don't joke about your student like that. It's so unlike you...","open","closed","base","mid")
    call cho_main("He's one of your bests! The best student \"Hufflepuff\" has ever seen!","open","base","base","mid")
    m "A \"Hufflepuff\"? Well, that explains everything..."
    m "If he's such an exceptionally great student, then why aren't you two still together?"
    call cho_main("Things didn't work out, naturally...","open","base","raised","R")
    call cho_main("The tourney ended, and he didn't win, so...","soft","base","raised","down")
    m "So you two broke up?... Because he didn't win?"
    call cho_main("That was one of the reasons...","soft","base","base","downR")
    call cho_main("There is also the fact that he's on the \"Hufflepuff Quidditch team\", as their Seeker.","open","base","base","mid")
    call cho_main("It's our last shot at winning the Quidditch house cup, for the both of us.","angry","base","base","down")
    call cho_main("We'd constantly be at each other's throats.","soft","narrow","angry","mid")
    g4 "Intriguing!"
    m "You are missing out, girl..." # Small text
    g9 "{size=-4}Hatesex is the best!{/size}" # Small text
    call cho_main("I didn't quite hear that, Sir.","base","base","base","mid")
    m "Who else did you do it with?"
    call cho_main("Do it with?","soft","narrow","raised","mid") # Shocked
    m "Smooshing, kissing, snogging,...{w} whatever you call it nowadays..."
    call cho_main("With all due respect, Professor, it's very odd that you'd ask me about those sort of things...","open","closed","base","mid")
    call cho_main("But,... you \"are\" helping me.{w} So I guess I owe you that much...","annoyed","base","base","R")
    g9 "That's what I wanted to hear."

    # Fleur
    call cho_main("Well, Cedric wasn't the only one I was with during the year of the tourney...","open","base","raised","down")
    g9 "Is that so...{w} feel free to elaborate!"
    call cho_main("I was sort of dating somebody else....","quiver","base","sad","downR")
    call cho_main("At the same time.","horny","base","sad","R") # Embarrassed
    m "No{w} way!"
    g4 "You were cheating on that Hufflepuffer?"
    call cho_main("I wouldn't call it cheating, Professor. It wasn't even that serious with Cedric to begin with.","annoyed","narrow","base","mid")
    call cho_main("I had a unique opportunity that's all...","soft","base","base","R")
    call cho_main("One of those \"no strings attached\" kind of things... Trying out new stuff...","smile","base","base","L")
    m "Like what?"
    call cho_main("Dating a girl, for example.","base","narrow","base","mid")
    g9 "(Finally this gets interesting!)"
    call cho_main("She was one of the students from Beauxbaton.","soft","base","base","downR")
    m "(...)"
    call cho_main("A French girl.","soft","base","base","down")
    g9 "And I hope you also frenched that french girl!"
    call cho_main("Among other things...","angry","closed","sad","mid") # Super embarrassed
    call cho_main("(Why am I telling him this?)","horny","narrow","sad","R")
    g9 "And who was it?"
    call cho_main("Fleur Delacour.{w} She was also a champion at the tourney.","soft","base","sad","mid")
    g4 "I'm in shock!"

    # Viktor
    call cho_main("Then there also was Viktor Crum who-","open","base","base","R")
    with hpunch
    g4 "Slow down, girl! I'm still not over the fact that you made out with a girl!"
    call cho_main("","annoyed","narrow","base","mid")

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_chang
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call bld

        "-Participate in the conversation-":
            $ masturbating = False

    g9 "I want to hear everything!"

    call cho_main("I'm sorry, Sir. It's just that...","open","closed","raised","mid")

    if daytime:
        call cho_main("I'm really late for classes. May we postpone this talk to some other time?","soft","narrow","sad","R")
    else:
        call cho_main("It's getting really late. May we postpone this talk to some other time?","soft","narrow","sad","R")

    if masturbating:
        g4 "What? Please don't go now. I've only just started!"
        call cho_main("Started with what, [cho_genie_name]?","annoyed","narrow","angry","mid")
        g4 "I'll give you 10 house points if you stay!{w=0.8} Just a tiny bit longer!"
        call cho_main("And what makes you believe that I'd agree to such a thing? Getting rewarded with points for doing nothing?","open","closed","base","mid")
        call cho_main("Earning house points in such a way is despicable, and it would be unfair towards the other school houses, as well as my fellow students...","open","narrow","base","mid")
        call cho_main("","annoyed","narrow","angry","mid")
        g4 "Fifty points?"
        call cho_main("I have to go now, Sir.","soft","closed","raised","mid")
        m "(Fuck me...)"

        call gen_chibi("sit_behind_desk")
        with d3
        pause.8

        call cho_main("Until next time!","base","narrow","base","mid")

    else:
        m "Okay, girl. You may leave..."
        call cho_main("Thank you, Sir.","base","base","base","down")
        call cho_main("See you next time.","smile","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "(...)"
    if masturbating:
        m "Well, I got blue-balled..."
        m "Feel like I've deserved it..."

    return


label cc_pf_talk_T1_E2: # Complete
    g9 "Get closer, [cho_name]..."
    call cho_main("...","annoyed","base","base","down")

    call cho_chibi("stand","desk","base")

    call play_music("chipper_doodle")
    call cho_main("","annoyed","narrow","angry","mid",xpos="mid",ypos="base",trans="fade")
    call ctc

    call cho_main("Another talk, Professor?","soft","narrow","angry","mid")
    call cho_main("Are we going to discuss my previous relationships again?","open","narrow","base","R")
    g9 "I don't know.{w} Would you like to?"
    call cho_main("I'd rather not.","soft","narrow","angry","mid")
    m "Tell me about yourself then."
    call cho_main("Of course, [cho_genie_name].","smile","base","base","mid")
    call cho_main("We did a couple more Quidditch session yesterday.{w} To get ready for our big game against \"Hufflepuff\".","open","narrow","base","mid")
    call cho_main("Our team really believes that we have a chance to win this time!{w} They got a huge boost of confidence after I've told'em that the great \"Albus Dumbledore\" would be training us himself!","smile","base","base","mid")
    m "Are you getting along with your team well?"
    call cho_main("I'd say so.{w} But there has been a time when...","soft","base","base","mid")
    call cho_main("Let's just say that it has been difficult for me at first. After all Quidditch is largely dominated by men...","open","narrow","sad","down")
    call cho_main("Getting accepted into our Quidditch team was a challenge. I really had to prove I was worth it.","angry","narrow","sad","mid")
    g9 "And how exactly did you manage that? Mind spilling the beans?"
    call cho_main("Through diligence, expertise, and determination!","open","closed","base","mid")
    m "(...)"
    m "I was sort of expecting something else entirely but,... you do you..."
    call cho_main("And as you can see it did work out in my favour, Sir.","open","base","base","mid")
    call cho_main("Very few teams have allowed a female player into their ranks over the past years.","open","narrow","angry","mid")
    call cho_main("And I've been the only female seeker at this school in over half a century.{w} Can you even believe that, [cho_genie_name]?","open","wide","base","mid")
    m "(Half a century? That's like a coffee break for me girl...)"
    call cho_main("I don't want to brag, [cho_genie_name], but the role of a seeker is \"the\" most important position in a team by far!","smile","narrow","base","mid")
    call cho_main("If you don't have a good seeker, you have no chance of winning!","soft","closed","base","mid")
    m "Which is why you need my help so badly..."
    m "Because you are great at it..."
    call cho_main("That we're losing is neither my fault, nor my team's, [cho_genie_name]!","annoyed","base","angry","mid")
    m "So who's is it then?"
    call cho_main("The enemy team's, obviously!","soft","narrow","angry","mid")
    call cho_main("They are cheating! And they have done so for years!","open","narrow","angry","R")
    call cho_main("This is my last chance! And I'm growing more and more desperate with my situation...","angry","narrow","angry","mid")
    m "(...)"

    menu:
        "-Jerk off while she is talking-":
            hide screen cho_chang
            hide screen bld1
            with d5
            pause.5

            call gen_chibi("jerking_off_behind_desk")
            with d3
            pause.8

            $ cho_jerk_off_counter += 1
            $ masturbating = True

        "-Participate in the conversation-":
            $ masturbating = False

    call cho_main("Ever since I was a little girl Quidditch has been my dream...","quiver","narrow","sad","down")
    call cho_main("[cho_genie_name], can you imagine how \"hard\" it was for me?","soft","narrow","sad","mid")
    if masturbating:
        g4 "{size=-4}Yes, yes... It's so hard for you, you little slut!!!{/size}"
    call cho_main("How difficult it was for me at first?","open","narrow","sad","R")
    call cho_main("Getting accepted?","soft","closed","sad","mid")
    if masturbating:
        g4 "{size=-4}I'd accept your ass on my cock if you're in such a need for acceptance, you whore!{/size}"
    call cho_main("I'm the only female in my team. Constantly surrounded by other men...","soft","base","sad","down")
    if masturbating:
        g4 "{size=-4}Yes! Yes! And they all would like to have their way with you!{/size}"
    else:
        m "(Quite a sausage-party this Quidditch I have to admit.)"
        g4 "(Maybe telling Hermione off was a bad idea after all...{w} An \"all female\" team would be more fun to watch...)"
    call cho_main("I can constantly feel their gazes behind my back...","angry","base","sad","down")
    call cho_main("My own team, [cho_genie_name]!{w} They treat me like the plague!","upset","base","sad","mid")
    call cho_main("They ignore me during classes...","soft","closed","base","mid")
    call cho_main("When we're in our dormitories they are going out of their way to not cross paths with me...","annoyed","narrow","angry","R")
    call cho_main("And in the showers they're scared to even look at me!","angry","angry","angry","mid")
    if masturbating:
        g4 "{size=-4}Yes, yes!{w} Even in the showers you who-{/size}"
        with hpunch
        m "Wait a bloody minute!{w} You shower \"with\" your team?"
    else:
        m "The showers?{w} You shower \"with\" your team?"
    call cho_main("Of course, [cho_genie_name]. It was after my request, after all.","soft","base","raised","mid")
    g4 "No kidding?"
    call cho_main("They shouldn't exclude me from team activities just because I'm a girl.","open","base","base","R")
    call cho_main("It makes absolutely no difference!","base","base","base","mid")
    if masturbating:
        g4 "You are naked with them? In the showers?"
    else:
        m "Just to be clear. You are naked with them, in the shower."
    call cho_main("Of course we're all naked, [cho_genie_name]!","soft","base","angry","mid")
    call cho_main("Why would I take showers with my clothes still on?","soft","closed","base","mid")

    # Genie cums.
    if masturbating:
        g4 "{size=-4}You exhibitionistic slut!{/size}"
        g4 "*Argh* {size=-4}Here it comes!{/size}"

        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call bld
        g4 "*heavy breathing* {size=-4}Take it!{/size}"

        call cum_block
        call cho_main("","base","narrow","raised","mid")
        g4 "*Argh!* {size=-4}Shower in this, you slut!{/size}"

        call cum_block
        call cho_main("[cho_genie_name], are you alright?","quiver","wide","base","mid")
        call cho_main("You're sweating and breathing quite heavily...","quiver","base","base","mid")

        call gen_chibi("came_on_desk")
        with d3
        pause.8

        call cho_main("Shall I get Madam Pomfrey to check on yo-","soft","narrow","base","mid")
        g4 "No, no! I'm..."
        m "I'm done.{w} Lets get back to the topic."
        call cho_main("Which was?","open","wink","raised","mid")
        m "You taking a shower with your \"teammates\"..."
        call cho_main("(...)","annoyed","narrow","angry","mid") # Annoyed

    m "Don't you think, the fact that they've seen you naked hasn't affected any of their actions?"
    call cho_main("Why would it, [cho_genie_name]? We're all adults here...","soft","closed","base","mid")
    m "Maybe that's your response to it, girl."
    call cho_main("","annoyed","narrow","angry","mid")
    g9 "Maybe your \"teammates\" aren't as... \"mature\" as you."
    call cho_main("I've known my team for years.{w} We're all professionals!","soft","narrow","base","mid")
    m "Let me ask you a question..."
    m "In the showers,{w} do they all have their backs turned towards you?"
    call cho_main("I don't know. Maybe they uhm-...","open","base","base","mid")
    call cho_main("!!!","scream","wide","raised","mid") # Cho remembers something?!
    g9 "Yes?"
    g9 "What is it?"
    call cho_main("May I... May I leave, [cho_genie_name]?","quiver","closed","base","mid")
    g9 "Don't want to tell me?"
    call cho_main("No...","quiver","closed","sad","mid")
    m "Fine...{w} you may leave..."
    call cho_main("Thank you, [cho_genie_name].","soft","wink","sad","mid")

    # Cho very slowly walks out of your office...
    call cho_walk(action="leave", speed=3)

    call bld
    m "(...)"
    g9 "(That just gave me an idea!)"
    stop music fadeout 1.0

    $ cho_requests_unlocked = True
    call popup("You can now buy \"Public Requests\" from Cho! (They are optional to her training.)", "Congratulations!", "interface/icons/head/head_cho_1.png")

    return


label cc_pf_talk_T1_E3: # Incomplete. Not posed.
    m "Care to tell me more about Quidditch?"
    cho "Of course, [cho_genie_name].{w} I always love talking about Quidditch!"
    m "Yeah, yeah... I know."
    m "First, come closer. Let me have a good look at you!"
    cho "Yes, Sir."

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    cho "Anything specific you'd like to know?"
    m "Yes. Let's talk some more about Diggory..."
    g9 "Your ex-boyfriend."
    cho "{size=-4}I knew I shouldn't have told him...{/size}"
    cho "Why do you have to keep bringing that up, Sir? What's past is in the past..."
    m "I believe otherwise..."
    g4 "Did you already forget that he's our enemy?!"
    m "Your relationship with him is of the utmost importance right now!"
    m "I need to know every tiny bit of detail about the two of you."
    g4 "What you were doing when you were together. How often you made out with him. The exact locations where he touched you..."
    cho "What?!"
    m "As well as his sexual preferences. Secret fetishes he might have. Everything!"
    cho "I will not tell you any of those things!"
    g4 "Didn't you say you wanted to win?"
    cho "I did, Sir... But..."
    m "What did he like about you? Tell me! Maybe we can use it to our advantage!"
    cho "Okay, [cho_genie_name].{w} I'm willing to cooperate..."
    cho "Cedric was never too interested in me. His mind was always somewhere else. Drifting off..."
    cho "He always had this dead look in his eyes. Except for when-"
    cho "(...)"
    m "Yes? Go on..."
    cho "He had this weird, unhealthy obsession with my panties, Sir."

    if huffl_matches_won == 0:
        m "A panties obsession? So so..."
    else:
        g9 "Ha! I knew it!"

    cho "It was almost creepy how often he tried to look up my skirt."
    cho "And he’d always walk behind me when we went up the stairs, to get a better view I bet..."
    m "Did you ever show them to him?"
    cho "My panties?"
    m "No, your good manners... Yes, your panties!"
    cho "Why would I have wanted to? We weren’t that close!"
    m "So you were not close enough for a healthy relationship?"
    cho "What?"
    m "What kind of girl doesn't show her panties to her beloved?"
    cho "That’s just ridiculous..."

    if huffl_matches_won == 0:
        m "But, that made me think..."
        m "If he’s as obsessed with panties as you say, why don’t we use that information to our advantage?"
        cho "Like how?"
        m "We use them as a distraction!"
        m "Now we only have to find out how to show them off properly during the game."
        cho "I have to say I don’t like this notion one bit. But it might be worth a try..."
    else:
        m "Well, it worked."
        m "Beating him at Quayditch was almost too easy!"
        cho "Quidditch, Sir..."
        m "All we had to do was put some good-old panties in front of his face..."
        g4 "And he was like a wild goat chasing after them!"
        cho "A goat?"
        m "Yes. Don't you have those here?"
        cho "I'm still surprised how well that worked out, if I'm honest."
        m "You’re welcome."

    # Add ending

    return



### Tier 2 (pre Slytherin) ###

label cc_pf_talk_T2_E1: # Complete. Needs review. Not posed.
    m "Miss Chang, it's time we have a little chat again!"
    m "Please come a bit closer..."
    call cho_main("Yes, Sir.","base","base","base","mid")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("","base","base","base","mid", xpos="mid", ypos="base", trans="fade")
    m "Tell me, how have you been?"
    g9 "I bet a lot has changed for you after your big win!"
    call cho_main("More or less...","soft","base","raised","mid")
    call cho_main("School has been rather uneventful the past couple of days.","soft","base","base","R")
    call cho_main("That is, if constantly getting bullied is the new norm at this school...","soft","narrow","angry","mid")
    m "Bullied by whom?"
    call cho_main("The Slytherin Quidditch team. They've been total dicks lately...","annoyed","narrow","angry","R")
    m "You don't say.{w} Why is that?"
    call cho_main("Because they are scared of us, I wager...","soft","narrow","angry","downR")

    call cho_main("We'll be playing against them next.","annoyed","narrow","base","R")
    call cho_main("And of course they have to behave like the absolute worst!","soft","narrow","angry","mid")
    call cho_main("They deserve to be publicly disgraced in front of the whole school! The whole lot of them!","scream","closed","angry","mid", trans="hpunch")
    call cho_main("I'll make sure of it, [cho_genie_name]!{w} The Slytherin team will lose!","angry","narrow","angry","mid")
    g9 "(And I'll win my bet with Snape even sooner! Sweet!)"
    m "Anything you can tell me about them?{w} Are they better than Hufflepuff?"
    call cho_main("They are, by quite a bit.","annoyed","base","base","mid")
    call cho_main("However, Hufflepuff only had one really good player. Which was Cedric.","soft","base","base","R")
    call cho_main("Slytherin on the other hand, they are almost unbeatable.{w} They might even be better than Gryffindor!","angry","wide","base","mid")
    m "You don't say. So why are they next and not Gryffindor?"
    call cho_main("Because of their seeker, he's...{w} so,{w} so bad!","soft","narrow","base","R")
    m "Who is?"
    call cho_main("Draco Malfoy, Sir.","soft","closed","base","mid")
    m "(The cocky fella! Snape mentioned him before...)"
    call cho_main("They've been continuously harassing my team...","annoyed","narrow","angry","R")
    call cho_main("Well, mostly me actually.","angry","narrow","base","downR") # Embarrassed

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_chang
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call bld
            m "(Just to make this clear, I'm not getting off because I like the thought that she's getting bullied...)"
            call nar("Right...")
            g4 "I hope you fought back those bullies?"
            call cho_main("Of course, [cho_genie_name]!","base","base","base","mid")

        "-Participate in the conversation-":
            $ masturbating = False
            m "(No, I need to focus!)"
            m "So,... would you like to report them?"
            call cho_main("No, Sir.","soft","closed","base","mid")
            m "No?"

    call cho_main("I do not endorse their behavior, Sir. And I hope no other student has to share the same harassment that I received.","soft","narrow","angry","mid")
    call cho_main("Unless maybe Granger...","annoyed","narrow","angry","R") # Small text.
    call cho_main("But{w}, watching them succumb to me has been rather fun...","base","narrow","angry","mid")
    m "Succumb to you?"
    call cho_main("Yes. They're so desperately trying to embarrass me. To make me doubt myself before the big game...","smile","narrow","angry","mid")

    if masturbating:
        g4 "Those asshole bullies... Show them who's boss!"
    else:
        g9 "And a strong, independent woman like yourself would never be intimidated by puny Slytherins!"
        call cho_main("Of course not, Sir.","soft","closed","base","mid")
        g4 "I'm so proud!"

    call cho_main("After all I'm only a small girl, and they are a group of strong, ruthless alpha males!","soft","base","sad","R")

    call cho_main("Their attempts are pathetic!","angry","narrow","angry","mid", trans="hpunch")
    call cho_main("Trying to lift my skirt with first-year spells...","soft","narrow","angry","R")
    call cho_main("Stealing my underwear while I'm taking a shower after practice...","angry","narrow","angry","downR")
    if masturbating:
        g4 "*Argh!* Dirty panties muggers!"
    call cho_main("They even had the audaciousness to write \"Cho, the Ravenclaw ho\" on the blackboard during divination class...","soft","narrow","angry","mid")
    if masturbating:
        g4 "They have seen your future, you whore!"
    call cho_main("Half the class saw it before I could get there.{w} Not that I care much about it...","annoyed","narrow","base","R")
    call cho_main("If I'm honest, I'm surprised they could even spell my name correctly...","soft","narrow","angry","mid")
    if masturbating:
        m "*Fap* *Fap* *Fap* *Fap*..."
    call cho_main("They think they can intimidate me. But that's where they are mistaken!","angry","narrow","angry","down")

    if masturbating:
        call cho_main("They should be scared of me, [cho_genie_name]!","soft","narrow","angry","mid")
        g4 "Yes! Show them, you slut!"
        call cho_main("Of what \"I'm\" capable off!","angry","narrow","angry","mid")
        g4 "*Argh!* I'm getting close!"
        cho  "Scared of what's about to come!","angry","angry","angry","mid")

        # Genie cums.
        g4 "Yes! Yes! It's coming!"

        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        call bld
        g4 "*Argh!* {size=-4}Take it!{/size}"

        call cum_block
        call cho_main("","base","narrow","raised","mid")

        call gen_chibi("came_on_desk")
        with d3
        pause.8

        m "(*Phewwww*...)"
        m "(That was nice.)"
        call cho_main("Are you feeling well, Sir?","open","narrow","base","mid")
        g9 "Never felt better!"
        call cho_main("That's good to hear.","smile","base","base","mid")

    m "I'm glad you aren't letting yourself get oppressed by those Slytherins."
    call cho_main("Not in a million years!","base","narrow","base","mid")
    m "Admirable."

    m "Anything else you could tell me about their team? Anything that could help us?"
    m "Did you maybe fool around with their seeker as well?"
    call cho_main("Malfoy?","soft","wide","base","mid") # Shocked
    call cho_main("*Tzzzz* I'd never surround myself with Slytherin scum!","angry","closed","angry","mid")
    call cho_main("","annoyed","narrow","angry","mid")
    m "I guess you and Granger have at least some things in common..."
    call cho_main("His daddy bought their whole team new brooms, which is the only reason they've even let him in.","soft","narrow","raised","mid")
    m "His \"daddy\"?"
    call cho_main("His father, Sir.","soft","closed","angry","mid")
    m "Oh. I thought you might be talking about a different \"daddy\"."
    call cho_main("Very funny, [cho_genie_name]...","annoyed","base","angry","R")
    call cho_main("If you don't mind, Sir.","soft","closed","base","mid")

    if daytime:
        call cho_main("Classes are about to start, and I'm already late for them...","soft","base","base","R")
        call cho_main("I hope it would be okay if I leave?","annoyed","base","sad","mid")
    else:
        call cho_main("It's getting late and I have to go and get some sleep...","soft","base","base","R")
        call cho_main("I hope you don't mind, Sir?","annoyed","base","sad","mid")

    m "Not at all. You may go now."
    call cho_main("Thank you, Sir.","smile","base","base","mid")
    call cho_main("Until next time...","base","narrow","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.5)

    return


label cc_pf_talk_T2_E2: # Complete. Needs review. Not posed.
    m "Would you mind if we had another chat?"
    call cho_main("Of course not, [cho_genie_name]!","smile","base","base","mid")
    m "Come closer..."

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("","base","base","base","R", xpos="mid", ypos="base", trans="fade")
    m "How's school? Have anything to tell me?"
    call cho_main("Quite a bit, Sir!","smile","base","base","mid")
    call cho_main("I feel like people have shown me more affection even since our game against Hufflepuff.","base","closed","base","mid")
    m "You don't say..."

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_chang
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call bld
            g4 "*Agh!* Go on!"
            call cho_main("What?{w} Oh, of course, [cho_genie_name]!","soft","wide","base","mid")
            call cho_main("I'm sorry. I had my head in the clouds there for a second, Sir.","soft","base","sad","downR")

        "-Participate in the conversation-":
            $ masturbating = False
            m "Do you have any idea why that might be?"
            call cho_main("Because of our win, of course!","base","closed","base","mid")
            m "And it had nothing to do with the fact that half the school got to see your panties?"
            call cho_main("No! Of course not!","soft","narrow","angry","mid")
            call cho_main("Please don't try to diminish my achievement, Sir!","annoyed","narrow","base","R")

    call cho_main("It's like I'm a celebrity now! I'm getting so much attention!","soft","base","base","R")
    call cho_main("It never happened that Ravenclaw won a game. And I made that possible!","smile","base","base","mid")
    if masturbating:
        g4 "And soon you'll be on your knees thanking me for it!"
    else:
        m "Hey! Don't you forget about me!"
        m "Where would you be without the great Dooblydore..."
        call cho_main("Of course, Sir! Sorry, Sir!","angry","closed","sad","mid")

        menu:
            m "Maybe it wouldn't be such a bad idea to..."
            "-Jerk off while she's talking-":
                $ cho_jerk_off_counter += 1
                $ masturbating = True

                hide screen cho_chang
                call nar(">You reach under the desk and grab your cock...")

                call gen_chibi("jerking_behind_desk")
                with d3
                pause.8

                call bld
                m "Please, don't let me interrupt your thought..."
                g9 "I'd like to hear more!"

            "-Participate in the conversation-":
                $ masturbating = False
                m "(No, I need to focus!)"
                m "Please, don't let me interrupt your thought..."
                m "Continue..."

    call cho_main("Of course, Sir.","base","base","base","mid")
    call cho_main("It's fun receiving all of the boys attention! And seeing how jealous it makes all of the girls!","soft","base","base","mid")
    call cho_main("Especially Granger!","smile","narrow","base","mid")
    if masturbating:
        g4 "Yes, the Gryffindor whore!"
    call cho_main("You should have seen her face, [cho_genie_name]. She's so angry at me! I love it!","smile","closed","base","mid")
    call cho_main("She can't even bear to look at me anymore.","soft","narrow","angry","mid")
    call cho_main("You should know, for whatever reason, almost all of Hufflepuff faults her for helping Ravenclaw secure the win!","soft","base","base","R")
    call cho_main("She announced several times that Hufflepuff was leading in points, when they actually weren't!","smile","narrow","base","R")
    call cho_main("Which resulted in Hufflepuff playing far more defensively, when they should have been aggressive!","smile","narrow","angry","mid")
    if masturbating:
        g4 "Oh you are one of those girls! I like going aggressive!"
    call cho_main("I caught the Snitch at just the right time!{w} If Hufflepuff had gone too far in the lead, we would have lost!","base","narrow","base","mid")
    call cho_main("I really need to thank Granger the next time I see her. I owe her a great deal...","soft","narrow","base","R")
    if masturbating:
        g4 "I'd love to watch you \"thank her\"!"
        call cho_main("Maybe I'll do something fun with her the next time I see her...","base","narrow","base","R")
        call cho_main("Do something that would rile her up even more!","smile","narrow","angry","downR")
    else:
        m "Yeah? How would you \"thank her\"?"
        call cho_main("I don't know. Maybe something that would rile her up even more...","annoyed","base","base","downR")
    call cho_main("Like a kiss on her cheek, or an uncomfortably long hug!","soft","narrow","base","mid")
    call cho_main("Or I'll do something more sinister! Something she'd never expect!","smile","narrow","base","R")
    g4 "*Argh!*"
    call cho_main("Give her a proper kiss on the lips, perhaps?","base","narrow","base","R")
    call cho_main("Yes! I bet a prude like her would be \"so\" shocked by that! I might even be her first!","smile","wide","angry","downR")

    # Forced to jerk off.
    if masturbating:
        g4 "Yes! You fucking sluts!"
    else:
        g4 "(Fuck it, this is too much!)"

        menu:
            "Jerk off":
                $ masturbating = True
                g4 "Please, continue!"

    call cho_main("Just thinking about her puffy pink lips...","soft","narrow","sad","down")
    g4 "Yes! Yes!"
    call cho_main("I should make her choke on my tongue, whether she likes it or not...","annoyed","narrow","angry","down")
    g4 "Yes! That's fucking hot!"
    call cho_main("Push her against a wall and force it into that bitch's mouth!","angry","angry","angry","down")
    g4 "*Argh!* You fucking sluts!"
    call cho_main("Pull her vest over those stupidly large breasts...","upset","closed","angry","mid")
    call cho_main("And embarrass her in front of the whole class!","soft","base","base","up")
    call cho_main("Show everyone her ridiculous cow tits!","angry","base","angry","R") # Angry
    g4 "Yes!!! I'm almost there!"
    call cho_main("She deserves it...","angry","closed","angry","mid")
    call cho_main("That know it all, pretentious little bitch!","soft","narrow","angry","downR")

    # Genie cums.
    g4 "Yes, yes! You nasty slut!"

    call cum_block
    call gen_chibi("cumming_behind_desk")
    with d3
    pause.8

    call bld
    g4 "*Argh!* {size=-4}Take it!{/size}"
    call cho_main("Oh, I'm so sorry, Sir.","soft","narrow","base","mid")
    call cho_main("I forgot I was talking to you for a second!","angry","closed","sad","mid")

    call cum_block
    g4 "*Argh* {size=-4}You lesbian slut!{/size}"
    call cho_main("I hope you didn't hear any of it! I would never do-","soft","narrow","sad","mid")

    call cum_block
    call cho_main("Sir?!","base","narrow","raised","mid")

    call cho_main("[cho_genie_name]! What the bloody hell are you doing?!","scream","wide","base","mid", trans="hpunch") # Scream
    call cho_main("","angry","narrow","angry","mid")
    m "(Oh no!)"
    g4 "(I'm busted!)"

    # Genie stops.
    hide screen bld1
    with d3
    pause.2

    call gen_chibi("came_on_desk")
    pause.8

    g4 "Nothing, I was just-"
    call cho_main("Don't tell me you were...","soft","wide","base","mid")
    g4 "I was merely scratching my leg!"
    call cho_main("Don't lie to me... I know exactly what you were doing!","angry","closed","angry","mid")
    call cho_main("You were touching yourself!","scream","closed","angry","mid", trans="hpunch") # Scream
    call cho_main("","angry","narrow","angry","mid")
    g4 "Not so loud! People might hear you!"
    call cho_main("Why would you think I care?!","soft","narrow","angry","L")
    call cho_main("You were wanking off!","soft","wide","base","down")
    m "No I wasn't..."
    call cho_main("In front of your own student!","soft","wide","sad","mid")
    m "(...)"
    m "Stop making a big deal out of it, would you?"
    call cho_main("So you're admitting that you did it!","angry","angry","angry","mid")
    m "Fine... I don't care at this point..."
    call cho_main("That's disgusting!","soft","narrow","base","mid")
    m "You're making an even bigger fuzz about it than Hermione..."
    call cho_main("Good for her!","angry","closed","base","mid")
    call cho_main("Maybe you should call her up here to clean up your mess as well!","soft","narrow","base","mid")
    call cho_main("And lick it all up!{w} I bet she'd love that!!!","angry","narrow","angry","mid")
    m "(...)"
    call cho_main("I'm leaving.","annoyed","narrow","base","mid")
    call cho_main("Have a nice day, [cho_genie_name]!","angry","closed","angry","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.5)

    call bld
    m "(I really did make a mess...)"
    m "(Maybe I should get Hermione to clean it up for me?)"
    g9 "(With her mouth!)"
    m "(..........)"
    m "(And I'm hard again...{w} Maybe some other time...)"

    $ cho_mood += 9

    return


label cc_pf_talk_T2_E3: # Incomplete. Not posed.
    g9 "[cho_name], how is my favourite Quidditch player doing today?"
    call cho_main("Me?","soft","base","raised","mid")
    m "I don't see anyone else in here besides the bird..."
    g9 "Come a bit closed, would you."
    call cho_main("Of course...","annoyed","base","base","R")

    call cho_walk(xpos="desk", ypos="base", speed=1.6)

    call cho_main("","annoyed", face="neutral", xpos="mid", ypos="base", trans="fade")
    g9 "So. How is school life?"
    m "I need to stay \"on top\" of all the latest \"hot goss\"..."
    call cho_main("Sir, I don't tend to pay attention to that sort of stuff.","soft","closed","base","mid")
    m "You must have at least heard something raunchy here at the school?"
    call cho_main("*Uhm*...{w} well...","annoyed","base","base","R")

    menu:
        "-Jerk off while she's talking-":
            $ cho_jerk_off_counter += 1
            $ masturbating = True

            hide screen cho_chang
            call nar(">You reach under the desk and grab your cock...")

            call gen_chibi("jerking_behind_desk")
            with d3
            pause.8

            call bld
            m "You don't mind if I..."
            call cho_main("Mind what?!","soft","wink","base","mid")
            call cho_main("!!!","upset","wide","base","mid") # Shocked
            m "I have needs, girl."
            call cho_main("Gross!!!","angry","closed","angry","mid")
            call cho_main("Well then, I'd suggest you sort those needs on your own!","soft","narrow","angry","R")
            call cho_main("Without me...","soft","narrow","angry","mid")
            m "What a Bummer...{w} Last time you were such a great aid..."
            call cho_main("What?! When did I ever help you with that?","soft","wide","base","mid")
            g9 "When you told me about that little fantasy you had with Granger!"
            call cho_main("You shouldn't have payed attention to any of that!","angry","closed","sad","mid")
            g9 "But I did!"
            m "..."
            m "I could just tell Hermione that you're into her, you know..."
            call cho_main("I am so not into her!","soft","narrow","angry","R")
            call cho_main("(...)","annoyed","narrow","sad","R") # Embarrassed
            g9 "Yes you are. Don't you dare lie to me... Or yourself for that matter."
            call cho_main("(...)","angry","narrow","sad","downR")
            m "So..."
            m "Will you honour the deal and aid me or what?"
            call cho_main("Fine...{w} If you can't help yourself.","annoyed","narrow","angry","mid")
            g9 "Great!"
            g9 "Pretend like I'm not even there!"
            call cho_main("I more likely will be pretending that \"I'm\" not here...","soft","closed","base","mid") # Small text

        "-Participate in the conversation-":
            $ masturbating = False
            m "(Seems like I'm not feeling the need to jack off today...)"
            m "(Might as well pay attention for once.)"
            m "Very well then..."

    menu:
        m "Tell me some more about..."

        "\"Granger\"":
            call cho_main("What more is there to tell?","annoyed","narrow","angry","R")
            call cho_main("She's a hypocrite and a slut...{w} I hate her...","soft","closed","base","mid")
            call cho_main("And if you could make her die of embarrassment, I'd be more than thankful for it...","soft","narrow","angry","mid")
            g9 "Embarrass her? How?"
            g9 "Share some of your ideas with me! I'd love to hear them!"
            call cho_main("Very well...","soft","closed","base","mid")
            call cho_main("(...)","annoyed","base","base","R") # Thinks
            call cho_main("(...........)","annoyed","narrow","angry","R") # Thinks
            if masturbating:
                g4 "Please?!"
            else:
                m "Anything?"
            call cho_main("I know!{w} Strip her down, and put her in a pillory!{w} In the middle of the Quidditch pitch!","soft","wide","base","mid")
            g9 "Naughty! I like it!"
            call cho_main("And let the entire school watch her as she's getting pounded by a horde of centaurs!!!","angry","angry","angry","mid")

            if masturbating:
                g4 "*Argh!*{w} What the hell?"
                call cho_main("While there are bludgers flying around, hitting her disgusting udders...","soft","narrow","angry","mid")
                g4 "That sounds really painful!"
                g4 "*Fap* *Fap* *Fap!*"
                call cho_main("Maybe another centaur takes her from the front...","soft","narrow","angry","R")
                g4 "*Agh!* Shit!{w} I won't last long if she continues like this!"
                call cho_main("And once those two are done breeding her, they trade places with another batch.","angry","angry","angry","R")
                g4 "*Ahh* This is getting too crazy!"
                call cho_main("Or even better, let some trolls have their way with her!{w} Let them rip her apart!","angry","wide","angry","downR")
                g4 "*Fuck!* Come on! Unload! Before it's too late!!!"

                # Genie cums.

                call cum_block
                call gen_chibi("cumming_behind_desk")
                with d3
                pause.8

                call bld
                g4 "Yes! Here it comes!"

                call cum_block
                g4 "*Agh!* Here comes another!"

                call cum_block
                m "*Phew*... That was close!"

                # Genie stops.
                hide screen bld1
                with d3
                pause.2

                call gen_chibi("came_on_desk")
                pause.8

                call cho_main("And why don't we put a large bucket under her so when they-","soft","closed","base","mid")
                g4 "Stop! No more!"
                g4 "I've heard enough!"
                call cho_main("(...)","annoyed","narrow","angry","mid")

                g4 "That was...{w} Very good."
                call cho_main("Are we done here, Sir?","soft","narrow","angry","mid")

            else:
                m "(...)"
                call cho_main("While there are bludgers flying around, hitting her disgusting udders...","soft","narrow","angry","downR")
                m "*Uhm*..."
                call cho_main("What?!","angry","angry","angry","mid", trans="hpunch") # Angry
                m "Don't you think that's a bit extreme?"
                call cho_main("Why? For putting Granger in her natural habitat?","annoyed","narrow","angry","mid")
                call cho_main("Enclosed on a vast grassy field...","soft","closed","base","mid")
                call cho_main("Getting bred by a horde of bulls!","soft","narrow","base","mid")
                call cho_main("A cow like her would love it...","annoyed","narrow","base","R")
                m "You seem very interested in the thought of it."
                g9 "From my perspective it appears that the worse you talk about her... The more attracted to her you truly are!"
                call cho_main("Rubbish...","soft","narrow","base","R")
                g9 "Girl, you are in denial!"
                call cho_main("I am not!","angry","closed","angry","mid")
                call cho_main("Sir are we done here?","soft","narrow","angry","mid")

            if daytime:
                call cho_main("I'm late for classes.","soft","narrow","angry","R")
            else:
                call cho_main("I need to get some sleep.","soft","narrow","angry","R")

            call cho_main("","annoyed","narrow","angry","mid")
            m "*Uhm*... Sure..."
            m "I suppose we can wrap things up here."
            m "You are dismissed..."
            call cho_main("Thank you, Sir.","soft","closed","base","mid")

            # Cho leaves.
            call cho_walk(action="leave", speed=2.5)

            call bld
            m "(Well that was weird.)"
            m "(That girl has a very comprehensive imagination, I got to say...)"

            return

        "\"Luna\"" if luna_unlocked:
            cho "Luna? What about her?"
            m "Aren't you two practically roommates?"
            g9 "I bet there are some fun memories you shared with her!"
            m "Mind telling me about them?"

            # Add section here.

            cho "Don't tell me you also buy favors from her?!"
            m "No, of course not!"
            m "She's more of a-..."
            m "It's complicated..."

            # Add ending here.



        "\"Boys\"":

            # Cho tells you more about the boys at her school,
            # her rise in popularity,
            # and how the Slytherin team is treating her...

            # Writing:
            # Their beaters are the worst!
            # They keep on hitting my arse with their stupid sticks whenever I walk past them.
            # It's like my bum has become their new target practice!
            # I swear if they continue with it I might just-... I will snap!

            "Not yet written."
            pass


    ### Maybe use this writing somewhere. ###
    #cho "In any case, dealing with him won't be an issue at all! It's their team I'm more worried about..."
    #cho "You don't just win by catching the snitch first. You also have to be leading in points!"
    #m "(Counting Cards in \"Black Jack\" is easier than counting the score of this game...)"
    #cho "If you catch the snitch too early, the game will be over."
    #cho "That's how Slytherin won most of their games in the past. They win by letting the other seeker catch the Snitch..."
    #m "(Those rules are so idiotic...)"
    #cho "We can't just narrow down our focus on their seeker this time!"
    #cho "For this one, we have to dismantle the other weak points in their team..."
    #m "Who would be?"
    #cho "Their beaters!"
    #cho "I'm talking about Crabbe and Goyle, of course..."
    #m "Of course..."
    #m "(I have no idea who you are talking about, girl...)"
    #m "And do you think can accomplish that?"
    #cho "*Tzzz!* There would nothing be easier!"
    #m "Yes?"
    #cho "They're Slytherin's two brainless thugs!"
    #cho "They aren't in the slightest bit devoted to their house!"
    #cho "They don't play Quidditch to win the cup... They play to beat people up and get away with it..."
    #cho "All I have to do is get them to play poorly..."
    #m "And how will you manage that?"
    #cho "Just leave that to me, Sir."
    #cho "They would happily throw the towel with the right kind of... motivation."
    #m "You've become quite the strategist, aren't you?"
    #cho "You could say that, Sir..."
    #g9 "How are you going to motivate them exactly?"

    return



###  Stretching ###

label cho_stretching: # Not in use.

    #If you begin masturbating:
    #Tell me how you get ready for practice...

    #If you don’t masturbate:
    #How about you do some squats for me...

    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while she talks.)\"":
            $ cho_jerk_off_counter += 1
            $ masturbating = True
        "\"(I’ll ask her to show her flexibility instead.)\"":
            $ masturbating = False
            m "In that case..."

    #Tell me how you get ready for practice:
    if masturbating:
        m "How about you start by telling me a little bit about your Quidditch training. How do you get ready for practice for example?"
        cho "Okay..."
        cho "Well, we usually wake up pretty early in the morning..."
        "You take your cock out and begin stroking it underneath your desk"
        cho "Once I’m up I usually start by doing some stretches to get the blood flowing."
        g4 "\"Keep talking and you’ll get mine going pretty soon.\""
        cho "Sometimes I’ll have to do it in the dark not to wake anyone up..."
        m "\"Wakey wakey..."
        cho "As during later parts of the year the sun hasn’t even risen yet!"
        g9 "\"There we go, it’s risen... Good morning!\""
        cho "When I’m done with stretching I get dressed and make myself down to the great hall for breakfast..."
        g4 "\"Hhng... nude stretching...\""
        cho" As a player on a Quidditch team we get the whole hall to ourselves and a specially protein rich and energy filled filled breakfast."
        m "\"Yes, protein rich... that’s important. I’ll have to remember that one...\""
        cho "And then...{nw}"
        cho "Sir, are you still paying attention?"
        m "What?"
        # Genie stops masturbating
        cho "..."
        g9 "Protein rich breakfast... very important..."
        cho "Quite..."
        cho "Anyway..."



    #How about you do some squats for me:
    else:
        m "How about you start by doing some squats..."
        cho "Squats, sir?"
        m "Yes, squats... You know, bend your knees and stretch your arms forward..."
        cho "I know what squats are..."
        cho "I’m just a bit confused as to why you want me to start doing squats in your office."
        m "Well, I need to see if what you’re claiming is true. I’d like to see for myself if you’re really on par with the rest of your team."
        m "You’re asking a lot of me here if I were to break up any sort of student movement for you."
        cho "I don’t...{nw}"
        m "Unless what you’re saying is just a lie and you’re also just one of those amateur posers that you mentioned..."
        cho "..." # Annoyed, blushing
        cho "I’m not... look! Can a poser do this?"
        # cho squats down (could just be sprite for starter)
        # Later on if we add more chibi positions she’d show off even more here
        m "Impressive..."
        cho "Thank you..."
        m "How about a handstand?"
        cho "A handstand..."
        cho "That hasn’t been part of my training so far..."
        m "I see.."
        cho "But I could...{nw}"
