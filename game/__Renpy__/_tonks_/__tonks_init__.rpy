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

    ###################
    # Public requests #
    ###################
    if not hasattr(renpy.store,'nt_pr_teach'):
        $ nt_pr_teach   = event_class(title = "Detention with Tonks.", start_label = "nt_pr_teach_start", events = [
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
        $ nt_pr_grope   = event_class(title = "Hands-on lessons!", start_label = "nt_pr_grope_start", events = [
            [
            ["nt_pr_grope_T1_E1"], # Slytherin boy
            ["nt_pr_grope_T1_E2"], # Ravenclaw boy
            ["nt_pr_grope_T1_E3"], # Potter & Weasley
            ["nt_pr_grope_T1_E4"]  # Slytherin girl
            ],

            [
            ["nt_pr_grope_T2_E1"], #
            ["nt_pr_grope_T2_E2"], #
            ["nt_pr_grope_T2_E3"], #
            ["nt_pr_grope_T2_E4"]  #
            ]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    if not hasattr(renpy.store,'nt_pr_kiss'):
        $ nt_pr_kiss   = event_class(title = "Oral practice!", start_label = "nt_pr_kiss_start", events = [
            [
            ["nt_pr_kiss_T1_E1"], #
            ["nt_pr_kiss_T1_E2"], #
            ["nt_pr_kiss_T1_E3"], #
            ["nt_pr_kiss_T1_E4"]  #
            ],

            [
            ["nt_pr_kiss_T2_E1"], #
            ["nt_pr_kiss_T2_E2"], #
            ["nt_pr_kiss_T2_E3"], #
            ["nt_pr_kiss_T2_E4"]  #
            ]

            ],
            iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

        $ nt_requests_list = [
            nt_pr_teach,
            nt_pr_grope,
            #nt_pr_kiss
            ]

    return
