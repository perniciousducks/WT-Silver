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

            # Outfits
            if outfit_choice == hg_maid_OBJ:
                m "Do you know what a maid is?"
                call her_main("Of course I know...","open","base")
                call her_main("Wait, why would you ask me that?","normal","narrow")
                g9 "I would like you to be my maid."
                if whoring >= 11: #Success
                    call her_main("Your maid? Does that mean I have to wear one of those silly outfits?","open","wink")
                    g9 "Absolutely!"
                    call her_main("...","normal","down")
                    call her_main("Fine...","open","baseL")
                    call her_main("And you expect me to clean up for you too?","open","wink")
                    m "No, actually. Just put on the outfit."
                    call her_main("Alright...","smile","base")
                else: #Fail
                    call her_main("Your maid? [genie_name] isn't it the house elf's job to clean up the rooms?","open","base")
                    call her_main("(Not that I approve of this horrible house-elf enslavement...)","annoyed","angryL")
                    call her_main("I have more important things to attent to. I have no time to clean up behind you...","open","closed")
                    call her_main("Unless... there are some points in it for me...","soft","baseL")
                    m "No points,..."
                    g9 "But I've got this cute outfit for you!"
                    call her_main("No thank you, [genie_name]...","open","closed")
                    call her_main("Outfits don't win house-cups...","soft","angry")
                    m "(Damn her...)"
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            if outfit_choice == hg_pirate_OBJ:
                m "Know anything about pirates [hermione_name]?"
                call her_main( "They pillage and kill people.","open","base")
                m "..."
                m "How do you feel about wearing a pirates outfit?"
                if whoring >= 5: #Success
                    call her_main( "Depends...[genie_name] what kind of pirate are we talking about?","base","base")
                    m "More of the adventurous type for sure."
                    call her_main( "I don't know...","open","base")
                    m "The kind that fights a corrupt government for the good of the people."
                    call her_main( "...","open","down_raised")
                    m "It will feel very empowering I'm sure."
                    m "The female pirates were said to have a very good relationship with their crew."
                    call her_main( "Fine... shipmate [genie_name].","crooked_smile","base")
                else: #Fail
                    call her_main( "Doesn't really sound like my kind of thing to be honest [genie_name].","base","baseL")
                    m "I thought you might be a fan of seamen..."
                    call her_main( "I don't really have anything against seamen...but pirates aren't really the same thing.","open","base")
                    m "Butt pirates?"
                    call her_main( "What?","base","base")
                    call her_main( "It's a bit to revealing... drop it for now okay?","disgust","base")
                    m "Fair enough, I'm sure we'll find something you'd like to wear."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe

            if outfit_choice == hg_japan_OBJ:
                m "Hogwarts isn't the only school with a dress code you know."
                call her_main( "I know that, I'm a muggle born after all.","open","base")
                m "Right, would you put this Japanese schoolgirl outfit on?"
                if whoring >= 8: #Success
                    call her_main( "Cute, where did you even get this? I didn't know you've visited Japan.","base","base")
                    m "It's a replica..."
                    call her_main( "oh...well, the colour is nice.", "grin","base")
                    call her_main( "I guess I could wear it for a bit.", "grin","heppyCl")
                else: #Fail
                    call her_main( "I'd rather not be accused of stirring cultural appropriation.", "annoyed","base")
                    m "Cultural what now?"
                    call her_main( "Never mind.", "annoyed" ,"angryCl")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe

            if outfit_choice == hg_christmas_OBJ:
                m "You better watch out--"
                m "You better not cry--"
                call her_main("Sir?","open","wink")
                g9 "Santa Claus is going to town!"
                if whoring >= 17: #Success
                    call her_main("Oh...","soft","baseL")
                    call her_main("Am I on the naughty list, Mr. Santa?","soft","glance",cheeks="blush")
                    g4 "You are!"
                    call her_main("Does that mean I'm not getting any presents?","base","glance")
                    m "No [hermione_name],..."
                    g9 "Santa is gonna stuff your stockings real good!"
                    m "But first, put on that outfit, would you..."
                    call her_main("Of course.","base","glance")
                else: #Fail
                    call her_main("Don't you mean, is coming to town?","open","wink")
                    g9 "Damn right he's going to cum!"
                    call her_main("You aren't making any sense, [genie_name]!","annoyed","baseL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            if outfit_choice == hg_present_OBJ:
                if whoring >= 20: #Success
                    m "[hermione_name], did you know today is my birthday?"
                    call her_main("Oh really, [genie_name]? Your birthday?","base","glance")
                    g9 "It is!"
                    if not birthday_happened:
                        $ birthday_happened = True
                        call her_main("(I hightly doubt that...)","base","baseL")
                    else:
                        call her_main("(What a poor liar...)","base","baseL")
                    call her_main("Well in that case...","open","glance")
                    call her_main("What does our birthday boy wish for his special day?","open","closed")
                    call her_main("You can have anything you want!","soft","glance")
                    g4 "(Hot damn!)"
                    g9 "How about your body?"
                    call her_main("Hmm... my body?","base","glance")
                    call her_main("... completely naked... wrapped in a tight ribbon for you to unwrap...","open","glanceL")
                    call her_main("... and play with...","open_tongue","glance")
                    call her_main("I bet you would like that, [genie_name]?","base","glance")
                    g9 "Indeed I would!"
                    call her_main("Well then, Happy Birthday, [genie_name].","soft","glance")
                else:
                    m "[hermione_name], did you know it's my birthday today?"
                    if not birthday_happened:
                        $ birthday_happened = True
                        call her_main("It is? But I've read in the daily prophet that your birthday is on the--","open","baseL")
                        m "No no, it's today!"
                        call her_main("Uhm. Ok... Happy bithday then, [genie_name].","soft","base")
                        m "Would you grant me a wish?"
                        call her_main("Of course.","base","base")
                        g9 "Could you dress up as my present?"
                        m "Just put this on."
                        call nar(">You hand her the ribbon.")
                    else:
                        call her_main("Sure, [genie_name]... Just like last time you said that.","open","baseL")
                        m "(Shit, she's right! I've already used that card.)"
                        call her_main("What is it you want, [genie_name]?","clench","annoyed")
                        g9 "Could you dress up as my present?"
                        call her_main("That again... [genie_name], do you happen to have some sort of... unpacking fetish?","open","annoyed")
                        m "I've never had a childhood..."
                        m "Just put this on."
                        call nar(">You hand her the ribbon.")
                    call her_main("I'm supposed to wrap it around me?","open","wink")
                    m "Yes. But first you need to get naked."
                    if whoring < 5:
                        call her_main("What?","shock","wide")
                        call her_main("Are you out of your mind, [genie_name]?","open","angryCl")
                        call her_main("Never ask me something like this again!","angry","angry")
                    else:
                        call her_main("Typical...","open","closed")
                        call her_main("I'm sorry, [genie_name]. But this just sounds like just another one of your silly ideas...","open","annoyed")
                    m "But,... my birthday!"
                    if not birthday_happened:
                        call her_main("Birthday or not, I would never do such a thing! For anyone!","scream","angryCl")
                    else:
                        call her_main("It's not your birthday!","scream","angry")
                        m "Alright, alright... No need to scream like that."
                    call her_main("(What a perv...)","annoyed","angryL")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe

            # Costumes
            if outfit_choice in [hg_powerGirl_OBJ,hg_msMarvel_OBJ]:
                m "Are there any heroines you know of?"
                if whoring >= 11: #Success
                    call her_main("You mean like super-heroines?","open","wink")
                    m "Yep"
                    if outfit_choice == hg_powerGirl_OBJ:
                        m "I've got this Power Girl outfit I would like you to wear..."
                    if outfit_choice == hg_msMarvel_OBJ:
                        m "I have this outfit for you. It's Miss Marvel's!"
                    call nar(">You hand her the outfit.")
                    call her_main("Fine. I'll wear it.","soft","baseL")
                    m "You will?"
                    call her_main("Of course! I like her. She's a great role model for young girls, after all!","open","closed")
                    if outfit_choice == hg_powerGirl_OBJ:
                        call her_main("Although... That cleavage on her is a bit much.","disgust","down")
                        g9 "But that's the best part!"
                        call her_main("Why doesn't that suprise me. That you would think so...","annoyed","angry")
                    call her_main("Just let me put it on...","smile","glance")
                else: #Fail
                    call her_main("Of course!","open","worriedL")
                    call her_main("Rowena Ravenclaw, Helga Hufflepuff, Isolt Sayre, Joan of Arc,...","open","worriedL")
                    call her_main("I can name you hundrets! All witches I admire and look up to!","grin","closed")
                    m "(Who?)"
                    m "No no, I'm talking about Comic-books! Super-heroes!"
                    call her_main("Oh...","soft","narrow")
                    call her_main("[genie_name], how do you even know about such things? Comics?","soft","wink")
                    g9 "I know all about human activities and pleasures!"
                    call her_main("Muggle activities? Well of course, somebody as wise as you would be knowledged about all sorts of things.","open","baseL")
                    call her_main("I myself don't think too highly of comic-books, [genie_name].","soft","narrow")
                    call her_main("Not to mention the contumelious treatment and over-sexualization of female heroines.","soft","narrow")
                    call her_main("It's disgusting...","open","closed")
                    call her_main("I have to refuse, [genie_name]!","annoyed","angry")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe


            if outfit_choice == hg_harleyQuinn_OBJ:
                m "Know anything about Batman?"
                call her_main( "Uh, do you mean like vampires?","soft","narrow")
                m "No, he's a comic book character."
                call her_main( "Comics are usually a bit to unrealistic to me.","base","base")
                m "\"In a world with actual wizards, Batman is too unrealistic?\""
                m "I'd like you to try out this villain outfit."
                if whoring >= 14: #Success
                    call her_main( "I don't know, sell it to me.","base","base")
                    m "Uh, she's a misunderstood girl in love with one of the main characters enemies."
                    call her_main( "I feel miss understood at times too, does she get her love in the end?","base","narrow")
                    m "Well, it's complicated. There's a bunch of different itterations too."
                    call her_main( "Will you stop talking about it if I put it on?","annoyed","worried")
                    m "Yes."
                    call her_main( "Fine." ,"base","base")
                else: #Fail
                    call her_main( "No thanks, it seems a bit too tight for me.", "soft", "worried")
                    m "\"I'll loosen you up soon enough.\""
                    call her_main( "What are you looking at. Is it something I said?","base","narrow")
                    m "Oh, nothing my dear...I was just meditating."
                    call her_main( "\"More like, falling asleep.\"","base","suspicious")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe

            if outfit_choice == hg_tifa_OBJ:
                m "Do you know anything about video games [hermione_name]?"
                call her_main( "I was usually too busy reading to have any time for such things, why?", "soft","narrow")
                m "I'd like you to put this Tifa outfit for me"
                if whoring >= 11: #Success
                    call her_main( "Why do you even know anything about video games professor?" ,"soft","narrow")
                    m "Some people say video games are art miss Granger."
                    call her_main( "And?" ,"soft","narrow")
                    m "And art is important muggle study material."
                    call her_main( "It does look creative." ,"soft","narrow")
                    m "You'd look great in it I'm sure."
                    call her_main( "Okay, thank you." ,"soft","narrow")
                else: #Fail
                    call her_main( "I'd rather just wear my own clothes..." ,"soft","narrow")
                    call her_main( "suspenders has never really been my kind of thing." ,"soft","narrow")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            if outfit_choice == hg_laraCroft_OBJ:
                m "[hermione_name]..."
                m "I'd like you to dress up."
                call her_main("As what?","open","worriedL")
                g9 "As the greatest british female archaeologist who's ever lived!"
                call her_main("Gertrude Bell?","grin","closed")
                m "What?"
                m "No... I'm talking about Lara Croft..."
                if whoring >= 17:
                    call her_main("...","annoyed","down")
                    call her_main("Fine, if I have to.","open","closed")
                    call her_main("Let me go and change.","annoyed","baseL")
                else:
                    call her_main("Uhm... who?","soft","wink")
                    m "She's a video game character."
                    call her_main("What?","scream","wide")
                    call her_main("In that case, absolutely not!","scream","angryCl")
                    m "Why not?"
                    call her_main("Video-games are for idiots.","annoyed","angryL")
                    m "..."
                    m "(No they aren't...)"
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            if outfit_choice == hg_witch_OBJ:
                m "[hermione_name], have you ever heard about witches?"
                call her_main("[genie_name]? I am a witch?","soft","narrow")
                m "Oh right,..."
                m "To my defense, you don't look much like one..."
                call her_main("I don't? How are witches supposed to look?","open","base")
                m "Well, normally they'd wear stuff like witch-hats,... frills,... and capes!"
                call her_main("Capes?","disgust","wink")
                if whoring >= 17: #Success
                    m "Here it is."
                    call nar(">You hand her the outfit.")
                    call her_main("It looks really old-fashioned...","disgust","down")
                    call her_main("And why is there a hole down there?","disgust","narrow")
                    g9 "It's great, isn't it!"
                    call her_main("No it isn't! Do you really expect me to show of my pussy like that, to everyone?","angry","angry")
                    m "Well, only to me..."
                    m "I believe you can cover it up with a spell or something..."
                    call her_main("Oh...","annoyed","down")
                    call her_main("You should have told me that first!","annoyed","annoyed")
                    g9 "Yeah yeah... Now put on the dress, my little witch!"
                    call her_main("Fine... Give me a minute...","smile","baseL")
                else: #Fail
                    call her_main("Capes are silly, [genie_name].","open","closed")
                    call her_main("I have to refuse.","annoyed","base")
                    m "I can respect that opinion."
                    m "(Is she nuts? Capes are awesome...)"
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            if outfit_choice in [hg_bio_OBJ,hg_yenn_OBJ]:
                m "[hermione_name], I have a new outfit for you!"
                call her_main("A new outfit? You mean as a gift?","open","wink")
                m "Yes. It's a character from a video-ga--"
                show screen blktone
                call her_main("...","normal","angry")
                m "I mean... she's a famous, ugh,... witch?"
                hide screen blktone
                call her_main("...","smile","base")
                m "(Phew, that was close...)"
                call nar(">You hand her the outfit.")
                if whoring >= 11: #Success
                    call her_main("It does look nice...","soft","down")
                    if outfit_choice == hg_bio_OBJ:
                        call her_main("(I really like her necklace...)","smile","down")
                    if outfit_choice == hg_yenn_OBJ:
                        call her_main("(I really like her scarf...)","smile","down")
                    call her_main("Let me put it on real quick.","smile","glance")
                else: #Fail
                    call her_main("It's a corset, [genie_name]!","open","wink")
                    m "So what?"
                    call her_main("It's too tight! How am I even supposed to breath in it?","open","closed")
                    m "Breathing is overrated..."
                    call her_main("I have to refuse, [genie_name].","normal","base")
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            # Dresses
            if outfit_choice == hg_heartDancer_OBJ:
                if whoring >= 11: #Success
                    m "Giuchie, Giuchie, ya-ya..."
                    call her_main("Da-Da","soft","glanceL")
                    m "Mocha Chocalata..."
                    call her_main("Ya-Ya","soft","ahegao")
                    g9 "Voulez vous coucher avec moi?"
                    call her_main("............","open_tongue","ahegao")
                    m "Girl?..."
                    call her_main("....................","open_tongue","ahegao_intense")
                    m "(Did she just break?)"
                    m "Snap out of it, [hermione_name]! I need you to put on this outfit here..."
                    call her_main("What just happened?!","open","wide",trans="hpunch")
                    call her_main("Oh right. The outfit! Give me a second!","angry","worriedCl",cheeks="blush")
                else: #Fail
                    m "Giuchie, Giuchie, ya ya..."
                    call her_main("(...?)","normal","wink")
                    m "Mocha Chocalata..."
                    call her_main("(...!)","clench","wide")
                    call her_main("[genie_name], what are you doing?","shock","worriedCl")
                    m "I'm singing... Don't you like that song?"
                    call her_main("No... {size=-10}Please stop.{/size}","disgust","base")
                    m "Fine..."
                    if cheats_active or game_difficulty <= 2:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            if outfit_choice == hg_ballDress_OBJ:
                if not have_no_dress_hap: # Dialogue for before she needs the dress.
                    m "Would you like to wear your new dress?"
                    call her_main("A dress? What would I need a dress for?","open","wink")
                    m "Well I just thought you'd look pretty in one so I--"
                    call her_main("I appreciate your concernes, [genie_name], but I'm not the type of girl who likes to wear dresses.","scream","wide")
                    call her_main("Especially in school. I have to refuse","normal","base")
                    jump return_to_wardrobe
                elif have_no_dress_hap and not her_dress_wearable: # You gift Hermione her dress event. Does not trigger the countdown anymore. Talk to hermione to start the ending now.
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

            call h_outfit_OBJ(outfit_choice)

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else: # No chit-chat
            hide screen hermione_main

            call h_outfit_OBJ(outfit_choice)

            call her_main(xpos="wardrobe")
            call screen wardrobe

    else: # Unequip
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

            call h_outfit_OBJ(None)

            call her_main(xpos="wardrobe")
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            hide screen hermione_main

            call h_outfit_OBJ(None)

            call her_main(xpos="wardrobe")
            call screen wardrobe



### Equip Astoria's Outfit ###
label equip_ast_outfit:
    if (outfit_choice != astoria_outfit_GLBL) or (outfit_choice == astoria_outfit_GLBL and not astoria_wear_outfit):

        call ast_outfit(outfit_choice)

        hide screen wardrobe
        call screen wardrobe

    else: # Unequip

        call ast_outfit(None)

        hide screen wardrobe
        call screen wardrobe



### Equip Susan's Outfit ###
label equip_sus_outfit:
    if (outfit_choice != susan_outfit_GLBL) or (outfit_choice == susan_outfit_GLBL and not susan_wear_outfit):

        call sus_outfit(outfit_choice)

        hide screen wardrobe
        call screen wardrobe

    else: # Unequip

        call sus_outfit(None)

        hide screen wardrobe
        call screen wardrobe
