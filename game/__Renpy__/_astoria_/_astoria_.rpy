
    

label imperio_spell_3_training: #third level imperio spell #needs posing
    if astoria_spell_progress == 0:
        #talk about what it does new and about sitting on lap
        $ astoria_affection = 2
    if astoria_spell_progress < 3:
        jump astoria_spell_practice
        
    label imperio_spell_3_complete: #Jump here after last spell practice!
        
    #Unlocks spell 3.
    $ astoria_spells[0] = 3
    jump astoria_requests

label imperio_spell_3:

    $ astoria_affection = 3
    $ astoria_spell_progress = 0
    $ spells_locked #Locks spells until you send Astoria to tonks.
    
    jump day_main_menu
    
    
    
    
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
    


label astoria_spell_practice:
    show screen blkfade 
    with d3
    #$ renpy.call('astoria_lap_'+str(astoria_affection)+'_'+str(astoria_spell_progress))
    hide screen blkfade
    with d3
    $ astoria_spell_progress += 1
    $ astoria_busy = True
    return


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