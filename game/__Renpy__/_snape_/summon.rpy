

label summon_snape:

    call play_sound("door")

    call sna_chibi("stand","mid","base")

    call sna_main("Yes, what is it?","snape_01",xpos="base",ypos="base")

    label snape_ready:
        pass

    menu:

        # Talk
        "-Talk-":
            if not chitchated_with_snape:
                call snape_chitchat

            if (letter_curse_complaint_OBJ.read and not astoria_unlocked) or ((third_curse_got_cast or spells_unlocked) and not snape_gave_spellbook):
                menu:
                    "-Talk about the ministry letter-" if letter_curse_complaint_OBJ.read and not astoria_unlocked:
                        #You tell Snape about the curses.
                        if hermione_on_the_lookout: #Already talked to Hermione.
                            $ hermione_finds_astoria = True
                            $ days_without_an_event = 0 #So the event won't happen right after.
                        if snape_on_the_lookout:
                            call sna_main("I'm still on the lookout, Genie.","snape_01")
                            call sna_main("If I find the little maggot that casts those spells,...","snape_10")
                            call sna_main("I will crush his bones!","snape_16")
                            jump snape_ready
                        $ snape_busy = True
                        $ snape_on_the_lookout = True
                        jump letter_intro_snape

                    "-Ask for a spellbook-" if (third_curse_got_cast or spells_unlocked) and not snape_gave_spellbook:
                        $ snape_gave_spellbook = True
                        jump snape_book_intro

                    "-Never mind":
                        jump snape_ready
            else:
                if chitchated_with_snape:
                    ">You have already talked with Snape today."
                pass

            $ chitchated_with_snape = True
            jump snape_ready


        # Fireplace Chats
        "-Let's hang-" if not daytime: # Turns TRUE when friendship with Snape been maxed out.
            if one_of_ten == 10 and game_difficulty >= 2:  #Doesn't happen with easy difficulty.
                jump not_today #Snape says: "I am busy tonight."
            else:
                jump snape_dates


        # Potions
        "-Get a potion-" if her_whoring > 10:
            jump snape_potion_menu


        # Cardgame
        "-Let's Duel- {image=interface/cards.png}" if deck_unlocked:
            jump snape_duel_menu


        # Dismiss
        "-Never mind-":
            stop music fadeout 1.0

            if daytime:
                sna "Alright, back to work then..."
            else:
                sna "Goodnight then."

            call play_sound("door")

            $ snape_busy = True

            jump main_room


# Potion Menu
label snape_potion_menu:
    hide screen snape_main
    with fade

    call sna_main("I notice you're making a bit of progress on Miss Granger.","snape_37", ypos="head")
    call sna_main("I've got some potions here that normally aren't available to students.","snape_47")
    call sna_main("These might help speed up the process...","snape_47")

    menu:
        "-Lactantium-" if potion_inv.has("p_milk_potion"):
            ">You already have a Lactantium potion."
            jump snape_ready
        "-Lactantium-" if not potion_inv.has("p_milk_potion"):
            if potion_scene_11_progress < 1:
                call sna_main("Ah yes, a unique concoction of mine. I have a bottle on hand at all times.","snape_37")
                call sna_main("Just in case...","snape_41")
                call sna_main("Here, take it!","snape_02")
                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            elif potion_scene_11_progress == 1:
                call sna_main("Good work on getting her to take it.","snape_37")
                call sna_main("Her breasts did look magnificently full in class.","snape_41")
                call sna_main("mmmm, and I think she was even leaking a little...","snape_41")
                call sna_main("Get her to take another!","snape_46")
                call sna_main("Here, I'll even give you a milker for the slut!","snape_02")
                ">Snape hands you an odd leather and metal harness."
                m "What is-"
                ">Snape quickly pushes another milky potion into your hands."
                ">Milking potion received!"
                call sna_main("Don't worry about it, just get her to put it on. It's enchanted so it will handle the rest...","snape_40")
                call sna_main("but I want it back before you leave!","snape_34")
                call sna_main("I spent a fortune on the self cleaning model...","snape_46")
                $ potion_inv.add("p_milk_potion")
            else:
                call sna_main("Mmmm, I wish I could be there to see you milk her...","snape_41")
                m "..."
                m "(That's probably not a good idea...)"
                call sna_main("All that {b}delicious{/b} milk...","snape_40")
                m "(definitely not a good idea.)"
                call sna_main("...","snape_41")
                call sna_main("Well anyway, I was wondering...","snape_37")
                call sna_main("Want me to augment the potion?","snape_37")
                m "Augmented?"
                m "I never asked for this..."
                call sna_main("I know... I'm offering it...","snape_34")
                m "Oh yeah, sorry. What sort of augmentation?"
                call sna_main("Well I can leave the potion as it is...","snape_38")
                call sna_main("Or I can add an extra little something to it.","snape_40")
                m "Such as?"
                call sna_main("Well...","snape_37")
                label snape_potion_choice:
                    pass
                menu:
                    "-Normal potion-":
                        call sna_main("Here you are Mr. Adventurous...","snape_35")
                        $ potion_version = 1
                    "-futa potion-":
                        call sna_main("What? Are you sure you want this one?","snape_44")
                        call sna_main("I mean I figured you were a bit of a pervert...","snape_02")
                        call sna_main("but I didn't think...","snape_45")
                        call sna_main("Oh well, if you want it, it's yours...","snape_02")
                        menu:
                            "-give it to me-":
                                call sna_main("really?","snape_44")
                                call sna_main("you're more Adventurous than I thought!","snape_02")
                                call sna_main("Here, I'll even give you an extra attachment for the milker!","snape_46")
                                ">Snape hands you a different cannister with a soft plastic opening in the bottom. It looks almost like an anus."
                                call sna_main("I also put an undetectable extension charm on the cannister... Promise to tell me what happens!","snape_45")
                            "-no-":
                                  call sna_main("Too bad...","snape_35")
                                  jump snape_potion_choice

                        $ potion_version = 2
                    "-Permanent breast expansion-":
                        call sna_main("The milk production will still only last a day...","snape_02")
                        call sna_main("But her big boobs will be permanent...","snape_37")
                        call sna_main("Are you sure you want this?","snape_02")
                        call sna_main("She might not like it...","snape_46")
                        menu:
                            "-yes-":
                                call sna_main("Fantastic!!!","snape_45")
                            "-no-":
                                  call sna_main("Too bad...","snape_35")
                                  jump snape_potion_choice

                        $ potion_version = 3
                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            jump snape_ready

        "-Veritaserum-" if potion_inv.has("p_veritaserum"):
            ">You already have a Veritaserum potion."
            jump snape_ready
        "-Veritaserum-" if not potion_inv.has("p_veritaserum"):
            call sna_main("Truth potion.","snape_01")
            call sna_main("This is dangerous stuff Genie...","snape_01")
            call sna_main("Use it to make anyone tell the truth.","snape_47")
            call sna_main("Just not me!","snape_36")
            ">Snape hands you the tiny vial filled with a strange gold liquid."
            ">Veritaserum received!"
            $ potion_inv.add("p_veritaserum")
            jump snape_ready

        "-Voluptatem-" if potion_inv.has("p_voluptatem"):
            ">You already a bottle of Voluptatem."
            jump snape_ready
        "-Voluptatem-" if not potion_inv.has("p_voluptatem"):
            m "Volupwhatem?"
            call sna_main("This is actually an experimental potion of mine...","snape_01")
            call sna_main("I'm not sure if this is ready for testing on humans yet.","snape_35")
            ">Snape hands you the small bottle filled with a swirling pink and purple liquid."
            ">Voluptatem received!"
            $ potion_inv.add("p_voluptatem")
            jump snape_ready

        "\"Never mind.\"":
            jump snape_ready



label snape_dates:  ### HANGING WITH SNAPE ###
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    $ sna_dates_counter += 1

    show screen blkfade
    hide screen genie
    hide screen chair_right
    $ fire_in_fireplace = True
    show screen fireplace_fire
    hide screen desk
    show screen desk
    show screen with_snape_animated

    hide screen snape_stand #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    hide screen blkfade
    with fade


    # High Priority Events First!

    # Hermione
    if snape_against_hermione: #Turns True after hermione_intro_E1 (Hermione shows up for the first time).
                               #Activates special event when hanging out with Snape next time.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape

    if snape_against_hermione_02: #Activates after second visit from Hermione (hermione_intro_E2).
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_02

    # Cho
    if cho_intro_state == "talk_with_snape":
        $ cho_intro_state = "talk_with_hermione"
        jump cho_snape_talk

    # After talking to Snape about Cho.
    # If you haven't yet beaten the Quiz.
    if snape_quid_help == True and quidditch_book_1_ITEM.unlocked == False and cho_quiz_complete == False: # After failing the Quiz.
        jump ask_snape_for_quidditch_help

    # General
    if hg_pf_dance.points >= 2 and not snape_invited_to_watch: #After second dance where Snape entered room.
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
        show screen bld1
        with d3
        if game_difficulty <= 2:
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            show screen notes
            ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
            hide screen notes
        else:
            ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him hasn't improved much."
        hide screen bld1
        with d3



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


### SPECIAL DATE ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
    $ snape_against_hermione = False #Turns True after hermione_intro_E1. Activates special event (THIS EVENT) when hanging out with Snape next time.
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


    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)

    jump day_start



label special_date_with_snape_02:
    # TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
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

    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)

    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start



label special_date_with_snape_03:
    # TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
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

    $ days_without_an_event = 0 #Making sure next even will not start right away.

    jump day_start



label wine_intro:
    call bld
    m "Look what I've got!"
    call sna_main("Hm..?","snape_05", ypos="head")
    call sna_main("Let me see...")
    pause.1
    $ the_gift = "interface/icons/item_wine.png" # WINE.
    show screen gift
    with d3
    ">You hand over the bottle you found in the cupboard to professor Snape..."
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
