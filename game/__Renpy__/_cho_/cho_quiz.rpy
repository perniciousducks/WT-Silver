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
        m "I'm ready to show you what I know about Quidditch..."
        call cho_main("Great!", "base", "base", "base", "L")
        call cho_main("Let's begin...", "open", "wide", "raised", "mid")
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
        g9 "The basketball rip off of wizards... My favourite sport! How could I forget..."
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
            $ cho_answer_2 = False
            m "The game is played on a rectangular court...{w=1.0}{nw}"
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
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
            $ cho_answer_2 = True
            m "You're not allowed outside the bounds whilst holding the ball or you'll have to hand it over to your opponents team..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
            $ renpy.sound.play("sounds/hmm1.mp3")
            call cho_main("I guess that's pretty much the same as in Quidditch...", "base", "wide", "raised", "L")
            $ _preferences.volumes['music'] = volume
            m "Great! I mean, obviously! And..."

    menu:
        "Each player takes a certain position...":
            $ cho_answer_3 = True
            m "Each player takes a certain position."
            m "There are defensive positions..."
            m "And offensive positions..."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
            $ renpy.sound.play( "sounds/hmm2.mp3")
            call cho_main("I guess Quidditch has something like that...", "base", "suspicious", "base", "R")
            $ _preferences.volumes['music'] = volume 
            g9 "Exactly, which is obviously why I brought it up, and lastly..."

        "You can’t run with the ball unless you dribble or pass":
            $ cho_answer_3 = False
            m "You can’t run whilst holding the ball,{w} you need to pass it or dribble...{w=1.0}{nw}"
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
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
            $ cho_answer_4 = False
            m "You’re not allowed to touch your opponent or it would be counted as a foul..."
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
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
            $ cho_answer_4 = True
            m "The way you score is by getting the ball through a hoop."
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            $ renpy.block_rollback()
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
        call exp_o_meter(fill=confidence_meter, opacity=0.0)
        m "So as you can see, Basketball and Quidditch is pretty much the same game..."
        call cho_main("I’m sure that can’t be right...", "annoyed", "base", "base", "mid")
        call cho_main("I’ll have to look up this... basketball thing.", "open", "suspicious", "base", "mid")
        m "No need, I think I pretty much covered it."
        call cho_main("I'm still quite unsure if you actually know Quidditch or am just trying to confuse me with Basketball terms...", "annoyed", "suspicious", "raised", "mid")
        call exp_o_meter(fill=75)
        g4 "(Fuck, she's onto me!)"
        g9 "Of course I'm not... I'll prove it to you!"
        call exp_o_meter(fill=50)
        g4 "(Wait, why did I say that?)"
        call cho_main("...", "smile", "base", "raised", "mid")
        call cho_main("Okay then, show me what you know...", "smile", "base", "raised", "mid")
        
        jump cho_quiz_2
    else:
        call cho_main("I guess it has some similarities...", "pout", "suspicious", "sad", "mid")
        m "Pretty much the same game I’d say..."
        call cho_main("I wouldn’t say that... You fly for one in quidditch...", "open", "base", "base", "mid")
        g4 "You do?!?"
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
    
    if cho_quiz2_first_attempt:
        $ cho_quiz2_first_attempt = False
        call cho_main("You do seem to know some basic things, but do you know anything about the balls?", "open", "suspicious", "base", "mid")
        m "I could probably teach you quite a lot. You should never neglect the balls."
        call cho_main("In that case...", "base", "base", "base", "mid")
    call cho_main("My position on the team is seeker, it is my job to catch the \"Blank\" to end the game and score our team 150 points.", "open", "base", "base", "L") 
    call exp_o_meter(fill=confidence_meter)
    menu:
        "Stitch":
            m "Stitch?"
            $ renpy.block_rollback() 
            call cho_main("no...", "soft", "angry", "raised", "R")
            g4 "Oh wait, that's that blue alien thing isn't it?"
            call cho_main("I don't know what a stitch is, sorry sir...", "annoyed", "suspicious", "raised", "mid")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down")             
        "Lich":
            m "Lich?"
            $ renpy.block_rollback() 
            call cho_main("the ball is an undead skeletal creature?", "soft", "angry", "raised", "R")
            g4 "Oh, that's what I said? I must've had a PTSD flashback from my tomb raiding days..."
            call cho_main("You've been tomb raiding?", "annoyed", "suspicious", "raised", "mid")
            m "..."
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            m "Of course not..."
            call cho_main("Next question...", "open", "base", "raised", "down") 
        "Snitch":
            m "Snitch?"
            $ renpy.block_rollback() 
            $ renpy.sound.play( "sounds/gasp.mp3")
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            call cho_main("Yes!", "smile", "wide", "raised", "L")
            g9 "Well then, surely that should show you how superio...{w=1.0}{nw}"
            call cho_main("Next question...", "open", "base", "raised", "down") 
            $ cho_answer_5 += 1

    call cho_main("Apart from the Snitch there are two other types of balls on the pitch, what are they called?", "open", "base", "base", "L") 
    menu:
        "Butter and Waffles":
            m "Butter and Waffles?"
            $ renpy.block_rollback() 
            call cho_main("Sir?", "annoyed", "suspicious", "raised", "mid")
            m "Sorry, I didn't have any lunch..."
            g4 "Actually, I can't even remember the last time I ate..."
            call cho_main("Well, you're obviously wrong...", "soft", "angry", "raised", "R")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down")
        
        "Bludger and Quaffle":
            m "Bludger and Quaffle?"
            $ renpy.block_rollback() 
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("Yes!", "smile", "wide", "raised", "L") 
            g9 "Great! Then lets get started with the...{w=1.0}{nw}"
            call cho_main("Next question...", "open", "base", "raised", "down") 
            $ cho_answer_5 += 1
            
        "Quabble and Bluffer":
            m "Quabble and bluffer?"
            $ renpy.block_rollback() 
            call cho_main("I think you got some letters mixed up there...", "soft", "angry", "raised", "R")
            m "Quibble and Blodger?"
            call cho_main("No, that's also...{w=1.0}{nw}", "open", "angry", "raised", "L")
            m "Qacker and Blugger?"
            call cho_main("Professor...", "pout", "wide", "raised", "R")
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Next question...", "open", "base", "raised", "down") 
    
    call cho_main("Let's do some history...", "base", "base", "base", "mid")
    g9 "I am made out of history, this should be a breeze..."
    call cho_main("Okay then...", "smile", "base", "raised", "mid")
    call cho_main("A game of Quidditch doesn't finish until the Snitch is caught, therefor it could go on forever...", "open", "base", "base", "down")
    call cho_main("In the longest ever match played they had to constantly bring on substitutes to let the players get some sleep...", "base", "wide", "raised", "down")
    call cho_main("For how long did the game go on for?", "open", "base", "base", "mid")    
    menu:
        "Three Months":
            m "Three months?"
            $ renpy.block_rollback() 
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("Yes!", "smile", "wide", "raised", "L")
            call cho_main("That's impressive, how did you know that one?", "open", "wide", "raised", "L")
            m "I feel like there wasn't that many realistic options available this time..."
            call cho_main("Okay... not sure what that means...", "soft", "suspicious", "base", "mid")
            call cho_main("Anyway, final question...", "open", "base", "raised", "down") 
            $ cho_answer_5 += 1
            
        "Seven Years":
            m "Seven years?"
            $ renpy.block_rollback() 
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("You crazy? That's the same amount of time a student stays at Hogwarts...", "annoyed", "suspicious", "raised", "mid")
            m "Oh right, I don't know what I was thinking... seven just seems like the magical right answer most of the time..."
            call cho_main("Not in this case...", "open", "base", "raised", "downR")
            call cho_main("Anyway, final question...", "open", "base", "raised", "down") 
            
        "Two Minutes":
            m "Two minutes?"
            $ renpy.block_rollback() 
            call cho_main("What?", "angry", "wide", "raised", "L")
            g4 "What?"
            call cho_main("Sir, what sport lasts only two minutes?", "annoyed", "base", "raised", "L")
            m "A Splurge race?"
            call cho_main("Never heard of it, is it anything like that basketball thing?", "open", "suspicious", "base", "L")
            g9 "Well, the balls has a big role of it..."
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("I'll have to take your word on that one...", "soft", "base", "base", "down")
            call cho_main("Anyway... final question...", "open", "base", "raised", "down") 
                
    cho "As you know, you may not go outside of the bounds with the ball during the game or you'd have to hand it over to the opposition..."
    call cho_main("But what is the penalty if the defensive goes out of bounds?", "open", "wide", "raised", "L") 
    menu:
        "Three Months":
            m "Three months?"
            $ renpy.block_rollback() 
            call cho_main("Three months, what?", "soft", "base", "raised", "L")
            m "Three months...{w=0.5} in prison?"
            call cho_main("Professor, you're not going to get a prison sentence unless you do something that's actually illegal...", "annoyed", "wide", "raised", "L")
            m "What if the Quidditch pitch was in prison?"
            m "And you flew outside the prison boundaries..."
            g9 "Did you consider that?"
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("I think you're going off track a bit...", "open", "base", "base", "down")
            g9 "Or off the pitch..."
            
        "A free shot at the goal":
            m "Free goal shot?"
            $ renpy.block_rollback() 
            call cho_main("No that's not right...", "soft", "angry", "raised", "R")
            m "Then what is it?"
            call cho_main("Well, I don't know...", "annoyed", "angry", "base", "downR")
            g4 "How am I supposed to then?"
            $ confidence_meter -= 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/kung-fu-punch.mp3")
            call cho_main("Not sure what else to tell you...", "open", "base", "base", "R")
            
        "I don't know...":
            m "Uh... I don't know..."
            $ renpy.block_rollback() 
            $ confidence_meter += 12
            call exp_o_meter(fill=confidence_meter)
            $ renpy.sound.play( "sounds/gasp.mp3")
            call cho_main("That's right!", "smile", "wide", "raised", "L")
            g4 "What?"
            call cho_main("Nobody knows what happens, there isn't any rule for it...", "open", "wide", "raised", "mid")
            g4 "Why wouldn't there be a rule for it?"
            call cho_main("Why would the defensive leave the pitch... they'd just leave the goal open...", "base", "base", "base", "L")
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
        call cho_main("Well sir, I thought for a minute that you only cared about basketball but it looks like I was wrong...", "smile", "wide", "raised", "mid")
        m "Of course, I am well versed in all sports. I just thought I'd teach you a thing or two."
        m "So, you will let me train you then?"
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
        
        hide screen cho_chang
        call cho_walk("mid","leave",2.5)
    else:
        call cho_main("You seem to care a lot about basketball sir but I'm not sure if you know that much about Quidditch...", "annoyed", "angry", "base", "downR")
        m "Or were you asking the wrong questions?"
        call cho_main("Sorry?", "open", "angry", "raised", "L")
        g9 "Time is just relative... what is the difference between a month or a few minutes really..."
        call cho_main("Sir, you got bunch of the questions wrong...", "upset", "angry", "raised", "L")
        m "The truth lies in the eyes of the beholder Miss Chang..."
        call cho_main("I don't...{nw=1.0}", "annoyed", "base", "base", "mid")
        m "You'll see, I'll show you the real truth..."
        m "(Once I can figure out what the fuck I'm doing)"
        call cho_main("...", "annoyed", "base", "base", "down")
        g9 "Next time..."
        call cho_main("Oh...", "open", "wide", "base", "mid")
        call cho_main("Good bye then...", "base", "base", "base", "mid")
    
        hide screen cho_chang
        call cho_walk("mid","leave",2.5)
    
        g4 "(What am I supposed to do now... I clearly don't know enough about Quidditch...)"
        m "(I’d rather not ask Snape... but unless there’s someone else that I could ask without sounding like a complete dumbass it might have to do...)"
        if store_intro_done:
            m "(Actually, perhaps the twins might be a better idea...)"
        $ cho_quiz_failed = True
            
    jump main_room
    
    