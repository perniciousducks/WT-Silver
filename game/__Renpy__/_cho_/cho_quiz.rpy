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
    
    #python:
        #import random
        #trnd_type = random.randint(0, 4)
    
    add "interface/meter/bubble/"+str(type)+".png" ypos 100 xpos 100
    timer 1.0 action Hide("swear_bubble")
            
label cho_quiz_1:    
    call cho_chibi(xpos="mid")
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
        m "So as you can see, Basketball and Quidditch is pretty much the same game..."
        call cho_main("I’m sure that can’t be right...", "annoyed", "base", "base", "mid")
        call cho_main("I’ll have to look up this... basketball thing.", "open", "suspicious", "base", "mid")
        m "No need, I think I pretty much covered it."
        call cho_main("I do have to say Sir, I'm very impressed!", "smile", "base", "raised", "L")
        g4 "You are?"
        g9 "I mean, of course you are!"
        g9 "So, you will let me train you?"
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
        
        $ cho_quiz_assed = True

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