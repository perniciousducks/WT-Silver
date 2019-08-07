init python:
    def stats_sortfilter(item, sortby=False):
        return item

####################################
############# Menu #################
####################################

default stats_show_locked = False

label stats_menu(xx=150, yy=90):

    $ hide_transitions = True
    $ renpy.suspend_rollback(True)
    # Styling
    if daytime:
        $ btn_hover = "#edc48240"
    else:
        $ btn_hover = "#7d75aa40"

    call update_stats

    # Stats dictionary
    $ stats_dict = {
                    "Genie": {"ico": "head_genie_1", "flag": True, "name": "Genie", "sex": "Yes", "height": "6.2ft", "weight": "200lb", "job": "Headmaster", "hates": "Lamps", "likes": "Tits"},
                    "Snape": {"ico": "head_snape_1", "flag": snape_unlocked, "name": "Severus Snape", "sex": "Male", "height": "5.9ft", "weight": "155lb", "job": "Teacher", "hates": "Everyone", "likes": "Rain"},
                    "Tonks": {"ico": "head_tonks_1", "flag": tonks_unlocked, "name": "Nymphadora Tonks", "sex": "Fluid", "height": "5.6ft", "weight": "130lb", "job": "Teacher", "hates": "Pineapple Pizza", "likes": "Girls"},
                    "Hermione": {"ico": "head_hermione_2", "flag": hermione_unlocked, "name": "Hermione Granger", "sex": "Female", "height": "5.2ft", "weight": "126lb", "job": "Student", "hates": "Slytherin", "likes": "Books"},
                    "Cho": {"ico": "head_cho_2", "flag": cho_unlocked, "name": "Cho Chang", "sex": "Female", "height": "5.1ft", "weight": "122lb", "job": "Student", "hates": "Hermione", "likes": "Winning"},
                    "Luna": {"ico": "head_luna_2", "flag": luna_unlocked, "name": "Luna Lovegood", "sex": "Female", "height": "5.2ft", "weight": "117lb", "job": "Student", "hates": "Wrackspurts", "likes": "{size=-2}Magical creatures{/size}"},
                    "Astoria": {"ico": "head_astoria_2", "flag": astoria_unlocked, "name": "Astoria Greengrass", "sex": "Female", "height": "5.0ft", "weight": "102lb", "job": "Student", "hates": "Rules", "likes": "Breaking them"},
                    "Susan": {"ico": "head_susan_2", "flag": susan_unlocked, "name": "Susan Bones", "sex": "Female", "height": "5.3ft", "weight": "135lb", "job": "Student", "hates": "Chores", "likes": "You {size=-4}Secretly..{/size}"}
                    }

    $ stats_categories_sorted = ["Genie", "Snape", "Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"] #"Ginny", "Daphne", "Padma", "Patil", "Myrtle", "Mafkin"
    $ stats_categories_sorted_length = len(stats_categories_sorted)

    $ current_category = stats_categories_sorted[0]
    $ current_item = stats_dict[current_category]
    $ current_subcategory = "overview"
    $ current_sorting = stats_show_locked

    $ category_items = stats_dict[current_category]
    $ menu_items = category_items
    $ menu_items_length = len(menu_items)

    label stats_menu_after_init:
    $ renpy.block_rollback()

    show screen bld1
    show screen stats_menu(xx, yy)
    show screen stats_menuitem(xx, yy)

    $ _return = ui.interact()

    hide screen bld1
    hide screen stats_menu
    hide screen stats_menuitem

    if _return[0] == "category":
        $ current_category = _return[1]
        $ category_items = stats_dict[current_category]
        $ menu_items = stats_sortfilter(category_items, current_sorting)
        $ menu_items_length = len(menu_items)
        $ current_item = stats_dict[current_category]
        #$ current_subcategory = "overview"
    elif _return[0] == "subcat":
        if _return[1] != current_subcategory:
            $ current_subcategory = _return[1]
    else:
        $ hide_transitions = False
        $ renpy.suspend_rollback(False)
        jump day_main_menu

    jump stats_menu_after_init

screen stats_menu(xx, yy):
    tag stats_menu
    zorder 4

    use top_bar_close_button
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"

        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "Show locked:" style "empty" xsize 195 ysize 32 text_align (0.4, 0.5) text_size 12 hover_background btn_hover action ToggleVariable("stats_show_locked", True, False)
                add "interface/general/"+str(interface_color)+"/check_"+str(stats_show_locked).lower()+".png" xalign 0.8 yoffset 2
        vbox:
            pos (6, 6)
            for category in stats_categories_sorted:
                if not stats_show_locked and not stats_dict[category]["flag"]:
                    pass
                else:
                    frame:
                        style "empty"
                        xsize 195
                        ysize 50
                        vbox:
                            if current_category == category:
                                if stats_dict[category]["flag"]:
                                    textbutton category xsize 195 ysize 48 style "empty" background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20
                                else:
                                    textbutton "???" xsize 195 ysize 48 style "empty" background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20
                            else:
                                if stats_dict[category]["flag"]:
                                    textbutton category xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 action Return(["category", category])
                                else:
                                    textbutton "???" xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 action Return(["category", category])
                            add "interface/achievements/"+interface_color+"/spacer_left.png"
                        add "interface/achievements/"+interface_color+"/iconbox.png" yoffset 1
                        if stats_dict[category]["flag"]:
                            $ image_zoom = crop_image_zoom("interface/icons/head/"+stats_dict.get(category).get("ico")+".png", 42, 42)
                        else:
                            $ image_zoom = crop_image_zoom("interface/icons/head/"+stats_dict.get(category).get("ico")+"_locked.png", 42, 42)
                        frame:
                            style "empty"
                            xsize 42
                            ysize 42
                            add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                        add "interface/achievements/glass_iconbox.png" pos (3, 3)

transform at_zoom(zoom=1.0):
    zoom zoom

screen stats_menuitem(xx, yy):
    tag stats_menuitem
    zorder 4
    frame:
        style "empty"
        pos (xx+217, yy-53)
        xsize 560 ysize 507

        #add "interface/achievements/inventory.png"
        add "interface/achievements/"+interface_color+"/panel.png"
        add "interface/achievements/markup.png"

        text "Characters" size 22 xalign 0.5 ypos 65

        hbox:
            pos (24, 70)
            textbutton "Overview" text_size 12 action [Return(["subcat", "overview"]), SelectedIf(current_subcategory=="overview")]
            textbutton "Details" text_size 12 action [Return(["subcat", "details"]), SelectedIf(current_subcategory=="details")]

        # Character sprites
        frame:
            style "empty"
            xsize 200 ysize 406
            align (1.0, 1.0)
            offset (-10, -4)

            if current_category == "Genie":
                add "characters/genie/base/base.png" zoom 0.346 align (1.0, 1.0) xzoom -1
            elif current_category == "Snape":
                if current_item["flag"]:
                    add "characters/snape/main/snape_09.png" zoom 0.34 align (0.9, 1.0)
                else:
                    add "interface/characters/snape_locked.png" zoom 0.34 align (0.9, 1.0)
            elif current_category == "Tonks":
                if current_item["flag"]:
                    add tonks_class.get_image() zoom 0.4 align (0.7, 1.0)
                else:
                    add "interface/characters/tonks_locked.png" zoom 0.4 align (0.7, 1.0)
            elif current_category == "Hermione":
                if current_item["flag"]:
                    frame:
                        style "empty"
                        #align (0.7, 1.0)
                        at at_zoom(0.75)
                        xoffset -395
                        yoffset -44

                        use hermione_main
                else:
                    add "interface/characters/hermione_locked.png" zoom 0.38 align (0.65, 1.0)
            elif current_category == "Cho":
                if current_item["flag"]:
                    add cho_class.get_image() zoom 0.4 align (0.65, 1.0)
                else:
                    add "interface/characters/cho_locked.png" zoom 0.4 align (0.65, 1.0)
            elif current_category == "Luna":
                if current_item["flag"]:
                    frame:
                        style "empty"
                        #align (0.7, 1.0)
                        at at_zoom(0.75)
                        xoffset -620
                        yoffset -44

                        use luna_main
                else:
                    add "interface/characters/luna_locked.png" zoom 0.38 align (0.75, 1.0)
            elif current_category == "Astoria":
                if current_item["flag"]:
                    add astoria_class.get_image() zoom 0.4 align (0.7, 1.0)
                else:
                    add "interface/characters/astoria_locked.png" zoom 0.38 align (0.7, 1.0)
            elif current_category == "Susan":
                if current_item["flag"]:
                    frame:
                        style "empty"
                        #align (0.7, 1.0)
                        at at_zoom(0.78)
                        xoffset -350
                        yoffset -62

                        use susan_main
                else:
                     add "interface/characters/susan_locked.png" zoom 0.385 align (0.65, 1.0)

        frame:
            style "empty"
            xsize 360 ysize 406
            yalign 1.0 xoffset 6

            if current_subcategory == "overview":
                if current_item["flag"]:
                    text current_item["name"] size 20 xalign 0.5 xanchor 0.5 ypos 5
                else:
                    text "???" size 20 xalign 0.5 xanchor 0.5 ypos 5

                vbox:
                    xoffset 10
                    hbox:
                        spacing 20
                        pos (10, 36)

                        vbox:
                            text "Sex:" size 15
                            text "Height:" size 15
                            text "Weight:" size 15

                        vbox:
                            spacing 3
                            if current_item["flag"]:
                                text current_item["sex"] size 12
                                text current_item["height"] size 12
                                text current_item["weight"] size 12
                            else:
                                text "unknown" size 12
                                text "unknown" size 12
                                text "unknown" size 12

                        vbox:
                            text "Job:" size 15
                            text "Hates:" size 15
                            text "Likes:" size 15

                        vbox:
                            spacing 3
                            if current_item["flag"]:
                                text current_item["job"] size 12
                                text current_item["hates"] size 12
                                text current_item["likes"] size 12
                            else:
                                text "unknown" size 12
                                text "unknown" size 12
                                text "unknown" size 12

                    if current_item["flag"]:
                        vbox:
                            yoffset 35
                            xoffset 50
                            #style "empty"
                            at at_zoom(0.62)
                            if current_category == "Genie":
                                use stat_bar(int(100/10), "-Lust-", "", 100)
                                use stat_bar(int(0/10), "-Sanity-", "", 0)
                                use stat_bar(int(imagination +bdsm_imagination/1), "-Imagination-", "", imagination +bdsm_imagination)
                                if not cheat_reading:
                                    use stat_bar(int(speed_writing/0.25), "-Speed Writing-", "", speed_writing)
                                    use stat_bar(int(speed_reading/0.25), "-Speed Reading-", "", speed_reading)
                                #text "Jerked off -"+str(phoenix_fed_counter)+"- times"
                            elif current_category == "Snape":
                                use stat_bar(int(3/1.0), "-Mood-" , "Grumpy", 3)
                                use stat_bar(int(sna_support/1.5), "-Support-", sna_support_word, sna_support)
                                use stat_bar(int(sna_friendship/10), "-Friendship-", sna_friendship_word, sna_friendship)
                            elif current_category == "Tonks":
                                use stat_bar(int(10/1.0), "-Mood-" , "Content", 10)
                                use stat_bar(int(ton_support/1.5), "-Support-", "Non-existent", ton_support)
                                use stat_bar(int(ton_friendship/10), "-Relationship-", ton_friendship_word, ton_friendship)
                            elif current_category == "Hermione":
                                use stat_bar(int(10-her_mood/1.0), "-Mood-" , her_mood_word, her_mood)
                                use stat_bar(int(her_whoring/2.4), "-Whoring-", her_whoring_word, her_whoring)
                                use stat_bar(int(her_reputation/2.4), "-Reputation-", her_reputation_word, her_reputation)
                                use stat_bar(int(her_tier/0.6), "-Favour Tier-", "", her_tier)
                                use stat_bar(int(her_tutoring/1.4), "-Tutoring-" , her_tutoring_word, her_tutoring)
                            elif current_category == "Cho":
                                use stat_bar(int(10-cho_mood/1.0), "-Mood-" , cho_mood_word, cho_mood)
                                use stat_bar(int(cho_whoring/0.9), "-Recklessness-", cho_whoring_word, cho_whoring)
                                use stat_bar(int(cho_reputation/0.9), "-Reputation-", cho_reputation_word, cho_reputation)
                                use stat_bar(int(cho_tier/0.6), "-Favour Tier-", "", cho_tier)
                                use stat_bar(int((huffl_matches_won+gryff_matches_won+slyth_matches_won)/0.6), "{size=-10}-Quidditch Training-{/size}" , "Not started", huffl_matches_won+gryff_matches_won+slyth_matches_won) # TODO: Add word list
                            elif current_category == "Luna":
                                use stat_bar(int(10-lun_mood/1.0), "-Mood-" , "Cheerful", lun_mood) # TODO: Add word list
                                use stat_bar(int(lun_whoring/0.9), "-Corruption-", "Naive", lun_whoring) # TODO: Add word list
                                use stat_bar(int(10/0.9), "-Reputation-", "Total Weirdo", 10) # Joke stat
                                use stat_bar(int(1/0.9), "-Favour Tier-", "", 1) # TODO: Add Luna tier
                                use stat_bar(int(0), "{size=-10}-Wrackspurts Therapy-{/size}" , "Not started", 0) # TODO: Add word list and variable
                            elif current_category == "Astoria":
                                use stat_bar(int(10-ast_mood/1.0), "-Mood-" , "Cheerful", ast_mood) # TODO: Add word list
                                use stat_bar(int(ast_affection/0.9), "-Affection-", "Non-existent", ast_affection) # TODO: Add word list
                                use stat_bar(int(3/0.9), "-Reputation-", "Mischevious", 4) # TODO: Add word list and variable, starts at level 4
                                use stat_bar(int(1/0.9), "-Favour Tier-", "", 1) # TODO: Add Astoria tier
                                use stat_bar(int(ast_training_counter/0.9), "-Spell training-" , "Not started", ast_training_counter) # TODO: Add word list
                            elif current_category == "Susan":
                                use stat_bar(int(10-sus_mood/1.0), "-Mood-" , "Cheerful", sus_mood) # TODO: Add word list
                                use stat_bar(int(sus_whoring/0.9), "-Confidence-", "Non-existent", sus_whoring) # TODO: Add word list
                                use stat_bar(int(0/0.9), "-Reputation-", "Invisible", 0) # TODO: Add word list and variable
                                use stat_bar(int(1/0.9), "-Favour Tier-", "", 1) # TODO: Add Susan tier
                                use stat_bar(int(0), "{size=-10}-Assertivness Training-{/size}" , "Not started", 0) # TODO: Add word list
            else:
                if current_item["flag"]:
                    vbox:
                        if current_category == "Genie":
                            use text_stat("Bird fed:")
                            use text_stat("- ", " times -", phoenix_fed_counter)
                            use text_stat("Bird petted:")
                            use text_stat("- ", " times -", phoenix_petted_counter)
                            use text_stat("You missed feeding your bird for:")
                            use text_stat("- ", " days...", (day - phoenix_fed_counter) )
                            use text_stat("If you were a Quidditch player, you'd be a:")
                            use text_stat("- \"", "\" -", genie_quid_position)

                        elif current_category == "Snape":
                            use text_stat("Hung out with Snape:")
                            use text_stat("- ", " times -", ss_he_counter)
                            use text_stat("Enjoyed some wine with Snape:")
                            use text_stat("- ", " times -", ss_he_drink.counter)

                        elif current_category == "Tonks":
                            use text_stat("Hung out with Tonks:")
                            use text_stat("- ", " times -", nt_he_counter)
                            use text_stat("Enjoyed some firewhisky with Tonks:")
                            use text_stat("- ", " times -", nt_he_drink.counter)
                            use text_stat("Hung out with Astoria:")
                            use text_stat("- ", " times -", ton_astoria_date_counter)
                            use text_stat("Tonks has sluttyfied:")
                            use text_stat("- ", "/7 outfits -", ton_clothing_upgrades)

                        elif current_category == "Hermione":
                            # Tier 1
                            use text_stat("You Jerked off in front of her:")
                            use text_stat("- ", " times -", her_jerk_off_counter)
                            use text_stat("You saw her panties:")
                            use text_stat("- ", " times -", hg_pf_admire_panties.counter)
                            use text_stat("You admired her tits:")
                            use text_stat("- ", " times -", hg_pf_admire_breasts.counter)
                            # Tier 2
                            use text_stat("You groped her:")
                            use text_stat("- ", " times -", hg_pf_grope.counter)
                            # Tier 3
                            use text_stat("Hermione has \"danced\" for you:")
                            use text_stat("- ", " times -", hg_pf_strip.counter)
                            # Tier 4
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Handjobs -", hg_pf_handjob.counter)
                            # Tier 5
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Blowjobs -", hg_pf_blowjob.counter)
                            use text_stat("Hermione has given you:")
                            use text_stat("- ", " Tit jobs -", hg_pf_titjob.counter)
                            # Tier 6
                            use text_stat("You've had sex with her:")
                            use text_stat("- ", " times -", hg_pf_sex.counter)

                        elif current_category == "Cho":
                            use text_stat("You Jerked off in front of her:")
                            use text_stat("- ", " times -", cho_jerk_off_counter)
                        elif current_category == "Luna":
                            pass
                        elif current_category == "Astoria":
                            pass
                        elif current_category == "Susan":
                            use text_stat("Times Cursed:")
                            use text_stat("- ", " times -", sus_curse_counter)
