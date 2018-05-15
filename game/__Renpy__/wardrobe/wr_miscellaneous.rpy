


#Needs to be updated
label give_her_acc(acc_id):
    hide screen hermione_main
    with d5

    if acc_id == 8:#Transparent
        if transparency == 1:
            if whoring <= 11:
                jump too_much
            call her_main("You want me to make my clothes see through?","normal","worriedCl")
            call her_main("Really, [genie_name]!","scream","angryCl")
            m "Just a little bit."
            call her_main("Fine...","open","suspicious")
            call her_main("How much should I drink...","annoyed","worriedL")
            menu: 
                "-A little bit-":
                    $ transparency_amount = 0.8
                    call her_main("(at least This shouldn't be too noticable.","normal","worriedCl")
                "-A fair bit-" if whoring >= 20:
                    $ transparency_amount = 0.5
                    call her_main("(Hopefully it's not too bad","annoyed","worriedL")
                "-A lot-" if whoring >= 23:
                    $ transparency_amount = 0.3
                    call her_main("(...)","base","down")
                "-All of it-" if whoring == 24:
                    $ transparency_amount = 0.1
                    call her_main("...","grin","baseL")

            call her_main("Alright then...","annoyed","down")
            hide screen hermione_main
            with d5
            $ transparency = transparency_amount
            $ hermione_breasts = "characters/hermione/body/breasts/breasts_normal.png"
            show screen hermione_main
            with d5
        else:
            call her_main("You want me to wear new clothes?","annoyed","ahegao")
            call her_main("Oh... alright then [genie_name].","annoyed","down")
            hide screen hermione_main
            with d5
            $ transparency = 1
            show screen hermione_main
            with d5