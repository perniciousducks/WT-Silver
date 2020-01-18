define her_face = {"mouth": {"neutral": ["annoyed","base"], "happy": ["smile","grin"], "naughty": ["grin"], "horny": ["grin"], "annoyed": ["annoyed"], "disgusted": ["clench","annoyed"], "angry": ["clench","angry"]},
                   "eyes": {"neutral": ["base"], "happy": ["base"], "naughty": ["narrow","base"], "horny": ["narrow","base"], "annoyed": ["narrow"], "disgusted": ["narrow"], "angry": ["narrow","base"]},
                   "eyebrows": {"neutral": ["base"], "happy": ["base"], "naughty": ["base"], "horny": ["base"], "annoyed": ["worried"], "disgusted": ["base", "angry"], "angry": ["angry"]},
                   "pupils": {"neutral": ["mid","L","R"], "happy": ["mid","L","R"], "naughty": ["mid","L","R","down"], "horny": ["mid","L","R","down"], "annoyed": ["mid","R"], "disgusted": ["down"], "angry": ["L"]}}

label her_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=False, tears=False, extra=False, emote=False, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    python:
    
        if flip != None:
            hermione_flip = -1 if flip else 1
            
        if animation != False:
            hermione_animation = animation
        
        if xpos:
            hermione_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            if ypos == "head":
                use_hermione_head = True
            elif ypos in ("base", "default"):
                use_hermione_head = False
                
            hermione_ypos = int(sprite_pos["y"].get(ypos, ypos))
            
        hermione.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)

        if face:
            if not mouth:
                hermione.set_face(mouth=renpy.random.choice(her_face["mouth"].get(face, None)))
            if not eyes:
                hermione.set_face(eyes=renpy.random.choice(her_face["eyes"].get(face, None)))
            if not eyebrows:
                hermione.set_face(eyebrows=renpy.random.choice(her_face["eyebrows"].get(face, None)))
            if not pupils:
                hermione.set_face(pupils=renpy.random.choice(her_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        show screen hermione_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(her, text)
        
    if use_hermione_head:
        hide screen hermione_main
    return


#label her_kneel(text="", mouth=None, eye=None, cheeks=None, tears=None, extra=None, emote=None, xpos=None, ypos=None, trans=None):
label her_kneel(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=False, tears=False, extra=False, emote=False, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):    
    #TODO Hermione's kneel pose was removed. Events that use it need to be posed again.
    call her_main(text, mouth, eyes, eyebrows, pupils, cheeks, tears, extra, emote, face, xpos, ypos, flip, trans, animation)
    return

label update_hermione:

    $ hermione_chibi.update()
    $ hermione_flip = 1
    $ use_hermione_head = False

    return

label end_hermione_event:
    call her_chibi("hide")
    hide screen hermione_main
    with d3
    pause.5

    call update_hermione

    $ active_girl = None
    $ hermione_busy = True
    $ hermione.wear("all")
    
    $ renpy.stop_predict(hermione.get_image())
    $ renpy.stop_predict("characters/hermione/face/*.png")

    call music_block
    jump main_room

screen hermione_main():
    tag hermione_main
    zorder hermione_zorder
    sensitive False
    default hermione_img = hermione.get_image()
    if hermione_animation != None:
        add hermione_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio) at hermione_animation
    else:
        add hermione_img xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    on ("show", "replace") action Function(apply_doll_transition, hermione, "hermione_main", "hermione_img", use_hermione_head)
