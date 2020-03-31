
# Miscellaneous CG code

label cg_scene(layer=None, folder=None, trans=d5):
    hide screen cg

    if folder != None:
        $ cg_path = "images/CG/"+folder+"/"

    if layer != None:
        $ cg_image = cg_path+layer+".png"

    show screen cg
    with trans
    return

screen cg():
    # Used by label cg_scene
    tag cg_screen
    zorder 14

    add cg_image xpos 540 xanchor 0.5 ypos 0 # At Screen Center

screen ccg():
    # Used by function ccg
    tag cg_screen
    zorder 14

    add "images/CG/"+ccg_folder+"/base.png"          xpos 540 xanchor 0.5 ypos 0 # At Screen Center
    add "images/CG/"+ccg_folder+"/"+str(ccg1)+".png" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg2)+".png" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg3)+".png" xpos 540 xanchor 0.5 ypos 0
    if loopimage is not None:
        add loopimage

screen sccg():
    # Used by function sc34CG
    zorder 14
    add Color("#000")
    add sc_cg_base xpos sccgxpos ypos sccgypos
    add sc_cg_image_1 xpos sccgxpos ypos sccgypos
    add sc_cg_image_2 xpos sccgxpos ypos sccgypos
    add sc_cg_image_3 xpos sccgxpos ypos sccgypos

# Snape CG
screen snape_groping():
    add "images/CG/scene_01.png"
    zorder 14

screen snape_facial():
    add "images/CG/scene_03.png"
    zorder 14

screen snape_sex():
    add "images/CG/scene_04.png"
    zorder 14

screen dual_hand_job():
    add "images/CG/scene_02.png"
    zorder 14

init python:###THANKS TO CLEANZO FOR WRITING THIS CODE

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

    def sc34CG(scene=None, image1=None, image2=None, image3=None, with_trans=True):
        global sc_cg_base
        global sc_cg_image_1
        global sc_cg_image_2
        global sc_cg_image_3
        renpy.hide_screen("sccg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))
        if scene is not None:
            sc_cg_base = "images/CG/sc34/"+str(scene)+"/base_1.png"
        if image1 is not None:
            sc_cg_image_1 = "images/CG/sc34/"+str(scene)+"/A_"+str(image1)+".png"
        else:
            sc_cg_image_1 = "blank"
        if image2 is not None:
            sc_cg_image_2 = "images/CG/sc34/"+str(scene)+"/B_"+str(image2)+".png"
        else:
            sc_cg_image_2 = "blank"
        if image3 is not None:
            sc_cg_image_3 = "images/CG/sc34/"+str(scene)+"/C_"+str(image3)+".png"
        else:
            sc_cg_image_3 = "blank"
        renpy.show_screen("sccg")
        if with_trans:
            renpy.with_statement(Dissolve(0.5))

    def dynamic_cg(folder, *args):
        d = tuple("images/CG/{}/{}.png".format(folder, file) for file in args)

        renpy.show_screen("dynamic_cg", d)
        renpy.with_statement(Dissolve(0.5))
        return

screen dynamic_cg(d):
    tag cg_screen
    zorder 14

    for img in d:
        add img
