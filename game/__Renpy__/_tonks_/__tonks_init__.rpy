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
    return
