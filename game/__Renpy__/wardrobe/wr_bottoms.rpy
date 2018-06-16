#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

label equip_bottom:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_bottom
    #Luna
    if active_girl == "luna":
        jump equip_lun_bottom
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_bottom
    #Susan
    if active_girl == "susan":
        jump equip_sus_bottom


### Equip Bottom ###

label equip_her_bottom:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

    if skirt_choice == h_skirt and bottom_color_choice == h_skirt_color:
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
                call h_action("none") from _call_h_action_2
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

            ### Uniform Skirts ###

            #Uniform Skirt Very Long #Done
            if skirt_choice == "uni_skirt_1":
                m "Would you wear your school skirt for me? The very long one." 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_608
                    call her_main("Let me go and change real quick.","base","base") from _call_her_main_609
                elif whoring < 11:
                    call her_main("Alright... sure, why not.","base","down") from _call_her_main_610
                    call her_main("Let me go and change real quick.","base","base") from _call_her_main_611
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","disgust","down_raised") from _call_her_main_612
                    call her_main("That thing looks rather plain...","open","closed") from _call_her_main_613
                    call her_main("I would much rather wear one a bit shorter!","angry","wink") from _call_her_main_614
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Ugh... Fine.","disgust","down_raised") from _call_her_main_615
                    call her_main("Let me just change it.","annoyed","annoyed") from _call_her_main_616
                else: #20+
                    call her_main("Are you serious?","angry","wink") from _call_her_main_617
                    call her_main("That thing is soooooo ugly!","annoyed","ahegao") from _call_her_main_618
                    call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","disgust","narrow") from _call_her_main_619
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Fine... Just let me change it...","disgust","glance") from _call_her_main_620
                    
            #Uniform Skirt Long #Done
            elif skirt_choice == "uni_skirt_2":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if whoring >= 5:
                    if whoring < 8:
                        call her_main("...","annoyed","annoyed") from _call_her_main_621
                        call her_main("Fine.","open","closed") from _call_her_main_622
                        call her_main("Let me go and change real quick.","base","base") from _call_her_main_623
                    elif whoring < 11:
                        call her_main("Sure, why not.","base","down") from _call_her_main_624
                        call her_main("Let me go and change real quick.","base","base") from _call_her_main_625
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_626
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_627
                    else: #20+
                        call her_main("...that old thing?","annoyed","angryL") from _call_her_main_628
                        m "Sure, is that a problem?"
                        call her_main("...","annoyed","ahegao") from _call_her_main_629
                        call her_main("I suppose not...","annoyed","down") from _call_her_main_630
                        call her_main("It's just so plain!","annoyed","angryL") from _call_her_main_631
                else:
                    call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_632
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_633
                    call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_634
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Medium Length #Done
            elif skirt_choice == "uni_skirt_3":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","base","down") from _call_her_main_635
                        call her_main("Let me go and change real quick.","base","base") from _call_her_main_636
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_637
                        call her_main("Let me go and change real quick.","base","glance") from _call_her_main_638
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_639
                        call her_main("(At least it is short enough...)","annoyed","ahegao") from _call_her_main_640
                        call her_main("OK, [genie_name].","soft","baseL") from _call_her_main_641
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_642
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_643
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_644
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_645
                    else:
                        call her_main("That's way too short, [genie_name]!","open","closed") from _call_her_main_646
                        call her_main("I have to refuse!","annoyed","suspicious") from _call_her_main_647
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Short #Done
            elif skirt_choice == "uni_skirt_4":
                m "Would you wear your school skirt for me? But make it a bit shorter would you."
                if whoring >= 14:
                    if whoring < 20:
                        call her_main("Sure, why not.","soft","baseL") from _call_her_main_648
                        call her_main("Let me change it real quick.","base","glance") from _call_her_main_649
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_650
                        call her_main("(At least it is short enough...)","annoyed","ahegao") from _call_her_main_651
                        call her_main("OK, [genie_name].","soft","baseL") from _call_her_main_652
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_653
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_654
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_655
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_656
                    else:
                        call her_main("That's way too short, [genie_name]!","open","closed") from _call_her_main_657
                        call her_main("I have to refuse!","annoyed","suspicious") from _call_her_main_658
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Shortest #Done
            elif skirt_choice == "uni_skirt_5":
                m "Would you wear your school skirt for me? The shortest one you have."  
                if whoring >= 17:
                    if whoring < 23:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_659
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_660
                    else: #23+
                        call her_main("(That old thing?)","annoyed","down") from _call_her_main_661
                        call her_main("Can't I wear something a little shorter?","open","baseL",cheeks="blush") from _call_her_main_662
                        m "I don't think they make anything shorter."
                        call her_main("I guess This will just have to do then...","open","ahegao_raised",cheeks="blush") from _call_her_main_663
                        call her_main("Let me go change...","base","ahegao_raised",cheeks="blush") from _call_her_main_664
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_665
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_666
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_667
                    else:
                        call her_main("How... How short?!","shock","wide") from _call_her_main_668
                        call her_main("Is that another one of your silly jokes, [genie_name]?","angry","worried") from _call_her_main_669
                        call her_main("No, please, don't tell me.","open","closed") from _call_her_main_670
                        call her_main("I don't even want to know...","annoyed","worriedL") from _call_her_main_671
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Gryffindor #Done
            elif skirt_choice == "uni_skirt_cheer_gryff":
                m "Could you wear your cheerleader skirt for me?"
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") from _call_her_main_672
                        call her_main("Let me go change.","base","base") from _call_her_main_673 
                    else:
                        call her_main("Alright, [genie_name]!","soft","base") from _call_her_main_674
                        call her_main("Let me just change it.","base","glance") from _call_her_main_675
                else:
                    call her_main("I don't know, [genie_name].","annoyed","down") from _call_her_main_676
                    call her_main("I'm not the cheerleader type!","angry","wink") from _call_her_main_677
                    call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") from _call_her_main_678
                    call her_main("My priority is to secure this years house-cup instead!","open","baseL") from _call_her_main_679
                    call her_main("I have to refuse, [genie_name].","soft","base") from _call_her_main_680
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Slytherin #Done
            elif skirt_choice == "uni_skirt_cheer" or skirt_choice == "uni_skirt_cheer_skimpy":
                if bottom_color_choice == "green" or bottom_color_choice == "blue" or bottom_color_choice == "yellow":
                    m "Would you wear this cheerleader skirt for me?" 
                    if whoring >= 11:
                        if whoring < 14:
                            if bottom_color_choice == "green":
                                call her_main("But [genie_name], that's for Slytherins!","angry","wink") from _call_her_main_681
                            if bottom_color_choice == "blue":
                                call her_main("But [genie_name], that's for Ravenclaws!","angry","wink") from _call_her_main_682
                            if bottom_color_choice == "yellow":
                                call her_main("But [genie_name], that's for Hufflepuffs!","angry","wink") from _call_her_main_683
                            m "And?"
                            call her_main("I'm a Gryffindor!","annoyed","annoyed") from _call_her_main_684
                            if bottom_color_choice == "green":
                                call her_main("(A muggle-born on top of that.)","disgust","down_raised") from _call_her_main_685
                            call her_main("I can't wear this!","open","worriedCl") from _call_her_main_686
                            m "Why not?"
                            call her_main("I've already told you, I'm a Gryffindor!","annoyed","ahegao") from _call_her_main_687
                            m "(...)"
                            g9 "(I've got an idea!)"
                            g4 "[hermione_name], I completely forgot to mention!"
                            m "As the top student of Gryffingdoor, you were selected to switch places with a fellow student form another house!"
                            m "As a form of bonding method... To bring the four houses closer together!"
                            call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","disgust","glance") from _call_her_main_688
                            g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students!"
                            if bottom_color_choice == "green":
                                m "Especially Gryffindor and Slytherin!"
                                m "I mean, do you like being called a mudblood every day by them?"
                                call her_main("No, [genie_name].","angry","wink") from _call_her_main_689
                                m "Or when they call you a slut..."
                                g4 "Or a whore!"
                                g9 "Or bitch!"
                                g4 "Or... a whore!"
                                g4 "Or--"
                                call her_main("I get your point, [genie_name]!!!","scream","worriedCl",cheeks="blush") from _call_her_main_690
                            m "I'm giving you an opportunity to better your relationship with them!"
                            m "Now are you going to wear this for me or not?..."
                            call her_main("(...)","annoyed","angryL") from _call_her_main_691
                            call her_main("Fine, [genie_name]... Let me just put it on.","annoyed","annoyed") from _call_her_main_692
                        elif whoring < 20:
                            call her_main("Fine, [genie_name].","soft","ahegao") from _call_her_main_693
                            call her_main("(How humiliating to wear this as a Gryffindor...)","disgust","narrow") from _call_her_main_694
                            call her_main("Let me just change it.","soft","baseL") from _call_her_main_695
                        else: #20+
                            if bottom_color_choice == "green":
                                call her_main("Of course I will wear it!","smile","angry") from _call_her_main_696
                                call her_main("Gimme-Gimme--Gimme!!!","smile","happyCl") from _call_her_main_697
                                call her_main("(I'm definitely going to root for them on the next game!)","soft","baseL",cheeks="blush") from _call_her_main_698
                                call her_main("(If they are winning I won't have to wear this thing long anyway!)","base","glance") from _call_her_main_699
                                call her_main("Whoooo, go Slytherin!","smile","happyCl") from _call_her_main_700
                            else:
                                call her_main("If I really have to...","annoyed","annoyed") from _call_her_main_701
                                call her_main("Let me just change it.","soft","baseL") from _call_her_main_702
                    else:
                        if bottom_color_choice == "green":
                            call her_main("In green?","shock","wide") from _call_her_main_703
                        if bottom_color_choice == "blue":
                            call her_main("In blue?","shock","wide") from _call_her_main_704
                        if bottom_color_choice == "yellow":
                            call her_main("In yellow?","shock","wide") from _call_her_main_705
                        call her_main("Are you serious, [genie_name]?","angry","angry") from _call_her_main_706
                        call her_main("Are you sure you didn't just pick the wrong colour for me?","annoyed","suspicious") from _call_her_main_707
                        if bottom_color_choice == "green":
                            m "(Something tells me she doesn't want to wear green stuff.)"
                            m "(Is she allergic to grasshoppers or something?)"
                        else:
                            m "(Could have sworn I picked the right color for her...)"
                        m "Forget about it, girl."
                        call her_main("I will!","annoyed","annoyed") from _call_her_main_708
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe

                else: #Gryffindor #Base color and red color.
                    m "Could you wear your cheerleader skirt for me?"
                    if whoring >= 5:
                        if whoring < 11:
                            call her_main("Of course, [genie_name]!","soft","baseL",cheeks="blush") from _call_her_main_709
                            call her_main("Let me go change.","base","base") from _call_her_main_710
                        else:
                            call her_main("Alright, [genie_name]!","soft","base") from _call_her_main_711
                            call her_main("Let me just change it.","base","glance") from _call_her_main_712
                    else:
                        call her_main("I don't know, [genie_name].","annoyed","down") from _call_her_main_713
                        call her_main("I'm not the cheerleader type!","angry","wink") from _call_her_main_714
                        call her_main("While I like the idea of supporting my house in Quidditch...","open","closed") from _call_her_main_715
                        call her_main("My priority is to secure this years house-cup instead!","open","baseL") from _call_her_main_716
                        call her_main("I have to refuse, [genie_name].","soft","base") from _call_her_main_717
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 5."
                        jump return_to_wardrobe
                    
                    
            ### Uniform Skirts Low ###

            #Uniform Skirt Low Very Long #Done
            elif skirt_choice == "uni_skirt_1_low":
                m "Would you wear your school skirt for me? The very long one. But pull it down a bit." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","base","down") from _call_her_main_718
                        call her_main("Let me go and change real quick.","base","base") from _call_her_main_719
                    elif whoring < 20:
                        call her_main("Are you sure, [genie_name]?","disgust","down_raised") from _call_her_main_720
                        call her_main("That thing looks rather plain...","open","closed") from _call_her_main_721
                        call her_main("I would much rather wear one a bit shorter!","angry","wink") from _call_her_main_722
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Ugh... Fine.","disgust","down_raised") from _call_her_main_723
                        call her_main("Let me just change it.","annoyed","annoyed") from _call_her_main_724
                    else: #20+
                        call her_main("Are you serious?","angry","wink") from _call_her_main_725
                        call her_main("That thing is soooooo ugly!","annoyed","ahegao") from _call_her_main_726
                        call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","disgust","narrow") from _call_her_main_727
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Fine... Just let me change it...","disgust","glance") from _call_her_main_728
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") from _call_her_main_729
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") from _call_her_main_730
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") from _call_her_main_731
                        call her_main("(disgusting old fool...)","annoyed","annoyed") from _call_her_main_732
                    else:
                        call her_main("No, [genie_name].","open","closed") from _call_her_main_733
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") from _call_her_main_734
                        call her_main("My panties would be visible...","disgust","down_raised") from _call_her_main_735
                        m "That's kind of the point, [hermione_name]."
                        call her_main("I refuse!","annoyed","annoyed") from _call_her_main_736
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Medium Length #Done
            elif skirt_choice == "uni_skirt_2_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("Alright... sure, why not.","base","down") from _call_her_main_737
                        call her_main("Let me go and change real quick.","base","base") from _call_her_main_738
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_739
                        call her_main("Let me go and change real quick.","base","glance") from _call_her_main_740
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_741
                        call her_main("(At least it is short enough...)","annoyed","ahegao") from _call_her_main_742
                        call her_main("OK, [genie_name].","soft","baseL") from _call_her_main_743
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_744
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") from _call_her_main_745
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") from _call_her_main_746
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") from _call_her_main_747
                        call her_main("(disgusting old fool...)","annoyed","annoyed") from _call_her_main_748
                    else:
                        call her_main("No, [genie_name].","open","closed") from _call_her_main_749
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") from _call_her_main_750
                        call her_main("My panties would be visible...","disgust","down_raised") from _call_her_main_751
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","open","closed") from _call_her_main_752
                        call her_main("I refuse!","annoyed","annoyed") from _call_her_main_753
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Short #Done
            elif skirt_choice == "uni_skirt_3_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("Of course, [genie_name].","soft","baseL") from _call_her_main_754
                        call her_main("Let me go and change real quick.","base","glance") from _call_her_main_755
                    else: #20+
                        call her_main("(...)","annoyed","annoyed") from _call_her_main_756
                        call her_main("(At least it is short enough...)","annoyed","ahegao") from _call_her_main_757
                        call her_main("OK, [genie_name].","soft","baseL") from _call_her_main_758
                        call her_main("Let me just change real quick.","base","glance") from _call_her_main_759
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","shock","wide") from _call_her_main_760
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","angry","angry") from _call_her_main_761
                        call her_main("How can you even suggest such a thing!","angry","worriedCl") from _call_her_main_762
                        call her_main("(disgusting old fool...)","annoyed","annoyed") from _call_her_main_763
                    else:
                        call her_main("No, [genie_name].","open","closed") from _call_her_main_764
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","annoyed","annoyed") from _call_her_main_765
                        call her_main("My panties would be visible...","disgust","down_raised") from _call_her_main_766
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","open","closed") from _call_her_main_767
                        call her_main("I refuse!","annoyed","annoyed") from _call_her_main_768
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Shortest (Micro Skirt) #Not implemented.
            elif skirt_choice == "uni_skirt_4_low":
                m "Could you wear this school skirt for me?" 
                ">You hand her the micro skirt." 
                if whoring >= 20:
                   call her_main("","base","base") from _call_her_main_769
                else:
                    call her_main("","base","base") from _call_her_main_770
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe


            ### Skirts ###
                    
            #Belted Mini Skirt #Done
            elif skirt_choice == "skirt_belted_mini":
                m "Could you wear this skirt I bought you?" 
                if whoring >= 8: 
                    if whoring < 14:
                        call her_main("(It's so short!)","disgust","down_raised") from _call_her_main_771
                        call her_main("(...)","annoyed","angryL") from _call_her_main_772
                        call her_main("Ok, [genie_name]... I will wear it.","open","closed") from _call_her_main_773
                        m "Really?"
                        call her_main("Give me the skirt before I change my mind!","annoyed","annoyed") from _call_her_main_774
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_775
                        call her_main("Let me just put it on.","base","glance") from _call_her_main_776
                    else: #23+
                        call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_777
                        call her_main("Give it to me!","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_778
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","base","glance") from _call_her_main_779
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_780
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_781
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_782
                    else: 
                        call her_main("Absolutely not, [genie_name]!","scream","worriedCl") from _call_her_main_783
                        call her_main("I'm not going to wear a skirt that short!","angry","angry") from _call_her_main_784
                        call her_main("(What is he thinking?...)","angry","worried") from _call_her_main_785
                        call her_main("I refuse","annoyed","annoyed") from _call_her_main_786
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Belted Micro Skirt #Done
            elif skirt_choice == "skirt_belted_micro":
                m "Could you wear this skirt I bought you?"
                if whoring >= 17: 
                    if whoring < 23: 
                        call her_main("(Oh wow, it's so short!)","disgust","down_raised") from _call_her_main_787
                        call her_main("(Everyone will be able to see my ass in this...)","soft","ahegao") from _call_her_main_788
                        call her_main("(...)","annoyed","angryL") from _call_her_main_789
                        call her_main("I will wear it!.","open","closed") from _call_her_main_790
                        m "Really?"
                        call her_main("Sure... It's short enough","soft","baseL") from _call_her_main_791
                        call her_main("Or would you say this is too inappropriate to wear in this school?","base","glance") from _call_her_main_792
                        g4 "Grrrrr--... You have my approval!"
                        call her_main("Thank you, [genie_name].","soft","baseL") from _call_her_main_793
                    else: #23+
                        call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_794
                        call her_main("Give it to me!","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_795
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","base","glance") from _call_her_main_796
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","base","base") from _call_her_main_797
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","open","closed") from _call_her_main_798
                        call her_main("I have to refuse, [genie_name].","normal","base") from _call_her_main_799
                    else: 
                        call her_main("Absolutely not, [genie_name]!","scream","worriedCl") from _call_her_main_800
                        call her_main("I'm not going to wear a skirt that short!","angry","angry") from _call_her_main_801
                        call her_main("(What is he thinking?...)","angry","worried") from _call_her_main_802
                        call her_main("I refuse","annoyed","annoyed") from _call_her_main_803
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe


            ### Pants ###
                    
            #Pants Jeans Long #Done
            elif skirt_choice == "pants_jeans_long":
                m "Could you wear these pants for me?" 
                if whoring >= 2: 
                    if whoring < 5:
                        call her_main("[genie_name], those are jeans!","angry","wink") from _call_her_main_804
                        m "... yes?"
                        call her_main("Muggle pants!","disgust","down_raised",cheeks="blush") from _call_her_main_805
                        call her_main("Girls are supposed to wear skirts here at Hogwarts!","open","closed") from _call_her_main_806 
                        call her_main("At all times! No exceptions!","annoyed","worriedL") from _call_her_main_807
                        m "That's a very sexist thing to say, don't you think?"
                        call her_main("I-- uhm...","angry","wink") from _call_her_main_808
                        call her_main("(Crap,... he is right...)","disgust","down_raised") from _call_her_main_809
                        call her_main("(Hmm... might as well wear them... They don't look too bad...)","clench","down_raised") from _call_her_main_810
                        m "(...)"
                        g4 "(How ridiculous!... How can she call those blankets around her hips skirts...)"
                        g9 "(At least I get a nice view of her ass in those pants!)"
                        call her_main("Fine, [genie_name].","annoyed","ahegao") from _call_her_main_811
                        call her_main("I will wear them.","soft","base") from _call_her_main_812
                    elif whoring < 8:
                        call her_main("Sure, [genie_name].","soft","baseL") from _call_her_main_813
                        call her_main("Let me go change.","base","base") from _call_her_main_814
                    else:
                        call her_main("But they are so long, [genie_name]!","annoyed","ahegao") from _call_her_main_815
                        call her_main("I can't even show off my legs in those!","annoyed","angry") from _call_her_main_816
                        call her_main("(They make my ass look amazing though...)","disgust","down_raised") from _call_her_main_817
                        call her_main("(Now that I think about it...)","annoyed","ahegao") from _call_her_main_818
                        call her_main("Fine, I will wear them.","base","glance") from _call_her_main_819
                else:
                    call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_820
                    call her_main("But pants are not part of Hogwarts' school attire.","open","closed") from _call_her_main_821
                    call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") from _call_her_main_822
                    call her_main("I have to refuse!","normal","base") from _call_her_main_823
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Pants Jeans Short #Done
            elif skirt_choice == "pants_jeans_short":
                m "Could you wear those pants for me?" 
                if whoring >= 11:
                    if whoring < 20:
                        call her_main("Sure, [genie_name].","soft","baseL") from _call_her_main_824
                        call her_main("Let me go change.","base","base") from _call_her_main_825
                    else: #20+
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_826
                        call her_main("(They are sooo tight,... I can barely even fit my ass into them...)","soft","ahegao") from _call_her_main_827
                        call her_main("Let me put them on for you.","base","glance") from _call_her_main_828
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_829
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") from _call_her_main_830
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") from _call_her_main_831
                        call her_main("I have to refuse!","normal","base") from _call_her_main_832
                    elif whoring < 5: 
                        call her_main("... What are these?","annoyed","suspicious") from _call_her_main_833
                        m "Pants..?"
                        call her_main("...","annoyed","annoyed") from _call_her_main_834
                        call her_main("These aren't pants!","angry","worriedCl") from _call_her_main_835
                        m "What are they then?"
                        call her_main("Underwear!","shock","wide") from _call_her_main_836
                        m "So you're not going to wear them?"
                        call her_main("NO!","scream","worriedCl") from _call_her_main_837
                        call her_main("...","angry","angry") from _call_her_main_838
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_839
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") from _call_her_main_840
                        call her_main("(They look really nice though...)","base","down") from _call_her_main_841
                        call her_main("(Maybe next time...)","base","baseL") from _call_her_main_842
                        call her_main("I have to refuse.","soft","base") from _call_her_main_843
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pants Retro Shorts #Done
            elif skirt_choice == "pants_retro_shorts":
                m "I want you to wear these pants for me." 
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("(These pants look so short...)","disgust","down_raised") from _call_her_main_844
                        call her_main("(My ass is gonna be on display the whole time in those...)","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_845
                        call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_846
                        call her_main("Let me just change it.","base","glance") from _call_her_main_847
                    else: #20+
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_848
                        call her_main("I bet you love how my ass looks in those.","smile","glance") from _call_her_main_849
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","base","glance") from _call_her_main_850
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_851
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") from _call_her_main_852
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") from _call_her_main_853
                        call her_main("I have to refuse!","normal","base") from _call_her_main_854
                    elif whoring < 11: 
                        call her_main("No, [genie_name].","open","worriedCl") from _call_her_main_855
                        call her_main("I will not wear pants that short here in school!","angry","worried") from _call_her_main_856
                        call her_main("(What is he thinking?!...)","annoyed","angryL") from _call_her_main_857
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_858
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") from _call_her_main_859
                        call her_main("(They look really nice though...)","base","down") from _call_her_main_860
                        call her_main("(Maybe next time...)","base","baseL") from _call_her_main_861
                        call her_main("I have to refuse.","soft","base") from _call_her_main_862
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Pants Rocker Shorts #Done
            elif skirt_choice == "pants_rocker":
                m "I want you to wear these pants for me." 
                if whoring >= 20: 
                    if whoring < 23:
                        call her_main("(These pants are so short...)","disgust","down_raised") from _call_her_main_863
                        call her_main("(I'm such a pervert!)","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_864
                        call her_main("Alright, [genie_name].","smile","happyCl") from _call_her_main_865
                        call her_main("Let me just change it.","base","glance") from _call_her_main_866
                    else:
                        call her_main("Alright, [genie_name].","soft","baseL") from _call_her_main_867
                        call her_main("I bet you love how my ass looks in those.","smile","glance") from _call_her_main_868
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","base","glance") from _call_her_main_869
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_870
                        call her_main("But pants are not part of Hogwarts' school attire.","open","closed") from _call_her_main_871
                        call her_main("Besides, I feel more comfortable in my school skirt.","open","suspicious") from _call_her_main_872
                        call her_main("I have to refuse!","normal","base") from _call_her_main_873
                    elif whoring < 5: 
                        call her_main("What?!...","angry","angry") from _call_her_main_874
                        call her_main("What?!... What is this?","angry","angry",emote="01") from _call_her_main_875
                        m "I just said those are--"
                        call her_main("[genie_name]!","shock","wide") from _call_her_main_876
                        call her_main("You can't just hand underwear to your students!","angry","worried") from _call_her_main_877
                        m "Underwear?"
                        call her_main("Yes, underwear! Panties!","open","worriedCl") from _call_her_main_878
                        call her_main("What else can you possibly call this?","annoyed","annoyed") from _call_her_main_879
                        m "That's a perfectly fine pair of jeans!"
                        m "No need to make such a fuss about them!... Just put them on!"
                        call her_main("No I will not!","scream","worriedCl") from _call_her_main_880
                        call her_main("(Not in a million years...)","angry","angry") from _call_her_main_881
                    elif whoring < 11: 
                        call her_main("I'm sorry, [genie_name].","open","worriedCl") from _call_her_main_882
                        call her_main("But I will not wear pants that short on school grounds!","angry","worried") from _call_her_main_883
                        call her_main("(What is he thinking?!...)","annoyed","angryL") from _call_her_main_884
                    else: 
                        call her_main("I'm sorry, [genie_name].","soft","baseL") from _call_her_main_885
                        call her_main("But I don't think I should wear pants like those on school grounds...","open","closed") from _call_her_main_886
                        call her_main("(They look really nice though...)","base","down") from _call_her_main_887
                        call her_main("(Maybe next time...)","base","baseL") from _call_her_main_888
                        call her_main("I have to refuse.","soft","base") from _call_her_main_889
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
            else:
                pass

            hide screen hermione_main
            with d3

            pause.5

            call set_h_bottom(skirt_choice,bottom_color_choice) from _call_set_h_bottom

            call her_main("","","",xpos="wardrobe") from _call_her_main_890
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if skirt_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that skirt just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if skirt_choice == "uni_skirt_2" and whoring < 5: #no vest
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3" and whoring < 8: #no tie
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_4" and whoring < 14: #cleavage
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_5" and whoring < 17: #crop top
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer" and whoring < 5:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that skirt just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">She won't wear that skirt just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe

            if skirt_choice == "uni_top_cheer_skimpy" and whoring < 8:
                if (bottom_color_choice == "green" or bottom_color_choice == "dark_green" or bottom_color_choice == "blue" or bottom_color_choice == "dark_blue" or bottom_color_choice == "yellow"):
                    if whoring < 11:
                        ">She won't wear that skirt just yet."
                        if cheats_active or game_difficulty <= 2:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                else: #Gryffindor
                    ">She won't wear that skirt just yet."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe


            #Uniform Low
            if skirt_choice == "uni_skirt_1_low" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_2_low" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3_low" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            #if skirt_choice == "uni_skirt_4_low" and whoring < 20:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 2:
            #        ">Try again at whoring level 20."
            #    jump return_to_wardrobe

            #Skirts
            if skirt_choice == "skirt_belted_mini" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "skirt_belted_micro" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe

            #Pants
            if skirt_choice == "pants_jeans_long" and whoring < 2:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if skirt_choice == "pants_jeans_short" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_retro_shorts" and whoring < 17:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if skirt_choice == "pants_rocker" and whoring < 20:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 2:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe



            else:
                pass

            $ wardrobe_active = 1
            call set_h_bottom(skirt_choice,bottom_color_choice) from _call_set_h_bottom_1
            call her_main("","","",xpos="wardrobe") from _call_her_main_891
            call screen wardrobe



### Equip Astoria's Bottom ###
label equip_ast_bottom: 
    call set_ast_bottom(skirt_choice) from _call_set_ast_bottom
        
    hide screen wardrobe
    call screen wardrobe

### Equip Susan's Bottom ###
label equip_sus_bottom:
    call set_sus_bottom(skirt_choice) from _call_set_sus_bottom

    hide screen wardrobe
    call screen wardrobe

