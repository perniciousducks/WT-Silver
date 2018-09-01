

label set_her_face(face="random"):
    hide screen hermione_main

    if face != "random":
        if face in ["neutral"]:
            $ h_mouth = renpy.random.choice(["normal","annoyed"])
            $ h_eyes =  renpy.random.choice(["base","baseL"])
        elif face in ["happy"]:
            $ h_mouth = renpy.random.choice(["base","smile","grin"])
            $ h_eyes =  renpy.random.choice(["base","baseL","squint","happy","happyCl"])
        elif face in ["naughty"]:
            $ h_mouth = renpy.random.choice(["base","smile","grin","soft"])
            $ h_eyes =  renpy.random.choice(["base","baseL","down","ahegao","ahegao_raised","glance","glanceL"])
            $ h_cheeks =  renpy.random.choice(["blush","00_blank"])
        elif face in ["annoyed"]:
            $ h_mouth = renpy.random.choice(["annoyed"])
            $ h_eyes =  renpy.random.choice(["base","baseL","suspicious","angry","angryL","closed"])
        elif face in ["angry"]:
            $ h_mouth = renpy.random.choice(["clench","angry"])
            $ h_eyes =  renpy.random.choice(["angry","angryL","angryCl","frown"])
        else:
            pass

    else:
        if mad > 0 and mad <= 10:
            call set_her_face("neutral")
        elif mad > 10:
            call set_her_face("angry")
        else: # 0
            call set_her_face("happy")

    call h_update
    return
