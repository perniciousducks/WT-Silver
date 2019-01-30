

label set_lun_face(change=None, mouth=None, eyes=None, brows=None, pupils=None):
    hide screen luna_main

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
            $ temp_mouth    = renpy.random.choice(["base","smile"])
        elif mouth in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["smile","grin", "smile_large"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["base","angry","clench","soft"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["normal","pout","upset"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["disgust"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["angry","clench","mad"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base","base","closed"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base","happyCl"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["seductive"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["annoyed","suspicious"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["base","suspicious"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["angry"])

    if brows != None:
        if brows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif brows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif brows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised"])
        elif brows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["angry","mad"])
        elif brows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["raised","sad"])
        elif brows in ["angry"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])

    if pupils != None:
        if pupils in ["neutral"]:
            $ temp_pupils   = renpy.random.choice(["L","R","up","down","downL"])
        elif pupils in ["happy"]:
            $ temp_pupils   = renpy.random.choice(["mid"])
        elif pupils in ["naughty","horny"]:
            $ temp_pupils   = renpy.random.choice(["mid","up","down","crossed"])
        elif pupils in ["annoyed"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R","down","downR"])
        elif pupils in ["disgusted"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R","down"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["mid"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(lun_mouth_layers)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(lun_eye_layers)
    elif change in ["brows"]:
        $ temp_eyebrows = renpy.random.choice(lun_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(lun_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        if lun_mood >= 1:
            call set_lun_face(mouth="annoyed",eyes="annoyed",brows="annoyed",pupils="annoyed")
        else:
            call set_lun_face(mouth="happy",eyes="happy",brows="happy",pupils="happy")


    $ changeLuna(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return

label luna_face_layers:

    $ lun_mouth_layers  = ["angry",
                           "base",
                           "clench",
                           "crazy",
                           "disgust",
                           "full",
                           "grin",
                           "mad",
                           "normal",
                           "open",   "open_tongue", "open_wide_tongue",
                           "pout",
                           "scream",
                           "shocked",
                           "silly",
                           "smile",  "smile_large",
                           "soft",
                           "upset"
                           ]

    $ lun_eye_layers    = ["angry",
                           "annoyed",
                           "base",
                           "closed",  "happyCl",
                           "mad",
                           "seductive",
                           "suspicious",
                           "wide",
                           "wink"
                           ]

    $ lun_brow_layers   = ["angry",
                           "base",
                           "mad",
                           "raised",
                           "sad"
                           ]

    $ lun_pupil_layers  = ["crossed",
                          "down",    "downL",
                          "empty",
                          "L",
                          "mid",
                          "R",
                          "up"
                          ]

    return
