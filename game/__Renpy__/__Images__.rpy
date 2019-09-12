default u_ani_pause_img = ""
default u_ani_play_img = ""
default u_ani_xpos = 1
default u_ani_ypos = 1

label set_u_ani(play = u_ani_play_img, pause = u_ani_pause_img, xpos = u_ani_xpos, ypos = u_ani_ypos):
    if play != u_ani_play_img:
        $ u_ani_play_img = play
    if pause != u_ani_pause_img:
        $ u_ani_pause_img = pause
    if xpos != u_ani_xpos:
        $ u_ani_xpos = xpos
    if ypos != u_ani_ypos:
        $ u_ani_ypos = ypos
    return

label u_play_ani:
    hide screen u_ani_pause
    show screen u_ani_play
    with d3
    return
label u_pause_ani:
    hide screen u_ani_play
    show screen u_ani_pause
    with d3
    return

label u_end_ani:
    hide screen u_ani_play
    hide screen u_ani_pause
    with d3
    return

screen u_ani_pause():
    tag u_animation
    add u_ani_pause_img at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)

screen u_ani_play():
    tag u_animation
    add u_ani_play_img at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)

# Common image definitions

image blank:
    "characters/dummy.png"

image textheart = "interface/textheart.png"
image check_07 = "interface/check_07.png"
image check_08 = "interface/check_08.png"

image heart_00 = "interface/heart_00.png"
image heart_01 = "interface/heart_01.png"
image heart_02 = "interface/heart_02.png"
image heart_03 = "interface/heart_03.png"
image heart_04 = "interface/heart_04.png"

image heal:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06

image love_heart:
    "magic/love09.png"
    pause.06
    "magic/love10.png"
    pause.06
    "magic/love11.png"
    pause.06
    "magic/love12.png"
    pause.06
    "magic/love13.png"
    pause.06
    "magic/love14.png"
    pause.06
    "magic/love15.png"

image magic = "magic/magic1.png"
image magic2 = "magic/magic2.png"
image magic3 = "magic/magic3.png"
image magic4 = "magic/magic4.png"
image magic5 = "magic/magic5.png"

image bld = "interface/bld.png"
image bld2 = "interface/bld2.png"
image white = "interface/white.jpg"
image white = "interface/white.jpg"
image blkfade = "interface/blackfade.png"
image blkfade = "interface/blackfade.png"
image whitefade = "interface/whitefade.png"
image whitefade = "interface/whitefade.png"
image con1 = "interface/cont1.png"
image blk50 = im.Alpha("interface/blackfade.png", 0.5)
image blk50 = im.Alpha("interface/blackfade.png", 0.5)

image ctc3 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.995, ypos=0.995, xanchor=1.0, yanchor=1.0)
image ctc4 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.99, ypos=0.995, xanchor=0.8, yanchor=1.0)
image ctc7 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2)

# Emotions ^_^

image emo01:
    "characters/emotes/animated/ex01.png"
    pause.5
    "characters/emotes/animated/ex02.png"
    pause.5
    "characters/emotes/animated/ex03.png"
    pause.5
    "characters/emotes/animated/ex04.png"
    pause 1
    "characters/emotes/animated/ex01.png"
    pause.5
    "characters/emotes/animated/ex00.png"
    repeat

image emo02:
    "characters/emotes/animated/exl01.png"
    pause.5
    "characters/emotes/animated/exl02.png"
    pause.5
    "characters/emotes/animated/exl03.png"
    pause.5
    "characters/emotes/animated/exl04.png"
    pause.5
    "characters/emotes/animated/exl05.png"
    pause.5
    "characters/emotes/animated/exl06.png"
    repeat

image emo03:
    "characters/emotes/animated/sad_01.png"
    pause.4
    "characters/emotes/animated/sad_02.png"
    pause.4
    "characters/emotes/animated/sad_03.png"
    pause.4
    "characters/emotes/animated/sad_04.png"
    pause.4
    "characters/emotes/animated/sad_03.png"
    pause.4
    "characters/emotes/animated/sad_02.png"
    pause.4
    repeat

image emo04:
    "characters/emotes/animated/hoot_01.png"
    pause.4
    "characters/emotes/animated/hoot_02.png"
    pause.4
    "characters/emotes/animated/hoot_03.png"
    pause.4
    "characters/emotes/animated/hoot_04.png"
    pause.4
    "characters/emotes/animated/hoot_05.png"
    pause.4
    "characters/emotes/animated/hoot_06.png"
    pause.4
    "characters/emotes/animated/hoot_07.png"
    pause.4
    repeat

image emoq:
    "characters/emotes/animated/q1.png"
    pause.5
    "characters/emotes/animated/q2.png"
    pause.5
    "characters/emotes/animated/q3.png"
    pause.5
    "characters/emotes/animated/q4.png"
    pause.5
    "characters/emotes/animated/q1.png"
    pause.5
    "characters/emotes/animated/q2.png"
    pause.5
    "characters/emotes/animated/q3.png"
    pause.5
    "characters/emotes/animated/q4.png"
    repeat

image emom:
    "characters/emotes/animated/emo00.png"
    pause.08
    "characters/emotes/animated/emo01.png"

image excl:
    "characters/emotes/animated/excl01.png"
    pause.5
    "characters/emotes/animated/excl02.png"
    pause.5
    "characters/emotes/animated/excl03.png"
    pause.5
    "characters/emotes/animated/excl04.png"
    pause.5
    repeat
image qu:
    "characters/emotes/animated/que1.png"
    pause.5
    "characters/emotes/animated/que2.png"
    pause.5
    "characters/emotes/animated/que3.png"
    pause.5
    "characters/emotes/animated/que4.png"
    pause.5
    "characters/emotes/animated/que5.png"
    pause.5
    "characters/emotes/animated/que6.png"
    repeat

image an:
    "characters/emotes/animated/an1.png"
    pause.2
    "characters/emotes/animated/an2.png"
    pause.2
    "characters/emotes/animated/an3.png"
    pause.2
    "characters/emotes/animated/an2.png"
    pause.2
    repeat

image sal:
    "characters/emotes/animated/s1.png"
    pause.08
    "characters/emotes/animated/s2.png"
    pause.2
    "characters/emotes/animated/s3.png"
    pause.08
    "characters/emotes/animated/s4.png"
    pause.2
    "characters/emotes/animated/s5.png"
    pause.08
    "characters/emotes/animated/s6.png"
    pause 1
    "characters/emotes/animated/00.png"
    pause.08
    repeat

image th:
    "characters/emotes/animated/t1.png"
    pause.2
    "characters/emotes/animated/t2.png"
    pause.2
    "characters/emotes/animated/t3.png"
    pause.2
    "characters/emotes/animated/t4.png"
    pause.2
    repeat

image emo7:
    "characters/emotes/animated/emotion00.png"
    pause.5
    "characters/emotes/animated/emotion01.png"
    pause.5
    "characters/emotes/animated/emotion00.png"
    pause.7
    "characters/emotes/animated/emotion01.png"
    pause.7
    "characters/emotes/animated/emotion00.png"
    pause.6
    "characters/emotes/animated/emotion01.png"
    pause.6
    repeat

image emo8:
    "characters/emotes/animated/emotion00.png"
    pause.7
    "characters/emotes/animated/emotion03.png"
    pause.7
    "characters/emotes/animated/emotion00.png"
    pause.6
    "characters/emotes/animated/emotion03.png"
    pause.6
    "characters/emotes/animated/emotion00.png"
    pause.5
    "characters/emotes/animated/emotion03.png"
    pause.5
    repeat

image sur:
    "characters/emotes/animated/sur1.png"
    pause.5
    "characters/emotes/animated/sur2.png"
    pause.5
    "characters/emotes/animated/sur3.png"
    pause.5
    "characters/emotes/animated/sur4.png"
    pause.5
    "characters/emotes/animated/sur5.png"
    pause.5
    "characters/emotes/animated/sur6.png"
    pause.5
    repeat
