
image ch_sna walk:
    "characters/snape/chibis/snape_01.png"
    pause .18
    "characters/snape/chibis/snape_02.png"
    pause .18
    "characters/snape/chibis/snape_01.png"
    pause .18
    "characters/snape/chibis/snape_03.png"
    pause .18
    repeat
    
image ch_sna stand:
    "characters/snape/chibis/snape_stand.png"

image ch_sna stand_shocked:
    "characters/snape/chibis/shocked/01.png"

image ch_sna hold_dick:
    yoffset -120
    "characters/snape/chibis/masturbating/02.png"

image ch_sna jerk_off:
    yoffset -120
    "characters/snape/chibis/masturbating/01.png"
    pause .2
    "characters/snape/chibis/masturbating/02.png"
    pause .2
    "characters/snape/chibis/masturbating/03.png"
    pause .2
    "characters/snape/chibis/masturbating/04.png"
    pause .2
    repeat

image ch_sna cum:
    size (300,500)
    contains:
        "ch_sna jerk_off"
    contains:
        zoom 2
        yoffset -480
        xoffset -980
        alpha 1
        "characters/snape/chibis/masturbating/sperm_01.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_02.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_03.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_04.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_05.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_06.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_07.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_08.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_09.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_10.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_11.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_12.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_13.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_14.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_15.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_16.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_17.png"
        pause .1
        "characters/snape/chibis/masturbating/sperm_18.png"
        pause 2
        linear .2 alpha 0
        pause .5
        repeat

image ch_sna cum_done:
    size (300,500)
    contains:
        yoffset -120
        "characters/snape/chibis/masturbating/02.png"
    contains:
        yoffset -480
        xoffset -980
        "characters/snape/chibis/masturbating/sperm_18.png"

#TODO Add Snape chibi wand cast actions
image ch_sna wand_idle:
    "characters/snape/chibis/wand_idle/wand_idle_1.png"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_2.png"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_3.png"
    pause.1
    "characters/snape/chibis/wand_idle/wand_idle_2.png"
    pause.1
    repeat

image ch_sna wand_defend:
    "characters/snape/chibis/wand_defend/wand_defend_1.png"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_2.png"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_3.png"
    pause.1
    "characters/snape/chibis/wand_defend/wand_defend_2.png"
    pause.1
    repeat

# Snape sitting in front of fireplace, right side
image snape_toast_goblet:
    "characters/snape/chibis/drinking/01.png"
    pause 2
    "characters/snape/chibis/drinking/02.png"
    pause .2
    "characters/snape/chibis/drinking/03.png"
    pause .2
    "characters/snape/chibis/drinking/04.png"
    pause 1
    "characters/snape/chibis/drinking/03.png"
    pause .2
    "characters/snape/chibis/drinking/01.png"
    pause 3
    repeat
