

### CGs ###

label cg_scene(layer=None, folder=None, trans=None):
    hide screen cg

    if folder != None:
        $ cg_path = "images/CG/"+folder+"/"

    if layer != None:
        $ cg_image = cg_path+layer+".png"

    show screen cg

    #Transitions
    if trans == None:
        with d5 # Default
    else:
        with trans

    return

screen cg(): #Used in tentacle event.
    tag cg_screen

    add cg_image xpos 540 xanchor 0.5 ypos 0 # At Screen Center

    zorder 4

screen ccg():
    tag cg_screen

    add "images/CG/"+ccg_folder+"/base.png"          xpos 540 xanchor 0.5 ypos 0 # At Screen Center
    add "images/CG/"+ccg_folder+"/"+str(ccg1)+".png" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg2)+".png" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg3)+".png" xpos 540 xanchor 0.5 ypos 0
    if loopimage is not None:
        add loopimage

    zorder 4

screen notes(): #A bunch of notes poping out with a "win" sound effect.
    add "notes" xpos 320+140 ypos 330
    zorder 1

#################################################################
#########JJ  Flower production/dismissal  #######################
screen H_Flowers_in():  #  Hermione waves her wand and produces flowers
    add "flower_appear" xpos 198+140 ypos 233
    zorder 1

screen H_Flowers_out():  #  Hermione waves her wand and flowers vanish
    add "vanish_effect_flower" xpos 198+140 ypos 235
    zorder 5

screen G_Flowers_in():  #  Genie produces flowers
    add "bouquet_appear" xpos 198+140 ypos 235
    zorder 1

screen G_Flowers_out():  #  Genie flowers vanish
    add "vanish_effect_bouquet" xpos 198+140 ypos 235
    zorder 5

screen gift():
    zorder 6
    #add "interface/frames/"+str(interface_color)+"/reward_background.png" xalign 0.5 yalign 0.547
    add the_gift align (0.5, 0.4) zoom get_zoom(the_gift, 320,320)

screen clothing_unlock():
    zorder 6
    add "interface/panels/"+str(interface_color)+"/clothing_panel_B.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio

screen emo(): #Character talking off screen.
    #zorder 3
    add "emo8" at Position(xpos=840, ypos=100, xanchor=0, yanchor=0)

### DUEL ###
screen snape_defends(xx=0):
    add "ch_sna defend" at Position(xpos=-90+140+xx, ypos=-5)
    zorder 2

### DAMAGE ###

transform damage_transform:
    alpha 1.0
    linear 1.5 yoffset -100 alpha 0.0

screen duel_damage(value=0, attacking=True):
    tag damage
    frame:
        style "empty"
        at damage_transform
        if attacking:
            xpos 780
            ypos 120
        else:
            xpos 450
            ypos 120
        add "images/dueling/damage/"+str(value)+".png"

screen duel_heal(value=300, player=True):
    tag damage
    frame:
        style "empty"
        at damage_transform
        if not player:
            xpos 780
            ypos 120
        else:
            xpos 450
            ypos 120
        add "images/dueling/damage/plus_"+str(value)+".png"

#GENIE HEALTH GAIN
screen plus_300():
    add "plus_300" at Position(xpos=450, ypos=120)


screen c_scene(): #Snape Classroom Scene
    tag gc
    add "images/CG/scene_01.png" xpos 140 ypos 0
    zorder 4


label teleport(position=None,effect=True,poof_label=None):
    if position == "genie":
        $ teleport_xpos = genie_chibi.pos[0]+75
        $ teleport_ypos = genie_chibi.pos[1]-15
        $ teleport_zorder = 3
    elif position == "hermione":
        $ teleport_xpos = hermione_chibi.pos[0]+45
        $ teleport_ypos = hermione_chibi.pos[1]-80
        $ teleport_zorder = 3
    elif position == "cho":
        $ teleport_xpos = cho_chibi.pos[0]+45
        $ teleport_ypos = cho_chibi.pos[1]-80
        $ teleport_zorder = 3
    elif position == "astoria":
        $ teleport_xpos = astoria_chibi.pos[0]+45
        $ teleport_ypos = astoria_chibi.pos[1]-80
        $ teleport_zorder = 3
    elif position == "desk":
        $ teleport_xpos = 320
        $ teleport_ypos = 160
        $ teleport_zorder = 1
        show screen desk
    else:
        $ teleport_xpos = position[0]
        $ teleport_ypos = position[1]
        $ teleport_zorder = 2

    if effect == True:
        $ renpy.play('sounds/magic4.ogg')
        show screen whitefade
        with d1

        hide screen whitefade
        with d1

        show screen blkfade
        with d1

        hide screen blkfade
        show screen heal_animation
        with d3

    #stop music fadeout 1

    hide screen heal_animation
    if poof_label != None:
        $ renpy.call(poof_label)
    show screen teleport_animation
    with d5

    hide screen teleport_animation
    with d5

    if effect == True:
        pause 1

    return

screen teleport_animation():
    add "teleport_ani" xalign 0.5 xpos teleport_xpos ypos teleport_ypos+60 zoom 0.5
    zorder teleport_zorder

screen heal_animation():
    add "heal_ani" xalign 0.5 xpos teleport_xpos ypos teleport_ypos zoom 0.5
    zorder teleport_zorder


screen credits_chibi(): # ONE CHIBI
    zorder 5
    add dermo at Position(xpos=420, ypos=140)


screen credits_chibi2(): # TWO CHIBIs
    zorder 5
    add dermo at Position(xpos=290, ypos=140)

screen uni_cr(): # UNIVERSAL CREDITS CHIBI
    zorder 5
    add dermo at Position(xpos=xder+140, ypos=yder)





### LOLA ###

screen l_head(): #Screen that shows a full sprite of HERMIONE.
    tag head
    zorder 8
    add lola_body xpos lx+140 ypos ly
    add lola_face xpos lx+140 ypos ly
    if l_blush:
        add "characters/misc/lola/blush.png" xpos lx+140 ypos ly
    if l_things:
        add "characters/misc/lola/things.png" xpos lx+140 ypos ly
    if l_question:
        add "characters/misc/lola/question.png" xpos lx+140 ypos ly
    if l_drop:
        add "characters/misc/lola/drop.png" xpos lx+140 ypos ly
    if l_hearts:
        add "characters/misc/lola/hearts.png" xpos lx+140 ypos ly
    if l_exclamation:
        add "characters/misc/lola/exclamation.png" xpos lx+140 ypos ly
    if l_tears:
        add "characters/misc/lola/tears.png" xpos lx+140 ypos ly



### CGs ###
screen snape_groping():
    add "images/CG/scene_01.png"
    zorder 6

screen snape_facial():
    add "images/CG/scene_03.png"
    zorder 6

screen snape_sex():
    add "images/CG/scene_04.png"
    zorder 6

screen dual_hand_job():
    add "images/CG/scene_02.png"
    zorder 6

screen sccg():
    add "interface/blackfade.png"
    add sc_cg_base xpos sccgxpos ypos sccgypos
    add sc_cg_image_1 xpos sccgxpos ypos sccgypos
    add sc_cg_image_2 xpos sccgxpos ypos sccgypos
    add sc_cg_image_3 xpos sccgxpos ypos sccgypos

    zorder 6

init python:###THANKS TO CLEANZO FOR WRITING THIS CODE

    def cg(image):
        global cg_image
        ###HIDE OLD SCREEN
        renpy.hide_screen("cg")
        #renpy.with_statement(Dissolve(0.5))
        if image is not None:
            cg_image = image
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg")
        renpy.with_statement(Dissolve(0.5))

    def ccg(layer1=None, layer2=None, layer3=None, loop=None):
        global ccg1
        global ccg2
        global ccg3
        global loopimage

        if layer1 is not None:
            ccg1 = layer1
        if layer2 is not None:
            ccg2 = layer2
        if layer3 is not None:
            ccg3 = layer3

        loopimage = loop

        renpy.show_screen("ccg")
        renpy.with_statement(Dissolve(0.5))

    def sc34CG(scene=None, image1=None, image2=None, image3=None):
        global sc_cg_base
        global sc_cg_image_1
        global sc_cg_image_2
        global sc_cg_image_3
        ###HIDE OLD SCREEN
        renpy.hide_screen("sccg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))
        if scene is not None:
            sc_cg_base = "images/CG/sc34/"+str(scene)+"/base_1.png"
        if image1 is not None:
            sc_cg_image_1 = "images/CG/sc34/"+str(scene)+"/A_"+str(image1)+".png"
        else:
            sc_cg_image_1 = "blank.png"
        if image2 is not None:
            sc_cg_image_2 = "images/CG/sc34/"+str(scene)+"/B_"+str(image2)+".png"
        else:
            sc_cg_image_2 = "blank.png"
        if image3 is not None:
            sc_cg_image_3 = "images/CG/sc34/"+str(scene)+"/C_"+str(image3)+".png"
        else:
            sc_cg_image_3 = "blank.png"
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("sccg")
        renpy.with_statement(Dissolve(0.5))