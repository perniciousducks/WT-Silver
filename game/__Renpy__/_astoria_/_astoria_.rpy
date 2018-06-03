label astoria_spell_event: #have genie talk to astoria about which spell to cast



label imperio_spell_1: #third level imperio spell
    if astoria_spell_progress == 0:
        #talk about needing to practice the spell, what it does new and about sitting on lap
        m "So I managed to get a book of brand new spells of an old friend of mine."
        m "Apparently he made them himself..."
        ast "Really? So no one else knows them?"
        m "Not a soul."
        ast "cool..."
        ast "So can I see it?"
        m "Sure, just come hop up on my lap and we can start reading it together."
        ast "WHAT???"
        ast "Why do I have to sit up on your lap?"
        ast "It was bad enough that you made me go hang out with that old hag, tonks..."
        m "(so that's her name...)"
        ast "Why can't I just use a chair?"
        m "Well there aren't many chairs in here..."
        m "And besides, it'll be fun!"
        ast "Fun?"
        m "it'll be fun for me..."
        ast "Ugh..."
        ast "At least tell me what the spell does and I'll decide..."
        m "OK, let me just open it up."
        call nar(">You try to open the spell book only to find it doesn't budge.")
        m "(What gives?)"
        ast "Come on old man!"
        m "I can't open it..."
        ast "What? You're not that weak are you dumby?"
        m "I'm not a damn cripple!"
        ast "Pffft, I think most cripples can open a book."
        m "I think it's magically locked..."
        ast "Really? It must be powerful then..."
        ast "Does it say anything on the cover?" #need soggy to draw the book here
        m "No."
        ast "The back?"
        m "There's a poem."
        ast "What does it say dumby!"
        m "When venus and mars meet, all my knowledge shall be at your feet..."
        ast "what does that mean?"
        jump astoria_book_question
        menu:
            "-We have to be touching to open it-":
                pass
            "-We have to wait until venus and mars are aligned-"

        ast "Oh... is that why you want me to sit on your lap?"
        m "o-of course... why else would I ask?"
        ast "hmmm...."
        ast "well alright... Just don't try anything funny!"
        call nar(">Astoria hops up onto your lap.")
        ast "I guess this isn't too bad..."
        ast "Now let's open the book!"
        m "(Snape better not have booby trapped this...)"
        call nar("You and astoria each grab a side of the book, gently peeling the covers open.")
        call nar("As it opens you swear you heard a slow sexual moan eminate from between the covers...")
        ast "Did the book just moan?"
        m "I think so..."
        ast "Cool! All the scary spell books in the forbidden section of the library to that too..."
        ast "Although they don't normally sound like that."
        
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    #expose boobs to genie
    $ astoria_spells[0] = 1
    $ astoria_spell_progress = 0
label imperio_spell_2: #third level imperio spell
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        $ astoria_affection = 1
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    #Strip susan for genie
    $ astoria_spells[0] = 2
    $ astoria_spell_progress = 0
label imperio_spell_3: #third level imperio spell
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        $ astoria_affection = 2
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    #Strip susan for genie
    if astoria_spells[0] == 2:
        $ astoria_spell_progress = 0
        $ astoria_spells[0] = 3
    #humiliate self for genie and astoria


label hornify_spell_1: #first level hornify spell
    #Start grinding her hips in front of genie
label hornify_spell_2: #second level hornify spell
    #Takes her top of and starts shaking her boobs for genie
label hornify_spell_3: #third level hornify spell
    #Plays with herself in front of astoria and genie


label slutify_spell_1: #first level sluttify spell
    #Underwear becomes slutty
label slutify_spell_2: #second level sluttify spell
    #Skirt becomes short, vest only and slutty Underwear
label slutify_spell_3: #third level sluttify spell
    #Pink heart dress and no underwear


label orgasmio_spell_1: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times




label astoria_tonks_event: #send astoria to go see tonks



label astoria_tonks_1: #First time astoria sent to tonks
    #Astoria says tonks just asked her a few questions
    #Stuff like her interests and age, what subjects she likes, etc
    #Astoria not sure why she had to spend time with tonks
    #Said that there was an almost hungry look in her eyes
    #Says she's unsure if she wants to see her anymore
    ">Your door swings open as Astoria enters."
    m "Oh, you're back!"
    ast "Are you surprised Dumby?"
    m "A little... She does seem a bit weird."
    ast "Then why would you send me there?!"
    m "eh..."
    ast "..."
    ast "Well it wasn't too bad..."
    ast "She only wanted to ask a few questions."
    m "What sort of questions?"
    ast "My favourite subjects, what I like, how old I am, stuff like that."
    m "That's it? She didn't ask you to do anything weird?"
    ast "Not really..."
    ast "Although she did have this look in her eyes... It was almost like she wanted to eat me..."
    ast "She's not a werewolf is she Dumby?"
    m "Holy shit! Are werewolves real here?"
    ast "What do you mean here? Of course werewolves are real... We all learn that as children."
    m "Just testing..."
    m "Oh, and I'm sure she's not a werewolf..."
    m "(I hope...)"
    ast "She better not be dumby!"
    m "I'm sure you'll get used to her."
    ast "Get used to her????"
    ast "I don't have to see her again do I?"
    m "Well... If you want to keep learning new spells you might have to..."
    ast "*hmph* you haven't even taught me any yet!"
    ast "They're probably not even fun..."
    m "Why don't you come over here then and we can start reading over the first one."
    ast "alright..."
    jump astoria_learn_spell

    
label astoria_tonks_2:
    #Astoria comes back and talks to genie
    #says tonks asked her more questions about school life
    #Says tonks talked about her uniform
    #Stuff like tonks thinks it's a little conservative
    #Astoria asking what genie thinks she means by that
    #Genie tells her not to worry about it and sends her on her way
    
label astoria_tonks_3:
    
label astoria_tonks_4:
    
label astoria_tonks_5:
    
label astoria_tonks_6:
    


label astoria_learn_spell: #Astoria spell learning loop
    if astoria_spells[0] == 0:
        jump imperio_spell_1
    elif astoria_spells[0] == 1:
        jump imperio_spell_2
    else:
        jump imperio_spell_3

label astoria_spell_practice:
    show screen blkfade 
    with d3
    $ renpy.call('astoria_lap_'+str(astoria_affection)+'_'+str(renpy.random.randint(1, 3)))
    hide screen blkfade
    with d3
    $ astoria_spell_practice =+ 1
    $ astoria_busy = True
    jump day_main_menu


#
label astoria_lap_sit_0_1:
    call nar(">Astoria lightly hops up onto your lap.")
    ast "I suppose this isn't too bad..."
    ast "At least your fat thighs are softer than the wood benches in the library..."
    m "Just start reading the spell..."
    ast "Do I have to..."
    ast "It looks kind of hard..."
    m "Didn't you beg me to teach you this sort of stuff?"
    ast "I thought it would be easier than this dumby!"
    m "Tough..."
    call nar(">You and Astoria spend the night pouring over the spell book, both of you talking about how you think it works...")
    call nar(">Your growing interest in the foreign magic distracts you from Asoria's incestant wiggling...")
    ast "ah.... I think I better go to bed now dumby..."
    m "So soon? But we've still got so many pages left..."
    ast "Tough!"
    m "Oh alright... I might stay up a little longer then..."
    ast "Don't read ahead!"
    m "Fine..."
    ast "Good... Night dumby!"
    call nar("With a cheerful grin, astoria hops of your lap and out of your office.")
    return
label astoria_lap_sit_0_2:
    call nar(">Astoria lightly hops up onto your lap.")
    ast "Do I really have to sit here?"
    m "Is it that bad?"
    ast "I guess not..."
    ast "But can't you just get another chair?"
    m "There's the one next to the fire."
    ast "That wood one?"
    ast "It looks so uncomfortable!"
    m "well then you'll just have to make do with my lap."
    ast "Fine!"
    call nar(">You and Astoria spend the night reading over the spell, both of you silently reading along...")
    ast "next page!"
    m "Already? I've still got a few lines left..."
    ast "Ugh! You're such a slow reader dumby!"
    m "You're right... It must be because it's so late..."
    ast "Can't we keep going?"
    m "Not if you expect me to keep up..."
    ast "*hmph* I'm not going to put up with your slowness old man..."
    ast "I may as well go to bed."
    ast "night dumby..."
    call nar("With a sullen put, astoria hops of your lap and out of your office.")
    return
label astoria_lap_sit_0_3: 
    call nar(">Astoria lightly hops up onto your lap.")
    ast "Can we start reading now?"
    m "Ready when you are."
    ast "Good... I can't wait to learn a {b}fun{/b} spell."
    ast "Do you know what your stupid school tried to teach me today?"
    m "I have no idea..."
    ast "They insisted I learn spells for locating the nearest dragons..."
    ast "You even have to specify which type!"
    ast "When am I ever going to use that?"
    m "When you're looking for a pile of gold?"
    ast "..."
    ast "Just open the book dumby."
    call nar(">You and Astoria read the book long into the night, occasionaly asking the other questions...")
    ast "ugh... that's the end of the page..."
    ast "should we stop here?"
    m "probably... it's getting a little late..."
    ast "Can't we keep going?"
    ast "alright... we can catch up on this later..."
    ast "goodnight dumby..."
    m "goodnight astoria."
    call nar("With tired face, astoria hops of your lap and out of your office.")
    return

#
label astoria_lap_sit_1_1:
    
    return
label astoria_lap_sit_1_2:
    
    return
label astoria_lap_sit_1_3: 
    
    return

#
label astoria_lap_sit_2_1:
    
    return
label astoria_lap_sit_2_2:
    
    return
label astoria_lap_sit_2_3: 
    
    return