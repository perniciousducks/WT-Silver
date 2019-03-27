transform crop_meter(fill, opacity):
    subpixel True
    transform_anchor True
    on show, appear, start:
        alpha opacity
        yanchor 1.0
        yzoom -1.0
        easein_back 1.0 crop (0, 0, 60, int((float(fill)/100)*500))
        repeat

label exp_o_meter(fill=50, opacity=1.0):
    show screen exp_o_meter(fill=fill, opacity=opacity)
    #with d3
    return
    
screen exp_o_meter(fill, opacity):
    tag exp_o_meter
    zorder 4
    
    frame:
        style "empty"
        xpos 50
        ypos 570
        
        add "interface/meter/"+interface_color+"/meter.png" yanchor 1.0 alpha opacity
        add "interface/meter/fill.png" at crop_meter(fill, opacity)
        add "interface/meter/glass.png" yanchor 1.0 alpha opacity
        
    frame:
        style "empty"
        xpos 150
        ypos 70
        add "interface/meter/"+interface_color+"/circle.png" alpha opacity
        if fill >= 90:
            add "interface/meter/100.png" alpha opacity
        elif fill >= 50:
            add "interface/meter/50.png" alpha opacity
        else:
            add "interface/meter/0.png" alpha opacity
    
screen swear_bubble(type):
    tag bubble
    zorder 6
    
    add "interface/meter/bubble/"+str(type)+".png" ypos 100 xpos 100
    timer 1.0 action Hide("swear_bubble")
            
label cho_quiz_1:    
    call cho_chibi(xpos="mid")
    
    if cho_quiz_assed:
        jump cho_quiz_2
        
    $ confidence_meter = 50
    call exp_o_meter(fill=confidence_meter, opacity=0.0)
        
    if cho_quiz_first_attempt:
        $ cho_quiz_first_attempt = False
        g9 "So, let’s begin on this Quiddetch thing then..."
        call cho_main("Quidditch sir... I’m sure I’ve seen you at our games before...", "annoyed", "suspicious", "raised", "mid")
        call cho_main("Two teams, balls, goal hoops... Ring a bell?", "soft", "angry", "raised", "R")
        g9 "Ah, yes... Quidditch, my tongue must’ve slipped!"
        call cho_main("...", "smile", "closed", "raised", "down")
        m "The basketball rip off of wizards... My favourite sport! How could I forget..."
        call cho_main("What’s basketball?", "open", "suspicious", "base", "mid")
        m "..."
        m "Never seen space Jam?"
        call cho_main("...", "pout", "base", "raised", "mid")
        g4 "Come on."
        m "Well..."
    else:
        m "I’m ready to make my case on how Quidditch is similar to basketball..."
        call cho_main("Really sir... again?", "open", "angry", "angry", "L")
        m "Of course, it’s an important subject for your education..."
        call cho_main("I can't really see how but I’m sure you know what you’re talking about...", "open", "base", "base", "mid")
        m "Alright, so..."
    
    $ renpy.music.play("music/ominous_music.mp3")
    $ renpy.music.stop("weather")
    
    
    call exp_o_meter(fill=confidence_meter)
    menu:
        "There’s five players on each team...":
            $ cho_answer_1 = False
            m "There’s two teams with each one having five players on the court at one time..."
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()   
            call cho_main("Whilst Quidditch does have two teams...{w=0.5} there’s 7 players on each...", "annoyed", "suspicious", "raised", "mid")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ _preferences.volumes['music'] = volume 
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Ah,{w=0.4} well..."
            
        "At the start of the game the ball gets thrown in the air...":
            $ cho_answer_1 = True
            m "You start the game by the referee throwing the ball into the air..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.sound.play( "sounds/hmm1.mp3")
            $ renpy.block_rollback()
            call cho_main("I guess that’s kind of similar...", "smile", "base", "raised", "mid")
            $ _preferences.volumes['music'] = volume 
            g9 "It is? I mean, yes... and also..."
    
    menu:
        "It’s played on a rectangular court...":
            $ renpy.block_rollback()
            $ cho_answer_2 = False
            m "The game is played on a rectangular court...{w=1.0}{nw}"
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            call cho_main("Well, that’s not similar at all then. The Quidditch pitch is oval shaped...", "annoyed", "suspicious", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ _preferences.volumes['music'] = volume 
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Of course!{w=0.4}... and in basketball..."
            
        "You may not go out of bounds with the ball...":
            $ renpy.block_rollback()
            $ cho_answer_2 = True
            m "You're not allowed outside the bounds whilst holding the ball or you'll have to hand it over to your opponents team..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.sound.play("sounds/hmm1.mp3")
            call cho_main("I guess that's pretty much the same as in Quidditch...", "base", "wide", "raised", "L")
            $ _preferences.volumes['music'] = volume
            m "Great! I mean, obviously! And..."

    menu:
        "Each player takes a certain position...":
            $ renpy.block_rollback()
            $ cho_answer_3 = True
            m "Each player takes a certain position."
            m "There are defensive positions..."
            m "And offensive positions..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.sound.play( "sounds/hmm2.mp3")
            call cho_main("I guess Quidditch has something like that...", "base", "suspicious", "base", "R")
            $ _preferences.volumes['music'] = volume 
            g9 "Exactly, which is obviously why I brought it up, and lastly..."

        "You can’t run with the ball unless you dribble or pass":
            $ renpy.block_rollback()
            $ cho_answer_3 = False
            m "You can’t run whilst holding the ball,{w} you need to pass it or dribble...{w=1.0}{nw}"
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            call cho_main("Well, you can move with the ball freely without passing in Quidditch, that’s why we have the beaters...", "annoyed", "suspicious", "raised", "mid")
            call cho_main("To make the opponents drop the ball.", "open", "suspicious", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ _preferences.volumes['music'] = volume
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Ah!{w=0.4} Well, I guess that is different... Lastly though..."
            
            
    menu:
        "You can’t touch your opponent...":
            $ renpy.block_rollback()
            $ cho_answer_4 = False
            m "You’re not allowed to touch your opponent or it would be counted as a foul..."
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            call cho_main("Well, that’s definitely not the case in Quidditch...", "annoyed", "suspicious", "raised", "mid")
            call cho_main("Except for excessive use of elbows...", "open", "suspicious", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            g4 "Well...{w=0.4}"
            m "Fine..."

        "You score by getting the ball through a hoop...":
            $ renpy.block_rollback()
            $ cho_answer_4 = True
            m "The way you score is by getting the ball through a hoop."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.sound.play( "sounds/hmm3.mp3")
            call cho_main("Hmm, well that’s the same as in Quidditch I suppose...", "smile", "suspicious", "base", "L")
            g9 "Naturally..."
    pause 1.0
    hide screen exp_o_meter
    with d3
    $ _preferences.volumes['music'] = volume
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    if raining:
        $ renpy.music.play("sounds/rain.mp3", "weather", fadeout=1.0, fadein=1.0)
    if blizzard:
        $ renpy.music.play("sounds/blizzard.ogg", "weather", fadeout=1.0, fadein=1.0)
    $ renpy.block_rollback()
    
    if not cho_answer_1 and not cho_answer_2 and not cho_answer_3 and not cho_answer_4:
        m "Well, I’m sure that the winning conditions are pretty similar at least..."
        call cho_main("And what are the winning conditions?", "base", "base", "base", "mid")
        m "You win by having the most amount of points when the time is over."
        call cho_main("Well, in Quidditch the game doesn’t end until the snitch is caught, so it could technically go on forever.", "open", "suspicious", "raised", "mid")
        call cho_main("So in short... nothing like basketball.", "pout", "closed", "base")
        m "The game doesn’t end until the snitch is caught?"
        call cho_main("Yes...", "base", "base", "base", "mid")
        m "Well, that is stupid..."
        call cho_main("Yes, that bit is kind of stupid...", "pout", "base", "sad", "down")
        call cho_main("Anyway...", "base", "closed", "base")
        call cho_main("I didn’t come here to listen to you talk about about basketball...", "pout", "base", "base", "downR")
        m "Right..."
        call cho_main("I came for you to tutor me...", "annoyed", "suspicious", "angry", "L")
        m "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)"
        g9 "Oh, well... look at the time!"
        call cho_main("What?", "open", "shocked", "raised", "mid")
        g9 "You’ve made me go about basketball for such a long time so we’re already at the end of today's session."
        call cho_main("But we didn’t even get to any tutoring...", "annoyed", "suspicious", "base", "mid")
        m "We’ll get there, don’t you worry... next time..."
        call cho_main("...{w=0.4}Fine.", "pout", "base", "base", "mid")
        call cho_main("Bye then professor...", "annoyed", "base", "base", "mid")
        
        hide screen cho_chang
        call cho_walk("mid","leave",2.5)
        
        g4 "(What am I supposed to do now... I clearly know fuckall about Quidditch...)"
        m "(I’d rather not ask Snape... but unless there’s someone else that I could ask without sounding like a complete dumbass it might have to do...)"
        if store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"
        $ cho_quiz_failed = True
        
    elif cho_answer_1 and cho_answer_2 and cho_answer_3 and cho_answer_4:
        $ cho_quiz_assed = True
        m "So as you can see, Basketball and Quidditch is pretty much the same game..."
        call cho_main("I’m sure that can’t be right...", "annoyed", "base", "base", "mid")
        call cho_main("I’ll have to look up this... basketball thing.", "open", "suspicious", "base", "mid")
        m "No need, I think I pretty much covered it."
        cho "I'm still quite unsure if you actually know Quidditch or am just trying to confuse me with Basketball terms..."
        m "(Fuck, she's onto me!)"
        m "Of course I'm not... I'll prove it to you!"
        m "(Wait, why did I say that?)"
        cho "..."
        cho "Okay then, show me what you got..."
        
        jump cho_quiz_2
    else:
        call cho_main("I guess it has some similarities...", "pout", "suspicious", "sad", "mid")
        m "Pretty much the same game I’d say..."
        call cho_main("I wouldn’t say that... You fly for one in quidditch...", "open", "base", "base", "mid")
        m "You do?!?"
        call cho_main("Very funny professor, of course you do...", "pout", "base", "raised", "down")  
        call cho_main("Anyway, weren’t you supposed to tutor me?...", "annoyed", "angry", "base", "L")
        m "Oh, right..."
        m "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)"
        g9 "Oh, well... look at the time!"
        call cho_main("What?", "upset", "closed", "sad")
        g9 "You’ve made me go about basketball for such a long time so we’re already at the end of today's session."
        call cho_main("But we didn’t even get to any tutoring...", "annoyed", "angry", "angry", "mid")
        m "We’ll get there, don’t you worry... next time..."
        call cho_main("...{w=0.4}Fine.", "annoyed", "angry", "base", "mid")
        call cho_main("Bye then professor...", "pout", "base", "base", "R")
        hide screen cho_chang
        call cho_walk("mid","leave",2.5)
        
        g4 "(The fuck am I supposed to do now... I feel like that must’ve been a fluke, I know nothing about Quidditch..)."
        m "(I’d rather not ask Snape... but unless there’s someone else that I could ask without sounding like a complete dumbass it might have to do...)"
        if store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"
        $ cho_quiz_failed = True 
        
    $ cho_busy = True        
    jump main_room
    
label cho_quiz_2:
    $ confidence_meter = 50
    $ cho_answer_5 = 0
    call exp_o_meter(fill=confidence_meter, opacity=0.0)
    
    $ renpy.music.play("music/determined_pursuit_loop.mp3")
    $ renpy.music.stop("weather")
    
    cho "You do seem to know some basic things, but do you know anything about the balls?"
    m "I could probably teach you quite a lot. You should never neglect the balls."
    cho "In that case..."
    cho "I am a seeker, it is my job to catch the \"Blank\" to end the game and score our team 150 points."
    call exp_o_meter(fill=confidence_meter)
        Menu:
            "Stitch":
                m "Stitch?"
                cho "no..."
                g4 "Oh wait, that's that blue alien thing isn't it?"
                cho "I don't know what a stitch is, sorry sir..."
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "Next question..."            
            "Lich":
                m "Lich?"
                cho "the ball is an undead skeletal creature?"
                g4 "Oh, that's what I said? I must've had a PTSD flashback from my tomb raiding days..."
                cho "You've been tomb raiding?"
                m "..."
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                m "NOOOoooo...."
                cho "Next question..."
            "Snitch":
                m "Snitch?"
                cho "Yes!"
                $ confidence_meter += 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/hmm1.mp3")
                g9 "Well then, surely that should show you how superio...{w=1.0}{nw}"
                cho "Next question..."
                $ cho_answer_5 += 1

    cho "Apart from the Snitch there are two other types of balls on the pitch, what are they called?"
        Menu:
            "Butter and Waffles":
                m "Butter and Waffles?"
                cho "Sir?"
                m "Sorry, I didn't have any lunch..."
                g4 "Actually, I can't even remember the last time I ate..."
                cho "Well, you're obviously wrong..."
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "Next question..."
            
            "Bludger and Quaffle":
                m "Bludger and Quaffle?"
                $ confidence_meter += 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/hmm2.mp3")
                cho "Yes!"
                g9 "Great! Then lets get started with the...{w=1.0}{nw}"
                cho "Next question..."
                $ cho_answer_5 += 1
                
            "Quabble and Bluffer":
                m "Quabble and bluffer?"
                cho "I think you got some letters mixed up there..."
                m "Quibble and Blodger?"
                cho "No, that's also...{w=1.0}{nw}"
                m "Qacker and Blugger?"
                cho "Professor..."
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "Next question..."
    
    cho "Let's do some history..."
    m "I am made out of history, this should be a breeze..."
    cho "Okay then..."
    cho "A game of Quidditch doesn't finish until the Snitch is caught, therefor it could go on forever..."
    cho "In the longest ever match played they had to constantly bring on substitutes to let the players get some sleep..."
    cho "For how long did the game go on for?"   

        Menu:
            "Three Months":
                m "Three months?"
                $ confidence_meter += 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/hmm3.mp3")
                cho "Yes!"
                cho "That's impressive, how did you know that one?"
                m "I feel like there wasn't that many realistic options available this time..."
                cho "Okay... not sure what that means..."
                cho "Anyway, final question..."
                $ cho_answer_5 += 1
                
            "Seven Years":
                m "Seven years?"
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "You crazy? That's the same amount of time a student stays at Hogwarts..."
                m "Oh right, I don't know what I was thinking... seven just seems like the magical right answer most of the time..."
                cho "Not in this case..."
                cho "Anyway, final question..."
                
            "Two Minutes":
                m "Two minutes?"
                cho "What?"
                m "What?"
                cho "Sir, what sport lasts only two minutes?"
                m "A Splurge race?"
                cho "Never heard of it, is it anything like basket ball?"
                m "Well, the balls has a big part of it..."
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "I'll have to take your word on that one..."
                cho "Anyway... final question..."
                
    cho "As you know, you may not go outside of the bounds with the ball during the game or you'd have to hand it over to the opposition..."
    cho "But what is the penalty if the defensive goes out of bounds?"
        Menu:
            "Three Months":
                m "Three months?"
                cho "Three months, what?"
                m "Three months... in jail?"
                cho "Professor, you're not going to get a jail penalty unless you do something that's actually illegal..."
                m "What if the Quidditch pitch was in prison?"
                m "And you flew outside the prison boundaries..."
                m "Did you consider that?"
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "I think you're going off track a bit..."
                m "Or off the field..."
                
            "A free shot at the goal"
                m "Free goal shot?"
                cho "No that's not right..."
                m "Then what is it?"
                cho "Well, I don't know..."
                m "How am I supposed to then?"
                $ confidence_meter -= 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
                cho "Not sure what else to tell you..."
                
            "I don't know...":
                m "Uh... I don't know..."
                $ confidence_meter += 12
                call exp_o_meter(fill=confidence_meter)
                $ renpy.sound.play( "sounds/hmm1.mp3")
                cho "That's right!"
                g4 "What?"
                cho "Nobody knows what happens, there isn't any rule for it..."
                m "Why wouldn't there be a rule for it?"
                cho "Why would the defensive leave the pitch... they'd just leave the goal open..."
                m "..."
                $ cho_answer_5 += 1
                
    pause 1.0
    hide screen exp_o_meter
    with d3
    $ _preferences.volumes['music'] = volume
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    if raining:
        $ renpy.music.play("sounds/rain.mp3", "weather", fadeout=1.0, fadein=1.0)
    if blizzard:
        $ renpy.music.play("sounds/blizzard.ogg", "weather", fadeout=1.0, fadein=1.0)
    $ renpy.block_rollback()
                
    if cho_answer_5 >= 4:
        cho "Well sir, I thought for a minute that you only cared about basketball but it looks like I was wrong..."
        g9 "Of course, I am well versed in all sports. I just thought I'd teach you a thing or two."
        g9 "So, you will let me train you then?"
        call cho_main("I suppose...", "soft", "base", "raised", "R")
        g9 "(Fuck yeah, here we go!)" # Small text.
        call cho_main("And I will stay true to my word... I'll sell you favours...{w}For wins...", "soft", "closed", "base", "mid")
        g4 "(Hell yes!)"
        call cho_main("But keep it civil. I won't do anything those Slytherin skanks do!", "angry", "angry", "sad", "R")
        call cho_main("And should you not be able to help me and my team beat Hufflepuff, this will be over before you can even say Snitch!", "scream", "closed", "raised", "mid")
        g4 "..."
        call cho_main("Anyway, got to go now or I'll be too late for classes.", "smile", "base", "base", "mid")
        call cho_main("I’ll be ready for training by tomorrow morning.", "soft", "base", "base", "down")
        m "{size=-5}Oh, I’m not so sure you’ll be that prepared...{/size}" # Small text.
        call cho_main("Until then, Sir.", "open", "base", "raised", "mid")
        m "Looking forward to it."
        [Training unlocks]
    else:
        cho "You seem to care a lot about basketball sir but I'm not sure if you know that much about Quidditch..."
        m "Or were you asking the wrong questions?"
        cho "Sorry?"
        m "Time is just relative... what is a month or two minutes really..."
        cho "Sir, you got all the questions wrong..."
        m "The truth lies in the eyes of the beholder Miss Chang..."
        cho "I don't..."
        m "You'll see, I'll show you the real truth..."
        m "(Once I can figure out what the fuck I'm doing)"
        cho "..."
        m "Next time..."
        cho "Oh..."
        cho "Good bye then..."
    
    hide screen cho_chang
    call cho_walk("mid","leave",2.5)
    jump main_room