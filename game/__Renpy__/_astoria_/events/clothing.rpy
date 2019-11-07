

#Door Events (Astoria wears random clothing.)

label astoria_summon_setup:
    
    if astoria_outfits_schedule:
        $ tmp_outfits = get_character_outfits_schedule("astoria")
        if len(tmp_outfits) > 0:
            $ astoria_class.equip(renpy.random.choice(tmp_outfits))

    $ astoria_wardrobe_unlocked = True

    call play_sound("door")
    call ast_chibi("stand","mid","base")
    with d3

    call play_music("astoria_theme")
    if ast_mood != 0:
        call ast_main("[genie_name]...", face="annoyed", xpos="base",ypos="base")
    elif one_of_ten < 4:
        call ast_main("Heya, [genie_name]!", face="neutral", xpos="base",ypos="base")
    elif one_of_ten < 7:
        call ast_main("Hello, [genie_name].", face="neutral", xpos="base",ypos="base")
    else:
        call ast_main("Hi, [genie_name]!", face="happy", xpos="base",ypos="base")

    return
