

### Tonks Chitchats ###

label tonks_chit_chat:

    $ chitchated_with_tonks = True
    
    ### Susan Spell level 1 ###
    if whoring >= 0: #PLACEHOLDER FOR SUSANS LEVEL #JUST FOR TESTING
        if one_out_of_three == 1:
            call ton_main("Susan is such a lovely girl...","open","base","base","mid")
            call ton_main("But she really isn't very confident in her body...","open","base","raised","R")
            call ton_main("I do hope your little games can help her opening up a bit...","base","base","base","mid")
        
        elif one_out_of_three == 2:
            call ton_main("Teaching has been so much fun!","open","base","raised","mid")
            call ton_main("It's so much better than working at the Ministry.","open","base","angry","mid")
            call ton_main("I can't believe how long I've spend in that shit-hole...","base","base","angry","R")

        else:
            call ton_main("I've spotted another cute little girl in my classes today...","open","base","angry","R")
            call ton_main("I hope she's as much into points as the rest.","horny","base","raised","mid")

    return
