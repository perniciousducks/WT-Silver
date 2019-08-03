

label set_ast_face(change=None, mouth=None, eyes=None, eyebrows=None, pupils=None):

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
            $ temp_mouth    = renpy.random.choice(["smile","pout"])
        elif mouth in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["smile","happy","grin"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["grin","clench"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["pout","upset"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["disgust","worried"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["clench"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base","base","closed"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base","happyCl"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["narrow","angry"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["narrow"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["wide","closed"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["angry"])

    if eyebrows != None:
        if eyebrows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base","wide"])
        elif eyebrows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base","angry"])
        elif eyebrows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["narrow"])
        elif eyebrows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["wide"])
        elif eyebrows in ["angry"]:
            $ temp_eyebrows = renpy.random.choice(["angry"])

    if pupils != None:
        if pupils in ["neutral"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["happy"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif pupils in ["naughty","horny"]:
            $ temp_pupils   = renpy.random.choice(["mid","L","R","down"])
        elif pupils in ["annoyed"]:
            $ temp_pupils   = renpy.random.choice(["mid","R"])
        elif pupils in ["disgusted"]:
            $ temp_pupils   = renpy.random.choice(["wide"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["angry","L"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(ast_mouth_layers)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(ast_eye_layers)
    elif change in ["eyebrows"]:
        $ temp_eyebrows = renpy.random.choice(ast_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(ast_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        if ast_mood >= 1:
            call set_ast_face(mouth="annoyed",eyes="annoyed",eyebrows="annoyed",pupils="annoyed")
        else:
            call set_ast_face(mouth="happy",eyes="happy",eyebrows="happy",pupils="happy")

    python:
        astoria_class.expression(mouth=temp_mouth, eyes=temp_eyes, eyebrows=temp_eyebrows, pupils=temp_pupils, cheeks=temp_cheeks, tears=temp_tears)
        astoria_class.special(emote=temp_emote)

    return

label astoria_face_layers:

    $ ast_mouth_layers  = ["clench",
                           "disgust",
                           "grin",
                           "happy",
                           "open",
                           "pout",
                           "scream",
                           "smile",
                           "tongue_disgust", "tongue_silly",
                           "upset",
                           "worried"
                           ]

    $ ast_eye_layers    = ["ahegao",
                           "angry",
                           "base",
                           "closed", "happyCl",
                           "narrow",
                           "wide",
                           "wink"
                           ]

    $ ast_brow_layers   = ["ahegao",
                           "angry",
                           "base",
                           "narrow",
                           "wide",
                           "worried"
                           ]

    $ ast_pupil_layers  = ["ahegao",
                           "angry",
                           "down",
                           "L",
                           "mid",
                           "R",
                           "wide"
                           ]

    return
