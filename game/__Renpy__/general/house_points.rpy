label add_house_points(house, points):
    $ house_pos = {"r":175,"s":286,"g":393,"h":502}
    show screen points_overlay(house)
    show screen adding_house_points(points, house_pos[house])
    with Dissolve(0.75)
    if house == "r":
        $ ravenclaw += int(points)
    if house == "s":
        $ slytherin += int(points)
    if house == "g":
        $ gryffindor += int(points)
    if house == "h":
        $ hufflepuff += int(points)
    pause 1
    hide screen adding_house_points
    hide screen points_overlay
    with Dissolve(0.75)
return

screen adding_house_points(points, house_xpos):
    text "[points]" at Position(xpos=house_xpos, ypos=8)
    zorder 4

screen points_overlay(house): #House points screen.
    add "interface/points/TopUI_Bar_Overlay.png" at Position(xpos=140, ypos=1)
    if house != "s":
        hbox:
            spacing 10 xpos 286 ypos 11
            text "{size=-5}[slytherin]{/size}"
    if house != "g":
        hbox:
            spacing 10 xpos 392 ypos 11
            text "{size=-5}[gryffindor]{/size}" #сумма текстом
    if house != "h":
        hbox: 
            spacing 10 xpos 505 ypos 11
            text "{size=-5}[hufflepuff]{/size}" 
    if house != "r":
        hbox: 
            spacing 10 xpos 177 ypos 11
            text "{size=-5}[ravenclaw]{/size}"
    zorder 3

### Gryffindor, Hufflepuff, Ravenclaw Points ###
label points_changes_gryffindor:

    ### GRYFFINDOR POINTS ###
    elif 3 <= generating_points_gryffindor <= 4:
        call add_house_points("g","+1")
    elif 5 <= generating_points_gryffindor <= 6:
        call add_house_points("g","+2")
    elif 7 <= generating_points_gryffindor <= 8:
        call add_house_points("g","+3")
    elif generating_points_gryffindor == 9:
        call add_house_points("g","+5")
    elif generating_points_gryffindor == 10:
        call add_house_points("g","+11")


    ###  Hufflepuff ###
    if 3 <= generating_points_hufflepuff <= 4:
        call add_house_points("h","+1")
    elif 5 <= generating_points_hufflepuff <= 6:
        call add_house_points("h","+2")
    elif 7 <= generating_points_hufflepuff <= 8:
        call add_house_points("h","+4")
    elif generating_points_hufflepuff == 9:
        call add_house_points("h","+7")
    elif generating_points_hufflepuff == 10:
        call add_house_points("h","+14")


    ### Ravenclaw ###
    if 3 <= generating_points_ravenclaw <= 4:
        call add_house_points("r","+1")
    elif 5 <= generating_points_ravenclaw <= 6:
        call add_house_points("r","+2")
    elif 7 <= generating_points_ravenclaw <= 8:
        call add_house_points("r","+6")
    elif generating_points_ravenclaw == 9:
        call add_house_points("r","+8")
    elif generating_points_ravenclaw == 10:
        call add_house_points("r","+13")

return