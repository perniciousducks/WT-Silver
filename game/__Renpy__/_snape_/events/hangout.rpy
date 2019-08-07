

### Snape Hangout Event ###

label snape_hangout:

    call setup_fireplace_hangout(char="snape")

    $ ss_he_counter += 1
    if wine_ITEM.number >= 1:
        $ wine_ITEM.number -= 1

    $ ss_he_drink.start()

    label snape_hangout_continue:
        hide sceen bld1
        show screen with_snape # No animation.
        with fade
        call bld

    # High Priority Events First!

    # Hermione
    if hermione_intro.E1_complete and not hang_with_snape.E1_complete:
        jump hang_with_snape_E1

    if hermione_intro.E2_complete and not hang_with_snape.E2_complete:
        jump hang_with_snape_E2

    # Tonks
    if tonks_intro.E1_complete and not hang_with_snape.E3_complete:
        jump hang_with_snape_E3

    if tonks_intro.E3_complete and not hang_with_snape.E4_complete:
        jump hang_with_snape_E4

    if hang_with_snape.E4_complete and not hang_with_snape.E5_complete:
        jump hang_with_snape_E5

    # Cho
    if cho_intro_state == "talk_with_snape":
        $ cho_intro_state = "talk_with_hermione"
        jump cho_snape_talk

    # After talking to Snape about Cho.
    # If you haven't yet beaten the Quiz.
    if snape_quid_help == True and quidditch_book_1_ITEM.unlocked == False and cho_quiz_complete == False: # After failing the Quiz.
        jump ask_snape_for_quidditch_help

    # General
    if hg_T3_strip_trigger and not snape_invited_to_watch: #After second dance where Snape entered room.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_03


    # Snape Tutor Stories.
    $ random_number = renpy.random.randint(1, 3)
    if random_number == 1:
        $ ss_he_story.start()
    else:
        call bld
        $ renpy.play('sounds/win_04.mp3')
        show screen notes
        ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
        hide screen notes


    label end_snape_hangout:
        pass

    if sna_friendship < 100: # max
        if game_difficulty < 2:      #Easy difficulty
            $ sna_friendship += 4
        elif game_difficulty == 2:   #Normal
            $ sna_friendship += 3
        else:                        #Hardcore, larger wine bonus.
            $ sna_friendship += 2

    if sna_friendship > 100:
        $ sna_friendship = 100

    if daytime:
        jump night_start
    else:
        jump day_start



label ss_he_wine_intro:
    call bld
    m "Look what I've got!"
    call sna_main("Hm..?","snape_05", ypos="head")
    call sna_main("Let me see...")
    pause.1

    # Show wine
    call give_reward(">You hand over the bottle you found in the cupboard to professor Snape...", gift="interface/icons/item_wine.png", sound=False)

    call sna_main("This one has got to be from Albus' personal stash!","snape_24")
    call sna_main("Some pricey and incredibly rare stuff.","snape_06")
    m "Shall we then?"
    call sna_main("We most certainly shall!","snape_02")

    jump snape_hangout_continue


label ss_he_wine_intro_E2:
    call bld
    m "Care for another bottle?"
    pause.1

    call give_reward(">You hand over the bottle you found in the cupboard to Professor Snape...",gift="interface/icons/item_wine.png", sound=False)

    call sna_main("Another bottle of Dumbledore's wine?","snape_05", ypos="head")
    call sna_main("Did you find Albus' secret stash or was it his personal wine cellar?","snape_05")
    m "It's more of a \"wine cabinet\", I'd say."
    m "And I believe there is more where this came from..."
    call sna_main("Seriously, how big is that stash?","snape_05")
    g9 "Why don't we find that out?"
    call sna_main("It's sure good to be us! let's uncork that bastard!","snape_02")

    jump snape_hangout_continue


label ss_he_wine_repeat:
    call bld
    m "Look what I've got!"
    pause.1

    call give_reward(">You hand over the bottle you found in the cupboard to Professor Snape...",gift="interface/icons/item_wine.png", sound=False)

    call sna_main("Another one?","snape_05", ypos="head")

    $ random_number = renpy.random.randint(1, 6)
    if random_number == 1:
        call sna_main("Splendid!","snape_02")
    elif random_number == 2:
        call sna_main("Well done, my friend!","snape_02")
    elif random_number == 3:
        call sna_main("Lately I am having hard time drinking anything but this!","snape_02")
    elif random_number == 4:
        call sna_main("Great! I feel less stressed out already!","snape_02")
    elif random_number == 5:
        call sna_main("This just keeps getting better and better!","snape_02")
    else:
        call sna_main("Let's uncork that bastard!","snape_02")

    jump snape_hangout_continue



### Events ###

label hang_with_snape_E1: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
    call sna_main("...........................","snape_31", ypos="head")
    m "...............................?"
    call sna_main("I hate her so much...","snape_08")

    menu:
        "\"Yeah! That bitch!\"":
            call sna_main("Good to know that we are on the same page...","snape_01")
            call sna_main("That girl...","snape_31")
        "\"You hate who?\"":
            call sna_main("Why would you ask that?","snape_01")
            call sna_main("That Hermione girl of course!","snape_01")
        "\"Is she that bad?\"":
            call sna_main("She is the worst!","snape_01")

    call sna_main("A top student...","snape_31")
    call sna_main("Leads all sorts of extracurricular activities and clubs...","snape_08")
    call sna_main("the president of the school's Student Representative Body...","snape_08")
    call sna_main("Likely to become the head girl soon...","snape_08")
    call sna_main("................","snape_31")
    call sna_main("............","snape_08")
    with hpunch
    call sna_main("{size=+7}I hate that fucking witch!!!{/size}","snape_33")
    g4 "{size=-4}(What the...?){/size}"
    call sna_main("..............","snape_31")
    call sna_main("She used to be just an annoyance, but these days...","snape_31")
    call sna_main("She's become a full-fledged menace...","snape_01")
    call sna_main("That witch is officially my least favorite student in the entire school now...","snape_01")
    m "What about that Potter boy?"
    call sna_main("The Potter boy? Ha! Who's that!?","snape_34")
    call sna_main("No, I'm serious...","snape_01")
    call sna_main("I will go as far as to say that Potter and his wretched father combined...","snape_01")
    call sna_main("Have never caused me as much grief as this little witch does lately...","snape_01")
    m "Now, now. We both know that's not true..."
    call sna_main("Yeah... You're probably right...","snape_31")
    call sna_main("That bastard James Potter really did a number on me--","snape_35")
    call sna_main("Wait, how do you know this?","snape_34")
    m "Well... I've read the books..."
    call sna_main("What? What books?","snape_34")
    m "Nah, never-mind. I'm a genie, remember? I know things..."
    call sna_main("Hm... And yet you need me to teach you stuff...","snape_37")
    m "Well, I told you. My magic is acting up in your world..."
    call sna_main("Sure, sure...","snape_37")
    m "......"
    m "She came by the other day..."
    call sna_main("Who did?","snape_38")
    m "The Hermione girl..."
    call sna_main("What?!","snape_01")
    call sna_main("I thought we agreed on the \"no human contact\" rule.","snape_31")
    call sna_main("(Even though lately I've been wondering whether or not she is human at all...)","snape_35")
    m "I know... She kinda forced her way in..."
    call sna_main("I imagine she did...","snape_01")
    call sna_main("What did she want?","snape_01")

    if jerked_off_during_hermione_intro:
        m "I'm not sure..."
        call sna_main("??","snape_39")
        m "I was jerking off the entire time she was talking..."
        call sna_main("You've been...","snape_31")
        call sna_main("... doing what?","snape_31")
        m "Hey, don't judge me!"
        m "You don't know what it's like to be cooped up in this tower like a prisoner!"
        call sna_main("You... y-you....","snape_31")
        call sna_main("......","snape_40")
        call sna_main("Ha.... ha-ha... HA-HA-HA!!!","snape_28")
        m "Wha..? What did I say?"
        call sna_main("Ha-ha-ha! You are amazing!","snape_42")
        call sna_main("Are all genies so... wonderfully nihilistic?","snape_37")
        m "Yeah... We immortals tend to not give a fuck."
        call sna_main("Understandable...","snape_37")
        call sna_main("Unfortunately, us mere mortals cannot afford such a luxury...","snape_38")

    else:
        m "Not sure... She was talking a lot..."
        m "Something about some \"greefeendo\" points... and..."
        m "Er... I wasn't paying attention to be honest..."
        call sna_main("Nah... Probably another load of self-righteous crap...","snape_01")
        call sna_main("She is famous for that...","snape_35")

    call sna_main("I have a class early tomorrow, so let us call it a night.","snape_35")
    m "What about you teaching me magic and stuff?"
    call sna_main("Yeah, absolutely...","snape_38")
    call sna_main("Next time...","snape_38")
    m "Alright..."


    $ hang_with_snape.E1_complete = True

    jump day_start



label hang_with_snape_E2:
    # TAKES PLACE AFTER SECOND VISIT FROM HERMIONE.
    # Where she says that she sent letter to the ministry.
    call bld
    m "......................."
    m "Hermione Granger came by again..."
    call sna_main("Don't mention the witch's name when I'm off duty...","snape_01", ypos="head")
    call sna_main("...............","snape_31")
    call sna_main("Dammit! I am a grown man, Albus!","snape_08")
    m "My name is not--"
    call sna_main("An esteemed wizard...","snape_08")
    m "Well, alright, let it out..."
    call sna_main("How come one tiny...cunt, is able to cause me so much grief?!","snape_31")
    call sna_main("I thought with you as my ally I will have a chance to--","snape_32")
    m "To unclench?"
    call sna_main("Yeah, that could be the word...","snape_31")
    call sna_main("But all I did was give her more leverage to harass me with...","snape_43")
    call sna_main("She's even turning the teachers against me now...","snape_43")
    call sna_main(".................","snape_08")
    call sna_main("She must go...","snape_35")
    m "What do you mean?"
    with hpunch
    call sna_main("{size=+6}I will have to kill her!{/size}","snape_33")
    g4 "Like, literally kill her?"
    call sna_main("Do I have any other choice?","snape_34")
    m "You're joking, right?"
    call sna_main("Am I?!","snape_34")
    call sna_main("Can you do this for me?","snape_39")
    m "Em..."
    m "As much I would \"enjoy\" murdering a teenage girl..."
    m "Genies can't kill..."
    call sna_main("Rats!","snape_35")
    m "And we frown upon murderers..."
    if jerked_off_during_hermione_intro:
        call sna_main("Really? I thought you didn't give a fuck...","snape_44")
        m "to a certain degree..."
        call sna_main(".............","snape_35")
    call sna_main("Well... don't mind me then...","snape_31")
    call sna_main("I'm all talk...","snape_31")
    call sna_main("I would never actually harm a student...","snape_31")
    call sna_main("(...permanently that is.)","snape_08")
    m "Listen, if she bugs you so much, why not just find a less radical way to deal with her?"
    call sna_main("Nah... Flogging has been outlawed for years now...","snape_35")
    m "That's not what I mean..."
    call sna_main("Huh?","snape_01")
    m "She is a top student, right?"
    call sna_main("Yes, damn her. The girl is a hard worker, I will give her that.","snape_31")
    m "She also has a reputation for being self-righteous."
    call sna_main("Oh, yes!","snape_34")
    m "And she thinks that she is better than everyone else..."
    call sna_main("Where are you going with this?","snape_44")
    m "Well, it seems like all of her power comes from her reputation..."
    call sna_main("......................?","snape_39")
    m "What if we take that away from her?"
    call sna_main("That would shut her up I suppose...","snape_38")
    call sna_main("But how? She's practically a saint.","snape_31")
    call sna_main("Even students who hate her secretly admire her.","snape_35")
    call sna_main("She hasn't failed a single test in her entire time here...","snape_31")
    call sna_main("She is always ahead of the schedule...","snape_31")
    call sna_main("Damn, how I hate it when she corrects me during my classes...","snape_08")
    call sna_main("And thanks to her the \"Gryffindor\" house is way ahead of everybody else now...","snape_34")
    call sna_main("Even \"Slytherin\" is no match for them this year...","snape_35")
    call sna_main("........................","snape_43")
    call sna_main("Dammit... I need more wine...","snape_34")
    m "The wine can wait. Hear me out!"
    call sna_main("Huh...?","snape_01")

    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label fuck_off:
    m "Hm... Let us..."
    menu:
        m "..."
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            call sna_main("What? You mean grade her unfairly?","snape_01")
            call sna_main("Nah... Dumbledore would never allow--","snape_31")
            call sna_main("Wait a second!","snape_37")
            m "Exactly!"
            call sna_main("You're right! I can grade her tests unfairly! I could even persuade other teachers to do the same!","snape_02")
            call sna_main("I could say that the order comes from you...","snape_02")
            call sna_main("And when the real Dumbledore shows up I will pretend that I had no idea that he was away...","snape_45")
            m "Works for me."
            call sna_main("Er...","snape_38")
            call sna_main("This is still you, genie, right?","snape_38")
            m "Yeah, yeah, still here..."
            call sna_main("OK, good.","snape_02")

            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Make sure \"Gryffindor\" loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            call sna_main("You mean to just start subtracting points from them for no good reason?","snape_01")
            call sna_main("Oh, I like that!","snape_02")
            call sna_main("There are a couple of \"Slytherin\" girls who are long overdue for receiving some extra house points as well.","snape_46")
            call sna_main("Oh, this will work out magnificently!","snape_45")
            call sna_main("You are a Genius!","snape_02")
            m "Yes, I am a genius genie. What are the odds of that..."

            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            call sna_main("Tarnish her reputation?","snape_01")
            call sna_main("But the girl is incorruptible...","snape_01")
            m "Nonsense!"
            m "All we need to do is convince her that she needs to make some sacrifices \"for the greater good\"."
            call sna_main("Oh, but of course...","snape_37")
            call sna_main("She would gladly \"Get her hands dirty\" to save the honour of her precious \"Gryffindor\" house!","snape_47")
            call sna_main("And when she does, we will have the leverage we need...","snape_37")

            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    call sna_main("This could actually work!","snape_37")
    m "I think so too."
    call sna_main("Oh, I feel so alive tonight!","snape_45")
    call sna_main("Pour me another goblet!","snape_28")
    call sna_main("The \"Defence Against the Dark Arts\" class will start late tomorrow!","snape_45")
    m "....."
    m "Don't you think this is a bit too brutal though?"
    m "I mean, she's just a girl..."
    call sna_main("Just a girl?","snape_36")
    call sna_main("Oh no, no, no...","snape_36")
    call sna_main("She is the embodiment of pure evil!","snape_32")
    call sna_main("If we don't do this now...","snape_31")
    call sna_main("One of those days I may just snap and \"Avada Kedavra\" her!","snape_08")
    m "You'll do what?"
    call sna_main("Murder her for real!","snape_32")
    m "Alright, alright... got it."
    m "Let's choose the lesser of two evils then."
    call sna_main("Yes...","snape_35")
    call sna_main("Now, pour me some more wine.","snape_34")

    ">You spend the rest of the evening in Snape's company drinking your worries away."

    $ hang_with_snape.E2_complete = True
    $ ss_event_pause += 1

    jump day_start


# You discuss Tonks and the Ministry with Snape.
label hang_with_snape_E3:

    call sna_main(".........................","snape_31", ypos="head")
    call sna_main("That bloody wench has outdone herself, once again!","snape_35")
    m "Granger?"
    call sna_main("Yes! Her and her cursed letters!","snape_08")
    call sna_main("I'm certain she was the one who informed the Ministry about our little escapades...","snape_16")
    call sna_main("And now we have an Auror breathing down our necks... All thanks to that mischievous little whore!","snape_15")
    m "................."
    call sna_main("....................","snape_31")
    m "On the subject of that Auror,..."
    call sna_main("Nymphadora?","snape_39")
    m "Yes, the Nympho."
    m "She came by the other day..."
    call sna_main("What?!","snape_36")
    m "Twice, actually..."
    call sna_main("And you're telling me about this... now?","snape_32")
    call sna_main("I'm surprised you didn't blow our cover right there and then...","snape_16")
    g9 "What can I say. I'm very good with the ladies!"
    call sna_main("Or you are just too lucky for your own good, more likely...","snape_43")
    m "That too, to a lesser extent..."

    if jerked_off_during_hermione_intro:
        call sna_main("Please tell me you didn't jerk off in front of her as well...","snape_03")
        m "Well..."
        call sna_main("Did you?","snape_01")
        m "Not this time..."

    call sna_main("Listen, we have to be even more cautious, now that there's an Auror making her rounds...","snape_10")
    call sna_main("They are the ministry's private investigators.","snape_35")
    call sna_main("One slip-up and they will have us locked up in no time!","snape_24")
    m "\"Us?\"...{w}what wrong did I do?"
    call sna_main("You snapped the most talented, clever, and most beloved wizard that's ever lived out of existence!","snape_10")
    m "Oh right...{w} Who again?"
    call sna_main("Albus{w} Percival{w} Wulfric{w} Brian{w} Dumbledore!","snape_34")
    m "..........................."
    m "I thought I traded places with just one person..."
    call sna_main("That \"is\" one person!","snape_30", trans="hpunch")
    call sna_main("It's our headmaster's full name. And it's your name now!{w} You best make sure to remember it.","snape_34")
    m "Yeah...{w}I'm not even going to try..."
    call sna_main("Let's just hope this whole Ministry situation will solve itself...","snape_31")

    call sna_main("Thankfully, out of all the people the ministry could have sent...","snape_06")
    call sna_main("They brought that clumsy, good-for-nothing \"hufflepuff\"...","snape_35")
    call sna_main("As long as we keep our heads down and act as if we've nothing to hide...","snape_03")
    call sna_main("There will be nothing to worry about.","snape_09")
    m "I have my doubts about that."
    call sna_main("Let her continue her little investigation. And you can be as unhelpfully helpful as usual...","snape_04")
    m "................."
    m "And what if she's not going to leave that easily?"
    m "Can you think of any spell, or potion to help us with that?"
    call sna_main("And what would this potion or spell achieve exactly?","snape_05")
    m "I don't know... Send her to the shadow realm or something?"
    call sna_main("What on earth...","snape_03")
    call sna_main("Actually, I'd rather not know...","snape_06")
    call sna_main("No, and even if there was one... we're still dealing with a trained Auror here.","snape_01")
    call sna_main("We should keep everything running as normal.","snape_35")
    call sna_main("Or as normal-as-can-be, without the real Albus...","snape_09")
    m ".................."
    call sna_main("Even if she finds any concrete proof of something going on, any involvement on our part should be kept quiet at all cost.","snape_01")
    call sna_main("And as soon as she is out of here, I'll go back to drinking wine, whilst enjoying my student's company...","snape_40")
    m "And Granger? What do you suggest we do with her?"
    call sna_main("*Tzzzgh*-{w=0.6} Like that annoying brat can do any harm to us...","snape_25")
    call sna_main("A girl her age would do anything for attention, is what I'd say...","snape_09")
    call sna_main("Do you think some students word would be as good as the headmaster's?","snape_02")
    call sna_main("The Headmaster of the most respected educational institution in the country, no less...","snape_37")
    g4 "I'm the headmaster of the most respected institution of the country!?!"
    call sna_main("It is also the only magical institution...","snape_09")
    m "...................................."

    "You spend the remaining day with Snape, drenching your worries in pleny of wine..."

    #m "So, what are your thoughts on this whole ministry situation?"
    #sna "I can't say I have a very high opinion on how those fools run the place."
    #sna "The Department of Magical Law Enforcement are a joke."
    #sna "The only decent auror they have is Alistair Moody and he's more concerned dealing with dark magic than petty rumours to get involved with this investigation."
    #sna "The minister of magic himself is a fool."
    #sna "He might bring a good smile and spirits to the people during times of rebuilding after great loss."
    #sna "But when it comes to making any worthwhile decisions or recognizing potential threats or misconduct..."
    #m "I was talking mostly about our current predicament rather thant he ministry at large..."
    #sna "I know..."
    #m "..."
    #m "Surely you must be slightly worried."
    #sna "I have committed many crimes much worse than chatting up some students, all of which I should've been incarcerated for."
    #sna "As I said, the current ministry is a shamble of what it once was... no change will come from this."
    #sna "Cornelius fudge is more interested in how the ministry looks from the outside rather than expose existing issues and dealing with them."
    #m "Such as?"
    #sna "Well, apart from leaving Hogwarts completely in the hands of the headmaster..."
    #sna "Corruption, illegal trades of magical artefacts and creatures. The list goes on..."
    #sna "The only one showing any interest in the schools business is the Head of the Department of Magical law Enforcement herself."
    #m "And that's not a problem because?"
    #sna "Because in the end you'd see a dementor getting frisky with a human before any of these things aren't getting swept under the carpet."
    #sna "You could put the tooth fairy in front of the minister and he'd still deny her existence if he were to have held that stance."
    #sna "And the other fools at the ministry would do so as well even if they witnessed it themselves."


    $ hang_with_snape.E3_complete = True
    $ ss_event_pause += 1

    jump day_start


# You inform Snape that Tonks is now an ally and has been made a teacher.
label hang_with_snape_E4:

    call sna_main(".........................","snape_31", ypos="head")
    call sna_main("So, here is the plan...","snape_03")
    call sna_main("You get a shovel and a body-bag ready, and I'll do the \"Avada Kedavra\"!","snape_01")
    m "\"Avra-ka-\"{w} What the fuck are you talking about?"
    call sna_main("Tonks! We need to get rid of her! Immediately!","snape_10")
    call sna_main("Otherwise things will never go back to how they were!","snape_03")
    m "Have you lost your mind again?"
    call sna_main("No, but I'm about to!","snape_01")
    call sna_main("I haven't had a mouth on my cock in so long...","snape_29")
    call sna_main("Please, Genie. I need a fix!","snape_19") # Weird look
    m "..................."
    call sna_main("...................","snape_19") # Weird look
    g4 "Would you stop looking at me like that!!!"
    call sna_main("What? Don't be ridiculous...","snape_14")
    m "..................."
    call sna_main("What a fool I was to believe that she'd be gone by now...","snape_31")
    call sna_main("But of course not! ","snape_32")
    call sna_main("{size=+5}Instead they made that mischievous {b}cunt{/b} a teacher!{/size}","snape_33", trans="hpunch") # Screaming
    m "Actually, that was-..."
    call sna_main("The whole universe has turned against me!","snape_43")
    call sna_main("That bloody Ministry! Curse them!","snape_35")
    call sna_main("Of course it was only a matter of time until they got themselves involved...","snape_06")
    call sna_main("We had something good, Genie. And now it's over...","snape_26")

    m "Well, lucky for us, it isn't over just yet..."
    call sna_main("What's that supposed to mean? Are you concocting something?!","snape_25")
    m "It's like you've said..."
    g9 "The situation solved itself!"
    m "She's going to join us."

    call sna_main("Join us? Doing what?","snape_05")
    g9 "Corrupting those precious little girls of course!"
    call sna_main("And according to you, Tonks wants to help us break the \"Gryffindor-Bitch\" as well?","snape_34")
    m "Yep."
    call sna_main("Ha-ha-ha!{w} That's just fucking silly!","snape_28")
    m "................"
    call sna_main("Good one...","snape_45")
    call sna_main("No seriously. What's going on?","snape_03")
    m "She asked me if she could join us..."
    call sna_main("A-ha-ha-ha-ha...","snape_28")
    m "Who do you think made her a teacher in the first place?"
    call sna_main("Stop it, please!!!","snape_42")
    m "You don't believe me..."
    call sna_main("Not a single word! A-Ha-ha-ha...","snape_28")
    m "Fair enough..."
    call sna_main("Ha-ha-ha-...{w=0.5}{nw}","snape_42")
    call sna_main("*cough*-{w=0.4}*cough*-{w=0.6}*cough*{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8}{nw}","snape_17", trans="hpunch")
    m "..............."
    call sna_main("...................","snape_31")

    call sna_main("But none of this makes any sense!","snape_03")
    m "Well, as it turns out..."
    call sna_main("She's a pervert!","snape_36") # Revelation
    m "She's a-... wait, how did you?"
    call sna_main("How could I've been so ignorant!","snape_08")
    m "Am I missing something here, you're not a mind reader, are you?"
    call sna_main("I'm a very skilled Occlumens, but no...","snape_31")
    m "(Occlu-what?)"
    m "Could you stop making up words..."
    call sna_main("It's quite obvious in hindsight...","snape_35")
    m "It{w=0.2}.{w=0.2}.{w=0.2}.{w=0.6} is?"
    call sna_main("Why would the Ministry have sent a full-fledged Auror, to deal with some eccentric insinuations made by some petty student...","snape_16")
    m "Shouldn't they?"
    call sna_main("Just because of some silly rumour about teachers having sexual intercourse with their students?","snape_34")
    m "And that's not a reasonable enough concern to send somebody to look into?"
    call sna_main("It's the Ministry we're talking about...{w=0.8} They don't give a shit...","snape_30")
    call sna_main("They wouldn't even believe it if \"you-know-who\" were to make a return...","snape_31")
    m "Who?"
    call sna_main("That Tonks had to be the only Ministry personnel that saw some truth in Granger's letters...","snape_35")
    call sna_main("What if she specifically requested to be sent here to investigate?","snape_03")
    m "She might have..."
    call sna_main("So...{w=0.4} what does she want?","snape_04")
    call sna_main("Surely she's taking the position for a reason...","snape_01")
    m "It appears that she'd like to be part of this whole favour trading business, which is also why she asked to be made a teacher..."
    m "And in return she'll keep things quiet with the ministry."

    call sna_main("*Hmm*... Not having to worry about the Ministry anymore, you say...","snape_38")
    call sna_main("And I'm supposed to believe that she'd be willing to do that for us?","snape_25")
    call sna_main("How exactly did you end up in this situation with her?","snape_04")
    m "I don't know... It just... happened."
    m "She pretty much figured everything out by herself."
    m "Straight-away even guessed that I'm a Genie..."
    call sna_main("So she knows everything? How did she?-","snape_03")
    m "It appears the \"illusion charm\" wasn't perfect. She momentarily got a glimpse through it..."
    call sna_main("That's impressive... perhaps I didn't give her enough credit...","snape_01")

    call sna_main("What a wicked-bitch!","snape_13")
    call sna_main("If only we were selling favours back then...","snape_46")
    call sna_main("You know what they say about students from \"Hufflepuff\"...","snape_20")
    call sna_main("They are quite the \"hard-working\" bunch!","snape_21")
    m "(...)"
    m "I'm calling dibs on her!"
    call sna_main("You do what?","snape_14")
    m "Dibs, she's mine. I said it first..."
    call sna_main("Are you twelve or something?","snape_04")
    m "Over Ten-thousand, actually."

    $ hang_with_snape.E4_complete = True
    $ ss_event_pause += 1

    jump day_start


label hang_with_snape_E5:

    call bld
    m "Our new partner-in-crime, is she getting on well?"
    call sna_main("Tonks? I haven't seen her since last time we talked...","snape_09", ypos="head")
    call sna_main("Shouldn't you know what that witch is up to? You made her a teacher, after all...","snape_01")
    m "I'm sure she's still just settling down..."
    call sna_main("Probably drinking booze down at Hogsmeade, more likely...","snape_35")
    call sna_main("What subject is she even supposed to teach? What did you give her?","snape_03")
    m "I have not the slightest clue..."
    call sna_main("................","snape_38")
    call sna_main("You know, I've been teaching \"Potions\" at this school for as long as I can remember...","snape_06")
    call sna_main("Of course I'm the best they have.{w=0.8} And they don't call me \"Master of Potions\" for nothing!","snape_17")
    call sna_main("But if we're honest, even a \"dim-witted Demiguise\" could teach potions to those simpletons...","snape_35")
    m "..............."
    call sna_main("But when it comes to \"Defence against the dark arts\"...","snape_03")
    call sna_main("That's a subject that requires skill and cunning!","snape_02")
    call sna_main("And a very competent and skilled teacher, to guide those hopeless souls through their lessons...","snape_40")
    call sna_main("Now, If you were to assign me for that, and give Tonks my old subject to teach...","snape_20")
    m "Yeah,...{w=0.4} I think gave that role to her..."
    call sna_main("{size=+5}You did what?!{/size}","snape_33", trans="hpunch")
    m "\"Defence against-...something-something\"..."
    call sna_main("You should have given me the \"defence against the dark arts\" position!","snape_34")
    call sna_main("And she could've had something else,...like \"muggle studies\", or something.","snape_16")
    m "First come, first served, I suppose..."
    call sna_main("Curse you...","snape_08")
    m "There wasn't really any room for me to argue with her..."
    m "It was either that, or jail."
    call sna_main("..................","snape_31")

    call sna_main("I can't say that I trust her just yet...","snape_35")
    call sna_main("Not before I get to slip in a couple drops of \"Veritaserum\" into her drink...","snape_03")
    m "\"Veritaserum?\""
    call sna_main("Truth potion!{w=0.4} I often-times use some on my \"very-attractive Slytherins\"...","snape_02")
    call sna_main("Only a single drop, and they'll tell me everything I want to know.","snape_41")
    call sna_main("Very handy should you need information to blackmail someone...","snape_46")
    call sna_main("Or learn everything about their secret fetishes...","snape_20")
    g9 "Neat!"

    "You take some time to muse about the fetishes Tonks might have..."
    "For blackmailing,... or to have some fun..."

    $ hang_with_snape.E5_complete = True
    $ ss_event_pause += 1

    jump day_start


label special_date_with_snape_03:
    # TAKES PLACE AFTER Hermione has danced for you and Snape.
    call sna_main("So...","snape_31", ypos="head")
    call sna_main("You got the girl to strip for you...","snape_35")
    call sna_main("And you didn't even invite me?!","snape_08")
    m "Well..."
    m "I don't think the girl would be willing to--"
    call sna_main("Those naked, perfectly shaped breasts...","snape_40")
    call sna_main("Those magnificent long legs...","snape_41")
    call sna_main("Her ample and tender behind...","snape_40")
    call sna_main("I've seen everything...","snape_41")
    call sna_main("I've seen it all!","snape_46")
    m "(...)"
    call sna_main("As much of a nuisance I think the girl is...","snape_43")
    call sna_main("{size=+7}I could stare at those tits all day!!!{/size}","snape_33")
    m "..."
    call sna_main("You've got to invite me next time, my friend!","snape_35")
    call sna_main("My life depends on it!","snape_36")

    menu:
        m "..."
        "-Sure, why the hell not-":
            pass
        "-Uhh-":
            pass

    call sna_main("Splendid!","snape_45")
    call sna_main("I can hardly wait I tell you!","snape_37")
    call sna_main("Do you think she will let me touch them...?","snape_47")

    ">You spend the rest of the evening in Snape's company talking about Hermione's naked breasts."

    $ snape_invited_to_watch = True

    hide screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes

    jump day_start



### Snape Narrative ###

label ss_he_story_E1:
    call bld
    m "Alright. Teach me your wand-based magic now."
    call sna_main("Sure, I could do that...","snape_23", ypos="head")
    call sna_main("Or I could tell you some more about those teenage \"slytherin\" sluts...","snape_02")
    g9 "The latter, please."
    call sna_main("Great... Get a load of this then...","snape_13")
    pause.1
    call blktone

    ">You spend the evening by discussing all sorts of inappropriate things with Professor Snape."
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You feel a faint bond forming between you two..."
    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E2:
    call bld
    m "For our little enterprise to succeed..."
    m "You need to be more generous with these house point things..."
    call sna_main("Right, of course...","snape_09", ypos="head")
    call sna_main("Miss Granger will require a strong incentive...","snape_09")
    call sna_main("So putting my house in the lead is essential...","snape_09")
    call sna_main("Could take time though...","snape_06")
    m "Take time?"
    m "Why not just award a couple of hundred points to \"Slytherin\" and be done with it?"
    call sna_main("No, we need to be discreet with this...","snape_24")
    call sna_main("Awarding a whole bunch of points to my house without any reason could draw in unnecessary attention...","snape_05")
    m "Hm... I see your point..."
    call blktone

    ">You spend the evening by conspiring against Hermione with professor Snape..."
    ">The faint bond of friendship between you two strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E3:
    call sna_main("Have you heard of that \"men's rights movement\" nonsense?","snape_01", ypos="head")
    call sna_main("She is smart, popular and has a will of iron...","snape_01")
    call sna_main("Lately I am starting to feel very doubtful about our whole plan...","snape_06")
    m "You shouldn't though..."
    call sna_main("Is that so...","snape_26")
    m "It may take some time, but I {size=+5}will{/size} break her."
    m "Just trust me."
    call sna_main("Alright...","snape_26")
    call sna_main("What choice do I have but to hope for the best...?","snape_06")
    call blktone

    ">You spend the evening by dreading the uncertain future with professor Snape."
    ">A faint bond of trust is forming between you two."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E4:
    call sna_main("Tell me something, Genie...","snape_24", ypos="head")
    m "Yes?"
    call sna_main("Do you believe in the theory of parallel worlds?","snape_25")
    m "Well, it's hard not to. All things considered."
    call sna_main("True...","snape_23")
    call sna_main("So, you think somewhere out there is another version of me?","snape_05")
    m "Probably..."
    call sna_main("Hm...","snape_23")
    call sna_main("Severus Snape - the ever cheerful white mage...","snape_23")
    m "Sure, why not?"
    call sna_main("What unsettling imagery you put into my mind...","snape_03")
    m "How about another version of that Granger girl?"
    call sna_main("Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!","snape_02")
    m "And what if in that other world the cheerful Severus teams up with some bizarre version of me?"
    m "And maybe together we train the slut Hermione to be a proper girl and a good student?"
    call sna_main("Ha-ha-ha! That's hilarious!","snape_28")
    pause.1
    call blktone

    ">You spend the evening by discussing science, metaphysics, philosophy and sluts."
    ">the bond of friendship between you and Professor Snape strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout



label ss_he_story_intro_E5:
    call sna_main("So... How is our little plan coming along?","snape_05", ypos="head")
    call sna_main("Is that wretched girl giving you trouble?","snape_05")

    menu:
        "\"Yeah. She's stubborn.\"":
            call sna_main("No surprise there...","snape_06")
        "\"No, not really...\"":
            call sna_main("Seriously?","snape_05")
            call sna_main("Interesting...","snape_05")

    call sna_main("But you are positive you will be able to break her?","snape_01")
    m "Oh, absolutely."
    m "It may take some time though..."
    call sna_main("Well, we do have time...","snape_06")
    call sna_main("You are still pretty much powerless, right?","snape_05")
    m "Yeah, pretty much..."
    call sna_main("Splendid!","snape_02")
    m "......................."
    call sna_main("I mean, it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?","snape_29")
    m "Right..."
    call blktone

    ">Professor Snape seems to feel awkward about benefitting from your misery..."
    ">The bond of friendship between you two strengthens slightly..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_E6:
    call bld
    m "So, tell me about those \"slytherin\" sluts some more!"
    call sna_main("What can I say? Life's been good to me lately, my friend.","snape_23", ypos="head")
    call sna_main("These days I have a whole harem of skimpy students to choose from.","snape_22")
    g9 "Nice!"
    call sna_main("Yes. Thanks to you, I can do whatever the bloody hell I want!","snape_02")
    call sna_main("And more importantly...","snape_02")
    call sna_main("Whoever the hell I want!","snape_13")
    m "Seriously?"
    call sna_main("Well, sort of...","snape_09")
    call sna_main("Obviously I don't actually walk around and \"do whoever I want\"...","snape_09")
    call sna_main("But you wouldn't believe what some of those girls are willing to do in exchange for house points!","snape_13")
    call sna_main("Or even for the mere promise of good grades...","snape_22")
    pause.1
    call blktone

    ">Professor Snape's usual cold exterior disintegrates before your eyes..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E7:
    call sna_main("So, back in your world you are some kind of all-powerful being?","snape_05", ypos="head")
    m "Yeah, sort of..."
    call sna_main("Then how come you do the bidding of that Jasmine woman?","snape_05")
    m "Oh... Well..."
    m "...she is a princess."
    call sna_main("So?","snape_05")
    call sna_main("Is she your princess? You are not even human.","snape_05")
    call sna_main("Did you swear your loyalty to her?","snape_05")
    m "Not really..."
    call sna_main("Why do you even bother then?","snape_06")
    call sna_main("The way I see it, you are an all-powerful being and she is just some muggle...","snape_09")
    m "She's a what?"
    call sna_main("A human... She's just a human...","snape_25")
    call sna_main("So why bother trying to please her?","snape_05")
    m "Well it's complicated..."
    call sna_main("..............","snape_05")
    m ".................."
    call sna_main("She's hot, isn't she?","snape_02")
    m "Smoking..."
    call sna_main("Gotcha.","snape_23")
    pause.1
    call blktone

    ">You and professor Snape share a bitter-sweet moment of complete male solidarity."
    ">The bond of your friendship strengthens."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E8:
    call bld
    call sna_main("Do you think if we wanted to...","snape_05", ypos="head")
    call sna_main("We could bring the public flogging back?","snape_05")
    m "What do you mean?"
    call sna_main("Well, years ago flogging was a completely acceptable measure of punishment for the students.","snape_06")
    call sna_main("*Sigh* Simpler times...","snape_06")
    call sna_main("These days students just completely lack discipline...","snape_16")
    call sna_main("I would like nothing more than to publicly flog every single one of them...","snape_16")
    call sna_main("Especially the girls...","snape_22")
    m "Hm... Fine by me..."
    m "But won't a reform like that attract unnecessary attention towards us?"
    call sna_main("Yes. You are right of course.","snape_29")
    call sna_main("I am getting greedy...","snape_29")
    call sna_main("I'm getting drunk with power, my friend!","snape_28")
    call sna_main("And this exquisite wine does not improve my judgment in the slightest either!","snape_28")
    pause.1
    call blktone

    ">Professor Snape seems to be completely at ease around you now."
    ">The bond of male friendship between you twe strengthens even more.\n>\"Slytherin\" house point payouts have increased formidably..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E9: # Replace this event.
    call sna_main("...so, after that I return back to Russia, right?","snape_24", ypos="head")
    g4 "Back to Russia?"
    call sna_main("But wait, it gets worse.","snape_01")
    call sna_main("Apparently I am fluent in Russian now.","snape_05")
    g4 "Wait, what?"
    call sna_main("And I am this miserable muggle guy who lives in this shithole of a town full of rundown buildings.","snape_06")
    call sna_main("I try to make a living by drawing comics and creating games with \"Ren'Py\"...","snape_06")
    call sna_main("And that is so bizarre because I don't even know what a \"Ren'Py\" is!","snape_24")
    m "Hm... Then what happened?"
    call sna_main("Not much... Mostly worked my ass off for months...","snape_05")
    call sna_main("Then managed to create a relatively successful game somehow...","snape_05")
    call sna_main("Eventually began to make decent money with my craft...","snape_24")
    call sna_main("And then, just when I was about to allow myself to feel hopeful about the future...","snape_06")
    call sna_main("I woke up...","snape_04")
    call sna_main("....................","snape_09")
    m "......................"
    call sna_main("What do you think all of that means?","snape_05")
    m "Some form of self insert, probably."
    call sna_main("What?","snape_05")
    m "Just ignore the whole thing."
    m "A silly dream, nothing more."
    call sna_main("Felt more like a nightmare...","snape_29")
    pause.1
    call blktone

    ">Professor Snape trusts you more than he used to..."
    ">(To the point where he doesn't think twice about sharing his weird-ass dreams with you)."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E10:
    call sna_main("What is the meaning of life, Genie?","snape_29", ypos="head")
    g4 "What?"
    call sna_main("Since you are an all-powerful being, you've got to know things like that, right?","snape_05")
    m "Maybe..."
    call sna_main("Great. Tell me then.","snape_06")
    m "Hm... You sure you're ready for this?"
    call sna_main("Yes. Lay it on me, friend.","snape_05")
    m "Alright then..."
    call sna_main("................!","snape_01")
    m "It's plastic..."
    call sna_main("I beg your pardon?","snape_05")
    m "it's plastic..."
    call sna_main("I don't get it...","snape_25")
    m "This planet plans to evolve into something else in a million years or so..."
    m "In order to do that it needs a special kind of material that it can't produce on it's own."
    m "So it spawns a new form of life - humans."
    call sna_main("..............","snape_11")
    m "You wanted to know the purpose of your existence?"
    m "It's to produce plastic. Simple as that."
    call sna_main("Are you fucking kidding me?!","snape_30")
    call sna_main("No, no... That can't be it...","snape_26")
    g9 "He-he..."
    call sna_main("Are you pulling my leg?","snape_25")
    g9 "You should've seen your face."
    call sna_main("You really got me worried there, you bloody non-human bastard!","snape_15")
    g9 "I know! It was hard to resist..."
    call blktone

    ">You spend the evening by skillfully avoiding a whole variety of similar questions."
    ">Despite your refusal to cooperate the bond of friendship between you two strengthens yet again."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E11:
    call sna_main("So... Back in your world, do you people have a country named England?","snape_05", ypos="head")
    m "We used to..."
    call sna_main("What happened?","snape_26")
    m "\"The great catastrophe\"..."
    m "It incinerated most of the worlds population in a matter of hours..."
    call sna_main("................","snape_26")
    m "Turning about eighty percent of the planet's surface into a scorching desert..."
    m "And the remaining twenty percent into an icy wasteland..."
    m "............."
    call sna_main("That is...","snape_26")
    call sna_main("Horrible...","snape_06")
    call sna_main("Are you sure that you want to return to that place?","snape_25")
    m "Of course."
    m "It may be a bit barbaric, but hey... it's home."
    call blktone

    ">Professor Snape finds a new level of respect for you..."
    ">The bond of friendship between you two solidifies."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E12:
    call sna_main("I've been thinking about what you've said the other day...","snape_09", ypos="head")
    call sna_main("About your home world being nothing but a scorched desert and all...","snape_09")
    m "Yes?"
    call sna_main("Do you think Albus will be alright there?","snape_06")
    m "Oh, absolutely!"
    m "Since I quite literally replaced him in his chair..."
    m "He probably replaced me in exactly the same place back in Agrabah."
    call sna_main("Agrabah?","snape_05")
    m "Yes... A very big city."
    m "One of the few that rose after the great catastrophe."
    m "Probably the biggest of them all as well..."
    m "The heart of the human civilization if you will."
    call sna_main("I am relieved to hear that...","snape_23")
    m "Sure..."
    m "Although if your Albus friend really materialized in exactly the same spot I occupied before I casted the spell..."
    m "I suppose the princess could have him beheaded..."
    call sna_main("WHAT?!","snape_01")
    m "But the probabilty of that happening is very slim..."
    m "About five percent... Maybe ten... Twenty percent tops."
    call sna_main(".......................................................","snape_03")
    pause.1
    call blktone

    ">Professor Snape seems grateful to you for (sort of) putting his concerns about Albus Dumbledore's well-being to rest..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E13:
    call sna_main("You know what?","snape_01", ypos="head")
    m "What?"
    call sna_main("For the first time in a very long time...","snape_01")
    call sna_main("I think...","snape_03")
    call sna_main("I am actually content with the way my life is going.","snape_25") # 0_0
    call sna_main("What an unsettling feeling...","snape_26")
    m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
    call sna_main("Could be.","snape_22")
    call sna_main("Nonetheless, training that girl had such a great impact on my life...","snape_24")
    call sna_main("And even the school itself...","snape_24")
    m "In other words you are getting less broody and you blame me."
    call sna_main("Something like that...","snape_23")
    call sna_main("I'm losing my dark presence, man.","snape_28") # :)
    pause.1
    call blktone

    ">Professor Snape really did become a little more cheerful lately..."
    ">He even looks younger now than back when you first met him..."
    ">Professor Snape's feeling of gratitude fortifies the bond of your friendship."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_E14:
    call sna_main("...so she says: \"Sir, could you choke me a little, please!\"","snape_02", ypos="head")
    call sna_main("And I am happy to oblige of course!","snape_13")
    call sna_main("So, I choke that little bitch while I'm fucking her, right?","snape_19")
    call sna_main("And she rolls her eyes up to the point where I can't even see her pupils anymore!","snape_19")
    call sna_main("Her face turns to a cute tint of purple and she's barely breathing.","snape_19")
    call sna_main("So I think that maybe I should loosen up my grip a little...","snape_14")
    call sna_main("And that's when the bitch starts to cum!","snape_21")
    m "Sweet! And then you woke up?"
    call sna_main("What? No, it actually happened.","snape_05")
    call sna_main("I finally nailed that blond witch from \"Slytherin\".","snape_13")
    g9 "Nice!"
    call sna_main("I know.","snape_13")
    call sna_main("She is pretty twisted though...","snape_25")
    call sna_main("And I mean really fucking messed up.","snape_26")
    g9 "Our type of girl!"
    call sna_main("Exactly!","snape_22")
    pause.1
    call blktone

    ">You and professor Snape bond over the similarities of your taste in women."
    ">The bond of your friendship has never been stronger."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label ss_he_story_intro_E15:
    call sna_main("It's been a while now...","snape_05", ypos="head")
    m "What do you mean?"
    call sna_main("The spell that brought you here...","snape_24")
    call sna_main("You said it would wear off in time...","snape_24")
    call sna_main("Do you feel any different?","snape_05")
    m "No... Not really..."
    m "Maybe it needs more time?"
    call sna_main("Could be...","snape_01")
    call sna_main("Or there could be something else...","snape_01")
    m "Like what?"
    call sna_main("No idea...","snape_09")
    call sna_main("But I shall give this some more thought...","snape_09")
    call sna_main("Oh, and one more thing...","snape_24")
    m "Hm...?"
    call sna_main("This time of the year is usually pretty busy...","snape_24")
    call sna_main("Even more so now when I need to constantly cover up for Albus' absence.","snape_24")
    m "..................."
    call sna_main("I'm not sure how often I will be able to spend my evenings with leisurely drinking wine anymore...","snape_06")
    m "Really?"
    call sna_main("Yes...","snape_06")
    call sna_main("I'll still be around for a quick chat from time to time, but that's about it.","snape_06")
    m "I see..."
    m "I will have to find another way of spending my evenings from now on then..."
    call sna_main("I'm sure miss granger will be happy to help.","snape_02")
    m "Yes, for as long as \"slytherin\" is in the lead."
    call sna_main("Seriously? She still cares about that?","snape_05")
    m "Very much so."
    call sna_main("Well in that case I shall personally ensure that \"slytherin\" house gets as many house points as possible.","snape_23")
    pause.1
    call blktone

    ">Your friendship level with professor Snape reached its maximum value."
    ">Congratulations. If this were a \"dating-sim\" you would be getting the ending with Severus Snape."
    ">The \"Slytherin\" house point payout has increased greatly and reached it's maximum level as well."

    call sly_plus
    call hide_blktone

    jump end_snape_hangout


label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">The \"Slytherin\" house point payout has increased..."
    return
