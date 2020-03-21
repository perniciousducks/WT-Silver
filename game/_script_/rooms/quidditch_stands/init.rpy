
# Quidditch stands

default quidditch_stands = {
    "weather": "sun_high",
    "rain": False,
    "puddles": False,
    "crowd": [],
    "crowd_react": [None, None, None],
    "spotlight": False,
    "hole": False,
    "tree_fire": False
}

# Crowd density presets
define crowd_few = ["low_1"]
define crowd_mid = ["low_1", "low_2", "tower_1"]
define crowd_full = ["low_1", "low_2", "low_3", "low_4", "tower_1", "tower_2"]

label quidditch_stands(hidden=False, reset=False, **kwargs):
    # Update and show the area.
    # Pass `hidden=True` to update only, `reset=True` to reset the area before applying arguments.
    if reset:
        $ reset_variables("quidditch_stands")
    $ quidditch_stands.update(kwargs)
    if not hidden:
        show screen quidditch_stands_back(**quidditch_stands)
        show screen quidditch_stands_front(**quidditch_stands)
    return


screen quidditch_stands_back(weather, rain=False, crowd=[], crowd_react=[None, None, None], tree_fire=False, puddles=False, **kwargs):
    zorder 0

    add "images/rooms/quidditch_stands/bg_{}.png".format(weather) zoom 0.5

    if tree_fire:
        add "quid_stands_fire" pos (870, -15)

    for c in set(crowd):
        add "images/rooms/quidditch_stands/crowd_{}.png".format(c) zoom 0.5

    add crowd_react[0] pos (570, 140)
    add crowd_react[1] pos (720, 90)
    add crowd_react[2] pos (960, 60)

    #TODO Add rain/puddle graphics


screen quidditch_stands_front(weather, spotlight=False, hole=False, rain=False, **kwargs):
    zorder 5

    add "images/rooms/quidditch_stands/fg_{}.png".format(weather) zoom 0.5

    if hole:
        add "images/rooms/quidditch_stands/hole.png" zoom 0.5

    if spotlight:
        add "images/rooms/quidditch_stands/spotlight.png" zoom 0.5

#TODO Align bludger movement to new tower design
screen bludger_flying(start, end, t=1.0):
    zorder 4
    tag bludger

    add "images/rooms/quidditch_stands/bludger.png":
        at transform:
            subpixel True
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            pos start
            ease t xpos end[0] ypos end[1]


image quid_stands_fire:
    zoom 0.5
    "images/rooms/quidditch_stands/fire/0.png" with d3
    pause 0.3
    "images/rooms/quidditch_stands/fire/1.png" with d3
    pause 0.3
    repeat


label test_stands:
    call ctc
    call quidditch_stands(hole=False)
    pause 1.5
    call quidditch_stands(weather="sun_low")
    pause 1.5
    call quidditch_stands(crowd=["low_1"])
    pause 0.5
    call quidditch_stands(crowd=["low_1", "low_2"])
    pause 0.5
    call quidditch_stands(crowd=["low_1", "low_2", "low_3"])
    pause 0.5
    call quidditch_stands(weather="sun_high", crowd=["low_1", "low_2", "low_3", "low_4"])
    pause 0.5
    call quidditch_stands(crowd=["low_1", "low_2", "low_3", "low_4", "tower_2"])
    pause 0.5
    call quidditch_stands(crowd=["low_1", "low_2", "low_3", "low_4", "tower_1", "tower_2"])
    pause 0.5
    call quidditch_stands(crowd=["low_1", "low_2", "low_3", "low_4", "tower_1", "tower_2"])
    pause 1.5
    call quidditch_stands(spotlight=True)
    pause 1.5
    call quidditch_stands(spotlight=False)
    pause 1.5
    call quidditch_stands(hole=True)
    pause 1
    call quidditch_stands(weather="overcast", crowd=["bj"])
    pause 1
    jump test_stands

