

### Susan Bones ###

label sus_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None):
    if eye!=None and pupil!=None and eyebrow!=None and mouth!=None:
        $ changeSus(eye, eyebrow, pupil, mouth)

    if text != "":
        $ renpy.say(sus, text)

    return




