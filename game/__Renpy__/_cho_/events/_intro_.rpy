

### Cho Intro ###

label cho_intro_1:

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "(...)"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "(Who's that?)"
    m "(Can't be Hermione, she never knocks anymore.)"
    m "(...)"
    g9 "I bet it’s another girl!"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "Please, give me a moment..."
    g4 "I just need to-{w} *urgh!*"
    call play_sound("equip_inventory")
    m "Adjust my pants...{w} There we go."

    menu:
        "\"Who is it?\"":
            $ cho_name_known = True
            call bld
            cho "Cho Chang, Sir."
            g4 "(Such a cute name... please be hot, please be hot...!)"
            cho "May I come in?"
            g9 "Please have nice tits!"
            cho "Sir?"
            m "Oh, right... Come in."

        "\"Come in!\"":
            $ cho_name_known = False
            pass


    # Cho enters your office for the first time.
    call cho_walk("660", "base", action="enter", speed=1.6)

    call cho_main("Good evening, Sir.","base","base","base","mid",xpos="mid",ypos="base")

    call ctc

    menu:
        "\"Hello, Miss Chang.\"" if cho_name_known == True:
            call cho_main("Hello to you too, Professor.", "open", "base", "raised", "L")

        "\"Hello, Princess.\"":
            call cho_main("*Uhm*... Sir,", "upset", "wide", "base", "down")
            call cho_main("I'd prefer not to be called nicknames.", "annoyed", "base", "base", "mid")
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
           g4 "Where?"
           call cho_main("In Scotland, Sir.", "soft", "wink", "base", "mid")
           call cho_main("People always act surprised when they find that out.", "base", "narrow", "base", "mid")
           call cho_main("It doesn't help that my name sounds so Asian...{w} Cho Chang...", "annoyed", "base", "sad", "down")
           m "..."
           call cho_main("Anyway...", "base", "closed", "base", "mid")


    call cho_main("I'm terribly sorry for bothering you, Sir.{p=0.8}Hope I'm not interrupting anything important.", "open", "base", "base", "down")
    m "No worries, I can always spare some of my...{w=0.6} valuable time...{p=1.0}*Ahem*{w=0.6} for my dear students..."
    g9 "What's on your mind?"

    # Talk about her issue with Hermione
    call cho_main("*Sigh...*", "upset", "closed", "sad", "mid")
    call cho_main("It's Hermione Granger, Sir.", "annoyed", "base", "base", "mid")
    m "Granger? What did she do this time?"
    g9 "I promise you, I'll give her a good, ole-fashioned spanking next time I see her."
    call cho_main("Spanking?", "angry", "base", "sad", "down")
    call cho_main("And why would you do that, Professor?", "annoyed", "narrow", "raised", "downR")
    call cho_main("(He really must be old...{w} They probably did stuff like that all the time back in the day...)", "upset", "narrow", "base", "downR")
    call cho_main("Well Sir, it's about that new movement of hers...", "soft", "angry", "raised", "mid")
    m "The \"Men's rights movement\"? I'm familiar."
    call cho_main("Not that one, Sir...{w=0.8} The other one...", "open", "angry", "raised", "L")
    g4 "Oh good...{w=0.5} another one..."
    call cho_main("Yes... And you need to stop it Professor!", "angry", "closed", "raised", "mid")
    call cho_main("Her{w=0.5} \"Quidditch equality movement\".", "soft", "angry", "angry", "down")
    m "Her what now?"
    call cho_main("I know! It's absolutely ridiculous...{w=0.5} It’s going to ruin the sport for all of us!", "open", "angry", "sad", "mid")

    m "Sport? Which sport?"
    call cho_main("Quidditch!", "scream", "angry", "angry", "mid")
    call cho_main("", "annoyed", "angry", "angry", "mid")
    m "(Quidditch? What a stupid name for a sport.)"
    call cho_main("The movements' goal is to grant a larger portion of our female students the ability to play.", "open", "angry", "base", "down")
    m "And...{w} that's a bad thing?"
    call cho_main("Her way of going about to achieve it is...", "open", "narrow", "angry", "R")
    call cho_main("Granger is trying to separate us into male and female teams.", "annoyed", "angry", "sad", "mid")
    call cho_main("She believes it would put girls on an equal playing field against other girl teams.", "open", "closed", "sad", "mid")
    call cho_main("But what she’s forgetting is that all the female players who made it into a team are already considered a valuable asset... or they wouldn’t be there!", "open", "angry", "angry", "R")
    call cho_main("I worked hard to be at the same level as my fellow teammates...", "annoyed", "angry", "sad", "downR")
    call cho_main("Splitting us up into a male and female league would just bring on girls that are just there to flaunt their bodies, instead off taking the sport seriously...", "upset", "angry", "angry", "downR")
    m "Doesn’t sound like the worst idea honestly..."
    call cho_main("Sir... I’ve trained all my life to be where I’m at.", "open", "angry", "raised", "mid")
    call cho_main("Just as hard as all the other great female Quidditch players of history!", "scream", "closed", "angry", "mid")
    call cho_main("They played side by side with men... Earning their place amongst the best! It never mattered what gender they were.", "angry", "narrow", "angry", "down")
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

    call play_sound("door")
    call her_chibi("stand","door","base")

    call her_main("Professor I'm sorry to bother you but I wanted to...","open","closed",ypos="head")
    call her_main("!!!","normal","wide",ypos="head",trans="hpunch")

    call her_walk(xpos="570", ypos="base", speed=2)
    call her_chibi("stand","570","base",flip=True)

    call cho_main("","annoyed","angry","angry","R",xpos="base",ypos="base")
    call her_main("Cho,{w} How nice to see you here...","open","baseL",xpos="mid",ypos="base",flip=True)
    call her_main("And why are you here exactly?","angry","annoyed")

    call cho_main("Oh, you know...{w=0.5} Just having a discussion with our dear headmaster...", "smile", "base", "base", "L")
    $ renpy.sound.play("sounds/card_punch4.mp3")
    call her_main("{size=-5}Bitch...{/size}","base","angryCl",trans="hpunch")
    $ renpy.sound.play("sounds/card_punch1.mp3")
    call cho_main("{size=-5}Whore...{/size}", "soft", "angry", "angry", "L",trans="hpunch")
    call her_main("...","normal","frown", cheeks="blush")
    call cho_main("...", "base", "angry", "base", "L")
    call her_main("So...{p=0.4}what have you been discussing? Anything I should know?","open","suspicious", cheeks="blush")
    call cho_main("Oh, it’s nothing that you need to worry your pretty little head about...", "smile", "wide", "angry", "L")
    m "(This could take a while...)"


    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while they talk.)\"":
            call hide_characters
            with d3
            pause.2

            call gen_chibi("jerking_off_behind_desk")
            with d3
            pause.5

            $ cho_jerk_off_counter += 1
            $ her_jerk_off_counter += 1
            $ jerked_off_during_cho_intro = True # Optional dialogue with Snape.

            $ masturbating = True

        "\"(I should probably listen to them.)\"":
            $ masturbating = False


    # Masturbating
    if masturbating:
        call nar("You pull your cock out and and begin masturbating... focusing on the now heated argument between the two girls in front of you.")

        show screen cho_chang
        call her_main("Oh yeah, well... I bet it can’t be anything good seeing how you usually act around men...","mad","angryL")
        call cho_main("What’s that supposed to mean?!?", "scream", "angry", "angry", "L")
        call her_main("You know exactly what I mean... I heard about how you were flaunting those...things of yours at Seamus Finnigan.","crooked_smile","glanceL")
        with hpunch
        call cho_main("Things?", "angry", "wide", "base", "L")
        call cho_main("Oh, miss perfect Hermione Granger. Afraid of using the word tits...", "horny", "narrow", "raised", "downR")
        call her_main("Cho!","scream","wide", cheeks="blush")
        call her_main(".{w=0.3}.{w=0.3}.","mad","worried", cheeks="blush")
        call cho_main("And so what? What’s wrong with being confident about your body... you should try it some time... You might even get a boyfriend one day...", "soft", "wide", "base", "L")
        call cho_main("Though what do I know? I didn’t need to get my teeth shortened so I wouldn’t be confused as a rabbit!", "base", "angry", "angry", "L")
        call cho_main("Not that anyone would even see them through that horribly bushy hair of yours...", "smile", "angry", "angry", "L")
        call her_main("Well, I heard that you were caught snogging someone in one off the carriages after the triwizard tournament. I’m sure that will go down in the Hogwarts book of history...","grin","closed", cheeks="blush")
        g9 "(How naughty, didn’t expect such indecent behavior from a girl with such a cute face...)"
        call cho_main("Yeah? You ever even kissed a boy before Granger? And I’m talking about a real kiss and not your daddy kissing you good night...", "soft", "angry", "raised", "L")
        call her_main("Oh...{w=0.5} Of course I have!","angry","worriedL", cheeks="blush")
        call her_main("Hey, just because I’m not the kind of person to jump on every opportunity they get to have a peek at some random boys wand... that doesn’t mean I’ve never kissed anyone...","open","WorriedCl", cheeks="blush")
        g9 "..."
        call her_main("And I didn’t need to have my breasts enlarged not to be confused as a boy!","open","WorriedL", cheeks="blush")
        call cho_main("Oh yeah, like you haven't been flaunting yours around either...", "base", "closed", "raised", "mid")
        call cho_main("Don’t you try and act all innocent!", "smile", "base", "angry", "L")
        call her_main("As If...","normal","Worried", cheeks="blush")
        call cho_main("I wouldn’t doubt that’s why you’re here. To push your stupid agendas whilst you push your breasts together at the same time.", "open", "base", "angry", "L")

        g4 "{size=-4}You fucking sluts!{/size}"

        # Genie cums
        call hide_characters
        with d3

        call cum_block
        call gen_chibi("cumming_behind_desk")
        with d3
        pause.8

        g4 "*heavy breathing* {size=-4}Fuck yes...{/size}"

        call cum_block

        g4 "*Argh!* {size=-4}You whores!{/size}"

        call cho_main("Sir?","soft","narrow","base","mid",ypos="head")

        m "(Shit...)"

        call gen_chibi("came_on_desk")
        with d3
        pause.8

        call cho_main("Sir, I’m sorry about all this... it’s not what I came here for...","open","closed","sad","mid",xpos="base",ypos="base")
        m "Oh, of course not!"
        call cho_main("Please consider what we’ve talked about...","base","base","sad","mid")
        m "Certainly..."

        # Cho walks to the door and stops.
        call cho_walk("door", "base", speed=1.6)
        pause.8
        call cho_chibi("stand","door","base")
        with d3
        pause.8

        call cho_main("{size=-4}You have fun now... getting at that wand of his...{/size}","angry","narrow","angry","L",ypos="head")
        call her_main("*Tzzzh!*...","clench","angryCl",ypos="head")


    # Not masturbating
    else:
        m "Ladies, no arguing now... you’re in the headmasters office, surely there’s a time and place."
        call her_main("...","annoyed","glanceL")
        call cho_main("*Hmph* There’s no argument here...","angry","narrow","angry","L")
        call cho_main("I’m sure that Hermione’s reasons for interrupting are totally valid...","upset","closed","angry","mid")
        call her_main("And I’m sure Cho wasn’t just coming here to flaunt her body again...","soft","closed")
        call cho_main("What’s that supposed to mean?!?","scream","base","base","mid",trans="hpunch")
        m "(I guess I’ll just have to wait this one out..)"

        # Black screen
        call hide_characters
        call blkfade
        pause 2

        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

        pause 1
        call hide_blkfade

        $ renpy.sound.play("sounds/snore1.mp3")
        gen "*Snore*{w=2.0}{nw}"
        show screen hermione_main
        call cho_main("Well I’m sure that your reasons for being here are totally legitimate...","soft","narrow","base","L",trans="hpunch")
        $ renpy.sound.play("sounds/snore2.mp3")
        gen "......{w=0.5}*Snore*{w=1.0}{nw}"
        call her_main("They are, for a fact. Completely legitimate... you tell her Professor!","clench","angryL",trans="hpunch")
        $ renpy.sound.play("sounds/snore3.mp3")
        gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
        call her_main("Professor!","scream","angryCl",trans="hpunch")
        g4 "*Grunt* {size=-4}Huh, what?{/size}"
        call her_main("I always have a valid reason for coming here, don’t I?","base","base")
        m "Of course you-{w=0.6}{nw}"
        call cho_main("Always? So you \"do\" come here often!","smile","narrow","base","L")
        call her_main("So what...","angry","angryCl")
        m "Ladies, I think it’s time to-{w=0.8}{nw}"
        call cho_main("Don’t worry about it Sir, I was just about to leave anyway...","soft","narrow","angry","mid")
        call her_main("...","annoyed","angryL")

        # Cho walks to the door and stops.
        call cho_walk("door", "base", speed=2.5)
        pause.8
        call cho_chibi("stand","door","base")
        with d3
        pause.8

        call cho_main("Professor, please do consider what we discussed earlier...","soft","closed","base","mid",ypos="head")
        m "Of course."
        call her_main("Hmmm?","normal","suspicious",ypos="head")


    # Cho leaves
    pause.2
    call cho_chibi("stand","door","base",flip=True)
    with d3
    pause.5

    call cho_chibi("leave")

    call her_chibi("stand","mid","base",flip=False)
    with d3
    pause.5

    call her_main("...","annoyed","angry",xpos="base",ypos="base",flip=False)
    m "..."
    call her_main("You’re selling favours to her aren’t you?","soft","glance")
    m "I’m...{p=0.8}{nw}"
    call her_main("I knew it!","angry","angry")
    g4 "Now, if you could just listen for a second!"
    call her_main("I don’t want to hear it!","open","closed")
    call her_main("I’m leaving.","normal","frown")

    # Hermione leaves
    call her_walk(action="leave", speed=2.5)

    # Hermione Mood down
    $ her_mood += 6
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
    call cho_walk("desk", "base", speed=2.2)
    pause.2

    call cho_main("I hate her!","scream","closed","angry","mid",xpos="mid",ypos="base",trans="hpunch")
    call cho_main("","angry","angry","angry","mid")

    g9 "Miss Chang! My favourite student!"
    g9 "I'm so glad to see you. Is there something I can-"

    call play_music("hitman")
    call cho_main("Cut the crap, Professor!{p=0.6}I know you've told her!","soft","narrow","angry","mid")
    g4 "{size=-4}Please don't hurt me.{/size}"
    call cho_main("How could you have done this?{p=0.6}Sending this dim-witted Gryffindor tramp after me?","open","angry","angry","mid")
    g4 "W-who?"
    call cho_main("Granger!","scream","closed","angry","mid",trans="hpunch")
    g4 "Aaa-h!{p=0.5}{nw}" # Girly scream
    call cho_main("Gryffindor's role model student.","angry","angry","angry","mid")
    call cho_main("She's out there spreading mean rumours about me!","open","narrow","base","R")
    m "How mean are we talking?"
    call cho_main("The worst kind! That I'm cheating at Quidditch!","angry","narrow","angry","down")
    call cho_main("How am I cheating, Professor? Ravenclaw is always in last place?!","soft","narrow","sad","downR")
    call cho_main("Not to mention that she's told everyone that I'm whoring myself out to my other classmates, and even my teachers!","open","narrow","angry","L")
    call cho_main("I did none of that, Professor! None!","scream","closed","angry","mid",trans="hpunch")
    call cho_main("And she still won't lay off her stupid equality movement thing!","angry","angry","angry","mid")
    m "You need to calm down, girl."
    call cho_main("{size=-4}When I'm out of here I'm going to rip that bitch's head off...{/size}","quiver","narrow","angry","downR")
    g4 "(Yikes!)"
    m "I could hear that."
    call cho_main("Good. Then you already know what I'm willing to do if this continues...","soft","closed","base","mid")
    call cho_main("If you can't stop her, Professor. Then I will!","open","narrow","base","mid")
    call cho_main("And rest assured that I will end her!","soft","narrow","angry","mid")
    m "I'd prefer you didn't."
    call cho_main("Don't even think about calling me to your office again until you've dealt with that skank!","open","narrow","angry","mid")
    call cho_main("Do I make myself clear, Sir?","scream","closed","angry","mid",trans="hpunch")
    call cho_main("","angry","narrow","angry","mid")
    m "I suppose..."

    # Back to cheerful.
    call play_music("night_theme")
    call cho_main("Good.","base","base","base","mid")
    m "(...)"
    call cho_main("Have a nice evening, Professor.","smile","closed","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=2.2)

    call bld
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

    call bld
    m "I had another girl visiting me the other day."
    call sna_main("I told you not to get involved with the outside world.","snape_09",ypos="head")
    call sna_main("I hope you were smart enough to not let her into your office.","snape_05")
    g9 "How couldn’t I let her in? She sounded cute."
    call sna_main("Why doesn't that surprise me...","snape_06")
    call sna_main("And who was this girl?","snape_03")

    menu:
        "\"Her name was Cho Chan.\"":
            call sna_main("Cho Chang?","snape_01")
            m "No, I'm sure it was \"Chan\"."
            call sna_main("I know my students names, Genie.","snape_04")

        "\"I can’t remember. I got too distracted by her legs...\"":
            call sna_main("Can you describe her?","snape_05")
            call sna_main("Hair colour, hight, her uniform colour? Anything?","snape_02")
            m "I believe she was asian."
            call sna_main("Cho Chang?","snape_10")
            m "Bless you."
            call sna_main("No. That's her name.","snape_08")
            call sna_main("We only have one asian girl at our school.","snape_24")
            call sna_main("You’d think as the only wizard school in all of britain, our school would be more diversive...","snape_09")

    call sna_main("And what did she want from you exactly?","snape_05")
    m "She asked me a couple of things about Quidditch."
    call sna_main("Of course.","snape_09")
    call sna_main("Her entire world revolves around that stupid broomstick rally.","snape_08")
    m "I take it that you aren't a fan?"

    m "She could be a great candidate for our little training scheme."
    call sna_main("What? Do you want to turn her into a slut too?","snape_01")
    m "Not only that. I believe she could be of help to deal with the Granger girl as well."
    call sna_main("Interesting. It seems like you have already made plans for her.","snape_02")
    m "I thought of a couple of things."
    call sna_main("You have my attention!","snape_13")

    label discuss_cho_plan:
        if "1" in cho_plan and "2" in cho_plan:
            jump discussed_cho_plan

    menu:
        "\"Help her win the Quidditch cup\"" if "1" not in cho_plan:
            $ cho_plan.append("1")
            call sna_main("And help her win against Slytherin?","snape_16")
            call sna_main("I can't agree to that, Genie. As much as I'd like to see the Potter boy demoralized by losing to a girl...","snape_10")
            call sna_main("Or Malfoy for that matter... He's been way too cocky lately.","snape_08")
            m "Who?"
            call sna_main("A student of mine... Rich parents, bought his way into our Quidditch team,... Spoiled beyond belief.","snape_29")
            m "Didn't you say you don't care much about Quidditch?"
            call sna_main("Of course I don't. But a win is a win.","snape_09")
            call sna_main("Besides, Ravenclaw doesn't have a chance against Slytherin.","snape_03")
            call sna_main("They are notoriously bad at Quidditch. And they have been for years.","snape_02")
            m "You sound very confident."
            g9 "Want to bet on it?"
            call sna_main("A bet? How very enticing!","snape_20")
            call sna_main("How much are you willing to bet?","snape_18")
            m "Twenty bucks?"
            call sna_main("Don't you mean gold?","snape_05")
            m "Twenty... gold then..."
            call sna_main("That's barely worth it.","snape_04")
            call sna_main("How about two thousand gold?","snape_13")

            if gold < 2000:
                m "I don't have that much gold."
                call sna_main("Well, you have plenty of time to gather that amount.","snape_22")
            else:
                m "Are you feeling \"that\" confident?"
                call sna_main("About Slytherin beating Ravenclaw in Quidditch?","snape_20")
                call sna_main("Absolutely!","snape_22")

            call sna_main("So, what do you say? Want to take the bet?","snape_13")
            m "Under one condition."
            m "You won't cheat, and you won't give Slytherin any unfair advantages."
            call sna_main("I'd never think of it.","snape_09")
            m "So. You want to take on the bet?"
            call sna_main("Indeed I will.","snape_02")
            call sna_main("At least Quidditch will be worth watching now. I can't say no to some good old gambling.","snape_20")
            call sna_main("But how will you help Miss Chang in Quidditch? You know nothing about it?","snape_05")

            menu:
                "\"I'll just read a book about it\"":
                    call sna_main("You are really planning to take this bet seriously, aren't you?","snape_04")
                    m "You have no idea! I'll do anything to get into that girl's panties."
                    call sna_main("Blinded by the sweet love for a girl...","snape_13")
                    call sna_main("You have already lost, my friend!","snape_21")
                    m "We'll see about that."
                    m "(Now, where could I get a book about Quidditch from...)"

                "\"I trust my instincts!\"":
                    call sna_main("Your instincts?","snape_14")
                    m "Never underestimate the capabilities of a Genie..."
                    call sna_main("(...)","snape_12")

            jump discuss_cho_plan

        "\"Have her and Hermione go at each other\"" if "2" not in cho_plan:
            $ cho_plan.append("2")
            call sna_main("Granger? Why her?","snape_05")
            m "They absolutely despise each other."
            call sna_main("They do?","snape_20")
            m "Yes. They had a little confrontation here in my room..."
            call sna_main("A confrontation? So so...","snape_13")
            call sna_main("What was it about?","snape_20")

            if jerked_off_during_hermione_intro and jerked_off_during_cho_intro:
                m "I have no idea. I jerked off during thier whole exchange."
                call sna_main("You did that again? And neither of them realized?","snape_22")
                m "Didn't seem like it. They were too occupied with insulting each other..."

            elif jerked_off_during_cho_intro:
                m "I have no idea. I jerked off during thier whole exchange."
                call sna_main("You did what?","snape_15")
                m "I jerked off.{w} Beat my meat.{w} Wrestled the snake.{w} Whatever you want to call it."
                m "Don't tell me you never do it..."
                call sna_main("Not in front of my students!","snape_07")
                call sna_main("How did neither of them realize what you were doing?","snape_10")
                m "They were too occupied with insulting each other..."
                call sna_main("I can imagine that...","snape_20")

            else:
                m "Some nonsense about wasting my time."
                call sna_main("Which they probably did?","snape_05")
                m "Yeah. But I slept through most of it..."
                call sna_main("I wish I could do the same.","snape_09")
                call sna_main("Zone out and dream of stuffing that witch's relentless mouth!","snape_06")
                m "I feel you..."

            call sna_main("Hmmm...{w} That reminds me of something I witnessed at the end of last year...","snape_23")
            call sna_main("Granger was scolding the poor girl for kissing a boy in the hallways.","snape_20")
            m "Hot...{w} What happened then?"
            call sna_main("They were screaming and grabbing at each others hair before I had the chance to interfere.","snape_18")
            call sna_main("I ended up taking fifty points from Gryffindor. I should have taken at least one hundred now that I think about it...","snape_22")
            m "Does she often do things like that?"
            call sna_main("Are you kidding? All the bloody time!","snape_17")
            call sna_main("Granger is a nuisance to everyone. Didn't I already tell you that?","snape_16")
            m "No. I meant the Cho girl..."
            g9 "Does she make out with boys often?"
            call sna_main("How should I know. I'm not her stalker.","snape_12")
            m "Well, if what you've said is true... Training her should be a piece of cake."
            g9 "And what a delicious piece of cake it will be!"

            jump discuss_cho_plan



    # Ending
    label discussed_cho_plan:

    show screen bld1
    show screen notes
    with d3
    $ renpy.play('sounds/win_04.mp3')

    ">You spend the rest of the evening in Snape's company talking about Cho's impressive thighs."

    hide screen bld1
    hide screen notes
    with d3

    jump day_start



### Talk with Hermione ###
label cho_hermione_talk:

    call her_main("",xpos="mid",ypos="base",trans="fade")

    # Intro
    if cho_intro_state == "talk_with_hermione":
        $ cho_intro_state = "nagotiate_with_hermione"

        m "I got some word about you that needs to be addressed..."
        call her_main("About what? Am I in trouble for anything?","soft","wide_stare")
        m "Miss Chang..."
        call her_main("Oh...","annoyed","ahegao_raised")
        call her_main("What about her...","annoyed","angry")
        m "Well, it has come to my attention that you’ve been spreading false rumours about her."
        call her_main("And? It’s well deserved in my opinion...","soft","annoyed")
        m "Well, don’t you feel like it’s unbefitting of you to publically talk badly about another student."
        call her_main("...","annoyed","down_raised")
        g9 "Surely that isn’t something to expect from Gryffindors finest.."
        call her_main("Did Cho put you up to this?","normal","suspicious")
        g4 "..."
        m "(She’s onto me!)"
        m "Of course not... it was another teacher, actually."
        call her_main("Who was it?","open","angry")
        m "Not important..."
        call her_main("It was Snape wasn’t it...","annoyed","glance")
        g4 "(She’s good!)"
        m "Well, I’d like you to stop and that’s all that matters..."
        m "And that includes the..."
        m "Quidditch-...{w} whatever it was...{w} movement."

    # Repeat
    else:
        m "[hermione_name], there is something we need to talk about."
        call her_main("Is it about Cho again?","annoyed","suspicious")
        m "Yes indeed."
        m "I’d like you to stop your..."
        m "Quidditch-...{w} something something...{w} movement."

    if her_whoring < 4: # If you haven't groped her breasts or ass yet.
        call her_main("My \"Quidditch equality movement\"?","soft","base")
        call her_main("But Sir, I'm on the verge of a breakthrough with it!","soft","closed")
        call her_main("I worked very hard on gathering all records of past Quidditch matches, throughout the complete history of Quidditch!","open","wink")
        call her_main("You'd be surprised just how few female-","soft","closed")
        m "I'll give you ten house points."
        call her_main("Ten points?","soft","wide",trans="hpunch")
        call her_main("Sir do you even realize how much time it took me to do all that research?","angry","frown")
        m "Twenty?"
        call her_main("Two hundred!","angry","angryCl")
        g4 "Two hundred? Are you nuts?"
        call her_main("And just points isn’t going to cut it...","open","closed")
        m "Then what else?"
        call her_main("Uhm...","annoyed","baseL")
        m "You’re testing my patience Miss Granger..."
        call her_main("Oh, I know!{p=0.5}I want a seat in the teacher stands during the Quidditch matches!","smile","happyCl")
        call her_main("Cho would be so jealous if she saw me sitting near the commentator and teachers...","grin","glance")
        m "So, you want both 200 points and a seat in the teacher stands..."
        call her_main("Yes...","base","happy")

        menu:
            m "(...)"
            "\"Very well...\"":
                m "Anything else?"
                call her_main("Well...","soft","squintL")
                m "Don’t push your luck..."
                call her_main("No, I think that should do...","smile","happyCl")
                m "200 points to gryffindor...{p=0.6}Happy?"
                $ gryffindor += 200

                call her_main("If I'm truly honest with you Sir,{p=0.6}My plans weren’t that popular with the Quidditch teams in any case.","soft","glance")
                m "I can’t imagine why..."
                pass

            "\"I don't think so!\"":
                call her_main("What?... Why?!","shock","wide",trans="hpunch")
                m "Because you are being unreasonable."
                call her_main("But you made it sound like it was something important to you!","disgust","concerned")
                m "And you believe that I'd just throw point at you because of that?"
                call her_main("{size=-4}It was worth a try...{/size}","annoyed","down")
                m "Try to remember this, Miss Granger. You can't rip me off that easily."
                call her_main("Tzzzz- I don't need your points anyway.","angry","angry")
                g9 "You may leave now."
                call her_main("I will!{w} Good day, Sir!","open","angryCl")

                call her_walk(action="leave", speed=2.5)

                call bld
                m "She might forget all about it in time."
                m "I can ask her again once I've trained her some more..."
                m "Maybe then she'll be persuaded more easily."

                $ her_mood += 6
                $ hermione_busy = True

                jump main_room


    elif her_whoring < 21:
        call her_main("Oh... My \"Quidditch equality movement\"?","soft","base")
        m "That's the one."
        call her_main("It never really got off the ground...","open","baseL")
        call her_main("No pun intended...","base","closed")
        m "(...)"
        call her_main("To be honest, I don’t have that much time apart from my visits here and studying...","open","down")
        call her_main("I might consider dropping it.","base","baseL")
        call her_main("Even though it would take away the immense pleasure of seeing Cho getting all worked up about it...","grin","base")
        m "(...)"
        call her_main("There is something I'd like from you in return, [genie_name].{p=0.8}Or else I'll' just continue with it!","base","glance")
        m "Go on girl."
        m "Tell me what you want."
        m "What you really{w}, really want..."
        call her_main("Very well, [genie_name].","soft","baseL")
        call her_main("I'll tell you what I want!","open","closed")
        call her_main("What I really, really want!","grin","glance")
        g9 "{size=-4}Nice!{/size}"
        call her_main("I’d like a seat in the teacher stands, during the Quidditch matches..","open","closed")
        m "Is that all?"
        call her_main("Oh, and a hundred points for Gryffindor...","grin","baseL")
        m "(...)"
        m "I’d say fifty would be more appropriate in this instance..."
        call her_main("Sir, it took a lot of effort to gather all those records of past Quidditch matches, throughout the whole history of Quidditch.","open","closed")
        g4 "fifty points..."
        call her_main("(...)","annoyed","angryL")
        call her_main("Very well then.","soft","closed")
        m "50 points, to the Gryffindor house..."
        $ gryffindor += 50
        call her_main("Thank you, [genie_name].","base","base")

    else:
        call her_main("My what?","open","glance")
        m "Your Quidditch movement."
        m "Regarding the male and female roles in Quidditch..."
        call her_main("Oh. I barely even remember that I did that.","annoyed","glanceL")
        m "So it wouldn't be an issue for you to drop it?"
        call her_main("I guess so...","soft","down")
        call her_main("Although, if I were to drop it...","open","down_raised")
        m "Yes?"
        call her_main("I want a seat in the teacher stands during Quidditch matches though!","grin","glance")
        m "I’m sure that could be arranged..."
        call her_main("Thank you, [genie_name].","base","glance")

    call her_main("[genie_name], may I ask.{p=0.6}What exactly were you and Cho talking about when I entered your office?","open","baseL")
    m "Oh. She just wanted my help with Quidditch."
    call her_main("Pffff-{p=0.4}Why doesn't it surprise me that she'd need your help with it.","grin","glanceL")
    call her_main("How else could she possibly win that stupid Quidditch cup...","soft","angryCl")
    m "I thought that cup was so important to you?"
    call her_main("I couldn’t care less about it, [genie_name].","open","closed")
    call her_main("The only cup that is worth winning is the \"house-cup\".","open","glanceL")
    call her_main("They’re completely different...","annoyed","angry")
    m "Totally different..."

    if her_whoring < 18:
        call her_main("It's the most prestigious award one could earn for your school-house!{p=0.6}The Quidditch cup is nothing in comparison...","open","closed")
        call her_main("Why are students even allowed to play this silly sport at our School?","annoyed","annoyed")

    if her_whoring < 8:
        call her_main("They're given the privilege of attending one of the most prestigious wizarding schools in the world...","open","angryL")
        call her_main("And they're wasting their time with some silly sports game that will get them nowhere...","open","angry")
        m "Yes. Because why enjoy yourself when you could study instead..."
        call her_main("Exactly!","normal","closed")
        m "(She's so predictable.)"

    m "Well... The quidditch teams is none of your concern anymore..."
    m "You'll tell Cho that you are sorry about your previous interferences."
    call her_main("(...)","annoyed","angry")
    m "And that the \"Quidditch equality movement\" will be...{w}\n\"no more\"."

    if her_whoring < 18:
        call her_main("Do I really have to do all that?","upset","baseL")
        m "If you want to keep on buying favours from me."
        call her_main("Ugh-{p=0.4}Very well, I guess...","soft","down")
    else:
        call her_main("Sure, whatever...","open","glanceL")


    # Summon Cho
    g9 "Great!"
    g9 "Let's call her up here then...."
    call her_main("What? Now?","clench","wide")

    # Hermione quickly gets dressed.
    if hermione_wear_top == False or hermione_wear_bottom == False:
        call her_main("Wait, she can't see me like this!","disgust","down")

        hide screen hermione_main
        with d3
        pause.8

        m "(...)"

        $ hermione_wear_top = True
        $ hermione_wear_bra = True
        $ hermione_wear_bottom = True
        $ hermione_wear_panties = True
        call update_her_body
        pause.5

    else:
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.5

    # Cho enters the office.
    call cho_walk("mid", "base", action="enter", speed=1.6)

    call cho_main("Hello, Sir.{p=0.6}You've called for me?","base","base","base","mid",xpos="base",ypos="base")
    call her_main("","normal","closed",xpos="450",ypos="base")
    call cho_main("Granger...","soft","narrow","angry","L")
    call her_main("Chang...","annoyed","angryL")
    m "Go on, girl. Tell her."
    call cho_main("Tell me what?","smile","angry","angry","mid")
    call her_main("...","annoyed","ahegao_raised")
    call her_main("About my \"Quidditch equality movement\"...","normal","closed")
    call cho_main("Did our Professor finally convince you what a terrible idea it would be?","soft","narrow","angry","mid")
    m "Actually, I still think granting more people the ability to-"
    call cho_main("*Shhush!*, Professor!{p=0.6}I’d like to hear it from her.","pout","narrow","angry","mid")
    call cho_main("I'm going to enjoy this!","horny","narrow","base","L")
    call her_main("...","annoyed","angry")
    call her_main("*Sigh*{p=0.6}I will end my movement. And I won't interfere with Quidditch again...","open","closed") #[Looking bored]
    call cho_main("This is amazing! I feel as if it's my birthday!","smile","base","base","mid")
    call her_main("After all, Quidditch is a huge waste of everyone's time.{p=0.6}Including mine...","soft","glanceL") #[Still looking bored]
    call cho_main("You're just jealous that I’m better than you at something.","smile","angry","angry","L")
    call her_main("I am not jealous!","angry","angryCl")
    m "You may go now, Miss Granger."
    call her_main("(...)","annoyed","angry")
    call her_main("Until next time, Sir.","normal","closed")
    call her_main("...","annoyed","glanceL")

    # Hermione leaves after glaring one last time at Cho.
    call her_walk(xpos="door", ypos="base", speed=2.5)
    pause.2
    call her_chibi("stand","door","base",flip=False)
    with d3
    pause.2

    call her_main("*glare*","normal","angry",ypos="head")
    # Add Cho glaring back with her 'head' image.

    call her_chibi("stand","door","base",flip=True)
    with d3
    pause.8

    call her_chibi("leave")

    call cho_main("Thank you for getting her off my back, Professor.","base","base","base","mid")
    m "No problem."
    call cho_main("Now, if you’ll excuse me. I'm expected back on the Quidditch field.","open","closed","base","mid")
    call cho_main("Just call me whenever I can be of service.","soft","narrow","base","mid")
    g9 "I will."
    call cho_main("Good day, Professor.","smile","base","base","mid")

    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    call bld
    m "That went better than expected."

    # You can now summon Cho Chang to your office.
    stop music fadeout 1.0

    $ cho_intro_state = "complete"

    $ cho_unlocked = True
    $ achievement.unlock("unlockcho")

    # End of Intro.
    $ hermione_busy = True
    $ cho_busy = True

    jump main_room
