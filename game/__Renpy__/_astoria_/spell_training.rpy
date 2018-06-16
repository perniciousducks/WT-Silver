

#Spell Training.
label astoria_spell_training:
    if astoria_spells[0] == 0 and astoria_affection == 0:
        jump imperio_spell_1_training
    elif astoria_spells[0] == 1 and astoria_affection == 1: #You have to try the spell once before you can train the next one.
        jump imperio_spell_2_training
    elif astoria_spells[0] == 2 and astoria_affection == 2: #You have to try the spell once before you can train the next one.
        jump imperio_spell_3_training
    elif astoria_affection >= 3: #ADD Max affection level.
        call nar(">There are currently no more spells to train!") from _call_nar_15
        jump astoria_requests
    else:
        call nar(">You haven't used your newest unlocked spell yet!\n>You should use it before training your next.") from _call_nar_16
        jump astoria_requests

        
        
label imperio_spell_1_training: #first level imperio spell

    #Spell Intro.
    if astoria_spell_progress == 0:
        #talk about needing to practice the spell, what it does new and about sitting on lap
        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade") from _call_ast_main
        m "So I managed to get a book of brand new spells of an old friend of mine."
        m "Apparently he made them himself..."
        call ast_main("Really? So no one else knows them?","happy","base","base","mid") from _call_ast_main_1
        m "Not a soul."
        call ast_main("cool...","grin","happyCl","base","mid") from _call_ast_main_2
        call ast_main("So can I see it?","grin","angry","angry","mid") from _call_ast_main_3
        m "Sure, just come hop up on my lap and we can start reading it together."
        call ast_main("WHAT???","scream","wide","wide","wide") from _call_ast_main_4
        call ast_main("Why do I have to sit up on your lap?","open","angry","angry","mid") from _call_ast_main_5
        call ast_main("It was bad enough that you made me go hang out with that old hag...","disgust","angry","angry","R") from _call_ast_main_6
        call ast_main("Why can't I just use a chair?","disgust","angry","angry","mid") from _call_ast_main_7
        m "I only have one chair..."
        call ast_main("There is another chair right here! Dumby!!!","scream","wide","wide","mid") from _call_ast_main_8
        m "No that's..."
        m "My antique shelve..."
        g9 "Besides, it'll be fun!"
        call ast_main("Fun?","pout","angry","angry","mid") from _call_ast_main_9
        g9 "It'll be fun for me..."
        call ast_main("Ugh...","disgust","ahegao","ahegao","ahegao") from _call_ast_main_10
        call ast_main("At least tell me what the spell does and I'll decide...","open","closed","base","mid") from _call_ast_main_11
        m "OK, let me just open it up."
        call ctc from _call_ctc_31
        
        call ast_main("","pout","narrow","narrow","mid") from _call_ast_main_12
        pause.5
        call nar(">You try to open the spell book only to find it doesn't budge.") from _call_nar_17
        m "(What gives?)"
        call ast_main("Come on, old man...","pout","narrow","narrow","L") from _call_ast_main_13
        m "I... can't open it..."
        call ast_main("What? You're not that weak are you, dumby?","tongue_silly","angry","angry","mid") from _call_ast_main_14
        m "I'm not a damn cripple!"
        call ast_main("Pffft, I think most cripples can open a book.","smile","base","base","mid") from _call_ast_main_15
        pause.8
        m "I think it's magically locked..."
        call ast_main("Really? It must be powerful then...","worried","wide","wide","wide") from _call_ast_main_16
        call ast_main("Does it say anything on the cover?","open","base","base","mid") from _call_ast_main_17      #need soggy to draw the book here
        m "No..."
        call ast_main("And on the back?","pout","base","base","R") from _call_ast_main_18
        m "Noth- no wait, there's a poem."
        call ast_main("What does it say, dumby!","grin","angry","angry","mid") from _call_ast_main_19
        m "When venus and mars meet, all my knowledge shall be at your feet..."
        call ast_main("What does that mean?!","open","wide","wide","mid") from _call_ast_main_20
        
        label astoria_book_question:
            menu:
                "-We have to be touching to open it-":
                    pass
                "-We have to wait until venus and mars are aligned-":
                    call ast_main("But that could take forever!","open","ahegao","ahegao","ahegao") from _call_ast_main_21
                    call ast_main("It's gotta be something else dumby!","pout","angry","angry","mid") from _call_ast_main_22
                    jump astoria_book_question
                "-We've gotta get some ancient gods to hook up-":
                    call ast_main("Stop being such a dumby!","pout","narrow","narrow","R") from _call_ast_main_23
                    jump astoria_book_question

        call ast_main("Oh... is that why you wanted me to sit on your lap?","disgust","base","base","down") from _call_ast_main_24
        m "o-of course... why else would I ask?"
        call ast_main("hmpf...","pout","angry","angry","R") from _call_ast_main_25
        call ast_main("well alright... Just don't try anything funny!","open","closed","base","mid") from _call_ast_main_26
        
        hide screen astoria_main
        hide screen bld1
        call blkfade from _call_blkfade_12
        
        call nar(">Astoria hops up onto your lap.") from _call_nar_18
        
        #Set up CG scene here.
        $ ccg_folder = "astoria_sit"
        $ ccg("e6","b3","m1")

        pause.5
        hide screen blkfade
        with fade
        
        ast "I guess this isn't too bad..."
        $ ccg("e3","b0","m0")
        ast "Now let's start reading!"
        m "(Snape better not have booby trapped this...)"
        call nar(">You and astoria begin to turn the pages together, words begining to manifest on the pages.","start") from _call_nar_19
        call nar(">As astoria flicks through the pages you hear a slow sexual moan eminate from between the covers...","end") from _call_nar_20
        $ ccg("e1","b1","m1")
        ast "Did the book just moan?"
        m "I think so..."
        $ ccg("e3","b0","m0")
        ast "Cool! All the scary spell books in the forbidden section of the library do to that too!"
        $ ccg("e0","b1","m3")
        ast "Although they don't normally sound like this..."
        m "Let's just see what the first spell is shall we?"
        call nar(">Astoria slowly opens the book, turning it to the first spell she can find.") from _call_nar_21
        $ ccg("e0","b0","m3")
        ast "\"imperio of the heart\""
        $ ccg("e1","b3","m1")
        ast "Imperio?!?!"
        $ ccg("e6","b3","m1")
        ast "Everyone and their dumb dog knows this one!"
        m "What's the heart mean?"
        $ ccg("e2","b3","m1")
        ast "Who cares! This isn't secret at all!"
        m "Just wait a second now, lets at least read the first line."
        $ ccg("e6","b1","m4")
        ast "Fine..."
        $ ccg("e0","b1","m4")
        ast "\"Imperio of the heart is a forbidden variant of the unforgivable curse.\""
        ast "\"Whereas the regular imperio only allows control over the victims mind, imperio of the heart allows the caster-\""
        ast "\"to implant desires into the heart of their victim whilst leaving the mind untouched...\""
        ast "..."
        $ ccg("e7","b1","m1")
        ast "What's that supposed to mean then Dumby?"
        m "I think it means you can make Susan want stuff?"
        $ ccg("e7","b2","m4")
        ast "Couldn't I do that with the regular spell?"
        m "I'm not sure..."
        m "Although when you cast it on her the other day she did seem to lose her free will."
        m "So maybe this lets her keep it?"
        $ ccg("e0","b1","m4")
        ast "Hmmmm..."
        $ ccg("e7","b1","m3")
        ast "So this spell lets us change what she wants? But not control her completely?"
        $ ccg("e7","b3","m1")
        ast "That seems worse than the regular version!"
        m "Not if you want to hide the fact that you've cast it on her."
        $ ccg("e0","b0","m0")
        ast "Ohhhh... so that means we can change stuff about her without her realising?"
        m "It would seem so."
        $ ccg("e3","b0","m1")
        ast "That is cool!"
        $ ccg("e3","b3","m2")
        ast "Maybe we could change her into a big slut who walks around school with her gross boobs hanging out."
        call nar(">You feel yourself starting to harden at the idea.") from _call_nar_22
        m "Hmmm..."
        $ ccg("e7","b4","m1")
        ast "Dumby!!!"
        
        call blkfade from _call_blkfade_13
        
        call nar(">Astoria quickly hops off your lap in response.") from _call_nar_23
        
        #Hide CG scene.
        hide screen ccg
        
        pause.5
        hide screen blkfade
        
        call ast_main("What the hell was that?!","scream","closed","angry","mid",trans="fade") from _call_ast_main_27
        m "I have no idea what you are talking about..."
        call ast_main("You better keep those nasty thoughts to yourself, old man!","scream","angry","angry","angry") from _call_ast_main_28
        call ast_main("Or you'll have to go and kiss that granny's feet yourself!","clench","angry","angry","angry") from _call_ast_main_29
        m "Fine... I'm sorry..."
        call ast_main("...","pout","angry","angry","R") from _call_ast_main_30
        
        hide screen bld1
        hide screen astoria_main
        call blkfade from _call_blkfade_14

        call nar(">Astoria hops back on to your lap.") from _call_nar_24
        
        $ astoria_spell_progress = 1
        
    if astoria_spell_progress < 4:
        call astoria_spell_practice from _call_astoria_spell_practice
        if astoria_spell_progress < 4:
            call play_sound("door") from _call_play_sound_38
            hide screen astoria_main
            hide screen bld1
            hide screen blkfade
            with fade
            
            if daytime:
                jump night_start
            else:
                jump day_start
        
    call ast_main("Don't worry, we can try it out later sir.","smile","base","base","mid") from _call_ast_main_31
    m "I look forward to it."
    m "Goodnight astoria."
    call ast_main("night dumby!","grin","closed","base","mid") from _call_ast_main_32
    hide screen astoria_main
    with d3
    pause.5
    
    call nar(">Astoria queitly walks out of your office, a small smirk forming in the corner of her mouth.") from _call_nar_25
    
    call give_reward(">Congratulations! Astoria has learned a new spell!","images/store/astoria_unlock_02.png") from _call_give_reward_1
    
    #Unlocks spell 1.
    $ astoria_spells[0] = 1
    
    if daytime:
        jump night_start
    else:
        jump day_start
        
    
label imperio_spell_2_training: #second level imperio spell
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        
        
        call ast_main("","smile","base","base","mid",xpos="right",ypos="base",trans="fade") from _call_ast_main_33
        m "ready to practice the next spell?"
        ast "Uh huh!"
        pass
        
        $ astoria_spell_progress = 1
        
    if astoria_spell_progress < 4:
        call astoria_spell_practice from _call_astoria_spell_practice_1
        if astoria_spell_progress < 4:
            call play_sound("door") from _call_play_sound_39
            hide screen astoria_main
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else:
                jump day_start
        
    call give_reward(">Congratulations! Astoria has learned a new spell!","images/store/astoria_unlock_02.png") from _call_give_reward_2
    
    #Unlocks Spell 2.
    $ astoria_spells[0] = 2
    
    if daytime:
        jump night_start
    else:
        jump day_start
        
    
label imperio_spell_3_training: #third level imperio spell
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        call ast_main("So are you ready to learn the final imperio spell, [ast_genie_name]?","grin","angry","angry","mid",xpos="right",ypos="base",trans="fade") from _call_ast_main_34
        m "Ready as I'll ever be..."
        
        $ astoria_spell_progress = 1
        
    if astoria_spell_progress < 4:
        call astoria_spell_practice from _call_astoria_spell_practice_2
        if astoria_spell_progress < 4:
            call play_sound("door") from _call_play_sound_40
            hide screen astoria_main
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else:
                jump day_start
        
    call give_reward(">Congratulations! Astoria has learned a new spell!","images/store/astoria_unlock_02.png") from _call_give_reward_3
    
    #Unlocks Spell 3.
    $ astoria_spells[0] = 3
    
    if daytime:
        jump night_start
    else:
        jump day_start
        
  
#susan event labels are on the other page.
label hornify_spell_1_training: #first level hornify spell
    #Start grinding her hips in front of genie
label hornify_spell_2_training: #second level hornify spell
    #Takes her top of and starts shaking her boobs for genie
label hornify_spell_3_training: #third level hornify spell
    #Plays with herself in front of astoria and genie


label slutify_spell_1_training: #first level sluttify spell
    #Underwear becomes slutty
label slutify_spell_2_training: #second level sluttify spell
    #Skirt becomes short, vest only and slutty Underwear
label slutify_spell_3_training: #third level sluttify spell
    #Pink heart dress and no underwear


label orgasmio_spell_1_training: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2_training: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3_training: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times
          
        
        
        
        
        
### SPELL PRACTICE / SIT ON LAP CG ###
label astoria_spell_practice:
    hide screen astoria_main
    hide screen bld1
    call blkfade from _call_blkfade_15
    
    #Set up CG scene here!
    $ ccg_folder = "astoria_sit"
    $ ccg("e6","b3","m1")

    hide screen blkfade
    with fade
    pause.8
    
    $ renpy.call('astoria_lap_sit_'+str(astoria_affection)+'_'+str(astoria_spell_progress))
    
    pause.8
    call blkfade from _call_blkfade_16
    
    #Hide CG scene here!
    hide screen ccg
    
    hide screen astoria_main
    hide screen bld1
    hide screen blkfade
    with fade
    
    $ astoria_spell_progress += 1
    $ astoria_busy = True
    
    return


#
label astoria_lap_sit_0_1:
    call nar(">Astoria lightly hops up onto your lap.") from _call_nar_26
    $ ccg("e6","b1","m3")
    ast "I suppose this isn't too bad..."
    $ ccg("e7","b0","m1")
    ast "At least your fat thighs are softer than the wood benches in the library..."
    m "Just start reading the spell..."
    $ ccg("e6","b1","m4")
    ast "Do I have to..."
    $ ccg("e0","b1","m4")
    ast "It looks kind of hard..."
    m "Didn't you beg me to teach you this sort of stuff?"
    $ ccg("e7","b4","m1")
    ast "I thought it would be easier than this dumby!"
    m "Tough..."
    $ ccg("e0","b1","m4")
    call nar(">You and Astoria spend the night pouring over the spell book, both of you talking about how you think it works...") from _call_nar_27
    call nar(">Your growing interest in the foreign magic distracts you from Asoria's incestant wiggling...") from _call_nar_28
    $ ccg("e2","b2","m1")
    ast "ah.... I think I better go to bed now dumby..."
    m "So soon? But we've still got so many pages left..."
    $ ccg("e7","b4","m1")
    ast "Tough!"
    m "Oh alright... I might stay up a little longer then..."
    ast "Don't read ahead!"
    m "Fine..."
    $ ccg("e7","b0","m1")
    ast "Good... Night dumby!"
    
    call nar("With a cheerful grin, astoria hops off your lap and out of your office.") from _call_nar_29
    
    return
    
label astoria_lap_sit_0_2:
    call nar(">Astoria lightly hops up onto your lap.") from _call_nar_30
    $ ccg("e7","b1","m3")
    ast "Do I really have to sit here?"
    m "Is it that bad?"
    $ ccg("e6","b1","m4")
    ast "I guess not..."
    $ ccg("e7","b1","m3")
    ast "But can't you just get another chair?"
    m "There's the one next to the fire."
    $ ccg("e6","b1","m1")
    ast "That wood one?"
    $ ccg("e7","b4","m1")
    ast "It looks so uncomfortable!"
    m "well then you'll just have to make do with my lap."
    $ ccg("e2","b4","m1")
    ast "Fine!"
    call nar(">You and Astoria spend the night reading over the spell, both of you silently reading along...") from _call_nar_31
    $ ccg("e0","b0","m0")
    ast "next page!"
    m "Already? I've still got a few lines left..."
    $ ccg("e7","b4","m0")
    ast "Ugh! You're such a slow reader dumby!"
    m "You're right... It must be because it's so late..."
    $ ccg("e7","b2","m1")
    ast "Can't we keep going?"
    m "Not if you expect me to keep up..."
    $ ccg("e2","b4","m4")
    ast "*hmph* I'm not going to put up with your slowness old man..."
    ast "I may as well go to bed."
    $ ccg("e6","b4","m4")
    ast "night dumby..."
    call nar("With a sullen put, astoria hops off your lap and out of your office.") from _call_nar_32
    
    return
    
label astoria_lap_sit_0_3:
    call nar(">Astoria lightly hops up onto your lap.") from _call_nar_33
    $ ccg("e7","b0","m1")
    ast "Can we start reading now?"
    m "Ready when you are."
    $ ccg("e0","b0","m1")
    ast "Good... I can't wait to learn a {b}fun{/b} spell."
    $ ccg("e7","b4","m1")
    ast "Do you know what your stupid school tried to teach me today?"
    m "I have no idea..."
    $ ccg("e6","b4","m4")
    ast "They insisted I learn spells for locating the nearest dragons..."
    ast "You even have to specify which type!"
    $ ccg("e7","b4","m1")
    ast "When am I ever going to use that?"
    m "When you're looking for a pile of gold?"
    $ ccg("e7","b4","m4")
    ast "..."
    $ ccg("e7","b1","m4")
    ast "Just open the book dumby."
    call nar(">You and Astoria read the book long into the night, occasionaly asking the other questions...") from _call_nar_34
    $ ccg("e0","b2","m0")
    ast "ugh... that's the end of the spell..."
    $ ccg("e7","b0","m1")
    ast "should we bring susan up here?"
    m "probably not... it's getting a little late..."
    $ ccg("e7","b4","m1")
    ast "Can't we do it now?"
    m "I don't think she'll be up."
    $ ccg("e6","b2","m4")
    ast "alright... we can try it out on her later..."
    $ ccg("e7","b2","m3")
    ast "goodnight dumby..."
    m "goodnight astoria."
    call nar("With tired face, astoria hops off of your lap and out of your office.") from _call_nar_35
    
    return
    
    
    
#
label astoria_lap_sit_1_1:
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.") from _call_nar_36
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.") from _call_nar_37
    $ ccg("e0","b1","m1")
    ast "According to the guide, this one is called imperio tempus..."
    $ ccg("e7","b0","m0")
    ast "It allows us to permanently set commands for the person we curse..."
    m "That seems useful!"
    $ ccg("e7","b0","m2")
    ast "And fun!"
    $ ccg("e0","b1","m1")
    ast "Hmmm... This one seems a lot harder than the last one though..."
    m "Do you think you'll be able to cast it?"
    $ ccg("e7","b4","m1")
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly pour over the book, your eyes occasionaly drifting shut...") from _call_nar_38
    $ ccg("e7","b4","m1")
    ast "Wake up dumby!"
    m "I'm up!"
    $ ccg("e7","b4","m4")
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    $ ccg("e7","b4","m1")
    ast "Well stop it!"
    $ ccg("e0","b1","m4")
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    $ ccg("e7","b1","m4")
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    $ ccg("e6","b4","m4")
    ast "Pfft, figures."
    $ ccg("e7","b4","m1")
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.") from _call_nar_39

    return
    
label astoria_lap_sit_1_2:
    call nar(">Astoria slowly hops up onto your lap, quietly opening the book.") from _call_nar_40
    $ ccg("e0","b2","m3")
    m "What's the matter? You seem a little tired."
    $ ccg("e7","b4","m1")
    ast "Am not!"
    $ ccg("e6","b1","m4")
    ast "I just had a long day is all..."
    ast "Ms Sprout made us spend all day plucking mandrakes to make juice..."
    $ ccg("e2","b4","m1")
    ast "They're really hard to pull out!"
    m "I bet..."
    m "If you're feeling tired, we can go through this tomorrow."
    $ ccg("e7","b4","m1")
    ast "I'm not tired!"
    m "If you say so..."
    call nar(">You begin to read over the complex spell, Astoria taking far longer to read through the pages...") from _call_nar_41
    $ ccg("e2","b1","m4")
    ast "..."
    m "Are you ready to read the next page?"
    $ ccg("e0","b1","m4")
    ast "yea..."
    $ ccg("e2","b2","m3")
    call nar(">As you turn the page you start to feel Astoria's body go limp on your lap.") from _call_nar_42
    m "Hmmm, poor little thing..."
    call nar(">You nudge astoria on the back slightly.") from _call_nar_43
    $ ccg("e5","b4","m4")
    ast "W-what... Keep your hands of me old man!"
    m "Pfft... I think it's time you went to bed."
    $ ccg("e2","b2","m1")
    ast "I told you, I'm not *yawn* tired..."
    m "..."
    $ ccg("e6","b2","m4")
    ast "Fine... we can keep reading tomorrow I guess."
    $ ccg("e7","b2","m4")
    ast "Night dumby..."
    m "Goodnight Astoria."
    call nar("With tired expression, astoria hops off of your lap and slowly out of your office.") from _call_nar_44
    
    return
    
label astoria_lap_sit_1_3: 
    call nar(">Astoria effortlessly hops up onto your lap, eager to start reading the final parts of the spell.") from _call_nar_45
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's go! We're almost done!"
    m "Alright..."
    call nar("You and Astoria turn to one of the last pages and start reading over where you left off.") from _call_nar_46
    $ ccg("e0","b1","m4")
    ast "Hmmm... we might need to go back a little bit..."
    m "Why?"
    $ ccg("e6","b1","m4")
    ast "I don't really remember this..."
    $ ccg("e3","b1","m5")
    ast "I might have fallen asleep last time..."
    m "I thought you weren't tired?"
    $ ccg("e6","b4","m1")
    ast "Shut up dumby, no one likes a smarty pants!"
    m "You're telling me..."
    call nar(">You and Astoria turn back a few pages and continue reading...") from _call_nar_47
    $ ccg("e1","b0","m2")
    ast "That's it!"
    m "Finally..."
    $ ccg("e7","b4","m1")
    ast "*hmph* we would have been done faster if you didn't ask me what every second word meant!"
    m "I'm just testing you..."
    $ ccg("e6","b4","m4")
    ast "Pfft!"
    $ ccg("e7","b4","m1")
    ast "I don't even know how you got to be headmaster here without knowing what wingardium leviosa does..."
    m "Uhhh, my work here's mostly administrative..."
    ast "Administering your grossness on the other girls more like!"
    m "Speaking of which... How about we get susan bones up here?"
    $ ccg("e7","b5","m1")
    ast "At this hour?"
    $ ccg("e7","b4","m1")
    ast "I don't think so dumby..."
    m "ugh... fine..."
    call nar("Astoria hops off of your lap.") from _call_nar_48
    
    return

    
    
#
label astoria_lap_sit_2_1:
    call nar(">Astoria quickly hops up onto your lap.") from _call_nar_49
    $ ccg("e7","b0","m1")
    ast "Let's go dumby!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the final version of the imperio spell.") from _call_nar_50
    $ ccg("e1","b0","m1")
    ast "wow... this one gives us complete control over someone..."
    m "How's that different from the regular one?"
    $ ccg("e7","b4","m1")
    ast "You know how dumby! regular imperio only controls someone's mind..."
    ast "And it doesn't last forever..."
    $ ccg("e1","b1","m1")
    ast "Apparently this one allows us to change how they \'perceive the world\'..."
    $ ccg("e6","b0","m1")
    ast "Whatever that means... plus it lasts forever!"
    m "So basically it allows us to do anything with susan..."
    $ ccg("e7","b4","m1")
    ast "Anything I want!"
    m "Don't I get a-"
    $ ccg("e3","b0","m0")
    ast "Nope! Now let's keep reading..."
    call nar(">You and Astoria star to pour over the book, astoria seeming to need to reread several pages to fully understand them...") from _call_nar_51
    $ ccg("e0","b1","m4")
    ast "This seems pretty hard..."
    $ ccg("e2","b1","m4")
    ast "I wish my Latin were better."
    m "Here, I'll read it for you."
    $ ccg("e7","b5","m1")
    ast "You can read Latin?"
    m "Of course! I was there when they invented it!"
    $ ccg("e3","b5","m0")
    ast "Wow... you really are old!"
    m "More than you know..."
    $ ccg("e6","b0","m1")
    ast "Well you can read it to me later, I promised Pansy I'd hang out tonight."
    m "alright then..."
    call nar("You close the book as astoria hops off of your lap and out of your office.") from _call_nar_52
    
    return
    
label astoria_lap_sit_2_2:
    call nar(">Astoria hops up onto your lap, wiggling her little butt as she settles in.") from _call_nar_53
    $ ccg("e7","b0","m1")
    ast "Come on Dumby, let's finish this spell so we can try it already!"
    $ ccg("e3","b0","m1")
    ast "I've even been practicing my Latin!"
    m "*yawn* old on a second..."
    $ ccg("e7","b4","m4")
    ast "What's wrong dumby, you're not going to fall asleep are you?"
    m "No... It's just Ms Granger has been tiring me out a little..."
    $ ccg("e7","b5","m1")
    ast "Hermione? You don't mean..."
    m "Forget I said anything."
    $ ccg("e6","b1","m4")
    ast "Hmmm, alright... let's just read the book old man."
    call nar(">You and astoria start to read over the complex spell. Your knowledge of latin proving essential to the small witch's understanding.") from _call_nar_54
    $ ccg("e7","b4","m1")
    ast "That's not a real word!"
    m "Yes it is..."
    $ ccg("e6","b4","m4")
    ast "Pffft... whoever made this dumb language is dumber than you dumby!"
    m "Ugh..."
    call nar(">You and astoria return to the book...") from _call_nar_55
    $ ccg("e0","b4","m1")
    ast "ugh... whoever wrote this book has terrible handwriting!"
    m "alright, I think we better call it there for tonight."
    $ ccg("e7","b4","m1")
    ast "*hmph* What? Why?!"
    m "I think someone's a little overtired..."
    $ ccg("e2","b4","m1")
    ast "I am not!"
    $ ccg("e7","b4","m1")
    ast "You're overtired!"
    m "Ugh, well either way, we can keep reading this later..."
    $ ccg("e6","b4","m3")
    ast "fine... but you're the one with the problem!"
    m "...."
    $ ccg("e2","b4","m4")
    call nar("With pouty face, astoria hops off of your lap and out of your office.") from _call_nar_56
    
    return
    
label astoria_lap_sit_2_3: 
    call nar(">Astoria leaps into your lap as if you were santa claus at christmas time...") from _call_nar_57
    $ ccg("e7","b0","m1")
    ast "Let's go dumby! We're almost at the end!"
    m "Almost..."
    $ ccg("e0","b0","m0")
    call nar(">You and Astoria turn to bookmarked page and start reading over the final pages of the spell.") from _call_nar_58
    $ ccg("e3","b0","m0")
    ast "Wow... I think I'm finally getting good at Latin!"
    m "You're alright..."
    $ ccg("e3","b0","m2")
    ast "I'm the best!"
    m "Ugh..."
    m "Well come on then, why don't you read the next page out loud then?"
    $ ccg("e6","b4","m1")
    ast "Fine!"
    call nar(">You and Astoria slowly read over the next few pages, Astoria stumbling over every second word...") from _call_nar_59
    $ ccg("e3","b0","m2")
    ast "Done! I told you I was the best Dumby!"
    m "You sure showed me..."
    $ ccg("e6","b4","m4")
    ast "*hmph*"
    m "Want to practice it now?"
    $ ccg("e7","b4","m1")
    ast "We would have been able to if you had been able to read the last page in less than an hour!"
    $ ccg("e6","b2","m3")
    ast "It's too late now..."
    m "You read the last page!"
    $ ccg("e2","b4","m1")
    ast "Well it doesn't matter now anyways, I wanna go to bed."
    m "Fine... I suppose it is getting a little late."
    $ ccg("e7","b0","m0")
    ast "At least you can read a clock!"
    call nar(">With a teasing look on her face, astoria hops off of your lap and out of your office.") from _call_nar_60
    
    return
    
    