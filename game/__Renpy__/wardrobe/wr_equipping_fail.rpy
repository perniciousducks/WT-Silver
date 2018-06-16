

label equipping_failed:

    if mad >= 1 and mad <=5:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3

            $ hermione_xpos = 665
            $ wardrobe_active = 0 #activates dissolve in her_main 

            m "[hermione_name]..."
            m "Would you wear this--"
            call her_main("I'm sorry [genie_name],...","open","closed") from _call_her_main_1100
            call her_main("But I don't feel like dressing up for you today.","open","worriedL") from _call_her_main_1101
            m "Any chance I could convince you otherwise?"
            call her_main("Hmm...","annoyed","base") from _call_her_main_1102 #very upset, default
            call her_main("I want 5 house points! And that's no guarantee that I'm actually going to wear...","open","closed") from _call_her_main_1103
            call her_main("Whatever it is you want me to put on.","annoyed","annoyed") from _call_her_main_1104

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "ahe--hem..."
                    m "Five points for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("...","normal","base") from _call_her_main_1105
                    call her_main("Thank you, [genie_name].","soft","baseL") from _call_her_main_1106
                    m "Great, now I forgot what I wanted you to wear..."
                    $ gryffindor += 5
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3") from _call_her_main_1107
                "-Don't give her the points-":
                    m "I don't think so, missy!"
                    call her_main("...","annoyed","frown") from _call_her_main_1108
                    call her_main("Fine!","angry","angry") from _call_her_main_1109
                    call her_main("I don't want them anyway!","annoyed","down") from _call_her_main_1110
                    m "You sure?"
                    call her_main("Tzzz--","angry","angry") from _call_her_main_1111
                    call her_main("","","",xpos="wardrobe",trans="d3") from _call_her_main_1112
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
                    call her_main_rndm_happy from _call_her_main_rndm_happy
                "-Don't bother-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry from _call_her_main_rndm_angry

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") from _call_her_main_1113
        call screen wardrobe
        

    if mad >= 6 and mad <=10:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "I'd like you to wear--"
            call her_main("No, [genie_name]...","open","closed",xpos="base") from _call_her_main_1114 #525=default Hermione xpos
            call her_main("I'm still mad at you for what you did!","open","worriedL") from _call_her_main_1115
            m "Will you wear it if I give Gryffindor some points?"
            call her_main("...","annoyed","suspicious") from _call_her_main_1116
            call her_main("Fifteen house points!","open","base") from _call_her_main_1117
            call her_main("And maybe I will wear it.-- Only maybe!","open","baseL") from _call_her_main_1118

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "Fifteen points..."
                    g4 "for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("(It's so easy to get points out of him!)","soft","baseL") from _call_her_main_1119
                    call her_main("Thank you,[genie_name].","open","closed") from _call_her_main_1120
                    m "No poblem. Now put on... {w=0.9}what was it again?"
                    $ gryffindor += 15
                    $ mad = 0
                    call her_main("","","",xpos="wardrobe",trans="d3") from _call_her_main_1121
                "-Don't give her the points-":
                    m "I'm already giving you new clothing! Isn't that enough?"
                    call her_main("No it's not enough, [genie_name]!","open","closed") from _call_her_main_1122
                    call her_main("I want those points!","angry","angry") from _call_her_main_1123
                    call her_main("(You can shove those clothes up your ass...)","annoyed","angryL") from _call_her_main_1124
                    m "I'm not giving you the points, [hermione_name]."
                    call her_main("Tzzz--","angry","angry") from _call_her_main_1125
                    call her_main("Well then wear your... {w=0.5}-stuff yourself!","scream","angryCl") from _call_her_main_1126
                    m "Wouldn't look good on me..."
                    call her_main("I don't care.","annoyed","annoyed") from _call_her_main_1127
                    call her_main("","","",xpos="wardrobe",trans="d3") from _call_her_main_1128
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
                    call her_main_rndm_happy from _call_her_main_rndm_happy_1
                "-Don't bother-":
                    $ hermione_xpos = 400
                    call her_main_rndm_angry from _call_her_main_rndm_angry_1

        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") from _call_her_main_1129
        call screen wardrobe


    if mad >= 11:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Would you please--"
            call her_main("No--","open","closed",xpos="base") from _call_her_main_1130 #525=default Hermione xpos
            call her_main("...","annoyed","annoyed") from _call_her_main_1131
            m "I just want you to wear--"
            call her_main("I SAID NO, [genie_name]!","scream","angryCl") from _call_her_main_1132
            call her_main("tzzzz...","annoyed","angryL") from _call_her_main_1133
            g4 "Fine! {w=0.9}Forget it."
            call her_main("","","",xpos="wardrobe",trans="d3") from _call_her_main_1134
        else:
            hide screen hermione_main
            with d3
            ">Hermione is really mad at you! There is no point in trying to make her wear it!"
            call her_main_rndm_angry from _call_her_main_rndm_angry_2


        $ wardrobe_active = 1
        call her_main("","","",xpos="wardrobe") from _call_her_main_1135
        call screen wardrobe









