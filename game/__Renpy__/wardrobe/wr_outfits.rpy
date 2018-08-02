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

            $ wardrobe_active = 0
            $ hermione_xpos = 665

            if outfit_choice == hg_laraCroft_OBJ:
                m "[hermione_name]..."
                m "I'd like you to dress up."
                call her_main("As what?","open","worriedL")
                g9 "As who, you should ask."
                m "I want you to dress up as Lara Croft"
                call her_main("Who?","open","wink")
                m "She's a video game character."
                if whoring >= 17:
                    call her_main("...","annoyed","down")
                    call her_main("Whatever, let me just change.","annoyed","base")
                else:
                    call her_main("No. Absolutely not!","scream","angryCl")
                    m "Why not?"
                    call her_main("Video-games are for idiots.","annoyed","angryL")
                    m "..."
                    m "(No they aren't...)"
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            if outfit_choice == hg_ballDress_OBJ:
                if not have_no_dress_hap: # Dialogue for before she needs the dress.
                    m "Would you like to wear your new dress?"
                    call her_main("A dress? What would I need a dress for?","open","wink")
                    m "Well I just thought you'd look pretty in one so I--"
                    call her_main("I appreciate your concernes, [genie_name], but I'm not the type of girl who likes to wear dresses.","scream","wide")
                    call her_main("Especially in school. I have to refuse","normal","base")
                    jump return_to_wardrobe
                elif have_no_dress_hap and not her_dress_wearable: # You gift Hermione her dress event. Does not trigger the countdown anymore.
                    hide screen wardrobe
                    with d3
                    pause.5
                    jump giving_the_dress
                else:
                    m "Remember that dress I gave you?"
                    call her_main("Of course! How could I ever forget!","open","wide")
                    call her_main("Thank you so much, [genie_name]!","grin","happyCl")
                    her "You got me a new ball dress?"
                    m "Indeed I did, but you'll have to earn it."
                    call her_main("Of course!","angry","wide")
                    call her_main("Let me try it on!","base","baseL",cheeks="blush")




            hide screen hermione_main
            with d3
            pause.5

            $ h_request_wear_outfit = True
            call h_outfit_OBJ(outfit_choice)

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            hide screen hermione_main

            $ h_request_wear_outfit = True
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

            $ h_request_wear_outfit = False
            $ hermione_costume = False

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            hide screen hermione_main

            $ h_request_wear_outfit = False
            $ hermione_costume = False

            call update_her_uniform
            call update_her_hair

            call her_main(xpos="wardrobe")
            show screen hermione_main
            call screen wardrobe
