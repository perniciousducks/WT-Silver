label phoenix:

    menu:
        "Dueling - Prototype sign drawing":
            jump magic_tutorial
        "Back":
            jump main_room_menu

    if not bird_examined:
        $ bird_examined = True
        hide screen genie
        call gen_chibi("stand","mid","base",flip=True)
        show screen chair_left #Empty chair near the desk.
        show screen desk
        with d5
        m "Hm....."
        m "Even this weird-looking bird radiates magic..."
        show screen genie
        hide screen genie_stand
        hide screen chair_left #Empty chair near the desk.
        hide screen desk
        with d5
        jump main_room_menu

    if not phoenix_is_fed:
        $ phoenix_is_fed = True
        $ phoenix_fed_counter += 1
        jump feeding
    if phoenix_is_fed and not phoenix_is_petted:
        $ phoenix_is_petted = True
        $ phoenix_petted_counter += 1
        jump petting

    jump main_room_menu

### FEEDING ###
label feeding:
    hide screen genie
    show screen feeding
    with d3
    pause .5

    show screen phoenix_food
    with d3

    $ random_number = renpy.random.randint(1, 3)
    if random_number == 1:
        m "There you go..."
    elif random_number == 2:
        m "Eat up, buddy."
    else:
        pause .8

    show screen genie
    hide screen feeding
    with d3

    jump main_room_menu

### PETTING ###
label petting:
    hide screen genie
    show screen petting
    with d3
    pause 1

    $ random_number = renpy.random.randint(1, 5)
    if random_number == 1:
        m "Who's a good bird?"
    elif random_number == 2:
        "*Pat *Pat *Pat..."
    elif random_number == 3:
        "Glad you aren't as noisy as Iago..."
    else:
        pause 2.4

    show screen genie
    hide screen petting
    with d3

    jump main_room_menu
