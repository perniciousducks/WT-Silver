

#Door Events (Astoria wears random clothing.)

label astoria_summon_setup:
    
    if astoria_outfits_schedule:
        $ astoria.equip_random_outfit()

    $ astoria_wardrobe_unlocked = True

    call play_sound("door")
    call ast_chibi("stand","mid","base")
    with d3

    call play_music("astoria")
    if ast_mood != 0:
        call ast_main("[ast_genie_name]...", face="annoyed", xpos="base",ypos="base")
    elif one_of_ten < 4:
        call ast_main("Heya, [ast_genie_name]!", face="neutral", xpos="base",ypos="base")
    elif one_of_ten < 7:
        call ast_main("Hello, [ast_genie_name].", face="neutral", xpos="base",ypos="base")
    else:
        call ast_main("Hi, [ast_genie_name]!", face="happy", xpos="base",ypos="base")

    return
