### House-Points ###

label points_changes: # Gets called every day/night.

    ### House-Points Generator ###
    if gryffindor > slytherin:  # G is in the lead. How unfair!
        $ generating_points = 2 # 2 = Slytherin is guaranteed to get points.
    else:
        $ generating_points = renpy.random.randint(1, 2) # 1 = No points today.

    $ generating_points_gryffindor = renpy.random.randint(1, 10)
    $ generating_points_hufflepuff = renpy.random.randint(1, 10)
    $ generating_points_ravenclaw = renpy.random.randint(1, 10)

    ### Gryffindor ###
    if 3 <= generating_points_gryffindor <= 4:
        $ gryffindor += 1
    elif 5 <= generating_points_gryffindor <= 6:
        $ gryffindor += 2
    elif 7 <= generating_points_gryffindor <= 8:
        $ gryffindor += 3
    elif generating_points_gryffindor == 9:
        $ gryffindor += 5
    elif generating_points_gryffindor == 10:
        $ gryffindor += 11

    ###  Hufflepuff ###
    if 3 <= generating_points_hufflepuff <= 4:
        $ hufflepuff += 1
    elif 5 <= generating_points_hufflepuff <= 6:
        $ hufflepuff += 2
    elif 7 <= generating_points_hufflepuff <= 8:
        $ hufflepuff += 4
    elif generating_points_hufflepuff == 9:
        $ hufflepuff += 7
    elif generating_points_hufflepuff == 10:
        $ hufflepuff += 14

    ### Ravenclaw ###
    if 3 <= generating_points_ravenclaw <= 4:
        $ ravenclaw += 1
    elif 5 <= generating_points_ravenclaw <= 6:
        $ ravenclaw += 2
    elif 7 <= generating_points_ravenclaw <= 8:
        $ ravenclaw += 6
    elif generating_points_ravenclaw == 9:
        $ ravenclaw += 8
    elif generating_points_ravenclaw == 10:
        $ ravenclaw += 13

    ### Slytherin ###
    if generating_points == 1 and game_difficulty >= 1: # Failed, no points for S today.
            pass

    else: # Success, award points to S today.

        if game_difficulty <= 1: # Easy Difficulty
            # sna_support = number between 0 and 15
            # ton_support = number between 0 and 12
            # Tonks' is lower since you can do events with her to directly increase points.
            $ slytherin += (sna_support * renpy.random.randint(2, 4))
            $ slytherin += (ton_support * renpy.random.randint(1, 3))

        else: # Normal & Hardcore difficulty
            # sna_support = number between 0 and 15
            # ton_support = number between 0 and 12
            # Tonks' is lower since you can do events with her to directly increase points.
            $ slytherin += (sna_support * renpy.random.randint(2, 3))
            $ slytherin += (ton_support * renpy.random.randint(1, 2))

    return