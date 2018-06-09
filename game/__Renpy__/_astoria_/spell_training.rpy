

#Spell Training.
label astoria_spell_training:
    if astoria_spells[0] == 0 and astoria_affection == 0:
        jump imperio_spell_1_training
    elif astoria_spells[0] == 1 and astoria_affection == 1: #You have to try the spell once before you can train the next one.
        jump imperio_spell_2_training
    elif astoria_spells[0] == 2 and astoria_affection == 2: #You have to try the spell once before you can train the next one.
        jump imperio_spell_3_training
    elif astoria_affection >= 10: #ADD Max affection level.
        call nar(">There are currently no more spells to train!")
        jump astoria_requests
    else:
        call nar(">You haven't used your newest unlocked spell yet!\nYou should use it before training your next.")
        jump astoria_requests

        
        
label imperio_spell_1_training: #first level imperio spell #needs posing

    #Spell Intro.
    if astoria_spell_progress == 0:
        #talk about needing to practice the spell, what it does new and about sitting on lap
        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade")
        m "So I managed to get a book of brand new spells of an old friend of mine."
        m "Apparently he made them himself..."
        call ast_main("Really? So no one else knows them?","happy","base","base","mid")
        m "Not a soul."
        call ast_main("cool...","grin","happyCl","base","mid")
        call ast_main("So can I see it?","grin","angry","angry","mid")
        m "Sure, just come hop up on my lap and we can start reading it together."
        call ast_main("WHAT???","scream","wide","wide","wide")
        call ast_main("Why do I have to sit up on your lap?","open","angry","angry","mid")
        call ast_main("It was bad enough that you made me go hang out with that old hag...","disgust","angry","angry","R")
        call ast_main("Why can't I just use a chair?","disgust","angry","angry","mid")
        m "I only have one chair..."
        call ast_main("There is another chair right here! Dumby!!!","scream","wide","wide","mid")
        m "No that's..."
        m "My antique shelve..."
        g9 "Besides, it'll be fun!"
        call ast_main("Fun?","pout","angry","angry","mid")
        g9 "It'll be fun for me..."
        call ast_main("Ugh...","disgust","ahegao","ahegao","ahegao")
        call ast_main("At least tell me what the spell does and I'll decide...","open","closed","base","mid")
        m "OK, let me just open it up."
        call ctc
        
        call ast_main("","pout","narrow","narrow","mid")
        pause.5
        call nar(">You try to open the spell book only to find it doesn't budge.")
        m "(What gives?)"
        call ast_main("Come on, old man...","pout","narrow","narrow","L")
        m "I... can't open it..."
        call ast_main("What? You're not that weak are you, dumby?","tongue_silly","angry","angry","mid")
        m "I'm not a damn cripple!"
        call ast_main("Pffft, I think most cripples can open a book.","smile","base","base","mid")
        pause.8
        m "I think it's magically locked..."
        call ast_main("Really? It must be powerful then...","worried","wide","wide","wide")
        call ast_main("Does it say anything on the cover?","open","base","base","mid")      #need soggy to draw the book here
        m "No..."
        call ast_main("And on the back?","pout","base","base","R")
        m "Noth- no wait, there's a poem."
        call ast_main("What does it say, dumby!","grin","angry","angry","mid")
        m "When venus and mars meet, all my knowledge shall be at your feet..."
        call ast_main("What does that mean?!","open","wide","wide","mid")
        
        label astoria_book_question:
            menu:
                "-We have to be touching to open it-":
                    pass
                "-We have to wait until venus and mars are aligned-":
                    call ast_main("But that could take forever!","open","ahegao","ahegao","ahegao")
                    call ast_main("It's gotta be something else dumby!","pout","angry","angry","mid")
                    jump astoria_book_question
                "-We've gotta get some ancient gods to hook up-":
                    call ast_main("Stop being such a dumby!","pout","narrow","narrow","R")
                    jump astoria_book_question

        call ast_main("Oh... is that why you wanted me to sit on your lap?","disgust","base","base","down")
        m "o-of course... why else would I ask?"
        call ast_main("hmpf...","pout","angry","angry","R")
        call ast_main("well alright... Just don't try anything funny!","open","closed","base","mid")
        
        hide screen astoria_main
        hide screen bld1
        call blkfade
        
        call nar(">Astoria hops up onto your lap.")
        
        #Set up CG scene here.
        
        pause.5
        hide screen blkfade
        with fade
        
        ast "I guess this isn't too bad..."
        ast "Now let's open the book!"
        m "(Snape better not have booby trapped this...)"
        call nar("You and astoria each grab a side of the book, gently peeling the covers open.","start")
        call nar("As it opens you swear you heard a slow sexual moan eminate from between the covers...","end")
        ast "Did the book just moan?"
        m "I think so..."
        ast "Cool! All the scary spell books in the forbidden section of the library do to that too!"
        ast "Although they don't normally sound like this..."
        m "Let's just see what the first spell is shall we?"
        call nar(">Astoria slowly opens the book, turning it to the first spell she can find.")
        ast "\"imperio of the heart\""
        ast "Imperio?!?!"
        ast "Everyone and their dumb dog knows this one!"
        m "What's the heart mean?"
        ast "Who cares! This isn't secret at all!"
        m "Just wait a second now, lets at least read the first line."
        ast "Fine..."
        ast "\"Imperio of the heart is a forbidden variant of the unforgivable curse.\""
        ast "\"Whereas the regular imperio only allows control over the victims mind, imperio of the heart allows the caster-\""
        ast "\"to implant desires into the heart of their victim whilst leaving the mind untouched...\""
        ast "..."
        ast "What's that supposed to mean then Dumby?"
        m "I think it means you can make Susan want stuff."
        ast "Couldn't I do that with the regular spell?"
        m "I'm not sure..."
        m "Although when you cast it on her the other day she did seem to lose her free will."
        m "So maybe this lets her keep it?"
        ast "Hmmmm..."
        ast "So this spell lets us change what she wants? But not control her completely?"
        ast "That seems worse than the regular version!"
        m "Not if you want to hide the fact that you've cast it on her."
        ast "Ohhhh... so that means we can change stuff about her without her realising?"
        m "It would seem so."
        ast "That is cool!"
        ast "Maybe we could change her into a big slut who walks around school with her gross boobs hanging out."
        call nar(">You feel yourself starting to harden at the idea.")
        m "Hmmm..."
        ast "Dumby!!!"
        
        call blkfade
        
        call nar(">Astoria quickly hops off your lap in response.")
        
        #Hide CG scene.
        
        pause.5
        hide screen blkfade
        
        call ast_main("What the hell was that?!","scream","closed","angry","mid",trans="fade")
        m "I have no idea what you are talking about..."
        call ast_main("You better keep those nasty thoughts to yourself, old man!","scream","angry","angry","angry")
        call ast_main("Or you'll have to go and kiss that granny's feet yourself!","clench","angry","angry","angry")
        m "Fine... I'm sorry..."
        call ast_main("...","pout","angry","angry","R")
        
        hide screen bld1
        hide screen astoria_main
        call blkfade

        call nar(">Astoria hops back on to your lap.")
        
        #Set up CG scene.
        
        pause.5
        hide screen blkfade
        with fade
        
    if astoria_spell_progress < 3:
        call astoria_spell_practice
        if astoria_spell_progress < 3:
            jump day_main_menu
        
    ast "I think that was the last page."
    ast "Doesn't seem to complicated to me..."
    ast "Can we try it out on Susan?"
    m "I don't see why not."
    ast "YAY! You're the best teacher ever dumby!"
    m "and you're probably the worst student..."
    ast "Dumby!"
    m "Not that I mind..."
    
    call give_reward(">Congratulations! Astoria has learned a new spell!","images/store/astoria_unlock_02.png")
    
    call blkfade
    call nar("Astoria quickly hops off your lap.")
    
    #Hide CG scene.
    
    hide screen blkfade
    call ast_main("","grin","angry","angry","mid",xpos="base",ypos="base",trans="fade")
    
    #Unlocks spell 1.
    $ astoria_spells[0] = 1
    
    jump astoria_requests       #Astoria summon menu.
    
    
    
label imperio_spell_2_training: #second level imperio spell #needs posing
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        
        
        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade")
        m "ready to practice the next spell?"
        ast "Uh huh!"
        pass
        
    if astoria_spell_progress < 3:
        call astoria_spell_practice
        if astoria_spell_progress < 3:
            jump day_main_menu
        
    ast "I think that's it."
    ast "That really looks like a fun one, [ast_genie_name]!"
    ast "Can we try it out? Please!"
    m "Sure..."
    ast "YAY! You're the best!"
    
    call give_reward(">Congratulations! Astoria has learned a new spell!","images/store/astoria_unlock_02.png")
    
    call blkfade
    call nar("Astoria quickly hops off your lap.")
    
    #Hide CG scene.
    
    hide screen blkfade
    call ast_main("","smile","base","base","mid",xpos="base",ypos="base",trans="fade")
    
    #Unlocks Spell 2.
    $ astoria_spells[0] = 2
    
    jump astoria_requests       #Astoria summon menu.
    
    
    