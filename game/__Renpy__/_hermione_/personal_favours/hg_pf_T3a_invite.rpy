

### Tier 1 ###

# Invite Snape

label hg_pf_strip_T1_Snape: # Fails
    hide screen blktone
    hide screen hermione_main
    with d3

    m "Miss, Granger, I will be buying another favour from you today."

    call her_main("Of course, [genie_name].","open","closed", xpos="base", ypos="base")
    m "But before that, do you think you could go and fetch professor Snape for me?"
    call her_main("...Professor Snape?","annoyed","suspicious")
    her "May I ask, why, [genie_name]?"
    m "Oh, I just think you could use a bigger audience for your striptease performance."
    call her_main("My striptease performance...?!!","shock","wide")
    call her_main("Are you completely out of your mind, [genie_name]?","angry","angry")
    call her_main("Wasn't it enough that I've had to embarrass myself in front my teacher once before?","open","angry")
    call her_main("And now you expect me to do it agiain,... but willingly?!","scream","angryCl")
    m "Short answer... yes."
    call her_main("I'm leaving!","angry","angry")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 15
    $ hg_pf_strip.fail()

    jump end_hermione_event



### Tier 2 ###

# Invite Snape

label hg_pf_strip_T2_Snape:
    if not hg_strip_snape_trigger:
        $ hg_strip_snape_trigger = True

        hide screen blktone
        hide screen hermione_main
        with d3

        m "Miss, Granger, I will be buying another favour from you today."

        call her_main("Of course, [genie_name].","open","closed", xpos="base", ypos="base")
        m "But before that, do you think you could go and fetch professor Snape for me?"
        call her_main("...professor Snape?","annoyed","suspicious")
        her "May I ask, why, [genie_name]?"
        m "Oh, I just think you could use a bigger audience for your striptease performance."
        call her_main("My striptease performance...?!!","shock","wide")
        call her_main("With all due respect, [genie_name]...","angry","angry")
        call her_main("{size=-5}(Which I have oh so little left for you...){/size}","normal","frown")
        call her_main("I refuse to degrade myself for professor Snape's amusement!","scream","angryCl")
        m "No, no, you got it all wrong, [hermione_name]."
        call her_main("Hm..?","soft","base")
        m "I want to prove that professor Snape is dirty, and I need your help."
        call her_main("!!!","shock","wide")
        m "Yes, I want to catch him in the act!"
        call her_main("[genie_name], I didn't realise...","open","worried")
        call her_main("I see now...","base","base")
        her "I am sorry for doubting you [genie_name]..."
        m "No biggy. Now go find professor Snape and bring him here."
        call her_main("Right away [genie_name]!","smile","angry")

    else:
        hide screen blktone
        hide screen hermione_main
        with d3

        m "Miss, Granger, I will be buying another favour from you today."

        call her_main("Of course, [genie_name].","open","closed", xpos="base", ypos="base")
        m "But before that, do you think you could go and fetch professor Snape again?"
        call her_main("...professor Snape?","annoyed","suspicious")
        her "may I ask, why, [genie_name]?"
        m "Oh, I just want you to dance for us."
        call her_main("!!!","open","base")
        m "I want to prove that professor Snape is dirty, and I need your help."
        call her_main("But didn't we already establish that last time I did this?","annoyed","worriedL")
        m "Well, ehm... sure..."
        m "But I will need more proof if I am to take this issue to the ministry of magic!"
        call her_main(".....","angry","angry")
        m "So, what do you say [hermione_name]?"
        m "One more dance for the greater good?"
        call her_main("Well, alright...","disgust","glance")
        m "Good. Go find professor Snape then."

    call her_walk(action="leave", speed=2.5)

    show screen blkfade
    with d5

    stop music fadeout 1.0
    ">...................{w}...................{w}...................{w}..................."

    call play_sound("door")
    call her_chibi("stand","desk","base")
    call sna_chibi("stand","mid","base")
    hide screen blkfade
    with d5
    pause.5

    call play_music("dark_fog")
    call sna_main("Genie... err, I mean Albus, you wanted to see me?","snape_01", xpos="base", ypos="base")
    m "Yes. Are you in the mood for a little striptease?"
    call sna_main("Oh...?","snape_05")
    sna "Miss Granger here will be performing I assume?"
    call her_main("..............","angry","worriedCl", emote="05", xpos="mid", ypos="base")
    m "Yes, our little mynx is more than happy to take off her clothes for our entertainment."
    call her_main("............","angry","worriedCl", emote="05")
    m "Aren't you [hermione_name]?"
    call hide_characters
    with d3
    pause.5

    call her_chibi("stand","desk","base", flip=True)
    with d1
    pause.8

    call her_chibi("stand","desk","base")
    with d1
    pause.5

    show screen snape_main
    call her_main("Yes, [genie_name].","angry","worriedCl", emote="05")
    m "Let's get started then!"
    hide screen hermione_main
    with d3
    pause.2
    call sna_main("","snape_13")
    pause.8

    hide screen snape_main
    show screen blkfade
    with d5

    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
    pause 3
    call her_chibi("dance","on_desk","on_desk")
    call sna_chibi("stand","desk_close","base")

    call her_main(".............","open","closed", ypos="head")
    call sna_main("......................","snape_05")
    m ".........................."

    hide screen bld1
    hide screen blkfade
    with d5
    pause.8

    call bld
    m "So... Severus... How's life?"
    call sna_main("Well, you know... same old, same old...","snape_09")
    call sna_main(" The Students are causing me grief...","snape_06")
    call sna_main("In fact, miss Granger here managed to cause me more stress than any other student...","snape_03")
    pause.2
    call her_main("...............................","grin","baseL", xpos="mid", ypos="base")
    m "Oh, I am sure she is very sorry about that..."
    call her_main("{size=-4}(Not even a little bit!){/size}","base","happyCl")
    m "And will make up for it today, won't you, [hermione_name]?"
    pause.2

    call her_main("Uhm... Yes, [genie_name].","base","squint")
    pause.2


    if hermione_wear_top and (h_top == "top_1" or h_top == "top_6"):
        call nar(">Hermione takes her vest off and starts to sway her hips seductively.")

        if h_top == "top_1":
            $ h_top = "top_2"
        else:
            $ h_top = "top_4"
        call update_her_uniform
        pause.2

        call her_main("")

    else:
        call nar(">Hermione starts to sway her hips seductively.")

    call ctc

    call her_main("...................","open","down")
    call sna_main("Hm... You are being suspiciously quiet, Miss Granger.","snape_05")
    call her_main("{size=-4}(Oh no! Is he onto us?){/size}","shock","wide")
    call her_main("I'm just doing what the headmaster told me to, Professor Snape...","grin","worriedCl", emote="05")
    call sna_main("Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day?","snape_03")
    m "Severus..."
    call sna_main("No, Albus I want to hear little miss perfect's answer.","snape_03")
    call her_main("I just want you to have a good time, Professor Snape...","grin","worriedCl", emote="05")
    call sna_main("Oh! It's \"Professor Snape\" now, is it?","snape_03")
    call sna_main("What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!","snape_10")
    g9 "{size=-5}( \"snape'o'doodle\, heh... that's funny.){/size}"
    call her_main(".............","grin","worriedCl", emote="05")
    call sna_main("Yes, I know what are you calling me behind my back, you wretched girl!","snape_08")
    call her_main("Well, maybe that's because you deserve it... Snivellus.","scream","angry", emote="01")
    call sna_main("What?!","snape_10")
    call sna_main("How dare you....?")
    call sna_main("Who do you think you are? You filthy mu--","snape_15")
    call her_main("[genie_name], one of your staff is verbally abusing me!","scream","angryCl")
    call her_main("Are you going to allow this?")
    call sna_main("Verbally abusing...?! You have some nerve, girl!","snape_08")
    call sna_main("Albus, will you allow her to talk back to a teacher like that?","snape_10")
    call her_main("[genie_name]!","scream","angryCl")
    call sna_main("Albus!","snape_10")

    menu:
        m "..."
        "\"[hermione_name], show some respect!\"":
            $ her_mood += 9
            call her_main("What?","annoyed","angry")
            call her_main("But [genie_name]!")
            m "Young lady, you {size=+4}will{/size} calm down now."
            call her_main("Tsk!","disgust","glance")
            m "And take off your skirt already, would you?"
            call her_main(".......","annoyed","angryL")
            call sna_main("...........","snape_13")

        "\"Severus, you started this.\"":
            call sna_main("What? Me?!","snape_10")
            call her_main("Thank you, [genie_name].","base","base")
            call sna_main("Albus, you are spoiling the girl! She must be taught a lesson!","snape_08")
            m "...............Severus."
            g4 "Did you hit your head?!"
            call sna_main("I beg your pardon?","snape_03")
            g4 "The girl is already stripping for you!"
            g4 "What punishment are you talking about?"
            call sna_main("Tsk... How about a flogging?","snape_16")
            g4 "Severus!"
            call sna_main("Alright, alright, I see your point...","snape_17")
            m "[hermione_name], are you going to strip or are you going to climb on my desk to give us a better view?"
            call her_main("Ehm...","open","down")
            m "Take of your skirt, [hermione_name]!"
            call her_main("Yes, [genie_name]...","soft","base")

        "\"Both of you, calm the fuck down.\"":
            m "You, tall-dark-and-handsome, calm down a bit, would you?"
            call sna_main("I beg your pardon?","snape_03")
            call her_main("Yes! You tell him profess--","annoyed","angryL")
            m "You as well, you perverted little mynx!"
            m "Calm down and take your skirt off already."
            call her_main("I am not perverted...","annoyed","annoyed")
            m "The skirt, [hermione_name]!"
            call her_main("......","annoyed","angryL")
            call sna_main(".............","snape_13")

        "-HARDCORE-" if game_difficulty >= 3: #Hardcore difficulty dialogue.
            $ her_mood += 18
            $ sna_friendship -= 10
            m "Both of you,..."
            stop music
            with hpunch
            g4 "Shut the fuck up!!!"
            g4 "You!... You good for nothing, ugly-faced, crooked-nosed-wannabe-wizard!"
            with hpunch
            call sna_main("(...)","snape_11")
            call her_main("(... yikes!)","angry","wink")
            call sna_main("(What did he just say to me?!)","snape_08")
            g4 "Shut your stupid mouth or I will send you flying out that bloody window!"
            g4 "That Bitch is already stripping for you, so what more do you want?!"
            call her_main("(That B-Bi--","shock","wide")
            g4 "And you,... stripper-whore!"
            g4 "Do what you are payed for and start stripping already!!!"
            call her_main("......","angry","angryCl", emote="01")
            call sna_main(".............","snape_05")
            call her_main("...","mad","frown")

    pause.2

    $ hermione_wear_panties = True
    call set_her_action("lift_skirt")
    pause.5

    $ hermione_wear_bottom = False
    call set_her_action("None")
    pause.2

    call nar(">Hermione swiftly takes off her \"Hogwarts\" skirt...")
    call ctc

    sna "Hm..."
    call her_main("........................","open","down")
    m "Yes, much better!"

    call nar(">Hermione keeps on dancing, while she's Wearing nothing but her shirt now...")

    menu:
        m "..."
        "\"Severus, what about that Potter boy?\"":
            call her_main("(.....?)","soft","base")
            call sna_main("What about him?","snape_09")
            m "Is he still causing you grief?"
            call sna_main("Oh...","snape_09")
            call sna_main("Not really, no...")
            call sna_main("To be honest I never really had a problem with the boy himself...","snape_06")
            sna "Although I did plan to make his life here miserable because of his father..."
            call sna_main("But lately I have way more interesting projects to occupy myself with...","snape_02")
            call her_main("...................","soft","base")

        "\"Severus, what about the Weasleys?\"":
            call sna_main("What about them?","snape_09")
            m "Are they still causing you trouble?"
            call sna_main("Yes... More than ever.","snape_09")
            m "Hm...?"
            m "You seem surprisingly indifferent about that..."
            call sna_main("That's because I know that they will get what they deserve eventually...","snape_05")
            m "Revenge? Cool! What do you have in mind?"
            call her_main("!!!","soft","base")
            call sna_main("Hm... Can't discuss this with \"the enemy\" present.","snape_06")
            call her_main("Tsk!","annoyed","angryL")
            call sna_main("All I can say is that it involves their beloved little sister Ginny...","snape_13")
            m "Ginny? Hm... What a curious name for a girl..."
            m "............."
            m "So, you plan to fuck her then?"
            call sna_main("!!?","snape_08")
            call sna_main("Albus, please, not in front of the girl!","snape_17")
            m "Alright, alright..."
            call her_main("{size=-5}(Ginny...){/size}","open","down")

        "\"How would you grade Hermione's butt?\"":
            call sna_main("miss Granger's buttocks?","snape_05")
            call her_main("!!!............","annoyed","angryL")
            m "Sure! As you would grade a paper."
            call sna_main("Hm...","snape_13")
            pause.1
            call nar(">Professor Snape gives Hermione's buttocks an appraising look...")
            call her_main(".........?","upset","wink")
            call sna_main("I would say...","snape_13")
            call her_main("............?!","base","down")
            call sna_main("Yes... \"{size=+5}F-{/size}\".","snape_09")
            call her_main("(What?!)","shock","wide")
            call sna_main("Unsatisfactory...","snape_09")
            sna "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
            call her_main("!!!!!!!!!!","angry","annoyed", emote="01")

    call nar(">One after another, Hermione undoes the buttons of her shirt...")
    pause.2

    $ hermione_wear_bra = False
    call set_her_action("lift_top")
    pause.5

    $ hermione_wear_top = False
    call set_her_action("None")
    pause.2

    call nar(">Then takes it off...")

    m "Alright! We Finally get to the good stuff!"
    call sna_main("Hm...","snape_13")

    call her_main("........","annoyed","closed")

    menu:
        m "..."
        "-Start jerking off-":
            jump hg_pf_strip_T2_Snape_masturbate

        "-Just keep on watching-":
            jump hg_pf_strip_T2_Snape_watch



label hg_pf_strip_T2_Snape_watch:
    call play_music("dark_fog")

    call her_chibi("dance","on_desk","on_desk")
    pause.5

    call her_main("I will just keep on dancing then...","open","closed")
    call ctc

    call nar(">Hermione squeezes her breasts and shakes her hips slightly...")

    m "Yes, [hermione_name]. Very good."
    call sna_main("*Khem!* Acceptable performance, miss Granger.","snape_12")
    call her_main("....","open","closed")
    m "Heh..."
    m "So,... how would you grade her tits?"
    call her_main("......","annoyed","closed")
    call sna_main("Hm......","snape_20")
    call her_main("........","annoyed","closed")
    call sna_main("\"B+\"!","snape_12")
    call her_main("!!!","open","wide")
    m "Really?"
    call sna_main("Yes. I do give credit where it's due.","snape_12")
    call her_main("(Professor...)","angry","wide")
    call her_main("(Time for my finishing act then!)","open","closed")
    pause.1

    $ hermione_wear_panties = False
    call set_her_action("pinch")
    pause.5

    call nar(">Hermione bends over and slides her panties down.","start")
    ">Her movements lack grace..."
    call nar(">But a pretty pussy is always a welcome sight nonetheless...","end")
    call ctc

    call sna_main("Yes... Yes...","snape_20")
    sna "Now shake those B+ titties for me, you harlot!"
    call her_main(".......","angry","worriedCl")

    call set_her_action("None")
    pause.5

    call nar(">Hermione suddenly breaks into a series of rather complex pirouettes.")
    call sna_main("Yes, such grace...","snape_19")
    call sna_main("That lithe, young body!","snape_20")
    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","open","closed")
    call nar(">Hermione seems very focused on her dancing routine...")
    call sna_main("Yes, and now another pirouette!","snape_19")
    call sna_main("Magnificent!")
    show screen blkfade
    with d5

    ">Hermione performs another set of movements and pirouettes..."
    ">Gives a little curtsy bow to the imaginary public..."
    ">And then slumps down on her butt exhausted."

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    show screen bld1
    call sna_main("Good job, you harlot!","snape_22")
    call her_main(".............","soft","squintL")

    if daytime:
        call sna_main("Well, my class is about to start so I will be leaving now.","snape_22")
        sna "Don't you have potion class with me today, Miss Granger?"
        call her_main("Yes, [genie_name]...","annoyed","dead")
        call sna_main("Well, don't be late, girl...","snape_22")
    else:
        call sna_main("Well, it is getting rather late. I think I will be leaving now.","snape_22")
        sna "Good night, Albus."
        m "Severus."
        call sna_main("Harlot.","snape_22")
        call her_main("Professor...","annoyed","dead")

    call ctc

    call hide_characters
    show screen blkfade
    with d5

    ">Professor Snape leaves..."
    stop music fadeout 1.0
    call her_main("....................","annoyed","dead", ypos="head")
    pause.5
    ">.................{w}.................{w}.................{w}................."

    call her_main("May I... may get paid now... [genie_name]...?","normal","worriedCl")

    jump end_hg_pf_strip



label hg_pf_strip_T2_Snape_masturbate:
    call play_music("playful_tension") # SEX THEME
    pause.2

    call hide_characters
    show screen blkfade
    with d5
    pause.2

    call her_main("[genie_name]?!","open","wide", ypos="head")
    m "It's alright, [hermione_name]. Don't mind me..."
    call sna_main("Oh, we're doing it like this then?","snape_12", ypos="head")
    call sna_main("Well, don't mind if I do...","snape_12")
    call her_main("!!!")

    show screen chair_left
    call gen_chibi("jerking_off","behind_desk","behind_desk")
    show screen desk
    call her_chibi("stand","on_desk","on_desk")
    call sna_chibi("jerking_off","desk","240")
    hide screen blktone
    hide screen blkfade
    with d5
    call ctc

    call her_main("No, guys... err I mean, sirs... Ehm, professors!","angry","wide", xpos="mid", ypos="base")
    m "Don't you mind us [hermione_name], just keep on doing your thing."
    call her_main("But...")
    call her_main("No! I refuse to dance with those things pointed at me!","angry","worriedCl")
    call her_main("You need to put them away or the dance is over!")
    m "You aren't in any position to give us orders, [hermione_name]."
    call her_main("that was not an order, [genie_name]. It was an ultimatum.","clench","angry", emote="01")

    menu:
        m "..."
        "\"Alright Severus, let's be civil...\"":
            hide screen hermione_main
            with d3
            pause.2
            call sna_main("I see Miss Granger manages to remain exceptionally stubborn in any situation...","snape_03")
            call hide_characters
            hide screen bld1
            with d5

            hide screen chair_left
            hide screen desk
            show screen genie
            call her_chibi("stand","on_desk","on_desk")
            call sna_chibi("stand","desk","base")
            with d7
            pause.3

            jump hg_pf_strip_T2_Snape_watch

        "\"(Pst! Remember why we are doing this!)\"":
            pass


    if her_tier < 5: # Hermione is NOT ok with it.
        call her_main("Oh...","open","wide")
        call her_main("No, I can't! This is just not worth it!","angry","worriedCl")
        call hide_characters
        show screen blkfade
        with d5

        ">Hermione jumps off the desk and starts to put her clothes back on."
        call sna_main("Well, this was awfully anticlimactic...","snape_03")
        g4 "You don't say..."
        call sna_main("May as well leave now I suppose. I will talk to you later, Albus.","snape_03")
        m "Yes, later, Severus."
        call sna_main("Miss Granger...","snape_04")
        call her_main("Professor...","angry","worriedCl", ypos="head")

        call sna_chibi("hide")
        call her_chibi("stand","desk","base")
        call play_sound("door")
        ">Professor Snape leaves..."
        stop music fadeout 1.0
        hide screen blkfade
        with d5

        call her_main("....................","annoyed","dead", xpos="mid", ypos="base")
        call ctc

        call her_main("...Can I get paid now... [genie_name]...?","normal","worriedCl")

        jump end_hg_pf_strip


    else: # Hermione IS ok with it.
        call her_main("Oh, right...","shock","wide")
        call sna_main("What was that?","snape_05")
        call her_main("Please don't mind what I just said...","silly","worriedCl", emote="05")
        call sna_main("Hm...?","snape_05")
        call her_main("I do not mind you touching yourself in front of me...","silly","worriedCl", emote="05")
        call her_main("Yes, I do not mind it at all...")
        call her_main("I will just keep on dancing then...")

        call nar(">You keep on jerking off while you're watching Hermione dance...","start")
        call nar(">Hermione squeezes her breasts and shakes her hips slightly...","end")

        m "Yes, [hermione_name]. Very good."
        call sna_main("*Khem!* Acceptable performance, miss Granger.","snape_12")
        call her_main("....................","angry","worriedCl")
        m "Heh..."
        m "So, how would you grade her tits?"
        call her_main("......","open","wide")
        call sna_main("Hm......","snape_13")
        call her_main("........","annoyed","angryL")
        call sna_main("\"B+\"!","snape_12")
        call her_main("!!!","open","wide")
        m "Really?"
        call sna_main("Yes. I do give credit where credit is due.","snape_12")
        call her_main("(Professor...)","annoyed","closed")
        call her_main("(Time for my finishing act then!)","open","closed")
        pause.1

        $ hermione_wear_panties = False
        call set_her_action("pinch")
        pause.5

        call nar(">Hermione bends over and slides her panties down.","start")
        ">Her movements lack grace..."
        ">But a pretty pussy is always a welcome sight nonetheless..."
        call nar(">You show your appreciation by stroking your cock even faster...","end")
        call ctc

        call sna_main("Yes... Yes!!!","snape_18")
        call sna_main("Now shake those B+ titties for me, you harlot!")
        call her_main(".......","angry","worriedCl")

        call set_her_action("None")
        pause.5

        call nar(">Hermione suddenly breaks into a series of rather complex pirouettes.")
        call sna_main("Yes, such grace...","snape_19")
        call sna_main("That lithe, young body!","snape_20")
        call her_main(".........","grin","ahegao")
        call sna_main("Oh, yes!","snape_20")
        call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","grin","ahegao")
        call nar(">Hermione seems very focused on her dancing routine...")
        call sna_main("Yes, and now another pirouette!","snape_19")
        call sna_main("Magnificent!")
        call sna_main("I would applaud you but one of my hands is very busy at the moment.","snape_13")
        m "{size=-4}(Was that an attempt at a joke?){/size}"
        m "{size=-4}(Man, horny Snape is weird...){/size}"

        call hide_characters
        show screen blkfade
        with d5

        ">Hermione performs another set of movements and pirouettes..."
        ">Gives a little curtsy bow to the imaginary public..."
        ">And then slumps down on her butt exhausted."

        call her_chibi("sit_naked","on_desk","on_desk")

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with d5
        call ctc

        call her_main("Whew... This was--","open","closed")
        with hpunch

        g4 "ARGH! YOU FUCKING WHORE!"

        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cumming","behind_desk","base")
        pause.2

        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
        $ u_sperm = "characters/hermione/face/auto_04.png"

        call her_main("??!!!","shock","wide")
        call her_main("","angry","worriedCl")
        call ctc

        call sna_main("Good job, you harlot!","snape_18")
        call sna_main("Here is your reward!","snape_21")

        call cum_block
        call sna_chibi("cumming","desk","240")
        pause.2

        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
        $ u_sperm = "characters/hermione/face/auto_05.png"

        call her_main("!!!!!!!!!!!","shock","wide")
        call ctc

        call sna_main("Oh... Yes...","snape_21")
        g4 "Little slut!"
        call her_main("...............................","grin","ahegao")

        $ s_c_c_u_pic = "characters/snape/chibis/masturbating/sperm_18.png"
        $ g_c_c_u_pic = "characters/genie/chibis/masturbating/sperm_wide_18.png"

        call sna_main("Ha-ha-ha! This is magnificent!","snape_21")
        g9 "I know, right!?"

        call gen_chibi("hold_dick","behind_desk","base")
        call sna_chibi("hold_dick","desk","240")
        pause.2

        call sna_main("Yes... We should do this more often.","snape_22")
        call her_main(".................","grin","ahegao")

        call sna_main("Your performance was acceptable, miss Granger...","snape_20")
        call her_main("Thank you................","annoyed","dead")
        call sna_main("But if I were to grade it...","snape_19")
        call her_main("...........","annoyed","dead")
        call sna_main("Hm....","snape_22")
        call her_main("............","annoyed","dead")
        call sna_main("\"{size=+5}F+{/size}\"!","snape_10")
        stop music

        call her_main("{size=+5}WHAT?!!!{/size}","shock","wide")
        call sna_main("Yes... Quite a few things could use some improvement actually.","snape_09")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("I cannot believe this!","clench","angry", emote="01")
        pause.5

        call hide_characters
        show screen blkfade
        with d5

        ">Hermione furiously jumps off your desk."
        pause 2
        hide screen hermione_main

        call sna_chibi("hold_dick","mid","240")
        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","desk","base", flip=True)

        hide screen bld1
        hide screen blktone
        hide screen blkfade
        with d5
        call ctc

        $ flip = True # Flips hermione_main screen.
        $ u_sperm = "characters/hermione/face/auto_05.png"

        call her_main("I demand a higher grade than that!","soft","angry", xpos="right", ypos="base")
        call sna_main("You do not demand a grade miss Granger, you earn it.","snape_09")
        call her_main("I did earn it!","open","baseL")
        call her_main("And could you at least have the decency to stop touching yourself, professor!","annoyed","angryL")
        call sna_main("Tch...","snape_12")
        hide screen hermione_main
        with d3

        m "(Are they for real?)"
        hide screen bld1
        with d3
        pause.2

        show screen blkfade
        with d5

        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
        ">Then he beats a hasty retreat before Hermione has a chance to start another argument..."
        pause 1

        $ flip = False # Flips hermione_main
        $ aftersperm = True #Show cum stains.
        $ uni_sperm = False #Don't show cum.
        call sna_chibi("stand","mid","base", flip=True)
        hide screen blkfade
        with d5

        call sna_walk(action="leave", speed=2)
        pause.5

        call her_chibi("stand","desk","base")
        pause.2

        call her_main("Well...","annoyed","worriedL", xpos="mid", ypos="base")
        her "Was our mission a success, [genie_name]?"

        menu:
            m "..."
            "\"Huh? What mission?\"":
                $ her_mood += 7
                call her_main("I only agreed to this so that you could catch professor Snape in the act, [genie_name]!","scream","worriedCl")
                call her_main("So that we would have definite proof that he is \"dirty\"!","normal","worriedCl")
                m "Oh, that mission..."
                m "Yes. Mission accomplished!"
            "\"Yes! Thanks to you!\"":
                pass

        m "Good job, [hermione_name]."
        call her_main("I am happy to have been of help, [genie_name]!","normal","worriedCl")
        pause.5
        show screen blkfade
        with d5

        call her_main("...Can I get paid now, please?","angry","worriedCl", emote="05", ypos="head")

        jump end_hg_pf_strip
