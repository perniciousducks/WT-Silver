init python:
        ### Weather Types ###

        ## Day ##
        # (cloud across sky)    w_g < 4
        # (heavy clouds)        w_g > 3
        # (rain)                w_g > 4
        # (lighting)            w_g > 5 or (w_g = 4 and chance success)
        # (snowy)               w_g > 3 (and chance success) (Cant be raining)
        # (blizzard)            w_g > 6 

        ## Night ##
        # (clear sky)           w_g = 1
        # (Clear sky with moon) w_g = 2
        # (clouds across moon)  w_g = 3
        # (heavy clouds)        w_g > 3
        # (rain)                w_g > 4
        # (rain and lighting)   w_g > 5 or (w_g = 4 and chance success)
        # (blizzard)            w_g > 6

    def show_weather():
        global weather_animations
        global weather_gen
        global raining
        global snowing
        global blizzard
        raining = False
        snowing = False
        blizzard = False
        weather_animations = []
        lightning_gen = renpy.random.randint(1, 2)
        if weather_gen == 6:
            blizzard = True
            weather_animations.append("blizzard")
            renpy.music.play("sounds/blizzard.mp3", "weather", fadeout=1.0, fadein=1.0)
        if weather_gen == 5 or (weather_gen == 4 and lightning_gen == 1): # (Heavy clouds with chance of lightning)
            weather_animations.append("lightning")
        if weather_gen > 4 and not blizzard:
            raining = True
            weather_animations.append("rain")
            renpy.music.play("sounds/rain.mp3", "weather", fadeout=1.0, fadein=1.0)
        if weather_gen > 3 and lightning_gen == 2 and not (raining or blizzard):
            snowing = True
            weather_animations.append("snow")
            

init -2:
    transform cloud_move: #http://www.renpy.org/wiki/atl
        xpos 520
        choice:
            ypos 150
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 280 # linear
        pause 7
        repeat

    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 520
        choice:
            ypos 130
        choice:
            ypos 150
        choice:
            ypos 150
        linear 30.0 xpos 280 # linear
        pause 2
        repeat

    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 520
        choice:
            ypos 150
        choice:
            ypos 170
        linear 70.0 xpos 280 # linear
        pause 2
        repeat

    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 520
        ypos 160
        linear 50.0 xpos 280 # linear
        pause 2
        repeat

image rain: #Rain.
    "images/rooms/main_room/weather/rain_01.png"
    pause.1
    "images/rooms/main_room/weather/rain_02.png"
    pause.1
    "images/rooms/main_room/weather/rain_03.png"
    pause.1
    repeat
    
image snow: #Snow.
    "images/rooms/main_room/weather/snow_01.png"
    pause.07
    "images/rooms/main_room/weather/snow_02.png"
    pause.07
    "images/rooms/main_room/weather/snow_03.png"
    pause.07
    "images/rooms/main_room/weather/snow_04.png"
    pause.07
    "images/rooms/main_room/weather/snow_05.png"
    pause.07
    "images/rooms/main_room/weather/snow_06.png"
    pause.07
    "images/rooms/main_room/weather/snow_07.png"
    pause.07
    "images/rooms/main_room/weather/snow_08.png"
    pause.07
    "images/rooms/main_room/weather/snow_09.png"
    pause.07
    "images/rooms/main_room/weather/snow_10.png"
    pause.07
    repeat
    
image blizzard: #Blizzard.
    "images/rooms/main_room/weather/blizzard_01.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_02.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_03.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_04.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_05.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_06.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_07.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_08.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_09.png"
    pause.05
    "images/rooms/main_room/weather/blizzard_10.png"
    pause.05
    repeat


image lightning: #Lightening during rain behind the window.
    pause 20
    "images/rooms/main_room/weather/lightining_01.png"
    pause.1
    "images/rooms/main_room/weather/lightining_02.png"
    pause.1
    "images/rooms/main_room/weather/lightining_03.png"
    pause.1
    "images/rooms/main_room/weather/lightining_04.png"
    pause.1
    "images/rooms/main_room/weather/lightining_05.png"
    pause.1
    "images/rooms/main_room/weather/lightining_06.png"
    pause.1
    "images/rooms/main_room/weather/lightining_05.png"
    pause.1
    "images/rooms/main_room/weather/lightining_06.png"
    pause.1
    "images/rooms/main_room/weather/lightining_05.png"
    pause 20
    repeat

screen weather:
    zorder -1
    if daytime:
        if weather_gen < 4:# (cloud across sky)
            add "images/rooms/main_room/weather/sky.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
            add "images/rooms/main_room/weather/cloud_small.png" at cloud_move
        if weather_gen >= 4:# (heavy clouds)
            add "images/rooms/main_room/weather/cloudy.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
    else:
        ## Weather Types
        if weather_gen == 1:# (clear sky)
            add "images/rooms/main_room/weather/night_sky.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 2:# (Clear sky with moon)
            add "images/rooms/main_room/weather/night_sky_02.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 3:# (clouds across moon)
            add "images/rooms/main_room/weather/night_sky_02.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
            add "images/rooms/main_room/weather/night_cloud_02.png" at cloud_night_move_01
            add "images/rooms/main_room/weather/night_cloud_01.png" at cloud_night_move_02
            add "images/rooms/main_room/weather/night_cloud_03.png" at cloud_night_move_03
        if weather_gen >= 4:# (heavy clouds)
            add "images/rooms/main_room/weather/night_sky_04.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")

    for img in weather_animations:
        add img at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
