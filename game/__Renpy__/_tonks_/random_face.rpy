

label set_ton_face(change=None, mouth=None, eyes=None, brows=None, pupils=None):
    hide screen tonks_main

    $ temp_mouth    = None
    $ temp_eyes     = None
    $ temp_eyebrows = None
    $ temp_pupils   = None
    $ temp_cheeks   = None
    $ temp_tears    = None
    $ temp_extra    = None
    $ temp_emote    = None


    #Face emotions
    if mouth != None:
        if mouth in ["neutral"]:
            $ temp_mouth    = renpy.random.choice(["base"])
        elif mouth in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["base","horny"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["base","horny"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["base"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["base"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["base"])

    if eyes != None: #Tonks needs more useful eye layers. She's only got 2.
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["base"])

    if brows != None:
        if brows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif brows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised"])
        elif brows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["raised","angry"])
        elif brows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["base","angry"])
        elif brows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["raised","worried"])
        elif brows in ["angry"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])

    if pupils != None:
        if pupils in ["neutral"]:
            $ temp_pupils   = renpy.random.choice(["mid"])
        elif pupils in ["happy"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["naughty","horny"]:
            $ temp_pupils   = renpy.random.choice(["mid","up","ahegao"])
        elif pupils in ["annoyed"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["disgusted"]:
            $ temp_pupils   = renpy.random.choice(["mid","down"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["mid"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(ton_mouth_layers)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(ton_eye_layers)
    elif change in ["brows"]:
        $ temp_eyebrows = renpy.random.choice(ton_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(ton_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        call set_ton_face(mouth="naughty",eyes="happy",brows="happy",pupils="happy")


    $ changeTonks(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return

label tonks_face_layers:

    $ ton_mouth_layers  = ["base",
                           "horny",
                           "open",
                           "open_wide_tongue"
                           ]

    $ ton_eye_layers    = ["base",
                           "wide"
                           ]

    $ ton_brow_layers   = ["angry",
                           "base",
                           "raised",
                           "wide",
                           "worried"
                           ]

    $ ton_pupil_layers  = ["ahegao", "ahegao_intense",
                           "down",
                           "L",
                           "mid",
                           "R",
                           "up",
                           "wide"
                           ]

    return
