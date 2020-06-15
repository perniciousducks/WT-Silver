init python:
    config.after_load_callbacks.append(load_assets)
    config.per_frame_screens.append("loading")

    def is_prediction_active():
        return renpy.game.interface.prediction_coroutine is not None

init -1 python:
    def load_assets():
        renpy.call_in_new_context("loading")
        return

label loading:
    call screen loading()
    return

screen loading():
    layer "interface"
    tag loading
    zorder 1000

    default step = 0
    default steps = {
        0: "Spinning up disks",
        1: "Lubricating Hermione",
        2: "Filling up Tonks' glass",
        3: "Rendering Cho's marvellous abs",
        4: "Teaching Astoria some manners",
        5: "Gazing into the crystal ball"
        }

    # Set to False as soon as prediction is interrupted, because prediction might resume unexpectedly
    default predicting = True
    $ predicting = not (not predicting or not is_prediction_active())

    frame style "empty" background "#000"
    text ("Loading {}%".format(int(float(step) / (len(steps) - 1) * 100))) size 32 color "#fff" align (0.5, 0.5)
    text ("{}".format(steps[step])) size 18 color "#808080" align (0.5, 0.55)

    timer 0.01 action SetScreenVariable("step", 1)

    if step is 1:
        add hermione.get_image() alpha 0
        timer 0.01 action SetScreenVariable("step", 2)
    elif step is 2:
        add tonks.get_image() alpha 0
        timer 0.01 action SetScreenVariable("step", 3)
    elif step is 3:
        add cho.get_image() alpha 0
        timer 0.01 action SetScreenVariable("step", 4)
    elif step is 4:
        add astoria.get_image() alpha 0
        timer 0.01 action SetScreenVariable("step", 5)
    elif step is 5 and not predicting: # not is_prediction_active():
        timer 0.01 action Return()
