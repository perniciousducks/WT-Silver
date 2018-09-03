###SCREEN CODE FOR GENIE
screen genie_sprite:
    add genie_sprite_base xpos genie_sprite_xpos ypos genie_sprite_ypos xzoom genie_sprite_flip zoom (1.0/scaleratio)#Add the base body
    add genie_sprite_exp xpos genie_sprite_xpos ypos genie_sprite_ypos xzoom genie_sprite_flip zoom (1.0/scaleratio)#Add genie expression

    zorder genie_zorder

label gen_main(text="",face=None,body=None):
    if face != None:
        $ genie_sprite_exp = "characters/genie/exp_" + str(face) + ".png"
    if body != None:
        $ genie_sprite_base = "characters/genie/base_" + str(body) + ".png"

    show screen genie_sprite
    if text != "":
        $ renpy.say(msp,text)
    return
