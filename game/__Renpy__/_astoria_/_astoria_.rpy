

### Astoria Greengrass ###

label ast_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=False, tears=False, emote=False, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    #Flip
    if flip == False:
        $ astoria_flip = 1 #Default
    if flip == True:
        $ astoria_flip = -1

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
                $ astoria_xpos = -80
            else:
                $ astoria_xpos = 650
            $ astoria_ypos = 200
            $ astoria_zorder = 8
        else:
            $ astoria_ypos = int(ypos)

    if face:
        if not mouth:
            call set_ast_face(mouth = face)
        if not eyes:
            call set_ast_face(eyes = face)
        if not eyebrows:
            call set_ast_face(eyebrows = face)
        if not pupils:
            call set_ast_face(pupils = face)

    if animation != False:
        $ astoria_animation = animation

    python:
        astoria.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        #astoria_class.special(emote=emote)

    if not renpy.get_screen("wardrobe_menu"):
        show screen astoria_main()
    show screen bld1

    if trans:
        with trans

    if text:
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
    $ astoria_chibi.update()
    $ astoria_chibi.position(flip=False)
    $ astoria_flip = 1
    hide screen astoria_cloth_pile

    return

label end_astoria_event:
    call ast_chibi("hide")
    hide screen astoria_main
    with d3
    pause.5

    call update_astoria

    $ active_girl = None
    $ astoria_busy = True

    jump main_room

screen astoria_main():
    tag astoria_main
    zorder astoria_zorder
    default astoria_img = astoria.get_image()
    if astoria_animation != None:
        add astoria_img xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio) at astoria_animation
    else:
        add astoria_img xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)
    
    on ("show", "replace") action Function(apply_doll_transition, astoria, "astoria_main", "astoria_img", use_astoria_head)
