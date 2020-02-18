

### Ravenclaw vs. Hufflepuff ###

label start_hufflepuff_match:
    call cho_main(xpos="mid", ypos="base", trans=fade)
    m "[cho_name], what do you say... ready for your first game of the season?"
    call cho_main("To be honest, [cho_genie_name], I'm feeling quite nervous.","soft","base","sad","R")
    m "Don't worry. I believe you are ready..."
    m "When are you going to play against Hufflepuff?"
    call cho_main("That's up to you, [cho_genie_name]. As headmaster you decide when the games will be held...","open","base","base","mid")
    m "So if I were to say tomorrow, it will happen tomorrow?"
    call cho_main("Yes, [cho_genie_name].","base","base","base","mid")
    g9 "Well then, tomorrow it is!"

    if raining:
        call cho_main("Sounds great, [cho_genie_name]. I just hope it stops raining until then.","soft","base","base","R")
    elif snowing:
        call cho_main("Sounds great, [cho_genie_name]. I just hope it stops snowing until then.","soft","base","base","R")
    else:
        call cho_main("Sounds great, [cho_genie_name]. I just hope the weather stays like it is too.","soft","base","base","R")

    m "With our tactics, this will be a piece of cake!"
    call cho_main("I hope you're right, [cho_genie_name].","base","base","base","mid")
    call cho_main("Anyhow, I need to prepare for the game.","soft","base","base","R")
    call cho_main("See you then, [cho_genie_name]!","smile","base","base","mid")
    m "Good luck!"

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho_quid.lock_training = True
    $ cho_quid.lock_practice = True

    $ cc_event_pause  += 1  # Event starts on the next day.
    $ cc_summon_pause += 1 # Can't be summoned until next event.

    $ cho_busy = True

    $ hufflepuff_match = "start"

    jump end_cho_event


### Main Match Against Hufflepuff ###

label hufflepuff_match:

    ### Event Setup ###
    $ cho_outfit_last.save()
    $ her_outfit_last.save()

    $ cho.equip(cho_outfit_quidditch)
    $ hermione.equip(her_outfit_default)


    # Scene before Match against Hufflepuff
    call play_music("stop")

    call sna_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    call play_music("snape")
    call sna_main("Are you ready to go?","snape_03",xpos="base",ypos="base")
    g4 "Can't you bloody knock?!"
    call sna_main("Should I?{w} I was sure you were already waiting for me...","snape_05")
    m "For what?"
    call sna_main("We have to head out for the pitch. The whole school is waiting on you.","snape_24")
    m "Didn't you nag me earlier not to leave this room unless absolutely necessary?"
    call sna_main("A rule which I’m sure you have disregarded a great many times already...","snape_29")
    call sna_main("You'll have to join me on this one. As headmaster, you are expected to attend the Quidditch matches.","snape_06")
    m "And that’s today?"
    call sna_main("Indeed.","snape_03")
    m "(...)"
    m "Wouldn’t the other teachers see me if I went?"
    call sna_main("Don't worry. I’ve arranged to have us moved from the teachers' seats to the commentator booth.","snape_24")
    call sna_main("Just the two of us...","snape_23")
    m "And Miss Granger?"
    call sna_main("Granger...","snape_08")
    call sna_main("Well, that’s very displeasing to say the least...","snape_07")
    call sna_main("In any case, you won't be seen up close by any of the other teachers.","snape_09")
    m "Sounds like a snore. Can't I stay here and you’ll tell them I'm ill or something?"
    call sna_main("No.","snape_04")
    call sna_main("That would just prompt the nurse to examine you closely...","snape_03")
    m "Well... I wouldn’t mind that."
    call sna_main("I’m sure you wouldn’t...","snape_06")
    call sna_main("Good thing though is that we’ll be able to bring a little something to keep us occupied.","snape_20")
    call hide_characters
    with d3

    # Show wine
    call give_reward(text=">Not grape-juice.",gift="interface/icons/item_wine.png")

    m "That's all the persuasion I needed my friend!"

    # Teleport
    call play_sound("kick")
    show screen chair_left
    show screen desk
    call gen_chibi("hide")
    with d3

    call gen_chibi("stand","door","base")
    call teleport(position="genie", effect=False)
    pause.5

    call gen_chibi("stand","door","base", flip=False)
    with d3
    pause.2

    call bld
    m "What are we waiting for. Let's go!"

    call sna_chibi("stand","mid","base",flip=True)
    hide screen bld1
    with d3
    pause.2

    call sna_main("(When did he?...)","snape_05",ypos="head")
    call sna_main("After you...","snape_09",ypos="head")
    pause.8

    m "Actually, I have no idea where we're going."

    call gen_chibi("stand","door","base")
    with d3
    pause.2

    call bld
    m "You should lead the way..."
    call sna_main("Right you are. Time to get smashed!","snape_02",ypos="head")

    call sna_walk(700, "base")

    # Blackfade
    stop music fadeout 2
    stop bg_sounds fadeout 2
    call play_sound("door")
    call blkfade
    pause 2

    ">You make your way towards the pitch with Snape, pondering if this was such a good idea."
    call play_sound("grass")
    ">After walking for a while across the school grounds a huge oval shaped pitch with massive towers around it looms before you."
    ">Amazed by...{w=0.6}{nw}"
    m "Agrabah's towers are larger..."
    ">Amazed... by the sight, Snape then leads you to the base of one of the towers."

    # Pitch entrance
    centered "{size=+7}{color=#cbcbcb}At the Quidditch pitch...{/color}{/size}"

    call room("quidditch_pitch")
    play bg_sounds "sounds/outskirts.mp3" fadein 2
    call sna_chibi("stand", "right", "base")
    call gen_chibi("stand", "mid", "base", flip=True)
    call hide_blkfade

    m "So, this is it? This is where the quidditch is played?"
    call sna_main("Of course, did you expect something else?","snape_05",ypos="head")
    m "I mean... What's the point of the grass and sand? Isn't it played in the air?"
    call sna_main("...","snape_25",ypos="head")
    m "Wouldn't it make more sense to have the ground be something soft if they fall?"
    g9 "Like...{w=0.3} magic marshmallow or something..."
    call sna_main("You think there's a spell for everything?","snape_35",ypos="head")
    m "From previous experiences with this world so far...{w} yes, pretty much."
    call sna_main("Anyhow... time go get moving, this place will be filled with teachers and students any minute now.","snape_03",ypos="head")
    call sna_main("After me...","snape_02",ypos="head")

    call sna_walk(path=[("stairs_base","base"),("stairs_up","stairs_up")])
    call gen_walk(650)
    call chibi_emote("exclaim", "genie")
    pause 0.8
    call chibi_emote("hide", "genie")
    call gen_chibi("stand_alt")
    with d3
    pause 0.8
    g9 "(*He-heh*... \"Snape sux\"...)"
    call gen_chibi("stand")
    call gen_walk(path=[("stairs_base", "base"),("stairs_up","stairs_up")])

    call blkfade

    # Sound check
    if get_volume_preference('music') < 0.1 or get_volume_preference('sfx') < 0.1:
        sil "This section of the game is best played with the sound turned on. Go to preferences to set the volume."

    pause 1

    # Pitch stands
    call room("quidditch_stands")
    $ qp_mob = 2 # Controls number of people
    $ qp_mob_reaction = [None, None, None] # Reset reactions
    #call sna_chibi("stand", 210, -40+250, flip=True)
    #call gen_chibi("stand", 130, 10+250)
    #call her_chibi("stand", 375, 105+186, flip=True)
    $ snape_chibi.zorder = 2
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 4

    ### Main Match Starts ###
    play bg_sounds "sounds/crowd.mp3" fadein 2
    call hide_blkfade
    pause 1

    call play_sound("footsteps")
    pause.8
    call sna_chibi("stand", 210, -40+250, flip=True)
    with d3
    pause.8
    call sna_chibi("stand", flip=False)
    with d3
    sna "Careful at the top. Don't hit your head."
    call play_sound("kick")
    with hpunch
    pause.6
    g4 "Bloody hell!"
    call play_sound("footsteps")
    pause.8
    call gen_chibi("stand", 130, 10+250)
    with d3
    pause.5
    call sna_chibi("stand", flip=True)
    with d3
    sna "Well, here we are..."
    sna "Now we are only waiting for-"
    call her_chibi("stand",220,50+186, flip=True)
    with d3
    pause.5
    call her_chibi("stand",230,50+186, flip=False)
    with d3
    her "Professors."
    sna "Granger..."
    call her_chibi("stand",220,50+186, flip=True)
    with d3
    pause.2
    call her_walk(375, 105+186)
    pause.5
    call her_main("Good Morning everyone, and welcome to the i-inaugural-", "soft", "base", "worried", "mid", flip=True, xpos="120", ypos="base")
    call her_main("", "normal", "base", "worried", "mid")
    call sna_main("Speak up girl! And would it kill you to enunciate?!","snape_03",ypos="head")
    call her_main("*Grrr*", "mad", "narrow", "angry", "R")
    call her_main("", "open", "closed", "angry", "mid")
    call her_main("Welcome to the first Quidditch game of the season...{fast}", "open", "base", "worried", "mid")
    $ qp_mob = 3
    call sna_main("Better... You’ve advanced from Troll to Dreadful....","snape_09",ypos="head")
    call her_main("", "normal", "closed", "base", "mid")
    m "{size=-4}Troll?{/size}" # Small text.
    call sna_main("{size=-4}Those are grades we give out to our students, for decidedly poor performances, like Granger’s...{/size}","snape_01",ypos="head")
    call her_main("...", "mad", "base", "angry", "mid")
    with hpunch

    stop bg_sounds fadeout 4

    call her_main("{size=+5}Quiet Please!{/size}", "scream", "base", "angry", "mid")
    call her_main("...", "normal", "closed", "angry", "mid")

    play bg_sounds "sounds/crowd_low.mp3" fadein 2

    call her_main("Thank you...", "open", "happy", "base", "mid_soft")
    call her_main("L-let's begin!", "base", "base", "base", "mid")

    call play_music("quidditch")

    call her_main("Hufflepuff versus Ravenclaw!", "smile", "base", "base", "mid_soft")
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo8"
    $ renpy.sound.play("sounds/crowd_cheer.mp3")
    ">A loud cheer roars from the grandstands."

    # Speech
    call her_main("And now, to say a few words and declare the games open, Professor Dumbledore!", "open", "closed", "base", "mid")
    call her_main("", "base", "base", "base", "mid_soft")
    call ctc

    hide screen hermione_main
    with d3

    m "{size=-4}What? Isn’t that me?{/size}"  # Small text.
    call sna_main("It is.","snape_02",ypos="head")
    $ qp_mob_reaction[2] = None
    m "Why did no one warn me about this?"
    $ qp_mob_reaction[1] = None
    call sna_main("I’ve been looking forward to watching you bumble your way through this...","snape_22",ypos="head")
    $ qp_mob_reaction[0] = None
    call sna_main("Besides, you only have to give some trivial speech about team spirit, gesticulate wildly and say \"let the games begin\". A child could manage it.","snape_24",ypos="head")
    call sna_main("Now get up there!","snape_10",ypos="head")

    stop bg_sounds fadeout 4
    stop music fadeout 2

    $ hermione_chibi.zorder = 4
    $ genie_chibi.zorder = 3
    call her_chibi("stand",350,185+186, flip=True)
    with d3

    call gen_walk(360, 45+250)

    $ genie_zorder = 15

    call gen_main(face="base", base="base", xpos=100, ypos=120)
    call ctc

    call gen_main("", face="angry")

    menu:
        "(Shit, what do I even talk about?)"
        "\"Miracles\"":
            play bg_sounds "music/fanfare.mp3" fadein 1.0
            call gen_main("Great moments are born from great opportunity.",face="base")
            ">A reverent hush falls over the crowd..."
            call gen_main("And that’s what you have here tonight-",face="base")
            call gen_main("That's what you've earned here tonight!",face="base")
            hide screen genie_main
            with d3
            pause .8

            $ renpy.sound.play("sounds/killswitch_on.mp3")
            $ qp_spotlight = True
            pause .8

            call gen_main("One game...",face="base")
            call gen_main("Tonight, WE are the greatest hockey team in the world!",face="base")
            call gen_main("You were born to be hockey players...",face="base")
            call gen_main("Every one of you...",face="base")
            $ qp_mob_reaction[0] = "emoq"
            call gen_main("And you were meant to be here tonight!",face="base")
            call gen_main("This is your time...",face="base")
            #Fade to black
            call gen_main("Their time is done, it’s over! I’m sick and tired about hearing what a great hockey team the soviets have!",face="base")
            $ qp_mob_reaction[1] = "qu"
            pause 1.5
            hide screen genie_main
            with d3
            mal "I think Dumbledore has finally started to lose his marbles..."
            mal2 "I think you might be right."
            play bg_sounds "sounds/wind_long_loop.mp3" fadein 2 fadeout 2
            $ qp_mob_reaction[0] = "sur"
            $ qp_mob_reaction[1] = None
            call gen_main("Screw it! This is our time...",face="base")
            $ qp_mob_reaction[0] = "sal"
            mal "..."
            $ renpy.sound.play("sounds/cough_male.mp3")
            $ qp_mob_reaction[1] = "sal"
            mal2 "..."
            $ qp_mob_reaction[0] = None
            $ qp_mob_reaction[1] = None
            $ qp_spotlight = False
            $ renpy.sound.play("sounds/killswitch_off.mp3")
            call gen_main("Now let the games begin!",face="base")

        "\"Freedom\"":
            play bg_sounds "music/fanfare.mp3" fadein 1.0
            call gen_main("Son's of Scotland!",face="angry")
            call gen_main("I am William Wallace...",face="base")
            $ qp_mob_reaction[0] = "qu"
            ">A confused murmur falls over the crowd."
            call sna_main("{size=-4}William Wallace?{/size}","snape_05",ypos="head")
            call gen_main("{size=-4}That's not your line...{/size}",face="angry")
            call gen_main("Yes... I am William Wallace!",face="grin")
            call gen_main("And I see a whole army of my countrymen, here in the defiance of tyranny...",face="grin")
            call gen_main("You have come to fight as free men, and free men you are. What would you do with that freedom? Will you fight?",face="grin")
            $ renpy.sound.play("sounds/murmur.mp3")
            $ qp_mob_reaction[1] = "emoq"
            hide screen genie_main
            with d3
            ">The sound of confused murmuring increases even further..."
            mal "Fight? Against what?"
            call gen_main("{size=-4}See, that guy knows his lines...{/size}",face="base")
            call sna_main("...","snape_03")
            call gen_main("Aye, fight and you may die...",face="base")

            call sna_chibi("stand",320,40+250, flip=True)
            call sna_main("I think it's time for you to step down from the...","snape_01")
            call gen_main("No, I'm just about to get to the best part!",face="angry")
            $ renpy.sound.play("sounds/cloth_sound.mp3")
            stop bg_sounds fadeout 2.0

            hide screen genie_main
            call sna_chibi("stand",300,40+250, flip=True)
            call gen_chibi("stand", 340, 45+250)
            with d3

            ">Snape then begins to drag you away from the podium."
            play bg_sounds "sounds/wind_long_loop.mp3"

            call gen_main("This is our chance... they may take away our microphones...{w=1.0} But they...{nw}{w=0.3}But they...{nw}",face="angry")
            $ renpy.sound.play("sounds/microphone_feedback.mp3")

            hide screen genie_main
            call sna_chibi("stand",320,40+250, flip=True)
            call gen_chibi("stand", 360, 45+250)
            with d3

            call gen_main("This is our chance... they may take away our microphones... {w=0.3}But they...{nw}{fast}{w=1.0}But they...{w=0.5}{nw}",face="angry")

            hide screen genie_main
            call sna_chibi("stand",280,40+250, flip=True)
            call gen_chibi("stand", 320, 45+250)
            with d3

            call gen_main("But they'll never take away our freedom!",face="angry")

            hide screen genie_main
            with d5

            $ snape_chibi.zorder = 3
            $ genie_chibi.zorder = 2
            call sna_chibi("stand",260,40+250, flip=True)
            call gen_chibi("stand", 340, 45+250, flip=False)
            with d3

        "\"Nam\"":
            play bg_sounds "sounds/wind_long_loop.mp3"
            call gen_main("{cps=7}Goooooooood{/cps}  morning,{w=0.1} Vietnam!",face="grin")
            call gen_main("Hey, this is not a test... This is rock and roll!",face="grin")
            call gen_main("Time to rock it from the delta to the DMZ!",face="grin")
            call gen_main("Is that me, or does that sound like an Elvis Presley movie?",face="grin")

            $ qp_mob_reaction[0] = "sal"
            $ qp_mob_reaction[1] = "emoq"
            ">A confused murmur falls over the crowd."
            call gen_main("Ugh...",face="base")

            $ renpy.sound.play("sounds/microphone_feedback.mp3")
            call gen_main("Is this thing on?",face="base")

            $ qp_mob_reaction[1] = "sal"
            $ renpy.sound.play("sounds/cough_male.mp3")
            mal "..."

            $ qp_mob_reaction[0] = "emoq"
            $ qp_mob_reaction[1] = "qu"
            call gen_main("It's O six hundred, what does the O stand for?",face="grin")
            call gen_main("Ooooh my god it's early!",face="grin")

            $ renpy.sound.play("sounds/murmur.mp3")
            ">The sound of confused murmuring increases even further..."
            mal "What's he on about? Is the fire lit but the cauldron empty?"
            mal2 "Looks like it..."
            call gen_main("Tough crowd... Anyway, let the games begin!",face="base")

    call play_music("quidditch")

    play bg_sounds "sounds/crowd_low.mp3" fadein 3 fadeout 2
    play sound "sounds/crowd_cheer.mp3"

    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo8"
    ">After a moment of confusion the crowd cheers excitedly, eager to see the match kickoff."
    $ qp_mob_reaction[0] = None
    $ qp_mob_reaction[1] = None
    $ qp_mob_reaction[2] = None

    call gen_walk(130, 10+250)

    $ snape_chibi.zorder = 2
    $ hermione_chibi.zorder   = 4
    $ genie_chibi.zorder = 3
    call gen_chibi("stand", 130, 10+250)
    call sna_chibi("stand", 210, -40+250, flip=True)
    with d3
    pause.2

    # Hermione commentates again.
    call her_chibi("stand",375,105+186, flip=True)
    with d3
    pause.8

    call her_main("Ugh... thank you for that, professor Dumbledore...", "soft", "narrow", "base", "R_soft", flip=True,xpos="120",ypos="base")
    call her_main("Now, to get this game underway!", "open", "closed", "base", "mid")

    # Player Introduction
    call her_main("First, let’s welcome everyone’s favourite underdogs, Ravenclaw!", "base", "happy", "base", "R")
    $ renpy.sound.play("sounds/crowd_stomping.mp3")
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    call her_main("", "base", "base", "base", "mid")
    ">The blue grandstand shakes violently with enthusiasm."
    call sna_main("At least try to sound like you’re awake, Miss Granger.","snape_03",ypos="head")
    call her_main("...", "normal", "closed", "angry", "mid", cheeks="blush")
    $ qp_mob_reaction[0] = None
    $ qp_mob_reaction[1] = None
    call her_main("And coming onto the field to face them are the equally impressive, Hufflepuff!", "open", "base", "base", "mid", cheeks="blush")
    $ renpy.sound.play("sounds/crowd_cheer2.mp3")
    $ qp_mob_reaction[2] = "emo8"
    call her_main("", "base", "base", "base", "mid", cheeks="blush")
    ">The yellow grandstand bursts into a mix of applause and whistles."
    hide screen hermione_main
    call sna_main("Back down to Troll...","snape_09",ypos="head")
    call her_chibi("stand",375,105+186, flip=False)
    with d3
    her "*grrrrr*"
    $ qp_mob_reaction[2] = None
    call her_chibi("stand",375,105+186, flip=True)
    call her_main("", flip=True,xpos="120",ypos="base")
    call her_main("It appears we’ve got an interesting game ahead of us. If I’m not mistaken, there’s some history between our seekers, Cho Chang and Cedric Diggory...", "crooked_smile", "closed", "base", "mid")
    call her_main("", "smile", "happy", "base", "mid_soft")
    ">Even though they are far down below on the pitch, you can clearly see Cho and Cedric glaring up at Hermione."
    call her_main("Given how essential the seekers role are in Quidditch, their complex past might cost one of them the game...", "open", "base", "base", "mid_soft")
    call sna_main("Complex past...","snape_01",ypos="head")
    call her_main("", "base", "closed", "base", "mid")
    call sna_main("I practically caught them chew each other’s tongues off at one point.","snape_02",ypos="head")
    call her_main("Speaking of important, I just realised that as the inaugural game, I should cover the rules of the game for any first-years watching.", "open", "happy", "base", "R")

    # Reading the rules
    stop music fadeout 4
    stop bg_sounds fadeout 2
    hide screen hermione_main
    ">Hermione heaves a heavy rule book{nw}"
    $ renpy.sound.play("sounds/punch01.mp3")
    ">Hermione heaves a heavy rule book{fast} from under the table and begins to monotonously recite it to the crowd."
    $ renpy.sound.play("sounds/sniff.mp3")
    her "..."
    play bg_sounds "sounds/wind_long_loop.mp3" fadein 2
    call her_main("The capturing of the snitch is worth 150 points-", "open", "narrow", "base", "down", flip=True,xpos="120",ypos="base")
    $ qp_mob_reaction[0] = "th"
    $ renpy.sound.play("sounds/murmur.mp3")
    call her_main("The game may not conclude until it has been caught, or an agreement is made between both capt-", "open", "base", "base", "mid")
    $ qp_mob_reaction[1] = "an"
    play bg_sounds "sounds/crowd.mp3" fadein 8 fadeout 2
    hide screen hermione_main
    mal "Just get on with it already you big-titted slag!"
    $ qp_mob_reaction[2] = "excl"
    mal2 "Yeh! Start the game!"
    qcr "START THE GAME! START THE GAME!"
    ">Hermione’s voice eventually gets drowned out by the growing restlessness of the crowd."
    call her_main("", "normal", "base", "base", "mid", xpos="120",ypos="base",flip=True)
    call her_main("Ugh, fine. If everyone wants us to begin play without knowing a SINGLE thing... then that’s OK! A good commentator knows when to accommodate for a crowd’s impatience!", "open", "closed", "base", "mid")
    hide screen hermione_main
    call sna_main("{size=-4}This should be good.{/size}","snape_02",ypos="head") # Small text.
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo8"
    $ renpy.sound.play("sounds/crowd_cheer.mp3")
    ">With that, the snitch and bludgers are released and fly off into the air."
    $ qp_mob_reaction[0] = None
    $ qp_mob_reaction[1] = None
    $ qp_mob_reaction[2] = None
    play bg_sounds "sounds/crowd_low.mp3" fadein 0.5 fadeout 0.5
    call her_main("Now then...", "open", "closed", "base", "mid", cheeks="blush", flip=True,xpos="120",ypos="base")
    call her_main("Let’s begin!", "base", "happy", "base", "mid_soft", cheeks="blush")
    hide screen hermione_main

    # Start of the Game
    $ renpy.sound.play("sounds/referee.mp3")
    call play_music("quidditch")
    ">A Grey haired woman then throws the quaffle into the air which signals the start of the match and the players quickly take off!"

    call her_main("Oh, wow... They’re going quite f-fast...", "normal", "wide", "worried", "shocked", flip=True,xpos="120",ypos="base")
    call her_main("", "normal", "happyCl", "base", "mid")
    call sna_main("Great commentary there girl... You might want to let them know the colour of the grass next...","snape_10",ypos="head")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call her_main("Um, I’m not sure if anyone’s scored yet...", "normal", "happy", "base", "mid")
    call her_main("Wait, that guy has the quaffle... I think...", "open", "squint", "base", "mid")
    call her_main("Scratch that last bit, he has a stick so he must be a beater!", "mad", "happy", "base", "mid")

    # Cho’s Skirt gets addressed
    show screen hufflepuff_match_cho_chase(1.0, 1.0)
    play bg_sounds "sounds/snitchloop.ogg" fadein 2 fadeout 2
    call her_main("Higher up, Cho seems to have caught an eye on the snitch and is chasing after it, directly followed by Cedric who...", "open", "slit", "low", "stare")
    show screen hufflepuff_match_cho_chase(1.0, 0.5)
    call her_main("Hold on a minute... Is Cho wearing a skirt?", "scream", "wide", "worried", "stare")
    $ renpy.sound.play("sounds/crowd_gasp.mp3")
    stop music fadeout 4
    $ qp_mob_reaction[0] = "emo02"
    $ qp_mob_reaction[1] = "excl"
    $ qp_mob_reaction[2] = "sur"
    call her_main("", "open", "wide", "worried", "shocked", cheeks="blush")
    qcr "!!!" # [screenshake?]
    play bg_sounds "sounds/crowd.mp3" fadein 2
    mal "..."
    $ renpy.sound.play("sounds/murmur.mp3")
    call her_main("", "open", "happyCl", "base", "mid", cheeks="blush")
    mal "She totally is!"
    $ renpy.sound.play("sounds/giggle2_loud.mp3")
    hide screen hermione_main
    "Female Student #1" "What a slut!"
    hide screen hufflepuff_match_cho_chase
    with d3

    call her_chibi("stand",375,105+186, flip=False)
    her "Professor, why won’t you say something? She’s clearly breaking the very basics of Quidditch rules!"
    m "I fail to see anything wrong with the way she’s dressed."
    her "But... she’s wearing a skirt!"
    her "Surely that must be against some kind of regulation..."
    m "You tell me Miss Granger, you’ve got the rulebook right there..."
    call sna_main("...","snape_13",ypos="head") # [Smirk]
    her "Perhaps I could get Madame Hooch to pause the game..."
    call her_chibi("stand",375,105+186, flip=True)
    call sna_main("Knowing her, she’s probably enjoying the sight of the Ravenclaw seeker rushing past her.","snape_20",ypos="head")
    call sna_main("{size=-4}Odds are she’s already tried to take a peek.{/size}","snape_20",ypos="head")  # Small text.
    m "{size=-4}Who’s Madame Hooch?{/size}"  # Small text.
    call sna_main("{size=-4}It’s that grey haired lady on the pitch that is seemingly unable to take her eyes off the underside of miss Chang's... undergarments.{/size}","snape_09",ypos="head") # [Smirk]
    call sna_main("{size=-4}Great idea with the skirt, if I might add.{/size}","snape_13",ypos="head")  # Small text.
    m "{size=-4}You’re welcome.{/size}"  # Small text.
    call sna_main("...","snape_12",ypos="head")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call sna_main("{size=-4}She is wearing something underneath I assume?{/size}","snape_13",ypos="head") # Small text.
    m "For now..."
    call sna_main("Excellent...","snape_22",ypos="head")

    $ renpy.sound.play("sounds/wolf_whistle.mp3")
    $ qp_mob_reaction[0] = "emo8"
    mal "Cho show us your panties!"
    $ renpy.sound.play("sounds/giggle2_loud.mp3")
    $ qp_mob_reaction[1] = "emo7"
    "Female Student #1" "We want to see them!"
    $ qp_mob_reaction[2] = "emo8"
    $ renpy.sound.play("sounds/crowd_cheer.mp3")

    # Back to commentating
    call play_music("quidditch")
    play bg_sounds "sounds/crowd_low.mp3" fadein 0.5 fadeout 0.5
    call her_main("...", "normal", "squint", "angry", "mid", flip=True,xpos="120",ypos="base")
    call her_main("Oh, apparently Ravenclaw scored during that... \"captivating\" bit of distraction...", "open", "narrow", "annoyed", "mid")
    g9 "Sarcasm much?"
    call her_main("", "normal", "closed", "base", "mid")
    call sna_main("...","snape_13",ypos="head") # [Smirk]
    call her_main("I think it’s 10-20!", "open", "happy", "base", "mid")
    call her_main("Or is that 20-10... I’m not sure, aren’t they both home teams...", "annoyed", "squint", "base", "mid")
    call sna_main("Surely you must have learnt how to read by now, Miss Granger?","snape_03",ypos="head")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    $ qp_mob_reaction[2] = None
    call her_main("Hey! I have excellent reading skills, I’ll have you know...", "mad", "narrow", "angry", "R")
    $ renpy.sound.play("sounds/crowd_cheer2.mp3")

    call her_main("...", "normal", "closed", "angry", "mid")
    $ qp_mob_reaction[1] = None
    call her_main("Wait, now it’s... 20-30... I think...", "annoyed", "happy", "base", "mid")
    $ renpy.sound.play("sounds/murmur.mp3")
    $ qp_mob_reaction[0] = "th"
    mal "Has this girl ever commentated even once in her life?"
    $ qp_mob_reaction[1] = "th"
    mal2 "She can’t help herself answering questions in class...."
    mal2 "I suppose the rule book was more for her benefit than ours."
    $ qp_mob_reaction[2] = "emo03"
    call her_main("", "annoyed", "closed", "base", "mid")
    mal "Then how’d she get the role over Lee Jordan?"
    mal2 "I heard he had an accident with a rogue bludger."
    $ renpy.sound.play("sounds/cough_male.mp3")
    mal "..."
    call her_main("Wow... that snitch is darting around like nobody’s business-", "base", "base", "base", "mid")
    $ qp_mob_reaction[0] = None
    hide screen hermione_main


    # Genie and Snape get Drunk
    # Cut to genie and snape
    call sna_main("Fancy a glass of wine then?","snape_02",ypos="head")
    $ qp_mob_reaction[1] = None
    $ qp_mob_reaction[2] = None
    m "Don’t mind if I do... Something to distract me from this... bizarre game..."
    pause.5
    call play_sound("bottle")
    pause.8

    call sna_main("{size=-4}I don’t care much for the game myself...{/size}","snape_09",ypos="head")
    call sna_main("{size=-4}Although, there is a special place in my heart for watching the bludgers catch a student...{/size}","snape_02",ypos="head")
    m "{size=-4}Blubbers?{/size}"
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call sna_main("{size=-4}Bludgers... See those cannonball looking things whizzing around?{/size}","snape_03",ypos="head")
    m "{size=-4}Oh... The ones those boys are whacking at?{/size}"
    call sna_main("{size=-4}Right... Well, we enchant them to go after the students while they play.{/size}","snape_23",ypos="head")
    m "{size=-4}I see... {/size}{w}{nw}"
    g4 "{size=-4}I see... {fast}Wait, Really? Why?{/size}"
    call sna_main("{size=-4}Makes things more interesting doesn’t it!{/size}","snape_02",ypos="head")
    m "{size=-4}So what happens when they hit their target?{/size}"
    call sna_main("{size=-4}Generally it’s just a concussion... Though sometimes they fall pretty far, that’s always entertaining.{/size}","snape_20",ypos="head")

    # hpunch
    with hpunch
    $ renpy.sound.play("sounds/punch02.mp3")
    her "..."
    $ qp_mob_reaction[0] = "sur"
    $ qp_mob_reaction[1] = "emo02"
    $ qp_mob_reaction[2] = "excl"
    $ renpy.sound.play("sounds/crowd_ouch.mp3")
    her "Oh no!"
    call sna_main("{size=+4}HA-HA-HA-HA!!{/size}","snape_28",ypos="head")
    her "Somebody on the Ravenclaw team just got hit by a bludger!"
    g9 "What an amazing turn of events!"
    call sna_main("See, I told you!","snape_22",ypos="head")
    call her_chibi("stand",375,105+186, flip=False)
    $ qp_mob_reaction[2] = None
    call her_main("Professors, could you please keep it down a little?", "normal", "base", "angry", "mid", flip=False,xpos="80",ypos="base")
    call sna_main("Why? It’s not like we’re interrupting anything important.","snape_18",ypos="head")
    $ qp_mob_reaction[1] = None
    call her_main("I’m trying to commentate the game!", "mad", "squint", "angry", "mid")
    $ qp_mob_reaction[0] = None
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call sna_main("Yes, and I was starting to enjoy it. You are missing most of it by the way...","snape_20",ypos="head")
    call her_main("As a result of your yelling!", "scream", "closed", "angry", "mid")
    call her_main("", "normal", "closed", "angry", "mid")
    call sna_main("Eyes forward... girl.","snape_13",ypos="head")
    hide screen hermione_main
    her "*Grrrrr*"
    call her_chibi("stand",375,105+186, flip=True)
    ">Hermione’s eyes briefly meet with yours as if she can’t believe you’re letting Snape talk to her that way."
    call sna_main("{size=-4}As I was saying... They’re the only reason I watch the bloody thing. Now, mind if I top that one off for you?{/size}","snape_20",ypos="head")

    $ qp_mob_reaction[0] = "th"
    $ qp_mob_reaction[2] = "emo8"
    $ renpy.sound.play("sounds/crowd_cheer.mp3", fadein=3)
    call her_main("So, I think... that Hufflepuff just scored another goal? They might even be unstoppable at this point!", "open", "base", "base", "mid", flip=True,xpos="120",ypos="base")
    # Fade to black
    stop bg_sounds fadeout 4
    stop music fadeout 4
    show screen blkfade with d5
    hide screen hermione_main
    $ qp_mob_reaction = [None, None, None]
    ">You and Snape lean back and watch the game, frequently shifting your focus to Cho, as she darts past the stands, only occasionally pausing for more wine or for Snape to ridicule Hermione’s commentating."

    # End of game
    play bg_sounds "sounds/crowd_low.mp3" fadein 2
    $ renpy.sound.play("sounds/referee.mp3")
    pause 1.0
    call hide_blkfade
    her "What was that? Did somebody do a foul?" # intentional 'do'
    "You see Cho flying over to the commentator booth glaring at Hermione with a look of pure hatred."

    # Transition to Cho on her broom.
    $ cho.set_pose("broom")
    $ cho_animation = sprite_fly_idle
    
    call cho_chibi("fly",1200,-100+180)
    call cho_walk(500, 50+180, speed=2)
    pause 1.5
    show screen bld2
    call her_main(face="neutral")
    call cho_main("Hey, Granger!", "open", "narrow", "angry", "L", ypos=-200, xpos=560)
    call her_main("What do you want? Shouldn’t you be busy with,{w=0.3} I don’t know...", "open", "base", "angry", "mid", flip=True,xpos="120",ypos="base")
    call cho_main("", "annoyed", "narrow", "raised", "L")
    call her_main("playing the game?", "smile", "closed", "base", "mid")
    call cho_main("The game is over, you dipstick!", "scream", "narrow", "angry","L")
    call cho_main("", "annoyed", "narrow", "raised", "L")
    call her_main("What? Already?", "shock", "wide", "worried", "stare")
    call cho_main("", "upset", "narrow", "angry","L")
    call her_main("But who caught the Snitch?", "open", "wide", "base", "stare")
    call cho_main("", "open", "narrow", "angry","L")
    $ cho.set_body(armright="snitch")
    with d3
    ">Cho waves the snitch in front of her."
    call her_main("", "mad", "wide", "worried", "shocked")
    $ cho.set_body(armright="down")
    call cho_main("My first ever win this season and you didn’t even notice it! No one did, thanks to your dreadful commentating!", "scream", "closed", "angry", "L")
    call cho_main("", "upset", "narrow", "angry","down")
    call her_main("Oh...", "normal", "wide", "worried", "shocked")
    call her_main("So should I announce it now?", "open", "happyCl", "worried", "mid")
    call sna_main("Obviousl-","snape_12",ypos="head")
    call cho_main("{size=+10}YES!{/size}", "scream", "narrow", "angry", "L", trans=vpunch)
    call her_main("", "normal", "base", "worried", "mid")
    call cho_main("{size=+6}WHAT ARE YOU EVEN WAITING FOR?{/size}", "scream", "narrow", "raised", "L", trans=hpunch)
    call cho_main("", "upset", "narrow", "angry","down")
    call her_main("Don’t scream at me like that, bitch!", "scream", "base", "angry", "mid", trans=hpunch)
    call cho_main("", "angry", "wide", "angry", "L")
    call her_main("", "normal", "base", "angry", "mid")
    call cho_main("{size=+6}WHAT DID YOU JUST CALL ME?!!!{/size}", "scream", "wide", "angry", "L", trans=vpunch)
    call cho_main("", "angry", "wide", "angry", "L")
    call her_main("Everyone, Ravenclaw wins!", "grin", "happy", "base", "mid_soft")
    call her_main("Cho Chang managed to catch it, the snitch that is...", "smile", "happyCl", "base", "mid")
    call cho_main("", "scream", "wide", "raised", "L")
    call her_main("With the help of her ridiculously short skirt!", "crooked_smile", "base", "angry", "mid")
    cho "{size=+10}!!!{/size}"
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo7"
    play bg_sounds "sounds/crowd.mp3" fadein 1 fadeout 1
    $ renpy.sound.play("sounds/crowd_applause.mp3")
    hide screen hermione_main
    hide screen bld2
    with d3
    call cho_main("", "quiver", "wide", "worried", "downR")
    ">Hermione’s commentating is drowned out by the sound of the Ravenclaw grandstand cheering."
    call cho_main("{size=+6}You are done, Granger!{/size}", "scream", "closed", "angry", "L")
    call cho_walk(1200, 500+180, speed=2)
    pause 5
    $ cho_animation = None
    $ cho.set_pose(None)
    call cho_chibi("reset")

    # Outro
    m "This isn’t such a bad game after all."
    call sna_main("I *hick* told you... so...","snape_22",ypos="head")
    m "Just bring more wine next time!"
    call sna_main("M-More?!","snape_20",ypos="head")
    m "Or at least share more of it with me!"
    $ renpy.sound.play("sounds/glass_shatter.mp3")
    call sna_main("Get your own, magic man!","snape_21",ypos="head")
    m "..."
    show screen blkfade with d5
    stop bg_sounds fadeout 4
    ">Snape wanders off in a drunken stupor..."
    pause.5
    call play_sound("grass")
    "> You hurry back to your office before giving anyone a chance to talk to you."
    call room("main_room")
    call gen_chibi("hide")
    show screen chair_left
    show screen desk
    call hide_blkfade
    pause 1.0

    call play_sound("door")
    call gen_chibi("stand","door","base",flip=False)
    with d3
    pause 0.3

    call bld
    m "I'm hom-...{w=0.8}{nw}"
    g4 "Dammit, I almost said that!"
    m "Anyway, I'm beat, time to hit the hay."

    call gen_walk("desk", "base")

    call blkfade

    # Skip to evening.
    jump night_start

# Return Response
label hufflepuff_match_return:
    # Cho returns after winning the Quidditch match.
    # She's outraged about Hermione.
    # Demands that you will find somebody to replace her.
    pause.8
    #$ renpy.sound.play("sounds/steps_grass.mp3")
    $ renpy.sound.play("sounds/snore1.mp3")
    m "*Snore*{w=2.0}{nw}"
    pause 1.0
    $ renpy.sound.play("sounds/snore3.mp3")
    m "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
    pause 1.0
    $ renpy.sound.play("sounds/snore2.mp3")
    m "......{w=0.5}*Snore*{w=1.0}{nw}"
    stop music fadeout 6.0
    call cho_walk("desk", "base", action="enter")

    $ renpy.sound.play("sounds/punch01.mp3")
    call cho_main("We beat Hufflepuff!!!","smile","angry","base","mid", ypos="base", trans=hpunch)
    $ renpy.sound.play("sounds/MaleGasp.mp3")
    g4 "{size=+10}IT WASN'T ME!{/size}"
    m "..........."
    call cho_main("huh?{w=0.5} Are you okay, [cho_genie_name]?","angry","narrow","base","mid")
    m "Wha-{w=0.5}{nw}"
    g4 "Of course I am!"
    call cho_main("...","annoyed","angry","raised","R")
    call cho_main("If you say so.....","annoyed","angry","base","mid")
    call play_music("cho")
    call cho_main("I can't believe that we've broken our 6 year dry streak and won a real game!","smile","base","base","mid")
    call cho_main("We could actually win the cup!","open","shocked","angry","L")
    m "And you weren't embarrassed?"
    call cho_main("I was a little at the start of the game...","quiver","narrow","sad","downR")
    call cho_main("But once I realised how much it was affecting those slack-jawed Hufflepuffs...","smile","angry","angry","R")
    call cho_main("It was like having my own personal weapon of mass distraction!","smile","shocked","angry","mid")
    call cho_main("I don't think Cedric even knew where the snitch was most of the time!","horny","base","base","downR")
    call cho_main("All he seemed to do was follow me around...","horny","narrow","sad","down")
    call cho_main("Him {size=-2}and {size=-2}half {size=-2}the {size=-2}team...{/size}","quiver","narrow","sad","downR")
    call cho_main("This might be the first real chance Ravenclaw has ever had to win the cup.","open","closed","sad","mid")
    m "I'm sure this must mean a lot to you..."
    call cho_main("It does... I might even get picked up by a pro team!","smile","base","base","R")
    m "..."
    call cho_main("*Argh* I can't wait!","scream","closed","base","mid")
    call cho_main("I better go celebrate with the team now!","open","base","base","mid")
    m "Well, off you go then."
    call cho_main("Thank you Professor...","smile","wink","base","mid")
    #
    # TODO: Add panty flash in form of a reward/tease
    #
    # cho "But before I go...." # blushes
    # (flashes panties)
    # g4 "!!!"
    # (equips skirt again)
    # cho "I gotta go."
    # starts walking out of the office
    # m "Hey but I ha-..."
    # (cho leaves)
    # m "Oh well.. At least I caught a glimpse of the goodies."

    # Cho leaves.
    call cho_walk(action="leave")

    stop music fadeout 1.0
    call popup("New favours for Cho have been unlocked!", "Congratulations!", "interface/icons/head/head_cho_2.png")
    call unlock_clothing(text=">New clothing items for Cho have been unlocked!", item=cho_outfit_cheerleader)

    #if cho_whoring < 24:
    #    $ cho_whoring = 24
    #    $ TBA_message("This concludes all Quidditch events for Cho as of version %s." % title_version)
    #    $ TBA_message("Cho's recklesness stat has been maxed out.\nYou can now use all of her wardrobe options.")

    $ cho_busy      = True
    $ hermione_busy = True
    $ snape_busy    = True

    # Reset Cho
    $ cho.equip(cho_outfit_last)

    $ cho_tier = 2
    $ cho_training_unlocked = True
    $ cho_quid.lock_practice = False
    $ cho_quid.lock_training = False
    $ cho_quid.lock_tactic   = False

    jump end_cho_event
