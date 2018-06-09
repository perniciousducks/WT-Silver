label astoria_spell_event: #have genie talk to astoria about which spell to cast



label imperio_spell_1: #first level imperio spell #needs posing
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
    ast "Pfft... you know..."
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
    ast "Imperio tempus..."
    ast "I didn't see what it could do though..."
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



label imperio_spell_2: #second level imperio spell #needs posing
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        m "ready to practice the next spell?"
        ast "Uh huh!"
        pass
        
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
    ast "Are you finally ready to try out the new spell Dumby?"
    m "You bet!"
    ast "Awesome, I can't wait to see the look on Susan's dumb face..."
    m "Let me just bring her up here."
    call nar(">You summon Susan up to your office.")
    sus "You wanted to see me sir?"
    sus "Astoria? What are you doing here?"
    ast "Oh... no reason..."
    sus "Is there something wrong Professor?"
    m "As a matter of fact there is..."
    sus "R-really? Is this about me returning my books to the library a day late?"
    sus "I swear it won't happen again!"
    m "What? No, I'm afraid there's an issue with your uniform..."
    sus "Oh... Is it because I'm not wearing the school robe?"
    sus "I can wear it from now on if you like!"
    m "Actually, Wearing too many clothes is the problem."
    sus "W-w-what???"
    sus "You can't be serious sir!"
    m "I am Ms bones... Hiding away those glorious milk duds of yours is a serious offense!"
    ast "(Pffft, gloriously gross)"
    sus "Professor Dumbledore! How can you say something like that!"
    sus "I think I better go..."
    call nar(">Susan turns to leave your office, but as soon as she turns her back, Astoria is a flurry of motion.")
    ast "Imperio Tempus!"
    call nar("A flash of purple smoke erupts from Astoria's wand and flies towards Susan.")
    sus "What is-"
    sus "..."
    ast "hahahaha"
    ast "Her face was priceless when you said milk duds..."
    m "You liked that?"
    ast "Of course! Anything to bring Bessy here down a peg."
    ast "Although you said that before I cast Imperio on her, so we might have to obliviate that if we want to keep this a secret."
    m "Yeah sure..."
    m "(What in the hells is obliviate?)"
    ast "So what should we make her do today Dumby?"
    m "Well, if the books to be believed, this spell should let us change something about her permanently."
    ast "Hmmm... I know!"
    ast "Lets make her forget everything that happens in this room as soon as she leaves!"
    ast "That way we don't have to worry about her tattling on us."
    m "Good thinking boy wonder."
    ast "..."
    m "But is that all we're going to change about her?"
    m "Can't we do something a little more... adventurous?"
    ast "You mean like making her show you her milk duds?"
    m "Well if you insist..."
    ast "ugh... you're such a filthy pervert dumby!"
    m "we can do something else if you-"
    ast "I didn't say no..."
    m "Oh... well how about you make it so-"
    ast "I get to choose dumby!"
    m "What? Why?"
    ast "Because it's my spell and my wand!"
    ast "Not to mention you'd probably do something over the top and gross..."
    m "Probably..."
    m "So what's your plan?"
    ast "Just wait and see old man!"
    ast "Susan, listen up!"
    sus "Yes..."
    ast "From now on, you'll no longer remember anything that happens in this office."
    sus "Ok..."
    m "Is that all?"
    ast "Shush old man, I'm not done yet!"
    ast "You'll also get an uncontrollable urge to take your top off whenever you see Dumby and I together, OK?"
    sus "yes..."
    m "Nice! But won't she just run away from now on?"
    ast "Hmmm, you're probably right..."
    ast "Last of all, you're not allowed to leave this office until I say so OK Susy?"
    sus "yes astoria..."
    ast "Awesome! Now wake up Bessy!"
    sus "..."
    call nar(">The colour slowly returns to Susan's eyes...")
    sus "ugh..."
    sus "What happened?"
    ast "Nothing Susy, Dumbledore was just explaining how your uniform wasn't up to scratch."
    sus "My uniform... You're right... Too many clothes..."
    sus "I need to take off my top..."
    ast "Mhmm, that's right susy... Why don't you show old dumby here your gross boobs..."
    sus "B-b-b-but he's so old..."
    ast "That's right... Only a nasty slut would show their boobs to such a wrinkly old man..."
    m "Hey!"
    ast "Shhh dumby, don't ruin my fun!"
    m "Fine..."
    sus "I-i-i-i'm not a slut..."
    ast "well I'm sure you'll be able to keep your top on then susy..."
    sus "I... There's something wrong sir!"
    sus "I can't help it..."
    call nar(">Tears begin to form in Susan's eyes as she slowly removes her top, exposing her veluptous chest...")
    g4 "Nice!"
    call nar(">Your hands unconciously drop to your rock hard cock and start to pump away as you gaze at the redheads embarressed form.")
    ast "Dumby! Are you touching yourself?"
    m "Ugh... I can't help it..."
    m "It's not everyday you get to see a rack like this..."
    ast "Well stop it! It's gross!"
    m "Alri-"
    sus "Please sir... it's too much!"
    sus "It's bad enough I have to show you my breasts..."
    ast "Wait..."
    ast "Keep going dumby!"
    m "What?"
    sus "What?"
    ast "Well if bessy here hates it... Then I love it!"
    ast "Besides, it's not like I can see anything under the desk."
    m "So you're OK with this?"
    ast "Mhmmm, just don't expect me to touch it old man!"
    sus "I'm not OK with this!"
    ast "Tough! No one asked you slut!"
    sus "I am not a slut!"
    ast "ha! You're standing here, letting old man dumbledore oggle your fat tits while he jerks his wrinkly old cock!"
    ast "If that's not a slut then I don't know what is!"
    sus "I-i-i-i-i don't know why I'm doing this..."
    sus "You probably cursed me!"
    ast "Duh!"
    sus "well stop it!"
    ast "Nuh!"
    sus "Please astoria..."
    call nar(">You start to zone out the two girls argument as you focus in on Susan's heaving boosom...")
    g4 "Ugh yeah... that's it..."
    ast "You can leave once old dumby here's done."
    sus "What? you mean I have to wait until he..."
    sus "This is unbelievable!"
    sus "I'm going to report both of you to the ministry of magic!"
    sus "My aunt is an auror you know!"
    ast "yeah... I've met your creepy old aunt."
    sus "What? Did you curse her two you evil little witch?"
    ast "I wish..."
    sus "Well she's going to lock both of you away in azkaban!"
    sus "You'll never see me or anyone else again..."
    ast "Ha!"
    sus "and you dumbledore! I hope you enjoy wanking that nasty cock of yours because it'll be the last time you ever get to!"
    g4 "Ugh yeah... say that again..."
    sus "Ugh! You're both sick!"
    g4 "mmm, keep shaking those tits of yours..."
    g4 "Almost there {b}slut!{/b}"
    sus "I am not a {size+=10}slut!{/size}"
    call nar(">As susan yells at the top of her voice, the effort causes her gigantic tits to rise and slap back together.")
    g4 "{size+=10}HERE IT COMES!{/size}"
    call nar(">The sight proves to much as your cock explodes, audibly painting the bottom of your desk in a thick layer of cum.")
    g4 "{size+=10}AHHH... YESS!!!!{/size}"
    ast "Woah... I didn't think you'd have that much in you dumby..."
    sus "{size+=10}Hmph! I hope you Enjoy azkaban perverts!{/size}"
    call nar(">With Susan's curse broken by your colossal ejaculation, she turns and runs out of your office, her shirt in hand...")
    m "Ugh... should we stop her?"
    ast "It's fine dumby, I made it so she forgets everything that happens in here, remember?"
    m "Oh... yeah..."
    ast "Well I'll let you clean up..."
    m "mmmm"
    ast "See ya dumby!, don't forget that we've got a new spell to learn!"
    m "Can't we just do that one again?"
    ast "NO!"
    m "Fine... See you later..."
    call nar(">Astoria turns to leave your office, skipping cheerfully as she goes...")
    ast "(I can't believe that old man could cum so much...)"



    $ astoria_affection = 2
    $ astoria_spells[0] = 2
    $ astoria_spell_progress = 0
    jump day_main_menu


label imperio_spell_3: #third level imperio spell #needs posing
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



label astoria_tonks_1: #First time astoria sent to tonks #needs posing
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
    $ renpy.call('astoria_lap_'+str(astoria_affection)+'_'+str(astoria_spell_progress))
    hide screen blkfade
    with d3
    $ astoria_spell_progress =+ 1
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
    ast "ugh... that's the end of the spell..."
    ast "should we bring susan up here?"
    m "probably not... it's getting a little late..."
    ast "Can't we do it now?"
    m "I don't think she'll be up."
    ast "alright... we can try it out on her later..."
    ast "goodnight dumby..."
    m "goodnight astoria."
    call nar("With tired face, astoria hops off of your lap and out of your office.")
    return

#
label astoria_lap_sit_1_1:
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.")
    ast "According to the guide, this one is called imperio tempus..."
    ast "It allows us to permanently set commands for the person we curse..."
    m "That seems useful!"
    ast "And fun!"
    ast "Hmmm... This one seems a lot harder than the last one though..."
    m "Do you think you'll be able to cast it?"
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly poor over the book, your eyes occasionaly drifting shut...")
    ast "Wake up dumby!"
    m "I'm up!"
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    ast "Well stop it!"
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    ast "Pfft, figures."
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.")

    return
label astoria_lap_sit_1_2:
    call nar(">Astoria slowly hops up onto your lap, quietly opening the book.")
    m "What's the matter? You seem a little tired."
    ast "Am not!"
    ast "I just had a long day is all..."
    ast "Ms Sprout made us spend all day plucking mandrakes to make juice..."
    ast "They're really hard to pull out!"
    m "I bet..."
    m "If you're feeling tired, we can go through this tomorrow."
    ast "I'm not tired!"
    m "If you say so..."
    call nar(">You begin to read over the complex spell, Astoria taking far longer to read through the pages...")
    ast "..."
    m "Are you ready to read the next page?"
    ast "yea..."
    call nar(">As you turn the page you start to feel Astoria's body go limp on your lap.")
    m "Hmmm, poor little thing..."
    call nar(">You nudge astoria on the back slightly.")
    ast "W-what... Keep your hands of me old man!"
    m "Pfft... I think it's time you went to bed."
    ast "I told you, I'm not *yawn* tired..."
    m "..."
    ast "Fine... we can keep reading tomorrow I guess."
    ast "Night dumby..."
    m "Goodnight Astoria."
    call nar("With tired expression, astoria hops off of your lap and slowly out of your office.")
    return
label astoria_lap_sit_1_3: 
    call nar(">Astoria effortlessly hops up onto your lap, eager to start reading the final parts of the spell.")
    ast "Come on Dumby, let's go! We're almost done!"
    m "Alright..."
    call nar("You and Astoria turn to one of the last pages and start reading over where you left off.")
    ast "Hmmm... we might need to go back a little bit..."
    m "Why?"
    ast "I don't really remember this..."
    ast "I might have fallen asleep last time..."
    m "I thought you weren't tired?"
    ast "Shut up dumby, no one likes a smarty pants!"
    m "You're telling me..."
    call nar(">You and Astoria turn back a few pages and continue reading...")
    ast "That's it!"
    m "Finally..."
    ast "*hmph* we would have been done faster if you didn't ask me what every second word meant!"
    m "I'm just testing you..."
    ast "Pfft!"
    ast "I don't even know how you got to be headmaster here without knowing what wingardium leviosa does..."
    m "Uhhh, my work here's mostly administrative..."
    ast "Administering your grossness on the other girls more like!"
    m "Speaking of which... How about we get susan bones up here?"
    ast "At this hour?"
    ast "I don't think so dumby..."
    m "ugh... fine..."
    call nar("Astoria hops off of your lap.")
    ast "Don't worry, we can try it out later sir."
    m "I look forward to it."
    m "Goodnight astoria."
    ast "night dumby!"
    call nar(">Astoria queitly walks out of your office, a small smirk forming in the corner of her mouth.")
    return

#
label astoria_lap_sit_2_1:
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.")
    ast "Hmmm... This one seems a lot harder than the last one..."
    m "Do you think you'll be able to cast it?"
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly poor over the book, your eyes occasionaly drifting shut...")
    ast "Wake up dumby!"
    m "I'm up!"
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    ast "Well stop it!"
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    ast "Pfft, figures."
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.")
    return
label astoria_lap_sit_2_2:
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.")
    ast "Hmmm... This one seems a lot harder than the last one..."
    m "Do you think you'll be able to cast it?"
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly poor over the book, your eyes occasionaly drifting shut...")
    ast "Wake up dumby!"
    m "I'm up!"
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    ast "Well stop it!"
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    ast "Pfft, figures."
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.")
    return
label astoria_lap_sit_2_3: 
<<<<<<< HEAD
    call nar(">Astoria excitedely hops up onto your lap, eager to start reading.")
    ast "Come on Dumby, let's start reading it already!"
    m "Alright..."
    call nar("You and Astoria turn to the page and start reading over the new spell.")
    ast "Hmmm... This one seems a lot harder than the last one..."
    m "Do you think you'll be able to cast it?"
    ast "Of course dumby! It'll just take me a while to learn it is all..."
    m "Good..."
    call nar(">You and Astoria slowly poor over the book, your eyes occasionaly drifting shut...")
    ast "Wake up dumby!"
    m "I'm up!"
    ast "*hmph* I bet your too busy thinking about Susan's gross boobs aren't you!"
    m "I am now..."
    ast "Well stop it!"
    ast "You should be focusing on the spell, this part seems pretty hard..."
    m "Ugh, can we continue this tomorrow?"
    ast "What's a matter dumby? Are you all tuckered out from sitting in your chair all day?"
    m "As a matter of fact I am."
    ast "Pfft, figures."
    ast "Well get some rest old man, I expect you to start pulling your weight next time!"
    m "ugh..."
    call nar("With teasing face, astoria hops off of your lap and out of your office.")
    return
=======
    
    return
    
    
    
    
    
    
    
label set_ast_susan_name:
    if one_of_ten == 1:
        $ ast_susan_name = "Susy"
    if one_of_ten == 2:
        $ ast_susan_name = "Cow"
    if one_of_ten == 3:
        $ ast_susan_name = "Cow Tits"
    if one_of_ten == 4:
        $ ast_susan_name = "Milk Bag"
    if one_of_ten == 5:
        $ ast_susan_name = "Slut"
    if one_of_ten == 6:
        $ ast_susan_name = "Whore"
    if one_of_ten == 7:
        $ ast_susan_name = "Piggy"
    if one_of_ten == 8:
        $ ast_susan_name = "Pig"
    if one_of_ten == 9:
        $ ast_susan_name = "Bessie"
    if one_of_ten == 10:
        $ ast_susan_name = "Moo Moo"
    
    return
    
    
label set_ast_tonks_name:
    if one_of_five == 1:
        $ ast_tonks_name = "Hag"
    if one_of_five == 2:
        $ ast_tonks_name = "Old Hag"
    if one_of_five == 3:
        $ ast_tonks_name = "Punk"
    if one_of_five == 4:
        $ ast_tonks_name = "Dyke"
    if one_of_five == 5:
        $ ast_tonks_name = "Lesbo"
        
    return
    
>>>>>>> 1ee2d884f937be58592a3372b3896fea4ba7112c
