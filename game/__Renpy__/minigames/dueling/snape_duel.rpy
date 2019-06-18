
init python:
    class silver_duel(object):
        in_progress = False
        snape = ""
        genie = ""

        def show(self,image=None,x=690,y=250,z=5):
            renpy.show(image,at_list=[Position(xpos=x, ypos=y, xanchor="center", yanchor="center")],layer="screens",zorder=z)
        def hide(self,image=None):
            renpy.hide(image,layer="screens")

    duel_OBJ = silver_duel()

label __init_variables:

    $ genie_max_hp = 1000
    $ snape_max_hp = 2000

    if not hasattr(renpy.store,'genie_hp'): #important!
        $ genie_hp = genie_max_hp
    if not hasattr(renpy.store,'snape_hp'): #important!
        $ snape_hp = snape_max_hp
    if not hasattr(renpy.store,'blocking'): #important!
        $ blocking = False
    if not hasattr(renpy.store,'snape_blocking'): #important!
        $ snape_blocking = False
    if not hasattr(renpy.store,'pentogram'): #important!
        $ pentogram = False

    return


label duel:
    ### DUEL ###
    $ d_flag_01 = False #Turns True after conversation triggered when Genie's HP runs low.
    $ d_flag_02 = False #Turns True after conversation triggered when Snape's HP runs low.

    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.

    # Hide all the screens.

    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen genie
    hide screen owl
    hide screen points
    hide screen ctc
    hide screen snape_defends
    hide screen blkfade


    ### Set Duel Defaults ###
    $ genie_hp = genie_max_hp
    $ snape_hp = snape_max_hp

    $ blocking = False #True when "block" command is chosen, when Gennie turn into a guard.
    $ snape_blocking = False #True when Snape goes into defensive stance.
    $ pentogram = False #True when pentagram been casted an is displayed on the floor.

    show screen duel

    hide screen snape_glass
    hide screen bld1
    with fade
    call ctc

    call bld
    m "This is foolish... You are no match for me..."
    call sna_main("Amusing...","snape_01", ypos="head")
    m "{size=-4}(Actually my human body is quite weak...){/size}"
    m "{size=-4}(But I should still be way more powerful than any human wizard...){/size}"
    call sna_main("Let the duel begin!","snape_01")
    hide screen bld1
    show screen hp_bar
    $ duel_OBJ.in_progress = True
    with d5


label duel_main:
    if genie_hp <= 300 and not d_flag_01:
        $ d_flag_01 = True
        call sna_main("Ready to give up yet?","snape_01", ypos="head")
        g4 "Tsk..."

    if snape_hp <= 400 and not d_flag_02:
        $ d_flag_02 = True
        g4 "{size=-4}(He is getting weaker, I can feel it!){/size}"
        call sna_main("*Panting*","snape_01", ypos="head")

    hide screen bld1
    call screen duel_buttons


screen duel_buttons():
    zorder 10

    imagebutton: # attack
        xpos 802
        yalign 1.0
        focus_mask True
        idle "images/dueling/snape/hp_bar_03.png"
        hover "images/dueling/snape/hp_bar_04.png"
        action [Jump("main_attack")]
    imagebutton: # aguard
        xpos 868
        yalign 1.0
        focus_mask True
        idle "images/dueling/snape/hp_bar_07.png"
        hover "images/dueling/snape/hp_bar_06.png"
        action [Jump("main_defend")]
    imagebutton: # item
        xpos 954
        yalign 1.0
        focus_mask True
        idle "images/dueling/snape/hp_bar_09.png"
        hover "images/dueling/snape/hp_bar_08.png"
        action [Jump("main_potion")]


label main_attack:
    $ blocking = False #To stop the game treating Genie as being in a block stance.
    if snape_blocking:
        $ snape_blocking = False
        pause 1
        jump snape_defends
    else:
        jump genie_attack

label main_defend:
    $ blocking = True
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=690, y=250,z=5)
    $ duel_OBJ.genie = "defend"
    pause 1
    jump snapes_turn

label main_potion:
    if potions >= 1:
        jump potion
    else:
        m "Crap! I'm out of healing potions!"
        jump duel_main



### SNAPE DEFENDS ### (Snape -0 HP)
label snape_defends:
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=690, y=250,z=5)
    $ duel_OBJ.show("snape_defend",x=690, y=250,z=4)
    $ duel_OBJ.snape = "block"

    pause 2.3
    show screen minus_0

    $ duel_OBJ.hide("snape_defend")
    $ duel_OBJ.snape = ""
    $ duel_OBJ.genie = "barb"
    pause 1

    $ duel_OBJ.show("smoke",x=690, y=250,z=5)
    $ duel_OBJ.genie = ""
    pause 1

    hide screen minus_0

    jump snapes_turn

### GENIE ATTACK ### (Snape -100 HP)
label genie_attack:
    $ renpy.play('sounds/magic4.ogg')
    $ duel_OBJ.show("smoke",x=690,y=250,z=5)
    $ duel_OBJ.show("genie_attack",x=690,y=250,z=4)
    $ duel_OBJ.genie = "attack"
    pause 1
    $ renpy.play('sounds/attack_axe.mp3')
    pause 1.8

    if pentogram:
        if game_difficulty <= 2: #Easy
            hide screen minus_500
            show screen minus_500
            $ snape_hp -= 500
        elif game_difficulty == 2: #Normal
            hide screen minus_500
            show screen minus_500
            $ snape_hp -= 500
        else: #Hardcore
            hide screen minus_500
            show screen minus_500
            $ snape_hp -= 500
    else:
        if game_difficulty <= 2: #Easy
            hide screen minus_300
            show screen minus_300
            $ snape_hp -= 300
        elif game_difficulty == 2: #Normal
            hide screen minus_100
            show screen minus_100
            $ snape_hp -= 100
        else: #Hardcore
            hide screen minus_100
            show screen minus_100
            $ snape_hp -= 100

    pause 1
    if snape_hp < 50: #Check for gameover
        jump snape_lost

    $ duel_OBJ.show("smoke",x=690, y=250,z=5)
    $ duel_OBJ.hide("genie_attack")
    $ duel_OBJ.genie = ""
    pause 1

    hide screen minus_300
    hide screen minus_100

    jump snapes_turn


### SNAPE'S TURN ###
label snapes_turn:
    if pentogram:
        $ pentogram = False
        $ duel_OBJ.snape = "hand"
        $ duel_OBJ.show("hand",x=690, y=250,z=4)
        $ renpy.play('sounds/attack_snape3.ogg')
        pause 1.5
        hide hand
        hide ch_gen
        $ renpy.play('sounds/attack_snape4.ogg')

        if blocking: # GENIE BLOCKS AGAINST THE HAND.(Genie -50 HP)
            $ blocking = False
            $ duel_OBJ.hide("hand")
            $ duel_OBJ.genie = "hand"
            $ duel_OBJ.show("hand_guard",x=690, y=250,z=4)
            pause 1.8
            $ duel_OBJ.hide("hand_guard")
            $ duel_OBJ.snape = ""

            if game_difficulty <= 2: #Easy
                hide screen minus_0_genie
                show screen minus_0_genie
            elif game_difficulty == 2: #Normal
                hide screen minus_50_genie
                show screen minus_50_genie
                $ genie_hp -= 50
            else: #Hardcore #Shouldn't increase the penalty if you blocked correctly...
                hide screen minus_50_genie
                show screen minus_50_genie
                $ genie_hp -= 50

            if genie_hp < 50: #Check for gameover
                jump genie_lost

            $ duel_OBJ.show("smoke",x=690, y=250,z=5)
            $ duel_OBJ.genie = ""
            hide screen minus_50_genie
            jump duel_main


        else: # GENIE DOESN'T BLOCK AGAINST THE HAND. (Genie -400 HP)
            $ duel_OBJ.hide("hand")
            $ duel_OBJ.genie = "hand"
            $ duel_OBJ.show("hand_genie")
            pause 1.3
            $ duel_OBJ.hide("hand_genie")
            $ duel_OBJ.snape = ""

            if game_difficulty <= 2: #Easy
                hide screen minus_300_genie
                show screen minus_300_genie
                $ genie_hp -= 300
            elif game_difficulty == 2: #Normal
                hide screen minus_400_genie
                show screen minus_400_genie
                $ genie_hp -= 400
            else: #Hardcore
                hide screen minus_500_genie
                show screen minus_500_genie
                $ genie_hp -= 500

            if genie_hp < 50: #Check for gameover
                jump genie_lost

            $ duel_OBJ.genie = ""
            hide screen minus_400_genie
            jump duel_main


    else:
        if snape_blocking:
            $ snape_blocking = False
            if blocking:
                $ blocking = False
                jump snape_attack_guard
            else:
                jump snape_attack

        $ snape_decides = renpy.random.randint(1, 2)

        if snape_decides in [1]: #BLOCK
            $ snape_blocking = True
            $ duel_OBJ.snape = "defend"
            pause 1
            jump duel_main

        elif snape_decides in [2]:  #MAGIC. CASTS THE PICTOGRAM.
            $ duel_OBJ.snape = "hand"
            show image "images/dueling/snape/snape_casting_01.png" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
            $ duel_OBJ.show("snape_summon",690,250,4)
            $ renpy.play('sounds/attack_snape2.ogg')
            pause.8
            $ pentogram = True
            pause 1
            $ duel_OBJ.hide("snape_summon")
            $ duel_OBJ.snape = ""

            jump duel_main


### GENIE DRINKS POTION ### (-300 HP)
label potion:
    pause.5
    $ duel_OBJ.show("heal_02",500,330,4)
    $ renpy.play('sounds/attack_heal.ogg')
    pause 1

    show screen plus_300
    pause 1
    $ potions -= 1
    $ genie_hp += 300
    pause.5

    $ duel_OBJ.hide("heal_02")
    hide screen plus_300

    jump snapes_turn



### SNAPE ATTACK ### (Genie -100 HP)
label snape_attack:
    $ duel_OBJ.show("snape_attack",x=690, y=250,z=5)
    $ duel_OBJ.snape = "attack"
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.45
    $ duel_OBJ.hide("snape_attack")
    $ duel_OBJ.snape = ""


    if game_difficulty <= 2: #Easy
        hide screen minus_100_genie
        show screen minus_100_genie
        $ genie_hp -= 100
    elif game_difficulty == 2: #Normal
        hide screen minus_100_genie
        show screen minus_100_genie
        $ genie_hp -= 100
    else: #Hardcore
        hide screen minus_300_genie
        show screen minus_300_genie
        $ genie_hp -= 300

    if genie_hp < 50: #Check for gameover
        jump genie_lost

    jump duel_main

### SNAPE ATTACKS GUARD ### (-0 HP)
label snape_attack_guard:
    $ duel_OBJ.show("snape_attack_guard",x=690, y=250,z=5)
    $ duel_OBJ.snape = "attack"
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.5
    show screen minus_0_genie
    $ duel_OBJ.hide("snape_attack_guard")
    $ duel_OBJ.snape = ""
    pause 1
    hide screen minus_0_genie
    jump duel_main



### DUEL ###
screen duel():
    zorder 2

    use chair_left
    use chair_right
    add "duel_table" at Position(xpos=325, ypos=330, xanchor="center", yanchor="center")

    if pentogram:
        add "pentogram" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")

    if duel_OBJ.genie in ["attack"] or duel_OBJ.snape in ["attack","block"]:
        pass
    else:
        if duel_OBJ.genie == "hand":
            pass
        elif duel_OBJ.genie == "no_magic":
            add "genie_no_magic" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.genie == "defend":
            add "ch_gen guard" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.genie == "barb":
            add "ch_gen barb" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
        else:
            add "ch_gen duel_01" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")

        if duel_OBJ.snape == "hand":
            pass
        elif duel_OBJ.snape == "lost":
            add "snape_lost" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
        elif duel_OBJ.snape == "defend":
            add "ch_sna defend" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
        else:
            add "ch_sna duel_01" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")


screen hp_bar():
    zorder 3

    ### health bar is 271 px wide ###
    add "images/dueling/snape/hp_bar_02.png" xpos int((genie_hp-genie_max_hp)/(genie_max_hp/271.0)) ypos 0
    add "images/dueling/snape/hp_bar.png" #Genie avatr pic.

    ### health bar is 727 px wide ###
    add "images/dueling/snape/hp_bar_11.png" #Black background for HP bar.
    add "images/dueling/snape/hp_bar_12.png" xpos int((snape_max_hp-snape_hp)/(snape_max_hp/727.0)) ypos 0
    add "images/dueling/snape/hp_bar_10.png" #Snape avatr pic.

    add "images/dueling/snape/hp_bar_05.png" xpos 140 ypos 0 #Inactive buttons.



### SNAPE LOSES ###
label snape_lost:
    $ pentogram = False
    $ duel_OBJ.show("smoke",x=690, y=250,z=5)
    $ duel_OBJ.hide("genie_attack")
    $ duel_OBJ.genie = ""
    $ duel_OBJ.snape = "lost"
    $ duel_OBJ.in_progress = False
    hide screen hp_bar
    with flashbulb
    pause 1
    $ snape_intro.duel_complete = True
    jump snape_intro_E4


### GENIE LOSES ###
label genie_lost:
    play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1

    hide screen duel
    hide screen hp_bar
    $ cg_image = "images/dueling/snape/game_over.jpg"
    show screen cg
    with flashbulb
    with hpunch
    call ctc
    menu:
        "-Try again-":
            stop music
            $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
            hide screen cg
            if rum_times == 1:
                $ potions = 1
            elif rum_times == 2:
                $ potions = 2
            elif rum_times == 3:
                $ potions = 3

            jump duel

        "-Give up-":
            pass
    $ MainMenu(confirm=False)

### DUEL IMAGES ###
init -1:
    ### BROKEN GLASS ###
    image glass: # Animation that shows a broken glass effect when the duel starts.
        "images/dueling/snape/01.png"
        pause 1.3
        "images/dueling/snape/02.png"
        pause.3
        "images/dueling/snape/03.png"
        pause.3
        "images/dueling/snape/04.png"
        pause.3
        "images/dueling/snape/05.png"
        pause.3
        "images/dueling/snape/06.png"
        pause.3
        "images/dueling/snape/07.png"

    ### Harry Potter DUEL ANIMATIONS ###
    image smoke:
        "images/animation/smoke_01.png"
        pause.1
        "images/animation/smoke_02.png"
        pause.1
        "images/animation/smoke_03.png"
        pause.1
        "images/animation/smoke_04.png"
        pause.1

    image duel_table:
        "images/rooms/main_room/desk_with_shadow.png"

    ### GENIE ###
    image ch_gen duel_01:
        "images/dueling/snape/gen_01.png"
        pause.1
        "images/dueling/snape/gen_02.png"
        pause.1
        "images/dueling/snape/gen_03.png"
        pause.1
        "images/dueling/snape/gen_02.png"
        pause.1
        repeat

    image ch_gen guard:
        "images/dueling/snape/guard_01.png"
        pause.1
        "images/dueling/snape/guard_02.png"
        pause.1
        "images/dueling/snape/guard_03.png"
        pause.1
        "images/dueling/snape/guard_02.png"
        pause.1
        repeat

    image ch_gen barb:
        "images/dueling/snape/barb_01.png"
        pause.15
        "images/dueling/snape/barb_02.png"
        pause.15
        repeat

    image genie_attack:
        "images/dueling/snape/genie_attack_01.png"
        pause.15
        "images/dueling/snape/genie_attack_02.png"
        pause.15
        "images/dueling/snape/genie_attack_01.png"
        pause.15
        "images/dueling/snape/genie_attack_02.png"
        pause.15
        "images/dueling/snape/genie_attack_01.png"
        pause.15
        "images/dueling/snape/genie_attack_02.png"
        pause.15
        "images/dueling/snape/genie_attack_03.png"
        pause.15
        "images/dueling/snape/genie_attack_04.png"
        pause.15
        "images/dueling/snape/genie_attack_05.png"
        pause.15
        "images/dueling/snape/genie_attack_06.png"
        pause.15
        "images/dueling/snape/genie_attack_07.png"
        pause.15
        "images/dueling/snape/genie_attack_08.png"
        pause.15
        "images/dueling/snape/genie_attack_09.png"
        pause.15
        "images/dueling/snape/genie_attack_10.png"
        pause.15
        "images/dueling/snape/genie_attack_11.png"
        pause.15
        "images/dueling/snape/genie_attack_12.png"
        pause.15
        "images/dueling/snape/genie_attack_13.png"
        pause.15
        "images/dueling/snape/genie_attack_14.png"
        pause.15
        "images/dueling/snape/genie_attack_15.png"
        pause.15
        "images/dueling/snape/genie_attack_14.png"
        pause.15
        "images/dueling/snape/genie_attack_15.png"
        pause.15
        repeat

    image genie_no_magic:
        "images/dueling/snape/no_magic.png"


    ### SNAPE ###
    image ch_sna duel_01:
        "images/dueling/snape/snape_01.png"
        pause.1
        "images/dueling/snape/snape_02.png"
        pause.1
        "images/dueling/snape/snape_03.png"
        pause.1
        "images/dueling/snape/snape_02.png"
        pause.1
        repeat

    image ch_sna defend:
        "images/dueling/snape/snape_defend_01.png"
        pause.1
        "images/dueling/snape/snape_defend_02.png"
        pause.1
        "images/dueling/snape/snape_defend_03.png"
        pause.1
        "images/dueling/snape/snape_defend_02.png"
        pause.1
        repeat

    image snape_attack:
        "images/dueling/snape/sna_attack_01.png"
        pause.08
        "images/dueling/snape/sna_attack_02.png"
        pause.08
        "images/dueling/snape/sna_attack_03.png"
        pause.08
        "images/dueling/snape/sna_attack_04.png"
        pause.08
        "images/dueling/snape/sna_attack_05.png"
        pause.08
        "images/dueling/snape/sna_attack_06.png"
        pause.08
        "images/dueling/snape/sna_attack_07.png"
        pause.08
        "images/dueling/snape/sna_attack_08.png"
        pause.08
        "images/dueling/snape/sna_attack_09.png"
        pause.08
        "images/dueling/snape/sna_attack_10.png"
        pause.08
        repeat

    image snape_defend: #Snape is in defense stance. Barbarian throws axes at him.
        "images/dueling/snape/sna_block_01.png"
        pause.15
        "images/dueling/snape/sna_block_02.png"
        pause.15
        "images/dueling/snape/sna_block_01.png"
        pause.15
        "images/dueling/snape/sna_block_02.png"
        pause.15
        "images/dueling/snape/sna_block_01.png"
        pause.15
        "images/dueling/snape/sna_block_02.png"
        pause.15
        "images/dueling/snape/sna_block_03.png"
        pause.15
        "images/dueling/snape/sna_block_04.png"
        pause.15
        "images/dueling/snape/sna_block_05.png"
        pause.15
        "images/dueling/snape/sna_block_06.png"
        pause.15
        "images/dueling/snape/sna_block_07.png"
        pause.15
        "images/dueling/snape/sna_block_08.png"
        pause.15
        "images/dueling/snape/sna_block_09.png"
        pause.15
        "images/dueling/snape/sna_block_10.png"
        pause.15
        "images/dueling/snape/sna_block_11.png"
        pause.15
        "images/dueling/snape/sna_block_12.png"
        pause.15
        "images/dueling/snape/sna_block_13.png"
        pause.15
        repeat

    image snape_summon:
        "images/dueling/snape/snape_casting_01.png"

    image snape_lost:
        "images/dueling/snape/snape.png"

    image snape_attack_guard: # CREDITS VERSION, with a longer pause.
        "images/dueling/snape/sna_attack_guard_01.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_02.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_03.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_04.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_05.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_06.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_07.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_08.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_09.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_10.png"
        pause.5
        repeat

    image snape_attack_guard:
        "images/dueling/snape/sna_attack_guard_01.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_02.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_03.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_04.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_05.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_06.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_07.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_08.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_09.png"
        pause.08
        "images/dueling/snape/sna_attack_guard_10.png"
        pause.08
        repeat


    ### HAND ###
    image pentogram:
        "images/dueling/snape/pen_05.png"
        pause.1
        "images/dueling/snape/pen_04.png"
        pause.1
        "images/dueling/snape/pen_03.png"
        pause.1
        "images/dueling/snape/pen_02.png"
        pause.1
        "images/dueling/snape/pen_01.png"
        pause.1
        "images/dueling/snape/pen_02.png"
        pause.1
        "images/dueling/snape/pen_03.png"
        pause.1
        "images/dueling/snape/pen_04.png"
        pause.1
        "images/dueling/snape/pen_05.png"
        pause.1
        repeat

    image hand: #Hand appears.
        "images/dueling/snape/hand_01.png"
        pause.1
        "images/dueling/snape/hand_02.png"
        pause.1
        "images/dueling/snape/hand_03.png"
        pause.1
        "images/dueling/snape/hand_04.png"
        pause.1
        "images/dueling/snape/hand_05.png"
        pause.1
        "images/dueling/snape/hand_06.png"
        pause.1
        "images/dueling/snape/hand_07.png"
        pause.1
        "images/dueling/snape/hand_08.png"
        pause.1
        "images/dueling/snape/hand_09.png"
        pause.1
        "images/dueling/snape/hand_10.png"
        pause.1
        "images/dueling/snape/hand_11.png"
        pause.1
        "images/dueling/snape/hand_12.png"
        pause.1
        "images/dueling/snape/hand_13.png"
        pause.1
        "images/dueling/snape/hand_14.png"
        pause.1
        "images/dueling/snape/hand_15.png"
        pause.1
        "images/dueling/snape/hand_16.png"
        pause.1
        repeat

    image hand_genie: #Hand attacks Genie.
        "images/dueling/snape/hand_genie_01.png"
        pause.1
        "images/dueling/snape/hand_genie_02.png"
        pause.1
        "images/dueling/snape/hand_genie_03.png"
        pause.1
        "images/dueling/snape/hand_genie_04.png"
        pause.1
        "images/dueling/snape/hand_genie_05.png"
        pause.1
        "images/dueling/snape/hand_genie_06.png"
        pause.1
        "images/dueling/snape/hand_genie_07.png"
        pause.1
        "images/dueling/snape/hand_genie_08.png"
        pause.1
        "images/dueling/snape/hand_genie_09.png"
        pause.1
        "images/dueling/snape/hand_genie_10.png"
        pause.1
        "images/dueling/snape/hand_genie_11.png"
        pause.1
        "images/dueling/snape/hand_genie_12.png"
        pause.1
        "images/dueling/snape/hand_genie_13.png"
        pause.1

    image hand_guard: #Hand attacks the guard.
        "images/dueling/snape/hand_guard_01.png"
        pause.1
        "images/dueling/snape/hand_guard_02.png"
        pause.1
        "images/dueling/snape/hand_guard_03.png"
        pause.1
        "images/dueling/snape/hand_guard_04.png"
        pause.1
        "images/dueling/snape/hand_guard_05.png"
        pause.1
        "images/dueling/snape/hand_guard_06.png"
        pause.1
        "images/dueling/snape/hand_guard_07.png"
        pause.1
        "images/dueling/snape/hand_guard_08.png"
        pause.1
        "images/dueling/snape/hand_guard_09.png"
        pause.1
        "images/dueling/snape/hand_guard_10.png"
        pause.1
        "images/dueling/snape/hand_guard_11.png"
        pause.1
        "images/dueling/snape/hand_guard_12.png"
        pause.1
        "images/dueling/snape/hand_guard_13.png"
        pause.1
        "images/dueling/snape/hand_guard_14.png"
        pause.1
        "images/dueling/snape/hand_guard_11.png"
        pause.1
        "images/dueling/snape/hand_guard_12.png"
        pause.1
        "images/dueling/snape/hand_guard_13.png"
        pause.1


    ### DAMAGE ###
    image plus_300:
        "images/dueling/damage/plus_300_01.png"
        pause.2
        "images/dueling/damage/plus_300_02.png"
        pause.2
        "images/dueling/damage/plus_300_03.png"
        pause.2
        "images/dueling/damage/plus_300_04.png"
        pause.2
        "images/dueling/damage/plus_300_05.png"
        pause.2
        "images/dueling/damage/plus_300_06.png"
        pause.2
        "images/dueling/damage/plus_300_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_0: #Hand attacks the guard.
        "images/dueling/damage/0_01.png"
        pause.2
        "images/dueling/damage/0_02.png"
        pause.2
        "images/dueling/damage/0_03.png"
        pause.2
        "images/dueling/damage/0_04.png"
        pause.2
        "images/dueling/damage/0_05.png"
        pause.2
        "images/dueling/damage/0_06.png"
        pause.2
        "images/dueling/damage/0_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_50:
        "images/dueling/damage/50_01.png"
        pause.2
        "images/dueling/damage/50_02.png"
        pause.2
        "images/dueling/damage/50_03.png"
        pause.2
        "images/dueling/damage/50_04.png"
        pause.2
        "images/dueling/damage/50_05.png"
        pause.2
        "images/dueling/damage/50_06.png"
        pause.2
        "images/dueling/damage/50_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_100: #Hand attacks the guard.
        "images/dueling/damage/100_01.png"
        pause.2
        "images/dueling/damage/100_02.png"
        pause.2
        "images/dueling/damage/100_03.png"
        pause.2
        "images/dueling/damage/100_04.png"
        pause.2
        "images/dueling/damage/100_05.png"
        pause.2
        "images/dueling/damage/100_06.png"
        pause.2
        "images/dueling/damage/100_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_300:
        "images/dueling/damage/300_01.png"
        pause.2
        "images/dueling/damage/300_02.png"
        pause.2
        "images/dueling/damage/300_03.png"
        pause.2
        "images/dueling/damage/300_04.png"
        pause.2
        "images/dueling/damage/300_05.png"
        pause.2
        "images/dueling/damage/300_06.png"
        pause.2
        "images/dueling/damage/300_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_400: #Hand attacks the guard.
        "images/dueling/damage/400_01.png"
        pause.2
        "images/dueling/damage/400_02.png"
        pause.2
        "images/dueling/damage/400_03.png"
        pause.2
        "images/dueling/damage/400_04.png"
        pause.2
        "images/dueling/damage/400_05.png"
        pause.2
        "images/dueling/damage/400_06.png"
        pause.2
        "images/dueling/damage/400_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2

    image minus_500: #Hand attacks the guard.
        "images/dueling/damage/500_01.png"
        pause.2
        "images/dueling/damage/500_02.png"
        pause.2
        "images/dueling/damage/500_03.png"
        pause.2
        "images/dueling/damage/500_04.png"
        pause.2
        "images/dueling/damage/500_05.png"
        pause.2
        "images/dueling/damage/500_06.png"
        pause.2
        "images/dueling/damage/500_07.png"
        pause.2
        "images/dueling/damage/00.png"
        pause.2


screen snape_glass():
    # add "interface/blackfade.png"
    add "glass" at Position(xpos=0,ypos=0)
    zorder 2
