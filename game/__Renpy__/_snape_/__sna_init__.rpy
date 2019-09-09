default snape_xpos = 525
default snape_ypos = 0
default snape_zorder = 5
default snape_flip = 1
default use_snape_head            = False

default s_sprite = "characters/snape/main/snape_01.png"

default sna_chibi_xpos    = 610
default sna_chibi_ypos    = 190
default sna_speed         = 2.0
default sna_chibi_flip    = 1
default sna_chibi_zorder  = 2

default sna_chibi_stand   = "characters/snape/chibis/snape_stand.png"
default sna_chibi_walk    = "snape_walk"

###SNAPE STATS###
default snape_busy = False #When True, you can't summon Snape.

default sna_support = 0 #Controls how much points is awarded to SLYTHERIN daily.
default snape_events = 0 #Get's +1 point every time a special event with Snape happens.
default sna_dates_counter = 0
default sna_friendship = 0 #Get's +1 after every evening spent is Snape's company.
default sna_friendship_maxed = False


# Snape events
default snape_invited_to_watch = False #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.

# Chitchat with snape
default chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.

default snape_unlocked = False

# Snape hangout events
default ss_he_counter = 0
default ss_he_drink   = event_class(title = "Snape Wine", start_label = "snape_hangout", events = [
    [
    ["ss_he_wine_intro"],
    ["ss_he_wine_repeat"],
    ["ss_he_wine_intro_E2"]
    ]

    ],
    iconset = [["star_empty", "star_yellow"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
    )

default ss_he_story   = event_class(title = "Snape Stories", start_label = "snape_hangout", events = [
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
