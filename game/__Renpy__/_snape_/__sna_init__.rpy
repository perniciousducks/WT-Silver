

label snape_init:

    if not hasattr(renpy.store,'sna_chibi_flip') or reset_persistants:
        $ snape_xpos = 525
        $ snape_ypos = 0
        $ snape_zorder = 5
        $ snape_flip = 1
        $ use_snape_head            = False

        $ s_sprite = "characters/snape/main/snape_01.png"

        $ sna_chibi_xpos    = 610
        $ sna_chibi_ypos    = 190
        $ sna_speed         = 2.0
        $ sna_chibi_flip    = 1
        $ sna_chibi_zorder  = 2

        $ sna_chibi_stand   = "characters/snape/chibis/snape_stand.png"
        $ sna_chibi_walk    = "snape_walk"

    return



label snape_progress_init:

    if not hasattr(renpy.store,'snape_busy') or reset_persistants:

        ###SNAPE STATS###
        $ snape_busy = False #When True, you can't summon Snape.

        $ sna_support = 0 #Controls how much points is awarded to SLYTHERIN daily.
        $ snape_events = 0 #Get's +1 point every time a special event with Snape happens.
        $ sna_dates_counter = 0
        $ sna_friendship = 0 #Get's +1 after every evening spent is Snape's company.
        $ sna_friendship_maxed = False


        ### SNAPE EVENTS ###
        $ snape_invited_to_watch = False #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.

        ### CHITCHATS WITH SNAPE ###
        $ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.



        ### SPECIAL DATES WITH SNAPE ###
        $ snape_unlocked = False
        $ hanging_with_snape = False #Removed! Not in use anymore!

    if not hasattr(renpy.store,'ss_he_counter'):
        $ ss_he_counter = 0
        $ ss_he_drink   = event_class(title = "Snape Wine", start_label = "snape_hangout", events = [
            [
            ["ss_he_wine_intro"],
            ["ss_he_wine_repeat"],
            ["ss_he_wine_intro_E2"]
            ]

            ],
            iconset = [["star_empty", "star_yellow"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    if not hasattr(renpy.store,'ss_he_story'):
        $ ss_he_story   = event_class(title = "Snape Stories", start_label = "snape_hangout", events = [
            [
            ["ss_he_story_E1"], # Teach me wand magic
            ["ss_he_story_intro_E2"], # More points for Slytherin
            ["ss_he_story_intro_E3"], # M.R.M. nonsense
            ["ss_he_story_intro_E4"], # Parallel worlds
            ["ss_he_story_intro_E5"], # Progress with Hermione?
            ["ss_he_story_E6"],       # Those nasty Slytherin Sluts!
            ["ss_he_story_intro_E7"], # Jasmine is a muggle
            ["ss_he_story_intro_E8"], # Flogging
            ["ss_he_story_intro_E9"], # Russian dream (replace this one)
            ["ss_he_story_intro_E10"],# The meaning of life
            ["ss_he_story_intro_E11"],# The great catastrophe
            ["ss_he_story_intro_E12"],# Albus might be dead?
            ["ss_he_story_intro_E13"],# Snape is happy
            ["ss_he_story_E14"],      # Choking Slytherin girls...
            ["ss_he_story_intro_E15"] # Busy days
            ]

            ],
            iconset = [["star_empty", "star_yellow"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
            )

    return
