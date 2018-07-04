#useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" \n

### Equip Outfit ###
label equip_outfit:

    #Hermione
    if active_girl == "hermione":
        jump equip_her_outfit
    #Astoria
    if active_girl == "astoria":
        jump equip_ast_outfit
    #Susan
    if active_girl == "susan":
        jump equip_sus_outfit


### Equip Hermione's Outfit ###
label equip_her_outfit:
    if mad >= 1:
        jump equipping_failed

    if (outfit_choice != hermoine_outfit_GLBL) or (outfit_choice == hermoine_outfit_GLBL and not hermione_costume):
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            m "[hermione_name]..."
            m "Could you wear this outfit for me?"

            $ wardrobe_active = 0
            $ hermione_xpos = 665

            call her_main("Of course, [genie_name].","base","base")




            hide screen hermione_main
            with d3
            pause.5

            call h_outfit_OBJ(outfit_choice)

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            hide screen hermione_main
            call h_outfit_OBJ(outfit_choice)

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            call screen wardrobe

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main
            with d3

            $ wardrobe_active = 0 #activates dissolve in her_main
            $ hermione_xpos = 665

            m "[hermione_name], could you take off that outfit again?"

            call her_main("Of course, [genie_name].","base","base")

            hide screen hermione_main
            with d3
            pause.5

            $ hermione_costume = False

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            hide screen hermione_main
            $ hermione_costume = False

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            show screen hermione_main
            call screen wardrobe
