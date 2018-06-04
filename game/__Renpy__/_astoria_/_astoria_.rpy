label astoria_spell_event: #have genie talk to astoria about which spell to cast



label imperio_spell_1: #first level imperio spell
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
        m "Noth- no wait, there's a poem."
        ast "What does it say dumby!"
        m "When venus and mars meet, all my knowledge shall be at your feet..."
        ast "what does that mean?"
        label astoria_book_question:
            menu:
                "-We have to be touching to open it-":
                    pass
                "-We have to wait until venus and mars are aligned-":
                    ast "That could take forever!"
                    ast "It's gotta be something else dumby!"
                    jump astoria_book_question
                "-We've gotta get some ancients gods to hook up-":
                    ast "Stop being such a dumby!"
                    jump astoria_book_question

        ast "Oh... is that why you wanted me to sit on your lap?"
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
        call nar(">Astoria quickly hops off your lap in response.")
        ast "Dumby!!!"
        m "Sorry... let's just keep reading then shall we?"
        ast "Alright... just try and keep those nasty thoughts to yourself from now on..."
        m "You said it!"
        ast "..."

        
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    ast "It's the end of the chapter!"
    ast "Can we try it out on Susan now?"
    m "I don't see why not."
    ast "YAY! You're the best teacher ever dumby!"
    m "and you're probably the worst student..."
    ast "Dumby!"
    m "Not that I mind..."
    ast "Good. Now Hurry up and bring her up here!"
    call nar(">You summon Susan up to your office.")
    sus "You wanted to see me sir-"
    sus "Astoria! What are you doing here!"
    sus "And why are you sitting on Dumbledore's lap?"
    ast "Because we were reading!"
    sus "I don't see why that makes it-"
    call nar(">With a quick flash, Astoria hops off your lap and pulls out her wand.")
    ast "Imperio Cor Meum!"
    sus "W-what are you-"
    call nar("A puff of orange smoke appears from the end of Astoria's wand, working it's way up into Susan's nose.")
    sus "-doing..."
    sus "..."
    ast "OK, so what should we do now?"
    m "You read the book as well didn't you?"
    ast "That was just on how to cast it Dumby!"
    ast "What should we make her want?"
    m "Hmmm?"
    m "How about making her want to strip?"
    ast "Dumby!"
    m "What? Didn't you already do that?"
    ast "I only made her take her top off."
    m "Ugh, fine... let's just go with that again."
    ast "OK..."
    ast "Susy, are you listening?"
    sus "yes..."
    ast "Good, I want you to pay attention."
    sus "..."
    ast "From now on you have an uncontrollable urge to show Dumby and I your boobs!"
    sus "My boobs? Ok..."
    ast "Alright, now wake up!"
    sus "I am awa-......"
    call nar(">Susan's body shifts a little as the life returns to her eyes.")
    sus "W-w-what happened?"
    sus "Weren't you sitting on Dumbledore's lap Astoria?"
    ast "No. Why would I sit on his gross old lap?!"
    m "Hey!"
    sus "You wouldn't..."
    sus "But there's something else."
    sus "I have to show you two something..."
    ast "reaaaally? And what's that Susy?"
    sus "I can't say... it's too-"
    sus "You have to close your eyes!"
    ast "How are you supposed to show us something with our eyes closed?"
    sus "I don't know! I-I-I-I have to show you my-"
    ast "Your what Susy?"
    sus "m-m-m-my..."
    pause
    sus "{size-=5}boobs...{/size}"
    show screen blkfade
    with d3
    call nar(">As susan finishes her sentence, her hands begin to slowly remove her shirt and vest in one smooth motion.")
    sus "Why do I..."
    hide screen blkfade
    with d3
    sus "..."
    call nar(">Susan stands in front of you and Astoria in only a bra, her eyes desperately trying to avoid yours.")
    sus "I-I-I'm sorry Professor Dumbledore, I don't know what's come over me..."
    sus "I'm Sorry you have to see this..."
    ast "See what Susy?"
    sus "My gross boobs..."
    ast "(I knew they were gross!)"
    ast "Well I don't think he can see them yet!"
    sus "WHAT?! Of course he can!"
    ast "Nuh-uh! You're still wearing a bra silly!"
    m "I have to agree with Miss Greengrass on this matter I'm afraid."
    m "A bra doesn't count."
    sus "Professor Dumbledore! How can you say something like that!"
    call nar(">As susan speaks her hands slowly slide up to her bra, gently undoing the clasp.")
    sus "You don't really expect me to show you both my breasts do you?"
    call nar(">Susan's bra slowly falls to the floor on top of her vest and shirt.")
    sus "!!!"
    g4 "{size+=10}Nice!{/size}"
    ast "Dumby!"
    m "What? You can't blame me for this!"
    ast "Not that! You're not supposed to think they're nice!"
    m "Why not?"
    ast "Because they're huge and soft and squishy and and and gross!"
    m "You're right about them looking huge and soft..."
    ast "Dumby!"
    sus "How can you two be so mean!"
    ast "Oh calm down Bessy!"
    sus "Bessy!? What's that supposed to mean?"
    ast "Pfft... you know."
    sus "How dare you!"
    sus "Are you just going to let her say that sir?"
    g4 "What's that? I was a little-ugh... distracted..."
    call nar(">Your eyes fall back down to Susan's heaving chest.")
    m "So big..."
    sus "..."
    ast "Alright, I think you're enjoying this a little too much Dumby..."
    m "Just a little longer..."
    ast "IMPERIO!"
    sus "W-w-what..."
    call nar(">A soft line of yellow smoke puffs from astoria's wand and into Susan's nose.")
    sus "..."
    ast "Get dressed Susy."
    sus "Alright..."
    call nar("Susan mechanically puts her clothes back on, her eyes staring blankly forward the entire time.")
    m "Aww... why'd you do that?"
    ast "You were getting too excited old man."
    m "So what?"
    ast "Well you can't go having too much fun, otherwise you'll never want to practice the new spells!"
    m "You could of at least made her dance or something..."
    ast "We could already do that!"
    m "Then why don't we?"
    ast "Because it's boring!"
    ast "I wanna learn more spells!"
    m "Ugh... fine..."
    ast "Good, I already read what the next one is called!"
    m "Really, what's that?"
    ast "Imperio of time..."
    ast "I didn't read what it does though..."
    m "Wanna start reading it now?"
    ast "It's a little late sir."
    ast "Besides, I better put bessy here back in her barn before people start to notice."
    m "Alright..."
    ast "Just let me know when you're ready to read the next chapter Dumby!"
    m "You got it."
    ast "Night dumby!"
    m "Good night Astoria."
    ast "Come on susy, go back to your room and go to sleep."
    sus "yes..."
    ast "(This is so much fun!)"



    $ astoria_affection = 1
    $ astoria_spells[0] = 1
    $ astoria_spell_progress = 0
    jump day_main_menu
label imperio_spell_2: #second level imperio spell
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    #Strip susan for genie

    $ astoria_affection = 2
    $ astoria_spells[0] = 2
    $ astoria_spell_progress = 0
    jump day_main_menu
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
    call nar("With a cheerful grin, astoria hops off your lap and out of your office.")
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
    call nar("With a sullen put, astoria hops off your lap and out of your office.")
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
    call nar("With tired face, astoria hops off of your lap and out of your office.")
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