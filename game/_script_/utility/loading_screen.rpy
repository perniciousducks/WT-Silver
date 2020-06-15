screen loading():
    layer "interface"
    tag loading
    zorder 1000

    default step = 0
    default step_max = 4
    default step_dict = {
        0: "Spinning up disks",
        1: "Lubricating Hermione",
        2: "Filling up Tonks' glass",
        3: "Rendering Cho's marvellous abs",
        4: "Teaching Astoria some manners"
        }


    frame style "empty" background "#000"
    text ("Loading {}%".format(int(float(step) / step_max * 100))) size 32 color "#fff" align (0.5, 0.5)
    text ("{}".format(step_dict[step])) size 18 color "#808080" align (0.5, 0.55)

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
        timer 0.01 action Return()
