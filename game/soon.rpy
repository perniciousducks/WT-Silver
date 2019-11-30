define _flashwhite = Fade(0.3, 0.2, 0.5, color='#fff')
define _flashwhite_slow = Fade(0.7, 0.5, 0.7, color='#fff')

define _shake_long = Move((0, 25), (0, -25), 0.2, bounce=True, repeat=True, delay=1.0)

image _her_lift_top:
    zoom 0.45
    xoffset -39
    yoffset -1
    
    contains:
        "characters/hermione/chibis/lift_top/boing01.png"
        pause 1.0
        "characters/hermione/chibis/lift_top/boing01.png"
        pause.22
        "characters/hermione/chibis/lift_top/boing02.png"
        pause.22
        "characters/hermione/chibis/lift_top/boing03.png"
        pause.22
        "characters/hermione/chibis/lift_top/boing04.png"
        pause.22
        "characters/hermione/chibis/lift_top/boing05.png"
        
image _her_lift_top_blink:
    zoom 0.45
    xoffset -39
    yoffset -1
    
    "characters/hermione/chibis/lift_top/boing05.png"
    pause 2
    "characters/hermione/chibis/lift_top/boing06.png"
    pause.08
    "characters/hermione/chibis/lift_top/boing05.png"
    pause 5
    "characters/hermione/chibis/lift_top/boing06.png"
    pause.08
    "characters/hermione/chibis/lift_top/boing05.png"
    pause.08
    "characters/hermione/chibis/lift_top/boing06.png"
    pause.08
    "characters/hermione/chibis/lift_top/boing05.png"
    pause 3

    repeat
    
image _qp_grope:
    contains:
        "images/super_secret/qp_0.png"
        pause.2
        "images/super_secret/qp_1.png"
        pause.2
        "images/super_secret/qp_2.png"
        pause.2
        "images/super_secret/qp_0.png"
        pause.2
        "images/super_secret/qp_1.png"
        pause.2
        repeat
    
image ghost_1_snape_walk:
    zoom 0.5
    
    "characters/snape/chibis/ghost_1/01.png"
    pause.18
    "characters/snape/chibis/ghost_1/02.png"
    pause.18
    "characters/snape/chibis/ghost_1/01.png"
    pause.18
    "characters/snape/chibis/ghost_1/03.png"
    pause.18
    repeat
    
image ghost_1_snape_stand:
    zoom 0.5
    
    "characters/snape/chibis/ghost_1/02.png"
    
image ghost_2_snape_walk:
    zoom 0.5
    
    "characters/snape/chibis/ghost_2/01.png"
    pause.18
    "characters/snape/chibis/ghost_2/02.png"
    pause.18
    "characters/snape/chibis/ghost_2/01.png"
    pause.18
    "characters/snape/chibis/ghost_2/03.png"
    pause.18
    repeat
    
image ghost_2_snape_stand:
    zoom 0.5
    
    "characters/snape/chibis/ghost_2/02.png"
    
image ghost_3_snape_walk:
    zoom 0.5
    
    "characters/snape/chibis/ghost_3/01.png"
    pause.18
    "characters/snape/chibis/ghost_3/02.png"
    pause.18
    "characters/snape/chibis/ghost_3/01.png"
    pause.18
    "characters/snape/chibis/ghost_3/03.png"
    pause.18
    repeat
    
image ghost_3_snape_stand:
    zoom 0.5
    
    "characters/snape/chibis/ghost_3/02.png"
    
image ghost_genie_stand:
    zoom 0.5
    
    "characters/genie/chibis/ghost_stand.png"
    
image ghost_genie_stand_alternative:
    zoom 0.5
    
    "characters/genie/chibis/ghost_stand2.png"
    
screen _her_controller(idle=False):
    tag hermione_chibi
    zorder her_chibi_zorder

    if not idle:
        add "_her_lift_top" xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip
    else:
        add "_her_lift_top_blink" xpos her_chibi_xpos ypos her_chibi_ypos xzoom her_chibi_flip

screen _location_0(bang=False):
    tag loc
    zorder 0

    add Solid("#000000")

    if not bang:
        add "glow_effect" zoom 0.2 anchor (0.5, 0.5) align (0.5, 0.5)

    if bang:
        add "images/super_secret/bang.png":
            at transform:
                zoom 0.0
                anchor (0.5, 0.5)
                pos (540, 300)
                easeout 15.0 zoom 2.7

screen _location_1():
    tag loc
    zorder 0

    add "_qp_grope"
    
screen _location_1_overlay():
    tag loc_ov
    zorder 3
    
    add "images/rooms/quidditch_pitch/tower_overlay.png"
    add "images/rooms/quidditch_pitch/hole.png"

screen _location_2():
    tag loc
    zorder 0

    add "images/super_secret/ss_office.png" zoom 0.5

    add "candle_fire_01" xpos 437 ypos 97
    add "candle_fire_01" xpos 420 ypos 97
    add "candle_fire_01" xpos 454 ypos 97
    
screen _location_3():
    tag loc
    zorder 3
    
    add "images/super_secret/youknowwho.png" xpos 830 ypos 250 zoom 0.5

screen _jerking_off(): #Genie sitting behind his desk and jerking off...
    tag genchi
    zorder 1
    add "genie_jerking_off" xpos 218 ypos 205

screen _sitting():
    tag genchi
    zorder 1
    add "newanimation" xpos 218 ypos 205

screen _standing():
    tag genchi
    zorder 1
    add "genie_stand_ani" xpos 500 ypos 190 xzoom 1

screen _kek():
    tag kek
    zorder 10
    add "images/super_secret/kek.png" anchor (0.5, 0.5) xalign 0.5 yalign 0.7

label xmas:
    call blkfade
    "You fall asleep and as you drift off, the power of Christmas grabs a hold of your soul."
    menu:
        "This story contains some potential spoilers and information about future patches, do you wish to continue or do you want to skip until tomorrow?"
        "Yes":
            pass
        "No (skip)":
            $ persistent.xmas_2019 = True
            jump main_room
            
    call hide_blkfade
    
    # Setup
    stop weather
    $ weather_gen = 5
    $ snow_gen = 1
    $ snowing = True
    $ weather_animations = ["snow"]
    show screen weather
    
    $ sna_chibi_stand = "ghost_1_snape_stand"
    $ sna_chibi_walk = "ghost_1_snape_walk"

    $ renpy.sound.play("sounds/snore1.mp3")
    m "*Snore*{w=2.0}{nw}"
    pause 1.0
    $ renpy.sound.play("sounds/snore3.mp3")
    m "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
    pause 1.0
    $ renpy.sound.play("sounds/snore2.mp3")
    m "......{w=0.5}*Snore*{w=1.0}{nw}"

    stop music fadeout 4.0
    $ renpy.sound.play("sounds/magic4.ogg")
    play bg_sounds "sounds/rumble.mp3" fadein 2
    call sna_chibi("stand","mid","base")
    with _flashwhite

    pause 0.7

    $ renpy.sound.play("sounds/MaleGasp.mp3")
    g4 "{size=+10}BLOODY HELL!{/size}"
    g4 "Who-... Wha-..."
    m "............."
    m "Snape, is that you?"
    g4 "Why are you wearing a blanket?"
    play music "music/Anguish.mp3" fadein 4
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I am the ghost of Christmas paaaaaast..."
    call sna_walk(xpos="desk", ypos="base", speed=2)
    m "Oh fuck,{w=0.5} I know this story..."
    m "Let me guess, you're here to tell me of some moral wrongdoing and convince me to get on the right path..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I am here to tell you of your moral wrooooongdoings, to set you on the right paaaaaath!" #about is technically corrrect, but 'of' sounds more dramatic and archaic, which is how i imagine the ghost of christmas past
    m "I knew it..."
    m "..."
    m "Just get to the flashback..."
    m "...{w=0.4}...{w=0.4}..."
    m "So, how long does this usually...{w=0.5}{nw}"
    #Flashback Overlay, screen is Black and white?
    #Genie and Christmas past ghost stands in the doorway (Slightly transparent)
    #
    $ gen_chibi_stand = "ghost_genie_stand"
    call room(hide_screens=True)
    $ renpy.sound.play("sounds/magic1.ogg")
    stop music fadeout 3
    show screen _location_0
    call sna_chibi("stand", 520, "base")
    call gen_chibi("stand", 400, "base")
    with _flashwhite_slow
    m "...take"
    m "...{w} Where...{w=0.7}{nw}"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Boooah shit, I must've hit the skip chapter button instead of rewind..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "The universe hasn't been createeeeed yet."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Give me a mooooooment!"
    $ gen_chibi_stand = "ghost_genie_stand_alternative"
    call gen_chibi("stand", 400, "base")
    with d3
    pause 1.0
    play bg_sounds "sounds/rumble.mp3" fadein 2
    m "What is that small point over there?"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "The uuuuuniverse.{w=1.0} And it is aboooooout to expand."
    $ gen_chibi_stand = "ghost_genie_stand"
    call gen_chibi("stand", 400, "base")
    with d3
    pause 1.0
    g4 "Expand?{w=0.4} Didn't it start with..{w=0.4} a bang?{w=0.8} {size=+4}a big bang?!{/size}"
    show screen _location_0(True)
    pause 1.5
    $ renpy.sound.play("sounds/bang.mp3")
    with _shake_long
    g4 "Take us out of here!{w=3.5}{nw}"
    $ renpy.sound.play("sounds/ghost2.mp3")
    "\"Ghost\"" "Hoooold ooooon, I'm wooooorking on it!{w=5.0}{nw}"
    #
    hide screen _location_0
    $ renpy.sound.stop(fadeout=2.0)
    play sound "sounds/magic1.ogg"
    call room("main_room", hide_screens=False)
    call gen_chibi("stand", 400, "base")
    show screen dumbledore
    with _flashwhite_slow
    play music "music/Anguish.mp3" fadein 6
    m "Aight, wher-...{w=0.4} {b}when{/b} the fuck are we?"
    call gen_chibi("stand", 400, "base", flip=True)
    with d3
    pause 1.0
    m "Hold on a second, that's not me..."
    m "It's that Dumbledore guy..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Duuuumbledooooore, you're looking at yourself from the paaaast..."
    call gen_chibi("stand", 400, "base", flip=False)
    with d3
    pause 1.0
    m "I think you got the wrong dude."
    call gen_chibi("stand", 400, "base", flip=True)
    with d3
    pause 1.0
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Loooook at this old maaaan..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Aloooone in his office..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "No frieeeeends..."
    m "Maybe he's just an introvert."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "And no bitches to baaaaaang."
    m "Some people just likes bo...{w=0.4}Sorry, what?"
    call gen_chibi("stand", 400, "base", flip=False)
    with d3
    pause 1.0
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "There's not a single bitch in this rooooom."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "All aloooooone...."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "No friends."
    m "(Is this guy just reading a script?)"
    $ renpy.sound.play("sounds/MaleGasp.mp3")
    g4 "Hey, look at that naked chick at the door!"
    #call gen_walk(xpos="door", ypos="base", speed=2)

    #call gen_chibi("stand", "door", "base", flip=True)
    #call sna_chibi("stand", 520, "base", flip=True)
    #with d3
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "You shall also be visited by the ghost of Christmas present and the ghost of Christmas future."
    m "Surprise surprise..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Now, to return to the present!"

    $ renpy.sound.play("sounds/magic1.ogg")
    stop music fadeout 5
    stop bg_sounds fadeout 4
    hide screen dumbledore
    call sna_chibi("hide")
    call gen_chibi("sit_behind_desk")
    with _flashwhite_slow

    m "Well... that was weird..."
    m "So the {w=0.4}\"ghost\"{w=0.4} wants me to do what I'm literally already doing..."
    m "Yeah, real subtle Snape..."

    call blkfade
    centered "{size=+7}{color=#cbcbcb}The Next Evening..{/color}{/size}{w=3.0}{nw}"
    call music_block
    call hide_blkfade
    pause 1.0

    $ renpy.sound.play("sounds/snore1.mp3")
    m "*Snore*{w=2.0}{nw}"

    $ renpy.sound.play("sounds/snore3.mp3")
    m "*Sn{cps=8}oooooooreeee*{/cps}{w=1.0}{nw}"
    
    $ sna_chibi_stand = "ghost_2_snape_stand"
    $ sna_chibi_walk = "ghost_2_snape_walk"

    stop music fadeout 4.0
    $ renpy.sound.play("sounds/magic4.ogg")
    play bg_sounds "sounds/rumble.mp3" fadein 2
    call sna_chibi("stand","mid","base")
    with _flashwhite

    call sna_walk(xpos="desk", ypos="base", speed=2)

    $ renpy.sound.play("sounds/snore2.mp3")
    m "......{w=0.5}*Snore*{w=1.0}{nw}"

    call sna_chibi("stand", "desk", "base", flip=True)
    with d3
    pause 0.8
    call sna_chibi("stand", "desk", "base", flip=False)
    with d3
    pause 0.5

    $ renpy.sound.play("sounds/ghost2.mp3")
    "\"Ghost\"" "{cps=60}I am the ghost of christmas present!{/cps}" with hpunch
    $ renpy.sound.play("sounds/drop.mp3")
    g4 "{size=+10}GAH!{/size}"
    pause 0.5
    g4 "{size=-4}You'll be the death of me, I swear...{/size}"
    pause 1.0
    play music "music/Anguish.mp3" fadein 4
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I am here to tell you about your moral wrongdoings, to set you on the right path!"
    m "..."
    m "You're still just Snape in a blanket..."
    m "And you better tell me before you do the...{w=1.0}{nw}"

    $ renpy.sound.play("sounds/magic1.ogg")
    with _flashwhite_slow

    g4 "What the, what did I just say..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "This is your present Dumbledore..."
    m "..."
    m "I'm still in my chair though...{w=0.4} Where's that Dumbledore guy."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Sitting in that chair..."
    m "Yes?"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Still no bitcheeeees..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "All aloooooone...."
    m "No friends?"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "No friends."
    m "This is just a repeat from the last one."
    m "This isn't a Christmas tale, this is some time loop bullshit..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Next, you will be visited by the ghost of Christmas future."
    m "Yep yep, return to the present...{w=0.4} Flashing light...{w=0.4} Burnt cornea...{w=0.4} Got it."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Now, to return to the present!"

    call sna_chibi("hide")
    $ renpy.sound.play("sounds/magic1.ogg")
    with _flashwhite_slow
    stop music fadeout 5
    stop bg_sounds fadeout 4

    pause 1.0

    m "Damnit, this must be some curse Snape set up for the old man before I arrived..."
    m "Did Snape really expect anyone to fall for this?"
    g4 "So how am I supposed convince this \"ghost\" following some shit script that I'm not Dumbledore..."
    m "Maybe I'll just play out the story and tick the {b}yes{/b} box for bitches at the end."

    call blkfade
    centered "{size=+7}{color=#cbcbcb}The Next Evening..{/color}{/size}{w=3.0}{nw}"
    call music_block
    $ sna_chibi_stand = "ghost_3_snape_stand"
    $ sna_chibi_walk = "ghost_3_snape_walk"
    call hide_blkfade
    pause 1.0
    $ renpy.sound.play("sounds/magic4.ogg")
    play bg_sounds "sounds/rumble.mp3" fadein 2
    call sna_chibi("stand","mid","base")
    with _flashwhite
    pause 1.0
    $ renpy.sound.play("sounds/snore1.mp3")
    m "*Snore*{w=2.0}{nw}"
    pause 1.0

    call sna_chibi("stand", "mid", "base", flip=True)
    with d3
    pause 0.8
    call sna_chibi("stand", "mid", "base", flip=False)
    with d3
    pause 0.5
    call sna_walk(xpos="desk", ypos="base", speed=2)

    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I am the gho-...{w=0.3}{nw}"
    stop music fadeout 1
    $ renpy.sound.play("sounds/punch01.mp3")
    g4 "Aha! Got you this time!" with vpunch
    m "You are not scaring me again, you Knob-Jockey!"
    play music "music/Anguish.mp3" fadein 4

    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I am the ghost of Christmas futuuuure..."
    m "Yep..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "You have yet to change your waaaaays..."
    m "I mean, you assume that..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Now, to show you your fuuuuuture."
    m "Fine...{w=0.4} But I'm closing my eyes this time cause this shit is getting annoying."

    $ renpy.sound.play("sounds/magic1.ogg")
    call sna_chibi("stand", 720, "base")
    call gen_chibi("stand", 600, "base", flip=True)
    call her_chibi("stand","desk","base")
    show screen _sitting
    with _flashwhite_slow
    pause 1.0

    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "This is you in the future..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "All alo...{w=0.5}{nw}"
    stop music fadeout 5
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Wait, who's this girl..."
    m "I told you shit's about to happen!"
    g9 "And it looks like we've got front row seats!"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "No, this isn't riiiiight."
    g9 "Oh yes baby...."
    pause 1.0
    call play_music("hermione_theme")
    her "You want me to take off my top sir?"
    her "Why of course!"

    show screen _her_controller
    with d3
    pause 1.0
    $ renpy.sound.play("sounds/boing02.mp3")
    pause 0.9

    show screen _her_controller(True)
    pause 1.0
    show screen _jerking_off
    with d3
    pause 1.0
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "You're supposed to be alooooone..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "This is the wroooong futuuuure."
    g9 "Looks right to me..."
    g9 "I thought this is what you wanted."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "I was supposed to help youuuuu...."
    g9 "Then go further..."
    m "Go further in my future."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Yes..."
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Fuuuuuuurther..."
    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    call her_chibi("hide")
    call ton_chibi("stand","desk","base")
    hide screen _her_controller
    show screen _sitting
    with _flashwhite_slow
    pause 1.0
    call play_music("tonks_theme")
    ton "Hmm... Why don't you find out for yourself..."
    ton "These puppies have been clambering to get out their basket..."
    pause 1.0
    $ renpy.sound.play("sounds/cloth_sound.mp3")
    $ tonks_class.strip("robe")
    with d3
    pause 0.8
    $ tonks_class.strip("top")
    with d3
    pause 1.0
    show screen _jerking_off
    with d3
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "No... This isn't what's supposed to happen..."
    if not tonks_unlocked:
        g9 "Looks like the future is bright, look at that hot lady!"
        m "Wonder what her name is..."
    else:
        g9 "Looks like the future is bright, look at that hot body!"
        g9 "You go Tonks!"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "Noooo, this is wrong. You can't seeee thiiis."

    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    call ton_chibi("hide")
    call lun_chibi("stand","desk","base")
    show screen _sitting
    with _flashwhite_slow

    pause 1.0

    m "When are we now?"
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "We're back in the preeesent."
    m "You sure, there's another girl there."
    call play_music("luna_theme")
    lun "You want me to help you again sir?"
    lun "With my mouth?"
    show screen _jerking_off
    with d3
    pause 1.0
    $ renpy.sound.play("sounds/ghost2.mp3")
    "\"Ghost\"" "{cps=10}Stoooooooooooooooop{/cps}"

    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    $ cho_class.strip("all")
    call lun_chibi("hide")
    call cho_chibi("stand","desk","base")
    show screen _sitting
    with _flashwhite_slow

    pause 1.0
    show screen _jerking_off
    with d3
    call play_music("cho_theme")

    cho "You'd better get Hermione in here then, that should convince you whose naked body is better!"
    "\"Dumbledore\"" "That's a splendid idea!"
    g9 "Splendid indeed!" #Swap the portrait to the right so it's the other genie saying it

    pause 0.5

    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    $ cho_class.strip("all")
    call cho_chibi("hide")
    call sus_chibi("stand",400,"base", flip=True)
    call ast_chibi("stand",530,"base")
    show screen _sitting
    with _flashwhite_slow

    pause 1.0
    call play_music("astoria_theme")

    ast "Imperio!{w=0.7}{nw}"
    call play_sound("spell")
    call ast_chibi(action="wand_imperio",xpos="530",ypos="base")
    pause 1.5
    sus "GAH!"
    ast "Now take out your tits, you cow!"
    $ susan_wear_top = False
    $ susan_wear_bra = False
    call update_sus_uniform
    with d3
    $ renpy.sound.play("sounds/boing03.mp3")
    pause 1.0
    show screen _jerking_off
    with d3
    pause 1.0

    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    $ gen_chibi_zorder = 1
    call room(hide_screens=True)
    hide screen _jerking_off
    show screen _location_1
    show screen _location_1_overlay
    call sna_chibi("stand", 110, 60, flip=True)
    call gen_chibi("stand", 150, 20, flip=False)
    with _flashwhite_slow
    $ renpy.music.play("music/11 The Quidditch Match_original.mp3", fadein=1)
    pause 1.0

    #Genie and Snape floating here looks a bit weird
    #her "YEEEEESSS!"
    pause 0.5
    $ renpy.sound.play("sounds/crowd_cheer.mp3")
    her "*Hmm*{w=0.3} Those boys are going... Ahh{w=0.5}, going way too fast! This game might be over before we know it!"
    pause 2.0

    stop music fadeout 2
    $ renpy.sound.play("sounds/magic1.ogg")
    $ gen_chibi_zorder = 2
    hide screen _location_1_overlay
    show screen _location_2
    call sna_chibi("stand", 160, "base", flip=True)
    call gen_chibi("stand", 250, "base", flip=False)
    show screen _standing
    with _flashwhite_slow

    pause 1.0
    #call play_music("snape_theme")
    $ renpy.music.play("music/the-chamber-by-kevin-macleod.mp3")
    play bg_sounds "sounds/brewing_idle.mp3" fadeout 1.0 fadein 1.0

    "\"Ghost\"" "What are you doing in my office? I told you not to wander around the castle..."

    # reset outfits
    $ tonks_class.wear("all")
    $ cho_class.wear("all")
    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform

    hide screen _location_2
    stop music fadeout 2
    stop bg_sounds fadeout 2
    $ renpy.sound.stop(fadeout=2.0)
    play sound "sounds/magic1.ogg"
    call room("main_room", hide_screens=False)
    show screen _sitting
    call sna_chibi("stand", 720, "base")
    call gen_chibi("stand", 600, "base", flip=True)
    call ton_chibi("stand","desk","base")
    with _flashwhite_slow

    pause 1.0
    play music "music/Juhani_Junkala.mp3" fadein 2

    ton "You want me to play..."

    call ton_chibi("hide")
    call sus_chibi("stand","desk","base")
    with _flashwhite

    sus "...a cardgame?"

    call sus_chibi("hide")
    call ast_chibi("reset","desk","base")
    with _flashwhite

    $ renpy.play('sounds/scratch.wav')
    stop music fadeout 1
    ast "But that's literally strip poker!"
    ast "..."
    play music "music/Juhani_Junkala.mp3" fadein 1
    ast "Sign me up!" # evil smile
    pause 0.5

    stop music fadeout 2
    stop bg_sounds fadeout 2
    play sound "sounds/magic1.ogg"
    $ gen_chibi_zorder = 4
    $ sna_chibi_zorder = 4
    call room("main_room", hide_screens=False)
    call sna_chibi("stand", 720, "base")
    call gen_chibi("stand", 600, "base", flip=True)
    call ast_chibi("hide")
    with _flashwhite_slow

    pause 1.0
    call play_sound("knocking")
    pause 1.0
    m "Come in!"
    pause 0.8
    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    her "Sir, I brought that girl I told you about."
    pause 1.0
    call play_sound("door")
    show screen _location_3
    with d3
    pause 1.0
    $ renpy.play('sounds/giggle.mp3')
    "???" "Hello professor.{image=textheart}"
    pause 1.0
    call blkfade
    hide screen _location_3
    centered "{size=+7}{color=#cbcbcb}Soon.{/color}{/size}{w=1.0}{nw}"
    $ renpy.play('sounds/pop01.mp3')
    show screen _kek
    centered "{size=+7}{color=#cbcbcb}Soon.{/color}{/size}{fast}"

    hide screen _kek
    call room("main_room", hide_screens=False)
    hide screen _sitting
    call sna_chibi("stand", "desk", "base")
    call gen_chibi("sit_behind_desk")
    call her_chibi("hide")
    call hide_blkfade

    play music "music/Anguish.mp3" fadein 4
    "\"Ghost\"" "{cps=2}...{/cps}"
    stop bg_sounds fadeout 4
    $ renpy.sound.play("sounds/ghost1.mp3")
    "\"Ghost\"" "What is my purpose..."
    m "Looks to me like your job is done."
    m "Why don't you slide through that door and revaluate your existence..."
    m "Bitches box, checked!"
    stop music fadeout 1
    play sound "sounds/boing.mp3"
    call sna_chibi("hide")
    with d1
    pause 1.0
    m "Well, that was fun..."
    m "Now for some shut eye..."
    m "Not sure I'll be able to sleep after all this excite{nw}"
    $ renpy.sound.play("sounds/snore1.mp3")
    m "Not sure I'll be able to sleep after all this excite{fast}...*Snore*."

    call blkfade
    # unlock decorations and add to room
    $ fireplace_xmas_ITEM.unlocked = True
    $ phoenix_xmas_ITEM.unlocked = True
    $ owl_xmas_ITEM.unlocked = True
    
    $ fireplace_deco_OBJ.room_image = fireplace_xmas_ITEM.id
    $ fireplace_xmas_ITEM.active = True
    
    $ phoenix_deco_OBJ.room_image = phoenix_xmas_ITEM.id
    $ phoenix_xmas_ITEM.active = True
    
    $ owl_deco_OBJ.room_image = owl_xmas_ITEM.id
    $ owl_xmas_ITEM.active = True
    #
    $ renpy.sound.play("sounds/snore3.mp3")
    m "*Snore*{w=2.0}{nw}"
    $ renpy.sound.play("sounds/snore2.mp3")
    m "......{w=0.5}*Snore*"
    san_[1] "Merry Christmas and a Happy new year!"
    san_[4] "See you all in 2020 for update 1.38...."
    call hide_blkfade

    # reset
    $ gen_chibi_zorder = 2
    $ sna_chibi_zorder = 2
    $ tonks_class.wear("all")
    $ cho_class.wear("all")

    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform
    $ sna_chibi_stand = "snape_stand"
    $ sna_chibi_walk = "snape_walk"
    $ gen_chibi_stand = "genie_stand_ani"
    
    $ persistent.xmas_2019 = True
    jump main_room
