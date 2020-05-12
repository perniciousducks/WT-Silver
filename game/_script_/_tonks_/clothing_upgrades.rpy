label clothing_upgrades:

    call upgrades

    if _return is False:
        jump tonks_talk

    m "[tonks_name]..."
    m "Do you think you could change this outfit?"
    m "You know..."
    g9 "Make it sluttier!"
    call ton_main("Let me see...","base","base","base","down")

    show screen blkfade
    with d3

    call ton_main("Oh I really like this one.","open","base","raised","down")
    call play_sound("cloth_upgrade")
    call ton_main("I could make some adjustments here...","base","base","raised","down")
    call ton_main("Maybe make this a bit shorter and...","horny","base","base","down")
    call play_sound("giggle")

    hide screen blkfade
    with d3

    call ton_main("There you go, [ton_genie_name], all done.","base","base","base","mid")

    g9 "Nice!"
    m "Thanks a ton!"
    call ton_main("Don't mention it, [ton_genie_name].","base","base","base","mid")
    jump tonks_talk

    return

