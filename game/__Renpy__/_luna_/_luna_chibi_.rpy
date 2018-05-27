

### LUNA CHIBI ###

screen luna_walk:
    tag luna_chibi
    add "ch_lun walk_a" at custom_walk_02(walk_xpos+140, walk_xpos2)
    zorder 4
screen luna_walk_f: #Luna Chibi. walking. animation. facing right. (Leaving tower).
    tag luna_chibi
    add "ch_lun walk_a_flip" at custom_walk_02(walk_xpos+140, walk_xpos2)
    zorder 4
screen luna_blink: #Luna stands still and blinks.
    tag luna_chibi
    add "ch_lun blink_a" at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
    zorder 4
screen luna_blink_f: #Luna stands still and blinks.
    tag luna_chibi
    add "ch_lun blink_a_flip" at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
    zorder 4


screen luna_01: #Luna stands still.
    tag luna_chibi
    add "characters/luna/chibis/walk/l_walk_a_01.png" at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
screen luna_01_f: #Luna stands still. (MIRRORED)
    tag luna_chibi
    add im.Flip("characters/luna/chibis/walk/l_walk_a_01.png", horizontal=True) at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
screen luna_02: #Luna stands still and blinks.
    tag luna_chibi
    add "ch_lun blink_a" at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
screen luna_walk_01:
    tag luna_chibi
    add "ch_lun walk_a" at custom_walk_02(walk_xpos+140, walk_xpos2)
screen luna_walk_01_f: #Luna Chibi. walking. animation. facing right. (Leaving tower).
    tag luna_chibi
    add "ch_lun walk_a_flip" at custom_walk_02(walk_xpos+140, walk_xpos2)
screen luna_chibi_robe: #Luna. Chibi. Walking. Wearing a robe.
    tag luna_chibi
    add "ch_lun walk_robe" at custom_walk_02(walk_xpos+140, walk_xpos2)
screen luna_chibi_robe_f: #Luna. Chibi. Walking. Wearing a robe.
    tag luna_chibi
    add "ch_lun walk_robe_flip" at custom_walk_02(walk_xpos+140, walk_xpos2)
screen luna_02_b: #Luna stands still wearing a robe.
    tag luna_chibi
    add "characters/luna/chibis/walk/l_walk_robe_01.png" at Position(xpos=luna_chibi_xpos+140, ypos=luna_chibi_ypos)
    


label luna_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = luna_speed, loiter = False,redux_pause = 0):
    hide screen luna_walk
    hide screen luna_walk_f
    $ walk_xpos = pos1 #(From)
    $ walk_xpos2 = pos2 #(To)
    $ luna_chibi_ypos = 250
    $ luna_speed = speed #Speed of walking animation. (lower = faster)
    hide screen luna_blink
    hide screen luna_blink_f
    if pos1 > pos2: #right to left (luna_walk)
        show screen luna_walk
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk
        if loiter:
            show screen luna_blink
    else: #left to right (luna_walk_f)
        show screen luna_walk_f
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk_f
        if loiter:
            show screen luna_blink_f
    return
    
label luna_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
        with Dissolve((dissolveTime/10))
    else:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
    return