# Sprite blinking
image spr_tonks blink = sprite_blink("characters/tonks/face/eyes/closed.png")

# Tonks chibi

image ch_ton stand:
    random_blink("characters/tonks/chibis/nt_stand_blink.png", "characters/tonks/chibis/nt_walk_01.png")

image ch_ton stand_shocked:
    size (200,360)
    contains:
        "ch_ton stand"
    contains:
        "characters/tonks/chibis/nt_shocked.png"

image ch_ton walk:
    "characters/tonks/chibis/nt_walk_01.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02.png"
    pause.08
    "characters/tonks/chibis/nt_walk_03.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02.png"
    pause.08
    "characters/tonks/chibis/nt_walk_01.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04.png"
    pause.08
    "characters/tonks/chibis/nt_walk_05.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04.png"
    pause.08

    repeat

image ch_ton walk shoes: # Walk shoes layer
    "characters/tonks/chibis/nt_walk_01_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_03_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_01_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_05_shoes.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04_shoes.png"
    pause.08

    repeat

image ch_ton walk trousers: # Walk trousers layer
    "characters/tonks/chibis/nt_walk_01_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_03_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_02_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_01_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_05_trousers.png"
    pause.08
    "characters/tonks/chibis/nt_walk_04_trousers.png"
    pause.08

    repeat

#Drinking chibi
image ch_ton sit_chair:
    zoom 0.5

    # Chair
    contains:
        "characters/tonks/chibis/drinking/chair.png"

image ch_ton sit:
    zoom 0.5

    # Blinking
    contains:
        "characters/tonks/chibis/drinking/nt_head_01.png"
        pause 2
        "characters/tonks/chibis/drinking/nt_head_02.png"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.png"
        pause 5
        "characters/tonks/chibis/drinking/nt_head_02.png"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.png"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_02.png"
        pause.08
        "characters/tonks/chibis/drinking/nt_head_01.png"
        pause 3
        repeat

    # Leg sway
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01.png"
        pause 2.5
        repeat

image ch_ton sit_trousers:
    zoom 0.5

    # Trousers
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_trousers.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01_trousers.png"
        pause 2.5
        repeat

image ch_ton sit_shoes:
    zoom 0.5

    # Shoes
    contains:
        "characters/tonks/chibis/drinking/nt_sit_01_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_04_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_03_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_02_shoes.png"
        pause.1
        "characters/tonks/chibis/drinking/nt_sit_01_shoes.png"
        pause 2.5
        repeat

image ch_ton sit_top:
    zoom 0.5
    "characters/tonks/chibis/drinking/nt_top.png"

image ch_ton sit_choker:
    zoom 0.5
    "characters/tonks/chibis/drinking/nt_choker.png"
