#label add_house_points(house, points):
#    show screen adding_house_points(points, house)
#    with Dissolve(0.5)
#    if house == "r":
#        $ ravenclaw += int(points)
#    if house == "s":
#        $ slytherin += int(points)
#    if house == "g":
#        $ gryffindor += int(points)
#    if house == "h":
#        $ hufflepuff += int(points)
#    hide screen adding_house_points
#    with Dissolve(0.5)
#    return

#label points_animation:
    #show screen all_house_points
    #with Dissolve(0.5)
    #pause 0.75
    #hide screen all_house_points
    #with Dissolve(0.5)
    #return

#screen all_house_points:
    #$ house_pos = {"r":175,"s":286,"g":393,"h":502}
    #add "interface/points/TopUI_Bar_Overlay.png" at Position(xpos=140, ypos=1)
    #text "[gryffindor_p_gain]" at Position(xpos=house_pos["g"], ypos=8)
    #text "[slytherin_p_gain]" at Position(xpos=house_pos["s"], ypos=8)
    #text "[hufflepuff_p_gain]" at Position(xpos=house_pos["h"], ypos=8)
    #text "[ravenclaw_p_gain]" at Position(xpos=house_pos["r"], ypos=8)
    #hbox:
    #    spacing 10 xpos 286 ypos 11
    #    text "{size=-5}[slytherin]{/size}"
    #zorder 3

#screen adding_house_points(points, house):
#    $ house_pos = {"r":175,"s":286,"g":393,"h":502}
#    text "[points]" at Position(xpos=house_pos[house], ypos=8)
#    zorder 3

### Gryffindor, Hufflepuff, Ravenclaw Points ###
label points_changes:
    $ gryffindor_p_gain = "+0"
    $ slytherin_p_gain = "+0"
    $ hufflepuff_p_gain = "+0"
    $ ravenclaw_p_gain = "+0"
    ### GRYFFINDOR POINTS ###
    if 3 <= generating_points_gryffindor <= 4:
        $ gryffindor += 1
        $ gryffindor_p_gain = "+1"
    elif 5 <= generating_points_gryffindor <= 6:
        $ gryffindor += 2
        $ gryffindor_p_gain = "+2"
    elif 7 <= generating_points_gryffindor <= 8:
        $ gryffindor += 3
        $ gryffindor_p_gain = "+3"
    elif generating_points_gryffindor == 9:
        $ gryffindor += 5
        $ gryffindor_p_gain = "+5"
    elif generating_points_gryffindor == 10:
        $ gryffindor += 11
        $ gryffindor_p_gain = "+11"


    ###  Hufflepuff ###
    if 3 <= generating_points_hufflepuff <= 4:
        $ hufflepuff += 1
        $ hufflepuff_p_gain = "+1"
    elif 5 <= generating_points_hufflepuff <= 6:
        $ hufflepuff += 2
        $ hufflepuff_p_gain = "+2"
    elif 7 <= generating_points_hufflepuff <= 8:
        $ hufflepuff += 4
        $ hufflepuff_p_gain = "+4"
    elif generating_points_hufflepuff == 9:
        $ hufflepuff += 7
        $ hufflepuff_p_gain = "+7"
    elif generating_points_hufflepuff == 10:
        $ hufflepuff += 14
        $ hufflepuff_p_gain = "+14"


    ### Ravenclaw ###
    if 3 <= generating_points_ravenclaw <= 4:
        $ ravenclaw += 1
        $ ravenclaw_p_gain = "+1"
    elif 5 <= generating_points_ravenclaw <= 6:
        $ ravenclaw += 2
        $ ravenclaw_p_gain = "+2"
    elif 7 <= generating_points_ravenclaw <= 8:
        $ ravenclaw += 6
        $ ravenclaw_p_gain = "+6"
    elif generating_points_ravenclaw == 9:
        $ ravenclaw += 8
        $ ravenclaw_p_gain = "+8"
    elif generating_points_ravenclaw == 10:
        $ ravenclaw += 13
        $ ravenclaw_p_gain = "+13"

    call slytherin_points

    return
