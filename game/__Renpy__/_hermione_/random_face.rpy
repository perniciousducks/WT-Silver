

label set_her_face(change=None, mouth=None, eyes=None):
    hide screen hermione_main

    $ temp_mouth    = None
    $ temp_eyes     = None
    $ temp_eyebrows = None
    $ temp_pupils   = None
    $ temp_cheeks   = None
    $ temp_tears    = None
    $ temp_extra    = None
    $ temp_emote    = None

    if mouth != None:
        if mouth in ["neutral","sad"]:
            $ temp_mouth = renpy.random.choice(["normal","annoyed"])
        elif mouth in ["happy"]:
            $ temp_mouth = renpy.random.choice(["base","smile"])
        elif mouth in ["naughty","horny"]:
            $ temp_mouth = renpy.random.choice(["base","smile","grin","soft"])
            $ temp_cheeks =  renpy.random.choice(["blank","blush"])
        elif mouth in ["annoyed"]:
            $ temp_mouth = renpy.random.choice(["annoyed"])
        elif mouth in ["angry"]:
            $ temp_mouth = renpy.random.choice(["clench","angry"])

    if eyes != None:
        if eyes in ["neutral"]:
            $ temp_eyes =  renpy.random.choice(["base","baseL"])
        elif eyes in ["happy"]:
            $ temp_eyes =  renpy.random.choice(["base","baseL","squint","happy","happyCl"])
        elif eyes in ["naughty","horny"]:
            $ temp_eyes =  renpy.random.choice(["base","baseL","down","ahegao","ahegao_raised","glance","glanceL"])
            $ temp_cheeks =  renpy.random.choice(["blank","blush"])
        elif eyes in ["annoyed"]:
            $ temp_eyes =  renpy.random.choice(["base","baseL","suspicious","angry","angryL","closed"])
        elif eyes in ["angry"]:
            $ temp_eyes =  renpy.random.choice(["angry","angryL","angryCl","frown"])
        elif eyes in ["sad"]:
            $ temp_eyes =  renpy.random.choice(["base","baseL","down"])


    #Completely random (out of all available layers.)
    if change in ["mouth"]:
        $ temp_mouth = renpy.random.choice(h_mouth_list)
    elif change in ["eyes"]:
        $ temp_eyes =  renpy.random.choice(h_eye_list)
    elif change in ["cheeks"]:
        $ temp_cheeks =  renpy.random.choice(h_cheeks_list)
    elif change in ["tears"]:
        $ temp_tears =  renpy.random.choice(h_tears_list)

    #Mood specific
    elif change in ["all","random"]:
        if her_mood > 0 and her_mood <= 10:
            call set_her_face(mouth="neutral", eyes="neutral")
        elif her_mood > 10:
            call set_her_face(mouth="angry", eyes="angry")
        else: # 0
            call set_her_face(mouth="happy", eyes="neutral")

    $ changeHermione(temp_mouth, temp_eyes, temp_cheeks, temp_tears, temp_extra, temp_emote)

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

define h_cheeks_list = [
    "blank",
    "blush",
    "freckles"
    ]

define h_tears_list = [
    "blank",
    "body",
    "crying", "crying_side",
    "down",
    "mascara", "mascara_crying", "mascara_soft",
    "messy",
    "soft", "soft_sweat",
    "sweat"
    ]
