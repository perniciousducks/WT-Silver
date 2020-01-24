# Sprite blinking
image spr_cho blink:
    sprite_blink("characters/cho/face/eyes/closed.png")
    
image spr_cho blink broom:
    sprite_blink("characters/cho/poses/broom/face/eyes/closed.png")

# Cho chibi

image ch_cho stand:
    random_blink("characters/cho/chibis/cc_stand_blink.png", "characters/cho/chibis/cc_walk_01.png")

image ch_cho walk:
    "characters/cho/chibis/cc_walk_01.png"
    pause.08
    "characters/cho/chibis/cc_walk_02.png"
    pause.08
    "characters/cho/chibis/cc_walk_03.png"
    pause.08
    "characters/cho/chibis/cc_walk_02.png"
    pause.08
    "characters/cho/chibis/cc_walk_01.png"
    pause.08
    "characters/cho/chibis/cc_walk_04.png"
    pause.08
    "characters/cho/chibis/cc_walk_05.png"
    pause.08
    "characters/cho/chibis/cc_walk_04.png"
    pause.08

    repeat

image ch_cho walk_shoes: # Walk shoes layer
    "characters/cho/chibis/cc_walk_01_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_03_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_01_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_05_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_shoes.png"
    pause.08

    repeat
    
image ch_cho walk_quid_shoes: # Walk Quidditch shoes layer
    "characters/cho/chibis/cc_walk_01_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_03_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_01_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_05_quid_shoes.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_quid_shoes.png"
    pause.08

    repeat
    
image ch_cho trousers: # Walk trousers layer
    "characters/cho/chibis/cc_walk_01_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_03_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_02_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_01_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_05_trousers.png"
    pause.08
    "characters/cho/chibis/cc_walk_04_trousers.png"
    pause.08

    repeat

image ch_cho fly:
    random_blink("characters/cho/chibis/fly/cc_fly_idle1.png", "characters/cho/chibis/fly/cc_fly_idle0.png")

image ch_cho fly_move:
    random_blink("characters/cho/chibis/fly_move/cc_fly1.png", "characters/cho/chibis/fly_move/cc_fly0.png")
