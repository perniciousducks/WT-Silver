
screen room_back:
    if daytime:
        add "interface/map/room_bg1.png"
    else:
        add "interface/map/room_bg2.png"
    zorder 0

screen shop_screen:
    tag room_screen

    zorder hermione_main_zorder-1

    if daytime:
        add "interface/map/room_bg1.png" at Position(xpos=140)
    else:
        add "interface/map/room_bg2.png" at Position(xpos=140)

    imagemap:
        ground "interface/map/shop_ground.png"
        hover "interface/map/shop_hover.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        hotspot (0, 0, 266, 110) clicked Jump("sscrolls") #Scrolls 1
        hotspot (0, 124, 268, 88) clicked Jump("sscrolls2") #Scrolls 2
        hotspot (0, 215, 233, 80) clicked Jump("shop_books") #Books
        hotspot (70, 340, 85, 75) clicked Jump("gifts_menu") #Gift Box
        hotspot (0, 455, 230, 128) clicked Jump("tentacle_shop_scene") #Tentacle Scroll
        hotspot (606+280, 0, 197, 538) clicked Jump("shop_potion_menu") #Potions
        hotspot (750+280, 550, 40, 40) clicked [Show("main_room_menu"),Jump("day_main_menu")] #Return Button

screen cg:
    add cg_image

screen ccg:
    add "images/28_cg/"+ccg_folder+"/base.png"
    add "images/28_cg/"+ccg_folder+"/"+str(ccg1)+".png"
    add "images/28_cg/"+ccg_folder+"/"+str(ccg2)+".png"
    add "images/28_cg/"+ccg_folder+"/"+str(ccg3)+".png"
    zorder 4

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    zorder 3

screen animation_feather: #Falling feather animation
    add "feather" xpos 360+140 ypos 140
    zorder 2

screen notes: #A bunch of notes poping out with a "win" sound effect.
    add "notes" xpos 320+140 ypos 330
    zorder 1

#################################################################
#########JJ  Flower production/dismissal  #######################
screen H_Flowers_in:  #  Hermione waves her wand and produces flowers
    add "flower_appear" xpos 198+140 ypos 233
    zorder 1

screen H_Flowers_out:  #  Hermione waves her wand and flowers vanish
    add "vanish_effect_flower" xpos 198+140 ypos 235
    zorder 5

screen G_Flowers_in:  #  Genie produces flowers
    add "bouquet_appear" xpos 198+140 ypos 235
    zorder 1

screen G_Flowers_out:  #  Genie flowers vanish
    add "vanish_effect_bouquet" xpos 198+140 ypos 235
    zorder 5


screen fireplace_glow:
    add "glow_effect" xpos 680 ypos 300 zoom 0.4 alpha 0.15
    zorder 10

screen candlefire:
    add "candle_fire_01" xpos 240 ypos 43
    add "candle_fire_02" xpos 723 ypos 108
    zorder 1


screen phoenix_food: #Phoenix's food.
    add "images/main_room/06_phoenix_food.png" xpos 350+140 ypos 49
    zorder 2

screen fireplace_fire: #FIREPLACE FIRE.
    add "fireplace_fire" xpos 436+140 ypos 141
    zorder 2


$ width_offset = 140

screen fireplace:
    add "images/main_room/fireplace.png" at Position(xpos=693, ypos=277, xanchor="center", yanchor="center")

screen desk: #Genie's desk.
    add "images/main_room/09_table.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")

screen chair_left: #aka chair_02
    add "images/main_room/chair_left.png" at Position(xpos=332, ypos=300, xanchor="center", yanchor="center")
screen chair_right:
    add "images/main_room/chair_right.png" at Position(xpos=793, ypos=300, xanchor="center", yanchor="center")

screen owl: #DEFAULT OWL WITH ENVELOPE IN IT'S MOUTH.
    add "images/main_room/owl_01.png" at Position(xpos=315+140, ypos=270, xanchor="center", yanchor="center")
screen owl_02: #OWL. No Envelope.
    add "images/main_room/owl_05.png" at Position(xpos=315+140, ypos=270, xanchor="center", yanchor="center")
screen package: #PACKAGE.
    add "images/main_room/owl_06.png" at Position(xpos=260+140, ypos=235, xanchor="center", yanchor="center")
screen owl_03: #OWL SITTING ON A PACKAGE.
    add "images/main_room/owl_05.png" at Position(xpos=310+140, ypos=235, xanchor="center", yanchor="center")

screen dumbledore: # DUMBLEDORE AND HIS DESK.
    tag chibi_genie
    add "images/main_room/dum.png" at Position(xpos=230+140, ypos=336, xanchor="center", yanchor="center")

### EMO
screen thought: #Thinking emotion over a chibi.
    tag emo
    add "thought" xpos tt_xpos+140 ypos tt_ypos
    zorder 2




screen universal_walk:
    tag chibi_walk
    add universal_walk_image at universal_chibi_walk(u_walk_x, u_walk_x2, u_walk_speed, u_walk_y)


### MISC SCREENS
screen bld1:
    tag bld
    add "interface/bld.png"
    zorder 3 #4

screen ctc:
    add "ctc4"
    zorder 9

screen points: #House points screen.
    add "interface/points/TopUI_Bar.png" at Position(xpos=0+140, ypos=1)
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 146+140 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его
        text "{size=-5}[slytherin]{/size}" #сумма текстом
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 252+140 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его
        text "{size=-5}[gryffindor]{/size}" #сумма текстом
    hbox:
        spacing 10 xpos 365+140 ypos 11
        text "{size=-5}[hufflepuff]{/size}"
    hbox:
        spacing 10 xpos 37+140 ypos 11
        text "{size=-5}[ravenclaw]{/size}"
    hbox: ### DAYS COUNTER ###
        spacing 10 xpos 475+140 ypos 10
        text "{size=-3}[day]{/size}"
    hbox: ### DGOLD COUNTER ###
        spacing 10 xpos 590+140 ypos 10
        text "{size=-4}[gold]{/size}"
    zorder 2


screen gift:
    zorder 6 #5
    add "interface/frames/"+str(interface_color)+"/reward_background.png"
    add the_gift at Position(xalign=0.5, yalign=0.5)


label give_reward(text="",gift=""):
    show screen blktone5
    with d3

    $ renpy.play('sounds/win2.mp3')
    show screen notes
    with d9
    hide screen notes
    with d3

    if gift!="":
        $ the_gift = gift
    else:
        $ the_gift = "images/store/01.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    if text != "":
        $ quest_reward_text = text

    show screen gift
    with d3

    menu:
        "[quest_reward_text]"
        "-Done Reading-":
            pass

    hide screen gift
    with d1

    hide screen blktone5
    with d3

    $ menu_y = 0.5 #return to default menu align

    return


screen clothing_unlock:
    zorder 6 #5
    add "interface/store/"+str(interface_color)+"/clothing_panel_B.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio

label unlock_clothing(text="",item=""):
    show screen blktone5
    with d3

    $ renpy.play('sounds/win2.mp3')
    show screen notes
    with d9
    hide screen notes
    with d3

    if item !="":
        $ mannequin_preview = item.getStoreImage()
    else:
        $ mannequin_preview = "images/store/01.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    if text != "":
        $ quest_reward_text = text

    show screen clothing_unlock
    with d3

    menu:
        "[quest_reward_text]"
        "-Done Reading-":
            pass

    hide screen clothing_unlock
    with d1

    hide screen blktone5
    with d3

    $ menu_y = 0.5 #return to default menu align

    return


screen letter:
    zorder 4
    add "interface/points/letter.png" at Position(xpos=340, ypos=30)
    hbox:
        spacing 40 xpos 410 ypos 80 xmaximum 250
        text letter_text

screen blkfade:
    zorder 6
    add "interface/blackfade.png"

screen blktone:
    tag blktone
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone5: #For narrator. (label nar) #Don't add tag blktone!
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.8)

screen whitetone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/white.jpg", 0.8)

screen white:
    zorder 3
    add "interface/white.jpg"

screen emo: #Character talking off screen.
    #zorder 3
    add "emo8" at Position(xpos=840, ypos=100, xanchor=0, yanchor=0)

### DUEL ###
screen snape_defends:
    add "ch_sna defend" at Position(xpos=-90+140, ypos=-5)
    zorder 2

### DAMAGE ###

screen minus_0:
    add "minus_0" at Position(xpos=640+140, ypos=120)
screen minus_50:
    add "minus_50" at Position(xpos=640+140, ypos=120)
screen minus_100:
    add "minus_100" at Position(xpos=640+140, ypos=120)

screen minus_300:
    add "minus_300" at Position(xpos=640+140, ypos=120)
screen minus_400:
    add "minus_400" at Position(xpos=640+140, ypos=120)
screen minus_500:
    add "minus_500" at Position(xpos=640+140, ypos=120)


#GENIE HEALTH LOSS
screen minus_0_genie:
    add "minus_0" at Position(xpos=450, ypos=120)
screen minus_50_genie:
    add "minus_50" at Position(xpos=450, ypos=120)
screen minus_100_genie:
    add "minus_100" at Position(xpos=450, ypos=120)

screen minus_300_genie:
    add "minus_300" at Position(xpos=450, ypos=120)
screen minus_400_genie:
    add "minus_400" at Position(xpos=450, ypos=120)
screen minus_500_genie:
    add "minus_500" at Position(xpos=450, ypos=120)

#GENIE HEALTH GAIN
screen plus_300:
    add "plus_300" at Position(xpos=450, ypos=120)



### HANGING WITH SNAPE ###

screen with_snape:
    add "images/main_room/with_snape.png" at Position(xpos=0+140, ypos=0)
    tag hanging_with_snape
    zorder 3
    
screen with_snape_animated:
    add "genie_toast_goblet" at Position(xpos=0+140, ypos=0)
    tag hanging_with_snape
    zorder 3



screen c_scene: #Custom Scenes
    tag gc
    if scene_number == 1:
        add "images/28_cg/scene_01.png" xpos 0+140 ypos 0
    if scene_number == 2:
        add "images/28_cg/scene_02.png" xpos 0+140 ypos 0
    if scene_number == 3:
        add "images/28_cg/scene_03.png" xpos 0+140 ypos 0
    if scene_number == 4:
        add "images/28_cg/scene_04.png" xpos 0+140 ypos 0
    zorder 3





screen ch_hotdog:
    add "ch_hem hotdog" xpos -210+140 ypos 10 #Desk sex ani.
    zorder 0


screen s_head: #Snape. Head.
    tag head
    add s_sprite xpos tt_xpos+140 ypos tt_ypos # x = 330, Right bottom corner: y = 340
    zorder 8

screen s_head2: #Snape. Head.
    tag head
    add s_sprite xpos snape_head_xpos+140 ypos snape_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8














### ENDING UNIVERSAL 01 ###
screen end_u_1:
    tag ending
    add "interface/blackfade.png"
    add end_u_1_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 02 ###
screen end_u_2:
    tag ending
    add "interface/blackfade.png"
    add end_u_2_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 03 ###
screen end_u_3:
    add end_u_3_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 04 ###
screen end_u_4:
    add end_u_4_pic at Position(xpos=140,ypos=0)
    zorder 2




screen credits_chibi: # ONE CHIBI
    zorder 5
    add dermo at Position(xpos=280+140, ypos=140)


screen credits_chibi2: # TWO CHIBIs
    zorder 5
    add dermo at Position(xpos=150+140, ypos=140)

screen uni_cr: # UNIVERSAL CREDITS CHIBI
    zorder 5
    add dermo at Position(xpos=xder+140, ypos=yder)





### LOLA ###

screen l_head: #Screen that shows a full sprite of HERMIONE.
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
screen snape_groping:
    add "images/28_cg/scene_01.png"
    zorder hermione_main_zorder

screen snape_facial:
    add "images/28_cg/scene_03.png"
    zorder hermione_main_zorder

screen snape_sex:
    add "images/28_cg/scene_04.png"
    zorder hermione_main_zorder

screen dual_hand_job:
    add "images/28_cg/scene_02.png"
    zorder hermione_main_zorder

screen blkback:
    zorder 1
    add "interface/blackfade.png"

screen sccg:
    add "interface/blackfade.png"
    add sc_cg_base xpos sccgxpos ypos sccgypos
    add sc_cg_image_1 xpos sccgxpos ypos sccgypos
    add sc_cg_image_2 xpos sccgxpos ypos sccgypos
    add sc_cg_image_3 xpos sccgxpos ypos sccgypos

    zorder hermione_main_zorder



init python:###THANKS TO CLEANZO FOR WRITING THIS CODE
    def changeHermioneMainScreen(   image_name,
                                    hid_char_list=None,
                                    hid_dialog_list=None,
                                    x_pos=370,
                                    y_pos=0,
                                    hide_trans=Dissolve(0.3),
                                    show_trans=Dissolve(0.3),
                                    char_list=None,
                                    dialog_list=None):
        # SCOPE THESE VARIABLES TO GLOBAL SO WE CAN REALLY
        # UPDATE THEM
        global h_xpos
        global h_ypos
        global h_body
        renpy.hide_screen("hermione_main")
        if hide_trans is not None:
            renpy.with_statement(hide_trans)
        #dialog if present
        if hid_char_list is not None:
            if len(hid_char_list) == 1:
                #single character
                for i in range(0,len(hid_dialog_list)):
                    renpy.say(hid_char_list[0],hid_dialog_list[i])
            elif len(hid_char_list) > 1:
                #multiple characters
                for i in range(0,len(hid_char_list)):
                    renpy.say(hid_char_list[i],hid_dialog_list[i])
        h_xpos = x_pos
        h_ypos = y_pos
        if image_name is not None:
            h_body = image_name

        renpy.show_screen("hermione_main")
        if show_trans is not None:
            renpy.with_statement(show_trans)
        #dialog if present
        if char_list is not None:
            if len(char_list) == 1:
                #single character
                for i in range(0,len(dialog_list)):
                    renpy.say(char_list[0],dialog_list[i])
            elif len(char_list) > 1:
                #multiple characters
                for i in range(0,len(char_list)):
                    renpy.say(char_list[i],dialog_list[i])

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

    def ccg(layer1=None, layer2=None, layer3=None):
        global ccg1
        global ccg2
        global ccg3

        if layer1 is not None:
            ccg1 = layer1
        if layer2 is not None:
            ccg2 = layer2
        if layer3 is not None:
            ccg3 = layer3
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
            sc_cg_base = "images/28_cg/sc34/"+str(scene)+"/base_1.png"
        if image1 is not None:
            sc_cg_image_1 = "images/28_cg/sc34/"+str(scene)+"/A_"+str(image1)+".png"
        else:
            sc_cg_image_1 = "00_blank.png"
        if image2 is not None:
            sc_cg_image_2 = "images/28_cg/sc34/"+str(scene)+"/B_"+str(image2)+".png"
        else:
            sc_cg_image_2 = "00_blank.png"
        if image3 is not None:
            sc_cg_image_3 = "images/28_cg/sc34/"+str(scene)+"/C_"+str(image3)+".png"
        else:
            sc_cg_image_3 = "00_blank.png"
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("sccg")
        renpy.with_statement(Dissolve(0.5))
