

label set_ast_face(face="random"):
    hide screen astoria_main

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
            $ temp_mouth    = renpy.random.choice(["smile","upset","worried"])
            $ temp_eyes     = renpy.random.choice(["base","closed","wink"])
            $ temp_eyebrows = renpy.random.choice(["base"])
            $ temp_pupils   = renpy.random.choice(["mid","L","R"])
        elif face in ["happy"]:
            $ temp_mouth    = renpy.random.choice(["smile","worried"])
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
            $ temp_mouth    = renpy.random.choice(["clench","disgust","grin","happy","open","pout","scream","smile","tongue_disgust","tongue_silly","upset","worried"])
        elif face in ["eyes"]:
            $ temp_eyes     = renpy.random.choice(["ahegao","angry","base","closed","happyCl","narrow","wide","wink"])
        elif face in ["eyebrows"]:
            $ temp_eyebrows = renpy.random.choice(["ahegao","angry","base","narrow","wide","worried"])
        elif face in ["pupils"]:
            $ temp_pupils   = renpy.random.choice(["ahegao","angry","down","L","mid","R","wide"])

        else:
            pass

    else:
        call set_ast_face("happy")

    $ changeAstoria(temp_mouth, temp_eyes, temp_eyebrows, temp_pupils, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return
