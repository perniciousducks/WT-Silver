# Unfinished

init python:
    def list_outfit_files():
        global active_girl

        path = "{}/game/outfits/".format(config.basedir)
        return ["/outfits/{}".format(f) for f in system.listdir(path) if system.path.isfile(system.path.join(path, f)) and f.endswith(".png")]

label file_explorer():
    $ files=list_outfit_files()

    call screen file_explorer(files)
    return

screen file_explorer(files):
    vbox:
        for i in files:
            add i zoom 0.5

    textbutton "back" action Return()
