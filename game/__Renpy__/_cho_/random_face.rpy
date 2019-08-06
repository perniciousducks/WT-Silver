

label set_cho_face(change=None, mouth=None, eyes=None, eyebrows=None, pupils=None):

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
            $ temp_mouth    = renpy.random.choice(["base","smile"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["quiver","horny","soft"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["annoyed","pout"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["angry","upset"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["angry","upset"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base","base","closed"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["base","narrow"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["base","closed","narrow"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["base","narrow"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["angry","narrow"])

    if eyebrows != None:
        if eyebrows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised"])
        elif eyebrows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["base","angry"])
        elif eyebrows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised","sad"])
        elif eyebrows in ["angry"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])

    if pupils != None:
        if pupils in ["neutral"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["happy"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["naughty","horny"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R","down","up"])
        elif pupils in ["annoyed"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R","down","downR"])
        elif pupils in ["disgusted"]:
            $ temp_pupils   = renpy.random.choice(["mid","down"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["mid"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(cho_mouth_layers)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(cho_eye_layers)
    elif change in ["eyebrows"]:
        $ temp_eyebrows = renpy.random.choice(cho_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(cho_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        if cho_mood >= 1:
            call set_cho_face(mouth="annoyed",eyes="annoyed",eyebrows="annoyed",pupils="annoyed")
        else:
            call set_cho_face(mouth="happy",eyes="happy",eyebrows="happy",pupils="happy")

    #$ changeCho(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)
    python:
        cho_class.expression(mouth=temp_mouth, eyes=temp_eyes, eyebrows=temp_eyebrows, pupils=temp_pupils, cheeks=temp_cheeks, tears=temp_tears)
        cho_class.special(emote=temp_emote)

    return

label cho_face_layers:

    $ cho_mouth_layers  = ["angry",
                           "annoyed",
                           "base",
                           "horny",
                           "open",
                           "pout",
                           "quiver",
                           "scream",
                           "smile",
                           "soft",
                           "upset"
                           ]

    $ cho_eye_layers    = ["angry",
                           "base",
                           "closed",
                           "shocked",
                           "narrow",
                           "wide",
                           "wink"
                           ]

    $ cho_brow_layers   = ["angry",
                           "base",
                           "raised",
                           "sad"
                           ]

    $ cho_pupil_layers  = ["down", "downR",
                           "L",
                           "mid",
                           "R",
                           "up"
                           ]

    return
