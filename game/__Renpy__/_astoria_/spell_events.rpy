





label susan_imperio:
    call ast_main("Alright, [ast_genie_name].","smile","base","base","mid")
    call ast_main("I will bring the [ast_susan_name]!","grin","angry","angry","mid")
    call blkfade
    
    call nar(">Astoria leaves to summon Susan.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Hello, Professor.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call sus_main("You wanted to see me?","upset","base","worried","down")
    
    m "Yes, Miss Bones, if you could just stand there in the middle while--"
    call ast_main("Wait a second, [ast_genie_name],...","scream","closed","base","mid",trans="hpunch")
    call ast_main("50 points, remember!","grin","angry","angry","mid")
    m "..."
    m "Right..."
    m "Alright... 50 points to \"Slytherin\"!"
    $ slytherin +=50
    call ast_main("Thank you!","grin","happyCl","base","mid")
    pause.5
    call blkfade
                    
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base") #uses the fade from the next line.
    hide screen blkfade
    call sus_main("What are you--","open","wide","worried","R",xpos="mid",ypos="base",trans="fade")
                    
    call cast_spell("imperio")
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")
                    
    show screen blktone
    call ast_main("[ast_susan_name], I command you to do whatever the old man tells you to do!")
    call sus_main("Of course, I will do whatever the old man sa--","open","base","base","up")
                    
    hide screen blktone
    call ast_main("All done, [ast_genie_name]! This will probably last a couple of days...","smile","base","base","R")
    call ast_main("You may leave now, [ast_susan_name]!","grin","happyCl","base","mid")
    call sus_main("Ok","base","base","base","up")
    hide screen susan_main
    with d3
                    
    $ susan_imperio_counter += 20 #Lasts 20 days.
    $ susan_imperio_influence = True
    $ spells_locked = True
                    
    call nar(">Susan is now under the influence of imperio.\n>The effect will last for 20 days.")
    jump astoria_requests
    
    
    
    
label imperio_spell_1:
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


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to tonks.
    
    $ astoria_affection = 1
    $ astoria_spell_progress = 0
    
    jump day_main_menu



        
label imperio_spell_2: #second level imperio spell #needs posing
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
    sus "What? Did you curse her too you evil little witch?"
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
    ast "See ya dumby! and don't forget that we've got a new spell to learn!"
    m "Can't we just do that one again?"
    ast "NO!"
    m "Fine... See you later..."
    call nar(">Astoria turns to leave your office, skipping cheerfully as she goes...")
    ast "(I can't believe that old man could cum so much...)"


    $ astoria_busy = True
    $ susan_busy = True
    $ spells_locked = True #Locks spells until you send Astoria to tonks.
    
    $ astoria_affection = 2
    $ astoria_spell_progress = 0
    
    jump day_main_menu
