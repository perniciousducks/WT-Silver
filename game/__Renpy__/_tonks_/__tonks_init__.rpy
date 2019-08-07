label tonks_init:
    if not hasattr(renpy.store,'tonks_xpos') or reset_persistants:
        $ tonks_xpos                = 600
        $ tonks_ypos                = 0
        $ tonks_zorder              = 5
        $ tonks_flip                = 1
        $ use_tonks_head            = False
        $ tonks_animation = None

        $ tonks_haircolor = [[243, 158, 189, 255]]
    return

label tonks_progress_init:
    if not hasattr(renpy.store,'tonks_unlocked') or reset_persistants:

        #Stats
        $ ton_friendship = 0 #Max is 100.
        $ ton_support = 0
        $ ton_reputation = 0
        $ ton_clothing_level = 100

        #Flags
        $ tonks_busy = False
        $ tonks_unlocked = False
        $ tonks_favors_unlocked = False
        $ tonks_requests_unlocked = False
        $ tonks_shaming_unlocked = False
        $ tonks_wardrobe_unlocked = False
        $ chitchated_with_tonks = False
        $ tonks_strip_happened = False #Tonks random clothing event.

        $ gave_tonks_gift    = False

        #Names
        $ tonks_name = "Tonks"
        $ ton_genie_name = "Professor"
        $ ton_astoria_name = "Cutie"

        #Stat Screen
        $ ton_clothing_upgrades = 0
        $ ton_astoria_date_counter = 0
        $ ton_hermione_date_counter = 0



    ### 1.37 updates ###

    if not hasattr(renpy.store,'ton_tier'):
        $ ton_tier = 1
        $ tonks_shared = False
        $ tonks_favors_unlocked   = False
        $ tonks_requests_unlocked = False
        $ tonks_shaming_unlocked  = False



    ### Tonks Hangout Events ###

    if not hasattr(renpy.store,'nt_he_counter'):
        $ nt_he_counter = 0
        $ nt_he_drink   = event_class(title = "Tonks Firewhisky", start_label = "tonks_hangout", events = [
            [
            ["nt_he_wine_intro"],
            ["nt_he_firewhisky_intro"],
            ["nt_he_firewhisky_E1"],
            ["nt_he_firewhisky_E2"],
            ["nt_he_firewhisky_E3"],
            ["nt_he_firewhisky_E4"]
            ]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    if not hasattr(renpy.store,'nt_he_story'):
        $ nt_he_story   = event_class(title = "Tonks Stories", start_label = "tonks_hangout", events = [
            [
            ["nt_he_story_intro_E1"], # Intro
            ["nt_he_story_intro_E2"], # Moody
            ["nt_he_story_intro_E3"], # Brooms and flying carpets
            ["nt_he_story_intro_E4"], # Turning water into wine
            ["nt_he_story_intro_E5"], # Lots of paperwork
            ["nt_he_story_E6"],       # Vampire story
            ["nt_he_story_intro_E7"], # Moody's teaching methods
            ["nt_he_story_E8"],       # Werewold story
            ["nt_he_story_intro_E9"], # Illegal love potion
            ["nt_he_story_intro_E10"], # Dumb game mechanics
            ["nt_he_story_E11"],      # Metamorphmagi
            ["nt_he_story_E12"]       # Invisible clothing charm
            ]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    ###################
    # Public requests #
    ###################

    if not hasattr(renpy.store,'nt_pr_teach'):
        $ nt_pr_teach   = event_class(title = "Detention with Tonks.", start_label = "nt_pr_teach_start", start_tier = 1, events = [
            [
            ["nt_pr_teach_T1_E1"], # Slytherin boy
            ["nt_pr_teach_T1_E2"], # Ravenclaw boy
            ["nt_pr_teach_T1_E3"], # Potter & Weasley
            ["nt_pr_teach_T1_E4"]  # Slytherin girl
            ],

            [
            ["nt_pr_teach_T2_E1"], # Hufflepuff girl
            ["nt_pr_teach_T2_E2"], # Ravenclaw boy
            ["nt_pr_teach_T2_E3"], # Slytherin boy
            ["nt_pr_teach_T2_E4"]  # Slytherin girl
            ]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    if not hasattr(renpy.store,'nt_pr_grope'):
        $ nt_pr_grope   = event_class(title = "Hands-on lessons!", start_label = "nt_pr_grope_start", start_tier = 2, events = [
            [
            ["nt_pr_grope_T1_E1"], # Slytherin boy
            ["nt_pr_grope_T1_E2"], # Ravenclaw boy
            ["nt_pr_grope_T1_E3"], # Potter & Weasley
            ["nt_pr_grope_T1_E4"]  # Slytherin girl
            ]#,

            #[
            #["nt_pr_grope_T2_E1"], #
            #["nt_pr_grope_T2_E2"], #
            #["nt_pr_grope_T2_E3"], #
            #["nt_pr_grope_T2_E4"]  #
            #]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    if not hasattr(renpy.store,'nt_pr_kiss'):
        $ nt_pr_kiss   = event_class(title = "Oral practice!", start_label = "nt_pr_kiss_start", start_tier = 2, events = [
            [
            ["nt_pr_kiss_T1_intro_E1"], # Ravenclaw boy
            ["nt_pr_kiss_T1_E2"],       #
            ["nt_pr_kiss_T1_E3"],       # Slytherin girls
            ["nt_pr_kiss_T1_E4"]        # Slytherin girl
            ]#,

            #[
            #["nt_pr_kiss_T2_E1"], # Slytherin boy
            #["nt_pr_kiss_T2_E2"], #
            #["nt_pr_kiss_T2_E3"], #
            #["nt_pr_kiss_T2_E4"]  #
            #]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    # Idea for "blowjob pr" name: "Stress Mitigation."

    $ nt_requests_list = [
        nt_pr_teach,
        nt_pr_grope,
        nt_pr_kiss
        ]

    return
