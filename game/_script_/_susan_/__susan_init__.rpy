# Main
default susan_xpos = 300
default susan_ypos = 0
default susan_zorder = 15
default susan_flip = 1
default use_susan_head = False

# Body
default susan_base     = "characters/susan/body/base/base_01.png"
default susan_breasts  = "characters/susan/body/base/boobs_nipfix.png"
default susan_l_arm    = "characters/susan/body/arms/l_arm_back.png"
default susan_r_arm    = "characters/susan/body/arms/r_arm_thigh.png"

# Face
default susan_mouth  = "characters/susan/face/mouth/base.png"
default sus_mouth    = "base"
default sus_lipstick = "nude"

default susan_eye     = "characters/susan/face/eyes/base.png"
default susan_eye_bg  = "characters/susan/face/eyes/_white_.png"
default susan_pupil   = "characters/susan/face/pupil/mid.png"
default sus_eye_color = "green"

default susan_eyebrow = "characters/susan/face/brow/base.png"

default susan_cheeks = "characters/susan/face/extras/cheeks_blank.png"
default susan_tears  = "characters/susan/face/extras/tears_blank.png"
default susan_emote  = "characters/emotes/blank.png"

# Hair
default susan_hair        = "characters/susan/body/hair/braided_red_base.png"
default susan_hair_shadow = "characters/susan/body/hair/braided_red_top.png"
default sus_hair_style    = "braided"
default sus_hair_color    = "red"

# Clothes

# Save State
default sus_request_wear_top     = True
default sus_request_wear_bra     = True
default sus_request_wear_bottom  = True
default sus_request_wear_panties = True

default sus_request_wear_onepiece   = False
default sus_request_wear_garterbelt = False

default sus_request_wear_neckwear  = False
default sus_request_wear_gloves    = False
default sus_request_wear_stockings = False
default sus_request_wear_robe      = False

default sus_request_wear_hat     = False
default sus_request_wear_glasses = False
default sus_request_wear_ears    = False
default sus_request_wear_makeup  = False
default sus_request_wear_accs    = False

default sus_request_wear_buttplug  = False
default sus_request_wear_piercings = False
default sus_request_wear_tattoos   = False

default sus_request_wear_outfit = False

# Toggle
default susan_wear_top     = True
default susan_wear_bra     = True
default susan_wear_bottom  = True
default susan_wear_panties = True

default susan_wear_onepiece   = False
default susan_wear_garterbelt = False

default susan_wear_neckwear  = False
default susan_wear_gloves    = False
default susan_wear_stockings = False
default susan_wear_robe      = False

default susan_wear_hat       = False
default susan_wear_glasses   = False
default susan_wear_ears      = False
default susan_wear_makeup    = False
default susan_wear_accs      = False
default susan_badges         = False
default susan_wear_piercings = False
default susan_wear_tattoos   = False

default susan_wear_outfit = False

# Top
default susan_top     = "characters/susan/clothes/tops/top_1.png"
default sus_top       = "top_1"
default sus_top_color = "base"

# Bottom
default susan_bottom     = "characters/susan/clothes/bottoms/skirt_1.png"
default sus_bottom       = "skirt_1"
default sus_bottom_color = "base"

# Underwear
default susan_bra     = "characters/susan/clothes/bras/bra_base.png"
default sus_bra       = "bra_base"
default sus_bra_color = "base"

default susan_panties     = "characters/susan/clothes/panties/panties_base.png"
default sus_panties       = "panties_base"
default sus_panties_color = "base"

default susan_onepiece     = "characters/susan/clothes/onepieces/blank.png"
default sus_onepiece       = "blank"
default sus_onepiece_color = "base"

default susan_garterbelt     = "characters/susan/clothes/garterbelts/blank.png"
default sus_garterbelt       = "blank"
default sus_garterbelt_color = "base"


# Other Clothing
default susan_neckwear     = "characters/susan/clothes/neckwear/blank.png"
default sus_neckwear       = "blank"
default sus_neckwear_color = "base"

default susan_accs_list = []

default susan_gloves     = "characters/susan/clothes/gloves/blank.png"
default sus_gloves       = "blank"
default sus_gloves_color = "base"

default susan_stockings     = "characters/susan/clothes/stockings/blank.png"
default sus_stockings       = "blank"
default sus_stockings_color = "base"

default susan_robe     = "characters/susan/clothes/robe/blank.png"
default sus_robe       = "blank"
default sus_robe_color = "base"


# Accessories
default susan_makeup_list = []

default susan_hat     = "characters/susan/clothes/hats/blank.png"
default sus_hat       = "blank"
default sus_hat_color = "base"

default susan_glasses     = "characters/susan/clothes/glasses/blank.png"
default sus_glasses       = "blank"
default sus_glasses_color = "base"

default susan_ears = "characters/susan/clothes/ears/blank.png"
default sus_ears   = "blank"

# Outfits
default susan_outfit_GLBL = None
default susan_temp_outfit = None

# Cum layers
default susan_face_covered = False
default susan_face_cum     = "characters/susan/face/cum/cum_0.png"

default susan_body_covered = False
default susan_body_cum     = "characters/susan/face/cum/cum_3.png"

default susan_aftersperm  = False
default susan_clothes_cum = "characters/susan/face/cum/aftersperm.png"

# Stats
default sus_whoring = 0
default sus_mood    = 0

# Flags
default susan_busy              = False
default susan_unlocked          = False
default susan_wardrobe_unlocked = False
default chitchated_with_susan   = False

# Favour stuff
default susan_imperio_influence = False
default susan_imperio_counter   = 0 # Maybe the higher Astoria's spell level gets, the longer this lasts?

# Names
default susan_name     = "Miss Bones"
default sus_genie_name = "Sir"

# Stats Screen
default sus_curse_counter = 2 # She got cursed twice beforeyou unlock her. Poor girl...

default gave_susan_gift = False

label reset_susan_progress:
    $ reset_variables(
        # Stats
        "sus_whoring",
        "sus_mood",

        # Flags
        "susan_busy",
        "susan_unlocked",
        "susan_wardrobe_unlocked",
        "chitchated_with_susan",

        # Favour stuff
        "susan_imperio_influence",
        "susan_imperio_counter",

        # Names
        "susan_name",
        "sus_genie_name",

        # Stats Screen
        "sus_curse_counter"
    )
    return

label reset_susan_clothing:
    $ reset_variables(
        # Body
        "susan_base",
        "susan_breasts",
        "susan_l_arm",
        "susan_r_arm",
        "susan_xpos",
        "susan_ypos",
        "susan_zorder",
        "susan_flip",
        "use_susan_head",

        # Face
        "susan_mouth",
        "sus_mouth",
        "sus_lipstick",
        "susan_eye",
        "susan_eye_bg",
        "susan_pupil",
        "sus_eye_color",
        "susan_eyebrow",
        "susan_cheeks",
        "susan_tears",
        "susan_emote",

        # Hair
        "susan_hair",
        "susan_hair_shadow",
        "sus_hair_style",
        "sus_hair_color",

        # Save State
        "sus_request_wear_top",
        "sus_request_wear_bra",
        "sus_request_wear_bottom",
        "sus_request_wear_panties",
        "sus_request_wear_onepiece",
        "sus_request_wear_garterbelt",
        "sus_request_wear_neckwear",
        "sus_request_wear_gloves",
        "sus_request_wear_stockings",
        "sus_request_wear_robe",
        "sus_request_wear_hat",
        "sus_request_wear_glasses",
        "sus_request_wear_ears",
        "sus_request_wear_makeup",
        "sus_request_wear_accs",
        "sus_request_wear_buttplug",
        "sus_request_wear_piercings",
        "sus_request_wear_tattoos",
        "sus_request_wear_outfit",

        # Toggle
        "susan_wear_top",
        "susan_wear_bra",
        "susan_wear_bottom",
        "susan_wear_panties",
        "susan_wear_onepiece",
        "susan_wear_garterbelt",
        "susan_wear_neckwear",
        "susan_wear_gloves",
        "susan_wear_stockings",
        "susan_wear_robe",
        "susan_wear_hat",
        "susan_wear_glasses",
        "susan_wear_ears",
        "susan_wear_makeup",
        "susan_wear_accs",
        "susan_badges",
        "susan_wear_piercings",
        "susan_wear_tattoos",
        "susan_wear_outfit",

        #Top
        "susan_top",
        "sus_top",
        "sus_top_color",

        # Bottom
        "susan_bottom",
        "sus_bottom",
        "sus_bottom_color",

        # Underwear
        "susan_bra",
        "sus_bra",
        "sus_bra_color",
        "susan_panties",
        "sus_panties",
        "sus_panties_color",
        "susan_onepiece",
        "sus_onepiece",
        "sus_onepiece_color",
        "susan_garterbelt",
        "sus_garterbelt",
        "sus_garterbelt_color",

        # Other Clothing
        "susan_neckwear",
        "sus_neckwear",
        "sus_neckwear_color",
        "susan_accs_list",
        "susan_gloves",
        "sus_gloves",
        "sus_gloves_color",
        "susan_stockings",
        "sus_stockings",
        "sus_stockings_color",
        "susan_robe",
        "sus_robe",
        "sus_robe_color",

        # Accessories
        "susan_makeup_list",
        "susan_hat",
        "sus_hat",
        "sus_hat_color",
        "susan_glasses",
        "sus_glasses",
        "sus_glasses_color",
        "susan_ears",
        "sus_ears",

        # Outfits
        "susan_outfit_GLBL",
        "susan_temp_outfit",

        # Cum layers
        "susan_face_covered",
        "susan_face_cum",
        "susan_body_covered",
        "susan_body_cum",
        "susan_aftersperm",
        "susan_clothes_cum"
    )
    return
