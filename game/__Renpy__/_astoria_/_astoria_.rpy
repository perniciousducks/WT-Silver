










label astoria_intro_branches: #This label runs every day and night. Never call to it!

    if not ministry_letter_received:

        if daytime:
            $ ministry_letter = True
            $ letters += 1 #Displays Owl

            jump day_resume

    #Talk to Hermione now.
    #Talk to Snape now.

    #Hermione finds Astoria. #Start of day.
    if daytime and hermione_finds_astoria and days_without_an_event >= 2 and not astoria_unlocked:
        $ astoria_unlocked = True
        $ days_without_an_event = 0
        jump astoria_captured_intro

    #Tonks intro.
    if astoria_unlocked and not tonks_intro_happened:
        $ tonks_intro_happened = True
        jump tonks_intro_event

    #Snape prevents the ministry from detecting curses.
    if tonks_intro_happened and not spells_unlocked:
        if daytime:
            pass
        else:
            $ spells_unlocked = True #Astoria can now use spells.
            jump snape_spell_intro

    #Talk to Astoria now. #Triggers Susan intro.

    #Talk to Snape now. #Snape gives you the book. Can be done later.

    #Tonks becomes a teacher.
    if third_curse_got_cast and not tonks_unlocked:
        $ tonks_unlocked = True
        $ astoria_intro_completed = True
        jump astoria_tonks_intro

    if daytime:
        jump day_resume
    else:
        jump night_resume





label set_ast_susan_name:
    $ ast_susan_name = renpy.random.choice(["Susy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    return

label set_ast_tonks_name:
    $ ast_tonks_name = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    return
