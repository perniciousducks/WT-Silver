

label set_her_face(change=None, mouth=None, eyes=None, eyebrows=None, pupils=None):

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
            $ temp_mouth    = renpy.random.choice(["annoyed","base"])
        elif mouth in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["smile","grin"])
        elif mouth in ["naughty"]:
            $ temp_mouth    = renpy.random.choice(["grin","horny"])
        elif mouth in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["annoyed"])
        elif mouth in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["clench","annoyed"])
        elif mouth in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["clench","angry"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["happy"]:
            $ temp_eyes     = renpy.random.choice(["base"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes     = renpy.random.choice(["narrow","base"])
        elif eyes in ["annoyed"]:
            $ temp_eyes     = renpy.random.choice(["narrow"])
        elif eyes in ["disgusted"]:
            $ temp_eyes     = renpy.random.choice(["narrow"])
        elif eyes in ["angry"]:
            $ temp_eyes     = renpy.random.choice(["narrow","base"])

    if eyebrows != None:
        if eyebrows in ["neutral"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["happy"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["naughty","horny"]:
            $ temp_eyebrows = renpy.random.choice(["base"])
        elif eyebrows in ["annoyed"]:
            $ temp_eyebrows = renpy.random.choice(["worried"])
        elif eyebrows in ["disgusted"]:
            $ temp_eyebrows = renpy.random.choice(["base", "angry"])
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
            $ temp_pupils   = renpy.random.choice(["down"])
        elif pupils in ["angry"]:
            $ temp_pupils   = renpy.random.choice(["L"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth    = renpy.random.choice(h_mouth_list)
    elif change in ["eyes"]:
        $ temp_eyes     = renpy.random.choice(h_eye_list)
    elif change in ["eyebrows"]:
        $ temp_eyebrows = renpy.random.choice(ast_brow_layers)
    elif change in ["pupils"]:
        $ temp_pupils   = renpy.random.choice(ast_pupil_layers)

    #Mood specific
    elif change in ["all","random"]:
        if ast_mood >= 1:
            call set_her_face(mouth="annoyed",eyes="annoyed",eyebrows="annoyed",pupils="annoyed")
        else:
            call set_her_face(mouth="happy",eyes="happy",eyebrows="happy",pupils="happy")

    python:
        hermione.set_face(mouth=temp_mouth, eyes=temp_eyes, eyebrows=temp_eyebrows, pupils=temp_pupils, cheeks=temp_cheeks, tears=temp_tears)
        #hermione_class.special(emote=temp_emote)

    return



define h_mouth_list = [
    "angry",
    "annoyed",
    "base",
    "clench",
    "crooked_smile",
    "cum",
    "disgust",
    "full", "full_cum",
    "gag",
    "grin",
    "mad",
    "mouthpiece", "mouthpiece_drool",
    "normal",
    "open", "open_tongue",
    "open_wide_tongue", "open_wide_tongue_cum",
    "scream",
    "shock",
    "silly",
    "smile",
    "soft",
    "upset"
    ]

define h_eye_list = [
    "ahegao", "ahegao_intense", "ahegao_mad", "ahegao_raised", "ahegao_squint", "ahegao_wide",
    "angry", "angryCl", "angryL",
    "annoyed",
    "base", "baseL",
    "closed",
    "concerned",
    "dead", "dead_mad",
    "down", "down_raised",
    "frown",
    "glance", "glanceL",
    "happy", "happyCl",
    "narrow",
    "shocked", "shocked_raised",
    "silly",
    "soft",
    "squint", "squintL",
    "surprised",
    "suspicious",
    "wide", "wide_stare", "wideL",
    "wink",
    "worried", "worriedCl", "worriedL"
    ]

# TODO: Add eyebrows and pupils lists.
