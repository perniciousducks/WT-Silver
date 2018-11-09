

label set_her_face(face="random"):
    hide screen hermione_main

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
            $ temp_mouth = renpy.random.choice(["normal","annoyed"])
            $ temp_eyes =  renpy.random.choice(["base","baseL"])
        elif face in ["happy"]:
            $ temp_mouth = renpy.random.choice(["base","smile","grin"])
            $ temp_eyes =  renpy.random.choice(["base","baseL","squint","happy","happyCl"])
        elif face in ["naughty","horny"]:
            $ temp_mouth = renpy.random.choice(["base","smile","grin","soft"])
            $ temp_eyes =  renpy.random.choice(["base","baseL","down","ahegao","ahegao_raised","glance","glanceL"])
            $ temp_cheeks =  renpy.random.choice(["blank","blush"])
        elif face in ["annoyed"]:
            $ temp_mouth = renpy.random.choice(["annoyed"])
            $ temp_eyes =  renpy.random.choice(["base","baseL","suspicious","angry","angryL","closed"])
        elif face in ["angry"]:
            $ temp_mouth = renpy.random.choice(["clench","angry"])
            $ temp_eyes =  renpy.random.choice(["angry","angryL","angryCl","frown"])

        elif face in ["mouth"]:
            $ temp_mouth = renpy.random.choice(h_mouth_list)
        elif face in ["eyes"]:
            $ temp_eyes =  renpy.random.choice(h_eye_list)
        elif face in ["cheeks"]:
            $ temp_cheeks =  renpy.random.choice(["blank","blush","freckles"])
        elif face in ["tears"]:
            $ temp_tears =  renpy.random.choice(["blank","body","crying","crying_side","down","mascara","mascara_crying","mascara_soft","messy","soft","soft_sweat","sweat"])

        else:
            pass

    else:
        if mad > 0 and mad <= 10:
            call set_her_face("neutral")
        elif mad > 10:
            call set_her_face("angry")
        else: # 0
            call set_her_face("happy")

    $ changeHermione(temp_mouth, temp_eyes, temp_cheeks, temp_tears, temp_extra, temp_emote)

    return
