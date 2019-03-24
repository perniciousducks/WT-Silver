

### Cho Intro ###

label cho_intro_1:

    "*Knock-knock-knock*"
    m "(...)"

    "*Knock-knock-knock*"
    m "(Who's that?)"
    m "(Can't be Hermione, she usually walks in after the second knock.)"
    m "(...)"
    g9 "I bet it’s another girl!"

    "*Knock-knock-knock*"
    m "Please, give me a moment..."
    g4 "I just need to-{w} ugh!-"
    m "Adjust my pants... There we go."

    $ cho_name_known = False
    menu:
        "\"Who is it?\"":
            $ cho_name_known = True # Affects talk with Snape.
            cho "Cho Chang, Sir."
            g4 "(Such a cute name... please be hot, please be hot...!)"
            cho "May I come in?"
            g9 "Please have nice tits!"
            cho "Sir?"
            m "Oh, right... Come in."

        "\"Come in!\"":
            $ cho_name_known = False # Affects talk with Snape.
            pass


    # Cho enters your office for the first time.
    call play_sound("door")
    call cho_walk("door","660",1.6)

    call cho_main("Good evening, Sir.",face="happy",xpos="mid",ypos="base")

    call ctc

    menu:
        "\"Hello, Miss Chang.\"" if cho_name_known == True:
            call cho_main("Hello to you too, Professor.", "open", "base", "raised", "L")

        "\"Hello, Princess.\"":
            call cho_main("Uhm- Sir,", "upset", "wide", "base", "down")
            call cho_main("I'd prefer not being called by nicknames.", "annoyed", "base", "base", "mid")
            call cho_main("Mutual respect is very important for a student-teacher relationship to work.", "open", "closed", "base", "mid")
            m "(She's must be fun at parties..)"
            call cho_main("I’d much prefer if you called me Cho or Miss Chang...", "base", "base", "raised", "down")
            g9 "And how is that any different..."
            call cho_main("It's my name, Sir!", "open", "shocked", "base", "L")
            m "I see..."
            m "Very well,... Miss Chang it is..."
            call cho_main("Thank you.", "smile", "base", "base", "mid")
            call cho_main("Anyway...", "base", "closed", "base", "mid")

        "\"Hey there, Chap.\"":
            call cho_main("Sir?", "upset", "wide", "base", "down")
            m "What?"
            call cho_main("I’m a girl!", "angry", "base", "base", "mid")
            g4 "Oh, of course you are... You just seemed a bit..."
            call cho_main("A bit what?", "annoyed", "wide", "raised", "L")
            m "(Don’t say tomboy-ish, don’t say tomboy-ish...)"

            menu: # doesn’t matter what you pick
                "\"Tomboyish\"":
                    pass
                "\"Flat\"":
                    pass
                "\"Short\"":
                    pass

            call cho_main("What? Professor how dare you suggest I'-", "angry", "angry", "raised", "mid")
            g4 "Hold on!"
            m "Silly me I forgot where I put my glasses."
            m "You have to excuse my poor eye-sight."
            m "I'm very,{w} very,{w} very,{w} very old."
            m "You’re clearly \"not\" a boy..."
            g9 "(Smooth...)"
            call cho_main("Right, well... Since you seem unable to to see very well...", "upset", "angry", "base", "downR")
            m "..."
            call cho_main("It’s Cho Chang.", "base", "angry", "raised", "mid")
            m "Ah, Miss Chang..."
            m "(Should I know who she is?)"
            call cho_main("Yes, anyway...", "base", "closed", "base", "mid")

        "\"Xiao Hua...\"":
           call cho_main("Uhm, thanks...", "open", "base", "raised", "down")
           call cho_main("But I don’t speak that much Mandarin...{w} I was actually born here...", "soft", "base", "base", "mid")
           g4 "In Scotland?"
           m "(Wait, are we even \"in\" Scotland?)"
           call cho_main("Yes, people always act surprised when they find that out.", "base", "wide", "raised", "R")
           call cho_main("It doesn't help that I have the most Asian sounding name ever...{w} Cho Chang...", "annoyed", "base", "sad", "down")
           m "..."
           call cho_main("Anyway...", "base", "closed", "base", "mid")


    call cho_main("I'm terribly sorry for bothering you, Sir. I hope I'm not interrupting anything important.", "open", "base", "base", "down")
    m "No worries, I can always spare some of my... valuable time for my *Ahem*.{w=0.5}.{w=0.5}.{w=0.5} students."
    g9 "What's on your mind?"

    # Talk about her issue with Hermione
    call cho_main("*Sigh...*", "upset", "closed", "sad", "mid")
    call cho_main("It's Hermione Granger, Sir.", "annoyed", "base", "base", "mid")
    m "Granger? What did she do this time?"
    g9 "I promise you, I'll give her a good, ole-fashioned spanking next time I see her."
    call cho_main("Spanking?", "angry", "base", "sad", "down")
    call cho_main("And why would you do that, Professor?", "annoyed", "suspicious", "raised", "downR")
    call cho_main("(He really must be old... {w} They probably did stuff like that all the time back in the day...)", "upset", "suspicious", "base", "downR")
    call cho_main("Well Sir, it's about a new movement of hers...", "soft", "angry", "raised", "mid")
    m "The \"Men's rights movement\"? I'm familiar."
    call cho_main("Not that one Sir...{w=0.5} The other one...", "open", "angry", "raised", "L")
    g4 "Oh good...{w=0.5} another one..."
    call cho_main("Yes... And you need to stop it Professor!", "angry", "closed", "raised", "mid")
    call cho_main("Her{w=0.5} \"Quidditch equality movement\".", "soft", "angry", "angry", "down")
    m "Her what now?"
    call cho_main("I know! It's absolutely ridiculous...{w=0.5} It’s going to ruin the sport for all of us!", "open", "angry", "sad", "mid")

    m "Sport? Which sport?"
    call cho_main("Quidditch!", "scream", "angry", "angry", "mid")
    m "(Quidditch? What a stupid name for a sport.)"
    call cho_main("The movements' goal is to grant a larger portion of our female students the ability to play.", "open", "angry", "base", "down")
    m "And...{w} that's a bad thing?"
    call cho_main("Her way of going about to achieve it is...", "open", "suspicious", "angry", "R")
    call cho_main("Granger is trying to separate us into male and female teams.", "angry", "angry", "sad", "mid")
    call cho_main("She believes it would put girls on an equal playing field against other girl teams.", "open", "closed", "sad", "mid")
    call cho_main("But what she’s forgetting is that all the female players who made it into a team are already considered a valuable asset... or they wouldn’t be there!", "open", "angry", "angry", "R")
    call cho_main("I worked hard to be at the same level as my fellow team-mates...", "annoyed", "angry", "sad", "downR")
    call cho_main("Splitting us up into a male and female league would just bring on girls that are just there to flaunt their bodies instead off taking the sport seriously...", "upset", "angry", "angry", "downR")
    m "Doesn’t sound like the worst idea honestly..."
    call cho_main("Sir... I’ve trained all my life to be where I’m at.", "open", "angry", "raised", "mid")
    call cho_main("Just as hard as all the other great female Quidditch players of history!", "scream", "closed", "angry", "mid")
    call cho_main("They played side by side with men... Earning their place amongst the best! It never mattered what gender they were.", "angry", "suspicious", "angry", "down")
    call cho_main("And to be shoved aside and forced to play alongside a collection of mediocre amateurs... I won't let that happen!", "angry", "closed", "angry", "down")
    call cho_main("It would undermine the whole sport, and I’d get even less attention as one of the few girls in the league...", "open", "angry", "angry", "down")
    m "Ah, so that’s where the problem lies..."

    call cho_main("Sir, could you please talk to her?", "upset", "base", "raised", "L") 
    call cho_main("I'd be very grateful if you did, I would be forever in your debt.", "base", "base", "raised", "L")
    m "Forever in my debt you say?"
    call cho_main("Yes, Professor. I'd do anything if you make this right.", "smile", "wide", "raised", "L")
    call cho_main("Anything!", "open", "shocked", "angry", "L")
    g9 "It's your lucky day, Miss Chang!"
    m "I will gladly talk to Miss Granger, but in return, how about you come over here and suck on my-"

    # Hermione walks in
    stop music fadeout 1.0
    call hide_characters
    with d3
    pause.1

    call play_sound("door")
    call her_chibi("stand","door","base")

    call her_main("Professor I'm sorry to bother you but I wanted to...","open","closed",ypos="head")
    call play_sound("shatter")
    call her_main("!!!","normal","wide",ypos="head",trans="hpunch")

    call her_walk("door","570",2)
    call her_chibi("stand","570","base",flip=True)

    call cho_main(xpos="base",ypos="base",face="happy")
    call her_main("Cho,{w} How nice to see you here...","open","baseL",xpos="mid",ypos="base",flip=True)
    call her_main("And why are you here exactly?","angry","annoyed")

    call cho_main("Oh, you know...{w=0.5} Just having a discussion with our dear headmaster...", "smile", "base", "base", "L")
    $ renpy.sound.play( "sounds/card_punch4.mp3")
    with hpunch
    call her_main("{size=-5}Bitch..{/size}","base","angryCl")
    $ renpy.sound.play( "sounds/card_punch1.mp3")
    with hpunch
    call cho_main("{size=-5}Whore...{/size}", "soft", "angry", "angry", "L")   
    call her_main("...","normal","frown", cheeks="blush")
    call cho_main("...", "base", "angry", "base", "L") 
    call her_main("So...{p=0.4}what have you been discussing, anything I should know?","open","suspicious", cheeks="blush")
    call cho_main("Oh, it’s nothing that you need to worry your pretty little head about...", "smile", "wide", "angry", "L")
    m "(This could take a while...)"


    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while they talk.)\"":
            $ cho_jerk_off_counter += 1
            $ masturbating = True
        "\"(I should probably listen to them.)\"":
            $ masturbating = False

    # Masturbating
    if masturbating:
        call nar("You pull your cock out and and begin masturbating... focusing on the now heated argument between the two girls in front of you.")
        call her_main("Oh yeah, well... I bet it can’t be anything good seeing how you usually act around men...","mad","angryL")
        call cho_main("What’s that supposed to mean?!?", "scream", "angry", "angry", "L")
        call her_main("You know exactly what I mean... I heard about how you were flaunting those...things of yours at Seamus Finnigan.","crooked_smile","glanceL")
        with hpunch
        call cho_main("Things?", "angry", "wide", "base", "L")
        call cho_main("Oh, miss perfect Hermione Granger. Afraid of using the word tits...", "horny", "suspicious", "raised", "downR")
        call her_main("Cho!","scream","wide", cheeks="blush")
        call her_main(".{w=0.3}.{w=0.3}.","mad","worried", cheeks="blush")
        call cho_main("And so what? What’s wrong with being confident about your body... you should try it some time... You might even get a boyfriend one day...", "soft", "wide", "base", "L")
        call cho_main("Though what do I know? I didn’t need to get my teeth shortened so I wouldn’t be confused as a rabbit!", "base", "angry", "angry", "L")
        call cho_main("Not that anyone would even see them through that horribly bushy hair of yours...", "smile", "angry", "angry", "L")
        call her_main("Well, I heard that you were caught snogging someone in one off the carriages after the triwizard tournament. I’m sure that will go down in the Hogwarts book of history...","grin","closed", cheeks="blush")
        g9 "(How naughty, didn’t expect such indecent behavior from a girl with such a cute face...)"
        call cho_main("Yeah? You ever even kissed a boy before Granger? And I’m not talking about a real kiss and not your daddy kissing you good night...", "soft", "angry", "raised", "L")
        call her_main("Oh...{w=0.5} Of course I have!","angry","worriedL", cheeks="blush")
        call her_main("Hey, just because I’m not the kind of person to jump on every opportunity they get to have a peek at some random boys wand... that doesn’t mean I’ve never kissed anyone...","open","WorriedCl", cheeks="blush")
        g9 "..."
        call her_main("And I didn’t need to have my breasts enlarged not to be confused as a boy!","open","WorriedL", cheeks="blush")
        call cho_main("Oh yeah, like you haven't been flaunting yours around either...", "base", "closed", "raised", "mid")
        call cho_main("Don’t you try and act all innocent!", "smile", "base", "angry", "L")
        call her_main("As If...","normal","Worried", cheeks="blush")
        call cho_main("I wouldn’t doubt that’s why you’re here. To push your stupid agendas whilst you push your breasts together at the same time.", "open", "base", "angry", "L")

        g4 "\"You fucking sluts!\""
        # Genie cums

        her "..."
        cho "Sir..."
        g4 "\"Shit...\""
        cho "Sir, I’m sorry about all this... it’s not why I came here for..."
        m "Oh, of course not!"
        cho "Please consider what I’ve talked to you about..."
        m "Certainly..."

        # Cho walks to the door and stops.
        call cho_walk("mid","door",1.6)
        pause.8
        call cho_chibi("stand","door","base")
        with d3
        pause.8

        cho "{size=-5}You have fun now... getting at that wand of his...{/size}"
        her "Tzzz-..."


    # Not masturbating
    else:
        m "Ladies, no arguing now... you’re in the headmasters office, surely there’s a time and     place."
        her "..."
        cho "Hmph, there’s no argument here..."
        cho "And I’m sure that Hermione’s reasons for interrupting are totally valid..."
        her "And I’m sure Cho wasn’t just coming here to flaunt her body again..."
        cho "What’s that supposed to mean?!?"
        m "(I guess I’ll just have to wait this one out..)"
        # Black screen
        # Centertext [Some time later]
        # Black screen goes away
        m "*ZZZZ*"
        cho "Well I’m sure that your reasons for being here are totally legitimate..."
        m "*ZZZZ*"
        her "They are, for a fact. Completely legitimate... you tell her Professor!"
        m "*ZZZZ*"
        her "Professor!"
        m "*Grunt* Huh, what?"
        her "I always have a valid reason for coming here don’t I?"
        m "Ofcourse you...{w=0.5}{nw}"
        cho "Always? So you do come here often!"
        her "So what..."
        m "Ladies, I think it’s time...{w=0.5}{nw}"
        cho "Don’t worry about it Sir, I was just about to leave anyway..."
        her "..."

        # Cho walks to the door and stops.
        call cho_walk("mid","door",2.5)
        pause.8
        call cho_chibi("stand","door","base")
        with d3
        pause.8

        cho "Professor, please do consider what we discussed earlier..."
        m "Of course."
        her "And what were you...{w=0.5}{nw}"


    # Cho leaves
    pause.2
    call cho_chibi("stand","door","base",flip=True)
    with d3
    pause.8

    call cho_chibi("leave")

    call her_chibi("stand","mid","base")
    with d3

    her "..."
    m "..."
    her "You’re selling favours to her aren’t you?"
    m "I’m..{nw}{p=0.4}"
    her "I knew it!"
    g4 "Now, if you could just listen for a seco...{w=0.5}{nw}"
    her "I don’t want to hear it!"
    her "I’m leaving."

    # Hermione leaves
    call her_walk("mid","leave",2.5)

    # Hermione Mood down
    $ her_mood += 9
    $ hermione_busy = True

    jump main_room



label cho_intro_2:

    # Cho abruptly bursts into your office! Slamming the door behind her.
    stop music fadeout 1.0
    call play_sound("door")
    call cho_chibi("stand","door","base")
    with d3
    pause.5
    call cho_chibi("stand","door","base",flip=True)
    with d1
    call play_sound("bump")
    pause.8
    call cho_chibi("stand","door","base",flip=False)
    with d1
    pause.3
    call cho_walk("door","desk",2.2)
    pause.2

    call cho_main("I hate her!","angry","angry","angry","mid",xpos="mid",ypos="base",trans="hpunch")

    g9 "Miss Chang! My favourite student!"
    g9 "I'm so glad to see you. Is there something I can-"

    call play_music("hitman")
    cho "Cut the crap, Professor!" # Scream
    cho "I know you've told her!"
    g4 "Please don't hurt me." # Small text
    cho "How could you have done this? Sending this dim-witted Gryffindor tramp after me?"
    g4 "W-who?"
    with hpunch
    cho "Granger!" # Scream
    g4 "Aaa-h!" # Girly scream
    cho "Gryffindor's role model student."
    cho "She's out there spreading mean rumours about me!"
    m "How mean are we talking?"
    cho "The worst kind! That I'm cheating at Quidditch!"
    cho "How am I cheating, Professor? Ravenclaw is always in last place?!"
    cho "Not to mention that she's told everyone that I'm whoring myself out to my other classmates, and even my teachers!"
    cho "I did none of that, Professor! None!" # Scream
    cho "And she still won't lay off her stupid equality movement thing!"
    m "You need to calm down, girl."
    cho "When I'm out of here I'm going to rip that bitch's head off..." # Small text
    g4 "(Yikes!)"
    m "I could hear that."
    cho "Good. Then you already know what I'm willing to do if this continues..."
    cho "If you can't stop her, Professor. Then I will!"
    cho "And rest assured that I will end her!" # Angry
    m "I'd prefer you didn't."
    cho "Don't even think about calling me to your office again until you've dealt with that skank!"
    cho "Do I make myself clear, Sir?"
    m "I suppose..."

    # Back to cheerful.
    call play_music("night_theme")
    cho "Good."
    cho "Have a nice evening, Professor."
    m "(...)"

    # Cho leaves.
    call cho_walk("desk","leave",2.2)

    m "I better talk to Hermione about this..."
    m "Or Snape first. Maybe he can help me more."
    g4 "With his unfailing wisdom."
    m "Who am I even kidding..."

    $ hermione_busy = True
    $ snape_busy = False

    jump main_room



### Cut Snape dialogue
### Could be used for something else...

#    m "Has anything out of the ordinary happened to you lately?"
#    sna "Just the usual..."
#    m "Let me guess. That Granger girl is still driving you nuts..."
#    sna "You know it."
#    m "Getting it on with a couple of Slytherin sluts..."
#    sna "You betcha."
#    m "That Potter boy making you question your sexuality..."
#    sna "Always."
#    sna "!!!" # Shocked
#    g9 "Gotcha!"
#    sna "You obviously tricked me."
#    sna "All \"Potter\" can make me feel is pain and suffering..."
#    sna "With the only thing keeping me sane being my \"exclusively female\" sex-pets!"
#    g9 "Keep telling yourself that..."

label cho_snape_talk:

    m "I had another girl visiting me the other day."
    sna "I told you not to get involved with the outside world."
    sna "I hope you were smart enough to not let her into your office."
    g9 "How couldn’t I let her in? She sounded cute."
    sna "Why doesn't that surprise me..."
    sna "And who was this girl?"

    menu:
        "Her name was Cho Chan.":
            sna "Cho Chang?"
            m "No, I'm sure it was \"Chan\"."
            sna "I know my students names, Genie."

        "I can’t remember. I was too distracted by her legs...":
            sna "Can you describe her?"
            sna "Hair colour, hight, her uniform colour? Anything?"
            m "I believe she was asian."
            sna "Cho Chang?"
            m "Bless you."
            sna "No. That's her name."
            sna "We only have one asian girl at our school."
    sna "You’d think as the only wizard school in all of britain, our school would be more diversive..."

    sna "And What did she want from you exactly?"
    m "She asked me a couple of things about Quidditch."
    sna "Of course."
    sna "Her entire world revolves around that stupid broomstick rally."
    m "I take it that you aren't a fan?"

    m "She could be a great candidate for our little training scheme."
    sna "What? Do you want to turn her into a slut too?"
    m "Not only that. I believe she could be of help to deal with Hermione as well."
    sna "Interesting. It seems like you have already made plans for her."
    m "I thought of a couple of things."
    sna "You have my attention!"

    menu:
        "-We'll let Ravenclaw win the Quidditch cup-":
            sna "You know I can't agree to that, Genie."
            sna "And as much as I'd like to see the Potter boy demoralized by losing to a girl..."
            sna "I will never help a Ravenclaw beat my own house."
            m "Didn't you say you don't care about Quidditch?"
            sna "Of course I don't. But a win is a win."
            sna "Unless, you can offer me something more interesting..."
            m "Like what?"
            sna "You make the offer..."
            m "Do you really believe I'll need your help to win this?"
            sna "Judging by your knowledge of the sport, this will be a piece of cake."
            m "If you're so confident, why don't we bet some gold on this?"
            sna "How enticing! How much are you willing to bet?"
            m "20 bucks?"
            sna "What’s a buck?"
            m "20... gold then...."
            sna "That's barely worth it."
            sna "How about 2000?"

            if gold < 2000:
                m "I don't have that much gold."
                sna "Well, you have plenty of time to gather that amount."
            else:
                m "Are you feeling that confident?"
                sna "About Slytherin beating Ravenclaw in Quidditch?"
                sna "Absolutely!"

            sna "So, what do you say? Want to take the bet?"
            m "Under one condition."
            m "You won't cheat, and you won't give Slytherin any unfair advantages."
            sna "I'd never think of it."
            m "So. You want to take on the bet?"
            sna "Indeed I will."
            sna "At least Quidditch will be worth watching now. I can't say no to some good old gambling."


        "-Have her and Hermione go at each other-":
            # Genie tells Snape that Hermione and Cho met in his office.
            # If Genie has jerked off he’ll tell Snape about it again,
            # if not he’ll tell Snape what they were arguing about.

            sna "Granger? Why her?"
            m "They absolutely despise each other."
            sna "Indeed they do..."
            sna "If we get them to waste their energy on each other, they will have less incentive to bother me as well."
            sna "Especially Granger!"

    # Needs an ending tied to the variations or is it just the normal? You spend the night drinking with snape stuff?


    show screen bld1
    show screen notes
    with d3
    $ renpy.play('sounds/win_04.mp3')

    ">You spend rest of the evening in Snape's company talking about Cho's impressive thights."

    hide screen bld1
    hide screen notes
    with d3

    jump day_start



### Talk with Hermione ###
label cho_hermione_talk:

    m "I got some word about you that needs to be addressed..."
    her "About what? Am I in trouble for anything?"
    m "Miss Chang..."
    her "What about her..."
    m "Well, it has come to my attention that you’ve been spreading false rumours about her."
    her "And? It’s well deserved in my opinion..."
    m "Well, don’t you feel like it’s unbefitting of you to publically talk badly about another student."
    her "..."
    g9 "Surely that isn’t something to expect from Gryffindors finest.."
    her "Did Cho put you up to this?"
    g4 "..."
    m "She’s onto me!" # Small text.
    m "Of course not... it was another teacher actually?"
    her "Who?"
    m "Not important..."
    her "It was Snape wasn’t it... {nw}"
    g4 "She’s good!" # Small text.
    m "Well, I’d like you to stop and that’s all that matters..."
    m "And that includes the..."
    m "Quidditch-...{w}whatever it was...{w}movement."

    if her_whoring < 8:
        her "My \"Quidditch equality movement\"?"
        her "But Sir, I'm on the verge of a breakthrough with it!"
        her "I worked very hard on gathering all records of past Quidditch matches, throughout the complete history of Quidditch!"
        her "You'd be surprised just how few female-"
        m "I'll give you ten house points."
        her "Ten? Sir do you even realize how much time it took me to do all that research?"
        m "Twenty?"
        her "Two hundred!"
        g4 "Two hundred? Are you joking?"
        her "And just points isn’t going to cut it..."
        m "Then what else?"
        her "Uhm..."
        m "You’re testing my patience Miss Granger..."
        her "Oh, I know! I want a seat in the teacher stands during the Quidditch matches!"
        her "Cho would be so jealous if she saw me sitting near the commentator and teachers..."
        m "So, you want both 200 points and a seat in the teacher stands..."
        her "Yes..."
        m "Anything else?"
        her "Well..."
        m "Don’t push your luck..."
        her "No, I think that should do..."
        m "200 points to gryffindor...{p=0.4} Happy?"
        # Add points.
        her "If I'm truly honest with you, Sir, my plans weren’t that popular with the Quidditch teams in any case."
        m "I can’t imagine why..."

    elif her_whoring < 18:
        her "Oh... My \"Quidditch equality movement\"?"
        m "That's the one."
        her "It never really got off the ground..."
        her "No pun intended..."
        m "..."
        her " To be honest I don’t have that much time apart from my visits here and studying..."
        her "I might consider dropping it, but it does take away another immense pleasure by seeing Cho getting so worked up about it..."
        her "Fine, I’ll drop it on one condition..."
        m "What?"
        her "I’d like a seat in the teacher stands during the Quidditch matches.."
        m "I’m sure that could be arranged..."
        her "Oh, and a hundred points for Gryffindor..."
        m "(...)"
        m "A hundred points and a seat and the teacher stands..."
        m "I’d say 50 would be more appropriate in this instance..."
        her "Sir, it took a lot of effort to gather all those records of past Quidditch matches, throughout the whole history of Quidditch."
        g4 "one-hundred points."
        her "(...)"
        her "Very well then."
        m "100 points, to the Gryffindor house..."

    else:
        her "My what?"
        m "Your Quidditch movement."
        m "Regarding the male and female roles in Quidditch..."
        her "Oh. I barely even remember that I did that."
        m "So it wouldn't be an issue for you to drop it?"
        her "I guess so..."
        her "Although, if I were to drop it..."
        m "Yes?"
        her "I want a seat in the teacher stands during Quidditch matches though!"
        m "Fine, I’m sure that could be arranged..."

    her "[genie_name], may I ask. What exactly were you and Cho talking about when I entered your office?"
    m "Oh. She just wanted my help with Quidditch."
    her "Pffff- doesn't surprise me that she'd need your help with it."
    her "How else could she possibly win that stupid Quidditch cup..."
    m "I thought that cup was so important to you?"
    her "I couldn’t care less about it, the most important cup is the \"house-cup\"."
    her "They’re completely different..."
    m "Totally different..."

    if her_whoring < 18:
        her "It's the most prestigious award one could earn for your school-house! The Quidditch cup is nothing in comparison..."
        her "Why are students even allowed to play this silly sport at our School?"

    if her_whoring < 15:
        her "They're given the privilege of attending one of the most prestigious wizarding schools in the world, and they're wasting their time with some silly sports game that will get them nowhere..."
        m "Yes. Because why enjoy yourself when you could study instead..."
        her "Exactly!"
        m "(She's so predictable.)"

    m "Well... The quidditch teams is none of your concern anymore..."
    m "You'll tell Cho that you are sorry about your previous interferences."
    her "(...)"
    m "And that the \"Quidditch equality movement\" will be... \"no more\"."

    if her_whoring < 18:
        her "Do I really have to do all that?"
        m "If you want to keep on buying favours from me."
        her "Ugh- Fine, I guess..."
    else:
        her "Sure, whatever..."


    # Summon Cho
    g9 "Great!"
    g9 "Let's call her up here then...."
    her "What? Now?"
    pause.8

    # Cho enters the office.
    call play_sound("door")
    call cho_walk("door","mid",2.5)

    cho "Hello, Sir... you called for me?"
    cho "Granger..."
    her "(...)"
    m "Go on, girl. Tell her."
    cho "Tell me what?"
    her "Ugh-..."
    her "About my \"Quidditch equality movement\"..."
    cho "Did our Professor finally convince you what a terrible idea it would be?"
    m "Actually, I still think granting more people the ability to-"
    cho "Please be quiet, Sir. I’d like to hear it from her."
    cho "I'm going to enjoy this!"
    her "..."
    her "*Sigh* I will end my movement. And I won't interfere with Quidditch again..." #[Looking bored]
    cho "This is amazing! I feel as if it's my birthday!"
    her "After all, Quidditch is a huge waste of everyone's time. Including mine..." #[Still looking bored]
    cho "You're just jealous that I’m better than you at something."
    her "I am not jealous!"
    m "You may go now, Miss Granger."
    her "(...)"
    her "Until next time, Sir."
    her "..."

    # Hermione leaves after glaring one last time at Cho.
    call her_walk("mid","door",2.5)
    pause.5
    call her_chibi("stand","door","base",flip=False)
    with d3
    pause.8

    call her_main("(...)","normal","angry",ypos="head")
    # Add Cho glaring back with her 'head' image.

    call her_chibi("stand","door","base",flip=True)
    with d3
    pause.8

    call her_chibi("leave")

    cho "Thank you for getting her off my back, Professor."
    m "No problem."
    cho "Now, if you’ll excuse me. I'm expected back on the Quidditch field."
    cho "Just call me whenever I can be of service."
    g9 "I will."
    cho "Good day, Professor."

    # Cho leaves.
    call cho_walk("mid","leave",2.5)

    m "That went better than expected."

    # You can now summon Cho Chang to your office.
    stop music fadeout 1.0
    call give_reward(">You've unlocked the ability to summon Cho to your office.","interface/icons/head/head_cho_1.png")


    # End of Intro.
    $ hermione_busy = True
    $ cho_busy = True

    jump main_room
