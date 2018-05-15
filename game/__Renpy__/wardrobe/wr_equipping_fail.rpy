

label equipping_failed:

    if mad >= 1 and mad <=5:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."
            m "Would you wear this--"
            call her_main("I'm sorry [genie_name],...","open","closed")
            call her_main("But I don't feel like dressing up for you today.","open","worriedL")
            m "Any chance I could convince you otherwise?"
            call her_main("Hmm...","annoyed","base") #very upset, default
            call her_main("I want 5 house points! And that's no guarantee that I'm actually going to wear...","open","closed")
            call her_main("Whatever it is you want me to put on.","annoyed","annoyed")

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "ahe--hem..."
                    m "Five points for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("...","normal","base")
                    call her_main("Thank you, [genie_name].","soft","baseL")
                    m "Great, now I forgot what I wanted you to wear..."
                    $ gryffindor += 5
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3")
                "-Don't give her the points-":
                    m "I don't think so, missy!"
                    call her_main("...","annoyed","frown")
                    call her_main("Fine!","angry","angry")
                    call her_main("I don't want them anyway!","annoyed","down")
                    m "You sure?"
                    call her_main("Tzzz--","angry","angry")
                    call her_main("","","",xpos="wardrobe",trans="d3")
        else:
            hide screen hermione_main
            with d3
            ">Hermione is mad at you! She won't wear it!"
            menu:
                ">You can give Gryffindor points to better her mood."
                "-5 points for Gryffindor!-":
                    $ gryffindor += 5
                    $ mad = 0
                    ">Hermione is no longer mad at you!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy
                "-Don't bother-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe")
        call screen wardrobe
        

    if mad >= 6 and mad <=10:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "I'd like you to wear--"
            call her_main("No, [genie_name]...","open","closed",xpos="base") #525=default Hermione xpos
            call her_main("I'm still mad at you for what you did!","open","worriedL")
            m "Will you wear it if I give Gryffindor some points?"
            call her_main("...","annoyed","suspicious")
            call her_main("Fifteen house points!","open","base")
            call her_main("And maybe I will wear it.-- Only maybe!","open","baseL")

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "Fifteen points..."
                    g4 "for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("(It's so easy to get points out of him!)","soft","baseL")
                    call her_main("Thank you,[genie_name].","open","closed")
                    m "No poblem. Now put on... {w=0.9}what was it again?"
                    $ gryffindor += 15
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3")
                "-Don't give her the points-":
                    m "I'm already giving you new clothing! Isn't that enough?"
                    call her_main("No it's not enough, [genie_name]!","open","closed")
                    call her_main("I want those points!","angry","angry")
                    call her_main("(You can shove those clothes up your ass...)","annoyed","angryL")
                    m "I'm not giving you the points, [hermione_name]."
                    call her_main("Tzzz--","angry","angry")
                    call her_main("Well then wear your... {w=0.5}-stuff yourself!","scream","angryCl")
                    m "Wouldn't look good on me..."
                    call her_main("I don't care.","annoyed","annoyed")
                    call her_main("","","",xpos="wardrobe",trans="d3")
        else:
            hide screen hermione_main
            with d3
            ">Hermione is really mad at you! She won't wear it!"
            menu:
                ">You can give Gryffindor points to better her mood."
                "-15 points for Gryffindor!-":
                    $ gryffindor += 15
                    $ mad = 0
                    ">Hermione is no longer mad at you!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy
                "-Don't bother-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe")
        call screen wardrobe


    if mad >= 11:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Would you please--"
            call her_main("No--","open","closed",xpos="base") #525=default Hermione xpos
            call her_main("...","annoyed","annoyed")
            m "I just want you to wear--"
            call her_main("I SAID NO, [genie_name]!","scream","angryCl")
            call her_main("tzzzz...","annoyed","angryL")
            g4 "Fine! {w=0.9}Forget it."
            call her_main("","","",xpos="wardrobe",trans="d3")
        else:
            hide screen hermione_main
            with d3
            ">Hermione is really mad at you! There is no point in trying to make her wear it!"
            call her_main_rndm_angry


        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe")
        call screen wardrobe









