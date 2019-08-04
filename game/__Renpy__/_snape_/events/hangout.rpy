

### Snape Hangout Event ###

label snape_dates:

    call setup_fireplace_hangout(char="snape")

    $ sna_dates_counter += 1

    # High Priority Events First!

    # Hermione
    if hermione_intro.E1_complete and not hang_with_snape.E1_complete:
        show screen with_snape #Makes sure the scene is not animated...
        jump hang_with_snape_E1

    if hermione_intro.E2_complete and not hang_with_snape.E2_complete:
        show screen with_snape #Makes sure the scene is not animated...
        jump hang_with_snape_E2

    # Tonks
    if tonks_intro.E1_complete and not hang_with_snape.E3_complete:
        show screen with_snape #Makes sure the scene is not animated...
        jump hang_with_snape_E3

    if tonks_intro.E3_complete and not hang_with_snape.E4_complete:
        show screen with_snape #Makes sure the scene is not animated...
        jump hang_with_snape_E4

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


    if wine >= 1:
        $ sna_wine_counter += 1
        $ wine -= 1

        if not wine_intro_done: # Using Dumbledor's wine for the first time.
            $ wine_intro_done = True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
            call wine_intro
        else:
            call drink_wine


    if sna_friendship >= 5 and snape_events == 0:
        call date_with_snape_01

    elif sna_friendship >= 12 and snape_events == 1: #LEVEL 02
        call date_with_snape_02

    elif sna_friendship >= 19 and snape_events == 2: #LEVEL 03
        call date_with_snape_03

    elif sna_friendship >= 27 and snape_events == 3: #LEVEL 04
        call date_with_snape_04

    elif sna_friendship >= 34 and snape_events == 4: #LEVEL 05
        call date_with_snape_05

    elif sna_friendship >= 41 and snape_events == 5: #LEVEL 06. Can't proceed after this until her_whoring >= Lv 3.
        call date_with_snape_06

    elif sna_friendship >= 48 and snape_events == 6: #LEVEL 07
        call date_with_snape_07

    elif sna_friendship >= 55 and snape_events == 7: #LEVEL 08
        call date_with_snape_08

    elif sna_friendship >= 62 and snape_events == 8: #LEVEL 09
        call date_with_snape_09

    elif sna_friendship >= 69 and snape_events == 9: #EVENT 10
        call date_with_snape_10

    elif sna_friendship >= 76 and snape_events == 10: #EVENT 10
        call date_with_snape_11

    elif sna_friendship >= 83 and snape_events == 11: #EVENT 11
        call date_with_snape_12

    elif sna_friendship >= 88 and snape_events == 12: #EVENT 12. If her_whoring level > 5.
        call date_with_snape_13

    elif sna_friendship >= 93 and snape_events == 13: #EVENT 13
        call date_with_snape_14

    elif sna_friendship >= 98 and snape_events == 14: #EVENT 14
        call date_with_snape_15
        $ sna_friendship = 100
        $ sna_friendship_maxed = True

    else:
        call bld
        if game_difficulty <= 2:
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            show screen notes
            ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
            hide screen notes
        else:
            ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him hasn't improved much."
        call bld("hide")

    if sna_friendship < 100:
        if game_difficulty < 2: #Easy & Normal
            $ sna_friendship += 3
        elif game_difficulty == 2:
            $ sna_friendship += 1
        else:
            $ sna_friendship += 0
        if sna_friendship > 100:
            $ sna_friendship = 100

    jump day_start


label wine_intro:
    call bld
    m "Look what I've got!"
    call sna_main("Hm..?","snape_05", ypos="head")
    call sna_main("Let me see...")
    pause.1

    # Show wine
    $ the_gift = "interface/icons/item_wine.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you fond in the cupboard to professor Snape..."
    hide screen gift
    with d3

    call sna_main("This one has got to be from Albus' personal stash!","snape_24")
    call sna_main("Some pricey and incredibly rare stuff.","snape_06")
    m "Shall we then?"
    call sna_main("We most certainly shall!","snape_02")

    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Your relationship with Professor Snape has improved."
    $ sna_friendship +=1

    return


label drink_wine:
    call bld
    m "Look what I've got!"
    pause.1

    # Show wine
    $ the_gift = "interface/icons/item_wine.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you fond in the cupboard to professor Snape..."
    hide screen gift
    with d3

    call sna_main("Another one?","snape_05", ypos="head")
    if one_of_ten == 1:
        call sna_main("Splendid!","snape_02")
    elif one_of_ten == 2:
        call sna_main("Alright!","snape_02")
    elif one_of_ten == 3:
        call sna_main("Awesome!","snape_02")
    elif one_of_ten == 4:
        call sna_main("Well done, my friend!","snape_02")
    elif one_of_ten == 5:
        call sna_main("Did you find Albus' secret stash or was it his personal wine cellar?","snape_05")
    elif one_of_ten == 6:
        call sna_main("lately I am having hard time drinking anything but this!","snape_02")
    elif one_of_ten == 7:
        call sna_main("Great! I feel less stressed out already!","snape_02")
    elif one_of_ten == 8:
        call sna_main("This just keeps getting better and better!","snape_02")
    elif one_of_ten == 9:
        call sna_main("Seriously, how big is that stash?","snape_05")
    else:
        call sna_main("It's sure good to be us! let's uncork that bastard!","snape_02")

    call nar(">Your relationship with Professor Snape has improved.")
    #">Your relationship with Professor Snape has improved."

    if sna_friendship < 100: #max
        if game_difficulty < 2:      #Easy difficulty
            $ sna_friendship += 2
        elif game_difficulty == 2:   #Normal
            $ sna_friendship += 2
        else:                        #Hardcore, larger wine bonus.
            $ sna_friendship += 3

    return


label not_today:
    if one_out_of_three == 1:
        sna "Sorry, I can't tonight..."
    elif one_out_of_three == 2:
        sna "Sorry, I have other business to attend to tonight..."
    elif one_out_of_three == 3:
        sna "Sorry, I have other plans. Maybe some other time?"

    jump snape_ready



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
    call sna_main("How come one tiny....cunt, is able to cause me so much grief?!","snape_31")
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
    call sna_main("Am i?!","snape_34")
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

    "Dev Note" "Add writing in which Snape and Genie discuss the Ministry's involvement."

    $ hang_with_snape.E3_complete = True
    $ ss_event_pause += 1

    jump day_start


# You inform Snape that Tonks is now an ally and has been made a teacher.
label hang_with_snape_E4:

    "Dev Note" "Add writing in which you tell Snape that Tonks is now a teacher."

    $ hang_with_snape.E4_complete = True
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

label date_with_snape_01:
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_02:
    call bld
    m "For our little enterprise to succeed..."
    m "You need to be more generous with these house point things..."
    call sna_main("Right, of course...","snape_09", ypos="head")
    sna "Miss Granger will require a strong incentive..."
    sna "So putting my house in the lead is essential..."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_03:
    call bld
    call sna_main("Have you heard of that \"men's rights movement\" nonsense?","snape_01", ypos="head")
    sna "She is smart, popular and has a will of iron..."
    call sna_main("Lately I am starting to feel very doubtful about our whole plan...","snape_06")
    m "You shouldn't though..."
    call sna_main("Is that so...","snape_26")
    m "It may take some time, but I {size=+5}will{/size} break her."
    m "Just trust me."
    sna "Alright..."
    call sna_main("What choice do I have but to hope for the best...?","snape_06")
    call blktone

    ">You spend the evening by dreading the uncertain future with professor Snape."
    ">A faint bond of trust is forming between you two."

    call sly_plus
    call hide_blktone

    $ sna_support += 1 #Controls how many points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_04:
    call bld
    call sna_main("Tell me something, Genie...","snape_24", ypos="head")
    m "Yes?"
    call sna_main("Do you believe in the theory of parallel worlds?","snape_25")
    m "Well, it's hard not to. All things considered."
    call sna_main("True...","snape_23")
    call sna_main("So, you think somewhere out there is another version of me?","snape_05")
    m "Probably..."
    call sna_main("Hm...","snape_23")
    sna "Severus Snape - the ever cheerful white mage..."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return



label date_with_snape_05:
    call bld
    call sna_main("So... How is our little plan coming along?","snape_05", ypos="head")
    sna "Is that wretched girl giving you trouble?"

    menu:
        "\"Yeah. She's stubborn.\"":
            call sna_main("No surprise there...","snape_06")
        "\"No, not really...\"":
            call sna_main("Seriously?","snape_05")
            sna "Interesting..."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_06:
    call bld
    m "So, tell me about those \"slytherin\" sluts some more!"
    call sna_main("What can I say? Life's been good to me lately, my friend.","snape_23", ypos="head")
    call sna_main("These days I have a whole harem of skimpy students to choose from.","snape_22")
    g9 "Nice!"
    call sna_main("Yes. Thanks to you, I can do whatever the bloody hell I want!","snape_02")
    sna "And more importantly..."
    call sna_main("Whoever the hell I want!","snape_13")
    m "Seriously?"
    call sna_main("Well, sort of...","snape_09")
    sna "Obviously I don't actually walk around and \"do whoever I want\"..."
    call sna_main("But you wouldn't believe what some of those girls are willing to do in exchange for house points!","snape_13")
    call sna_main("Or even for the mere promise of good grades...","snape_22")
    pause.1
    call blktone

    ">Professor Snape's usual cold exterior disintegrates before your eyes..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus
    call hide_blktone

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_07:
    call bld
    call sna_main("So, back in your world you are some kind of all-powerful being?","snape_05", ypos="head")
    m "Yeah, sort of..."
    call sna_main("Then how come you do the bidding of that Jasmine woman?","snape_05")
    m "Oh... Well..."
    m "...she is a princess."
    call sna_main("So?","snape_05")
    sna "Is she your princess? You are not even human."
    sna "Did you swear your loyalty to her?"
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_08:
    call bld
    call sna_main("Do you think if we wanted to...","snape_05", ypos="head")
    sna "We could bring the public flogging back?"
    m "What do you mean?"
    call sna_main("Well, years ago flogging was a completely acceptable measure of punishment for the students.","snape_06")
    sna "*Sigh* Simpler times..."
    call sna_main("These days students just completely lack discipline...","snape_16")
    sna "I would like nothing more than to publicly flog every single one of them..."
    call sna_main("Especially the girls...","snape_22")
    m "Hm... Fine by me..."
    m "But won't a reform like that attract unnecessary attention towards us?"
    call sna_main("Yes. You are right of course.","snape_29")
    sna "I am getting greedy..."
    call sna_main("I'm getting drunk with power, my friend!","snape_28")
    sna "And this exquisite wine does not improve my judgment in the slightest either!"
    pause.1
    call blktone

    ">Professor Snape seems to be completely at ease around you now."
    ">The bond of male friendship between you twe strengthens even more.\n>\"Slytherin\" house point payouts have increased formidably..."

    call sly_plus
    call hide_blktone

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_09:
    call bld
    call sna_main("...so, after that I return back to Russia, right?","snape_24", ypos="head")
    g4 "Back to Russia?"
    call sna_main("But wait, it gets worse.","snape_01")
    call sna_main("Apparently I am fluent in Russian now.","snape_05")
    g4 "Wait, what?"
    call sna_main("And I am this miserable muggle guy who lives in this shithole of a town full of rundown buildings.","snape_06")
    sna "I try to make a living by drawing comics and creating games with \"Ren'Py\"..."
    call sna_main("And that is so bizarre because I don't even know what a \"Ren'Py\" is!","snape_24")
    m "Hm... Then what happened?"
    call sna_main("Not much... Mostly worked my ass off for months...","snape_05")
    sna "Then managed to create a relatively successful game somehow..."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_10:
    call bld
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_11:
    call bld
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_12:
    call bld
    call sna_main("I've been thinking about what you've said the other day...","snape_09", ypos="head")
    sna "About your home world being nothing but a scorched desert and all..."
    m "Yes?"
    call sna_main("Do you think Albus will be alright there?","snape_06")
    m "Oh, absolutely!"
    m "Since I quite literally replaced him in his chair..."
    m "He probably replaced me in exactly the same place back in Agrabah."
    call sna_main("Agrabah?","snape_05")
    m "Yes... A very big city."
    m "One of the few that rose after the great catastrophe."
    m "Probably the biggest of them all as well..."
    m "the heart of the human civilization if you will."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_13:
    call bld
    call sna_main("You know what?","snape_01", ypos="head")
    m "What?"
    call sna_main("For the first time in a very long time...","snape_01")
    call sna_main("I think...","snape_03")
    call sna_main("I am actually content with the way my life is going.","snape_25") # 0_0
    call sna_main("What an unsettling feeling...","snape_26")
    m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
    call sna_main("Could be.","snape_22")
    call sna_main("Nonetheless, you may only be training just one girl...","snape_09")
    call sna_main("But it has a great impact on my life...","snape_24")
    sna "And even the school itself..."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_14:
    call bld
    call sna_main("...so she says: \"Sir, could you choke me a little, please!\".","snape_02", ypos="head")
    call sna_main("And I am happy to oblige of course!","snape_13")
    call sna_main("So, I choke that little bitch while I'm fucking her, right?","snape_19")
    sna "And she rolls her eyes up to the point where I can't even see her pupils anymore!"
    sna "Her face turns to a cute tint of purple and she's barely breathing."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_15:
    call sna_main("It's been a while now...","snape_05", ypos="head")
    m "What do you mean?"
    call sna_main("The spell that brought you here...","snape_24")
    sna "You said it would wear off in time..."
    call sna_main("Do you feel any different?","snape_05")
    m "No... Not really..."
    m "Maybe it needs more time?"
    call sna_main("Could be...","snape_01")
    sna "Or there could be something else..."
    m "Like what?"
    call sna_main("No idea...","snape_09")
    sna "But I shall give this some more thought..."
    call sna_main("Oh, and one more thing...","snape_24")
    m "Hm...?"
    call sna_main("This time of the year is usually pretty busy...","snape_24")
    sna "Even more so now when I need to constantly cover up for Albus' absence."
    m "..................."
    call sna_main("I'm not sure if I will be able to spend my evenings with leisurely drinking wine anymore...","snape_06")
    m "Really?"
    call sna_main("Yes...","snape_06")
    sna "I'll  still be around for a quick chat from time to time, but that's about it."
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

    $ sna_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    $ sna_friendship_maxed = True # Turns TRUE when friendship with Snape been maxed out.

    return


label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">The \"Slytherin\" house point payout has increased..."
    return
