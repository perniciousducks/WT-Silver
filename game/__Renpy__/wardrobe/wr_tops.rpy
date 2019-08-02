#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_top:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_top
    #Luna
    if active_girl == "luna":
        jump equip_lun_top
    #Susan
    if active_girl == "susan":
        jump equip_sus_top


### Equip Hermione's Top ###

label equip_her_top:

    if top_choice == h_top:
        $ hide_transitions = True
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    if her_mood >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ hermione_xpos = 665
            $ hide_transitions = False #activates dissolve in her_main

            m "[hermione_name]..."

            ### Uniform ###

            #Uniform Top Vest and Tie #Done
            if top_choice in ["top_1_g","top_1_s"]:
                m "Would you wear your uniform top for me? All of it, vest and tie!"
                if her_whoring < 8:
                    call her_main("Of course, [genie_name].","soft","baseL")
                    call her_main("Let me go and change real quick.","base","base")
                elif her_whoring < 14:
                    call her_main("Alright, [genie_name].","smile","happyCl")
                    call her_main("Let me go and change real quick.","base","glance")
                elif her_whoring < 20:
                    call her_main("Are you sure, [genie_name]?","angry","wink")
                    call her_main("My old school top?","angry","base")
                    call her_main("You don't even want me to remove my tie or show off my cleavage??","disgust","glance")
                    m "No, [hermione_name]. No cleavage today."
                    call her_main("(Is he up to something?)","annoyed","suspicious")
                    call her_main("(Maybe this is a test of some sort...)","disgust","down_raised")
                    call her_main("OK, let me change it real quick","annoyed","annoyed")
                else: #20+
                    call her_main("That old thing?","angry","wide")
                    call her_main("Is this some silly joke, [genie_name]?","angry","angry")
                    m "..."
                    m "(I don't know. Is it?)"
                    call her_main("This is unacceptable!","scream","worriedCl")
                    call her_main("It doesn't even show any skin!","angry","down_raised")
                    m "(...)"
                    call her_main("You are insulting my tits, [genie_name]!!!","soft","base",tears="soft")
                    g4 "*Gasps* {w=0.9}I would never do that, [hermione_name]!"
                    if one_of_ten == 1:
                        g4 "Your tits are marvelous!"
                    if one_of_ten == 2:
                        g4 "Your tits are magnificent!"
                    if one_of_ten == 3:
                        g4 "Your tits are breathtaking!"
                    if one_of_ten == 4:
                        g4 "Your tits are wonderful!"
                    if one_of_ten == 5:
                        g4 "Your tits are spectacular!"
                    if one_of_ten == 6:
                        g4 "Your tits are sensational!"
                    if one_of_ten == 7:
                        g4 "Your tits are glorious!"
                    if one_of_ten == 8:
                        g4 "Your tits are beautiful!"
                    if one_of_ten == 9:
                        g4 "Your tits are lovely!"
                    if one_of_ten == 10:
                        g4 "Your tits are bananas!"
                    call her_main("And yet you want me to wear those... rags!","annoyed","annoyed")
                    m "You going to wear it or not?"
                    call her_main("Ugh--Fine, let me change it real quick.","annoyed","baseL")

            #Uniform Top Tie only #Done
            elif top_choice in ["top_2_g","top_2_s"]:
                m "Would you wear your uniform top for me? But leave the vest off."
                if her_whoring >= 2:
                    if her_whoring < 5:
                        call her_main("OK, [genie_name].","base","glance")
                        call her_main("While I find it inappropriate for a Hogwarts student to not wear their proper school attire at all times,...","open","closed")
                        call her_main("(And of course half of house Slytherin doesn't even bother to tie their shoes...)","annoyed","angryL")
                        call her_main("You are the headmaster, after all. You make the rules.","open","closed")
                        call her_main("Let me just go and change, [genie_name].","base","base")
                    elif her_whoring < 11:
                        call her_main("Alright, [genie_name].","soft","baseL")
                        call her_main("Let me go and change it real quick.","base","base")
                    elif her_whoring < 17:
                        call her_main("Sure, [genie_name].","grin","baseL")
                        call her_main("I will just change it right here if you don't mind.","base","glance")
                        #g4 "(Baby I don't mind at all!)"
                        #g9 "(Show me those titties!)"
                        # $ wardrobe_strip = True
                    else: #17+
                        call her_main("Just my school shirt and my tie?","soft","base")
                        m "Yes, [hermione_name]."
                        call her_main("Do you want me to tie the shirt around my breasts?","open","baseL")
                        m "No, put it on properly."
                        call her_main("Properly, [genie_name]?","angry","wink")
                        m "You know, buttons and everything."
                        call her_main("(I completely forgot this shirt even had buttons...)","annoyed","down")
                        call her_main("Can't I leave these buttons open, [genie_name]?","soft","baseL")
                        m "I'm afraid not, [hermione_name]."
                        call her_main("(I'm gonna get laughed at for wearing my shirt like this.)","annoyed","ahegao")
                        call her_main("Fine, let me just change it real quick.","base","baseL")
                else:
                    call her_main("I'm sorry, [genie_name].","base","base")
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed")
                    call her_main("I have to refuse, [genie_name].","normal","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 2."
                    jump return_to_wardrobe

            #Uniform Top No Tie #Done
            elif top_choice in ["top_3_g","top_3_s"]:
                m "Would you wear your uniform top for me? But remove the tie and the vest."
                if her_whoring >= 5:
                    if her_whoring < 11:
                        call her_main("You better appreciate this, [genie_name].","annoyed","annoyed")
                        call her_main("Can't believe I'm willing to remove my precious Gryffindor tie for you...","angry","angry")
                        m "It's only a tie, girl!"
                        call her_main("No, it is not...","scream","worriedCl")
                        call her_main("...","annoyed","worriedL")
                        call her_main("Just let me go and change...","annoyed","base")
                    elif her_whoring < 15:
                        call her_main("OK, [genie_name]","base","base")
                    else:
                        call her_main("My old school top? But it looks so plain...","annoyed","down_raised")
                        call her_main("Do I really have to?","open","wink")
                        m "You do."
                        call her_main(".......","annoyed","down")
                        call her_main("(How embarassing...)","annoyed","ahegao")
                else:
                    call her_main("No thank you, [genie_name].","open","worriedL")
                    call her_main("No amount of points will ever convince me to remove my precious Gryffindor tie!","open","closed")
                    call her_main("It's the single most valuable piece of clothing I possess!","soft","baseL")
                    m "(Maybe for you girl...)"
                    g9 "(But for me it's your panties!)"
                    call her_main("My tie represents my affiliation and commitment to the house Gryffindor, after all...","soft","base")
                    m "..."
                    call her_main("Every Gryffindor student knows that--","open","down")
                    m "(There she goes again, rambling on about her school-house...)"
                    call her_main("...when Godric Gryffindor, the greatest of the four founders of Hogwarts, choose the colours red and gold for his house he...","open","closed")
                    m "(I don't understand a word she's is saying,... {w=0.9}but she has a lovely accent!)"
                    call her_main("...the golden mane of a lion, which is also our houses emblematic animal,...","smile","happyCl")
                    m "(Should I just jerk off again while she's talking?)"
                    m "(Probably too late now... {w=0.9}Please tell me she's almost done...)"
                    call her_main("...as can be read about in \"Hogwarts: A History\", which you [genie_name], of course have read a great many times...","open","closed")
                    m "(...)"
                    call her_main("...it is also important for a student of Hogwarts to--","soft","baseL")
                    g4 "Enough, girl!"
                    m "Leave your tie on."
                    g4 "(And stop talking!)"
                    call her_main("Very well, [genie_name].","soft","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 5."
                    jump return_to_wardrobe

            #Uniform Top Cleavage #Done
            elif top_choice in ["top_4_g","top_4_s"]:
                m "Would you wear your uniform top for me? Just the shirt..."
                g9 "And unbutton some of those buttons! I want you to show some cleavage!"
                if her_whoring >= 8:
                    if her_whoring < 11:
                        call her_main("(Lets just hope nobody stares at them too much.)","annoyed","down")
                        call her_main("Fine, [genie_name]. {w=0.9}Let me go change.","open","suspicious")
                    elif her_whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL")
                        call her_main("I will just change it here.","base","glance")
                        m "Yes, do that, [hermione_name]."
                        g4 "(And show me those tits!)"
                    else: #20+
                        call her_main("(Buttons?...)","base","suspicious")
                        call her_main("(Oh, he means those.)","base","down")
                        call her_main("Can't I just tie the shirt around my breasts so I can remove it more easily?","open","closed")
                        m "Is that really a concern of yours, [hermione_name]"
                        call her_main("Well, yes.","soft","baseL")
                        call her_main("I like showing them to people!","grin","wink",cheeks="blush")
                        g4 "You hopeless slut!"
                        call her_main("...","base","glance")
                        m "Wear your shirt properly, for now."
                        m "If you are in luck, and I change my mind, I will let you know."
                        call her_main("Yes, [genie_name]. {w=0.9}Let me just change it!","soft","baseL")
                else:
                    if her_whoring >=2:
                        call her_main("Show some...","open","suspicious")
                        call her_main("Cleavage?","angry","angry")
                        call her_main("[genie_name], with all due respect,...","open","closed")
                        call her_main("I'm not going to walk around school looking like some... {w=0.9}harlot!","angry","angry",emote="01")
                        call her_main("(What does he think I am? A Slytherin?)","annoyed","angryL")
                        m "It can greatly boost a women's self-confidence if she's willing to show some--"
                        call her_main("I feel very self-confident just the way am, [genie_name].","open","closed")
                        call her_main("I definitely refuse.","annoyed","suspicious")
                    else:
                        call her_main("Whoops.","angry","down_raised")
                        call her_main("I dropped my wand.","open","down")
                        call her_main("I'm sorry, [genie_name]. {w=0.9}Let me just pick it up real quick.","open","baseL",cheeks="blush")
                        hide screen hermione_main
                        with d3
                        ">You are walking on very thin ice here!"
                        call her_main("What was it you wanted from me, [genie_name]?","soft","baseL")
                        m "(Maybe it's not a good idea to ask her that now.)"
                        m "Never mind, girl."
                        call her_main("OK, [genie_name].","base","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 8."
                    jump return_to_wardrobe

            #Uniform Crop-Top #Done
            elif top_choice in ["top_5_g","top_5_s"]:
                m "I want you to pull up the two ends of your school top and tie them together around your chest."
                if her_whoring >= 11:
                    if her_whoring < 14:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","open","closed")
                        call her_main("Everybody is going to look at my breasts...","annoyed","down")
                        g9 "I would be concerned if they didn't!"
                        call her_main("Ugh--Fine. {w=0.9}Let me just change it real quick.","soft","angry")
                    elif her_whoring < 20:
                        call her_main("Tie my shirt around my breasts?.","open","suspicious")
                        m "Yes, if you could do that."
                        call her_main("Of course, [genie_name].","grin","angry",cheeks="blush")
                        call her_main("I will just change right here, if you don't mind.","base","glance")
                    else: #20+
                        call her_main("Of course, [genie_name].","soft","baseL") #soft, baseL
                        call her_main("I love wearing my top like this! It's so handy!","smile","happyCl",emote="06")
                        call her_main("I can just untie it whenever a Slytherin boy walks past me!","soft","ahegao")
                        call her_main("Or a Slytherin girl of course! I'm not saying that I'm leaving them out!","smile","happyCl")
                        m "And what about students of other houses?"
                        call her_main("They too of course!","open","baseL",cheeks="blush")
                        call her_main("(But not as much, now that I think about it.)","annoyed","ahegao")
                        call her_main("Let me change my top for you real quick!","grin","baseL")
                else:
                    call her_main("This is just ridiculous!","angry","angry")
                    call her_main("I'm not walking around school wearing my shirt like that!","annoyed","suspicious")
                    call her_main("I refuse!","open","worriedL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            #Uniform Top Vest with Cleavage #Done
            elif top_choice in ["top_6_g","top_6_s"]:
                m "Would you wear your vest for me? Just the vest. Maybe your shirt beneath it. But don't think about closing any of those buttons!"
                if her_whoring >= 8:
                    if her_whoring < 11:
                        call her_main("Sure, why not.","soft","baseL")
                        call her_main("Let me just change it.","base","base")
                    elif her_whoring < 20:
                        call her_main("Just my vest?","annoyed","down")
                        call her_main("(At least I get to show off my cleavage.)","annoyed","ahegao")
                        call her_main("Alright, [genie_name]. I will change it.","base","glance")
                    else: #20+
                        call her_main("My vest, [genie_name]?","angry","wink")
                        call her_main("Don't you have anything more fashionable?","annoyed","ahegao")
                        call her_main("Besides, red and yellow doesn't really suit me.","open","closed")
                        m "Wear it, or I will have you cover up your tits too!"
                        call her_main("(That would be horrible!)","shock","wide")
                        call her_main("Yes, [genie_name]. Let me change it for you.","soft","baseL")
                else:
                    if her_whoring < 5:
                        call her_main("Just my vest?","base","base")
                        call her_main("Without my Gryffindor tie?!","shock","wide")
                        call her_main("Why would I want to do that? I refuse, [genie_name]!","angry","base")
                    else:
                        call her_main("I'm sorry, [genie_name].","open","closed")
                        call her_main("But there is no way I will walk around school with...","angry","angry")
                        call her_main("I will not show off my cleavage, [genie_name]!","open","closed")
                        call her_main("I have to refuse!","annoyed","baseL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 8."
                    jump return_to_wardrobe

            elif top_choice in ["top_7_g","top_7_s"]:
                m "Could you wear your uniform top, but like this?"
                if her_whoring >= 17:
                    if her_whoring < 14:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","open","closed")
                        call her_main("Everybody is going to look at my breasts...","annoyed","down")
                        g9 "I would be concerned if they didn't!"
                        call her_main("Ugh--Fine. {w=0.9}Let me just change it real quick.","soft","angry")
                    else:
                        call her_main("Of course, [genie_name].","grin","angry",cheeks="blush")
                        call her_main("I will just change right here, if you don't mind.","base","glance")
                else:
                    call her_main("This is just ridiculous!","angry","angry")
                    call her_main("I'm not walking around school wearing a shirt like that!","annoyed","suspicious")
                    call her_main("I refuse!","open","worriedL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 17."
                    jump return_to_wardrobe


            #Uniform Top Cheer #Done
            elif top_choice in ["top_cheer_g","top_cheer_s","top_cheer_r","top_cheer_h"] or top_choice in ["top_cheer_sexy_g","top_cheer_sexy_s","top_cheer_sexy_r","top_cheer_sexy_h"]:
                if top_choice in ["top_cheer_s","top_cheer_r","top_cheer_h"] or top_choice in ["top_cheer_sexy_s","top_cheer_sexy_r","top_cheer_sexy_h"]: #Not gryffindor!
                    m "Would you wear this cheerleader top for me?"
                    if her_whoring >= 11:
                        if her_whoring < 14:
                            if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                                call her_main("But [genie_name], that's for Slytherins!","angry","wink")
                            if top_choice in ["top_cheer_r","top_cheer_sexy_r"]:
                                call her_main("But [genie_name], that's for Ravenclaws!","angry","wink")
                            if top_choice in ["top_cheer_h","top_cheer_sexy_h"]:
                                call her_main("But [genie_name], that's for Hufflepuffs!","angry","wink")
                            m "And?"
                            call her_main("I'm a Gryffindor!","annoyed","annoyed")
                            if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                                call her_main("(A muggle-born on top of that.)","disgust","down_raised")
                            call her_main("I can't wear this!","open","worriedCl")
                            m "Why not?"
                            call her_main("I've already told you, I'm a Gryffindor!","annoyed","ahegao")
                            m "(...)"
                            g9 "(I've got an idea!)"
                            g4 "[hermione_name], I completely forgot to mention!"
                            m "As the top student of Gryffingdoor, you were selected to switch places with a fellow student form another house!"
                            m "As a form of bonding method... To bring the four houses closer together!"
                            call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","disgust","glance")
                            g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students!"
                            if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                                m "Especially Gryffindor and Slytherin!"
                                m "I mean, do you like being called a mudblood every day by them?"
                                call her_main("No, [genie_name].","angry","wink")
                                m "Or when they call you a slut..."
                                g4 "Or a whore!"
                                g9 "Or bitch!"
                                g4 "Or... a whore!"
                                g4 "Or--"
                                call her_main("I get your point, [genie_name]!!!","scream","worriedCl",cheeks="blush")
                            m "I'm giving you an opportunity to better your relationship with them!"
                            m "Now are you going to wear this for me or not?..."
                            call her_main("(...)","annoyed","angryL")
                            call her_main("Fine, [genie_name]... Let me just put it on.","annoyed","annoyed")
                        elif her_whoring < 20:
                            call her_main("Fine, [genie_name].","soft","ahegao")
                            call her_main("(How humiliating to wear this as a Gryffindor...)","disgust","narrow")
                            call her_main("Let me just change it.","soft","baseL")
                        else: #20+
                            if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                                call her_main("Of course I will wear it!","smile","angry")
                                call her_main("Gimme-Gimme--Gimme!!!","smile","happyCl")
                                call her_main("(I'm definitely going to root for them on the next game!)","soft","baseL",cheeks="blush")
                                call her_main("(If they are winning I won't have to wear this thing long anyway!)","base","glance")
                                call her_main("Whoooo, go Slytherin!","smile","happyCl")
                            else:
                                call her_main("If I really have to...","annoyed","annoyed")
                                call her_main("Let me just change it.","soft","baseL")
                    else:
                        if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                            call her_main("In green?","shock","wide")
                        if top_choice in ["top_cheer_r","top_cheer_sexy_r"]:
                            call her_main("In blue?","shock","wide")
                        if top_choice in ["top_cheer_h","top_cheer_sexy_h"]:
                            call her_main("In yellow?","shock","wide")
                        call her_main("Are you serious, [genie_name]?","angry","angry")
                        call her_main("Are you sure you didn't just pick the wrong colour for me?","annoyed","suspicious")
                        if top_choice in ["top_cheer_s","top_cheer_sexy_s"]:
                            m "(Something tells me she doesn't want to wear green stuff.)"
                            m "(Is she grasshoppers allergies or something?)"
                        else:
                            m "(Could have sworn I picked the right color for her...)"
                        m "Forget about it, girl."
                        call her_main("I will!","annoyed","annoyed")
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at Whoring level 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    if top_choice in ["top_cheer_g"]:

                        m "Could you wear your cheerleader attire for me? Just the top."
                        if her_whoring >= 5:
                            if her_whoring < 11:
                                call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush")
                                call her_main("Let me go change.","base","base")
                            elif her_whoring < 20:
                                call her_main("Alright, [genie_name]!","soft","base")
                                call her_main("Let me just change it.","base","glance")
                            else: #20+
                                call her_main("What is this? Is this for boys?","angry","wide")
                                call her_main("Did you steal this from the Gryffindor mascot, [genie_name]?","angry","angry")
                                call her_main("Want me to put on that giant lion-head too?","open","worriedL")
                                m "(A lion-head? Do they have stuff like that here?)"
                                call her_main("You can't be serious, [genie_name]!","open","worriedCl")
                                m "Wear it, or I will have you go naked!"
                                call her_main("...","shock","wide")
                                call her_main("(Does he really think of making me do that?)","angry","wink")
                                call her_main("{size=-5}(How exciting!){/size}","smile","happyCl")
                                call her_main("I will wear it if I absolutely have to,...","open","closed")
                                call her_main("{size=-5}Do I?{/size}","angry","wink")
                                m "Yes."
                                call her_main("Tzzz--Your loss...","angry","angry")
                        else:
                            call her_main("I don't know, [genie_name].","annoyed","down")
                            call her_main("I'm not the cheerleader type!","angry","wink")
                            call her_main("While I like the idea of supporting my house in Quidditch...","open","closed")
                            call her_main("My priority is to secure this years house-cup instead!","open","baseL")
                            call her_main("I have to refuse, [genie_name].","soft","base")
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at Whoring level 5."
                            jump return_to_wardrobe

                    if top_choice in ["top_cheer_sexy_g"]:
                        m "Could you wear the top from your cheerleader attire for me?"
                        if her_whoring >= 8:
                            g9 "The skimpy one!"
                            if her_whoring < 14:
                                call her_main("Sure, [genie_name]!","soft","baseL",cheeks="blush")
                                call her_main("Let me go change.","base","base")
                            elif her_whoring < 23:
                                call her_main("Alright, [genie_name]!","soft","base")
                                call her_main("Let me just change it.","base","glance")
                            else: #23+
                                call her_main("The Gryffindor one?","annoyed","suspicious")
                                call her_main("But Gryffindor isn't even the winning team!","angry","wink")
                                call her_main("Gryffindor isn't even trying to win!","open","worriedL")
                                call her_main("(They are so embarrassing...)","annoyed","ahegao")
                                call her_main("Do I really have to?","angry","wink")
                                m "Yes, [hermione_name]. Wear the Gryffindor one!"
                                call her_main("Fine, if I have to... Let me just change it.","annoyed","annoyed")
                        else:
                            if her_whoring < 3:
                                g9 "The skimp--"
                                m "Girl? What are you doing?"
                                ">You see Hermione eying the piece of cloth."
                                call her_main("(Thats the schools Quidditch uniform alright, but...)","annoyed","down")
                                call her_main("(There are so many holes in it...)","disgust","down_raised")
                                call her_main("(Could it be...!)","soft","wide")
                                call her_main("[genie_name], do you have a rat problem?","open","closed")
                                m "A rat problem?"
                                call her_main("Yes, rats! They are everywhere in Hogwarts.","open","worried")
                                call her_main("And I'm not talking about pet-rats.","disgust","glance")
                                m "(People here keep rats as their pet?)"
                                call her_main("You should talk with Mr. Filch. He will surely know what to do about it!","open","closed")
                                call her_main("And throw this away while you're at it. It has holes everywhere!","annoyed","annoyed")
                            else:
                                g9 "The skimpy one!"
                                call her_main("The skimpy one?","shock","wide")
                                call her_main("Are you out of your mind, [genie_name]?","scream","worriedCl")
                                call her_main("I'm not going to walk around looking like those... Slytherins!","angry","worried")
                                m "But it's a Gryffindor uniform!"
                                call her_main("That has nothing to do with it!","angry","angry")
                                call her_main("(stupid sluts... always distracting our team with their breasts...)","annoyed","annoyed")
                                call her_main("(Always flashed their tits at our players...)","annoyed","angryL")
                                call her_main("(I hate those skunks! I will never fall that low.)","angry","angry")
                                call her_main("I'm not going to wear that, [genie_name]!","annoyed","annoyed")
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at Whoring level 8."
                            jump return_to_wardrobe


            ### Muggle ###

            #Muggle Pullover #Done
            elif top_choice == "top_pullover_1":
                m "Could you wear your pullover again?"
                if her_whoring >= 0:
                    if her_whoring < 5:
                        call her_main("My pullover? But that's muggle clothing?","angry","wink")
                        m "So what? Didn't you already wear it before?"
                        call her_main("Well yes, but that was an exception. Because it was raining and-","open","baseL")
                        m "Pull it over already..."
                        call her_main("Fine... Just give me a second...","annoyed","angryL")
                    else:
                        call her_main("Alright, [genie_name].","soft","baseL")
                        call her_main("(I really like the colour...)","base","down")
                        call her_main("(I probably look really cute in it!)","base","happyCl")
                        call her_main("Let me put it on, [genie_name].","base","glance")
                else:
                    pass

            #Muggle Pullover #Done
            elif top_choice == "top_pullover_2":
                m "Could you wear your pullover again?"
                if her_whoring >= 5:
                    call her_main("The one with the heart, [genie_name]?","open","baseL")
                    g9 "Oh yes,... The one that shows your cleavage!"
                    call her_main("Alright. Just give me a second.","base","down")
                    call her_main("(I hope I remember the spell correctly...)","disgust","down")
                    ">Hermione's quickly waving her wand. You watch as a heart shaped hole magically appeared in the fabric!"
                    g9 "Nice! That's quite the magic trick, [hermione_name]!"
                    call her_main("Thank you, [genie_name].","base","glance")
                else:
                    call her_main("This one?","soft","base")
                    m "Yes, the one with the hole in it."
                    call her_main("Hole, [genie_name]? There aren't any holes in my clothing!...","open","closed")
                    call her_main("Do you want me to wear it or not?","open","angry")
                    m "Sure."
                    m "(No cleavage for me today...)"
                    call her_main("Here you go.","base","base")
                    $ top_choice == "top_pullover_1"

            #Muggle Sweater #Done
            elif top_choice == "top_sweater_1":
                m "Could you wear that sweater again?"
                if her_whoring >= 0:
                    if her_whoring < 5:
                        call her_main("But, [genie_name], that's muggle clothing!","angry","wink")
                        m "... So what?"
                        call her_main("They are against the Hogwarts rules for--","open","closed")
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","annoyed","annoyed")
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","annoyed","angryL")
                    elif her_whoring < 20:
                        call her_main("OK, [genie_name].","soft","baseL")
                        call her_main("Let me put it on.","base","base")
                    else: #20+
                        call her_main("Sure, [genie_name].","smile","glance")
                        call her_main("Let me put it on real quick.","base","glance")
                else:
                    pass

            #Muggle Waitress Top #Kinda done
            elif top_choice == "top_frilled_1":
                m "Would you wear this top again. The one with the massive cleavage?"
                if her_whoring >= 5:
                    if her_whoring < 11:
                        call her_main("(I already regret wearing this in front of him... But it was so hot that day...)","disgust","down")
                        call her_main("Fine, [genie_name].","open","closed")
                        call her_main("Just don't stare too much at my chest this time.","annoyed","angry")
                    else: #11+
                        call her_main("Alright, [genie_name].","soft","ahegao")
                        call her_main("Let me just change it.","base","glance")
                else:
                    call her_main("What? I'm not wearing a top like that!","open","wide")
                    m "Please?"
                    call her_main("Not a chance, [genie_name]!","clench","angry")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 5."
                    jump return_to_wardrobe


            ### Wicked ###

            #Leather Jacket #Done
            elif top_choice in ["top_jacket_2","top_jacket_3","top_jacket_1"]:
                m "Could you wear this leather Jacket for me?"

                if her_whoring >= 17:
                    if her_whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed")
                        call her_main("I don't mind wearing this in your office.","open","worriedL")
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed")
                        call her_main("But wearing something like this in class...","angry","angry")
                        call her_main("You better appreciate this, [genie_name]!","annoyed","angry")
                    elif her_whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed")
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down")
                        call her_main("Let me just change it.","base","base")
                    else: #23+
                        call her_main("Of course, [genie_name]!","smile","happyCl")
                        call her_main("I really love this jacket!","smile","glance")
                        call her_main("(Maybe I will wear it open a couple of times...)","soft","ahegao")
                        call her_main("(I want to show the boys my new bra...)","grin","baseL")
                        call her_main("Let me just put it on real quick.","base","glance")
                else:
                    if her_whoring < 5:
                        call her_main("[genie_name]?!","shock","wide")
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink")
                        call her_main("What kind of silly joke is this?","shock","worriedCl")
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious")
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif her_whoring < 11:
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry")
                        call her_main("A leather jacket?... On me?","angry","worried")
                        call her_main("Not even a Slytherin would wear something like that!","open","closed")
                        call her_main("I definitely refuse!","annoyed","annoyed")
                    else:
                        call her_main("No, [genie_name].","open","closed")
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL")
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed")
                        call her_main("I refuse!","normal","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 17."
                    jump return_to_wardrobe

            #Leather Jacket Open #Done
            elif top_choice in ["top_jacket_open_2","top_jacket_open_3","top_jacket_open_1"]:
                m "Could you wear this leather Jacket for me?"
                g9 "But leave the front open!"
                if her_whoring >= 11:
                    g9 "Those puppies need to breath!"

                if her_whoring >= 17:
                    if her_whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed")
                        call her_main("I don't mind wearing this in your office.","open","worriedL")
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed")
                        call her_main("But wearing something like this in class...","angry","angry")
                        call her_main("(no way in hell am I going to leave it open once I step out of his office...)","annoyed","ahegao")
                        call her_main("You better appreciate this, [genie_name]!","angry","angry")
                    elif her_whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed")
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down")
                        call her_main("Just... do you expect me to leave it open the whole time?","angry","wink")
                        m "Naturally, [hermione_name]."
                        call her_main("With just my bra beneath it?","disgust","narrow")
                        g9 "You betcha!"
                        call her_main("(Can't believe I'm agreeing to this...)","angry","angry")
                        call her_main("Fine, [genie_name]. I will wear it open.","annoyed","annoyed")
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","baseL")
                        call her_main("Should I wear a bra beneath it, or would you like me to really show them off!?","smile","glance")
                        m "Uhm..."
                        call her_main("I'm kidding!","smile","happyCl")
                        call her_main("The other teachers wouldn't allow that sadly.","annoyed","down")
                        call her_main("(Except for maybe Professor Snape...)","annoyed","ahegao")
                        call her_main("Let me just put it on real quick.","base","glance")
                else:
                    if her_whoring < 5:
                        call her_main("[genie_name]?!","shock","wide")
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink")
                        call her_main("What kind of silly joke is this?","shock","worriedCl")
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious")
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif her_whoring < 11:
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry")
                        call her_main("A leather jacket?... On me?","angry","worried")
                        call her_main("Not even a Slytherin would wear something like that!","open","closed")
                        call her_main("I definitely refuse!","annoyed","annoyed")
                    else:
                        call her_main("No, [genie_name].","open","closed")
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL")
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed")
                        call her_main("I refuse!","normal","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 17."
                    jump return_to_wardrobe

            #Rocker Top #Done
            elif top_choice == "top_rocker":
                if her_whoring < 5:
                    m "Could you wear this top-"
                else:
                    m "Could you wear this top for me?"

                if her_whoring >= 20:
                    if her_whoring < 23:
                        call her_main("Sure, why not.","open","closed")
                        m "really?"
                        call her_main("Yes,... It's just a normal top after all...","soft","baseL")
                        m "(...)"
                        m "(Am I going crazy?)"
                        call her_main("Just let me change it real quick.","base","glance")
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","ahegao")
                        call her_main("I like how much it emphasizes my breasts!","smile","glance")
                        call her_main("I really do love it!","smile","happyCl")
                        call her_main("Let me just put it on real quick.","base","glance")
                else:
                    if her_whoring < 5:
                        call her_main("A--...","shock","worriedCl")
                        call her_main("A--Achou!!","angry","worriedCl",cheeks="blush",emote="05",trans="hpunch")
                        call nar(">Hermione sneezed.")
                        call her_main("Ahh,...","silly","ahegao")
                        call her_main("I'm terribly sorry [genie_name]...","angry","wink")
                        call her_main("Thank you...","base","happyCl")
                        call nar(">Hermione grabs the tissue.")
                        g4 "(Wait! what tissue?! Not my...)"
                        call nar(">Hermione sneezes into the top.")
                        m "(Oh that's just perfect...)"
                        call her_main("I'm sorry sir. What was it you asked me?","soft","baseL")
                        m "Nothing, girl..."
                    elif her_whoring < 11:
                        call her_main("What?... What is this?!","shock","wide")
                        call her_main("Wizard... Sex?!","scream","angry",emote="01")
                        call her_main("What is this even supposed to mean?","angry","angry")
                        m "It's just something the kids say nowadays!"
                        call her_main("It most certainly is not!","annoyed","annoyed")
                        m "If you say so..."
                        call her_main("Keep this offensive... thing for yourself, [genie_name].","scream","angryCl")
                        call her_main("I'm not going to wear it!","angry","worried")
                    else: #11-19
                        call her_main("No, [genie_name]!","open","closed")
                        call her_main("I'm not going to wear a shirt like this on school grounds!","open","worriedL")
                        call her_main("What are you even thinking!","angry","angry")
                        call her_main("I refuse!","annoyed","annoyed")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe


            elif top_choice in ["top_fishnets_1"]:
                g9 "I have something for you! Try it out!"
                if her_whoring >= 20: #Success
                    call her_main("Wow. Fishnets?","smile","down")
                    call her_main("That's so naughty!","grin","glance")
                    g9 "Glad you like it!"
                    call her_main("Indeed I do, [genie_name].","soft","baseL")
                    call her_main("Let me put it on for you.","base","glance")
                else: #Fail
                    if her_whoring < 5:
                        call her_main("What? Oh what's this?","soft","base")
                        m "It's a fishnet to-"
                        call her_main("Oh, I get it!","grin","down")
                        call her_main("This isn't really a hobby I considered pursuing, [genie_name]...","open","baseL")
                        call her_main("But if you say it will help me with my grades then I'll try my best.","soft","down")
                        m "Wait what?"
                        call her_main("I will go down to the lake later and try it out, if that's ok with you, [genie_name].","base","glance")
                        m "(...)"
                        m "(Wait, does she want to go fishing with it...?)"
                    else:
                        call her_main("Another one of your way too revealing tops?","disgust","angry")
                        g9 "Yes, glad you noticed! Now if you don't mind just-"
                        call her_main("I'm not going to wear it! You can see everything in this! My nipples would poke right through it!!!","scream","angryCl")
                        m "I wouldn't mind if they did..."
                        call her_main("That's just... typical!","clench","angry")
                        call her_main("You disgust me, [genie_name]!","clench","angry")
                        m "Alright- Jeesh... I'm sorry."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_her_top(top_choice)

            call her_main(xpos="wardrobe")
            $ hide_transitions = True
            call screen wardrobe

        else:
            #Change this to:
            #if top_choice == wardrobe_item and Whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at Whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice in ["top_2_g","top_2_s"] and her_whoring < 2: #no vest
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 2."
                jump return_to_wardrobe
            if top_choice in ["top_3_g","top_3_s"] and her_whoring < 5: #no tie
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 5."
                jump return_to_wardrobe
            if top_choice in ["top_4_g","top_4_s"] and her_whoring < 8: #cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 8."
                jump return_to_wardrobe
            if top_choice in ["top_5_g","top_5_s"] and her_whoring < 11: #crop top
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 11."
                jump return_to_wardrobe
            if top_choice in ["top_6_g","top_6_s"] and her_whoring < 8: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 8."
                jump return_to_wardrobe
            if top_choice in ["top_7_g","top_7_s"] and her_whoring < 17: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 17."
                jump return_to_wardrobe

            if top_choice in ["top_cheer_g"]:
                if her_whoring < 5:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 5."
                    jump return_to_wardrobe

            if top_choice in ["top_cheer_s","top_cheer_r","top_cheer_h"]:
                    if her_whoring < 11:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at Whoring level 11."
                        jump return_to_wardrobe

            if top_choice in ["top_cheer_sexy_g"]:
                if her_whoring < 8:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 8."
                    jump return_to_wardrobe

            if top_choice in ["top_cheer_sexy_s","top_cheer_sexy_r","top_cheer_sexy_h"]:
                if her_whoring < 11:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at Whoring level 11."
                    jump return_to_wardrobe

            if top_choice in ["top_jacket_2","top_jacket_3","top_jacket_1"] and her_whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 17."
                jump return_to_wardrobe
            if top_choice in ["top_jacket_open_2","top_jacket_open_3","top_jacket_open_1"] and her_whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 17."
                jump return_to_wardrobe
            if top_choice == "top_rocker" and her_whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 20."
                jump return_to_wardrobe
            if top_choice == "top_fishnets_1" and her_whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at Whoring level 20."
                jump return_to_wardrobe

            #Success!
            $ hide_transitions = True
            call set_her_top(top_choice)
            call her_main(xpos="wardrobe")
            call screen wardrobe



### Equip Luna's Top ###
label equip_lun_top:
    call set_lun_top(top_choice)

    jump return_to_wardrobe
    
### Equip Susan's Top ###
label equip_sus_top:
    call set_sus_top(top_choice)

    jump return_to_wardrobe