

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
        call transition(trans)

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

screen gui_tooltip(img=None, xx=335, yy=210):
    add img xpos xx ypos yy
    zorder 3

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



screen animation_feather(): #Falling feather animation
    add "feather" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 2

screen phoenix_food(): #Phoenix's food.
    tag phoenix_food
    add "images/rooms/_objects_/phoenix/food.png" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 2


screen fireplace(): #Used to display a fireplace in a different room. Not needed for main room. Included in screen "main_room".
    tag fireplace
    add fireplace_OBJ.get_room_image() xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 1

screen fireplace_fire(): #Used to display fire without the fireplace.
    tag fireplace_fire
    add "fireplace_fire" xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos+25 xanchor 0.5 yanchor 0.5 #xpos 576 ypos 141
    zorder 2

screen fireplace_glow():
    tag fireplace_glow
    add "glow_effect" xpos 680 ypos 300 zoom 0.4 alpha 0.2
    zorder 3

$ width_offset = 140



screen desk(xposistion=360): #Desk only!
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=xposistion, ypos=330, xanchor="center", yanchor="center")
    zorder 2

screen chair_left():
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=332, ypos=300, xanchor="center", yanchor="center")
screen chair_right():
    add "images/rooms/main_room/chair_right.png" at Position(xpos=793, ypos=300, xanchor="center", yanchor="center")
    zorder 1

#Mail
screen owl():
    tag owl

    if letter_queue_list != []: #Owl with letter.
        add owl_OBJ.get_idle_image() xpos owl_OBJ.xpos ypos owl_OBJ.ypos xanchor 0.5 yanchor 1.0
    else:
        add owl_OBJ.get_room_image() xpos owl_OBJ.xpos ypos owl_OBJ.ypos xanchor 0.5 yanchor 1.0

screen package():
    add package_OBJ.get_room_image() xpos package_OBJ.xpos ypos package_OBJ.ypos xanchor 0.5 yanchor 1.0

screen dumbledore(): # DUMBLEDORE AND HIS DESK.
    tag chibi_genie
    add "images/rooms/main_room/dum.png" at Position(xpos=370, ypos=336, xanchor="center", yanchor="center")



screen universal_walk():
    tag chibi_walk
    add universal_walk_image at universal_chibi_walk(u_walk_x, u_walk_x2, u_walk_speed, u_walk_y)


### MISC SCREENS
screen bld1():
    tag bld1
    if not current_room == "quidditch_pitch":
        add "interface/bld.png"
    zorder 3

screen bld2():
    tag bld2
    add im.Flip("interface/bld.png", vertical=True)
    zorder 3

screen ctc():
    add "ctc4"
    zorder 9

screen points(): #House points screen.
    use ui_top_bar

screen gift():
    zorder 6
    #add "interface/frames/"+str(interface_color)+"/reward_background.png" xalign 0.5 yalign 0.547
    add the_gift align (0.5, 0.4) zoom get_zoom(the_gift, 320,320)


label give_reward(text="",gift="", sound=True):

    if sound == True:
        $ renpy.play('sounds/win2.mp3')
        show screen notes
        with d9
        hide screen notes
        with d3

    if gift!="":
        $ the_gift = gift
    else:
        $ the_gift = "interface/icons/box_blue_2.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    $ reward_text = text

    show screen gift
    show screen blktone5
    with d3

    menu:
        "[reward_text]"
        "-Done Reading-":
            pass

    hide screen gift
    hide screen blktone5
    with d3

    call reset_menu_position

    return


screen clothing_unlock():
    zorder 6
    add "interface/panels/"+str(interface_color)+"/clothing_panel_B.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio

label unlock_clothing(text="",item=None):

    $ renpy.play('sounds/win2.mp3')
    show screen notes
    with d9
    hide screen notes
    with d3

    if item != None:
        $ mannequin_preview = item.get_image()
    else:
        $ mannequin_preview = "interface/icons/outfits/mannequin_1.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    show screen clothing_unlock
    show screen blktone5
    with d3

    menu:
        "[text]"
        "-Done Reading-":
            pass

    hide screen clothing_unlock
    hide screen blktone5
    with d3

    $ unlock_clothing_compat(item)

    call reset_menu_position

    return


label item_description(item):

    $ the_gift = item.get_image() #Prints whole imagepath!

    show screen blktone5
    show screen gift
    with d3

    "[item.description]"

    hide screen blktone5
    hide screen gift
    with d3

    return



screen blkfade():
    tag blkfade
    zorder 6
    add "interface/blackfade.png"

screen whitefade():
    tag whitefade
    zorder 6
    add "interface/whitefade.png"

screen blktone():
    tag blktone
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone2():
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.2)

screen blktone5(): #For narrator. (label nar) #Don't add tag blktone!
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone8():
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.8)

screen whitetone8():
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/white.jpg", 0.8)

screen white():
    zorder 5
    add "interface/white.jpg"

screen emo(): #Character talking off screen.
    #zorder 3
    add "emo8" at Position(xpos=840, ypos=100, xanchor=0, yanchor=0)

### DUEL ###
screen snape_defends(xx=0):
    add "ch_sna defend" at Position(xpos=-90+140+xx, ypos=-5)
    zorder 2

### DAMAGE ###

screen minus_0():
    add "minus_0" at Position(xpos=780, ypos=120)
screen minus_50():
    add "minus_50" at Position(xpos=780, ypos=120)
screen minus_100():
    add "minus_100" at Position(xpos=780, ypos=120)

screen minus_300():
    add "minus_300" at Position(xpos=780, ypos=120)
screen minus_400():
    add "minus_400" at Position(xpos=780, ypos=120)
screen minus_500():
    add "minus_500" at Position(xpos=780, ypos=120)


#GENIE HEALTH LOSS
screen minus_0_genie():
    add "minus_0" at Position(xpos=450, ypos=120)
screen minus_50_genie():
    add "minus_50" at Position(xpos=450, ypos=120)
screen minus_100_genie():
    add "minus_100" at Position(xpos=450, ypos=120)

screen minus_300_genie():
    add "minus_300" at Position(xpos=450, ypos=120)
screen minus_400_genie():
    add "minus_400" at Position(xpos=450, ypos=120)
screen minus_500_genie():
    add "minus_500" at Position(xpos=450, ypos=120)

#GENIE HEALTH GAIN
screen plus_300():
    add "plus_300" at Position(xpos=450, ypos=120)



### HANGING WITH SNAPE ###

screen with_snape():
    add "images/rooms/main_room/with_snape.png" at Position(xpos=140, ypos=0)
    tag hanging_with_snape
    zorder 3

screen with_snape_animated():
    add "genie_toast_goblet" at Position(xpos=435, ypos=200)
    add "snape_toast_goblet" at Position(xpos=618, ypos=200)
    tag hanging_with_snape
    zorder 3



screen c_scene(): #Snape Classroom Scene
    tag gc
    add "images/CG/scene_01.png" xpos 140 ypos 0
    zorder 4

screen ch_hotdog():
    add "ch_hem hotdog" xpos -70 ypos 10 #Desk sex ani.
    zorder 0



label teleport(position=None,effect=True,poof_label=None):
    if position == "genie":
        $ teleport_xpos = gen_chibi_xpos+75
        $ teleport_ypos = gen_chibi_ypos-15
        $ teleport_zorder = 3
    elif position == "hermione":
        $ teleport_xpos = her_chibi_xpos+45
        $ teleport_ypos = her_chibi_ypos-80
        $ teleport_zorder = 3
    elif position == "cho":
        $ teleport_xpos = cho_chibi_xpos+45
        $ teleport_ypos = cho_chibi_ypos-80
        $ teleport_zorder = 3
    elif position == "desk":
        $ teleport_xpos = 320
        $ teleport_ypos = 160
        $ teleport_zorder = 1
        show screen desk

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

label get_chibi_position(char=None):

    if char == "genie":
        $ chibi_xpos   = gen_chibi_xpos
        $ chibi_ypos   = gen_chibi_ypos
        $ chibi_zorder = gen_chibi_zorder
    elif char == "snape":
        $ chibi_xpos   = sna_chibi_xpos
        $ chibi_ypos   = sna_chibi_ypos
        $ chibi_zorder = sna_chibi_zorder
    #elif char == "tonks":
    #    $ chibi_xpos   = ton_chibi_xpos
    #    $ chibi_ypos   = ton_chibi_ypos
    #    $ chibi_zorder = ton_chibi_zorder

    elif char == "hermione":
        $ chibi_xpos   = her_chibi_xpos
        $ chibi_ypos   = her_chibi_ypos
        $ chibi_zorder = her_chibi_zorder
    #elif char == "astoria":
    #    $ chibi_xpos   = ast_chibi_xpos
    #    $ chibi_ypos   = ast_chibi_ypos
    #    $ chibi_zorder = ast_chibi_zorder
    elif char == "susan":
        $ chibi_xpos   = sus_chibi_xpos
        $ chibi_ypos   = sus_chibi_ypos
        $ chibi_zorder = sus_chibi_zorder
    elif char == "luna":
        $ chibi_xpos   = lun_chibi_xpos
        $ chibi_ypos   = lun_chibi_ypos
        $ chibi_zorder = lun_chibi_zorder
    elif char == "cho":
        $ chibi_xpos   = cho_chibi_xpos
        $ chibi_ypos   = cho_chibi_ypos
        $ chibi_zorder = cho_chibi_zorder

    return



### Chibi Effects ###

label chibi_effect(action=None, chibi=None):
    call hide_chibi_effects

    if chibi != None:
        call get_chibi_position(chibi)
        if chibi in ["snape","genie"]: # Their chibis have a different size border than the girls'.
            $ chibi_xpos = chibi_xpos +40
            $ chibi_ypos = chibi_ypos -10
        else:
            $ chibi_xpos = chibi_xpos
            $ chibi_ypos = chibi_ypos -50

    if action in [None, "hide"]:
        with d3
        return

    elif action == "thought":
        show screen emo_thought
    elif action in ["!","exclamation"]:
        show screen emo_exclamation
    elif action == "sad":
        show screen emo_sad
    elif action == "hoot":
        show screen emo_hoot

    with d3

    return

screen emo_thought():
    tag emo
    add "thought" xpos chibi_xpos ypos chibi_ypos
    zorder chibi_zorder+1

screen emo_exclamation():
    tag emo
    add "exclaim_01" xpos chibi_xpos ypos chibi_ypos
    zorder chibi_zorder+1

screen emo_sad():
    tag emo
    add "sad_01" xpos chibi_xpos ypos chibi_ypos
    zorder chibi_zorder+1

screen emo_hoot():
    tag emo
    add "hoot" xpos chibi_xpos ypos chibi_ypos
    zorder chibi_zorder+1

label hide_chibi_effects:
    hide screen emo_thought
    hide screen emo_exclamation
    hide screen emo_sad
    hide screen emo_hoot

    return


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
    zorder her_chibi_zorder

screen snape_facial():
    add "images/CG/scene_03.png"
    zorder her_chibi_zorder

screen snape_sex():
    add "images/CG/scene_04.png"
    zorder her_chibi_zorder

screen dual_hand_job():
    add "images/CG/scene_02.png"
    zorder her_chibi_zorder

screen blkback():
    zorder 1
    add "interface/blackfade.png"

screen sccg():
    add "interface/blackfade.png"
    add sc_cg_base xpos sccgxpos ypos sccgypos
    add sc_cg_image_1 xpos sccgxpos ypos sccgypos
    add sc_cg_image_2 xpos sccgxpos ypos sccgypos
    add sc_cg_image_3 xpos sccgxpos ypos sccgypos

    zorder 6

screen luncg():

    add lun_cg_base

    add lun_cg_body         xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_hair         xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_cheeks       xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_mouth        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eyewhite     xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_pupil        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eye          xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eyebrow      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_tears        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    if luna_wear_glasses:
        add lun_cg_eyewear  xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_hairtop      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_1      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_2      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_3      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom

    add lun_cg_overlay      # xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom # Overlay should cover the screen and not move with the CG.
    add lun_cg_dick         xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom
    add lun_cg_genie        xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom

    zorder 6

screen hercg():

    add her_cg_base
    add her_cg_genie        xpos her_cg_xpos_abs ypos her_cg_ypos_abs   xzoom her_cg_zoom


    add her_cg_body         xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_mouth        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eyebrow      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eyewhite     xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_pupil        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eye          xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_cheeks       xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_tears        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_1      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_2      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_3      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom

    add her_cg_overlay      # xpos her_cg_xpos_abs ypos her_cg_ypos_abs   xzoom her_cg_zoom # Overlay should cover the screen and not move with the CG.

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

    def lunCG(mouth=None, eye=None, eyebrow=None, pupil=None, xpos=None, ypos=None, cheeks=None, tears=None, extra_1=None, extra_2=None, extra_3=None, pos=None, overlay=None, body=None):
        global lun_cg_body, lun_cg_overlay, lun_cg_hair, lun_cg_cheeks, lun_cg_mouth, lun_cg_eyewhite, lun_cg_eyewear, lun_cg_pupil, lun_cg_eye, lun_cg_eyebrow, lun_cg_eyewear, lun_cg_tears, lun_cg_hairtop, lun_cg_extra_1, lun_cg_extra_2, lun_cg_extra_3, lun_cg_xpos, lun_cg_ypos, lun_cg_dick

        ###HIDE OLD SCREEN
        renpy.hide_screen("luncg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))

        lun_cg_eyewhite     = lun_cg_path+"eye_white.png"
        lun_cg_eyewear      = lun_cg_path+"glasses.png"
        lun_cg_hair         = lun_cg_path+lun_hair_style+"_hair.png"
        lun_cg_hairtop      = lun_cg_path+lun_hair_style+"_hair_top.png"


        if body:
            lun_cg_body     = lun_cg_path+"body_base.png"
        if cheeks:
            lun_cg_cheeks   = lun_cg_path+"c_"+str(cheeks)+".png"
        if mouth:
            lun_cg_mouth    = lun_cg_path+"m_"+str(mouth)+".png"
        if eye:
            lun_cg_eye      = lun_cg_path+"eye_"+str(eye)+".png"
        if eyebrow:
            lun_cg_eyebrow  = lun_cg_path+"eb_"+str(eyebrow)+".png"
        if pupil:
            lun_cg_pupil    = lun_cg_path+"pup_"+str(pupil)+".png"
        if tears:
            lun_cg_tears    = lun_cg_path+str(tears)+".png"
        if extra_1:
            lun_cg_extra_1  = lun_cg_path+str(extra_1)+".png"
        if extra_2:
            lun_cg_extra_2  = lun_cg_path+str(extra_2)+".png"
        if extra_3:
            lun_cg_extra_3  = lun_cg_path+str(extra_3)+".png"
        if xpos:
            lun_cg_xpos     = xpos
        if ypos:
            lun_cg_ypos     = ypos
        if overlay:
            lun_cg_overlay  = lun_cg_path+str(overlay)+".png"

        if pos != None:
            lun_cg_xpos = lun_loop_xpos[pos]
            lun_cg_ypos = lun_loop_ypos[pos]
            lun_cg_dick = lun_cg_path+"dick_"+str(pos)+".png"




        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luncg")
        renpy.with_statement(Dissolve(0.1))

    def herCG(mouth=None, eye=None, eyebrow=None, pupil=None, xpos=None, ypos=None, cheeks=None, tears=None, extra_1=None, extra_2=None, extra_3=None, pos=None, overlay=None, body=None):
        global her_cg_body, her_cg_overlay, her_cg_hair, her_cg_cheeks, her_cg_mouth, her_cg_eyewhite, her_cg_eyewear, her_cg_pupil, her_cg_eye, her_cg_eyebrow, her_cg_eyewear, her_cg_tears, her_cg_hairtop, her_cg_extra_1, her_cg_extra_2, her_cg_extra_3, her_cg_xpos, her_cg_ypos, her_cg_dick

        ###HIDE OLD SCREEN
        renpy.hide_screen("hercg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))

        her_cg_eyewhite     = her_cg_path+"eye_white.png"

        if body:
            her_cg_body     = her_cg_path+"body_base.png"
        if cheeks:
            her_cg_cheeks   = her_cg_path+"c_"+str(cheeks)+".png"
        if mouth:
            her_cg_mouth    = her_cg_path+"m_"+str(mouth)+".png"
        if eye:
            her_cg_eye      = her_cg_path+"eye_"+str(eye)+".png"
        if eyebrow:
            her_cg_eyebrow  = her_cg_path+"eb_"+str(eyebrow)+".png"
        if pupil:
            her_cg_pupil    = her_cg_path+"pup_"+str(pupil)+".png"
        if tears:
            her_cg_tears    = her_cg_path+str(tears)+".png"
        if extra_1:
            her_cg_extra_1  = her_cg_path+str(extra_1)+".png"
        if extra_2:
            her_cg_extra_2  = her_cg_path+str(extra_2)+".png"
        if extra_3:
            her_cg_extra_3  = her_cg_path+str(extra_3)+".png"
        if xpos:
            her_cg_xpos     = xpos
        if ypos:
            her_cg_ypos     = ypos
        if overlay:
            her_cg_overlay  = her_cg_path+str(overlay)+".png"


        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("hercg")
        renpy.with_statement(Dissolve(0.1))
