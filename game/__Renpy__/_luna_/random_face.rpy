

label set_lun_face(face="random"):
    hide screen luna_main

    $ temp_mouth    = None
    $ temp_eyes     = None
    $ temp_eyebrows = None
    $ temp_pupils   = None
    $ temp_cheeks   = None
    $ temp_tears    = None
    $ temp_extra    = None
    $ temp_emote    = None

    if face != "random":

        if face in ["neutral"]:
            $ temp_mouth    = renpy.random.choice(["base","upset","worried"])
            $ temp_eyes     = renpy.random.choice(["base","closed","wink"])
            $ temp_eyebrows = renpy.random.choice(["base"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif face in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["base","worried"])
            $ temp_eyes     = renpy.random.choice(["base","happyCl","wink"])
            $ temp_eyebrows = renpy.random.choice(["base"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif face in ["naughty","horny"]:
            $ temp_mouth    = renpy.random.choice(["smile","upset","worried"])
            $ temp_eyes     = renpy.random.choice(["base","closed","wink"])
            $ temp_eyebrows = renpy.random.choice(["base","ahegao"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R","ahegao","down"])
        elif face in ["annoyed"]:
            $ temp_mouth    = renpy.random.choice(["disgust","upset","worried"])
            $ temp_eyes     = renpy.random.choice(["base","closed","wink"])
            $ temp_eyebrows = renpy.random.choice(["base","narrow"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif face in ["disgusted"]:
            $ temp_mouth    = renpy.random.choice(["disgust","tongue_disgust","worried"])
            $ temp_eyes     = renpy.random.choice(["base","baseL"])
            $ temp_eyebrows = renpy.random.choice(["base","worried"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif face in ["angry"]:
            $ temp_mouth    = renpy.random.choice(["clench","upset","scream"])
            $ temp_eyes     = renpy.random.choice(["base","closed","wink"])
            $ temp_eyebrows = renpy.random.choice(["base","angry"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])

        elif face in ["mouth"]:
            $ temp_mouth    = renpy.random.choice(["angry","base","clench","crazy","disgust","full","grin","mad","normal","open","open_tongue","open_wide_tongue","pout","scream","silly","smile","smile_large","soft","upset","yell"])
        elif face in ["eyes"]:
            $ temp_eyes     = renpy.random.choice(["angry","annoyed","base","closed","happyCl","mad","seductive","suspicious","wide","wink"])
        elif face in ["eyebrows"]:
            $ temp_eyebrows = renpy.random.choice(["angry","base","mad","raised","sad"])
        elif face in ["pupils"]:
            $ temp_pupils   = renpy.random.choice(["crossed","down","downL","empty","L","mid","nose","R","stareL","up"])

        else:
            pass

    else:
        call set_lun_face("happy")

    $ changeLuna(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return
