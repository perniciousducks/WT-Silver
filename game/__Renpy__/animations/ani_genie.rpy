

### Genie Solo Animations ###

image genie_stand_ani: #Default Genie walk animation.
    zoom 0.5
    
    "characters/genie/chibis/walk_01.png"
    
image genie_stand_alternative: #Default Genie walk animation.
    zoom 0.5
    
    "characters/genie/chibis/standing.png"

### Walk ###
image genie_walk_ani: #Default Genie walk animation.
    zoom 0.5
    
    "characters/genie/chibis/walk_01.png"
    pause.18
    "characters/genie/chibis/walk_02.png"
    pause.18
    "characters/genie/chibis/walk_03.png"
    pause.18
    "characters/genie/chibis/walk_04.png"
    pause.18
    repeat

image genie_walk_ani_f: #Default Genie walk animation.
    zoom 0.5
    
    im.Flip("characters/genie/chibis/walk_01.png", horizontal=True)
    pause.18
    im.Flip("characters/genie/chibis/walk_02.png", horizontal=True)
    pause.18
    im.Flip("characters/genie/chibis/walk_03.png", horizontal=True)
    pause.18
    im.Flip("characters/genie/chibis/walk_04.png", horizontal=True)
    pause.18
    repeat

### Cupboard ###
image genie_rum_ani:
    zoom 0.5
    
    "characters/genie/chibis/rummage/rum_01.png"
    pause.3
    "characters/genie/chibis/rummage/rum_02.png"
    pause.3
    "characters/genie/chibis/rummage/rum_03.png"
    pause.3
    "characters/genie/chibis/rummage/rum_04.png"
    pause 1
    "characters/genie/chibis/rummage/rum_03.png"
    pause.3
    "characters/genie/chibis/rummage/rum_02.png"
    pause.3
    repeat


### Sitting Desk ###
image newanimation:
    zoom 0.5
    
    "characters/genie/chibis/idle/desk_01.png"
    pause.1
    "characters/genie/chibis/idle/desk_02.png"
    pause.1
    "characters/genie/chibis/idle/desk_03.png"
    pause.1
    "characters/genie/chibis/idle/desk_02.png"
    pause.1
    "characters/genie/chibis/idle/desk_01.png"
    pause 5
    "characters/genie/chibis/idle/desk_01.png"
    pause.15
    "characters/genie/chibis/idle/desk_04.png"
    pause.15
    "characters/genie/chibis/idle/desk_01.png"
    pause.15
    "characters/genie/chibis/idle/desk_04.png"
    pause.15
    "characters/genie/chibis/idle/desk_01.png"
    pause 6
    repeat
    
### Hover desk ###

image newanimation_hover:
    zoom 0.5

    "characters/genie/chibis/idle/desk_hover.png"


### Paperwork ###
image paperwork_02: #Genie working behind his desk.
    zoom 0.5
    
    "characters/genie/chibis/working/01.png"
    pause.15
    "characters/genie/chibis/working/02.png"
    pause.15
    "characters/genie/chibis/working/01.png"
    pause.15
    "characters/genie/chibis/working/02.png"
    pause.15
    "characters/genie/chibis/working/01.png"
    pause.15
    "characters/genie/chibis/working/02.png"
    pause 1
    "characters/genie/chibis/working/03.png"
    pause.15
    "characters/genie/chibis/working/04.png"
    pause.15
    "characters/genie/chibis/working/05.png"
    pause.15
    "characters/genie/chibis/working/06.png"
    pause.15
    "characters/genie/chibis/working/05.png"
    pause.15
    "characters/genie/chibis/working/06.png"
    pause.15
    "characters/genie/chibis/working/05.png"
    pause.15
    "characters/genie/chibis/working/06.png"
    pause 1
    "characters/genie/chibis/working/07.png"
    pause.15
    "characters/genie/chibis/working/08.png"
    pause.15
    "characters/genie/chibis/working/09.png"
    pause.15
    "characters/genie/chibis/working/08.png"
    pause.15
    "characters/genie/chibis/working/07.png"
    pause.15
    "characters/genie/chibis/working/08.png"
    pause.15
    "characters/genie/chibis/working/09.png"
    pause.15
    "characters/genie/chibis/working/08.png"
    pause.15
    "characters/genie/chibis/working/03.png"
    pause.15
    "characters/genie/chibis/working/02.png"
    pause.15
    repeat


### Reading ###
image reading: #Genie reading.
    zoom 0.5
    
    im.Flip("characters/genie/chibis/reading/01.png", horizontal=True)
    pause 2
    im.Flip("characters/genie/chibis/reading/06.png", horizontal=True)
    pause.15
    im.Flip("characters/genie/chibis/reading/05.png", horizontal=True)
    pause.15
    im.Flip("characters/genie/chibis/reading/04.png", horizontal=True)
    pause.15
    im.Flip("characters/genie/chibis/reading/03.png", horizontal=True)
    pause.15
    im.Flip("characters/genie/chibis/reading/02.png", horizontal=True)
    pause.15
    im.Flip("characters/genie/chibis/reading/01.png", horizontal=True)
    pause 2
    repeat

image reading_near_fire: #Genie reading near the fireplace.
    zoom 0.5
    
    "characters/genie/chibis/reading/01.png"
    pause 2
    "characters/genie/chibis/reading/06.png"
    pause.15
    "characters/genie/chibis/reading/05.png"
    pause.15
    "characters/genie/chibis/reading/04.png"
    pause.15
    "characters/genie/chibis/reading/03.png"
    pause.15
    "characters/genie/chibis/reading/02.png"
    pause.15
    "characters/genie/chibis/reading/01.png"
    pause 2
    repeat


### Drinking ###
image genie_toast_goblet: # Genie sitting in front of fireplace, left sire.
    zoom 0.5
    
    "characters/genie/chibis/drinking/01.png"
    pause 2
    "characters/genie/chibis/drinking/02.png"
    pause.2
    "characters/genie/chibis/drinking/03.png"
    pause.2
    "characters/genie/chibis/drinking/04.png"
    pause 1
    "characters/genie/chibis/drinking/03.png"
    pause.2
    "characters/genie/chibis/drinking/01.png"
    pause 3
    repeat
    
### Drinking ###
image genie_toast_goblet_daytime: # Genie sitting in front of fireplace, left sire.
    zoom 0.5
    
    "characters/genie/chibis/drinking/01_day.png"
    pause 2
    "characters/genie/chibis/drinking/02_day.png"
    pause.2
    "characters/genie/chibis/drinking/03_day.png"
    pause.2
    "characters/genie/chibis/drinking/04_day.png"
    pause 1
    "characters/genie/chibis/drinking/03_day.png"
    pause.2
    "characters/genie/chibis/drinking/01_day.png"
    pause 3
    repeat


### Jerking Off ###
image genie_jerking_off: #Genie sitting behind his desk and jerking off...
    zoom 0.5
    
    "characters/genie/chibis/masturbating/desk_01.png"
    pause.2
    "characters/genie/chibis/masturbating/desk_02.png"
    pause.2
    "characters/genie/chibis/masturbating/desk_03.png"
    pause.2
    "characters/genie/chibis/masturbating/desk_02.png"
    pause.2
    repeat

image genie_jerking_sperm_ani: #Sperm after jerking off.
    "characters/genie/chibis/masturbating/desk_sperm_01.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_02.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_03.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_04.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_05.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_06.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_07.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_08.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_09.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_10.png"
    pause.1
    "characters/genie/chibis/masturbating/desk_sperm_11.png"
    pause 2
    repeat

### CUM_02 ###
image genie_cum_03: #Genie cuming on Hermione after she is done striping.
    "characters/genie/chibis/masturbating/sperm_wide_01.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_02.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_03.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_04.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_05.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_06.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_07.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_08.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_09.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_10.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_11.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_12.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_13.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_14.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_15.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_16.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_17.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_18.png"
    pause 2
    "characters/genie/chibis/masturbating/sperm_wide_19.png"
    pause.1
    "characters/genie/chibis/masturbating/sperm_wide_20.png"
    pause.1
    "images/animation/00.png"
    pause.5
    repeat

image grab_mid:
    zoom 0.5
    
    "characters/genie/chibis/grab/grab_01.png"
    pause.5
    "characters/genie/chibis/grab/grab_02.png"
    pause.1
    "characters/genie/chibis/grab/grab_03.png"
    pause.7
    "characters/genie/chibis/grab/grab_02.png"
    pause.1
    "characters/genie/chibis/grab/grab_01.png"

image grab_high:
    zoom 0.5
    
    "characters/genie/chibis/grab/grab_01.png"
    pause.5
    "characters/genie/chibis/grab/grab_02.png"
    pause.1
    "characters/genie/chibis/grab/grab_03.png"
    pause.1
    "characters/genie/chibis/grab/grab_04.png"
    pause.1
    "characters/genie/chibis/grab/grab_05.png"
    pause.5
    "characters/genie/chibis/grab/grab_03.png"
    pause.1
    "characters/genie/chibis/grab/grab_02.png"
    pause.1
    "characters/genie/chibis/grab/grab_01.png"

### Phoenix ###
image petting: #PETTING THE PHOENIX.
    zoom 0.5
    
    "images/rooms/_objects_/phoenix/petting_ani/petting_01.png"
    pause 1
    "images/rooms/_objects_/phoenix/petting_ani/petting_02.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_03.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_04.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_05.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_06.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_05.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_06.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_05.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_06.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_05.png"
    pause.2
    "images/rooms/_objects_/phoenix/petting_ani/petting_04.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_03.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_02.png"
    pause.1
    "images/rooms/_objects_/phoenix/petting_ani/petting_01.png"
    pause 3
    repeat
