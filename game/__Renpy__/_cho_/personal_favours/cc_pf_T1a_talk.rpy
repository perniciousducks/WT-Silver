

### Talk with Cho ###

label cc_pf_talk:

    # Tier 1
    if main_matches_won == 0:

        if cho_whoring == 0:
            # Ask about boyfriends.
            call cc_pf_talk_T1_E1

        elif cho_whoring == 1:
            # Ask about boyfriends some more.
            # Unlocks public requests favours.
            $ cho_requests_unlocked = True
            call cc_pf_talk_T1_E2

        else:
            call cc_pf_talk_T1_E3

        if cho_whoring < 3: # Points til 3
            $ cho_whoring += 1
        if cc_pf_talk_OBJ.level < 3: # Hearts 1+2
            $ cc_pf_talk_OBJ.level += 1

    # Tier 2
    elif main_matches_won == 1:

        # Talk with Cho about her Quidditch team.
        call cc_pf_talk_T2_E1 #Temporary?

        if cho_whoring < 8: # Points til 8
            $ cho_whoring += 1
        if cc_pf_talk_OBJ.level < 3: # Hearts 1+2
            $ cc_pf_talk_OBJ.level += 1

    # Stats
    $ cc_pf_talk_OBJ.points += 1

    jump end_cho_event



### Tier 1 ###

label cc_pf_talk_T1_E1:
    m "Let’s have a little chat shall we."
    g9 "Just to get to know each other a little bit better."
    call cho_main("O' course, Sir.","smile","base","base","mid")
    m "First, I'd like you to come a bit closer."
    call cho_main("Very well, [cho_genie_name]...","soft","base","base","R")

    call cho_walk("desk", "base", 1.6)

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
            call cho_main("NO Sir, please!{w=0.5} I don't want to know any o' that!","scream","closed","angry","mid",trans="hpunch")
            call cho_main("(Gross!{w=0.5} Keep it to yourself...)","angry","narrow","sad","R")
            m "I just wanted to expand my backstory a little bit...{w=0.5} What's so wrong with that..."

            jump get_cho_to_talk

    # Cedric Diggory
    call cho_main("Cedric was my boyfriend during the time Hogwarts was hosting the \"triwizards tournament\".","soft","base","base","R")
    m "(They host tournaments here? Interesting...)"
    call cho_main("That year was the most fun I've ever had!","smile","base","base","mid")
    m "Was he that good?"
    call cho_main("What?{w=0.5} No, Sir, not because o' him!{w} The tourney, [cho_genie_name]!","soft","narrow","base","mid")
    m "Sure..."
    call cho_main("We should have it every year if ye were to ask me!","open","closed","base","mid")
    g9 "(A cosplay tournament is what this school needs...)"
    call cho_main("Sir that would be great!","smile","narrow","base","mid")
    g4 "(Wait, wait!{w=0.8} A \"nude\" cosplay tournament!{w=0.6} Even better!)"
    call cho_main("And with new contesters every month! You've got to do this, Sir!","smile","base","base","mid")
    m "I'll think about it..."

    m "Now tell me, how come you two ended up together?"
    call cho_main("Oh. Well...","soft","base","base","down")
    call cho_main("I have this thing for...{w=0.5} athletes.","horny","base","base","down")
    call cho_main("Cedric was the representative champion of our school, so o' course I had to date him.","horny","base","sad","down")
    m "Of course..."
    m "(She's into athletes, so so...)"
    g4 "(You should see me, girl. I'm shredded!)"
    m "(Too bad you can only see the body of that wrinkly old geezer...)"
    m "(Maybe there's like a steroid spell...)"
    g4 "{size=-4}Plexus maximus!{/size}"
    call cho_main("Did ye say something?","soft","base","raised","mid")
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
    call cho_main("But,... you \"are\" helping me.{w} So I guess I owe ye that much...","annoyed","base","base","R")
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
        call cho_main("And what makes you believe that I'd agree to such a thing? Getting rewardred with points for doing nothing?","open","closed","base","mid")
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
        call cho_main("See ye next time.","smile","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
    m "(...)"
    if masturbating:
        m "Well, I got blue-balled..."
        m "Feel like I've deserved it..."

    return



# Second Event
label cc_pf_talk_T1_E2:
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
    call cho_main("O' course, [cho_genie_name].","smile","base","base","mid")
    call cho_main("We did a couple more Quidditch session yesterday.{w} To get ready for our big game against \"Hufflepuff\".","open","narrow","base","mid")
    call cho_main("Our team really believes that we have a chance to win this time!{w} They got a great boost in confidance after I've told'em that the great \"Albus Dumbledore\" would be training us himself!","smile","base","base","mid")
    m "Are you getting along with your team well?"
    call cho_main("I'd say so.{w} But there has been a time when...","soft","base","base","mid")
    call cho_main("Let's just say that it has been difficult for me at first. After all Quidditch is largely dominated by men...","open","narrow","sad","down")
    call cho_main("Getting accepted into our Quidditch team was a challenge. I really had to prove I was worth it.","angry","narrow","sad","mid")
    g9 "And how exactly did you manage that? Mind spilling the beans?"
    call cho_main("Through diligance, expertice, and determination!","open","closed","base","mid")
    m "(...)"
    m "I was sort of expecting something else entirely but,... you do you..."
    call cho_main("And as you can see it did work out in my favour, Sir.","open","base","base","mid")
    call cho_main("Very few teams have allowed a female player into their ranks over the past years.","open","narrow","angry","mid")
    call cho_main("And I've been the only female seeker at this school in over half a century.{w} Can ye even believe that, [cho_genie_name]?","open","wide","base","mid")
    m "(A century? That's like a coffee brake for me girl...)"
    call cho_main("I don't want to brag, [cho_genie_name], but the role of a seeker is \"the\" most important position in a team by far!","smile","narrow","base","mid")
    call cho_main("If ye don't have a good seeker, you have no chance of winning!","soft","closed","base","mid")
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
    call cho_main("O' course, [cho_genie_name]. It was after my request, after all.","soft","base","raised","mid")
    g4 "No kidding?"
    call cho_main("They shouldn't exclude me from team activities just because I'm a girl.","open","base","base","R")
    call cho_main("It makes absolutely no difference!","base","base","base","mid")
    if masturbating:
        g4 "You are naked with them? In the shower?"
    else:
        m "Just to be clear. You are naked with them, in the shower."
    call cho_main("O' course we're all naked, [cho_genie_name]!","soft","base","angry","mid")
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
        call cho_main("[cho_genie_name], are ye alright?","quiver","wide","base","mid")
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

    m "Don't you think, the fact that they've seen you naked has no affect on their actions?"
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
    call cho_main("May I... May I go, [cho_genie_name]?","quiver","closed","base","mid")
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
    call give_reward(">You can now buy \"Public Requests\" from Cho! (They are optional to her training.)","interface/icons/head/head_cho_1.png")


    return



# Third event
## Asking more questions abour her ex boyfriends and jerking off.

label cc_pf_talk_T1_E3:

    m "Care to tell me more about Quidditch?"
    cho "O' course, [cho_genie_name]. Anything specific you'd like to know?"
    m "Yes. Let's talk some more about Diggory..."
    g9 "Your ex-boyfriend."
    cho "{size=-4}I knew I shouldn't have told him...{/size}"
    cho "Why do ye have to keep bringing that up, Sir? What's past is in the past..."
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
        m "A panties obsession? So so…"
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
        m "But, that made me think…"
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

    return


### Tier 2 ###

label cc_pf_talk_T2_E1:

    m "Could you tell me anything about who we are up against next?"
    cho "Our next game is against the Slytherin team."
    g9 "(Sweet! I will win Snape's bet sooner than I thought!)"
    m "Are they better than Hufflepuff?"
    cho "They are, by quite a bit."
    cho "However, Hufflepuff only had one really good player. Which was Cedric."
    cho "Slytherin on the other hand, they are almost unbeatable. They might even be better than Gryffindor!"
    m "You don't say. So why are they next and not Gryffindor?"
    cho "Because of their seeker, he's...{w} so,{w} so bad!"
    m "Who is?"
    cho "Draco Malfoy, Sir."
    m "Any chance you fooled around with him too?"
    cho "*Tzzzz* I'd never surround myself with Slytherin shite."
    m "I guess you and Granger have at least something in common..."
    cho "His daddy bought their whole team new brooms, which is the only reason they've let him in."
    m "His daddy?"
    cho "His father, Sir."
    m "Oh. I thought you might be talking about a different \"daddy\"."
    cho "Very funny, [cho_genie_name]..."
    cho "In any case, dealing with him won't be an issue at all! It's their team I'm more worried 'bout..."
    cho "You don't just win by catching the snitch first. Ye also have to be leading in points!"
    cho "If you catch the snitch too early, the game will be over."
    cho "That's how Slytherin won most of their games in the past. They win by letting the other seeker catch the Snitch..."
    m "Those rules are so idiotic..."

    # Plan how to deal with Slytherin's team.

    # Cho leaves.

    return


label cc_pf_T2_talking_2:

    # Tell her to talk dirty.
    # She's a bit bad at it.
    # You encourage her to thinking of hermione and try again.
    # Cho is getting aggressive which gets you off.

    return


label cc_pf_T2_talking_3:

    return



###  Stretching ###

label cho_stretching:

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




### Old Writing ###

label cho_favor_1:
    $ current_payout = 20

    if cho_whoring <= 0:
        m "{size=-4}(All I'll do is admire her body a bit...){/size}"
        menu:
            "\"(Yes, let's do that.)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_requests

    hide screen cho_chang
    call blkfade
    pause.2
    hide screen blkfade
    call cho_main(xpos="mid",ypos="base",trans="d5")

    if cho_whoring <= 0:
        jump cho_favor_1_1 #First time event.
    elif cho_whoring <= 1:
        jump cho_favor_1_2 #Second time event.
    else:
        jump cho_favor_1_3 #Third time event.



# Favour 1 - First time event.
label cho_favor_1_1:
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
            $ cho_wear_bottom = False
            call ctc
            jump let_cho_strip

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
            $ cho_wear_top = False
            call ctc
            jump let_cho_strip

        "\"Come here and suck my cock!\"":
            m "{size=-5}(Too early for this... It's always too early for this...){/size}"
            jump cho_favor_1_1

        "\"Do you eat ass, Miss Chong?\"":
            call cho_main("Miss... Chong?","open","wide","raised","mid")
            call cho_main("My name Is Chang, [cho_genie_name],... Cho Chang!","open","angry","angry","mid")
            call cho_main("...","pout","narrow","angry","R")
            m "..."
            m "(She didn't answer my question...)"
            $ cho_mood += 5
            jump cho_favor_1_1


    label let_cho_strip:
        call cho_main("Um, I forgot to ask, but how many points do I get for this?","open","base","sad","mid")
        m "You're a terrible negotiator."
        call cho_main("I know.","smile","base","sad","R")
        call cho_main("What do you pay Hermione?","soft","base","raised","mid")
        m "(Too much if you ask me...)"
        m "A couple of points, maybe..."

        call cho_main("I bet my body is worth more than hers!","open","base","base","mid")
        call cho_main("Does Hermione have abs like this? Of course she doesn't!","horny","base","raised","down")
        if her_whoring < 17:
            call cho_main("That boring book glutton is sitting at the library all day as if it's her home...","open","angry","angry","mid")
        else:
            call cho_main("That stupid slut can't spend even a single day without flirting with somebody that has legs attached...","open","angry","angry","mid")

        call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","angry","narrow","angry","mid")
        call cho_main("My body's at the absolute peak of human and wizard conditioning!","open","angry","angry","mid")
        g4 "It is quite impressive, I've got to say!"
        call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
        call cho_main("Now... How badly do you want me to take off the rest?","soft","angry","base","mid")

        m "(...)"
        m "I will give you..."

        menu:
            "-10 points-":
                call cho_main("(10 points... I hope that's a good price.)","horny","narrow","sad","downR")
                call cho_main("I guess that's ok, [cho_genie_name].","angry","narrow","sad","down")
                call blktone
                m "(Really? She'd strip down for barely anything?)"
                m "(Even Hermione gets more points for just her mindless talking...)"
                g4 "(Now she made me feel bad... I should probably pay her a little more.)"
                call hide_blktone
                m "Only the first time, Miss Chang. I will pay you 20 regularily."
                call cho_main("Ok! Thank you, [cho_genie_name].","smile","base","sad","mid")
                $ current_payout = 10
            "-20 points-":
                call cho_main("20 sounds reasonable.","soft","base","base","R")
                m "It sure does..."
                call cho_main("(...)","angry","base","base","R")
                m "(Is it just me, or is the middle choice always the boring one...?)"
                m "Anyway..."
                $ current_payout = 20
            "-100 points-":
                call cho_main("100?","scream","wide","raised","mid")
                call cho_main("Wow, that's a lot!","open","base","raised","L")
                m "(Yeah, it's way too much... what was I thinking?)"
                m "Just today, Miss Chang. I will pay you 20 after this time."
                call cho_main("Thank you so much, [cho_genie_name].","smile","base","base","mid")
                $ current_payout = 100

        g9 "Why don't you thank me by taking off that bra?"
        call cho_main("Of course, sir.","horny","base","sad","down")
        pause.5
        $ cho_wear_bra = False
        call ctc
        call cho_main("I bet my tight body looks way better than Hermione's...","soft","base","raised","mid")

        menu:
            "-Yeah, she's gross-":
                m  "Miss Granger's body is nothing compared to yours."
                call cho_main("Really?","open","wide","raised","mid")
                m  "Her tits sag too much, and her fat hips are disgusting..."
                call blktone
                g4 "(I think something inside me just died saying this.)"
                call hide_blktone
                call cho_main("She really is a...","open","closed","raised","mid")
                call cho_main("...stupid...","angry","closed","angry","mid")
                call cho_main("...fat...","angry","narrow","angry","mid")
                call cho_main("...cow, isn't she?","quiver","narrow","angry","mid")
                $ cho_mood = 0
            "-I can't choose-":
                m  "You're both hot."
                call cho_main("I guess.","pout","narrow","angry","downR")
            "-Nope, you lose-":
                m "I'm afraid, Miss Granger is simply... how shall I put it... sexier!"
                call cho_main("What?","scream","wide","angry","mid")
                m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
                call cho_main("But she doesn't even do work-outs, [cho_genie_name]!","angry","narrow","angry","downR")
                $ cho_mood +=5

        jump jerk_off_to_cho



# Favour 1 - Second time event.
label cho_favor_1_2:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","narrow","sad","down")
    m "I want to see your body!"
    call cho_main("You want me to get naked, sir?","open","base","sad","R")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","pout","wide","sad","mid",trans="hpunch")
    call cho_main("I'll do it.","horny","base","sad","R")
    $ cho_wear_top = False
    call cho_main("There! How is that?","horny","base","sad","R")

    menu:
        "-Be aggressive-":
            g9 "Nice!"
            m "Now the bottom."
            call cho_main("Yes, uhm... [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            call cho_main("(House points...loads of house points...)","horny","closed","sad","mid")
            $ cho_wear_bra = False
            call cho_main("(Am I really doing this?)","angry","base","sad","down")
            $ cho_wear_panties = False
            call cho_main("(Too late now...)","angry","closed","sad","mid")
            call ctc

            m "Very good."
            call cho_main("(...)","upset","closed","sad","mid")
            call cho_main("Uhm... is that enough?","annoyed","wink","sad","mid")

        "-Be nice-":
            m "Go on, girl."
            call cho_main("Yes, sir!","smile","base","sad","R")
            call nar("Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips.")
            $ cho_wear_bottom = False
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            call nar("Her hands nervously move to her bra.")
            call cho_main("Is this okay?","pout","base","sad","mid")
            $ cho_wear_bra = False
            call cho_main("What do you think?","horny","angry","sad","R")
            m "Simply gorgeous."
            call nar("Finally, she pushes her panties down.")
            $ cho_wear_panties = False
            call cho_main("...","upset","closed","sad","mid")
            g4 "Very nice."
            call cho_main("(...)","pout","base","sad","mid")
            call cho_main("Um...","base","base","sad","R")
            call cho_main("Can I put my clothes back on now?","open","narrow","sad","down")

    jump jerk_off_to_cho



# Favour 1 - Third time event.
label cho_favor_1_3:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","angry","sad","mid")
    m "I want to see your body again."
    call cho_main("You want me to get naked, sir?","horny","narrow","sad","down")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","scream","wide","sad","mid")
    call cho_main("I'll do it.","smile","base","base","R")
    call cho_main("Only...","open","angry","sad","mid")
    call cho_main("You're not going to...you know...again, are you sir?","horny","angry","sad","mid")
    m "And what would that be, girl?"
    "Cho shifts uncomfortably on her feet."
    call cho_main("Don't make me say it, Professor.","open","angry","sad","R")
    m "Say what, girl?"
    call cho_main("....masturbate.","horny","angry","sad","mid")
    m "What was that?"
    call cho_main("You're not going to jerk off again, are you?","open","base","angry","mid")

    label cho_wants_you_to_jerk_off:
    menu:
        "-Be Aggressive-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Get on with it, girl."
            call cho_main("Yes, [cho_genie_name]!","base","base","sad","R")
            $ cho_wear_top = False
            "Cho grits her teeth and removes her top in one swift motion."
            m "That's better. Now the bottoms."
            call cho_main("Yes, [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("(house points...loads of house points....)","smile","base","base","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very good."
            call cho_main("........","smile","base","base","mid")

        "-Be Nice-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Go on, girl."
            call cho_main("Yes, [cho_genie_name]!","smile","base","sad","R")
            $ cho_wear_top = False
            "Cho flashes a subdued smile and removes her top in one swift motion."
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("is this okay?","pout","base","sad","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            call cho_main("what do you think?","horny","angry","sad","R")
            m "Simply. gorgeous."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very nice."
            call cho_main("........","upset","closed","sad","mid")

        "-I hadn't planned on it-":
            m "I hadn't planned on it."
            call cho_main("Oh.","pout","base","sad","R")
            call cho_main("Okay then.","base","base","base","mid")
            jump cho_wants_you_to_jerk_off

    jump jerk_off_to_cho



### Jerking off to naked Cho ###
label jerk_off_to_cho:
    menu:
        "-Start jerking off-":
            hide screen cho_chang
            hide screen bld1
            with d3
            pause.2
            call gen_chibi("jerking_off_behind_desk")
            pause.8

            if cho_mood <= 0: #OK with it.
                if cho_whoring in [0]:
                    call cho_main("(!!!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], are you...","horny","narrow","sad","R")
                    call nar(">Cho's voice is soft and slightly husky. She almost sounds...aroused.")
                    call cho_main("Touching yourself?","quiver","narrow","angry","down")
                    call cho_main("[cho_genie_name], I didn't agree to this...","angry","narrow","sad","down")
                elif cho_whoring in [1]:
                    call cho_main("[cho_genie_name]...","horny","narrow","raised","mid")
                    call cho_main("You are touching yourself.","quiver","narrow","raised","down")
                else:
                    call cho_main("I knew you would do that...","smile","angry","angry","mid")

                label keep_jerking_off_to_cho:
                menu:
                    "-Keep jerking off-":
                        if cho_whoring in [0]:
                            call nar(">Your eyes continue to drift over the young Quidditch players tight, athletic body.","start")
                            call nar(">You lean back in your chair and begin stroking in earnest.","end")
                        call cho_main("...","quiver","narrow","raised","downR")
                        call nar(">The young seeker looks mesmerized by your actions.")
                        call cho_main("...","quiver","narrow","base","down")
                        call nar(">Her eyes glued to your thick cock.")

                        if cho_whoring in [0]: #Not really ok with it.
                            call cho_main("I-I've never seen one before.","open","narrow","sad","down")
                            call cho_main("Are they always so... BIG?","smile","narrow","raised","down")
                            m "(Look at the body on that slut!)"
                            call cho_main("(...)","horny","narrow","sad","downR")
                            call ctc

                            call cho_main("[cho_genie_name], how much longer are you going to-","horny","narrow","sad","downR")
                            g4 "Here it comes!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cum_block
                            call cho_main("(...)","horny","wide","sad","L")
                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "I think that was it..."
                            call cho_main("Can I have my points now, [cho_genie_name]?","smile","base","base","R")
                            m "Sure..."

                            if cho_whoring <= 0:
                                $ cho_whoring = 1

                            jump end_cho_favor


                        if cho_whoring >= 1: #Very OK with it!
                            if cho_whoring in [1]:
                                call cho_main("It's so big...","horny","narrow","raised","down")
                                call cho_main("Does it always get like this??","soft","base","raised","mid")
                            else:
                                call cho_main("Keep stroking your cock, [cho_genie_name].","open","angry","angry","down")

                            menu:
                                "-Tell her to shut up-":
                                    if cho_whoring <= 1:
                                        m "Quiet, girl! Don't ruin this for me."
                                        call cho_main("...","annoyed","angry","angry","mid")
                                        call cho_main("","base","closed","base","mid")
                                        call ctc
                                        g4 "(Is she flexing her muscles?!)"
                                    else:
                                        m "Shut up, [cho_name],... and start flexing those muscles!"
                                        call cho_main("Of course, [cho_genie_name].","horny","base","raised","downR")
                                        call ctc
                                    call nar(">You pump your cock faster and faster...")
                                    g4 "(Look at those fucking abs on that girl!)"
                                    call nar("Cho's athletic, young body has you hard as stone.")
                                    g4 "(I want to play xylophone on it...)"

                                "-Play along-":
                                    if cho_whoring <= 1:
                                        m  "Only when I'm around athletic students like you, Miss Chang."
                                        call cho_main("...","horny","base","raised","R")
                                        call cho_main("I'm glad to hear that, [cho_genie_name].","soft","base","base","mid")
                                        m "Such a nice body you have there..."
                                    else:
                                        m "I can't help it, [cho_name]."
                                        m "When I get to see young girls, with bodies like yours..."
                                        g4 "I always get hard!"
                                    if cho_whoring <= 1:
                                        call cho_main("[cho_genie_name], does Hermione let you grope her?","horny","wink","raised","mid")
                                        g9 "She does!"
                                        call cho_main("Maybe next time, [cho_genie_name], I'll give you something that feels a lot nicer than her disgusting tits!","soft","closed","raised","mid")
                                        call ctc
                                    else:
                                        call cho_main("Is my body that good?","quiver","narrow","raised","mid")
                                        call ctc
                                        call cho_main("You're' dripping everywhere, professor","horny","narrow","sad","downR")
                                        call cho_main("oh god...your balls looks so full. There's so much.","horny","base","raised","down")
                                        call nar("The perverse wonder in Cho's voice pushes you over the edge.")
                                    call cho_main("Wouldn't you just love to touch every muscle on my bod-","soft","base","raised","R")

                            g4 "Fuck, here it comes!!!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cho_main("[cho_genie_name]?!","soft","wide","raised","down")
                            call cum_block

                            if cho_whoring <= 1:
                                call cho_main("(Wow. He's cumming so much...)","horny","base","raised","downR")
                                call cho_main("(Just from looking at my body...)","base","base","base","down")
                            else:
                                call cho_main("(Look at all that cum!)","horny","wide","raised","down")
                                call cho_main("......","horny","base","base","downR")
                                call cho_main("(I wonder what it tastes like...)","quiver","narrow","raised","L")

                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "Girl, that was amazing!"
                            call cho_main("...","horny","base","raised","mid")

                            if cho_whoring <= 1:
                                call cho_main("(I can't believe I agreed to that...)","horny","narrow","sad","down")
                                call cho_main("Can I have my points now, [cho_genie_name]?","soft","base","base","mid")
                            else:
                                call cho_main("I'd like to get my points now, [cho_genie_name].","soft","base","base","mid")
                            m "Of course..."

                            if cho_whoring < 2:
                                $ cho_whoring += 1

                            jump end_cho_favor


            else: #Cho is mad! Not OK with it!!!
                if cho_whoring in [0]:
                    call cho_main("(Is he?!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], stop!","scream","closed","angry","mid")
                    call cho_main("I won't let you do that!","open","angry","angry","mid")
                    m "Do what? I'm just scratching my leg..."
                    call cho_main("Don't take me for a fool! I know exactly what you are doing!","angry","closed","angry","mid")
                    call cho_main("Stop!","open","closed","angry","mid",trans="hpunch")
                    call cho_main("Touching!","scream","angry","angry","mid",trans="hpunch")
                    call cho_main("Yourself!!!","angry","angry","angry","mid",trans="hpunch")
                    g4 "Jeeze..., no need to scream like that..."
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("sit_behind_desk")
                    pause.8
                    call bld
                    m "I will stop..."
                    m "scratching..."
                    m "my leg..."

                elif cho_whoring in [1]:
                    call cho_main("No,[cho_genie_name]! Stop doing that!","horny","wide","sad","L")
                    m "Doing what?"
                    call cho_main("Stop touching yourself!","horny","wide","sad","L")
                    m "Whatever... You ruined the mood anyway..."
                    call gen_chibi("sit_behind_desk")
                    m "Better?"

                else: #OK again!
                    call cho_main("[cho_genie_name]! You are touching yourself again!","horny","wide","sad","L")
                    m "What? Don't you like it?"
                    call cho_main("(...)","horny","wide","sad","L")
                    jump keep_jerking_off_to_cho

                call cho_main("Thank you, [cho_genie_name].","annoyed","angry","angry","R")
                call cho_main("Can I have my points now?","open","closed","raised","mid")
                m "Sure..."
                jump end_cho_favor

        "-Better not-":
            call nar(">You decide not to indulge your baser instincts.")
            m "Alright, Miss [cho_name]."

            if cho_whoring <= 0:
                $ cho_whoring = 1

            else:
                call cho_main("[cho_genie_name], are we done, already?","horny","base","sad","R")
                call cho_main("(I thought he would maybe...)","smile","base","base","R")
                m "Yes. We are done for today."
            jump end_cho_favor



label end_cho_favor:
    #if not first_cho_favor_done:
    #    $ first_cho_favor_done = True

    m "[current_payout] points to Gryffindor!"
    $ gryffindor += current_payout
    call cho_main("[cho_genie_name], I'm from Ravenclaw!","open","wide","raised","mid")
    m "Right, what did I say?"
    $ gryffindor -= current_payout

    m "[current_payout] points to Ravenclaw!"
    $ ravenclaw += current_payout
    $ cho_mood -= 10

    call cho_main("Thank you.","soft","base","base","mid")

    call nar(">Cho quickly puts her clothes on before leaving.")
    call load_cho_clothing_saves
    if daytime:
        call cho_main("Good day, [cho_genie_name].","smile","base","base","mid")
    else:
        call cho_main("Good night, [cho_genie_name].","smile","base","base","mid")
    call play_sound("door")

    jump end_cho_event
