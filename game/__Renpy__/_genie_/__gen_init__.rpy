
label __init_variables:
    
    
    #Genie
    if not hasattr(renpy.store,'genie_xpos'):
        $ genie_xpos = 60
        $ genie_ypos = 0
        $ genie_zorder = 5

        #$ genie_head_xpos = 60
        #$ genie_head_ypos = 0
        #$ genie_head_zorder = 8

        $ genie_chibi_xpos=500
        $ genie_chibi_ypos=250
        $ genie_speed = 2.0
        $ genie_chibi_zorder = 2
    
    if not hasattr(renpy.store,'secretly_jerking_off'):
        $ secretly_jerking_off = False

    return