

label nothing_to_see_here_048:
    m "Now did you manage to win today's game?"
    call cho_main("...", "annoyed", "narrow", "worried", "downR")
    call cho_main("No...", "open", "narrow", "worried", "down")
    m "You didn't? Why not?"
    m "Wasn't your skirt distracting enough?"
    call cho_main("It wasn't that...", "annoyed", "narrow", "worried", "downR")
    call cho_main("If anything went wrong it's that my skirt was too distracting!", "annoyed", "narrow", "angry", "R")
    m "How's that? Don't you want the other players distracted?"
    call cho_main("I do...", "quiver", "narrow", "worried", "R")
    call cho_main("But this was too much!","scream","closed","angry","mid")
    call cho_main("I couldn't get them off of me!", "open", "narrow", "angry", "R")
    call cho_main("Half the slytherin team spent the whole game following me around, trying to get a peak from underneath!", "scream", "narrow", "angry", "mid")
    m "Hmmm, I was worried this might happen...."
    call cho_main("Well how are you going to fix it then, [cho_genie_name]?", "annoyed", "narrow", "angry", "mid")


label nothing_to_see_here_049:
    call play_sound("door")
    call cho_main("", "annoyed", "narrow", "angry", "R",xpos="close",ypos="base")
    pause.1
    call play_sound("bump")
    pause.5
    call cho_main("", "annoyed", "narrow", "angry", "mid",xpos="mid",ypos="base",trans=fade)
    pause.3
    call cho_main("[cho_genie_name]! It's not fair!", "scream", "narrow", "worried", "mid", trans=hpunch)
    call cho_main("Malfoy's pompous old man just bought the whole Slytherin' team brand new Nimbus 2018s!","scream","closed","angry","mid")
    call cho_main("Ravenclaw can't be expected to win against that!", "angry", "narrow", "angry", "downR")
    call cho_main("I demand you level the playing field, [cho_genie_name]!", "scream", "narrow", "angry", "mid")
    m "Why? Is that crooked as well?"
    call cho_main("This isn't funny, [cho_genie_name]! With Slytherin playing dirty there's no way we can win!", "open", "narrow", "worried", "R")
    call cho_main("Ugh! I knew you wouldn't do anything...", "annoyed", "narrow", "angry", "mid")
    m "So you don't want to hear my solution then?"
    call cho_main("Wait... You are going to help?!", "smile", "wide", "worried", "mid")
    call cho_main("Thank you, thank you, thank you!","smile","closed","base","mid")
    call cho_main("I take a small size broom and I'd like gold trim with a dark-","open","base","base","R")
    m "I'm not buying you a broom..."
    m "(Is quidditch like curling then?)"
    call cho_main("Oh...", "annoyed", "wide", "worried", "downR")
    call cho_main("Then what's your solution?","open","narrow","angry","mid")
    m "You said that the Slytherins were playing dirty..."
    m "How about you fight fire with fire then?"
    call cho_main("So you think we should fight dirty too?","horny","narrow","base","mid")
    call cho_main("But how? The rules forbid almost all foul play.", "annoyed", "narrow", "worried", "downR")
    m "Hmmmm..."
