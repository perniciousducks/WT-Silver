screen bludger_flying(start, end, t=1.0):
    zorder 4
    tag bludger
    
    add "images/rooms/quidditch_pitch/bludger.png":
        at transform:
            subpixel True
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            pos start
            ease t xpos end[0] ypos end[1]
        

### Main Match ###

# Chat with Cho the day before.
label start_slytherin_match:
    call cho_main(xpos="mid", ypos="base", trans="fade")
    g9 "Alright, [cho_name]. Let's do this!"
    g4 "Tomorrow we shall wipe the floor with those Slytherins, and bathe in their salty tears!"
    g9 "(Snape's tears in particular, after I get a hold of all of his gold!)"
    call cho_main("I'll do my best, Sir.", "soft", "base", "angry", "mid")
    m "Are you ready?"
    call cho_main("I am!", "base", "base", "angry", "mid")
    m "Then show me the money."
    call cho_main("What?", "upset", "base", "raised", "mid")
    g9 "Say it with me,[cho_name]!{w} Show me the money!"
    call cho_main("I don't have any on me, Sir.", "angry", "narrow", "sad", "mid")
    m "..."
    call cho_main("Show me the money?", "open", "narrow", "raised", "mid")
    g9 "Yes! Say it like you mean it, brother!"
    call cho_main("What?", "angry", "wide", "base", "mid")
    with hpunch
    g4 "{size=+5}Show me the money!{/size}" # loud
    call cho_main("(He knows I'm a girl...why would he say that?)", "annoyed", "narrow", "angry", "mid")
    with hpunch
    call cho_main("Sir, Are you all right?", "soft", "narrow", "sad", "mid")
    g9 "What you gonna do, [cho_name]?"
    call cho_main("Get the nurse?", "upset", "narrow", "angry", "mid")
    m "You're gonna win that match tomorrow, that's what!"
    call cho_main("If we're going to play tomorrow, I'll first have to prepare my gear and charm my Quidditch googles...", "soft", "base", "base", "R")
    call cho_main("Or they'll just fog-up and not dispel the rain properly...", "soft", "narrow", "base", "mid")
    m "Hold up!{w=0.3} It's going to rain tomorrow?"
    call cho_main("Most likely...", "annoyed", "base", "sad", "mid")
    g4 "(This might be just what we need!)"
    call cho_main("Professor Trelawney told us to wear our robes tomorrow.", "soft", "base", "base", "R")
    call cho_main("According to her, there are some heavy rain-clouds approaching...", "open", "narrow", "raised", "mid")
    call cho_main("But that's just Trelawney... She can be a bit inconsistent with her weather forecasts...", "soft", "base", "sad", "down")
    call cho_main("Well, she's quite inconsistent with everything, if we're honest...", "annoyed", "narrow", "base", "R")
    g9 "Let's hope she's right this time!"
    call cho_main("But, Sir! Wouldn't this put us at a huge disadvantage?", "open", "narrow", "sad", "mid")
    m "Nonsense..."
    call cho_main("[cho_genie_name], I'm gonna get soaked without my coat on!", "soft", "base", "sad", "mid")
    g9 "Counting on it!"
    g9 "I - for one - am quite looking forward to the possibility of you getting wet."
    call cho_main("Let's just hope for the best...", "upset", "narrow", "sad", "down")
    g9 "That we shall."
    g9 "Off you go then. And good luck."
    call cho_main("(...)", "annoyed", "narrow", "angry", "R")
    call cho_main("See you tomorrow, [cho_genie_name].", "soft", "narrow", "sad", "mid")

    call cho_walk(action="leave", speed=2.2)

    $ cho_busy = True
    $ cc_event_pause  += 1  # Event starts on the next day.
    $ cc_summon_pause += 1  # Can't be summoned until next event.

    $ cho_quid.lock_training = True
    $ cho_quid.lock_practice = True

    $ slytherin_match = "start"

    jump main_room



#Office before game
label slytherin_match:

    ### Event Setup ###
    $ cho_outfit_last.save()
    $ hermione_outfit_last.save()
    $ tonks_outfit_last.save()

    $ cho_class.equip(cho_outfit_quidditch)
    $ hermione_class.equip(hermione_outfit_default)
    $ tonks_class.equip(tonks_outfit_default)


    # Scene before Match against Slytherin
    call play_music("stop")

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"

    menu:
        m "(...)"
        "\"Who is it?\"":
            call bld
            ton "Tonks, Sir."
            m "First and last name, please."
            with hpunch
            ton "What?!"
            g9 "Tell me your first and last name, and you may enter."
            ton "Are you fucking with me right now?"
            m "No. Unless that's on the table..."
            g9 "Or desk."
            ton "Bloody hell..."
            m "Full name please."
            ton "Nymphadora Tonks...{w=0.3} Can I come in now?"
            g9 "Of course..."
        "\"Come in...\"":
            pass

    #Tonks enters
    call ton_walk(action="enter", xpos="desk", ypos="base", speed=2.5)

    call play_music("tonks")
    call ton_main("Hi, [ton_genie_name].","base","base","base","mid", xpos="mid", ypos="base")
    m "Tonks... a pleasure as always."
    call ton_main("Pleasure's all mine...","horny","base","raised","mid")
    call ton_main("I was afraid you might've forgotten about today's-","open","base","base","mid")
    g9 "Quidditch match?"
    call ton_main("So you didn't forget!","open","base","raised","mid")
    g9 "How could I? Last match was a great show!"
    call ton_main("It sure was...","base","base","angry","mid")
    call ton_main("So, is Hermione going to show up as well?","horny","base","angry","mid")
    m "Who knows with her, honestly..."
    call ton_main("May I be allowed to accompany you anyway?","upset","base","worried","mid") #sad
    call ton_main("I've been looking forward to watching the game from the commentator booth...","open","base","sad","R")
    g9 "Of course! I'd be delighted to have you!"
    call ton_main("Thank you, [ton_genie_name].{image=textheart}","base","happyCl","base","mid", hair="happy")
    call ton_main("Are we to expect another great performance this time around?","horny","base","base","mid", hair="neutral")
    g9 "Oh, you'll see..."
    call ton_main("Great, shall we?","base","base","angry","mid")
    g9 "We certainly shall!"

    call play_music("stop")
    call hide_characters
    hide screen bld1
    with d3

    # Teleport
    call play_sound("kick")
    show screen chair_left
    show screen desk
    call gen_chibi("hide")
    with d3

    call gen_chibi("stand","door","base", flip=False)
    call teleport(position="genie", effect=False)
    pause .2

    call ton_chibi("stand","desk","base", flip=True)
    with d3
    pause .2

    call gen_chibi("stand","door","base", flip=True)
    with d3
    pause .3

    call ton_main("*huh?*... (When did he?)","upset","base","worried","L", ypos="head")
    call ton_main("(Impressive. I wonder if his stamina can keep up with that speed...)","horny","base","raised","R")
    g9 "Ladies first."
    call ton_main("What a gentleman.","base","happyCl","base","mid")

    call ton_walk(xpos="680", ypos="base", speed=2.2)

    call play_sound("door")
    call ton_chibi("hide")
    with d3
    pause .2

    call gen_chibi("stand","door","base", flip=False)
    with d3
    pause .5

    call play_sound("door")
    call gen_chibi("hide")
    with d3
    pause .8

    # Black screen
    call play_music("stop")
    show screen blkfade
    with d5
    pause .5


    ### Lower Quidditch Pitch Area ###


    call play_sound("grass")
    nar "You make your way across the castle grounds accompanied by Tonks."
    nar "You find Snape waiting for you at the entrance of the Quidditch pitch towers."

    play bg_sounds "sounds/crowd.mp3" fadein 2

    call sna_main("Gen-","snape_03", ypos="head")
    call sna_main("*Ahem*... Albus, Glad you made it in time.","snape_09")
    call ton_main("I know who he is, Snape. There's no need for the pretence.","open","closed","base","L", ypos="head", flip=True)
    call sna_main("Of course there is. We're outside the headmaster's office, after all.","snape_16")
    call sna_main("We have to keep up the act in front of the students...","snape_01")
    call ton_main("*Hmm*... Good point...","base","base","base","R")
    m "I'm standing right here."
    call sna_main("I would've gone and fetched him myself but...","snape_03")
    call sna_main("I had some... business to attend to.","snape_35")
    call ton_main("Business, huh?","horny","base","angry","L")

    call sna_main("You will be accompanying us I presume?","snape_04")
    call ton_main("If that's okay with you?","base","happyCl","base","mid")
    m "(Why aren't they paying attention to me?)"
    call sna_main("I suppose...","snape_05")
    call ton_main("Great!","smile","base","angry","L")

    call ton_main("So, are we going?","base","base","angry","L")
    call sna_main("Ah *ahem*, yes... I suppose.","snape_12") #throat clear in the middle of the sentence for extra awkardness
    m "I may be immortal but I'm afraid I'll die from this awkwardness..."
    m "I'd take a hundred years in the lamp over this."
    $ renpy.sound.play("sounds/giggle2_loud.mp3")
    call ton_main("*Giggles*","base","happyCl","base","mid")
    call sna_main("...","snape_14")
    call sna_main("After me then...","snape_12")

    stop bg_sounds fadeout 4

    #nar "You continue making your way down to the Quidditch pitch, the silence only broken by Tonks giggling to herself every so often..."
    nar "The three of you climb up the Quidditch tower."


    ### Main Match Starts ###

    #Scene Cloudy/rainy pitch
    #Sounds slightly windy/rain (Might need a new sound we'll see... It shouldn't overpower things)
    
    $ qp_mob = 0 # Controls number of people
    $ qp_mob_reaction = [None, None, None] # Reset reactions
    #call sna_chibi("stand", "210", -40, flip=True)
    #call gen_chibi("stand", "130", "10")
    #call her_chibi("stand", "375", "105", flip=True)
    $ snape_chibi.zorder = 1
    $ hermione_chibi.zorder = 2
    $ tonks_chibi.zorder = 3
    $ genie_chibi.zorder = 4

    call room("quidditch_pitch")
    with d3
    play bg_sounds "sounds/crowd.mp3" fadein 2    
    pause 1

    #Quidditch pitch fills up a little
    $ qp_mob = 1
    with d3
    pause 1

    call play_sound("footsteps")
    pause .8
    call sna_chibi("stand", 210, -40, flip=True)
    with d3
    pause .5

    call ton_chibi("stand", 200, 50, flip=True)
    with d3
    pause .3
    call ton_chibi("stand", 200, 50, flip=False)
    with d3
    pause .1

    #Snape enters and stands at the back
    call ton_main("Mind your head!","base","base","worried","down", ypos="head", flip=False)

    call play_sound("kick")
    with hpunch
    pause .6
    g4 "Bloody bleachers!" #noone uses blooming in a serious context, unless they're some kind of yorkshire caricature
    call sna_main("...","snape_45", ypos="head") #Smirks
    pause .2

    call play_sound("footsteps")
    pause .8
    call gen_chibi("stand", 130, 10)
    with d3
    pause .2
    call ton_chibi("stand", 200, 50, flip=True)
    with d3
    pause .3

    call ton_walk(xpos= 220, ypos= 130, speed=1)
    pause .2

    call ton_main("Oh, what a view! Much better than the one from the Hufflepuff stands!","base","happyCl","base","mid", flip=True, ypos="head")

    #Hermione enters from the left and walks up to the podium

    call her_chibi("stand", 220, 50, flip=True)
    with d3
    pause .3
    call her_walk(xpos=375, ypos=105, speed=2)
    pause .5

    #Hermione turns around
    call her_chibi(flip=False)
    with d3
    pause .1

    call her_main("Oh- hello, Professor Tonks!","soft","base","base","L", flip=False, ypos="head")
    call ton_main("Miss Granger, so glad you made it!","base","base","base","L", flip=True, ypos="head")
    call her_main("Of course, as you know I take my responsibilities seriously!","open","base","angry","L")

    #Quidditch pitch fills up a little
    $ qp_mob = 2
    with d3

    #Crowdsound goes up
    call sna_main("{size=-4}Unfortunately...{/size}","snape_31") #small text
    call ton_main("I'm here if you need me!","base","happyCl","base","mid")
    call her_main("I appreciate the thought, Professor... but I'll be fine.","open","closed","base","mid")
    call her_main("I'd be made fun of even more if you had to take over...","open","narrow","angry","L")
    call ton_main("Whatever you want, sweetie.","horny","base","base","L") #smile
    call her_main("...","mad","base","worried","down", cheeks="blush") #smiles and blushes

    # Tonks goes back up, now stands between Snape and Genie.
    pause.2
    call ton_chibi("stand", 200, 50, flip=True)
    with d5
    pause.3

    #Quidditch pitch full
    $ qp_mob = 3
    with d3
    call sna_main("The crowd is waiting, Miss Granger...","snape_31")
    call her_main("Sorry!","clench","base","worried","down", emote="05")

    #Hermione turns
    call her_chibi(flip=True)
    with d3
    pause .5

    call her_main("","base","base","worried","mid", flip=True, xpos="120", ypos="base")
    pause .8

    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    play bg_sounds "sounds/crowd_low.mp3" fadein 3
    call her_main("*Ahem*","soft","narrow","worried","mid")
    #Crowdsounds go down
    call her_main("Welcome back to the second match of the season!","base","happyCl","base","mid")
    sly1 "{size=+5}Not the Gryffindor slut again!{/size}"
    with hpunch
    $ qp_mob_reaction[2] = "emo8"
    sly2 "{size=+8}Get off the podium, Mudblood!{/size}"
    sly1 "{size=+15}Boooo!{/size}"
    call her_main("*Hmph!*","annoyed","narrow","angry","mid")

    #Hermione Turns to Tonks, Genie and Snape
    call hide_characters
    with d3
    pause .2
    call her_chibi(flip=False)
    with d3
    pause .3

    call her_main("Sir, I'm trying to do my job here - and those Slytherin boys just can't keep their filthy mouths shut!","soft","narrow","angry","mid", flip=False, ypos="head")
    call sna_main("Surely you've been called worse Miss Granger...","snape_05")
    $ qp_mob_reaction = [None, None, None]
    call ton_main("Just ignore them sweetie, you're doing great.","base","happyCl","base","mid")
    call her_main("...","annoyed","narrow","angry","down") #annoyed
    call her_main("Fine...","soft","base","base","R") #Open mouth glances to the right


    #Hermione turns to the crowd again
    pause .2
    call her_chibi(flip=True)
    with d3
    pause .5

    call her_main("I know the weather might not be optimal, but the games must go on.","soft","closed","base","mid", flip=True, xpos="120", ypos="base")
    call her_main("Therefore, let me now welcome onto the pitch...","open","base","base","down")
    call her_main("The team known for their technical prowess and... lately... unconventional tactics...","disgust","base","worried","down")
    call her_main("Team Ravenclaw!","open","base","base","mid")

    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo8"
    $ renpy.sound.play("sounds/crowd_cheer.mp3")
    ">A loud cheer roars from the grandstands."
    $ qp_mob_reaction = [None, None, None]

    #Crowd Sounds
    call her_main("And their opponents...","soft","closed","base","mid")
    call her_main("The team known for their...","open","narrow","angry","down")
    call her_main("Their...","open","narrow","angry","L")
    $ qp_mob_reaction[2] = "emo8"
    sly1 "{size=+5}Got a cock down your throat?{w=0.8} Get on with it!{/size}"
    sly2 "{size=+8}Yeah!{w=0.5} Get on with it!{/size}"
    call her_main("...","annoyed","closed","angry","mid")
    with hpunch
    qcr "{size=+15}Get on with it!{/size}" # loud
    $ qp_mob_reaction[2] = None
    call her_main("The team known for their thick skin... or should I say, thick skulls...","angry","base","angry","mid", emote="01")
    call her_main("Team Slytherin!","annoyed","narrow","angry","mid")

    $ renpy.sound.play("sounds/crowd_stomping.mp3")
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    call her_main("", "base", "base", "base", "mid")
    ">The green grandstand shakes violently with enthusiasm."
    $ qp_mob_reaction[0] = None
    $ qp_mob_reaction[1] = None

    g9 "..."
    call sna_main("...","snape_38")
    call her_main("And now, if both teams have managed to find their way to their starting positions...","open","closed","base","mid")
    call her_main("Madam Hooch, if you please!","soft","base","base","L")
    
    hide screen hermione_main
    with d3
    
    pause.5

    $ renpy.sound.play("sounds/referee.mp3")
    call play_music("quidditch")
    call nar("The grey haired lady glances up to the podium and gives Hermione a wink - as she throws the quaffle into the air.")


    call her_main("And we're off!","base","happyCl","base","mid")
    call nar("Looking up you can see Cho giving Malfoy a quick smirk as she darts off towards the Slytherin half of the pitch.")
    call her_main("Ravenclaw chaser and team captain Roger Davies immediately goes for the quaffle...","open","base","angry","L")
    call her_main("The Slytherin captain Graham Montague not far behind.","open","base","angry","up")
    call her_main("Oh! Davies catches it and passes to Bradley...","smile","base","angry","up")
    call ton_main("She's pretty cute when she's excited, isn't she.","base","happyCl","base","mid")
    m "..."
    call ton_main("I feel like we've got the best seats in the house, right behind the podium...","horny","base","base","L", hair="horny")
    call ton_main("Who cares about the match if you got a view like that...","horny","base","angry","L")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    m "You might enjoy it a bit more if you took a look towards the Slytherin side of the pitch..."
    call ton_main("Oh... I see, miss Chang has decided to forego the coat today...","open","base","raised","up")
    call ton_main("And those trousers seem to sit pretty tight on her...","horny","base","base","up")
    m "I did my research..."
    g9 "I know for a fact that those Slytherin boys are men of class -{w=0.2} they enjoy such things as much as you."
    call ton_main("I bet they do...","open","base","raised","R")
    call sna_main("Feels a bit like cheating, considering our bet...","snape_09")
    if gold >= 2000:
        g4 "Fuck{w=0.3}, I forgot he was here..."
    else:
        g4 "Oh shit{w=0.3}, the bet..."
    call sna_main("And I can still hear you...","snape_03")
    call sna_main("I had imagined that you wouldn't use such tactics during the game against Slytherin...","snape_04")
    m "(There goes that fucking bet...)"

    call her_main("The Slytherin beaters, Crabbe and Goyle, are now focusing their efforts on beating the bludgers as hard as they can towards the enemy chasers!","open","base","angry","R")

    m "Well, if you remembered the bet correctly, you'd know that we said nothing about any tampering on my part."
    g9 "It was only you who made such an agreement..."
    call ton_main("Oooh, that's so naughty...","upset","base","worried","mid", hair="neutral")
    call sna_main("Quite...","snape_04")
    call ton_main("Surely a bet like this should be made on equal terms... where's the sportsmanship?","open","base","raised","mid")

    menu:
        g4 "(Damnit! Two against one... That's not fair!)"
        "-Agree, and call the bet off...-":  # No option actually calls it off
            call ton_main("That's the spirit, now let's just enjoy the... *uhm*...","horny","base","raised","L", hair="horny")
            call ton_main("The match, is what I wanted to say...","upset","base","worried","L")
            call sna_main("No no, it's fine. I've got some cards up my sleeves.","snape_09") #I think a repeated 'no' here works well, sort of a posh English way of being dismissive. But you can just use one it makes no real difference
            #Keep the bet going, Snape should've listened properly
            call sna_main("A bet is a bet, after all...","snape_02")
            call sna_main("I'm confident in my abilit-... my team's abilities though.","snape_24")
            call ton_main("...","horny","base","base","L") # Distracted
            call ton_main("I'm sorry. Did you guys say something?","open","base","raised","L")

        "-Forfeit, and give Snape the money...-":
            if gold >= 2000:
                m "Fuck no, you think I'm some kind of charity?"
            else:
                m "With what money?"   
            call sna_main("What?","snape_03")
            #Back to other two options

    $ renpy.sound.play("sounds/ball_hit.mp3")
    call her_main("Crabbe just whacked the bludger straight towards Davis' broom-","open","base","angry","up")
    call her_main("Scratch that, he hit the quaffle out of his hand!","clench","base","worried","up")
    call her_main("That's crazy lucky!","open","base","angry","up")
    call her_main("Where's the quaffle?{w} Oh, Pucey's got it!","soft","base","base","L")
    call her_main("And he's already flown past the beaters!","smile","base","angry","L")
    g4 "..."
    call her_main("But can he get through the keeper!","soft","base","base","up")

    #Screen shake audience groans
    with hpunch
    $ qp_mob_reaction[0] = "sur"
    $ qp_mob_reaction[1] = "emo02"
    $ qp_mob_reaction[2] = "excl"
    $ renpy.sound.play("sounds/crowd_ouch.mp3")
    call her_main("Another bludger hit by Crabbe - going straight into the stomach of the Ravenclaw keeper!","clench","base","worried","up")
    $ qp_mob_reaction[2] = None
    $ qp_mob_reaction[1] = None
    $ qp_mob_reaction[0] = None
    call her_main("Pucey passes the quaffle to Warrington, who scores another goal for team Slytherin!","annoyed","base","angry","up")
    hide screen hermione_main
    with d3
    
    call sna_main("...","snape_45") #Smirks
    m "That's insane, how the hell did he hit that?"
    g4 "He was on the other side of the pitch!"
    call sna_main("That's my boys!","snape_37")
    call sna_main("Thick as oatmeal, but built like a brick shithouse.","snape_28")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call ton_main("They're so strong... I've never seen a bludger hit its target from that far before...","horny","base","base","up", hair="horny") #horny
    call ton_main("Is it me or is it getting a bit hot in here?","upset","base","worried","ahegao")
    call sna_main("Something to cool you down perhaps?","snape_02")
    call ton_main("Good idea, Did you bring any of that firewhisky?","base","base","angry","mid")
    m "Err..."
    call sna_main("Firewhisky? For such a special day as today I've brought some of my finest wine.","snape_20")
    call sna_main("Now, if I may, Miss Tonks?","snape_13")
    call ton_main("*Hmm*... I tend not to drink wine too often...","upset","base","raised","down")
    call ton_main("Oh what the heck, go on then. I'll have a glass.","base","base","angry","down")

    call nar("You sit down with Snape and Tonks to enjoy the match - drinking some of the finest wine you've tasted.","start")
    call nar("Tonks' cheeks turning redder as the game continues.","end")

    m "Doesn't look great..."
    call ton_main("What do you mean? Only thing that would make this better would be those firm cheeks on my lap!","horny","base","angry","L", hair="horny")
    call sna_main("He's talking about the game...","snape_09")
    call ton_main("Game? What game...","open","base","raised","L")
    call ton_main("Oh, Quidditch! Of course!","upset","base","worried","ahegao")

    call her_main("And we're now 60-0 to Slytherin as their onslaught continues, the seekers not yet having spotted the snitch.","open","base","angry","L")
    call her_main("If it wasn't for those foul tactics - from the brutes on the Slytherin team...","angry","base","angry","L")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call her_main("Ravenclaw would have no issues beating the ever living sh-{w=1.2}{nw}","angry","narrow","angry","L")

    #Hermione gets hit in the face by a bludger
    call hide_characters
    with d3
    pause .2

    # Ball hitting the chibi's face.
    # DEVVV
    
    
    show screen bludger_flying((530, -100), (-50, 1000))
    pause .18
    $ renpy.play(["sounds/card_punch4.mp3", "sounds/microphone_feedback.mp3"])
    show screen gfx_effect(435, 118, img="glow_effect", zoom=0.7, duration=0.3)
    show screen hermione_hit_on_head
    with vpunch
    hide screen gfx_effect
    show screen gfx_effect(355, 320, img="smoke", zoom=0.5)
    call play_sound("kick")
    $ qp_hole = True
    with None

    #Audience groans
    stop bg_sounds fadeout 2
    stop music fadeout 2
    pause 0.5
    $ renpy.sound.play("sounds/crowd_gasp.mp3")
    call ton_chibi("slack_jaw", 200, 50, flip=True)
    call gen_chibi("stand_shocked", 130, 10, flip=False)
    call sna_chibi("stand_shocked", 210, -40, flip=True)
    pause 1.0
    $ renpy.sound.play("sounds/dizzy.mp3", loop=True)
    pause 2.0
    call sna_main("*Pfffffffffff*-","snape_14") # Snape has wine gushing out of his nose (image edit)
    call sna_main("*Ha-ha-HA-HA!*","snape_42")
    $ renpy.sound.stop(fadeout=1.0)

    call play_music("fun")
    stop weather fadeout 0.5
    show screen blkfade
    with d1

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    call play_music("stop")
    pause.5

    call hide_characters
    $ snape_chibi.zorder = 1
    $ hermione_chibi.zorder = 3
    $ tonks_chibi.zorder = 2
    $ genie_chibi.zorder = 4

    call her_chibi("lying", 330, 160)
    call ton_chibi("stand", xpos=395, ypos=110, flip=False)
    call sna_chibi("stand", xpos=260, ypos=0, flip=True)
    call gen_chibi("stand", xpos=210, ypos=40, flip=False) # TODO: mirror Genie's flip so it's the same as any other character.
    with d3

    call weather_sound
    call play_music("quidditch")
    hide screen blkfade
    with d3
    pause .8

    call sna_main("I'm surprised she didn't swallow that one - with how wide she was blabbing her mouth.","snape_42", ypos="head")
    call sna_main("That's liquid luck for you!","snape_45")
    call ton_main("What?","angry","shocked","base","wide", hair="neutral", ypos="head", flip=True, trans="hpunch") #Shocked
    g4 "What the fuck is liquid luck?"
    call ton_main("You gave those brutes a luck potion?!","scream","base","angry","L", hair="angry")
    call sna_main("Well...{w=0.8}{nw}","snape_14")
    call ton_main("I can't believe you, Snape...{w=0.5} look what they've done to her face!","angry","base","worried","down", hair="sad")
    call ton_main("Her beautiful face...","upset","base","sad","down") #Sad
    call sna_main("Looks like an improvement to me.","snape_46")
    call ton_main("Quiet!","angry","base","angry","L", hair="angry")
    m "..."
    call ton_main("I'm taking her to the hospital wing...","open","base","angry","down", hair="neutral")
    m "What about the game..."
    call ton_main("Leave it to me...","open","base","angry","mid")
    g4 "What?"

    call hide_characters
    call ton_chibi(flip=True)
    with d3
    pause .2

    call ton_walk(xpos=430, ypos=70, speed=0.5)


    pause .5

    $ renpy.sound.play("sounds/referee.mp3")
    call nar("Tonks Signals Hooch and a whistle is heard to signify a short break... a murmur erupts across the crowd, some not realizing what has gone down.")

    call ton_chibi(flip=False)
    with d3

    call ton_walk(xpos=395, ypos=110, speed=1)
    pause .5

    call play_sound("footsteps")
    show screen blkfade
    with d5
    pause .8

    hide screen hermione_lying
    call ton_chibi("hide")
    call her_chibi("hide")
    call gen_chibi("stand", xpos=255, ypos=0, flip=True)
    call sna_chibi("stand", xpos=170, ypos=-20, flip=False)
    with d3

    hide screen blkfade
    with d5
    pause .3

    m "She sure sobered up quickly..."

    #Genie and Snape sprite should probably both be turned left and swapped in this section.
    with hpunch
    $ renpy.sound.play("sounds/falling_stairs.mp3")
    pause 1
    ton "Bloody stairs!"
    m "Nevermind..."
    call sna_main("This isn't good.","snape_03")
    g4 "You tell me, her face is fucked, and not in the fun way."
    #Snape should turn forward here
    call sna_main("I'm talking about the crowd... Granger will be out of it for now - but should be fine by the end of the day.","snape_09")
    call sna_main("Unfortunately...","snape_35")
    m "(...)"
    pause .5

    #Black screen
    show screen blkfade
    with d5
    pause .2

    "A couple of minutes go by - and there's no sign of Tonks..."
    $ renpy.sound.play("sounds/murmur.mp3")
    $ qp_mob_reaction[1] = "emoq"
    "The crowd now whispering even more, some beginning to spot the empty podium."

    #Fades back, crowd noises louder
    $ qp_mob_reaction[1] = None

    pause .2
    hide screen blkfade
    with d5
    pause .5

    call sna_chibi(flip=True)
    with d3
    pause .2

    call sna_main("You'd better get up there and do something.","snape_03")
    m "What do you want me to do? You already made me do a speech last time..."
    g4 "I'm out of material."
    m "Also, doesn't this feel a bit like rehashing content?"

    #Snape starts walking slowly to the podium
    call sna_main("Fine, in that case. I'll just go up and give a motivational-","snape_01")

    #Genie walks past him and snape stops
    call gen_chibi(flip=False)
    with d3
    pause .5
    m "No..."
    pause .3

    call gen_walk(xpos=360, ypos=45, speed=2)
    pause .8

    $ genie_zorder = 5
    show screen blktone5
    call gen_main(face="base", xpos="100", ypos="120")
    call ctc

    call gen_main("I've got this...")
    #idk this feels more 'hollywood' and 'dramatic' than "i got it" which I think is good considering the speeches coming up

    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    hide screen blktone5
    with d3
    pause .2
    call gen_main("Ladies and gentlemen...", face="open")

    call gen_main("An intermission if you will...{w} for some motivation...{w} for both teams... ", face="base")
    stop music fadeout 2

    #cho "..." # Doesn't really make sense for Cho to appear at this point, especially since she doesn't say anything

    menu:
        "(Let's give them what they came for...)"
        "\"Independence!\"": #Independence day
            play bg_sounds "music/fanfare.mp3" fadein 1.0
            call gen_main("Good morning...", face="base")
            $ qp_mob_reaction[0] = "emoq"
            call gen_main("In less than an hour, aircrafts from here will join others from around the world. And you will be launching the largest aerial battle in this history of mankind.", face="open")
            call gen_main("", face="base")
            call sna_main("Not again...","snape_17")
            call gen_main("Mankind...{w=0.3} that word should have new meaning for all of us today.", face="open")
            $ qp_mob_reaction[1] = "qu"
            call gen_main("We can't be consumed by our petty differences anymore.", face="base")
            call gen_main("We will be united in our common interests.", face="open")
            call gen_main("Perhaps its fate that today is the 4th of July, and you will once again be fighting for our freedom, not from tyranny, oppression, or persecution -- but from annihilation.", face="open")
            call gen_main("We're fighting for our right to live, to exist.", face="angry")
            call gen_main("And should we win the day, the 4th of July will no longer be known as an American holiday, but as the day when the world declared in one voice.", face="open")
            call gen_main("We will not go quietly into the night!", face="base")
            call gen_main("We will not vanish without a fight!", face="open")
            call gen_main("We're going to live on!{w} We're going to survive!", face="angry")
            $ qp_mob_reaction[0] = None
            $ qp_mob_reaction[1] = None

        "\"Sunshine and rainbows.\"": #Rocky
            play bg_sounds "music/BattleThemeB.mp3" fadein 3.0
            call gen_main("The world ain’t all sunshine and rainbows...\nIt is a very mean and nasty place and it will beat you to your knees and keep you there permanently if you let it.", face="base")
            mal "An inspirational speech in the middle of the game?"
            call gen_main("You, me, or nobody is gonna hit as hard as life.", face="base")
            call sna_main("Aint that true...","snape_09")
            call gen_main("But it ain’t how hard you hit...{w} it’s about how hard you can get hit, and keep moving forward.", face="angry")
            cra "Bullshit."
            call gen_main("How much you can take, and keep moving forward. That’s how winning is done.", face="open")
            call gen_main("Now, if you know what you’re worth, then go out and get what you’re worth.", face="open")
            call gen_main("But you gotta be willing to take the hit, and not pointing fingers saying you ain’t where you are because of him, or her, or anybody.", face="angry")
            call gen_main("Cowards do that and that ain’t you. You’re better than that!", face="angry")
            stop bg_sounds fadeout 2
            $ renpy.sound.play("sounds/crowd_cheer.mp3")
            call gen_main("...", face="grin")
            call gen_main("Nailed it.", face="grin")

        "\"Be winners!\"": #"\"Don't care about the scoreboard\"": #Hoosiers
            play bg_sounds "music/fanfare.mp3" fadein 1.0
            call gen_main("There's a tradition in tournament play to not talk about the next step until you've climbed the one in front of you.", face="base")
            call gen_main("I'm sure going to the state finals is beyond your wildest dreams, so let's just keep it right there.", face="base")
            #Crowd confusion
            cho "(State finals?!?)"
            call gen_main("Forget about the crowds, the size of the school, their fancy uniforms, and remember what got you here.", face="angry")
            call gen_main("Focus on the fundamentals that we've gone over time and time again.", face="open")
            call gen_main("And most important, don't get caught up thinking about winning or losing this game.", face="base")
            call gen_main("If you put your effort and concentration into playing to your potential, to be the best that you can be, I don't care what the scoreboard says at the end of the game, in my book we're gonna be winners!", face="open")
            call gen_main("{size=+5}Okay?!!{/size}", face="angry") #Large text
            $ renpy.sound.play("sounds/crowd_cheer2.mp3")
            call gen_main("{size=+8}Alright!!{/size}", face="open")
            call gen_main("{size=+10}Let's go!!{/size}", face="angry")
            call gen_main("{size=+10}Let's go!!{/size}", face="angry")
            call gen_main("{size=+10}Let me hear it!!!{/size}", face="angry")
            #Applause

    call play_sound("footsteps")
    call hide_characters
    with d3
    pause .5

    $ snape_chibi.zorder = 1
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 2

    call her_chibi("stand", 160, 70, flip=True)
    with d3
    pause .5
    call gen_chibi(flip=True)
    with d3
    pause .2

    call her_walk(xpos=310, ypos=105, speed=2)
    pause .3

    play bg_sounds "sounds/crowd_low.mp3" fadein 3 fadeout 2

    call her_main("I'm back!","soft","base","worried","L", cheeks="blush", ypos="head", flip=True) #whispering #Blushing from this point forward
    call sna_main("Miss Granger?","snape_05", ypos="head")
    call her_main("It's...","disgust","base","worried","down", cheeks="blush")

    call gen_walk(xpos=345, ypos=25, speed=0.3)
    pause .2

    m "Get up there, the crowd has started to suspect something..."
    call her_main("Oh...{w=0.5} of course!","soft","narrow","worried","mid", cheeks="blush")

    call her_walk(xpos=375, ypos=105, speed=1)
    pause .1
    call gen_chibi("hide")
    with d3
    call gen_chibi("stand", 130, 10, flip=False)
    with d3
    pause .5

    #Microphone static sound
    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    call her_main("*Ahem*...","base","base","base","mid", flip=True, xpos="120", ypos="base")
    call her_main("{size=-4}Oh, these boobs are so heavy...{/size}","disgust","base","worried","down", cheeks="blush")
    #Crowd ???
    call her_main("{size=-4}And why is this shirt so hot...{/size}","soft","base","base","down", cheeks="blush")
    
    $ renpy.sound.play("sounds/cloth_sound.mp3")
    $ hermione_class.equip(hermione_outfit_default_no_vest)
    with d3
    pause 1.0

    g4 "..."
    $ renpy.sound.play("sounds/cloth_sound2.mp3")
    $ hermione_class.equip(hermione_outfit_default_no_tie_open_shirt)
    with d3
    pause 1.0
    
    call her_main("{size=-4}That's better.{/size}","base","base","base","down", cheeks="blush")
    call her_main("So, after that short... intermission and removing that... streaker of the pitch...","open","base","base","L")
    #Crowd !!!
    g4 "There was a streaker on the pitch? WHEN!?!"
    call sna_main("She's deflecting the attention from the podium...","snape_09")
    m "Oh, of course..."

    call her_main("Now, back to your positions...","open","base","base","mid")
    call her_main("{size=-4}How nice, I'm not used to being listened to this easily!{/size}","base","base","base","ahegao", cheeks="blush")

    #Crowd exclamation
    sly1 "{size=+8}Oh, shut up slut... or I'll make you!{/size}"
    call her_main("Looking forward to it!","base","base","angry","L")

    #Crowd questionmark
    sly1 "..."
    m "What's wrong with her, did she get hit too hard?"
    call her_main("Hooch, give that whistle a good blow for me will you?","soft","base","angry","L")
    pause 0.5
    $ renpy.sound.play("sounds/referee.mp3")
    call play_music("quidditch")
    pause 1.5
    hide screen hermione_main
    with d3
    call sna_main("...","snape_04")
    call sna_main("Hmm... wouldn't be the first time a students personality changed from a bludger hit... ","snape_35")
    call sna_main("Perhaps Madam Pomfrey's healing drafts aren't being distilled properly...","snape_09")
    m "If you say so..."

    call her_main("With those strong and muscular Slytherins in a firm lead, we're now back in the game.","open","base","base","L")
    $ renpy.sound.play("sounds/ball_hit.mp3")
    call her_main("Look at those bats swing! I wouldn't mind being hit by one of those, if you know what I'm saying.","angry","base","angry","L")
    call her_main("And watch those Ravenclaws go, such finesse and style is a rare sight...","open","base","base","L")
    call her_main("Miss Chang sure knows how to handle that broom between her thighs.","angry","base","angry","L")
    cho "!!!"

    # Section where genie goes up and touches Hermione (tonks) under her skirt
    call sna_main("You know... Tonks isn't here right now...","snape_05") #Small text
    m "So?" #Small text
    call sna_main("...","snape_37") #Smirks
    g9 "Oh...{w=0.3} I see what you mean..."#Small text
    call gen_walk(xpos=290, ypos=55, speed=2.5)
    call gen_chibi(action="hide")
    $ hermione_chibi.zorder = 5
    #
    #
    #
    # You can use chibi call to display images if you set action="animation" and pic="image"
    #
    #
    #
    call hg_chibi_transition("grope_on_podium_idle")
    with d3
    pause .5
    # Genie starts sneaking up behind Hermione (Tonks)
    call her_main("Cute brunette passes to handsome blonde boy...","base","base","base","mid")
    hide screen hermione_main
    with d3
    pause 1.0
    call hg_chibi_transition("grope_on_podium")
    with d3
    pause 2.0
    call her_main("Whoa!","base","base","base","mid") # Look of surprise
    hide screen hermione_main
    with d3
    call ctc
    # Crowd ???
    g9 "..."
    call her_main("No worries ladies and gentlemen, just had a bit of a slip. It's very...{w=0.3} wet up here...","base","base","base","mid") #blushing
    m "(And it will be getting even wetter in a minute...)"
    call hg_chibi_transition("grope_on_podium_horny")
    hide screen hermione_main
    show screen blktone5
    with d5
    pause .2
    "You move your hands gently up and down underneath Hermione's skirt, massaging her butt and thighs."
    hide screen blktone5
    with d5
    pause .2
    call her_main("*Hmm*{w=0.3} Those boys are going... *Ahh*{w=0.5}, going way too fast! This game might be over before we know it.","base","base","base","mid")
    g9 "(Let's slow down a bit then shall we...)"
    hide screen hermione_main
    show screen blktone5
    with d5
    pause .2
    "You continue touching Hermione and as you go on she's finding it more and more difficult to focus on the game."
    hide screen blktone5
    with d5
    pause .2
    call her_main("*Ahh*{w=0.3} Still...{w=0.3} Still no...*Ahh*{w=0.3} sign of the golden snitch...","base","base","base","mid")
    m "(It's right here... I'm rubbing it for good luck...)"
    call her_main("*Mmmm*{w=0.4} Those boys sure are doing well. I've never...{w=0.4} *Hnngh*{w=0.3} experienced such a...{w=0.5} such a...{w=0.6} thrill before!","base","base","base","mid") #Thrill big text
    g9 "(Time to get some of my own liquid luck!)"
    hide screen hermione_main
    show screen blktone5
    with d5
    pause .2
    "You keep touching Hermione, moving your hand further and further underneath her skirt and as you begin rubbing her vagina with increased pressure you feel a bit of a wet spot forming across her panties."
    hide screen blktone5
    with d5
    pause .2
    call her_main("Oh! That's naughty!{w=0.3} *Ahh*...{w=0.3} One of the Slytherin beaters just went head on and smashed their elbow into an opposing player...","base","base","base","mid")
    hide screen hermione_main
    show screen blktone5
    with d5
    pause .2
    "Noticing Hermione's breathing becoming more and more erratic you pick up the pace, moving your middle finger back and forwards across the underside of her wet panties."
    hide screen blktone5
    with d5
    pause .2
    call her_main("And we all know...{w=0.3} *Ahh*{w=0.3} No excessive use of elbows...{w=0.3} *Ahh*{w=0.3} Permitted...","base","base","base","mid")
    call her_main("But it seems to have done the trick!","base","base","base","mid")
    call her_main("The Slytherin chasers are... {w=0.3}*Ahh*...{w=0.3} Edging ever closer... to the goal posts!","base","base","base","mid")
    call hg_chibi_transition("grope_on_podium_close")
    hide screen hermione_main
    show screen blktone5
    with d5
    pause .2
    "As the quaffle is thrown towards one of the hoops you give Hermione one last rub across her panties bringing her over the edge."
    hide screen blktone5

    $ renpy.sound.play("sounds/crowd_applause.mp3")
    call her_main("{size=+8}Goooaaal!!!{/size}","base","base","base","mid") # Orgasmic face. Yell "Cumming!!!" instead?
    hide screen hermione_main
    with d3
    pause 0.5
    call cum_block
    call hg_chibi_transition("grope_on_podium_cumming")
    pause 0.7
    show screen blktone5
    with d5
    "Hermione's legs tremble as her knees buckle, the words of her orgasm drowned out by the cheers of the crowd."
    call ctc
    hide screen blktone5
    with d5
    pause 1.0

    # Hermione (Tonks) falls to her knees
    $ hermione_chibi.zorder = 2
    $ genie_chibi.zorder = 3
    hide screen hermione_main
    hide screen grope_ass_podium
    call her_chibi("kneel_pant", 325, 170)
    call gen_chibi("stand", flip=True)
    with d5
    # Genie walks back to his seat
    call gen_walk(xpos=130, ypos=10, speed=2)
    call gen_chibi("stand", flip=False)

    "With Hermione collapsed on the ground you give last quick look and then swiftly head back to your seat..."
    "Her legs still shaking slightly she tries fruitlessly to stand up and compose herself."
    #Loafy move Hermione sprite down on the screen until she stands
    call her_main("*Ahh*...{w=0.3}*Ahh*...{w=0.3}Sir...{w=0.2} that was...{w=0.3} *Ahh*...","base","base","base","mid")
    #Loafy Hermione' sprite should probably not stay on the screen here
    #"Before she finishes her sentence you give Hermione a quick smirk and swiftly head back to your seat..."
    g9 "Now, where were we?" #Small text
    hide screen hermione_main
    with d3
    call sna_main("Another goal for Slytherin... Although you might've missed it...","snape_37") #Small text
    "You smirk and look back at Hermione who's still on the floor trying to catch her breath."
    call sna_main("You can wipe that smile off your face now...","snape_01")
    call sna_main("Whatever your plan is I doubt you'll succeed...","snape_03") #smirk
    call sna_main("Another couple of goals and you won't win even if Miss Chang manages to catch the snitch.","snape_45")
    call sna_main("Ravenclaw has no chance, We've got this game in the bag.","snape_01")
    g9 "You say that..."
    call nar("Cho, now with her eyes fixed behind one of the goalposts, seemingly having spotted the snitch, gives you a quick glance and a smile as she flies up to Crabbe and Goyle.")


    ### Cho CG ###

    call hide_characters
    show screen blkfade
    with d5
    pause .8

    hide screen blkfade
    with d5

    # TODO: add ass shot (CG)
    cho "Hey boys, check this out..."
    cra "What do you want slut-"
    call nar("Cho spins around, flaunts her butt and gives them a quick wink.")
    goy "..."
    goy "Looks like this little Ravenclaw slut has finally come to her senses, Crabbe."
    cra "Why wouldn't she Goyle... Those Ravenclaw cucks got nothing even close to our sheer strength!" #have is correct grammar here but crabbe and goyle are dumb shits so
    call nar("Cho tightens her butt cheeks and flutters her eyelashes in a way that to anyone except Crabbe and Goyle would be an obvious distraction tactic.")

    play sound "sounds/crowd_cheer.mp3"
    call her_main("And there's a goal for Ravenclaw ladies and gentlemen, look at those cuties go... those clothes must be completely stuck to their skin in this weather!","soft","base","base","up", ypos="head", flip=True)

    call nar("Malfoy suddenly turns around with a surprised look on his face that a goal was let in and then angrily flies up to Crabbe and Goyle.")
    malf "What the hell are you guys doing, have those bludgers been hitting you too hard? You're supposed to be blocking the goal until that Ravenclaw girl spots the snitch!"
    cra "Well, about that..."
    malf "How dare you speak over me, I'm not done with you!"
    cra "But Dra...{w=0.6}{nw}"
    malf "What?!?"
    cra "She's going after the Snitch!"

    call nar("Malfoy spins his head around. Finally noticing that Cho's currently chasing the snitch in the distance, he quickly darts after her.")
    malf "You fucking idiots!"
    
    #Hermione should now stand up after the CG
    
    call her_main("Oh... it looks like things are heating up! Malfoy has finally realised Chang is going for the Snitch...","open","base","angry","L")
    $ renpy.sound.play("sounds/giggle2_loud.mp3")
    call her_main("*giggles* Look at that girl fly! I didn't think you could grip a broom so tightly... maybe I could learn a thing or two from her.","grin","base","angry","L")
    call sna_main("I see we've been playing different games...","snape_37")
    g9 "Quite..."
    call her_main("Chang, now only inches away, can almost taste that ball...","grin","base","angry","up")
    call her_main("Malfoy on his superior broom edging ever closer...","open","base","angry","L")
    call sna_main("Well, congratulations... You've got me beat...","snape_37")
    call sna_main("Sure as hell is a better view than last season...","snape_20")
    $ qp_mob_reaction[0] = "emo8"
    $ qp_mob_reaction[1] = "emo7"
    $ qp_mob_reaction[2] = "emo7"
    play bg_sounds "sounds/crowd.mp3" fadein 1 fadeout 1
    $ renpy.sound.play("sounds/crowd_applause.mp3")
    call her_main("And she's caught it! Ravenclaw wins and makes it to the finals against Gryffindor!","smile","base","angry","L")
    call sna_main("I was looking forward to seeing that cup in my office again this year... Oh well...","snape_41")
    call her_main("And what a well deserved victory as well!","soft","narrow","base","mid")
    m "You put the cup in your office?"

    #Fades to black
    call hide_characters
    show screen blkfade
    with d5
    pause .8

    #TODO Show standing Hermione chibi when Cho's CG is hidden
    call her_chibi("hide") # Hermione is already gone.
    call gen_chibi("standing_alt", xpos=130, ypos=10, flip=False)
    call sna_chibi("stand", xpos=220, ypos=-50, flip=False)

    $ qp_mob_reaction[0] = None
    $ qp_mob_reaction[1] = None
    $ qp_mob_reaction[2] = None
    $ qp_mob = 0

    stop bg_sounds fadeout 4
    stop music fadeout 2

    #Fades back to empty stadium
    hide screen blkfade
    with d5
    pause .5

    play bg_sounds "sounds/wind_long_loop.mp3" fadein 2 fadeout 2

    call sna_main("Well, that was good...","snape_03")
    call sna_main("And to my dismay the commentary was... acceptable.","snape_09")
    m "What?!"
    m "I thought that you didn't like miss Granger..."
    g9 "Where's that Slytherin pride you're so adamant about?"
    call sna_main("*HMPH*... I'm sure you can find your own way back to your office...","snape_05")
    m "What about our bet?"
    sna "The bet?"
    m "I beat you, Slytherin is out of the competition!"
    g9 "Show me the money!"
    sna "..."
    sna "The Bet was for Slytherin or Ravenclaw winning the cup."
    sna "You'll get your money if Ravenclaw beats Gryffindor in the finals."
    g4 "Balls..."
    sna "Who would've foreseen it would be in my best interest for Gryffindor to win the cup..."




    #Blackfade
    show screen blkfade
    with d9
    pause .5

    stop bg_sounds fadeout 4

    call play_sound("grass")
    "You make your way back to your office... wondering how the real old man could stand all these stairs, no wonder he always stayed in there."

    # Reset
    $ tonks_class.equip(tonks_outfit_last) # Equip player outfit.
    $ hermione_class.equip(hermione_outfit_last) # Equip player outfit.
    $ cho_class.equip(cho_outfit_last) # Equip player outfit.

    jump night_start



label slytherin_match_return:
    #Office screen, evening after game
    menu:
        "event not posed yet!"
        "got it.":
            pass
    m "(That went well... Wine,{w=0.8} Ass...{w=0.5} and a good sho-...){w=0.8}{nw}"

    #Tonks as Hermione walks in
    m "(Oh, shit...)"
    call her_main("That was...{w=0.5} amazing!","base","base","base","mid")
    g4 "What?"
    call her_main("I've never experienced such a thrill before...","base","base","base","mid")
    call her_main("Trying to keep it together when everyone was watching the game...","base","base","base","mid")
    g4 "Err..."
    g9 "Glad you enjoyed it!"
    call her_main("*Hmm* - I think someone deserves a bit of a reward...","base","base","base","mid") #Horny
    g4 "What do you-...{w=0.8}{nw}"
    #Hermione takes her top off
    m "Miss Granger?"
    call her_main("Be quiet you, just enjoy it!","base","base","base","mid")
    #Hermione takes her bottoms off
    call her_main("*Hmm* - You like these cute panties?","base","base","base","mid")
    #Giggle sound effect
    call her_main("*Hi-Hi-Hi*","base","base","base","mid")
    g4 "..."
    call her_main("Or these little puppies...","base","base","base","mid")
    #Hermione takes her bra off
    nar "Hermione glances at her breasts and removes her bra whilst shaking her breasts at you lustfully."
    call her_main("Much better without the bra don't you think?","base","base","base","mid")
    m "I..."
    call her_main("You like looking at this body, don't you?","base","base","base","mid")
    call her_main("Tell me!","base","base","base","mid")
    g4 "I do!"
    call her_main("I knew you did, I could feel your eyes in the back of my neck when I was up there...","base","base","base","mid")
    m "Who wouldn't with a body like that..."
    call her_main("Damn right...*Mmmm*","base","base","base","mid")
    call her_main("And since you love this butt so much...","base","base","base","mid")
    nar "Hermione bends over and takes her panties off, throwing them to the side."
    call her_main("...","base","base","base","mid")
    call her_main("What do you think?","base","base","base","mid")
    m "Looking grea-{w=0.6}{nw}"

    #Cho walks in
    cho "I did it! We won the...{w=0.8}{nw}"
    #Hermione turns to Cho
    cho "!!!" #Shocked face
    call her_main("Oh, hello there Miss Chang...","base","base","base","mid")
    call her_main("Like what you see?","base","base","base","mid")
    cho "I..."
    #Giggle sound effect
    call her_main("*Hi-Hi-Hi*","base","base","base","mid")
    call her_main("What's wrong sweetie?","base","base","base","mid")
    call her_main("Want to find out if Gryffindors taste the same as Ravenclaws?","base","base","base","mid")
    cho "..." #Blushes
    cho "*HMPH!"
    #Cho walks out and slams the door
    call her_main("Meh...{w=0.4} Suit yourself...","base","base","base","mid") #Shruggs it off and turns back to genie
    m "What the hell are you doing Granger?"
    call her_main("Granger?","base","base","base","mid") #confused
    call her_main("What are you talking about genie?","base","base","base","mid")
    #Tonks turns back into herself (clothed)
    g4 "Whoa!"

    if tonks_morph_known:
        m "It all makes sense now."
        call ton_main("Hello sweet cheeks!","base","base","base","mid")
        call ton_main("Thought I was about to lose focus there for a second when you started going at it!","base","base","base","mid")
        m "You should’ve told me it was you..."
        call ton_main("I tried to!","base","base","base","mid")
        call ton_main("You pretty much pushed me onto the podium when I got back...","base","base","base","mid")
        m "Oh, yeah..."

    else:
        $ tonks_morph_known = True
        g4 "You were Miss Granger the whole time?"
        m "Plot twist of the fucking century."
        call ton_main("Of course not, don't be silly...","base","base","base","mid")
        call ton_main("I'm a metamorphmagi...","base","base","base","mid")
        m "A meta what?"
        m "(I thought I was the only one allowed to be meta in this game...)"

    call ton_main("It means I can look like whatever I want.","base","base","base","mid")
    m "Really?"
    call ton_main("Of course!","base","base","base","mid")
    #Tonks turns into cho
    cho "Hi professor, want to give this snatch a little lick?"
    #Tonks turns into Astoria if you've met her
    ast "How about giving this little butt a spanking?"
    #Tonks Turns into Susan if you've met her
    sus "You want to s...spank me? W-Why would you want to s... spank me professor? Did I do something wrong?"
    #Tonks turns into Luna if you've met her
    lun "Oh, Tonks look out you got a jigglypuff on your shoulder, let me lick it off for you!" #lmao nice
    lun "*Hi-Hi-Hi*"
    #Tonks turn into snape (Wearing the weird hat and handbag?)
    call sna_main("Want some of this Genie? Mind if I...{w=0.4} Slithered in?","snape_01")
    g4 "..."
    call sna_main("*Hi-Hi-Hi*","snape_01")
    #Tonks turns into herself
    call ton_main("I'm especially proud of that last one...","base","base","base","mid")
    m "..."
    m "So...{w=0.2} Can all wizards do this?"
    call ton_main("Nah, I was born with it.","base","base","base","mid")
    m "This world, I swear there's something new every day..."
    m "What next?{w=0.2} Can you time travel?"
    call ton_main("I wish! The ministry won't let me do it...","base","base","base","mid")
    call ton_main("If I could I'd just go back to kill baby \"you know who\"...","base","base","base","mid")
    m "(That is always the first thing people consider when talking about time travel...)"
    m "Unbelievable..."

    m "So...when Miss Granger got hit by that bludger..."
    call ton_main("I took her to the hospital wing...","base","base","base","mid")
    call ton_main("And I replaced her so she wouldn't get bullied.","base","base","base","mid")
    m "I see..."
    m "And she..."
    call ton_main("Her face is fine... *Hmmm* - Your face is so cute when you worry, you know...","base","base","base","mid")
    m "So, won't people find out you replaced her?"
    call ton_main("You think so?","base","base","base","mid")
    call ton_main("I can lie if I want! Who will they believe?","base","base","base","mid")
    g4 "..."
    call ton_main("Anyway...","base","base","base","mid")
    call ton_main("Unless she has a really good reason to I doubt she'll tell anyone.","base","base","base","mid")
    call ton_main("*Urgh* My head hurts I'm gonna go sleep off whatever this is...","base","base","base","mid")
    call ton_main("Toodaloo!","base","base","base","mid")
    #Tonks leaves
    #End

    $ tonks_busy = True
    $ snape_busy = True
    $ hermione_busy = True
    $ cho_busy = True

    #$ cho_tier = 3 # TODO: activate this after adding favors.

    jump main_room
