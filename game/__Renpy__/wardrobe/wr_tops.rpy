#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_top:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_top
    #Luna
    if active_girl == "luna":
        jump equip_lun_top
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_top
    #Susan
    if active_girl == "susan":
        jump equip_sus_top


### Equip Hermione's Top ###

label equip_her_top:    

    if top_choice == h_top and top_color_choice == h_top_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    if hermione_action == "hands_behind" or hermione_action == "covering" or hermione_action == "fingering" or hermione_action == "covering_top" or hermione_action == "pinch" or hermione_action == "hands_cuffed" or hermione_action == "milk_breasts":

        $ wardrobe_active = 1
        hide screen hermione_main
        with d3
        ">Hermione is currently posing,... naked.\nWould you like her to get dressed?"
        menu:
            "-Make her get dressed-":
                call h_action("none") from _call_h_action_80
                hide screen hermione_main

            "-nvm-":
                show screen hermione_main
                with d3
                jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."

            ### Uniform ###

            #Uniform Top Vest and Tie #Done
            if top_choice == "uni_top_1":
                m "Would you wear your uniform top for me? All of it, vest and tie!" 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_5719
                    call her_main("Let me go and change real quick.","base","base") from _call_her_main_5720
                elif whoring < 14:
                    call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_5721
                    call her_main("Let me go and change real quick.","base","glance") from _call_her_main_5722
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","angry","wink") from _call_her_main_5723
                    call her_main("My old school top?","angry","base") from _call_her_main_5724
                    call her_main("You don't even want me to remove my tie or show off my cleavage??","disgust","glance") from _call_her_main_5725
                    m "No, [hermione_name]. No cleavage today."
                    call her_main("(Is he up to something?)","annoyed","suspicious") from _call_her_main_5726
                    call her_main("(Maybe this is a test of some sort...)","disgust","down_raised") from _call_her_main_5727
                    call her_main("OK, let me change it real quick","annoyed","annoyed") from _call_her_main_5728
                else: #20+
                    call her_main("That old thing?","angry","wide") from _call_her_main_5729
                    call her_main("Is this some silly joke, [genie_name]?","angry","angry") from _call_her_main_5730
                    m "..."
                    m "(I don't know. Is it?)"
                    call her_main("This is unacceptable!","scream","worriedCl") from _call_her_main_5731
                    call her_main("It doesn't even show any skin!","angry","down_raised") from _call_her_main_5732
                    m "(...)"
                    call her_main("You are insulting my tits, [genie_name]!!!","soft","base",tears="soft") from _call_her_main_5733
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
                    call her_main("And yet you want me to wear those... rags!","annoyed","annoyed") from _call_her_main_5734
                    m "You going to wear it or not?"
                    call her_main("Ugh--Fine, let me change it real quick.","annoyed","baseL") from _call_her_main_5735
                    
            #Uniform Top Tie only #Done
            elif top_choice == "uni_top_2":
                m "Would you wear your uniform top for me? But leave the vest off." 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("OK, [genie_name].","base","glance") from _call_her_main_5736
                        call her_main("While I find it inappropriate for a Hogwarts student to not wear their proper school attire at all times,...","open","closed") from _call_her_main_5737
                        call her_main("(And of course half of house Slytherin doesn't even bother to tie their shoes...)","annoyed","angryL") from _call_her_main_5738
                        call her_main("You are the headmaster, after all. You make the rules.","open","closed") from _call_her_main_5739
                        call her_main("Let me just go and change, [genie_name].","base","base") from _call_her_main_5740
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_5741
                        call her_main("Let me go and change it real quick.","base","base") from _call_her_main_5742
                    elif whoring < 17:
                        call her_main("Sure, [genie_name].","grin","baseL") from _call_her_main_5743
                        call her_main("I will just change it right here if you don't mind.","base","glance") from _call_her_main_5744
                        #g4 "(Baby I don't mind at all!)"
                        #g9 "(Show me those titties!)"
                        # $ wardrobe_strip = True 
                    else: #17+
                        call her_main("Just my school shirt and my tie?","soft","base") from _call_her_main_5745
                        m "Yes, [hermione_name]."
                        call her_main("Do you want me to tie the shirt around my breasts?","open","baseL") from _call_her_main_5746
                        m "No, put it on properly."
                        call her_main("Properly, [genie_name]?","angry","wink") from _call_her_main_5747
                        m "You know, buttons and everything."
                        call her_main("(I completely forgot this shirt even had buttons...)","annoyed","down") from _call_her_main_5748
                        call her_main("Can't I leave these buttons open, [genie_name]?","soft","baseL") from _call_her_main_5749
                        m "I'm afraid not, [hermione_name]."
                        call her_main("(I'm gonna get laughed at for wearing my shirt like this.)","annoyed","ahegao") from _call_her_main_5750
                        call her_main("Fine, let me just change it real quick.","base","baseL") from _call_her_main_5751
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_5752
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_5753
                    call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_5754
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Uniform Top No Tie #Done
            elif top_choice == "uni_top_3":
                m "Would you wear your uniform top for me? But remove the tie and the vest." 
                if whoring >= 5: #Gets removed at level 11.
                    call her_main("You better appreciate this, [genie_name].","annoyed","annoyed") from _call_her_main_5755
                    call her_main("Can't believe I'm willing to remove my precious Grffindor tie for you...","angry","angry") from _call_her_main_5756
                    m "It's only a tie, girl!"
                    call her_main("No it is not...","scream","worriedCl") from _call_her_main_5757
                    call her_main("...","annoyed","worriedL") from _call_her_main_5758
                    call her_main("Just let me go and change...","annoyed","base") from _call_her_main_5759
                else:
                    call her_main("No thank you, [genie_name].","open","worriedL") from _call_her_main_5760
                    call her_main("No amount of points will ever convince me to remove my precious Gryffindor tie!","open","closed") from _call_her_main_5761
                    call her_main("It's the single most valuable piece of clothing I possess!","soft","baseL") from _call_her_main_5762
                    m "(Maybe for you girl...)"
                    g9 "(But for me it's your panties!)"
                    call her_main("My tie represents my affiliation and commitment to the house Gryffindor, after all...","soft","base") from _call_her_main_5763
                    m "..."
                    call her_main("Every Gryffindor student knows that--","open","down") from _call_her_main_5764
                    m "(There she goes again, rambling on about her school-house...)"
                    call her_main("...when Godric Gryffindor, the greatest of the four founders of Hogwarts, choose the colours red and gold for his house he...","open","closed") from _call_her_main_5765
                    m "(I don't understand a word she's is saying,... {w=0.9}but she has a lovely accent!)"
                    call her_main("...the golden mane of a lion, which is also our houses emblematic animal,...","smile","happyCl") from _call_her_main_5766
                    m "(Should I just jerk off again while she's talking?)"
                    m "(Probably too late now... {w=0.9}Please tell me she's almost done...)"
                    call her_main("...as can be read about in \"Hogwarts: A History\", which you [genie_name], of course have read a great many times...","open","closed") from _call_her_main_5767
                    m "(...)"
                    call her_main("...it is also important for a student of Hogwarts to--","soft","baseL") from _call_her_main_5768
                    g4 "Enough, girl!"
                    m "Leave your tie on."
                    g4 "(And stop talking!)"
                    call her_main("Very well, [genie_name].","soft","base") from _call_her_main_5769
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Cleavage #Done
            elif top_choice == "uni_top_4":
                m "Would you wear your uniform top for me? Just the shirt..." 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("(Lets just hope nobody stares at them too much.)","annoyed","down") from _call_her_main_5770
                        call her_main("Fine, [genie_name]. {w=0.9}Let me go change.","open","suspicious") from _call_her_main_5771
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_5772
                        call her_main("I will just change it here.","base","glance") from _call_her_main_5773
                        m "Yes, do that, [hermione_name]."
                        g4 "(And show me those tits!)"
                    else: #20+
                        call her_main("(Buttons?...)","base","suspicious") from _call_her_main_5774
                        call her_main("(Oh, he means those.)","base","down") from _call_her_main_5775
                        call her_main("Can't I just tie the shirt around my breasts so I can remove it more easily?","open","closed") from _call_her_main_5776
                        m "Is that really a concern of yours, [hermione_name]"
                        call her_main("Well, yes.","soft","baseL") from _call_her_main_5777
                        call her_main("I like showing them to people!","grin","wink",cheeks="blush") from _call_her_main_5778
                        g4 "You hopeless slut!"
                        call her_main("...","base","glance") from _call_her_main_5779
                        m "Wear your shirt properly, for now."
                        m "If you are in luck, and I change my mind, I will let you know."
                        call her_main("Yes, [genie_name]. {w=0.9}Let me just change it!","soft","baseL") from _call_her_main_5780
                else:
                    if whoring >=2:
                        call her_main("Show some...","open","suspicious") from _call_her_main_5781
                        call her_main("Cleavage?","angry","angry") from _call_her_main_5782
                        call her_main("[genie_name], with all due respect,...","open","closed") from _call_her_main_5783
                        call her_main("I'm not going to walk around school looking like some... {w=0.9}harlot!","angry","angry",emote="01") from _call_her_main_5784
                        call her_main("(What does he think I am? A Slytherin?)","annoyed","angryL") from _call_her_main_5785
                        m "It can greatly boost a women's self-confidence if she's willing to show some--"
                        call her_main("I feel very self-confident just the way am, [genie_name].","open","closed") from _call_her_main_5786
                        call her_main("I definitely refuse.","annoyed","suspicious") from _call_her_main_5787
                    else:
                        call her_main("Whoops.","angry","down_raised") from _call_her_main_5788
                        call her_main("I dropped my wand.","open","down") from _call_her_main_5789
                        call her_main("I'm sorry, [genie_name]. {w=0.9}Let me just pick it up real quick.","open","baseL",cheeks="blush") from _call_her_main_5790
                        hide screen hermione_main
                        with d3
                        ">You are walking on very thin ice here!"
                        call her_main("What was it you wanted from me, [genie_name]?","soft","baseL") from _call_her_main_5791
                        m "(Maybe it's not a good idea to ask her that now.)"
                        m "Never mind, girl."
                        call her_main("OK, [genie_name].","base","base") from _call_her_main_5792
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Crop-Top #Done
            elif top_choice == "uni_top_5":
                m "I want you to pull up the two ends of your school top and tie them together around your chest." 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","open","closed") from _call_her_main_5793
                        call her_main("Everybody is going to look at my breasts...","annoyed","down") from _call_her_main_5794
                        g9 "I would be concerned if they didn't!"
                        call her_main("Ugh--Fine. {w=0.9}Let me just change it real quick.","soft","angry") from _call_her_main_5795
                    elif whoring < 20:
                        call her_main("Tie my shirt around my breasts?.","open","suspicious") from _call_her_main_5796
                        m "Yes, if you could do that."
                        call her_main("Of course, [genie_name].","grin","angry",cheeks="blush") from _call_her_main_5797
                        call her_main("I will just change right here, if you don't mind.","base","glance") from _call_her_main_5798
                        #m "{w=0.5}.{w=0.5}.{w=0.5}.{w=1.0}!"
                        # $ wardrobe_strip = True 
                    else: #20+
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_5799 #soft, baseL
                        call her_main("I love wearing my top like this! It's so handy!","smile","happyCl",emote="06") from _call_her_main_5800
                        call her_main("I can just untie it whenever a Slytherin boy walks past me!","soft","ahegao") from _call_her_main_5801
                        call her_main("Or a Slytherin girl of course! I'm not saying that I'm leaving them out!","smile","happyCl") from _call_her_main_5802
                        m "And what about students of other houses?"
                        call her_main("They too of course!","open","baseL",cheeks="blush") from _call_her_main_5803
                        call her_main("(But not as much, now that I think about it.)","annoyed","ahegao") from _call_her_main_5804
                        call her_main("Let me change my top for you real quick!","grin","baseL") from _call_her_main_5805
                        # $ wardrobe_strip = True 
                else:
                    call her_main("This is just ridiculous!","angry","angry") from _call_her_main_5806
                    call her_main("I'm not walking around school wearing my shirt like that!","annoyed","suspicious") from _call_her_main_5807
                    call her_main("I refuse!","open","worriedL") from _call_her_main_5808
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Top Vest with Cleavage #Done
            elif top_choice == "uni_top_6":
                m "Would you wear your vest for me? Just the vest. Maybe your shirt beneath it. But don't think about closing any of those buttons!"
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Sure, why not.","soft","baseL") from _call_her_main_5809
                        call her_main("Let me just change it.","base","base") from _call_her_main_5810
                    elif whoring < 20:
                        call her_main("Just my vest?","annoyed","down") from _call_her_main_5811
                        call her_main("(At least I get to show off my cleavage.)","annoyed","ahegao") from _call_her_main_5812
                        call her_main("Alright, [genie_name]. I will change it.","base","glance") from _call_her_main_5813
                    else: #20+
                        call her_main("My vest, [genie_name]?","angry","wink") from _call_her_main_5814
                        call her_main("Don't you have anything more fashionable?","annoyed","ahegao") from _call_her_main_5815
                        call her_main("Besides, red and yellow doesn't really suit me.","open","closed") from _call_her_main_5816
                        m "Wear it, or I will have you cover up your tits too!"
                        call her_main("(That would be horrible!)","shock","wide") from _call_her_main_5817
                        call her_main("Yes, [genie_name]. Let me change it for you.","soft","baseL") from _call_her_main_5818
                else:
                    if whoring < 5:
                        call her_main("Just my vest?","base","base") from _call_her_main_5819
                        call her_main("Without my Gryffindor tie?!","shock","wide") from _call_her_main_5820
                        call her_main("Why would I want to do that? I refuse, [genie_name]!","angry","base") from _call_her_main_5821
                    else:
                        call her_main("I'm sorry, [genie_name].","open","closed") from _call_her_main_5822
                        call her_main("But there is no way I will walk around school with...","angry","angry") from _call_her_main_5823
                        call her_main("I will not show off my cleavage, [genie_name]!","open","closed") from _call_her_main_5824
                        call her_main("I have to refuse!","annoyed","baseL") from _call_her_main_5825
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                   
                    
            #Uniform Top Cheer #Done
            elif top_choice == "uni_top_cheer" or top_choice == "uni_top_cheer_skimpy":
                if top_color_choice == "green" or top_color_choice == "blue" or top_color_choice == "yellow":
                    m "Would you wear this cheerleader skirt for me?" 
                    if whoring >= 11:
                        if whoring < 14:
                            if top_color_choice == "green":
                                call her_main("But [genie_name], that's for Slytherins!","angry","wink") from _call_her_main_5826
                            if top_color_choice == "blue":
                                call her_main("But [genie_name], that's for Ravenclaws!","angry","wink") from _call_her_main_5827
                            if top_color_choice == "yellow":
                                call her_main("But [genie_name], that's for Hufflepuffs!","angry","wink") from _call_her_main_5828
                            m "And?"
                            call her_main("I'm a Gryffindor!","annoyed","annoyed") from _call_her_main_5829
                            if top_color_choice == "green":
                                call her_main("(A muggle-born on top of that.)","disgust","down_raised") from _call_her_main_5830
                            call her_main("I can't wear this!","open","worriedCl") from _call_her_main_5831
                            m "Why not?"
                            call her_main("I've already told you, I'm a Gryffindor!","annoyed","ahegao") from _call_her_main_5832
                            m "(...)"
                            g9 "(I've got an idea!)"
                            g4 "[hermione_name], I completely forgot to mention!"
                            m "As the top student of Gryffingdoor, you were selected to switch places with a fellow student form another house!"
                            m "As a form of bonding method... To bring the four houses closer together!"
                            call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","disgust","glance") from _call_her_main_5833
                            g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students!"
                            if top_color_choice == "green":
                                m "Especially Gryffindor and Slytherin!"
                                m "I mean, do you like being called a mudblood every day by them?"
                                call her_main("No, [genie_name].","angry","wink") from _call_her_main_5834
                                m "Or when they call you a slut..."
                                g4 "Or a whore!"
                                g9 "Or bitch!"
                                g4 "Or... a whore!"
                                g4 "Or--"
                                call her_main("I get your point, [genie_name]!!!","scream","worriedCl",cheeks="blush") from _call_her_main_5835
                            m "I'm giving you an opportunity to better your relationship with them!"
                            m "Now are you going to wear this for me or not?..."
                            call her_main("(...)","annoyed","angryL") from _call_her_main_5836
                            call her_main("Fine, [genie_name]... Let me just put it on.","annoyed","annoyed") from _call_her_main_5837
                        elif whoring < 20:
                            call her_main("Fine, [genie_name].","soft","ahegao") from _call_her_main_5838
                            call her_main("(How humiliating to wear this as a Gryffindor...)","disgust","narrow") from _call_her_main_5839
                            call her_main("Let me just change it.","soft","baseL") from _call_her_main_5840
                        else: #20+
                            if top_color_choice == "green":
                                call her_main("Of course I will wear it!","smile","angry") from _call_her_main_5841
                                call her_main("Gimme-Gimme--Gimme!!!","smile","happyCl") from _call_her_main_5842
                                call her_main("(I'm definitely going to root for them on the next game!)","soft","baseL",cheeks="blush") from _call_her_main_5843
                                call her_main("(If they are winning I won't have to wear this thing long anyway!)","base","glance") from _call_her_main_5844
                                call her_main("Whoooo, go Slytherin!","smile","happyCl") from _call_her_main_5845
                            else:
                                call her_main("If I really have to...","annoyed","annoyed") from _call_her_main_5846
                                call her_main("Let me just change it.","soft","baseL") from _call_her_main_5847
                    else:
                        if top_color_choice == "green":
                            call her_main("In green?","shock","wide") from _call_her_main_5848
                        if top_color_choice == "blue":
                            call her_main("In blue?","shock","wide") from _call_her_main_5849
                        if top_color_choice == "yellow":
                            call her_main("In yellow?","shock","wide") from _call_her_main_5850
                        call her_main("Are you serious, [genie_name]?","angry","angry") from _call_her_main_5851
                        call her_main("Are you sure you didn't just pick the wrong colour for me?","annoyed","suspicious") from _call_her_main_5852
                        if top_color_choice == "green":
                            m "(Something tells me she doesn't want to wear green stuff.)"
                            m "(Is she allergic to grasshoppers or something?)"
                        else:
                            m "(Could have sworn I picked the right color for her...)"
                        m "Forget about it, girl."
                        call her_main("I will!","annoyed","annoyed") from _call_her_main_5853
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    if top_choice == "uni_top_cheer":

                        m "Could you wear your cheerleader attire for me? Just the top."
                        if whoring >= 5:
                            if whoring < 11:
                                call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") from _call_her_main_5854
                                call her_main("Let me go change.","base","base") from _call_her_main_5855
                            elif whoring < 20:
                                call her_main("Alright, [genie_name]!","soft","base") from _call_her_main_5856
                                call her_main("Let me just change it.","base","glance") from _call_her_main_5857
                            else: #20+
                                call her_main("What is this? Is this for boys?","angry","wide") from _call_her_main_5858
                                call her_main("Did you steal this from the Gryffindor mascot, [genie_name]?","angry","angry") from _call_her_main_5859
                                call her_main("Want me to put on that giant lion-head too?","open","worriedL") from _call_her_main_5860
                                m "(A lion-head? Do they have stuff like that here?)"
                                call her_main("You can't be serious, [genie_name]!","open","worriedCl") from _call_her_main_5861
                                m "Wear it, or I will have you go naked!"
                                call her_main("...","shock","wide") from _call_her_main_5862
                                call her_main("(Does he really think of making me do that?)","angry","wink") from _call_her_main_5863
                                call her_main("{size=-5}(How exciting!){/size}","smile","happyCl") from _call_her_main_5864
                                call her_main("I will wear it if I absolutely have to,...","open","closed") from _call_her_main_5865
                                call her_main("{size=-5}Do I?{/size}","angry","wink") from _call_her_main_5866
                                m "Yes."
                                call her_main("Tzzz--Your loss...","angry","angry") from _call_her_main_5867
                        else:
                            call her_main("I don't know, [genie_name].","annoyed","down") from _call_her_main_5868
                            call her_main("I'm not the cheerleader type!","angry","wink") from _call_her_main_5869
                            call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") from _call_her_main_5870
                            call her_main("My priority is to secure this years house-cup instead!","open","baseL") from _call_her_main_5871
                            call her_main("I have to refuse, [genie_name].","soft","base") from _call_her_main_5872
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at whoring level 5."
                            jump return_to_wardrobe

                    if top_choice == "uni_top_cheer_skimpy":
                        m "Could you wear the top from your cheerleader attire for me?"
                        if whoring >= 8: 
                            g9 "The skimpy one!" 
                            if whoring < 14:
                                call her_main("Sure, [genie_name]!","soft","baseL",cheeks="blush") from _call_her_main_5873
                                call her_main("Let me go change.","base","base") from _call_her_main_5874
                            elif whoring < 23:
                                call her_main("Alright, [genie_name]!","soft","base") from _call_her_main_5875
                                call her_main("Let me just change it.","base","glance") from _call_her_main_5876
                            else: #23+
                                call her_main("The Gryffindor one?","annoyed","suspicious") from _call_her_main_5877
                                call her_main("But Gryffindor isn't even the winning team!","angry","wink") from _call_her_main_5878
                                call her_main("Gryffindor isn't even trying to win!","open","worriedL") from _call_her_main_5879
                                call her_main("(They are so embarrassing...)","annoyed","ahegao") from _call_her_main_5880
                                call her_main("Do I really have to?","angry","wink") from _call_her_main_5881
                                m "Yes, [hermione_name]. Wear the Gryffindor one!"
                                call her_main("Fine, if I have to... Let me just change it.","annoyed","annoyed") from _call_her_main_5882
                        else:
                            if whoring < 3: 
                                g9 "The skimp--" 
                                m "Girl? What are you doing?" 
                                ">You see Hermione eying the piece of cloth." 
                                call her_main("(Thats the schools Quidditch uniform alright, but...)","annoyed","down") from _call_her_main_5883
                                call her_main("(There are so many holes in it...)","disgust","down_raised") from _call_her_main_5884
                                call her_main("(Could it be...!)","soft","wide") from _call_her_main_5885
                                call her_main("[genie_name], do you have a rat problem?","open","closed") from _call_her_main_5886
                                m "A rat problem?"
                                call her_main("Yes, rats! They are everywhere in Hogwarts.","open","worried") from _call_her_main_5887
                                call her_main("And I'm not talking about pet-rats.","disgust","glance") from _call_her_main_5888
                                m "(People here keep rats as their pet?)"
                                call her_main("You should talk with Mr. Filch. He will surely know what to do about it!","open","closed") from _call_her_main_5889
                                call her_main("And throw this away while you're at it. It has holes everywhere!","annoyed","annoyed") from _call_her_main_5890
                            else: 
                                g9 "The skimpy one!" 
                                call her_main("The skimpy one?","shock","wide") from _call_her_main_5891
                                call her_main("Are you out of your mind, [genie_name]?","scream","worriedCl") from _call_her_main_5892
                                call her_main("I'm not going to walk around looking like those... Slytherins!","angry","worried") from _call_her_main_5893
                                m "But it's a Gryffindor uniform!"
                                call her_main("That has nothing to do with it!","angry","angry") from _call_her_main_5894
                                call her_main("(stupid sluts... always distracting our team with their breasts...)","annoyed","annoyed") from _call_her_main_5895
                                call her_main("(Always flashed their tits at our players...)","annoyed","angryL") from _call_her_main_5896
                                call her_main("(I hate those skunks! I will never fall that low.)","angry","angry") from _call_her_main_5897
                                call her_main("I'm not going to wear that, [genie_name]!","annoyed","annoyed") from _call_her_main_5898
                            if cheats_active or game_difficulty <= 2:
                                ">Try again at whoring level 8."
                            jump return_to_wardrobe

        
            ### Muggle ###

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover":
                m "Could you wear this top I bought you?" 
                if whoring >= 0:
                    if whoring < 5:
                        call her_main("[genie_name], that's a pullover!","angry","wink") from _call_her_main_5899
                        m "... So what?"
                        call her_main("Muggle clothing!","disgust","down_raised",cheeks="blush") from _call_her_main_5900
                        call her_main("Muggle clothes are against the Hogwarts rules for--","open","closed") from _call_her_main_5901
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_5902 #very upset, annoyed
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","annoyed","angryL") from _call_her_main_5903
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_5904
                        call her_main("(I really like the colour...)","base","down") from _call_her_main_5905
                        call her_main("(I probably look really cute in it!)","base","happyCl") from _call_her_main_5906
                        call her_main("Let me put it on, [genie_name].","base","base") from _call_her_main_5907
                    else: #11+
                        call her_main("Sure, [genie_name].","smile","glance") from _call_her_main_5908
                        call her_main("Let me put it on real quick.","base","glance") from _call_her_main_5909
                else:
                    pass

            #Muggle Pullover #Done
            elif top_choice == "normal_pullover_sexy":
                m "Could you wear this pullover I bought you?" 
                if whoring >= 2:
                    if whoring < 11:
                        call her_main("Very well, [genie_name]. Just let me---","soft","baseL") from _call_her_main_5910
                        m "One second,... I'm almost done..."
                        call her_main("Done, [genie_name]? What are you doing with the--","open","suspicious") from _call_her_main_5911
                        m "Shhh! Be quiet, girl... I have to read the manual."
                        g4 "(Right,... I just have to push here, and pull on this...)"
                        ">A heart shaped hole magically appeared in the fabric!"
                        g9 "(Ah, there is is!)"
                        m "Ok girl, now put it on."
                        call her_main("(What did he just do to that pullover?)","annoyed","suspicious") from _call_her_main_5912
                        call her_main("(Doesn't look any different to me...)","annoyed","down") from _call_her_main_5913
                        call her_main("OK, [genie_name]. Let me put it on.","soft","baseL") from _call_her_main_5914
                    elif whoring < 20:
                        call her_main("You never mentioned that there's a hole in it.","open","down") from _call_her_main_5915
                        call her_main("(Right over my enormous cleavage...)","disgust","down_raised") from _call_her_main_5916
                        m "It's not my fault you never noticed..."
                        call her_main("I can really feel that it's brimming with magic!","base","glance") from _call_her_main_5917
                        call her_main("Maybe to see it you need a certain degree of... sexual awareness, for it to appear...","soft","baseL",cheeks="blush") from _call_her_main_5918
                        m "Oh yes! I think something like that was mentioned in the manual!"
                        call her_main("(...)","disgust","glance") from _call_her_main_5919
                        call her_main("Fine... Let me just put it on.","soft","ahegao") from _call_her_main_5920
                    else: #20+
                        call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_5921
                        call her_main("Let me put it on real quick.","base","glance") from _call_her_main_5922
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_5923
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_5924
                    call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_5925
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Muggle Sweater #Done
            elif top_choice == "normal_sweater":
                m "Could you wear this top I bought you?" 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("[genie_name], that's a sweater!","angry","wink") from _call_her_main_5926
                        m "... So what?"
                        call her_main("Muggle clothing!","disgust","down_raised",cheeks="blush") from _call_her_main_5927
                        call her_main("Muggle clothes are against the Hogwarts rules for--","open","closed") from _call_her_main_5928
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_5929
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","annoyed","angryL") from _call_her_main_5930
                    elif whoring < 20:
                        call her_main("OK, [genie_name].","soft","baseL") from _call_her_main_5931
                        call her_main("(It does look a lot like one of my old sweaters...)","annoyed","down") from _call_her_main_5932
                        call her_main("Let me put it on.","base","base") from _call_her_main_5933
                    else: #20+
                        call her_main("Sure, [genie_name].","smile","glance") from _call_her_main_5934
                        call her_main("Let me put it on real quick.","base","glance") from _call_her_main_5935
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_5936
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_5937
                    call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_5938
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Muggle Waitress Top #Kinda done
            elif top_choice == "normal_waitress_top":
                m "Would you wear this top I bought you." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Fine, [genie_name].","open","closed") from _call_her_main_5939
                        call her_main("Let me put it on before I change my mind...","annoyed","annoyed") from _call_her_main_5940
                    else: #11+
                        call her_main("Alright, [genie_name].","soft","ahegao") from _call_her_main_5941
                        call her_main("Let me just change it.","base","glance") from _call_her_main_5942
                else:
                    if whoring < 2:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_5943
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_5944
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_5945
                    else: #2-7
                        call her_main("I'm sorry, [genie_name].","open","closed") from _call_her_main_5946
                        call her_main("But don't even think I would wear a top like this in school!","angry","angry") from _call_her_main_5947
                        call her_main("No thanks.","annoyed","annoyed") from _call_her_main_5948
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    

            ### Wicked ###

            #Leather Jacket #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves" or top_choice == "wicked_leather_jacket_sleeveless" or top_choice == "wicked_leather_jacket_sleeves":
                m "Could you wear this leather Jacket for me?"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed") from _call_her_main_5949
                        call her_main("I don't mind wearing this in your office.","open","worriedL") from _call_her_main_5950
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed") from _call_her_main_5951
                        call her_main("But wearing something like this in class...","angry","angry") from _call_her_main_5952
                        call her_main("You better appreciate this, [genie_name]!","annoyed","angry") from _call_her_main_5953
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed") from _call_her_main_5954
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down") from _call_her_main_5955
                        call her_main("Let me just change it.","base","base") from _call_her_main_5956
                    else: #23+
                        call her_main("Of course, [genie_name]!","smile","happyCl") from _call_her_main_5957
                        call her_main("I really love this jacket!","smile","glance") from _call_her_main_5958
                        call her_main("(Maybe I will wear it open a couple of times...)","soft","ahegao") from _call_her_main_5959
                        call her_main("(I want to show the boys my new bra...)","grin","baseL") from _call_her_main_5960
                        call her_main("Let me just put it on real quick.","base","glance") from _call_her_main_5961
                else:
                    if whoring < 5: 
                        call her_main("[genie_name]?!","shock","wide") from _call_her_main_5962
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink") from _call_her_main_5963
                        call her_main("What kind of silly joke is this?","shock","worriedCl") from _call_her_main_5964
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious") from _call_her_main_5965
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry") from _call_her_main_5966
                        call her_main("A leather jacket?... On me?","angry","worried") from _call_her_main_5967
                        call her_main("Not even a Slytherin would wear something like that!","open","closed") from _call_her_main_5968
                        call her_main("I definitely refuse!","annoyed","annoyed") from _call_her_main_5969
                    else:
                        call her_main("No, [genie_name].","open","closed") from _call_her_main_5970
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL") from _call_her_main_5971
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed") from _call_her_main_5972
                        call her_main("I refuse!","normal","base") from _call_her_main_5973
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Leather Jacket Open #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves_open" or top_choice == "wicked_leather_jacket_sleeveless_open" or top_choice == "wicked_leather_jacket_sleeves_open": 
                m "Could you wear this leather Jacket for me?"
                g9 "But leave the front open!"
                if whoring >= 11: 
                    g9 "Those puppies need to breath!"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","open","closed") from _call_her_main_5974
                        call her_main("I don't mind wearing this in your office.","open","worriedL") from _call_her_main_5975
                        call her_main("(Or wearing nothing at all most of the time.)","annoyed","annoyed") from _call_her_main_5976
                        call her_main("But wearing something like this in class...","angry","angry") from _call_her_main_5977
                        call her_main("(no way in hell am I going to leave it open once I step out of his office...)","annoyed","ahegao") from _call_her_main_5978
                        call her_main("You better appreciate this, [genie_name]!","angry","angry") from _call_her_main_5979
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","open","closed") from _call_her_main_5980
                        call her_main("It is a really nice looking jacked, after all...","annoyed","down") from _call_her_main_5981
                        call her_main("Just... do you expect me to leave it open the whole time?","angry","wink") from _call_her_main_5982
                        m "Naturally, [hermione_name]."
                        call her_main("With just my bra beneath it?","disgust","narrow") from _call_her_main_5983
                        g9 "You betcha!"
                        call her_main("(Can't believe I'm agreeing to this...)","angry","angry") from _call_her_main_5984
                        call her_main("Fine, [genie_name]. I will wear it open.","annoyed","annoyed") from _call_her_main_5985
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_5986
                        call her_main("Should I wear a bra beneath it, or would you like me to really show them off!?","smile","glance") from _call_her_main_5987
                        m "Uhm..."
                        call her_main("I'm kidding!","smile","happyCl") from _call_her_main_5988
                        call her_main("The other teachers wouldn't allow that sadly.","annoyed","down") from _call_her_main_5989
                        call her_main("(Except for maybe Professor Snape...)","annoyed","ahegao") from _call_her_main_5990
                        call her_main("Let me just put it on real quick.","base","glance") from _call_her_main_5991
                else:
                    if whoring < 5:
                        call her_main("[genie_name]?!","shock","wide") from _call_her_main_5992
                        call her_main("How can you even suggest something like that to one of your student!","angry","wink") from _call_her_main_5993
                        call her_main("What kind of silly joke is this?","shock","worriedCl") from _call_her_main_5994
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","annoyed","suspicious") from _call_her_main_5995
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","angry","angry") from _call_her_main_5996
                        call her_main("A leather jacket?... On me?","angry","worried") from _call_her_main_5997
                        call her_main("Not even a Slytherin would wear something like that!","open","closed") from _call_her_main_5998
                        call her_main("I definitely refuse!","annoyed","annoyed") from _call_her_main_5999
                    else:
                        call her_main("No, [genie_name].","open","closed") from _call_her_main_6000
                        call her_main("Even with all the favours I'm willing to do for you...","open","worriedL") from _call_her_main_6001
                        call her_main("I am not going to wear a jacket like this on school grounds.","annoyed","annoyed") from _call_her_main_6002
                        call her_main("I refuse!","normal","base") from _call_her_main_6003
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Rocker Top #Done
            elif top_choice == "wicked_rocker_top":
                if whoring < 5: 
                    m "Could you wear this top--"
                else: 
                    m "Could you wear this top for me?"

                if whoring >= 20: 
                    if whoring < 23: 
                        call her_main("Sure, why not.","open","closed") from _call_her_main_6004
                        m "really?"
                        call her_main("Yes,... It's just a normal top after all...","soft","baseL") from _call_her_main_6005
                        m "(...)"
                        m "(Am I going crazy?)"
                        call her_main("Just let me change it real quick.","base","glance") from _call_her_main_6006
                    else: #23+
                        call her_main("Of course, [genie_name].","soft","ahegao") from _call_her_main_6007
                        call her_main("I like how much it emphasizes my breasts!","smile","glance") from _call_her_main_6008
                        call her_main("I really do love it!","smile","happyCl") from _call_her_main_6009
                        call her_main("Let me just put it on real quick.","base","glance") from _call_her_main_6010
                else:
                    if whoring < 5: 
                        call her_main("A--...","shock","worriedCl") from _call_her_main_6011 #Add screen shake and sneeze sound.
                        call her_main("A--Achou!!","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_6012 #Add screen shake and sneeze sound.
                        ">Hermione sneezed."
                        call her_main("Ahh,...","silly","ahegao") from _call_her_main_6013
                        call her_main("I'm terribly sorry [genie_name]...","angry","wink") from _call_her_main_6014
                        call her_main("Thank you...","base","happyCl") from _call_her_main_6015
                        ">Hermione grabs the tissue."
                        g4 "(Wait! what tissue?! Not my...)"
                        ">Hermione sneezes into the top."
                        m "(Oh that's just perfect...)"
                        call her_main("I'm sorry sir. What was it you asked me?","soft","baseL") from _call_her_main_6016
                        m "Nothing, girl..."
                    elif whoring < 11: 
                        call her_main("What?... What is this?!","shock","wide") from _call_her_main_6017
                        call her_main("Wizard... Sex?!","scream","angry",emote="01") from _call_her_main_6018
                        call her_main("What is this even supposed to mean?","angry","angry") from _call_her_main_6019
                        m "It's just something the kids say nowadays!"
                        call her_main("It most certainly is not!","annoyed","annoyed") from _call_her_main_6020
                        m "If you say so..."
                        call her_main("Keep this offensive... thing for yourself, [genie_name].","scream","angryCl") from _call_her_main_6021
                        call her_main("I'm not going to wear it!","angry","worried") from _call_her_main_6022
                    else: #11-19
                        call her_main("No, [genie_name]!","open","closed") from _call_her_main_6023
                        call her_main("I'm not going to wear a shirt like this on school grounds!","open","worriedL") from _call_her_main_6024
                        call her_main("What are you even thinking!","angry","angry") from _call_her_main_6025
                        call her_main("I refuse!","annoyed","annoyed") from _call_her_main_6026
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe
                    
            
            #Misc #Doesn't have texts yet.
            elif top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_ripped_tie_striped":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_tie_striped":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green"):
                if whoring >= 17:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
            elif top_choice == "top_fishnets":
                if whoring >= 20:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_top(top_choice,top_color_choice) from _call_set_h_top

            call her_main("","","",xpos="wardrobe") from _call_her_main_6027
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if top_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice == "uni_top_2" and whoring < 2: #no vest
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "uni_top_3" and whoring < 5: #no tie
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_4" and whoring < 8: #cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_5" and whoring < 11: #crop top
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_6" and whoring < 8: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if top_choice == "uni_top_cheer":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 5:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 5."
                        jump return_to_wardrobe

            if top_choice == "uni_top_cheer_skimpy":
                if (top_color_choice == "green" or top_color_choice == "dark_green" or top_color_choice == "blue" or top_color_choice == "dark_blue" or top_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    if whoring < 8:
                        ">She won't wear that top just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 8."
                        jump return_to_wardrobe

            #Muggle
            if top_choice == "normal_pullover" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_pullover_sexy" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_sweater" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "normal_waitress_top" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Wicked
            if top_choice == "wicked_leather_jacket_short_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_short_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_rocker_top" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe

            #Misc
            if top_choice == "top_banner" and top_color_choice != "green" and top_color_choice != "dark_green" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_ripped_tie_striped" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_tie_striped" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_banner" and (top_color_choice == "green" or top_color_choice == "dark_green") and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "top_fishnets" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_h_top(top_choice,top_color_choice) from _call_set_h_top_1
            call her_main("","","",xpos="wardrobe") from _call_her_main_6028
            call screen wardrobe

            


### Equip Astoria's Top ###
label equip_ast_top: 
    call set_ast_top(top_choice) from _call_set_ast_top
        
    hide screen wardrobe
    call screen wardrobe
        
### Equip Susan's Top ###
label equip_sus_top:
    call set_sus_top(top_choice) from _call_set_sus_top_1

    hide screen wardrobe
    call screen wardrobe
        
        



