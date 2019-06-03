

### Tier 1 ###

# Doesn't exist.
# Tier 1 always fails.



### Tier 2 ###

label hg_pf_grope_ass_T1:
    stop music fadeout 5.0
    call hg_chibi_transition("grope_ass", flip=False, trans="d7")

    call her_main("[genie_name]!?","mad","wide", cheeks="blush", ypos="head")
    m "Relax, [hermione_name]. It will be the easiest [current_payout] points you've ever made, I promise."
    m "All I am going to do is squeeze your little butt a couple of times..."
    call her_main("No! I demand you to stop!","scream","angryCl", cheeks="blush")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d5")

    call her_main("This is inappropriate, [genie_name]................","angry","angryCl", cheeks="blush")
    m "Nobody needs to know how exactly you got the points..."
    call her_main("But....","annoyed","angry")
    m "Do it for \"Gryffimdor\"..."
    call her_main("(These [current_payout] points could really make a difference...)","disgust","down_raised", cheeks="blush")
    call her_main("(Darn it.....!)","angry","worriedCl", cheeks="blush")
    call her_main("(...............................)","annoyed","angryL", cheeks="blush")

    call her_main("Can I at least turn around then, Sir?","soft","angry", cheeks="blush")

    menu:
        m "*Hmm*..."

        "\"Yes. Turn around, [hermione_name].\"": # Can fail
            jump hg_pf_grope_ass_T1_back

        "\"No. Just stand still, [hermione_name].\"": # Fails
            jump hg_pf_grope_ass_T1_front



label hg_pf_grope_ass_T1_front:
    call hg_chibi_transition("stand_behind_desk", trans="d7")

    call her_main("(...)","disgust","down", cheeks="blush", ypos="head")

    call hg_chibi_transition("grope_ass", flip=False, trans="d5")
    call ctc

    call her_main("(...)","disgust","down_raised", cheeks="blush")
    call her_main("I'm sorry, Sir. But I can't do this!","soft","down_raised", cheeks="blush")
    m "What is the problem, [hermione_name]?"

    call hg_chibi_transition("stand", xpos="desk", ypos="base", flip=False, trans="fade")

    "Dev Note" "Add more writing."

    call her_main("Good day, Sir.","disgust","down", cheeks="blush")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 4

    jump end_hermione_event



label hg_pf_grope_ass_T1_back:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")

    call her_main("As you say, [genie_name]...","annoyed","angryL", cheeks="blush")

    call hg_chibi_transition("stand_behind_desk", flip=True, trans="d5")
    call ctc

    call her_main(".............","annoyed","angryL", cheeks="blush")
    call her_main("...........................","annoyed","angry", cheeks="blush")
    call her_main("[genie_name], I would like to be done with this sooner rather then later...","soft","angryCl", cheeks="blush")
    m "Don't rush me [hermione_name]... Let me savour the moment..."
    call her_main(".............................","annoyed","angryL", cheeks="blush")

    menu:
        m "Hm..."
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T1_continue

        "-Give her butt a slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
    call her_main("[genie_name]!!?","scream","wide", cheeks="blush")

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main(".......................","annoyed","angryL", cheeks="blush")

            jump hg_pf_grope_ass_T1_continue

        "-Give her butt another slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
    call her_main("[genie_name], what are you doing!?","angry","angryCl", cheeks="blush")
    call her_main("You said all you were going to do is touch!","angry","angry", cheeks="blush")

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main(".......................","annoyed","angryL", cheeks="blush")

            jump hg_pf_grope_ass_T1_continue

        "-Give her butt another slap-":
            $ her_mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    call her_main("Ouch! It hurts!","angry","angryCl", cheeks="blush")
    call her_main("This is so demeaning!","angry","angry", cheeks="blush")
    call her_main("You said all you were going to do is touch...","angry","angry", cheeks="blush")
    g4 "Just stand still, [hermione_name]!"
    call her_main("I don't think so, [genie_name]!","angry","worriedCl", cheeks="blush")
    call her_main("No amount of points are worth this humiliation!","scream","angry", cheeks="blush",emote="01")
    call her_main("You are abusing your power, [genie_name]!","scream","angry", cheeks="blush",emote="01")
    g4 "What?"
    call her_main("I'm leaving!","angry","worriedCl", cheeks="blush", ypos="head")

    call hg_chibi_transition("stand", xpos="desk", ypos="base", trans="fade")

    # Event Fails
    menu:
        g4 "Tsk..."
        "\"I... I apologize...\"":
            call her_main("An apology won't be enough, [genie_name]!","angry","angry", cheeks="blush")
            m "What else do you want? More points?"
            call her_main("Yes, I believe I'm owed at least that much!","angry","angry", cheeks="blush")
            m "[current_payout] is what we agreed on. You won't get any more than that."
            call her_main("*tzzh*... Fine!","clench","angryCl", cheeks="blush")
            call her_main("Keep your points.","angry","angry", cheeks="blush")
            call her_main("All of them! I don't even want them anymore.","scream","angryCl", cheeks="blush")
            m "Are you sure about that?"
            call her_main("I'm leaving. Good day, Sir.","angry","angry", cheeks="blush")

            call her_walk(action="leave", speed=3)

            call bld
            m "(Whatever...)"

            $ her_mood += 15

            jump end_hermione_event

        "\"You are not getting any points for this!\"":
            call her_main("Ha! See if I care, [genie_name]!","angry","angry", cheeks="blush")

            call her_walk(action="leave", speed=3)

            call bld
            g4 "*Tsk!* (You little brat!)"

            $ her_mood += 20

            jump end_hermione_event

        "\"I'm subtracting points from you then!\"":
            call her_main("You can't be serious!?","scream","wide", cheeks="blush")
            g4 "The \"Gryffindor\" house, minus 10 points!"
            g4 "There! It's done!"
            call her_main("Gr...........","angry","angry", cheeks="blush")
            call her_main("........................","angry","angry", cheeks="blush")
            call her_main("This is not fair...","angry","suspicious", cheeks="blush", tears="messy")
            m "What? Hey, wait, don't you start crying on me..."
            call her_main("I hate you, [genie_name]! I hate you!","scream","worriedCl", cheeks="blush", tears="messy")

            # Hermione runs out of the room.
            call her_walk(action="run", speed=2, loiter=False)
            call play_sound("door")
            pause.2

            call bld
            m ".............."

            menu:
                "\"Dammit. Now I feel like crap...\"":
                    m "Dammit... Now I feel like crap..."
                    g9 "But who could resist slapping that little behind of her's?"
                "\"She made me do this, that brat!\"":
                    g4 "She made me do this, that brat!"
                    m "Acting all wounded now..."
                    g9 "I bet she actually enjoyed the slapping and just won't admit it..."

            $ gryffindor -=10
            $ her_mood += 30

            jump end_hermione_event



label hg_pf_grope_ass_T1_continue:
    call hg_chibi_transition("grope_ass", flip=True, trans="d7")
    # show screen groping_02
    call ctc

    call her_main("..............","annoyed","angryL", cheeks="blush")
    call nar("*squeeze* *squeeze* *squeeze*...")

    call her_main(".........................","annoyed","angry", cheeks="blush")
    call her_main("(I can't believe this is really happening...)","disgust","worriedCl", cheeks="blush")
    call her_main("If you don't mind, Sir...","soft","worriedCl", cheeks="blush")
    call her_main("I'd like you to unhand me now...","disgust","worried", cheeks="blush")
    m "What? Already?"
    call her_main("Yes! This has been demeaning enough!","annoyed","angry", cheeks="blush")
    call her_main("Please let go of me, Sir.","soft","angry", cheeks="blush")
    m "Fine..."
    call nar(">You give her butt one last squeeze...")
    call her_main("...................","annoyed","angryL", cheeks="blush")

    jump end_hg_pf_grope












### Tier 3 ###

label hg_pf_grope_ass_T2:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")

    call her_main("Do you want me to turn around then, [genie_name]?","base","baseL", cheeks="blush", ypos="head")

    call play_music("playful_tension") # SEX THEME.

    menu:
        m "Hm..."
        "\"Yes. Turn around, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","base","baseL", cheeks="blush")

            jump hg_pf_grope_ass_T2_back

        "\"No. Just stand still, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","annoyed","angryL", cheeks="blush", ypos="head")

            jump hg_pf_grope_ass_T2_front



label hg_pf_grope_ass_T2_front:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")
    #show screen no_groping_01
    call ctc

    call her_main("[genie_name], please hurry up, before someone discovers us like this...","soft","baseL", cheeks="blush", ypos="head")
    m "What's the problem, [hermione_name]?"
    m "You know you are doing this for your house."
    call her_main("I do know.","annoyed","angryL", cheeks="blush")
    call her_main("But not everyone would see it that way...","annoyed","angryL", cheeks="blush")
    call her_main("So let us be done with this as quick as possible...","annoyed","angryL", cheeks="blush")
    call her_main("Please...","open","baseL", cheeks="blush")
    m "Well, if you insist..."
    show screen groping_01
    with d7

    call her_main("!!!","mad","wide", cheeks="blush")
    m "What is it?"
    call her_main("nothing, [genie_name]. Your hands are cold, that's all...","open","baseL", cheeks="blush")

    call nar(">You run your hands up and down Hermione's legs...")
    call her_main(".........................","annoyed","angryL", cheeks="blush")

    call nar(">And give her Ass a good squeeze...")
    call her_main(".................","angry","worriedCl", cheeks="blush")
    m "Don't look away, girl. I want you to look into my eyes."
    call her_main("I would rather not, [genie_name]...","angry","worriedCl", cheeks="blush")

    menu:
        m "..."
        "\"Fine. Just keep on standing still then.\"":
            call her_main("Thank you, [genie_name]...","angry","worriedCl", cheeks="blush", ypos="head")

            call nar(">You massage her ass-cheeks lightly...")
            call her_main("....................","angry","worriedCl", cheeks="blush")

            call nar(">And keep enjoying the sensation of her butt under your hands...")
            call her_main(".....................","angry","worriedCl", cheeks="blush")

            call nar(">Then You give Hermione's butt one last squeeze.")
            call her_main(".....................","angry","worriedCl", cheeks="blush")

            jump end_hg_pf_grope

        "\"Open your eyes, or you'll lose the points!\"":
            $ her_mood += 10

            call her_main("Tsk! {size=-5}(You perverted old--{/size}","angry","worriedCl", cheeks="blush", ypos="head")
            m "Did you say something, [hermione_name]?"
            call her_main("It's nothing, [genie_name].","angry","angry")

            call nar(">You massage her ass-cheeks lightly...","start")
            call nar(">Hermione maintains eye contact as she's been told...","end")

            call her_main("....................","angry","angry")
            call her_main("...............................","annoyed","angryL", cheeks="blush")
            m "What did I tell you about looking away?"
            call her_main("Yes, I remember...","angry","worriedCl", cheeks="blush")
            call her_main(".................................","angry","angry")
            call her_main("...................................","annoyed","angryL", cheeks="blush")
            call her_main("..................................................","annoyed","angryL", cheeks="blush")

            call nar(">You keep enjoying the sensation of her soft buttocks under your fingertips...")
            call her_main(".....................","angry","angry")

            call nar(">Then You give Hermione's butt one last squeeze.")
            call her_main(".....................","annoyed","angry", cheeks="blush")

            jump end_hg_pf_grope



label hg_pf_grope_ass_T2_back:
    call hg_chibi_transition("stand_behind_desk", flip=True, trans="d7")
    # show screen no_groping_02
    call ctc

    call her_main(".............","base","ahegao_raised", cheeks="blush")

    menu:
        m "Hm..."
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T2_continue

        "-Give her butt a slap-":
            call slap_her
            call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
            call her_main("[genie_name]....?","base","baseL", cheeks="blush")

            pass

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main("It's Ok...","base","baseL", cheeks="blush")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            call slap_her
            call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
            call her_main("[genie_name], what are you doing!?","base","baseL", cheeks="blush")
            call her_main("You said all you are going to do is touch!","base","baseL", cheeks="blush")

            pass

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            call her_main("It's not a big deal...","base","baseL", cheeks="blush")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            call slap_her

            call her_main("[genie_name], not so loud, please...","silly","ahegao_raised", cheeks="blush")
            call her_main("What if somebody hears us?","silly","ahegao_raised", cheeks="blush")
            m "Alright, alright... proceeding with groping then..."
            call her_main("................","base","baseL", cheeks="blush")

            jump hg_pf_grope_ass_T2_continue



label hg_pf_grope_ass_T2_continue:
    call hg_chibi_transition("grope_ass", flip=True, trans="d7")
    # show screen groping_02
    call ctc

    call her_main("...................","base","baseL", cheeks="blush", ypos="head")
    m "You are being awfully quiet today, [hermione_name]."
    call her_main("Am I...?","base","baseL", cheeks="blush")

    if her_tier <= 5:
        call her_main("Well, you know me, [genie_name]...","base","ahegao_raised", cheeks="blush")
        call her_main("I'm just happy to be able to do my part for the \"Gryffindor\" house....","base","ahegao_raised", cheeks="blush")
    else:
        call her_main("Please don't mind it and continue...","base","ahegao_raised", cheeks="blush")
        call her_main("(...to grope me...)","base","glance", cheeks="blush")

    call nar(">You keep on playing with Hermione's ass...","start")
    call nar(">And continue sliding your hands up and down her inner tighs...","end")

    call her_main("................","base","baseL", cheeks="blush")

    call her_main("!!!!!!?","mad","wide", cheeks="blush", ypos="head")
    m "What is it, [hermione_name]?"
    call her_main("It's nothing [genie_name]...","angry","worriedCl", cheeks="blush")
    call her_main("It's just... ","angry","worriedCl", cheeks="blush")
    call her_main("This is so... inappropriate...","angry","worriedCl", cheeks="blush")
    m "Relax, [hermione_name]. It's not like you are enjoying this..."
    call her_main("What? Of course not! This is depraved...","angry","worriedCl", cheeks="blush")
    call her_main("I am making this sacrifice for the the honour of my house...","angry","worriedCl", cheeks="blush")
    m "Yes, concentrate on that..."
    call her_main("....................","angry","angry", cheeks="blush")
    call ctc

    call her_main("But, [genie_name]...","open","baseL", cheeks="blush")
    call her_main("Why are {size=+7}you{/size} doing this?","open","baseL", cheeks="blush")

    menu:
        m "Hm..."
        "\"I have my reasons...\"":
            call her_main("Oh...","disgust","down_raised", cheeks="blush")
            call her_main("Hm...","annoyed","angryL", cheeks="blush")

        "\"In the name of science of course!\"":
            call her_main("Really?!","soft","wide")
            call her_main("Is this research of some kind?","soft","wide")
            m "Yeah, sure, I'm researching ehm... er..."
            m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
            call her_main("I see...","soft","wide")
            call her_main("Well, if it is for research then I am glad to be of help...","annoyed","angryL")

        "-Just squeeze her butt cheeks tighter-":
            call nar(">You give Hermione's butt cheeks a couple of extra firm squeezes.")
            call her_main("....................","open","baseL", cheeks="blush")
            call her_main("(Shall I just be quiet, then.....?)","disgust","down_raised", cheeks="blush")

    call nar(">You keep on playing with Hermione's buttocks...","start")

    call nar(">You slide your hands up and down her inner tighs...","end")

    call her_main("................","angry","worriedCl", cheeks="blush")

    menu:
        "-Slide your hands under her panties-":
            call nar(">You slowly slide one of your hands under the fabric of the girl's panties...")
            call her_main("[genie_name]... What are you...?","mad","wide", cheeks="blush", ypos="head")
            m "That's alright, just think about those 15 points your house is about to receive..."
            call her_main(".............","disgust","down_raised", cheeks="blush")

            pass

        "-No. That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    menu:
        "-Prod her pussy with one of your fingers-":
            call nar(">You slide one of your fingers down and place it against the girl's little slit...")
            call her_main("[genie_name]? No! What are you...?","mad","wide", cheeks="blush")
            call nar(">Hermione tries to pull away from you...")
            $ her_mood += 3

            menu:
                "-Force your finger into her pussy!-":
                    ">You force one of your fingers into her little pussy..."
                    ">It's very tight and warm..."
                    ">Also it is relatively dry... Doesn't look like Hermione's taking any pleasure in this..."

                    jump hg_pf_grope_ass_T2_fail

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butt-hole instead-":
            call nar(">You place your one of your thumbs against the girl's little butt-hole...")
            call her_main("[genie_name]? No! What are you doing!?","mad","wide", cheeks="blush")
            call nar(">Hermione tries to pull away from you...")
            $ her_mood += 3

            menu:
                "-Force your thumb into her butt-hole-":
                    call nar(">You force one of your thumbs into her little butt-hole...")
                    with hpunch
                    call her_main("!!?","angry","wide")
                    call nar(">It's very tight and warm inside...")

                    jump hg_pf_grope_ass_T2_fail

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope



label hg_pf_grope_ass_T2_fail:
    call her_main("NO! What have you done!!?","angry","worriedCl", cheeks="blush", tears="soft_blink", ypos="head")
    call nar(">Hermione gives you an unexpectedly strong shove...")

    call hg_chibi_transition("stand_behind_desk", flip=False, trans="hpunch")

    call her_main("Why would you do this to me, [genie_name]...?","angry","worriedCl", cheeks="blush", tears="soft_blink")
    call her_main("I never agreed to... to...","angry","worriedCl", cheeks="blush", tears="crying_blink")
    call her_main("You... you...","angry","worriedCl", cheeks="blush", tears="crying_blink")
    call her_main("{size=+7}YOU RAPED ME!{/size}","scream","worriedCl", cheeks="blush", tears="messy", trans="hpunch")
    g4 "What? Don't be ridiculous, [hermione_name]! I did no such thing!"
    call her_main("Yes you did! Yes you did!","scream","worriedCl", cheeks="blush", tears="messy")
    g4 "I most certainly did not!"
    call her_main("No, you did, [genie_name]!","scream","worriedCl", cheeks="blush", tears="messy")
    call her_main("Now, you will give me 20-","angry","angry", cheeks="blush", tears="down")
    call her_main("No, 100 house points or I am reporting you to the Ministry of magic!","angry","angry", cheeks="blush", tears="down")

    menu:
        m "(Ah, crap...)"
        "\"Alright, alright... 100 points it is...\"":
            $ gryffindor += 100
            $ her_mood += 9

            m "One hundred points to \"Gryffindor\" !"
            m "There, it is done..."
            m "Now would you calm yourself down, [hermione_name]?"
            call her_main("No, I will not!","scream","worriedCl", cheeks="blush", tears="messy", ypos="head")
            call her_main("I've just been raped!","scream","worriedCl", cheeks="blush", tears="messy")
            g4 "Oh, snap out of it [hermione_name], I didn't rape you! All I did was-"
            call her_main("{size=+7}You raped me!!!{/size}","scream","worriedCl", cheeks="blush", tears="messy" , trans="hpunch")
            g4 "By the great desert sands, would you keep it down about the rapes!?"
            g4 "Someone may hear you!"
            call her_main("Good! I want them to hear!","scream","worriedCl", cheeks="blush", tears="messy")
            m "Why would you want that? I already paid you!"
            call her_main("Oh... right...","angry","base", cheeks="blush", tears="mascara")
            call her_main("But I hate you! I hate you [genie_name]!","scream","angryCl", cheeks="blush", tears="mascara")

        "\"You're bluffing, [hermione_name]!\"":
            $ her_mood += 27

            call her_main("No, I'm not! I'm gonna do it!","scream","worriedCl", cheeks="blush", tears="messy", ypos="head")
            g4 "By all means, go ahead..."
            g4 "There was no rape!"
            call her_main("I hate you, [genie_name]!","scream","worriedCl", cheeks="blush", tears="messy")


    call hg_chibi_transition("stand","desk","base", flip=False, trans="fade")

    call her_walk(xpos="door", ypos="base", speed=2)

    call her_main("...........................","disgust","down_raised", cheeks="blush", ypos="head")

    call her_chibi(action="leave")

    jump end_hermione_event









### Tier 4 ###

label hg_pf_grope_ass_T3:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")

    call her_main("Do you want me to turn around then, [genie_name]?","base","baseL", cheeks="blush", ypos="head")

    call play_music("playful_tension") # SEX THEME.

    menu:
        m "Hm..."
        "\"Yes. Turn around, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","base","baseL", cheeks="blush")
            jump hg_pf_grope_ass_T3_back

        "\"No. Just stand still, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","soft","base", cheeks="blush", ypos="head")
            jump hg_pf_grope_ass_T3_front



label hg_pf_grope_ass_T3_front:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")

    "Dev Note" "This section is missing writing."

    menu:
        "-Slide your hands under her panties-":
            call hg_chibi_transition("grope_ass", flip=False, trans="d7")

        "-No. That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T3_continue



label hg_pf_grope_ass_T3_back:
    call hg_chibi_transition("stand_behind_desk", flip=True, trans="d7")

    "Dev Note" "This section is missing writing."

    menu:
        "-Slide your hands under her panties-":
            call hg_chibi_transition("grope_ass", flip=True, trans="d7")

        "-No. That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T3_continue








label hg_pf_grope_ass_T3_continue:

    call nar(">You slowly slide one of your hands under the fabric of the girl's panties...")
    call her_main("[genie_name]... What are you...?","open","baseL", cheeks="blush", ypos="head")

    if her_tier <= 5:
        m "It's alright, just think about those 15 points your house is about to receive..."
    else:
        m "It's alright, just try to relax and enjoy yourself"

    call her_main("As you say...","open","baseL", cheeks="blush")

    menu:
        "-Prod her pussy with one of your fingers-":
            ">You slide one of your fingers down and place it against the girl's little slit..."
            call her_main("[genie_name]?","base","baseL", cheeks="blush")

            menu:
                "-Force your finger into her pussy!-":
                    ">You force one of your fingers into her little pussy..."
                    ">It's very tight and warm..."
                    ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."

                    call her_main("Ah....","silly","glance", cheeks="blush")
                    call her_main("It's inside of me...")
                    call her_main("No, [genie_name], you must stop now...","base","glance", cheeks="blush")
                    m "Why? You don't like it?"
                    call her_main("It doesn't matter whether I like this or not, [genie_name].")
                    call her_main("You know why I'm doing this...")
                    call her_main("And it is wrong for me to let you do this to me for a meagre 15 points...")
                    ">Hermione pulls away from you..."
                    m "Heh... I see..."
                    m "Well, in that case..."

                    jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butt-hole instead-":
            ">You place your one of your thumbs against the girl's little butt-hole..."
            call her_main("[genie_name]? What are planning on doing?","base","baseL", cheeks="blush")

            menu:
                "-Force your thumb into her butt-hole-":
                    ">You force one of your thumbs into her little butt-hole..."
                    with hpunch
                    call her_main("ah... your finger is up my...","silly","worried", cheeks="blush", tears="soft")
                    ">It's very tight and warm inside..."
                    call her_main("Ah....","silly","glance", cheeks="blush")
                    call her_main("It's inside of me...")
                    call her_main("No, [genie_name], you must stop now...","base","glance", cheeks="blush")
                    m "Why? You don't like it?"
                    call her_main("It doesn't matter whether I like this or not, [genie_name].")
                    call her_main("You know why I'm doing this...")
                    call her_main("And it is wrong for me to let you do this to me for a meagre 15 points...")
                    ">Hermione pulls away from you..."
                    m "Heh... I see..."
                    m "Well, in that case..."

                    jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope
















### Tier 5 ###

label hg_pf_grope_ass_T4:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")

    call her_main("Do you want me to turn around then, [genie_name]?","soft","glance", cheeks="blush", ypos="head")

    call play_music("playful_tension") # SEX THEME.

    menu:
        m "Hm..."
        "\"Yes. Turn around, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","base","baseL", cheeks="blush")
            jump hg_pf_grope_ass_T4_back

        "\"No. Just stand still, [hermione_name].\"":
            call her_main("As you say, [genie_name]...","soft","base", cheeks="blush", ypos="head")
            jump hg_pf_grope_ass_T4_front



label hg_pf_grope_ass_T4_front:
    call hg_chibi_transition("stand_behind_desk", flip=False, trans="d7")
    #show screen no_groping_01
    call ctc

    "Dev Note" "This favor needs to be rewritten!"

    call her_main("[genie_name], please hurry...","soft","baseL", cheeks="blush")
    m "What's the problem, [hermione_name]?"

    if daytime:
        call her_main("I don't have long before class.","annoyed","angryL", cheeks="blush")
    else:
        call her_main("I don't have long before others notice im missing.","annoyed","angryL", cheeks="blush")

    m "do you enjoy this so much?"
    call her_main("I wouldn't phrase it like that...","annoyed","wink", cheeks="blush")

    call her_main("Can we just start, please...?","angry","worriedCl", cheeks="blush",emote="05")
    m "Well, since you asked so nicely..."
    show screen groping_01
    with d7

    call her_main("!!!","mad","wide", cheeks="blush")
    m "What is it?"
    call her_main("nothing, [genie_name].","base","ahegao_raised", cheeks="blush")
    m "it didn't sound like nothing."
    call her_main("...","base","ahegao_raised", cheeks="blush")

    call nar(">You run your hands up and down Hermione's legs...")
    call her_main(".........................","base","ahegao_raised", cheeks="blush")

    call nar(">And give her Ass a good squeeze...")
    call her_main(".................","base","glance")
    m "Don't look away, girl. I want you to look into my eyes."
    call her_main("but its embarrassing, [genie_name]...","angry","down_raised")
    m "..."
    call her_main("...fine, [genie_name]...","base","ahegao_raised", cheeks="blush")
    m "you're being so quiet."
    call her_main("....................","base","closed")
    m "not even a word..."

    call nar(">you  enjoy the sensation of her butt under your hands...")
    m "as my hands explore you..."
    m "your thighs..."

    call nar(">your hands rub in circles from the sides of her legs to her inner thighs")
    m "your big, firm ass..."

    call nar(">You massage her ass-cheeks lightly...")
    call her_main(".....................","grin","ahegao")
    m "your loins..."

    call nar(">one hand circling just above her clit.")
    call her_main(".....................","silly","dead")
    m "is there something you want?"
    call her_main(".....................","annoyed","wink", cheeks="blush")
    call her_main("...i... {size=-5}...i want you to finger me...{/size}","disgust","down_raised", cheeks="blush")
    m "Did you say something, [hermione_name]?"
    call her_main("...it's nothing, [genie_name]...","open","ahegao_raised", cheeks="blush")

    call nar(">You massage her ass-cheeks lightly with one hand as the other continues to circle above her cunt, fingers brushing against her clit...","start")
    call nar(">Hermione maintains eye contact as she's been told...","end")

    m "you're lying."
    call her_main("I... i said i want you to finger me!","shock","worriedCl")

    call nar(">You swiftly plunge two fingers into her drenched snatch.")
    call her_main("!!!{image=textheart}{image=textheart}","grin","ahegao")

    call nar(">you start to pump your fingers inside her before she can do more than gasp.")
    call her_main("...................................","disgust","down_raised", cheeks="blush")
    m "did i say you could look away?"
    call her_main("..................................................","base","ahegao_raised", cheeks="blush", tears="soft")
    m "good girl"

    call nar(">her hips roll in rhythm as you fuck her with your fingers")
    m "do you like this?"
    m "you like it when i finger your cunt?"
    call her_main("i love it!{image=textheart} i love your long fingers in my tight, wet cunt!!{image=textheart}","silly","ahegao", tears="crying")
    m "well, i think we can do better."

    call nar(">with your other hand, you force a finger up her tight asshole.")
    call her_main("!!!","scream","surprised", cheeks="blush", tears="messy")
    call her_main("my cunt and my ass!","grin","dead", cheeks="blush", tears="messy")

    call nar(">you don't even need to move as she pounds herself against your fingers.")
    call her_main("fingering my cunt and ass!{image=textheart}{image=textheart}","silly","dead", tears="messy")
    m "no, we can still do better."

    call nar(">you force another finger up her ass.")
    call her_main("iloveitiloveitiloveit","grin","ahegao", tears="messy")
    m "what do you love, [hermione_name]?"
    call her_main("ah!!{image=textheart} i love your fingers in my ass and cunt!{image=textheart}","shock","wide", tears="messy")

    call nar(">her movements have become more frantic.")
    m "are you cumming, [hermione_name]?"
    call her_main("yes!!","scream","surprised", cheeks="blush", tears="messy")
    call her_main("i'm cumming!!","scream","worriedCl", cheeks="blush", tears="messy")
    call her_main("i'm cumming from being fucked with your fingers!!","grin","dead", cheeks="blush", tears="messy")
    m "look at me!"
    m "show me your fuck-face!"
    m "i want to see you cum from Whoring yourself for fifteen points."
    call her_main("aaaaaaaaah!!!","scream","surprised", cheeks="blush", tears="messy")

    jump end_hg_pf_grope



label hg_pf_grope_ass_T4_back:
    call hg_chibi_transition("stand_behind_desk", flip=True, trans="d7")
    # show screen no_groping_02
    call ctc

    "Dev Note" "This favor needs to be rewritten."

    call her_main(".............","base","ahegao_raised", cheeks="blush")

    menu:
        m "Hm..."
        "-Give her butt a squeeze-":
            pass

        "-Give her butt a slap-":
            call slap_her

            call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
            call her_main("[genie_name]....?","base","baseL", cheeks="blush")

            call slap_her
            call her_main("!!!!!!!!!!!!!","scream","wide", cheeks="blush")
            call her_main("[genie_name], what are you doing!?","silly","worried", cheeks="blush", tears="soft")
            call her_main("You said all you are going to do is touch!","silly","worried", cheeks="blush", tears="soft")
            m "do you want me to stop, [hermione_name]?"

            call slap_her
            call her_main("ahh!!","silly","ahegao_raised", cheeks="blush")
            call her_main("...I-","disgust","down_raised", cheeks="blush")

            call slap_her
            call her_main("no!!","scream","wide")
            m "then what do you want me to do?"

            call slap_her
            call her_main("to keep slapping me!!","silly","ahegao_raised", cheeks="blush")
            m "and what do you want me to slap?"

            call slap_her
            call her_main("my ass!!","silly","ahegao")
            call her_main("slap my slutty ass!!","open_tongue","ahegao_raised", cheeks="blush")
            m "you'll have to speak up. I couldn't quite hear you."
            call slap_her

            call her_main("slap my slutty ass harder!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
            m "you're being rather loud today."

            call slap_her
            call her_main("yess!!","open_tongue","ahegao_raised", cheeks="blush")
            call her_main("harder!!","silly","ahegao")
            m "what if someone hears?"

            call slap_her
            call her_main("I don't care!!","shock","wide", cheeks="blush")

            call slap_her
            call her_main("yes!!!","silly","ahegao_raised", cheeks="blush")

            call slap_her
            call her_main("just a little-","grin","ahegao")

            call slap_her
            call her_main("I'm gunna","silly","dead")

            call slap_her
            call her_main("cumcumcummingcumming","silly","ahegao")
            call her_main("I'm cumming!!!{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
            ">you take a moment watch her spasms"
            m "well, then... proceeding with groping..."
            call her_main("................","base","ahegao_raised")

    call ctc
    show screen groping_02
    with d7

    call her_main("-wait I juuuus-!!!","base","baseL", cheeks="blush", ypos="head")
    call nar(">Her voice trails off to a squeak as you start to knead her big, round ass")
    m "Hm? what's that? i couldn't hear you, [hermione_name]."
    call her_main("You bastard{image=textheart}","grin","ahegao_mad", cheeks="blush")
    call nar(">Hermione's body quivers as her hips roll")
    m "Well, someone's enjoying herself."
    call her_main("Well, you know me, [genie_name]...","base","ahegao_raised", cheeks="blush")
    call her_main("I'm just happy to be able to do my part","base","ahegao_raised", cheeks="blush")
    call her_main("Please don't mind it and continue...","base","ahegao_raised", cheeks="blush")
    call her_main("(...to grope me...)","silly","dead")

    call nar(">You keep on playing with Hermione's ass...","start")
    call nar(">And continue sliding your hands up and down her inner thighs...","end")

    call her_main("................","base","baseL", cheeks="blush")

    jump hg_pf_grope_T4_continue



label hg_pf_grope_T4_continue:

    menu:
        "-Slide your hands between her legs-":
            call nar(">You slowly slide one of your hands towards her crotch...")
            call her_main("[genie_name]... What are you...?","base","ahegao_raised", cheeks="blush")
            m "something you'll enjoy."
            m "just relax and leave everything to me."
            call her_main("As you say...","base","ahegao_raised", cheeks="blush")

            pass

        "-No. That's enough for today. Dismiss her-":

            jump end_hg_pf_grope

    menu:
        "-Prod her pussy with one of your fingers-":
            ">You slide one of your fingers down and place it against the girl's little slit..."
            call her_main("[genie_name]?","base","ahegao_raised", cheeks="blush", ypos="head")

            ">You force one of your fingers into her little pussy..."
            ">It's very tight and warm..."
            ">It is quite wet as well...  Seems like Hermione's taking pleasure in this..."
            pause.8

            call her_main("Ah... your finger is in my...","silly","ahegao")
            call her_main("Ah... wait--","angry","dead", cheeks="blush", tears="crying")
            ">you slowly start to pump your fingers..."
            call her_main("-Only fifteen poin-","shock","down_raised", cheeks="blush", tears="crying")
            ">you speed up slightly..."
            call her_main("{image=textheart}-My duty-{image=textheart}","open","surprised", cheeks="blush", tears="messy")
            ">you start rubbing her clit..."
            call her_main("!!{image=textheart}-Gryffindor-{image=textheart}","angry","suspicious", cheeks="blush", tears="messy")
            m "we can, of course, stop right here, unfulfilled. If that's what you really want."
            call her_main("...","angry","dead", cheeks="blush", tears="crying")
            m "well?"
            call her_main("...Keep going...","shock","down_raised", cheeks="blush", tears="crying")
            m "hm?"
            call her_main("Keep fingering my pussy!!","scream","angry", cheeks="blush", tears="messy")
            m "You want me to keep fingering your cunt? is that what your saying?"
            call her_main("Yes, [genie_name]! {image=textheart} Fuck my cunt with your fingers!{image=textheart}","open_wide_tongue","ahegao", tears="messy")
            ">Her hips roll and slam into your fingers."
            call her_main("Shove them deep in my slutty fuckhole!!{image=textheart}","silly","dead", tears="messy")
            m "Hm... I don't think my fingers are up to this task after all..."
            ">You take your fingers out of the girl's gushing cunt."
            call her_main("what!!? no, don't st-","scream","worriedCl", cheeks="blush", tears="crying")
            ">...so you can take the dildo out of your desk."
            call her_main("oh, god yes!!","grin","dead", cheeks="blush", tears="messy")
            m "this is a much better fit isn't it?"
            call her_main("aah!{image=textheart}","silly","dead", tears="messy")
            m "you're far too much of slut to be satisfied by fingers, aren't you?"
            call her_main("yesfinewhatever!","scream","angry", cheeks="blush", tears="messy")
            call her_main("i don't care!","scream","surprised", cheeks="blush", tears="messy")
            call her_main("just don't stop!","silly","ahegao", tears="messy")
            ">her hips meet your every thrust, nearly tearing the toy from your grip."
            call her_main("donstopdonstopdonstop-","grin","dead", cheeks="blush", tears="messy")
            call her_main("pleasepleasepleaseplease-","scream","worriedCl", cheeks="blush", tears="messy")
            m "are you enjoying yourself, [hermione_name]?"
            call her_main("yes! I love how you spank me!","grin","dead", cheeks="blush", tears="messy")
            call her_main("I love how you grope me!","scream","worriedCl", cheeks="blush", tears="crying")
            call her_main("I love how you play with my little fuckholes!","grin","ahegao_mad", cheeks="blush", tears="messy")
            call her_main("ohgodohgodohgod","scream","surprised", cheeks="blush", tears="messy")
            ">Hermione tries to scream as her body bucks and the orgasm takes her, but can't get enough air to do more then moan."
            call her_main("oooooooh...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")

            jump end_hg_pf_grope

        "-Prod her butt-hole instead-":
            ">You place your one of your thumbs against the girl's little butt-hole..."
            call her_main("[genie_name]? you're not planning t-","open","baseL", cheeks="blush", ypos="head")

            ">You force one of your thumbs into her little butt-hole..."
            with hpunch
            call her_main("ah... your finger is up my...","silly","ahegao")
            ">It's very tight and warm inside..."
            call her_main("ah... wait-","angry","dead", cheeks="blush", tears="crying")
            ">you slowly start to pump your thumb"
            pause.8

            call her_main("-only fifteen poin-","shock","down_raised", cheeks="blush", tears="crying")
            ">you speed up slightly"
            call her_main("{image=textheart}-my duty-{image=textheart}","open","surprised", cheeks="blush", tears="messy")
            ">you rotate thumb as you go"
            call her_main("!!{image=textheart}-gryffindor-{image=textheart}","angry","suspicious", cheeks="blush", tears="messy")
            m "we can, of course, stop right here, unfulfilled. if that's what you really want."
            call her_main("...","angry","dead", cheeks="blush", tears="crying")
            m "well?"
            call her_main("...keep going...","shock","down_raised", cheeks="blush", tears="crying")
            m "hm?"
            call her_main("keep fingering my ass!!","scream","angry", cheeks="blush", tears="messy")
            ">you pull your thumb out of her tight little asshole..."
            call her_main("w-what!?","scream","surprised", cheeks="blush", tears="messy")
            call her_main("why w-","scream","angry", cheeks="blush", tears="messy")
            ">...and replace it with two fingers"
            call her_main("Aaah!","scream","surprised", cheeks="blush", tears="messy")
            call her_main("B-Bastard!{image=textheart}","scream","worriedCl", cheeks="blush", tears="messy")
            call her_main("Y-you teasing b-bastard!{image=textheart}{image=textheart}","grin","dead", cheeks="blush", tears="messy")
            m "do you like this, [hermione_name]?"
            call her_main("yes!!!","angry","dead", cheeks="blush", tears="crying")
            m "do you love it?"
            call her_main("oh, god, yes!!!","silly","ahegao", tears="messy")
            m "tell me what you love!"
            call slap_her

            call her_main("aaah!!{image=textheart}{image=textheart}{image=textheart}","scream","surprised", cheeks="blush", tears="messy")
            m "I asked you a question."

            call slap_her
            call her_main("when you finger my ass!","scream","worriedCl", cheeks="blush", tears="messy")
            call her_main("i love it when you fuck my ass with your fingers!","grin","dead", cheeks="blush", tears="messy")
            m "what else do you love?"

            call slap_her
            call her_main("when you slap my slutty ass!","scream","worriedCl", cheeks="blush", tears="messy")

            call slap_her
            call her_main("a-again! i'm c-c","scream","surprised", cheeks="blush", tears="messy")
            m "you're cumming again?"

            call slap_her
            call her_main("yes!","scream","suspicious", cheeks="blush", tears="messy")
            m "you're cumming from being spanked again?"

            call slap_her
            call her_main("yes!!","scream","worriedCl", cheeks="blush", tears="messy")
            m "you're cumming from having your headmaster's fingers shoved up your tight little asshole?"

            call slap_her
            call her_main("yes!!!{image=textheart}","scream","surprised", cheeks="blush", tears="messy")
            ">Hermione's body starts to buck wildly."
            ">you grab herby the hair with your free hand to keep her on the desk even as you frantically pump your fingers into her big, tight ass"
            call her_main("ohgodohgodohgod","scream","surprised", cheeks="blush", tears="messy")
            m "what are you cumming from, little whore?"
            call her_main("!!!!","mad","wide", cheeks="blush", tears="messy")
            m "where's all this pleasure coming from?!"
            call her_main("my aaaaaaaass!{image=textheart}","open_wide_tongue","ahegao", tears="messy")
            ">with one last spasm,hermione collapses to the desk. even after fainting, her Body still twitches, and her hips keep rolling."

            jump end_hg_pf_grope
