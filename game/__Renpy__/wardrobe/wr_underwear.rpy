#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

### Equip Bra ###
label equip_bra:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_bra
    #Luna
    if active_girl == "luna":
        jump equip_lun_bra
    #Susan
    if active_girl == "susan":
        jump equip_sus_bra


### Equip Hermione's Bra ###
label equip_her_bra:
    if underwear_choice == h_bra:
        $ hide_transitions = True
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif her_mood >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ hide_transitions = False #activates dissolve in her_main
            $ hermione_xpos = 665

            #Bras
            if underwear_choice in ["bra_base"]:
                m "Would you wear this bra for me?"
                if her_whoring >= 11: #Success
                    if her_whoring < 17:
                        call her_main("Of course, [genie_name].","base","glance")
                    else:
                        call her_main("That old thing?","disgust","down")
                        call her_main("It looks so mundane...","annoyed","down")
                        call her_main("Do I really have to wear this?","soft","base")
                        m "Yep..."
                        call her_main("Fine... Let me put it on real quick.","base","baseL")
                else: #Fail
                    call her_main("No, [genie_name]!","open","closed")
                    m "Why not?"
                    call her_main("Why not?!","shock","wide")
                    call her_main("Why would you even requests something like that from one of your students?","angry","angry")
                    call her_main("I see no reason why I should ever change my bra for you...","open","closed")
                    call her_main("(Disgusting...)","annoyed","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_lace","bra_silk"]:
                g9 "Do you like this bra I bought you?"
                if her_whoring >= 11: #Success
                    if her_whoring < 17:
                        call her_main("Hmm...","annoyed","down")
                        call her_main("It looks decent enough...","annoyed","down_raised")
                        call her_main("Alright, I'll wear it.","open","baseL")
                        call her_main("Give me a second to put it on.","base","base")
                    else:
                        call her_main("Of course, [genie_name]! I love that one!","grin","closed")
                        call her_main("It's so soft and comfy!","grin","base")
                        call her_main("Let me put it on for you.","base","glance")
                else: #Fail
                    if her_whoring < 5:
                        call her_main("A bra?","shock","shocked")
                        call her_main("Why on earth would you buy me a bra, [genie_name]?","disgust","down")
                        m "So you can... uhm... wear it?"
                        call her_main("Wear it? Are you out of your mind?","angry","angry")
                        call her_main("I'm your student! Don't ever request something like that again!","angry","angry")
                        m "Fine. Forget about it..."
                        call her_main("(Bloody pervert...)","annoyed","angry")
                    else:
                        call her_main("No, [genie_name]!","annoyed","closed")
                        m "Why not? It's a really nice one!"
                        m "And it's so soft..."
                        m "I'd wear it myself but I lack the tits..."
                        call her_main("(Disgusting perv...)","clench","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_bikini","bra_bikini_string"]:
                m "[hermione_name], do you like wearing bikinis?"
                if her_whoring >= 14: #Success
                    if her_whoring < 20:
                        call her_main("If I have to.","soft","baseL")
                        g9 "Great! That's good enough for me!"
                        call her_main("(I hope I won't regret this...)","disgust","down")
                    else:
                        call her_main("Of course!","grin","happyCl")
                        m "Really?"
                        call her_main("Of course, I sometimes do sun-bathing during break-time.","open","closed")
                        call her_main("I'll just lie down in the grass and unwind for a bit. I'll even take off my top at times so I won't get any tan-lines!","smile","base")
                        call her_main("I'm always attracting a crowd... Seems like the boys quite like ogling at me.","base","glance")
                else: #Fail
                    call her_main("Bikinis?","soft","wink")
                    call her_main("I mostly wear a bathing-suit when I'm out swimming.","open","baseL")
                    call her_main("Why do you ask, [genie_name]?","base","base")
                    m "I would like you to wear one."
                    call her_main("At school? [genie_name], we don't even have swimming lessons here.","open","wide_stare")
                    m "Swimming lessons, hmm."
                    m "Do you think something like that could be arranged? Down at the lake?"
                    call her_main("The lake? That water is way too cold to swim in, [genie_name]! Especially in a bikini!","disgust","base")
                    m "Right then, I'll think of another school activity we could do in a bikini."
                    call her_main("There are none, [genie_name]...","annoyed","angry")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 14."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_latex"]:
                g9 "[hermione_name], I have a new bra for you!"
                if her_whoring >= 17: #Success
                    call her_main("Oh wow...","soft","down")
                    call her_main("And you'd like me to wear it?","open","base")
                    m "Yes please."
                    call her_main("Very well...","base","baseL")
                    call her_main("Anything for you, [genie_name].","base","glance")
                else: #Fail
                    if her_whoring < 8:
                        call her_main("What? [genie_name] why would you give me a bra?","shock","shocked")
                        m "So you can wear it for me?"
                        call her_main("No! I'm not going to wear bras for you!","angry","angry")
                        call her_main("What is this even made of? I's so rubbery...","disgust","down")
                        m "It's-"
                        call her_main("I don't care! You can have it back!","open","closed")
                        m "Fine. Maybe another time then..."
                        call her_main("(Weirdo...)","annoyed","angryL")
                    elif her_whoring < 11:
                        call her_main("Please, [genie_name]...","open","closed")
                        call her_main("Stop buying me bras...","annoyed","angry")
                        m "Don't you like them?"
                        call her_main("That doesn't matter, [genie_name]. Bras aren't appropriate gifts for students!","annoyed","angry")
                        m "Well if you don't like gifts... I will just keep it."
                    else:
                        call her_main("No, [genie_name]. They are way too sexual!","open","angry")
                        g4 "What? How could you say such a thing?"
                        m "That bra is perfectly fine!"
                        call her_main("Where did you even get this one? From an adult shop?","annoyed","angry")
                        g4 "That's none of your concern!"
                        call her_main("Tzzz!","clench","angryCl")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_french_maid"]:
                m "[hermione_name], I bought a new bra for you."
                if her_whoring >= 20: #Success
                    m "I'd like you to wear it!"
                    call her_main("Of course, [genie_name].","base","glance")
                    m "You don't mind wearing this, even in classes?"
                    call her_main("Why? Oh right, the holes...","soft","down")
                    call her_main("I can just cover myself with some books if I have to...","open","closed")
                    call her_main("(Not that I'd want to!)","base","ahegao")
                else: #Fail
                    if her_whoring < 8:
                        call her_main("What? [genie_name] why would you give me a bra?","shock","shocked")
                        m "So you could wear it for me?"
                        call her_main("No! I'm not going to wear bras for you!","angry","angry")
                        m "But this one has those pretty frills!"
                        call her_main("I don't care! You can keep it!","open","closed")
                        m "Fine. Maybe another time then..."
                        call her_main("(Pervert...)","annoyed","angryL")
                    elif her_whoring < 14:
                        call her_main("Please, [genie_name]...","open","closed")
                        call her_main("Stop buying me bras...","annoyed","angry")
                        m "Don't you like them?"
                        call her_main("That doesn't matter, [genie_name]. Bras aren't appropriate gifts for students!","annoyed","angry")
                        m "Well if you don't like gifts... I will just keep it."
                    else:
                        call her_main("No, [genie_name]. They are way too sexual!","open","angry")
                        g4 "What? How could you say such a thing?"
                        m "That bra is perfectly normal!"
                        call her_main("There is a giant hole in it!","scream","angryCl")
                        m "Okay, fine... No need to scream."
                        m "I see your point."
                        call her_main("Tzzz!","clench","angryCl")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe

            elif underwear_choice in ["bra_tape"]:
                m "[hermione_name], could you take off your bra for me? And then put these over your nipples."
                if her_whoring >= 20: #Success
                    call her_main("Pasties?... My tits might as well be completely exposed if I were to wear those...","soft","down")
                    g9 "Just leaving enough to the imagination!"
                    call her_main("Hmm... I can already see the boys imagine doing all kinds of things with them...","open","ahegao")
                    call her_main("They always tell me how great my breasts look!","base","glance")
                else: #Fail
                    if her_whoring < 11:
                        call her_main("Do you ask this from every girl, [genie_name]?","open","wink")
                        m "Why uhm... I mean yes. All the girls..."
                        call her_main("Is this some sort of protection for-","open","down")
                        call her_main("It's those Blast-Ended Skrewts again, isn't it?!","soft","wide",trans="hpunch")
                        call her_main("[genie_name], are they biting off the student's nipples???","open","wide_stare")
                        m "What's so bad about biting nipples?"
                        call her_main("[genie_name], these are some serious matters! We immediately have to inform the other teachers about this issue!","open","angry")
                        m "What?! No just put on the pasties!"
                        call her_main("I'm sorry, [genie_name], but this protection tape won't be enough! Hagrid can't let students handle those horrible creatures again!","open","closed")
                        call her_main("Here, you can have these back. I'll have the situation settled by tomorrow! You can count on me.","base","angry")
                        m "Damn it..."
                    else:
                        call her_main("You want me to put these bits of tape on my tits?","open","angryCl")
                        call her_main("That's ridiculous!","scream","angry")
                        m "What's so bad about it? Your breasts are covered..."
                        call her_main("It would look as if I had a target on them!","disgust","down")
                        call her_main("No!... And you can have your disgusting duct tape back...","annoyed","angry")
                        m "Hey! No need to insult duct tape... It's like magic..."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe

            elif underwear_choice in ["top_fishnets_1"]:
                g9 "I've got something for you! Try it out!"
                if her_whoring >= 20: #Success
                    call her_main("Wow. Fishnets?","smile","down")
                    call her_main("That's so naughty!","grin","glance")
                    g9 "Glad you like it!"
                    call her_main("I do, [genie_name]!","soft","baseL")
                    call her_main("Let me take off my bra and put these on instead.","base","glance")
                else: #Fail
                    if her_whoring < 5:
                        call her_main("What? Oh, what's this?","soft","base")
                        m "It's a fishnet to-"
                        call her_main("Oh, I get it!","grin","down")
                        call her_main("This isn't really a hobby I considered pursuing, [genie_name]...","open","baseL")
                        call her_main("But if you say it would help me with my grades then I'll try my best.","soft","down")
                        m "Wait, what?"
                        call her_main("I will go down to the lake later and try it out, if that's ok with you, [genie_name].","base","glance")
                        m "(...)"
                        m "(Wait, is she expecting to catch fish with it...?)"
                    else:
                        call her_main("Another one of your way too revealing tops?","disgust","angry")
                        g9 "Yes, but I want you to wear it as a bra!"
                        call her_main("What?!","open","wide")
                        call her_main("But you can see everything in this! My nipples would poke right through it!!!","scream","angryCl")
                        m "I wouldn't mind if they did..."
                        call her_main("That's just... typical!","clench","angry")
                        call her_main("You disgust me, [genie_name]!","clench","angry")
                        m "Okay- Jeesh... I'm sorry."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe



            call set_her_bra(underwear_choice)

            call her_main(xpos="wardrobe")
            $ hide_transitions = 1
            call screen wardrobe

        else:
            $ hide_transitions = True

            #Fails
            if her_whoring < 11 and underwear_choice in ["bra_base","bra_lace","bra_silk"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 11."
                jump return_to_wardrobe

            if her_whoring < 14 and underwear_choice in ["bra_bikini","bra_bikini_string"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 14."
                jump return_to_wardrobe

            if her_whoring < 17 and underwear_choice in ["bra_latex"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 17."
                jump return_to_wardrobe

            if her_whoring < 20 and underwear_choice in ["bra_french_maid","bra_tape","top_fishnets_1"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 20."
                jump return_to_wardrobe

            #Success!
            call set_her_bra(underwear_choice)

            call her_main(xpos="wardrobe")
            hide screen wardrobe
            call screen wardrobe




### Equip Luna's Bra ###
label equip_lun_bra:
    call set_lun_bra(underwear_choice)

    jump return_to_wardrobe

### Equip Susan's Bra ###
label equip_sus_bra:
    call set_sus_bra(underwear_choice)

    jump return_to_wardrobe

### Equip Onepiece ###
label equip_onepiece:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_onepiece
    #Luna
    if active_girl == "luna":
        jump equip_lun_onepiece
    #Susan
    if active_girl == "susan":
        jump equip_sus_onepiece

### Equip Hermione's OnePiece/Nighty ###
label equip_her_onepiece:
    call set_her_onepiece(underwear_choice)

    jump return_to_wardrobe

### Equip Luna's OnePiece/Nighty ###
label equip_lun_onepiece:
    call set_lun_onepiece(underwear_choice)

    jump return_to_wardrobe

### Equip Susan's OnePiece/Nighty ###
label equip_sus_onepiece:
    call set_sus_onepiece(underwear_choice)

    jump return_to_wardrobe

### Equip Panties ###
label equip_panties:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_panties
    #Luna
    if active_girl == "luna":
        jump equip_lun_panties
    #Susan
    if active_girl == "susan":
        jump equip_sus_panties

### Equip Hermione's Panties ###
label equip_her_panties:
    if underwear_choice == h_panties:
        $ hide_transitions = True
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif her_mood >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ hide_transitions = False #activates dissolve in her_main
            $ hermione_xpos = 665

            #Bras
            if underwear_choice in ["panties_base"]:
                m "Could you wear your normal panties again for me?"
                if her_whoring >= 11: #Success
                    if her_whoring < 17:
                        call her_main("Of course, [genie_name].","base","glance")
                    else:
                        call her_main("These old things?","disgust","down")
                        call her_main("They look so boring...","annoyed","down")
                        call her_main("Do I really have to?","soft","base")
                        m "Yep..."
                        call her_main("Fine... Let me put them on real quick.","base","baseL")
                else: #Fail
                    call her_main("No, [genie_name]!","open","closed")
                    m "Why not?"
                    call her_main("Why not?!","shock","wide")
                    call her_main("Why would you even requests something like that from one of your students?","angry","angry")
                    call her_main("I see no reason why I should ever change my panties for you...","open","closed")
                    call her_main("(Disgusting...)","annoyed","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["panties_lace","panties_silk","panties_silk_low"]:
                g9 "Do you like these panties I bought you?"
                if her_whoring >= 11: #Success
                    if her_whoring < 17:
                        call her_main("Hmm...","annoyed","down")
                        call her_main("They looks decent enough...","annoyed","down_raised")
                        call her_main("Fine, I'll wear them.","open","baseL")
                        call her_main("Give me a second to put them on.","base","base")
                    else:
                        call her_main("Of course, [genie_name]! I love those!","grin","closed")
                        call her_main("They're so soft and comfy!","grin","base")
                        call her_main("Let me put them on for you.","base","glance")
                else: #Fail
                    if her_whoring < 5:
                        call her_main("Panties?!","shock","shocked")
                        call her_main("Why on earth would you buy me panties, [genie_name]?","disgust","down")
                        m "So you can... uhm... wear them?"
                        call her_main("Wear them? Are you out of your mind?","angry","angry")
                        call her_main("I'm your student! Don't ever request something like that again!","angry","angry")
                        m "Fine. Forget about it..."
                        call her_main("(Damn perv...)","annoyed","angry")
                    else:
                        call her_main("No, [genie_name]!","annoyed","closed")
                        m "Why not? They're really nice and soft!"
                        m "I'd wear it myself but I lack a great ass..."
                        call her_main("(Disgusting perv...)","clench","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            elif underwear_choice in ["panties_bikini","panties_bikini_string"]:
                m "[hermione_name], do you like wearing bikinis?"
                if her_whoring >= 14: #Success
                    if her_whoring < 20:
                        call her_main("If I have to.","soft","baseL")
                        g9 "Great! That's good enough for me!"
                        call her_main("(I hope I won't regret this...)","disgust","down")
                    else:
                        call her_main("Of course!","grin","happyCl")
                        m "Really?"
                        call her_main("Yeah I sometimes do sun-bathing during break-time.","open","closed")
                        call her_main("I'll just lie down in the grass and unwind for a bit. I'll even take off my top at times so I won't get any tan-lines!","smile","base")
                        call her_main("I'm always attracting a crowd... Seems like the boys quite like ogling at me.","base","glance")
                else: #Fail
                    call her_main("Bikinis?","soft","wink")
                    call her_main("I mostly wear a bathing-suit when I'm out swimming.","open","baseL")
                    call her_main("Why do you ask, [genie_name]?","base","base")
                    m "I would like you to wear one."
                    call her_main("At school? [genie_name], we don't even have swimming lessions here.","open","wide_stare")
                    m "Swimming lessions, hmm."
                    m "Do you think something like that could be arranged? Down at the lake?"
                    call her_main("The lake? That water is way too cold to swim in, [genie_name]! Especially in a bikini!","disgust","base")
                    m "Right then, I'll think of another school activity we could do in a bikini."
                    call her_main("There are none, [genie_name]...","annoyed","angry")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 14."
                    jump return_to_wardrobe

            elif underwear_choice in ["panties_latex"]:
                g9 "[hermione_name], I have some new panties for you!"
                if her_whoring >= 17: #Success
                    call her_main("Oh wow...","soft","down")
                    call her_main("And you'd like me to wear them?","open","base")
                    m "Yes please."
                    call her_main("Very well...","base","baseL")
                    call her_main("Anything for you, [genie_name].","base","glance")
                else: #Fail
                    if her_whoring < 8:
                        call her_main("What? [genie_name] why would you give me panties?","shock","shocked")
                        m "So you can wear them for me?"
                        call her_main("No! I'm not going to wear panties for you!","angry","angry")
                        call her_main("What are these panties even made of? They're so rubbery...","disgust","down")
                        m "It's-"
                        call her_main("I don't care! You can have them back!","open","closed")
                        m "Fine. Maybe another time then..."
                        call her_main("(Pervert...)","annoyed","angryL")
                    elif her_whoring < 11:
                        call her_main("Please, [genie_name]...","open","closed")
                        call her_main("Stop buying me panties...","annoyed","angry")
                        m "Don't you like them?"
                        call her_main("That doesn't matter, [genie_name]. Panties aren't appropriate gifts for students!","annoyed","angry")
                        m "Well if you don't like gifts... I will just keep them."
                    else:
                        call her_main("No, [genie_name]. They are way too perverted!","open","angry")
                        g4 "What? How could you say such a thing?"
                        m "Those panties is perfectly normal!"
                        call her_main("Where did you even get this one? From an adult shop?","annoyed","angry")
                        g4 "That's none of your concern!"
                        call her_main("Tzzz!","clench","angryCl")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 17."
                    jump return_to_wardrobe

            elif underwear_choice in ["panties_french_maid"]:
                m "[hermione_name], I bought some new panties for you."
                if her_whoring >= 20: #Success
                    m "I'd like you to wear them."
                    call her_main("Of course, [genie_name].","base","glance")
                    m "Really? You don't mind wearing them, even in classes?"
                    call her_main("Why? Oh right, there is a hole in it...","soft","down")
                    call her_main("I can just cover myself with some books if I have to...","open","closed")
                    call her_main("(Not that I'd want to!)","base","ahegao")
                else: #Fail
                    if her_whoring < 8:
                        call her_main("What? [genie_name] why would you give me panties?","shock","shocked")
                        m "So you could wear them for me?"
                        call her_main("No! I'm not going to wear panties for you!","angry","angry")
                        m "But this one has those pretty frills!"
                        call her_main("I don't care! You can keep them!","open","closed")
                        m "Fine. Maybe another time then..."
                        call her_main("(Pervert...)","annoyed","angryL")
                    elif her_whoring < 14:
                        call her_main("Please, [genie_name]...","open","closed")
                        call her_main("Stop buying me panties...","annoyed","angry")
                        m "Don't you like them?"
                        call her_main("That doesn't matter, [genie_name]. Panties aren't appropriate gifts for students!","annoyed","angry")
                        m "Well if you don't like gifts... I will just keep them."
                    else:
                        call her_main("No, [genie_name]. They are way too sexual!","open","angry")
                        g4 "What? How could you say such a thing?"
                        m "Those panties is perfectly normal!"
                        call her_main("There is a giant hole in it!","scream","angryCl")
                        m "Okay, fine... No need to scream."
                        m "I see your point."
                        call her_main("Tzzz!","clench","angryCl")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe

            elif underwear_choice in ["panties_fishnet","panties_fishnet_string"]:
                g9 "I have something for you! Try it out!"
                if her_whoring >= 20: #Success
                    call her_main("Wow. Fishnet Panties?","smile","down")
                    call her_main("That's so naughty!","grin","glance")
                    g9 "Glad you like them!"
                    call her_main("I do, [genie_name].","soft","baseL")
                    call her_main("Let me put them on real quick.","base","glance")
                else: #Fail
                    if her_whoring < 11:
                        call her_main("Don't tell me it's panties again...","annoyed","angry")
                        m "Yes, how did you know."
                        call her_main("[genie_name], I've told you before, gifting your students panties is not ok!","clench","closed")
                        m "You haven't even looked at them!"
                        call her_main("Because I don't need to.","open","angry")
                        call her_main("(And I also don't want to!)","annoyed","angryL")
                        call her_main("You can keep them...","annoyed","angry")
                        m "(She'll wear them sooner or later...)"
                    else:
                        call her_main("Another one of your way too revealing panties?","disgust","angry")
                        g9 "Even better! I can see through the net!"
                        call her_main("What?!","open","wide")
                        call her_main("This doesn't even cover anything!!!","soft","wide")
                        call her_main("[genie_name], this is disgusting!","scream","angryCl")
                        call her_main("You can have them back you freak...","clench","angry")
                        m "Okay- Jeesh... No need to make a scene..."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe



            call set_her_panties(underwear_choice)

            call her_main(xpos="wardrobe")
            $ hide_transitions = 1
            call screen wardrobe

        else:
            $ hide_transitions = True

            #Fails
            if her_whoring < 11 and underwear_choice in ["panties_base","panties_lace","panties_silk","panties_silk_low"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 11."
                jump return_to_wardrobe

            if her_whoring < 14 and underwear_choice in ["panties_bikini","panties_bikini_string"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 14."
                jump return_to_wardrobe

            if her_whoring < 17 and underwear_choice in ["panties_latex"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 17."
                jump return_to_wardrobe

            if her_whoring < 20 and underwear_choice in ["panties_french_maid","panties_fishnet","panties_fishnet_string"]:
                "She won't wear this item just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 20."
                jump return_to_wardrobe

            #Success!
            call set_her_panties(underwear_choice)

            call her_main(xpos="wardrobe")
            hide screen wardrobe
            call screen wardrobe


### Equip Luna's Panties ###
label equip_lun_panties:
    call set_lun_panties(underwear_choice)

    jump return_to_wardrobe

### Equip Susan's Panties ###
label equip_sus_panties:
    call set_sus_panties(underwear_choice)

    jump return_to_wardrobe

### Equip Garterbelt ###
label equip_garterbelt:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_garterbelt
    #Luna
    if active_girl == "luna":
        jump equip_lun_garterbelt
    #Susan
    if active_girl == "susan":
        jump equip_sus_garterbelt

### Equip Hermione's Garterbelt ###
label equip_her_garterbelt:
    call set_her_garterbelt(underwear_choice)

    jump return_to_wardrobe

### Equip Luna's Garterbelt ###
label equip_lun_garterbelt:
    call set_lun_garterbelt(underwear_choice)

    jump return_to_wardrobe

### Equip Susan's Garterbelt ###
label equip_sus_garterbelt:
    call set_sus_garterbelt(underwear_choice)

    jump return_to_wardrobe