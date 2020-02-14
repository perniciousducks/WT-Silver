

### Room Animations###
#(interactions can be found in ani_genie.rpy)


### Fireplace ###
image fireplace_fire: #Fireplace fire.
    "images/rooms/_objects_/fireplace/fireplace_fire_01.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_02.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_03.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_04.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_05.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_06.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_07.png"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_08.png"
    pause.1
    repeat


###Glow effect###
image glow_effect: #Candle fire.
    "images/animation/glow_effect/glow_1.png"
    pause.1
    "images/animation/glow_effect/glow_2.png"
    pause.1
    "images/animation/glow_effect/glow_3.png"
    pause.1
    "images/animation/glow_effect/glow_4.png"
    pause.2
    "images/animation/glow_effect/glow_3.png"
    pause.1
    "images/animation/glow_effect/glow_2.png"
    pause.1
    "images/animation/glow_effect/glow_4.png"
    pause.2
    "images/animation/glow_effect/glow_3.png"
    pause.1
    "images/animation/glow_effect/glow_2.png"
    pause.1
    "images/animation/glow_effect/glow_1.png"
    pause.1
    repeat

### Candle Fire ###
image candle_fire_01: #Candle fire.
    "images/rooms/_objects_/candles/fire_01.png"
    pause.1
    "images/rooms/_objects_/candles/fire_02.png"
    pause.1
    "images/rooms/_objects_/candles/fire_03.png"
    pause.1
    "images/rooms/_objects_/candles/fire_04.png"
    pause.1
    "images/rooms/_objects_/candles/fire_05.png"
    pause.1
    "images/rooms/_objects_/candles/fire_06.png"
    pause.1
    "images/rooms/_objects_/candles/fire_07.png"
    pause.1
    "images/rooms/_objects_/candles/fire_08.png"
    pause.1
    "images/rooms/_objects_/candles/fire_09.png"
    pause.1
    "images/rooms/_objects_/candles/fire_10.png"
    pause.1
    repeat

image candle_fire_02: #Candle fire.
    "images/rooms/_objects_/candles/fire_01.png"
    pause.1
    "images/rooms/_objects_/candles/fire_04.png"
    pause.1
    "images/rooms/_objects_/candles/fire_03.png"
    pause.1
    "images/rooms/_objects_/candles/fire_02.png"
    pause.1
    "images/rooms/_objects_/candles/fire_08.png"
    pause.1
    "images/rooms/_objects_/candles/fire_06.png"
    pause.1
    "images/rooms/_objects_/candles/fire_07.png"
    pause.1
    "images/rooms/_objects_/candles/fire_05.png"
    pause.1
    "images/rooms/_objects_/candles/fire_10.png"
    pause.1
    "images/rooms/_objects_/candles/fire_09.png"
    pause.1
    repeat


### Phoenix ###
image phoenix_idle:
    zoom 0.5
    
    "images/rooms/_objects_/phoenix/phoenix_01.png"
    pause 2
    "images/rooms/_objects_/phoenix/phoenix_02.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_03.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_01.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_03.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.png"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_01.png"
    pause 10
    repeat

image phoenix_hover:
    zoom 0.5

    "images/rooms/_objects_/phoenix/phoenix_hover.png"

image feather:
    zoom 0.5
    
    pause 10
    alpha 1.0
    "images/rooms/_objects_/phoenix/feather_ani/pho_01.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_02.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_03.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_04.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_05.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_06.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_07.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_08.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_09.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_10.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_11.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_12.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_13.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_14.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_15.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_16.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_17.png"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_18.png"
    pause 10
    linear .5 alpha 0.0
    pause 20
    repeat
    
# Door
image door_idle:
    zoom 0.5
    
    "images/rooms/_objects_/doors/door_idle.png"
    
image door_hover:
    zoom 0.5

    "images/rooms/_objects_/doors/door_hover.png"

image door_idle_night:
    zoom 0.5

    "images/rooms/_objects_/doors/door_idle_night.png"
    
image door_hover_night:
    zoom 0.5

    "images/rooms/_objects_/doors/door_hover_night.png"
    
# Fireplace
image fireplace_idle:
    zoom 0.5
    
    "images/rooms/_objects_/fireplace/fireplace_idle.png"
    
# Fireplace
image fireplace_idle_shadow:
    zoom 0.5
    
    "images/rooms/_objects_/fireplace/fireplace_w_shadow.png"
    
image fireplace_hover:
    zoom 0.5

    "images/rooms/_objects_/fireplace/fireplace_hover.png"
    
### Owl Post ###
image owl_idle:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_idle_01.png"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_02.png"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_03.png"
    pause.15
    "images/rooms/_objects_/mail/owl_idle_02.png"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_01.png"
    pause 7
    repeat
    
image owl_letter:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_01.png"
    pause.1
    "images/rooms/_objects_/mail/owl_02.png"
    pause.1
    "images/rooms/_objects_/mail/owl_03.png"
    pause.15
    "images/rooms/_objects_/mail/owl_02.png"
    pause.1
    "images/rooms/_objects_/mail/owl_01.png"
    pause 7
    repeat
    
image owl_letter_hover:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_hover.png"
    
    
#Black owl
image owl_idle_black:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_idle_black.png"
    
image owl_letter_black:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_01_black.png"
    pause.1
    "images/rooms/_objects_/mail/owl_02_black.png"
    pause.1
    "images/rooms/_objects_/mail/owl_03_black.png"
    pause.15
    "images/rooms/_objects_/mail/owl_02_black.png"
    pause.1
    "images/rooms/_objects_/mail/owl_01_black.png"
    pause 7
    repeat
    
image owl_letter_hover_black:
    zoom 0.5
    
    "images/rooms/_objects_/mail/owl_hover_black.png"
