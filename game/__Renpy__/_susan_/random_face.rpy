

label set_sus_face(change=None, mouth=None, eyes=None, brows=None, pupils=None):
    hide screen susan_main

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
            $ temp_mouth    = renpy.random.choice(["base","grin"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["base"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["upset"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["open"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["upset"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base","base","closed"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base","eager"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["base","suspicious"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["base","narrow","suspicious"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["wide"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["suspicious"])

    if brows != None:
        if brows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif brows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif brows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base","worried"])
        elif brows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])
        elif brows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["worried"])
        elif brows in ["angry"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])

    if pupils != None:
        if pupils in ["neutral"]:
            $ temp_pupils   = renpy.random.choice(["mid"])
        elif pupils in ["happy"]:
            $ temp_pupils   = renpy.random.choice(["mid","down"])
        elif pupils in ["naughty","horny"]:
            $ temp_pupils   = renpy.random.choice(["L","R","down"])
        elif pupils in ["annoyed"]:
            $ temp_pupils   = renpy.random.choice(["R","down"])
        elif pupils in ["disgusted"]:
            $ temp_pupils   = renpy.random.choice(["R","wide"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["mid"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(sus_mouth_layers)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(sus_eye_layers)
    elif change in ["brows"]:
        $ temp_eyebrows = renpy.random.choice(sus_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(sus_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        if sus_mood >= 1:
            call set_sus_face(mouth="annoyed",eyes="annoyed",brows="annoyed",pupils="annoyed")
        else:
            call set_sus_face(mouth="happy",eyes="happy",brows="happy",pupils="happy")


    $ changeSusan(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return

label susan_face_layers:

    $ sus_mouth_layers  = ["base",
                           "grin",
                           "open", "open_tongue", "open_wide",
                           "scream",
                           "upset"
                           ]

    $ sus_eye_layers    = ["base",
                           "closed",
                           "eager",
                           "narrow", "suspicious",
                           "wide",
                           "worriedCl"
                           ]

    $ sus_brow_layers   = ["angry",
                           "base",
                           "worried"
                           ]

    $ sus_pupil_layers  = ["down",
                           "L",
                           "mid",
                           "R",
                           "up",
                           "wide"
                           ]

    return
