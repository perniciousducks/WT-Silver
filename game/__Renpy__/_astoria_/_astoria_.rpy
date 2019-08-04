

### Astoria Greengrass ###

label ast_main(text="", mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    #Flip
    if flip == False:
        $ astoria_flip = 1 #Default
    if flip == True:
        $ astoria_flip = -1

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if extra == None:
        $ extra = "blank"
    if emote == None:
        $ emote = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the right.
            $ astoria_xpos = 640
        elif xpos == "mid":                # Centered.
            $ astoria_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ astoria_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ astoria_xpos = 540
        else:
            $ astoria_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ astoria_ypos = 0
            $ astoria_scaleratio = 2
            $ astoria_zorder = 5
            $ use_astoria_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_astoria_head = True
            $ astoria_scaleratio = 2

            if astoria_flip == -1: #Flipped
                $ astoria_xpos = 620
            else:
                $ astoria_xpos = 590
            $ astoria_ypos = 230
            $ astoria_zorder = 8
        else:
            $ astoria_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_ast_face(mouth = face)
        if eyes == None:
            call set_ast_face(eyes = face)
        if eyebrows == None:
            call set_ast_face(eyebrows = face)
        if pupils == None:
            call set_ast_face(pupils = face)
            
    if animation != False:
        $ astoria_animation = animation

    python:
        astoria_class.expression(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        astoria_class.special(emote=emote)

    show screen astoria_main()
    show screen bld1

    call transition(trans, True)

    if text != "":
        $ renpy.say(ast, text)

    if use_astoria_head:
        hide screen astoria_main

    return

label set_random_nicknames:
    $ random_number = renpy.random.randint(0, 5)
    if random_number in [1,5]:
        $ ast_susan_name = renpy.random.choice(["Susy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    if random_number in [2,5]:
        $ ast_tonks_name = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    if random_number in [3,5]:
        $ ton_astoria_name = renpy.random.choice(["Cutie","Kitty","Princess","Little girl","Honey"])

    return
            
label update_astoria:

    # Chibi Update
    $ update_chibi_image("astoria")
    $ astoria_flip = 1
    $ astoria_cloth_pile = False

    return
            
label end_astoria_event:
    #call astoria_chibi("hide") TODO: Fix me
    hide screen astoria_main
    with d3
    pause.5

    call update_astoria

    $ active_girl = None
    $ astoria_busy = True

    call music_block
    jump main_room

screen astoria_main():
    tag astoria_main
    zorder astoria_zorder
    if astoria_animation != None:
        add astoria_class.get_image() xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio) at astoria_animation
    else:
        add astoria_class.get_image() xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)