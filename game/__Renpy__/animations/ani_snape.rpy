

image snape_walk: #Default Snape walk animation.
    "characters/snape/chibis/snape_02.png"
    pause.18
    "characters/snape/chibis/snape_03.png"
    pause.18
    "characters/snape/chibis/snape_02.png"
    pause.18
    "characters/snape/chibis/snape_05.png"
    pause.18
    repeat

image snape_walk_f: #Default Snape walk animation.
    im.Flip("characters/snape/chibis/snape_02.png", horizontal=True)
    pause.18
    im.Flip("characters/snape/chibis/snape_03.png", horizontal=True)
    pause.18
    im.Flip("characters/snape/chibis/snape_02.png", horizontal=True)
    pause.18
    im.Flip("characters/snape/chibis/snape_05.png", horizontal=True)
    pause.18
    repeat

### HANGING WITH SNAPE ###
image genie_toast_goblet: #Genie and Snape sitting in front of fireplace...
    "images/animation/hanging_with_snape_01.png"
    pause 2
    "images/animation/hanging_with_snape_02.png"
    pause.2
    "images/animation/hanging_with_snape_03.png"
    pause.2
    "images/animation/hanging_with_snape_04.png"
    pause 1
    "images/animation/hanging_with_snape_03.png"
    pause.2
    "images/animation/hanging_with_snape_01.png"
    pause 3
    repeat