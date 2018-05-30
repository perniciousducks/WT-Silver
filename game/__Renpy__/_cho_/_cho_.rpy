

### Cho Chang ###

label cho_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None):
    if eye!=None and pupil!=None and eyebrow!=None and mouth!=None:
        $ changeCho(eye, eyebrow, pupil, mouth)

    if text != "":
        $ renpy.say(cho, text)

    return


label FH_day:
    # Increment shit
    if cho_known:
        $ days_since_cho += 1

    #reset cho's outfit just incase
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True

    return


