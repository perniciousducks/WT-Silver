

label open_stat_menu:

    call update_unlocked_character_list
    call update_hermione
    call update_luna
    call update_astoria
    call update_susan
    call update_cho
    call update_genie
    call update_snape
    call update_tonks

    jump stat_screen_character


label stat_screen_character:
    call update_stats
    $ hide_transitions = True

    if charName == "hermione":
        call set_her_face("random")
        call her_main(xpos="wardrobe",ypos="base")
        call screen stat_menu("hermione")

    elif charName == "luna":
        call lun_main("","base","base","base","mid",xpos="wardrobe",ypos="base")
        call screen stat_menu("luna")

    elif charName == "astoria":
        call ast_main("","smile","base","base","mid",xpos="wardrobe",ypos="base")
        call screen stat_menu("astoria")

    elif charName == "susan":
        call sus_main("","base","base","base","mid",xpos="wardrobe",ypos="base")
        call screen stat_menu("susan")

    elif charName == "cho":
        call cho_main("","base","base","base","mid",xpos="wardrobe",ypos="base")
        call screen stat_menu("cho")

    elif charName == "genie":
        call gen_main(xpos="wardrobe",ypos="55",flip=True)
        call screen stat_menu("genie")

    elif charName == "snape":
        call sna_main("","snape_09",xpos="wardrobe",ypos="55")
        call screen stat_menu("snape")

    elif charName == "tonks":
        call ton_main("","base","base","base","mid",xpos="wardrobe",ypos="base")
        call screen stat_menu("tonks")

    elif charName=="Close":
        $charName ="genie"
        jump close_stats_screen

    show screen stat_menu(charName)

    $ charName = _return
    call hide_characters

    jump stat_screen_character

label close_stats_screen:
    hide screen stat_menu
    hide screen stat_content

    call hide_characters
    hide screen bld1

    $ hide_transitions = False

    jump day_main_menu


screen stat_menu(character=""):
    tag stat_menu
    zorder 4

    add "interface/stat_select/"+str(interface_color)+"/ground_stat_screen_"+str(wardrobe_color)+".png"


    use close_button

    #Character Buttons.

    use generic_character_select(unlocked_character_list, "-Character Select-")

    text "- Character Stats- " xalign 0.5 xpos 433 ypos 118 size 30

    if character == "genie":
        use charecter_name("genie")
        use genie_stat_menu

    if character == "snape":
        use charecter_name("snape")
        use snape_stat_menu

    if character == "hermione":
        use charecter_name(hermione_name)
        use hermione_stat_menu

    if character == "luna":
        use charecter_name(luna_name)
        use luna_stat_menu

    if character == "astoria":
        use charecter_name(astoria_name)
        use astoria_stat_menu

    if character == "susan":
        use charecter_name(susan_name)
        use susan_stat_menu

    if character == "cho":
        use charecter_name(cho_name)
        use cho_stat_menu

    if character == "tonks":
        use charecter_name(tonks_name)
        use tonks_stat_menu



#steps is how many bars should be fill where 10 is max
screen stat_bar(steps, top_text, buttom_text, stat_number, top_padding = 20):
    $stateFullImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Full.png"
    $stateEmptyImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Empty.png"

    #Just some padding
    frame:
        background #00000000
        ysize top_padding

    text top_text xalign 0.5 size 30 bold 0.1
    frame:
        background #00000000
        xalign 0.5
        ysize 30
        xsize 360
        add LiveCrop((0, 0, steps*36, 600), stateFullImage)
        add stateEmptyImage
    text "" +buttom_text+ " (lvl " +str(stat_number)+ ")" xalign 0.5 size 20



screen text_stat(startText="", endText="", amount="", top_padding = 20):
    #Just some padding
    frame:
        background #00000000
        ysize top_padding

    text (startText +str(amount)+ endText) xpos 20 size 20

screen charecter_name(name):

    text ""+name xalign 0.5 xpos 820 ypos 57 size 20



### Character Stats ###

screen genie_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(100/10), "-Lust-", "", 100)
                use stat_bar(int(0/10), "-Sanity-", "", 0)

                use text_stat("Bird fed:")
                use text_stat("- ", " times -", phoenix_fed_counter)
                use text_stat("Bird petted:")
                use text_stat("- ", " times -", phoenix_petted_counter)
                use text_stat("You didn't feed your bird for ", " days...", (day - phoenix_petted_counter) )

        vbar value YScrollValue("vp")

    zorder 8

screen snape_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(sna_support/1.5), "-Support-", sna_support_word, sna_support) #Max is 15

                use stat_bar(int(sna_friendship/10), "-Friendship-", sna_friendship_word, sna_friendship)   #max is 100.

                use text_stat("Hung out with Snape:")
                use text_stat("- ", " times -", sna_dates_counter)
                use text_stat("Enjoyed some wine with Snape:")
                use text_stat("- ", " times -", sna_wine_counter)

        vbar value YScrollValue("vp")

    zorder 8


screen hermione_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(her_whoring/2.4), "-Whoring-", her_whoring_word, her_whoring) #Max 24

                use stat_bar(int(her_reputation/2.4), "Reputation", her_reputation_word, her_reputation) #Max 24

                use stat_bar(int(her_tutoring/1.4), "-Tutoring-" , her_tutoring_word, her_tutoring) #Max 14

                #Imagination 2:
                use text_stat("You Jerked off in front of her:")
                use text_stat("- ", " times -", her_jerk_off_counter)
                use text_stat("You saw her panties:")
                use text_stat("- ", " times -", hg_pf_NicePanties_OBJ.points)

                #Imagination 2:
                if imagination >= 2:
                    use text_stat("You admired her tits:")
                    use text_stat("- ", " times -", hg_pf_BreastMolester_OBJ.points)
                    use text_stat("You admired her butt:")
                    use text_stat("- ", " times -", (hg_pf_ButtMolester_OBJ.points + hg_pf_ShowMeYourAss_OBJ.points) )
                else:
                    use text_stat("Hidden")
                    use text_stat("Hidden")

                #Imagination 3:
                if imagination >= 3:
                    use text_stat("Hermione has danced for you:")
                    use text_stat("- ", " times -", hg_pf_DanceForMe_OBJ.points)
                else:
                    use text_stat("Hidden")

                #Imagination 4:
                if imagination >= 4:
                    use text_stat("Hermione has masturbated for you:")
                    use text_stat("- ", " times -", hg_pf_TouchYourself_OBJ.points)
                    use text_stat("Hermione has given you:")
                    use text_stat("- ", " Handjobs -", hg_pf_TouchMe_OBJ.points)
                    use text_stat("- ", " Blowjobs -", hg_pf_SuckIt_OBJ.points)
                    use text_stat("- ", " Tit jobs -", hg_pf_TitJob_OBJ.points)
                else:
                    use text_stat("Hidden")
                    use text_stat("Hidden")
                    use text_stat("Hidden")
                    use text_stat("Hidden")

                #Imagination 5:
                if imagination >= 5:
                    use text_stat("You've had sex with her:")
                    use text_stat("- ", " times -", hg_pf_LetsHaveSex_OBJ.points)
                    use text_stat("You've had anal sex with her:")
                    use text_stat("- ", " times -", hg_pf_TimeForAnal_OBJ.points)
                else:
                    use text_stat("Hidden")
                    use text_stat("Hidden")

        vbar value YScrollValue("vp")

    zorder 8

screen luna_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(lun_corruption/2.4), "-Corruption-", "", lun_corruption)
                use stat_bar(int(lun_dom/2.4), "-Dom points-", "", lun_dom)
                use stat_bar(int(lun_sub/2.4), "-Sub points-", "", lun_sub)

        vbar value YScrollValue("vp")

    zorder 8

screen astoria_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(ast_spells[0]/0.4), "-Spells-", "", ast_spells[0]) #Max is 4
                use stat_bar(int(ast_training_counter/0.9), "-Training-", "", ast_training_counter) #Max is 9
                use stat_bar(int(ast_affection/0.3), "-Affection-", "", ast_affection) #Max is 4

        vbar value YScrollValue("vp")

    zorder 8

screen susan_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use text_stat("Times Cursed:")
                use text_stat("- ", " times -", sus_curse_counter)

        vbar value YScrollValue("vp")

    zorder 8

screen cho_stat_menu:
    zorder 8

screen tonks_stat_menu:
    tag stat_content
    side "c r":
        area (220, 150, 425, 420)

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                use stat_bar(int(69/6.9), "-Lust-", "", 69)
                #use stat_bar(int(sna_support/1.5), "-Support-", "", tonks_support) #Number of Tonks events.
                #use stat_bar(int(sna_friendship/10), "-Friendship-", "", tonks_friendship)   #max is 100.
                #use stat_bar(int(0/10), "-Reputation-", "", tonks_reputation)
                use stat_bar(int(ton_clothing_level/10), "-Sluttiness-", ton_sluttiness_word, ton_clothing_level)

                use text_stat("Hung out with Astoria:")
                use text_stat("- ", " times -", ton_astoria_date_counter)

                use text_stat("Tonks has sluttyfied:")
                use text_stat("- ", "/5 outfits -", ton_clothing_upgrades)

        vbar value YScrollValue("vp")

    zorder 8

label update_stats:
    #$ madWords = ["Happy", "Slightly upset", "annoyed", "upset", "very upset", "mad", "angry", "hateful", "despises you", "Furious", "Absolutely Furious"] #Her face will be angry if she's mad. No need to display a stat for it.

    #Hermione
    $ her_whoring_word_list = ["Pure", "Naive", "Curious", "Naughty", "Perverse", "Immoral", "Slutty", "Shameless", "Cumslut", "Total Cumslut", "Shameless Cumslut"]
    $ her_whoring_word = her_whoring_word_list[int(her_whoring/2.4)]

    $ her_reputation_word_list = ["Teacher's pet", "School star", "good girl", "minx", "slutty schoolgirl", "easy lay", "whore", "slut for sex", "gryffindor whore", "school cumdump", "mudblood cumdump"]
    #$ slutWords = ["Teacher's pet", "School star", "good girl", "principal's pet", "slutty schoolgirl", "slut", "principal's slut", "daddy's girl", "gryffindor slut", "Dumbledore's whore", "Dumbledore's cumdump"]

    $ her_tutoring_word_list = ["pure ", "naive", "tempted", "curious", "tainted", "eager", "sinful", "perverted", "corrupted", "depraved", "shattered"]
    $ her_tutoring_word = her_tutoring_word_list[int(her_tutoring/1.4)]

    if lock_public_favors:
        $ her_reputation_word = "- Locked Off -"
    else:
        $ her_reputation_word = her_reputation_word_list[int(her_reputation/2.4)]

    #Astoria
    #call astoria_clothing_level
    #$ ast_cuteness_word_list = ["Ugly Duckling", "Swot", "", "", "", "", "", "Cutypie", "", "", ""]
    #$ ast_cuteness_word = ast_cuteness_word_list[int(ast_clothing_level/10)]

    #Snape
    $ sna_friendship_word_list = ["Unknown", "College", "Confidant", "Trusted", "Acquaintance", "Friend", "Good friend", "Homie", "If I had to pick a dude...", "BFF", "Bros"]
    $ sna_friendship_word = sna_friendship_word_list[int(sna_friendship/10)]

    $ sna_support_word_list = ["Tight-Arse", "Miser", "Stingy", "Sparing", "Adequate", "Loose", "Easy", "Generous", "Frivolous", "Excessive", "Exorbitant"]
    $ sna_support_word = sna_support_word_list[int(sna_support/1.5)]

    #Tonks
    call tonks_clothing_level
    $ ton_sluttiness_word_list = ["Masochist", "Disgrace", "Street Whore", "Harlot", "Tart", "Sexually open", "Naughty Teacher", "Easy Going", "Professor", "Bore", "Nun"]
    $ ton_sluttiness_word = ton_sluttiness_word_list[int(ton_clothing_level/10)]

    return
