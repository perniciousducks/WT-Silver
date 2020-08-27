
# Miscellaneous CG code

label cg_scene(layer=None, folder=None, trans=d5):
    hide screen cg

    if folder != None:
        $ cg_path = "images/CG/"+folder+"/"

    if layer != None:
        $ cg_image = cg_path+layer+".webp"

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

    add "images/CG/"+ccg_folder+"/base.webp"          xpos 540 xanchor 0.5 ypos 0 # At Screen Center
    add "images/CG/"+ccg_folder+"/"+str(ccg1)+".webp" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg2)+".webp" xpos 540 xanchor 0.5 ypos 0
    add "images/CG/"+ccg_folder+"/"+str(ccg3)+".webp" xpos 540 xanchor 0.5 ypos 0
    if loopimage is not None:
        add loopimage

screen sccg(base, a, b, c):
    # Used by function sc34CG
    zorder 14
    default cgpos = (200, 50)
    add "black"
    add base pos cgpos
    add a pos cgpos
    add b pos cgpos
    add c pos cgpos

# Snape CG
screen snape_groping():
    add "images/CG/scene_01.webp" zoom 0.5
    zorder 14

screen snape_facial():
    add "images/CG/scene_03.webp" zoom 0.5
    zorder 14

screen snape_sex():
    add "images/CG/scene_04.webp" zoom 0.5
    zorder 14

screen dual_hand_job():
    add "images/CG/scene_02.webp" zoom 0.5
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

    def sc34CG(base=None, a=None, b=None, c=None, trans=d5):
        renpy.hide_screen("sccg")
        renpy.hide_screen("blkfade")

        img_base = "images/CG/sc34/{}/base_1.webp".format(base) if base else None
        img_a = "images/CG/sc34/{}/A_{}.webp".format(base, a) if a else None
        img_b = "images/CG/sc34/{}/B_{}.webp".format(base, b) if b else None
        img_c = "images/CG/sc34/{}/C_{}.webp".format(base, c) if c else None

        renpy.show_screen("sccg", img_base, img_a, img_b, img_c)

        if trans:
            renpy.with_statement(trans)

    def dynamic_cg(folder, *args):
        d = tuple("images/CG/{}/{}.webp".format(folder, file) for file in args)

        renpy.show_screen("dynamic_cg", d)
        renpy.with_statement(d5)
        return

screen dynamic_cg(d):
    tag cg_screen
    zorder 14

    for img in d:
        add img
