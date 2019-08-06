

label set_ton_face(change=None, mouth=None, eyes=None, eyebrows=None, pupils=None, hair=None):
    hide screen tonks_main

    $ temp_mouth    = None
    $ temp_eyes     = None
    $ temp_eyebrows = None
    $ temp_pupils   = None
    $ temp_cheeks   = None
    $ temp_tears    = None
    $ temp_extra    = None
    $ temp_emote    = None

    if hair != None:
        if hair in ("angry"):
            $ tonks_class.get_cloth("hair").color = [[164, 34, 34, 255]] # red
        elif hair in ("annoyed"):
            $ tonks_class.get_cloth("hair").color = [[228, 93, 34, 255]] # orange
        elif hair in ("happy"):
            $ tonks_class.get_cloth("hair").color = [[240, 240, 50, 255]] # yellow
        elif hair in ("disgusted"):
            $ tonks_class.get_cloth("hair").color = [[111, 205, 75, 255]] # green
        elif hair in ("sad"):
            $ tonks_class.get_cloth("hair").color = [[64, 75, 205, 255]] # blue
        elif hair in ("naughty", "horny"):
            $ tonks_class.get_cloth("hair").color = [[242, 126, 168, 255]] # pink
        $ tonks_class.get_cloth("hair").cached = False


    #Face emotions
    if mouth != None:
        if mouth in ["neutral"]:
            $ temp_mouth    = renpy.random.choice(["base"])
        elif mouth in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["base","smile"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["horny"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["upset"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["angry","upset"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["angry"])

    if eyes != None:
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

    if eyebrows != None:
        if eyebrows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised"])
        elif eyebrows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base","raised","angry"])
        elif eyebrows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["base","angry"])
        elif eyebrows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["raised","worried"])
        elif eyebrows in ["angry"]:
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
    elif change in ["eyebrows"]:
        $ temp_eyebrows = renpy.random.choice(ton_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(ton_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        call set_ton_face(mouth="naughty",eyes="happy",eyebrows="happy",pupils="happy")

    python:
        tonks_class.expression(mouth=temp_mouth, eyes=temp_eyes, eyebrows=temp_eyebrows, pupils=temp_pupils, cheeks=temp_cheeks, tears=temp_tears)
        tonks_class.special(emote=temp_emote)

    return

label tonks_face_layers:

    $ ton_mouth_layers  = ["angry",
                           "base",
                           "horny",
                           "open",
                           "open_wide_tongue",
                           "scream",
                           "smile",
                           "upset"
                           ]

    $ ton_eye_layers    = ["base",
                           "closed",
                           "happyCl",
                           "shocked",
                           "wide"
                           ]

    $ ton_brow_layers   = ["angry",
                           "base",
                           "raised",
                           "sad",
                           "upset",
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
