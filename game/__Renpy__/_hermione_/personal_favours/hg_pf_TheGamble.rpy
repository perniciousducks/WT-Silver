

### The Gamble ###

label hg_pf_TheGamble:
    hide screen hermione_main
    with d3
    m "{size=-4}(I'm bored...){/size}"
    g9 "{size=-4}(Should I try something completely different?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        ">This may be {i}{size=+7}the end{/size}{/i} of her..."
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump hermione_requests_menu

    call play_music("chipper_doodle")
    show screen hermione_main
    with d3

    m "You know what? I've been doing too much of the work lately."
    call her_main("[genie_name]?","open","base") #247
    m "You heard me. Lately, all you've done is bend over the desk, while I slam your cunt and your ass to a sloppy, screaming orgasm."
    if her_whoring < 21:
        jump too_much

    call her_main("I... then... ahem. What would you like to do then?","open","worriedL") #249
    m "I am going to sit back and you are going to sit and bounce on my cock."
    call her_main("What?! [genie_name], I don't-","angry","wide") #250
    m "So Gryffindor doesn't need any points then? Oh, well. I tried. Good day Miss Granger."
    call her_main("Aright, alright. So... what's the pay?","annoyed","frown") #252
    m "The standard. I have been doing all the work lately. It's only fair."

    call play_music("playful_tension") # SEX THEME.

    call her_walk(400,325,1.25)

    show screen blkfade
    with fade

    hide screen blktone
    show screen bld1
    hide screen hermione_main

    call her_main("...fine. Just let me... there we...","open","angryCl",ypos="head") #253

    #*Penetration transition*
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris

    call her_main("OOOOOOOHH! {image=textheart}","body_235") #254
    call her_main("Yes...","body_236") #255

    hide screen hermione_main
    hide screen genie
    $ genie_chibi_xpos = -170 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 35
    $ g_c_u_pic = "bounce_ani_s"
    show screen desk_03
    show screen g_c_u
    hide screen blkfade
    with d3

    ">Hermione begins to slowly slide up and down your dick."
    m "You can do better than this! Pick up the pace whore!"
    call her_main("Ah... ah...{image=textheart}","body_237") #256
    "She moves a little faster..."
    $ g_c_u_pic = "bounce_ani"
    show screen g_c_u
    m "Did you hear me, slut? I said go faster you little whore!"
    ">You feel a shiver pass through her with each insult."
    m "Go."
    call soft_slaps
    m "Faster."
    call soft_slaps
    #">You punctuate each word with a slap to her ass."
    call her_main("AAAH! {image=textheart} {image=textheart} {image=textheart}","open_tongue","ahegao_raised",cheeks="blush") #257
    "She starts to move much faster."
    $ g_c_u_pic = "bounce_ani_f"
    show screen g_c_u
    call her_main("Yes! Harder!","body_232") #258
    m "Honestly."
    ">You reach under her shirt with one hand and start to twist and pull on one of her nipples."
    ">You spank even harder with the other."
    call hard_slaps
    call her_main("IT HUUURTS! {image=textheart} {image=textheart}","smile","angry",cheeks="blush") #259
    m "Even now, I still have to take the initiative, you self-deluding whore!"
    call her_main("I- AH! {image=textheart} I'm n- Ah-a!","body_235") #260
    m "You're still claiming this is all just for the house points? Even while you're bouncing yourself up and down on my cock? "
    call her_main("I-i-it i-i-i-isss- Ah! {image=textheart}","body_236") #261
    m "All right, fine. Prove it. If you can go {i}ONE FULL MONTH{/i} without any form of sexual relief;"
    m "I'll award \"Gryffindor\" {i}ONE THOUSAND{/i} points and double the points of any favours you choose to take thereafter."
    call her_main("!!!! REALLY?! (Oh god, I'm getting so close...)","soft","wide") #262
    m "Yes. BUT. If you can't, you belong to me. No more house points. You'll be my personal fucktoy from then on. Do we have a deal?"
    call her_main("Yessss...","body_236") #263
    m "Answer me clearly, whore! Do we have a deal?"
    call her_main("OH GOD! YES! YES WE HAVE A DEAL!","body_234") #264
    call her_main("I! I'M-","body_234") #265
    stop music fadeout 1
    m "Good."

    show screen blkfade
    with fade
    hide screen desk_03
    hide screen g_c_u
    $ hermione_chibi_xpos = 500 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen genie

    ">You lift Hermione off of you."
    call her_main("!!! W-what are you-","shock","wide",cheeks="blush") #266
    m "We did just make an agreement. Of course if you wish to forfeit already..."


    hide screen bld1
    hide screen blkfade
    with d3

    #show full sprite and chibi in middle

    call her_main("I- N-no! I was just surprised.","angry","worriedCl",cheeks="blush",emote="05",xpod="right",ypos="base")
    m "Oh, and before I forget."
    call cast_spell
    ">You cast a spell on Hermione"
    m "There."
    call her_main("What did you just do?","mad","wide",cheeks="blush")
    m "I cast a spell to prevent you from feeling any relief."
    m "After all, it wouldn't due for you to lose by accident! This is a test of character, not chance. "
    call her_main("I suppose.","annoyed","angryL",cheeks="blush") #*Looks at you cautiously*
    call her_main("...Thank you.","open","baseL",cheeks="blush")
    m "You'll need to stop by every morning so I can reapply it."
    call her_main("I-very well. Until then.","disgust","down_raised",cheeks="blush")

    call hermione_exit
    $ hermione_busy = True

    m "Well. My balls are going to be the right colour for a little while..."
    show screen blkfade
    with fade
    $ hg_pf_TheGamble_OBJ.points = 1
    $ hg_pf_TheGamble_Flag = True
    $ hg_pf_TheGamble_FlagA = True
    jump night_start

label hg_pf_TheGamble_complete:

    if hg_pf_TheGamble_FlagA:
        jump hg_pf_TheGamble_TellSnape
    elif hg_pf_TheGamble_FlagB:
        pass
    elif hg_pf_TheGamble_FlagC:
        jump hg_pf_TheGamble_MySlave_n


    if hg_pf_TheGamble_OBJ.points < 3:
        if hg_pf_TheGamble_OBJ.points == 1:
            #*Scene transitions to morning. Hermione enters.*

            call hermione_enter

            call her_main("","normal","worriedCl")
            call her_main("G-good morning, [genie_name].","upset","wink")
            ">Hermione can't stop twitching and fidgeting."
            m "Good morning, Miss Granger."
            m "Hm. You don't appear to have slept well. Is something the matter?"
            call her_main("I-no! I mean- its fine.","disgust","narrow")
            m "...If you say so."
            call cast_spell
            ">You cast a spell on Hermione"
            m "There you go. Until next time."
            call her_main("I-yes.","angry","worriedCl",emote="05")
            $ hg_pf_TheGamble_OBJ.points += 1
        elif hg_pf_TheGamble_OBJ.points == 2:
            #*Scene transitions to morning*

            m "Huh. What do you know? She's late."
            pause 1.0
            ">Hermione enters the room dazed and distracted"
            call hermione_enter

            m "Miss Granger?"
            m "Hello?"

            hide screen genie
            show screen chair_left
            hide screen desk
            show screen desk
            show screen genie_stand
            with d3
            #"You stand and move out from behind the desk."


            m "{size=+7}WHORE!{/size}"
            with hpunch
            ">Hermione jumps"
            call her_main("I- Oh. Good morning [genie_name]...","grin","dead")
            ">As she trails off you notice her repeatedly glancing at your crotch."
            m "You don't seem to have improved from yesterday morning. Did you sleep at all?"
            call her_main("I-","base","down")
            ">her hands keep drifting towards her groin and chests before she jerks and moves them away"
            call her_main("I'm fine.","grin","dead")
            m "Are you certain?"
            call her_main("I, uh, I need to get to class.","soft","ahegao")
            m "Very well, then."
            call cast_spell
            ">you cast the spell."
            call her_main("","base","down")
            ">Hermione glances at your groin one last time before she leaves."
            $ hg_pf_TheGamble_OBJ.points += 1

        jump end_hg_pf

    else:
        jump hg_pf_TheGamble_MySlave




    label hg_pf_TheGamble_TellSnape:
        #*Scene skips to Genie and Snape drinking wine by the fire.*
        show screen with_snape_animated
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...

        $ fire_in_fireplace = True
        hide screen genie
        hide screen chair_right
        hide screen desk
        show screen fireplace
        show screen desk

        hide snape_stand #Snape stands still.
        hide screen bld1
        hide screen snape_main
        with d3


        hide screen blkfade
        with fade
        "You tell Snape about what happened."
        sna_[5] "!!! You did what!? Are you completely MAD?!"
        m "Not completely, no. All is well in hand. Stop worrying so much."
        sna_[4] "But-"
        m "Think about it."
        m "I've spent how long getting her hooked on orgasms? And now I've forced her to go cold turkey."
        m "No matter how much she masturbates or how frantically she fucks she can't cum."
        m "She can still get excited, though."
        m "With her frustration constantly building, I wouldn't give her much before she snaps. A week, week and a half, tops."
        sna_[11] "Hmm... Well, we'll just have to hope for the best."
        m "It will all work out. Just trust me."
        $ hg_pf_TheGamble_FlagA = False
        $ hg_pf_TheGamble_FlagB = True
        jump day_start

    label hg_pf_TheGamble_MySlave:
        #*Scene transitions to morning*
        pause 0.25
        # call play_sound("door") #Sound of a door opening.
        # $ walk_xpos=570 #Animation of walking chibi. (From)
        # $ walk_xpos2=400 #Coordinates of it's movement. (To)
        # $ hermione_speed = 2.1 #The speed of moving the walking animation across the screen.
        # call play_sound("door") #Sound of a door opening.
        # show screen hermione_walk_01
        # with d4
        # pause 2.1
        # $ hermione_chibi_xpos = 500 #Near the desk.
        # show screen hermione_blink #Hermione stands still.
        # with d3
        ">Hermione enters. She does not look happy"
        call hermione_enter
        m "Miss Granger?"

        call her_walk(400,320,1.25)
        show screen blkfade
        with fade
        "She says nothing as she walks around the desk."
        #show screen blktone
        m "Mi-"


        call play_music("playful_tension") # SEX THEME.
        hide screen hermione_main
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_left
        show screen g_c_u

        hide screen hermione_blink #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        show screen bld1
        with d3
        #"You're interrupted as she jerks your pants down and swallows your cock to the root."
        ">Hermione jerks your pants down and swallows your cock to the root."



        m "HOLY! I suppose this means you forfeit?"
        her "Gobble! Glurk! Gulp!"
        #"She says nothing, the only noise she makes are the desperate mewling and the sounds of gobbling your dick."
        ">Hermione says nothing, the only noise she makes is the desperate mewling and gobbling of your dick."
        m "Have it your way."
        ">You grab her head and start to fuck her throat."
        m "YES! TAKE IT ALL THE WAY DOWN!"
        her "!!! Gobble -- Gobble -- Gobble!!!!"
        m "USE YOUR TONGUE, YOU FILTHY BITCH!"
        her "Gobble! Lick! Lick! Lick! Gobble!"
        m "(Damn. The past couple days are getting to me. I was hoping to make this last.)"
        ">You force your pulsing cock all the way down her throat and start cumming."

        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u # SUCKING
        with d3
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch


        her "GHT!!!!"
        m "ARGH!!!"
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "SUCK IT ALL OUT!"
        her "GULP! GULP! GULP! GULP!"
        m "Ah!"

        ">As you release her, Hermione falls to the ground shivering."
        ">She doesn't seem very coherent as she grasps at your leg."

        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani"
        call u_pause_ani
        # show screen h_c_u
        # hide screen g_c_u
        # with d3
        show screen blkfade
        with d3
        hide screen h_c_u # NOT SUCKING

        #her "Please- Give- Need- Please!"
        call her_main("Please- Give- Need- Please!","grin","wink",cheeks="blush",ypos="head")
        m "So much for a month! You couldn't even last a week!"
        #her "Need- Please-"
        call her_main("Need- Please-","scream","wide",cheeks="blush")
        #">She scrambles to stand as you lift her by her hair and half toss her onto the desk."
        ">Hermione scrambles to stand as you lift her by her hair and half toss her onto the desk."
        m "Well, since you asked so nicely."

        #*penetration transition*
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris

        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u

        hide screen blkfade
        with d3


        #her "AAAAAAAAAAHHH! Biiiiiiig!!!!!"
        call her_main("AAAAAAAAAAHHH! Biiiiiiig!!!!!","open_tongue","ahegao_raised",cheeks="blush")
        m "Has your pussy actually gotten tighter?"
        #her "AAAAH! NO! NO! STILL NEEEEED!!!"
        call her_main("AAAAH! NO! NO! STILL NEEEEED!!!","mad","wide",cheeks="blush")
        m "Oh, right the spell. Well, you'll just have to wait till I'm ready to cum myself."
        #her "!!!"
        call her_main("!!!","mad","angry",cheeks="blush")
        ">Hermione starts slamming herself against you with abandon."
        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        with hpunch
        #her "GIVE! GIVE! GIVE! GIVE! GIVE!"
        call her_main("GIVE! GIVE! GIVE! GIVE! GIVE!","base","ahegao_raised",cheeks="blush")
        ">With every thrust she seems to get tighter."
        m "FUCK! ALMOST. ALMOST! HERE WE GO!"
        ">You undo the spell as you flood Hermione's cunt with your cum."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen g_c_u
        pause .35
        with d3
        pause .15
        show screen remove_spell
        pause 1.7
        hide screen remove_spell
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc

        $ g_c_u_pic = "pause_sex"

        call her_main("!!!!","body_234")
        ">Hermione tries to scream but can only manage to gasp and convulse as she finally gets her release."
        ">You watch her and wait for her spasms to die down."

        show screen blkfade
        with d3
        hide screen g_c_u

        m "Can you understand me?"
        ">Hermione's eyes are still glassy but she nods."
        m "Good. A deal is a deal. You belong to me now. Understand?"
        call her_main("Yesss.","disgust","down_raised",cheeks="blush")
        m "Ready for more?"
        ">Still twitching on the ground, she speaks slowly, as though her thoughts are traveling through molasses."
        call her_main("I... but... class...","shock","wide",cheeks="blush")
        m "Oh, you're not going to class."
        m "I'm going to thoroughly enjoy my first day as your owner."
        ">You walk to the door and send for Snape."
        m "Now, what to do next... Ah! I know!"
        ">You walk over to Hermione and lift her. Keeping her back to your chest and your hands under her thighs, you hold her up with her legs spread."
        m "Now put your hands around the back of my neck and tell me what you are."
        call her_main("Your whore.","grin","wink",cheeks="blush")
        m "Wrong."
        call her_main("?","scream","wide",cheeks="blush")
        m "You see, whores get paid. Whores are people."
        m "You don't get paid. You stopped being a person when you sold yourself to me for release."
        m "You are my slave now. My toy. My pretty little fucktoy."
        m "SAY IT."
        call her_main("I'm your fucktoy.","disgust","down_raised",cheeks="blush")
        m "Now, what does a fucktoy want?"
        ">You lower her, teasing her asshole with the tip of your cock."
        call her_main("N-Nothing. A toy w-wants nothing. It's just used by its owner.","wide_open_tongue","ahegao_mad",cheeks="blush")
        m "VERY good."
        ">You drop her onto your dick."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_main("MY AAASS!!!","open_tongue","ahegao_raised",cheeks="blush")
        m "Whose ass?"
        ">You lift her off your dick."
        call her_main("YOURS! YOUR FUCKTOY'S ASS!","soft","dead")
        ">Desperate tears form in her eyes."
        m "Since it is your first day, I'll be nice."
        m "I'll give you a few choices."
        m "Do you want me to fuck your ass?"
        call her_main("Yes.","wide_open_tongue","ahegao_mad",cheeks="blush")
        m "How?"
        call her_main("Haaard. Pound me. Fill me with your cum!","base","ahegao_raised",cheeks="blush")
        m "As you wish!"
        ">You drop her back onto your dick and start pounding her ass, your dick is harder than it's ever been."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_main("MY ASS!!! YOU'LL BREAK IT!!","open_tongue","ahegao_raised",cheeks="blush")
        ">You lift her up slowly, making the threat clear."
        call her_main("AHH!! BREAK IT!! BREAK ME!! HARDER!!","body_236")
        call snape_enter
        sna_[1] "What did you-"
        sna_[8] "!!!"
        call her_main("CUMMING!! MY ASS IS CUMMING!!","body_236")
        m "As you can see, Miss Granger will be indisposed."
        ">Hermione's grip slips and she catches herself on your desk. She quivers as you adapt and start pounding her from behind."

        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        hide screen blkfade
        with d3

        m "Can you arrange an excuse for the next day? Or three?"
        call her_main("AAAAH! OH GOD!","body_238")
        sna_[18] "Ha! Of course!"
        call her_main("AGAIN!! CUMMING AGAIN!! {image=textheart} {image=textheart}","body_237")
        sna_[21] "(This might be the happiest day of my life!)"
        call snape_leave
        ">Hermione kept screaming and shaking her ass on your dick. You're fairly certain she didn't notice the conversation."
        call her_main("I'm going insane! Your dick is driving your fucktoy insane!","body_236")
        m "You and your way with words!"
        call her_main("CUMMING! STILL CUMMING!","body_234")
        m "Here, let me JOIN YOU!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc


        call her_main("MY ASS! SO HOT!","body_235")
        call her_main("FILLING MY ASS!","body_236")
        m "YOU LIKE IT?"
        call her_main("YES!!!! {image=textheart} {image=textheart}","body_234")
        m "HAVE SOME MORE!"
        ">Hermione tries to scream as you flood her ass but once again can only manage gasps as she collapses to your desk, quivering."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc

        m "So, Toy, what should... Toy?"
        ">Hermoine lies there, unresponsive to your words and shakes."
        $ g_c_u_pic = "pause_sex"
        m "Huh. She passed out. I guess having the biggest orgasms of your life after being too horny to sleep for three days will do that."
        m "Now, how to pass the time..."
        $ hg_pf_TheGamble_FlagB = False
        $ hg_pf_TheGamble_FlagC = True
        jump night_start

    #transition to nighttime menu
    #after daytime menu

    label hg_pf_TheGamble_MySlave_n:
        #$ hermione_chibi_xpos = 500 #Near the desk.
        #$ hermione_chibi_ypos
        #show screen hermione_blink #Hermione stands still.
        #hide screen blkfade
        #with d3
        #$ h_c_u_pic = ""
        #show screen h_c_u

        her "Hn... Wha... Where..."
        m "Good evening, Toy. I was beginning to worry."
        her "Oh... Oh God... I - we - the bet-"
        m "You lost the bet, yes, and then you passed out. I had to entertain myself. I hope you don't mind."
        her "Mind?"
        m "You Haven't noticed?"
        her "...Noticed what?"
        m "This."
        "You rip the anal beads out in one motion."
        her "!!!!"
        "She had started to rise but promptly falls back to the desk as her legs give out."
        m "Now that you're more or less in your right mind, I will make myself perfectly clear. We had an agreement."
        her "I-"
        "You walk behind her, grasp her hips and forcefully shove her ass against you. Your rigid cock grinding against the lips of her pussy."
        m "You made your own choices. Took your chances. And you FAILED.So now you. Are. MINE."
        "You slip your hand to her cunt, and shove your fingers inside."
        m "THIS belongs to me."
        her "Ah-"
        "You remove your fingers, now sopping wet. You give her young, bountiful ass a slap and plunge your thumb into her tight asshole."
        m "THIS belongs to ME."
        her "HAH-AH-"
        "You start pumping her ass with your thumb as you slowly rub her pussy with your dick."
        m "Is that clear?"
        her "..."
        her "*sobs* yes."
        m "Good."
        "You open a desk drawer, remove a black leather collar, and toss it in front of her face."
        m "Put it on."
        "Crestfallen, she slowly puts it on."
        m "A few key points. That collar is enchanted. Only you could put it on and only if you were willing. If you were unwilling, it would refuse to close."
        m "Only I can remove it. If you refuse my orders it will activate an aphrodisiac charm as well as the same charm I cast on you for the last three days until you comply."
        m "I can, of course, activate it at will as well."
        m "Now, get on your knees."
        "Once she's done so, you rip her shirt open. You pay the flying buttons and her halfhearted sounds of protest no mind."
        "You grab her tits roughly in each hand; jerking her forward, and wrapping them around your cock."
        "You twist her nipples as you thrust between her breasts."
        her "...Ah... ha... ah..."
        m "Do you like this, Toy?"
        her "...Ah... n-no..."
        m "Tell me the truth, Toy. Do you enjoy this?"
        her "N-no- AH-AH-AH!!!"
        "Her panting becomes even heavier and her hands quickly move to her pussy."
        her "I -AH!- I-"
        "Her breath hitches as she frantically stirs her pussy with her fingers."
        her "N-AH!- -HAH!- YES! {image=textheart} {image=textheart} YES! I ENJOY IT!!"
        "Her hips start to rock, and you squeeze her tits with force."
        her "AH! {image=textheart}"
        m "Are you you going to cum?"
        her "YES!! {image=textheart}"
        m "Are you going to cum from having your tits manhandled?"
        her "*sobs* YES!!! {image=textheart}"
        m "No, you're not. You're not allowed to cum before I do."
        her "!! AH! NO! PLEASE!"
        m "Tell me what I am slave! Who are you begging?"
        her "MASTER! MY MASTER! PLEASE LET ME CUM, MASTER!"
        m "What? Did I not make myself clear before? You're my little toy. What does this little toy want?"
        her "CUM ON ME, MASTER! COVER ME IN JIZZ! DROWN ME WITH YOUR SPUNK!"
        m "You and your words! Everytime!"
        "As you soak her hair, face, and perky teen tits with your cum, Hermione's body starts to spasm."
        "You have trouble keeping your hold on her as she her back bows and her body jumps in place."
        "You couldn't say how many times the pain caused by her own thrashing makes her cum as you hold tight to her tits."
        "Eventually, she collapses against you. You can feel her breath on your cock."
        m "Look at yourself."
        m "All of that pride and self-righteousness you had at the beginning, and now you're collapsed against me, drooling on my dick, and... you can't even hear me, can you?"
        "You grab her hair and slap her face."
        m "Can you!"
        her "AH!! {image=textheart} AH!! {image=textheart} AH!! {image=textheart}"
        "Your slap sends a short series of tremors through her body."
        "As you watch her hips buck, you feel your dick growing harder."
        m "...I am not waiting for morning."
        m "Come on. Up and at 'em."
        "You start slapping her face with your cock, careful not to hit hard enough to send her into another round of paingasms."
        her "..."
        "She moans blearily as you cockslap her back to some semblance of consciousness."
        m "Wakey, wakey. Now, what should you be doing?"
        "You let go of her hair. Her eyes are still dazed as she opens her mouth, tongue sticking out, and tries to catch your still swaying dick in her mouth."
        "She fumbles at first and you find yourself tempted to tease her. Before you can decide she manages to get her lips around your cockhead and holds on stubbornly, if weakly."
        "She slowly forces your cock deeper and deeper into to her throat."
        her "Glurk... Gobble... Lick..."
        m "Do I need to explain what will happen if you don't pick up the pace?"
        "The threat seems to rouse her some."
        her "GLURK! GOBBLE! GOBBLE! GULP!"
        "As her motions become more frantic, you can't stop your hips from thrusting."
        m "See? That wasn't so difficult. Now, take a deep-breath through your nose..."
        "You grab her by her soaked, matted hair and force you dick as far as it will go and keep it there."
        her "..............."
        m "Oh, yes. Your throat is the best."
        her ".............................."
        m "Actually, I can't think of any part of your body that isn't."
        her ".............................."
        m "It's as though you were made to be my personal plaything!"
        her "......"
        m "I suppose I'm really quite blessed."
        her "!!!"
        m "Hm? what's this?"
        "You watch as Hermione's hips start to roll."
        her "!!!!!!!"
        m "Oh, this is just precious!"
        "Hermione's hand has drifted toward her pussy."
        her "!!!!!!!!!!"
        m "Here I am, choking you with my cock, and not only are you getting off, you're actually masturbating!"
        "She wildly fingers herself with one hand as the other firmly rubs your balls with the other."
        her "!!!!!!!!!!!!!!"
        m "I don't know what I could have done to deserve a wonderful little toy like you! Now, TAKE IT ALL!"
        her "GHT!!!!!!!!"
        "Your fucktoy's eyes roll back as you flood her throat, her hand has stopped massaging your balls and is now twisting one of her nipples."
        her "GULP! GULP! GULP! GULP! GULP! GULP! GULP!"
        m "ALL OF IT! DOWN YOUR THROAT!"
        "As her body is once consumed by her climax, you hold tight to her hair."
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "COME ON! ALMOST DONE!"
        her "GULP! GULP! GULP! GULP!"
        "You pull her off your dick. It takes more effort than you expected, and are rewarded with an interesting popping sound, accompanied by a more interesting sensation."
        $ renpy.play('sounds/pop02.mp3')
        "Not having finished, you spatter her face with still more of your cum."
        m "There!"
        "You let go of your toy's hair and she falls to the ground, still jerking and twitching."
        m "Oooh, no. No, you don't. You're not passing out again."
        "You gently shake her, trying to keep her awake."
        m "I should have known better. Here."
        "After you're (mostly) certain she won't pass out again, you hand her a slip of paper."
        m "Take this hall pass and go take a bath at the prefect's bath. The password should be lemony fresh. Then go to bed."
        "She blinks blearily at the pass and then at you. You can almost see as she tries to form a coherent thought."
        m "Don't be mistaken. You're my new little fucktoy, and I intend to make frequent and hard use of you for as long as I am able."
        m "That means I need to keep you well maintained."
        m "Now go."
        "Hermione staggers out of the room."
        $ hg_pf_TheGamble_Flag = False
        $ per_quest_30c = False

        jump day_start
