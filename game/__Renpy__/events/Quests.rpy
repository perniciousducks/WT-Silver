

### Quests ###

# Add any event triggers to this list.
# Only one event can play for each day/night (this might change.)
# Add date specific events at the start of the list (create the date if it's not there.)


label quests:

    if day >= 1:
        if daytime:
            if not genie_intro.E1_complete:
                jump genie_intro_E1
        else:
            if ss_event_pause == 0 and not snape_intro.E1_complete:
                # Snape visits for the first time.
                jump snape_intro_E1

    if day >= 2:
        if not letter_from_hermione_B_OBJ.read:
            $ letter_from_hermione_B_OBJ.mailLetter()
        if daytime:
            if not genie_intro.E3_complete:
                jump genie_intro_E3
        else:
            if ss_event_pause == 0 and not snape_intro.E2_complete:
                # Snape's second visit.
                jump snape_intro_E2

    if day >= 3:
        if daytime:
            pass
        else:
            if ss_event_pause == 0 and not snape_intro.E3_complete:
                # Day of the duel.
                jump snape_intro_E3

    if day >= 4:
        if not letter_paperwork_unlock_OBJ.read:
            $ letter_paperwork_unlock_OBJ.mailLetter()
        if daytime:
            pass
        else:
            if ss_event_pause == 0 and not snape_intro.E5_complete:
                # You bother decide to just "roll with it"... Snape summon unlocked.
                jump snape_intro_E5

    if day >= 5:
        if daytime:
            if hg_event_pause == 0 and not hermione_intro.E1_complete:
                # Hermione shows up for the first time.
                jump hermione_intro_E1

    if day >= 6:
        if daytime:
            if hg_event_pause == 0 and hang_with_snape.E1_complete and not hermione_intro.E2_complete:
                # Second visit from Hermione. Says she sent a letter to the Minestry.
                jump hermione_intro_E2

    if day >= 7:
        if hermione_intro.E2_complete and not letter_favor_complaint_OBJ.read:
            $ letter_favor_complaint_OBJ.mailLetter()
        if daytime:
            pass
        else:
            if hg_event_pause == 0 and hang_with_snape.E2_complete and not hermione_intro.E3_complete:
                # Takes place after first special event with Snape, where he just complains about Hermione.
                # Hermione might have failed a test...
                jump hermione_intro_E3

    if day >= 8:
        if daytime:
            pass
        else:
            if hg_event_pause == 0 and hermione_intro.E3_complete and not hermione_intro.E4_complete:
                # She failed a test and cries.
                jump hermione_intro_E4

    if day >= 9:
        if daytime:
            if hg_event_pause == 0 and hermione_intro.E4_complete and not hermione_intro.E5_complete:
                # Hermione asks to be tutored. Summon unlocked!
                jump hermione_intro_E5

    if day >= 10:
        if daytime:
            if nt_event_pause == 0 and hermione_intro.E5_complete and not tonks_intro.E1_complete:
                # Tonks visits for the first time.
                jump tonks_intro_E1
        else:
            if tonks_intro.E1_complete and not tonks_intro.E2_complete:
                # Tonks has found no evidence so far.
                jump tonks_intro_E2

    if day >= 11:
        if daytime:
            pass
        else:
            if nt_event_pause == 0 and hang_with_snape.E3_complete and not tonks_intro.E3_complete:
                # Tonks becomes a teacher. Summon unlocked!
                jump tonks_intro_E3

    if day >= 13:
        if daytime:
            if hg_event_pause == 0 and hermione_intro.E5_complete and hang_with_snape.E3_complete and hang_with_tonks.E1_complete and not hermione_intro.E6_complete:
                # Hermione wants to buy favors. Favors unlocked!
                jump hermione_intro_E6

    if day >= 16:
        if daytime:
            if her_whoring >= 2 and cho_intro_state == "event_1":
                $ cho_intro_state = "event_2"
                jump cho_intro_1

    if day >= 25:
        if her_whoring >= 9 and not letter_curse_complaint_OBJ.read:
            $ letter_curse_complaint_OBJ.mailLetter()

    if day >= 26:
        if not deck_unlocked:
            $ letter_deck.mailLetter()



    # Cardgame
    if day >= twins_cards_delay:
        if deck_unlocked and twins_first_win and not twins_cards_stocked:
            $ letter_cards_store.mailLetter()

    if geniecard_level < 2 and snape_third_win and her_third_win and twins_second_win:
        $ letter_cardgame_t2.mailLetter()



    # Hermione events not triggered by a date.
    if hg_event_pause == 0:
        if daytime:

            # Ending events
            if her_whoring >= 15 and not event_chairman_happened:
                #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
                jump ball_quest_E1

            if her_whoring >= 15 and event_chairman_happened and not snape_against_chairman_hap:
                # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
                jump ball_quest_E2

            if her_whoring >= 18 and snape_against_chairman_hap and not have_no_dress_hap:
                #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
                jump ball_quest_E3

            if her_whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics:
                #Turns TRUE after Hermione comes and apologizes for the day (event) before.
                jump ball_quest_E4

            if collar == 5:
                $ hg_event_pause += 2
                jump collar_scene

        else:
            if gave_the_dress:
                jump ball_ending_E1

    # Luna events not triggered by a date.
    if ll_event_pause == 0:
        if daytime:

            # Intro
            if her_whoring >= 21 and not hat_known:
                jump hat_intro

            if luna_reverted and lun_whoring == -2:
                jump luna_reverted_greeting_1 #Sets lun_whoring to -1, returns next night.

            # Unlock reverted favors.
            if luna_reverted:

                # Masturbate
                if lun_whoring >= 0 and ll_pf_masturbate not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_masturbate)
                    $ lun_tier = 2
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(2, 3)

                    $ ll_pf_masturbate.start()

                # Blowjob
                if lun_whoring >= 3 and ll_pf_blowjob not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_blowjob)
                    $ lun_tier = 3
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(4, 6)

                    $ ll_pf_blowjob.start()

        else:
            if luna_known and not luna_unlocked:
                jump hat_intro_3

            # Unlock reverted favors.
            if luna_reverted:

                # Sex
                if lun_whoring >= 9 and ll_pf_sex not in ll_favor_list:
                    $ ll_favor_list.append(ll_pf_sex)
                    $ lun_tier = 4
                    call update_luna_favors

                    $ ll_event_pause += renpy.random.randint(2, 4)

                    $ ll_pf_sex.start()

    # Cho events not triggered by a date.
    if cc_event_pause == 0:
        if daytime:

            if huffl_matches_won == 1 and quidditch_commentator == "none":
                $ lock_cho_practice = True
                $ quidditch_commentator = "talk_with_hermione"
                jump quidditch_commentator_event_1

            if main_match_1_stage == "start":
                $ main_match_1_stage = "return" # Triggers the return during the evening.
                jump hufflepuff_match

        else:
            if cho_intro_state == "event_2": # Happens right after intro.
                $ cho_intro_state = "talk_with_snape"
                jump cho_intro_2

            if quidditch_match_in_progress:
                $ quidditch_match_in_progress = False
                jump quidditch_match_return

            if main_match_1_stage == "return":
                $ main_match_1_stage = "end"
                jump hufflepuff_match_return

    # Astoria events not triggered by a date.
    if ag_event_pause == 0:
        if daytime:
            if hermione_finds_astoria and not astoria_unlocked:
                $ astoria_unlocked = True
                jump astoria_captured_intro

    # Tonks events not triggered by a date.
    if nt_event_pause == 0:
        if daytime:
            pass
        else:
            if astoria_unlocked and not tonks_intro_happened:
                $ tonks_intro_happened = True
                $ nt_event_pause += 1
                jump tonks_intro_event

            # Snape prevents the ministry from detecting curses.
            if tonks_intro_happened and not spells_unlocked:
                $ spells_unlocked = True #Astoria can now use spells.
                $ nt_event_pause += 1
                jump snape_spell_intro

            # Tonks becomes a teacher.
            if third_curse_got_cast and not tonks_unlocked:
                $ tonks_unlocked = True
                $ astoria_intro_completed = True
                jump astoria_tonks_intro

    jump main_room



### Quests flags ###

label quest_init:

    if not hasattr(renpy.store,'genie_intro'):
        $ genie_intro   = quest_class(
        E1_complete=False,
        E2_complete=False,
        E3_complete=False,
        )

    if not hasattr(renpy.store,'snape_intro'):
        $ snape_intro   = quest_class(
        E1_complete=False,   # 1st visit
        E2_complete=False,   # 2nd visit
        E3_complete=False,   # 3rd visit, before the duel.
        duel_complete=False, # Duel
        E4_complete=False,   # After the duel.
        E5_complete=False,   # 4th visit, summon unlocked.
        )

    if not hasattr(renpy.store,'hang_with_snape'):
        $ hang_with_snape   = quest_class(
        E1_complete=False,   # I hate her!
        E2_complete=False,   # Let's ruin her!
        E3_complete=False,   # Discuss Tonks with Snape.
        E4_complete=False,   # Inform him that Tonks has joined you both.
        E5_complete=False,   # Tonks is teaching DAtDA. Snape might use Veritaserum on her...
        )

    if not hasattr(renpy.store,'hermione_intro'):
        $ hermione_intro   = quest_class(
        E1_complete=False, # 1st visit
        E2_complete=False, # 2nd visit, MRM + informed the Ministry.
        E3_complete=False, # 3rd visit, did she fail a test?
        E4_complete=False, # 4th visit, she's crying. Failed a test.
        E5_complete=False, # 5th visit, asks to be tutored, summon unlocked.
        E6_complete=False, # 6th visit, asks to buy favors, favors unlocked.
        )

    if not hasattr(renpy.store,'tonks_intro'):
        $ tonks_intro   = quest_class(
        E1_complete=False,   # 1st visit
        E2_complete=False,   # 2nd visit
        E3_complete=False,   # 3rd visit, summon unlocked.
        )

    if not hasattr(renpy.store,'hang_with_tonks'):
        $ hang_with_tonks   = quest_class(
        E1_complete=False,
        E2_complete=False,
        E3_complete=False,
        )

    return
